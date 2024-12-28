from jawikt.furigana.templates import ふりがな, おくりがな2, おくりがな3


def test_furigana():
    assert ふりがな("漢字", "かんじ") == "{{ふりがな|漢字|かんじ}}"


def test_okurigana2():
    # Test with the example from the comment: 辞める|や|める|やめる
    assert (
        おくりがな2("辞", "や", "める", "やめる") == "{{おくりがな2|辞|や|める|やめる}}"
    )


def test_okurigana3():
    # Test with the example from the comment: 思|おも|い|遣|や|り|おもいやり
    assert (
        おくりがな3("思", "おも", "い", "遣", "や", "り", "おもいやり")
        == "{{おくりがな3|思|おも|い|遣|や|り|おもいやり}}"
    )
