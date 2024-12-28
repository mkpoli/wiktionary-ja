from typing import Generator, Mapping, Optional
from ..utils.file import FileCache

from abc import ABC, abstractmethod
from dataclasses import dataclass

import vibrato
import tempfile
import tarfile
import zstandard
from pathlib import Path

dctx = zstandard.ZstdDecompressor()

try:
    import MeCab
except ImportError:
    _has_mecab = False
else:
    _has_mecab = True

try:
    import janome.tokenizer
except ImportError:
    _has_janome = False
else:
    _has_janome = True


def get_model_data(model_path: str) -> bytes:
    # logger.info(f"Downloading model {model_path.split('/')[-1]} ...")
    print("get_model_file", model_path)

    def read_dic_zst(file_path: Path) -> bytes:
        with open(file_path, "rb") as f:
            with dctx.stream_reader(f) as reader:
                return reader.read()

    if model_path.startswith("http"):
        cached_file = file_cache.get_cached_file(model_path)
        print("cached_file", cached_file)

        if model_path.endswith(".tar.xz"):
            with tempfile.TemporaryDirectory() as tmpdir:
                tarfile.open(cached_file, "r:xz").extractall(tmpdir, filter="data")
                print("extracted into", tmpdir)
                for file in Path(tmpdir).glob("**/*.dic.zst"):
                    if file.is_file():
                        return read_dic_zst(file)
                else:
                    raise FileNotFoundError("Cannot find .dic.zst model file")
        elif model_path.endswith(".dic.zst"):
            return read_dic_zst(cached_file)
        else:
            raise ValueError(f"Invalid model path from url: {model_path}")
    elif model_path.endswith(".dic.zst"):
        return read_dic_zst(Path(model_path))
    else:
        raise ValueError("Invalid model path")


# import MeCab


file_cache = FileCache()

# tagger = MeCab.Tagger("-d /usr/local/lib/mecab/dic/ipadic")


@dataclass(frozen=True)
class MecabFeatures:
    pos1: Optional[str] = None
    pos2: Optional[str] = None
    pos3: Optional[str] = None
    pos4: Optional[str] = None
    cType: Optional[str] = None
    cForm: Optional[str] = None
    lForm: Optional[str] = None
    lemma: Optional[str] = None
    orth: Optional[str] = None
    pron: Optional[str] = None
    kana: Optional[str] = None
    goshu: Optional[str] = None
    orthBase: Optional[str] = None
    pronBase: Optional[str] = None
    kanaBase: Optional[str] = None
    formBase: Optional[str] = None
    iType: Optional[str] = None
    iForm: Optional[str] = None
    iConType: Optional[str] = None
    fType: Optional[str] = None
    fForm: Optional[str] = None
    fConType: Optional[str] = None
    aType: Optional[str] = None
    aConType: Optional[str] = None
    aModType: Optional[str] = None


[
    "代名詞",
    "*",
    "*",
    "*",
    "*",
    "*",
    "ワタクシ",
    "私-代名詞",
    "私",
    "ワタクシ",
    "私",
    "ワタクシ",
    "和",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "体",
    "ワタクシ",
    "ワタクシ",
    "ワタクシ",
    "ワタクシ",
    "0",
    "*",
    "*",
    "11345327978324480",
    "41274",
]


@dataclass
class Token:
    surface: str
    lemma: str
    pronunciation: str
    part_of_speech: list[str]
    orthographical_form: str


class Tokenizer(ABC):
    @abstractmethod
    def tokenize(self, text: str) -> list[Token]:
        pass


from typing import TypedDict


class IndexMap(TypedDict):
    part_of_speech: list[int]
    lemma: int
    pronunciation: int
    orthographical_form: int


class VibratoTokenizer(Tokenizer):
    """
    Tokenizer on Vibrato backend.

    * Notes
    You must use a model with at least pronunciation, lemma for this to work
    """

    tokenizer: vibrato.Vibrato
    index_map: IndexMap

    # ['代名詞', '*', '*', '*', '*', '*', 'ワタクシ', '私-代名詞', '私', 'ワタクシ', '私', 'ワタクシ', '和', '*', '*', '*', '*', '*', '*', '体', 'ワ
    def __init__(
        self,
        model_path: str = "https://github.com/daac-tools/vibrato/releases/download/v0.5.0/bccwj-suw+unidic-cwj-3_1_1+compact.tar.xz",
        index_map: IndexMap | None = None,
    ):
        model_data = get_model_data(model_path)
        self.tokenizer = vibrato.Vibrato(model_data)

        if index_map is None:
            index_map = {
                "part_of_speech": [0, 1, 2, 3],  # pos1
                # "lemma_form": 6,
                "lemma": 7,
                # "orthographical": 8,
                "pronunciation": 9,
                "orthographical_form": 10,
            }

        # if "part_of_speech" not in index_map:
        #     raise ValueError("part_of_speech is required")

        # if "lemma" not in index_map:
        #     raise ValueError("lemma is required")

        # if "pronunciation" not in index_map:
        #     raise ValueError("pronunciation is required")

        # if "orthographical_form" not in index_map:
        #     raise ValueError("orthographical_form is required")

        self.index_map = index_map

    def tokenize(self, text: str) -> Generator[Token, None, None]:
        for token in self.tokenizer.tokenize(text):
            features = token.feature().split(",")
            print(features)
            yield Token(
                surface=token.surface(),
                lemma=features[self.index_map["lemma"]],
                pronunciation=features[self.index_map["pronunciation"]],
                part_of_speech=[
                    features[i]
                    for i in self.index_map["part_of_speech"]
                    if features[i] != "*"
                ],
                orthographical_form=features[self.index_map["orthographical_form"]],
            )


class MecabTokenizer(Tokenizer):
    tagger: MeCab.Tagger

    def __init__(self, dict_path: str):
        if not _has_mecab:
            raise ImportError(
                "MeCab is not installed, you need to install with [MeCab] feature, i.e. pip install jawikt[MeCab]"
            )
        self.tagger = MeCab.Tagger(f"-d {dict_path}")
        raise NotImplementedError("MecabTokenizer is not implemented yet")


class JanomeTokenizer(Tokenizer):
    tokenizer: janome.tokenizer.Tokenizer

    def __init__(self):
        if not _has_janome:
            raise ImportError(
                "Janome is not installed, you need to install with [Janome] feature, i.e. pip install jawikt[Janome]"
            )

        self.tokenizer = janome.tokenizer.Tokenizer()
        raise NotImplementedError("JanomeTokenizer is not implemented yet")
