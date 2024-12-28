from jawikt.furigana.annotator import FuriganaAnnotator
from jawikt.furigana.tokenizer import VibratoTokenizer


def test_annotator():
    tokenizer = VibratoTokenizer()
    result = list(
        FuriganaAnnotator(tokenizer).annotate("私は北海道でアイヌ語を勉強しています。")
    )
    assert len(result) == 13
    features = [
        ["代名詞", "ワタクシ"],
        ["助詞-係助詞", "ワ"],
        ["名詞-固有名詞-地名-一般", "ホッカイドー"],
        ["助詞-格助詞", "デ"],
        ["名詞-固有名詞-一般", "アイヌ"],
        ["名詞-普通名詞-一般", "ゴ"],
        ["助詞-格助詞", "オ"],
        ["名詞-普通名詞-サ変可能", "ベンキョー"],
        ["動詞-非自立可能", "シ"],
        ["助詞-接続助詞", "テ"],
        ["動詞-非自立可能", "イ"],
        ["助動詞", "マス"],
        ["補助記号-句点", "*"],
    ]
    for token, (expected_pos, expected_pron) in zip(result, features):
        assert token.part_of_speech == expected_pos.split("-")
        assert token.pronunciation == expected_pron
