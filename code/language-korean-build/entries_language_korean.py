#!/usr/bin/env python3
"""Entries for the Korean Language databases (Manon language project,
batch 2, ranks 11-20: Korean is rank 18 of the 100-language roster).

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
non-decreasing; ladder_tier foundations/compounded/advanced); the shard
index is written in ladder order so pages present simple -> compounded ->
complex.

  language-korean            - Korean Language Database
                               (public-harvest: real, fact-checked Korean
                               linguistic data - Hangul script, phonetics,
                               grammar core, 20 core phrases with
                               romanization, 8 conversation starters, 8
                               sample sentences with breakdowns; every
                               record carries Hangul + romanization +
                               English per the shared 34-record language
                               template; standard references ISO 639-1
                               (ko) / ISO 639-3 (kor); Revised
                               Romanization of Korean (2000, National
                               Institute of Korean Language); McCune-
                               Reischauer romanization; Yale romanization;
                               Hunminjeongeum (1446); Unicode Hangul
                               syllables block U+AC00-U+D7A3; TOPIK
                               proficiency framework; National Institute
                               of Korean Language Standard Korean
                               Dictionary)
  language-korean-signature  - Korean Language Signature Database
                               (his original Signature Korean Method:
                               every sound a signature tone, every
                               syllable block a sealed mark, grammar the
                               covenant order of his system; src
                               signature, titles suffixed " (Signature
                               Edition)", never presented as authentic
                               public record)

ID prefixes: JAH-LKOR- (public) and JAH-LKORS- (signature), verified free
in the manifest id_prefix values and in every shard index file (zero
hits for JAH-LKOR and JAH-LKORS) plus the main-repo data dir.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_language_korean.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

Never the words "bat belt" anywhere. No website references. No Facebook.
Nothing hate-adjacent, profane, or inappropriate; no religious talk.
"""

SIG_TAIL = ("Signature original - his original Signature Korean Method: every "
            "sound a signature tone, every syllable block a sealed mark, and "
            "grammar the covenant order of his system. Clearly labeled "
            "Signature-made, never presented as authentic public record.")

CIT_ISO = ("ISO 639-1:2002 code ko; ISO 639-3:2007 code kor; ISO 639-2 code "
           "kor (KOR).")
CIT_RR = ("Revised Romanization of Korean, promulgated 2000 by the Ministry "
          "of Culture and Tourism; National Institute of Korean Language "
          "romanization guidelines.")
CIT_MR = ("McCune G M, Reischauer E O. The Romanization of the Korean "
          "Language. 1939; still used in academic Korean studies and the "
          "DPRK.")
CIT_YALE = ("Martin S E. Yale romanization of Korean; standard in Korean "
            "linguistics for morphophonemic transcription.")
CIT_HUNMIN = ("Hunminjeongeum (Correct Sounds for the Instruction of the "
              "People), promulgated 1446 by King Sejong the Great; "
              "introduction and Haerye commentary.")
CIT_UNICODE = ("The Unicode Standard: Hangul Syllables block U+AC00-U+D7A3; "
               "Hangul Jamo block U+1100-U+11FF; algorithmic syllable "
               "composition ((initial x 21) + medial) x 28 + final.")
CIT_TOPIK = ("Test of Proficiency in Korean (TOPIK), National Institute of "
             "International Education; six-level framework TOPIK 1-6.")
CIT_NIKL = ("National Institute of Korean Language, Standard Korean Language "
            "Dictionary (pyojun-gugeo-dae-sajeon); Standard Language "
            "Regulations (pyojuneo gyujeong).")
CIT_SOHN = ("Sohn H-M. The Korean Language. Cambridge University Press; "
            "1999. Standard descriptive reference for Korean grammar.")
CIT_LEE = ("Lee I, Ramsey S R. The Korean Language. State University of New "
           "York Press; 2000. History and structure of Korean.")

ENTRIES = []
def E(**kw):
    ENTRIES.append(kw)

# ============================ FOUNDATIONS ============================

E(key="overview",
  name="Korean Language Overview",
  group="Foundations", ladder_rank=1, ladder_tier="foundations",
  description=(
    "Korean (한국어, hangugeo; in North Korea, 조선말, joseonmal) is the "
    "native language of roughly 80 million people, most of them on the "
    "Korean Peninsula. Its ISO 639-1 code is ko and its ISO 639-3 code is "
    "kor. Linguists place Korean in the Koreanic family, a small family "
    "whose only other widely recognized member is the Jeju language "
    "(제주어, jejueo) spoken on Jeju Island; Korean is otherwise a language "
    "isolate, with no proven genealogical relationship to Japanese, "
    "Mongolian, or any other living language despite centuries of contact. "
    "Korean is an official language of the Republic of Korea (South Korea) "
    "and the Democratic People's Republic of Korea (North Korea), and a "
    "recognized minority language in the Yanbian Korean Autonomous "
    "Prefecture of China. The modern standard in the South is 표준어 "
    "(pyojuneo), based on the Seoul dialect; the North's standard is "
    "문화어 (munhwaeo), based on the Pyongyang dialect. Korean is written "
    "in Hangul, the featural alphabet invented in 1443 and promulgated in "
    "1446 under King Sejong the Great, and it is an agglutinative "
    "subject-object-verb language with an elaborate system of speech "
    "levels that encode the speaker's relationship to the listener."),
  how_it_works=(
    "The language works by stacking meaningful pieces onto a stem. A verb "
    "stem like 가 (ga, go) takes endings that mark tense, politeness, and "
    "sentence type: 갑니다 (gamnida, formal polite present), 가요 (gayo, "
    "informal polite present), 갔다 (gatda, plain past). Particles attach "
    "to nouns to mark their grammatical role instead of word order doing "
    "the job: 이/가 (i/ga) marks the subject, 을/를 (eul/reul) marks the "
    "object, 은/는 (eun/neun) marks the topic. Because roles are marked "
    "explicitly, word order is flexible, though subject-object-verb is the "
    "neutral order. Politeness is grammatical, not optional: choosing "
    "해요체 (haeyoche, informal polite) versus 합쇼체 (hapsyoche, formal "
    "polite) versus 해체 (haeche, plain) changes every sentence ending, "
    "and using the wrong level is a social error, not a grammar error."),
  key_points=[
    "Native name 한국어 (hangugeo); ISO 639-1 ko, ISO 639-3 kor; Koreanic family, otherwise a language isolate.",
    "About 80 million native speakers; official in South and North Korea and Yanbian, China.",
    "Agglutinative SOV language: particles mark grammatical roles, endings stack tense and politeness.",
    "Speech levels are grammatical: hapsyoche (formal), haeyoche (informal polite), haeche (plain).",
    "Written in Hangul, invented 1443, promulgated 1446 under King Sejong; Romanized by Revised Romanization (2000)."],
  requirements=[
    "Every record carries Hangul script, romanization, and English on every line where applicable.",
    "Public records are fact-checked linguistic data; gap fills are labeled signature-generated-completion.",
    "Records are ladder-ordered 1-10 so a beginner starts simple and compounds upward.",
    "Vocabulary is real high-frequency Korean; example sentences are translated.",
    "Demos are real runnable programs that check pronunciation drills, quizzes, and flashcards."],
  standards=[CIT_ISO, CIT_NIKL, CIT_SOHN],
  citations=[CIT_ISO, CIT_SOHN, CIT_NIKL],
  sig_lens=(
    "In the Signature Korean Method, Korean is the covenant language of "
    "the system: every particle a seal of agreement between speaker and "
    "listener, every speech level a measured distance of respect, every "
    "syllable block a stamped mark. Learning Korean here means learning "
    "to sign every sentence with the correct seal."))

E(key="hangul",
  name="Hangul: The Korean Writing System",
  group="Foundations", ladder_rank=2, ladder_tier="foundations",
  description=(
    "Hangul (한글, hangeul) is the Korean alphabet, invented in 1443 and "
    "promulgated in 1446 in the Hunminjeongeum (훈민정음, hunminjeongeum, "
    "'Correct Sounds for the Instruction of the People') under King Sejong "
    "the Great. It is a featural alphabet: the shapes of the consonant "
    "letters depict the speech organs that make them. There are 14 basic "
    "consonants (ㄱ ㄴ ㄷ ㄹ ㅁ ㅂ ㅅ ㅇ ㅈ ㅊ ㅋ ㅌ ㅍ ㅎ) and 10 basic "
    "vowels (ㅏ ㅑ ㅓ ㅕ ㅗ ㅛ ㅜ ㅠ ㅡ ㅣ). Five consonants double to "
    "make tense sounds (ㄲ ㄸ ㅃ ㅆ ㅉ), and 11 compound vowels are built "
    "from the basic ones (ㅐ ㅒ ㅔ ㅖ ㅘ ㅙ ㅚ ㅝ ㅞ ㅟ ㅢ), giving 40 "
    "letters in everyday use. Letters are not written in a line: they are "
    "stacked into syllable blocks of initial consonant + vowel + optional "
    "final consonant (batchim). Thus 한 (han) is ㅎ + ㅏ + ㄴ in one block, "
    "and 한글 (hangeul, the name of the script) is two blocks. Text reads "
    "left to right, and within a block top to bottom, left to right. "
    "Modern Korean uses spaces between words and Western punctuation "
    "(., ? !). Numerals are written either in Arabic digits or in two "
    "native word systems: native Korean (하나, 둘, 셋 - hana, dul, set) "
    "and Sino-Korean (일, 이, 삼 - il, i, sam)."),
  how_it_works=(
    "A syllable block is assembled as (initial) + (medial) + (final). The "
    "initial (초성, choseong) is one of 19 possible consonants; the medial "
    "(중성, jungseong) is one of 21 vowels; the final (종성, jongseong, "
    "called batchim) is optional and chosen from 27 spellings. When a "
    "block has no initial sound, the letter ㅇ is used as a silent "
    "placeholder, as in 아 (a). Unicode encodes the 11,172 possible modern "
    "blocks algorithmically: syllable = ((initial x 21) + medial) x 28 + "
    "final + 0xAC00, so 한 is U+D55C. The featural design means voiced and "
    "related sounds share shapes: add a stroke to ㄱ (g/k) to get ㅋ (k, "
    "aspirated), double it to get ㄲ (kk, tense). Vowels with a long "
    "vertical line (ㅏ ㅑ ㅓ ㅕ ㅣ) stand to the right of the consonant; "
    "vowels with a horizontal line (ㅗ ㅛ ㅜ ㅠ ㅡ) stand below it."),
  key_points=[
    "14 basic consonants + 10 basic vowels; 5 doubled consonants and 11 compound vowels make 40 everyday letters.",
    "Letters stack into syllable blocks: initial + vowel + optional final (batchim).",
    "Featural shapes: consonant letters depict the speech organs; strokes mark aspiration, doubling marks tenseness.",
    "Silent ㅇ is the placeholder initial before vowels; text reads left to right, top to bottom within a block.",
    "Two number-word systems coexist: native Korean (하나 둘 셋) and Sino-Korean (일 이 삼)."],
  requirements=[
    "Show every letter with its name and English approximation.",
    "Demonstrate syllable-block assembly with worked examples.",
    "Give both numeral systems with the contexts each is used in.",
    "Name the three romanization systems and which is official.",
    "Include a demo that decomposes real syllables with Unicode arithmetic."],
  standards=[CIT_HUNMIN, CIT_UNICODE, CIT_RR],
  citations=[CIT_HUNMIN, CIT_UNICODE, CIT_RR],
  sig_lens=(
    "In the Signature Korean Method, each Hangul letter is a signature "
    "stroke: the consonant shapes are the pressure of the hand, the "
    "vowels the direction of the light, and each finished syllable block "
    "a sealed mark. Writing Hangul here is practiced as signing, one "
    "block at a time, until the hand seals syllables without thinking."))

E(key="phonology",
  name="Korean Pronunciation and Phonology",
  group="Foundations", ladder_rank=3, ladder_tier="foundations",
  description=(
    "Korean has 19 consonants and 10 vowels in its standard inventory "
    "(modern Seoul speech merges some vowels, leaving 7 to 8 distinct "
    "monophthongs: ㅏ ㅓ ㅗ ㅜ ㅡ ㅣ, with ㅐ and ㅔ merged for most "
    "speakers). Its most famous feature is the three-way laryngeal "
    "contrast among stops and affricates: plain (lenis) ㄱ ㄷ ㅂ ㅈ, tense "
    "(fortis) ㄲ ㄸ ㅃ ㅉ, and aspirated ㅋ ㅌ ㅍ ㅊ. These are not "
    "voiced-versus-voiceless like English b and p; the difference is made "
    "with vocal-fold tension and a puff of air. English approximations: "
    "plain ㄱ sounds like g between vowels and k at the start of a word; "
    "tense ㄲ is a hard, tight kk with no puff of air; aspirated ㅋ is k "
    "with a strong puff, like the k in 'kite'. Korean has no lexical tone "
    "and no word stress; instead, intonation rises and falls over phrases, "
    "and a rising intonation at the end of a sentence can turn a statement "
    "into a question. Final consonants (batchim) neutralize: 27 spellings "
    "collapse to 7 sounds (ㄱ, ㄴ, ㄷ, ㄹ, ㅁ, ㅂ, ㅇ), so 꽃 (kkot, flower) "
    "is pronounced with a final t-like sound even though it is spelled "
    "with ㅊ. Spoken examples: 물 (mul, water), 불 (bul, fire), 달 (dal, "
    "moon), 말 (mal, horse or speech), 산 (san, mountain), 강 (gang, "
    "river), 바람 (baram, wind), 사람 (saram, person), 하늘 (haneul, sky), "
    "바다 (bada, sea), 나무 (namu, tree), 친구 (chingu, friend)."),
  how_it_works=(
    "Sound changes (음운 변동, eumun byeondong) connect syllables. "
    "Nasalization: a batchim ㄱ, ㄷ, ㅂ before ㄴ or ㅁ becomes ㅇ, ㄴ, ㅁ, "
    "so 국립 (guknip, national) is pronounced 궁닙 (gungnip). "
    "Assimilation: the batchim ㅎ meets following consonants to make "
    "aspirates. Liaison: a final consonant moves to begin the next "
    "syllable when the next syllable starts with ㅇ, so 옷 안 (ot an, "
    "inside the clothes) sounds like 오단 (odan). Tensification: after a "
    "batchim, a following plain consonant hardens, so 학교 (hakgyo, "
    "school) is pronounced 학꾜 (hakkkyo). The practical rule for learners: "
    "pronounce what you hear in careful speech, because the spelling "
    "preserves the underlying form and the sound rules derive the surface "
    "pronunciation. Ten spoken anchor words with English approximations: "
    "가다 (gada, to go - ga-da), 오다 (oda, to come - o-da), 먹다 (meokda, "
    "to eat - mawg-da), 보다 (boda, to see - bo-da), 좋다 (jota, good - "
    "jo-ta), 나쁘다 (nappeuda, bad - na-ppeu-da), 크다 (keuda, big - keu-"
    "da), 작다 (jakda, small - jag-da), 빠르다 (ppareuda, fast - ppa-reu-"
    "da), 느리다 (neurida, slow - neu-ri-da)."),
  key_points=[
    "Three-way stop contrast: plain ㄱ, tense ㄲ, aspirated ㅋ - tension and air, not voicing.",
    "No lexical tone and no word stress; phrase intonation carries questions and emphasis.",
    "27 batchim spellings neutralize to 7 final sounds (ㄱ ㄴ ㄷ ㄹ ㅁ ㅂ ㅇ).",
    "Regular sound changes: nasalization, assimilation, liaison, tensification.",
    "10+ spoken anchor words with English approximations for drilling the contrasts."],
  requirements=[
    "List the full consonant and vowel inventory with English approximations.",
    "Explain the three-way contrast with minimal triplets.",
    "State the batchim neutralization rule with the 7 surviving sounds.",
    "Give 10 or more spoken example words with translations.",
    "Describe stress and intonation rules for sentence melody."],
  standards=[CIT_SOHN, CIT_YALE, CIT_NIKL],
  citations=[CIT_SOHN, CIT_YALE, CIT_NIKL],
  sig_lens=(
    "In the Signature Korean Method, pronunciation is tuning the "
    "instrument: plain sounds are the open string, tense sounds the "
    "fretted string, aspirated sounds the plucked string. The drill is "
    "simple - hear the triplet, feel the air on the hand, sign the "
    "syllable - until the ear certifies what the mouth produces."))

E(key="nouns1",
  name="Core Korean Nouns I: People, Places, Things",
  group="Foundations", ladder_rank=4, ladder_tier="foundations",
  description=(
    "Twenty-five essential Korean nouns with an example sentence each. "
    "Korean nouns do not change for number or gender; context and counters "
    "do that work. 1. 사람 (saram) person: 사람이 왔어요 (sarami wasseoyo, "
    "a person came). 2. 집 (jip) house: 집이 커요 (jibi keoyo, the house "
    "is big). 3. 물 (mul) water: 물을 마셔요 (mureul masyeoyo, drink "
    "water). 4. 밥 (bap) rice, meal: 밥을 먹어요 (babeul meogeoyo, eat a "
    "meal). 5. 학교 (hakgyo) school: 학교에 가요 (hakgyoe gayo, go to "
    "school). 6. 선생님 (seonsaengnim) teacher: 선생님이 좋아요 "
    "(seonsaengnimi joayo, the teacher is nice). 7. 친구 (chingu) friend: "
    "친구를 만나요 (chingureul mannayo, meet a friend). 8. 가족 (gajok) "
    "family: 가족이 행복해요 (gajogi haengbokhaeyo, the family is happy). "
    "9. 시간 (sigan) time: 시간이 없어요 (sigani eopseoyo, there is no "
    "time). 10. 돈 (don) money: 돈이 필요해요 (doni piryohaeyo, money is "
    "needed). 11. 음식 (eumsik) food: 음식이 맛있어요 (eumsigi masisseoyo, "
    "the food is delicious). 12. 차 (cha) tea, car: 차를 마셔요 (chareul "
    "masyeoyo, drink tea). 13. 책 (chaek) book: 책을 읽어요 (chaegeul "
    "ilgeoyo, read a book). 14. 컴퓨터 (keompyuteo) computer: 컴퓨터를 "
    "켜요 (keompyuteoreul kyeoyo, turn on the computer). 15. 전화 "
    "(jeonhwa) phone: 전화를 받아요 (jeonhwareul badayo, answer the "
    "phone). 16. 나라 (nara) country: 나라가 아름다워요 (naraga "
    "areumdawoyo, the country is beautiful). 17. 도시 (dosi) city: 도시가 "
    "커요 (dosiga keoyo, the city is big). 18. 길 (gil) road: 길이 길어요 "
    "(giri gireoyo, the road is long). 19. 하늘 (haneul) sky: 하늘이 "
    "파래요 (haneuri paraeyo, the sky is blue). 20. 바다 (bada) sea: 바다가 "
    "보여요 (badaga boyeoyo, the sea is visible). 21. 산 (san) mountain: "
    "산에 가요 (sane gayo, go to the mountain). 22. 나무 (namu) tree: 나무가 "
    "많아요 (namuga manayo, there are many trees). 23. 꽃 (kkot) flower: "
    "꽃이 예뻐요 (kkochi yeppeoyo, the flower is pretty). 24. 개 (gae) dog: "
    "개가 짖어요 (gaega jijeoyo, the dog barks). 25. 고양이 (goyangi) cat: "
    "고양이가 자요 (goyangiga jayo, the cat sleeps)."),
  how_it_works=(
    "A noun becomes a sentence subject by adding 이 after a consonant "
    "ending or 가 after a vowel ending: 집 + 이 = 집이, 고양이 + 가 = "
    "고양이가. It becomes an object with 을 after a consonant or 를 after "
    "a vowel: 밥 + 을 = 밥을, 차 + 를 = 차를. Plurality is usually left "
    "unmarked - 사람 can mean person or people - and 들 (deul) is added "
    "only when plurality needs emphasis: 사람들 (saramdeul, people). "
    "Counting nouns requires counters between the number and the noun: "
    "책 세 권 (chaek se gwon, three books), 사람 두 명 (saram du myeong, "
    "two people), 개 한 마리 (gae han mari, one dog). The topic particle "
    "은/는 reframes the noun as what the sentence is about: 저는 학생이에요 "
    "(jeoneun haksaengieyo, as for me, I am a student)."),
  key_points=[
    "Nouns are invariant: no gender, no plural inflection, no articles.",
    "이/가 marks subjects, 을/를 marks objects, 은/는 marks topics.",
    "들 adds explicit plurality only when it matters.",
    "Counters sit between number and noun: 세 권, 두 명, 한 마리.",
    "25 nouns each paired with a translated example sentence."],
  requirements=[
    "25 essential nouns covering person, place, and thing.",
    "Each noun with Hangul, romanization, English, and one example sentence.",
    "Explain subject, object, and topic particles with the consonant/vowel rule.",
    "Explain counters with three worked examples.",
    "All sentences translated into English."],
  standards=[CIT_NIKL, CIT_SOHN, CIT_TOPIK],
  citations=[CIT_NIKL, CIT_SOHN, CIT_TOPIK],
  sig_lens=(
    "In the Signature Korean Method, nouns are the named seals of the "
    "world: person, place, thing, each given its mark. The drill seals "
    "one noun at a time - say the block, mark its role with the particle, "
    "speak the sentence - until naming becomes signing."))

E(key="verbs1",
  name="Core Korean Verbs I: Essential Actions",
  group="Foundations", ladder_rank=4, ladder_tier="foundations",
  description=(
    "Twenty-five essential Korean verbs in dictionary form (ending in "
    "다, da) with an example sentence each in polite present tense. 1. "
    "가다 (gada) to go: 학교에 가요 (hakgyoe gayo, go to school). 2. 오다 "
    "(oda) to come: 집에 와요 (jibe wayo, come home). 3. 먹다 (meokda) to "
    "eat: 밥을 먹어요 (babeul meogeoyo, eat a meal). 4. 마시다 (masida) to "
    "drink: 물을 마셔요 (mureul masyeoyo, drink water). 5. 보다 (boda) to "
    "see, watch: 영화를 봐요 (yeonghwareul bwayo, watch a movie). 6. 듣다 "
    "(deutda) to listen: 음악을 들어요 (eumageul deureoyo, listen to "
    "music). 7. 말하다 (malhada) to speak: 한국어를 말해요 (hangugeoreul "
    "malhaeyo, speak Korean). 8. 읽다 (ilkda) to read: 책을 읽어요 "
    "(chaegeul ilgeoyo, read a book). 9. 쓰다 (sseuda) to write, use: "
    "편지를 써요 (pyeonjireul sseoyo, write a letter). 10. 배우다 (baeuda) "
    "to learn: 한국어를 배워요 (hangugeoreul baewoyo, learn Korean). 11. "
    "가르치다 (gareuchida) to teach: 영어를 가르쳐요 (yeongeoreul "
    "gareuchyeoyo, teach English). 12. 일하다 (ilhada) to work: 회사에서 "
    "일해요 (hoesaeseo ilhaeyo, work at a company). 13. 공부하다 "
    "(gongbuhada) to study: 도서관에서 공부해요 (doseogwaneseo "
    "gongbuhaeyo, study at the library). 14. 자다 (jada) to sleep: 일찍 "
    "자요 (iljjik jayo, sleep early). 15. 일어나다 (ireonada) to wake up, "
    "get up: 아침에 일어나요 (achime ireonayo, wake up in the morning). "
    "16. 앉다 (anjda) to sit: 의자에 앉아요 (uijae anjayo, sit on a "
    "chair). 17. 서다 (seoda) to stand: 문 앞에 서요 (mun ape seoyo, "
    "stand in front of the door). 18. 걷다 (geotda) to walk: 공원에서 "
    "걸어요 (gongwoneseo georeoyo, walk in the park). 19. 뛰다 (ttwida) to "
    "run: 빨리 뛰어요 (ppalli ttwieoyo, run fast). 20. 사다 (sada) to buy: "
    "빵을 사요 (ppangeul sayo, buy bread). 21. 팔다 (palda) to sell: "
    "과일을 팔아요 (gwaireul parayo, sell fruit). 22. 주다 (juda) to give: "
    "선물을 줘요 (seonmureul jwoyo, give a gift). 23. 받다 (batda) to "
    "receive: 편지를 받아요 (pyeonjireul badayo, receive a letter). 24. "
    "만들다 (mandeulda) to make: 음식을 만들어요 (eumsigeul mandeureoyo, "
    "make food). 25. 돕다 (dopda) to help: 친구를 도와요 (chingureul "
    "dowayo, help a friend)."),
  how_it_works=(
    "The dictionary form ends in 다; remove 다 to get the stem, then add "
    "endings. For the informal-polite present (해요체), add 아요 after "
    "stems whose last vowel is ㅏ or ㅗ, and 어요 after all other vowels: "
    "가 + 아요 = 가요, 먹 + 어요 = 먹어요, 보 + 아요 = 봐요 (the vowels "
    "contract). 하다 verbs simply become 해요: 일하다 -> 일해요, 공부하다 "
    "-> 공부해요. Irregular verbs shift their stems: 듣다 -> 들어요 (the "
    "ㄷ becomes ㄹ before a vowel), 돕다 -> 도와요 (ㅂ becomes 우), 만들다 "
    "-> 만들어요 (ㄹ drops before ㄴ/ㅅ only, stays here). The pattern to "
    "memorize is small: stem + 아/어 + 요 covers most daily speech, and "
    "every verb in this record follows it or one of the three common "
    "irregular shifts shown above."),
  key_points=[
    "Dictionary form ends in 다; the stem is what remains after removing 다.",
    "해요체 present: 아요 after ㅏ/ㅗ stems, 어요 after other vowels, plus 요.",
    "하다 verbs collapse to 해요; common irregulars: 듣다->들어요, 돕다->도와요.",
    "25 verbs each with a translated polite-present example sentence.",
    "Verb + object particle 을/를 frames the basic transitive sentence."],
  requirements=[
    "25 essential verbs with Hangul, romanization, and English gloss.",
    "Each verb with one translated example sentence in 해요체 present.",
    "Explain the 아/어/여요 conjugation rule with worked contractions.",
    "Show the three most common irregular shifts with examples.",
    "All sentences translated into English."],
  standards=[CIT_SOHN, CIT_NIKL, CIT_TOPIK],
  citations=[CIT_SOHN, CIT_NIKL, CIT_TOPIK],
  sig_lens=(
    "In the Signature Korean Method, verbs are the strokes of action: "
    "the stem is the hand, the ending the seal of when and how politely. "
    "The drill moves the same verb through its endings - 가요, 갔어요, "
    "갈 거예요 - until the hand signs time itself."))

E(key="adjectives",
  name="Korean Adjectives and Adverbs",
  group="Foundations", ladder_rank=5, ladder_tier="foundations",
  description=(
    "Twenty-five Korean adjectives (descriptive verbs) and fifteen adverbs, "
    "each with an example sentence. Korean adjectives conjugate like "
    "verbs, so 크다 (keuda, to be big) becomes 커요 (keoyo, is big). 1. "
    "크다 big: 집이 커요 (jibi keoyo, the house is big). 2. 작다 (jakda) "
    "small: 방이 작아요 (bangi jagayo, the room is small). 3. 좋다 (jota) "
    "good: 날씨가 좋아요 (nalssiga joayo, the weather is good). 4. 나쁘다 "
    "(nappeuda) bad: 기분이 나빠요 (gibuni nappayo, the mood is bad). 5. "
    "많다 (manta) many: 사람이 많아요 (sarami manayo, there are many "
    "people). 6. 적다 (jeokda) few: 시간이 적어요 (sigani jeogeoyo, time "
    "is short). 7. 빠르다 (ppareuda) fast: 차가 빨라요 (chaga ppallayo, "
    "the car is fast). 8. 느리다 (neurida) slow: 걸음이 느려요 (georeumi "
    "neuryeoyo, the walk is slow). 9. 높다 (nopda) high: 산이 높아요 "
    "(sani nopayo, the mountain is high). 10. 낮다 (natda) low: 목소리가 "
    "낮아요 (moksoriga najayo, the voice is low). 11. 길다 (gilda) long: "
    "강이 길어요 (gangi gireoyo, the river is long). 12. 짧다 (jjalda) "
    "short: 머리가 짧아요 (meoriga jjalbayo, the hair is short). 13. 넓다 "
    "(neolda) wide: 방이 넓어요 (bangi neolbeoyo, the room is wide). 14. "
    "좁다 (jopda) narrow: 길이 좁아요 (giri jobayo, the road is narrow). "
    "15. 무겁다 (mugeopda) heavy: 가방이 무거워요 (gabangi mugeowoyo, the "
    "bag is heavy). 16. 가볍다 (gabyeopda) light: 마음이 가벼워요 (ma-eumi "
    "gabyeowoyo, the heart feels light). 17. 뜨겁다 (tteugeopda) hot: 국이 "
    "뜨거워요 (gugi tteugeowoyo, the soup is hot). 18. 차갑다 (chagapda) "
    "cold: 물이 차가워요 (muri chagawoyo, the water is cold). 19. 맛있다 "
    "(masitda) delicious: 김치가 맛있어요 (gimchiga masisseoyo, the kimchi "
    "is delicious). 20. 재미있다 (jaemiitda) fun, interesting: 영화가 "
    "재미있어요 (yeonghwaga jaemiisseoyo, the movie is fun). 21. 어렵다 "
    "(eoryeopda) difficult: 한국어가 어려워요 (hangugeo-ga eoryeowoyo, "
    "Korean is difficult). 22. 쉽다 (swipda) easy: 문제가 쉬워요 (munjega "
    "swiwoyo, the problem is easy). 23. 바쁘다 (bappeuda) busy: 오늘 "
    "바빠요 (oneul bappayo, I am busy today). 24. 예쁘다 (yeppeuda) "
    "pretty: 꽃이 예뻐요 (kkochi yeppeoyo, the flower is pretty). 25. "
    "행복하다 (haengbokhada) happy: 가족이 행복해요 (gajogi haengbokhaeyo, "
    "the family is happy). Adverbs: 아주 (aju) very - 아주 좋아요 (aju "
    "joayo, very good); 매우 (maeu) very; 정말 (jeongmal) really - 정말 "
    "맛있어요 (jeongmal masisseoyo, really delicious); 너무 (neomu) too, "
    "so - 너무 비싸요 (neomu bissayo, too expensive); 잘 (jal) well - 잘 "
    "먹어요 (jal meogeoyo, eat well); 빨리 (ppalli) quickly - 빨리 와요 "
    "(ppalli wayo, come quickly); 천천히 (cheoncheonhi) slowly - 천천히 "
    "말해요 (cheoncheonhi malhaeyo, speak slowly); 항상 (hangsang) always; "
    "자주 (jaju) often - 자주 만나요 (jaju mannayo, meet often); 가끔 "
    "(gakkeum) sometimes; 절대 (jeoldae) never - 절대 안 해요 (jeoldae an "
    "haeyo, never do it); 벌써 (beolsseo) already; 아직 (ajik) yet - 아직 "
    "안 왔어요 (ajik an wasseoyo, has not come yet); 같이 (gachi) together "
    "- 같이 가요 (gachi gayo, go together); 혼자 (honja) alone - 혼자 "
    "먹어요 (honja meogeoyo, eat alone)."),
  how_it_works=(
    "Adjectives (형용사, hyeongyongsa) are descriptive verbs: they take "
    "the same 아/어/여요 endings as action verbs, and before a noun they "
    "take the modifier form 은/ㄴ: 큰 집 (keun jip, big house), 작은 방 "
    "(jageun bang, small room), 예쁜 꽃 (yeppeun kkot, pretty flower). "
    "Adverbs (부사, busa) never conjugate and sit before the word they "
    "modify. Many adverbs are built from adjectives: 빠르다 -> 빨리 "
    "(quickly), 천천히 from 천천하다, and some adjectives take 이/히: "
    "조용하다 -> 조용히 (quietly). Position rule: the adverb comes right "
    "before the verb or adjective it modifies, and negation 안 sits "
    "between them: 아주 빨리 가요 (very quickly go), 안 빨리 가요 would "
    "be wrong - say 빨리 안 가요 for 'do not go quickly'."),
  key_points=[
    "Korean adjectives conjugate like verbs: 크다 -> 커요; modifier form 큰/작은/예쁜 before nouns.",
    "No agreement: adjectives never change for number or gender.",
    "Adverbs never conjugate and precede the word they modify.",
    "이/히 and 리 forms derive adverbs from adjectives: 조용히, 빨리.",
    "25 adjectives + 15 adverbs, each with a translated example sentence."],
  requirements=[
    "25 adjectives with Hangul, romanization, English, and example sentences.",
    "15 adverbs with the same treatment.",
    "Explain adjective conjugation and the 은/ㄴ modifier form.",
    "Explain adverb position and the 이/히 derivation.",
    "All sentences translated into English."],
  standards=[CIT_SOHN, CIT_NIKL, CIT_TOPIK],
  citations=[CIT_SOHN, CIT_NIKL, CIT_TOPIK],
  sig_lens=(
    "In the Signature Korean Method, adjectives are the colors of the "
    "signature and adverbs the pressure of the stroke: 아주, 정말, 빨리 "
    "press harder on the meaning. The drill pairs each quality with its "
    "pressure - 아주 커요, 정말 빨라요 - until description signs itself."))

E(key="pronouns",
  name="Korean Pronouns and Demonstratives",
  group="Foundations", ladder_rank=5, ladder_tier="foundations",
  description=(
    "Korean pronouns shift with politeness, and names plus titles are "
    "often used where English would use 'you'. Personal: 나 (na) I, "
    "informal - 나는 학생이에요 (naneun haksaengieyo, I am a student); 저 "
    "(jeo) I, humble polite - 저는 김민준이에요 (jeoneun Gim Minjunieyo, I "
    "am Kim Minjun); 너 (neo) you, informal - 너는 어디 가? (neoneun eodi "
    "ga, where are you going); 당신 (dangsin) you, formal but sparingly "
    "used - 당신을 믿어요 (dangsineul mideoyo, I trust you); 우리 (uri) "
    "we, also 'my/our' by extension - 우리 집 (uri jip, our house / my "
    "house); 그 (geu) he - 그는 선생님이에요 (geuneun seonsaengnimieyo, he "
    "is a teacher); 그녀 (geunyeo) she - 그녀는 의사예요 (geunyeoneun "
    "uisayeyo, she is a doctor); 그것 (geugeot) it - 그것이 문제예요 "
    "(geugeosi munjeyeyo, that is the problem). Possessive: 내 (nae) my - "
    "내 책 (nae chaek, my book); 제 (je) my, humble - 제 이름 (je ireum, "
    "my name); 네 (ne) your, informal - 네 가방 (ne gabang, your bag); 그 "
    "사람의 (geu saramui) his/her, formal; 우리 (uri) our. Demonstratives: "
    "이 (i) this near me - 이 책 (i chaek, this book); 그 (geu) that near "
    "you - 그 책 (geu chaek, that book); 저 (jeo) that over there - 저 책 "
    "(jeo chaek, that book over there); 여기 (yeogi) here - 여기 앉아요 "
    "(yeogi anjayo, sit here); 거기 (geogi) there - 거기 있어요 (geogi "
    "isseoyo, it is there); 저기 (jeogi) over there - 저기 봐요 (jeogi "
    "bwayo, look over there). Interrogatives: 누구 (nugu) who - 누구세요 "
    "(nuguseyo, who is it); 무엇/뭐 (mueot/mwo) what - 뭐 해요 (mwo haeyo, "
    "what are you doing); 어디 (eodi) where - 어디에 있어요 (eodie "
    "isseoyo, where is it); 언제 (eonje) when - 언제 와요 (eonje wayo, "
    "when are you coming); 왜 (wae) why - 왜 울어요 (wae ureoyo, why are "
    "you crying); 어떻게 (eotteoke) how - 어떻게 가요 (eotteoke gayo, how "
    "do you go); 얼마나 (eolmana) how much - 얼마예요 (eolmayeyo, how much "
    "is it); 몇 (myeot) how many - 몇 개예요 (myeot gaeyeyo, how many are "
    "there)."),
  how_it_works=(
    "Pronouns take particles exactly like nouns: 나는/나는, 너를/너를, "
    "그에게 (geuege, to him). The informal 나 contracts with particles: "
    "나 + 의 = 내 (my), 너 + 의 = 네 (your). The humble 저 gives 제 (my, "
    "humble) and the formal 저 (that over there) is a different word that "
    "happens to sound the same - context disambiguates. The three-way "
    "demonstrative system (이 near me, 그 near you, 저 away from both) "
    "extends to places (여기/거기/저기), directions (이쪽/그쪽/저쪽), and "
    "kinds (이렇게/그렇게/저렇게). Second person is socially loaded: to "
    "strangers use titles (선생님, 손님/sonnim, customer) or no pronoun at "
    "all; 당신 is reserved for spouses, writing, or confrontation. When in "
    "doubt, drop the pronoun - Korean is pro-drop, and the verb ending "
    "already tells who is speaking."),
  key_points=[
    "나/저 (I) and 너/당신 (you) shift with politeness; 우리 doubles as 'my' by extension.",
    "Possessives contract: 나의->내, 너의->네, 저의->제.",
    "Three-way demonstratives: 이 (near me), 그 (near you), 저 (away from both).",
    "Full interrogative set: 누구, 무엇/뭐, 어디, 언제, 왜, 어떻게, 얼마나, 몇.",
    "Korean is pro-drop: omit pronouns the verb ending already implies."],
  requirements=[
    "Full personal, possessive, demonstrative, and interrogative paradigms.",
    "Each form with Hangul, romanization, English, and an example sentence.",
    "Explain the 이/그/저 three-way system across things, places, and kinds.",
    "Explain the social rules for second-person address.",
    "All sentences translated into English."],
  standards=[CIT_SOHN, CIT_NIKL, CIT_TOPIK],
  citations=[CIT_SOHN, CIT_NIKL, CIT_TOPIK],
  sig_lens=(
    "In the Signature Korean Method, pronouns are the seals of "
    "relationship: 나 for the self among friends, 저 for the self bowed "
    "before elders, and silence for the stranger whose name is not yet "
    "earned. The drill practices the bow of 저 until humility signs "
    "itself."))

E(key="numbers",
  name="Korean Numbers, Dates, and Time",
  group="Foundations", ladder_rank=6, ladder_tier="foundations",
  description=(
    "Korean uses two number systems. Native Korean numbers (for counting "
    "things, age, and hours): 하나 (hana, 1), 둘 (dul, 2), 셋 (set, 3), "
    "넷 (net, 4), 다섯 (daseot, 5), 여섯 (yeoseot, 6), 일곱 (ilgop, 7), "
    "여덟 (yeodeol, 8), 아홉 (ahop, 9), 열 (yeol, 10), 열하나 "
    "(yeolhana, 11), 열둘 (yeoldul, 12), 스물 (seumul, 20), 서른 (seoreun, "
    "30), 마흔 (maheun, 40), 쉰 (swin, 50), 예순 (yesun, 60), 일흔 "
    "(ilheun, 70), 여든 (yeodeun, 80), 아흔 (aheun, 90). Before counters, "
    "1-4 shorten: 한 개 (han gae, one thing), 두 개 (du gae), 세 개 (se "
    "gae), 네 개 (ne gae). Sino-Korean numbers (for dates, money, "
    "minutes, phone numbers): 일 (il, 1), 이 (i, 2), 삼 (sam, 3), 사 (sa, "
    "4), 오 (o, 5), 육 (yuk, 6), 칠 (chil, 7), 팔 (pal, 8), 구 (gu, 9), 십 "
    "(sip, 10), 십일 (sibil, 11), 이십 (isip, 20), 삼십 (samsip, 30), 백 "
    "(baek, 100), 천 (cheon, 1000), 만 (man, 10000). Ordinals: 첫째 "
    "(cheotjjae, first, native), 둘째 (duljjae, second), or 제일 (jeil) / "
    "제 + sino-number + 째: 제삼 (jesam) is rare - use 세 번째 (se beonjjae, "
    "third time). Days of the week: 월요일 (woryoil, Monday), 화요일 "
    "(hwayoil, Tuesday), 수요일 (suyoil, Wednesday), 목요일 (mogyoil, "
    "Thursday), 금요일 (geumyoil, Friday), 토요일 (toyoil, Saturday), "
    "일요일 (iryoil, Sunday). Months: 일월 (irwol, January), 이월 (iwol), "
    "삼월 (samwol), 사월 (sawol), 오월 (owol), 유월 (yuwol, June - "
    "irregular), 칠월 (chirwol), 팔월 (parwol), 구월 (guwol), 시월 (siwol, "
    "October - irregular), 십일월 (sibilwol), 십이월 (sibiwol). Seasons: "
    "봄 (bom, spring), 여름 (yeoreum, summer), 가을 (ga-eul, autumn), 겨울 "
    "(gyeoul, winter). Clock time mixes both systems: hours are native, "
    "minutes are Sino-Korean. 세 시 (se si, 3 o'clock - native 세 + 시); "
    "세 시 십오 분 (se si sibo bun, 3:15). Dates: Sino-Korean month + "
    "Sino-Korean day + 일: 삼월 십오일 (samwol siboir, March 15th). "
    "Example sentences: 사과 세 개 주세요 (sagwa se gae juseyo, please "
    "give me three apples); 지금 세 시예요 (jigeum se siyeyo, it is 3 "
    "o'clock now); 오월 오일이에요 (owol oirieyo, it is May 5th); 일요일에 "
    "만나요 (iryoire mannayo, meet on Sunday); 스무 살이에요 (seumu "
    "sarieyo, I am twenty years old)."),
  how_it_works=(
    "Choose the system by context, not by size. Native Korean counts "
    "discrete things with counters (개, 명, 마리, 권, 살 for age) and "
    "tells the hour: 한 시 (han si, 1 o'clock), 두 시 (du si, 2 o'clock). "
    "Sino-Korean handles money (삼천 원, samcheon won, 3000 won), minutes "
    "(오 분, o bun, 5 minutes), dates, months, years, addresses, and phone "
    "numbers (공, gong, is used for zero in phone numbers). The two "
    "systems meet in clock time - native hour + Sino minute - and in age: "
    "스무 살 (seumu sal, 20 years old, native) for casual speech, 이십 세 "
    "(isip se, Sino) for formal documents. Ordinals usually attach 번째 "
    "(beonjjae, -th time) or 째 to the number: 첫 번째 (cheot beonjjae, "
    "the first). Years are Sino-Korean plus 년 (nyeon): 이천이십육 년 "
    "(icheonisipnyuk nyeon, the year 2026)."),
  key_points=[
    "Two systems: native (하나 둘 셋) for counting things, hours, age; Sino (일 이 삼) for dates, money, minutes.",
    "Numbers 1-100 in both systems, with the 1-4 counter shortenings 한/두/세/네.",
    "Ordinals with 첫째/둘째 and 번째/째; days 월요일-일요일; months 일월-십이월 with 유월/시월 irregulars.",
    "Clock time: native hour + Sino minute (세 시 십오 분); dates: Sino month + day + 일.",
    "Seasons 봄/여름/가을/겨울; each item paired with translated example sentences."],
  requirements=[
    "Numbers 1-100 in both native and Sino-Korean systems.",
    "Ordinals, days of the week, months, and seasons with romanization.",
    "Clock time, dates, and age with the mixed-system rule explained.",
    "Each section with translated example sentences.",
    "A demo that converts 1-100 in both systems and verifies known values."],
  standards=[CIT_NIKL, CIT_TOPIK, CIT_RR],
  citations=[CIT_NIKL, CIT_TOPIK, CIT_RR],
  sig_lens=(
    "In the Signature Korean Method, numbers are the measure-marks of "
    "the system: native numbers count what the hand can hold, Sino "
    "numbers count what the ledger must record. The drill counts to one "
    "hundred in both voices until the tongue carries two abacuses at "
    "once."))

E(key="greetings",
  name="Korean Greetings and Everyday Phrases",
  group="Foundations", ladder_rank=6, ladder_tier="foundations",
  description=(
    "Thirty greetings, farewells, and politeness phrases with usage "
    "notes. 1. 안녕하세요 (annyeonghaseyo) hello - the universal polite "
    "greeting, literally 'are you at peace'. 2. 안녕히 가세요 "
    "(annyeonghi gaseyo) goodbye to someone leaving - 'go in peace'. 3. "
    "안녕히 계세요 (annyeonghi gyeseyo) goodbye to someone staying - "
    "'stay in peace'. 4. 감사합니다 (gamsahamnida) thank you, formal. 5. "
    "고맙습니다 (gomapseumnida) thank you, warm formal. 6. 고마워요 "
    "(gomawoyo) thanks, informal polite. 7. 죄송합니다 (joesonghamnida) I "
    "am sorry, formal. 8. 미안해요 (mianhaeyo) sorry, informal polite. 9. "
    "처음 뵙겠습니다 (cheoeum boepgetsseumnida) nice to meet you, formal - "
    "used at first meetings. 10. 잘 부탁드립니다 (jal butakdeurimnida) I "
    "ask for your kind favor - said when beginning a relationship. 11. "
    "식사하셨어요 (siksahasyeosseoyo) have you eaten - the classic caring "
    "greeting. 12. 잘 지내셨어요 (jal jinaesyeosseoyo) have you been well. "
    "13. 오랜만이에요 (oraenmanieyo) long time no see. 14. 반갑습니다 "
    "(bangapseumnida) glad to meet you. 15. 잘 가요 (jal gayo) bye, to a "
    "friend leaving. 16. 좋은 아침이에요 (joheun achimieyo) good morning - "
    "less common than 안녕하세요. 17. 좋은 하루 보내세요 (joheun haru "
    "bonaeseyo) have a good day. 18. 안녕히 주무세요 (annyeonghi jumuseyo) "
    "good night, to someone staying. 19. 잘 자요 (jal jayo) good night, "
    "informal. 20. 수고하셨습니다 (sugohasyeotsseumnida) thank you for "
    "your hard work - said to anyone finishing work. 21. 천만에요 "
    "(cheonmaneyo) you are welcome. 22. 괜찮아요 (gwaenchanayo) it is okay, "
    "no thanks needed. 23. 실례합니다 (sillyehamnida) excuse me - getting "
    "attention or apologizing for intrusion. 24. 여보세요 (yeoboseyo) "
    "hello, on the phone. 25. 잠깐만요 (jamkkanmanyo) just a moment. 26. "
    "알겠습니다 (algesseumnida) understood, formal. 27. 축하합니다 "
    "(chukahamnida) congratulations. 28. 생일 축하해요 (saengil "
    "chukahaeyo) happy birthday. 29. 새해 복 많이 받으세요 (saehae bok "
    "manhi badeuseyo) Happy New Year - 'receive many blessings'. 30. 잘 "
    "먹겠습니다 (jal meokgetsseumnida) said before eating - 'I will eat "
    "well'; 잘 먹었습니다 (jal meogeotsseumnida) after eating - 'I ate "
    "well'. Extra table manners: 건배 (geonbae) cheers; 어서 오세요 "
    "(eoseo oseyo) welcome, said by shopkeepers; 또 만나요 (tto mannayo) "
    "see you again; 조심히 가세요 (josimhi gaseyo) get home safely; "
    "힘내세요 (himnaeseyo) cheer up, hang in there."),
  how_it_works=(
    "Korean greetings encode direction and relationship. The two "
    "goodbyes split on who moves: the leaver hears 안녕히 가세요 (go in "
    "peace), the stayer hears 안녕히 계세요 (stay in peace) - mixing them "
    "up is the classic beginner error. Politeness rides the verb ending: "
    "감사합니다 (formal) versus 고마워요 (informal polite) versus 고마워 "
    "(plain, to close friends). Bowing accompanies greetings; the depth "
    "of the bow tracks the formality of the words. Phone greetings use "
    "여보세요 on answering and end with 끊겠습니다 (kkeunkgetsseumnida, I "
    "will hang up, formal) or 먼저 끊을게요 (meonjeo kkeuneulgeyo, I will "
    "hang up first, informal). The rule of thumb: default to the 요/ㅂ니다 "
    "forms with anyone you do not know well, and let the other person "
    "invite you down to informal speech."),
  key_points=[
    "안녕하세요 is the universal polite hello; goodbyes split by who leaves (가세요) and who stays (계세요).",
    "30 greetings and politeness phrases, each with romanization, English, and usage notes.",
    "Formality rides verb endings: 합니다 > 해요 > 해 across every phrase.",
    "식사하셨어요 (have you eaten) functions as a caring greeting, not a literal question.",
    "잘 먹겠습니다 / 잘 먹었습니다 frame every shared meal."],
  requirements=[
    "30 greetings, farewells, and politeness phrases with usage notes.",
    "Hangul, romanization, and English on every phrase.",
    "Explain the 가세요/계세요 goodbye split and the ending-based formality scale.",
    "Cover phone, meal, and celebration phrases.",
    "A demo that matches phrases to formality levels and social situations."],
  standards=[CIT_NIKL, CIT_TOPIK, CIT_SOHN],
  citations=[CIT_NIKL, CIT_TOPIK, CIT_SOHN],
  sig_lens=(
    "In the Signature Korean Method, greetings are the opening seals of "
    "every encounter: 안녕하세요 signs peace, 감사합니다 signs gratitude, "
    "수고하셨습니다 signs honor for work done. The drill opens and closes "
    "thirty encounters a day until the seals come unbidden."))

E(key="grammar",
  name="Korean Grammar Essentials",
  group="Foundations", ladder_rank=7, ladder_tier="foundations",
  description=(
    "The core grammar of Korean in seven rules, each with translated "
    "examples. 1. Word order is subject-object-verb: 저는 사과를 먹어요 "
    "(jeoneun sagwareul meogeoyo, I eat an apple) - the verb always comes "
    "last. 2. Particles mark roles: 이/가 subject (고양이가 자요, goyangiga "
    "jayo, the cat sleeps), 을/를 object (책을 읽어요, chaegeul ilgeoyo, "
    "read a book), 은/는 topic (저는 학생이에요, jeoneun haksaengieyo, I "
    "am a student), 에 to/at (학교에 가요, hakgyoe gayo, go to school), "
    "에서 at/from (집에서 먹어요, jibeseo meogeoyo, eat at home), 에게/한테 "
    "to a person (친구에게 줘요, chinguege jwoyo, give to a friend), 와/과 "
    "and/with (친구와 가요, chinguwa gayo, go with a friend), 의 possessive "
    "(나의 책 -> 내 책, nae chaek, my book), 도 also/too (저도 가요, jeodo "
    "gayo, I go too). 3. There are no articles and no grammatical gender: "
    "그 사람 (geu saram) is 'the/that person' regardless of sex. 4. Number "
    "is marked with counters, not noun inflection: 사과 세 개 (sagwa se "
    "gae, three apples). 5. Negation: 안 before the verb (안 먹어요, an "
    "meogeoyo, do not eat) or 지 않다 after the stem (먹지 않아요, meokji "
    "anayo, do not eat); inability uses 못 (못 가요, mot gayo, cannot go). "
    "6. Questions: add a question word or raise intonation - 어디에 있어요 "
    "(eodie isseoyo, where is it), and yes/no questions reuse the "
    "statement form with rising tone: 가요? (gayo, are you going). 7. "
    "Politeness levels change every ending: 갑니다 (gamnida, formal), "
    "가요 (gayo, informal polite), 가 (ga, plain). Honorifics raise the "
    "subject: 할머니께서 주무세요 (halmeonikkeseo jumuseyo, grandmother "
    "sleeps - honorific)."),
  how_it_works=(
    "Build a sentence inside-out: pick the verb last, then hang the "
    "arguments before it with their particles. 저는 (topic) 친구에게 "
    "(to friend) 선물을 (object) 줬어요 (gave): 'I gave a gift to a "
    "friend.' Tense lives in the verb ending: 먹어요 (present), 먹었어요 "
    "(past - 았/었), 먹을 거예요 (future - ㄹ 것). Modifiers precede what "
    "they modify: 예쁜 꽃 (pretty flower), 빨리 가는 차 (fast-going car). "
    "Clauses chain with connectors: -고 (and then), -지만 (but), -서 "
    "(because/and so), -면 (if): 밥을 먹고 학교에 가요 (babeul meokgo "
    "hakgyoe gayo, eat and then go to school). Relative clauses precede "
    "the noun with the modifier ending: 읽은 책 (ilgeun chaek, the book "
    "that was read), 먹을 음식 (meogeul eumsik, the food to eat). The "
    "whole system is agglutinative: meaning stacks onto the stem in a "
    "fixed slot order - stem + honorific + tense + politeness + sentence "
    "type."),
  key_points=[
    "SOV order with the verb always last; particles mark subject, object, topic, and oblique roles.",
    "No articles, no grammatical gender; number via counters.",
    "Negation with 안/지 않다; inability with 못.",
    "Questions via question words or rising intonation; politeness levels reshape every ending.",
    "Agglutination: stem + honorific + tense + politeness + sentence-type in fixed slots."],
  requirements=[
    "Cover word order, particles, articles, gender, number, negation, and questions.",
    "Every rule with translated example sentences carrying Hangul and romanization.",
    "Show the particle consonant/vowel alternations (이/가, 을/를, 은/는).",
    "Show the three speech levels on the same verb.",
    "A demo that selects correct particles for sample nouns."],
  standards=[CIT_SOHN, CIT_LEE, CIT_NIKL],
  citations=[CIT_SOHN, CIT_LEE, CIT_NIKL],
  sig_lens=(
    "In the Signature Korean Method, grammar is the covenant order: the "
    "verb sealed last, every argument marked with its seal of role, "
    "politeness measured to the listener. The drill builds sentences "
    "inside-out until the order signs itself without thought."))

# ============================ COMPOUNDED ============================

E(key="home",
  name="Home and Family Sentences",
  group="Compounded", ladder_rank=7, ladder_tier="compounded",
  description=(
    "Twenty sentences about house, rooms, furniture, and family members. "
    "1. 우리 집은 아파트예요 (uri jibeun apateuyeyo, our house is an "
    "apartment). 2. 거실이 넓어요 (geosiri neolbeoyo, the living room is "
    "spacious). 3. 부엌에서 밥을 해요 (bueokeseo babeul haeyo, cook rice "
    "in the kitchen). 4. 침실에 침대가 있어요 (chimsire chimdaega isseoyo, "
    "there is a bed in the bedroom). 5. 화장실이 어디예요 (hwajangsiri "
    "eodiyeyo, where is the bathroom). 6. 소파에 앉아요 (sopae anjayo, sit "
    "on the sofa). 7. 책상 위에 책이 있어요 (chaeksang wie chaegi isseoyo, "
    "there is a book on the desk). 8. 창문을 열어요 (changmuneul yeoreoyo, "
    "open the window). 9. 불을 꺼요 (bureul kkeoyo, turn off the light). "
    "10. 아버지는 회사에 가세요 (abeojineun hoesae gaseyo, father goes to "
    "the company). 11. 어머니는 요리를 하세요 (eomeonineun yorireul "
    "haseyo, mother cooks). 12. 형이 대학교에 다녀요 (hyeongi "
    "daehakgyoe danyeoyo, my older brother attends university - male "
    "speaker). 13. 언니가 선물을 줬어요 (eonniga seonmureul jwosseoyo, my "
    "older sister gave a gift - female speaker). 14. 남동생이 축구를 해요 "
    "(namdongsaengi chukgureul haeyo, my younger brother plays soccer). "
    "15. 여동생이 피아노를 쳐요 (yeodongsaengi pianoreul chyeoyo, my "
    "younger sister plays the piano). 16. 할아버지가 신문을 읽으세요 "
    "(harabeojiga sinmuneul ilgeuseyo, grandfather reads the newspaper). "
    "17. 할머니가 이야기를 해 주세요 (halmeoniga iyagireul hae juseyo, "
    "grandmother tells a story). 18. 가족이 모두 모였어요 (gajogi modu "
    "moyeosseoyo, the whole family gathered). 19. 강아지가 마당에서 놀아요 "
    "(gangajiga madangeseo norayo, the puppy plays in the yard). 20. 오늘 "
    "밤에 손님이 와요 (oneul bame sonnimi wayo, a guest is coming "
    "tonight). Family terms shift with the speaker: a man calls his older "
    "brother 형 (hyeong) and older sister 누나 (nuna); a woman calls them "
    "오빠 (oppa) and 언니 (eonni); younger siblings are 동생 (dongsaeng) "
    "for everyone."),
  how_it_works=(
    "Home sentences run on location particles: 에 for static location "
    "(침실에 있어요, is in the bedroom) and 에서 for the place of action "
    "(부엌에서 해요, cook in the kitchen). Family sentences run on "
    "honorifics: parents and grandparents take 주무시다 (jumusida, to "
    "sleep - honorific) instead of 자다, 드시다 (deusida, to eat - "
    "honorific) instead of 먹다, and 계시다 (gyesida, to be - honorific) "
    "instead of 있다. The subject particle upgrades too: 아버지께서 "
    "(abeojikkeseo) instead of 아버지가. Kinship terms are relative, not "
    "absolute - 형/오빠 depends on who is speaking, which is why Korean "
    "learns family as a network of relationships rather than a list of "
    "labels."),
  key_points=[
    "에 marks static location; 에서 marks the place where an action happens.",
    "Family elders take honorific verbs: 주무시다, 드시다, 계시다.",
    "Kinship terms are speaker-relative: 형/오빠, 누나/언니, 동생.",
    "20 sentences covering rooms, furniture, and every family member.",
    "Every sentence with Hangul, romanization, and English."],
  requirements=[
    "20 sentences: house, rooms, furniture, family members.",
    "Explain 에 vs 에서 with examples from the sentences.",
    "Explain honorific verbs for elders with three examples.",
    "Explain speaker-relative sibling terms.",
    "All sentences translated into English."],
  standards=[CIT_NIKL, CIT_SOHN, CIT_TOPIK],
  citations=[CIT_NIKL, CIT_SOHN, CIT_TOPIK],
  sig_lens=(
    "In the Signature Korean Method, the home is the first archive and "
    "the family its first circle of seals: each room a chamber, each "
    "elder a seal raised higher. The drill walks the house naming every "
    "room and bows to every elder in the grammar until home signs "
    "itself."))

E(key="food",
  name="Food and Cooking Sentences",
  group="Compounded", ladder_rank=7, ladder_tier="compounded",
  description=(
    "Twenty sentences about meals, ingredients, cooking actions, and "
    "restaurants. 1. 아침을 먹었어요 (achimeul meogeosseoyo, I ate "
    "breakfast). 2. 점심은 비빔밥이에요 (jeomsimeun bibimbabieyo, lunch is "
    "bibimbap). 3. 저녁에 김치찌개를 끓여요 (jeonyeoge gimchijjigaereul "
    "kkeuryeoyo, boil kimchi stew for dinner). 4. 밥을 지어요 (babeul "
    "jieoyo, cook rice). 5. 물을 끓여요 (mureul kkeuryeoyo, boil water). "
    "6. 야채를 썰어요 (yachaereul sseoreoyo, slice the vegetables). 7. "
    "고기를 구워요 (gogireul guwoyo, grill the meat). 8. 계란을 삶아요 "
    "(gyeraneul salmayo, boil the eggs). 9. 간을 봐요 (ganeul bwayo, taste "
    "for seasoning - literally 'see the liver/saltiness'). 10. 소금을 조금 "
    "넣어요 (sogeumeul jogeum neoheoyo, add a little salt). 11. 설탕 대신 "
    "꿀을 써요 (seoltang daesin kkureul sseoyo, use honey instead of "
    "sugar). 12. 음식이 정말 맛있어요 (eumsigi jeongmal masisseoyo, the "
    "food is really delicious). 13. 매운 음식을 잘 먹어요 (maeun eumsigeul "
    "jal meogeoyo, I eat spicy food well). 14. 식당에서 불고기를 시켰어요 "
    "(sikdangeseo bulgogireul sikyeosseoyo, ordered bulgogi at the "
    "restaurant). 15. 메뉴를 보여 주세요 (menyureul boyeo juseyo, please "
    "show me the menu). 16. 이거 얼마예요 (igeo eolmayeyo, how much is "
    "this). 17. 포장해 주세요 (pojanghae juseyo, please pack it to go). "
    "18. 물 좀 주세요 (mul jom juseyo, please give me some water). 19. "
    "계산서 주세요 (gyesanseo juseyo, the bill please). 20. 잘 먹었습니다 "
    "(jal meogeotsseumnida, I ate well - said after the meal). Staple "
    "ingredients: 쌀 (ssal, rice grain), 김치 (gimchi, kimchi), 된장 "
    "(doenjang, soybean paste), 고추장 (gochujang, red pepper paste), 간장 "
    "(ganjang, soy sauce), 마늘 (maneul, garlic), 파 (pa, green onion)."),
  how_it_works=(
    "Cooking verbs are precise: 끓이다 (kkeurida, to boil a liquid), 삶다 "
    "(salmda, to boil a solid in liquid), 찌다 (jjida, to steam), 굽다 "
    "(gupda, to grill/bake), 볶다 (bokda, to stir-fry), 튀기다 (twigida, "
    "to deep-fry), 썰다 (sseolda, to slice), 다지다 (dajida, to mince). "
    "Restaurant speech is a fixed ritual: order with ~을/를 주세요 or "
    "~주세요, ask prices with 얼마예요, request the bill with 계산서 "
    "주세요, and close with 잘 먹었습니다. The counter for servings is "
    "인분 (inbun): 삼 인분 주세요 (sam inbun juseyo, three servings "
    "please). Spice level is negotiated: 맵게 해 주세요 (maepge hae "
    "juseyo, make it spicy) or 안 맵게 해 주세요 (an maepge hae juseyo, "
    "make it not spicy)."),
  key_points=[
    "Distinct verbs for each cooking method: 끓이다, 삶다, 찌다, 굽다, 볶다, 튀기다.",
    "Restaurant ritual: order, price, pack, water, bill, closing thanks.",
    "Servings counted with 인분; spice negotiated with 맵게/안 맵게.",
    "20 sentences covering meals, ingredients, cooking, and restaurants.",
    "Seven staple ingredients with glosses."],
  requirements=[
    "20 sentences: meals, ingredients, cooking actions, restaurant.",
    "List the core cooking verbs with English glosses.",
    "Teach the restaurant ordering ritual in order.",
    "Give the staple ingredient vocabulary.",
    "All sentences translated into English."],
  standards=[CIT_NIKL, CIT_TOPIK, CIT_SOHN],
  citations=[CIT_NIKL, CIT_TOPIK, CIT_SOHN],
  sig_lens=(
    "In the Signature Korean Method, the kitchen is the laboratory of "
    "transformation: raw sealed into cooked, each method its own "
    "signature - the boil, the grill, the ferment. The drill cooks the "
    "twenty sentences until flavor signs itself."))

E(key="travel",
  name="Travel and Directions Sentences",
  group="Compounded", ladder_rank=8, ladder_tier="compounded",
  description=(
    "Twenty sentences about transport, asking directions, tickets, and "
    "lodging. 1. 지하철을 타요 (jihacheoreul tayo, take the subway). 2. "
    "버스가 왔어요 (beoseuga wasseoyo, the bus came). 3. 택시를 불러요 "
    "(taeksireul bulleoyo, call a taxi). 4. 기차역이 어디예요 (gichayeogi "
    "eodiyeyo, where is the train station). 5. 공항까지 얼마나 걸려요 "
    "(gonghangkkaji eolmana geollyeoyo, how long does it take to the "
    "airport). 6. 이 버스가 시청에 가요 (i beoseuga sicheonge gayo, does "
    "this bus go to City Hall). 7. 여기서 내려요 (yeogiseo naeryeoyo, get "
    "off here). 8. 갈아타야 해요 (garataya haeyo, I need to transfer). 9. "
    "표 두 장 주세요 (pyo du jang juseyo, two tickets please). 10. 왕복으로 "
    "주세요 (wangbogeuro juseyo, round trip please). 11. 몇 번 출구예요 "
    "(myeot beon chulguyeyo, which exit number is it). 12. 오른쪽으로 "
    "가세요 (oreunjjogeuro gaseyo, go to the right). 13. 왼쪽에 있어요 "
    "(oenjjoge isseoyo, it is on the left). 14. 직진하세요 (jikjinhaseyo, "
    "go straight). 15. 신호등에서 돌아요 (sinhodeungeseo dorayo, turn at "
    "the traffic light). 16. 호텔을 예약했어요 (hotereul yeyakhaesseoyo, I "
    "reserved a hotel). 17. 체크인은 몇 시예요 (chekeuineun myeot siyeyo, "
    "what time is check-in). 18. 방이 조용해요 (bangi joyonghaeyo, the "
    "room is quiet). 19. 아침 식사가 포함돼요 (achim siksaga pohamdwaeyo, "
    "breakfast is included). 20. 짐을 맡아 주세요 (jimeul mata juseyo, "
    "please keep my luggage). Key transport words: 지하철 (jihacheol, "
    "subway), 버스 (beoseu, bus), 택시 (taeksi, taxi), 기차 (gicha, "
    "train), 비행기 (bihaenggi, airplane), 배 (bae, boat), 표 (pyo, "
    "ticket), 역 (yeok, station)."),
  how_it_works=(
    "Direction sentences pivot on three particles: 에 for destination "
    "(공항에 가요, go to the airport), 에서 for origin (서울에서 왔어요, "
    "came from Seoul), and (으)로 for direction or route (오른쪽으로, to "
    "the right). Asking directions follows a template: ~이/가 어디예요 "
    "(where is ~), 어떻게 가요 (how do I get there), 얼마나 걸려요 (how "
    "long does it take). Transport verbs pair with 을/를 타다 (to ride): "
    "버스를 타요, 지하철을 타요; getting off is 내리다, transferring is "
    "갈아타다. Lodging runs on 예약하다 (to reserve), 체크인/체크아웃, "
    "and the request pattern ~해 주세요. The flat-thing counter 장 counts "
    "tickets: 표 두 장."),
  key_points=[
    "에 destination, 에서 origin, (으)로 direction: the three direction particles.",
    "Direction-asking template: 어디예요 / 어떻게 가요 / 얼마나 걸려요.",
    "타다 to ride, 내리다 to get off, 갈아타다 to transfer.",
    "Tickets counted with 장; round trip is 왕복.",
    "20 sentences covering transport, directions, tickets, lodging."],
  requirements=[
    "20 sentences: transport, asking directions, tickets, lodging.",
    "Explain 에/에서/(으)로 with examples.",
    "Teach the direction-asking template.",
    "Give the transport verb set and ticket counter.",
    "All sentences translated into English."],
  standards=[CIT_NIKL, CIT_TOPIK, CIT_SOHN],
  citations=[CIT_NIKL, CIT_TOPIK, CIT_SOHN],
  sig_lens=(
    "In the Signature Korean Method, travel is the signature in motion: "
    "every ticket a sealed passage, every direction a line drawn true. "
    "The drill asks the way twenty times until the road signs itself."))

E(key="workschool",
  name="Work and School Sentences",
  group="Compounded", ladder_rank=8, ladder_tier="compounded",
  description=(
    "Twenty sentences about jobs, the office, the classroom, and "
    "learning. 1. 회사원이에요 (hoesawonieyo, I am an office worker). 2. "
    "아홉 시에 출근해요 (ahop sie chulgeunhaeyo, start work at nine). 3. "
    "여섯 시에 퇴근해요 (yeoseot sie toegeunhaeyo, leave work at six). 4. "
    "회의가 있어요 (hoeuiga isseoyo, there is a meeting). 5. 보고서를 써요 "
    "(bogoseoreul sseoyo, write a report). 6. 이메일을 보내요 (imeireul "
    "bonaeyo, send an email). 7. 상사에게 물어봐요 (sangsaege mureobwayo, "
    "ask the boss). 8. 동료와 점심을 먹어요 (dongnyowa jeomsimeul "
    "meogeoyo, eat lunch with a coworker). 9. 야근을 해요 (yageuneul "
    "haeyo, work overtime). 10. 월급이 올랐어요 (wolgeubi ollasseoyo, the "
    "salary went up). 11. 학생이에요 (haksaengieyo, I am a student). 12. "
    "수업이 재미있어요 (sueobi jaemiisseoyo, the class is fun). 13. "
    "숙제를 했어요 (sukjereul haesseoyo, I did the homework). 14. 시험이 "
    "어려웠어요 (siheomi eoryeowosseoyo, the exam was difficult). 15. "
    "선생님께 질문해요 (seonsaengnimkke jilmunhaeyo, ask the teacher a "
    "question). 16. 도서관에서 공부해요 (doseogwaneseo gongbuhaeyo, study "
    "at the library). 17. 한국어를 열심히 배워요 (hangugeoreul yeolsimhi "
    "baewoyo, study Korean diligently). 18. 발음이 좋아졌어요 (bareumi "
    "joajyeosseoyo, my pronunciation improved). 19. 장학금을 받았어요 "
    "(janghakgeumeul badasseoyo, I received a scholarship). 20. 졸업을 "
    "앞두고 있어요 (joreobeul apdugo isseoyo, I am about to graduate). "
    "Work words: 회사 (hoesa, company), 출근 (chulgeun, going to work), "
    "퇴근 (toegeun, leaving work), 회의 (hoeu, meeting), 월급 (wolgeup, "
    "salary). School words: 수업 (sueop, class), 숙제 (sukje, homework), "
    "시험 (siheom, exam), 성적 (seongjeok, grades)."),
  how_it_works=(
    "Workplace Korean runs one level more formal than daily speech: "
    "합니다 endings to superiors, 해요 to peers. Asking uses ~아/어 "
    "드릴까요 (shall I do it for you) and reporting uses ~았습니다. "
    "School Korean runs on the study verbs: 배우다 (learn), 공부하다 "
    "(study), 외우다 (oeuda, memorize), 복습하다 (bokseuphada, review). "
    "Time expressions anchor both worlds: ~에 for clock time (아홉 시에), "
    "~부터 ~까지 for spans (아홉 시부터 여섯 시까지, from nine to six). "
    "The humble verbs 올리다/드릴다 appear in offers: 도와 드릴까요 "
    "(dowa deurilkkayo, shall I help you). Promotions and grades use "
    "오르다 (to rise): 성적이 올랐어요 (grades went up)."),
  key_points=[
    "Workplace defaults to 합니다 with superiors, 해요 with peers.",
    "출근/퇴근 frame the workday; time spans use 부터/까지.",
    "Study verbs: 배우다, 공부하다, 외우다, 복습하다.",
    "20 sentences covering jobs, office, classroom, learning.",
    "Work and school vocabulary glosses included."],
  requirements=[
    "20 sentences: jobs, office, classroom, learning.",
    "Explain workplace vs peer speech levels.",
    "Teach the study-verb set and time-span pattern.",
    "Give work and school vocabulary glosses.",
    "All sentences translated into English."],
  standards=[CIT_NIKL, CIT_TOPIK, CIT_SOHN],
  citations=[CIT_NIKL, CIT_TOPIK, CIT_SOHN],
  sig_lens=(
    "In the Signature Korean Method, work is the daily sealing and study "
    "the sharpening of the seal: 출근 signs the morning, 복습 signs the "
    "lesson. The drill works and studies the twenty sentences until "
    "diligence signs itself."))

E(key="health",
  name="Health and Body Sentences",
  group="Compounded", ladder_rank=8, ladder_tier="compounded",
  description=(
    "Twenty sentences about body parts, symptoms, the doctor visit, and "
    "the pharmacy. 1. 머리가 아파요 (meoriga apayo, my head hurts). 2. "
    "배가 아파요 (baega apayo, my stomach hurts). 3. 목이 아파요 (mogi "
    "apayo, my throat hurts). 4. 열이 나요 (yeori nayo, I have a fever). "
    "5. 기침이 나요 (gichimi nayo, I have a cough). 6. 콧물이 나요 "
    "(konmuri nayo, I have a runny nose). 7. 어지러워요 (eojireowoyo, I "
    "feel dizzy). 8. 속이 메스꺼워요 (sogi meseukkeowoyo, I feel "
    "nauseous). 9. 다리를 다쳤어요 (darireul dachyeosseoyo, I hurt my "
    "leg). 10. 팔이 부었어요 (pari bueosseoyo, my arm is swollen). 11. "
    "병원에 가야 해요 (byeongwone gaya haeyo, I need to go to the "
    "hospital). 12. 어디가 아프세요 (eodiga apeuseyo, where does it hurt "
    "- polite). 13. 언제부터 아팠어요 (eonjebuteo apasseoyo, since when "
    "has it hurt). 14. 약을 먹었어요 (yageul meogeosseoyo, I took "
    "medicine). 15. 주사를 맞았어요 (jusareul majasseoyo, I got an "
    "injection). 16. 푹 쉬어야 해요 (puk swieoya haeyo, you need full "
    "rest). 17. 물을 많이 마셔요 (mureul manhi masyeoyo, drink lots of "
    "water). 18. 약국에서 약을 샀어요 (yakgugeseo yageul sasseoyo, bought "
    "medicine at the pharmacy). 19. 처방전이 필요해요 (cheobangjeoni "
    "piryohaeyo, I need a prescription). 20. 이제 괜찮아요 (ije "
    "gwaenchanayo, I am fine now). Body parts: 머리 (meori, head), 눈 "
    "(nun, eye), 코 (ko, nose), 입 (ip, mouth), 귀 (gwi, ear), 목 (mok, "
    "neck/throat), 어깨 (eokkae, shoulder), 팔 (pal, arm), 손 (son, hand), "
    "손가락 (songarak, finger), 다리 (dari, leg), 발 (bal, foot), 배 "
    "(bae, stomach), 등 (deung, back), 심장 (simjang, heart)."),
  how_it_works=(
    "Symptom sentences use the pattern [body part] + 이/가 + 아파요 (hurts) "
    "or [symptom] + 이/가 + 나요 (comes out / I have): 머리가 아파요, 열이 "
    "나요, 기침이 나요. The experiencer is usually omitted - 아파요 alone "
    "means 'I hurt' when you are the speaker. Doctor questions run in "
    "polite forms: 어디가 아프세요, 언제부터 그러셨어요. Medical requests "
    "use ~아/어 주세요 and obligation uses ~아/어야 해요: 쉬어야 해요 "
    "(must rest), 먹어야 해요 (must take). At the pharmacy, name the "
    "symptom and ask: 감기약 주세요 (gamgiyak juseyo, cold medicine "
    "please). Severity scales with adverbs: 조금 아파요 (a little), 많이 "
    "아파요 (a lot), 너무 아파요 (too much)."),
  key_points=[
    "Symptom pattern: body part + 이/가 아파요; symptom + 이/가 나요.",
    "The experiencer is omitted; the verb ending implies who hurts.",
    "Obligation with ~아/어야 해요; requests with ~아/어 주세요.",
    "15 body parts glossed; doctor and pharmacy dialogue frames.",
    "20 sentences covering body, symptoms, doctor visit, pharmacy."],
  requirements=[
    "20 sentences: body parts, symptoms, doctor visit, pharmacy.",
    "Teach the 아파요/나요 symptom patterns.",
    "Give 15 body-part glosses with romanization.",
    "Teach the doctor-question and pharmacy-request frames.",
    "All sentences translated into English."],
  standards=[CIT_NIKL, CIT_TOPIK, CIT_SOHN],
  citations=[CIT_NIKL, CIT_TOPIK, CIT_SOHN],
  sig_lens=(
    "In the Signature Korean Method, the body is the first instrument "
    "and health its tuning: each symptom a signal, each remedy a "
    "recalibration. The drill names every part and reports every signal "
    "until the instrument signs its own condition."))

E(key="emotions",
  name="Emotions and Feelings Sentences",
  group="Compounded", ladder_rank=9, ladder_tier="compounded",
  description=(
    "Twenty sentences about being happy, sad, angry, afraid, in love, and "
    "surprised. 1. 기뻐요 (gippeoyo, I am glad). 2. 행복해요 "
    "(haengbokhaeyo, I am happy). 3. 슬퍼요 (seulpeoyo, I am sad). 4. "
    "외로워요 (oerowoyo, I am lonely). 5. 화가 나요 (hwaga nayo, I am "
    "angry - 'anger comes out'). 6. 짜증 나요 (jjajeung nayo, I am "
    "annoyed). 7. 무서워요 (museowoyo, I am scared). 8. 걱정돼요 "
    "(geokjeongdwaeyo, I am worried). 9. 사랑해요 (saranghaeyo, I love "
    "you). 10. 보고 싶어요 (bogo sipeoyo, I miss you - 'want to see'). "
    "11. 놀라워요 (nollawoyo, I am surprised). 12. 신나요 (sinnayo, I am "
    "excited). 13. 피곤해요 (pigonhaeyo, I am tired). 14. 지루해요 "
    "(jiruhaeyo, I am bored). 15. 부끄러워요 (bukkeureowoyo, I am "
    "embarrassed). 16. 고마워요 (gomawoyo, I am thankful). 17. 미안해요 "
    "(mianhaeyo, I feel sorry). 18. 자랑스러워요 (jarangseureowoyo, I am "
    "proud). 19. 실망했어요 (silmanghaesseoyo, I am disappointed). 20. "
    "마음이 편해요 (ma-eumi pyeonhaeyo, my heart is at ease). Emotion "
    "words: 기쁨 (gippeum, joy), 슬픔 (seulpeum, sadness), 분노 (bunno, "
    "anger), 두려움 (duryeoum, fear), 사랑 (sarang, love), 놀람 (nollam, "
    "surprise), 걱정 (geokjeong, worry), 희망 (huimang, hope)."),
  how_it_works=(
    "Feelings conjugate as descriptive verbs: 슬프다 -> 슬퍼요, 기쁘다 -> "
    "기뻐요 (the ㅡ drops before 어). Some emotions are noun + 하다/되다 "
    "constructions: 걱정 + 되다 = 걱정돼요 (become worried), 사랑 + 하다 "
    "= 사랑해요. First-person feelings are stated directly, but "
    "third-person feelings require ~아/어 하다: 그는 슬퍼해요 (geuneun "
    "seulpeohaeyo, he acts/looks sad) - saying 그는 슬퍼요 claims direct "
    "knowledge of his inner state, which Korean grammar treats as "
    "overreach. Intensity scales: 조금 슬퍼요, 많이 슬퍼요, 너무 슬퍼요. "
    "보고 싶어요 covers 'miss' for people and things alike; 사랑해요 is "
    "reserved for deep love, while 좋아해요 (joahaeyo, I like) handles "
    "everything lighter."),
  key_points=[
    "Emotions conjugate as descriptive verbs: 슬프다 -> 슬퍼요.",
    "Third-person feelings require ~아/어 하다: 슬퍼해요, not 슬퍼요.",
    "Noun + 하다/되다 builds complex feelings: 걱정돼요, 사랑해요.",
    "보고 싶어요 means 'miss'; 사랑해요 is reserved for deep love.",
    "20 sentences across happy, sad, angry, afraid, love, surprise."],
  requirements=[
    "20 sentences covering the six emotion families.",
    "Explain the first-person vs third-person feeling rule.",
    "Show the 하다/되다 emotion constructions.",
    "Distinguish 사랑해요, 좋아해요, 보고 싶어요.",
    "All sentences translated into English."],
  standards=[CIT_NIKL, CIT_SOHN, CIT_TOPIK],
  citations=[CIT_NIKL, CIT_SOHN, CIT_TOPIK],
  sig_lens=(
    "In the Signature Korean Method, emotions are the weather of the "
    "seal: joy the clear sky, anger the thunderhead, love the deep "
    "current. The drill speaks each weather truly - mine signed plainly, "
    "another's signed with 하다 - until feeling signs itself."))

E(key="nature",
  name="Nature and Weather Sentences",
  group="Compounded", ladder_rank=9, ladder_tier="compounded",
  description=(
    "Twenty sentences about animals, plants, seasons, and weather talk. "
    "1. 비가 와요 (biga wayo, it is raining). 2. 눈이 와요 (nuni wayo, it "
    "is snowing). 3. 바람이 불어요 (barami bureoyo, the wind is blowing). "
    "4. 날씨가 좋아요 (nalssiga joayo, the weather is nice). 5. 하늘이 "
    "맑아요 (haneuri malgayo, the sky is clear). 6. 구름이 많아요 (gureumi "
    "manayo, it is cloudy). 7. 더워요 (deowoyo, it is hot). 8. 추워요 "
    "(chuwoyo, it is cold). 9. 시원해요 (siwonhaeyo, it is cool and "
    "refreshing). 10. 봄에는 꽃이 피어요 (bomeneun kkochi pieoyo, flowers "
    "bloom in spring). 11. 여름에는 바다에 가요 (yeoreumeneun badae gayo, "
    "go to the sea in summer). 12. 가을에는 단풍이 예뻐요 (gaeureneun "
    "danpungi yeppeoyo, the autumn leaves are pretty). 13. 겨울에는 눈이 "
    "많이 와요 (gyeoureneun nuni manhi wayo, it snows a lot in winter). "
    "14. 강아지가 공원에서 뛰어놀아요 (gangajiga gongwoneseo ttwieonorayo, "
    "the puppy romps in the park). 15. 새가 노래해요 (saega noraehaeyo, "
    "the bird sings). 16. 나무에 잎이 돋아요 (namue ipi dodnayo, leaves "
    "sprout on the trees). 17. 산에 올라가요 (sane ollagayo, climb the "
    "mountain). 18. 바다에서 수영해요 (badaeseo suyeonghaeyo, swim in the "
    "sea). 19. 무지개가 떴어요 (mujigaega tteosseoyo, a rainbow appeared). "
    "20. 내일은 맑을 거예요 (naeireun malgeul geoyeyo, tomorrow will be "
    "clear). Animals: 개 (gae, dog), 고양이 (goyangi, cat), 새 (sae, "
    "bird), 물고기 (mulgogi, fish), 토끼 (tokki, rabbit), 호랑이 (horangi, "
    "tiger), 곰 (gom, bear). Plants: 나무 (namu, tree), 꽃 (kkot, flower), "
    "잎 (ip, leaf), 풀 (pul, grass), 열매 (yeolmae, fruit)."),
  how_it_works=(
    "Weather sentences drop the subject entirely - 비가 와요 has no 'it'; "
    "the rain itself is the subject with 가. Seasons take 에는 for 'in "
    "the season of': 봄에는, 여름에는. Temperature and conditions are "
    "descriptive verbs conjugated plainly: 덥다 -> 더워요, 춥다 -> 추워요 "
    "(ㅂ irregular: 춥 + 어요 = 추워요). Animal sounds are onomatopoeic "
    "and fun to drill: 멍멍 (meongmeong, woof), 야옹 (yaong, meow), 음매 "
    "(eummae, moo), 꿀꿀 (kkulkkul, oink). Nature verbs of change use "
    "~아/어지다: 맑아져요 (becomes clear), 어두워져요 (gets dark). "
    "Forecasts use the future: 비가 올 거예요 (it will rain), derived "
    "from 오다 -> 올 거예요."),
  key_points=[
    "Weather drops dummy subjects: 비가 와요, 눈이 와요, 바람이 불어요.",
    "Seasons with 에는; temperature verbs include the ㅂ irregular (춥다->추워요).",
    "Animal onomatopoeia: 멍멍, 야옹, 음매, 꿀꿀.",
    "Change-of-state with ~아/어지다; forecasts with ~ㄹ 거예요.",
    "20 sentences plus animal and plant vocabulary."],
  requirements=[
    "20 sentences: animals, plants, seasons, weather talk.",
    "Explain the subjectless weather pattern.",
    "Teach the ㅂ irregular through 춥다/덥다.",
    "Give animal and plant vocabulary with romanization.",
    "All sentences translated into English."],
  standards=[CIT_NIKL, CIT_SOHN, CIT_TOPIK],
  citations=[CIT_NIKL, CIT_SOHN, CIT_TOPIK],
  sig_lens=(
    "In the Signature Korean Method, nature is the original signature: "
    "the sky signs in cloud, the seasons seal in turn, each animal voices "
    "its own mark. The drill speaks the weather daily until the world "
    "signs back."))

E(key="shopping",
  name="Shopping and Money Sentences",
  group="Compounded", ladder_rank=9, ladder_tier="compounded",
  description=(
    "Twenty sentences about the market, prices, bargaining, and paying. "
    "1. 시장에 가요 (sijange gayo, go to the market). 2. 이거 얼마예요 "
    "(igeo eolmayeyo, how much is this). 3. 저거 보여 주세요 (jeogeo "
    "boyeo juseyo, please show me that one). 4. 다른 색 있어요 (dareun "
    "saek isseoyo, do you have another color). 5. 더 큰 거 있어요 (deo "
    "keun geo isseoyo, do you have a bigger one). 6. 입어 봐도 돼요 (ibeo "
    "bwado dwaeyo, may I try it on). 7. 너무 비싸요 (neomu bissayo, too "
    "expensive). 8. 깎아 주세요 (kkakka juseyo, please give a discount). "
    "9. 만 원에 주세요 (man wone juseyo, please give it for 10,000 won). "
    "10. 카드 돼요 (kadeu dwaeyo, do you take card). 11. 현금으로 할게요 "
    "(hyeongeumeuro halgeyo, I will pay cash). 12. 영수증 주세요 "
    "(yeongsujeung juseyo, receipt please). 13. 봉투에 넣어 주세요 "
    "(bongtue neoheo juseyo, please put it in a bag). 14. 세일 중이에요 "
    "(seil jungieyo, it is on sale). 15. 신상품이에요 (sinsangpumieyo, it "
    "is a new product). 16. 품절됐어요 (pumjeoldwaesseoyo, it is sold "
    "out). 17. 교환할 수 있어요 (gyohwanhal su isseoyo, I can exchange "
    "it). 18. 환불해 주세요 (hwanbulhae juseyo, please refund it). 19. "
    "포인트 적립해 주세요 (pointeu jeongniphae juseyo, please add the "
    "points). 20. 또 올게요 (tto olgeyo, I will come again). Money words: "
    "원 (won, Korean won), 가격 (gagyeok, price), 거스름돈 (geoseureumdon, "
    "change), 할인 (harin, discount), 세일 (seil, sale), 영수증 "
    "(yeongsujeung, receipt). Numbers for prices are Sino-Korean: 삼천 원 "
    "(samcheon won, 3,000 won), 오만 원 (oman won, 50,000 won)."),
  how_it_works=(
    "Market Korean is a call-and-response ritual. The buyer opens with "
    "이거 얼마예요; the seller answers with the price in Sino-Korean "
    "numbers + 원. Bargaining is polite and formulaic: 좀 깎아 주세요 "
    "(please cut it a little), with the seller countering 안 돼요 (no "
    "can do) or 조금만 깎아 드릴게요 (I will cut just a little). Trying "
    "things on: 입어 보다 (try on clothes), 신어 보다 (try on shoes) - "
    "보다 attached to a verb means 'try'. Payment: 카드 돼요 asks "
    "acceptance; 계산은 카드로 할게요 (I will pay by card) states the "
    "method. Exchanges and refunds are rights-based: 교환/환불 돼요 asks "
    "what is possible before demanding. The softener 좀 (a little, "
    "please) makes every request gentler: 좀 보여 주세요."),
  key_points=[
    "Price ritual: 얼마예요 -> Sino-Korean number + 원 -> 깎아 주세요.",
    "보다 attached to verbs means 'try': 입어 보다, 신어 보다.",
    "Payment with 카드 돼요 / 현금으로; receipts with 영수증 주세요.",
    "좀 softens every request; 교환/환불 frames returns politely.",
    "20 sentences covering market, prices, bargaining, paying."],
  requirements=[
    "20 sentences: market, prices, bargaining, paying.",
    "Teach the price-asking and bargaining ritual.",
    "Explain the ~아/어 보다 'try' construction.",
    "Give money vocabulary and Sino-Korean price numbers.",
    "All sentences translated into English."],
  standards=[CIT_NIKL, CIT_TOPIK, CIT_SOHN],
  citations=[CIT_NIKL, CIT_TOPIK, CIT_SOHN],
  sig_lens=(
    "In the Signature Korean Method, the market is the exchange of "
    "seals: price asked, value weighed, bargain sealed with a bow. The "
    "drill haggles the twenty sentences until every won signs its "
    "worth."))

E(key="friendship",
  name="Friendship and Social Life Sentences",
  group="Compounded", ladder_rank=9, ladder_tier="compounded",
  description=(
    "Twenty sentences about meeting people, invitations, and "
    "celebrations. 1. 친구를 사귀었어요 (chingureul sagwieosseoyo, I made "
    "a friend). 2. 처음 만났어요 (cheoeum mannasseoyo, we met for the "
    "first time). 3. 이름이 뭐예요 (ireumi mwoyeyo, what is your name - "
    "informal polite). 4. 어디서 왔어요 (eodiseo wasseoyo, where are you "
    "from). 5. 취미가 뭐예요 (chwimiga mwoyeyo, what is your hobby). 6. "
    "같이 밥 먹을래요 (gachi bap meogeullaeyo, want to eat together). 7. "
    "주말에 만날래요 (jumare mannallaeyo, want to meet this weekend). 8. "
    "생일 파티에 초대해요 (saengil patie chodaehaeyo, invite to a "
    "birthday party). 9. 결혼식에 갔어요 (gyeolhonsige gasseoyo, went to a "
    "wedding). 10. 축하해요 (chukahaeyo, congratulations). 11. 건배해요 "
    "(geonbaehaeyo, let's toast). 12. 오랜 친구예요 (oraen chinguyeyo, an "
    "old friend). 13. 사이가 좋아요 (saiga joayo, we get along well - "
    "'the between is good'). 14. 자주 연락해요 (jaju yeollakhaeyo, keep "
    "in touch often). 15. 문자를 보냈어요 (munjareul bonaesseoyo, I sent a "
    "text). 16. 사진을 같이 찍어요 (sajineul gachi jjigeoyo, take a photo "
    "together). 17. 노래방에 가요 (noraebange gayo, go to karaoke). 18. "
    "술 한 잔 해요 (sul han jan haeyo, have a drink - 'do one glass'). "
    "19. 즐거웠어요 (jeulgeowosseoyo, it was fun). 20. 다음에 또 봐요 "
    "(daeume tto bwayo, see you next time). Social words: 모임 (moim, "
    "gathering), 회식 (hoesik, company dinner), 동창 (dongchang, "
    "schoolmate), 선배 (seonbae, senior), 후배 (hubae, junior)."),
  how_it_works=(
    "Social Korean runs on invitations and soft proposals: ~ㄹ래요 "
    "(want to / shall we) makes the friendly offer - 갈래요, 먹을래요, "
    "만날래요 - while ~ㄹ까요 asks the group's opinion: 갈까요. Meeting "
    "someone new follows a script: 처음 뵙겠습니다 (formal first meeting), "
    "name exchange, 어디서 오셨어요 (where are you from - honorific), and "
    "the closer 잘 부탁드립니다. Age matters socially: Koreans ask 나이가 "
    "어떻게 되세요 (how old are you - honorific) early, because speech "
    "level and sibling terms (형/오빠/누나/언니 vs 친구) depend on who is "
    "older. Celebrations have fixed frames: 생일 축하해요, 결혼 축하해요, "
    "건배. Partings promise return: 다음에 또 봐요, 연락할게요 (I will "
    "contact you)."),
  key_points=[
    "Invitations with ~ㄹ래요; group suggestions with ~ㄹ까요.",
    "First-meeting script: greeting, name, origin, 잘 부탁드립니다.",
    "Age is asked early because speech level depends on it.",
    "선배/후배 mark senior-junior bonds; 사이가 좋아요 measures closeness.",
    "20 sentences covering meeting, invitations, celebrations."],
  requirements=[
    "20 sentences: meeting people, invitations, celebrations.",
    "Teach ~ㄹ래요 and ~ㄹ까요 with examples.",
    "Explain the first-meeting script and the age question.",
    "Give social vocabulary glosses.",
    "All sentences translated into English."],
  standards=[CIT_NIKL, CIT_SOHN, CIT_TOPIK],
  citations=[CIT_NIKL, CIT_SOHN, CIT_TOPIK],
  sig_lens=(
    "In the Signature Korean Method, friendship is the circle of seals: "
    "each meeting a new mark exchanged, each invitation a door opened. "
    "The drill opens twenty doors until welcome signs itself."))

E(key="technology",
  name="Technology and Communication Sentences",
  group="Compounded", ladder_rank=9, ladder_tier="compounded",
  description=(
    "Twenty sentences about phones, the internet, computers, and "
    "messaging. 1. 스마트폰을 써요 (seumateuponeul sseoyo, I use a "
    "smartphone). 2. 전화를 걸어요 (jeonhwareul georeoyo, make a phone "
    "call). 3. 문자를 보내요 (munjareul bonaeyo, send a text message). 4. "
    "사진을 찍어요 (sajineul jjigeoyo, take a photo). 5. 동영상을 봐요 "
    "(dongyeongsangeul bwayo, watch a video). 6. 인터넷으로 검색해요 "
    "(inteones euro geomsaekhaeyo, search on the internet). 7. 와이파이에 "
    "연결해요 (waipaie yeongyeolhaeyo, connect to Wi-Fi). 8. 배터리가 "
    "없어요 (baeteoriga eopseoyo, the battery is dead). 9. 충전기를 빌려요 "
    "(chungjeonggireul billyeoyo, borrow a charger). 10. 앱을 다운로드해요 "
    "(aebeul daunrodeuhaeyo, download an app). 11. 컴퓨터를 켜요 "
    "(keompyuteoreul kyeoyo, turn on the computer). 12. 파일을 저장해요 "
    "(paireul jeojanghaeyo, save the file). 13. 이메일을 확인해요 "
    "(imeireul hwaginh aeyo, check email). 14. 비밀번호를 입력해요 "
    "(bimilbeonhoreul imnyeokhaeyo, enter the password). 15. 화면이 "
    "꺼졌어요 (hwamyeoni kkeojyeosseoyo, the screen went off). 16. 다시 "
    "시작해요 (dasi sijakhaeyo, restart it). 17. 업데이트가 필요해요 "
    "(eopdeiteuga piryohaeyo, it needs an update). 18. 온라인으로 주문해요 "
    "(onllaineuro jumunhaeyo, order online). 19. 배송이 왔어요 (baesongi "
    "wasseoyo, the delivery arrived). 20. 영상 통화를 해요 (yeongsang "
    "tonghwareul haeyo, make a video call). Tech words: 핸드폰 (haendeupon, "
    "mobile phone - also 휴대폰 hyudaepon), 문자 (munja, text), 카톡 "
    "(katok, KakaoTalk message - verb 카톡하다), 와이파이 (waipai, "
    "Wi-Fi), 충전기 (chungjeonggi, charger), 화면 (hwamyeon, screen)."),
  how_it_works=(
    "Tech Korean is heavily Konglish - English loanwords written in "
    "Hangul: 스마트폰, 인터넷, 앱, 이메일, 와이파이, 다운로드. Loanwords "
    "take native particles and verbs without friction: 이메일을 보내요, "
    "다운로드해요. Device verbs are a closed set: 켜다/끄다 (turn on/off), "
    "연결하다 (connect), 저장하다 (save), 삭제하다 (sakjehada, delete), "
    "설치하다 (seolchihada, install). Messaging verbs: 보내다 (send), "
    "받다 (receive), 답장하다 (dapjanghada, reply). Troubleshooting "
    "follows a script: 안 돼요 (it does not work), 다시 시작해 보세요 "
    "(try restarting), 업데이트하세요 (update it). Video calls: 영상 "
    "통화; voice calls: 음성 통화. The counter for messages is 통 "
    "(tong): 문자 세 통 (three texts)."),
  key_points=[
    "Konglish loanwords take native particles freely: 이메일을 보내요.",
    "Device verb set: 켜다/끄다, 연결하다, 저장하다, 삭제하다, 설치하다.",
    "Troubleshooting script: 안 돼요 -> 다시 시작 -> 업데이트.",
    "Messages counted with 통; KakaoTalk verbs with 카톡하다.",
    "20 sentences covering phone, internet, computer, messaging."],
  requirements=[
    "20 sentences: phone, internet, computer, messaging.",
    "Explain Konglish integration with particles.",
    "Teach the device-verb set and troubleshooting script.",
    "Give tech vocabulary glosses.",
    "All sentences translated into English."],
  standards=[CIT_NIKL, CIT_TOPIK, CIT_SOHN],
  citations=[CIT_NIKL, CIT_TOPIK, CIT_SOHN],
  sig_lens=(
    "In the Signature Korean Method, technology is the extended hand of "
    "the seal: the phone a distant voice, the screen a far window. The "
    "drill operates every device in Korean until the machine signs in "
    "the language."))

E(key="tenses",
  name="Korean Verb Tenses in Sentences",
  group="Compounded", ladder_rank=9, ladder_tier="compounded",
  description=(
    "Present, past, and future across five sentences each, plus aspect "
    "and mood notes. PRESENT (present habitual and ongoing): 1. 매일 "
    "운동해요 (maeil undonghaeyo, I exercise every day). 2. 지금 밥을 "
    "먹어요 (jigeum babeul meogeoyo, I am eating now). 3. 한국어를 배워요 "
    "(hangugeoreul baewoyo, I learn Korean). 4. 비가 와요 (biga wayo, it "
    "is raining). 5. 학교에 다녀요 (hakgyoe danyeoyo, I attend school - "
    "habitual). PAST (completed action): 1. 어제 영화를 봤어요 (eoje "
    "yeonghwareul bwasseoyo, I watched a movie yesterday). 2. 밥을 "
    "먹었어요 (babeul meogeosseoyo, I ate). 3. 친구가 왔어요 (chinguga "
    "wasseoyo, a friend came). 4. 선물을 받았어요 (seonmureul badasseoyo, "
    "I received a gift). 5. 열심히 공부했어요 (yeolsimhi gongbuhaesseoyo, "
    "I studied hard). FUTURE (intention and prediction): 1. 내일 갈 "
    "거예요 (naeil gal geoyeyo, I will go tomorrow). 2. 열심히 하겠어요 "
    "(yeolsimhi hagesseoyo, I will work hard - volitional). 3. 비가 올 "
    "거예요 (biga ol geoyeyo, it will rain). 4. 곧 도착할 거예요 (got "
    "dochakal geoyeyo, I will arrive soon). 5. 도와줄게요 (dowajulgeyo, I "
    "will help you - promise). ASPECT: progressive -고 있다 (먹고 있어요, "
    "is eating); resultative -아/어 있다 (문이 열려 있어요, the door is "
    "open as a result); experiential -아/어 보다 (먹어 봤어요, have tried "
    "eating). MOOD: -겠- for intention (가겠어요), -(으)ㄹ 것이다 for "
    "neutral future, -아/어야 하다 for obligation (가야 해요, must go), "
    "-아/어도 되다 for permission (가도 돼요, may go)."),
  how_it_works=(
    "Tense stacks after the stem in a fixed slot. Present: stem + 아/어/여 "
    "+ 요. Past: stem + 았/었 + 어요 - the vowel harmony matches the "
    "stem's last vowel (가 -> 갔어요, 먹 -> 먹었어요), and 하다 collapses "
    "to 했어요. Future has two engines: -(으)ㄹ 거예요 for plans and "
    "predictions (갈 거예요, 먹을 거예요), and -겠어요 for will, intention, "
    "and formal conjecture (가겠어요, 비가 오겠어요). Aspect rides beside "
    "tense: -고 있다 marks ongoing action in the present, -았/었었다 marks "
    "a past-before-past (먹었었어요, had eaten). The retrospective -더- "
    "marks directly witnessed past: 먹더라 (I saw him eating). Learners "
    "should master 았/었 first, then ㄹ 것, then 겠 - that order covers "
    "ninety percent of daily tense needs."),
  key_points=[
    "Present 아/어/여요; past 았/었어요 with vowel harmony; future (으)ㄹ 거예요 and 겠어요.",
    "하다 collapses to 했어요 in the past; irregulars shift before 았/었.",
    "Aspect: -고 있다 progressive, -아/어 보다 experiential, -더- retrospective.",
    "Mood: -아/어야 하다 obligation, -아/어도 되다 permission.",
    "5+ translated sentences per tense plus aspect and mood frames."],
  requirements=[
    "Present, past, future with 5 translated sentences each.",
    "Explain vowel harmony in past-tense formation.",
    "Contrast (으)ㄹ 거예요 vs 겠어요.",
    "Cover progressive, experiential, obligation, permission.",
    "All sentences with Hangul, romanization, English."],
  standards=[CIT_SOHN, CIT_LEE, CIT_NIKL],
  citations=[CIT_SOHN, CIT_LEE, CIT_NIKL],
  sig_lens=(
    "In the Signature Korean Method, tense is the seal of time: 았/었 "
    "seals what is done, ㄹ 것 seals what is promised, 고 있다 seals what "
    "is happening now. The drill moves one verb through all time until "
    "the seal dates itself."))

E(key="qa",
  name="Korean Questions and Answers",
  group="Compounded", ladder_rank=10, ladder_tier="compounded",
  description=(
    "Twenty question-and-answer pairs covering who, what, where, when, "
    "why, and how. 1. Q: 누구세요 (nuguseyo, who is it) A: 김민준이에요 "
    "(Gim Minjunieyo, I am Kim Minjun). 2. Q: 뭐 해요 (mwo haeyo, what "
    "are you doing) A: 책 읽어요 (chaek ilgeoyo, reading a book). 3. Q: "
    "어디에 있어요 (eodie isseoyo, where is it) A: 책상 위에 있어요 "
    "(chaeksang wie isseoyo, on the desk). 4. Q: 언제 와요 (eonje wayo, "
    "when are you coming) A: 내일 와요 (naeil wayo, coming tomorrow). 5. "
    "Q: 왜 울어요 (wae ureoyo, why are you crying) A: 슬퍼서 울어요 "
    "(seulpeoseo ureoyo, crying because I am sad). 6. Q: 어떻게 가요 "
    "(eotteoke gayo, how do you get there) A: 지하철로 가요 (jihacheollo "
    "gayo, go by subway). 7. Q: 얼마예요 (eolmayeyo, how much is it) A: "
    "오천 원이에요 (ocheon wonieyo, it is 5,000 won). 8. Q: 몇 시예요 "
    "(myeot siyeyo, what time is it) A: 세 시예요 (se siyeyo, it is 3 "
    "o'clock). 9. Q: 무슨 요일이에요 (museun yoiliyeyo, what day is it) A: "
    "금요일이에요 (geumyoiliyeyo, it is Friday). 10. Q: 누구랑 갔어요 "
    "(nugurang gasseoyo, who did you go with) A: 친구랑 갔어요 (chingurang "
    "gasseoyo, I went with a friend). 11. Q: 뭐 먹을래요 (mwo "
    "meogeullaeyo, what do you want to eat) A: 비빔밥 먹을래요 (bibimbap "
    "meogeullaeyo, I want bibimbap). 12. Q: 어디서 만날까요 (eodiseo "
    "mannalkkayo, where shall we meet) A: 역 앞에서 만나요 (yeok apeseo "
    "mannayo, meet in front of the station). 13. Q: 왜 안 왔어요 (wae an "
    "wasseoyo, why did you not come) A: 아파서 못 왔어요 (apaseo mot "
    "wasseoyo, I was sick so I could not come). 14. Q: 얼마나 걸려요 "
    "(eolmana geollyeoyo, how long does it take) A: 삼십 분 걸려요 "
    "(samsip bun geollyeoyo, it takes 30 minutes). 15. Q: 몇 개 있어요 "
    "(myeot gae isseoyo, how many are there) A: 다섯 개 있어요 (daseot gae "
    "isseoyo, there are five). 16. Q: 누구 거예요 (nugu geoyeyo, whose is "
    "it) A: 제 거예요 (je geoyeyo, it is mine). 17. Q: 무슨 뜻이에요 "
    "(museun tteusieyo, what does it mean) A: '사랑'은 love예요 ('sarang'-"
    "eun love-yeyo, 'sarang' means love). 18. Q: 어떻게 생각해요 "
    "(eotteoke saenggakhaeyo, what do you think) A: 좋은 생각이에요 "
    "(joheun saenggagieyo, it is a good idea). 19. Q: 언제부터 배웠어요 "
    "(eonjebuteo baewosseoyo, since when have you learned) A: 작년부터 "
    "배웠어요 (jangnyeonbuteo baewosseoyo, since last year). 20. Q: 왜 "
    "한국어를 배워요 (wae hangugeoreul baewoyo, why do you learn Korean) "
    "A: 한국이 좋아서 배워요 (hangugi joaseo baewoyo, I learn because I "
    "like Korea)."),
  how_it_works=(
    "Korean question words stay in place - there is no wh-movement: "
    "어디에 있어요 keeps 어디 where the answer's location sits. Answers "
    "mirror the question's structure and usually drop what is already "
    "known: Q 뭐 먹을래요 A 비빔밥 (just the new information). Why-"
    "questions answer with -아/어서 (because): 슬퍼서, 아파서. Choice "
    "questions use ~인가: 커피인가 차인가 (coffee or tea). Yes/no "
    "questions are statements with rising intonation, answered with 네 "
    "(yes) or 아니요 (no) - but careful: 네 to a negative question "
    "agrees with the question's premise ('yes, that is right, I did not'), "
    "not with English-style polarity. Embedded questions take -는지: "
    "어디에 있는지 알아요 (I know where it is)."),
  key_points=[
    "Question words stay in situ; no wh-movement.",
    "Answers mirror structure and drop given information.",
    "Why-answers use -아/어서; 네/아니요 agree with the question's premise.",
    "20 pairs across who/what/where/when/why/how.",
    "Every pair with Hangul, romanization, and English."],
  requirements=[
    "20 question-and-answer pairs with translations.",
    "Cover who, what, where, when, why, how.",
    "Explain in-situ question words and the 네/아니요 polarity rule.",
    "Show -아/어서 in why-answers.",
    "All pairs with Hangul, romanization, English."],
  standards=[CIT_SOHN, CIT_NIKL, CIT_TOPIK],
  citations=[CIT_SOHN, CIT_NIKL, CIT_TOPIK],
  sig_lens=(
    "In the Signature Korean Method, questions are the open seals and "
    "answers the closing ones: each pair a call and its echo. The drill "
    "asks twenty questions and seals each answer until inquiry signs "
    "itself."))

E(key="commands",
  name="Korean Commands and Requests",
  group="Compounded", ladder_rank=10, ladder_tier="compounded",
  description=(
    "Twenty imperative and polite-request sentences, formal versus "
    "informal. FORMAL (하십시오체, to groups/strangers): 1. 앉으십시오 "
    "(anjeusipsio, please be seated). 2. 조용히 하십시오 (joyonghi "
    "hasipsio, please be quiet). 3. 문을 닫으십시오 (muneul dadeusipsio, "
    "please close the door). 4. 천천히 말씀하십시오 (cheoncheonhi "
    "malsseumhasipsio, please speak slowly). POLITE (해요체, everyday "
    "polite requests): 5. 앉으세요 (anjeuseyo, please sit). 6. 이리 오세요 "
    "(iri oseyo, please come here). 7. 창문을 열어 주세요 (changmuneul "
    "yeoreo juseyo, please open the window). 8. 도와주세요 (dowajuseyo, "
    "please help me). 9. 잠깐만 기다려 주세요 (jamkkanman gidaryeo juseyo, "
    "please wait a moment). 10. 다시 말해 주세요 (dasi malhae juseyo, "
    "please say it again). 11. 천천히 말해 주세요 (cheoncheonhi malhae "
    "juseyo, please speak slowly). 12. 보여 주세요 (boyeo juseyo, please "
    "show me). 13. 가르쳐 주세요 (gareuchyeo juseyo, please teach me). "
    "INFORMAL (해체, to close friends/juniors): 14. 앉아 (anja, sit). 15. "
    "이리 와 (iri wa, come here). 16. 문 닫아 (mun dada, close the door). "
    "17. 빨리 와 (ppalli wa, come quickly). 18. 먹어 (meogeo, eat). 19. "
    "조용히 해 (joyonghi hae, be quiet). 20. 걱정 마 (geokjeong ma, do "
    "not worry). Prohibitions use -지 마세요 (polite) / -지 마 (informal): "
    "가지 마세요 (gaji maseyo, please do not go), 만지지 마 (manjiji ma, "
    "do not touch). Suggestions: 같이 가요 (gachi gayo, let's go "
    "together), 쉴까요 (swilkkayo, shall we rest)."),
  how_it_works=(
    "Commands are verb endings, and each ending sets the social distance. "
    "십시오 is the formal imperative (verb stem + (으)십시오); 세요 is "
    "the polite imperative that doubles as an honorific statement "
    "(가세요 can mean 'please go' or 'he/she goes [honorific]'); the bare "
    "stem + 아/어 is the intimate imperative (가, 먹어). Requests soften "
    "commands with 주세요 (please give/do for me): 열어 주세요 is far "
    "gentler than 여세요. The pattern ~아/어 주시겠어요 (would you please) "
    "is the most deferential: 도와주시겠어요. Negative commands use 말다: "
    "-지 마세요 / -지 마십시오. Note the special verb 주다 in 주세요 - it "
    "is the humble 'give', so every 주세요 request literally says 'please "
    "give me the favor of ...'. Never use the intimate imperative upward "
    "in age or rank; default to 세요/주세요 with strangers."),
  key_points=[
    "십시오 formal, 세요 polite, 아/어 intimate: three imperative endings.",
    "주세요 softens any command into a request; 주시겠어요 is most deferential.",
    "Prohibitions with -지 마세요 / -지 마.",
    "세요 doubles as honorific statement - context disambiguates.",
    "20 sentences across formal, polite, and informal registers."],
  requirements=[
    "20 imperative/polite-request sentences, formal vs informal.",
    "Explain the three imperative endings with formation rules.",
    "Teach 주세요 softening and the prohibition pattern.",
    "Warn on the upward-use of intimate imperatives.",
    "All sentences translated into English."],
  standards=[CIT_SOHN, CIT_NIKL, CIT_TOPIK],
  citations=[CIT_SOHN, CIT_NIKL, CIT_TOPIK],
  sig_lens=(
    "In the Signature Korean Method, commands are seals of direction: "
    "하십시오 the proclamation, 주세요 the sealed request, 마 the "
    "withheld seal. The drill commands and requests at each distance "
    "until authority signs itself."))

# ============================ ADVANCED ============================

E(key="descriptions",
  name="Describing People and Places in Korean",
  group="Advanced", ladder_rank=10, ladder_tier="advanced",
  description=(
    "Twenty sentences describing people, places, and things in detail. "
    "1. 키가 크고 눈이 큰 사람이에요 (kiga keugo nuni keun saramieyo, a "
    "tall person with big eyes). 2. 머리가 길고 웃는 얼굴이에요 (meoriga "
    "gilgo unneun eolgurieyo, long hair and a smiling face). 3. 성격이 밝고 "
    "친절해요 (seonggyeogi balkgo chinjeolhaeyo, bright and kind "
    "personality). 4. 목소리가 부드러워요 (moksoriga budeureowoyo, the "
    "voice is gentle). 5. 할아버지는 키가 크셨어요 (harabeojineun kiga "
    "keusyeosseoyo, grandfather was tall - honorific). 6. 아기는 눈이 "
    "맑아요 (agineun nuni malgayo, the baby's eyes are clear). 7. 서울은 "
    "사람이 많은 도시예요 (seoureun sarami manheun dosiyeyo, Seoul is a "
    "crowded city). 8. 바다가 보이는 방이에요 (badaga boineun bangieyo, a "
    "room with a sea view). 9. 조용하고 깨끗한 마을이에요 (joyonghago "
    "kkaekkeuthan maeurieyo, a quiet and clean village). 10. 높은 산과 "
    "깊은 계곡이 있어요 (nopeun sangwa gipeun gyegogi isseoyo, there are "
    "high mountains and deep valleys). 11. 오래된 절이 산속에 있어요 "
    "(oraedoen jeori sansoge isseoyo, an old temple is in the mountains). "
    "12. 넓은 강이 도시를 가로질러요 (neolbeun gangi dosireul "
    "garojilleoyo, a wide river crosses the city). 13. 빨간 지붕의 작은 "
    "집이에요 (ppalgan jibungui jageun jibieyo, a small house with a red "
    "roof). 14. 맛있는 냄새가 나요 (masinneun naemsaega nayo, a delicious "
    "smell comes out). 15. 부드러운 바람이 불어요 (budeureoun barami "
    "bureoyo, a gentle wind blows). 16. 반짝이는 별이 보여요 "
    "(banjjagineun byeori boyeoyo, twinkling stars are visible). 17. "
    "시원한 물이 흘러요 (siwonhan muri heulleoyo, cool water flows). 18. "
    "따뜻한 햇살이 들어와요 (ttatteuthan haetsari deureowayo, warm "
    "sunlight comes in). 19. 복잡한 거리지만 정이 있어요 (bokjapan "
    "georijiman jeongi isseoyo, a busy street but with warmth). 20. 처음 "
    "보는 곳인데 낯익어요 (cheoeum boneun gosinde najigeoyo, a place seen "
    "for the first time yet familiar)."),
  how_it_works=(
    "Descriptions stack modifiers before the noun: the modifier ending "
    "-는 marks present/habitual (웃는 얼굴, smiling face; 보이는 방, "
    "visible room), -은/ㄴ marks completed state (오래된 절, old temple; "
    "반짝이는 별 keeps 는 because twinkling is ongoing). Multiple "
    "qualities chain with -고: 키가 크고 눈이 커요. Body-part topics use "
    "the double-subject pattern: 코가 높아요 is literally 'as for the "
    "nose, it is high' - Korean describes people part by part rather than "
    "with 'have'. Colors and textures take the modifier form: 빨간 "
    "(red), 파란 (blue), 하얀 (white), 까만 (black) - these are the "
    "native color adjectives, distinct from the Sino-style 빨강. "
    "Honorifics lift descriptions of elders: 크셨어요, not 컸어요."),
  key_points=[
    "Modifier endings: -는 ongoing, -은/ㄴ completed state, stacked before the noun.",
    "Double-subject pattern describes people part by part: 눈이 커요.",
    "Qualities chain with -고; native color adjectives 빨간/파란/하얀/까만.",
    "Honorifics apply to descriptions of elders.",
    "20 detailed descriptive sentences with breakdowns."],
  requirements=[
    "20 sentences describing people, places, things in detail.",
    "Explain -는 vs -은/ㄴ modifier endings.",
    "Teach the double-subject description pattern.",
    "Cover native color adjectives and quality chaining.",
    "All sentences with Hangul, romanization, English."],
  standards=[CIT_SOHN, CIT_NIKL, CIT_LEE],
  citations=[CIT_SOHN, CIT_NIKL, CIT_LEE],
  sig_lens=(
    "In the Signature Korean Method, description is the portrait-seal: "
    "each modifier a brushstroke, each part-topic a measured line. The "
    "drill paints twenty portraits until likeness signs itself."))

E(key="story1",
  name="Korean Story I: A Day at the Park",
  group="Advanced", ladder_rank=10, ladder_tier="advanced",
  description=(
    "A ten-sentence simple story in Korean with line-by-line English "
    "translation. 1. 오늘은 토요일이에요 (oneureun toyoilieyo, today is "
    "Saturday). 2. 아침에 공원에 갔어요 (achime gongwone gasseoyo, I went "
    "to the park in the morning). 3. 날씨가 정말 좋았어요 (nalssiga "
    "jeongmal joasseoyo, the weather was really nice). 4. 많은 사람들이 "
    "산책했어요 (manheun saramdeuri sanchaekhaesseoyo, many people were "
    "strolling). 5. 아이들이 공을 찼어요 (aideuri gongeul chasseoyo, "
    "children were kicking a ball). 6. 벤치에 앉아서 책을 읽었어요 "
    "(benchie anjaseo chaegeul ilgeosseoyo, I sat on a bench and read a "
    "book). 7. 새들이 노래했어요 (saedeuri noraehaesseoyo, birds were "
    "singing). 8. 점심으로 김밥을 먹었어요 (jeomsimeuro gimbabeul "
    "meogeosseoyo, I ate kimbap for lunch). 9. 오후에는 사진을 찍었어요 "
    "(ohueneun sajineul jjigeosseoyo, in the afternoon I took photos). "
    "10. 행복한 하루였어요 (haengbokhan haruyeosseoyo, it was a happy "
    "day). Grammar notes: the story stays in the past tense 았/었어요; "
    "time words (오늘은, 아침에, 오후에는) open sentences; -아/어서 links "
    "sequential actions (앉아서 읽었어요, sat and then read); descriptive "
    "modifiers (많은, 행복한) precede their nouns."),
  how_it_works=(
    "A simple narrative runs on three rails: time anchors, past-tense "
    "verbs, and sequential connectors. Open with the day (오늘은 "
    "토요일이에요), then move through the day with time words. Keep every "
    "verb in 았/었어요 for a clean past narrative; switch to present only "
    "for timeless description. Link actions with -아/어서 (앉아서, "
    "sitting and then) and -고 (먹고, eat and). End with an evaluative "
    "sentence (행복한 하루였어요) - Korean stories close with the "
    "speaker's feeling, not just the last event. Read the story aloud "
    "three times: first for pronunciation, second translating each line, "
    "third retelling it from memory with the book closed."),
  key_points=[
    "10-sentence story, all past tense, with line-by-line translation.",
    "Time anchors open sentences; -아/어서 links sequential actions.",
    "Stories close with an evaluative feeling sentence.",
    "Three-pass reading method: pronounce, translate, retell.",
    "Grammar notes decode every structural choice."],
  requirements=[
    "A 10-sentence simple story in Korean.",
    "Line-by-line English translation.",
    "Grammar notes on tense, connectors, modifiers.",
    "A reading method for learners.",
    "Hangul and romanization on every line."],
  standards=[CIT_NIKL, CIT_TOPIK, CIT_SOHN],
  citations=[CIT_NIKL, CIT_TOPIK, CIT_SOHN],
  sig_lens=(
    "In the Signature Korean Method, the simple story is the first "
    "sealed narrative: ten marks in order, each day signed as lived. The "
    "drill tells the park day until memory signs it without the page."))

E(key="story2",
  name="Korean Story II: The Lost Umbrella",
  group="Advanced", ladder_rank=10, ladder_tier="advanced",
  description=(
    "A ten-sentence story using past tense forms, with line-by-line "
    "translation. 1. 어제 비가 많이 왔어요 (eoje biga manhi wasseoyo, "
    "yesterday it rained a lot). 2. 우산을 쓰고 나갔어요 (usaneul sseugo "
    "nagasseoyo, I went out with an umbrella). 3. 버스에서 내릴 때 우산을 "
    "잊었어요 (beoseueseo naeril ttae usaneul ijeosseoyo, when getting off "
    "the bus I forgot the umbrella). 4. 회사에 도착해서야 알았어요 "
    "(hoesae dochakhaeseoya arasseoyo, only on arriving at work did I "
    "realize). 5. 너무 아쉬웠어요 (neomu aswiwosseoyo, I was so "
    "disappointed). 6. 점심시간에 편의점에 갔어요 (jeomsimsigane "
    "pyeonuijeome gasseoyo, at lunchtime I went to the convenience store). "
    "7. 새 우산을 하나 샀어요 (sae usaneul hana sasseoyo, I bought a new "
    "umbrella). 8. 퇴근할 때 비가 그쳤어요 (toegeunhal ttae biga "
    "geuchyeosseoyo, when leaving work the rain had stopped). 9. 우산이 두 "
    "개가 됐어요 (usani du gaega dwaesseoyo, now I had two umbrellas). 10. "
    "잃어버린 우산은 버스 회사에 전화했어요 (ireobeorin usaneun beoseu "
    "hoesae jeonhwahaesseoyo, about the lost umbrella, I called the bus "
    "company). Grammar notes: -았/었을 때 for 'when' clauses (내릴 때, "
    "퇴근할 때); -아서야 for 'only upon' (도착해서야); the retrospective "
    "-더- is absent because this is personal experience; topic shift with "
    "잃어버린 우산은 reframes the lost object."),
  how_it_works=(
    "Past narratives layer more than simple 았/었어요. The -았/었을 때 "
    "clause sets a time frame (내릴 때, when getting off); -아/어서야 "
    "marks a belated realization (도착해서야 알았어요); -게 되다 marks "
    "an unintended result (두 개가 됐어요, ended up with two). Cause "
    "flows through -아/어서: 비가 와서 우산을 썼어요. Contrast with -지만: "
    "새 우산을 샀지만 비가 그쳤어요 (I bought one, but the rain "
    "stopped). The story's arc - problem, reaction, resolution, loose end "
    "- mirrors the Korean narrative habit of ending with an unresolved "
    "thread (the phone call), inviting the listener to imagine the rest."),
  key_points=[
    "10-sentence past-tense story with line-by-line translation.",
    "-았/었을 때 time clauses; -아/어서야 belated realization; -게 되다 unintended results.",
    "Cause with -아/어서, contrast with -지만.",
    "Topic reframing with 은/는 mid-story.",
    "Grammar notes decode every structural choice."],
  requirements=[
    "A 10-sentence story using past tense forms.",
    "Line-by-line English translation.",
    "Teach the past-narrative connectors used.",
    "Show cause, contrast, and result constructions.",
    "Hangul and romanization on every line."],
  standards=[CIT_NIKL, CIT_SOHN, CIT_LEE],
  citations=[CIT_NIKL, CIT_SOHN, CIT_LEE],
  sig_lens=(
    "In the Signature Korean Method, the past story is the sealed "
    "record: what happened signed in order, causes chained, loose ends "
    "left open. The drill tells the umbrella's tale until the past "
    "signs itself."))

E(key="story3",
  name="Korean Story III: The Future Garden",
  group="Advanced", ladder_rank=10, ladder_tier="advanced",
  description=(
    "A ten-sentence story using future and conditional forms, with "
    "line-by-line translation. 1. 내년 봄에는 정원을 만들 거예요 (naenyeon "
    "bomeneun jeongwoneul mandeul geoyeyo, next spring I will make a "
    "garden). 2. 먼저 땅을 고를 거예요 (meonjeo ttangeul goreul geoyeyo, "
    "first I will choose the land). 3. 씨앗을 뿌리면 싹이 날 거예요 "
    "(ssiasseul ppurimyeon ssagi nal geoyeyo, if I sow seeds, sprouts "
    "will come up). 4. 매일 물을 줄 거예요 (maeil mureul jul geoyeyo, I "
    "will water every day). 5. 꽃이 피면 정말 예쁠 거예요 (kkochi pimyeon "
    "jeongmal yeppeul geoyeyo, when the flowers bloom it will be really "
    "pretty). 6. 여름에는 열매를 딸 수 있을 거예요 (yeoreumeneun "
    "yeolmaereul ttal su isseul geoyeyo, in summer I will be able to pick "
    "fruit). 7. 친구들을 초대할 거예요 (chingudeureul chodaehal geoyeyo, I "
    "will invite my friends). 8. 함께 차를 마시면서 이야기할 거예요 "
    "(hamkke chareul masimyeonseo iyagihal geoyeyo, we will talk while "
    "drinking tea together). 9. 비가 와도 정원은 자랄 거예요 (biga wado "
    "jeongwoneun jaral geoyeyo, even if it rains the garden will grow). "
    "10. 내년 가을에는 수확을 하겠어요 (naenyeon gaeureneun suhageul "
    "hagesseoyo, next autumn I will harvest - volitional). Grammar notes: "
    "-(으)ㄹ 거예요 for plans and predictions; -면 for conditionals "
    "(뿌리면, 피면); -면서 for simultaneous action (마시면서); -아/어도 for "
    "'even if' (와도); -겠- for volition in the closing line."),
  how_it_works=(
    "Future narratives run on two futures: -(으)ㄹ 거예요 states plans "
    "and confident predictions, while -겠어요 adds will and volition - "
    "the closing 하겠어요 is a vow, not a forecast. Conditionals use "
    "-면 on the condition clause with the future in the main clause: "
    "뿌리면 날 거예요. Concessions use -아/어도: 와도 자랄 거예요. "
    "Simultaneous actions pair with -면서: 마시면서 이야기할 거예요. "
    "Sequence in the future uses -고 나서 or -은 후에: 심고 나서 물을 "
    "줄 거예요. The story arc moves plan -> conditions -> tending -> "
    "harvest, and Korean future stories conventionally close with a "
    "-겠- vow, sealing the speaker's commitment."),
  key_points=[
    "10-sentence future/conditional story with line-by-line translation.",
    "-(으)ㄹ 거예요 plans vs -겠어요 volition.",
    "-면 conditionals, -아/어도 concessions, -면서 simultaneity.",
    "Future sequence with -고 나서 / -은 후에.",
    "Closing -겠- vow as the conventional seal."],
  requirements=[
    "A 10-sentence story using future/conditional forms.",
    "Line-by-line English translation.",
    "Contrast the two futures with examples.",
    "Teach conditional, concessive, simultaneous constructions.",
    "Hangul and romanization on every line."],
  standards=[CIT_NIKL, CIT_SOHN, CIT_LEE],
  citations=[CIT_NIKL, CIT_SOHN, CIT_LEE],
  sig_lens=(
    "In the Signature Korean Method, the future story is the seal not "
    "yet pressed: plans drawn, conditions weighed, the vow signed last. "
    "The drill tells the garden's future until intention signs itself."))

E(key="idioms",
  name="Korean Idioms and Proverbs",
  group="Advanced", ladder_rank=10, ladder_tier="advanced",
  description=(
    "Twenty Korean idioms and proverbs with literal translation, real "
    "meaning, and an example sentence. 1. 백지장도 맞들면 낫다 "
    "(baekjijangdo matdeulmyeon natda) - literal: 'even a sheet of paper "
    "is lighter when lifted together'; meaning: many hands make light "
    "work; ex: 함께 하니 백지장도 맞들면 낫다 (hamkke hani baekjijangdo "
    "matdeulmyeon natda, doing it together, many hands make light work). "
    "2. 고생 끝에 낙이 온다 (gosaeng kkeute nagi onda) - 'at the end of "
    "hardship comes joy'; ex: 고생 끝에 낙이 온다고 했어요 (gosaeng "
    "kkeute nagi ondago haesseoyo, they said joy comes after hardship). "
    "3. 가는 말이 고와야 오는 말이 곱다 (ganeun mari gowaya oneun mari "
    "gopda) - 'only kind outgoing words bring kind incoming words'; "
    "meaning: speak kindly to be spoken to kindly. 4. 꿩 먹고 알 먹기 "
    "(kkwong meokgo al meokgi) - 'eating the pheasant and eating its eggs "
    "too'; meaning: killing two birds with one stone. 5. 누워서 떡 먹기 "
    "(nuwoseo tteok meokgi) - 'eating rice cake lying down'; meaning: a "
    "piece of cake. 6. 발 없는 말이 천 리 간다 (bal eomneun mari cheon ri "
    "ganda) - 'a horse without feet goes a thousand li'; meaning: rumors "
    "spread fast. 7. 원숭이도 나무에서 떨어진다 (wonsungido namueseo "
    "tteoreojinda) - 'even monkeys fall from trees'; meaning: even "
    "experts err. 8. 낮말은 새가 듣고 밤말은 쥐가 듣는다 (nanmareun saega "
    "deutgo banmareun jwiga deunneunda) - 'day words the bird hears, night "
    "words the rat hears'; meaning: walls have ears. 9. 콩 심은 데 콩 "
    "나고 팥 심은 데 팥 난다 (kong simeun de kong nago pat simeun de pat "
    "nanda) - 'where beans are planted beans grow'; meaning: you reap "
    "what you sow. 10. 티끌 모아 태산 (tikkeul moa taesan) - 'dust "
    "gathered becomes Mount Tae'; meaning: many a little makes a mickle. "
    "11. 시작이 반이다 (sijagi banida) - 'starting is half'; meaning: well "
    "begun is half done. 12. 호랑이도 제 말 하면 온다 (horangido je mal "
    "hamyeon onda) - 'speak of the tiger and it comes'; meaning: speak of "
    "the devil. 13. 소 잃고 외양간 고친다 (so ilko oeyanggan gochinda) - "
    "'fix the barn after losing the cow'; meaning: lock the stable door "
    "after the horse has bolted. 14. 엎질러진 물 (eopjilleojin mul) - "
    "'spilled water'; meaning: no use crying over spilled milk. 15. "
    "개천에서 용 난다 (gaecheoneseo yong nanda) - 'a dragon rises from a "
    "ditch'; meaning: greatness from humble origins. 16. 바늘 도둑이 소 "
    "도둑 된다 (baneul dodugi so doduk doenda) - 'a needle thief becomes a "
    "cow thief'; meaning: small crimes grow. 17. 마른 하늘에 날벼락 "
    "(mareun haneure nalbyeorak) - 'a thunderbolt from a dry sky'; "
    "meaning: a bolt from the blue. 18. 그림의 떡 (geurimui tteok) - 'rice "
    "cake in a picture'; meaning: pie in the sky. 19. 첫술에 배부르랴 "
    "(cheotsure baebureurya) - 'can the first spoonful fill you'; "
    "meaning: Rome was not built in a day. 20. 아는 길도 물어가라 (aneun "
    "gildo mureogara) - 'ask the way even on a road you know'; meaning: "
    "there is no harm in double-checking."),
  how_it_works=(
    "Proverbs (속담, sokdam) use the plain dictionary form - 낫다, 온다, "
    "간다 - because they state timeless truths. Quote one with ~다고 "
    "하다: 고생 끝에 낙이 온다고 했어요. Idioms slot into sentences as "
    "noun phrases (누워서 떡 먹기예요, it is a piece of cake) or verb "
    "phrases (티끌 모아 태산이다). Many encode Confucian social wisdom - "
    "the speech proverb (가는 말이 고와야) and the caution proverbs "
    "(낮말은 새가 듣고) - so using them correctly signals cultural "
    "fluency, not just vocabulary. Learn them in pairs of opposites where "
    "possible: 고생 끝에 낙이 온다 with 첫술에 배부르랴 (patience now, "
    "patience later). Drop one proverb per conversation at most; more "
    "sounds like a speech contest."),
  key_points=[
    "20 idioms/proverbs: literal gloss, real meaning, example sentence.",
    "Proverbs use the plain 다 form for timeless truth; quoted with ~다고 하다.",
    "Many encode Confucian social wisdom - use signals cultural fluency.",
    "Learn in contrasting pairs; one proverb per conversation at most.",
    "Every entry with Hangul, romanization, English."],
  requirements=[
    "20 idioms/proverbs with literal translation, real meaning, example sentence.",
    "Explain the plain-form convention and ~다고 하다 quoting.",
    "Note the cultural-wisdom dimension.",
    "Give a usage-frequency caution.",
    "All entries with Hangul, romanization, English."],
  standards=[CIT_NIKL, CIT_SOHN, CIT_LEE],
  citations=[CIT_NIKL, CIT_SOHN, CIT_LEE],
  sig_lens=(
    "In the Signature Korean Method, proverbs are the old seals: wisdom "
    "pressed by generations, each saying a stamp of how to live. The "
    "drill carries twenty old seals and learns when to press each one."))

E(key="registers",
  name="Formal and Polite Registers in Korean",
  group="Advanced", ladder_rank=10, ladder_tier="advanced",
  description=(
    "Fifteen formal-versus-informal pairs for letters, business, and "
    "elders, with translations. 1. Formal: 식사하셨어요 (siksahasyeosseoyo, "
    "have you eaten - honorific) / Informal: 밥 먹었어 (bap meogeosseo, "
    "did you eat). 2. Formal: 어디에 계세요 (eodie gyeseyo, where are you "
    "- honorific) / Informal: 어디 있어 (eodi isseo, where are you). 3. "
    "Formal: 성함이 어떻게 되세요 (seonghami eotteoke doeseyo, what is "
    "your name - honorific) / Informal: 이름이 뭐야 (ireumi mwoya, what "
    "is your name). 4. Formal: 연세가 어떻게 되세요 (yeonsega eotteoke "
    "doeseyo, how old are you - honorific) / Informal: 몇 살이야 (myeot "
    "sariya, how old are you). 5. Formal: 말씀해 주십시오 (malsseumhae "
    "jusipsio, please tell me - honorific) / Informal: 말해 줘 (malhae "
    "jwo, tell me). 6. Formal: 도와주시겠어요 (dowajusigesseoyo, would you "
    "help me) / Informal: 도와줘 (dowajwo, help me). 7. Formal: "
    "감사드립니다 (gamsadeurimnida, I humbly thank you) / Informal: 고마워 "
    "(gomawo, thanks). 8. Formal: 죄송합니다 (joesonghamnida, I "
    "apologize) / Informal: 미안 (mian, sorry). 9. Formal: 안녕히 가십시오 "
    "(annyeonghi gasipsio, farewell) / Informal: 잘 가 (jal ga, bye). 10. "
    "Formal: 회의에 참석하겠습니다 (hoeuie chamseokhagetsseumnida, I will "
    "attend the meeting) / Informal: 회의에 갈게 (hoeuie galge, I will go "
    "to the meeting). 11. Formal: 검토해 주시기 바랍니다 (geomtohae jusigi "
    "baramnida, I humbly ask your review - letter style) / Informal: "
    "확인해 줘 (hwaginhae jwo, check it). 12. Formal: 댁이 어디세요 "
    "(daegi eodiseyo, where is your home - honorific) / Informal: 집이 "
    "어디야 (jibi eodiya, where is your house). 13. Formal: 편히 쉬십시오 "
    "(pyeonhi swisipsio, please rest comfortably) / Informal: 잘 쉬어 (jal "
    "swieo, rest well). 14. Formal: 건강하십시오 (geonganghasipsio, stay "
    "healthy) / Informal: 건강해 (geonganghae, stay healthy). 15. Formal: "
    "뵙게 되어 영광입니다 (boepge doeeo yeonggwangimnida, honored to meet "
    "you - letter style) / Informal: 만나서 반가워 (mannaseo bangawo, nice "
    "to meet you). Register notes: 하십시오체 for announcements and the "
    "military; 해요체 for daily polite life; 해체 for intimates; 하오체/하게체 "
    "survive in historical dramas and some elder speech. Honorific nouns: "
    "집->댁, 밥->진지, 말->말씀, 이름->성함, 나이->연세. Humble verbs: "
    "주다->드리다, 먹다/마시다->잡수시다 (honorific subject)."),
  how_it_works=(
    "Register is a whole-sentence transformation, not a word swap. Moving "
    "formal: raise the subject with 께서/께 and honorific verbs (계시다, "
    "주무시다, 드시다), lift nouns to their honorific forms (성함, 연세, "
    "댁), humble your own actions (드리다, 뵙다), and close with ㅂ니다/십시오. "
    "Moving informal: drop all of it and use the plain stem + 아/어. "
    "Business letters run on ~바랍니다 and ~드립니다 frames: 검토해 주시기 "
    "바랍니다, 감사드립니다. Elders get the full honorific stack even in "
    "casual family speech: 할머니, 진지 잡수셨어요 (grandmother, have you "
    "eaten - honorific meal). The dangerous middle - 해요체 to a superior "
    "about a superior's actions without honorifics - is the most common "
    "foreigner error: say 아버지가 주무세요, never 아버지가 자요."),
  key_points=[
    "15 formal/informal pairs across letters, business, elders.",
    "Register transforms the whole sentence: honorific verbs, nouns, humble forms, endings.",
    "Honorific nouns: 댁, 진지, 말씀, 성함, 연세; humble: 드리다, 뵙다.",
    "하십시오체, 해요체, 해체, and the surviving 하오체/하게체 mapped.",
    "Every pair with Hangul, romanization, English."],
  requirements=[
    "15 formal vs informal pairs with translations.",
    "Explain the full-sentence register transformation.",
    "List honorific nouns and humble verbs.",
    "Map the five speech levels with their domains.",
    "All pairs with Hangul, romanization, English."],
  standards=[CIT_SOHN, CIT_NIKL, CIT_LEE],
  citations=[CIT_SOHN, CIT_NIKL, CIT_LEE],
  sig_lens=(
    "In the Signature Korean Method, register is the measured distance "
    "of the seal: pressed deep for elders, light for friends, and never "
    "the wrong depth. The drill practices all fifteen distances until "
    "respect signs itself."))

E(key="complex",
  name="Compound and Complex Korean Sentences",
  group="Advanced", ladder_rank=10, ladder_tier="advanced",
  description=(
    "Fifteen long sentences with clauses, connectors, and relative "
    "clauses, parsed and translated. 1. 비가 와서 우산을 쓰고 나갔어요 "
    "(biga waseo usaneul sseugo nagasseoyo, because it rained, I took an "
    "umbrella and went out) - cause -아/어서 + sequence -고. 2. 배가 "
    "고팠지만 시간이 없어서 못 먹었어요 (baega gopatjiman sigani eopseoseo "
    "mot meogeosseoyo, I was hungry but had no time so I could not eat) - "
    "contrast -지만 + cause -아/어서 + inability 못. 3. 친구가 추천한 "
    "영화를 어제 봤는데 정말 재미있었어요 (chinguga chucheonhan yeonghwareul "
    "eoje bwanneunde jeongmal jaemiisseosseoyo, the movie my friend "
    "recommended - I watched it yesterday and it was really fun) - "
    "relative -ㄴ + background -는데. 4. 내일 비가 오면 집에 있을 거예요 "
    "(naeil biga omyeon jibe isseul geoyeyo, if it rains tomorrow I will "
    "stay home) - conditional -면 + future. 5. 열심히 공부해서 시험에 "
    "합격했어요 (yeolsimhi gongbuhaeseo siheome hapgyeokhaesseoyo, I "
    "studied hard and so passed the exam) - cause -아/어서. 6. 돈이 "
    "없어서 버스를 탔어요 (doni eopseoseo beoseureul tasseoyo, having no "
    "money, I took the bus). 7. 밥을 먹으면서 뉴스를 봐요 (babeul "
    "meokmyeonseo nyuseureul bwayo, I watch the news while eating) - "
    "simultaneous -면서. 8. 피곤해도 운동을 해요 (pigonhaedo undongeul "
    "haeyo, even though tired, I exercise) - concessive -아/어도. 9. "
    "한국어를 배우려고 학원에 다녀요 (hangugeoreul baeuryego hagwone "
    "danyeoyo, I attend an academy in order to learn Korean) - purpose "
    "-(으)려고. 10. 너무 바빠서 전화를 못 받았어요 (neomu bappaseo "
    "jeonhwareul mot badasseoyo, I was too busy so I could not answer the "
    "phone). 11. 어제 산 책이 정말 재미있어요 (eoje san chaegi jeongmal "
    "jaemiisseoyo, the book I bought yesterday is really interesting) - "
    "relative -ㄴ. 12. 내일 만날 사람은 김민준 씨예요 (naeil mannal sarameun "
    "Gim Minjun ssiyeyo, the person I will meet tomorrow is Mr. Kim "
    "Minjun) - relative -(으)ㄹ. 13. 지금 먹고 있는 음식은 비빔밥이에요 "
    "(jigeum meokgo inneun eumsigeun bibimbabieyo, the food I am eating "
    "now is bibimbap) - relative -는. 14. 비가 오기 전에 집에 가요 (biga "
    "ogi jeone jibe gayo, I go home before it rains) - -기 전에. 15. 밥을 "
    "먹은 후에 산책해요 (babeul meogeun hue sanchaekhaeyo, after eating I "
    "take a walk) - -(으)ㄴ 후에."),
  how_it_works=(
    "Complex sentences are clause chains: every clause except the last "
    "ends in a connector, and the final verb carries the tense and "
    "politeness for the whole sentence. The connector inventory: -고 "
    "(and/then), -아/어서 (cause, sequence), -지만 (but), -(으)니까 "
    "(cause with command/suggestion), -면 (if), -아/어도 (even if), -면서 "
    "(while), -(으)려고 (in order to), -기 전에 (before), -(으)ㄴ 후에 "
    "(after), -는데 (background). Relative clauses precede the noun with "
    "-는 (present), -(으)ㄴ (past), -(으)ㄹ (future): 먹는 음식, 먹은 음식, "
    "먹을 음식. Quoting embeds with -다고: 간다고 했어요 (said he is "
    "going). Nominalization with -기 turns clauses into nouns: 공부하기가 "
    "어려워요 (studying is hard). The parse order for learners: find the "
    "final verb, then cut at each connector - each cut is one clause to "
    "translate."),
  key_points=[
    "Clause chains: every non-final clause ends in a connector; the final verb carries tense.",
    "Connector inventory: -고, -아/어서, -지만, -면, -아/어도, -면서, -(으)려고, -기 전에, -(으)ㄴ 후에, -는데.",
    "Relative clauses precede nouns: -는 / -(으)ㄴ / -(으)ㄹ.",
    "Quoting with -다고; nominalization with -기.",
    "15 long sentences, each parsed and translated."],
  requirements=[
    "15 long sentences with clauses, connectors, relative clauses.",
    "Each sentence parsed (connector inventory) and translated.",
    "Teach the relative-clause triple -는/-(으)ㄴ/-(으)ㄹ.",
    "Cover quoting and nominalization.",
    "All sentences with Hangul, romanization, English."],
  standards=[CIT_SOHN, CIT_LEE, CIT_NIKL],
  citations=[CIT_SOHN, CIT_LEE, CIT_NIKL],
  sig_lens=(
    "In the Signature Korean Method, the complex sentence is the "
    "great seal: clauses chained in order, each connector a link, the "
    "final verb the press that sets them all. The drill parses fifteen "
    "great seals until structure signs itself."))

E(key="market",
  name="Korean Conversation: At the Market",
  group="Advanced", ladder_rank=10, ladder_tier="advanced",
  description=(
    "A 20-line bilingual dialogue at a traditional market, annotated. "
    "Seller (S), Buyer (B). 1. S: 어서 오세요 (eoseo oseyo, welcome). 2. "
    "B: 안녕하세요 (annyeonghaseyo, hello). 3. S: 뭐 찾으세요 (mwo "
    "chajeuseyo, what are you looking for - honorific). 4. B: 사과 얼마예요 "
    "(sagwa eolmayeyo, how much are the apples). 5. S: 한 봉지에 오천 "
    "원이에요 (han bongjie ocheon wonieyo, 5,000 won a bag). 6. B: 너무 "
    "비싸요 (neomu bissayo, too expensive). 7. S: 맛있는 사과예요 (masinneun "
    "sagwayeyo, they are delicious apples). 8. B: 맛 좀 봐도 돼요 (mat jom "
    "bwado dwaeyo, may I taste one). 9. S: 네, 드셔 보세요 (ne, deusyeo "
    "boseyo, yes, please try - honorific). 10. B: 정말 맛있네요 (jeongmal "
    "masinneyo, really delicious - exclamatory). 11. B: 두 "
    "봉지 주세요 (du bongji juseyo, two bags please). 12. S: 만 원입니다 "
    "(man wonimnida, 10,000 won). 13. B: 팔천 원에 주세요 (palcheon wone "
    "juseyo, please give it for 8,000). 14. S: 안 돼요, 구천 원에 드릴게요 "
    "(an dwaeyo, gucheon wone deurilgeyo, no can do, I will give it for "
    "9,000 - humble 드리다). 15. B: 좋아요, 구천 원에 주세요 (joayo, "
    "gucheon wone juseyo, fine, for 9,000 please). 16. S: 카드 돼요 "
    "(kadeu dwaeyo... buyer asks) B: 카드 돼요 (kadeu dwaeyo, do you take "
    "card). 17. S: 네, 돼요 (ne, dwaeyo, yes we do). 18. S: 봉투에 넣어 "
    "드릴게요 (bongtue neoheo deurilgeyo, I will bag it for you - "
    "humble). 19. B: 감사합니다 (gamsahamnida, thank you). 20. S: 또 "
    "오세요 (tto oseyo, come again). Annotations: the seller uses "
    "honorific verbs (찾으세요, 드셔 보세요, 드릴게요) to elevate the "
    "buyer; the buyer bargains in plain 해요체; 맛 좀 봐도 돼요 uses the "
    "~아/어 보다 'try' construction; the final price settles by splitting "
    "the difference - the standard market dance."),
  how_it_works=(
    "Market dialogue runs on four moves: greeting ritual (어서 오세요 / "
    "안녕하세요), price discovery (얼마예요 -> Sino number + 원), "
    "bargaining (비싸요 -> 깎아 주세요 -> counter-offer with 드릴게요), "
    "and closing (payment method -> bagging -> thanks -> 또 오세요). "
    "Honorific direction is one-way: the seller elevates the buyer "
    "(찾으세요, 드세요), the buyer stays in 해요체. The humble verb 드리다 "
    "replaces 주다 whenever the seller gives to the buyer: 드릴게요. "
    "Tasting uses the permission frame ~아/어 봐도 돼요. Learners should "
    "memorize the four moves in order - real markets follow this script "
    "with almost no variation - and practice the bargaining line until it "
    "sounds cheerful, never aggressive."),
  key_points=[
    "20-line bilingual dialogue with speaker labels and annotations.",
    "Four moves: greeting, price, bargaining, closing - a fixed script.",
    "One-way honorifics: seller elevates buyer with 찾으세요/드릴게요.",
    "Bargaining splits the difference; tasting uses ~아/어 봐도 돼요.",
    "Every line with Hangul, romanization, English."],
  requirements=[
    "A 20-line bilingual dialogue (Korean + English), annotated.",
    "Speaker labels for seller and buyer.",
    "Annotate honorific direction and the bargaining moves.",
    "Teach the tasting and payment frames.",
    "All lines with Hangul, romanization, English."],
  standards=[CIT_NIKL, CIT_TOPIK, CIT_SOHN],
  citations=[CIT_NIKL, CIT_TOPIK, CIT_SOHN],
  sig_lens=(
    "In the Signature Korean Method, the market dialogue is the exchange "
    "of seals in public: price asked, worth weighed, bargain sealed with "
    "a smile. The drill plays both parts until the dance signs itself."))

E(key="friendconv",
  name="Korean Conversation: Meeting a Friend",
  group="Advanced", ladder_rank=10, ladder_tier="advanced",
  description=(
    "A 20-line bilingual dialogue between friends, annotated. Minjun (M), "
    "Sara (S). 1. M: 오랜만이야 (oraenmaniya, long time no see - "
    "informal). 2. S: 정말 오랜만이다 (jeongmal oraenmanida, really long "
    "time). 3. M: 잘 지냈어 (jal jinaesseo, have you been well). 4. S: 응, "
    "너는 (eung, neoneun, yeah, and you). 5. M: 나도 잘 지냈어 (nado jal "
    "jinaesseo, me too). 6. S: 요즘 뭐 해 (yojeum mwo hae, what are you up "
    "to these days). 7. M: 한국어 공부해 (hangugeo gongbuhae, studying "
    "Korean). 8. S: 우와, 발음이 좋아졌네 (uwa, bareumi joajyeonne, wow, "
    "your pronunciation improved - exclamatory 네). 9. M: 고마워, 열심히 "
    "했어 (gomawo, yeolsimhi haesseo, thanks, I worked hard). 10. S: 밥 "
    "먹었어 (bap meogeosseo, did you eat). 11. M: 아직, 같이 먹을래 (ajik, "
    "gachi meogeullae, not yet, want to eat together). 12. S: 좋아, 뭐 "
    "먹을래 (joa, mwo meogeullae, good, what do you want). 13. M: 비빔밥 "
    "어때 (bibimbap eottae, how about bibimbap). 14. S: 좋아, 가자 (joa, "
    "gaja, good, let's go). 15. M: 저 식당 알아 (jeo sikdang ara, I know "
    "that restaurant). 16. S: 얼마나 걸려 (eolmana geollyeo, how long does "
    "it take). 17. M: 십 분쯤 걸려 (sip bunjjeum geollyeo, about ten "
    "minutes). 18. S: 그럼 걷자 (geureom geotja, then let's walk). 19. M: "
    "그래, 날씨도 좋아 (geurae, nalssido joa, yeah, the weather is nice "
    "too). 20. S: 다음에는 내 차례야 (daeumeneun nae charyeya, next time "
    "it is my turn - to treat). Annotations: close friends use 해체 "
    "throughout - no 요 endings; 오랜만이야 opens reunions; 뭐 해 replaces "
    "formal questions; ~ㄹ래 proposals (먹을래) and 자 suggestions (걷자, "
    "가자) drive plans; the treat-turn (차례) closes the social "
    "account."),
  how_it_works=(
    "Friend dialogue runs in 해체: every verb ends in the bare intimate "
    "form (지냈어, 먹었어, 가자), pronouns go informal (너, 나), and "
    "sentence-final particles carry feeling - 네 for exclamation "
    "(좋아졌네), 지 for shared knowledge, 잖아 for 'as you know'. The "
    "reunion script: greeting (오랜만이야), wellbeing exchange (잘 지냈어), "
    "catch-up question (요즘 뭐 해), proposal (~ㄹ래), plan (가자/걷자), "
    "and the treat-turn promise (다음에는 내 차례야). Learners must not "
    "import 해체 into non-intimate relationships - the dialogue is "
    "marked informal throughout, and the annotation flags every line that "
    "would offend a stranger. Practice by shadowing both roles aloud."),
  key_points=[
    "20-line bilingual dialogue, fully informal 해체, annotated.",
    "Reunion script: greeting, wellbeing, catch-up, proposal, plan, treat-turn.",
    "~ㄹ래 proposals and 자 suggestions drive friend plans.",
    "Sentence-final particles 네/지/잖아 carry feeling.",
    "Explicit warning: never use 해체 upward or with strangers."],
  requirements=[
    "A 20-line bilingual dialogue (Korean + English), annotated.",
    "Consistent informal register with speaker labels.",
    "Annotate the reunion script and proposal forms.",
    "Warn against upward use of informal speech.",
    "All lines with Hangul, romanization, English."],
  standards=[CIT_NIKL, CIT_SOHN, CIT_TOPIK],
  citations=[CIT_NIKL, CIT_SOHN, CIT_TOPIK],
  sig_lens=(
    "In the Signature Korean Method, the friend dialogue is the seal "
    "among equals: no distance measured, every line signed plainly. The "
    "drill plays both friends until ease signs itself - and learns "
    "exactly where ease must stop."))

E(key="problemconv",
  name="Korean Conversation: Solving a Problem",
  group="Advanced", ladder_rank=10, ladder_tier="advanced",
  description=(
    "A 20-line bilingual dialogue solving a lost-wallet problem, "
    "annotated. Jiwon (J), Officer (O). 1. J: 실례합니다 (sillyehamnida, "
    "excuse me). 2. O: 네, 말씀하세요 (ne, malsseumhaseyo, yes, please "
    "speak - honorific). 3. J: 지갑을 잃어버렸어요 (jigabeul "
    "ireobeoryeosseoyo, I lost my wallet). 4. O: 언제 잃어버리셨어요 "
    "(eonje ireobeorisyeosseoyo, when did you lose it - honorific). 5. J: "
    "오늘 아침에 잃어버린 것 같아요 (oneul achime ireobeorin geot gatayo, "
    "I think I lost it this morning). 6. O: 어디에서 잃어버리셨어요 "
    "(eodieseo ireobeorisyeosseoyo, where did you lose it). 7. J: "
    "지하철에서 내릴 때인 것 같아요 (jihacheoreseo naeril ttaein geot "
    "gatayo, I think when getting off the subway). 8. O: 몇 호선이에요 "
    "(myeot hoseoniyeyo, which line). 9. J: 2호선이에요 (ihoseoniyeyo, "
    "line 2). 10. O: 지갑에 뭐가 들어 있었어요 (jigabe mweoga deureo "
    "isseosseoyo, what was in the wallet). 11. J: 현금하고 카드가 있었어요 "
    "(hyeongeumhago kadeuga isseosseoyo, there was cash and cards). 12. O: "
    "신분증도 있었어요 (sinbunjeungdo isseosseoyo, was there ID too). 13. "
    "J: 네, 있었어요 (ne, isseosseoyo, yes there was). 14. O: 분실 신고를 "
    "할게요 (bunsil singoreul halgeyo, I will file a loss report). 15. J: "
    "감사합니다 (gamsahamnida, thank you). 16. O: 연락처를 알려 주세요 "
    "(yeollakcheoreul allyeo juseyo, please give me your contact). 17. J: "
    "010-1234-5678이에요 (gongil공... 010-1234-5678이에요, it is "
    "010-1234-5678). 18. O: 찾으면 연락드리겠습니다 (chajeumyeon "
    "yeollakdeurigetsseumnida, if found I will contact you - humble). 19. "
    "J: 정말 감사합니다 (jeongmal gamsahamnida, thank you so much). 20. O: "
    "조심히 가세요 (josimhi gaseyo, get home safely). Annotations: the "
    "officer uses honorific verbs (잃어버리셨어요) and humble forms "
    "(연락드리겠습니다); uncertainty is softened with ~ㄴ 것 같아요; the "
    "problem script runs report -> details -> action -> contact -> "
    "thanks; phone digits use 공 for zero and Sino-Korean numbers."),
  how_it_works=(
    "Problem-solving dialogue is a formal information exchange. The "
    "official asks with honorific interrogatives (잃어버리셨어요, 어디에서), "
    "the citizen answers in 해요체 with softened uncertainty (~ㄴ 것 "
    "같아요, 'it seems'). The script: state the problem (잃어버렸어요), "
    "establish when/where (언제/어디에서), inventory the loss (뭐가 들어 "
    "있었어요), take action (신고할게요), exchange contact (알려 주세요), "
    "close with thanks and safety wishes. Key grammar: -아/어버리다 marks "
    "regrettable completion (잃어버리다, to end up losing); -으면 for the "
    "official's conditional promise (찾으면 연락드리겠습니다). Learners "
    "should memorize the problem script cold - emergencies leave no time "
    "to conjugate from scratch."),
  key_points=[
    "20-line bilingual dialogue with officer honorifics, annotated.",
    "Problem script: report, when/where, inventory, action, contact, thanks.",
    "Uncertainty softened with ~ㄴ 것 같아요.",
    "-아/어버리다 marks regrettable completion; -으면 the official's promise.",
    "Phone digits: 공 for zero, Sino-Korean numbers."],
  requirements=[
    "A 20-line bilingual dialogue (Korean + English), annotated.",
    "Honorific officer speech vs polite citizen speech.",
    "Teach the problem-solving script in order.",
    "Explain -아/어버리다 and ~ㄴ 것 같아요.",
    "All lines with Hangul, romanization, English."],
  standards=[CIT_NIKL, CIT_TOPIK, CIT_SOHN],
  citations=[CIT_NIKL, CIT_TOPIK, CIT_SOHN],
  sig_lens=(
    "In the Signature Korean Method, the problem dialogue is the seal "
    "under pressure: facts stated plainly, uncertainty signed softly, "
    "help requested with both hands. The drill solves the lost wallet "
    "until composure signs itself."))

E(key="mastery",
  name="Korean Mastery Review and Full Reference",
  group="Advanced", ladder_rank=10, ladder_tier="advanced",
  description=(
    "The whole database in one teaching summary. ALPHABET: 14 basic "
    "consonants ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎ (giyeok, nieun, digeut, rieul, "
    "mieum, bieup, siot, ieung, jieut, chieut, kieuk, tieut, pieup, hieut); "
    "10 basic vowels ㅏㅑㅓㅕㅗㅛㅜㅠㅡㅣ (a, ya, eo, yeo, o, yo, u, yu, "
    "eu, i); 5 tense doubles ㄲㄸㅃㅆㅉ; 11 compound vowels ㅐㅒㅔㅖㅘㅙㅚㅝㅞㅟㅢ. "
    "Syllable blocks: initial + vowel + optional batchim; silent ㅇ "
    "placeholder. 200 CORE WORDS (Hangul - romanization - English): 사람 "
    "saram person, 집 jip house, 물 mul water, 밥 bap rice/meal, 학교 "
    "hakgyo school, 선생님 seonsaengnim teacher, 친구 chingu friend, 가족 "
    "gajok family, 시간 sigan time, 돈 don money, 음식 eumsik food, 차 cha "
    "tea/car, 책 chaek book, 컴퓨터 keompyuteo computer, 전화 jeonhwa "
    "phone, 나라 nara country, 도시 dosi city, 길 gil road, 하늘 haneul "
    "sky, 바다 bada sea, 산 san mountain, 나무 namu tree, 꽃 kkot flower, "
    "개 gae dog, 고양이 goyangi cat, 가다 gada go, 오다 oda come, 먹다 "
    "meokda eat, 마시다 masida drink, 보다 boda see, 듣다 deutda listen, "
    "말하다 malhada speak, 읽다 ikda read, 쓰다 sseuda write, 배우다 baeuda "
    "learn, 가르치다 gareuchida teach, 일하다 ilhada work, 공부하다 "
    "gongbuhada study, 자다 jada sleep, 일어나다 ireonada wake up, 앉다 "
    "anjda sit, 서다 seoda stand, 걷다 geotda walk, 뛰다 ttwida run, 사다 "
    "sada buy, 팔다 palda sell, 주다 juda give, 받다 batda receive, 만들다 "
    "mandeulda make, 돕다 dopda help, 크다 keuda big, 작다 jakda small, "
    "좋다 jota good, 나쁘다 nappeuda bad, 많다 manta many, 적다 jeokda few, "
    "빠르다 ppareuda fast, 느리다 neurida slow, 높다 nopda high, 낮다 natda "
    "low, 길다 gilda long, 짧다 jjalda short, 넓다 neolda wide, 좁다 jopda "
    "narrow, 무겁다 mugeopda heavy, 가볍다 gabyeopda light, 뜨겁다 tteugeopda "
    "hot, 차갑다 chagapda cold, 맛있다 masitda delicious, 재미있다 jaemiitda "
    "fun, 어렵다 eoryeopda difficult, 쉽다 swipda easy, 바쁘다 bappeuda "
    "busy, 예쁘다 yeppeuda pretty, 행복하다 haengbokhada happy, 나 na I "
    "(informal), 저 jeo I (humble), 너 neo you (informal), 우리 uri we, "
    "그 geu he, 그녀 geunyeo she, 이것 igeot this, 그것 geugeot that, 저것 "
    "jeogeot that over there, 여기 yeogi here, 거기 geogi there, 저기 "
    "jeogi over there, 누구 nugu who, 무엇 mueot what, 어디 eodi where, "
    "언제 eonje when, 왜 wae why, 어떻게 eotteoke how, 얼마 eolma how "
    "much, 하나 hana one, 둘 dul two, 셋 set three, 넷 net four, 다섯 daseot "
    "five, 여섯 yeoseot six, 일곱 ilgop seven, 여덟 yeodeol eight, 아홉 ahop "
    "nine, 열 yeol ten, 일 il one (Sino), 이 i two (Sino), 삼 sam three "
    "(Sino), 사 sa four (Sino), 오 o five (Sino), 육 yuk six (Sino), 칠 chil "
    "seven (Sino), 팔 pal eight (Sino), 구 gu nine (Sino), 십 sip ten "
    "(Sino), 월요일 woryoil Monday, 화요일 hwayoil Tuesday, 수요일 suy oil "
    "Wednesday, 목요일 mogyoil Thursday, 금요일 geumyoil Friday, 토요일 "
    "toyoil Saturday, 일요일 iryoil Sunday, 봄 bom spring, 여름 yeoreum "
    "summer, 가을 gaeul autumn, 겨울 gyeoul winter, 아버지 abeoji father, "
    "어머니 eomeoni mother, 형 hyeong older brother (male speaker), 오빠 "
    "oppa older brother (female speaker), 누나 nuna older sister (male "
    "speaker), 언니 eonni older sister (female speaker), 동생 dongsaeng "
    "younger sibling, 할아버지 harabeoji grandfather, 할머니 halmeoni "
    "grandmother, 머리 meori head, 눈 nun eye, 코 ko nose, 입 ip mouth, 귀 "
    "gwi ear, 손 son hand, 발 bal foot, 병원 byeongwon hospital, 약 yak "
    "medicine, 약국 yakguk pharmacy, 시장 sijang market, 가격 gagyeok "
    "price, 식당 sikdang restaurant, 메뉴 menyu menu, 지하철 jihacheol "
    "subway, 버스 beoseu bus, 택시 taeksi taxi, 기차 gicha train, 비행기 "
    "bihaenggi airplane, 표 pyo ticket, 역 yeok station, 호텔 hotel hotel, "
    "회사 hoesa company, 회의 hoeui meeting, 수업 sueop class, 숙제 sukje "
    "homework, 시험 siheom exam, 비 bi rain, 눈 nun snow, 바람 baram wind, "
    "날씨 nalssi weather, 새 sae bird, 물고기 mulgogi fish, 스마트폰 "
    "seumateupon smartphone, 문자 munja text message, 사진 sajin photo, "
    "인터넷 inteonet internet, 이메일 imeil email, 컴퓨터 keompyuteo "
    "computer, 안녕하세요 annyeonghaseyo hello, 감사합니다 gamsahamnida "
    "thank you, 죄송합니다 joesonghamnida sorry, 네 ne yes, 아니요 aniyo "
    "no, 아주 aju very, 정말 jeongmal really, 잘 jal well, 빨리 ppalli "
    "quickly, 항상 hangsang always, 같이 gachi together, 사랑 sarang love, "
    "행복 haengbok happiness, 걱정 geokjeong worry, 희망 huimang hope, "
    "오늘 oneul today, 내일 naeil tomorrow, 어제 eoje yesterday, 지금 "
    "jigeum now, 여기 yeogi here. KEY GRAMMAR: SOV order, verb last; "
    "particles 이/가 subject, 을/를 object, 은/는 topic, 에/에서 location, "
    "에게 to person, 의 possessive; no articles, no gender; counters with "
    "numbers; negation 안/지 않다, inability 못; questions in situ or "
    "rising intonation; speech levels 합쇼체/해요체/해체; honorifics for "
    "elders; present 아/어/여요, past 았/었어요, future (으)ㄹ 거예요/겠어요; "
    "connectors -고 -아/어서 -지만 -면 -아/어도 -면서 -(으)려고; relative "
    "-는/-(으)ㄴ/-(으)ㄹ. PHRASE TABLES: greetings (안녕하세요, 감사합니다, "
    "죄송합니다, 식사하셨어요, 수고하셨습니다); restaurant (주세요, 얼마예요, "
    "계산서 주세요, 잘 먹었습니다); directions (어디예요, 어떻게 가요, "
    "얼마나 걸려요); market (얼마예요, 깎아 주세요, 카드 돼요); emergency "
    "(도와주세요, 병원, 아파요). Study order: records 1-10 foundations, "
    "11-23 compounded, 24-34 advanced; three-pass reading for stories; "
    "daily drills: 10 flashcards, 5 conjugations, 1 dialogue shadowing."),
  how_it_works=(
    "Use this record as the daily dashboard. Start each session by "
    "reading the alphabet table aloud, then drill one row of the 200 "
    "words with flashcards (Korean side first, then English side). Pick "
    "one grammar rule and write five new sentences with it. Shadow one "
    "dialogue: play the Korean lines aloud, pause, translate, continue. "
    "Weekly: retell one story from memory; monthly: re-read all three "
    "stories and both market and friend dialogues without the English. "
    "The ladder is the curriculum - do not skip foundations even if "
    "compounded looks more fun, because every advanced record assumes "
    "the particles, endings, and honorifics of the first ten. When a "
    "sentence fails, diagnose by layer: wrong particle, wrong ending, "
    "wrong level - in that order. The database's generator can produce "
    "fresh practice sentences on any topic; the archive records remain "
    "the authoritative examples."),
  key_points=[
    "Full alphabet table with letter names and romanization.",
    "200 core words: Hangul, romanization, English.",
    "Key grammar condensed: particles, negation, questions, levels, tenses, connectors.",
    "Phrase tables: greetings, restaurant, directions, market, emergency.",
    "A daily/weekly/monthly study order using the ladder."],
  requirements=[
    "Consolidated quick-reference of the whole database.",
    "Alphabet, 200 core words, key grammar, all phrase tables.",
    "A usable study order and diagnostic method.",
    "Every word with Hangul, romanization, English.",
    "Generator note: archive records are authoritative."],
  standards=[CIT_ISO, CIT_RR, CIT_TOPIK],
  citations=[CIT_ISO, CIT_RR, CIT_TOPIK],
  sig_lens=(
    "In the Signature Korean Method, the mastery review is the complete "
    "seal-book: every mark learned, every distance measured, every story "
    "told. Keep it open on the desk; a seal-book is for daily use, not "
    "for the shelf."))
