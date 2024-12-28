import vibrato

# import jaconv

import logging

from jawikt.furigana.tokenizer import Tokenizer

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)


class FuriganaAnnotator:
    tokenizer: Tokenizer

    def __init__(
        self,
        tokenizer: Tokenizer,
    ):
        # self.tokenizer = VibratoTokenizer(model_path)
        self.tokenizer = tokenizer
        print([a for a in dir(self.tokenizer) if not a.startswith("_")])

    def annotate(self, text: str):
        return self.tokenizer.tokenize(text)

    # def get_hiragana(text: str) -> str:
    #     return jaconv.kata2hira(text)


# from Language.linguistics.japanese.ruby import extract_ruby_pairs
# from Language.linguistics.japanese.mecab.unidic import parse


# def get_hiragana(text: str) -> str:
#     return jaconv.kata2hira(
#         "".join(
#             node.feature.lemma
#             for node in parse(tagger, text)
#             if node.surface and node.feature.lemma
#         )
#     )


# def add_furigana(text: str):
#     result = []

#     for node in list(parse(tagger, text)):
#         if not node.surface:
#             continue

#         if node.feature.pos1 == "記号":
#             result.append(node.surface)
#             continue

#         if not node.feature.lemma:
#             print("No lemma")
#             print(node)
#             continue

#         if node.surface == node.feature.lemma:  # カタカナ語
#             result.append(node.surface)
#             continue

#         hiragana = jaconv.kata2hira(node.feature.lemma)

#         if node.surface == hiragana:  # ひらがな語
#             result.append(node.surface)
#             continue

#         pairs = extract_ruby_pairs(node.surface, hiragana)

#         # print(node)
#         # if node.feature.pos1 == "動詞" or node.feature.pos1 == "形容詞":
#         #     if not node.feature.lForm:
#         #         print("No lForm")
#         #         continue
#         #     try:
#         #         print(get_hiragana(node.feature.lForm))
#         #     except Exception as e:
#         #         print(e)
#         # def uninflect(node: Node) -> str:
#         #     if node.pos1 == '動詞':
#         #         if hiragana[-1] == "っ"
#         #         return hiragana[:-1] + ("う" if "ワ行" in node.feature.cType else "る")
#         #     if hiragana[-1] == "っ"
#         #     else hiragana

#         #     pass
#         # lemma = hiragana

#         lemma = get_hiragana(node.feature.lForm) if node.feature.lForm else hiragana

#         if all(len(pair) == 2 for pair in pairs):
#             # ふりがな only
#             result.append("".join(ふりがな(node.surface, hiragana)))
#         elif len(pairs) == 2 and len(pairs[0]) == 2 and len(pairs[1]) == 1:
#             result.append(おくりがな2(pairs[0][0], pairs[0][1], pairs[1][0], lemma))
#         elif (
#             len(pairs) in [3, 4]
#             and len([pair for pair in pairs if len(pair) == 2]) == 2
#         ):
#             kanji1 = pairs.pop(0)
#             if len(kanji1) != 2:
#                 raise ValueError("Expected first Kanji node")
#             if len(pairs[0]) == 2:
#                 kana1 = ""
#             else:
#                 kana1 = pairs.pop(0)
#             kanji2 = pairs.pop(0)
#             if len(kanji2) != 2:
#                 raise ValueError("Expected second Kanji node")
#             kana2 = ("",) if len(pairs) == 0 else pairs.pop(0)
#             result.append(
#                 おくりがな3(
#                     kanji1[0],
#                     kanji1[1],
#                     kana1[0],
#                     kanji2[0],
#                     kanji2[1],
#                     kana2[0],
#                     lemma,
#                 )
#             )
#         else:
#             result.append("".join(pair[0] for pair in pairs))
#     return "".join(result)
