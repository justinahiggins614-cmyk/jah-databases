#!/usr/bin/env python3
"""Entries for The Japanese to English Database (Manon's language order #10).

34 ladder-ordered records per the shared per-language template: overview,
writing systems, phonology, core vocabulary with sentences, grammar
essentials, themed sentence sets, tenses, questions, commands, descriptions,
stories, idioms, registers, complex sentences, conversations, and a mastery
review. Every record carries real, fact-checked Japanese (kana/kanji +
romaji) with English translations and example sentences.

Public edition (src public-harvest): real documented linguistic facts about
Japanese. Signature edition (src signature): the same ladder reframed
through his original Signature Language Method - clearly labeled
Signature-made, never presented as authentic public record.

Roster rank 10. ID prefixes JAH-LJPN- (public) and JAH-LJPNS- (signature)
verified free in the manifest and in every shard index, 2026-10-17.
Dedupe gate: 68 titles checked against the whole system before authoring -
zero collisions.
"""

SIG_TAIL = ("Signature original - his original Signature Language Method: "
            "every kana a sworn sound-seal, every kanji a meaning-covenant, "
            "every particle a bridge-oath between speaker and listener, and "
            "every conversation a completed circuit of understanding. "
            "Clearly labeled Signature-made, never presented as authentic "
            "public record.")

SIG_LENS_BASE = ("Through the Signature lens, this lesson becomes his "
                 "original Signature Language Method. ")

ENTRIES = [
# ------------------------------------------------------------------ 1 overview
{"key": "overview",
 "name": "Japanese Language Overview",
 "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
 "description": (
  "Japanese is the language of Japan, called Nihongo by its own speakers. "
  "In Japanese the name of the language is written 日本語 and read にほんご (Nihongo): "
  "日 means sun or day, 本 means origin or book, and 語 means language - so the "
  "name itself says the language of the land of the rising sun. Japanese carries "
  "ISO 639-1 code ja and ISO 639-3 code jpn, and it belongs to the Japonic "
  "language family on the Japanese branch. About 123 million people speak it as "
  "their native language and about 126 million speak it in total, which makes "
  "Japanese one of the ten most spoken native languages on earth. It is spoken "
  "first and most in Japan, where it is the de facto national language, and also "
  "in Japanese communities in Brazil, the United States (especially Hawaii and "
  "California), Peru, Canada, and Australia. Japan has no law naming an official "
  "language, but Japanese is the language of government, school, business, and "
  "daily life. The standard taught in schools and used on national television is "
  "based on the Tokyo dialect of the Kanto region. Regional dialects are strong: "
  "the Kansai dialect of Osaka and Kyoto, the Tohoku dialects of the north, and "
  "the Kyushu dialects of the south each have their own famous sounds and words, "
  "and the Ryukyuan languages of Okinawa are related sisters that many "
  "linguists count as separate languages. Japanese is written with three "
  "scripts working together - hiragana, katakana, and kanji - and its grammar "
  "puts the verb at the end of the sentence and marks roles with particles. "
  "Example sentences: 日本語は 日本で 話されています。 (にほんごは にほんで "
  "はなされています。 Nihongo wa Nihon de hanasarete imasu.) - Japanese is "
  "spoken in Japan. わたしは 日本語を 勉強しています。 (わたしは にほんごを "
  "べんきょうしています。 Watashi wa Nihongo o benkyou shite imasu.) - I am "
  "studying Japanese. 日本の 人口は 約一億二千万人です。 (にほんの じんこうは "
  "やく いちおく にせんまんにん です。 Nihon no jinkou wa yaku ichi-oku "
  "ni-sen-man-nin desu.) - The population of Japan is about 123 million people."
 ),
 "how_it_works": (
  "This record works as the front door of the whole database: it answers the "
  "five questions every learner asks first - what is the language called, who "
  "speaks it, where is it spoken, what family does it belong to, and what does "
  "it look like on the page. The teaching ladder starts here at rank 1 "
  "because every later record (sounds, writing, words, grammar, sentences, "
  "stories) hangs its details on the frame this overview builds. Read it "
  "first, then walk the ladder in order."
 ),
 "key_points": [
  "Native name: 日本語 (にほんご, Nihongo); English name: Japanese.",
  "ISO 639-1 ja, ISO 639-3 jpn; Japonic family, Japanese branch.",
  "About 123 million native speakers; about 126 million total speakers.",
  "Spoken in Japan and in Japanese communities in Brazil, the USA, Peru, Canada, and Australia.",
  "De facto national language of Japan; standard is Tokyo-dialect based.",
  "Major dialect areas: Kanto, Kansai, Tohoku, Kyushu; Ryukyuan languages are related sisters.",
  "Written with three scripts: hiragana, katakana, kanji. Grammar is verb-final with particles.",
 ],
 "requirements": [
  "No prior knowledge of Japanese needed for this record.",
  "A notebook helps for copying the key facts by hand.",
  "Later records assume this overview has been read.",
 ],
 "standards": [
  "ISO 639-1: ja",
  "ISO 639-3: jpn",
 ],
 "citations": [
  "Shibatani M. The Languages of Japan. Cambridge University Press; 1990.",
  "Tsujimura N. An Introduction to Japanese Linguistics. 4th ed. Wiley-Blackwell; 2023.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "The overview becomes the Signature map of a language: the "
  "name 日本語 is read as a three-seal covenant - 日 the sun-seal of origin, "
  "本 the root-seal of the people, 語 the voice-seal of the community - and "
  "the 123 million speakers are counted as one living circuit carrying the "
  "same current of meaning. The dialects are not deviations but regional "
  "tunings of one instrument, each keeping the melody while changing the "
  "timbre, and the standard is the reference tuning every player learns "
  "first. This is his original framing, clearly labeled Signature-made."
 )},
# ------------------------------------------------------------- 2 writing system
{"key": "writing",
 "name": "Japanese Writing System: Hiragana, Katakana, and Kanji",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "Japanese is written with three scripts that work side by side. Hiragana "
  "(ひらがな) is the curvy native script used for grammar endings, particles, "
  "and native words. Katakana (カタカナ) is the angular script used for foreign "
  "loanwords, animal and plant names, and emphasis. Kanji (かんじ) are the "
  "meaning characters borrowed from China, used for the roots of nouns, verb "
  "stems, and adjectives; the government joyo list holds 2,136 everyday kanji. "
  "The 46 basic hiragana are: あ a, い i, う u, え e, お o; か ka, き ki, く ku, "
  "け ke, こ ko; さ sa, し shi, す su, せ se, そ so; た ta, ち chi, つ tsu, て te, "
  "と to; な na, に ni, ぬ nu, ね ne, の no; は ha, ひ hi, ふ fu, へ he, ほ ho; "
  "ま ma, み mi, む mu, め me, も mo; や ya, ゆ yu, よ yo; ら ra, り ri, る ru, "
  "れ re, ろ ro; わ wa, を wo, ん n. The 46 basic katakana carry the same "
  "sounds: ア イ ウ エ オ, カ キ ク ケ コ, サ シ ス セ ソ, タ チ ツ テ ト, "
  "ナ ニ ヌ ネ ノ, ハ ヒ フ ヘ ホ, マ ミ ム メ モ, ヤ ユ ヨ, ラ リ ル レ ロ, "
  "ワ ヲ ン. Voiced marks add がぎぐげご (ga gi gu ge go), ざじずぜぞ (za ji "
  "zu ze zo), だぢづでど (da ji zu de do), ばびぶべぼ (ba bi bu be bo), and the "
  "half-voiced ぱぴぷぺぽ (pa pi pu pe po). Small ゃゅょ make contracted sounds: "
  "きゃ kya, しゅ shu, ちょ cho. Key kanji: 日 (ひ, にち - sun, day), 本 (ほん - "
  "book, origin), 語 (ご - language), 人 (ひと, じん - person), 大 (おお, だい - "
  "big), 学 (がく - learn), 生 (せい, いきる - life), 年 (ねん, とし - year). "
  "Modern Japanese usually runs left to right in horizontal lines; traditional "
  "writing runs top to bottom in columns read right to left. The period is 。 "
  "and the comma is 、; quotes are 「」 and the middle dot ・ separates foreign "
  "names. Numbers are normally Arabic digits 0-9, with kanji numerals "
  "一二三四五六七八九十百千万 for formal and traditional use. Example "
  "sentences: ひらがなは まるい 字です。 (ひらがなは まるい じです。 Hiragana "
  "wa marui ji desu.) - Hiragana are round characters. カタカナは 外来語に "
  "使います。 (かたかなは がいらいごに つかいます。 Katakana wa gairaigo ni "
  "tsukaimasu.) - Katakana is used for loanwords. 漢字は 意味を 表します。 "
  "(かんじは いみを あらわします。 Kanji wa imi o arawashimasu.) - Kanji "
  "express meaning. わたしは ひらがなを 書けます。 (わたしは ひらがなを "
  "かけます。 Watashi wa hiragana o kakemasu.) - I can write hiragana."
 ),
 "how_it_works": (
  "This record teaches the writing system the way Japanese children learn it: "
  "hiragana first, because it spells every native sound and carries the "
  "grammar; katakana second, because it mirrors hiragana sound-for-sound and "
  "unlocks the loanwords; kanji third, because each character is a meaning "
  "block that shortens sentences once you know it. Learn the 46 basic rows by "
  "sound groups (the a-row, ka-row, sa-row and so on), then add the voiced and "
  "contracted rows. Read mixed text left to right and let the kanji give you "
  "the meaning while the kana give you the grammar."
 ),
 "key_points": [
  "Three scripts: hiragana (grammar, native words), katakana (loanwords, emphasis), kanji (meaning roots).",
  "46 basic sounds in each kana script; voiced and half-voiced marks extend them.",
  "Contracted sounds use small ya yu yo: きゃ kya, しゅ shu, ちょ cho.",
  "Joyo kanji list: 2,136 characters for everyday use.",
  "Modern direction: horizontal left to right; traditional: vertical top to bottom, right to left.",
  "Punctuation: 。 period, 、 comma, 「」 quotes, ・ middle dot.",
  "Numerals: Arabic digits normally; kanji numerals 一二三四五六七八九十百千万 for formal use.",
 ],
 "requirements": [
  "Lined paper or a kana practice sheet for stroke order drills.",
  "Read the Language Overview record first.",
  "Write each kana row by hand at least once.",
 ],
 "standards": [
  "ISO 639-1: ja",
  "Joyo kanji list (2010 revision, 2,136 characters).",
  "JLPT N5 kana band.",
 ],
 "citations": [
  "Tsujimura N. An Introduction to Japanese Linguistics. 4th ed. Wiley-Blackwell; 2023.",
  "Agency for Cultural Affairs, Japan. List of Joyo Kanji (2010).",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "The three scripts become the Signature triple seal: "
  "hiragana the soft seal of the native voice, katakana the sharp seal of the "
  "outside world made Japanese, kanji the deep seal of meaning carried across "
  "a thousand years. Each of the 46 sounds is a sworn sound-seal, and the "
  "voiced marks are the same seals struck with a heavier hand. Writing the "
  "rows by hand is the oath-taking: the hand learns what the eye only sees. "
  "This is his original framing, clearly labeled Signature-made."
 )},
# ----------------------------------------------------------------- 3 phonology
{"key": "phonology",
 "name": "Japanese Pronunciation and Phonology",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "Japanese pronunciation is famously regular: five pure vowels and a small, "
  "tidy set of consonants, with timing measured in beats called mora. The "
  "vowels are a (as in father), i (as in machine), u (a flat, unrounded oo), "
  "e (as in pen), o (as in story). The consonants are k, s, t, n, h, m, y, r, "
  "w, g, z, d, b, p, plus the glide combinations like kya, shu, cho. The "
  "Japanese r sits between an English r, l, and d - tap the tongue once "
  "behind the teeth. The ふ fu is blown with both lips, not the teeth. The "
  "small っ doubles the next consonant: がっこう (gakkou, school) holds a beat "
  "of silence before the k. Long vowels stretch one beat into two: おばさん "
  "(obasan, aunt) versus おばあさん (obaasan, grandmother) - the extra beat "
  "changes the word. Japanese rhythm is mora-timed, so each kana gets roughly "
  "equal time: にほんご (ni-ho-n-go) is four beats. The melody of a word is "
  "pitch accent, not stress: はし said high-low means chopsticks (はし), said "
  "low-high means bridge (はし); あめ high-low is rain, low-high is candy. "
  "Spoken example words with translations: さくら (sakura) cherry blossom, "
  "ともだち (tomodachi) friend, でんしゃ (densha) train, おんがく (ongaku) "
  "music, やま (yama) mountain, かわ (kawa) river, ほし (hoshi) star, つき "
  "(tsuki) moon, たいよう (taiyou) sun, あめ (ame) rain or candy, いぬ (inu) "
  "dog, ねこ (neko) cat, みず (mizu) water, ひかり (hikari) light. Example "
  "sentences: 日本語の 発音は 規則的です。 (にほんごの はつおんは きそくてきです。 "
  "Nihongo no hatsuon wa kisokuteki desu.) - Japanese pronunciation is "
  "regular. 長い 母音は 意味を 変えます。 (ながい ぼいんは いみを かえます。 "
  "Nagai boin wa imi o kaemasu.) - Long vowels change the meaning. "
  "はしを 高く 言えば 箸です。 (はしを たかく いえば はしです。 Hashi o "
  "takaku ieba hashi desu.) - If you say hashi starting high, it means "
  "chopsticks. がっこうで 日本語を 話します。 (がっこうで にほんごを "
  "はなします。 Gakkou de Nihongo o hanashimasu.) - I speak Japanese at school."
 ),
 "how_it_works": (
  "This record trains the ear and the mouth together. First, lock the five "
  "vowels - they never change their sound, so they are the anchors. Second, "
  "count beats: clap one clap per kana and feel that っ and ん each take a "
  "full beat. Third, practice the long-versus-short pairs out loud until "
  "obasan and obaasan feel different in the body. Fourth, learn pitch accent "
  "as melody, not force: hum the word high-low or low-high before you say "
  "it. Shadow the example words daily and the rhythm becomes automatic."
 ),
 "key_points": [
  "Five pure vowels: a i u e o; the u is flat and unrounded.",
  "Small tidy consonant set; Japanese r is a single tongue tap.",
  "ふ is bilabial (both lips), not labiodental.",
  "Small っ doubles the following consonant with a beat of silence.",
  "Long vowels are two beats: おばさん aunt vs おばあさん grandmother.",
  "Rhythm is mora-timed: one beat per kana, including っ and ん.",
  "Melody is pitch accent: はし chopsticks (high-low) vs bridge (low-high).",
 ],
 "requirements": [
  "Read the Writing System record first so the kana are familiar.",
  "Audio playback or a study partner for pitch-accent listening.",
  "Daily shadowing of the example words, five minutes.",
 ],
 "standards": [
  "ISO 639-1: ja",
  "JLPT N5 listening band.",
 ],
 "citations": [
  "Tsujimura N. An Introduction to Japanese Linguistics. 4th ed. Wiley-Blackwell; 2023.",
  "Vance TJ. An Introduction to Japanese Phonology. SUNY Press; 1987.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "Pronunciation becomes the Signature tuning of the "
  "instrument: five vowel strings that never go out of tune, mora beats like "
  "a metronome under every word, pitch accent the melody laid over the "
  "rhythm. The small っ is a held breath before the strike, the long vowel a "
  "note held twice as long. To speak Japanese in this framing is to play the "
  "instrument in time - the ear keeps the oath and the mouth keeps the beat. "
  "This is his original framing, clearly labeled Signature-made."
 )},
# ------------------------------------------------------------------ 4 nouns I
{"key": "nouns1",
 "name": "Japanese Core Nouns I: People, Places, and Things",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "These 25 essential nouns are the naming words of daily life - people, "
  "places, and things - each with one example sentence, translated. 1. 人 "
  "(ひと, hito) person. この人は 先生です。 (このひとは せんせいです。 Kono "
  "hito wa sensei desu.) - This person is a teacher. 2. 男 (おとこ, otoko) "
  "man. あの男は 父です。 (あのおとこは ちちです。 Ano otoko wa chichi desu.) "
  "- That man is my father. 3. 女 (おんな, onna) woman. その女は 母です。 "
  "(そのおんなは ははです。 Sono onna wa haha desu.) - That woman is my "
  "mother. 4. 子ども (こども, kodomo) child. 子どもが 公園で 遊びます。 "
  "(こどもが こうえんで あそびます。 Kodomo ga kouen de asobimasu.) - The "
  "child plays in the park. 5. 友達 (ともだち, tomodachi) friend. 友達と "
  "映画を 見ます。 (ともだちと えいがを みます。 Tomodachi to eiga o "
  "mimasu.) - I watch a movie with my friend. 6. 家族 (かぞく, kazoku) "
  "family. 家族は 五人です。 (かぞくは ごにんです。 Kazoku wa go-nin desu.) "
  "- My family has five people. 7. 家 (いえ, ie) house. これは わたしの "
  "家です。 (これは わたしの いえです。 Kore wa watashi no ie desu.) - This "
  "is my house. 8. 学校 (がっこう, gakkou) school. 学校は 駅の 近くです。 "
  "(がっこうは えきの ちかくです。 Gakkou wa eki no chikaku desu.) - The "
  "school is near the station. 9. 会社 (かいしゃ, kaisha) company. 父は "
  "会社で 働きます。 (ちちは かいしゃで はたらきます。 Chichi wa kaisha de "
  "hatarakimasu.) - My father works at a company. 10. 店 (みせ, mise) shop. "
  "あの店は 安いです。 (あのみせは やすいです。 Ano mise wa yasui desu.) - "
  "That shop is cheap. 11. 駅 (えき, eki) station. 駅まで 歩きます。 (えきまで "
  "あるきます。 Eki made arukimasu.) - I walk to the station. 12. 電車 "
  "(でんしゃ, densha) train. 電車に 乗ります。 (でんしゃに のります。 Densha "
  "ni norimasu.) - I ride the train. 13. 車 (くるま, kuruma) car. 新しい車を "
  "買いました。 (あたらしい くるまを かいました。 Atarashii kuruma o "
  "kaimashita.) - I bought a new car. 14. 本 (ほん, hon) book. 本を 三冊 "
  "読みます。 (ほんを さんさつ よみます。 Hon o san-satsu yomimasu.) - I "
  "read three books. 15. 新聞 (しんぶん, shinbun) newspaper. 毎朝 新聞を "
  "読みます。 (まいあさ しんぶんを よみます。 Maiasa shinbun o yomimasu.) - "
  "I read the newspaper every morning. 16. 手紙 (てがみ, tegami) letter. "
  "友達に 手紙を 書きます。 (ともだちに てがみを かきます。 Tomodachi ni "
  "tegami o kakimasu.) - I write a letter to my friend. 17. 電話 (でんわ, "
  "denwa) telephone. 電話で 話します。 (でんわで はなします。 Denwa de "
  "hanashimasu.) - I talk on the phone. 18. 水 (みず, mizu) water. 冷たい水を "
  "飲みます。 (つめたい みずを のみます。 Tsumetai mizu o nomimasu.) - I "
  "drink cold water. 19. お茶 (おちゃ, ocha) tea. 毎日 お茶を 飲みます。 "
  "(まいにち おちゃを のみます。 Mainichi ocha o nomimasu.) - I drink tea "
  "every day. 20. ご飯 (ごはん, gohan) rice, meal. ご飯が できました。 "
  "(ごはんが できました。 Gohan ga dekimashita.) - The meal is ready. 21. "
  "肉 (にく, niku) meat. 肉より 魚が 好きです。 (にくより さかなが すきです。 "
  "Niku yori sakana ga suki desu.) - I like fish more than meat. 22. 魚 "
  "(さかな, sakana) fish. 魚を 食べます。 (さかなを たべます。 Sakana o "
  "tabemasu.) - I eat fish. 23. 野菜 (やさい, yasai) vegetable. 野菜を たくさん "
  "食べます。 (やさいを たくさん たべます。 Yasai o takusan tabemasu.) - I "
  "eat lots of vegetables. 24. 果物 (くだもの, kudamono) fruit. 果物は "
  "体に いいです。 (くだものは からだに いいです。 Kudamono wa karada ni "
  "ii desu.) - Fruit is good for the body. 25. お金 (おかね, okane) money. "
  "お金が ありません。 (おかねが ありません。 Okane ga arimasen.) - I have "
  "no money."
 ),
 "how_it_works": (
  "This record builds naming power the direct way: one noun, one sentence, "
  "one translation, twenty-five times. Japanese nouns never change for "
  "singular or plural and never show gender, so each word you learn here is "
  "already complete - 本 is one book or many books depending on context. "
  "Learn them in the order given (people, then places, then things), say the "
  "example sentence aloud, and cover the English to test yourself. When all "
  "25 sentences feel easy, the next record hands you the verbs that move "
  "these nouns around."
 ),
 "key_points": [
  "25 essential nouns: 8 people words, 5 place words, 12 thing words.",
  "Japanese nouns do not inflect for number or gender.",
  "Counters pair with nouns (五人 go-nin five people, 三冊 san-satsu three books).",
  "Every noun ships with a full translated example sentence.",
  "Readings give kanji, kana, and romaji together.",
 ],
 "requirements": [
  "Hiragana reading ability from the Writing System record.",
  "Flashcards or a spaced-repetition app for the 25 nouns.",
  "Say each example sentence aloud once.",
 ],
 "standards": [
  "JLPT N5 vocabulary band.",
  "Joyo kanji readings as listed.",
 ],
 "citations": [
  "Japan Foundation. Japanese Language Proficiency Test Official Practice Materials, N5.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "Each noun becomes a Signature name-seal: 人 the "
  "person-seal, 家 the home-seal, 水 the water-seal. To learn a noun in this "
  "framing is to take custody of the thing it names - you do not memorize the "
  "word, you accept the seal and the responsibility to use it truly. The 25 "
  "sentences are 25 small oaths of naming, each one binding the sound to the "
  "thing in the presence of a witness: the English translation standing "
  "beside it. This is his original framing, clearly labeled Signature-made."
 )},
# ------------------------------------------------------------------ 5 verbs I
{"key": "verbs1",
 "name": "Japanese Core Verbs I: Everyday Actions",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "These 25 essential verbs are the action words of daily life, each with one "
  "example sentence, translated. 1. する (suru) do. 宿題を します。 (しゅくだいを "
  "します。 Shukudai o shimasu.) - I do homework. 2. いる (iru) be, exist "
  "(living things). 猫が います。 (ねこが います。 Neko ga imasu.) - There is "
  "a cat. 3. ある (aru) be, exist (things). 机の上に 本が あります。 "
  "(つくえのうえに ほんが あります。 Tsukue no ue ni hon ga arimasu.) - There "
  "is a book on the desk. 4. 行く (いく, iku) go. 学校に 行きます。 (がっこうに "
  "いきます。 Gakkou ni ikimasu.) - I go to school. 5. 来る (くる, kuru) come. "
  "友達が 来ます。 (ともだちが きます。 Tomodachi ga kimasu.) - My friend "
  "comes. 6. 帰る (かえる, kaeru) return. 六時に 帰ります。 (ろくじに "
  "かえります。 Roku-ji ni kaerimasu.) - I return at six. 7. 食べる (たべる, "
  "taberu) eat. 朝ご飯を 食べます。 (あさごはんを たべます。 Asagohan o "
  "tabemasu.) - I eat breakfast. 8. 飲む (のむ, nomu) drink. コーヒーを "
  "飲みます。 (こーひーを のみます。 Koohii o nomimasu.) - I drink coffee. 9. "
  "見る (みる, miru) see, watch. テレビを 見ます。 (てれびを みます。 Terebi "
  "o mimasu.) - I watch TV. 10. 聞く (きく, kiku) listen, ask. 音楽を 聞きます。 "
  "(おんがくを ききます。 Ongaku o kikimasu.) - I listen to music. 11. 話す "
  "(はなす, hanasu) speak. 日本語で 話します。 (にほんごで はなします。 "
  "Nihongo de hanashimasu.) - I speak in Japanese. 12. 読む (よむ, yomu) read. "
  "本を 読みます。 (ほんを よみます。 Hon o yomimasu.) - I read a book. 13. "
  "書く (かく, kaku) write. 手紙を 書きます。 (てがみを かきます。 Tegami o "
  "kakimasu.) - I write a letter. 14. 買う (かう, kau) buy. パンを 買います。 "
  "(ぱんを かいます。 Pan o kaimasu.) - I buy bread. 15. 売る (うる, uru) "
  "sell. 車を 売ります。 (くるまを うります。 Kuruma o urimasu.) - I sell the "
  "car. 16. 作る (つくる, tsukuru) make. 晩ご飯を 作ります。 (ばんごはんを "
  "つくります。 Bangohan o tsukurimasu.) - I make dinner. 17. 働く (はたらく, "
  "hataraku) work. 会社で 働きます。 (かいしゃで はたらきます。 Kaisha de "
  "hatarakimasu.) - I work at a company. 18. 勉強する (べんきょうする, "
  "benkyou suru) study. 毎日 日本語を 勉強します。 (まいにち にほんごを "
  "べんきょうします。 Mainichi Nihongo o benkyou shimasu.) - I study Japanese "
  "every day. 19. 教える (おしえる, oshieru) teach. 先生が 英語を 教えます。 "
  "(せんせいが えいごを おしえます。 Sensei ga Eigo o oshiemasu.) - The "
  "teacher teaches English. 20. 習う (ならう, narau) learn (from someone). "
  "ピアノを 習います。 (ぴあのを ならいます。 Piano o naraimasu.) - I learn "
  "piano. 21. 会う (あう, au) meet. 駅で 友達に 会います。 (えきで ともだちに "
  "あいます。 Eki de tomodachi ni aimasu.) - I meet my friend at the station. "
  "22. 知る (しる, shiru) know, get to know. 彼の 名前を 知っています。 "
  "(かれの なまえを しっています。 Kare no namae o shitte imasu.) - I know "
  "his name. 23. 思う (おもう, omou) think. いいと 思います。 (いいと "
  "おもいます。 Ii to omoimasu.) - I think it is good. 24. 寝る (ねる, neru) "
  "sleep, go to bed. 十一時 に 寝ます。 (じゅういちじに ねます。 Juuichi-ji "
  "ni nemasu.) - I go to bed at eleven. 25. 起きる (おきる, okiru) wake up, "
  "get up. 七時に 起きます。 (しちじに おきます。 Shichi-ji ni okimasu.) - I "
  "wake up at seven."
 ),
 "how_it_works": (
  "This record gives you the engine of Japanese sentences: the verb. Every "
  "example uses the polite ます form because it is the safest default - "
  "食べます works in shops, schools, and offices alike. Notice the pattern: "
  "dictionary forms end in u-sounds (たべる, のむ, かく), and the polite form "
  "shifts the last sound to the i-row and adds ます. Japanese verbs fall into "
  "three groups - Group 1 (u-verbs like 書く), Group 2 (ru-verbs like 食べる), "
  "and the two irregulars する and 来る. Learn the dictionary form and the "
  "ます form together now; the tenses record later builds every other form "
  "from the dictionary form."
 ),
 "key_points": [
  "25 essential verbs with full translated example sentences.",
  "All examples use the polite ます form, the safe default.",
  "Three verb groups: Group 1 (u-verbs), Group 2 (ru-verbs), irregulars する and 来る.",
  "いる for living things, ある for inanimate things.",
  "Dictionary form ends in a u-sound; ます form shifts to the i-row plus ます.",
 ],
 "requirements": [
  "Core Nouns I record for the nouns these verbs act on.",
  "Practice pairing each verb with its example sentence aloud.",
  "Learn dictionary form and ます form as a pair.",
 ],
 "standards": [
  "JLPT N5 verb band.",
  "Standard polite-form conjugation rules.",
 ],
 "citations": [
  "Martin SE. A Reference Grammar of Japanese. University of Hawaii Press; 1975.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "Each verb becomes a Signature action-seal: 行く the "
  "going-seal, 食べる the eating-seal, 思う the thinking-seal. In this "
  "framing the ます ending is the seal of respect stamped on every action "
  "before it leaves the mouth - the speaker swears the action is offered "
  "politely to the listener. Group 1 verbs are the strong seals that shift "
  "their own shape, Group 2 the steady seals that simply open, and する and "
  "来る the two wild seals that answer to no pattern. This is his original "
  "framing, clearly labeled Signature-made."
 )},
# ------------------------------------------------------ 6 adjectives/adverbs
{"key": "adjadv",
 "name": "Japanese Adjectives and Adverbs",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Japanese has two adjective families. I-adjectives end in い and conjugate "
  "like verbs; na-adjectives need な before a noun and だ at the end of a "
  "sentence. 25 adjectives with sentences: 1. 大きい (おおきい, ookii) big. "
  "大きい家です。 (おおきい いえです。 Ookii ie desu.) - It is a big house. "
  "2. 小さい (ちいさい, chiisai) small. 小さい犬です。 (ちいさい いぬです。 "
  "Chiisai inu desu.) - It is a small dog. 3. 新しい (あたらしい, atarashii) "
  "new. 新しい本です。 (あたらしい ほんです。 Atarashii hon desu.) - It is a "
  "new book. 4. 古い (ふるい, furui) old. 古い町です。 (ふるい まちです。 "
  "Furui machi desu.) - It is an old town. 5. 高い (たかい, takai) high, "
  "expensive. 高い山です。 (たかい やまです。 Takai yama desu.) - It is a "
  "high mountain. 6. 安い (やすい, yasui) cheap. 安い店です。 (やすい みせです。 "
  "Yasui mise desu.) - It is a cheap shop. 7. 暑い (あつい, atsui) hot "
  "(weather). 今日は 暑いです。 (きょうは あついです。 Kyou wa atsui desu.) "
  "- Today is hot. 8. 寒い (さむい, samui) cold (weather). 冬は 寒いです。 "
  "(ふゆは さむいです。 Fuyu wa samui desu.) - Winter is cold. 9. 美味しい "
  "(おいしい, oishii) delicious. このケーキは 美味しいです。 (このけーきは "
  "おいしいです。 Kono keeki wa oishii desu.) - This cake is delicious. 10. "
  "忙しい (いそがしい, isogashii) busy. 今週は 忙しいです。 (こんしゅうは "
  "いそがしいです。 Konshuu wa isogashii desu.) - This week is busy. 11. 楽しい "
  "(たのしい, tanoshii) fun. 旅行は 楽しかったです。 (りょこうは たのしかったです。 "
  "Ryokou wa tanoshikatta desu.) - The trip was fun. 12. 悲しい (かなしい, "
  "kanashii) sad. 悲しい映画です。 (かなしい えいがです。 Kanashii eiga "
  "desu.) - It is a sad movie. 13. 嬉しい (うれしい, ureshii) happy, glad. "
  "とても 嬉しいです。 (とても うれしいです。 Totemo ureshii desu.) - I am "
  "very happy. 14. 近い (ちかい, chikai) near. 駅は 近いです。 (えきは "
  "ちかいです。 Eki wa chikai desu.) - The station is near. 15. 遠い (とおい, "
  "tooi) far. 学校は 遠いです。 (がっこうは とおいです。 Gakkou wa tooi "
  "desu.) - The school is far. 16. 速い (はやい, hayai) fast. 速い電車です。 "
  "(はやい でんしゃです。 Hayai densha desu.) - It is a fast train. 17. 遅い "
  "(おそい, osoi) slow, late. 遅いバスです。 (おそい ばすです。 Osoi basu "
  "desu.) - It is a slow bus. 18. 明るい (あかるい, akarui) bright. 明るい部屋です。 "
  "(あかるい へやです。 Akarui heya desu.) - It is a bright room. 19. 暗い "
  "(くらい, kurai) dark. 暗い道です。 (くらい みちです。 Kurai michi desu.) "
  "- It is a dark road. 20. 強い (つよい, tsuyoi) strong. 強い風です。 "
  "(つよい かぜです。 Tsuyoi kaze desu.) - It is a strong wind. 21. 弱い "
  "(よわい, yowai) weak. 弱いチームです。 (よわい ちーむです。 Yowai chiimu "
  "desu.) - It is a weak team. 22. 有名 (ゆうめい, yuumei) famous [na]. 有名な "
  "歌手です。 (ゆうめいな かしゅです。 Yuumei na kashu desu.) - She is a "
  "famous singer. 23. 親切 (しんせつ, shinsetsu) kind [na]. 親切な人です。 "
  "(しんせつな ひとです。 Shinsetsu na hito desu.) - He is a kind person. 24. "
  "元気 (げんき, genki) healthy, energetic [na]. 元気な子どもです。 (げんきな "
  "こどもです。 Genki na kodomo desu.) - She is a healthy child. 25. 静か "
  "(しずか, shizuka) quiet [na]. 静かな町です。 (しずかな まちです。 Shizuka "
  "na machi desu.) - It is a quiet town. Adverbs (15) with sentences: とても "
  "(totemo) very - とても 大きいです。(とても おおきいです。 Totemo ookii "
  "desu.) Very big. すごく (sugoku) very - すごく 暑いです。(すごく あついです。 "
  "Sugoku atsui desu.) Very hot. あまり (amari) not much - あまり 高くないです。"
  "(あまり たかくないです。 Amari takakunai desu.) Not very expensive. 全然 "
  "(ぜんぜん, zenzen) not at all - 全然 難しくないです。(ぜんぜん むずかしくないです。 "
  "Zenzen muzukashikunai desu.) Not difficult at all. もう (mou) already - "
  "もう 食べました。(もう たべました。 Mou tabemashita.) I already ate. まだ "
  "(mada) still - まだ 学生です。(まだ がくせいです。 Mada gakusei desu.) "
  "Still a student. いつも (itsumo) always - いつも 忙しいです。(いつも "
  "いそがしいです。 Itsumo isogashii desu.) Always busy. よく (yoku) often - "
  "よく 来ます。(よく きます。 Yoku kimasu.) Comes often. ときどき "
  "(tokidoki) sometimes - ときどき 泳ぎます。(ときどき およぎます。 Tokidoki "
  "oyogimasu.) I swim sometimes. ゆっくり (yukkuri) slowly - ゆっくり 話して "
  "ください。(ゆっくり はなして ください。 Yukkuri hanashite kudasai.) "
  "Please speak slowly. はやく (hayaku) quickly - はやく 来て ください。"
  "(はやく きて ください。 Hayaku kite kudasai.) Please come quickly. たくさん "
  "(takusan) a lot - たくさん 食べました。(たくさん たべました。 Takusan "
  "tabemashita.) I ate a lot. 少し (すこし, sukoshi) a little - 少し 休みます。"
  "(すこし やすみます。 Sukoshi yasumimasu.) I will rest a little. ぜひ (zehi) "
  "by all means - ぜひ 来て ください。(ぜひ きて ください。 Zehi kite "
  "kudasai.) Please come by all means. きっと (kitto) surely - きっと 上手に "
  "なります。(きっと じょうずに なります。 Kitto jouzu ni narimasu.) You will "
  "surely improve. Rules: i-adjective + noun directly (大きい家); na-adjective "
  "+ な + noun (有名な歌手); i-adjective past: い to かった (楽しかった); "
  "na-adjective past: だった (静かだった); i-adjective to adverb: い to く "
  "(はやく); na-adjective to adverb: に (しずかに)."
 ),
 "how_it_works": (
  "This record teaches description in two moves. First, sort every adjective "
  "into its family on sight: ends in い (with the one famous exception きれい, "
  "which is na) means i-family; everything else is na-family. Second, apply "
  "the family rule: i-adjectives touch the noun directly and conjugate by "
  "themselves, na-adjectives need な before a noun and だ or です at the "
  "sentence end. Adverbs are simpler - most never change form, they just sit "
  "before the word they color. The adverb rule is one line: i-adjective minus "
  "い plus く, na-adjective plus に."
 ),
 "key_points": [
  "Two families: i-adjectives (大きい) and na-adjectives (有名な).",
  "I-adjectives attach directly to nouns; na-adjectives need な.",
  "I-adjective past: かった; na-adjective past: だった.",
  "I-adjective to adverb: く; na-adjective to adverb: に.",
  "15 adverbs with sentences: time, degree, frequency, manner.",
  "あまり and 全然 pair with negatives.",
 ],
 "requirements": [
  "Core Nouns I and Core Verbs I records.",
  "Sort each new adjective into i-family or na-family on sight.",
  "Drill the く/に adverb rule until automatic.",
 ],
 "standards": [
  "JLPT N5 adjective and adverb band.",
  "Standard i/na conjugation rules.",
 ],
 "citations": [
  "Tsujimura N. An Introduction to Japanese Linguistics. 4th ed. Wiley-Blackwell; 2023.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "Adjectives become Signature color-seals: the i-family "
  "the seals that change their own shape to fit the sentence, the na-family "
  "the seals that call for the bridge-word な before they touch a noun. "
  "Adverbs are the seasoning-seals, dusted over verbs to change their flavor "
  "- とても the more-seal, ゆっくり the slow-seal. In this framing every "
  "description is a small ceremony of fitting the right seal to the right "
  "thing, and a wrong seal (a na-adjective used bare) breaks the oath of "
  "precision. This is his original framing, clearly labeled Signature-made."
 )},
# ----------------------------------------------------------------- 7 pronouns
{"key": "pronouns",
 "name": "Japanese Pronouns: I, You, This, That, Who",
 "group": "Foundations", "ladder_rank": 4, "ladder_tier": "foundations",
 "description": (
  "Japanese pronouns carry social meaning: who you are talking to changes "
  "which word you may use. Personal pronouns: わたし (watashi) I, polite, used "
  "by everyone - わたしは 学生です。(わたしは がくせいです。 Watashi wa "
  "gakusei desu.) I am a student. わたくし (watakushi) I, very formal - "
  "わたくしは 田中と 申します。(わたくしは たなかと もうします。 Watakushi wa "
  "Tanaka to moushimasu.) I am called Tanaka. ぼく (boku) I, used by boys and "
  "young men, casual-polite - ぼくは サッカーが 好きです。(ぼくは さっかーが "
  "すきです。 Boku wa sakkaa ga suki desu.) I like soccer. おれ (ore) I, rough "
  "male speech, close friends only - おれは 行かない。(おれは いかない。 Ore "
  "wa ikanai.) I am not going. あたし (atashi) I, casual female speech - "
  "あたしは コーヒーにする。(あたしは こーひーにする。 Atashi wa koohii ni "
  "suru.) I will have coffee. あなた (anata) you, polite but distant - あなたは "
  "先生ですか。(あなたは せんせいですか。 Anata wa sensei desu ka.) Are you a "
  "teacher. Note: Japanese usually avoids you and uses the name plus さん. "
  "きみ (kimi) you, familiar, to juniors or intimates - きみは 来るかい。"
  "(きみは くるかい。 Kimi wa kuru kai.) Are you coming. おまえ (omae) you, "
  "rough, close male friends - おまえも 来い。(おまえも こい。 Omae mo koi.) "
  "You come too. かれ (kare) he - かれは 友達です。(かれは ともだちです。 Kare "
  "wa tomodachi desu.) He is a friend. かのじょ (kanojo) she - かのじょは "
  "学生です。(かのじょは がくせいです。 Kanojo wa gakusei desu.) She is a "
  "student. Possession uses の: わたしの本 (わたしの ほん, watashi no hon) my "
  "book; あなたの車 (あなたの くるま, anata no kuruma) your car; かれの家 "
  "(かれの いえ, kare no ie) his house. Demonstratives follow the ko-so-a-do "
  "system - near me, near you, far from both, question: これ (kore) this one - "
  "これは 本です。(これは ほんです。 Kore wa hon desu.) This is a book. それ "
  "(sore) that one near you - それは 何ですか。(それは なんですか。 Sore wa "
  "nan desu ka.) What is that. あれ (are) that one over there - あれは 富士山です。"
  "(あれは ふじさんです。 Are wa Fujisan desu.) That is Mt. Fuji. どれ (dore) "
  "which one - どれが いいですか。(どれが いいですか。 Dore ga ii desu ka.) "
  "Which one is good. この/その/あの/どの come before nouns: この本 (この ほん, "
  "kono hon) this book; その店 (その みせ, sono mise) that shop; あの人 (あの "
  "ひと, ano hito) that person; どの電車 (どの でんしゃ, dono densha) which "
  "train. ここ/そこ/あそこ/どこ are places: ここは 東京です。(ここは とうきょうです。 "
  "Koko wa Toukyou desu.) This place is Tokyo. どこに 行きますか。(どこに "
  "いきますか。 Doko ni ikimasu ka.) Where are you going. こちら/そちら/あちら/"
  "どちら are the polite forms: こちらは 田中です。(こちらは たなかです。 "
  "Kochira wa Tanaka desu.) This is Tanaka (introducing oneself). Interrogatives: "
  "だれ (dare) who - だれですか。(だれですか。 Dare desu ka.) Who is it. なに "
  "(nani) / なん (nan) what - これは 何ですか。(これは なんですか。 Kore wa "
  "nan desu ka.) What is this. いつ (itsu) when - いつ 来ますか。(いつ きますか。 "
  "Itsu kimasu ka.) When are you coming. どう (dou) how - どう 思いますか。"
  "(どう おもいますか。 Dou omoimasu ka.) What do you think. なぜ (naze) why - "
  "なぜ 遅いのですか。(なぜ おそいのですか。 Naze osoi no desu ka.) Why are "
  "you late. いくつ (ikutsu) how many - いくつ ありますか。(いくつ ありますか。 "
  "Ikutsu arimasu ka.) How many are there."
 ),
 "how_it_works": (
  "This record teaches pronouns as social tools, not just word swaps. Rule "
  "one: default to わたし for I and to the listener's name plus さん for you - "
  "these two choices are never wrong. Rule two: the ko-so-a-do compass always "
  "points from the speaker - ko is near me, so is near you, a is far from us "
  "both, do asks the question. Rule three: れ-words (これ/それ/あれ) stand "
  "alone, の-words (この/その/あの) must touch a noun, こ-words (ここ/そこ/"
  "あそこ) are places. Master these three rules and every pointing word in "
  "Japanese falls into place."
 ),
 "key_points": [
  "I-words rank by formality: わたくし > わたし > ぼく/あたし > おれ.",
  "Default safe choices: わたし for I, name plus さん for you.",
  "Ko-so-a-do compass: ko near me, so near you, a far, do question.",
  "これ/それ/あれ stand alone; この/その/あの need a noun; ここ/そこ/あそこ are places.",
  "Possession is always の: わたしの本 my book.",
  "こちら/そちら/あちら are the polite pointing words.",
 ],
 "requirements": [
  "Adjectives and Adverbs record for describing the people and things pointed at.",
  "Practice the ko-so-a-do compass with real objects in the room.",
  "Never use おれ or おまえ outside close friendships.",
 ],
 "standards": [
  "JLPT N5 pronoun band.",
  "Standard keigo-adjacent usage notes.",
 ],
 "citations": [
  "Shibatani M. The Languages of Japan. Cambridge University Press; 1990.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "Pronouns become Signature position-seals: each one swears "
  "where the speaker stands - socially and in space. わたし is the "
  "neutral-ground seal anyone may plant; ぼく and おれ are seals only certain "
  "speakers may raise; あなた is the far-standing seal, respectful but "
  "distant. The ko-so-a-do compass is the Signature pointing ritual: the "
  "speaker plants a flag at their own feet and every これ and あれ is measured "
  "from that flag. To point wrongly in this framing is to misplace yourself "
  "in the room. This is his original framing, clearly labeled Signature-made."
 )},
# ------------------------------------------------------------ 8 numbers & time
{"key": "numbers",
 "name": "Japanese Numbers and Time",
 "group": "Foundations", "ladder_rank": 4, "ladder_tier": "foundations",
 "description": (
  "Numbers: 1 いち (ichi), 2 に (ni), 3 さん (san), 4 し/よん (shi/yon), 5 ご "
  "(go), 6 ろく (roku), 7 しち/なな (shichi/nana), 8 はち (hachi), 9 きゅう "
  "(kyuu), 10 じゅう (juu). Teens add to ten: 11 じゅういち (juuichi), 12 "
  "じゅうに (juuni), 19 じゅうきゅう (juukyuu). Tens multiply ten: 20 にじゅう "
  "(nijuu), 30 さんじゅう (sanjuu), 90 きゅうじゅう (kyuujuu). 21 is にじゅういち "
  "(nijuuichi), 99 is きゅうじゅうきゅう (kyuujuukyuu). 100 ひゃく (hyaku), "
  "1,000 せん (sen), 10,000 まん (man) - Japanese counts in ten-thousands, so "
  "100,000 is じゅうまん (juuman). Kanji numerals: 一二三四五六七八九十百千万. "
  "Example: 三百四十二 is 342 - さんびゃく よんじゅう に (sanbyaku yonjuu ni). "
  "Ordinals add 番目 (ばんめ, banme): 一番目 (いちばんめ, ichibanme) first, "
  "二番目 (にばんめ, nibanme) second. Days of the week carry the elements: "
  "月曜日 (げつようび, getsuyoubi) Monday, 火曜日 (かようび, kayoubi) Tuesday, "
  "水曜日 (すいようび, suiyoubi) Wednesday, 木曜日 (もくようび, mokuyoubi) "
  "Thursday, 金曜日 (きんようび, kinyoubi) Friday, 土曜日 (どようび, doyoubi) "
  "Saturday, 日曜日 (にちようび, nichiyoubi) Sunday. Months number the moon: "
  "一月 (いちがつ, ichigatsu) January, 二月 (にがつ, nigatsu) February, 三月 "
  "(さんがつ, sangatsu) March, 四月 (しがつ, shigatsu) April, 五月 (さつき, "
  "satsuki) May, 六月 (ろくがつ, rokugatsu) June, 七月 (しちがつ, shichigatsu) "
  "July, 八月 (はちがつ, hachigatsu) August, 九月 (くがつ, kugatsu) "
  "September, 十月 (じゅうがつ, juugatsu) October, 十一月 (じゅういちがつ, "
  "juuichigatsu) November, 十二月 (じゅうにがつ, juunigatsu) December. Seasons: "
  "春 (はる, haru) spring, 夏 (なつ, natsu) summer, 秋 (あき, aki) autumn, 冬 "
  "(ふゆ, fuyu) winter. Clock time: 時 (じ, ji) hour, 分 (ふん/ぷん, fun/pun) "
  "minute, 半 (はん, han) half: 三時 (さんじ, sanji) 3 o'clock, 三時半 "
  "(さんじはん, sanjihan) 3:30, 午前 (ごぜん, gozen) AM, 午後 (ごご, gogo) PM. "
  "Dates: 年 (ねん, nen) year, 月 (がつ, gatsu) month, 日 (にち, nichi) day: "
  "二千二十六年十月十七日 (にせん にじゅうろくねん じゅうがつ じゅうしちにち) "
  "October 17, 2026. Example sentences: 今は 三時です。(いまは さんじです。 "
  "Ima wa sanji desu.) It is 3 o'clock now. 誕生日は 五月三日です。(たんじょうびは "
  "さつき みっか です。 Tanjoubi wa satsuki mikka desu.) My birthday is May "
  "3rd. 電車は 九時半に 来ます。(でんしゃは くじはんに きます。 Densha wa "
  "kujihan ni kimasu.) The train comes at 9:30. 百円 ください。(ひゃくえん "
  "ください。 Hyaku-en kudasai.) 100 yen, please. 去年は 二千二十五年でした。"
  "(きょねんは にせん にじゅうごねんでした。 Kyonen wa nisen nijuugonen "
  "deshita.) Last year was 2025."
 ),
 "how_it_works": (
  "This record teaches counting as building with blocks: ones, then tens as "
  "multiples of じゅう, then hundreds of ひゃく, thousands of せん, and the "
  "big block まん for ten thousand - the one place Japanese and English "
  "count differently, so give まん extra practice. Time words then bolt onto "
  "the numbers: 時 for hours, 分 for minutes, 曜日 for weekdays, 月 for "
  "months, 年 for years. Read every price tag, clock, and calendar you meet "
  "aloud in Japanese and the system locks in within a week."
 ),
 "key_points": [
  "1-10: いち に さん し/よん ご ろく しち/なな はち きゅう じゅう.",
  "Tens multiply じゅう; hundreds ひゃく; thousands せん; ten-thousands まん.",
  "Kanji numerals: 一二三四五六七八九十百千万.",
  "Weekdays carry elements: moon fire water tree gold earth sun.",
  "Time: 時 hours, 分 minutes, 半 half, 午前 AM, 午後 PM.",
  "Dates read year-month-day: 年月日.",
 ],
 "requirements": [
  "Kana reading from the Writing System record.",
  "A clock and calendar for daily read-aloud practice.",
  "Extra drills on まん, the ten-thousand block.",
 ],
 "standards": [
  "JLPT N5 number and time band.",
  "Joyo kanji numeral readings.",
 ],
 "citations": [
  "Japan Foundation. Japanese Language Proficiency Test Official Practice Materials, N5.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "Numbers become Signature measure-seals: each block from "
  "いち to まん a sworn unit of counting, and まん the great ten-thousand "
  "seal where the Japanese and English measuring rods part ways. Time words "
  "are the calendar-seals - 曜日 the seven sky-seals turning the week, 月 "
  "the moon-seals numbering the year. In this framing every price spoken "
  "aloud is a small oath of exactness: the number must match the thing, seal "
  "to substance. This is his original framing, clearly labeled Signature-made."
 )},
# --------------------------------------------------------------- 9 greetings
{"key": "greetings",
 "name": "Japanese Greetings and Everyday Phrases",
 "group": "Foundations", "ladder_rank": 5, "ladder_tier": "foundations",
 "description": (
  "30 greetings, farewells, and politeness phrases with usage notes. 1. "
  "おはようございます (ohayou gozaimasu) Good morning - formal; to family "
  "say おはよう (ohayou). 2. こんにちは (konnichiwa) Hello, good afternoon - "
  "the daytime greeting. 3. こんばんは (konbanwa) Good evening. 4. おやすみなさい "
  "(oyasuminasai) Good night - to family おやすみ (oyasumi). 5. さようなら "
  "(sayounara) Goodbye - formal, implies long parting; friends say じゃあまた "
  "(jaa mata) See you. 6. はじめまして (hajimemashite) Nice to meet you - "
  "first meetings only. 7. よろしくおねがいします (yoroshiku onegaishimasu) "
  "Please treat me well - said after introductions and when asking favors. 8. "
  "ありがとうございます (arigatou gozaimasu) Thank you - casual ありがとう "
  "(arigatou). 9. どうもありがとう (doumo arigatou) Thank you very much - "
  "warm. 10. すみません (sumimasen) Excuse me, sorry - also calls a waiter "
  "and softens requests. 11. ごめんなさい (gomennasai) I am sorry - casual "
  "ごめん (gomen). 12. おねがいします (onegaishimasu) Please (requesting) - "
  "used when asking for something. 13. どうぞ (douzo) Please, go ahead - "
  "offering. 14. いらっしゃいませ (irasshaimase) Welcome (to our store) - "
  "staff to customers. 15. いただきます (itadakimasu) Said before eating - "
  "thanks for the meal received. 16. ごちそうさまでした (gochisousama deshita) "
  "Said after eating - thanks for the feast. 17. おつかれさまでした "
  "(otsukaresama deshita) Good work today - to coworkers leaving. 18. "
  "おめでとうございます (omedetou gozaimasu) Congratulations. 19. あけまして"
  "おめでとうございます (akemashite omedetou gozaimasu) Happy New Year. 20. "
  "おだいじに (odaiji ni) Get well soon - to the sick. 21. がんばって "
  "(ganbatte) Do your best - encouragement. 22. きをつけて (ki o tsukete) Take "
  "care - to someone departing. 23. ただいま (tadaima) I am home - said "
  "entering the house. 24. おかえりなさい (okaerinasai) Welcome home - the "
  "reply. 25. しつれいします (shitsurei shimasu) Excuse me (entering/leaving) "
  "- also said hanging up the phone: しつれいします. 26. おじゃまします "
  "(ojama shimasu) Sorry to intrude - entering someone's home. 27. どういたしまして "
  "(douitashimashite) You are welcome - the reply to thanks. 28. おげんきですか "
  "(ogenki desu ka) How are you - formal; friends ask げんき (genki). 29. "
  "おひさしぶりです (ohisashiburi desu) Long time no see. 30. また あした "
  "(mata ashita) See you tomorrow. Example sentences: はじめまして。田中です。"
  "よろしくおねがいします。(はじめまして。たなかです。よろしくおねがいします。 "
  "Hajimemashite. Tanaka desu. Yoroshiku onegaishimasu.) Nice to meet you. I "
  "am Tanaka. Please treat me well. すみません、トイレは どこですか。(すみません、"
  "といれは どこですか。 Sumimasen, toire wa doko desu ka.) Excuse me, where "
  "is the bathroom. いただきます。(Itadakimasu.) Said before eating. おつかれ"
  "さまでした。(Otsukaresama deshita.) Good work today."
 ),
 "how_it_works": (
  "This record teaches phrases as social keys: each one opens a specific "
  "door and fits no other. Do not translate them word by word - learn each "
  "as a fixed set phrase with its situation: いただきます belongs before the "
  "first bite, おつかれさまでした belongs at the end of the workday, すみません "
  "belongs at the start of any interruption. Practice them in pairs with the "
  "reply phrases (ただいま with おかえり, ありがとう with どういたしまして) "
  "so the call-and-response becomes reflex."
 ),
 "key_points": [
  "30 greetings, farewells, and politeness phrases with usage notes.",
  "Time-of-day set: おはようございます, こんにちは, こんばんは, おやすみなさい.",
  "Meal pair: いただきます before, ごちそうさまでした after.",
  "Home pair: ただいま entering, おかえりなさい replying.",
  "すみません covers excuse me, sorry, and getting attention.",
  "Each phrase is a fixed set phrase learned with its situation.",
 ],
 "requirements": [
  "No new grammar needed; memorize with situations.",
  "Practice call-and-response pairs aloud with a partner.",
  "Use one new phrase in real life each day.",
 ],
 "standards": [
  "JLPT N5 phrase band.",
 ],
 "citations": [
  "Japan Foundation. Japanese Language Proficiency Test Official Practice Materials, N5.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "Greetings become Signature door-seals: each phrase a "
  "sworn key that opens one exact social door - いただきます the meal-door "
  "seal, ただいま the home-door seal, おつかれさまでした the workday-door "
  "seal. In this framing politeness is not decoration but the oath-work of "
  "the language: every すみません a small bow of the voice, every ありがとう "
  "a sealed receipt for kindness given. The speaker who carries all 30 keys "
  "can enter any room in Japan. This is his original framing, clearly "
  "labeled Signature-made."
 )},
# -------------------------------------------------------- 10 grammar essentials
{"key": "grammar",
 "name": "Japanese Grammar Essentials",
 "group": "Foundations", "ladder_rank": 5, "ladder_tier": "foundations",
 "description": (
  "The skeleton of every Japanese sentence. Word order is subject-object-verb: "
  "わたしは りんごを 食べます。(わたしは りんごを たべます。 Watashi wa ringo "
  "o tabemasu.) I eat an apple - the verb always comes last. Japanese has no "
  "grammatical gender and no articles: 本 (ほん, hon) is a book or the book, "
  "and number is usually unmarked - 本 alone can mean books in context, though "
  "counters like 三冊 (さんさつ, san-satsu) pin the number down. Roles are "
  "marked by particles, the small words after nouns: は (wa) marks the topic - "
  "わたしは 学生です。(わたしは がくせいです。 Watashi wa gakusei desu.) As "
  "for me, I am a student. が (ga) marks the subject, especially new "
  "information - 猫が います。(ねこが います。 Neko ga imasu.) There is a cat. "
  "を (o) marks the direct object - 本を 読みます。(ほんを よみます。 Hon o "
  "yomimasu.) I read a book. に (ni) marks direction, time, and the indirect "
  "object - 学校に 行きます。(がっこうに いきます。 Gakkou ni ikimasu.) I go "
  "to school; 友達に あげます。(ともだちに あげます。 Tomodachi ni agemasu.) "
  "I give it to my friend. へ (e) marks direction - 東京へ 行きます。(とうきょうへ "
  "いきます。 Toukyou e ikimasu.) I go to Tokyo. で (de) marks the place of "
  "action or the means - 公園で 遊びます。(こうえんで あそびます。 Kouen de "
  "asobimasu.) I play in the park; 電車で 行きます。(でんしゃで いきます。 "
  "Densha de ikimasu.) I go by train. と (to) means with or and - 友達と "
  "行きます。(ともだちと いきます。 Tomodachi to ikimasu.) I go with my friend. "
  "も (mo) means also - わたしも 行きます。(わたしも いきます。 Watashi mo "
  "ikimasu.) I go too. から (kara) from and まで (made) until - 九時から "
  "五時まで (くじから ごじまで, kuji kara goji made) from 9 to 5. の (no) "
  "marks possession and noun connection - わたしの本 (わたしの ほん, watashi "
  "no hon) my book. Negation: plain ない and polite ません - 食べない "
  "(たべない, tabenai) do not eat; 食べません (たべません, tabemasen) do not "
  "eat (polite). Adjective negation: 高くない (たかくない, takakunai) not "
  "expensive. Questions add か at the end with rising intonation: 学生ですか。"
  "(がくせいですか。 Gakusei desu ka.) Are you a student. Answers: はい "
  "(hai) yes, いいえ (iie) no. Example sentences: これは 何ですか。(これは "
  "なんですか。 Kore wa nan desu ka.) What is this. どこで 買いましたか。"
  "(どこで かいましたか。 Doko de kaimashita ka.) Where did you buy it. "
  "明日は 雨です。(あしたは あめです。 Ashita wa ame desu.) Tomorrow is rain "
  "(it will rain tomorrow). 肉を 食べません。(にくを たべません。 Niku o "
  "tabemasen.) I do not eat meat."
 ),
 "how_it_works": (
  "This record teaches grammar as plumbing: the verb is the drain at the end "
  "of the sentence, and the particles are the pipes that carry each noun to "
  "its job. Build sentences in three steps: pick the verb and put it last, "
  "mark the doer with は or が, mark the receiver with を, に, へ, or で. "
  "Then flip the switches: add か for a question, swap ます for ません for "
  "polite negation. Drill the ten particles until you can hear the wrong one "
  "- は versus が is the pair to master, and the rule of thumb is は for the "
  "topic you keep talking about, が for the new thing you just introduced."
 ),
 "key_points": [
  "Word order is subject-object-verb; the verb always comes last.",
  "No gender, no articles; number usually unmarked.",
  "Ten core particles: は が を に へ で と も から/まで の.",
  "は marks the topic; が marks the subject as new information.",
  "Polite negation: ません; plain negation: ない.",
  "Questions: add か with rising intonation; answers はい/いいえ.",
 ],
 "requirements": [
  "All vocabulary records so far, for sentence building material.",
  "Particle drills: build 5 sentences per particle.",
  "Master the は versus が distinction with contrast pairs.",
 ],
 "standards": [
  "JLPT N5 grammar band.",
  "Standard particle usage.",
 ],
 "citations": [
  "Kuno S. The Structure of the Japanese Language. MIT Press; 1973.",
  "Martin SE. A Reference Grammar of Japanese. University of Hawaii Press; 1975.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "Grammar becomes the Signature bridge-work: the verb the "
  "keystone set last so the whole arch holds, the particles the sworn cables "
  "binding each noun to its load - は the topic-cable, を the object-cable, "
  "に the direction-cable. In this framing a sentence is a small bridge the "
  "speaker builds for the listener to cross, and a misplaced particle is a "
  "cable tied to the wrong pier. Negation is the drawbridge raised, か the "
  "gate-bell rung for an answer. This is his original framing, clearly "
  "labeled Signature-made."
 )},
# -------------------------------------------------------------- 11 home & family
{"key": "home",
 "name": "Japanese Home and Family Sentences",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "20 sentences about the house, rooms, furniture, and family members. 1. "
  "これは わたしの 家です。(これは わたしの いえです。 Kore wa watashi no ie "
  "desu.) This is my house. 2. 家は 駅の 近くに あります。(いえは えきの "
  "ちかくに あります。 Ie wa eki no chikaku ni arimasu.) The house is near "
  "the station. 3. リビングは 広いです。(りびんぐは ひろいです。 Ribingu wa "
  "hiroi desu.) The living room is spacious. 4. 台所で 料理を します。(だいどころで "
  "りょうりを します。 Daidokoro de ryouri o shimasu.) I cook in the kitchen. "
  "5. 寝室は 二階に あります。(しんしつは にかいに あります。 Shinshitsu wa "
  "nikai ni arimasu.) The bedroom is on the second floor. 6. お風呂は 毎日 "
  "入ります。(おふろは まいにち はいります。 Ofuro wa mainichi hairimasu.) I "
  "take a bath every day. 7. トイレは どこですか。(といれは どこですか。 Toire "
  "wa doko desu ka.) Where is the bathroom. 8. 玄関で 靴を 脱ぎます。(げんかんで "
  "くつを ぬぎます。 Genkan de kutsu o nugimasu.) I take off my shoes at the "
  "entrance. 9. 居間には ソファが あります。(いまには そふぁが あります。 Ima "
  "ni wa sofa ga arimasu.) There is a sofa in the living room. 10. 机の上に "
  "本が あります。(つくえのうえに ほんが あります。 Tsukue no ue ni hon ga "
  "arimasu.) There is a book on the desk. 11. 父は 会社員です。(ちちは かいしゃいんです。 "
  "Chichi wa kaishain desu.) My father is an office worker. 12. 母は 料理が "
  "上手です。(ははは りょうりが じょうずです。 Haha wa ryouri ga jouzu desu.) "
  "My mother is good at cooking. 13. 兄は 大学生です。(あには だいがくせいです。 "
  "Ani wa daigakusei desu.) My older brother is a college student. 14. 妹は "
  "高校生です。(いもうとは こうこうせいです。 Imouto wa koukousei desu.) My "
  "younger sister is a high school student. 15. 祖父は 元気です。(そふは "
  "げんきです。 Sofu wa genki desu.) My grandfather is healthy. 16. 祖母と "
  "一緒に 住んでいます。(そぼと いっしょに すんでいます。 Sobo to issho ni "
  "sunde imasu.) I live with my grandmother. 17. 家族は 五人です。(かぞくは "
  "ごにんです。 Kazoku wa go-nin desu.) There are five in my family. 18. 子ども部屋は "
  "明るいです。(こどもべやは あかるいです。 Kodomobeya wa akarui desu.) The "
  "child's room is bright. 19. 庭に 花が 咲いています。(にわに はなが さいています。 "
  "Niwa ni hana ga saite imasu.) Flowers are blooming in the garden. 20. 毎晩 "
  "家族で ご飯を 食べます。(まいばん かぞくで ごはんを たべます。 Maiban "
  "kazoku de gohan o tabemasu.) Every evening I eat dinner with my family."
 ),
 "how_it_works": (
  "This record moves the ladder from single words to lived-in sentences: the "
  "foundations gave you nouns, verbs, and particles, and now those parts "
  "assemble into the rooms of a house and the members of a family. Notice the "
  "humble forms for your own family (父 chichi, 母 haha) versus the polite "
  "forms for someone else's (お父さん otousan, お母さん okaasan) - Japanese "
  "lowers your own and raises the other's. Read each sentence, picture the "
  "room or person, and say it aloud; the home is the first territory where "
  "the language must live."
 ),
 "key_points": [
  "20 sentences: house, rooms, furniture, family members.",
  "Room words: リビング, 台所, 寝室, お風呂, 玄関, 居間, 庭.",
  "Own family: 父, 母, 兄, 妹, 祖父, 祖母; others' family adds お-さん.",
  "Location pattern: placeに あります for existence.",
  "Action-at-place pattern: placeで verb for where you do things.",
 ],
 "requirements": [
  "Grammar Essentials record for particles に, で, の.",
  "Draw a floor plan and label each room in Japanese.",
  "Say all 20 sentences aloud in order.",
 ],
 "standards": [
  "JLPT N5 sentence band.",
 ],
 "citations": [
  "Japan Foundation. Japanese Language Proficiency Test Official Practice Materials, N5.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "The home becomes the Signature first territory: each "
  "room a sealed chamber of the language - 台所 the fire-seal room, 寝室 the "
  "rest-seal room, 玄関 the threshold-seal where shoes and the outside world "
  "are set down. Family words are rank-seals: your own family spoken low with "
  "父 and 母, another's raised with お父さん and お母さん, the humility "
  "itself a sworn oath of respect. In this framing the learner does not study "
  "the house, they take possession of it room by room. This is his original "
  "framing, clearly labeled Signature-made."
 )},
# ------------------------------------------------------------ 12 food & cooking
{"key": "food",
 "name": "Japanese Food and Cooking Sentences",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "20 sentences about meals, ingredients, cooking actions, and restaurants. "
  "1. 朝ご飯に パンを 食べます。(あさごはんに ぱんを たべます。 Asagohan ni "
  "pan o tabemasu.) I eat bread for breakfast. 2. 昼ご飯は うどんです。(ひるごはんは "
  "うどんです。 Hirugohan wa udon desu.) Lunch is udon noodles. 3. 晩ご飯を "
  "作ります。(ばんごはんを つくります。 Bangohan o tsukurimasu.) I make "
  "dinner. 4. 味噌汁は 熱いです。(みそしるは あついです。 Misoshiru wa atsui "
  "desu.) The miso soup is hot. 5. この寿司は 新鮮です。(このすしは しんせんです。 "
  "Kono sushi wa shinsen desu.) This sushi is fresh. 6. 野菜を 切ります。(やさいを "
  "きります。 Yasai o kirimasu.) I cut the vegetables. 7. 肉を 焼きます。(にくを "
  "やきます。 Niku o yakimasu.) I grill the meat. 8. ご飯を 炊きます。(ごはんを "
  "たきます。 Gohan o takimasu.) I cook rice. 9. 卵を ゆでます。(たまごを "
  "ゆでます。 Tamago o yudemasu.) I boil eggs. 10. 塩を 少し 入れます。(しおを "
  "すこし いれます。 Shio o sukoshi iremasu.) I add a little salt. 11. 醤油の "
  "味が します。(しょうゆの あじが します。 Shouyu no aji ga shimasu.) It "
  "tastes of soy sauce. 12. レストランで 晩ご飯を 食べました。(れすとらんで "
  "ばんごはんを たべました。 Resutoran de bangohan o tabemashita.) I ate "
  "dinner at a restaurant. 13. メニューを 見せて ください。(めにゅーを みせて "
  "ください。 Menyu o misete kudasai.) Please show me the menu. 14. これを "
  "ください。(これを ください。 Kore o kudasai.) This one, please. 15. お水を "
  "ください。(おみずを ください。 Omizu o kudasai.) Water, please. 16. お会計を "
  "おねがいします。(おかいけいを おねがいします。 Okaikei o onegaishimasu.) "
  "The bill, please. 17. とても 美味しかったです。(とても おいしかったです。 "
  "Totemo oishikatta desu.) It was very delicious. 18. 辛い物は 苦手です。(からい "
  "ものは にがてです。 Karai mono wa nigate desu.) I am not good with spicy "
  "food. 19. 母の カレーが 一番 好きです。(ははの かれーが いちばん すきです。 "
  "Haha no karee ga ichiban suki desu.) I like my mother's curry best. 20. "
  "いただきます。(Itadakimasu.) Said before eating - I humbly receive."
 ),
 "how_it_works": (
  "This record teaches the kitchen as a verb laboratory: 切る cut, 焼く "
  "grill, 炊く cook rice, ゆでる boil, 入れる put in - five cooking verbs that "
  "cover nearly every recipe. Pair them with the restaurant frame: ordering "
  "is just これをください (this, please) pointed at anything, and paying is "
  "お会計をおねがいします. The meal words 朝ご飯/昼ご飯/晩ご飯 lock the "
  "three daily anchors. Cook one Japanese dish while narrating each step "
  "aloud and the verbs stop being vocabulary and become muscle memory."
 ),
 "key_points": [
  "20 sentences: meals, ingredients, cooking actions, restaurant.",
  "Five core cooking verbs: 切る, 焼く, 炊く, ゆでる, 入れる.",
  "Meals: 朝ご飯 breakfast, 昼ご飯 lunch, 晩ご飯 dinner.",
  "Restaurant frame: メニューを見せてください, これをください, お会計をおねがいします.",
  "Taste words: 美味しい, 辛い, 塩, 醤油, 新鮮.",
 ],
 "requirements": [
  "Core Verbs I record for the cooking verbs.",
  "Cook one Japanese dish while narrating steps aloud.",
  "Practice the restaurant frame as a role-play.",
 ],
 "standards": [
  "JLPT N5 sentence band.",
 ],
 "citations": [
  "Japan Foundation. Japanese Language Proficiency Test Official Practice Materials, N5.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "The kitchen becomes the Signature transformation chamber: "
  "raw ingredients enter and sworn dishes leave, each cooking verb a seal of "
  "change - 切る the dividing seal, 焼く the fire seal, 炊く the steam seal. "
  "The restaurant is the exchange hall where これをください, the pointing "
  "oath, trades words for food, and いただきます is the receipt-seal sworn "
  "before the first bite. In this framing the cook does not follow steps, "
  "they keep the oaths of heat, salt, and timing. This is his original "
  "framing, clearly labeled Signature-made."
 )},
# ------------------------------------------------------- 13 travel & directions
{"key": "travel",
 "name": "Japanese Travel and Directions Sentences",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "20 sentences about transport, asking directions, tickets, and lodging. 1. "
  "駅は どこですか。(えきは どこですか。 Eki wa doko desu ka.) Where is the "
  "station. 2. トイレは どこに ありますか。(といれは どこに ありますか。 Toire "
  "wa doko ni arimasu ka.) Where is the bathroom. 3. この電車は 新宿に 行きますか。"
  "(このでんしゃは しんじゅくに いきますか。 Kono densha wa Shinjuku ni "
  "ikimasu ka.) Does this train go to Shinjuku. 4. 切符を 二枚 ください。(きっぷを "
  "にまい ください。 Kippu o ni-mai kudasai.) Two tickets, please. 5. 東京まで "
  "いくらですか。(とうきょうまで いくらですか。 Toukyou made ikura desu ka.) "
  "How much is it to Tokyo. 6. 右に 曲がって ください。(みぎに まがって "
  "ください。 Migi ni magatte kudasai.) Please turn right. 7. 左の 角を 曲がります。"
  "(ひだりの かどを まがります。 Hidari no kado o magarimasu.) I turn at the "
  "left corner. 8. まっすぐ 行って ください。(まっすぐ いって ください。 "
  "Massugu itte kudasai.) Please go straight. 9. 信号を 渡ります。(しんごうを "
  "わたります。 Shingou o watarimasu.) I cross at the traffic light. 10. バス停は "
  "あそこです。(ばすていは あそこです。 Basutei wa asoko desu.) The bus stop "
  "is over there. 11. タクシーで 行きます。(たくしーで いきます。 Takushii de "
  "ikimasu.) I go by taxi. 12. 空港まで 三十分 かかります。(くうこうまで "
  "さんじゅっぷん かかります。 Kuukou made sanjuppun kakarimasu.) It takes 30 "
  "minutes to the airport. 13. 新幹線の 予約を しました。(しんかんせんの "
  "よやくを しました。 Shinkansen no yoyaku o shimashita.) I reserved a "
  "Shinkansen seat. 14. ホテルに チェックイン します。(ほてるに ちぇっくいん "
  "します。 Hoteru ni chekkuin shimasu.) I check in at the hotel. 15. 部屋の "
  "鍵を ください。(へやの かぎを ください。 Heya no kagi o kudasai.) The room "
  "key, please. 16. 朝食は 何時からですか。(ちょうしょくは なんじからですか。 "
  "Choushoku wa nanji kara desu ka.) From what time is breakfast. 17. 地図を "
  "見せて ください。(ちずを みせて ください。 Chizu o misete kudasai.) Please "
  "show me the map. 18. ここから 歩いて 五分です。(ここから あるいて ごふんです。 "
  "Koko kara aruite gofun desu.) It is five minutes on foot from here. 19. "
  "道に 迷いました。(みちに まよいました。 Michi ni mayoimashita.) I am lost. "
  "20. 助けて ください。(たすけて ください。 Tasukete kudasai.) Please help me."
 ),
 "how_it_works": (
  "This record is a survival kit: 20 sentences that get a traveler fed, "
  "housed, and pointed the right way. The asking frame is always the same - "
  "placeはどこですか for where, いくらですか for how much, ください for "
  "please give me - so you can swap any noun into the frame and be "
  "understood. Direction words 右 (みぎ right), 左 (ひだり left), まっすぐ "
  "(straight), 角 (かど corner) combine into any route. Memorize the kit in "
  "order, then practice by navigating your own neighborhood in Japanese."
 ),
 "key_points": [
  "20 sentences: transport, directions, tickets, lodging.",
  "Asking frame: placeはどこですか; いくらですか; nounをください.",
  "Direction words: 右, 左, まっすぐ, 角, 信号.",
  "Transport: 電車, バス, タクシー, 新幹線, 空港.",
  "Lodging: ホテル, 予約, チェックイン, 鍵, 朝食.",
 ],
 "requirements": [
  "Numbers and Time record for fares and schedules.",
  "Practice navigating your neighborhood in Japanese.",
  "Role-play the ticket counter and hotel desk.",
 ],
 "standards": [
  "JLPT N5 sentence band.",
 ],
 "citations": [
  "Japan Foundation. Japanese Language Proficiency Test Official Practice Materials, N5.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "Travel becomes the Signature wayfinding oath: every "
  "どこですか a compass-seal cast into the unknown, every まっすぐ a "
  "straight-line vow, every 切符 a passage-seal bought with exact coin. The "
  "traveler in this framing does not wander - they lay a trail of sworn "
  "questions, and each answered question is a bridge plank over unfamiliar "
  "ground. 道に迷いました is the honest signal that the trail needs "
  "re-laying, and 助けてください the call for a fellow traveler. This is his "
  "original framing, clearly labeled Signature-made."
 )},
# ------------------------------------------------------------ 14 work & school
{"key": "workschool",
 "name": "Japanese Work and School Sentences",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "20 sentences about jobs, the office, the classroom, and learning. 1. わたしは "
  "先生です。(わたしは せんせいです。 Watashi wa sensei desu.) I am a teacher. "
  "2. 会社で 働いています。(かいしゃで はたらいています。 Kaisha de "
  "hataraite imasu.) I work at a company. 3. 毎朝 九時に 出社します。(まいあさ "
  "くじに しゅっしゃします。 Maiasa kuji ni shussha shimasu.) I arrive at the "
  "office at nine every morning. 4. 会議は 十時からです。(かいぎは じゅうじからです。 "
  "Kaigi wa juuji kara desu.) The meeting is from ten. 5. 書類を コピーして "
  "ください。(しょるいを こぴーして ください。 Shorui o kopii shite kudasai.) "
  "Please copy the documents. 6. メールを 送りました。(めーるを おくりました。 "
  "Meeru o okurimashita.) I sent the email. 7. 上司に 報告します。(じょうしに "
  "ほうこくします。 Joushi ni houkoku shimasu.) I report to my boss. 8. 残業が "
  "多いです。(ざんぎょうが おおいです。 Zangyou ga ooi desu.) There is a lot "
  "of overtime. 9. 休憩を 取りましょう。(きゅうけいを とりましょう。 Kyuukei o "
  "torimashou.) Let us take a break. 10. お先に 失礼します。(おさきに しつれいします。 "
  "Osaki ni shitsurei shimasu.) Excuse me for leaving first. 11. 学校は 八時半に "
  "始まります。(がっこうは はちじはんに はじまります。 Gakkou wa hachijihan "
  "ni hajimarimasu.) School starts at 8:30. 12. 授業は 楽しいです。(じゅぎょうは "
  "たのしいです。 Jugyou wa tanoshii desu.) The lessons are fun. 13. 宿題を "
  "忘れました。(しゅくだいを わすれました。 Shukudai o wasuremashita.) I "
  "forgot my homework. 14. 先生に 質問します。(せんせいに しつもんします。 "
  "Sensei ni shitsumon shimasu.) I ask the teacher a question. 15. 友達と "
  "一緒に 勉強します。(ともだちと いっしょに べんきょうします。 Tomodachi to "
  "issho ni benkyou shimasu.) I study with my friends. 16. 試験は 来週です。"
  "(しけんは らいしゅうです。 Shiken wa raishuu desu.) The exam is next week. "
  "17. 図書館で 本を 借ります。(としょかんで ほんを かります。 Toshokan de hon "
  "o karimasu.) I borrow books at the library. 18. 漢字を 練習します。(かんじを "
  "れんしゅうします。 Kanji o renshuu shimasu.) I practice kanji. 19. 成績が "
  "上がりました。(せいせきが あがりました。 Seiseki ga agarimashita.) My "
  "grades improved. 20. 卒業したら 先生に なります。(そつぎょうしたら せんせいに "
  "なります。 Sotsugyou shitara sensei ni narimasu.) After graduating I will "
  "become a teacher."
 ),
 "how_it_works": (
  "This record teaches the two great daytime worlds - office and classroom - "
  "as sentence patterns you can reuse forever. The office runs on "
  "request-and-report: してください for asking, しました for reporting done, "
  "お先に失礼します for leaving. The school runs on the learning cycle: "
  "勉強します, 質問します, 練習します, 上がりました. Notice how ます/ました "
  "carry the whole politeness load at work and school - the plain forms from "
  "the verbs record would sound rough here. Shadow these sentences before "
  "work or class and the day starts in Japanese."
 ),
 "key_points": [
  "20 sentences: jobs, office, classroom, learning.",
  "Office frame: requests with してください, reports with しました.",
  "Leaving phrase: お先に失礼します.",
  "School cycle: 勉強します, 質問します, 練習します, 上がりました.",
  "Polite ます/ました forms suit work and school.",
 ],
 "requirements": [
  "Core Verbs I and Grammar Essentials records.",
  "Shadow the sentences before work or class.",
  "Write a one-day diary in Japanese using the frames.",
 ],
 "standards": [
  "JLPT N5-N4 sentence band.",
 ],
 "citations": [
  "Japan Foundation. Japanese Language Proficiency Test Official Practice Materials, N5.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "Work and school become the Signature day-oath grounds: "
  "the office a hall of sworn exchanges - 報告します the report-seal, お先に"
  "失礼します the departure-seal - and the classroom a forge where 勉強します "
  "is the hammer-seal struck daily. In this framing every workday is a "
  "circuit of small oaths kept: arrive, report, request, complete, depart. "
  "The student keeps the same circuit with books instead of briefcases. This "
  "is his original framing, clearly labeled Signature-made."
 )},
# ------------------------------------------------------------ 15 health & body
{"key": "health",
 "name": "Japanese Health and Body Sentences",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "20 sentences about body parts, symptoms, the doctor visit, and the "
  "pharmacy. 1. 頭が 痛いです。(あたまが いたいです。 Atama ga itai desu.) "
  "My head hurts. 2. 喉が 痛いです。(のどが いたいです。 Nodo ga itai desu.) "
  "My throat hurts. 3. お腹が 痛いです。(おなかが いたいです。 Onaka ga itai "
  "desu.) My stomach hurts. 4. 熱が あります。(ねつが あります。 Netsu ga "
  "arimasu.) I have a fever. 5. 咳が 出ます。(せきが でます。 Seki ga demasu.) "
  "I have a cough. 6. 鼻水が 出ます。(はなみずが でます。 Hanamizu ga demasu.) "
  "I have a runny nose. 7. 体が だるいです。(からだが だるいです。 Karada ga "
  "darui desu.) My body feels heavy. 8. 目が かゆいです。(めが かゆいです。 "
  "Me ga kayui desu.) My eyes are itchy. 9. 歯が 痛いです。(はが いたいです。 "
  "Ha ga itai desu.) My tooth hurts. 10. 腰が 痛いです。(こしが いたいです。 "
  "Koshi ga itai desu.) My back hurts. 11. 風邪を ひきました。(かぜを ひきました。 "
  "Kaze o hikimashita.) I caught a cold. 12. 病院に 行きます。(びょういんに "
  "いきます。 Byouin ni ikimasu.) I go to the hospital. 13. 医者に 診て "
  "もらいます。(いしゃに みて もらいます。 Isha ni mite moraimasu.) I have "
  "the doctor examine me. 14. 薬を 飲みます。(くすりを のみます。 Kusuri o "
  "nomimasu.) I take medicine. 15. 薬局で 薬を 買います。(やっきょくで くすりを "
  "かいます。 Yakkyoku de kusuri o kaimasu.) I buy medicine at the pharmacy. "
  "16. 注射は 痛いですか。(ちゅうしゃは いたいですか。 Chuusha wa itai desu "
  "ka.) Does the shot hurt. 17. 安静に して ください。(あんせいに して "
  "ください。 Ansei ni shite kudasai.) Please rest quietly. 18. もう 大丈夫です。"
  "(もう だいじょうぶです。 Mou daijoubu desu.) I am fine now. 19. 手を 洗います。"
  "(てを あらいます。 Te o araimasu.) I wash my hands. 20. 早く 寝て ください。"
  "(はやく ねて ください。 Hayaku nete kudasai.) Please go to bed early."
 ),
 "how_it_works": (
  "This record teaches the body as a reporting system: partが痛いです (the "
  "part hurts) and symptomが あります/出ます (I have a symptom) cover nearly "
  "every complaint a doctor needs to hear. Learn the body parts as a set - "
  "頭, 目, 鼻, 口, 喉, 胸, お腹, 背中, 腰, 手, 足 - then bolt any of them "
  "onto the が痛いです frame. The clinic frame is three steps: 病院に行きます, "
  "医者に診てもらいます, 薬を飲みます. Practice by narrating a pretend "
  "checkup; in a real clinic these exact sentences will carry you."
 ),
 "key_points": [
  "20 sentences: body parts, symptoms, doctor visit, pharmacy.",
  "Complaint frame: body-partが痛いです; symptomが あります/出ます.",
  "Body parts: 頭, 目, 鼻, 口, 喉, 胸, お腹, 背中, 腰, 手, 足.",
  "Clinic frame: 病院に行きます, 医者に診てもらいます, 薬を飲みます.",
  "Pharmacy: 薬局で薬を買います; rest: 安静にしてください.",
 ],
 "requirements": [
  "Core Nouns I and Grammar Essentials records.",
  "Learn the body-part set as one group.",
  "Practice a pretend checkup narration.",
 ],
 "standards": [
  "JLPT N5-N4 sentence band.",
 ],
 "citations": [
  "Japan Foundation. Japanese Language Proficiency Test Official Practice Materials, N5.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "The body becomes the Signature inner territory: each "
  "part a named province - 頭 the high province, 心 the central province - "
  "and pain the honest signal-fire raised when a province needs aid. In this "
  "framing the symptom sentence is a sworn report from the interior, exact "
  "and without exaggeration, and the doctor is the allied engineer called to "
  "the repair. The medicine is the remedy-seal, taken on schedule as sworn. "
  "This is his original framing, clearly labeled Signature-made."
 )},
# ------------------------------------------------------------- 16 emotions
{"key": "emotions",
 "name": "Japanese Emotions and Feelings Sentences",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "20 sentences about being happy, sad, angry, afraid, in love, and "
  "surprised. 1. とても 嬉しいです。(とても うれしいです。 Totemo ureshii "
  "desu.) I am very happy. 2. 合格して 良かったです。(ごうかくして よかったです。 "
  "Goukaku shite yokatta desu.) I passed, so I am glad. 3. 悲しい 映画を "
  "見ました。(かなしい えいがを みました。 Kanashii eiga o mimashita.) I "
  "watched a sad movie. 4. 涙が 出ました。(なみだが でました。 Namida ga "
  "demashita.) Tears came out. 5. 怒って います。(おこって います。 Okotte "
  "imasu.) I am angry. 6. 弟に 怒られました。(おとうとに おこられました。 "
  "Otouto ni okoraremashita.) I was scolded by my younger brother. 7. 怖い "
  "夢を 見ました。(こわい ゆめを みました。 Kowai yume o mimashita.) I had a "
  "scary dream. 8. 一人で 夜道が 怖いです。(ひとりで よみちが こわいです。 "
  "Hitori de yomichi ga kowai desu.) Walking alone at night is scary. 9. 彼女が "
  "好きです。(かのじょが すきです。 Kanojo ga suki desu.) I love her. 10. 家族を "
  "愛しています。(かぞくを あいしています。 Kazoku o aishite imasu.) I love "
  "my family. 11. びっくりしました。(Bikkuri shimashita.) I was surprised. "
  "12. 驚いて 声を 出しました。(おどろいて こえを だしました。 Odoroite koe "
  "o dashimashita.) I was startled and cried out. 13. 心配です。(しんぱいです。 "
  "Shinpai desu.) I am worried. 14. 母の 病気が 心配です。(ははの びょうきが "
  "しんぱいです。 Haha no byouki ga shinpai desu.) I am worried about my "
  "mother's illness. 15. ほっとしました。(Hotto shimashita.) I felt relieved. "
  "16. 緊張して います。(きんちょうして います。 Kinchou shite imasu.) I am "
  "nervous. 17. 恥ずかしいです。(はずかしいです。 Hazukashii desu.) I am "
  "embarrassed. 18. 寂しいです。(さびしいです。 Sabishii desu.) I am lonely. "
  "19. 懐かしい 気持ちです。(なつかしい きもちです。 Natsukashii kimochi "
  "desu.) I feel nostalgic. 20. 感動しました。(かんどうしました。 Kandou "
  "shimashita.) I was deeply moved."
 ),
 "how_it_works": (
  "This record teaches feelings as inner weather: Japanese usually reports "
  "emotion with adjectives (嬉しい, 悲しい, 怖い, 恥ずかしい) or with set "
  "phrases (びっくりしました, ほっとしました, 感動しました). The pattern is "
  "simple - causeを/が + feelingです - but the social rule matters: strong "
  "feelings like 怒っています are softened in public, while joy and "
  "gratitude are spoken freely. Learn these 20 as the emotional vocabulary "
  "of the heart, and pair each with the facial expression it belongs to."
 ),
 "key_points": [
  "20 sentences: happy, sad, angry, afraid, love, surprise, and more.",
  "Core feeling adjectives: 嬉しい, 悲しい, 怖い, 恥ずかしい, 寂しい, 懐かしい.",
  "Set phrases: びっくりしました, ほっとしました, 感動しました.",
  "好きです for like/love; 愛しています for deep love.",
  "Strong anger is softened in public speech.",
 ],
 "requirements": [
  "Adjectives and Adverbs record for the feeling adjectives.",
  "Pair each sentence with its facial expression.",
  "Keep a one-line feelings diary in Japanese for a week.",
 ],
 "standards": [
  "JLPT N5-N4 sentence band.",
 ],
 "citations": [
  "Japan Foundation. Japanese Language Proficiency Test Official Practice Materials, N5.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "Emotions become the Signature inner weather: 嬉しい the "
  "clear-sky seal, 悲しい the rain seal, 怒り the storm seal, ほっとした the "
  "clearing seal after the storm. In this framing the speaker is the "
  "weather-keeper of their own interior, sworn to report the sky honestly - "
  "neither hiding the rain nor faking the sun. 愛しています is the deepest "
  "oath of the set, spoken rarely and meant completely. This is his original "
  "framing, clearly labeled Signature-made."
 )},
# ------------------------------------------------------- 17 nature & weather
{"key": "nature",
 "name": "Japanese Nature and Weather Sentences",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "20 sentences about animals, plants, seasons, and weather talk. 1. 今日は "
  "いい 天気です。(きょうは いい てんきです。 Kyou wa ii tenki desu.) Today "
  "is fine weather. 2. 明日は 雨です。(あしたは あめです。 Ashita wa ame "
  "desu.) Tomorrow is rain. 3. 雪が 降っています。(ゆきが ふっています。 Yuki "
  "ga futte imasu.) It is snowing. 4. 風が 強いです。(かぜが つよいです。 Kaze "
  "ga tsuyoi desu.) The wind is strong. 5. 桜が 咲きました。(さくらが さきました。 "
  "Sakura ga sakimashita.) The cherry blossoms bloomed. 6. 紅葉が きれいです。"
  "(もみじが きれいです。 Momiji ga kirei desu.) The autumn leaves are "
  "beautiful. 7. 山に 登りました。(やまに のぼりました。 Yama ni "
  "noborimashita.) I climbed the mountain. 8. 川で 魚を 釣りました。(かわで "
  "さかなを つりました。 Kawa de sakana o tsurimashita.) I fished in the "
  "river. 9. 海で 泳ぎました。(うみで およぎました。 Umi de oyogimashita.) I "
  "swam in the sea. 10. 犬が 庭で 走っています。(いぬが にわで はしっています。 "
  "Inu ga niwa de hashitte imasu.) The dog is running in the garden. 11. 猫が "
  "日向ぼっこを しています。(ねこが ひなたぼっこを しています。 Neko ga "
  "hinatabokko o shite imasu.) The cat is sunbathing. 12. 鳥が 空を 飛んで "
  "います。(とりが そらを とんで います。 Tori ga sora o tonde imasu.) Birds "
  "are flying in the sky. 13. 虫の 声が します。(むしの こえが します。 Mushi "
  "no koe ga shimasu.) I hear insects. 14. 春は 花が 咲きます。(はるは はなが "
  "さきます。 Haru wa hana ga sakimasu.) In spring flowers bloom. 15. 夏は "
  "暑いです。(なつは あついです。 Natsu wa atsui desu.) Summer is hot. 16. 秋は "
  "涼しいです。(あきは すずしいです。 Aki wa suzushii desu.) Autumn is cool. "
  "17. 冬は 寒いです。(ふゆは さむいです。 Fuyu wa samui desu.) Winter is "
  "cold. 18. 虹が 出ました。(にじが でました。 Niji ga demashita.) A rainbow "
  "appeared. 19. 星が きれいです。(ほしが きれいです。 Hoshi ga kirei desu.) "
  "The stars are beautiful. 20. 月が 明るいです。(つきが あかるいです。 Tsuki "
  "ga akarui desu.) The moon is bright."
 ),
 "how_it_works": (
  "This record teaches the oldest small talk on earth - the weather - plus "
  "the living world around it. The weather frame is one line: timeは weather "
  "です, with 降っています for falling rain and snow. The seasons each get "
  "their adjective (春-花, 夏-暑い, 秋-涼しい, 冬-寒い) and their famous event "
  "(桜, 紅葉, 雪). Animals pair with their verbs: 犬は走る, 鳥は飛ぶ, 魚は泳ぐ. "
  "Open every conversation with 今日はいい天気ですね and you will never lack "
  "a first sentence in Japanese."
 ),
 "key_points": [
  "20 sentences: animals, plants, seasons, weather talk.",
  "Weather frame: timeは weatherです; 降っています for rain and snow.",
  "Season set: 春-桜, 夏-暑い, 秋-紅葉, 冬-雪.",
  "Animal verbs: 走る run, 飛ぶ fly, 泳ぐ swim, 鳴く cry.",
  "今日はいい天気ですね opens any conversation.",
 ],
 "requirements": [
  "Adjectives and Adverbs record for weather adjectives.",
  "Describe the sky aloud in Japanese every day.",
  "Learn the four season words as a set.",
 ],
 "standards": [
  "JLPT N5-N4 sentence band.",
 ],
 "citations": [
  "Japan Foundation. Japanese Language Proficiency Test Official Practice Materials, N5.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "Nature becomes the Signature great outdoors: the four "
  "seasons four sworn turnings of the year-seal - 春 the blossom seal, 夏 the "
  "heat seal, 秋 the harvest seal, 冬 the snow seal. Weather talk is the "
  "peace-oath between strangers, the one subject on which all speakers stand "
  "equal under the same sky. In this framing the learner does not memorize "
  "weather words, they join the ancient watch: reporting the sky truly, as "
  "every farmer and sailor has done. This is his original framing, clearly "
  "labeled Signature-made."
 )},
# ------------------------------------------------------- 18 shopping & money
{"key": "shopping",
 "name": "Japanese Shopping and Money Sentences",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "20 sentences about the market, prices, bargaining, and paying. 1. これは "
  "いくらですか。(これは いくらですか。 Kore wa ikura desu ka.) How much is "
  "this. 2. 三千円です。(さんぜんえんです。 Sanzen-en desu.) It is 3,000 yen. "
  "3. 高いです。(たかいです。 Takai desu.) It is expensive. 4. 安いですね。(やすいですね。 "
  "Yasui desu ne.) It is cheap, is it not. 5. もう少し 安く なりませんか。"
  "(もうすこし やすく なりませんか。 Mou sukoshi yasuku narimasen ka.) Can "
  "you make it a little cheaper. 6. 五千円で どうですか。(ごせんえんで どうですか。 "
  "Gosen-en de dou desu ka.) How about 5,000 yen. 7. それでは 買います。(それでは "
  "かいます。 Sore de wa kaimasu.) Then I will buy it. 8. やめて おきます。"
  "(やめて おきます。 Yamete okimasu.) I will pass on it. 9. サイズは ありますか。"
  "(さいずは ありますか。 Saizu wa arimasu ka.) Do you have the size. 10. 試着して "
  "もいいですか。(しちゃくして もいいですか。 Shichaku shite mo ii desu ka.) "
  "May I try it on. 11. 他の 色は ありますか。(ほかの いろは ありますか。 Hoka "
  "no iro wa arimasu ka.) Do you have another color. 12. 領収書を ください。"
  "(りょうしゅうしょを ください。 Ryoushuusho o kudasai.) A receipt, please. "
  "13. カードで 払えますか。(かーどで はらえますか。 Kaado de haraemasu ka.) "
  "Can I pay by card. 14. 現金で 払います。(げんきんで はらいます。 Genkin de "
  "haraimasu.) I pay in cash. 15. おつりです。(おつりです。 Otsuri desu.) Here "
  "is your change. 16. 袋は 要りません。(ふくろは いりません。 Fukuro wa "
  "irimasen.) I do not need a bag. 17. 閉店は 何時ですか。(へいてんは なんじですか。 "
  "Heiten wa nanji desu ka.) What time do you close. 18. セール中です。(せーるちゅうです。 "
  "Seeru-chuu desu.) It is on sale. 19. 新商品です。(しんしょうひんです。 "
  "Shinshouhin desu.) It is a new product. 20. また 来ます。(また きます。 "
  "Mata kimasu.) I will come again."
 ),
 "how_it_works": (
  "This record teaches shopping as a negotiation dance with fixed steps: ask "
  "the price (いくらですか), react (高いですね), bargain (もう少し安くなりませんか), "
  "decide (それでは買います or やめておきます), pay (カードで払えますか), "
  "close (領収書をください). Each step is one sentence, and the whole dance "
  "runs the same in a department store and a flea market. Money math stays "
  "in yen with tax included on the tag - the price you see is the price you "
  "pay. Practice the full dance with a friend playing the shopkeeper until "
  "the steps flow without thinking."
 ),
 "key_points": [
  "20 sentences: market, prices, bargaining, paying.",
  "Bargaining frame: もう少し安くなりませんか; 五千円でどうですか.",
  "Payment: カードで払えますか; 現金で払います; おつりです.",
  "Sizing and color: サイズはありますか; 他の色はありますか.",
  "Closing: 領収書をください; 袋は要りません.",
 ],
 "requirements": [
  "Numbers and Time record for prices.",
  "Practice the full buy-dance as a role-play.",
  "Learn yen amounts 100 to 100,000 by heart.",
 ],
 "standards": [
  "JLPT N5-N4 sentence band.",
 ],
 "citations": [
  "Japan Foundation. Japanese Language Proficiency Test Official Practice Materials, N5.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "Shopping becomes the Signature exchange rite: every "
  "いくらですか a weighing-seal laid on the counter, every bargain a "
  "good-faith haggling oath where both sides seek the fair weight. The price "
  "spoken is a sworn number - the tag tells no lies in this framing - and "
  "the payment is the settling seal: coin or card, the debt dies on the "
  "spot. おつりです is the balance-seal returned exactly. The merchant who "
  "keeps these oaths earns the rarest seal of all: また来ます, I will come "
  "again. This is his original framing, clearly labeled Signature-made."
 )},
# ------------------------------------------------------------ 19 friendship
{"key": "friendship",
 "name": "Japanese Friendship and Social Life Sentences",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "20 sentences about meeting people, invitations, and celebrations. 1. はじめまして。"
  "田中です。(はじめまして。たなかです。 Hajimemashite. Tanaka desu.) Nice to "
  "meet you. I am Tanaka. 2. どこから 来ましたか。(どこから きましたか。 Doko "
  "kara kimashita ka.) Where did you come from. 3. 趣味は 何ですか。(しゅみは "
  "なんですか。 Shumi wa nan desu ka.) What is your hobby. 4. 映画が 好きです。"
  "(えいがが すきです。 Eiga ga suki desu.) I like movies. 5. 今度の 日曜日に "
  "遊びに 来ませんか。(こんどの にちようびに あそびに きませんか。 Kondo no "
  "nichiyoubi ni asobi ni kimasen ka.) Will you come visit next Sunday. 6. "
  "ぜひ 来て ください。(ぜひ きて ください。 Zehi kite kudasai.) Please come "
  "by all means. 7. 一緒に ご飯を 食べましょう。(いっしょに ごはんを たべましょう。 "
  "Issho ni gohan o tabemashou.) Let us eat together. 8. 映画を 見に 行きましょう。"
  "(えいがを みに いきましょう。 Eiga o mi ni ikimashou.) Let us go see a "
  "movie. 9. パーティーに 招待します。(ぱーてぃーに しょうたいします。 Paatii "
  "ni shoutai shimasu.) I invite you to the party. 10. 誕生日 おめでとう。"
  "(たんじょうび おめでとう。 Tanjoubi omedetou.) Happy birthday. 11. 乾杯。"
  "(かんぱい。 Kanpai.) Cheers. 12. 久しぶり。(ひさしぶり。 Hisashiburi.) "
  "Long time no see. 13. 元気だった。(げんきだった。 Genki datta.) I have been "
  "well. 14. 最近 どう。(さいきん どう。 Saikin dou.) How have you been lately. "
  "15. また 遊ぼう。(また あそぼう。 Mata asobou.) Let us hang out again. 16. "
  "連絡して ね。(れんらくして ね。 Renraku shite ne.) Keep in touch. 17. 友達を "
  "紹介します。(ともだちを しょうかいします。 Tomodachi o shoukai shimasu.) "
  "Let me introduce my friend. 18. こちらは 佐藤さんです。(こちらは さとうさんです。 "
  "Kochira wa Satou-san desu.) This is Ms. Sato. 19. どうぞ よろしく。(どうぞ "
  "よろしく。 Douzo yoroshiku.) Pleased to meet you (casual). 20. 楽しかったです。"
  "ありがとう。(たのしかったです。ありがとう。 Tanoshikatta desu. Arigatou.) "
  "I had fun. Thank you."
 ),
 "how_it_works": (
  "This record teaches friendship as a ladder of closeness: first meetings "
  "use the full polite set (はじめまして, よろしくおねがいします), growing "
  "friendships shift to invitations (来ませんか, ましょう), and close friends "
  "drop to casual (久しぶり, また遊ぼう). The invitation frame 来ませんか is "
  "the workhorse - soft, polite, easy to accept or decline. Introductions "
  "follow the fixed ritual: こちらは nameさんです, then どうぞよろしく. "
  "Climb the ladder one sentence at a time and never use casual forms upward "
  "to seniors."
 ),
 "key_points": [
  "20 sentences: meeting people, invitations, celebrations.",
  "Closeness ladder: polite first meetings, ましょう invitations, casual close friends.",
  "Invitation frame: verb-ませんか.",
  "Introduction ritual: こちらは nameさんです, どうぞよろしく.",
  "Celebrations: 誕生日おめでとう, 乾杯, 久しぶり.",
 ],
 "requirements": [
  "Greetings record for the first-meeting phrases.",
  "Practice introductions with real names.",
  "Never use casual forms to seniors.",
 ],
 "standards": [
  "JLPT N5-N4 sentence band.",
 ],
 "citations": [
  "Japan Foundation. Japanese Language Proficiency Test Official Practice Materials, N5.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "Friendship becomes the Signature bonding rite: first "
  "meetings the formal oath-exchange of はじめまして, invitations the "
  "bridge-seals cast toward another person - 来ませんか the gentlest bridge, "
  "easy to cross or decline with honor. In this framing every friend is a "
  "sworn ally of the language journey, and また遊ぼう is the renewal oath "
  "that keeps the bond current. Introductions are the witness ceremony: one "
  "friend vouches another into the circle. This is his original framing, "
  "clearly labeled Signature-made."
 )},
# ------------------------------------------------------------ 20 technology
{"key": "technology",
 "name": "Japanese Technology and Communication Sentences",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "20 sentences about the phone, internet, computer, and messaging. 1. スマホで "
  "写真を 撮ります。(すまほで しゃしんを とります。 Sumaho de shashin o "
  "torimasu.) I take photos with my smartphone. 2. インターネットで 調べます。"
  "(いんたーねっとで しらべます。 Intaanetto de shirabemasu.) I look it up on "
  "the internet. 3. パソコンで 仕事を します。(ぱそこんで しごとを します。 "
  "Pasokon de shigoto o shimasu.) I work on the computer. 4. メールを 送ります。"
  "(めーるを おくります。 Meiru o okurimasu.) I send an email. 5. メッセージを "
  "読みました。(めっせーじを よみました。 Messeeji o yomimashita.) I read the "
  "message. 6. 電話を かけます。(でんわを かけます。 Denwa o kakemasu.) I make "
  "a phone call. 7. 充電が ありません。(じゅうでんが ありません。 Juuden ga "
  "arimasen.) The battery is dead. 8. Wi-Fiに つなぎます。(わいふぁいに "
  "つなぎます。 Waifai ni tsunagimasu.) I connect to Wi-Fi. 9. パスワードを "
  "入れます。(ぱすわーどを いれます。 Pasuwaado o iremasu.) I enter the "
  "password. 10. アプリを ダウンロード します。(あぷりを だうんろーど します。 "
  "Apuri o daunroodo shimasu.) I download the app. 11. 動画を 見ます。(どうがを "
  "みます。 Douga o mimasu.) I watch videos. 12. 音楽を 聴きます。(おんがくを "
  "ききます。 Ongaku o kikimasu.) I listen to music. 13. 画面が 明るいです。"
  "(がめんが あかるいです。 Gamen ga akarui desu.) The screen is bright. 14. "
  "キーボードで 入力します。(きーぼーどで にゅうりょくします。 Kiiboodo de "
  "nyuuryoku shimasu.) I type on the keyboard. 15. ファイルを 保存します。"
  "(ふぁいるを ほぞんします。 Fairu o hozon shimasu.) I save the file. 16. "
  "プリンターで 印刷します。(ぷりんたーで いんさつします。 Purintaa de "
  "insatsu shimasu.) I print with the printer. 17. オンラインで 会議します。"
  "(おんらいんで かいぎします。 Onrain de kaigi shimasu.) I meet online. 18. "
  "SNSで 友達と 話します。(えすえぬえすで ともだちと はなします。 Esuenuesu "
  "de tomodachi to hanashimasu.) I talk with friends on social media. 19. 検索して "
  "みます。(けんさくして みます。 Kensaku shite mimasu.) I will try searching. "
  "20. 電源を 切ります。(でんげんを きります。 Dengen o kirimasu.) I turn off "
  "the power."
 ),
 "how_it_works": (
  "This record teaches modern life in katakana: most technology words are "
  "loanwords written in the angular script - スマホ, インターネット, パソコン, "
  "アプリ, Wi-Fi - so the katakana from the writing record pays off here. "
  "The action frame is always toolで verb: スマホで撮ります, パソコンで仕事を"
  "します. Learn the ten device nouns as a set, then bolt any verb onto the "
  "で frame. Narrate your own phone use in Japanese for one evening and the "
  "whole digital vocabulary becomes yours."
 ),
 "key_points": [
  "20 sentences: phone, internet, computer, messaging.",
  "Tech words are katakana loanwords: スマホ, パソコン, アプリ, Wi-Fi.",
  "Tool frame: deviceで verb.",
  "Core actions: 送る send, 保存する save, 印刷する print, 検索する search.",
  "つなぎます connect; 切ります turn off.",
 ],
 "requirements": [
  "Writing System record for katakana reading.",
  "Narrate one evening of phone use in Japanese.",
  "Learn the ten device nouns as a set.",
 ],
 "standards": [
  "JLPT N5-N4 sentence band.",
 ],
 "citations": [
  "Japan Foundation. Japanese Language Proficiency Test Official Practice Materials, N5.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "Technology becomes the Signature signal-realm: devices "
  "the sworn relay towers - スマホ the pocket tower, パソコン the desk tower "
  "- and every message a sealed packet launched across the air. In this "
  "framing the learner is the signal-keeper: 送ります launches the packet, "
  "保存します seals it in the vault, 検索します casts the seeking net. The "
  "katakana themselves are the foreign-name seals, marking words that "
  "crossed the sea to serve. This is his original framing, clearly labeled "
  "Signature-made."
 )},
# -------------------------------------------------------------- 21 verb tenses
{"key": "tenses",
 "name": "Japanese Verb Tenses in Sentences",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "Japanese verbs mark present and past; the future is the present form plus "
  "a time word, and intention uses つもり. Present (non-past), five "
  "sentences: 1. 毎日 新聞を 読みます。(まいにち しんぶんを よみます。 Mainichi "
  "shinbun o yomimasu.) I read the newspaper every day. 2. 学校に 行きます。"
  "(がっこうに いきます。 Gakkou ni ikimasu.) I go to school. 3. コーヒーを "
  "飲みます。(こーひーを のみます。 Koohii o nomimasu.) I drink coffee. 4. "
  "日本語を 勉強します。(にほんごを べんきょうします。 Nihongo o benkyou "
  "shimasu.) I study Japanese. 5. 友達に 会います。(ともだちに あいます。 "
  "Tomodachi ni aimasu.) I meet my friend. Past, five sentences: 1. 昨日 映画を "
  "見ました。(きのう えいがを みました。 Kinou eiga o mimashita.) I watched a "
  "movie yesterday. 2. 朝ご飯を 食べました。(あさごはんを たべました。 "
  "Asagohan o tabemashita.) I ate breakfast. 3. 東京に 行きました。(とうきょうに "
  "いきました。 Toukyou ni ikimashita.) I went to Tokyo. 4. 本を 買いました。"
  "(ほんを かいました。 Hon o kaimashita.) I bought a book. 5. 手紙を 書きました。"
  "(てがみを かきました。 Tegami o kakimashita.) I wrote a letter. Future "
  "with time words, five sentences: 1. 明日 大阪に 行きます。(あした おおさかに "
  "いきます。 Ashita Oosaka ni ikimasu.) I will go to Osaka tomorrow. 2. 来週 "
  "試験が あります。(らいしゅう しけんが あります。 Raishuu shiken ga arimasu.) "
  "There is an exam next week. 3. 来年 日本に 行きます。(らいねん にほんに "
  "いきます。 Rainen Nihon ni ikimasu.) I will go to Japan next year. 4. 今晩 "
  "友達に 会います。(こんばん ともだちに あいます。 Konban tomodachi ni "
  "aimasu.) I will meet my friend tonight. 5. 週末は 休みます。(しゅうまつは "
  "やすみます。 Shuumatsu wa yasumimasu.) I will rest on the weekend. "
  "Intention with つもり, five sentences: 1. 日本語を 勉強する つもりです。"
  "(にほんごを べんきょうする つもりです。 Nihongo o benkyou suru tsumori "
  "desu.) I intend to study Japanese. 2. 来年 結婚する つもりです。(らいねん "
  "けっこんする つもりです。 Rainen kekkon suru tsumori desu.) I intend to "
  "marry next year. 3. 車を 買う つもりです。(くるまを かう つもりです。 Kuruma "
  "o kau tsumori desu.) I intend to buy a car. 4. 早く 寝る つもりです。(はやく "
  "ねる つもりです。 Hayaku neru tsumori desu.) I intend to sleep early. 5. "
  "明日 休む つもりです。(あした やすむ つもりです。 Ashita yasumu tsumori "
  "desu.) I intend to take tomorrow off. Rule: dictionary form to ます form "
  "to ました form; つもり attaches to the plain present."
 ),
 "how_it_works": (
  "This record teaches time as a two-switch system with one helper. Switch "
  "one: ます (present) versus ました (past) - the single most important "
  "conjugation in Japanese, built from the ます stem you already know. "
  "Switch two is not a switch at all: the future wears the present form and "
  "lets a time word (明日, 来週, 来年) do the dating. The helper つもり "
  "declares intention and attaches to the plain present form. Drill the "
  "triple for ten verbs - 読みます/読みました/読むつもりです - until the "
  "three time positions feel like three rooms you can walk between."
 ),
 "key_points": [
  "Present: ます form; past: ました form; future: present form plus a time word.",
  "Intention: plain present plus つもりです.",
  "The ます to ました switch is the core past-tense move.",
  "Time words: 明日, 来週, 来年, 今晩, 週末.",
  "20 sentences: 5 present, 5 past, 5 future, 5 intention.",
 ],
 "requirements": [
  "Core Verbs I record for dictionary and ます forms.",
  "Drill the triple ます/ました/つもり for ten verbs.",
  "Write yesterday, today, and tomorrow diary lines.",
 ],
 "standards": [
  "JLPT N5-N4 tense band.",
  "Standard ます/ました conjugation.",
 ],
 "citations": [
  "Martin SE. A Reference Grammar of Japanese. University of Hawaii Press; 1975.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "Tenses become the Signature time-seals: ます the "
  "present-seal stamped on the now, ました the past-seal pressed into "
  "memory, the future a present-seal dated forward by 明日 and 来年 like a "
  "letter marked for later delivery. つもり is the intention-seal, the "
  "speaker's sworn signature on what is to come. In this framing every verb "
  "is a time traveler carrying its seal, and the listener always knows which "
  "era the traveler arrived from. This is his original framing, clearly "
  "labeled Signature-made."
 )},
# ---------------------------------------------------------------- 22 questions
{"key": "qa",
 "name": "Japanese Questions and Answers",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "20 question-and-answer pairs covering who, what, where, when, why, and "
  "how. 1. Q: お名前は 何ですか。(おなまえは なんですか。 Onamae wa nan desu "
  "ka.) What is your name. A: 田中です。(たなかです。 Tanaka desu.) I am "
  "Tanaka. 2. Q: どこから 来ましたか。(どこから きましたか。 Doko kara "
  "kimashita ka.) Where did you come from. A: 大阪から 来ました。(おおさかから "
  "きました。 Oosaka kara kimashita.) I came from Osaka. 3. Q: いつ 日本に "
  "来ましたか。(いつ にほんに きましたか。 Itsu Nihon ni kimashita ka.) When "
  "did you come to Japan. A: 三年前に 来ました。(さんねんまえに きました。 "
  "San-nen mae ni kimashita.) I came three years ago. 4. Q: 誰と 来ましたか。"
  "(だれと きましたか。 Dare to kimashita ka.) Who did you come with. A: 家族と "
  "来ました。(かぞくと きました。 Kazoku to kimashita.) I came with my family. "
  "5. Q: 何を しますか。(なにを しますか。 Nani o shimasu ka.) What will you "
  "do. A: 買い物を します。(かいものを します。 Kaimono o shimasu.) I will go "
  "shopping. 6. Q: どうやって 来ましたか。(どうやって きましたか。 Douyatte "
  "kimashita ka.) How did you come. A: 電車で 来ました。(でんしゃで きました。 "
  "Densha de kimashita.) I came by train. 7. Q: なぜ 遅いのですか。(なぜ "
  "おそいのですか。 Naze osoi no desu ka.) Why are you late. A: 電車が 遅れました。"
  "(でんしゃが おくれました。 Densha ga okuremashita.) The train was delayed. "
  "8. Q: いくらですか。(Ikura desu ka.) How much is it. A: 五百円です。(ごひゃくえんです。 "
  "Gohyaku-en desu.) It is 500 yen. 9. Q: 何時ですか。(なんじですか。 Nanji "
  "desu ka.) What time is it. A: 三時です。(さんじです。 Sanji desu.) It is "
  "three o'clock. 10. Q: お元気ですか。(おげんきですか。 Ogenki desu ka.) How "
  "are you. A: 元気です。(げんきです。 Genki desu.) I am fine. 11. Q: どの "
  "電車ですか。(どの でんしゃですか。 Dono densha desu ka.) Which train is it. "
  "A: あの 電車です。(あの でんしゃです。 Ano densha desu.) That train over "
  "there. 12. Q: 英語が 分かりますか。(えいごが わかりますか。 Eigo ga "
  "wakarimasu ka.) Do you understand English. A: 少し 分かります。(すこし "
  "わかります。 Sukoshi wakarimasu.) I understand a little. 13. Q: おいしいですか。"
  "(Oishii desu ka.) Is it delicious. A: とても おいしいです。(とても おいしいです。 "
  "Totemo oishii desu.) Very delicious. 14. Q: どこに 住んで いますか。(どこに "
  "すんで いますか。 Doko ni sunde imasu ka.) Where do you live. A: 東京に "
  "住んで います。(とうきょうに すんで います。 Toukyou ni sunde imasu.) I "
  "live in Tokyo. 15. Q: 兄弟が いますか。(きょうだいが いますか。 Kyoudai ga "
  "imasu ka.) Do you have siblings. A: 妹が 一人 います。(いもうとが ひとり "
  "います。 Imouto ga hitori imasu.) I have one younger sister. 16. Q: 何が "
  "好きですか。(なにが すきですか。 Nani ga suki desu ka.) What do you like. "
  "A: 音楽が 好きです。(おんがくが すきです。 Ongaku ga suki desu.) I like "
  "music. 17. Q: いつ 帰りますか。(いつ かえりますか。 Itsu kaerimasu ka.) "
  "When will you return. A: 六時に 帰ります。(ろくじに かえります。 Rokuji ni "
  "kaerimasu.) I return at six. 18. Q: どう 思いますか。(どう おもいますか。 "
  "Dou omoimasu ka.) What do you think. A: いいと 思います。(いいと おもいます。 "
  "Ii to omoimasu.) I think it is good. 19. Q: 誰ですか。(だれですか。 Dare "
  "desu ka.) Who is it. A: 友達です。(ともだちです。 Tomodachi desu.) It is my "
  "friend. 20. Q: どこで 買いましたか。(どこで かいましたか。 Doko de "
  "kaimashita ka.) Where did you buy it. A: デパートで 買いました。(でぱーとで "
  "かいました。 Depaato de kaimashita.) I bought it at the department store."
 ),
 "how_it_works": (
  "This record teaches questions as a key ring: each interrogative opens one "
  "kind of answer - だれ opens who, なに opens what, どこ opens where, いつ "
  "opens when, なぜ opens why, どう opens how, いくら opens how much, いつ "
  "opens when. The grammar never changes: put the question word where the "
  "answer would sit, add か, raise the voice at the end. Answers mirror the "
  "question's frame exactly. Drill all 20 pairs as call-and-response until "
  "the question word and its answer type are welded together."
 ),
 "key_points": [
  "20 question-and-answer pairs: who, what, where, when, why, how.",
  "Question word sits where the answer sits; add か at the end.",
  "だれ who, なに/なん what, どこ where, いつ when, なぜ why, どう how.",
  "いくら how much; いくつ how many; どの which.",
  "Answers mirror the question's frame.",
 ],
 "requirements": [
  "Pronouns record for the interrogatives.",
  "Drill the 20 pairs as call-and-response.",
  "Ask and answer about your own day.",
 ],
 "standards": [
  "JLPT N5 question band.",
 ],
 "citations": [
  "Kuno S. The Structure of the Japanese Language. MIT Press; 1973.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "Questions become the Signature key-ring: eight sworn "
  "keys - だれ, なに, どこ, いつ, なぜ, どう, いくら, どの - each cut to open "
  "exactly one kind of locked answer. In this framing every か is the "
  "key-turn, the small click that asks the world to open, and every answer "
  "is the door swinging wide. The asker swears honest curiosity, the "
  "answerer swears a true reply, and the exchange is complete. This is his "
  "original framing, clearly labeled Signature-made."
 )},
# --------------------------------------------------------------- 23 commands
{"key": "commands",
 "name": "Japanese Commands and Requests",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "20 imperative and polite-request sentences, formal versus informal. Polite "
  "requests with てください: 1. 見て ください。(みて ください。 Mite kudasai.) "
  "Please look. 2. 待って ください。(まって ください。 Matte kudasai.) Please "
  "wait. 3. ゆっくり 話して ください。(ゆっくり はなして ください。 Yukkuri "
  "hanashite kudasai.) Please speak slowly. 4. ここに 書いて ください。(ここに "
  "かいて ください。 Koko ni kaite kudasai.) Please write here. 5. 教えて "
  "ください。(おしえて ください。 Oshiete kudasai.) Please tell me. Soft "
  "requests with てもいいですか: 6. 座って もいいですか。(すわって もいいですか。 "
  "Suwatte mo ii desu ka.) May I sit down. 7. 写真を 撮って もいいですか。"
  "(しゃしんを とって もいいですか。 Shashin o totte mo ii desu ka.) May I "
  "take a photo. 8. 使って もいいですか。(つかって もいいですか。 Tsukatte mo "
  "ii desu ka.) May I use it. Formal with なさい: 9. 座りなさい。(すわりなさい。 "
  "Suwarinasai.) Please be seated (formal). 10. 静かに しなさい。(しずかに "
  "しなさい。 Shizuka ni shinasai.) Be quiet (formal). Plain imperatives, "
  "close friends and family only: 11. 見ろ。(みろ。 Miro.) Look. 12. 来い。"
  "(こい。 Koi.) Come. 13. 食べろ。(たべろ。 Tabero.) Eat. 14. 行け。(いけ。 "
  "Ike.) Go. 15. 書け。(かけ。 Kake.) Write. Invitations with ましょう: 16. "
  "行きましょう。(いきましょう。 Ikimashou.) Let us go. 17. 食べましょう。"
  "(たべましょう。 Tabemashou.) Let us eat. 18. 休みましょう。(やすみましょう。 "
  "Yasumimashou.) Let us rest. Prohibitions: 19. 触らないで ください。(さわらないで "
  "ください。 Sawaranaide kudasai.) Please do not touch. 20. ここで タバコを "
  "吸わないで ください。(ここで たばこを すわないで ください。 Koko de tabako "
  "o suwanaide kudasai.) Please do not smoke here."
 ),
 "how_it_works": (
  "This record teaches telling people what to do as a politeness staircase "
  "with four steps. Step one, the safe default: て-form plus ください - "
  "polite, works everywhere. Step two, asking permission: てもいいですか - "
  "even softer. Step three, formal instruction: ます stem plus なさい - for "
  "teachers and manuals. Step four, the plain imperative - 書け, 来い, 食べろ "
  "- for close friends, family, and emergencies only; never upward. The "
  "invitation ましょう sits beside the staircase as the friendly let's. "
  "Climb down the staircase only as closeness allows."
 ),
 "key_points": [
  "Politeness staircase: てください, てもいいですか, なさい, plain imperative.",
  "てください is the safe default everywhere.",
  "Plain imperatives (書け, 来い) are for close friends and emergencies only.",
  "Group 1 imperative: final kana to e-row; Group 2: る to ろ.",
  "ましょう invites: let us do it together.",
  "ないでください makes polite prohibitions.",
 ],
 "requirements": [
  "Core Verbs I record for te-forms and verb groups.",
  "Practice each staircase step in matching situations.",
  "Never use plain imperatives upward to seniors.",
 ],
 "standards": [
  "JLPT N5-N4 imperative band.",
  "Standard imperative conjugation rules.",
 ],
 "citations": [
  "Martin SE. A Reference Grammar of Japanese. University of Hawaii Press; 1975.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "Commands become the Signature order-seals, ranked by "
  "weight: てください the courteous request-seal anyone may present, てもいい"
  "ですか the permission-seal that kneels before asking, なさい the "
  "instructor's seal of office, and the plain imperative the bare blade-seal "
  "drawn only among sworn close companions or in true emergency. In this "
  "framing every command is a transfer of will, and the politeness level is "
  "the oath wrapping that keeps the transfer honorable. ましょう is the "
  "fellowship seal - let us go together. This is his original framing, "
  "clearly labeled Signature-made."
 )},
# ------------------------------------------------------------ 24 descriptions
{"key": "descriptions",
 "name": "Japanese Descriptions of People and Places",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "20 sentences describing people, places, and things in detail. 1. 彼女は "
  "背が 高くて 目が 大きいです。(かのじょは せが たかくて めが おおきいです。 "
  "Kanojo wa se ga takakute me ga ookii desu.) She is tall with big eyes. 2. "
  "彼は 優しい 笑顔の 男性です。(かれは やさしい えがおの だんせいです。 Kare "
  "wa yasashii egao no dansei desu.) He is a man with a kind smile. 3. 先生は "
  "四十代の 女性です。(せんせいは よんじゅうだいの じょせいです。 Sensei wa "
  "yonjuudai no josei desu.) The teacher is a woman in her forties. 4. 子どもは "
  "元気で 明るいです。(こどもは げんきで あかるいです。 Kodomo wa genki de "
  "akarui desu.) The child is healthy and cheerful. 5. 祖父は 白髪の 紳士です。"
  "(そふは はくはつの しんしです。 Sofu wa hakuhatsu no shinshi desu.) My "
  "grandfather is a white-haired gentleman. 6. 東京は 大きくて 賑やかな 街です。"
  "(とうきょうは おおきくて にぎやかな まちです。 Toukyou wa ookikute "
  "nigiyaka na machi desu.) Tokyo is a big, lively city. 7. 京都は 静かで "
  "美しい 古都です。(きょうとは しずかで うつくしい こと です。 Kyouto wa "
  "shizuka de utsukushii koto desu.) Kyoto is a quiet, beautiful old capital. "
  "8. 富士山は 高くて 有名な 山です。(ふじさんは たかくて ゆうめいな やまです。 "
  "Fujisan wa takakute yuumei na yama desu.) Mt. Fuji is a high, famous "
  "mountain. 9. この 公園は 広くて 緑が 多いです。(この こうえんは ひろくて "
  "みどりが おおいです。 Kono kouen wa hirokute midori ga ooi desu.) This park "
  "is spacious with lots of greenery. 10. 海は 青くて 静かです。(うみは "
  "あおくて しずかです。 Umi wa aokute shizuka desu.) The sea is blue and "
  "calm. 11. 部屋は 明るくて きれいです。(へやは あかるくて きれいです。 Heya "
  "wa akarukute kirei desu.) The room is bright and clean. 12. この ラーメンは "
  "熱くて 美味しいです。(この らーめんは あつくて おいしいです。 Kono raamen "
  "wa atsukute oishii desu.) This ramen is hot and delicious. 13. 彼の 車は "
  "新しくて 速いです。(かれの くるまは あたらしくて はやいです。 Kare no "
  "kuruma wa atarashikute hayai desu.) His car is new and fast. 14. この 本は "
  "厚くて 面白いです。(この ほんは あつくて おもしろいです。 Kono hon wa "
  "atsukute omoshiroi desu.) This book is thick and interesting. 15. 冬の 朝は "
  "寒くて 静かです。(ふゆの あさは さむくて しずかです。 Fuyu no asa wa "
  "samukute shizuka desu.) Winter mornings are cold and quiet. 16. 彼女の 声は "
  "優しくて きれいです。(かのじょの こえは やさしくて きれいです。 Kanojo no "
  "koe wa yasashikute kirei desu.) Her voice is gentle and beautiful. 17. この "
  "町の 人々は 親切です。(この まちの ひとびとは しんせつです。 Kono machi no "
  "hitobito wa shinsetsu desu.) The people of this town are kind. 18. 庭の 花は "
  "赤くて 黄色いです。(にわの はなは あかくて きいろいです。 Niwa no hana wa "
  "akakute kiiroi desu.) The garden flowers are red and yellow. 19. 夜空は "
  "暗くて 星が きれいです。(よぞらは くらくて ほしが きれいです。 Yozora wa "
  "kurakute hoshi ga kirei desu.) The night sky is dark and the stars are "
  "beautiful. 20. 彼の 日本語は 上手で 自然です。(かれの にほんごは じょうずで "
  "しぜんです。 Kare no Nihongo wa jouzu de shizen desu.) His Japanese is "
  "skilled and natural."
 ),
 "how_it_works": (
  "This record teaches rich description through chaining: the て-form of "
  "adjectives links qualities into a flowing portrait - 高くて大きい, 静かで"
  "美しい. I-adjectives chain with くて, na-adjectives with で, and the final "
  "adjective carries the です that closes the sentence. Body descriptions use "
  "the partが adjective pattern (目が大きい, 背が高い); place descriptions "
  "stack two or three chained adjectives before the noun. Paint one person "
  "and one place per day with three chained adjectives each."
 ),
 "key_points": [
  "20 detailed descriptive sentences.",
  "Chaining: i-adjectives with くて, na-adjectives with で.",
  "Body pattern: partが adjective (目が大きい, 背が高い).",
  "People: age, build, face, manner; places: size, mood, features.",
  "Final adjective carries the closing です.",
 ],
 "requirements": [
  "Adjectives and Adverbs record for the chaining rules.",
  "Describe one person and one place daily with three adjectives.",
  "Practice the partが adjective pattern.",
 ],
 "standards": [
  "JLPT N4 descriptive band.",
 ],
 "citations": [
  "Tsujimura N. An Introduction to Japanese Linguistics. 4th ed. Wiley-Blackwell; 2023.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "Description becomes the Signature portrait rite: each "
  "chained adjective another brushstroke - くて the joining stroke, で the "
  "seam between colors - until the person or place stands fully painted in "
  "words. In this framing the describer is sworn to truth of observation: "
  "the tallness must be tall, the kindness must be kind, for a false stroke "
  "ruins the portrait's oath. 目が大きい is the window-seal of the face, "
  "静かで美しい the twin seals of old Kyoto. This is his original framing, "
  "clearly labeled Signature-made."
 )},
# ---------------------------------------------------------------- 25 story I
{"key": "story1",
 "name": "Japanese Short Story I: A Simple Day",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "A 10-sentence simple story in Japanese, with line-by-line English "
  "translation. 1. 朝、 太郎は 七時に 起きます。(あさ、 たろうは しちじに "
  "おきます。 Asa, Tarou wa shichiji ni okimasu.) In the morning, Taro wakes "
  "up at seven. 2. 顔を 洗って 朝ご飯を 食べます。(かおを あらって あさごはんを "
  "たべます。 Kao o aratte asagohan o tabemasu.) He washes his face and eats "
  "breakfast. 3. パンと 卵と 牛乳です。(ぱんと たまごと ぎゅうにゅうです。 Pan "
  "to tamago to gyuunyuu desu.) It is bread, eggs, and milk. 4. 八時に 家を "
  "出ます。(はちじに いえを でます。 Hachiji ni ie o demasu.) He leaves home "
  "at eight. 5. 駅まで 自転車で 行きます。(えきまで じてんしゃで いきます。 "
  "Eki made jitensha de ikimasu.) He goes to the station by bicycle. 6. 電車で "
  "学校に 行きます。(でんしゃで がっこうに いきます。 Densha de gakkou ni "
  "ikimasu.) He goes to school by train. 7. 友達と 一緒に 勉強します。(ともだちと "
  "いっしょに べんきょうします。 Tomodachi to issho ni benkyou shimasu.) He "
  "studies with his friends. 8. 昼ご飯は カレーを 食べます。(ひるごはんは "
  "かれーを たべます。 Hirugohan wa karee o tabemasu.) He eats curry for "
  "lunch. 9. 午後は 体育の 授業です。(ごごは たいいくの じゅぎょうです。 Gogo "
  "wa taiiku no jugyou desu.) The afternoon is PE class. 10. 五時に 家に 帰って "
  "宿題を します。(ごじに いえに かえって しゅくだいを します。 Goji ni ie "
  "ni kaette shukudai o shimasu.) He returns home at five and does his "
  "homework. Reading guide: the story runs on the present ます form from "
  "waking to homework; て-form links the morning actions (洗って, 帰って); "
  "time words (七時に, 八時に, 五時に) carry the day forward."
 ),
 "how_it_works": (
  "This record proves the ladder works: every grammar point from records 1 "
  "through 24 appears in one ordinary day. Read it three ways. First, read "
  "the Japanese aloud straight through for flow. Second, cover the English "
  "and translate each line yourself. Third, retell Taro's day in your own "
  "words, swapping in your own times and meals. When you can retell the day "
  "without looking, the foundations have become reflex."
 ),
 "key_points": [
  "10-sentence story with line-by-line English translation.",
  "Runs on the present ます form: a day from waking to homework.",
  "て-form links sequential actions: 洗って, 帰って.",
  "Time words carry the narrative: 七時に, 八時に, 五時に.",
  "Three-way reading: aloud, translate, retell.",
 ],
 "requirements": [
  "All foundations and compounded records.",
  "Read aloud, translate covered, retell in own words.",
  "Rewrite the story with your own day.",
 ],
 "standards": [
  "JLPT N5-N4 reading band.",
 ],
 "citations": [
  "Japan Foundation. Japanese Language Proficiency Test Official Practice Materials, N5.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "The simple day becomes the Signature daily circuit: "
  "Taro's ten sentences ten sworn stations of an ordinary day - waking, "
  "washing, eating, departing, learning, returning - each sealed with ます "
  "like a timecard punched at every post. In this framing the ordinary is "
  "the highest oath of all: to do the small things rightly, in order, every "
  "day, is the foundation every greater work stands on. The learner who can "
  "retell the day owns the circuit. This is his original framing, clearly "
  "labeled Signature-made."
 )},
# --------------------------------------------------------------- 26 story II
{"key": "story2",
 "name": "Japanese Short Story II: A Past Adventure",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "A 10-sentence story using past-tense forms, with line-by-line English "
  "translation. 1. 去年の 夏、 家族で 海に 行きました。(きょねんの なつ、 "
  "かぞくで うみに いきました。 Kyonen no natsu, kazoku de umi ni "
  "ikimashita.) Last summer, I went to the sea with my family. 2. 朝早く 車で "
  "出発しました。(あさはやく くるまで しゅっぱつしました。 Asahayaku kuruma "
  "de shuppatsu shimashita.) We departed early in the morning by car. 3. 三時間 "
  "かかりました。(さんじかん かかりました。 Sanjikan kakarimashita.) It took "
  "three hours. 4. 海は 青くて きれいでした。(うみは あおくて きれいでした。 "
  "Umi wa aokute kirei deshita.) The sea was blue and beautiful. 5. 泳いだり "
  "貝を 拾ったり しました。(およいだり かいを ひろったり しました。 Oyoidari "
  "kai o hirottari shimashita.) We swam and gathered shells, among other "
  "things. 6. 昼ご飯に 海鮮丼を 食べました。(ひるごはんに かいせんどんを "
  "たべました。 Hirugohan ni kaisendon o tabemashita.) We ate a seafood bowl "
  "for lunch. 7. とても 美味しかったです。(とても おいしかったです。 Totemo "
  "oishikatta desu.) It was very delicious. 8. 夕方、 夕日が きれいでした。"
  "(ゆうがた、 ゆうひが きれいでした。 Yuugata, yuuhi ga kirei deshita.) In "
  "the evening, the sunset was beautiful. 9. 写真を たくさん 撮りました。(しゃしんを "
  "たくさん とりました。 Shashin o takusan torimashita.) We took lots of "
  "photos. 10. 楽しい 思い出に なりました。(たのしい おもいでに なりました。 "
  "Tanoshii omoide ni narimashita.) It became a happy memory. Reading guide: "
  "the story runs on ました/でした past forms; たり lists representative "
  "actions (泳いだり...拾ったり); い-adjectives turn past with かった "
  "(美味しかった, きれいでした for na)."
 ),
 "how_it_works": (
  "This record moves the story into the past: ます becomes ました, です "
  "becomes でした, and adjectives take かった/でした. The たり form lists "
  "sample actions from a longer day - 泳いだり貝を拾ったり means swimming "
  "and shell-gathering among other unlisted fun. Read it as a memory: first "
  "translate each line, then close the book and retell the trip as your own "
  "memory in the past tense. The past tense is the tense of stories, and "
  "this record hands it to you complete."
 ),
 "key_points": [
  "10-sentence past-tense story with line-by-line translation.",
  "Past forms: ました for verbs, でした for です, かった for i-adjectives.",
  "たり lists representative actions: 泳いだり貝を拾ったりしました.",
  "Time anchors: 去年の夏, 朝早く, 夕方.",
  "Retell as your own memory to lock the past tense.",
 ],
 "requirements": [
  "Verb Tenses record for ました/でした forms.",
  "Story I record for the three-way reading method.",
  "Retell the trip as your own past memory.",
 ],
 "standards": [
  "JLPT N5-N4 reading band.",
 ],
 "citations": [
  "Japan Foundation. Japanese Language Proficiency Test Official Practice Materials, N5.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "The past adventure becomes the Signature memory-vault: "
  "each ました a seal pressed into the record of what was, each でした a "
  "plaque mounted on the finished day. The たり form is the sampler's seal - "
  "two actions named honestly as samples of a fuller day, never pretending "
  "to be the whole. In this framing memory is the treasury: 楽しい思い出に"
  "なりました is the vault door closing on a day well sealed. This is his "
  "original framing, clearly labeled Signature-made."
 )},
# -------------------------------------------------------------- 27 story III
{"key": "story3",
 "name": "Japanese Short Story III: A Future Dream",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "A 10-sentence story using future and conditional forms, with line-by-line "
  "English translation. 1. 来年、 わたしは 日本に 行く つもりです。(らいねん、 "
  "わたしは にほんに いく つもりです。 Rainen, watashi wa Nihon ni iku "
  "tsumori desu.) Next year, I intend to go to Japan. 2. 東京で 一ヶ月 暮らす "
  "予定です。(とうきょうで いっかげつ くらす よていです。 Toukyou de "
  "ikkagetsu kurasu yotei desu.) I plan to live in Tokyo for a month. 3. 日本語学校に "
  "通う でしょう。(にほんごがっこうに かよう でしょう。 Nihongo gakkou ni "
  "kayou deshou.) I will probably attend a Japanese language school. 4. 毎日 "
  "日本語で 話す ように なります。(まいにち にほんごで はなす ように なります。 "
  "Mainichi Nihongo de hanasu you ni narimasu.) I will get to where I speak "
  "Japanese every day. 5. もし 時間が あれば、 京都にも 行きたいです。(もし "
  "じかんが あれば、 きょうとにも いきたいです。 Moshi jikan ga areba, Kyouto "
  "ni mo ikitai desu.) If I have time, I want to go to Kyoto too. 6. 友達が "
  "できたら、 一緒に 旅行します。(ともだちが できたら、 いっしょに りょこうします。 "
  "Tomodachi ga dekitara, issho ni ryokou shimasu.) If I make friends, we "
  "will travel together. 7. おいしい物を たくさん 食べる でしょう。(おいしい "
  "ものを たくさん たべる でしょう。 Oishii mono o takusan taberu deshou.) "
  "I will probably eat lots of delicious food. 8. 富士山に 登りたいです。(ふじさんに "
  "のぼりたいです。 Fujisan ni noboritai desu.) I want to climb Mt. Fuji. 9. "
  "帰る時には、 日本語が 上手に なって いるでしょう。(かえるときには、 にほんごが "
  "じょうずに なって いるでしょう。 Kaeru toki ni wa, Nihongo ga jouzu ni "
  "natte iru deshou.) By the time I return, my Japanese will probably have "
  "improved. 10. 夢が 叶う日を 楽しみに しています。(ゆめが かなうひを "
  "たのしみに しています。 Yume ga kanau hi o tanoshimi ni shite imasu.) I "
  "am looking forward to the day the dream comes true. Reading guide: つもり "
  "and 予定 declare plans; でしょう softens predictions; ば/たら build "
  "if-conditions (あれば, できたら); たい expresses want (行きたい, 登りたい)."
 ),
 "how_it_works": (
  "This record opens the future: つもり for firm intention, 予定 for "
  "scheduled plans, でしょう for soft predictions, たい for wants, and the "
  "ば/たら conditionals for if-then dreams. Notice the humility built into "
  "the grammar - Japanese rarely declares the future bluntly; でしょう "
  "probablizes, たい wants without demanding, たら conditions on what may "
  "come. Write your own ten-sentence future story using all five tools, and "
  "the future tense becomes a plan instead of a grammar point."
 ),
 "key_points": [
  "10-sentence future/conditional story with line-by-line translation.",
  "つもり firm intention; 予定 scheduled plan; でしょう soft prediction.",
  "たい expresses want: 行きたい, 登りたい.",
  "Conditionals: ば (あれば), たら (できたら).",
  "Japanese softens future claims; でしょう probablizes.",
 ],
 "requirements": [
  "Verb Tenses record for つもり.",
  "Stories I and II for the reading method.",
  "Write your own ten-sentence future story.",
 ],
 "standards": [
  "JLPT N4 reading band.",
 ],
 "citations": [
  "Martin SE. A Reference Grammar of Japanese. University of Hawaii Press; 1975.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "The future dream becomes the Signature forward-oath: "
  "つもり the carved intention-seal, 予定 the scheduled seal entered in the "
  "ledger, でしょう the humble probability-seal that never overclaims, たい "
  "the honest want-seal. The conditionals are the gate-seals - たら the gate "
  "that opens if friends are made, ば the gate that opens if time allows. In "
  "this framing a dream is not a wish but a forward contract, signed in "
  "grammar, witnessed by the listener. This is his original framing, clearly "
  "labeled Signature-made."
 )},
# ----------------------------------------------------------------- 28 idioms
{"key": "idioms",
 "name": "Japanese Idioms and Proverbs",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "20 idioms and proverbs - literal translation, real meaning, and an "
  "example sentence each. 1. 猿も木から落ちる (さるも きから おちる, saru mo "
  "ki kara ochiru) - literal: even monkeys fall from trees; meaning: experts "
  "make mistakes too. 先生でも 間違える。猿も木から落ちる。(せんせいでも "
  "まちがえる。さるも きから おちる。 Sensei demo machigaeru. Saru mo ki kara "
  "ochiru.) Even teachers err - even monkeys fall from trees. 2. 石の上にも"
  "三年 (いしの うえにも さんねん, ishi no ue ni mo sannen) - literal: three "
  "years on a stone; meaning: perseverance wins. 3. 七転八起 (ななころび "
  "やおき, nanakorobi yaoki) - literal: fall seven times, rise eight; "
  "meaning: never give up. 4. 虎穴に入らずんば虎子を得ず (こけつに いらずんば "
  "こじを えず, koketsu ni irazunba koji o ezu) - literal: if you do not enter "
  "the tiger's cave you will not catch its cub; meaning: nothing ventured, "
  "nothing gained. 5. 花より団子 (はなより だんご, hana yori dango) - literal: "
  "dumplings over flowers; meaning: substance over style. 6. 井の中の蛙 (いの "
  "なかの かわず, i no naka no kawazu) - literal: a frog in a well; meaning: "
  "a narrow-minded person. 7. 猫に小判 (ねこに こばん, neko ni koban) - "
  "literal: gold coins to a cat; meaning: pearls before swine. 8. 十人十色 "
  "(じゅうにん といろ, juunin toiro) - literal: ten people, ten colors; "
  "meaning: to each their own. 9. 一期一会 (いちご いちえ, ichigo ichie) - "
  "literal: one time, one meeting; meaning: cherish each encounter as "
  "unrepeatable. 10. 塵も積もれば山となる (ちりも つもれば やまとなる, chiri "
  "mo tsumoreba yama to naru) - literal: dust piled up becomes a mountain; "
  "meaning: many a little makes a mickle. 11. 口は災いの元 (くちは わざわいの "
  "もと, kuchi wa wazawai no moto) - literal: the mouth is the source of "
  "calamity; meaning: watch your words. 12. 笑う門には福来る (わらう かどには "
  "ふく きたる, warau kado ni wa fuku kitaru) - literal: fortune comes to the "
  "laughing gate; meaning: happiness attracts happiness. 13. 郷に入っては郷に"
  "従え (ごうに いっては ごうに したがえ, gou ni itte wa gou ni shitagae) - "
  "literal: entering a village, follow the village; meaning: when in Rome, do "
  "as the Romans do. 14. 能ある鷹は爪を隠す (のうある たかは つめを かくす, "
  "nou aru taka wa tsume o kakusu) - literal: the able hawk hides its talons; "
  "meaning: the truly skilled do not show off. 15. 早起きは三文の徳 (はやおきは "
  "さんもんの とく, hayaoki wa sanmon no toku) - literal: early rising is "
  "three coins of profit; meaning: the early bird catches the worm. 16. 継続は"
  "力なり (けいぞくは ちからなり, keizoku wa chikara nari) - literal: "
  "continuation becomes strength; meaning: persistence is power. 17. 失敗は"
  "成功のもと (しっぱいは せいこうの もと, shippai wa seikou no moto) - "
  "literal: failure is the root of success; meaning: failure teaches success. "
  "18. 時は金なり (ときは かねなり, toki wa kane nari) - literal: time is "
  "money; meaning: time is money. 19. 類は友を呼ぶ (るいは ともを よぶ, rui "
  "wa tomo o yobu) - literal: kind calls kind; meaning: birds of a feather "
  "flock together. 20. 明日は明日の風が吹く (あしたは あしたの かぜが ふく, "
  "ashita wa ashita no kaze ga fuku) - literal: tomorrow's wind will blow "
  "tomorrow; meaning: tomorrow will take care of itself."
 ),
 "how_it_works": (
  "This record teaches idioms as compressed wisdom: each one is a whole "
  "essay folded into a single line. Learn them in the three-part rhythm used "
  "here - say the Japanese, picture the literal scene (a monkey falling, "
  "dust becoming a mountain), then land the real meaning. The literal image "
  "is the memory hook; the meaning is the tool. Drop one fitting proverb "
  "into conversation per week and native speakers will hear the years of "
  "study behind it."
 ),
 "key_points": [
  "20 idioms and proverbs with literal translation, real meaning, and example.",
  "Learn in three beats: Japanese, literal image, real meaning.",
  "The literal scene is the memory hook.",
  "Proverbs signal deep cultural fluency.",
  "Use one per week in real conversation.",
 ],
 "requirements": [
  "All vocabulary records for the words inside the idioms.",
  "Picture each literal scene vividly.",
  "Use one proverb per week in conversation.",
 ],
 "standards": [
  "JLPT N4-N3 idiom band.",
 ],
 "citations": [
  "Japanese proverb collections (kotowaza) as documented in standard references.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "Idioms become the Signature wisdom-seals: each proverb a "
  "truth compressed and sworn by generations - 七転八起 the "
  "rise-again seal, 一期一会 the unrepeatable-meeting seal, 継続は力なり the "
  "persistence seal. In this framing the speaker who uses a proverb does not "
  "quote words but invokes witnesses: countless speakers who sealed the same "
  "truth before. The literal image is the seal's face, the meaning its "
  "impression. This is his original framing, clearly labeled Signature-made."
 )},
# --------------------------------------------------------------- 29 registers
{"key": "registers",
 "name": "Japanese Formal and Polite Registers",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "15 formal versus informal pairs for letters, business, and elders, with "
  "translations. The system: sonkeigo (respectful language) raises the other "
  "person; kenjougo (humble language) lowers yourself; teineigo (polite "
  "です/ます language) is the neutral middle. 1. 食べる (たべる, taberu) eat "
  "→ 召し上がる (めしあがる, meshiagaru) eat (respectful). どうぞ 召し上がって "
  "ください。(どうぞ めしあがって ください。 Douzo meshiagatte kudasai.) "
  "Please eat. 2. 見る (みる, miru) see → ご覧になる (ごらんになる, goran ni "
  "naru) see (respectful). ご覧に なりましたか。(ごらんに なりましたか。 Goran "
  "ni narimashita ka.) Did you see it. 3. する (suru) do → なさる (nasaru) do "
  "(respectful). どう なさいますか。(どう なさいますか。 Dou nasaimasu ka.) "
  "What will you do. 4. 言う (いう, iu) say → おっしゃる (ossharu) say "
  "(respectful). 先生が おっしゃいました。(せんせいが おっしゃいました。 "
  "Sensei ga osshaimashita.) The teacher said. 5. 来る (くる, kuru) come → "
  "いらっしゃる (irassharu) come (respectful). 明日 いらっしゃいますか。(あした "
  "いらっしゃいますか。 Ashita irasshaimasu ka.) Will you come tomorrow. 6. "
  "いる (iru) be → いらっしゃる (irassharu) be (respectful). 社長は いらっしゃいますか。"
  "(しゃちょうは いらっしゃいますか。 Shachou wa irasshaimasu ka.) Is the "
  "president in. 7. 知る (しる, shiru) know → ご存知 (ごぞんじ, gozonji) know "
  "(respectful noun). ご存知ですか。(ごぞんじですか。 Gozonji desu ka.) Do you "
  "know. 8. もらう (morau) receive → いただく (itadaku) receive (humble). "
  "いただきます。(Itadakimasu.) I humbly receive. 9. あげる (ageru) give → "
  "さしあげる (sashiageru) give (humble). 先生に さしあげます。(せんせいに "
  "さしあげます。 Sensei ni sashiagemasu.) I give it to the teacher. 10. いる "
  "(iru) be → おる (oru) be (humble). 私は 東京に おります。(わたしは とうきょうに "
  "おります。 Watashi wa Toukyou ni orimasu.) I am in Tokyo (humble). 11. する "
  "(suru) do → いたす (itasu) do (humble). 案内 いたします。(あんない いたします。 "
  "Annai itashimasu.) I will guide you (humble). 12. 言う (いう, iu) say → "
  "申す (もうす, mousu) say (humble). 田中と 申します。(たなかと もうします。 "
  "Tanaka to moushimasu.) I am called Tanaka (humble). 13. 見る (みる, miru) "
  "see → 拝見する (はいけんする, haiken suru) see (humble). 拝見 いたします。"
  "(はいけん いたします。 Haiken itashimasu.) I will look (humble). 14. 食べる "
  "(たべる, taberu) eat → いただく (itadaku) eat (humble). いただきます。"
  "(Itadakimasu.) I humbly partake. 15. 行く (いく, iku) go → 参る (まいる, "
  "mairu) go (humble). 明日 参ります。(あした まいります。 Ashita mairimasu.) "
  "I will go tomorrow (humble). Rule of thumb: raise others with sonkeigo, "
  "lower yourself with kenjougo, and when in doubt use teineigo."
 ),
 "how_it_works": (
  "This record teaches keigo as a three-gear system. Gear one is teineigo - "
  "the です/ます you already speak - which is correct in most daily life. "
  "Gear two is sonkeigo, which raises the other person's actions: 食べる "
  "becomes 召し上がる, 来る becomes いらっしゃる. Gear three is kenjougo, "
  "which lowers your own actions: もらう becomes いただく, 言う becomes 申す. "
  "The master rule: never use sonkeigo on yourself and never use kenjougo "
  "on the other person. Learn the 15 pairs as swaps, and practice by "
  "rewriting one polite email per day in full keigo."
 ),
 "key_points": [
  "Three gears: teineigo (neutral polite), sonkeigo (raises others), kenjougo (lowers self).",
  "15 formal versus informal pairs with translations.",
  "Sonkeigo: 召し上がる, ご覧になる, なさる, おっしゃる, いらっしゃる.",
  "Kenjougo: いただく, さしあげる, おる, いたす, 申す, 拝見する, 参る.",
  "Never sonkeigo for yourself; never kenjougo for others.",
 ],
 "requirements": [
  "Core Verbs I and Commands records.",
  "Learn the 15 pairs as direct swaps.",
  "Rewrite one polite email per day in keigo.",
 ],
 "standards": [
  "JLPT N4-N3 keigo band.",
  "Standard sonkeigo/kenjougo forms.",
 ],
 "citations": [
  "Shibatani M. The Languages of Japan. Cambridge University Press; 1990.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "Registers become the Signature elevation-seals: "
  "sonkeigo the raising seal lifted beneath the other person - 召し上がる "
  "the lifted-eating seal, いらっしゃる the lifted-coming seal - and kenjougo "
  "the lowering seal the speaker places beneath themselves - いただく the "
  "lowered-receiving seal, 申す the lowered-speaking seal. In this framing "
  "politeness is load-bearing architecture: the speaker lowers their own "
  "floor so the other's ceiling rises, and the building of the conversation "
  "stands straight. This is his original framing, clearly labeled "
  "Signature-made."
 )},
# ----------------------------------------------------- 30 complex sentences
{"key": "complex",
 "name": "Japanese Compound and Complex Sentences",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "15 long sentences with clauses, connectors, and relative clauses - parsed "
  "and translated. 1. 雨が 降ったから、 家に いました。(あめが ふったから、 "
  "いえに いました。 Ame ga futta kara, ie ni imashita.) Because it rained, I "
  "stayed home. [から = because] 2. 忙しいので、 明日 行きます。(いそがしいので、 "
  "あした いきます。 Isogashii node, ashita ikimasu.) Since I am busy, I will "
  "go tomorrow. [ので = since, softer than から] 3. 日本語は 難しいですが、 "
  "楽しいです。(にほんごは むずかしいですが、 たのしいです。 Nihongo wa "
  "muzukashii desu ga, tanoshii desu.) Japanese is difficult, but it is fun. "
  "[が = but] 4. 安いけど、 いい 店です。(やすいけど、 いい みせです。 Yasui "
  "kedo, ii mise desu.) It is cheap, but it is a good shop. [けど = but, "
  "casual] 5. 彼は 優しくて、 頭も いいです。(かれは やさしくて、 あたまも "
  "いいです。 Kare wa yasashikute, atama mo ii desu.) He is kind and also "
  "smart. [て-form chains qualities] 6. 映画を 見たり、 音楽を 聴いたり します。"
  "(えいがを みたり、 おんがくを きいたり します。 Eiga o mitari, ongaku o "
  "kiitari shimasu.) I watch movies and listen to music, among other things. "
  "[たり lists sample actions] 7. 早く 起きれば、 間に合います。(はやく おきれば、 "
  "まにあいます。 Hayaku okireba, maniaimasu.) If you wake early, you will "
  "make it in time. [ば = if] 8. 雨が 降ったら、 中止です。(あめが ふったら、 "
  "ちゅうしです。 Ame ga futtara, chuushi desu.) If it rains, it is "
  "cancelled. [たら = if/when] 9. 春に なると、 桜が 咲きます。(はるに なると、 "
  "さくらが さきます。 Haru ni naru to, sakura ga sakimasu.) When spring "
  "comes, the cherry blossoms bloom. [と = when, natural consequence] 10. 音楽を "
  "聴きながら、 勉強します。(おんがくを ききながら、 べんきょうします。 Ongaku "
  "o kikinagara, benkyou shimasu.) I study while listening to music. [ながら "
  "= while] 11. 健康の ために、 運動します。(けんこうの ために、 うんどうします。 "
  "Kenkou no tame ni, undou shimasu.) I exercise for my health. [ために = for "
  "the sake of] 12. 分かる ように、 説明します。(わかる ように、 せつめいします。 "
  "Wakaru you ni, setsumei shimasu.) I explain so that you understand. [ように "
  "= so that] 13. 窓を 開けた まま、 出かけました。(まどを あけた まま、 "
  "でかけました。 Mado o aketa mama, dekakemashita.) I went out leaving the "
  "window open. [まま = as it is] 14. 若い うちに、 旅行しなさい。(わかい "
  "うちに、 りょこうしなさい。 Wakai uchi ni, ryokou shinasai.) Travel while "
  "you are young. [うちに = while the state lasts] 15. 昨日 買った 本は、 "
  "とても 面白いです。(きのう かった ほんは、 とても おもしろいです。 Kinou "
  "katta hon wa, totemo omoshiroi desu.) The book I bought yesterday is very "
  "interesting. [relative clause: 昨日買った modifies 本]"
 ),
 "how_it_works": (
  "This record teaches long sentences as clause carpentry: build two short "
  "sentences you already know, then join them with one connector. The "
  "connectors each carry one job - から/ので for reason, が/けど for "
  "contrast, ば/たら for if, と for natural when, ながら for while, ために "
  "for purpose, ように for aim, まま for unchanged state, うちに for while-it-"
  "lasts. Relative clauses work backwards from English: the describing "
  "clause comes before the noun (昨日買った本 = yesterday-bought book). "
  "Parse each of the 15 with the bracketed notes, then build five of your "
  "own by joining sentence pairs."
 ),
 "key_points": [
  "15 parsed long sentences with connectors and relative clauses.",
  "から/ので reason; が/けど contrast; ば/たら if; と natural when.",
  "ながら while; ために purpose; ように aim; まま unchanged; うちに while-it-lasts.",
  "Relative clauses precede the noun: 昨日買った本.",
  "Build by joining two known short sentences with one connector.",
 ],
 "requirements": [
  "Grammar Essentials and Verb Tenses records.",
  "Parse all 15 with the bracketed notes.",
  "Build five own sentences by joining pairs.",
 ],
 "standards": [
  "JLPT N4-N3 grammar band.",
 ],
 "citations": [
  "Kuno S. The Structure of the Japanese Language. MIT Press; 1973.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "Complex sentences become the Signature joinery: each "
  "connector a sworn joint between timbers - から the reason-dovetail, が the "
  "contrast-hinge, ば the if-latch, ながら the parallel beam carrying two "
  "loads at once. The relative clause is the carved inscription set before "
  "the noun it honors: 昨日買った本, the book bearing yesterday's mark. In "
  "this framing the sentence-builder is a carpenter whose joints must hold "
  "under the weight of meaning, tested by reading aloud. This is his "
  "original framing, clearly labeled Signature-made."
 )},
# ------------------------------------------------------- 31 market dialogue
{"key": "convmarket",
 "name": "Japanese Conversation: At the Market",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "A 20-line bilingual dialogue at the market, annotated. A is the shopper, "
  "B the shopkeeper. 1. A: こんにちは。(Konnichiwa.) Hello. [greeting] 2. B: "
  "いらっしゃいませ。(Irasshaimase.) Welcome. [shop greeting] 3. A: この りんごは "
  "いくらですか。(Kono ringo wa ikura desu ka.) How much are these apples. "
  "[price ask] 4. B: 一つ 百円です。(Hitotsu hyaku-en desu.) 100 yen each. "
  "[price answer] 5. A: 高いですね。もう少し 安く なりませんか。(Takai desu ne. "
  "Mou sukoshi yasuku narimasen ka.) That is pricey. Can you go a little "
  "lower. [soft bargain] 6. B: 五つで 四百五十円で どうですか。(Itsutsu de "
  "yonhyaku-gojuu-en de dou desu ka.) How about five for 450 yen. "
  "[counter-offer] 7. A: 四百円で おねがいします。(Yonhyaku-en de onegaishimasu.) "
  "400 yen, please. [firm offer] 8. B: 分かりました。四百円です。(Wakarimashita. "
  "Yonhyaku-en desu.) Understood. 400 yen it is. [acceptance] 9. A: この みかんも "
  "ください。(Kono mikan mo kudasai.) These mandarins too, please. [add-on] "
  "10. B: みかんは 一袋 三百円です。(Mikan wa hitofukuro sanbyaku-en desu.) "
  "The mandarins are 300 yen a bag. [add-on price] 11. A: じゃあ、 りんごと "
  "みかんで 七百円ですね。(Jaa, ringo to mikan de nanahyaku-en desu ne.) So "
  "apples and mandarins, 700 yen total. [total check] 12. B: はい、七百円です。"
  "(Hai, nanahyaku-en desu.) Yes, 700 yen. [confirm] 13. A: 千円で おねがいします。"
  "(Sen-en de onegaishimasu.) 1,000 yen, please. [pay] 14. B: 千円 お預かりします。"
  "おつり 三百円です。(Sen-en oazukari shimasu. Otsuri sanbyaku-en desu.) "
  "1,000 received. 300 yen change. [change] 15. A: 袋は 要りません。(Fukuro wa "
  "irimasen.) I do not need a bag. [eco choice] 16. B: かしこまりました。(Kashiko"
  "marimashita.) Certainly. [polite reply] 17. A: 領収書を ください。(Ryoushuusho "
  "o kudasai.) A receipt, please. [receipt] 18. B: はい、どうぞ。(Hai, douzo.) "
  "Here you are. [hand over] 19. A: ありがとうございました。また 来ます。"
  "(Arigatou gozaimashita. Mata kimasu.) Thank you. I will come again. "
  "[thanks and loyalty] 20. B: ありがとうございました。(Arigatou gozaimashita.) "
  "Thank you very much. [closing thanks] Study notes: the bargain runs lines "
  "5-8; the total-check at line 11 prevents money mistakes; おつり is given "
  "with the polite お預かりします frame."
 ),
 "how_it_works": (
  "This record stages the whole market dance from the shopping record as a "
  "live dialogue: greeting, price ask, soft bargain, counter-offer, firm "
  "offer, acceptance, add-on, total check, payment, change, receipt, thanks. "
  "Perform it with a partner, swapping roles, until the bargain lines (5-8) "
  "flow without pausing. Then improvise: change the fruit, change the "
  "numbers, keep the frames. The dialogue is the exam for everything the "
  "ladder taught about buying."
 ),
 "key_points": [
  "20-line bilingual market dialogue, annotated line by line.",
  "Bargain arc: lines 5-8 (ask, counter, offer, accept).",
  "Total-check line 11 prevents money mistakes.",
  "Payment frame: 千円お預かりします, おつり三百円です.",
  "Perform with a partner, swap roles, then improvise.",
 ],
 "requirements": [
  "Shopping and Money record for the bargain frames.",
  "A partner for role-play; swap A and B.",
  "Improvise with new fruit and new numbers.",
 ],
 "standards": [
  "JLPT N4 conversation band.",
 ],
 "citations": [
  "Japan Foundation. Japanese Language Proficiency Test Official Practice Materials, N5.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "The market dialogue becomes the Signature exchange "
  "ceremony in full: twenty sworn moves from こんにちは to ありがとうございま"
  "した, each line a seal pressed in sequence - the weighing, the haggling, "
  "the settling, the change returned exact. In this framing buyer and seller "
  "are not opponents but co-keepers of the fair-weight oath, and また来ます "
  "is the highest seal a merchant can earn: the customer's sworn return. "
  "This is his original framing, clearly labeled Signature-made."
 )},
# ------------------------------------------------------- 32 friend dialogue
{"key": "convfriend",
 "name": "Japanese Conversation: Meeting a Friend",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "A 20-line bilingual dialogue between old friends, annotated. A and B are "
  "friends meeting after a long time. 1. A: 久しぶり。(Hisashiburi.) Long "
  "time no see. [warm opener] 2. B: 本当に 久しぶりだね。(Hontou ni "
  "hisashiburi da ne.) Really long time. [agreement] 3. A: 元気だった。"
  "(Genki datta.) I have been well. [casual report] 4. B: うん、元気だよ。"
  "最近 どう。(Un, genki da yo. Saikin dou.) Yeah, fine. How about you lately. "
  "[return ask] 5. A: 仕事が 忙しくてさ。(Shigoto ga isogashikute sa.) Work "
  "has been busy. [casual て-form] 6. B: そうなんだ。大変だね。(Sou nan da. "
  "Taihen da ne.) I see. That is tough. [sympathy] 7. A: でも 週末は 休めるよ。"
  "(Demo shuumatsu wa yasumeru yo.) But I can rest on weekends. [relief] 8. "
  "B: 今度の 日曜日、 空いてる。(Kondo no nichiyoubi, aiteru.) Are you free "
  "next Sunday. [invitation] 9. A: うん、空いてるよ。(Un, aiteru yo.) Yeah, "
  "I am free. [accept] 10. B: じゃあ、映画を 見に 行こう。(Jaa, eiga o mi ni "
  "ikou.) Then let us go see a movie. [proposal] 11. A: いいね。何を 見る。"
  "(Ii ne. Nani o miru.) Sounds good. What shall we watch. [pick] 12. B: 新しい "
  "アクション映画が いいな。(Atarashii akushon eiga ga ii na.) The new action "
  "movie sounds good. [choice] 13. A: いいよ。何時に 会う。(Ii yo. Nanji ni "
  "au.) Fine. What time shall we meet. [time] 14. B: 二時に 駅前で どう。"
  "(Niji ni ekimae de dou.) How about 2 at the station front. [meetup] 15. A: "
  "分かった。二時にね。(Wakatta. Niji ni ne.) Got it. Two o'clock. [confirm] "
  "16. B: 楽しみだな。(Tanoshimi da na.) I am looking forward to it. "
  "[anticipation] 17. A: 俺もだよ。(Ore mo da yo.) Me too. [match] 18. B: "
  "じゃあ、また 日曜日に。(Jaa, mata nichiyoubi ni.) See you Sunday then. "
  "[parting] 19. A: うん、またね。(Un, mata ne.) Yeah, see you. [casual bye] "
  "20. B: バイバイ。(Baibai.) Bye. [loanword bye] Study notes: casual forms "
  "dominate - だ, だよ, だね, さ endings; invitations use the volitional "
  "行こう; the meetup is fixed with time plus place."
 ),
 "how_it_works": (
  "This record teaches the casual register as its own dialect: だ/だよ/だね "
  "endings, さ sentence softeners, volitional invitations (行こう), and "
  "dropped particles - all the things textbooks delay but friends use "
  "constantly. Perform it fast and loose, the way friends actually talk, "
  "then perform it again in polite form to feel the distance the register "
  "creates. The rule to carry away: casual is for equals and intimates "
  "only; the moment a senior enters, the whole dialogue shifts back to "
  "です/ます."
 ),
 "key_points": [
  "20-line bilingual friends dialogue, annotated.",
  "Casual markers: だ/だよ/だね, さ, volitional 行こう, dropped particles.",
  "Meetup frame: time plus place (二時に駅前で).",
  "Contrast with the polite register to feel the distance.",
  "Casual is for equals and intimates only.",
 ],
 "requirements": [
  "Friendship record and Commands record (volitional).",
  "Perform fast in casual, then again in polite.",
  "A close friend or study partner for realism.",
 ],
 "standards": [
  "JLPT N4 conversation band.",
 ],
 "citations": [
  "Japan Foundation. Japanese Language Proficiency Test Official Practice Materials, N5.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "The friends dialogue becomes the Signature reunion rite: "
  "twenty lines of the unsealed speech - だ and だよ the bare-voice seals "
  "that only sworn close companions may use with each other. In this framing "
  "casual speech is not careless speech but the highest trust-oath: to drop "
  "the polite armor is to swear the other person is safe. The meetup sealed "
  "with 二時に駅前で is the renewal of the alliance, kept exactly. This is "
  "his original framing, clearly labeled Signature-made."
 )},
# ------------------------------------------------------ 33 problem dialogue
{"key": "convproblem",
 "name": "Japanese Conversation: Solving a Problem",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "A 20-line bilingual dialogue solving a lost-wallet problem, annotated. A "
  "lost a wallet; B is a station attendant. 1. A: すみません。(Sumimasen.) "
  "Excuse me. [attention] 2. B: はい、何でしょうか。(Hai, nan deshou ka.) "
  "Yes, how may I help. [service open] 3. A: 財布を なくしました。(Saifu o "
  "nakushimashita.) I lost my wallet. [problem stated] 4. B: どこで なくされ"
  "ましたか。(Doko de nakusaremashita ka.) Where did you lose it. [respectful "
  "past] 5. A: 電車の 中だと 思います。(Densha no naka da to omoimasu.) I "
  "think it was in the train. [best guess] 6. B: 何線でしたか。(Nansen deshita "
  "ka.) Which line was it. [narrow down] 7. A: 山手線です。(Yamanotesen desu.) "
  "The Yamanote line. [answer] 8. B: お名前と ご連絡先を 教えて ください。"
  "(Onamae to gorenrakusaki o oshiete kudasai.) Please tell me your name and "
  "contact. [info request] 9. A: 田中太郎です。電話は ゼロ九ゼロ...です。"
  "(Tanaka Tarou desu. Denwa wa zero-kyuu-zero... desu.) I am Taro Tanaka. My "
  "phone is 090... [info given] 10. B: 財布の 特徴を 教えて ください。(Saifu no "
  "tokuchou o oshiete kudasai.) Please describe the wallet. [description ask] "
  "11. A: 茶色の 長財布です。(Chairo no nagazaifu desu.) A brown long wallet. "
  "[description] 12. B: 中身は 覚えて いますか。(Nakami wa oboete imasu ka.) "
  "Do you remember the contents. [verify] 13. A: 現金が 一万円と カードが "
  "二枚です。(Genkin ga ichiman-en to kaado ga ni-mai desu.) 10,000 yen cash "
  "and two cards. [contents] 14. B: 調べますので、 少々 お待ち ください。"
  "(Shirabemasu node, shoushou omachi kudasai.) I will check, so please wait "
  "a moment. [action promised] 15. A: おねがいします。(Onegaishimasu.) Please. "
  "[trust] 16. B: ありました。こちらです。(Arimashita. Kochira desu.) Found it. "
  "Here it is. [resolution] 17. A: あった。ありがとうございます。(Atta. "
  "Arigatou gozaimasu.) There it is. Thank you. [relief and thanks] 18. B: "
  "中身を ご確認 ください。(Nakami o gokakunin kudasai.) Please check the "
  "contents. [verify return] 19. A: 大丈夫です。本当に 助かりました。(Daijoubu "
  "desu. Hontou ni tasukarimashita.) All fine. You really saved me. [confirm] "
  "20. B: お気をつけて。(Oki o tsukete.) Take care. [warm close] Study notes: "
  "the attendant uses respectful forms (なくされましたか, お待ちください); "
  "the problem follows state-narrow-describe-verify-resolve; 中身の確認 "
  "protects both sides."
 ),
 "how_it_works": (
  "This record teaches problem-solving as a five-move protocol: state the "
  "problem (なくしました), narrow it down (何線でしたか), describe the thing "
  "(茶色の長財布です), verify ownership (中身は覚えていますか), resolve and "
  "confirm (ご確認ください). The keigo here is real-world: station staff "
  "speak respectful Japanese to every customer, and matching their "
  "politeness keeps the interaction smooth. Memorize the five moves and you "
  "can report anything lost, broken, or wrong anywhere in Japan."
 ),
 "key_points": [
  "20-line bilingual problem-solving dialogue, annotated.",
  "Five-move protocol: state, narrow, describe, verify, resolve.",
  "Respectful forms: なくされましたか, お待ちください, ご確認ください.",
  "Contents check (中身の確認) protects both sides.",
  "Protocol works for anything lost, broken, or wrong.",
 ],
 "requirements": [
  "Formal and Polite Registers record.",
  "Memorize the five moves in order.",
  "Practice with a different lost item.",
 ],
 "standards": [
  "JLPT N4 conversation band.",
 ],
 "citations": [
  "Japan Foundation. Japanese Language Proficiency Test Official Practice Materials, N5.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "The problem dialogue becomes the Signature recovery "
  "rite: the lost wallet a broken circuit, the five moves the sworn repair "
  "protocol - state the break, narrow the field, describe the missing part, "
  "verify the rightful owner, restore and confirm. In this framing the "
  "attendant is the repair-sworn keeper of the station, and お気をつけて is "
  "the closing ward-seal against future loss. Nothing is truly lost while "
  "the protocol is kept. This is his original framing, clearly labeled "
  "Signature-made."
 )},
# ------------------------------------------------------------ 34 mastery
{"key": "mastery",
 "name": "Japanese Mastery Review and Full Reference",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "The whole database in one teaching summary. Kana quick table: the 46 "
  "basic sounds あいうえお through わをん in hiragana and アイウエオ through "
  "ワヲン in katakana, plus voiced がぎぐげご/ざじずぜぞ/だぢづでど/ばびぶべぼ/"
  "ぱぴぷぺぽ and contracted きゃきゅきょ/しゃしゅしょ/ちゃちゅちょ. Core "
  "vocabulary consolidated: the 25 nouns (人, 男, 女, 子ども, 友達, 家族, 家, "
  "学校, 会社, 店, 駅, 電車, 車, 本, 新聞, 手紙, 電話, 水, お茶, ご飯, 肉, 魚, "
  "野菜, 果物, お金), the 25 verbs (する, いる, ある, 行く, 来る, 帰る, 食べる, "
  "飲む, 見る, 聞く, 話す, 読む, 書く, 買う, 売る, 作る, 働く, 勉強する, 教える, "
  "習う, 会う, 知る, 思う, 寝る, 起きる), the 25 adjectives (大きい, 小さい, "
  "新しい, 古い, 高い, 安い, 暑い, 寒い, 美味しい, 忙しい, 楽しい, 悲しい, "
  "嬉しい, 近い, 遠い, 速い, 遅い, 明るい, 暗い, 強い, 弱い, 有名, 親切, 元気, "
  "静か), the 15 adverbs (とても, すごく, あまり, 全然, もう, まだ, いつも, "
  "よく, ときどき, ゆっくり, はやく, たくさん, 少し, ぜひ, きっと), the "
  "pronoun compass (わたし/ぼく/おれ, あなた/きみ, かれ/かのじょ, これ/それ/あれ/"
  "どれ, この/その/あの/どの, ここ/そこ/あそこ/どこ), the numbers (いち to "
  "じゅう, ひゃく, せん, まん), the time words (曜日, 月, 季節, 時分), the 30 "
  "greetings, the 20 idioms, and the 15 keigo pairs - over 200 core words in "
  "all. Grammar condensed: SOV order; particles は が を に へ で と も から "
  "まで の; i-adjectives conjugate, na-adjectives take な; ます/ました "
  "present/past; て-form joins; ない/ません negate; か questions; ば/たら "
  "conditionals; sonkeigo raises others, kenjougo lowers self. Phrase tables: "
  "the meal pair (いただきます/ごちそうさまでした), the home pair (ただいま/"
  "おかえり), the shopping dance (いくらですか/安くなりませんか/ください), the "
  "travel kit (どこですか/いくらですか/助けてください), the problem protocol "
  "(state/narrow/describe/verify/resolve). Conversation frames: market "
  "bargain, friend meetup, lost-and-found. Study path: read records 1-10 for "
  "the skeleton, drill 11-20 for daily life, perform 21-34 for fluency; "
  "retell all three stories from memory; hold one full keigo conversation. "
  "Example capstone sentences: 一年間 日本語を 勉強しました。(いちねんかん "
  "にほんごを べんきょうしました。 Ichinenkan Nihongo o benkyou shimashita.) "
  "I studied Japanese for one year. まだまだ ですが、 毎日 頑張ります。(まだまだ "
  "ですが、 まいにち がんばります。 Madamada desu ga, mainichi ganbarimasu.) "
  "I am still learning, but I do my best every day. 日本語で 夢を 語れる ように "
  "なりました。(にほんごで ゆめを かたれる ように なりました。 Nihongo de "
  "yume o katareru you ni narimashita.) I became able to talk about my dreams "
  "in Japanese."
 ),
 "how_it_works": (
  "This record is the capstone and the index: everything the 33 records "
  "before it taught, compressed onto one page for review and lookup. Use it "
  "three ways. As a checklist, tick off each block you can produce from "
  "memory. As a reference, jump to any table when a conversation demands it. "
  "As an exam, cover the Japanese column and reproduce it, then uncover and "
  "correct. When every block passes from memory, the ladder is climbed: "
  "foundations, compounded, and advanced all live in one speaker now."
 ),
 "key_points": [
  "Consolidated quick-reference: kana, 200+ core words, key grammar, all phrase tables.",
  "Vocabulary blocks: 25 nouns, 25 verbs, 25 adjectives, 15 adverbs, pronouns, numbers, greetings, idioms, keigo.",
  "Grammar condensed to one paragraph.",
  "Phrase tables: meals, home, shopping, travel, problem protocol.",
  "Three uses: checklist, reference, exam.",
 ],
 "requirements": [
  "All 33 preceding records.",
  "Tick each block from memory; reproduce covered columns.",
  "Retell all three stories from memory.",
 ],
 "standards": [
  "JLPT N5-N4 cumulative band.",
  "Joyo kanji and kana tables as listed.",
 ],
 "citations": [
  "Shibatani M. The Languages of Japan. Cambridge University Press; 1990.",
  "Tsujimura N. An Introduction to Japanese Linguistics. 4th ed. Wiley-Blackwell; 2023.",
  "Martin SE. A Reference Grammar of Japanese. University of Hawaii Press; 1975.",
  "Kuno S. The Structure of the Japanese Language. MIT Press; 1973.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "The mastery review becomes the Signature completion "
  "ceremony: all 34 seals gathered on one page - the sound-seals, the "
  "name-seals, the action-seals, the bridge-seals, the time-seals, the "
  "wisdom-seals - and the learner counts them like a general reviewing "
  "troops before the final march. In this framing fluency is not a score but "
  "a kept covenant: every seal sworn along the ladder, every oath honored in "
  "speech. The speaker who holds all 34 may open any door in the language. "
  "This is his original framing, clearly labeled Signature-made."
 )},
]
