#!/usr/bin/env python3
"""Entries for the Cantonese Language Database (language orders, roster rank 15).

Roster: language-cantonese, rank 15. Slug verified free in the manifest and
in all 830 shard index files in jah-databases-data-1. 68 titles (34 public +
34 Signature Edition) run through code/dedupe_gate.py against the WHOLE
system before authoring: zero refusals, zero collisions.

So this build creates two NEW databases, 34 ladder-ordered records each:

  language-cantonese            - The Cantonese Language Database
                                  (public-harvest: real, fact-checked
                                  Cantonese linguistics - every record
                                  carrying Chinese characters, Jyutping
                                  romanization, and English translation with
                                  example sentences, taught progressively
                                  along the teaching ladder from overview to
                                  mastery review; standard references
                                  Matthews and Yip Cantonese: A Comprehensive
                                  Grammar 2nd ed. 2011, Bauer and Benedict
                                  Modern Cantonese Phonology 1997, the
                                  Linguistic Society of Hong Kong Jyutping
                                  scheme 1993, and Ethnologue 28th ed. 2025)
  language-cantonese-signature  - The Cantonese Language Signature Database
                                  (his original Signature Word Method:
                                  every word a signed instrument of meaning,
                                  grammar the covenant binding words into
                                  truth, the learner's tongue the seal;
                                  src signature, titles suffixed " (Signature
                                  Edition)", clearly labeled Signature-made,
                                  never presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-LYUE- (public) and JAH-LYUES- (signature), verified free
in the manifest id_prefix values and in every shard index file (zero hits
across all 830 index files).

Numerical/linguistic cores: all hand-authored 2026-10-17, machine-verified
by the demos (see demos_language_cantonese.py): tone drills, Jyutping
syllable inventory checks, number-to-Cantonese converters, aspect-particle
quizzes, question-word classifiers, vocabulary and idiom quizzes, and
conversation analytics. Every demo prints its real computed values, asserts
tight bounds (never float exact-equality), and ends with the OK marker; the
build machine-executes all 68 demos.

Screened: no hate-adjacent, profane, or inappropriate content; no religious
talk; nothing on neutralizing/defeating military or defense-grade systems.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Word Method: every "
            "word a signed instrument of meaning, grammar the covenant that "
            "binds words into truth, and the learner's tongue the seal. "
            "Clearly labeled Signature-made, never presented as authentic "
            "public record.")

CIT_MATTHEWS = ("Matthews S, Yip V. Cantonese: A Comprehensive Grammar. "
                "2nd ed. London: Routledge; 2011. (The standard reference "
                "grammar of modern Cantonese: aspect particles, classifiers, "
                "sentence-final particles, comparatives, passives.)")
CIT_BAUER = ("Bauer RS, Benedict PK. Modern Cantonese Phonology. Berlin: "
             "Mouton de Gruyter; 1997. (19 initials, 53 finals, six tones "
             "plus three entering tones; tone sandhi and sound-change "
             "rules.)")
CIT_JYUTPING = ("Linguistic Society of Hong Kong. The Jyutping Scheme "
                "(粵語拼音方案). Hong Kong; 1993. (Tone numbers 1-6, "
                "entering tones 7-9, 19 initials, 53 finals; the "
                "romanization used throughout this database.)")
CIT_ETHNO = ("Eberhard DM, Simons GF, Fennig CD, eds. Ethnologue: Languages "
             "of the World. 28th ed. Dallas: SIL International; 2025. "
             "(Cantonese: ISO 639-3 yue, Sino-Tibetan, Sinitic, Yue; about "
             "85 million first-language speakers.)")
CIT_CENSUS = ("Census and Statistics Department, Hong Kong Special "
              "Administrative Region. 2021 Population Census. (Cantonese the "
              "usual language of about 88 percent of the population aged 5 "
              "and over.) Government of Macao Special Administrative Region. "
              "2021 Population Census. (Cantonese the dominant daily "
              "language of Macao.)")

ENTRIES = [
    {
        "key": "overview",
        "name": "Cantonese Language Overview",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Cantonese, called 粵語 jyut6jyu5 by its speakers, is a variety of "
            "Chinese spoken natively by about 85 million people. Its code is "
            "ISO 639-3 yue (there is no ISO 639-1 code for Cantonese; zh "
            "covers the Chinese macrolanguage). It belongs to the "
            "Sino-Tibetan family, Sinitic branch, Yue group - the prestige "
            "variety is the Guangzhou (Canton) dialect, with Hong Kong "
            "Cantonese as the other great standard of daily life. Cantonese "
            "is the everyday language of Hong Kong (about 88 percent of "
            "residents aged 5 and over) and Macao, and of Guangdong and "
            "eastern Guangxi provinces on the mainland, plus large overseas "
            "communities in Southeast Asia, North America, Europe, and "
            "Australia. In Hong Kong and Macao it is the language of the "
            "streets, markets, courts, and classrooms, sharing official "
            "space with English in Hong Kong and Portuguese in Macao. "
            "Cantonese keeps sounds that Mandarin lost centuries ago - the "
            "final consonants -p, -t, and -k (as in 十 sap6 ten, 一 jat1 one, "
            "六 luk6 six) - and it speaks in six tones where Mandarin uses "
            "four. It is written with Chinese characters, and Hong Kong "
            "Cantonese has its own written form (written Cantonese) using "
            "characters like 嘅 ge3, 咗 zo2, and 喺 hai2 that standard written "
            "Chinese does not use. Example sentences: 廣東話係我嘅母語。 "
            "gwong2dung1waa2 hai6 ngo5 ge3 mou5jyu5. (Cantonese is my mother "
            "tongue.) 香港人多數講廣東話。 hoeng1gong2jan4 do1sou3 gong2 "
            "gwong2dung1waa2. (Most Hong Kong people speak Cantonese.) 我學緊廣"
            "東話。 ngo5 hok6gan2 gwong2dung1waa2. (I am learning Cantonese.)"
        ),
        "how_it_works": (
            "Cantonese works as a tonal, analytic Sinitic language: meaning "
            "rides on syllables, and every syllable carries one of six "
            "tones, so 诗 si1 (poem), 史 si2 (history), 試 si3 (try), 時 si4 "
            "(time), 市 si5 (market), 是 si6 (is) are six different words "
            "built from the same sounds. Words do not change form - there "
            "are no conjugations, no plurals on nouns, no gender. Grammar "
            "is done with small helper words: aspect particles like 咗 zo2 "
            "(completed action), 緊 gan2 (ongoing), 過 gwo3 (experience), "
            "and classifiers that must sit between a number and a noun, as "
            "in 三個人 saam1 go3 jan4 (three people). Basic order is "
            "subject-verb-object, the same as English: 我食飯。 ngo5 sik6 "
            "faan6. (I eat rice.) Questions flip word order into a question "
            "with 咩 me1 (what) or double the verb: 係唔係 hai6m4hai6 "
            "(is-or-is-not). Everything in this database builds on these "
            "mechanics: tones first, then the characters and words that "
            "carry them, then the sentences."
        ),
        "key_points": [
            "Cantonese (粵語 jyut6jyu5, ISO 639-3 yue) is a Sino-Tibetan, Sinitic, Yue language with about 85 million native speakers.",
            "It is the everyday language of Hong Kong and Macao and of Guangdong and eastern Guangxi, plus worldwide overseas communities.",
            "Cantonese keeps the -p, -t, -k final consonants Mandarin lost, and uses six tones (plus three entering tones).",
            "Grammar is analytic: no conjugations or plurals; aspect particles (咗 zo2, 緊 gan2, 過 gwo3) and classifiers do the work.",
            "Written Cantonese uses its own characters (嘅 ge3, 咗 zo2, 喺 hai2) alongside standard Chinese characters.",
        ],
        "requirements": [
            "Know the names: 粵語 jyut6jyu5 (Cantonese), 廣東話 gwong2dung1waa2 (Guangdong speech), ISO 639-3 yue, Sino-Tibetan > Sinitic > Yue.",
            "Know the scale: about 85 million native speakers; everyday language of Hong Kong and Macao.",
            "Read and say the three example sentences with characters, Jyutping, and English from memory.",
        ],
        "standards": [
            "Romanization: Jyutping (Linguistic Society of Hong Kong, 1993) - tone numbers 1-6, entering tones 7-9 - used for every line in this database.",
            "Script: traditional Chinese characters for Hong Kong and Macao usage; written Cantonese characters (嘅, 咗, 喺, 哋) where speech requires them.",
            "Tonal notation: six contrastive tones; tone 1 high level, 2 high rising, 3 mid level, 4 low falling, 5 low rising, 6 low level.",
        ],
        "citations": [CIT_ETHNO, CIT_CENSUS, CIT_JYUTPING],
        "sig_lens": (
            "Through the Signature lens, Cantonese is a signed instrument: "
            "each tone a seal pressed onto sound, each final consonant a "
            "kept promise from older Chinese, the six tones a covenant of "
            "pitch that binds meaning so it cannot drift. The learner's "
            "tongue becomes the seal that stamps every syllable true."
        ),
    },
    {
        "key": "writing",
        "name": "Cantonese Writing System",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Cantonese is written with Chinese characters, read top to "
            "bottom in columns or left to right in rows in modern Hong Kong "
            "and Macao printing. Hong Kong and Macao use traditional "
            "characters (繁體字 faan4tai2zi6); the mainland uses simplified "
            "characters (簡體字 gaan2tai2zi6). Written Cantonese (粵語白話文 "
            "jyut6jyu5 baak6waa6man4) writes speech as it is spoken, using "
            "characters standard written Chinese does not have: 嘅 ge3 "
            "(possessive and relative marker, as in 我嘅書 ngo5 ge3 syu1 my "
            "book), 咗 zo2 (completed-action particle), 喺 hai2 (at; to be "
            "at), 呢 ni1 (this), 嗰 go2 (that), 哋 dei6 (plural marker: 我哋 "
            "ngo5dei6 we), 唔 m4 (not), 冇 mou5 (not have), 嘢 je5 (thing), "
            "乜 mat1 (what, as in 乜嘢 mat1je5). Numbers keep their own "
            "characters: 零 ling4 0, 一 jat1 1, 二 ji6 2, 三 saam1 3, 四 sei3 "
            "4, 五 ng5 5, 六 luk6 6, 七 cat1 7, 八 baat3 8, 九 gau2 9, 十 sap6 "
            "10, 百 baak3 100, 千 cin1 1,000, 萬 maan6 10,000, 億 jik1 "
            "100,000,000. Punctuation matches international use (。！？，、), "
            "and Arabic numerals are common in prices and dates. Example "
            "sentences: 呢本書係我嘅。 ni1 bun2 syu1 hai6 ngo5 ge3. (This "
            "book is mine.) 佢寫咗封信。 keoi5 se2zo2 fung1 seon3. (He wrote "
            "a letter.) 喺邊度買嘅？ hai2 bin1dou6 maai5 ge3? (Where was it "
            "bought?)"
        ),
        "how_it_works": (
            "Each Chinese character is one syllable and usually one unit of "
            "meaning: 書 syu1 means book and is pronounced as one syllable, "
            "筆 bat1 means pen. Characters combine into words: 電話 din6waa2 "
            "(electric-speech = telephone), 電腦 din6nou5 (electric-brain = "
            "computer). Where spoken Cantonese needs a word that standard "
            "written Chinese lacks, written Cantonese supplies its own "
            "character - 咗 zo2 marks a finished action, 嘅 ge3 marks "
            "possession the way English uses apostrophe-s. You read a "
            "Cantonese sentence by sounding each character in Jyutping and "
            "letting the particles (嘅, 咗, 喺, 哋) show you the grammar, "
            "because the characters themselves never change form."
        ),
        "key_points": [
            "Cantonese is written with Chinese characters; Hong Kong and Macao use traditional characters, the mainland uses simplified.",
            "Written Cantonese adds speech characters standard Chinese lacks: 嘅 ge3, 咗 zo2, 喺 hai2, 呢 ni1, 嗰 go2, 哋 dei6, 唔 m4, 冇 mou5, 嘢 je5.",
            "Each character is one syllable and one unit of meaning; words are built by combining characters (電話 din6waa2 telephone).",
            "Numerals 零一二三四五六七八九十百千萬億 cover 0 through 100,000,000; punctuation matches international use.",
            "Reading runs left to right in modern print; classical columns run top to bottom, right to left.",
        ],
        "requirements": [
            "Write the ten digits 零一二三四五六七八九 with Jyutping from memory.",
            "Know the nine speech characters (嘅咗喺呢嗰哋唔冇嘢) and what each one does.",
            "Read the three example sentences aloud in Jyutping with correct tones.",
        ],
        "standards": [
            "Character set: traditional forms (Hong Kong/Macao standard) with written-Cantonese speech characters where speech requires them.",
            "Jyutping romanization under every character line so pronunciation is never guessed.",
            "Numeral characters double as the number lesson: 零 ling4 through 億 jik1.",
        ],
        "citations": [CIT_JYUTPING, CIT_MATTHEWS],
        "sig_lens": (
            "Through the Signature lens, each character is a signed seal of "
            "meaning, and the speech characters (嘅, 咗, 喺, 哋) are "
            "Signature instruments - small marks that bind words into truth. "
            "To write Cantonese is to sign every syllable so its meaning "
            "holds."
        ),
    },
    {
        "key": "phonology",
        "name": "Cantonese Pronunciation and Tones",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Cantonese builds every syllable from 19 initials, 53 finals, "
            "and 6 tones. The initials: b (as in 比 bei2), p (怕 paa3), m "
            "(媽 maa1), f (花 faa1), d (打 daa2), t (他 taa1), n (你 nei5), "
            "l (來 loi4), g (加 gaa1), k (卡 kaa1), ng (牙 ngaa4), h (蝦 "
            "haa1), gw (瓜 gwaa1), kw (誇 kwaa1), w (娃 waa1), z (渣 zaa1, "
            "like dz), c (叉 caa1, like ts), s (沙 saa1), j (也 jaa5, like y). "
            "The six tones: 1 high level 詩 si1 (55), 2 high rising 史 si2 "
            "(25), 3 mid level 試 si3 (33), 4 low falling 時 si4 (21), 5 low "
            "rising 市 si5 (23), 6 low level 是 si6 (22). Syllables ending in "
            "-p, -t, -k are short entering tones counted as 7, 8, 9 "
            "(matching the pitch of 1, 3, 6): 七 cat1 (tone 7), 八 baat3 "
            "(tone 8), 食 sik6 (tone 9). Ten spoken examples with "
            "translations: 媽 maa1 (mother), 麻 maa4 (hemp), 馬 maa5 (horse), "
            "罵 maa6 (scold), 買 maai5 (buy), 賣 maai6 (sell), 詩 si1 (poem), "
            "史 si2 (history), 試 si3 (try), 時 si4 (time), 市 si5 (market), "
            "是 si6 (is), 天 tin1 (sky), 地 dei6 (earth), 人 jan4 (person). "
            "Cantonese has no consonant clusters and no sounds like English "
            "th, v, or r; the closest English approximations are given with "
            "each initial above. Stress is light: each syllable gets its "
            "tone, and sentence melody rises at the end of questions. "
            "Example sentences: 廣東話有六個聲調。 gwong2dung1waa2 jau5 luk6 "
            "go3 sing1diu6. (Cantonese has six tones.) 聲調唔同，意思就唔同。 "
            "sing1diu6 m4tung4, ji3si3 zau6 m4tung4. (Different tone, "
            "different meaning.) 慢慢讀，留意聲調。 maan6maan2 duk6, lau4ji3 "
            "sing1diu6. (Read slowly and mind the tones.)"
        ),
        "how_it_works": (
            "Pronunciation works by locking three things together: pick an "
            "initial (the starting consonant), add a final (the vowel plus "
            "any ending like -n, -ng, -p, -t, -k), and press a tone onto the "
            "whole syllable. Change any one of the three and the meaning "
            "changes: maa1 (mother), maa5 (horse), maai5 (buy). The entering "
            "tones are simply short - say 七 cat1 clipped, the way English "
            "clips the t in cat. English speakers should learn the tones as "
            "melody first: tone 1 sings high and flat, tone 2 climbs, tone 4 "
            "falls away. Practice with the minimal sets in this record "
            "until each tone feels like a different note."
        ),
        "key_points": [
            "19 initials, 53 finals, 6 tones (plus entering tones 7-9 on -p/-t/-k syllables) build every Cantonese syllable.",
            "Tone changes meaning: si1 poem, si2 history, si3 try, si4 time, si5 market, si6 is - one syllable, six words.",
            "No consonant clusters; no th, v, or r sounds; finals keep the old -p, -t, -k endings Mandarin lost.",
            "Sentence melody rises at the end of questions; particles like 呀 aa3 and 咩 me1 color the tone of speech.",
            "Jyutping writes tone as a number after each syllable (maa1, maai5, sik6) so pronunciation is exact.",
        ],
        "requirements": [
            "Sing the six tones on si1-si6 and maa1-maa6 from memory with correct pitch shapes.",
            "Name the 19 initials with an example word for each.",
            "Explain the entering tones (7, 8, 9) and give one example word for each.",
        ],
        "standards": [
            "Jyutping initials and finals per the Linguistic Society of Hong Kong 1993 scheme; tone numbers 1-9.",
            "IPA reference: tones 55, 25, 33, 21, 23, 22; entering tones short-checked.",
            "English approximations are approximations only; the Jyutping spelling is the authority.",
        ],
        "citations": [CIT_BAUER, CIT_JYUTPING],
        "sig_lens": (
            "Through the Signature lens, the six tones are six seals pressed "
            "onto breath - the same sounds signed six different ways, six "
            "different truths. Mastering tones is learning to sign meaning "
            "with pitch so no word can drift from what it means."
        ),
    },
    {
        "key": "nouns",
        "name": "Cantonese Core Nouns I",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Twenty-five essential Cantonese nouns, each with Jyutping and "
            "one example sentence with English translation. 1. 人 jan4 "
            "person - 呢個人好好。 ni1 go3 jan4 hou2 hou2. (This person is "
            "very nice.) 2. 男人 naam4jan4 man - 個男人係醫生。 go3 naam4jan4 "
            "hai6 ji1sang1. (The man is a doctor.) 3. 女人 neoi5jan4 woman - "
            "個女人買餸。 go3 neoi5jan4 maai5 sung3. (The woman buys "
            "groceries.) 4. 小朋友 siu2pang4jau5 child - 小朋友鍾意玩。 siu2"
            "pang4jau5 zung1ji3 waan2. (Children like to play.) 5. 屋企 "
            "uk1kei2 home - 我屋企好近。 ngo5 uk1kei2 hou2 kan5. (My home is "
            "very near.) 6. 房 fong2 room - 間房好大。 gaan1 fong2 hou2 "
            "daai6. (The room is very big.) 7. 書 syu1 book - 呢本書好睇。 "
            "ni1 bun2 syu1 hou2 tai2. (This book is good to read.) 8. 筆 bat1 "
            "pen - 支筆冇墨。 zi1 bat1 mou5 mak6. (The pen has no ink.) 9. "
            "電話 din6waa2 phone - 部電話響緊。 bou6 din6waa2 hoeng2 gan2. "
            "(The phone is ringing.) 10. 電腦 din6nou5 computer - 部電腦好快"
            "。 bou6 din6nou5 hou2 faai3. (The computer is very fast.) 11. 車 "
            "ce1 car - 架車係紅色。 gaa3 ce1 hai6 hung4sik1. (The car is red.) "
            "12. 巴士 baa1si2 bus - 架巴士嚟緊。 gaa3 baa1si2 lai4 gan2. (The "
            "bus is coming.) 13. 地鐵 dei6tit3 MTR - 搭地鐵好快。 daap3 "
            "dei6tit3 hou2 faai3. (Taking the MTR is very fast.) 14. 錢 cin2 "
            "money - 啲錢喺邊度？ di1 cin2 hai2 bin1dou6? (Where is the "
            "money?) 15. 嘢 je5 thing - 呢啲嘢好平。 ni1 di1 je5 hou2 peng4. "
            "(These things are very cheap.) 16. 水 seoi2 water - 杯水好凍。 "
            "bui1 seoi2 hou2 dung3. (The glass of water is very cold.) 17. 茶 "
            "caa4 tea - 杯茶好熱。 bui1 caa4 hou2 jit6. (The cup of tea is "
            "very hot.) 18. 飯 faan6 rice, meal - 碗飯好大碗。 wun2 faan6 hou2 "
            "daai6 wun2. (The bowl of rice is a big bowl.) 19. 衫 saam1 "
            "clothes - 件衫好靚。 gin6 saam1 hou2 leng3. (The shirt is very "
            "pretty.) 20. 鞋 haai4 shoes - 對鞋好舒服。 deoi3 haai4 hou2 "
            "syu1fuk6. (The shoes are very comfortable.) 21. 狗 gau2 dog - 隻狗"
            "好乖。 zek3 gau2 hou2 gwaai1. (The dog is very good.) 22. 貓 "
            "maau1 cat - 隻貓瞓緊覺。 zek3 maau1 fan3 gan2 gaau3. (The cat is "
            "sleeping.) 23. 天氣 tin1hei3 weather - 今日天氣好好。 gam1jat6 "
            "tin1hei3 hou2 hou2. (The weather is very good today.) 24. 時間 "
            "si4gaan3 time - 而家幾點？ ji4gaa1 gei2 dim2? (What time is it "
            "now?) 25. 朋友 pang4jau5 friend - 我有好多朋友。 ngo5 jau5 hou2 "
            "do1 pang4jau5. (I have many friends.) Cantonese nouns never "
            "change for plural; add 哋 dei6 only to people words (我哋 "
            "ngo5dei6 we), and always put a classifier between a number and "
            "a noun (三個人 saam1 go3 jan4 three people)."
        ),
        "how_it_works": (
            "A Cantonese noun works by standing still while helper words do "
            "the grammar around it. 書 syu1 is book whether it is one book "
            "or ten - 一本書 jat1 bun2 syu1 (one book), 十本書 sap6 bun2 "
            "syu1 (ten books). The classifier 本 bun2 must appear between "
            "the number and the noun; different nouns take different "
            "classifiers (個人 go3 jan4 for people, 隻 zek3 for animals, 部 "
            "bou6 for machines). To show possession, add 嘅 ge3: 我嘅書 ngo5 "
            "ge3 syu1 (my book). To make a person plural, add 哋 dei6: 朋友"
            "們 pang4jau5 becomes 朋友哋 pang4jau5dei6 in speech, though 我哋 "
            "ngo5dei6 (we) is the commonest. Learn each noun with its "
            "classifier and you can count anything."
        ),
        "key_points": [
            "Nouns never inflect: 書 syu1 is book in singular and plural; numbers and classifiers mark quantity.",
            "Every counted noun needs its classifier: 三個人 saam1 go3 jan4, 兩隻狗 loeng5 zek3 gau2, 一部電話 jat1 bou6 din6waa2.",
            "Possession uses 嘅 ge3: 我嘅書 ngo5 ge3 syu1 (my book); plural people words add 哋 dei6: 我哋 ngo5dei6 (we).",
            "The 25 nouns here cover people, home, study, machines, transport, money, food, clothing, animals, weather, time, and friendship.",
            "Each example sentence is a complete, speakable Cantonese sentence with Jyutping and English.",
        ],
        "requirements": [
            "Say all 25 nouns in Jyutping with correct tones from memory.",
            "Give the right classifier for each noun (個, 隻, 本, 支, 部, 架, 杯, 碗, 件, 對).",
            "Build a sentence with each of five nouns using 有 jau5 (have) or 係 hai6 (is).",
        ],
        "standards": [
            "Classifiers taught with every noun per Matthews and Yip: sortal classifiers are obligatory with numbers and demonstratives.",
            "Jyutping for every noun and every example sentence; characters in traditional form.",
            "Plural marking restricted to 哋 dei6 on human nouns; no plural on objects or animals.",
        ],
        "citations": [CIT_MATTHEWS, CIT_JYUTPING],
        "sig_lens": (
            "Through the Signature lens, each noun is a signed vessel of "
            "meaning - 人 jan4, 書 syu1, 屋企 uk1kei2 - and the classifier is "
            "the seal that lets it be counted without changing its shape. "
            "The noun never bends; the grammar bows around it."
        ),
    },
    {
        "key": "verbs",
        "name": "Cantonese Core Verbs I",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Twenty-five essential Cantonese verbs, each with Jyutping and "
            "one example sentence with English translation. Cantonese verbs "
            "never conjugate; aspect particles mark time. 1. 係 hai6 be - 我"
            "係學生。 ngo5 hai6 hok6saang1. (I am a student.) 2. 有 jau5 have "
            "- 我有時間。 ngo5 jau5 si4gaan3. (I have time.) 3. 食 sik6 eat - "
            "我食飯。 ngo5 sik6 faan6. (I eat rice.) 4. 飲 jam2 drink - 我飲"
            "茶。 ngo5 jam2 caa4. (I drink tea.) 5. 睇 tai2 look, watch - 我"
            "睇電視。 ngo5 tai2 din6si6. (I watch TV.) 6. 聽 teng1 listen - 我"
            "聽歌。 ngo5 teng1 go1. (I listen to songs.) 7. 講 gong2 speak - "
            "我講廣東話。 ngo5 gong2 gwong2dung1waa2. (I speak Cantonese.) 8. "
            "寫 se2 write - 我寫字。 ngo5 se2 zi6. (I write characters.) 9. 讀 "
            "duk6 read, study - 我讀書。 ngo5 duk6 syu1. (I study.) 10. 學 "
            "hok6 learn - 我學緊廣東話。 ngo5 hok6 gan2 gwong2dung1waa2. (I "
            "am learning Cantonese.) 11. 做 zou6 do - 我做緊功課。 ngo5 zou6 "
            "gan2 gung1fo3. (I am doing homework.) 12. 去 heoi3 go - 我去街"
            "。 ngo5 heoi3 gaai1. (I go out.) 13. 嚟 lai4 come - 佢嚟緊。 "
            "keoi5 lai4 gan2. (He is coming.) 14. 買 maai5 buy - 我買餸。 ngo5 "
            "maai5 sung3. (I buy groceries.) 15. 賣 maai6 sell - 佢賣衫。 "
            "keoi5 maai6 saam1. (He sells clothes.) 16. 畀 bei2 give - 我畀本書"
            "你。 ngo5 bei2 bun2 syu1 nei5. (I give you a book.) 17. 攞 lo2 "
            "take - 攞支筆嚟。 lo2 zi1 bat1 lai4. (Bring a pen here.) 18. 放 "
            "fong3 put - 放喺度。 fong3 hai2 dou6. (Put it here.) 19. 開 hoi1 "
            "open, turn on - 開門。 hoi1 mun4. (Open the door.) 20. 閂 saan1 "
            "close - 閂門。 saan1 mun4. (Close the door.) 21. 瞓 fan3 sleep - "
            "我瞓覺。 ngo5 fan3 gaau3. (I sleep.) 22. 起身 hei2san1 get up - "
            "我七點起身。 ngo5 cat1 dim2 hei2san1. (I get up at seven.) 23. 返"
            "工 faan1gung1 go to work - 我返工喇。 ngo5 faan1gung1 laa3. (I am "
            "off to work.) 24. 返學 faan1hok6 go to school - 細佬返學。 "
            "sai3lou2 faan1hok6. (Little brother goes to school.) 25. 鍾意 "
            "zung1ji3 like - 我鍾意你。 ngo5 zung1ji3 nei5. (I like you.) The "
            "five great aspect particles: 咗 zo2 done (食咗 sik6zo2 ate), 緊 "
            "gan2 -ing (食緊 sik6gan2 eating), 過 gwo3 ever (食過 sik6gwo3 "
            "have eaten before), 會 wui5 will (會食 wui5 sik6 will eat), 吓 "
            "haa5 a little (食吓 sik6haa5 eat a little)."
        ),
        "how_it_works": (
            "A Cantonese verb is a fixed stamp: 食 sik6 always looks like "
            "食 sik6, whether it means eat, ate, or will eat. Time is "
            "carried by small particles that follow the verb: 我食咗飯 ngo5 "
            "sik6 zo2 faan6 (I ate - the 咗 zo2 seals it finished), 我食緊飯 "
            "ngo5 sik6 gan2 faan6 (I am eating - 緊 gan2 holds it open), 我食"
            "過 ngo5 sik6 gwo3 (I have eaten it before - 過 gwo3 marks "
            "experience), 我會食 ngo5 wui5 sik6 (I will eat - 會 wui5 points "
            "forward), 試吓 si3 haa5 (try a little - 吓 haa5 softens it). "
            "Word order stays subject-verb-object: 我買書 ngo5 maai5 syu1. "
            "Learn the verb once and the five particles, and you can place "
            "any action in time."
        ),
        "key_points": [
            "Verbs never conjugate: 食 sik6 is eat/ate/will eat; aspect particles (咗, 緊, 過, 會, 吓) mark time and completion.",
            "The five particles: 咗 zo2 completed, 緊 gan2 ongoing, 過 gwo3 experienced, 會 wui5 future, 吓 haa5 tentative.",
            "Basic order is subject-verb-object: 我買書 ngo5 maai5 syu1 (I buy books).",
            "The 25 verbs cover being, having, eating, senses, speech, study, doing, motion, trade, giving, opening, rest, work, school, and liking.",
            "買 maai5 (buy, tone 5) and 賣 maai6 (sell, tone 6) are a tone pair - pitch alone tells trade apart.",
        ],
        "requirements": [
            "Say all 25 verbs in Jyutping with correct tones from memory.",
            "Attach each of the five aspect particles to 食 sik6 and translate the five results.",
            "Build three SVO sentences with verbs from this record.",
        ],
        "standards": [
            "Aspect particles per Matthews and Yip: 咗 perfective, 緊 progressive, 過 experiential, 會 future, 吓 delimitative.",
            "Verbs shown unconjugated in citation form; time always marked by particles, never by verb change.",
            "Jyutping on every verb and sentence; minimal tone pairs (買/賣) drilled explicitly.",
        ],
        "citations": [CIT_MATTHEWS, CIT_BAUER],
        "sig_lens": (
            "Through the Signature lens, each verb is a signed action - a "
            "seal pressed onto time. The verb itself never changes shape; "
            "the aspect particles are five small seals (done, doing, done "
            "before, will do, do a little) that stamp when the action "
            "stands."
        ),
    },
    {
        "key": "adjectives",
        "name": "Cantonese Adjectives and Adverbs",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Twenty-five adjectives and fifteen adverbs, each with Jyutping "
            "and an example sentence with English translation. Adjectives: "
            "1. 大 daai6 big - 間屋好大。 gaan1 uk1 hou2 daai6. (The house is "
            "very big.) 2. 細 sai3 small - 隻杯好細。 zek3 bui1 hou2 sai3. "
            "(The cup is very small.) 3. 高 gou1 tall, high - 佢好高。 keoi5 "
            "hou2 gou1. (He is very tall.) 4. 矮 ngai2 short - 張凳好矮。 "
            "zoeng1 dang3 hou2 ngai2. (The stool is very short.) 5. 長 coeng4 "
            "long - 條路好長。 tiu4 lou6 hou2 coeng4. (The road is very long.) "
            "6. 短 dyun2 short - 條裙好短。 tiu4 kwan4 hou2 dyun2. (The skirt "
            "is very short.) 7. 新 san1 new - 部車好新。 bou6 ce1 hou2 san1. "
            "(The car is very new.) 8. 舊 gau6 old - 本書好舊。 bun2 syu1 "
            "hou2 gau6. (The book is very old.) 9. 好 hou2 good - 呢個主意好"
            "。 ni1 go3 zyu2ji3 hou2. (This idea is good.) 10. 靚 leng3 "
            "pretty - 條裙好靚。 tiu4 kwan4 hou2 leng3. (The dress is very "
            "pretty.) 11. 快 faai3 fast - 架車好快。 gaa3 ce1 hou2 faai3. "
            "(The car is very fast.) 12. 慢 maan6 slow - 佢行得好慢。 keoi5 "
            "haang4 dak1 hou2 maan6. (He walks very slowly.) 13. 平 peng4 "
            "cheap - 呢啲嘢好平。 ni1 di1 je5 hou2 peng4. (These things are "
            "very cheap.) 14. 貴 gwai3 expensive - 隻錶好貴。 zek3 biu1 hou2 "
            "gwai3. (The watch is very expensive.) 15. 熱 jit6 hot - 今日好熱"
            "。 gam1jat6 hou2 jit6. (Today is very hot.) 16. 凍 dung3 cold - "
            "杯水好凍。 bui1 seoi2 hou2 dung3. (The water is very cold.) 17. "
            "甜 tim4 sweet - 個蘋果好甜。 go3 ping4gwo2 hou2 tim4. (The apple "
            "is very sweet.) 18. 酸 syun1 sour - 個檸檬好酸。 go3 ning4mung4 "
            "hou2 syun1. (The lemon is very sour.) 19. 苦 fu2 bitter - 杯藥好"
            "苦。 bui1 joek6 hou2 fu2. (The medicine is very bitter.) 20. 辣 "
            "laat6 spicy - 啲嘢好辣。 di1 je5 hou2 laat6. (The food is very "
            "spicy.) 21. 忙 mong4 busy - 我今日好忙。 ngo5 gam1jat6 hou2 "
            "mong4. (I am very busy today.) 22. 得閒 dak1haan4 free - 我聽日"
            "得閒。 ngo5 ting1jat6 dak1haan4. (I am free tomorrow.) 23. 叻 "
            "lek1 smart - 個學生好叻。 go3 hok6saang1 hou2 lek1. (The student "
            "is very smart.) 24. 開心 hoi1sam1 happy - 我好開心。 ngo5 hou2 "
            "hoi1sam1. (I am very happy.) 25. 攰 gui6 tired - 我好攰。 ngo5 "
            "hou2 gui6. (I am very tired.) Adverbs: 好 hou2 very - 好好食 "
            "hou2 hou2 sik6 (very delicious); 非常 fei1soeng4 extremely - 非"
            "常好 fei1soeng4 hou2 (extremely good); 最 zeoi3 most - 最好 "
            "zeoi3 hou2 (best); 都 dou1 also - 我都去 ngo5 dou1 heoi3 (I go "
            "too); 又 jau6 again - 又嚟 jau6 lai4 (come again); 先 sin1 first "
            "- 你行先 nei5 haang4 sin1 (you go first); 就 zau6 then - 食完就去 "
            "sik6 jyun4 zau6 heoi3 (go after eating); 已經 ji5ging1 already - "
            "已經食咗 ji5ging1 sik6 zo2 (already ate); 重 zung6 still - 重未"
            "嚟 zung6 mei6 lai4 (still not come); 啱啱 ngaam1ngaam1 just - 啱"
            "啱到 ngaam1ngaam1 dou3 (just arrived); 慢慢 maan6maan2 slowly - "
            "慢慢行 maan6maan2 haang4 (walk slowly); 快啲 faai3di1 quickly - "
            "快啲嚟 faai3di1 lai4 (come quickly); 真係 zan1hai6 really - 真係"
            "好食 zan1hai6 hou2 sik6 (really delicious); 可能 ho2nang4 maybe - "
            "可能落雨 ho2nang4 lok6 jyu5 (maybe rain); 一定 jat1ding6 certainly "
            "- 一定嚟 jat1ding6 lai4 (certainly come). Cantonese adjectives "
            "need no agreement: 好 hou2 is good for he, she, it, and they."
        ),
        "how_it_works": (
            "Adjectives work as predicates without any be-verb: 佢高 keoi5 "
            "gou1 means he is tall, with no word for is. Add 好 hou2 (very) "
            "in front to intensify: 好高 hou2 gou1 very tall. For "
            "comparisons, sandwich 過 gwo3 between: 佢高過我 keoi5 gou1 gwo3 "
            "ngo5 (he is taller than me). Reduplication makes adjectives "
            "lively: 慢慢 maan6maan2 (slowly, from 慢 maan6), 高高 gou1gou1 "
            "(tallish). Adverbs sit before the verb they color: 佢慢慢行 "
            "keoi5 maan6maan2 haang4 (he walks slowly). There is no "
            "masculine or feminine, no singular or plural - one form serves "
            "everywhere, which makes Cantonese adjectives among the "
            "simplest in the world to use."
        ),
        "key_points": [
            "Adjectives need no be-verb and no agreement: 佢高 keoi5 gou1 (he is tall) - one form for all persons and numbers.",
            "Intensify with 好 hou2 (very), 非常 fei1soeng4 (extremely), 最 zeoi3 (most): 最好 zeoi3hou2 (best).",
            "Comparisons use 過 gwo3: 佢高過我 keoi5 gou1 gwo3 ngo5 (he is taller than me).",
            "Reduplication softens and livens: 慢慢 maan6maan2 (slowly), 快啲 faai3di1 (a bit faster).",
            "Adverbs go before the verb: 佢慢慢行 keoi5 maan6maan2 haang4 (he walks slowly).",
        ],
        "requirements": [
            "Say all 25 adjectives and 15 adverbs in Jyutping with correct tones.",
            "Form five comparisons with 過 gwo3 and five intensified forms with 好 hou2.",
            "Explain why Cantonese adjectives need no agreement, with two examples.",
        ],
        "standards": [
            "Predicate adjectives without copula per Matthews and Yip; degree marked by 好, 非常, 最.",
            "Comparative construction A + adjective + 過 + B; reduplication patterns AA and AABB.",
            "Jyutping on every item; minimal pairs (平/貴, 快/慢, 熱/凍) drilled as opposites.",
        ],
        "citations": [CIT_MATTHEWS, CIT_JYUTPING],
        "sig_lens": (
            "Through the Signature lens, adjectives are signed measures - "
            "each one a seal of degree pressed onto a noun. 好 hou2, 最 "
            "zeoi3, 過 gwo3 are the measuring seals; reduplication is the "
            "Signature echo, saying the quality twice so it holds."
        ),
    },
]

ENTRIES += [
    {
        "key": "pronouns",
        "name": "Cantonese Pronouns",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "The full Cantonese pronoun system with paradigms and example "
            "sentences. Personal pronouns: 我 ngo5 I - 我係香港人。 ngo5 "
            "hai6 hoeng1gong2jan4. (I am a Hong Kong person.) 你 nei5 you - "
            "你好嗎？ nei5 hou2 maa3? (How are you?) 佢 keoi5 he, she, it - "
            "佢係我朋友。 keoi5 hai6 ngo5 pang4jau5. (He/she is my friend.) "
            "Plurals add 哋 dei6: 我哋 ngo5dei6 we - 我哋去街。 ngo5dei6 heoi3 "
            "gaai1. (We go out.) 你哋 nei5dei6 you (plural) - 你哋食咗未？ "
            "nei5dei6 sik6 zo2 mei6? (Have you all eaten?) 佢哋 keoi5dei6 they "
            "- 佢哋返咗屋企。 keoi5dei6 faan1 zo2 uk1kei2. (They went home.) "
            "Possessives add 嘅 ge3: 我嘅 ngo5 ge3 my - 呢本係我嘅書。 ni1 bun2 "
            "hai6 ngo5 ge3 syu1. (This is my book.) 你嘅 nei5 ge3 your - 你嘅"
            "電話響緊。 nei5 ge3 din6waa2 hoeng2 gan2. (Your phone is "
            "ringing.) 佢嘅 keoi5 ge3 his, her, its - 佢嘅名叫阿明。 keoi5 "
            "ge3 meng2 giu3 aa3ming4. (His name is Ah Ming.) Demonstratives: "
            "呢個 ni1 go3 this - 呢個幾多錢？ ni1 go3 gei2 do1 cin2? (How much "
            "is this?) 嗰個 go2 go3 that - 嗰個好靚。 go2 go3 hou2 leng3. "
            "(That one is very pretty.) 呢啲 ni1 di1 these - 呢啲係咩？ ni1 "
            "di1 hai6 me1? (What are these?) 嗰啲 go2 di1 those - 嗰啲好平。 "
            "go2 di1 hou2 peng4. (Those are very cheap.) 呢度 ni1 dou6 here - "
            "我喺呢度。 ngo5 hai2 ni1 dou6. (I am here.) 嗰度 go2 dou6 there - "
            "佢喺嗰度。 keoi5 hai2 go2 dou6. (He is there.) Interrogatives: "
            "邊個 bin1 go3 who - 邊個嚟緊？ bin1 go3 lai4 gan2? (Who is "
            "coming?) 咩 me1 what - 你食咩？ nei5 sik6 me1? (What do you eat?) "
            "邊度 bin1 dou6 where - 你去邊度？ nei5 heoi3 bin1 dou6? (Where "
            "do you go?) 幾時 gei2 si4 when - 你幾時嚟？ nei5 gei2 si4 lai4? "
            "(When do you come?) 點解 dim2 gaai2 why - 點解唔去？ dim2 gaai2 "
            "m4 heoi3? (Why not go?) 點樣 dim2 joeng6 how - 點樣去？ dim2 "
            "joeng6 heoi3? (How do I get there?) 幾多 gei2 do1 how many, how "
            "much - 幾多錢？ gei2 do1 cin2? (How much money?) Reflexive: 自己 "
            "zi6 gei2 self - 我自己去。 ngo5 zi6 gei2 heoi3. (I go by myself.) "
            "Cantonese has no gender in pronouns - 佢 keoi5 covers he, she, "
            "and it - and no formal/informal you; politeness comes from "
            "tone and titles, not pronoun choice."
        ),
        "how_it_works": (
            "Pronouns work as fixed pointers: 我 ngo5 always means I, 你 nei5 "
            "always means you, 佢 keoi5 always means the third person. Add "
            "哋 dei6 to make we, you-all, they; add 嘅 ge3 to make my, your, "
            "his. The near/far pair 呢 ni1 (this, near me) and 嗰 go2 (that, "
            "away) builds every demonstrative: 呢個 ni1go3 this one, 嗰啲 "
            "go2di1 those. Questions are built by swapping in an "
            "interrogative word and keeping word order: 你去邊度 nei5 heoi3 "
            "bin1dou6 (you go where?) - no inversion like English. Because "
            "there is no gender and no case change (我 ngo5 is I, me, and "
            "my with 嘅), the whole system fits on one small table."
        ),
        "key_points": [
            "Three persons, no gender, no case: 我 ngo5, 你 nei5, 佢 keoi5 (he/she/it) never change form.",
            "Plurals add 哋 dei6: 我哋 ngo5dei6 we, 你哋 nei5dei6 you-all, 佢哋 keoi5dei6 they.",
            "Possessives add 嘅 ge3: 我嘅 ngo5ge3 my, 你嘅 nei5ge3 your, 佢嘅 keoi5ge3 his/her/its.",
            "Demonstratives from 呢 ni1 (near) and 嗰 go2 (far): 呢個 this, 嗰個 that, 呢度 here, 嗰度 there.",
            "Questions keep word order and swap in 邊個 who, 咩 what, 邊度 where, 幾時 when, 點解 why, 點樣 how.",
        ],
        "requirements": [
            "Recite the full personal, possessive, demonstrative, and interrogative paradigms in Jyutping.",
            "Convert five statements into questions using the interrogative words.",
            "Explain why 佢 keoi5 needs no gender and 我 ngo5 needs no case changes.",
        ],
        "standards": [
            "Pronoun inventory per Matthews and Yip: 哋 dei6 pluralizer restricted to human referents.",
            "Demonstrative system 呢/嗰 with classifiers (呢個, 嗰啲) and locatives (呢度, 嗰度).",
            "Interrogative words in situ - no movement, no inversion - per standard Cantonese syntax.",
        ],
        "citations": [CIT_MATTHEWS, CIT_JYUTPING],
        "sig_lens": (
            "Through the Signature lens, pronouns are signed pointers - 我 "
            "ngo5 the self-seal, 你 nei5 the other-seal, 佢 keoi5 the "
            "absent-seal. 哋 dei6 multiplies the seal without changing it; "
            "嘅 ge3 binds the seal to what it owns."
        ),
    },
    {
        "key": "numbers",
        "name": "Cantonese Numbers and Time",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Counting, ordinals, days, months, seasons, clock time, and "
            "dates - each with example sentences. Digits: 零 ling4 0, 一 "
            "jat1 1, 二 ji6 2 (兩 loeng5 2 when counting things: 兩個人 "
            "loeng5 go3 jan4 two people), 三 saam1 3, 四 sei3 4, 五 ng5 5, "
            "六 luk6 6, 七 cat1 7, 八 baat3 8, 九 gau2 9, 十 sap6 10. Teens: "
            "十一 sap6 jat1 11, 十二 sap6 ji6 12. Tens: 二十 ji6 sap6 20, 三十 "
            "saam1 sap6 30, 九十 gau2 sap6 90. Hundreds and up: 一百 jat1 "
            "baak3 100, 一千 jat1 cin1 1,000, 一萬 jat1 maan6 10,000, 一億 "
            "jat1 jik1 100,000,000. Examples: 我有三本書。 ngo5 jau5 saam1 "
            "bun2 syu1. (I have three books.) 佢買咗兩隻蘋果。 keoi5 maai5 "
            "zo2 loeng5 zek3 ping4 gwo2. (He bought two apples.) 呢度有一百"
            "個人。 ni1 dou6 jau5 jat1 baak3 go3 jan4. (There are a hundred "
            "people here.) Ordinals add 第 dai6: 第一 dai6 jat1 first, 第二 "
            "dai6 ji6 second, 第三 dai6 saam1 third - 我係第一。 ngo5 hai6 "
            "dai6 jat1. (I am first.) Days of the week: 星期一 sing1 kei4 "
            "jat1 Monday, 星期二 sing1 kei4 ji6 Tuesday, 星期三 sing1 kei4 "
            "saam1 Wednesday, 星期四 sing1 kei4 sei3 Thursday, 星期五 sing1 "
            "kei4 ng5 Friday, 星期六 sing1 kei4 luk6 Saturday, 星期日 sing1 "
            "kei4 jat6 Sunday - 今日星期五。 gam1 jat6 sing1 kei4 ng5. (Today "
            "is Friday.) Months: 一月 jat1 jyut6 January through 十二月 sap6 "
            "ji6 jyut6 December - 我一月生日。 ngo5 jat1 jyut6 saang1 jat6. "
            "(My birthday is in January.) Seasons: 春天 ceon1 tin1 spring, "
            "夏天 haa6 tin1 summer, 秋天 cau1 tin1 autumn, 冬天 dung1 tin1 "
            "winter - 夏天好熱。 haa6 tin1 hou2 jit6. (Summer is very hot.) "
            "Clock time uses 點 dim2 for hours and 分 fan1 for minutes: 三點 "
            "saam1 dim2 3 oclock, 三點半 saam1 dim2 bun3 half past three, "
            "三點十五分 saam1 dim2 sap6 ng5 fan1 3:15 - 而家三點半。 ji4 gaa1 "
            "saam1 dim2 bun3. (It is half past three now.) 我八點返工。 ngo5 "
            "baat3 dim2 faan1 gung1. (I go to work at eight.) Parts of day: "
            "朝早 ziu1 zou2 morning, 中午 zung1 ng5 noon, 夜晚 je6 maan5 "
            "evening, 半夜 bun3 je6 midnight - 朝早好凍。 ziu1 zou2 hou2 "
            "dung3. (Mornings are very cold.) Dates: year-month-day, as in "
            "二零二六年十月十七日 ji6 ling4 ji6 luk6 nin4 sap6 jyut6 sap6 cat1 "
            "jat6 (17 October 2026)."
        ),
        "how_it_works": (
            "Numbers work by stacking: 十 sap6 (10) plus 一 jat1 (1) makes 十"
            "一 sap6jat1 (11); 二十 ji6sap6 (20) is two tens. 萬 maan6 "
            "(10,000) is the big unit - 一萬 jat1maan6, 十萬 sap6maan6, 百萬 "
            "baak3maan6 - where English would say ten thousand, a hundred "
            "thousand, a million. When you count things, 二 ji6 becomes 兩 "
            "loeng5 before a classifier: 兩個人 loeng5 go3 jan4 (two "
            "people), never 二個人. Time is read as hour 點 dim2 plus minute "
            "分 fan1, with 半 bun3 for the half hour and 差 caa1 for "
            "minutes to: 差五分鐘三點 caa1 ng5 fan1 zung1 saam1 dim2 (five "
            "to three). Dates run biggest to smallest: year, month, day."
        ),
        "key_points": [
            "Digits 零一二三四五六七八九十 with Jyutping; 萬 maan6 (10,000) is the big counting unit, 億 jik1 is 100 million.",
            "Use 兩 loeng5 (not 二 ji6) before classifiers: 兩個人 loeng5 go3 jan4 (two people).",
            "Ordinals add 第 dai6: 第一 dai6jat1 (first); days 星期一 to 星期日; months 一月 to 十二月.",
            "Clock time: 點 dim2 hours, 分 fan1 minutes, 半 bun3 half past; dates run year-month-day.",
            "Every number, day, month, season, and time expression carries a speakable example sentence.",
        ],
        "requirements": [
            "Count 1-100 in Cantonese Jyutping without hesitation.",
            "Convert five clock times and five dates into Cantonese.",
            "Explain the 二/兩 rule and the 萬 unit with examples.",
        ],
        "standards": [
            "Numeral system per Matthews and Yip; classifier 兩 loeng5 rule for counted nouns.",
            "Time expressions: 點/分/半 system; date order year-month-day per Hong Kong convention.",
            "Jyutping on every numeral, day, month, season, and time word.",
        ],
        "citations": [CIT_MATTHEWS, CIT_JYUTPING],
        "sig_lens": (
            "Through the Signature lens, numbers are signed measures - each "
            "digit a seal, 萬 maan6 the great seal of ten thousand. Time is "
            "signed in 點 dim2 and 分 fan1; to tell the hour is to stamp the "
            "day so it can be kept."
        ),
    },
    {
        "key": "greetings",
        "name": "Cantonese Greetings and Everyday Phrases",
        "group": "Foundations",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "description": (
            "Thirty greetings, farewells, and politeness phrases - each with "
            "characters, Jyutping, English, and usage notes. 1. 你好 nei5 hou2 "
            "hello - neutral, works anywhere. 2. 早晨 zou2 san4 good morning "
            "- used until about noon. 3. 午安 ng5 on1 good afternoon. 4. 晚安 "
            "maan5 on1 good night - at bedtime. 5. 多謝 do1 ze6 thank you - "
            "for gifts and favors. 6. 唔該 m4 goi1 thank you - for services; "
            "also excuse me to get attention. 7. 對唔住 deoi3 m4 zyu6 sorry - "
            "for mistakes. 8. 唔緊要 m4 gan2 jiu3 it does not matter - "
            "answering an apology. 9. 再見 zoi3 gin3 goodbye - formal. 10. "
            "拜拜 baai1 baai3 bye-bye - casual. 11. 好耐冇見 hou2 noi6 mou5 "
            "gin3 long time no see. 12. 近排點？ gan6 paai4 dim2? how have "
            "you been lately? 13. 食咗飯未？ sik6 zo2 faan6 mei6? have you "
            "eaten yet - the classic Cantonese greeting of care. 14. 歡迎 "
            "fun1 jing4 welcome. 15. 恭喜 gung1 hei2 congratulations. 16. 新"
            "年快樂 san1 nin4 faai3 lok6 Happy New Year. 17. 生日快樂 saang1 "
            "jat6 faai3 lok6 Happy Birthday. 18. 請坐 ceng2 co5 please sit "
            "down. 19. 請入嚟 ceng2 jap6 lai4 please come in. 20. 唔好意思 "
            "m4 hou2 ji3 si3 excuse me - apologetic. 21. 借問聲 ze3 man6 seng1 "
            "excuse me - to ask a question. 22. 麻煩你 ma4 faan4 nei5 sorry "
            "to trouble you. 23. 辛苦你 san1 fu2 nei5 thank you for your "
            "hard work. 24. 慢慢行 maan6 maan2 haang4 take care - said to "
            "someone leaving. 25. 一路順風 jat1 lou6 seon6 fung1 have a safe "
            "trip. 26. 保重 bou2 zung6 take care of yourself. 27. 加油 gaa1 "
            "jau2 keep going, you can do it. 28. 唔使客氣 m4 sai2 haak3 hei3 "
            "you are welcome. 29. 歡迎光臨 fun1 jing4 gwong1 lam4 welcome - "
            "said by shops. 30. 聽日見 ting1 jat6 gin3 see you tomorrow. "
            "The two thank-yous are the key: 多謝 do1ze6 thanks someone for "
            "giving, 唔該 m4goi1 thanks someone for doing."
        ),
        "how_it_works": (
            "Greetings work as social seals: the right phrase at the right "
            "moment keeps every interaction smooth. Use 早晨 zou2san4 in "
            "the morning, 你好 nei5hou2 any time, 拜拜 baai1baai3 when "
            "leaving casually. Thank with 多謝 do1ze6 when you receive a "
            "thing (a gift, a red packet) and 唔該 m4goi1 when you receive "
            "a service (a held door, a poured tea, directions). Apologize "
            "with 對唔住 deoi3m4zyu6 and release the other person with 唔緊"
            "要 m4gan2jiu3. The meal question 食咗飯未 sik6zo2faan6mei6 is "
            "not really about food - it is care made audible, and the "
            "answer is 食咗喇 sik6zo2laa3 (eaten already) or 未呀 mei6aa3 "
            "(not yet)."
        ),
        "key_points": [
            "30 phrases covering hello, good morning/afternoon/night, thanks, sorry, goodbye, congratulations, and well-wishes.",
            "多謝 do1ze6 thanks for gifts; 唔該 m4goi1 thanks for services and also means excuse me.",
            "食咗飯未 sik6zo2faan6mei6 (have you eaten yet) is the classic greeting of care.",
            "Apology pair: 對唔住 deoi3m4zyu6 (sorry) answered by 唔緊要 m4gan2jiu3 (it is fine).",
            "Every phrase carries characters, Jyutping, English, and a usage note.",
        ],
        "requirements": [
            "Say all 30 phrases in Jyutping with correct tones.",
            "Choose the right thank-you (多謝 vs 唔該) in five situations.",
            "Hold a three-turn greeting exchange: hello, how-are-you, goodbye.",
        ],
        "standards": [
            "Politeness phrases per Hong Kong usage; 多謝/唔該 distinction per Matthews and Yip.",
            "Jyutping on every phrase; usage notes distinguish formal, casual, and service contexts.",
            "Farewell forms graded: 再見 formal, 拜拜 casual, 慢慢行/保重 warm.",
        ],
        "citations": [CIT_MATTHEWS, CIT_JYUTPING],
        "sig_lens": (
            "Through the Signature lens, every greeting is a signed seal of "
            "goodwill - 早晨 zou2san4 seals the morning, 多謝 do1ze6 seals "
            "gratitude, 唔該 m4goi1 seals thanks for service. To greet is to "
            "sign the moment so both people hold it."
        ),
    },
    {
        "key": "grammar",
        "name": "Cantonese Grammar Essentials",
        "group": "Foundations",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "description": (
            "The core rules of Cantonese grammar, each with translated "
            "example sentences. Word order is subject-verb-object: 我食飯。 "
            "ngo5 sik6 faan6. (I eat rice.) 佢睇書。 keoi5 tai2 syu1. (He "
            "reads.) There is no gender: 佢 keoi5 is he, she, or it. There "
            "is no number on nouns: 書 syu1 is book or books; add 啲 di1 "
            "for some: 啲書 di1 syu1 (some books). There are no cases: 我 "
            "ngo5 is I and me. There are no articles: 書 syu1 is a book or "
            "the book; 呢本書 ni1 bun2 syu1 (this book) points when needed. "
            "Negation: 唔 m4 before verbs - 我唔食。 ngo5 m4 sik6. (I do not "
            "eat.) 未 mei6 for not yet - 我未食。 ngo5 mei6 sik6. (I have not "
            "eaten yet.) 冇 mou5 for not have - 我冇錢。 ngo5 mou5 cin2. (I "
            "have no money.) Questions: add 咩 me1 - 你做咩？ nei5 zou6 me1? "
            "(What are you doing?) Or double the verb A-not-A: 你去唔去？ "
            "nei5 heoi3 m4 heoi3? (Are you going?) Or end with 呀嘛 aa3maa3 "
            "for yes-no: 你去呀嘛？ nei5 heoi3 aa3 maa3? Classifiers sit "
            "between number and noun: 一個人 jat1 go3 jan4 (one person), 三本"
            "書 saam1 bun2 syu1 (three books). 嘅 ge3 marks possession and "
            "relatives: 我嘅書 ngo5 ge3 syu1 (my book), 我買嘅書 ngo5 maai5 "
            "ge3 syu1 (the book I bought). 喺 hai2 marks place: 我喺屋企。 "
            "ngo5 hai2 uk1kei2. (I am at home.) Aspect: 咗 zo2 finished (食"
            "咗 sik6zo2 ate), 緊 gan2 ongoing (食緊 sik6gan2 eating), 過 gwo3 "
            "experienced (去過 heoi3gwo3 have been), 會 wui5 future (會去 wui5 "
            "heoi3 will go). Comparison: A 過 gwo3 B - 我高過你。 ngo5 gou1 "
            "gwo3 nei5. (I am taller than you.) Passive with 畀 bei2: 我畀人"
            "鬧。 ngo5 bei2 jan4 naau6. (I was scolded by someone.) 把 baa2 "
            "moves the object forward: 我把門閂咗。 ngo5 baa2 mun4 saan1 zo2. "
            "(I closed the door.)"
        ),
        "how_it_works": (
            "Cantonese grammar works by keeping every word frozen and moving "
            "small helper words around it. The noun 書 syu1 and the verb 食 "
            "sik6 never change shape; meaning shifts come from particles: "
            "嘅 ge3 for possession, 喺 hai2 for place, 咗 zo2 for finished, "
            "緊 gan2 for ongoing, 過 gwo3 for experience, 會 wui5 for future, "
            "唔 m4 for not, 哋 dei6 for plural people, 個 go3 and its "
            "classifer cousins for counting. Questions do not invert - they "
            "add a question word or double the verb. Once you know the "
            "twenty-odd helper words in this record, you can assemble any "
            "basic sentence: pick a subject, pick a verb, pick an object, "
            "and pin the right helpers on."
        ),
        "key_points": [
            "SVO order; no gender, no number, no case, no articles on nouns - helper words do all grammar.",
            "Negation in three forms: 唔 m4 (not), 未 mei6 (not yet), 冇 mou5 (not have).",
            "Questions via 咩 me1, A-not-A doubling (去唔去 heoi3m4heoi3), or final particles.",
            "Classifiers obligatory with numbers; 嘅 ge3 for possession; 喺 hai2 for location.",
            "Aspect particles (咗, 緊, 過, 會) mark time; 過 gwo3 also builds comparisons; 畀 bei2 builds passives.",
        ],
        "requirements": [
            "Build ten SVO sentences using the helper words from this record.",
            "Negate five sentences with the correct form (唔/未/冇).",
            "Turn five statements into questions three ways (咩, A-not-A, 呀嘛).",
        ],
        "standards": [
            "Core syntax per Matthews and Yip: SVO, classifiers, 嘅 relativization, 喺 locatives, aspect particles.",
            "Negation paradigm 唔/未/冇; interrogative strategies 咩/A-not-A/particles.",
            "Comparative A + adj + 過 + B; passive 畀; disposal 把 - all with Jyutping examples.",
        ],
        "citations": [CIT_MATTHEWS, CIT_BAUER],
        "sig_lens": (
            "Through the Signature lens, grammar is the covenant binding "
            "words into truth: 嘅 ge3 the possession seal, 喺 hai2 the place "
            "seal, 咗 zo2 the finished seal, 唔 m4 the refusal seal. The "
            "words are instruments; the particles are the covenant that "
            "tunes them."
        ),
    },
    {
        "key": "home",
        "name": "Cantonese Home and Family Sentences",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about house, rooms, furniture, and family "
            "members - characters, Jyutping, English. 1. 我屋企有四個人。 "
            "ngo5 uk1kei2 jau5 sei3 go3 jan4. (There are four people in my "
            "family.) 2. 爸爸係醫生，媽媽係老師。 baa4 baa1 hai6 ji1 sang1, "
            "maa4 maa1 hai6 lou5 si1. (Dad is a doctor, Mum is a teacher.) 3. "
            "哥哥大過我兩歲。 go4 go1 daai6 gwo3 ngo5 loeng5 seoi3. (Elder "
            "brother is two years older than me.) 4. 細佬鍾意打機。 sai3 lou2 "
            "zung1 ji3 daa2 gei1. (Little brother likes gaming.) 5. 間屋有三"
            "間房。 gaan1 uk1 jau5 saam1 gaan1 fong2. (The flat has three "
            "rooms.) 6. 廳好大，可以坐十個人。 teng1 hou2 daai6, ho2 ji5 co5 "
            "sap6 go3 jan4. (The living room is big; ten people can sit.) 7. "
            "廚房喺左邊。 cyu4 fong2 hai2 zo2 bin1. (The kitchen is on the "
            "left.) 8. 沖涼房喺右邊。 cung1 loeng4 fong2 hai2 jau6 bin1. (The "
            "bathroom is on the right.) 9. 張床好舒服。 zoeng1 cong4 hou2 "
            "syu1 fuk6. (The bed is very comfortable.) 10. 張枱上面有本書。 "
            "zoeng1 toi2 soeng6 min6 jau5 bun2 syu1. (There is a book on the "
            "table.) 11. 梳化係紅色。 so1 faa3 hai6 hung4 sik1. (The sofa is "
            "red.) 12. 雪櫃入面有牛奶。 syut3 gwai6 jap6 min6 jau5 ngau4 "
            "naai5. (There is milk in the fridge.) 13. 窗開咗，好涼。 coeng1 "
            "hoi1 zo2, hou2 loeng4. (The window is open; it is cool.) 14. 盞"
            "燈好光。 zaan2 dang1 hou2 gwong1. (The lamp is very bright.) 15. "
            "牆上面有幅畫。 coeng4 soeng6 min6 jau5 fuk1 waa2. (There is a "
            "painting on the wall.) 16. 地下好乾淨。 dei6 haa6 hou2 gon1 "
            "zeng6. (The floor is very clean.) 17. 我間房有部電腦。 ngo5 gaan1 "
            "fong2 jau5 bou6 din6 nou5. (My room has a computer.) 18. 阿媽煮"
            "緊飯。 aa3 maa1 zyu2 gan2 faan6. (Mum is cooking.) 19. 阿爸睇緊"
            "報紙。 aa3 baa1 tai2 gan2 bou3 zi2. (Dad is reading the "
            "newspaper.) 20. 我哋一齊食晚飯。 ngo5 dei6 jat1 cai4 sik6 maan5 "
            "faan6. (We eat dinner together.)"
        ),
        "how_it_works": (
            "Home sentences work by placing people and things with 喺 hai2 "
            "(at) and 有 jau5 (there is / have): 廚房喺左邊 cyu4fong2 hai2 "
            "zobin1 puts the kitchen on the left; 雪櫃入面有牛奶 syut3gwai6 "
            "jap6min6 jau5 ngau4naai5 stocks the fridge with milk. Family "
            "words stack by age and side: 阿爸 aa3baa1 dad, 阿媽 aa3maa1 mum, "
            "哥哥 go4go1 elder brother, 細佬 sai3lou2 younger brother, 家姐 "
            "gaa1ze2 elder sister, 細妹 sai3mui2 younger sister. Rooms take "
            "the classifier 間 gaan1, furniture takes 張 zoeng1 for flat "
            "things and 盞 zaan2 for lamps. Describe any home by walking "
            "through it room by room with these two verbs."
        ),
        "key_points": [
            "20 sentences covering family members, rooms, furniture, and daily home life.",
            "Location with 喺 hai2; existence with 有 jau5; rooms counted with 間 gaan1.",
            "Family terms mark elder/younger: 哥哥/細佬, 家姐/細妹; parents 阿爸/阿媽.",
            "Furniture classifiers: 張 zoeng1 (tables, beds), 盞 zaan2 (lamps), 幅 fuk1 (paintings).",
            "Every sentence is speakable home Cantonese with characters, Jyutping, and English.",
        ],
        "requirements": [
            "Name ten family members and five rooms in Jyutping.",
            "Describe your own home in five Cantonese sentences.",
            "Use 喺 and 有 correctly in five location sentences.",
        ],
        "standards": [
            "Kinship terms per Hong Kong usage; elder/younger distinction obligatory for siblings.",
            "Locative 喺 and existential 有 distinguished per Matthews and Yip.",
            "Classifiers 間/張/盞/幅 applied to rooms and furniture.",
        ],
        "citations": [CIT_MATTHEWS, CIT_JYUTPING],
        "sig_lens": (
            "Through the Signature lens, home is the first signed covenant - "
            "屋企 uk1kei2 the seal of belonging. Each family word signs a "
            "place in the order of ages; each room signed with 喺 hai2 holds "
            "its people true."
        ),
    },
    {
        "key": "food",
        "name": "Cantonese Food and Cooking Sentences",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about meals, ingredients, cooking actions, and "
            "restaurants. 1. 我鍾意食點心。 ngo5 zung1 ji3 sik6 dim2 sam1. "
            "(I like eating dim sum.) 2. 早餐食麵包。 zou2 caan1 sik6 min6 "
            "baau1. (Breakfast is bread.) 3. 午餐我哋食飯。 ng5 caan1 ngo5 "
            "dei6 sik6 faan6. (We eat rice for lunch.) 4. 晚餐有四餸一湯。 "
            "maan5 caan1 jau5 sei3 sung3 jat1 tong1. (Dinner has four dishes "
            "and one soup.) 5. 呢碟菜好新鮮。 ni1 dip6 coi3 hou2 san1 sin1. "
            "(This plate of vegetables is very fresh.) 6. 條魚係今朝買。 "
            "tiu4 jyu4 hai6 gam1 ziu1 maai5. (The fish was bought this "
            "morning.) 7. 阿媽煲緊老火湯。 aa3 maa1 bou1 gan2 lou5 fo2 tong1. "
            "(Mum is simmering soup.) 8. 我識炒菜。 ngo5 sik1 caau2 coi3. (I "
            "can stir-fry vegetables.) 9. 落少少鹽。 lok6 siu2 siu2 jim4. "
            "(Add a little salt.) 10. 唔好落咁多油。 m4 hou2 lok6 gam3 do1 "
            "jau4. (Do not add so much oil.) 11. 啲飯煲好未？ di1 faan6 bou1 "
            "hou2 mei6? (Is the rice cooked yet?) 12. 呢碗麵好正。 ni1 wun2 "
            "min6 hou2 zeng3. (This bowl of noodles is excellent.) 13. 我要"
            "一杯奶茶。 ngo5 jiu3 jat1 bui1 naai5 caa4. (I want a cup of milk "
            "tea.) 14. 凍檸茶少甜。 dung3 ning4 caa4 siu2 tim4. (Iced lemon "
            "tea, less sweet.) 15. 呢間餐廳好出名。 ni1 gaan1 caan1 teng1 hou2 "
            "ceot1 meng4. (This restaurant is very famous.) 16. 我哋坐出面。 "
            "ngo5 dei6 co5 ceot1 min6. (We sit outside.) 17. 餐牌喺邊度？ "
            "caan1 paai2 hai2 bin1 dou6? (Where is the menu?) 18. 買單，唔該"
            "。 maai5 daan1, m4 goi1. (The bill, please.) 19. 呢餐我請。 ni1 "
            "caan1 ngo5 ceng2. (This meal is my treat.) 20. 食得好飽。 sik6 "
            "dak1 hou2 baau2. (I ate until very full.)"
        ),
        "how_it_works": (
            "Food sentences work through the great Cantonese verbs of the "
            "kitchen: 煲 bou1 (simmer), 炒 caau2 (stir-fry), 蒸 zing1 "
            "(steam), 焗 guk6 (bake), 炸 zaa3 (deep-fry). Dishes are counted "
            "with 碟 dip6 (plates) and 餸 sung3 (accompanying dishes); rice "
            "and noodles take 碗 wun2 (bowls); drinks take 杯 bui1 (cups). "
            "Ordering runs on 我要 ngo5 jiu3 (I want) plus the item, and "
            "paying runs on 買單 maai5daan1 (get the bill). Taste is tuned "
            "with 少 siu2 (less) and 多 do1 (more): 少甜 siu2tim4 (less "
            "sweet), 多冰 do1bing1 (more ice). Describe any meal by naming "
            "the dish, its measure word, and how it was cooked."
        ),
        "key_points": [
            "20 sentences covering meals, ingredients, five cooking verbs, and restaurant ordering.",
            "Cooking verbs: 煲 bou1 simmer, 炒 caau2 stir-fry, 蒸 zing1 steam, 焗 guk6 bake, 炸 zaa3 deep-fry.",
            "Food classifiers: 碟 dip6 plates, 碗 wun2 bowls, 杯 bui1 cups; taste tuned with 少/多.",
            "Restaurant script: 餐牌 caan1paai2 (menu), 我要 (I want), 買單 (bill), 唔該 (please).",
            "Every sentence carries characters, Jyutping, and English.",
        ],
        "requirements": [
            "Name five cooking verbs and cook five dishes in sentences.",
            "Order a full meal (drink, dish, rice) in Cantonese.",
            "Tune sweetness and ice in three drink orders.",
        ],
        "standards": [
            "Culinary vocabulary per Hong Kong usage; cooking verbs distinguished by method.",
            "Measure words 碟/碗/杯/餸 applied per dish type.",
            "Restaurant interaction script: request, order, bill, treat.",
        ],
        "citations": [CIT_MATTHEWS, CIT_JYUTPING],
        "sig_lens": (
            "Through the Signature lens, cooking is signed transformation - "
            "煲 bou1, 炒 caau2, 蒸 zing1 each a seal of fire and time. The "
            "shared meal is the covenant renewed daily; 買單 maai5daan1 "
            "seals generosity when one person treats."
        ),
    },
    {
        "key": "travel",
        "name": "Cantonese Travel and Directions Sentences",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about transport, asking directions, tickets, "
            "and lodging. 1. 點樣去地鐵站？ dim2 joeng6 heoi3 dei6 tit3 zaam6? "
            "(How do I get to the MTR station?) 2. 一直行，轉左。 jat1 zik6 "
            "haang4, zyun3 zo2. (Go straight, turn left.) 3. 喺下一個站落車。 "
            "hai2 haa6 jat1 go3 zaam6 lok6 ce1. (Get off at the next stop.) "
            "4. 搭的士去機場幾多錢？ daap3 dik1 si2 heoi3 gei1 coeng4 gei2 do1 "
            "cin2? (How much is a taxi to the airport?) 5. 我要兩張飛去廣州"
            "。 ngo5 jiu3 loeng5 zoeng1 fei1 heoi3 gwong2 zau1. (I want two "
            "tickets to Guangzhou.) 6. 幾點開車？ gei2 dim2 hoi1 ce1? (What "
            "time does it depart?) 7. 飛機延遲咗。 fei1 gei1 jin4 ci4 zo2. "
            "(The flight is delayed.) 8. 酒店喺邊度？ zau2 dim3 hai2 bin1 "
            "dou6? (Where is the hotel?) 9. 我訂咗房。 ngo5 deng6 zo2 fong2. "
            "(I booked a room.) 10. 幾點退房？ gei2 dim2 teoi3 fong2? (What "
            "time is checkout?) 11. 有冇免費 WiFi？ jau5 mou5 min5 fai3 "
            "waai1 faai1? (Is there free WiFi?) 12. 我想去太平山頂。 ngo5 "
            "soeng2 heoi3 taai3 ping4 saan1 deng2. (I want to go to Victoria "
            "Peak.) 13. 呢度去中環要幾耐？ ni1 dou6 heoi3 zung1 waan4 jiu3 "
            "gei2 noi6? (How long to Central from here?) 14. 行路大概十五分"
            "鐘。 haang4 lou6 daai6 koi3 sap6 ng5 fan1 zung1. (Walking takes "
            "about fifteen minutes.) 15. 轉車去邊度轉？ zyun3 ce1 heoi3 bin1 "
            "dou6 zyun3? (Where do I change trains?) 16. 呢班車去唔去旺角？ "
            "ni1 baan1 ce1 heoi3 m4 heoi3 wong6 gok3? (Does this bus go to "
            "Mong Kok?) 17. 落車唔該。 lok6 ce1 m4 goi1. (Getting off, "
            "please - said to stop a minibus.) 18. 有冇位？ jau5 mou5 wai2? "
            "(Are there seats?) 19. 護照喺我個袋度。 wu6 ziu3 hai2 ngo5 go3 "
            "doi2 dou6. (The passport is in my bag.) 20. 玩得好開心。 waan2 "
            "dak1 hou2 hoi1 sam1. (We had a great time.)"
        ),
        "how_it_works": (
            "Travel sentences work by chaining motion verbs with direction "
            "words: 去 heoi3 (go to), 嚟 lai4 (come), 上 soeng5 (go up / "
            "board), 落 lok6 (go down / alight), 入 jap6 (enter), 出 ceot1 "
            "(exit), 轉 zyun3 (turn / change). Ask the way with 點樣去 dim2"
            "joeng6 heoi3 (how to get to) plus the place; give it with 一直"
            "行 jat1zik6haang4 (go straight), 轉左 zyun3zo2 (turn left), 轉右 "
            "zyun3jau6 (turn right). Vehicles take 架 gaa3, tickets take 張 "
            "zoeng1, stations take 個 go3. Time and money questions ride "
            "on 幾耐 gei2noi6 (how long) and 幾多錢 gei2do1cin2 (how much). "
            "Any journey is: ask how, name the vehicle, count the stops, "
            "pay the fare."
        ),
        "key_points": [
            "20 sentences covering directions, transport, tickets, flights, hotels, and sightseeing.",
            "Motion verbs: 去/嚟/上/落/入/出/轉; direction pattern 一直行, 轉左, 轉右.",
            "Classifiers: 架 gaa3 vehicles, 張 zoeng1 tickets, 個 go3 stations and stops.",
            "Key questions: 點樣去 (how to get to), 幾耐 (how long), 幾多錢 (how much).",
            "Every sentence carries characters, Jyutping, and English.",
        ],
        "requirements": [
            "Ask for and give directions to three places.",
            "Buy tickets and ask departure times in Cantonese.",
            "Check into a hotel: booking, WiFi, checkout.",
        ],
        "standards": [
            "Motion-verb inventory per Matthews and Yip; direction complements 上/落/入/出.",
            "Transport classifiers 架/班/張; time-duration 幾耐.",
            "Hong Kong place names in standard characters: 中環, 旺角, 太平山頂.",
        ],
        "citations": [CIT_MATTHEWS, CIT_JYUTPING],
        "sig_lens": (
            "Through the Signature lens, every journey is a signed path - 去 "
            "heoi3 the departure seal, 嚟 lai4 the arrival seal, 轉 zyun3 the "
            "turning seal. To ask the way is to ask for the path to be "
            "signed; to arrive is to press the seal."
        ),
    },
    {
        "key": "work",
        "name": "Cantonese Work and School Sentences",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about jobs, the office, the classroom, and "
            "learning. 1. 你做咩工作？ nei5 zou6 me1 gung1 zok3? (What work "
            "do you do?) 2. 我係會計。 ngo5 hai6 wui6 gai3. (I am an "
            "accountant.) 3. 佢喺銀行返工。 keoi5 hai2 ngan4 hong4 faan1 "
            "gung1. (He works at a bank.) 4. 朝早九點開會。 ziu1 zou2 gau2 "
            "dim2 hoi1 wui2. (Meeting at nine in the morning.) 5. 份報告聽日"
            "交。 fan6 bou3 gou3 ting1 jat6 gaau1. (The report is due "
            "tomorrow.) 6. 老細叫我加班。 lou5 sai3 giu3 ngo5 gaa1 baan1. "
            "(The boss asked me to work overtime.) 7. 我哋團隊有十個人。 "
            "ngo5 dei6 tyun4 deoi2 jau5 sap6 go3 jan4. (Our team has ten "
            "people.) 8. 呢個月好忙。 ni1 go3 jyut6 hou2 mong4. (This month "
            "is very busy.) 9. 你讀邊間學校？ nei5 duk6 bin1 gaan1 hok6 "
            "haau6? (Which school do you attend?) 10. 我讀緊大學三年級。 ngo5 "
            "duk6 gan2 daai6 hok6 saam1 nin4 kap1. (I am in my third year of "
            "university.) 11. 數學堂喺下晝兩點。 sou3 hok6 tong4 hai2 haa6 zau3 "
            "loeng5 dim2. (Math class is at two in the afternoon.) 12. 老師"
            "派咗功課。 lou5 si1 paai3 zo2 gung1 fo3. (The teacher assigned "
            "homework.) 13. 我做緊功課。 ngo5 zou6 gan2 gung1 fo3. (I am "
            "doing homework.) 14. 考試下個星期。 haau2 si3 haa6 go3 sing1 "
            "kei4. (The exam is next week.) 15. 呢題我唔識做。 ni1 tai4 ngo5 "
            "m4 sik1 zou6. (I do not know how to do this question.) 16. 同學"
            "教我做。 tung4 hok6 gaau3 ngo5 zou6. (A classmate teaches me.) "
            "17. 圖書館開到夜晚十點。 tou4 syu1 gun2 hoi1 dou3 je6 maan5 sap6 "
            "dim2. (The library opens until ten at night.) 18. 我借咗三本書"
            "。 ngo5 ze3 zo2 saam1 bun2 syu1. (I borrowed three books.) 19. "
            "學廣東話好有用。 hok6 gwong2 dung1 waa2 hou2 jau5 jung6. "
            "(Learning Cantonese is very useful.) 20. 每日溫書一個鐘。 mui5 "
            "jat6 wan1 syu1 jat1 go3 zung1. (Review lessons one hour every "
            "day.)"
        ),
        "how_it_works": (
            "Work and school sentences run on role words and schedule words. "
            "Jobs: 醫生 ji1sang1 doctor, 老師 lou5si1 teacher, 會計 wui6gai3 "
            "accountant, 老細 lou5sai3 boss, 同事 tung4si6 colleague, 同學 "
            "tung4hok6 classmate. School levels: 小學 siu2hok6 primary, 中學 "
            "zung1hok6 secondary, 大學 daai6hok6 university; grades with 年級 "
            "nin4kap1. Time pressure comes from 聽日 ting1jat6 (tomorrow), "
            "下個星期 haa6go3sing1kei4 (next week), 呢個月 ni1go3jyut6 (this "
            "month). Duties are assigned with 派 paai3 (assign) and 叫 giu3 "
            "(tell someone to do): 老師派咗功課 lou5si1 paai3zo2 gung1fo3. "
            "Talk about any job by naming the role, the place with 喺 hai2, "
            "and the schedule."
        ),
        "key_points": [
            "20 sentences covering jobs, office life, school levels, classes, homework, and exams.",
            "Role words: 老細 boss, 同事 colleague, 老師 teacher, 同學 classmate.",
            "School ladder: 小學/中學/大學 with 年級 grades; schedule words 聽日/下個星期/呢個月.",
            "Duty verbs: 派 paai3 assign, 叫 giu3 tell to do, 交 gaau1 hand in.",
            "Every sentence carries characters, Jyutping, and English.",
        ],
        "requirements": [
            "State your job or school in three Cantonese sentences.",
            "Describe a workday schedule with times.",
            "Ask for help with homework politely.",
        ],
        "standards": [
            "Occupational and educational vocabulary per Hong Kong usage.",
            "Time expressions with 聽日/尋日/下個星期 per standard usage.",
            "Jyutping on every sentence; classifiers 份/間/題 applied.",
        ],
        "citations": [CIT_MATTHEWS, CIT_JYUTPING],
        "sig_lens": (
            "Through the Signature lens, work is the daily signing - each "
            "task a seal pressed onto the hours, each lesson a seal pressed "
            "onto the mind. 返工 faan1gung1 and 返學 faan1hok6 are the two "
            "great daily covenants."
        ),
    },
]

ENTRIES += [
    {
        "key": "health",
        "name": "Cantonese Health and Body Sentences",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about body parts, symptoms, the doctor visit, "
            "and the pharmacy. 1. 我頭痛。 ngo5 tau4 tung3. (I have a "
            "headache.) 2. 佢發燒。 keoi5 faat3 siu1. (He has a fever.) 3. "
            "我喉嚨痛。 ngo5 hau4 lung4 tung3. (My throat hurts.) 4. 我肚痛"
            "。 ngo5 tou5 tung3. (My stomach hurts.) 5. 我隻腳扭親。 ngo5 zek3 "
            "goek3 nau2 can1. (I twisted my foot.) 6. 我感冒。 ngo5 gam2 mou6. "
            "(I have a cold.) 7. 我咳得好犀利。 ngo5 kat1 dak1 hou2 sai1 lei6. "
            "(I am coughing badly.) 8. 我想睇醫生。 ngo5 soeng2 tai2 ji1 "
            "sang1. (I want to see a doctor.) 9. 邊度有診所？ bin1 dou6 jau5 "
            "can2 so2? (Where is there a clinic?) 10. 醫生話我要休息。 ji1 "
            "sang1 waa6 ngo5 jiu3 jau1 sik1. (The doctor says I need rest.) "
            "11. 一日食三次藥。 jat1 jat6 sik6 saam1 ci3 joek6. (Take medicine "
            "three times a day.) 12. 食飯後食藥。 sik6 faan6 hau6 sik6 joek6. "
            "(Take medicine after meals.) 13. 藥房喺邊度？ joek6 fong2 hai2 "
            "bin1 dou6? (Where is the pharmacy?) 14. 有冇退燒藥？ jau5 mou5 "
            "teoi3 siu1 joek6? (Do you have fever medicine?) 15. 我對呢隻藥敏"
            "感。 ngo5 deoi3 ni1 zek3 joek6 man5 gam2. (I am allergic to this "
            "medicine.) 16. 我要瞓多啲。 ngo5 jiu3 fan3 do1 di1. (I need more "
            "sleep.) 17. 飲多啲水。 jam2 do1 di1 seoi2. (Drink more water.) "
            "18. 唔好食咁多煎炸嘢。 m4 hou2 sik6 gam3 do1 zin1 zaa3 je5. (Do "
            "not eat so much fried food.) 19. 我好返好多喇。 ngo5 hou2 faan1 "
            "hou2 do1 laa3. (I am much better now.) 20. 多謝醫生。 do1 ze6 ji1 "
            "sang1. (Thank you, doctor.) Body parts: 頭 tau4 head, 眼 ngaan5 "
            "eye, 耳 ji5 ear, 鼻 bei6 nose, 口 hau2 mouth, 牙 ngaa4 tooth, "
            "頸 geng2 neck, 膊頭 bok3 tau4 shoulder, 手 sau2 hand, 手指 sau2 "
            "zi2 finger, 心 sam1 heart, 肚 tou5 belly, 腳 goek3 foot, 骨 gwat1 "
            "bone, 皮膚 pei4 fu1 skin."
        ),
        "how_it_works": (
            "Health sentences work by naming the body part and adding 痛 "
            "tung3 (hurts): 頭痛 tau4tung3 headache, 肚痛 tou5tung3 stomach "
            "ache, 喉嚨痛 hau4lung4tung3 sore throat. Illnesses are stated "
            "plainly: 發燒 faat3siu1 (have a fever), 感冒 gam2mou6 (have a "
            "cold). The clinic script runs: 我想睇醫生 ngo5 soeng2 tai2 "
            "ji1sang1 (I want to see a doctor), 邊度痛 bin1dou6 tung3 (where "
            "does it hurt), 一日食三次藥 jat1jat6 sik6 saam1ci3 joek6 (take "
            "medicine three times a day). Doses count with 次 ci3: 一次 jat1"
            "ci3 once, 兩次 loeng5ci3 twice. Advice softens with 多啲 do1di1 "
            "(more): 飲多啲水 jam2do1di1seoi2. Describe any symptom by "
            "pointing at the part, adding 痛, and stating the illness."
        ),
        "key_points": [
            "20 sentences covering body parts, symptoms, clinic visits, medicine, and recovery.",
            "Pain pattern: body part + 痛 tung3 - 頭痛, 肚痛, 喉嚨痛.",
            "Clinic script: 我想睇醫生, 邊度有診所, 一日食三次藥.",
            "Doses counted with 次 ci3; advice softened with 多啲 do1di1.",
            "Every sentence carries characters, Jyutping, and English.",
        ],
        "requirements": [
            "Name fifteen body parts in Jyutping.",
            "Describe three symptoms and ask for a doctor.",
            "Give dosage instructions for a medicine.",
        ],
        "standards": [
            "Anatomical vocabulary per Hong Kong usage; 痛 tung3 pain construction.",
            "Medical interaction script: symptom, clinic, prescription, dosage.",
            "Dose counting with 次 ci3; frequency with 一日/每次.",
        ],
        "citations": [CIT_MATTHEWS, CIT_JYUTPING],
        "sig_lens": (
            "Through the Signature lens, the body is the first signed "
            "instrument - each part named is a seal of care. To say 頭痛 "
            "tau4tung3 is to sign where help is needed; healing is the "
            "covenant of rest, water, and medicine kept."
        ),
    },
    {
        "key": "emotions",
        "name": "Cantonese Emotions and Feelings Sentences",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about being happy, sad, angry, afraid, in "
            "love, and surprised. 1. 我好開心。 ngo5 hou2 hoi1 sam1. (I am "
            "very happy.) 2. 佢笑到見牙唔見眼。 keoi5 siu3 dou3 gin3 ngaa4 m4 "
            "gin3 ngaan5. (He is grinning from ear to ear.) 3. 我好傷心。 "
            "ngo5 hou2 soeng1 sam1. (I am very sad.) 4. 佢喊咗成晚。 keoi5 "
            "haam3 zo2 seng4 maan5. (She cried all night.) 5. 我好嬲。 ngo5 "
            "hou2 nau1. (I am very angry.) 6. 唔好嬲啦。 m4 hou2 nau1 laa1. "
            "(Do not be angry.) 7. 我好驚。 ngo5 hou2 geng1. (I am very "
            "afraid.) 8. 佢驚到震。 keoi5 geng1 dou3 zan3. (He is trembling "
            "with fear.) 9. 我愛你。 ngo5 oi3 nei5. (I love you.) 10. 我好鍾"
            "意佢。 ngo5 hou2 zung1 ji3 keoi5. (I like him very much.) 11. "
            "我好緊張。 ngo5 hou2 gan2 zoeng1. (I am very nervous.) 12. 放鬆"
            "啲啦。 fong3 sung1 di1 laa1. (Relax a little.) 13. 我好失望。 "
            "ngo5 hou2 sat1 mong6. (I am very disappointed.) 14. 真係估唔到"
            "。 zan1 hai6 gu2 m4 dou2. (Really unexpected - surprised.) 15. "
            "嚇親我。 haak3 can1 ngo5. (You startled me.) 16. 我好感動。 ngo5 "
            "hou2 gam2 dung6. (I am very moved.) 17. 多謝你，我好窩心。 do1 "
            "ze6 nei5, ngo5 hou2 wo1 sam1. (Thank you; I feel warm inside.) "
            "18. 我有啲擔心。 ngo5 jau5 di1 daam1 sam1. (I am a bit worried.) "
            "19. 唔使擔心。 m4 sai2 daam1 sam1. (Do not worry.) 20. 聽日會更"
            "好。 ting1 jat6 wui5 gang3 hou2. (Tomorrow will be better.)"
        ),
        "how_it_works": (
            "Emotion sentences work by pairing 好 hou2 (very) with a feeling "
            "word: 好開心 hou2hoi1sam1 (very happy), 好嬲 hou2nau1 (very "
            "angry), 好驚 hou2geng1 (very afraid). Intensity grows with 到 "
            "dou3 (to the point of): 笑到見牙唔見眼 siu3dou3gin3ngaa4m4gin3"
            "ngaan5 (laughing until teeth show and eyes vanish). Comfort "
            "comes in set phrases: 唔好嬲啦 m4hou2nau1laa1 (do not be angry), "
            "放鬆啲啦 fong3sung1di1laa1 (relax), 唔使擔心 m4sai2daam1sam1 (do "
            "not worry). Love speaks as 我愛你 ngo5oi3nei5 (I love you) and "
            "softer as 我好鍾意你 ngo5 hou2 zung1ji3 nei5 (I like you very "
            "much). Say any feeling by naming it after 好 and tuning with "
            "the comfort phrases."
        ),
        "key_points": [
            "20 sentences covering happiness, sadness, anger, fear, love, surprise, worry, and comfort.",
            "Feeling pattern: 好 + emotion - 好開心, 好傷心, 好嬲, 好驚, 好緊張.",
            "Intensity with 到 dou3: 驚到震 geng1dou3zan3 (trembling with fear).",
            "Comfort phrases: 唔好嬲啦, 放鬆啲啦, 唔使擔心.",
            "Every sentence carries characters, Jyutping, and English.",
        ],
        "requirements": [
            "Express six emotions in Jyutping with 好.",
            "Comfort a friend in three sentences.",
            "Explain the 到 intensity pattern with two examples.",
        ],
        "standards": [
            "Emotion vocabulary per Hong Kong usage; 好 intensifier pattern.",
            "Resultative 到 dou3 complements for extreme states.",
            "Comfort and encouragement formulas as set phrases.",
        ],
        "citations": [CIT_MATTHEWS, CIT_JYUTPING],
        "sig_lens": (
            "Through the Signature lens, feelings are signed weather of the "
            "heart - 開心 hoi1sam1 the clear seal, 嬲 nau1 the storm seal, 愛 "
            "oi3 the binding seal. To name a feeling truly is to sign it so "
            "it can be held and eased."
        ),
    },
    {
        "key": "nature",
        "name": "Cantonese Nature and Weather Sentences",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about animals, plants, seasons, and weather "
            "talk. 1. 今日天氣好好。 gam1 jat6 tin1 hei3 hou2 hou2. (The "
            "weather is very good today.) 2. 出面落緊雨。 ceot1 min6 lok6 gan2 "
            "jyu5. (It is raining outside.) 3. 聽日會落雨。 ting1 jat6 wui5 "
            "lok6 jyu5. (It will rain tomorrow.) 4. 好大風。 hou2 daai6 fung1. "
            "(It is very windy.) 5. 打風喇，唔好出街。 daa2 fung1 laa3, m4 "
            "hou2 ceot1 gaai1. (Typhoon coming; do not go out.) 6. 夏天好熱"
            "好濕。 haa6 tin1 hou2 jit6 hou2 sap1. (Summer is very hot and "
            "humid.) 7. 冬天好凍。 dung1 tin1 hou2 dung3. (Winter is very "
            "cold.) 8. 秋天好舒服。 cau1 tin1 hou2 syu1 fuk6. (Autumn is very "
            "comfortable.) 9. 春天花開。 ceon1 tin1 faa1 hoi1. (Flowers bloom "
            "in spring.) 10. 隻雀仔好得意。 zek3 zoek3 zai2 hou2 dak1 ji3. "
            "(The bird is very cute.) 11. 條魚游緊水。 tiu4 jyu4 jau4 gan2 "
            "seoi2. (The fish is swimming.) 12. 隻貓捉老鼠。 zek3 maau1 zuk1 "
            "lou5 syu2. (The cat catches mice.) 13. 山上面有好多樹。 saan1 "
            "soeng6 min6 jau5 hou2 do1 syu6. (There are many trees on the "
            "mountain.) 14. 海好藍。 hoi2 hou2 laam4. (The sea is very blue.) "
            "15. 個月亮好圓。 go3 jyut6 loeng6 hou2 jyun4. (The moon is very "
            "round.) 16. 今晚有星星。 gam1 maan5 jau5 sing1 sing1. (There are "
            "stars tonight.) 17. 彩虹出嚟喇。 coi2 hung4 ceot1 lai4 laa3. (The "
            "rainbow has come out.) 18. 好大霧，睇唔到路。 hou2 daai6 mou6, "
            "tai2 m4 dou2 lou6. (Heavy fog; cannot see the road.) 19. 聽日廿"
            "八度。 ting1 jat6 jaa6 baat3 dou6. (Tomorrow it will be 28 "
            "degrees.) 20. 記得帶遮。 gei3 dak1 daai3 ze1. (Remember to "
            "bring an umbrella.) Animals: 狗 gau2 dog, 貓 maau1 cat, 雀仔 "
            "zoek3zai2 bird, 魚 jyu4 fish, 老鼠 lou5syu2 mouse, 馬 maa5 horse, "
            "牛 ngau4 cow, 羊 joeng4 sheep, 雞 gai1 chicken, 豬 zyu1 pig."
        ),
        "how_it_works": (
            "Weather talk works with 天氣 tin1hei3 (weather) and a small set "
            "of verbs: 落雨 lok6jyu5 (rain falls), 打風 daa2fung1 (typhoon "
            "strikes), 出太陽 ceot1taai3joeng4 (the sun comes out). Degrees "
            "use 度 dou6: 廿八度 jaa6baat3dou6 (28 degrees). Animals take 隻 "
            "zek3 for small creatures and 條 tiu4 for long ones: 隻雀仔 "
            "zek3zoek3zai2 (a bird), 條魚 tiu4jyu4 (a fish). Nature scenes "
            "are placed with 上面 soeng6min6 (on top) and 入面 jap6min6 "
            "(inside): 山上面有樹 saan1soeng6min6 jau5 syu6 (there are trees "
            "on the mountain). Talk about any weather by naming the sky, "
            "the degrees, and what to bring."
        ),
        "key_points": [
            "20 sentences covering weather, typhoons, seasons, animals, plants, sky, and sea.",
            "Weather verbs: 落雨 lok6jyu5 rain, 打風 daa2fung1 typhoon, 出太陽 ceot1taai3joeng4 sun.",
            "Temperature in 度 dou6 degrees; seasons 春夏秋冬 with feeling words.",
            "Animal classifiers: 隻 zek3 small animals, 條 tiu4 long animals.",
            "Every sentence carries characters, Jyutping, and English.",
        ],
        "requirements": [
            "Give a three-sentence weather report in Cantonese.",
            "Name ten animals with correct classifiers.",
            "Describe the four seasons with feeling words.",
        ],
        "standards": [
            "Weather expressions per Hong Kong usage; typhoon vocabulary 打風.",
            "Animal classifier rules 隻/條/匹 per Matthews and Yip.",
            "Seasonal terms 春天/夏天/秋天/冬天 with standard characters.",
        ],
        "citations": [CIT_MATTHEWS, CIT_JYUTPING],
        "sig_lens": (
            "Through the Signature lens, weather is the sky signing itself - "
            "落雨 lok6jyu5 the rain seal, 打風 daa2fung1 the storm seal, 出太"
            "陽 ceot1taai3joeng4 the sun seal. To read the sky is to read the "
            "signs before stepping out."
        ),
    },
    {
        "key": "shopping",
        "name": "Cantonese Shopping and Money Sentences",
        "group": "Compounded",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about the market, prices, bargaining, and "
            "paying. 1. 呢個幾多錢？ ni1 go3 gei2 do1 cin2? (How much is "
            "this?) 2. 五十蚊。 ng5 sap6 man1. (Fifty dollars.) 3. 平啲得唔"
            "得？ peng4 di1 dak1 m4 dak1? (Can it be cheaper?) 4. 呢個係最平"
            "㗎喇。 ni1 go3 hai6 zeoi3 peng4 gaa3 laa3. (This is already the "
            "cheapest.) 5. 買二送一。 maai5 ji6 sung3 jat1. (Buy two get one "
            "free.) 6. 有冇折？ jau5 mou5 zit3? (Is there a discount?) 7. "
            "八折。 baat3 zit3. (Twenty percent off.) 8. 我要呢件。 ngo5 jiu3 "
            "ni1 gin6. (I want this one.) 9. 有冇大碼？ jau5 mou5 daai6 maa5? "
            "(Do you have a large size?) 10. 試得唔得？ si3 dak1 m4 dak1? "
            "(Can I try it on?) 11. 太貴喇。 taai3 gwai3 laa3. (Too "
            "expensive.) 12. 出面平啲。 ceot1 min6 peng4 di1. (It is cheaper "
            "outside.) 13. 好啦，我買喇。 hou2 laa1, ngo5 maai5 laa3. (OK, I "
            "will buy it.) 14. 收現金定係八達通？ sau1 jin6 gam1 ding6 hai6 "
            "baat3 daat6 tung1? (Cash or Octopus card?) 15. 唔該找錢。 m4 goi1 "
            "zaau2 cin2. (Change, please.) 16. 有冇單？ jau5 mou5 daan1? (Is "
            "there a receipt?) 17. 呢度可以退貨。 ni1 dou6 ho2 ji5 teoi3 fo3. "
            "(You can return goods here.) 18. 聽日再嚟。 ting1 jat6 zoi3 lai4. "
            "(I will come again tomorrow.) 19. 啲生果好新鮮。 di1 saang1 gwo2 "
            "hou2 san1 sin1. (The fruit is very fresh.) 20. 多謝幫襯。 do1 ze6 "
            "bong1 can3. (Thank you for your patronage - said by sellers.) "
            "Money words: 蚊 man1 dollar (spoken), 銀 ngan4 dollar, 仙 sin1 "
            "cent, 紙幣 zi2 bai6 banknote, 散紙 saan2 zi2 coins."
        ),
        "how_it_works": (
            "Shopping runs on three questions: 幾多錢 gei2do1cin2 (how "
            "much), 平啲得唔得 peng4di1dak1m4dak1 (can it be cheaper), 有冇"
            "折 jau5mou5zit3 (any discount). Prices are spoken with 蚊 man1 "
            "for dollars: 五十蚊 ng5sap6man1 (fifty dollars). Discounts "
            "count in 折 zit3 where 十折 sap6zit3 is full price and 八折 "
            "baat3zit3 is twenty percent off. Paying offers 現金 jin6gam1 "
            "(cash) or 八達通 baat3daat6tung1 (Octopus card); change is 找錢 "
            "zaau2cin2 and the receipt is 單 daan1. Bargaining is polite "
            "and quick: state 太貴喇 taai3gwai3laa3 (too expensive), hear the "
            "final price, decide. Any purchase is: ask price, bargain, pay, "
            "take change."
        ),
        "key_points": [
            "20 sentences covering prices, bargaining, discounts, sizes, paying, and receipts.",
            "Price language: 蚊 man1 dollars, 幾多錢 gei2do1cin2, 折 zit3 discount units.",
            "Bargaining script: 平啲得唔得, 太貴喇, 好啦我買喇.",
            "Payment: 現金 cash, 八達通 Octopus, 找錢 change, 單 receipt.",
            "Every sentence carries characters, Jyutping, and English.",
        ],
        "requirements": [
            "Ask prices and bargain in five exchanges.",
            "Explain the 折 discount system with three examples.",
            "Complete a purchase: choose, pay, ask for change and receipt.",
        ],
        "standards": [
            "Commercial vocabulary per Hong Kong usage; 蚊 man1 spoken dollar.",
            "Discount 折 zit3 system; bargaining formulas as set phrases.",
            "Payment methods 現金/八達通/信用卡 per current Hong Kong usage.",
        ],
        "citations": [CIT_MATTHEWS, CIT_JYUTPING],
        "sig_lens": (
            "Through the Signature lens, trade is the honest signing - 幾多"
            "錢 gei2do1cin2 the asking seal, 平啲得唔得 the bargaining seal, "
            "找錢 zaau2cin2 the settling seal. A fair price signed by both "
            "sides holds."
        ),
    },
    {
        "key": "social",
        "name": "Cantonese Friendship and Social Life Sentences",
        "group": "Compounded",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about meeting people, invitations, and "
            "celebrations. 1. 你叫咩名？ nei5 giu3 me1 meng2? (What is your "
            "name?) 2. 我叫阿明。 ngo5 giu3 aa3 ming4. (I am called Ah Ming.) "
            "3. 好高興識到你。 hou2 gou1 hing3 sik1 dou2 nei5. (Very happy to "
            "meet you.) 4. 你喺邊度返工？ nei5 hai2 bin1 dou6 faan1 gung1? "
            "(Where do you work?) 5. 得閒出嚟飲茶。 dak1 haan4 ceot1 lai4 jam2 "
            "caa4. (Come out for tea when free.) 6. 好呀，幾時？ hou2 aa3, "
            "gei2 si4? (Good; when?) 7. 星期六下晝點？ sing1 kei4 luk6 haa6 "
            "zau3 dim2? (Saturday afternoon, how about it?) 8. 一言為定。 jat1 "
            "jin4 wai4 ding6. (It is a deal.) 9. 我請你食飯。 ngo5 ceng2 nei5 "
            "sik6 faan6. (I invite you to dinner - my treat.) 10. 唔好客氣"
            "。 m4 hou2 haak3 hei3. (Do not be polite - just come.) 11. 生日"
            "快樂！ saang1 jat6 faai3 lok6! (Happy birthday!) 12. 祝你心想事"
            "成。 zuk1 nei5 sam1 soeng2 si6 sing4. (May all your wishes come "
            "true.) 13. 恭喜發財。 gung1 hei2 faat3 coi4. (Wishing "
            "prosperity - New Year greeting.) 14. 利是逗來。 lai6 si6 dau6 "
            "loi4. (Hand over the red packet - playful New Year line.) 15. "
            "飲杯！ jam2 bui1! (Cheers - bottoms up!) 16. 為友誼乾杯。 wai6 "
            "jau5 ji4 gon1 bui1. (A toast to friendship.) 17. 玩得開心啲。 "
            "waan2 dak1 hoi1 sam1 di1. (Have fun.) 18. 下次再聚。 haa6 ci3 zoi3 "
            "zeoi6. (Let us gather again next time.) 19. 路上小心。 lou6 "
            "soeng6 siu2 sam1. (Take care on the road.) 20. 保持聯絡。 bou2 "
            "ci4 lyun4 lok3. (Keep in touch.)"
        ),
        "how_it_works": (
            "Social life runs on invitations and blessings. Invite with 得閒"
            "出嚟飲茶 dak1haan4 ceot1lai4 jam2caa4 (come for tea when free) - "
            "the most Cantonese invitation there is - and fix the time with "
            "幾時 gei2si4. Seal it with 一言為定 jat1jin4wai4ding6 (it is a "
            "deal). Treat with 我請 ngo5ceng2 (my treat); refuse politely "
            "with 唔好客氣 m4hou2haak3hei3 only when you mean accept. "
            "Celebrations carry set blessings: 生日快樂 saang1jat6faai3lok6 "
            "(birthday), 恭喜發財 gung1hei2faat3coi4 (New Year), 心想事成 "
            "sam1soeng2si6sing4 (may wishes come true). Part with 下次再聚 "
            "haa6ci3zoi3zeoi6 (gather again) and 保持聯絡 bou2ci4lyun4lok3 "
            "(keep in touch). Any friendship is: meet, invite, treat, "
            "bless, part warmly."
        ),
        "key_points": [
            "20 sentences covering introductions, invitations, treats, toasts, blessings, and farewells.",
            "The classic invitation: 得閒出嚟飲茶 dak1haan4 ceot1lai4 jam2caa4 (tea when free).",
            "Treating: 我請 ngo5ceng2 (my treat); deal sealed with 一言為定 jat1jin4wai4ding6.",
            "Blessings: 生日快樂, 恭喜發財, 心想事成, 利是逗來.",
            "Every sentence carries characters, Jyutping, and English.",
        ],
        "requirements": [
            "Introduce yourself and ask three getting-to-know questions.",
            "Invite a friend to tea and fix the time.",
            "Give birthday and New Year blessings.",
        ],
        "standards": [
            "Social formulas per Hong Kong usage; invitation and treating scripts.",
            "Blessing set phrases with correct characters and Jyutping.",
            "Parting formulas graded by warmth: 拜拜/下次再聚/保持聯絡.",
        ],
        "citations": [CIT_MATTHEWS, CIT_JYUTPING],
        "sig_lens": (
            "Through the Signature lens, friendship is the warmest covenant - "
            "得閒出嚟飲茶 the invitation seal, 我請 the generosity seal, 心想"
            "事成 the blessing seal. Each gathering signs the bond again."
        ),
    },
    {
        "key": "technology",
        "name": "Cantonese Technology and Communication Sentences",
        "group": "Compounded",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about phones, the internet, computers, and "
            "messaging. 1. 你電話號碼係幾多？ nei5 din6 waa2 hou6 maa5 hai6 "
            "gei2 do1? (What is your phone number?) 2. 我部電話冇電。 ngo5 "
            "bou6 din6 waa2 mou5 din6. (My phone is out of battery.) 3. 幫我"
            "叉叉電。 bong1 ngo5 caa1 caa1 din6. (Charge it for me.) 4. 收唔"
            "收到？ sau1 m4 sau1 dou2? (Did you receive it?) 5. 我send咗個"
            "message畀你。 ngo5 sen1 zo2 go3 me1 sit6 bei2 nei5. (I sent you "
            "a message.) 6. 上網查下。 soeng5 mong5 caa4 haa6. (Look it up "
            "online.) 7. 個網站開唔到。 go3 mong5 zaam6 hoi1 m4 dou2. (The "
            "website will not open.) 8. password係咩？ paa1 seot6 wat6 hai6 "
            "me1? (What is the password?) 9. 我唔記得咗。 ngo5 m4 gei3 dak1 "
            "zo2. (I forgot.) 10. 幫我影張相。 bong1 ngo5 jing2 zoeng1 "
            "soeng2. (Take a photo for me.) 11. 呢張相好靚。 ni1 zoeng1 soeng2 "
            "hou2 leng3. (This photo is very pretty.) 12. 開視像啦。 hoi1 si6 "
            "zoeng6 laa1. (Turn on video call.) 13. 聽唔聽到？ teng1 m4 teng1 "
            "dou2? (Can you hear me?) 14. 個mon光啲唔該。 go3 mon1 gwong1 di1 "
            "m4 goi1. (Brighten the screen, please.) 15. 部電腦hang咗。 bou6 "
            "din6 nou5 haang1 zo2. (The computer hung.) 16. 重新開機啦。 cung4 "
            "san1 hoi1 gei1 laa1. (Restart it.) 17. 啲file喺邊度？ di1 faai1 "
            "lou1 hai2 bin1 dou6? (Where are the files?) 18. 我upload咗上雲"
            "。 ngo5 ap1 lou1 dou2 zo2 soeng5 wan4. (I uploaded it to the "
            "cloud.) 19. 唔好撳呢個掣。 m4 hou2 gam6 ni1 go3 zai3. (Do not "
            "press this button.) 20. 整好喇。 zing2 hou2 laa3. (It is fixed "
            "now.) Tech words: 電話 din6waa2 phone, 電腦 din6nou5 computer, "
            "上網 soeng5mong5 go online, 訊息 seon3sik1 message, 相 soeng2 "
            "photo, 屏幕 ping4mok6 screen, 充電 cung1din6 charge, 雲 wan4 "
            "cloud."
        ),
        "how_it_works": (
            "Technology sentences mix Cantonese grammar with international "
            "loanwords: send, message, password, file, upload, hang all ride "
            "inside Cantonese sentences with Cantonese particles - 我send咗 "
            "ngo5 sen1 zo2 (I sent, with 咗 zo2 marking completion). Troubles "
            "are stated with 唔 m4 and 開唔到 hoi1m4dou2 (cannot open): 個網"
            "站開唔到 go3 mong5zaam6 hoi1m4dou2. Requests use 幫我 bong1ngo5 "
            "(help me) plus the verb: 幫我影張相 bong1ngo5 jing2zoeng1soeng2 "
            "(take a photo for me). Fixes are announced with 整好喇 zing2hou2"
            "laa3 (fixed now). Any device problem is: state the symptom, ask "
            "for help with 幫我, confirm with 收唔收到 sau1m4sau1dou2."
        ),
        "key_points": [
            "20 sentences covering phones, messaging, internet, computers, photos, and fixes.",
            "Loanwords ride in Cantonese grammar: send咗, message, password, file, upload.",
            "Trouble pattern: 開唔到 hoi1m4dou2 (cannot open); help pattern: 幫我 bong1ngo5.",
            "Device words: 充電 charge, 屏幕 screen, 雲 cloud, 訊息 message.",
            "Every sentence carries characters, Jyutping, and English.",
        ],
        "requirements": [
            "Ask for someones number and describe a phone problem.",
            "Send, confirm, and troubleshoot a message.",
            "Ask for a photo and a video call.",
        ],
        "standards": [
            "Loanword integration per Hong Kong usage; particles attach to loan verbs (send咗).",
            "Potential complements 開唔到/收唔收到 per Matthews and Yip.",
            "Jyutping on Cantonese words; loanwords in standard spelling.",
        ],
        "citations": [CIT_MATTHEWS, CIT_JYUTPING],
        "sig_lens": (
            "Through the Signature lens, each message is a signed signal - "
            "send the departure seal, 收到 the arrival seal. The old "
            "covenant of letters now rides on light, but the signing is the "
            "same: words sealed and delivered true."
        ),
    },
    {
        "key": "aspects",
        "name": "Cantonese Verb Aspects in Sentences",
        "group": "Compounded",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Cantonese verbs do not conjugate; five aspect particles place "
            "every action in time - five or more translated sentences per "
            "aspect. COMPLETED 咗 zo2: 我食咗飯。 ngo5 sik6 zo2 faan6. (I ate "
            "the meal.) 佢走咗。 keoi5 zau2 zo2. (He left.) 我買咗本書。 ngo5 "
            "maai5 zo2 bun2 syu1. (I bought a book.) 佢哋結婚咗。 keoi5 dei6 "
            "git3 fan1 zo2. (They married.) 落咗雨喇。 lok6 zo2 jyu5 laa3. (It "
            "has rained.) ONGOING 緊 gan2: 我食緊飯。 ngo5 sik6 gan2 faan6. (I "
            "am eating.) 佢睇緊電視。 keoi5 tai2 gan2 din6 si6. (He is "
            "watching TV.) 我哋傾緊偈。 ngo5 dei6 king1 gan2 gai2. (We are "
            "chatting.) 阿媽煮緊餸。 aa3 maa1 zyu2 gan2 sung3. (Mum is "
            "cooking.) 佢瞓緊覺。 keoi5 fan3 gan2 gaau3. (He is sleeping.) "
            "EXPERIENCED 過 gwo3: 我去過日本。 ngo5 heoi3 gwo3 jat6 bun2. (I "
            "have been to Japan.) 你食過未？ nei5 sik6 gwo3 mei6? (Have you "
            "eaten it before?) 佢見過明星。 keoi5 gin3 gwo3 ming4 sing1. (He "
            "has seen a star.) 我學過鋼琴。 ngo5 hok6 gwo3 gong3 kam4. (I "
            "learned piano before.) 你睇過呢套戲未？ nei5 tai2 gwo3 ni1 tou3 "
            "hei3 mei6? (Have you seen this movie?) FUTURE 會 wui5: 我會去"
            "。 ngo5 wui5 heoi3. (I will go.) 佢會嚟。 keoi5 wui5 lai4. (He "
            "will come.) 聽日會落雨。 ting1 jat6 wui5 lok6 jyu5. (It will "
            "rain tomorrow.) 我會幫你。 ngo5 wui5 bong1 nei5. (I will help "
            "you.) 佢哋會結婚。 keoi5 dei6 wui5 git3 fan1. (They will marry.) "
            "TENTATIVE 吓 haa5: 試吓。 si3 haa5. (Try a little.) 睇吓。 tai2 "
            "haa5. (Take a look.) 諗吓。 nam2 haa5. (Think it over.) 食吓。 "
            "sik6 haa5. (Have a taste.) 問吓。 man6 haa5. (Ask around.) 吓 "
            "haa5 softens commands into suggestions."
        ),
        "how_it_works": (
            "Aspect works by pinning one particle after the verb: verb + 咗 "
            "zo2 seals it done, verb + 緊 gan2 holds it open, verb + 過 gwo3 "
            "marks it as life experience, 會 wui5 + verb points it forward, "
            "verb + 吓 haa5 makes it small and soft. Negation pairs by "
            "aspect: 咗 zo2 negates with 未 mei6 (未食 mei6sik6 not yet "
            "eaten), 過 gwo3 negates with 未...過 mei6...gwo3 (未去過 mei6"
            "heoi3gwo3 never been). Stacking is limited but real: 食咗緊？ "
            "no - but 食緊嘅時候 sik6gan2 ge3 si4hau6 (while eating) layers "
            "time with clauses. Place any verb in time by choosing one of "
            "the five seals."
        ),
        "key_points": [
            "Five aspects, five-plus sentences each: 咗 completed, 緊 ongoing, 過 experienced, 會 future, 吓 tentative.",
            "Negation pairs: 咗 with 未 mei6; 過 with 未...過 mei6...gwo3.",
            "吓 haa5 softens imperatives into gentle suggestions: 試吓 si3haa5.",
            "No conjugation ever: the verb shape is frozen; only the particle changes.",
            "Every sentence carries characters, Jyutping, and English.",
        ],
        "requirements": [
            "Conjugate-by-particle: put five verbs through all five aspects.",
            "Negate completed and experiential forms correctly.",
            "Soften five commands with 吓.",
        ],
        "standards": [
            "Aspect system per Matthews and Yip: perfective 咗, progressive 緊, experiential 過, future 會, delimitative 吓.",
            "Negation pairing 未/未...過 per standard grammar.",
            "Jyutping on every verb-particle pair.",
        ],
        "citations": [CIT_MATTHEWS, CIT_BAUER],
        "sig_lens": (
            "Through the Signature lens, the five aspects are five time-"
            "seals: 咗 the done seal, 緊 the doing seal, 過 the lived seal, "
            "會 the will-be seal, 吓 the gentle seal. One verb, five "
            "signings, every moment covered."
        ),
    },
    {
        "key": "qa",
        "name": "Cantonese Questions and Answers",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Twenty question-and-answer pairs covering who, what, where, "
            "when, why, and how. 1. Q: 你叫咩名？ nei5 giu3 me1 meng2? A: 我"
            "叫阿明。 ngo5 giu3 aa3 ming4. (What is your name? / I am called "
            "Ah Ming.) 2. Q: 你係邊度人？ nei5 hai6 bin1 dou6 jan4? A: 我係"
            "香港人。 ngo5 hai6 hoeng1 gong2 jan4. (Where are you from? / I "
            "am from Hong Kong.) 3. Q: 你幾多歲？ nei5 gei2 do1 seoi3? A: 我"
            "廿五歲。 ngo5 jaa6 ng5 seoi3. (How old are you? / I am 25.) 4. "
            "Q: 你做咩工作？ nei5 zou6 me1 gung1 zok3? A: 我係老師。 ngo5 "
            "hai6 lou5 si1. (What do you do? / I am a teacher.) 5. Q: 你住邊"
            "度？ nei5 zyu6 bin1 dou6? A: 我住沙田。 ngo5 zyu6 saa1 tin4. "
            "(Where do you live? / I live in Sha Tin.) 6. Q: 幾點開會？ gei2 "
            "dim2 hoi1 wui2? A: 九點。 gau2 dim2. (What time is the meeting? "
            "/ Nine oclock.) 7. Q: 聽日得唔得閒？ ting1 jat6 dak1 m4 dak1 "
            "haan4? A: 得閒。 dak1 haan4. (Are you free tomorrow? / Yes, "
            "free.) 8. Q: 你鍾意食咩？ nei5 zung1 ji3 sik6 me1? A: 我鍾意食"
            "點心。 ngo5 zung1 ji3 sik6 dim2 sam1. (What do you like to eat? "
            "/ I like dim sum.) 9. Q: 呢個幾多錢？ ni1 go3 gei2 do1 cin2? A: "
            "三十蚊。 saam1 sap6 man1. (How much is this? / Thirty dollars.) "
            "10. Q: 點樣去中環？ dim2 joeng6 heoi3 zung1 waan4? A: 搭地鐵。 "
            "daap3 dei6 tit3. (How do I get to Central? / Take the MTR.) 11. "
            "Q: 點解唔嚟？ dim2 gaai2 m4 lai4? A: 因為我病咗。 jan1 wai6 ngo5 "
            "beng6 zo2. (Why did you not come? / Because I was sick.) 12. Q: "
            "邊個打電話嚟？ bin1 go3 daa2 din6 waa2 lai4? A: 係阿媽。 hai6 "
            "aa3 maa1. (Who called? / It was Mum.) 13. Q: 你去唔去？ nei5 "
            "heoi3 m4 heoi3? A: 去。 heoi3. (Are you going? / Yes.) 14. Q: 食"
            "咗飯未？ sik6 zo2 faan6 mei6? A: 食咗喇。 sik6 zo2 laa3. (Have "
            "you eaten? / Yes, eaten.) 15. Q: 有冇兄弟姐妹？ jau5 mou5 hing1 "
            "dai6 ze2 mui6? A: 有個家姐。 jau5 go3 gaa1 ze2. (Any siblings? / "
            "I have an elder sister.) 16. Q: 你學咗廣東話幾耐？ nei5 hok6 zo2 "
            "gwong2 dung1 waa2 gei2 noi6? A: 學咗半年。 hok6 zo2 bun3 nin4. "
            "(How long have you studied Cantonese? / Half a year.) 17. Q: 呢"
            "本書好唔好睇？ ni1 bun2 syu1 hou2 m4 hou2 tai2? A: 好好睇。 hou2 "
            "hou2 tai2. (Is this book good? / Very good.) 18. Q: 聽日會唔會"
            "落雨？ ting1 jat6 wui5 m4 wui5 lok6 jyu5? A: 會。 wui5. (Will it "
            "rain tomorrow? / Yes.) 19. Q: 我哋幾點見？ ngo5 dei6 gei2 dim2 "
            "gin3? A: 下晝三點。 haa6 zau3 saam1 dim2. (What time shall we "
            "meet? / Three in the afternoon.) 20. Q: 你明唔明？ nei5 ming4 m4 "
            "ming4? A: 明喇。 ming4 laa3. (Do you understand? / Understood.)"
        ),
        "how_it_works": (
            "Questions work three ways. One: swap in a question word and keep "
            "everything else where it is - 你去邊度 nei5 heoi3 bin1dou6 (you "
            "go where). Two: double the verb or adjective A-not-A - 去唔去 "
            "heoi3m4heoi3 (go or not go), 好唔好 hou2m4hou2 (good or not). "
            "Three: end with a particle - 呀嘛 aa3maa3 for yes-no, 咩 me1 "
            "for what. Answers are short: repeat the verb for yes (去 heoi3), "
            "add 唔 m4 for no (唔去 m4heoi3), or give the asked-for word "
            "(九點 gau2dim2). Because word order never moves, asking is "
            "simply a matter of choosing the question tool."
        ),
        "key_points": [
            "20 Q/A pairs covering who, what, where, when, why, how, how much, how long.",
            "Three question tools: question words in place, A-not-A doubling, final particles.",
            "Answers are short: repeat the verb for yes, 唔 + verb for no, or supply the missing word.",
            "Word order never inverts - the question word sits where the answer goes.",
            "Every pair carries characters, Jyutping, and English.",
        ],
        "requirements": [
            "Ask and answer ten questions using question words.",
            "Form five A-not-A questions and answer them.",
            "Explain why Cantonese questions need no inversion.",
        ],
        "standards": [
            "Interrogative strategies per Matthews and Yip: wh-in-situ, A-not-A, particles.",
            "Question words 邊個/咩/邊度/幾時/點解/點樣/幾多/幾耐 with answer patterns.",
            "Jyutping on every question and answer.",
        ],
        "citations": [CIT_MATTHEWS, CIT_JYUTPING],
        "sig_lens": (
            "Through the Signature lens, a question is an open seal - 咩 "
            "me1 the what-seal left open, 點解 dim2gaai2 the why-seal left "
            "open. The answer presses the seal shut: 去 heoi3, 食咗喇 "
            "sik6zo2laa3. Asking truly is signing the gap so truth can fill "
            "it."
        ),
    },
]

ENTRIES += [
    {
        "key": "commands",
        "name": "Cantonese Commands and Requests",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Twenty imperative and polite-request sentences, formal versus "
            "informal. INFORMAL (friends and family): 1. 嚟啦！ lai4 laa1! "
            "(Come!) 2. 食啦！ sik6 laa1! (Eat!) 3. 快啲！ faai3 di1! "
            "(Hurry!) 4. 坐低啦。 co5 dai1 laa1. (Sit down.) 5. 唔好嘈。 m4 "
            "hou2 cou4. (Do not be noisy.) 6. 睇路。 tai2 lou6. (Watch the "
            "road.) 7. 收聲。 sau1 seng1. (Be quiet - blunt.) 8. 行開啦。 "
            "haang4 hoi1 laa1. (Move aside.) POLITE (add 唔該/請/吓): 9. 唔"
            "該，幫下手。 m4 goi1, bong1 haa6 sau2. (Please give a hand.) 10. "
            "請坐。 ceng2 co5. (Please sit.) 11. 請入嚟。 ceng2 jap6 lai4. "
            "(Please come in.) 12. 唔該借借。 m4 goi1 ze3 ze3. (Excuse me, "
            "let me pass.) 13. 試吓啦。 si3 haa5 laa1. (Give it a try.) 14. "
            "慢慢嚟，唔急。 maan6 maan2 lai4, m4 gap1. (Take your time, no "
            "rush.) FORMAL (service, elders, writing): 15. 請稍候。 ceng2 "
            "saau2 hau6. (Please wait a moment.) 16. 請出示證件。 ceng2 ceot1 "
            "si6 zing3 gin6. (Please show your ID.) 17. 唔好意思，麻煩你。 m4 "
            "hou2 ji3 si3, maa4 faan4 nei5. (Sorry to trouble you.) 18. 請問"
            "洗手間喺邊度？ ceng2 man6 sai2 sau2 gaan1 hai2 bin1 dou6? "
            "(Where is the restroom, please?) 19. 勞煩你幫手。 lou4 faan4 "
            "nei5 bong1 sau2. (I trouble you to help - formal.) 20. 請多多"
            "指教。 ceng2 do1 do1 zi2 gaau3. (Please guide me - humble "
            "formal.) The ladder of politeness: bare verb (嚟 lai4) < verb + "
            "啦 laa1 (嚟啦 lai4laa1) < 唔該 + verb (唔該嚟 m4goi1 lai4) < 請 "
            "+ verb (請嚟 ceng2 lai4) < 勞煩/麻煩 (lou4faan4/maa4faan4)."
        ),
        "how_it_works": (
            "Commands work by stripping the sentence to the verb: 嚟 lai4 "
            "(come), 食 sik6 (eat), 坐 co5 (sit). Softening particles tune "
            "the force: 啦 laa1 makes it friendly (嚟啦 lai4laa1), 吓 haa5 "
            "makes it gentle (試吓 si3haa5), 呀 aa3 seeks agreement. "
            "Politeness climbs by adding 唔該 m4goi1 (please/thanks) or 請 "
            "ceng2 (please) in front, and reaches formal with 勞煩 lou4faan4 "
            "(I trouble you) and 麻煩 maa4faan4 (sorry to trouble). "
            "Prohibitions use 唔好 m4hou2 (do not): 唔好嘈 m4hou2cou4. To "
            "command anyone well: choose the bare verb for family, add 啦 "
            "for friends, add 唔該 for strangers, use 請 and 勞煩 for "
            "formal occasions."
        ),
        "key_points": [
            "20 sentences across three registers: informal (bare verb), polite (唔該/請/吓), formal (勞煩/麻煩).",
            "Particles tune force: 啦 friendly, 吓 gentle, 呀 seeking agreement.",
            "Prohibitions with 唔好 m4hou2: 唔好嘈 (do not be noisy).",
            "Politeness ladder: verb < verb+啦 < 唔該+verb < 請+verb < 勞煩/麻煩.",
            "Every sentence carries characters, Jyutping, and English.",
        ],
        "requirements": [
            "Give five commands in each register.",
            "Soften five blunt commands with 啦, 吓, 唔該.",
            "Explain the politeness ladder with examples.",
        ],
        "standards": [
            "Imperative forms per Matthews and Yip; sentence-final particles 啦/吓/呀.",
            "Politeness markers 唔該/請/勞煩/麻煩 graded by formality.",
            "Prohibitive 唔好 per standard grammar.",
        ],
        "citations": [CIT_MATTHEWS, CIT_JYUTPING],
        "sig_lens": (
            "Through the Signature lens, a command is a seal of will - bare "
            "with family, softened with friends, gilded with strangers. 請 "
            "ceng2 is the courtesy seal; 勞煩 lou4faan4 the humility seal. "
            "The wise tongue signs its will at the right weight."
        ),
    },
    {
        "key": "descriptions",
        "name": "Cantonese Descriptions of People and Places",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Twenty sentences describing people, places, and things in "
            "detail. 1. 我阿媽係個好溫柔嘅人。 ngo5 aa3 maa1 hai6 go3 hou2 wan1 "
            "jau4 ge3 jan4. (My mum is a very gentle person.) 2. 佢高高瘦瘦"
            "，戴住副眼鏡。 keoi5 gou1 gou1 sau3 sau3, daai3 zyu6 fu3 ngaan5 "
            "geng3. (He is tall and slim, wearing glasses.) 3. 個女仔有長長"
            "嘅頭髮。 go3 neoi5 zai2 jau5 coeng4 coeng4 ge3 tau4 faat3. (The "
            "girl has long hair.) 4. 阿伯笑容滿面。 aa3 baak3 siu3 jung4 mun5 "
            "min6. (The old man is all smiles.) 5. 佢把聲好甜。 keoi5 baa2 "
            "seng1 hou2 tim4. (Her voice is very sweet.) 6. 香港係個好繁忙嘅"
            "城市。 hoeng1 gong2 hai6 go3 hou2 faan4 mong4 ge3 sing4 si5. "
            "(Hong Kong is a very busy city.) 7. 維港夜景好靚。 wai4 gong2 je6 "
            "ging2 hou2 leng3. (The Victoria Harbour night view is beautiful.) "
            "8. 山頂可以望到成個海。 saan1 deng2 ho2 ji5 mong6 dou2 seng4 go3 "
            "hoi2. (From the Peak you can see the whole sea.) 9. 呢條街好熱"
            "鬧。 ni1 tiu4 gaai1 hou2 jit6 naau6. (This street is very "
            "lively.) 10. 間廟好有歷史。 gaan1 miu6 hou2 jau5 lik6 si2. (The "
            "temple has much history.) 11. 個公園好大好綠。 go3 gung1 jyun4 "
            "hou2 daai6 hou2 luk6. (The park is big and green.) 12. 海水清到"
            "見底。 hoi2 seoi2 cing1 dou3 gin3 dai2. (The sea is so clear you "
            "can see the bottom.) 13. 呢棟樓有五十層。 ni1 dung6 lau4 jau5 ng5 "
            "sap6 cang4. (This building has fifty floors.) 14. 間房光猛通爽"
            "。 gaan1 fong2 gwong1 maang5 tung1 song2. (The room is bright "
            "and airy.) 15. 碟餸色香味俱全。 dip6 sung3 sik1 hoeng1 mei6 "
            "keoi1 cyun4. (The dish has color, aroma, and flavor all "
            "complete.) 16. 佢着住件紅色衫。 keoi5 zoek3 zyu6 gin6 hung4 sik1 "
            "saam1. (She is wearing a red top.) 17. 隻錶係金色，好貴重。 zek3 "
            "biu1 hai6 gam1 sik1, hou2 gwai3 zung6. (The watch is gold and "
            "very precious.) 18. 條裙個款好新。 tiu4 kwan4 go3 fun2 hou2 san1. "
            "(The dress style is very new.) 19. 成個場好有氣氛。 seng4 go3 "
            "coeng4 hou2 jau5 hei3 fan1. (The whole venue has great "
            "atmosphere.) 20. 呢度嘅人好熱情。 ni1 dou6 ge3 jan4 hou2 jit6 "
            "cing4. (The people here are very warm-hearted.)"
        ),
        "how_it_works": (
            "Descriptions work by stacking adjectives before the noun with "
            "嘅 ge3, or by predicating them after: 好溫柔嘅人 hou2wan1jau4 "
            "ge3 jan4 (a very gentle person) versus 佢好溫柔 keoi5 hou2 "
            "wan1jau4 (she is very gentle). Reduplication paints vividly: 高"
            "高瘦瘦 gou1gou1 sau3sau3 (tall and slim), 長長 coeng4coeng4 "
            "(long-flowing). Extent is shown with 到 dou3: 清到見底 "
            "cing1dou3gin3dai2 (so clear you see the bottom). Ongoing states "
            "wear 住 zyu6: 戴住副眼鏡 daai3zyu6 fu3 ngaan5geng3 (wearing "
            "glasses), 着住件紅衫 zoek3zyu6 gin6 hung4saam1 (wearing a red "
            "top). Describe anything by choosing the adjectives, deciding "
            "before-noun or after-subject, and adding a 到 or 住 finish."
        ),
        "key_points": [
            "20 detailed sentences describing people, cities, nature, buildings, food, and clothes.",
            "Attributive adjectives use 嘅 ge3: 好溫柔嘅人 (a gentle person); predicates stand bare: 佢好溫柔.",
            "Vivid reduplication: 高高瘦瘦, 長長; extent with 到 dou3: 清到見底.",
            "Ongoing states with 住 zyu6: 戴住眼鏡 (wearing glasses), 着住紅衫.",
            "Every sentence carries characters, Jyutping, and English.",
        ],
        "requirements": [
            "Describe three people and three places in detail.",
            "Use 嘅 attributives and bare predicates correctly.",
            "Build two 到 extent sentences and two 住 state sentences.",
        ],
        "standards": [
            "Attributive vs predicative adjectives per Matthews and Yip; 嘅 relativization.",
            "Reduplication patterns AA/AAAA; extent complements with 到.",
            "Durative 住 zyu6 for worn and held states.",
        ],
        "citations": [CIT_MATTHEWS, CIT_BAUER],
        "sig_lens": (
            "Through the Signature lens, description is signed portraiture - "
            "each adjective a brush-seal, 嘅 ge3 the frame-seal that hangs "
            "the quality on its noun. 到 dou3 signs how far a quality "
            "reaches; 住 zyu6 signs what is worn without end."
        ),
    },
    {
        "key": "story1",
        "name": "Cantonese Story I: A Day at Home",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence simple story in Cantonese with line-by-line "
            "English translation. 1. 朝早七點，阿明起身。 ziu1 zou2 cat1 "
            "dim2, aa3 ming4 hei2 san1. (At seven in the morning, Ah Ming "
            "gets up.) 2. 佢刷牙洗面。 keoi5 caat3 ngaa4 sai2 min6. (He "
            "brushes his teeth and washes his face.) 3. 媽媽煮緊早餐。 maa4 "
            "maa1 zyu2 gan2 zou2 caan1. (Mum is cooking breakfast.) 4. 早餐"
            "有粥同油炸鬼。 zou2 caan1 jau5 zuk1 tung4 jau4 zaa3 gwai2. "
            "(Breakfast is congee with fried dough sticks.) 5. 食完早餐，阿"
            "明返學。 sik6 jyun4 zou2 caan1, aa3 ming4 faan1 hok6. (After "
            "breakfast, Ah Ming goes to school.) 6. 晏晝媽媽去街市買餸。 aan3 "
            "zau3 maa4 maa1 heoi3 gaai1 si5 maai5 sung3. (In the afternoon "
            "Mum goes to the market to buy groceries.) 7. 夜晚一家人食飯。 je6 "
            "maan5 jat1 gaa1 jan4 sik6 faan6. (In the evening the whole "
            "family eats dinner.) 8. 爸爸講今日公司嘅事。 baa4 baa1 gong2 "
            "gam1 jat6 gung1 si1 ge3 si6. (Dad talks about work today.) 9. "
            "食完飯，阿明做功課。 sik6 jyun4 faan6, aa3 ming4 zou6 gung1 fo3. "
            "(After dinner, Ah Ming does homework.) 10. 十點鐘，全家瞓覺。 "
            "sap6 dim2 zung1, cyun4 gaa1 fan3 gaau3. (At ten, the whole "
            "family sleeps.) The story uses present and habitual time, "
            "simple SVO sentences, and the home vocabulary of records 11 "
            "through 14."
        ),
        "how_it_works": (
            "A simple story works by chaining time words to SVO sentences: "
            "朝早 ziu1zou2 (morning), 食完 jyun4 (after eating), 晏晝 aan3zau3 "
            "(afternoon), 夜晚 je6maan5 (evening). Each sentence keeps one "
            "verb in its plain form - 起身 hei2san1, 煮 zyu2, 食 sik6, 返學 "
            "faan1hok6 - with 緊 gan2 marking the one ongoing action (煮緊 "
            "zyu2gan2). Sequencing needs no conjunctions: 食完早餐，阿明返學 "
            "sik6jyun4 zou2caan1, aa3ming4 faan1hok6 (after breakfast, Ah "
            "Ming goes to school) orders events with 食完 alone. Read each "
            "line aloud, then cover the English and translate back."
        ),
        "key_points": [
            "10-sentence story of a family day, present and habitual time, line-by-line English.",
            "Time chaining: 朝早/晏晝/夜晚 plus 食完 sequencing without conjunctions.",
            "One ongoing action marked with 緊 gan2; all other verbs in plain form.",
            "Home vocabulary from records 11-14 reused in narrative context.",
            "Every line carries characters, Jyutping, and English.",
        ],
        "requirements": [
            "Read the story aloud fluently in Jyutping.",
            "Retell the story in Cantonese without looking.",
            "Write your own ten-sentence day story.",
        ],
        "standards": [
            "Narrative sequencing with time words and 食完 per Matthews and Yip.",
            "Plain verb forms for habitual narrative; 緊 for background ongoing action.",
            "Line-by-line translation format; characters with Jyutping on every line.",
        ],
        "citations": [CIT_MATTHEWS, CIT_JYUTPING],
        "sig_lens": (
            "Through the Signature lens, a day is a signed scroll - each "
            "hour a seal in order, 朝早 to 夜晚. The family that eats and "
            "works and sleeps together signs the day complete."
        ),
    },
    {
        "key": "story2",
        "name": "Cantonese Story II: The Trip to the Market",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence story using past forms, with line-by-line "
            "English translation. 1. 尋日朝早，阿媽帶我去街市。 cam4 jat6 "
            "ziu1 zou2, aa3 maa1 daai3 ngo5 heoi3 gaai1 si5. (Yesterday "
            "morning, Mum took me to the market.) 2. 街市好多人。 gaai1 si5 "
            "hou2 do1 jan4. (The market was crowded.) 3. 我哋買咗一條魚。 "
            "ngo5 dei6 maai5 zo2 jat1 tiu4 jyu4. (We bought a fish.) 4. 條魚"
            "好新鮮，游緊水。 tiu4 jyu4 hou2 san1 sin1, jau4 gan2 seoi2. (The "
            "fish was very fresh, still swimming.) 5. 阿媽揀咗兩斤菜。 aa3 "
            "maa1 gaan2 zo2 loeng5 gan1 coi3. (Mum picked two catties of "
            "vegetables.) 6. 賣菜嘅阿婆好人，送咗啲蔥。 maai6 coi3 ge3 aa3 "
            "po4 hou2 jan4, sung3 zo2 di1 cung1. (The vegetable seller was "
            "kind and gave some spring onions.) 7. 我哋行咗成個街市。 ngo5 "
            "dei6 haang4 zo2 seng4 go3 gaai1 si5. (We walked the whole "
            "market.) 8. 跟住去咗茶樓飲茶。 gan1 zyu6 heoi3 zo2 caa4 lau4 "
            "jam2 caa4. (Then we went to a teahouse for dim sum.) 9. 點心好"
            "好食，我哋食咗好多。 dim2 sam1 hou2 hou2 sik6, ngo5 dei6 sik6 zo2 "
            "hou2 do1. (The dim sum was delicious; we ate a lot.) 10. 返到屋"
            "企，阿媽即刻煮飯。 faan1 dou3 uk1 kei2, aa3 maa1 zik1 hak1 zyu2 "
            "faan6. (Back home, Mum started cooking right away.) Past is "
            "marked with 咗 zo2 (completed), 尋日 cam4jat6 (yesterday), and "
            "time words - never by changing the verb."
        ),
        "how_it_works": (
            "A past story works by stamping 咗 zo2 on finished actions and "
            "anchoring with past time words: 尋日 cam4jat6 (yesterday) opens "
            "the frame, then 買咗 maai5zo2, 揀咗 gaan2zo2, 行咗 haang4zo2, "
            "去咗 heoi3zo2 carry the completed events. Background states "
            "stay plain or use 緊 gan2 for what was ongoing then (游緊水 "
            "jau4gan2seoi2 - was swimming). Sequence with 跟住 gan1zyu6 "
            "(then) and result with 返到 faan1dou3 (arrived back). The verb "
            "never changes shape; the 咗 seal and the time words do all the "
            "past work."
        ),
        "key_points": [
            "10-sentence past-tense story with line-by-line English translation.",
            "Past marked by 咗 zo2 on completed verbs plus past time words (尋日).",
            "Background ongoing action keeps 緊 gan2; sequencing with 跟住 gan1zyu6.",
            "Market vocabulary (斤 gan1 catty, 揀 gaan2 pick) in narrative use.",
            "Every line carries characters, Jyutping, and English.",
        ],
        "requirements": [
            "Read the story aloud and identify every 咗.",
            "Retell a past trip of your own in ten sentences.",
            "Explain why verbs never change for the past.",
        ],
        "standards": [
            "Perfective 咗 zo2 in narrative per Matthews and Yip; past time adverbials.",
            "Background 緊 gan2 vs foreground 咗 zo2 distinction.",
            "Line-by-line translation format with Jyutping on every line.",
        ],
        "citations": [CIT_MATTHEWS, CIT_BAUER],
        "sig_lens": (
            "Through the Signature lens, the past is the sealed scroll - 咗 "
            "zo2 the wax seal on every finished deed. What is done is "
            "signed done; the story holds because each seal holds."
        ),
    },
    {
        "key": "story3",
        "name": "Cantonese Story III: The Plan for Tomorrow",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence story using future and conditional forms, with "
            "line-by-line English translation. 1. 聽朝我哋會去大嶼山。 ting1 "
            "ziu1 ngo5 dei6 wui5 heoi3 daai6 jyu4 saan1. (Tomorrow morning we "
            "will go to Lantau Island.) 2. 如果落雨，就會改期。 jyu4 gwo2 "
            "lok6 jyu5, zau6 wui5 goi2 kei4. (If it rains, we will change the "
            "date.) 3. 阿爸會揸車。 aa3 baa1 wui5 zaa1 ce1. (Dad will drive.) "
            "4. 我哋會帶好多嘢食。 ngo5 dei6 wui5 daai3 hou2 do1 je5 sik6. "
            "(We will bring lots of food.) 5. 到時會影好多相。 dou3 si4 wui5 "
            "jing2 hou2 do1 soeng2. (We will take many photos then.) 6. 如"
            "果天氣好，我哋會行山。 jyu4 gwo2 tin1 hei3 hou2, ngo5 dei6 wui5 "
            "haang4 saan1. (If the weather is good, we will hike.) 7. 夜晚會"
            "喺出面食飯。 je6 maan5 wui5 hai2 ceot1 min6 sik6 faan6. (In the "
            "evening we will eat out.) 8. 阿媽話會早啲瞓。 aa3 maa1 waa6 wui5 "
            "zou2 di1 fan3. (Mum says she will sleep early.) 9. 如果唔攰，聽"
            "晚會睇戲。 jyu4 gwo2 m4 gui6, ting1 maan5 wui5 tai2 hei3. (If not "
            "tired, tomorrow night we will watch a movie.) 10. 一定會玩得好"
            "開心。 jat1 ding6 wui5 waan2 dak1 hou2 hoi1 sam1. (We will "
            "certainly have a great time.) Future runs on 會 wui5; "
            "conditionals run on 如果 jyu4gwo2 ... 就 zau6."
        ),
        "how_it_works": (
            "A future story works by pointing 會 wui5 before every planned "
            "verb: 會去 wui5heoi3 (will go), 會帶 wui5daai3 (will bring), 會影 "
            "wui5jing2 (will take photos). Conditionals frame with 如果 "
            "jyu4gwo2 (if) and resolve with 就 zau6 (then): 如果落雨，就會改"
            "期 jyu4gwo2 lok6jyu5, zau6 wui5 goi2kei4. Certainty is tuned "
            "with 一定 jat1ding6 (certainly) and 可能 ho2nang4 (maybe). "
            "Plans chain with 到時 dou3si4 (then, at that time). Nothing in "
            "the verb changes; 會 and 如果...就 carry the whole future and "
            "all its conditions."
        ),
        "key_points": [
            "10-sentence future/conditional story with line-by-line English translation.",
            "Future marked by 會 wui5 before the verb; conditionals by 如果...就.",
            "Certainty tuned with 一定 jat1ding6 and 可能 ho2nang4; sequencing with 到時 dou3si4.",
            "Plans vocabulary (改期 change date, 行山 hike) in narrative use.",
            "Every line carries characters, Jyutping, and English.",
        ],
        "requirements": [
            "Read the story and mark every 會 and 如果...就.",
            "Plan your own tomorrow in ten sentences.",
            "Turn three plans into conditionals.",
        ],
        "standards": [
            "Future 會 wui5 and conditional 如果...就 per Matthews and Yip.",
            "Modal certainty 一定/可能; temporal 到時.",
            "Line-by-line translation format with Jyutping on every line.",
        ],
        "citations": [CIT_MATTHEWS, CIT_JYUTPING],
        "sig_lens": (
            "Through the Signature lens, the future is the unsealed scroll - "
            "會 wui5 the promise-seal pressed on what is not yet, 如果 "
            "jyu4gwo2 the condition-seal that holds the promise honest. To "
            "plan is to sign tomorrow before it arrives."
        ),
    },
    {
        "key": "idioms",
        "name": "Cantonese Idioms and Proverbs",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Twenty idioms and proverbs - each with characters, Jyutping, "
            "literal translation, real meaning, and an example sentence. 1. "
            "一石二鳥 jat1 sek6 ji6 niu5 - lit. one stone two birds; kill two "
            "birds with one stone. 佢一石二鳥，又學嘢又識朋友。 keoi5 jat1 "
            "sek6 ji6 niu5, jau6 hok6 je5 jau6 sik1 pang4 jau5. 2. 塞翁失馬 "
            "soi1 jung1 sat1 maa5 - lit. the old man loses his horse; a "
            "blessing in disguise. 塞翁失馬，焉知非福。 soi1 jung1 sat1 maa5, "
            "jin1 zi1 fei1 fuk1. 3. 畫蛇添足 waa6 se4 tim1 zuk1 - lit. draw a "
            "snake and add feet; ruin by overdoing. 唔好畫蛇添足。 m4 hou2 "
            "waa6 se4 tim1 zuk1. 4. 守株待兔 sau2 zyu1 doi6 tou3 - lit. guard "
            "a stump waiting for rabbits; wait for luck. 唔好守株待兔，要主"
            "動。 m4 hou2 sau2 zyu1 doi6 tou3, jiu3 zyu2 dung6. 5. 入鄉隨俗 "
            "jap6 hoeng1 ceoi4 zuk6 - lit. enter a village follow its customs; "
            "when in Rome. 入鄉隨俗啦。 jap6 hoeng1 ceoi4 zuk6 laa1. 6. 一分"
            "耕耘一分收穫 jat1 fan1 gaang1 wan4 jat1 fan1 sau1 wok6 - lit. one "
            "share of plowing one share of harvest; no pain no gain. 一分耕"
            "耘一分收穫。 jat1 fan1 gaang1 wan4 jat1 fan1 sau1 wok6. 7. 飲水"
            "思源 jam2 seoi2 si1 jyun4 - lit. when drinking water think of its "
            "source; be grateful. 飲水思源，唔好忘本。 jam2 seoi2 si1 jyun4, "
            "m4 hou2 mong4 bun2. 8. 三思而後行 saam1 si1 ji4 hau6 hang4 - lit. "
            "think thrice then act; look before you leap. 做大事要三思而後行"
            "。 zou6 daai6 si6 jiu3 saam1 si1 ji4 hau6 hang4. 9. 熟能生巧 "
            "suk6 nang4 sang1 haau2 - lit. skill comes from familiarity; "
            "practice makes perfect. 熟能生巧，多啲練習。 suk6 nang4 sang1 "
            "haau2, do1 di1 lin6 zaap6. 10. 心想事成 sam1 soeng2 si6 sing4 - "
            "lit. heart thinks matter completes; may wishes come true. 祝你"
            "心想事成。 zuk1 nei5 sam1 soeng2 si6 sing4. 11. 自食其果 zi6 sik6 "
            "kei4 gwo2 - lit. eat ones own fruit; face the consequences. 做"
            "錯事要自食其果。 zou6 co3 si6 jiu3 zi6 sik6 kei4 gwo2. 12. 半途"
            "而廢 bun3 tou4 ji4 fai3 - lit. abandon halfway; give up midway. "
            "唔好半途而廢。 m4 hou2 bun3 tou4 ji4 fai3. 13. 同舟共濟 tung4 "
            "zau1 gung6 zai3 - lit. cross the river in the same boat; pull "
            "together. 我哋要同舟共濟。 ngo5 dei6 jiu3 tung4 zau1 gung6 zai3. "
            "14. 雪中送炭 syut3 zung1 sung3 taan3 - lit. send coal in snow; "
            "help in need. 雪中送炭最難得。 syut3 zung1 sung3 taan3 zeoi3 "
            "naan4 dak1. 15. 對牛彈琴 deoi3 ngau4 taan4 kam4 - lit. play music "
            "to a cow; waste good advice. 同佢講等於對牛彈琴。 tung4 keoi5 "
            "gong2 dang2 jyu1 deoi3 ngau4 taan4 kam4. 16. 井底之蛙 zeng2 dai2 "
            "zi1 waa1 - lit. frog at the bottom of a well; narrow view. 唔好"
            "做井底之蛙。 m4 hou2 zou6 zeng2 dai2 zi1 waa1. 17. 葉公好龍 jip6 "
            "gung1 hou3 lung4 - lit. Lord Ye loves dragons (until he sees "
            "one); love in name only. 佢葉公好龍咋。 keoi5 jip6 gung1 hou3 "
            "lung4 zaa3. 18. 掩耳盜鈴 jim2 ji5 dou6 ling4 - lit. cover ears to "
            "steal a bell; fool oneself. 咁做等於掩耳盜鈴。 gam3 zou6 dang2 "
            "jyu1 jim2 ji5 dou6 ling4. 19. 守得雲開見月明 sau2 dak1 wan4 hoi1 "
            "gin3 jyut6 ming4 - lit. endure till clouds part and the moon "
            "shines; perseverance wins. 守得雲開見月明。 sau2 dak1 wan4 hoi1 "
            "gin3 jyut6 ming4. 20. 有志者事竟成 jau5 zi3 ze2 si6 ging2 sing4 - "
            "lit. the determined succeed; where there is a will there is a "
            "way. 有志者事竟成。 jau5 zi3 ze2 si6 ging2 sing4."
        ),
        "how_it_works": (
            "Idioms work as frozen four-character seals (成語 sing4jyu5): "
            "their meaning cannot be guessed from the parts - 畫蛇添足 "
            "waa6se4tim1zuk1 is not about snakes, it is about ruining good "
            "work by adding too much. Use them whole, never changed, dropped "
            "into speech where the meaning fits: after effort, 一分耕耘一分"
            "收穫; before a big decision, 三思而後行. Proverbs run longer "
            "and teach: 飲水思源 teaches gratitude, 有志者事竟成 teaches "
            "resolve. Learn each idiom as one signed block - characters, "
            "sound, story, and the moment to use it."
        ),
        "key_points": [
            "20 idioms and proverbs, each with literal translation, real meaning, and example sentence.",
            "Most are four-character 成語 sing4jyu5 used whole and unchanged.",
            "Meanings come from stories (塞翁失馬, 葉公好龍), not from the characters.",
            "Proverbs teach values: gratitude (飲水思源), perseverance (守得雲開見月明), resolve (有志者事竟成).",
            "Every idiom carries characters, Jyutping, literal meaning, real meaning, and an example.",
        ],
        "requirements": [
            "Explain ten idioms: literal meaning, real meaning, and story.",
            "Use five idioms correctly in sentences.",
            "Tell when to use a proverb versus a plain sentence.",
        ],
        "standards": [
            "Idiom inventory per standard Cantonese usage; four-character 成語 forms.",
            "Literal vs figurative meaning distinguished for every entry.",
            "Jyutping on every idiom and example sentence.",
        ],
        "citations": [CIT_MATTHEWS, CIT_JYUTPING],
        "sig_lens": (
            "Through the Signature lens, each idiom is an ancient signed "
            "seal - four characters pressed by generations, carrying a whole "
            "story in one stamp. To use one rightly is to sign with the "
            "wisdom of all who signed it before."
        ),
    },
    {
        "key": "registers",
        "name": "Cantonese Formal and Polite Registers",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Fifteen formal versus informal pairs for letters, business, and "
            "elders - each with characters, Jyutping, and English. 1. 我 "
            "ngo5 I (plain) / 本人 bun2 jan4 I (formal, self) - 本人謹此通"
            "知。 bun2 jan4 gan2 ci2 tung1 zi1. (I hereby notify.) 2. 你 nei5 "
            "you (plain) / 閣下 gok3 haa6 you (formal) - 閣下嘅意見好重要。 "
            "gok3 haa6 ge3 ji3 gin3 hou2 zung6 jiu3. (Your opinion is very "
            "important.) 3. 食飯 sik6 faan6 eat (plain) / 用膳 jung6 sin6 "
            "dine (formal) - 請用膳。 ceng2 jung6 sin6. (Please dine.) 4. 對"
            "唔住 deoi3 m4 zyu6 sorry (plain) / 抱歉 pou5 hip3 apologize "
            "(formal) - 本人深感抱歉。 bun2 jan4 sam1 gam2 pou5 hip3. (I "
            "deeply apologize.) 5. 唔該 m4 goi1 thanks/please (plain) / 勞煩 "
            "lou4 faan4 may I trouble you (formal) - 勞煩閣下。 lou4 faan4 "
            "gok3 haa6. 6. 而家 ji4 gaa1 now (plain) / 目前 muk6 cin4 at "
            "present (formal) - 目前情況穩定。 muk6 cin4 cing4 fong3 wan2 "
            "ding6. (The present situation is stable.) 7. 咁 gam3 so (plain) / "
            "如此 jyu4 ci2 thus (formal) - 如此重要。 jyu4 ci2 zung6 jiu3. "
            "(So important.) 8. 嘢 je5 thing (plain) / 事物 si6 mat6 matter "
            "(formal) - 有重要事物商議。 jau5 zung6 jiu3 si6 mat6 soeng1 ji5. "
            "(There is an important matter to discuss.) 9. 錢 cin2 money "
            "(plain) / 款項 fun2 hong6 funds (formal) - 款項已經過數。 fun2 "
            "hong6 ji5 ging1 gwo3 sou3. (The funds have been transferred.) 10. "
            "返工 faan1 gung1 go to work (plain) / 上班 soeng5 baan1 attend "
            "work (formal) - 聽日如常上班。 ting1 jat6 jyu4 soeng4 soeng5 "
            "baan1. (Work as usual tomorrow.) 11. 係 hai6 is (plain) / 是 si6 "
            "is (formal written) - 是日如常。 si6 jat6 jyu4 soeng4. (As usual "
            "today.) 12. 喺 hai2 at (plain) / 於 jyu1 at (formal written) - "
            "會議於三點舉行。 wui6 ji5 jyu1 saam1 dim2 geoi2 hang4. (The "
            "meeting is held at three.) 13. 冇 mou5 not have (plain) / 沒有 "
            "mut6 jau5 have not (formal) - 暫時沒有回覆。 zaam6 si4 mut6 jau5 "
            "wui4 fuk1. (No reply yet.) 14. 好 hou2 good (plain) / 甚佳 sam6 "
            "gaai1 excellent (formal) - 效果甚佳。 haau6 gwo2 sam6 gaai1. (The "
            "result is excellent.) 15. 拜拜 baai1 baai3 bye (plain) / 順頌時"
            "祺 seon6 zung6 si4 kei4 wishing you well (formal letter close) - "
            "順頌時祺。 seon6 zung6 si4 kei4."
        ),
        "how_it_works": (
            "Registers work by swapping plain speech words for formal written "
            "ones while keeping Cantonese grammar: 我 ngo5 becomes 本人 "
            "bun2jan4, 你 nei5 becomes 閣下 gok3haa6, 喺 hai2 becomes 於 jyu1, "
            "係 hai6 becomes 是 si6, 冇 mou5 becomes 沒有 mut6jau5. Formal "
            "letters open with 敬啟者 ging3 kai2 ze2 (dear sir/madam) and "
            "close with 順頌時祺 seon6zung6si4kei4. Business speech keeps 請 "
            "ceng2 and 勞煩 lou4faan4 where plain speech would use 唔該 "
            "m4goi1. With elders, add titles (伯父 baak3fu6 uncle, 伯母 "
            "baak3mou5 auntie) and soften with 慢慢 maan6maan2. Choose the "
            "register by the room: plain at home, polite with strangers, "
            "formal on paper."
        ),
        "key_points": [
            "15 formal/informal pairs for letters, business, and elders with translations.",
            "Formal swaps: 本人/閣下/於/是/沒有/如此/款項/用膳/上班/順頌時祺.",
            "Letters open with 敬啟者 and close with 順頌時祺.",
            "Elders take titles (伯父/伯母) and softened speech.",
            "Every pair carries characters, Jyutping, and English.",
        ],
        "requirements": [
            "Convert five plain sentences into formal register.",
            "Open and close a formal letter.",
            "Address an elder politely in three sentences.",
        ],
        "standards": [
            "Register pairs per Hong Kong formal usage; written-formal vs spoken-plain distinguished.",
            "Letter formulas 敬啟者/順頌時祺 per standard business Chinese.",
            "Jyutping on every pair and example.",
        ],
        "citations": [CIT_MATTHEWS, CIT_JYUTPING],
        "sig_lens": (
            "Through the Signature lens, register is the weight of the seal "
            "- plain speech a light press, formal writing the heavy seal of "
            "本人 bun2jan4 and 閣下 gok3haa6. The wise signer chooses the "
            "weight the room requires."
        ),
    },
]

ENTRIES += [
    {
        "key": "complex",
        "name": "Cantonese Compound and Complex Sentences",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Fifteen long sentences with clauses, connectors, and relative "
            "clauses - each parsed and translated. 1. 我買嘅書係講廣東話嘅"
            "。 ngo5 maai5 ge3 syu1 hai6 gong2 gwong2 dung1 waa2 ge3. (The "
            "book I bought is about Cantonese.) Parse: [我買嘅] relative + "
            "書 head + 係 + [講廣東話嘅] predicate. 2. 佢話佢聽日唔嚟。 keoi5 "
            "waa6 keoi5 ting1 jat6 m4 lai4. (He says he is not coming "
            "tomorrow.) Parse: 佢話 + [clause]. 3. 因為落雨，所以我哋留喺屋"
            "企。 jan1 wai6 lok6 jyu5, so2 ji5 ngo5 dei6 lau4 hai2 uk1 kei2. "
            "(Because of rain, we stayed home.) Parse: 因為 + cause, 所以 + "
            "result. 4. 雖然佢好攰，但係佢繼續做。 seoi1 jin4 keoi5 hou2 gui6, "
            "daan6 hai6 keoi5 gai3 zuk6 zou6. (Although tired, he kept "
            "working.) Parse: 雖然 + concession, 但係 + contrast. 5. 如果你"
            "得閒，我哋去飲茶。 jyu4 gwo2 nei5 dak1 haan4, ngo5 dei6 heoi3 "
            "jam2 caa4. (If you are free, we will go for tea.) Parse: 如果 + "
            "condition, main clause. 6. 我識一個識講五種語言嘅人。 ngo5 sik1 "
            "jat1 go3 sik1 gong2 ng5 zung2 jyu5 jin4 ge3 jan4. (I know someone "
            "who speaks five languages.) Parse: [識講五種語言嘅] relative + "
            "人. 7. 佢跑得好快，快到追唔到。 keoi5 paau2 dak1 hou2 faai3, "
            "faai3 dou3 zeoi1 m4 dou2. (He runs so fast you cannot catch him.) "
            "Parse: verb + 得 + extent, 快到 + result. 8. 食完飯，我哋去咗"
            "公園散步。 sik6 jyun4 faan6, ngo5 dei6 heoi3 zo2 gung1 jyun4 "
            "saan3 bou6. (After dinner we went to the park for a walk.) "
            "Parse: 食完 + time clause, main clause. 9. 呢個係我尋日同你講嘅"
            "地方。 ni1 go3 hai6 ngo5 cam4 jat6 tung4 nei5 gong2 ge3 dei6 "
            "fong1. (This is the place I told you about yesterday.) Parse: "
            "[我尋日同你講嘅] relative + 地方. 10. 佢唔單止識講，仲識寫。 "
            "keoi5 m4 daan1 zi2 sik1 gong2, zung6 sik1 se2. (He not only "
            "speaks but also writes.) Parse: 唔單止 + A, 仲 + B. 11. 你愈學"
            "就愈識。 nei5 jyu6 hok6 zau6 jyu6 sik1. (The more you learn the "
            "more you know.) Parse: 愈 + A 就愈 + B. 12. 無論幾忙，我都會嚟"
            "。 mou4 leon6 gei2 mong4, ngo5 dou1 wui5 lai4. (However busy, I "
            "will come.) Parse: 無論 + concession, 都 + main. 13. 佢一邊食"
            "一邊睇電視。 keoi5 jat1 bin1 sik6 jat1 bin1 tai2 din6 si6. (He "
            "eats while watching TV.) Parse: 一邊 + A 一邊 + B. 14. 等我返"
            "到嚟先講。 dang2 ngo5 faan1 dou3 lai4 sin1 gong2. (Wait till I "
            "get back, then talk.) Parse: 等 + clause + 先. 15. 唔係我唔想"
            "去，係我冇時間。 m4 hai6 ngo5 m4 soeng2 heoi3, hai6 ngo5 mou5 "
            "si4 gaan3. (It is not that I do not want to go; I have no time.) "
            "Parse: 唔係 + denied reason, 係 + real reason."
        ),
        "how_it_works": (
            "Complex sentences work by linking clauses with fixed pairs: 因"
            "為...所以 jan1wai6...so2ji5 (because...therefore), 雖然...但係 "
            "seoi1jin4...daan6hai6 (although...but), 如果...就 jyu4gwo2...zau6 "
            "(if...then), 唔單止...仲 m4daan1zi2...zung6 (not only...also), "
            "愈...愈 jyu6...jyu6 (the more...the more), 無論...都 mou4leon6..."
            "dou1 (no matter...still), 一邊...一邊 jat1bin1...jat1bin1 "
            "(while). Relative clauses come before the noun with 嘅 ge3: 我"
            "買嘅書 ngo5 maai5 ge3 syu1 (the book I bought). Reported speech "
            "needs no that-word: 佢話佢唔嚟 keoi5 waa6 keoi5 m4 lai4 (he says "
            "he is not coming). Build long sentences by choosing a pair, "
            "filling both halves, and letting 嘅-clauses modify any noun."
        ),
        "key_points": [
            "15 long sentences with clauses, connectors, and relative clauses - each parsed and translated.",
            "Connector pairs: 因為...所以, 雖然...但係, 如果...就, 唔單止...仲, 愈...愈, 無論...都, 一邊...一邊.",
            "Relative clauses precede the noun with 嘅 ge3: 我買嘅書 (the book I bought).",
            "Reported speech with 話 waa6 needs no conjunction.",
            "Every sentence carries characters, Jyutping, English, and a parse.",
        ],
        "requirements": [
            "Build sentences with five different connector pairs.",
            "Form three 嘅 relative clauses on nouns.",
            "Parse a complex sentence into its clauses.",
        ],
        "standards": [
            "Clause linkage per Matthews and Yip: paired conjunctions, 嘅 relativization.",
            "Extent complements verb + 得 + 到; correlative 愈...愈.",
            "Jyutping on every sentence and parse.",
        ],
        "citations": [CIT_MATTHEWS, CIT_JYUTPING],
        "sig_lens": (
            "Through the Signature lens, complex sentences are signed "
            "architecture - 因為...所以 the cause-and-result arch, 雖然..."
            "但係 the concession arch, 嘅 the keystone that locks a clause "
            "onto its noun. Each arch signed true, the whole building "
            "stands."
        ),
    },
    {
        "key": "conversation-market",
        "name": "Cantonese Conversation: At the Market",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A twenty-line bilingual market dialogue, annotated. Seller S, "
            "buyer B (Ah Ming). 1. S: 靚仔，買咩呀？ leng3 zai2, maai5 me1 "
            "aa3? (Handsome, what are you buying?) [Note: 靚仔 calls a young "
            "man; sellers use it freely.] 2. B: 啲橙幾多錢一斤？ di1 caang2 "
            "gei2 do1 cin2 jat1 gan1? (How much are the oranges per catty?) "
            "3. S: 十二蚊一斤，好甜㗎。 sap6 ji6 man1 jat1 gan1, hou2 tim4 "
            "gaa3. (Twelve dollars a catty, very sweet.) 4. B: 平啲啦，十蚊"
            "得唔得？ peng4 di1 laa1, sap6 man1 dak1 m4 dak1? (Cheaper please; "
            "ten dollars OK?) 5. S: 十蚊真係唔得，十一啦。 sap6 man1 zan1 "
            "hai6 m4 dak1, sap6 jat1 laa1. (Ten really will not do; eleven.) "
            "6. B: 好啦，要兩斤。 hou2 laa1, jiu3 loeng5 gan1. (OK, two "
            "catties.) 7. S: 好，兩斤廿二蚊。 hou2, loeng5 gan1 jaa6 ji6 man1. "
            "(Good; two catties, twenty-two dollars.) 8. B: 啲蘋果呢？ di1 "
            "ping4 gwo2 ne1? (What about the apples?) 9. S: 蘋果八蚊一斤。 "
            "ping4 gwo2 baat3 man1 jat1 gan1. (Apples eight dollars a catty.) "
            "10. B: 幫我揀四個大嘅。 bong1 ngo5 gaan2 sei3 go3 daai6 ge3. "
            "(Pick four big ones for me.) 11. S: 呢四個最靚。 ni1 sei3 go3 "
            "zeoi3 leng3. (These four are the nicest.) 12. B: 加埋幾多錢？ "
            "gaa1 maai4 gei2 do1 cin2? (How much altogether?) 13. S: 橙廿二"
            "加蘋果十六，三十八。 caang2 jaa6 ji6 gaa1 ping4 gwo2 sap6 luk6, "
            "saam1 sap6 baat3. (Oranges 22 plus apples 16: 38.) 14. B: 找四十"
            "蚊。 zaau2 sei3 sap6 man1. (Here is forty dollars - lit. give "
            "change from forty.) [Note: 找 here means hand over for change.] "
            "15. S: 找返兩蚊。 zaau2 faan1 loeng5 man1. (Two dollars change.) "
            "16. B: 有冇袋？ jau5 mou5 doi2? (Is there a bag?) 17. S: 有，幫"
            "你入好喇。 jau5, bong1 nei5 jap6 hou2 laa3. (Yes, packed for "
            "you.) 18. B: 唔該。 m4 goi1. (Thanks.) 19. S: 唔使客氣，聽日再"
            "嚟。 m4 sai2 haak3 hei3, ting1 jat6 zoi3 lai4. (You are welcome; "
            "come again tomorrow.) 20. B: 好，拜拜。 hou2, baai1 baai3. (OK, "
            "bye.)"
        ),
        "how_it_works": (
            "A market dialogue works in five moves: greet (靚仔 leng3zai2), "
            "ask price (幾多錢一斤 gei2do1cin2 jat1gan1), bargain (平啲啦 "
            "peng4di1laa1), total (加埋 gaa1maai4), pay and part (找錢 "
            "zaau2cin2, 拜拜). Weight is sold by the catty 斤 gan1 (about 600 "
            "grams); fruit is counted with 個 go3. Sellers call young men 靚"
            "仔 and young women 靚女 leng3neoi2 - it is friendliness, not "
            "flattery. Bargaining is expected and quick: one counter-offer "
            "each, then decide. Run any market trip with these five moves."
        ),
        "key_points": [
            "20-line bilingual dialogue: greeting, price, bargain, total, pay, part - fully annotated.",
            "Market units: 斤 gan1 catty; price pattern 幾多錢一斤.",
            "Seller address terms 靚仔/靚女; bargaining etiquette in two moves.",
            "Payment and change: 找錢, 找返; bag request 有冇袋.",
            "Every line carries characters, Jyutping, English, and notes.",
        ],
        "requirements": [
            "Role-play buyer and seller through all five moves.",
            "Bargain a price down politely in Cantonese.",
            "Explain 斤 and the 靚仔 address term.",
        ],
        "standards": [
            "Market interaction script per Hong Kong usage; weight unit 斤 gan1.",
            "Bargaining formulas as set phrases; change and bag requests.",
            "Jyutping on every line; annotations explain usage.",
        ],
        "citations": [CIT_MATTHEWS, CIT_JYUTPING],
        "sig_lens": (
            "Through the Signature lens, the market is the daily exchange of "
            "seals - price asked, price answered, both sides signing the "
            "deal with 好啦 hou2laa1. The honest bargain is a covenant both "
            "can keep."
        ),
    },
    {
        "key": "conversation-friend",
        "name": "Cantonese Conversation: Meeting a Friend",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A twenty-line bilingual dialogue of two friends meeting, "
            "annotated. A (Ah Ming), B (Ah Kuen). 1. A: 阿娟！好耐冇見！ "
            "aa3 gyun3! hou2 noi6 mou5 gin3! (Ah Kuen! Long time no see!) 2. "
            "B: 阿明！真係好耐冇見！ aa3 ming4! zan1 hai6 hou2 noi6 mou5 gin3! "
            "(Ah Ming! Really long time!) 3. A: 近排點呀？ gan6 paai4 dim2 "
            "aa3? (How have you been?) 4. B: 幾好，忙到暈。 gei2 hou2, mong4 "
            "dou3 wan4. (Pretty good; busy to the point of dizziness.) 5. A: "
            "做緊咩呀？ zou6 gan2 me1 aa3? (What are you doing these days?) "
            "6. B: 轉咗工，而家做設計。 zyun2 zo2 gung1, ji4 gaa1 zou6 cit3 "
            "gai3. (Changed jobs; now doing design.) 7. A: 咁正！人工加咗"
            "未？ gam3 zeng3! jan4 gung1 gaa1 zo2 mei6? (Great! Pay rise yet?) "
            "8. B: 加咗少少啦。 gaa1 zo2 siu2 siu2 laa1. (A small rise.) 9. "
            "A: 得閒出嚟飲茶。 dak1 haan4 ceot1 lai4 jam2 caa4. (Come for tea "
            "when free.) 10. B: 好呀，星期六得唔得？ hou2 aa3, sing1 kei4 "
            "luk6 dak1 m4 dak1? (Good; is Saturday OK?) 11. A: 得，下晝三點"
            "。 dak1, haa6 zau3 saam1 dim2. (Yes; three in the afternoon.) 12. "
            "B: 邊度等？ bin1 dou6 dang2? (Where shall we meet?) 13. A: 旺角"
            "地鐵站。 wong6 gok3 dei6 tit3 zaam6. (Mong Kok MTR station.) 14. "
            "B: 好，一言為定。 hou2, jat1 jin4 wai4 ding6. (Good; it is a "
            "deal.) 15. A: 你屋企人好嗎？ nei5 uk1 kei2 jan4 hou2 maa3? (Is "
            "your family well?) 16. B: 好，阿媽成日問起你。 hou2, aa3 maa1 "
            "seng4 jat6 man6 hei2 nei5. (Well; Mum often asks about you.) 17. "
            "A: 代我問候佢。 doi6 ngo5 man6 hau6 keoi5. (Give her my regards.) "
            "18. B: 一定。我趕時間，走先喇。 jat1 ding6. ngo5 gon2 si4 gaan3, "
            "zau2 sin1 laa3. (Certainly. I am in a hurry; leaving first.) 19. "
            "A: 好，星期六見。 hou2, sing1 kei4 luk6 gin3. (OK, see you "
            "Saturday.) 20. B: 星期六見，拜拜。 sing1 kei4 luk6 gin3, baai1 "
            "baai3. (See you Saturday, bye.)"
        ),
        "how_it_works": (
            "A reunion dialogue works in five moves: exclaim (好耐冇見 "
            "hou2noi6mou5gin3), catch up (近排點 gan6paai4dim2, 做緊咩 "
            "zou6gan2me1), invite (得閒出嚟飲茶), fix time and place (幾時/邊"
            "度), part warmly (代我問候, 星期六見). News is traded with 咗 "
            "zo2 for what changed (轉咗工 zyun2zo2gung1 - changed jobs). "
            "Family regards are passed with 代我問候 doi6ngo5man6hau6. "
            "Leaving first is excused with 趕時間 gon2si4gaan3 (in a hurry). "
            "Meet any old friend with these five moves."
        ),
        "key_points": [
            "20-line bilingual dialogue: reunion, catch-up, invitation, plan, regards, parting - annotated.",
            "Reunion openers: 好耐冇見, 近排點; news with 咗 (轉咗工).",
            "Invitation and plan: 得閒出嚟飲茶, 一言為定, time and place fixed.",
            "Family regards: 代我問候; hurried exit: 趕時間, 走先.",
            "Every line carries characters, Jyutping, English, and notes.",
        ],
        "requirements": [
            "Role-play a reunion through all five moves.",
            "Trade news using 咗 for changes.",
            "Pass regards and part warmly.",
        ],
        "standards": [
            "Reunion script per Hong Kong usage; invitation and planning formulas.",
            "Change-of-state with 咗; regards formulas 代我問候.",
            "Jyutping on every line; annotations explain usage.",
        ],
        "citations": [CIT_MATTHEWS, CIT_JYUTPING],
        "sig_lens": (
            "Through the Signature lens, reunion is the re-signing of "
            "friendship - 好耐冇見 the old seal recognized, 一言為定 the new "
            "seal pressed. Each meeting signs the bond again so time cannot "
            "erase it."
        ),
    },
    {
        "key": "conversation-problem",
        "name": "Cantonese Conversation: Solving a Problem",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A twenty-line bilingual dialogue solving a lost-wallet problem, "
            "annotated. A (Ah Ming, lost his wallet), B (friend). 1. A: 弊"
            "喇！我唔見咗個銀包！ bai6 laa3! ngo5 m4 gin3 zo2 go3 ngan4 baau1! "
            "(Oh no! I lost my wallet!) 2. B: 唔好慌，慢慢諗。 m4 hou2 fong1, "
            "maan6 maan2 nam2. (Do not panic; think slowly.) 3. A: 我記得搭"
            "地鐵嗰陣仲有。 ngo5 gei3 dak1 daap3 dei6 tit3 go2 zan6 zung6 jau5. "
            "(I remember I still had it on the MTR.) 4. B: 邊個站落車？ bin1 "
            "go3 zaam6 lok6 ce1? (Which station did you alight at?) 5. A: 中"
            "環站。 zung1 waan4 zaam6. (Central station.) 6. B: 打電話去失物"
            "處問下。 daa2 din6 waa2 heoi3 sat1 mat6 cyu3 man6 haa6. (Call the "
            "lost property office and ask.) 7. A: 有冇電話號碼？ jau5 mou5 "
            "din6 waa2 hou6 maa5? (Do you have the number?) 8. B: 上網查下啦"
            "。 soeng5 mong5 caa4 haa6 laa1. (Look it up online.) 9. A: 查到"
            "喇，我打去。 caa4 dou2 laa3, ngo5 daa2 heoi3. (Found it; I am "
            "calling.) 10. B: 開擴音，我幫你聽。 hoi1 kong3 jam1, ngo5 bong1 "
            "nei5 teng1. (Put it on speaker; I will listen with you.) 11. A: "
            "(講電話) 唔該，我唔見咗銀包。 (gong2 din6 waa2) m4 goi1, ngo5 m4 "
            "gin3 zo2 ngan4 baau1. ([on the phone] Hello, I lost my wallet.) "
            "12. B: 佢點講？ keoi5 dim2 gong2? (What did they say?) 13. A: 佢"
            "話有人執到，叫我去攞。 keoi5 waa6 jau5 jan4 zap1 dou2, giu3 ngo5 "
            "heoi3 lo2. (They said someone found it; told me to collect it.) "
            "14. B: 太好喇！證件齊唔齊？ taai3 hou2 laa3! zing3 gin6 cai4 m4 "
            "cai4? (Great! Are the documents all there?) 15. A: 佢話齊晒。 "
            "keoi5 waa6 cai4 saai3. (They said all there.) 16. B: 快啲去攞啦"
            "。 faai3 di1 heoi3 lo2 laa1. (Go collect it quickly.) 17. A: 多"
            "謝你幫手。 do1 ze6 nei5 bong1 sau2. (Thank you for your help.) "
            "18. B: 唔使客氣，下次小心啲。 m4 sai2 haak3 hei3, haa6 ci3 siu2 "
            "sam1 di1. (You are welcome; be more careful next time.) 19. A: "
            "我請你飲茶。 ngo5 ceng2 nei5 jam2 caa4. (I treat you to tea.) "
            "20. B: 好呀，走啦。 hou2 aa3, zau2 laa1. (Good; let us go.)"
        ),
        "how_it_works": (
            "A problem dialogue works in six moves: alarm (弊喇 bai6laa3), "
            "calm (唔好慌 m4hou2fong1), recall (我記得 ngo5 gei3dak1), plan "
            "(打電話去 daa2din6waa2 heoi3), act (the phone call with 唔該開"
            "頭), resolve and thank (太好喇, 多謝你幫手). Memory is traced "
            "with 嗰陣 go2zan6 (at that time): 搭地鐵嗰陣仲有 daap3dei6tit3 "
            "go2zan6 zung6jau5 (still had it on the MTR). Help is offered "
            "with 我幫你 ngo5 bong1 nei5. The treat at the end (我請你飲茶) "
            "closes the social debt. Solve any problem by moving through "
            "these six steps."
        ),
        "key_points": [
            "20-line bilingual dialogue: alarm, calm, recall, plan, act, resolve - annotated.",
            "Crisis words: 弊喇, 唔好慌, 唔見咗 (lost).",
            "Recall with 嗰陣; help with 我幫你; phone script with 唔該開頭.",
            "Resolution sealed with a treat: 我請你飲茶.",
            "Every line carries characters, Jyutping, English, and notes.",
        ],
        "requirements": [
            "Role-play a problem through all six moves.",
            "Trace a memory with 嗰陣 in three sentences.",
            "Make a help phone call politely.",
        ],
        "standards": [
            "Problem-solving script per Hong Kong usage; 失物處 lost property office.",
            "Recall construction 嗰陣; reported speech with 話 waa6.",
            "Jyutping on every line; annotations explain usage.",
        ],
        "citations": [CIT_MATTHEWS, CIT_JYUTPING],
        "sig_lens": (
            "Through the Signature lens, solving a problem is re-signing "
            "order - 弊喇 the broken seal named, 唔好慌 the steadying seal, "
            "the found wallet the seal restored. Help given is a seal that "
            "returns as tea."
        ),
    },
    {
        "key": "mastery",
        "name": "Cantonese Mastery Review and Full Reference",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The whole database in one teaching summary: alphabet, 200 core "
            "words, key grammar, and all phrase tables. JYUTPING QUICK "
            "TABLE: 19 initials - b p m f d t n l g k ng h gw kw w z c s j; "
            "key finals - aa ai au aam aan aang aap aat aak e ei eng i iu in "
            "ing ip it ik o oi ou on ong ot ok u ui un ung ut uk oe oeng yu "
            "yun yut m ng; 6 tones - 1 high level si1, 2 high rising si2, 3 "
            "mid level si3, 4 low falling si4, 5 low rising si5, 6 low level "
            "si6; entering 7/8/9 on -p/-t/-k (cat1, baat3, sik6). 200 CORE "
            "WORDS (characters + Jyutping + English): people - 我 ngo5, 你 "
            "nei5, 佢 keoi5, 人 jan4, 男人 naam4jan4, 女人 neoi5jan4, 小朋友 "
            "siu2pang4jau5, 朋友 pang4jau5, 爸爸 baa4baa1, 媽媽 maa4maa1, 哥哥 "
            "go4go1, 細佬 sai3lou2, 家姐 gaa1ze2, 細妹 sai3mui2, 老師 lou5si1, "
            "學生 hok6saang1, 醫生 ji1sang1, 老細 lou5sai3, 同事 tung4si6, 同"
            "學 tung4hok6; home - 屋企 uk1kei2, 房 fong2, 廳 teng1, 廚房 "
            "cyu4fong2, 沖涼房 cung1loeng4fong2, 床 cong4, 枱 toi2, 梳化 "
            "so1faa3, 雪櫃 syut3gwai6, 窗 coeng1, 門 mun4, 燈 dang1; study - "
            "書 syu1, 筆 bat1, 字 zi6, 功課 gung1fo3, 考試 haau2si3, 學校 "
            "hok6haau6; machines - 電話 din6waa2, 電腦 din6nou5, 車 ce1, 巴士 "
            "baa1si2, 地鐵 dei6tit3, 的士 dik1si2, 飛機 fei1gei1; food - 飯 "
            "faan6, 麵 min6, 菜 coi3, 魚 jyu4, 肉 juk6, 水 seoi2, 茶 caa4, "
            "奶茶 naai5caa4, 湯 tong1, 生果 saang1gwo2, 蘋果 ping4gwo2, 橙 "
            "caang2; clothes - 衫 saam1, 褲 fu3, 鞋 haai4, 眼鏡 ngaan5geng3; "
            "nature - 天 tin1, 地 dei6, 日 jat6, 月 jyut6, 星 sing1, 山 saan1, "
            "海 hoi2, 河 ho4, 樹 syu6, 花 faa1, 狗 gau2, 貓 maau1, 雀仔 "
            "zoek3zai2; time - 而家 ji4gaa1, 今日 gam1jat6, 聽日 ting1jat6, 尋"
            "日 cam4jat6, 朝早 ziu1zou2, 夜晚 je6maan5, 星期 sing1kei4, 月 "
            "jyut6, 年 nin4, 時間 si4gaan3; money - 錢 cin2, 蚊 man1, 銀包 "
            "ngan4baau1; body - 頭 tau4, 眼 ngaan5, 手 sau2, 腳 goek3, 心 sam1, "
            "肚 tou5; feelings - 開心 hoi1sam1, 傷心 soeng1sam1, 嬲 nau1, 驚 "
            "geng1, 愛 oi3, 鍾意 zung1ji3; qualities - 大 daai6, 細 sai3, 好 "
            "hou2, 靚 leng3, 快 faai3, 慢 maan6, 平 peng4, 貴 gwai3, 新 san1, "
            "舊 gau6, 熱 jit6, 凍 dung3, 高 gou1, 矮 ngai2, 長 coeng4, 忙 "
            "mong4, 得閒 dak1haan4, 叻 lek1; verbs - 係 hai6, 有 jau5, 食 "
            "sik6, 飲 jam2, 睇 tai2, 聽 teng1, 講 gong2, 寫 se2, 讀 duk6, 學 "
            "hok6, 做 zou6, 去 heoi3, 嚟 lai4, 買 maai5, 賣 maai6, 畀 bei2, 攞 "
            "lo2, 放 fong3, 開 hoi1, 閂 saan1, 瞓 fan3, 起身 hei2san1, 返工 "
            "faan1gung1, 返學 faan1hok6, 用 jung6, 識 sik1, 記得 gei3dak1, 唔記"
            "得 m4gei3dak1, 幫 bong1, 教 gaau3, 玩 waan2, 笑 siu3, 喊 haam3; "
            "helpers - 嘅 ge3, 咗 zo2, 緊 gan2, 過 gwo3, 會 wui5, 吓 haa5, 喺 "
            "hai2, 唔 m4, 未 mei6, 冇 mou5, 哋 dei6, 呢 ni1, 嗰 go2, 咩 me1, "
            "點 dim2, 邊 bin1, 幾 gei2, 都 dou1, 就 zau6, 已經 ji5ging1, 重 "
            "zung6, 先 sin1, 又 jau6, 啦 laa1, 呀 aa3, 咩 me1, 嘛 maa3, 嘅 ge3, "
            "嘞 laak3; numbers - 一 jat1, 二 ji6, 兩 loeng5, 三 saam1, 四 sei3, "
            "五 ng5, 六 luk6, 七 cat1, 八 baat3, 九 gau2, 十 sap6, 百 baak3, "
            "千 cin1, 萬 maan6. KEY GRAMMAR: SVO; no conjugation; 咗/緊/過/"
            "會/吓 aspects; 唔/未/冇 negation; classifiers with numbers; 嘅 "
            "possession and relatives; 喺 location; A-not-A and 咩 questions; "
            "過 gwo3 comparatives; 畀 bei2 passives. PHRASE TABLES: greetings "
            "(你好, 早晨, 多謝, 唔該, 對唔住, 再見), thanks (多謝 for gifts, "
            "唔該 for services), market (幾多錢, 平啲得唔得, 買單), travel "
            "(點樣去, 幾耐, 搭地鐵), time (點/分/半, 星期一至日, 一月至十二"
            "月). Study path: tones (record 3) -> words (4-9) -> grammar "
            "(10) -> themed sentences (11-21) -> questions and commands "
            "(22-23) -> stories and idioms (25-28) -> conversations (31-33) "
            "-> this review."
        ),
        "how_it_works": (
            "Mastery works by cycling the ladder: say the six tones, read "
            "the 200 words aloud, rebuild ten sentences from each grammar "
            "rule, retell the three stories, use five idioms in speech, and "
            "hold the three conversations. Test yourself: cover the English "
            "and translate the Cantonese; cover the Cantonese and produce it "
            "from the English; shadow the Jyutping until the tones are "
            "automatic. A learner who can do all of this - tones clean, 200 "
            "words ready, grammar rules applied without thinking, stories "
            "retold, conversations held - speaks working Cantonese. Return "
            "to any record for repair; the ladder is always here."
        ),
        "key_points": [
            "Complete quick reference: Jyutping table (19 initials, key finals, 6+3 tones), 200 core words, key grammar, phrase tables.",
            "200 words across people, home, study, machines, food, clothes, nature, time, money, body, feelings, qualities, verbs, helpers, numbers.",
            "Grammar condensed: SVO, five aspects, three negations, classifiers, 嘅, 喺, questions, comparatives, passives.",
            "Phrase tables: greetings, thanks, market, travel, time.",
            "Study path maps every record 1-34 into a learning order.",
        ],
        "requirements": [
            "Recite the Jyutping table and six tones from memory.",
            "Produce all 200 core words in Jyutping.",
            "Hold a five-minute conversation using only this database.",
        ],
        "standards": [
            "Reference completeness: every record's core content condensed here.",
            "Jyutping authority on all 200 words; traditional characters throughout.",
            "Study path follows the teaching ladder simple to complex.",
        ],
        "citations": [CIT_MATTHEWS, CIT_BAUER, CIT_JYUTPING, CIT_ETHNO],
        "sig_lens": (
            "Through the Signature lens, mastery is the fully signed tongue "
            "- every tone a seal, every word an instrument, every rule a "
            "covenant kept. The learner who signs all 200 words and walks "
            "the whole ladder carries the language as a sealed trust."
        ),
    },
]
