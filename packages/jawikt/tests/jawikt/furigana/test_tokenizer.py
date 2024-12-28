from jawikt.furigana.tokenizer import VibratoTokenizer, Token


def test_vibrato_tokenizer():
    tokenizer = VibratoTokenizer()
    assert list(tokenizer.tokenize("私は北海道でアイヌ語を勉強しています。")) == [
        Token(
            surface="私",
            lemma="私-代名詞",
            orthographical_form="私",
            pronunciation="ワタクシ",
            part_of_speech=["代名詞"],
        ),
        Token(
            surface="は",
            lemma="は",
            orthographical_form="は",
            pronunciation="ワ",
            part_of_speech=["助詞", "係助詞"],
        ),
        Token(
            surface="北海道",
            lemma="ホッカイドウ",
            orthographical_form="北海道",
            pronunciation="ホッカイドー",
            part_of_speech=["名詞", "固有名詞", "地名", "一般"],
        ),
        Token(
            surface="で",
            lemma="で",
            orthographical_form="で",
            pronunciation="デ",
            part_of_speech=["助詞", "格助詞"],
        ),
        Token(
            surface="アイヌ",
            lemma="アイヌ-Ainu",
            orthographical_form="アイヌ",
            pronunciation="アイヌ",
            part_of_speech=["名詞", "固有名詞", "一般"],
        ),
        Token(
            surface="語",
            lemma="語",
            orthographical_form="語",
            pronunciation="ゴ",
            part_of_speech=["名詞", "普通名詞", "一般"],
        ),
        Token(
            surface="を",
            lemma="を",
            orthographical_form="を",
            pronunciation="オ",
            part_of_speech=["助詞", "格助詞"],
        ),
        Token(
            surface="勉強",
            lemma="勉強",
            orthographical_form="勉強",
            pronunciation="ベンキョー",
            part_of_speech=["名詞", "普通名詞", "サ変可能"],
        ),
        Token(
            surface="し",
            lemma="為る",
            orthographical_form="する",
            pronunciation="シ",
            part_of_speech=["動詞", "非自立可能"],
        ),
        Token(
            surface="て",
            lemma="て",
            orthographical_form="て",
            pronunciation="テ",
            part_of_speech=["助詞", "接続助詞"],
        ),
        Token(
            surface="い",
            lemma="居る",
            orthographical_form="いる",
            pronunciation="イ",
            part_of_speech=["動詞", "非自立可能"],
        ),
        Token(
            surface="ます",
            lemma="ます",
            orthographical_form="ます",
            pronunciation="マス",
            part_of_speech=["助動詞"],
        ),
        Token(
            surface="。",
            lemma="。",
            orthographical_form="。",
            pronunciation="*",
            part_of_speech=["補助記号", "句点"],
        ),
    ]
