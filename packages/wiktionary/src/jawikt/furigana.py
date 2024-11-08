from wikitext import Template


def ふりがな(origin: str, kana: str) -> str:
    return str(Template("ふりがな", origin, kana))


# {{おくりがな2|辞める|や|める|やめる}}}
def おくりがな2(han: str, kana: str, okurigana: str, whole: str) -> str:
    return str(Template("おくりがな2", han, kana, okurigana, whole))


# {{おくりがな3|思|おも|い|遣|や|り|おもいやり}}。
def おくりがな3(
    han1: str,
    kana1: str,
    okurigana1: str,
    han2: str,
    kana2: str,
    okurigana2: str,
    whole: str,
) -> str:
    return str(
        Template("おくりがな3", han1, kana1, okurigana1, han2, kana2, okurigana2, whole)
    )
