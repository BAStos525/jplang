from lxml import etree

data="kanjidic2.xml"

tree = etree.parse(data)
root = tree.getroot()

sounds = {}

for character in tree.iter("character"):
    freq = character.xpath(".//freq")
    if freq == None or len(freq) == 0:
        continue
    freq_int = 3000 - int(freq[0].text)
    literal = character.xpath(".//literal")
    onyomi = character.xpath('.//reading[@r_type="ja_on"]')
    for on in onyomi:
        #print("{}={}".format(literal[0].text, on.text))
        if on.text in sounds:
            sounds[on.text] += freq_int
        else:
            sounds[on.text] = freq_int
            
 
print(len(sounds.keys()))
frequency_ordered = sorted(sounds.items(), key=lambda item: item[1])
ends = {}
for k,v in frequency_ordered:
    if len(k) > 1:
        if k[-1] in ends:
            ends[k[-1]] += 1
        else:
            ends[k[-1]] = 1
    print("{:10}\t{:10}\t\t{:10}".format(v, k, len(k)))
    


letters = [
("とお", "トオ", "too", "too"),
("とう", "トう", "tou", "toː"),
("きゃ", "キャ", "kya", "kʲa"),
("きゅ", "キュ", "kyu", "kʲɯ"),
("きょ", "キョ", "kyo", "kʲo"),
("しゃ", "シャ", "sha", "ɕa"),
("しゅ", "シュ", "shu", "ɕɯ"),
("しょ", "ショ", "sho", "ɕo"),
("ちゃ", "チャ", "cha", "tɕa"),
("ちゅ", "チュ", "chu", "tɕɯ"),
("ちょ", "チョ", "cho", "tɕo"),
("にゃ", "ニャ", "nya", "nʲa"),
("にゅ", "ニュ", "nyu", "nʲɯ"),
("にょ", "ニョ", "nyo", "nʲo"),
("ひゃ", "ヒャ", "hya", "ça"),
("ひゅ", "ヒュ", "hyu", "çɯ"),
("ひょ", "ヒョ", "hyo", "ço"),
("みゃ", "ミャ", "mya", "mʲa"),
("みゅ", "ミュ", "myu", "mʲɯ"),
("みょ", "ミョ", "myo", "mʲo"),
("りゃ", "リャ", "rya", "ɾʲa"),
("りゅ", "リュ", "ryu", "ɾʲɯ"),
("りょ", "リョ", "ryo", "ɾʲo"),
("ぎゃ", "ギャ", "gya", "gʲa"),
("ぎゅ", "ギュ", "gyu", "gʲɯ"),
("ぎょ", "ギョ", "gyo", "gʲo"),
("じゃ", "ジャ", "ja", "dʑa"),
("じゅ", "ジュ", "ju", "dʑɯ"),
("じょ", "ジョ", "jo", "dʑo"),
("ぢゃ", "ヂャ", "ja", "dʑa"),
("ぢゅ", "ヂュ", "ju", "dʑɯ"),
("ぢょ", "ヂョ", "jo", "dʑo"),
("びゃ", "ビャ", "bya", "bʲa"),
("びゅ", "ビュ", "byu", "bʲɯ"),
("びょ", "ビョ", "byo", "bʲo"),
("ぴゃ", "ピャ", "pya", "pʲa"),
("ぴゅ", "ピュ", "pyu", "pʲɯ"),
("ぴょ", "ピョ", "pyo", "pʲo"),
("いぇ", "イェ", "ye", "je"),
("うぃ", "ウィ", "wi", "wi"),
("うぇ", "ウェ", "we", "we"),
("うぉ", "ウォ", "wo", "wo"),
("しぇ", "シェ", "she", "ɕe"),
("つぁ", "ツァ", "tsa", "tsa"),
("つぃ", "ツィ", "tsi", "tsɯ"), 
("つぇ", "ツェ", "tse", "tse"), 
("つぉ", "ツォ", "tso", "tso"),
("ちぇ", "チェ", "che", "tɕe"), 
("てぃ", "ティ", "ti", "ti"),
("とぅ", "トゥ", "tu", "tɯ"),
("ふぁ", "ファ", "fa", "ɸa"),
("ふぃ", "フィ", "fi", "ɸi"),
("ふぇ", "フェ", "fe", "ɸe"),
("ふぉ", "フォ", "fo", "ɸo"),
("ふゅ", "フュ", "fu", "ɸʲɯ"),
("ゔぁ", "ヴァ", "ba", "ba"),
("ゔぃ", "ヴィ", "bi", "bi"),
("ゔぇ", "ヴェ", "be", "be"),
("ゔぉ", "ヴォ", "bo", "bo"),
("ゔ", "ヴ", "bu", "bɯ"),
("じぇ", "ジェ", "je", "dʑe"), 
("でぃ", "ディ", "di", "di"),
("どぅ", "ドゥ", "du", "dɯ"),
("あ", "ア", "a", "a"),
("い", "イ", "i", "i"),
("う", "ウ", "u", "ɯ"),
("え", "エ", "e", "e"),
("お", "オ", "o", "o"),
("か", "カ", "ka", "ka"),
("き", "キ", "ki", "kʲi"),
("く", "ク", "ku", "kɯ"),
("け", "ケ", "ke", "ke"),
("こ", "コ", "ko", "ko"),
("さ", "サ", "sa", "sa"),
("し", "シ", "shi", "ɕi"),
("す", "ス", "su", "sɯ"),
("せ", "セ", "se", "se"),
("そ", "ソ", "so", "so"),
("た", "タ", "ta", "ta"),
("ち", "チ", "chi", "tɕi"),
("つ", "ツ", "tsu", "tsɯ"),
("て", "テ", "te", "te"),
("と", "ト", "to", "to"),
("な", "ナ", "na", "na"),
("に", "ニ", "ni", "nʲi"),
("ぬ", "ヌ", "nu", "nɯ"),
("ね", "ネ", "ne", "ne"),
("の", "ノ", "no", "no"),
("は", "ハ", "ha", "ha"),
("ひ", "ヒ", "hi", "çi"),
("ふ", "フ", "fu", "ɸɯ"),
("へ", "ヘ", "he", "he"),
("ほ", "ホ", "ho", "ho"),
("ま", "マ", "ma", "ma"),
("み", "ミ", "mi", "mi"),
("む", "ム", "mu", "mɯ"),
("め", "メ", "me", "me"),
("も", "モ", "mo", "mo"),
("や", "ヤ", "ya", "ja"),
("ゆ", "ユ", "yu", "jɯ"),
("よ", "ヨ", "yo", "jo"),
("ら", "ラ", "ra", "ɾa"),
("り", "リ", "ri", "ɾi"),
("る", "ル", "ru", "ɾɯ"),
("れ", "レ", "re", "ɾe"),
("ろ", "ロ", "ro", "ɾo"),
("わ", "ワ", "wa", "wa"),
("ゐ", "ヰ", "wi", "i"),
("ゑ", "ヱ", "(y)e", "e"),
("を", "ヲ", "wo", "o"),
("ん", "ン", "n", "N"),
("が", "ガ", "ga", "ga"),
("ぎ", "ギ", "gi", "gʲi"),
("ぐ", "グ", "gu", "gɯ"),
("げ", "ゲ", "ge", "ge"),
("ご", "ゴ", "go", "go"),
("ざ", "ザ", "za", "dza"),
("じ", "ジ", "ji", "dʑi"),
("ず", "ズ", "zu", "dzɯ"),
("ぜ", "ゼ", "ze", "dze"),
("ぞ", "ゾ", "zo", "dzo"),
("だ", "ダ", "da", "da"),
("ぢ", "ヂ", "ji", "dʑi"),
("づ", "ヅ", "zu", "dzɯ"),
("で", "デ", "de", "de"),
("ど", "ド", "do", "do"),
("ば", "バ", "ba", "ba"),
("び", "ビ", "bi", "bi"),
("ぶ", "ブ", "bu", "bɯ"),
("べ", "ベ", "be", "be"),
("ぼ", "ボ", "bo", "bo"),
("ぱ", "パ", "pa", "pa"),
("ぴ", "ピ", "pi", "pi"),
("ぷ", "プ", "pu", "pɯ"),
("ぺ", "ペ", "pe", "pe"),
("ぽ", "ポ", "po", "po"),
]

print("Ends")
for k,v in ends.items():
    romaji = k[:]
    for equiv in letters:
        romaji = romaji.replace(equiv[1], equiv[2])
    print("{} or {} appears {} times".format(k, romaji, v))
    