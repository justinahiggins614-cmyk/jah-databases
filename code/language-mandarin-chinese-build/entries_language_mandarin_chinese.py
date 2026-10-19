#!/usr/bin/env python3
"""Entries for The Mandarin Chinese to English Database (language-mandarin-chinese).

Manon's language orders #10-11, 2026-10-17, roster rank 1.
Slug `language-mandarin-chinese` is roster-verified free; id_prefixes
JAH-LCMN- (public) and JAH-LCMNS- (signature) verified free in the manifest
id_prefix values and across every shard index file (zero hits) 2026-10-17.

34 ladder-ordered records each (public-harvest: real, fact-checked Mandarin
teaching - simplified characters, standard Hanyu Pinyin with tone marks,
English on every line; signature-generated-completion labeled where gaps
are filled by construction, never passed off as authentic public record).

Teaching ladder (ranks 1-10, non-decreasing):
  Foundations  - records 1-9   (ranks 1-5): overview, writing, phonology,
                 core nouns, core verbs, adjectives/adverbs, pronouns,
                 numbers/time, greetings
  Compounded   - records 10-23 (ranks 6-9): grammar essentials, 10 themed
                 sentence sets, aspect/tense, Q&A, commands, descriptions
  Advanced     - records 24-34 (ranks 9-10): descriptions, 3 stories,
                 idioms, registers, complex sentences, 3 dialogues, mastery

Public record source facts (fact-checked 2026-10-17):
  Mandarin Chinese (Zhongwen / Putonghua / Huayu / Guoyu), ISO 639-1 zh,
  ISO 639-3 cmn, Sino-Tibetan family, Sinitic branch, ~929M native
  speakers, ~1.1B+ total speakers; official in China, Taiwan, Singapore;
  one of six UN official languages. Standard Mandarin is based on the
  Beijing dialect. Hanyu Pinyin romanization (ISO 7098:2015). Four lexical
  tones plus neutral tone. Simplified characters standard in mainland
  China and Singapore; traditional in Taiwan, Hong Kong, Macau.

Numerical cores: all hand-set 2026-10-17, machine-verified by the demos
(see demos_language_mandarin_chinese.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

Never the words "bat belt" anywhere. No website references. No Facebook.
No religious talk. Nothing hate-adjacent, profane, or inappropriate.
"""

SIG_TAIL = ("Signature original - his original Signature Language Method: "
            "every character a stamped seal of meaning, every tone a "
            "signature pitch-line, every sentence signed by the learner. "
            "Stamp the sound, seal the character, sign the sentence. "
            "Clearly labeled Signature-made, never presented as authentic "
            "public record.")

CIT_YIP = ("Yip P-C, Rimmington D. Chinese: A Comprehensive Grammar. "
           "2nd ed. Routledge; 2015.")
CIT_LI = ("Li CN, Thompson SA. Mandarin Chinese: A Functional Reference "
          "Grammar. University of California Press; 1989.")
CIT_ISO7098 = ("ISO 7098:2015. Information and documentation - Romanization "
               "of Chinese.")
CIT_NORMAN = ("Norman J. Chinese. Cambridge University Press; 1988.")
CIT_HSK = ("Chinese Proficiency Test (HSK) syllabus, levels 1-6 "
           "vocabulary lists; Hanban/Chinese Testing International.")
CIT_PSC = ("Putonghua Shuiping Ceshi (PSC) - Putonghua proficiency test "
           "syllabus; State Language Commission of China.")
CIT_GB18030 = ("GB 18030-2022. Information technology - Chinese coded "
               "character set.")

# ------------------------------------------------------------------ data
# Shared source data: entries AND demos read from these same constants,
# so entry text and demo outputs always agree (cross-check by construction).

# (characters, pinyin, english, example_chars, example_pinyin, example_english)
NOUNS = [
    ("人", "rén", "person", "他是好人。", "Tā shì hǎorén.", "He is a good person."),
    ("男人", "nánrén", "man", "那个男人是医生。", "Nàge nánrén shì yīshēng.", "That man is a doctor."),
    ("女人", "nǚrén", "woman", "这位女人是老师。", "Zhè wèi nǚrén shì lǎoshī.", "This woman is a teacher."),
    ("孩子", "háizi", "child", "孩子们在公园玩。", "Háizimen zài gōngyuán wán.", "The children are playing in the park."),
    ("朋友", "péngyou", "friend", "他是我的好朋友。", "Tā shì wǒ de hǎo péngyou.", "He is my good friend."),
    ("老师", "lǎoshī", "teacher", "老师教我们中文。", "Lǎoshī jiāo wǒmen Zhōngwén.", "The teacher teaches us Chinese."),
    ("学生", "xuésheng", "student", "我是学生。", "Wǒ shì xuésheng.", "I am a student."),
    ("医生", "yīshēng", "doctor", "医生在医院工作。", "Yīshēng zài yīyuàn gōngzuò.", "The doctor works at the hospital."),
    ("家庭", "jiātíng", "family", "我的家庭很幸福。", "Wǒ de jiātíng hěn xìngfú.", "My family is very happy."),
    ("狗", "gǒu", "dog", "这只狗很可爱。", "Zhè zhī gǒu hěn kěài.", "This dog is very cute."),
    ("猫", "māo", "cat", "猫喜欢睡觉。", "Māo xǐhuan shuìjiào.", "Cats like to sleep."),
    ("水", "shuǐ", "water", "我要喝水。", "Wǒ yào hē shuǐ.", "I want to drink water."),
    ("米饭", "mǐfàn", "rice", "中国人爱吃米饭。", "Zhōngguó rén ài chī mǐfàn.", "Chinese people love to eat rice."),
    ("苹果", "píngguǒ", "apple", "这个苹果很甜。", "Zhège píngguǒ hěn tián.", "This apple is very sweet."),
    ("书", "shū", "book", "桌子上有一本书。", "Zhuōzi shang yǒu yì běn shū.", "There is a book on the table."),
    ("笔", "bǐ", "pen", "这支笔是我的。", "Zhè zhī bǐ shì wǒ de.", "This pen is mine."),
    ("桌子", "zhuōzi", "table", "桌子上有电脑。", "Zhuōzi shang yǒu diànnǎo.", "There is a computer on the table."),
    ("椅子", "yǐzi", "chair", "请坐在这把椅子上。", "Qǐng zuò zài zhè bǎ yǐzi shang.", "Please sit on this chair."),
    ("门", "mén", "door", "请把门关上。", "Qǐng bǎ mén guānshang.", "Please close the door."),
    ("车", "chē", "car / vehicle", "他的车很快。", "Tā de chē hěn kuài.", "His car is very fast."),
    ("电话", "diànhuà", "telephone", "我的电话号码是...。", "Wǒ de diànhuà hàomǎ shì...", "My phone number is..."),
    ("电脑", "diànnǎo", "computer", "我在电脑上学习。", "Wǒ zài diànnǎo shang xuéxí.", "I study on the computer."),
    ("城市", "chéngshì", "city", "北京是中国的首都。", "Běijīng shì Zhōngguó de shǒudū.", "Beijing is the capital of China."),
    ("国家", "guójiā", "country", "中国是一个大国。", "Zhōngguó shì yí ge dà guó.", "China is a big country."),
    ("时间", "shíjiān", "time", "时间过得很快。", "Shíjiān guò de hěn kuài.", "Time passes very quickly."),
]

VERBS = [
    ("吃", "chī", "eat", "我吃米饭。", "Wǒ chī mǐfàn.", "I eat rice."),
    ("喝", "hē", "drink", "他喝茶。", "Tā hē chá.", "He drinks tea."),
    ("去", "qù", "go", "我去学校。", "Wǒ qù xuéxiào.", "I go to school."),
    ("来", "lái", "come", "朋友来了。", "Péngyou lái le.", "A friend has come."),
    ("看", "kàn", "look / watch / read", "我看书。", "Wǒ kàn shū.", "I read a book."),
    ("听", "tīng", "listen", "我听音乐。", "Wǒ tīng yīnyuè.", "I listen to music."),
    ("说", "shuō", "speak / say", "他说中文。", "Tā shuō Zhōngwén.", "He speaks Chinese."),
    ("读", "dú", "read aloud", "学生读课文。", "Xuésheng dú kèwén.", "The student reads the text aloud."),
    ("写", "xiě", "write", "我在写信。", "Wǒ zài xiě xìn.", "I am writing a letter."),
    ("学", "xué", "learn", "我学中文。", "Wǒ xué Zhōngwén.", "I am learning Chinese."),
    ("教", "jiāo", "teach", "老师教英文。", "Lǎoshī jiāo Yīngwén.", "The teacher teaches English."),
    ("工作", "gōngzuò", "work", "他在公司工作。", "Tā zài gōngsī gōngzuò.", "He works at a company."),
    ("买", "mǎi", "buy", "我买苹果。", "Wǒ mǎi píngguǒ.", "I buy apples."),
    ("卖", "mài", "sell", "他卖电脑。", "Tā mài diànnǎo.", "He sells computers."),
    ("给", "gěi", "give", "我给你一本书。", "Wǒ gěi nǐ yì běn shū.", "I give you a book."),
    ("拿", "ná", "take / hold", "请拿这支笔。", "Qǐng ná zhè zhī bǐ.", "Please take this pen."),
    ("放", "fàng", "put", "把书放在桌子上。", "Bǎ shū fàng zài zhuōzi shang.", "Put the book on the table."),
    ("开", "kāi", "open / drive / turn on", "请开门。", "Qǐng kāi mén.", "Please open the door."),
    ("关", "guān", "close / turn off", "请关灯。", "Qǐng guān dēng.", "Please turn off the light."),
    ("走", "zǒu", "walk / go", "我们走路去。", "Wǒmen zǒu lù qù.", "We walk there."),
    ("跑", "pǎo", "run", "孩子们在跑步。", "Háizimen zài pǎobù.", "The children are running."),
    ("坐", "zuò", "sit", "请坐。", "Qǐng zuò.", "Please sit down."),
    ("睡", "shuì", "sleep", "孩子睡了。", "Háizi shuì le.", "The child has fallen asleep."),
    ("笑", "xiào", "laugh / smile", "他笑了。", "Tā xiào le.", "He laughed."),
    ("爱", "ài", "love", "我爱我的家庭。", "Wǒ ài wǒ de jiātíng.", "I love my family."),
]

ADJECTIVES = [
    ("大", "dà", "big", "这间房子很大。", "Zhè jiān fángzi hěn dà.", "This house is very big."),
    ("小", "xiǎo", "small", "这只猫很小。", "Zhè zhī māo hěn xiǎo.", "This cat is very small."),
    ("高", "gāo", "tall / high", "他很高。", "Tā hěn gāo.", "He is very tall."),
    ("矮", "ǎi", "short", "这棵树很矮。", "Zhè kē shù hěn ǎi.", "This tree is very short."),
    ("长", "cháng", "long", "这条河很长。", "Zhè tiáo hé hěn cháng.", "This river is very long."),
    ("短", "duǎn", "short", "他的头发很短。", "Tā de tóufa hěn duǎn.", "His hair is very short."),
    ("新", "xīn", "new", "这是我的新书。", "Zhè shì wǒ de xīn shū.", "This is my new book."),
    ("旧", "jiù", "old", "这件衣服很旧。", "Zhè jiàn yīfu hěn jiù.", "This clothing is very old."),
    ("好", "hǎo", "good", "今天天气很好。", "Jīntiān tiānqì hěn hǎo.", "The weather is very good today."),
    ("坏", "huài", "bad", "这个习惯不好。", "Zhège xíguàn bù hǎo.", "This habit is not good."),
    ("快", "kuài", "fast", "这辆车很快。", "Zhè liàng chē hěn kuài.", "This car is very fast."),
    ("慢", "màn", "slow", "他走得很慢。", "Tā zǒu de hěn màn.", "He walks very slowly."),
    ("热", "rè", "hot", "夏天很热。", "Xiàtiān hěn rè.", "Summer is very hot."),
    ("冷", "lěng", "cold", "冬天很冷。", "Dōngtiān hěn lěng.", "Winter is very cold."),
    ("漂亮", "piàoliang", "beautiful", "她很漂亮。", "Tā hěn piàoliang.", "She is very beautiful."),
    ("难", "nán", "difficult", "中文很难吗？", "Zhōngwén hěn nán ma?", "Is Chinese very difficult?"),
    ("容易", "róngyì", "easy", "这个问题很容易。", "Zhège wèntí hěn róngyì.", "This question is very easy."),
    ("贵", "guì", "expensive", "这件衣服很贵。", "Zhè jiàn yīfu hěn guì.", "This clothing is very expensive."),
    ("便宜", "piányi", "cheap", "这里的东西很便宜。", "Zhèlǐ de dōngxi hěn piányi.", "Things here are very cheap."),
    ("多", "duō", "many / much", "人很多。", "Rén hěn duō.", "There are very many people."),
    ("少", "shǎo", "few / little", "时间很少。", "Shíjiān hěn shǎo.", "There is very little time."),
    ("远", "yuǎn", "far", "学校离家很远。", "Xuéxiào lí jiā hěn yuǎn.", "The school is very far from home."),
    ("近", "jìn", "near", "商店离家很近。", "Shāngdiàn lí jiā hěn jìn.", "The shop is very near home."),
    ("开心", "kāixīn", "happy", "我今天很开心。", "Wǒ jīntiān hěn kāixīn.", "I am very happy today."),
    ("忙", "máng", "busy", "他最近很忙。", "Tā zuìjìn hěn máng.", "He has been very busy lately."),
]

ADVERBS = [
    ("很", "hěn", "very", "他很高。", "Tā hěn gāo.", "He is very tall."),
    ("非常", "fēicháng", "extremely", "我非常喜欢。", "Wǒ fēicháng xǐhuan.", "I like it extremely."),
    ("太", "tài", "too", "太贵了。", "Tài guì le.", "It is too expensive."),
    ("都", "dōu", "all", "我们都去。", "Wǒmen dōu qù.", "We are all going."),
    ("也", "yě", "also", "我也去。", "Wǒ yě qù.", "I am going too."),
    ("不", "bù", "not", "我不去。", "Wǒ bú qù.", "I am not going."),
    ("没", "méi", "not (past)", "我没去。", "Wǒ méi qù.", "I did not go."),
    ("只", "zhǐ", "only", "我只买一个。", "Wǒ zhǐ mǎi yí ge.", "I am only buying one."),
    ("已经", "yǐjīng", "already", "他已经走了。", "Tā yǐjīng zǒu le.", "He has already left."),
    ("正在", "zhèngzài", "in progress", "我在正在看书。", "Wǒ zhèngzài kàn shū.", "I am reading a book right now."),
    ("常常", "chángcháng", "often", "他常常跑步。", "Tā chángcháng pǎobù.", "He often runs."),
    ("马上", "mǎshàng", "immediately", "我马上来。", "Wǒ mǎshàng lái.", "I am coming right away."),
    ("一起", "yìqǐ", "together", "我们一起去。", "Wǒmen yìqǐ qù.", "We go together."),
    ("慢慢", "mànman", "slowly", "请慢慢说。", "Qǐng mànman shuō.", "Please speak slowly."),
    ("真", "zhēn", "really", "真好吃！", "Zhēn hǎochī!", "Really delicious!"),
]

GREETINGS = [
    ("你好", "nǐ hǎo", "Hello", "First greeting to learn; neutral and universal."),
    ("您好", "nín hǎo", "Hello (polite)", "Use with elders, officials, and in service settings."),
    ("早上好", "zǎoshang hǎo", "Good morning", "Before about 10 a.m.; 早 alone is casual."),
    ("晚上好", "wǎnshang hǎo", "Good evening", "After dark; common in shops and restaurants."),
    ("再见", "zàijiàn", "Goodbye", "Literally see you again; the standard farewell."),
    ("谢谢", "xièxie", "Thank you", "The single most-used politeness word."),
    ("不客气", "bú kèqi", "You are welcome", "Reply to 谢谢; also means do not stand on ceremony."),
    ("对不起", "duìbuqǐ", "Sorry", "For real apologies; stronger than 不好意思."),
    ("没关系", "méi guānxi", "It does not matter", "Reply to 对不起; releases the other person."),
    ("请", "qǐng", "Please", "Softens any request; 请坐 = please sit."),
    ("请进", "qǐng jìn", "Please come in", "Said at the door when welcoming a guest."),
    ("请坐", "qǐng zuò", "Please sit down", "Said when offering a seat."),
    ("欢迎", "huānyíng", "Welcome", "欢迎光临 = welcome in (to a shop)."),
    ("好久不见", "hǎo jiǔ bú jiàn", "Long time no see", "Warm reunion phrase between friends."),
    ("最近怎么样", "zuìjìn zěnmeyàng", "How have you been lately", "Friendly check-in; answer with 还不错."),
    ("吃了吗", "chī le ma", "Have you eaten", "Classic caring greeting, not a lunch invitation."),
    ("早", "zǎo", "Morning", "Casual short form of 早上好 among colleagues."),
    ("晚安", "wǎn'ān", "Good night", "Said before sleep, not as an evening hello."),
    ("明天见", "míngtiān jiàn", "See you tomorrow", "Parting phrase when meeting again soon."),
    ("祝你生日快乐", "zhù nǐ shēngrì kuàilè", "Happy birthday to you", "Sung and said at birthdays."),
    ("恭喜", "gōngxǐ", "Congratulations", "For weddings, new jobs, New Year: 恭喜发财."),
    ("加油", "jiāyóu", "Keep going / you can do it", "Cheering phrase; literally add oil."),
    ("慢走", "màn zǒu", "Take care going (polite farewell)", "Said by the host as guests leave."),
    ("一路顺风", "yílù shùnfēng", "Have a smooth trip", "Said to someone setting off on a journey."),
    ("保重", "bǎozhòng", "Take care of yourself", "Warm parting, especially for longer separations."),
    ("不好意思", "bù hǎoyìsi", "Excuse me / sorry", "Light apology for small troubles and interruptions."),
    ("劳驾", "láojià", "Excuse me (may I trouble you)", "Polite way to get a stranger's attention."),
    ("请问", "qǐngwèn", "May I ask", "Opens any question to a stranger politely."),
    ("没问题", "méi wèntí", "No problem", "Casual reassurance; service staff use it constantly."),
    ("谢谢你的帮助", "xièxie nǐ de bāngzhù", "Thank you for your help", "Fuller thanks after someone helps you."),
]

# (chars, pinyin, english) x 10 lines each
STORY1 = [
    ("今天是星期天。", "Jīntiān shì xīngqītiān.", "Today is Sunday."),
    ("天气很好。", "Tiānqì hěn hǎo.", "The weather is very nice."),
    ("小明去公园。", "Xiǎo Míng qù gōngyuán.", "Xiaoming goes to the park."),
    ("公园里有很多花。", "Gōngyuán lǐ yǒu hěn duō huā.", "There are many flowers in the park."),
    ("他看见一只小狗。", "Tā kànjiàn yì zhī xiǎo gǒu.", "He sees a little dog."),
    ("小狗很快乐。", "Xiǎo gǒu hěn kuàilè.", "The little dog is very happy."),
    ("小明和朋友一起玩。", "Xiǎo Míng hé péngyou yìqǐ wán.", "Xiaoming plays together with his friend."),
    ("他们吃苹果，喝水。", "Tāmen chī píngguǒ, hē shuǐ.", "They eat apples and drink water."),
    ("下午，他们回家。", "Xiàwǔ, tāmen huí jiā.", "In the afternoon, they go home."),
    ("今天真开心！", "Jīntiān zhēn kāixīn!", "Today is really fun!"),
]

STORY2 = [
    ("昨天下雨了。", "Zuótiān xià yǔ le.", "It rained yesterday."),
    ("小红带了一把伞。", "Xiǎo Hóng dài le yì bǎ sǎn.", "Xiaohong took an umbrella."),
    ("她去了学校。", "Tā qù le xuéxiào.", "She went to school."),
    ("下午，雨停了。", "Xiàwǔ, yǔ tíng le.", "In the afternoon, the rain stopped."),
    ("她忘记了伞。", "Tā wàngjì le sǎn.", "She forgot the umbrella."),
    ("回家以后，她发现伞不见了。", "Huí jiā yǐhòu, tā fāxiàn sǎn bú jiàn le.", "After returning home, she found the umbrella was gone."),
    ("她很快回到学校。", "Tā hěn kuài huí dào xuéxiào.", "She hurried back to school."),
    ("伞还在教室里。", "Sǎn hái zài jiàoshì lǐ.", "The umbrella was still in the classroom."),
    ("她拿起伞笑了。", "Tā ná qǐ sǎn xiào le.", "She picked up the umbrella and smiled."),
    ("从那以后，她再也没有丢过东西。", "Cóng nà yǐhòu, tā zài yě méiyǒu diū guo dōngxi.", "Since then, she has never lost anything again."),
]

STORY3 = [
    ("明天是我的生日。", "Míngtiān shì wǒ de shēngrì.", "Tomorrow is my birthday."),
    ("我会请朋友来我家。", "Wǒ huì qǐng péngyou lái wǒ jiā.", "I will invite friends to my home."),
    ("妈妈会做一个大蛋糕。", "Māma huì zuò yí ge dà dàngāo.", "Mom will make a big cake."),
    ("我们将一起唱歌。", "Wǒmen jiāng yìqǐ chàng gē.", "We will sing together."),
    ("如果下雨，我们就在家里玩。", "Rúguǒ xià yǔ, wǒmen jiù zài jiā lǐ wán.", "If it rains, we will play at home."),
    ("要是天气好，我们就去公园。", "Yàoshi tiānqì hǎo, wǒmen jiù qù gōngyuán.", "If the weather is good, we will go to the park."),
    ("我要给朋友们准备礼物。", "Wǒ yào gěi péngyoumen zhǔnbèi lǐwù.", "I am going to prepare gifts for my friends."),
    ("大家一定会很开心。", "Dàjiā yídìng huì hěn kāixīn.", "Everyone will surely be very happy."),
    ("生日过后，我会写感谢信。", "Shēngrì guò hòu, wǒ huì xiě gǎnxiè xìn.", "After the birthday, I will write thank-you notes."),
    ("明天会是美好的一天！", "Míngtiān huì shì měihǎo de yì tiān!", "Tomorrow will be a wonderful day!"),
]

# (chars, pinyin, literal, meaning, ex_chars, ex_pinyin, ex_english)
IDIOMS = [
    ("一心一意", "yì xīn yí yì", "one heart one mind", "wholeheartedly; with full concentration",
     "他一心一意地学习中文。", "Tā yì xīn yí yì de xuéxí Zhōngwén.", "He studies Chinese wholeheartedly."),
    ("马马虎虎", "mǎma hūhu", "horse horse tiger tiger", "so-so; just passable; careless",
     "他的中文马马虎虎。", "Tā de Zhōngwén mǎma hūhu.", "His Chinese is so-so."),
    ("加油", "jiāyóu", "add oil", "keep going; you can do it (cheering)",
     "考试加油！", "Kǎoshì jiāyóu!", "Do your best on the exam!"),
    ("入乡随俗", "rù xiāng suí sú", "enter village follow customs", "when in Rome, do as the Romans do",
     "入乡随俗，我们也用筷子。", "Rù xiāng suí sú, wǒmen yě yòng kuàizi.", "When in Rome, we use chopsticks too."),
    ("活到老，学到老", "huó dào lǎo, xué dào lǎo", "live till old, learn till old", "never too old to learn",
     "爷爷七十岁还学英语，真是活到老，学到老。", "Yéye qīshí suì hái xué Yīngyǔ, zhēn shì huó dào lǎo, xué dào lǎo.", "Grandpa still learns English at seventy - never too old to learn."),
    ("熟能生巧", "shú néng shēng qiǎo", "skill can produce cleverness", "practice makes perfect",
     "多说多练，熟能生巧。", "Duō shuō duō liàn, shú néng shēng qiǎo.", "Speak and practice more; practice makes perfect."),
    ("井底之蛙", "jǐng dǐ zhī wā", "frog at the bottom of a well", "a person of narrow vision",
     "不要做井底之蛙，要多看看世界。", "Bú yào zuò jǐng dǐ zhī wā, yào duō kànkan shìjiè.", "Do not be a frog in a well; go see more of the world."),
    ("画蛇添足", "huà shé tiān zú", "draw snake add feet", "ruin something by overdoing it",
     "文章已经很好了，不要画蛇添足。", "Wénzhāng yǐjīng hěn hǎo le, bú yào huà shé tiān zú.", "The essay is already good; do not ruin it by overdoing."),
    ("对牛弹琴", "duì niú tán qín", "play the lute to cows", "waste effort on an unappreciative audience",
     "跟他讲道理，真是对牛弹琴。", "Gēn tā jiǎng dàolǐ, zhēn shì duì niú tán qín.", "Reasoning with him is like playing the lute to cows."),
    ("守株待兔", "shǒu zhū dài tù", "guard stump wait for rabbit", "wait idly for luck instead of working",
     "成功不会从天上掉下来，不要守株待兔。", "Chénggōng bú huì cóng tiānshang diào xialai, bú yào shǒu zhū dài tù.", "Success will not fall from the sky; do not wait idly for luck."),
    ("亡羊补牢", "wáng yáng bǔ láo", "lose sheep mend fold", "better late than never; fix after a loss",
     "虽然丢了钱，现在开始存钱就是亡羊补牢。", "Suīrán diū le qián, xiànzài kāishǐ cún qián jiù shì wáng yáng bǔ láo.", "Though money was lost, starting to save now is mending the fold."),
    ("刻舟求剑", "kè zhōu qiú jiàn", "carve boat seek sword", "rigid thinking; clinging to outdated methods",
     "时代变了，刻舟求剑是行不通的。", "Shídài biàn le, kè zhōu qiú jiàn shì xíng butōng de.", "Times have changed; rigid old methods will not work."),
    ("叶公好龙", "Yè Gōng hào lóng", "Lord Ye loves dragons", "claiming to love what one really fears",
     "他说喜欢挑战，遇到困难就跑，真是叶公好龙。", "Tā shuō xǐhuan tiǎozhàn, yùdào kùnnan jiù pǎo, zhēn shì Yè Gōng hào lóng.", "He claims to love challenges but flees difficulty - Lord Ye loving dragons."),
    ("掩耳盗铃", "yǎn ěr dào líng", "cover ears steal bell", "deceive oneself; futile self-deception",
     "不承认错误就是掩耳盗铃。", "Bù chéngrèn cuòwù jiù shì yǎn ěr dào líng.", "Refusing to admit a mistake is deceiving yourself."),
    ("拔苗助长", "bá miáo zhù zhǎng", "pull seedlings help grow", "spoil things by being over-hasty",
     "学习要一步一步来，不能拔苗助长。", "Xuéxí yào yí bù yí bù lái, bù néng bá miáo zhù zhǎng.", "Learning must go step by step; haste spoils it."),
    ("滥竽充数", "làn yú chōng shù", "poor yu-pipe fill numbers", "pass oneself off as competent; make up numbers",
     "他不懂装懂，完全是滥竽充数。", "Tā bù dǒng zhuāng dǒng, wánquán shì làn yú chōng shù.", "He pretends to understand; he is just making up the numbers."),
    ("鹬蚌相争", "yù bàng xiāng zhēng", "snipe and clam fight each other", "two parties fight while a third benefits",
     "他们鹬蚌相争，最后让别人得了好处。", "Tāmen yù bàng xiāng zhēng, zuìhòu ràng biéren dé le hǎochù.", "They fought each other and a third party got the benefit."),
    ("塞翁失马", "Sài Wēng shī mǎ", "old Sai loses a horse", "a blessing in disguise; loss may bring gain",
     "丢了工作却找到了更好的，真是塞翁失马。", "Diū le gōngzuò què zhǎodào le gèng hǎo de, zhēn shì Sài Wēng shī mǎ.", "Losing the job led to a better one - a blessing in disguise."),
    ("破釜沉舟", "pò fǔ chén zhōu", "break cauldrons sink boats", "burn one's bridges; go all in with no retreat",
     "他辞职创业，破釜沉舟，一定要成功。", "Tā cízhí chuàngyè, pò fǔ chén zhōu, yídìng yào chénggōng.", "He quit to start a business, burning his bridges to succeed."),
    ("水滴石穿", "shuǐ dī shí chuān", "water drops pierce stone", "persistence overcomes all; little by little",
     "每天学一点，水滴石穿，中文一定能学好。", "Měitiān xué yì diǎn, shuǐ dī shí chuān, Zhōngwén yídìng néng xué hǎo.", "A little each day - dripping water pierces stone; your Chinese will improve."),
]

# (informal_chars, informal_pinyin, informal_en, formal_chars, formal_pinyin, formal_en, note)
REGISTERS = [
    ("你好", "nǐ hǎo", "hi", "您好", "nín hǎo", "hello (respectful)", "您 replaces 你 for elders, clients, officials."),
    ("谢谢", "xièxie", "thanks", "非常感谢", "fēicháng gǎnxiè", "thank you very much", "非常感谢 fits letters and speeches."),
    ("再见", "zàijiàn", "bye", "慢走", "màn zǒu", "farewell (host to guest)", "Said by the one staying as the other leaves."),
    ("对不起", "duìbuqǐ", "sorry", "非常抱歉", "fēicháng bàoqiàn", "my sincere apologies", "非常抱歉 fits written and business apologies."),
    ("没事", "méi shì", "no worries", "没关系", "méi guānxi", "it does not matter", "没关系 is the safe reply in all settings."),
    ("给我", "gěi wǒ", "give me", "请给我", "qǐng gěi wǒ", "please give me", "Bare imperatives sound rude; add 请."),
    ("过来", "guòlái", "come here", "请过来一下", "qǐng guòlái yíxià", "please come here a moment", "一下 softens any request."),
    ("坐", "zuò", "sit", "请坐", "qǐng zuò", "please be seated", "请坐 is standard hospitality language."),
    ("看这个", "kàn zhège", "look at this", "请看", "qǐng kàn", "please have a look", "Presentations and service use 请看."),
    ("你知道吗", "nǐ zhīdào ma", "do you know", "请问您知道吗", "qǐngwèn nín zhīdào ma", "may I ask if you know", "请问 opens any stranger question."),
    ("我想吃", "wǒ xiǎng chī", "I want to eat", "我想用餐", "wǒ xiǎng yòngcān", "I would like to dine", "用餐 replaces 吃 in formal dining."),
    ("多少钱", "duōshao qián", "how much", "请问价格是多少", "qǐngwèn jiàgé shì duōshao", "may I ask the price", "Full-sentence form suits hotels and offices."),
    ("快点", "kuài diǎn", "hurry up", "麻烦您快一点", "máfan nín kuài yìdiǎn", "please hurry a little", "麻烦您 (trouble you) is the polite pusher."),
    ("不行", "bù xíng", "no way", "恐怕不行", "kǒngpà bù xíng", "I am afraid not", "恐怕 (fear) softens every refusal."),
    ("走了", "zǒu le", "I am off", "我先告辞了", "wǒ xiān gàocí le", "I will take my leave first", "告辞 is the formal exit line."),
]

# (chars, pinyin, english, parse_note)
COMPLEX = [
    ("因为下雨，所以我们没去公园。", "Yīnwèi xià yǔ, suǒyǐ wǒmen méi qù gōngyuán.", "Because it rained, we did not go to the park.", "Paired conjunctions 因为...所以... frame cause and effect; neither can stand comfortably alone."),
    ("虽然他很忙，但是他每天都学习中文。", "Suīrán tā hěn máng, dànshì tā měitiān dōu xuéxí Zhōngwén.", "Although he is very busy, he studies Chinese every day.", "虽然...但是... marks concession; 但是 can drop in casual speech, 虽然 cannot."),
    ("如果你努力，你就会成功。", "Rúguǒ nǐ nǔlì, nǐ jiù huì chénggōng.", "If you work hard, you will succeed.", "如果...就... builds the condition; 就 must sit before the result verb."),
    ("他不但会说中文，而且会写汉字。", "Tā búdàn huì shuō Zhōngwén, érqiě huì xiě Hànzì.", "He not only speaks Chinese but also writes characters.", "不但...而且... adds a stronger second fact; the second clause carries the emphasis."),
    ("既然你来了，就多坐一会儿吧。", "Jìrán nǐ lái le, jiù duō zuò yíhuìr ba.", "Since you have come, sit a while longer.", "既然...就... states a known fact as the reason; softer than 因为."),
    ("无论多难，我都要学会。", "Wúlùn duō nán, wǒ dōu yào xuéhuì.", "No matter how hard, I will master it.", "无论...都... concedes every case; 都 locks the conclusion to all of them."),
    ("只有努力，才能成功。", "Zhǐyǒu nǔlì, cái néng chénggōng.", "Only with hard work can one succeed.", "只有...才... sets the single condition; 才 marks the result as earned."),
    ("他一回家，就开始做饭。", "Tā yì huí jiā, jiù kāishǐ zuò fàn.", "As soon as he got home, he started cooking.", "一...就... compresses two events; the actions feel immediate and linked."),
    ("越学越有意思。", "Yuè xué yuè yǒu yìsi.", "The more you learn, the more interesting it gets.", "越...越... scales two changes together; both verbs stay bare."),
    ("我把作业做完了。", "Wǒ bǎ zuòyè zuò wán le.", "I finished the homework.", "把 moves the object before the verb; the verb needs a result complement like 完."),
    ("我的手机被他拿走了。", "Wǒ de shǒujī bèi tā ná zǒu le.", "My phone was taken away by him.", "被 marks the passive; it usually carries an unhappy outcome."),
    ("我是昨天来的。", "Wǒ shì zuótiān lái de.", "It was yesterday that I came.", "是...的 frames a past detail (time, place, manner); the 的 closes the emphasis."),
    ("你喜欢吃米饭还是面条？", "Nǐ xǐhuan chī mǐfàn háishi miàntiáo?", "Do you like rice or noodles?", "还是 asks an either-or question; 吗 never appears with 还是."),
    ("他去哪儿了呢？", "Tā qù nǎr le ne?", "Where could he have gone?", "呢 stretches a question with wondering; it softens interrogatives and follows new topics."),
    ("这本书我看过三遍了，每一遍都有新的收获。", "Zhè běn shū wǒ kàn guo sān biàn le, měi yí biàn dōu yǒu xīn de shōuhuò.", "I have read this book three times, and each time brought something new.", "过 marks experience; 三遍 counts it; the second clause comments with 每...都...."),
]

# 200 core words: (chars, pinyin, english). Demo asserts exactly 200.
CORE200_A = [
    ("的", "de", "possessive particle"), ("了", "le", "completed-action particle"),
    ("是", "shì", "to be"), ("在", "zài", "at / in / -ing"),
    ("有", "yǒu", "to have"), ("和", "hé", "and"),
    ("我", "wǒ", "I"), ("你", "nǐ", "you"),
    ("他", "tā", "he"), ("她", "tā", "she"),
    ("这", "zhè", "this"), ("那", "nà", "that"),
    ("个", "ge", "measure word"), ("上", "shàng", "on / up"),
    ("下", "xià", "under / down"), ("大", "dà", "big"),
    ("小", "xiǎo", "small"), ("中", "zhōng", "middle"),
    ("国", "guó", "country"), ("人", "rén", "person"),
]
CORE200_B = [
    ("年", "nián", "year"), ("月", "yuè", "month"), ("日", "rì", "day"),
    ("时", "shí", "hour"), ("分", "fēn", "minute"), ("好", "hǎo", "good"),
    ("不", "bù", "not"), ("没", "méi", "not (past)"),
    ("很", "hěn", "very"), ("都", "dōu", "all"),
    ("也", "yě", "also"), ("就", "jiù", "then / just"),
    ("才", "cái", "only then"), ("再", "zài", "again"),
    ("每", "měi", "every"), ("各", "gè", "each"),
    ("些", "xiē", "some"), ("种", "zhǒng", "kind"),
    ("样", "yàng", "manner"), ("里", "lǐ", "inside"),
]
CORE200_C = [
    ("外", "wài", "outside"), ("前", "qián", "front / before"), ("后", "hòu", "back / after"),
    ("左", "zuǒ", "left"), ("右", "yòu", "right"), ("东", "dōng", "east"),
    ("西", "xī", "west"), ("南", "nán", "south"), ("北", "běi", "north"),
    ("家", "jiā", "home / family"), ("学校", "xuéxiào", "school"), ("公司", "gōngsī", "company"),
    ("商店", "shāngdiàn", "shop"), ("医院", "yīyuàn", "hospital"), ("银行", "yínháng", "bank"),
    ("饭馆", "fànguǎn", "restaurant"), ("公园", "gōngyuán", "park"), ("车站", "chēzhàn", "station"),
    ("机场", "jīchǎng", "airport"), ("衣服", "yīfu", "clothes"),
]
CORE200_D = [
    ("鞋", "xié", "shoes"), ("钱", "qián", "money"), ("手机", "shǒujī", "mobile phone"),
    ("电视", "diànshì", "TV"), ("电影", "diànyǐng", "movie"), ("音乐", "yīnyuè", "music"),
    ("照片", "zhàopiàn", "photo"), ("信", "xìn", "letter"), ("报纸", "bàozhǐ", "newspaper"),
    ("菜单", "càidān", "menu"), ("钥匙", "yàoshi", "key"), ("包", "bāo", "bag"),
    ("伞", "sǎn", "umbrella"), ("杯子", "bēizi", "cup"), ("碗", "wǎn", "bowl"),
    ("筷子", "kuàizi", "chopsticks"), ("牛奶", "niúnǎi", "milk"), ("茶", "chá", "tea"),
    ("咖啡", "kāfēi", "coffee"), ("果汁", "guǒzhī", "juice"),
]
CORE200_E = [
    ("米", "mǐ", "rice (grain)"), ("面", "miàn", "noodles / flour"), ("肉", "ròu", "meat"),
    ("鱼", "yú", "fish"), ("鸡蛋", "jīdàn", "egg"), ("蔬菜", "shūcài", "vegetables"),
    ("水果", "shuǐguǒ", "fruit"), ("糖", "táng", "sugar"), ("盐", "yán", "salt"),
    ("早饭", "zǎofàn", "breakfast"), ("午饭", "wǔfàn", "lunch"), ("晚饭", "wǎnfàn", "dinner"),
    ("爸爸", "bàba", "dad"), ("妈妈", "māma", "mom"), ("哥哥", "gēge", "older brother"),
    ("姐姐", "jiějie", "older sister"), ("弟弟", "dìdi", "younger brother"), ("妹妹", "mèimei", "younger sister"),
    ("儿子", "érzi", "son"), ("女儿", "nǚér", "daughter"),
]
CORE200_F = [
    ("丈夫", "zhàngfu", "husband"), ("妻子", "qīzi", "wife"), ("老板", "lǎobǎn", "boss"),
    ("同事", "tóngshì", "colleague"), ("同学", "tóngxué", "classmate"), ("邻居", "línjū", "neighbor"),
    ("客人", "kèren", "guest"), ("服务员", "fúwùyuán", "server"), ("春天", "chūntiān", "spring"),
    ("夏天", "xiàtiān", "summer"), ("秋天", "qiūtiān", "autumn"), ("冬天", "dōngtiān", "winter"),
    ("天气", "tiānqì", "weather"), ("雨", "yǔ", "rain"), ("雪", "xuě", "snow"),
    ("风", "fēng", "wind"), ("太阳", "tàiyang", "sun"), ("月亮", "yuèliang", "moon"),
    ("山", "shān", "mountain"), ("河", "hé", "river"),
]
CORE200_G = [
    ("海", "hǎi", "sea"), ("树", "shù", "tree"), ("花", "huā", "flower"),
    ("鸟", "niǎo", "bird"), ("马", "mǎ", "horse"), ("牛", "niú", "cow"),
    ("身体", "shēntǐ", "body"), ("头", "tóu", "head"), ("眼睛", "yǎnjing", "eyes"),
    ("耳朵", "ěrduo", "ears"), ("手", "shǒu", "hand"), ("脚", "jiǎo", "foot"),
    ("心", "xīn", "heart"), ("病", "bìng", "illness"), ("药", "yào", "medicine"),
    ("爱", "ài", "love"), ("喜欢", "xǐhuan", "like"), ("想", "xiǎng", "want / think"),
    ("觉得", "juéde", "feel / think"), ("知道", "zhīdào", "know"),
]
CORE200_H = [
    ("认识", "rènshi", "know (a person)"), ("明白", "míngbai", "understand"), ("记得", "jìde", "remember"),
    ("忘记", "wàngjì", "forget"), ("希望", "xīwàng", "hope"), ("需要", "xūyào", "need"),
    ("应该", "yīnggāi", "should"), ("可以", "kěyǐ", "can / may"), ("能", "néng", "be able to"),
    ("会", "huì", "will / know how"), ("要", "yào", "want / will"), ("让", "ràng", "let"),
    ("帮助", "bāngzhù", "help"), ("谢谢", "xièxie", "thanks"), ("对不起", "duìbuqǐ", "sorry"),
    ("请", "qǐng", "please"), ("问", "wèn", "ask"), ("回答", "huídá", "answer"),
    ("告诉", "gàosu", "tell"), ("名字", "míngzi", "name"),
]
CORE200_I = [
    ("语言", "yǔyán", "language"), ("汉语", "Hànyǔ", "Chinese language"), ("英语", "Yīngyǔ", "English"),
    ("中国", "Zhōngguó", "China"), ("北京", "Běijīng", "Beijing"), ("上海", "Shànghǎi", "Shanghai"),
    ("工作", "gōngzuò", "work"), ("学习", "xuéxí", "study"), ("考试", "kǎoshì", "exam"),
    ("问题", "wèntí", "question"), ("答案", "dáàn", "answer"), ("意思", "yìsi", "meaning"),
    ("办法", "bànfǎ", "method"), ("机会", "jīhuì", "opportunity"), ("时间", "shíjiān", "time"),
    ("现在", "xiànzài", "now"), ("今天", "jīntiān", "today"), ("明天", "míngtiān", "tomorrow"),
    ("昨天", "zuótiān", "yesterday"), ("早上", "zǎoshang", "morning"),
]
CORE200_J = [
    ("晚上", "wǎnshang", "evening"), ("中午", "zhōngwǔ", "noon"), ("下午", "xiàwǔ", "afternoon"),
    ("星期", "xīngqī", "week"), ("号", "hào", "day of month"), ("点", "diǎn", "o'clock"),
    ("半", "bàn", "half"), ("刻", "kè", "quarter hour"), ("远", "yuǎn", "far"),
    ("近", "jìn", "near"), ("快", "kuài", "fast"), ("慢", "màn", "slow"),
    ("新", "xīn", "new"), ("旧", "jiù", "old"), ("多", "duō", "many"),
    ("少", "shǎo", "few"), ("高", "gāo", "tall"), ("长", "cháng", "long"),
    ("漂亮", "piàoliang", "beautiful"), ("开心", "kāixīn", "happy"),
]
CORE200 = (CORE200_A + CORE200_B + CORE200_C + CORE200_D + CORE200_E +
           CORE200_F + CORE200_G + CORE200_H + CORE200_I + CORE200_J)


def _vocab_lines(items):
    return "\n".join(
        "%d. %s (%s) - %s. %s (%s) - %s" % (i + 1, c, p, e, sc, sp, se)
        for i, (c, p, e, sc, sp, se) in enumerate(items))


def _story_lines(story):
    return "\n".join(
        "%d. %s\n   %s\n   %s" % (i + 1, c, p, e)
        for i, (c, p, e) in enumerate(story))


def _greet_lines():
    return "\n".join(
        "%d. %s (%s) - %s. Usage: %s" % (i + 1, c, p, e, u)
        for i, (c, p, e, u) in enumerate(GREETINGS))


def _idiom_lines():
    return "\n".join(
        "%d. %s (%s)\n   Literal: %s. Real meaning: %s.\n   %s (%s) - %s"
        % (i + 1, c, p, lit, mean, sc, sp, se)
        for i, (c, p, lit, mean, sc, sp, se) in enumerate(IDIOMS))


def _register_lines():
    return "\n".join(
        "%d. Informal: %s (%s) - %s\n   Formal: %s (%s) - %s\n   Note: %s"
        % (i + 1, ic, ip, ie, fc, fp, fe, n)
        for i, (ic, ip, ie, fc, fp, fe, n) in enumerate(REGISTERS))


def _complex_lines():
    return "\n".join(
        "%d. %s\n   %s\n   %s\n   Parse: %s"
        % (i + 1, c, p, e, n)
        for i, (c, p, e, n) in enumerate(COMPLEX))


def _core200_lines():
    return "\n".join(
        "%d. %s (%s) - %s" % (i + 1, c, p, e)
        for i, (c, p, e) in enumerate(CORE200))

# ---------------------------------------------------------------- entries

ENTRIES = [
    {
        "key": "overview",
        "name": "Mandarin Chinese Language Overview",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "ladder": 1,
        "description": (
            "Mandarin Chinese (中文 Zhōngwén) is the most spoken native "
            "language on earth. Its standard spoken form is called Putonghua "
            "(普通话 Pǔtōnghuà, common speech) in mainland China, Guoyu "
            "(国语 Guóyǔ, national language) in Taiwan, and Huayu "
            "(华语 Huáyǔ, Chinese language) in Singapore and Malaysia. "
            "The language code is ISO 639-1 zh and ISO 639-3 cmn; it belongs "
            "to the Sino-Tibetan family, Sinitic branch. About 929 million "
            "people speak Mandarin as a first language, and well over one "
            "billion speak it in total - roughly one in seven humans. It is "
            "an official language of China, Taiwan, and Singapore, and one "
            "of the six official working languages of the United Nations. "
            "Standard Mandarin is based on the Beijing dialect, and it is "
            "taught in schools across the Chinese-speaking world. Related "
            "varieties such as Cantonese (Yue), Wu (Shanghainese), Min "
            "(Hokkien), Hakka, Xiang, and Gan are historically sister "
            "tongues, not dialects of Mandarin in the linguistic sense - "
            "they are mutually unintelligible with Mandarin in speech, "
            "though they share the written character system. Mandarin "
            "itself has regional accents - northern speakers roll the "
            "tongue more (儿化 érhuà), southern speakers may merge certain "
            "sounds - but the standard is understood everywhere. This "
            "record is the front door of the database: everything after it "
            "teaches the writing, the sounds, the words, and the grammar, "
            "one sealed step at a time."
        ),
        "how_it_works": (
            "Learning Mandarin works the same way in this database every "
            "time: meet the language in overview, learn the writing system "
            "so the characters stop looking like pictures, train the ear on "
            "the four tones so ma can mean mother or horse on purpose, "
            "collect core vocabulary with a full sentence attached to every "
            "word, then assemble the grammar - word order, measure words, "
            "negation, questions - until sentences come out whole. Each "
            "record is a complete lesson file: real Mandarin in simplified "
            "characters, standard Hanyu Pinyin with tone marks, and plain "
            "English on every line. Read the characters, sound the pinyin "
            "aloud, check the English, then cover the English and translate "
            "back. Ten minutes a day through all thirty-four records builds "
            "a working foundation: greetings, numbers, time, family, food, "
            "travel, work, health, feelings, shopping, and real "
            "conversations - plus the stories, idioms, and formal speech "
            "that make a learner sound like a person instead of a phrasebook."
        ),
        "key_points": [
            "Mandarin Chinese (ISO 639-3 cmn, Sino-Tibetan family) has about 929 million native speakers and over one billion total speakers - the largest native language on earth.",
            "Standard Mandarin is based on the Beijing dialect and is called Putonghua in China, Guoyu in Taiwan, and Huayu in Singapore and Malaysia.",
            "It is official in China, Taiwan, and Singapore, and one of six UN working languages.",
            "Cantonese, Wu, Min, Hakka, Xiang, and Gan are sister varieties, mutually unintelligible with Mandarin in speech but sharing the written characters.",
            "This database teaches simplified characters plus Hanyu Pinyin with tone marks plus English on every line, ladder-ordered from foundations to mastery.",
        ],
        "requirements": [
            "Every record carries Mandarin in simplified characters, standard pinyin with tone marks, and English - no vocabulary-list-only records.",
            "Every word entry attaches at least one full example sentence, translated line by line.",
            "Records are ladder-ordered 1-34: foundations first, compounded in the middle, advanced last; ranks 1-10 non-decreasing.",
            "Signature editions reframe the same ladder through the Signature Language Method and are labeled Signature-made, never presented as authentic public record.",
        ],
        "standards": [
            "Romanization follows Hanyu Pinyin per ISO 7098:2015, with tone marks on the correct vowel.",
            "Character forms follow the simplified standard used in mainland China and Singapore (GB 18030-2022 coded character set).",
            "Vocabulary selection cross-checked against the HSK levels 1-6 syllabus word lists.",
        ],
        "citations": [CIT_ISO7098, CIT_NORMAN, CIT_HSK, CIT_GB18030],
        "sig_lens": (
            "The Signature read: a language is a covenant between speaker "
            "and listener, and Mandarin keeps its covenant in tones. The "
            "Signature Language Method stamps each sound with its pitch "
            "line, seals each character with its meaning, and signs each "
            "sentence only when it can be spoken aloud without fear. One "
            "billion speakers keep this covenant daily; the learner joins "
            "them one sealed sentence at a time."
        ),
    },
    {
        "key": "writing",
        "name": "Mandarin Writing System: Characters and Pinyin",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "ladder": 2,
        "description": (
            "Mandarin is written with Chinese characters (汉字 Hànzì). Each "
            "character is one syllable and usually one meaningful unit: 人 "
            "(rén) means person, 山 (shān) means mountain, 水 (shuǐ) means "
            "water. Mainland China and Singapore use simplified characters "
            "(简体字 jiǎntǐzì); Taiwan, Hong Kong, and Macau use traditional "
            "characters (繁體字 fántǐzì). Examples: 国 (guó, country) "
            "simplified vs 國 traditional; 语 (yǔ, language) simplified vs "
            "語 traditional; 学 (xué, learn) simplified vs 學 traditional. "
            "Characters are built from about two hundred reusable components "
            "called radicals (部首 bùshǒu): the water radical 氵 appears in "
            "河 (hé, river), 海 (hǎi, sea), and 洗 (xǐ, wash). Stroke order "
            "follows fixed rules - top before bottom, left before right, "
            "horizontal before vertical - and correct order makes handwriting "
            "fast and readable. Beside characters, Mandarin uses Hanyu "
            "Pinyin (拼音 pīnyīn), the roman alphabet spelling of every "
            "syllable with tone marks: 你好 is written nǐ hǎo. Pinyin is "
            "the learner's training wheels and the standard input method on "
            "phones and computers - type nihao and pick 你好. Mandarin is "
            "written left to right, top to bottom, in horizontal lines, "
            "exactly like English; classical texts run top to bottom in "
            "right-to-left columns. Punctuation has full-width forms: 。 "
            "period, ， comma, 、 the enumeration comma used in lists, "
            "！ ？ ； ： and the book-title brackets 《》. Numbers use the "
            "characters 一二三四五六七八九十 (1-10); formal financial writing "
            "uses complex forms 壹贰叁肆伍陆柒捌玖拾 to prevent forgery."
        ),
        "how_it_works": (
            "The writing system works as a two-track code. Characters carry "
            "meaning directly: see 木 (mù, wood), see two of them 林 (lín, "
            "grove), see three 森 (sēn, forest) - meaning compounds "
            "visibly. About eighty percent of characters are "
            "phono-semantic: one part hints at meaning, one part hints at "
            "sound, as in 妈 (mā, mother - the 女 woman radical plus 马 mǎ "
            "for sound). Pinyin carries sound exactly: every Mandarin "
            "syllable is an initial (starting consonant) plus a final "
            "(vowel ending) plus a tone, and pinyin writes all three. A "
            "learner reads pinyin first, speaks the sentence, then matches "
            "the characters to the sounds already in the mouth. Stroke "
            "order rules make every character drawable from memory: write "
            "the enclosing frame first, fill it, then close the bottom; "
            "dots and small strokes come last. Digital text needs no "
            "handwriting at all - pinyin input converts keystrokes to "
            "characters, which is how a billion people type Chinese daily."
        ),
        "key_points": [
            "One character is one syllable and usually one meaning unit; about 3,000-4,000 characters cover everyday reading.",
            "Simplified characters are standard in mainland China and Singapore; traditional in Taiwan, Hong Kong, and Macau.",
            "Characters decompose into roughly 200 radicals; most characters are phono-semantic (meaning part + sound part).",
            "Hanyu Pinyin spells every syllable in the roman alphabet with tone marks and is the standard typing input method.",
            "Modern text runs left to right horizontally; punctuation uses full-width forms (。 ， 、 《》).",
        ],
        "requirements": [
            "Every character shown with its pinyin (tone marks) and English gloss on first appearance.",
            "Simplified forms used throughout; traditional noted where the difference is instructive.",
            "Stroke-count and radical notes attach to characters in the writing drills.",
            "Pinyin input behavior (type pinyin, pick characters) described so learners can type from day one.",
        ],
        "standards": [
            "Simplified character forms follow the mainland standard character tables (GB 18030-2022).",
            "Pinyin spelling and tone-mark placement follow ISO 7098:2015.",
            "Radical names and counts follow the standard 214-radical (Kangxi) system as simplified.",
        ],
        "citations": [CIT_ISO7098, CIT_GB18030, CIT_NORMAN],
        "sig_lens": (
            "The Signature read: a character is a stamped seal - one "
            "impression carrying sound, meaning, and history in a single "
            "block. The Signature Language Method teaches radicals as the "
            "seal-cutter's toolkit: learn the two hundred parts and every "
            "new character is a recombination, never a stranger. Stamp the "
            "radical, seal the character, sign the word."
        ),
    },
    {
        "key": "phonology",
        "name": "Mandarin Pronunciation and the Four Tones",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "ladder": 3,
        "description": (
            "Mandarin has about twenty-one initial consonants and about "
            "three dozen finals (vowel endings); every syllable is initial "
            "+ final + tone. English approximations: b/p (unaspirated, like "
            "the b in spy), p (aspirated, like p in pie), m, f, d/t, n, l, "
            "g/k, h, j/q/x (tongue-tip sounds with no English twin - j like "
            "a soft dj, q like ch with lips spread, x like sh with lips "
            "spread), zh/ch/sh/r (tongue curled back), z/c/s, y, w. The "
            "heart of Mandarin pronunciation is tone: four main tones plus "
            "a neutral tone. First tone is high and flat (mā 妈 mother), "
            "second rises (má 麻 hemp), third dips down then up (mǎ 马 "
            "horse), fourth falls sharply (mà 骂 scold), and the neutral "
            "tone is short and light (ma 吗 question particle). The same "
            "syllable with different tones is a different word - tone is "
            "not decoration, it is spelling. Ten spoken examples with "
            "translations: 妈 (mā) mother, 麻 (má) hemp, 马 (mǎ) horse, "
            "骂 (mà) to scold, 买 (mǎi) to buy, 卖 (mài) to sell, "
            "水 (shuǐ) water, 睡觉 (shuìjiào) to sleep, 你好 (nǐ hǎo) "
            "hello, 谢谢 (xièxie) thank you. Tone sandhi - tones changing "
            "next to each other - follows rules: two third tones in a row "
            "turn the first into a second tone, so 你好 is spoken ní hǎo; "
            "不 (bù) becomes bú before a fourth tone (不对 bú duì); 一 "
            "(yī) becomes yí before a fourth tone (一个 yí ge) and yì "
            "before other tones (一年 yì nián). Stress is light: in "
            "two-syllable words the first syllable usually carries the "
            "weight, and grammatical particles go neutral."
        ),
        "how_it_works": (
            "Tones work as pitch shapes laid over the syllable. Think of "
            "the voice as a hand drawing in the air: first tone draws a "
            "high flat line, second draws a rising slash, third draws a "
            "dip like a valley, fourth draws a falling chop. The neutral "
            "tone draws nothing - it is quick, quiet, and borrows its "
            "pitch from what came before. Minimal pairs prove the system: "
            "change only the tone of ma and the meaning jumps from mother "
            "to hemp to horse to scold. Learners train tones in pairs, "
            "never alone, because the ear learns contrast: drill mā-má, "
            "mǎ-mà, mǎi-mài until the hand in the air moves without "
            "thinking. Tone sandhi keeps speech flowing: the rules above "
            "are automatic for native speakers, and learners simply apply "
            "them when reading pinyin - see nǐ hǎo, say ní hǎo. Intonation "
            "across a sentence is gentle; Mandarin does not use English "
            "stress melodies, so a flat, clear delivery with correct "
            "lexical tones sounds more native than an expressive one with "
            "wrong tones."
        ),
        "key_points": [
            "Four lexical tones plus neutral tone: high-flat, rising, dipping, falling - tone changes meaning, not emphasis.",
            "ma demonstrates all five: 妈 mā mother, 麻 má hemp, 马 mǎ horse, 骂 mà scold, 吗 ma question particle.",
            "Tone sandhi: two third tones turn the first to second (你好 -> ní hǎo); 不 and 一 shift before fourth tones.",
            "Buy vs sell is a tone pair: 买 mǎi (third tone) vs 卖 mài (fourth tone) - tones do real economic work.",
            "Train tones in minimal pairs with a hand drawing the pitch shape; flat clear delivery beats expressive wrong tones.",
        ],
        "requirements": [
            "Every pinyin transcription carries tone marks on the correct vowel (a, o, e, i, u, ü priority order).",
            "Neutral-tone syllables written without a mark (吗 ma, 谢谢 xièxie).",
            "Sandhi-affected readings noted wherever textbook pinyin differs from spoken pitch (你好 ní hǎo).",
            "At least ten spoken-example words with English translations in the phonology record.",
        ],
        "standards": [
            "Pinyin tone-mark placement follows ISO 7098:2015 vowel priority (a > o > e > i/u/ü).",
            "Tone descriptions follow the standard five-point pitch scale (55, 35, 214, 51).",
            "Sandhi rules stated per the standard Putonghua prescription (PSC syllabus).",
        ],
        "citations": [CIT_ISO7098, CIT_PSC, CIT_LI],
        "sig_lens": (
            "The Signature read: each tone is a signature pitch-line drawn "
            "in the air - flat, rising, dipping, falling - and the voice "
            "signs every syllable. The Signature Language Method trains "
            "the hand to draw the tone while the mouth speaks it, so the "
            "body remembers what the ear is still learning. Stamp the "
            "pitch, seal the syllable, sign the word."
        ),
    },
    {
        "key": "nouns1",
        "name": "Core Nouns I: People, Places, and Things",
        "group": "Core Vocabulary",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "ladder": 4,
        "description": (
            "Twenty-five essential nouns - people, places, and things - "
            "each with pinyin, English, and a full example sentence "
            "translated line by line. Mandarin nouns do not change for "
            "number or gender: 人 means person or people depending on "
            "context, and 们 (men) marks human plurals explicitly (朋友 "
            "friend, 朋友们 friends). Measure words pair with nouns when "
            "counting - covered fully in the grammar record.\n"
            + _vocab_lines(NOUNS)
        ),
        "how_it_works": (
            "A Mandarin noun works by naming without inflecting. There are "
            "no plurals to memorize, no genders to assign, no cases to "
            "decline: the word stays one shape and context does the rest. "
            "Number comes from numbers and measure words (一个人 one "
            "person, 三本书 three books), definiteness from demonstratives "
            "(这个 this, 那个 that) or from context alone. Human nouns "
            "take 们 for explicit plurals: 老师们 the teachers, 孩子们 the "
            "children. Possession is built with 的: 我的书 my book, 老师的"
            "电脑 the teacher's computer. To learn a noun, learn its "
            "measure word alongside it from the start - 本 for books, 张 "
            "for flat things, 把 for handled things - because counting "
            "without the measure word is the most audible beginner error. "
            "Each noun below is sealed with a sentence so the word is met "
            "in the wild, not in a list."
        ),
        "key_points": [
            "Mandarin nouns never inflect: no plurals, no gender, no case - 人 is person or people by context.",
            "Human plurals take 们: 朋友们 (friends), 孩子们 (children).",
            "Possession is built with 的: 我的书 (my book).",
            "Every noun pairs with a measure word when counted: 一本书, 三张纸.",
            "Learn each noun inside a full sentence; isolated words fade, sentences stick.",
        ],
        "requirements": [
            "25 nouns minimum, each with characters, pinyin, English, and one translated example sentence.",
            "People, places, and things all represented; at least one human-plural 们 example.",
            "Measure-word pairings shown in the example sentences where counting occurs.",
        ],
        "standards": [
            "Word selection cross-checked against HSK levels 1-3 vocabulary lists.",
            "Pinyin per ISO 7098:2015; simplified characters per GB 18030-2022.",
        ],
        "citations": [CIT_HSK, CIT_LI, CIT_ISO7098],
        "sig_lens": (
            "The Signature read: a noun is a stamped seal of a thing - "
            "person, place, or object pressed into one unchanging block. "
            "The Signature Language Method seals twenty-five foundation "
            "nouns first, because every sentence is built on named things. "
            "Stamp the thing, seal the word, sign the sentence."
        ),
    },
    {
        "key": "verbs1",
        "name": "Core Verbs I: Essential Actions",
        "group": "Core Vocabulary",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "ladder": 5,
        "description": (
            "Twenty-five essential verbs - the actions of daily life - "
            "each with pinyin, English, and a full example sentence "
            "translated line by line. Mandarin verbs never conjugate: 吃 "
            "is eat, eats, ate, and eating depending on time words and "
            "aspect particles. Time is carried by words like 今天 (today), "
            "昨天 (yesterday), 明天 (tomorrow), and completion by 了.\n"
            + _vocab_lines(VERBS)
        ),
        "how_it_works": (
            "A Mandarin verb works as an unchanging action block. English "
            "bends verbs for person and tense - I eat, he eats, they ate - "
            "while Mandarin keeps one form and adds small helper words "
            "around it. Past time comes from 昨天 (yesterday) or from the "
            "particle 了 after the verb: 我吃了 I ate. Ongoing action comes "
            "from 在 or 正在 before the verb: 我在吃饭 I am eating. Future "
            "comes from 会 or 要: 我会去 I will go. Negation sits directly "
            "before the verb: 不吃 (not eat), 不去 (not go), 没吃 (did not "
            "eat) - 不 for present and future, 没 for past. The verb-object bond is "
            "tight: 吃饭 (eat rice = have a meal), 睡觉 (sleep sleep = "
            "sleep), 唱歌 (sing song = sing) are separable verb-object "
            "compounds that split around aspect markers - 睡了一个觉. Learn "
            "verbs in their natural pairs with objects, and the grammar of "
            "time attaches itself with almost no memorization."
        ),
        "key_points": [
            "Mandarin verbs never conjugate: one form serves all persons and tenses.",
            "Time is marked by time words (昨天, 明天) and aspect particles (了, 过, 着), not by verb changes.",
            "Negation sits before the verb: 不 for present/future, 没 for past.",
            "Many daily verbs are verb-object compounds: 吃饭, 睡觉, 唱歌.",
            "Learn each verb with its object partner; the pair is the real vocabulary unit.",
        ],
        "requirements": [
            "25 verbs minimum, each with characters, pinyin, English, and one translated example sentence.",
            "At least one 了-completion, one 在-progressive, and one negation example among the sentences.",
            "Separable verb-object compounds (吃饭, 睡觉) represented.",
        ],
        "standards": [
            "Word selection cross-checked against HSK levels 1-3 vocabulary lists.",
            "Aspect terminology follows Li and Thompson's functional grammar.",
        ],
        "citations": [CIT_HSK, CIT_LI, CIT_YIP],
        "sig_lens": (
            "The Signature read: a verb is a seal of motion - one block "
            "stamped the same in every tense, with time carried by small "
            "satellite seals around it. The Signature Language Method "
            "teaches the action once and reuses it forever: stamp the "
            "action, seal the time-word, sign the sentence."
        ),
    },
    {
        "key": "adj_adv",
        "name": "Adjectives and Adverbs",
        "group": "Core Vocabulary",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "ladder": 6,
        "description": (
            "Twenty-five adjectives and fifteen adverbs, each with a full "
            "translated example sentence. Mandarin adjectives act like "
            "verbs: 好 can mean good or to be good, and 高 means tall or to "
            "be tall. As predicates they usually take 很 (which here is a "
            "grammatical linker more than very): 他很高 (he is tall). For "
            "emphasis, 太...了 frames excess: 太贵了 (too expensive). "
            "Attributive adjectives link to nouns with 的: 漂亮的衣服 "
            "(beautiful clothes). Adverbs sit before the verb they modify "
            "and never change form: 慢慢说 (speak slowly), 马上来 (come "
            "right away). There is no gender or number agreement anywhere - "
            "an adjective keeps one shape for every noun.\nAdjectives:\n"
            + _vocab_lines(ADJECTIVES)
            + "\nAdverbs:\n"
            + _vocab_lines(ADVERBS)
        ),
        "how_it_works": (
            "Adjectives work as stative verbs: where English needs is, "
            "Mandarin often needs nothing - 他高 is a complete sentence "
            "(he is tall). The 很 before a predicate adjective is usually "
            "a softener, not an intensifier: 他很高 most often means he "
            "is tall, while 他非常高 means he is extremely tall. Comparison "
            "uses 比: 他比我高 (he is taller than me), and superlatives "
            "use 最: 他最高 (he is the tallest). Reduplication turns "
            "adjectives into lively adverbs: 慢 (slow) becomes 慢慢 "
            "(slowly), and the pattern adjective + 地 marks adverbs "
            "explicitly: 快乐地唱 (sing happily). Degree adverbs stack "
            "before the adjective - 很, 非常, 太, 最 - in a fixed order of "
            "strength. Negation of adjectives uses 不: 不好 (not good), "
            "不贵 (not expensive). Because adjectives never agree with "
            "anything, the whole system reduces to word order: degree "
            "word, adjective, 的, noun."
        ),
        "key_points": [
            "Mandarin adjectives behave like verbs: 他高 alone means he is tall - no is needed.",
            "Predicate adjectives usually take 很 as a grammatical linker: 他很高 = he is tall.",
            "Comparison is 比 (他比我高); superlative is 最 (他最高).",
            "Adverbs precede the verb and never inflect: 慢慢说, 马上来.",
            "No agreement of any kind: one adjective shape fits every noun, singular or plural.",
        ],
        "requirements": [
            "25 adjectives and 15 adverbs, each with a translated example sentence.",
            "At least one 比 comparison, one 最 superlative, and one 太...了 example.",
            "Attributive 的 usage shown (漂亮的衣服).",
        ],
        "standards": [
            "Word selection cross-checked against HSK levels 1-4 vocabulary lists.",
            "Stative-verb analysis follows Li and Thompson's functional grammar.",
        ],
        "citations": [CIT_HSK, CIT_LI, CIT_YIP],
        "sig_lens": (
            "The Signature read: an adjective is a seal of quality pressed "
            "onto a noun with 的, and an adverb is a seal of manner pressed "
            "before a verb. The Signature Language Method grades every "
            "quality on one pitch-line of degree - 很, 非常, 太, 最 - so "
            "the learner stamps intensity the way tones stamp pitch."
        ),
    },
    {
        "key": "pronouns",
        "name": "Mandarin Pronouns: Full Paradigms",
        "group": "Core Vocabulary",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "ladder": 7,
        "description": (
            "The complete Mandarin pronoun system with full paradigms and "
            "translated example sentences. Personal pronouns: 我 (wǒ, I), "
            "你 (nǐ, you), 您 (nín, you polite), 他 (tā, he), 她 (tā, she), "
            "它 (tā, it); plurals add 们: 我们 (wǒmen, we), 你们 (nǐmen, "
            "you all), 他们 (tāmen, they masculine/mixed), 她们 (tāmen, "
            "they feminine), 它们 (tāmen, they for things). Possessives add "
            "的: 我的 (my), 你的 (your), 他的 (his), 我们的 (our). "
            "Demonstratives: 这 (zhè, this), 那 (nà, that), 这些 (these), "
            "那些 (those), 这里/这儿 (here), 那里/那儿 (there), 这么 "
            "(like this), 那么 (like that). Interrogatives: 谁 (shéi, who), "
            "什么 (shénme, what), 哪里/哪儿 (nǎlǐ/nǎr, where), 哪个 "
            "(nǎge, which), 怎么 (zěnme, how), 为什么 (wèishénme, why), "
            "多少 (duōshao, how many/much), 几 (jǐ, how many - small "
            "numbers). Example sentences: 我是学生。(Wǒ shì xuésheng.) I "
            "am a student. 你叫什么名字？(Nǐ jiào shénme míngzi?) What is "
            "your name? 这是我的书。(Zhè shì wǒ de shū.) This is my book. "
            "他们是我的朋友。(Tāmen shì wǒ de péngyou.) They are my "
            "friends. 你们去哪里？(Nǐmen qù nǎlǐ?) Where are you going? "
            "谁是老师？(Shéi shì lǎoshī?) Who is the teacher? 这个多少"
            "钱？(Zhège duōshao qián?) How much is this? 你为什么学中文？"
            "(Nǐ wèishénme xué Zhōngwén?) Why are you learning Chinese? "
            "我们明天见。(Wǒmen míngtiān jiàn.) See you tomorrow (we meet "
            "tomorrow). 您请坐。(Nín qǐng zuò.) Please sit down (polite). "
            "它很可爱。(Tā hěn kěài.) It is very cute. 那些是我的。(Nàxiē "
            "shì wǒ de.) Those are mine. 你怎么来？(Nǐ zěnme lái?) How "
            "are you coming? 几个人？(Jǐ ge rén?) How many people? 这里很"
            "漂亮。(Zhèlǐ hěn piàoliang.) It is beautiful here. 那是我的家。"
            "(Nà shì wǒ de jiā.) That is my home."
        ),
        "how_it_works": (
            "Pronouns work by position, not by form: 我 is I, me, and my "
            "depending on where it sits, with 的 marking possession "
            "explicitly when needed. There is no subject/object split - "
            "no I/me, he/him - so the paradigm is tiny: six singulars, "
            "five plurals, one possessive particle. 您 is the politeness "
            "upgrade of 你, used for elders, customers, and officials, and "
            "it has no plural in standard usage. 他/她/它 sound identical "
            "(tā) and differ only in writing - speech relies on context. "
            "Reflexives use 自己: 我自己 (myself), 他自己 (himself). "
            "Interrogative pronouns stay in place - no wh-movement: 你去哪"
            "里 keeps where at the end where English would front it. 谁 "
            "asks who, 什么 asks what, and 什么 also means something in "
            "statements: 我想吃点什么 (I want to eat something). The whole "
            "system fits on one page, and once placed correctly, pronouns "
            "never surprise again."
        ),
        "key_points": [
            "No subject/object forms: 我 is I and me; position decides the role.",
            "Plurals add 们: 我们, 你们, 他们/她们/它们; possessives add 的: 我的, 你的.",
            "您 is the polite you; 他/她/它 are pronounced identically (tā) and differ only in writing.",
            "Interrogatives stay in place: 你去哪里 (where at the end), never fronted.",
            "自己 builds reflexives: 我自己 (myself); 什么 doubles as something in statements.",
        ],
        "requirements": [
            "Full personal, possessive, demonstrative, and interrogative paradigms with pinyin and English.",
            "At least 15 translated example sentences covering every pronoun class.",
            "您 politeness usage and the 他/她/它 written distinction explained.",
        ],
        "standards": [
            "Paradigm tables follow the standard Putonghua prescription (PSC syllabus).",
            "Pinyin per ISO 7098:2015.",
        ],
        "citations": [CIT_PSC, CIT_LI, CIT_YIP],
        "sig_lens": (
            "The Signature read: pronouns are the signature block of the "
            "sentence - 我 signs the speaker, 你 signs the listener, 他 "
            "signs the third party. The Signature Language Method teaches "
            "the signer to place each seal in its exact position, because "
            "in Mandarin the seal never changes shape, only its place on "
            "the page."
        ),
    },
    {
        "key": "numbers_time",
        "name": "Numbers, Time, and Dates",
        "group": "Core Vocabulary",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "ladder": 8,
        "description": (
            "The complete Mandarin number and time system, every form with "
            "pinyin, English, and example sentences. Digits 1-10: 一 (yī), "
            "二 (èr), 三 (sān), 四 (sì), 五 (wǔ), 六 (liù), 七 (qī), 八 "
            "(bā), 九 (jiǔ), 十 (shí). Teens add ten first: 十一 (shíyī, "
            "11), 十二 (12), 十九 (19). Tens multiply: 二十 (èrshí, 20), "
            "三十 (30), 九十 (90). Compounds stack: 二十五 (25), 四十二 "
            "(sìshíèr, 42), 四十八 (48), 九十九 (99). One hundred is 一百 "
            "(yìbǎi); 一千 (yìqiān) "
            "is a thousand; 一万 (yíwàn) is ten thousand - Mandarin counts "
            "in ten-thousands, so 100,000 is 十万 (shíwàn). Ordinals add "
            "第: 第一 (dìyī, first), 第二 (second), 第十 (tenth). Days of "
            "the week: 星期一 (xīngqīyī, Monday) through 星期六 (Saturday), "
            "星期天/星期日 (Sunday). Months: 一月 (yīyuè, January) through "
            "十二月 (December). Seasons: 春天 (chūntiān, spring), 夏天 "
            "(xiàtiān, summer), 秋天 (qiūtiān, autumn), 冬天 (dōngtiān, "
            "winter). Clock time: 点 (diǎn, o'clock), 分 (fēn, minute), "
            "半 (bàn, half), 刻 (kè, quarter): 三点 (sān diǎn, 3:00), "
            "三点半 (3:30), 三点一刻 (3:15), 三点四十五分 (3:45). Dates "
            "run big to small: 2026年10月17日 (èr líng èr liù nián shí "
            "yuè shíqī rì, October 17, 2026). Example sentences: 我有三个"
            "苹果。(Wǒ yǒu sān ge píngguǒ.) I have three apples. 现在三点"
            "半。(Xiànzài sān diǎn bàn.) It is 3:30 now. 今天是星期五。"
            "(Jīntiān shì xīngqīwǔ.) Today is Friday. 我的生日是五月十号。"
            "(Wǒ de shēngrì shì wǔ yuè shí hào.) My birthday is May 10th. "
            "他是第一名。(Tā shì dìyī míng.) He is number one. 一年有十二"
            "个月。(Yì nián yǒu shíèr ge yuè.) A year has twelve months. "
            "冬天很冷。(Dōngtiān hěn lěng.) Winter is very cold. 我们八点"
            "见。(Wǒmen bā diǎn jiàn.) See you at eight. 这本书一百块。"
            "(Zhè běn shū yìbǎi kuài.) This book is 100 yuan."
        ),
        "how_it_works": (
            "Mandarin numbers work as a transparent base-ten construction "
            "kit. Ten is 十 and every teen is ten-plus-digit; every ten is "
            "digit-times-ten; compounds just concatenate: forty-eight is "
            "four-ten-eight (四十八). The ten-thousand 万 is the only "
            "surprise for English speakers: where English restarts at "
            "thousand, Mandarin restarts at 万, so a million is 一百万 "
            "(one hundred ten-thousands). Zero 零 appears between nonzero "
            "digits: 101 is 一百零一. Phone numbers and years are read "
            "digit by digit: 2026 is 二零二六. Time phrases build outward "
            "from the hour: hour + 点, then 分 or 半 or 刻. Dates stack "
            "largest to smallest - year, month, day, then weekday - which "
            "is also the logic of Mandarin addresses and names. Measure "
            "words ride along with numbers: 三个人 (three people), 五本书 "
            "(five books). Drill the construction rules, not the list: "
            "with ten digits and five patterns, every number to a hundred "
            "million is readable."
        ),
        "key_points": [
            "Numbers are a construction kit: 十一 (10+1), 二十 (2x10), 四十八 (4x10+8).",
            "Mandarin counts in ten-thousands: 一万 = 10,000; a million is 一百万.",
            "Ordinals add 第: 第一 (first); time uses 点/分/半/刻; dates run year-month-day.",
            "Zero 零 appears between nonzero digits: 101 = 一百零一; years read digit by digit.",
            "Numbers always pair with measure words when counting nouns: 三个人.",
        ],
        "requirements": [
            "Digits 1-10 with pinyin; teens, tens, and compounds to 100; 100/1,000/10,000 forms.",
            "Ordinals, weekdays, months, seasons, clock-time patterns, and date format, each with example sentences.",
            "At least 8 translated example sentences using numbers and time.",
        ],
        "standards": [
            "Number constructions follow the standard Putonghua prescription (PSC syllabus).",
            "Financial complex numerals noted per standard accounting practice (壹贰叁肆伍陆柒捌玖拾).",
        ],
        "citations": [CIT_PSC, CIT_LI, CIT_HSK],
        "sig_lens": (
            "The Signature read: numbers are the most honest seals in the "
            "language - every digit stamps exactly what it means, and ten "
            "digits build every quantity to a hundred million. The "
            "Signature Language Method teaches the five construction "
            "patterns, never the list, so the learner can sign any number "
            "ever spoken."
        ),
    },
    {
        "key": "greetings",
        "name": "Greetings and Everyday Phrases",
        "group": "Core Vocabulary",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "ladder": 9,
        "description": (
            "Thirty greetings, farewells, and politeness phrases - the "
            "social survival kit - each with pinyin, English, and a usage "
            "note explaining exactly when to say it.\n"
            + _greet_lines()
        ),
        "how_it_works": (
            "Greetings work as social seals: the right phrase at the right "
            "moment marks the speaker as considerate, and Mandarin "
            "politeness runs on small, fixed formulas rather than long "
            "speeches. 你好 opens everything; 您好 upgrades it for "
            "respect; 早上好 and 晚上好 split the day. Thanks are short - "
            "谢谢 - and the reply is shorter: 不客气. Apologies scale: "
            "不好意思 for small bumps, 对不起 for real faults, and the "
            "reply 没关系 releases everyone. 请 is the universal softener "
            "that turns any command into a request. The caring questions - "
            "吃了吗, 最近怎么样 - are phatic: they ask after wellbeing, "
            "not for information, and the right answer is short and warm "
            "(吃了, 还不错). Farewells mirror the meeting: 再见 for "
            "friends, 慢走 from a host, 一路顺风 for a traveler. Learn the "
            "thirty in pairs of call and response, and the first minute of "
            "every Mandarin conversation takes care of itself."
        ),
        "key_points": [
            "你好 is universal; 您好 adds respect for elders, clients, and officials.",
            "谢谢 / 不客气 and 对不起 / 没关系 are call-and-response pairs - learn both halves.",
            "请 softens any request; 请问 opens any question to a stranger.",
            "吃了吗 and 最近怎么样 are caring formulas - answer short and warm, not literally.",
            "Farewells match the situation: 再见, 慢走 (host), 一路顺风 (traveler).",
        ],
        "requirements": [
            "30 greetings/farewells/politeness phrases with pinyin, English, and usage notes.",
            "Call-and-response pairs (thanks, apologies, farewells) explicitly paired.",
            "Politeness levels noted (neutral vs respectful forms).",
        ],
        "standards": [
            "Phrases selected from HSK 1-2 communicative functions lists.",
            "Usage notes follow standard Putonghua pragmatics (PSC syllabus).",
        ],
        "citations": [CIT_HSK, CIT_PSC, CIT_YIP],
        "sig_lens": (
            "The Signature read: a greeting is the first seal pressed on "
            "a conversation - small, exact, and carrying the whole "
            "relationship in one impression. The Signature Language Method "
            "teaches greetings as call-and-response pairs, because a seal "
            "is only complete when the other party presses back."
        ),
    },
    {
        "key": "grammar_essentials",
        "name": "Mandarin Grammar Essentials",
        "group": "Core Vocabulary",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "ladder": 10,
        "description": (
            "The seven load-bearing rules of Mandarin grammar, each with "
            "translated example sentences. 1) Word order is subject-verb-"
            "object, and time and place come before the verb: 我今天在家吃"
            "饭。(Wǒ jīntiān zài jiā chī fàn.) I eat at home today. 2) No "
            "gender, no number, no case, no conjugation - words keep one "
            "shape. 3) Aspect particles mark completion and experience: 了 "
            "(le, completed), 过 (guo, experienced), 着 (zhe, ongoing "
            "state): 我吃了 (I ate), 我吃过 (I have eaten before), 门开着 "
            "(the door is open). 4) Measure words count nouns: 一个人, "
            "两本书, 三只猫. 5) Negation: 不 before present/future verbs "
            "(我不去), 没 before past verbs and 有 (我没去, 没有). 6) "
            "Questions: add 吗 to a statement (你是学生吗？), or use "
            "question words in place (你是谁？), or offer alternatives "
            "with 还是 (你要茶还是咖啡？). 7) 是 for identity (我是学生), "
            "有 for possession and existence (我有书; 有人), 在 for "
            "location and progressive (我在家; 我在看书). Topic-comment "
            "structure fronts the topic: 这本书我看过。(This book, I have "
            "read it.)"
        ),
        "how_it_works": (
            "Mandarin grammar works by word order plus small particles - "
            "there is almost no morphology to memorize. The sentence is a "
            "fixed assembly line: time, place, subject, adverb, verb, "
            "object. Slot a word into the wrong position and the meaning "
            "shifts or breaks: 我吃饭在家 is wrong because place must "
            "precede the verb. Particles do the jobs that inflections do "
            "in European languages: 了 closes an action, 过 opens a life "
            "experience, 着 holds a state, 吗 turns a statement into a "
            "yes-no question, 呢 bounces a question back (我很好，你呢？). "
            "的 links modifiers to nouns (我的书, 漂亮的衣服), 地 links "
            "adverbs to verbs (慢慢地说), 得 links verbs to their results "
            "(说得很好) - three particles, one sound, three jobs, told "
            "apart by position. 把 moves the object before the verb for "
            "disposal actions (把门关上), and 被 marks the passive (杯子被"
            "打破了). Master the assembly line and the dozen particles, "
            "and the grammar of the whole language is in hand."
        ),
        "key_points": [
            "Fixed assembly line: time, place, subject, adverb, verb, object - position carries the grammar.",
            "No inflections: aspect particles 了/过/着 and time words do the work of tenses.",
            "Measure words are mandatory when counting: 一个人, 两本书.",
            "不 negates present/future; 没 negates past and 有.",
            "吗 makes yes-no questions; question words stay in place; 还是 offers alternatives.",
            "的/地/得 share one sound with three jobs, told apart by position.",
        ],
        "requirements": [
            "Word order, aspect, measure words, negation, question formation, 是/有/在 each with translated examples.",
            "At least 12 translated example sentences across the rules.",
            "的/地/得 distinction stated with examples.",
        ],
        "standards": [
            "Grammatical analysis follows Li and Thompson's functional reference grammar.",
            "Terminology cross-checked with Yip and Rimmington's comprehensive grammar.",
        ],
        "citations": [CIT_LI, CIT_YIP, CIT_PSC],
        "sig_lens": (
            "The Signature read: grammar is the assembly line where seals "
            "are pressed in order - time, place, actor, action - and the "
            "particles are the small seals that stamp tense, question, and "
            "possession. The Signature Language Method teaches the line, "
            "not the exceptions, because a straight line presses true "
            "every time."
        ),
    },
]

# --- themed sentence sets (records 11-20): (chars, pinyin, english) x 20 ---

HOME_SENT = [
    ("这是我的家。", "Zhè shì wǒ de jiā.", "This is my home."),
    ("我家有四口人。", "Wǒ jiā yǒu sì kǒu rén.", "My family has four people."),
    ("爸爸在客厅看电视。", "Bàba zài kètīng kàn diànshì.", "Dad is watching TV in the living room."),
    ("妈妈在厨房做饭。", "Māma zài chúfáng zuò fàn.", "Mom is cooking in the kitchen."),
    ("我的房间很干净。", "Wǒ de fángjiān hěn gānjìng.", "My room is very clean."),
    ("床上有一床被子。", "Chuáng shang yǒu yì chuáng bèizi.", "There is a quilt on the bed."),
    ("书桌上有很多书。", "Shūzhuō shang yǒu hěn duō shū.", "There are many books on the desk."),
    ("哥哥在卧室睡觉。", "Gēge zài wòshì shuìjiào.", "Older brother is sleeping in the bedroom."),
    ("妹妹喜欢在阳台上玩。", "Mèimei xǐhuan zài yángtái shang wán.", "Younger sister likes playing on the balcony."),
    ("我们家的沙发很舒服。", "Wǒmen jiā de shāfā hěn shūfu.", "Our sofa is very comfortable."),
    ("冰箱里有牛奶和水果。", "Bīngxiāng lǐ yǒu niúnǎi hé shuǐguǒ.", "There is milk and fruit in the fridge."),
    ("爷爷奶奶住在乡下。", "Yéye nǎinai zhù zài xiāngxia.", "Grandpa and grandma live in the countryside."),
    ("每天晚上我们一起吃饭。", "Měitiān wǎnshang wǒmen yìqǐ chī fàn.", "Every evening we eat dinner together."),
    ("卫生间里有镜子。", "Wèishēngjiān lǐ yǒu jìngzi.", "There is a mirror in the bathroom."),
    ("窗户开着，空气很好。", "Chuānghu kāi zhe, kōngqì hěn hǎo.", "The window is open; the air is nice."),
    ("墙上挂着一张照片。", "Qiáng shang guà zhe yì zhāng zhàopiàn.", "A photo hangs on the wall."),
    ("我爱我的家庭。", "Wǒ ài wǒ de jiātíng.", "I love my family."),
    ("弟弟今年十岁。", "Dìdi jīnnián shí suì.", "Younger brother is ten years old this year."),
    ("姐姐在大学读书。", "Jiějie zài dàxué dú shū.", "Older sister studies at university."),
    ("周末我们打扫房间。", "Zhōumò wǒmen dǎsǎo fángjiān.", "On weekends we clean the rooms."),
]

FOOD_SENT = [
    ("我喜欢吃中国菜。", "Wǒ xǐhuan chī Zhōngguó cài.", "I like eating Chinese food."),
    ("早饭我吃面包和鸡蛋。", "Zǎofàn wǒ chī miànbāo hé jīdàn.", "For breakfast I eat bread and eggs."),
    ("午饭我们在食堂吃。", "Wǔfàn wǒmen zài shítáng chī.", "We eat lunch in the canteen."),
    ("妈妈做的菜很好吃。", "Māma zuò de cài hěn hǎochī.", "Mom's cooking is delicious."),
    ("请给我一碗米饭。", "Qǐng gěi wǒ yì wǎn mǐfàn.", "Please give me a bowl of rice."),
    ("这碗面太咸了。", "Zhè wǎn miàn tài xián le.", "This bowl of noodles is too salty."),
    ("我想喝一杯茶。", "Wǒ xiǎng hē yì bēi chá.", "I would like a cup of tea."),
    ("服务员，请拿菜单来。", "Fúwùyuán, qǐng ná càidān lái.", "Waiter, please bring the menu."),
    ("我们点四个菜吧。", "Wǒmen diǎn sì ge cài ba.", "Let's order four dishes."),
    ("这个菜有点辣。", "Zhège cài yǒudiǎn là.", "This dish is a bit spicy."),
    ("你吃过北京烤鸭吗？", "Nǐ chī guo Běijīng kǎoyā ma?", "Have you ever eaten Beijing roast duck?"),
    ("我对花生过敏。", "Wǒ duì huāshēng guòmǐn.", "I am allergic to peanuts."),
    ("请少放一点盐。", "Qǐng shǎo fàng yìdiǎn yán.", "Please use a little less salt."),
    ("水果很新鲜。", "Shuǐguǒ hěn xīnxiān.", "The fruit is very fresh."),
    ("他在学做包子。", "Tā zài xué zuò bāozi.", "He is learning to make steamed buns."),
    ("先把油烧热。", "Xiān bǎ yóu shāo rè.", "First heat the oil."),
    ("把菜切成小块。", "Bǎ cài qiē chéng xiǎo kuài.", "Cut the vegetables into small pieces."),
    ("晚饭六点开始。", "Wǎnfàn liù diǎn kāishǐ.", "Dinner starts at six."),
    ("吃饱了吗？", "Chī bǎo le ma?", "Have you eaten your fill?"),
    ("谢谢款待！", "Xièxie kuǎndài!", "Thanks for the treat!"),
]

TRAVEL_SENT = [
    ("请问，火车站在哪里？", "Qǐngwèn, huǒchēzhàn zài nǎlǐ?", "Excuse me, where is the train station?"),
    ("一直往前走。", "Yìzhí wǎng qián zǒu.", "Go straight ahead."),
    ("在第二个路口左转。", "Zài dì èr ge lùkǒu zuǒ zhuǎn.", "Turn left at the second intersection."),
    ("地铁站在右边。", "Dìtiězhàn zài yòubian.", "The subway station is on the right."),
    ("离这里远吗？", "Lí zhèlǐ yuǎn ma?", "Is it far from here?"),
    ("走路大概十分钟。", "Zǒu lù dàgài shí fēnzhōng.", "About ten minutes on foot."),
    ("我想买一张去北京的票。", "Wǒ xiǎng mǎi yì zhāng qù Běijīng de piào.", "I want to buy a ticket to Beijing."),
    ("火车几点开？", "Huǒchē jǐ diǎn kāi?", "What time does the train leave?"),
    ("飞机晚点了。", "Fēijī wǎndiǎn le.", "The flight is delayed."),
    ("请帮我叫一辆出租车。", "Qǐng bāng wǒ jiào yí liàng chūzūchē.", "Please help me call a taxi."),
    ("去机场多少钱？", "Qù jīchǎng duōshao qián?", "How much to the airport?"),
    ("请打表。", "Qǐng dǎ biǎo.", "Please use the meter."),
    ("在这儿下车。", "Zài zhèr xià chē.", "Get off here."),
    ("我预订了一个房间。", "Wǒ yùdìng le yí ge fángjiān.", "I booked a room."),
    ("有空房吗？", "Yǒu kòng fáng ma?", "Do you have any vacancies?"),
    ("我要住三天。", "Wǒ yào zhù sān tiān.", "I will stay three days."),
    ("早餐包括在内吗？", "Zǎocān bāokuò zài nèi ma?", "Is breakfast included?"),
    ("请给我地图。", "Qǐng gěi wǒ dìtú.", "Please give me a map."),
    ("洗手间在哪里？", "Xǐshǒujiān zài nǎlǐ?", "Where is the restroom?"),
    ("祝你旅途愉快！", "Zhù nǐ lǚtú yúkuài!", "Have a pleasant trip!"),
]

WORK_SENT = [
    ("我在一家公司工作。", "Wǒ zài yì jiā gōngsī gōngzuò.", "I work at a company."),
    ("他是工程师。", "Tā shì gōngchéngshī.", "He is an engineer."),
    ("我们九点开会。", "Wǒmen jiǔ diǎn kāi huì.", "We have a meeting at nine."),
    ("这个项目下周完成。", "Zhège xiàngmù xià zhōu wánchéng.", "This project finishes next week."),
    ("请把报告发给我。", "Qǐng bǎ bàogào fā gěi wǒ.", "Please send me the report."),
    ("老板很满意。", "Lǎobǎn hěn mǎnyì.", "The boss is very satisfied."),
    ("我在学校学习中文。", "Wǒ zài xuéxiào xuéxí Zhōngwén.", "I study Chinese at school."),
    ("明天有考试。", "Míngtiān yǒu kǎoshì.", "There is an exam tomorrow."),
    ("老师布置了很多作业。", "Lǎoshī bùzhì le hěn duō zuòyè.", "The teacher assigned a lot of homework."),
    ("这道题怎么做？", "Zhè dào tí zěnme zuò?", "How do you do this problem?"),
    ("我的成绩进步了。", "Wǒ de chéngjì jìnbù le.", "My grades have improved."),
    ("图书馆八点开门。", "Túshūguǎn bā diǎn kāi mén.", "The library opens at eight."),
    ("同学们在认真听讲。", "Tóngxuémen zài rènzhēn tīngjiǎng.", "The classmates are listening attentively."),
    ("下课后我们去打球。", "Xià kè hòu wǒmen qù dǎ qiú.", "After class we go play ball."),
    ("我想申请这份工作。", "Wǒ xiǎng shēnqǐng zhè fèn gōngzuò.", "I want to apply for this job."),
    ("工作时间是几点到几点？", "Gōngzuò shíjiān shì jǐ diǎn dào jǐ diǎn?", "What are the working hours?"),
    ("午休一个小时。", "Wǔxiū yí ge xiǎoshí.", "Lunch break is one hour."),
    ("他升职了。", "Tā shēngzhí le.", "He got promoted."),
    ("我们一起努力吧。", "Wǒmen yìqǐ nǔlì ba.", "Let's work hard together."),
    ("下班后你有空吗？", "Xià bān hòu nǐ yǒu kòng ma?", "Are you free after work?"),
]

HEALTH_SENT = [
    ("我头疼。", "Wǒ tóu téng.", "I have a headache."),
    ("他发烧了。", "Tā fāshāo le.", "He has a fever."),
    ("我感冒了。", "Wǒ gǎnmào le.", "I caught a cold."),
    ("我的嗓子疼。", "Wǒ de sǎngzi téng.", "My throat hurts."),
    ("你哪里不舒服？", "Nǐ nǎlǐ bù shūfu?", "Where do you feel unwell?"),
    ("我肚子疼。", "Wǒ dùzi téng.", "My stomach hurts."),
    ("请多喝水。", "Qǐng duō hē shuǐ.", "Please drink more water."),
    ("你需要多休息。", "Nǐ xūyào duō xiūxi.", "You need more rest."),
    ("每天锻炼身体。", "Měitiān duànliàn shēntǐ.", "Exercise every day."),
    ("他去看医生了。", "Tā qù kàn yīshēng le.", "He went to see a doctor."),
    ("医生说没事。", "Yīshēng shuō méi shì.", "The doctor said it is nothing serious."),
    ("请按时吃药。", "Qǐng ànshí chī yào.", "Please take your medicine on time."),
    ("药店在哪里？", "Yàodiàn zài nǎlǐ?", "Where is the pharmacy?"),
    ("我想买感冒药。", "Wǒ xiǎng mǎi gǎnmào yào.", "I want to buy cold medicine."),
    ("你的眼睛很红。", "Nǐ de yǎnjing hěn hóng.", "Your eyes are very red."),
    ("小心别着凉。", "Xiǎoxīn bié zháoliáng.", "Be careful not to catch cold."),
    ("早睡早起身体好。", "Zǎo shuì zǎo qǐ shēntǐ hǎo.", "Early to bed and early to rise is good for health."),
    ("他跑步扭伤了脚。", "Tā pǎobù niǔshāng le jiǎo.", "He sprained his ankle running."),
    ("多吃蔬菜水果。", "Duō chī shūcài shuǐguǒ.", "Eat more vegetables and fruit."),
    ("祝你早日康复！", "Zhù nǐ zǎorì kāngfù!", "Wish you a speedy recovery!"),
]

EMOTION_SENT = [
    ("我今天很开心。", "Wǒ jīntiān hěn kāixīn.", "I am very happy today."),
    ("听到这个消息，他很高兴。", "Tīngdào zhège xiāoxi, tā hěn gāoxìng.", "Hearing the news, he was delighted."),
    ("她难过得哭了。", "Tā nánguò de kū le.", "She cried from sadness."),
    ("别担心，一切都会好的。", "Bié dānxīn, yíqiè dōu huì hǎo de.", "Do not worry; everything will be fine."),
    ("我有点紧张。", "Wǒ yǒudiǎn jǐnzhāng.", "I am a bit nervous."),
    ("他生气了。", "Tā shēngqì le.", "He got angry."),
    ("冷静一点。", "Lěngjìng yìdiǎn.", "Calm down a bit."),
    ("我感到很惊讶。", "Wǒ gǎndào hěn jīngyà.", "I feel very surprised."),
    ("这部电影很感人。", "Zhè bù diànyǐng hěn gǎnrén.", "This movie is very touching."),
    ("我爱你。", "Wǒ ài nǐ.", "I love you."),
    ("他害怕黑。", "Tā hàipà hēi.", "He is afraid of the dark."),
    ("别害怕，我在这里。", "Bié hàipà, wǒ zài zhèlǐ.", "Do not be afraid; I am here."),
    ("我为你感到骄傲。", "Wǒ wèi nǐ gǎndào jiāoào.", "I am proud of you."),
    ("他觉得很孤单。", "Tā juéde hěn gūdān.", "He feels very lonely."),
    ("放松一下吧。", "Fàngsōng yíxià ba.", "Relax a bit."),
    ("我很想念家人。", "Wǒ hěn xiǎngniàn jiārén.", "I miss my family very much."),
    ("这个笑话真好笑。", "Zhège xiàohua zhēn hǎoxiào.", "This joke is really funny."),
    ("他害羞地笑了。", "Tā hàixiū de xiào le.", "He smiled shyly."),
    ("保持乐观！", "Bǎochí lèguān!", "Stay optimistic!"),
    ("心情不好的时候，去散散步。", "Xīnqíng bù hǎo de shíhou, qù sànsan bù.", "When you feel down, go for a walk."),
]

NATURE_SENT = [
    ("今天天气很好。", "Jīntiān tiānqì hěn hǎo.", "The weather is nice today."),
    ("天空很蓝。", "Tiānkōng hěn lán.", "The sky is very blue."),
    ("太阳出来了。", "Tàiyang chūlái le.", "The sun has come out."),
    ("外面在下雨。", "Wàimian zài xià yǔ.", "It is raining outside."),
    ("明天会下雪吗？", "Míngtiān huì xià xuě ma?", "Will it snow tomorrow?"),
    ("风很大。", "Fēng hěn dà.", "The wind is strong."),
    ("春天花开了。", "Chūntiān huā kāi le.", "Flowers bloom in spring."),
    ("秋天树叶黄了。", "Qiūtiān shùyè huáng le.", "Leaves turn yellow in autumn."),
    ("山上有很多树。", "Shān shang yǒu hěn duō shù.", "There are many trees on the mountain."),
    ("河里有鱼。", "Hé lǐ yǒu yú.", "There are fish in the river."),
    ("这只鸟很漂亮。", "Zhè zhī niǎo hěn piàoliang.", "This bird is beautiful."),
    ("夏天很热，冬天很冷。", "Xiàtiān hěn rè, dōngtiān hěn lěng.", "Summer is hot, winter is cold."),
    ("今天多少度？", "Jīntiān duōshao dù?", "What is the temperature today?"),
    ("出门记得带伞。", "Chūmén jìde dài sǎn.", "Remember to take an umbrella when going out."),
    ("彩虹出来了！", "Cǎihóng chūlái le!", "A rainbow has appeared!"),
    ("海很蓝，很美。", "Hǎi hěn lán, hěn měi.", "The sea is blue and beautiful."),
    ("草地上有小兔子。", "Cǎodì shang yǒu xiǎo tùzi.", "There are little rabbits on the grass."),
    ("夜晚星星很多。", "Yèwǎn xīngxing hěn duō.", "There are many stars at night."),
    ("空气很新鲜。", "Kōngqì hěn xīnxiān.", "The air is very fresh."),
    ("保护环境，人人有责。", "Bǎohù huánjìng, rénrén yǒu zé.", "Protecting the environment is everyone's duty."),
]

SHOP_SENT = [
    ("我想去买东西。", "Wǒ xiǎng qù mǎi dōngxi.", "I want to go shopping."),
    ("商店几点开门？", "Shāngdiàn jǐ diǎn kāi mén?", "What time does the shop open?"),
    ("这个多少钱？", "Zhège duōshao qián?", "How much is this?"),
    ("太贵了，便宜一点吧。", "Tài guì le, piányi yìdiǎn ba.", "Too expensive; make it cheaper."),
    ("可以打折吗？", "Kěyǐ dǎzhé ma?", "Can you give a discount?"),
    ("我只带了一百块。", "Wǒ zhǐ dài le yìbǎi kuài.", "I only brought 100 yuan."),
    ("能刷卡吗？", "Néng shuākǎ ma?", "Can I pay by card?"),
    ("我用手机支付。", "Wǒ yòng shǒujī zhīfù.", "I will pay by phone."),
    ("请给我发票。", "Qǐng gěi wǒ fāpiào.", "Please give me a receipt."),
    ("这件有大号的吗？", "Zhè jiàn yǒu dà hào de ma?", "Do you have this in large?"),
    ("我想试穿一下。", "Wǒ xiǎng shìchuān yíxià.", "I would like to try it on."),
    ("试衣间在哪里？", "Shìyījiān zài nǎlǐ?", "Where is the fitting room?"),
    ("颜色有点深，有浅色的吗？", "Yánsè yǒudiǎn shēn, yǒu qiǎn sè de ma?", "The color is a bit dark; do you have a lighter one?"),
    ("质量很好。", "Zhìliàng hěn hǎo.", "The quality is very good."),
    ("我再看看。", "Wǒ zài kànkan.", "I will look around some more."),
    ("可以退换吗？", "Kěyǐ tuìhuàn ma?", "Can I return or exchange it?"),
    ("打八折是多少？", "Dǎ bā zhé shì duōshao?", "How much is 20 percent off?"),
    ("买二送一。", "Mǎi èr sòng yī.", "Buy two, get one free."),
    ("找您二十块。", "Zhǎo nín èrshí kuài.", "Here is your 20 yuan change."),
    ("谢谢光临！", "Xièxie guānglín!", "Thanks for coming!"),
]

FRIEND_SENT = [
    ("很高兴认识你。", "Hěn gāoxìng rènshi nǐ.", "Nice to meet you."),
    ("我们是好朋友。", "Wǒmen shì hǎo péngyou.", "We are good friends."),
    ("周末有空吗？", "Zhōumò yǒu kòng ma?", "Are you free this weekend?"),
    ("我们一起去看电影吧。", "Wǒmen yìqǐ qù kàn diànyǐng ba.", "Let's go see a movie together."),
    ("好啊，几点见？", "Hǎo a, jǐ diǎn jiàn?", "Sounds good; what time?"),
    ("这是我的电话号码。", "Zhè shì wǒ de diànhuà hàomǎ.", "This is my phone number."),
    ("常联系！", "Cháng liánxì!", "Keep in touch!"),
    ("生日快乐！", "Shēngrì kuàilè!", "Happy birthday!"),
    ("恭喜你找到新工作！", "Gōngxǐ nǐ zhǎodào xīn gōngzuò!", "Congrats on the new job!"),
    ("谢谢你的礼物。", "Xièxie nǐ de lǐwù.", "Thanks for your gift."),
    ("不客气，应该的。", "Bú kèqi, yīnggāi de.", "You're welcome; it's nothing."),
    ("有空来我家玩。", "Yǒu kòng lái wǒ jiā wán.", "Come visit my place when free."),
    ("好久不见，你好吗？", "Hǎo jiǔ bú jiàn, nǐ hǎo ma?", "Long time no see; how are you?"),
    ("我很好，你呢？", "Wǒ hěn hǎo, nǐ ne?", "I'm fine; and you?"),
    ("听说你搬家了。", "Tīngshuō nǐ bān jiā le.", "I heard you moved."),
    ("是啊，欢迎来做客。", "Shì a, huānyíng lái zuòkè.", "Yes; welcome to visit."),
    ("我们是老同学。", "Wǒmen shì lǎo tóngxué.", "We are old classmates."),
    ("十年没见了！", "Shí nián méi jiàn le!", "Haven't seen you in ten years!"),
    ("以后多聚聚。", "Yǐhòu duō jùju.", "Let's get together more."),
    ("朋友一生一起走。", "Péngyou yìshēng yìqǐ zǒu.", "Friends walk together for life."),
]

TECH_SENT = [
    ("我的手机没电了。", "Wǒ de shǒujī méi diàn le.", "My phone is out of battery."),
    ("有充电器吗？", "Yǒu chōngdiànqì ma?", "Do you have a charger?"),
    ("这里有无线网吗？", "Zhèlǐ yǒu wúxiàn wǎng ma?", "Is there Wi-Fi here?"),
    ("密码是多少？", "Mìmǎ shì duōshao?", "What is the password?"),
    ("我发你一条消息。", "Wǒ fā nǐ yì tiáo xiāoxi.", "I'll send you a message."),
    ("你收到我的邮件了吗？", "Nǐ shōudào wǒ de yóujiàn le ma?", "Did you get my email?"),
    ("电脑死机了。", "Diànnǎo sǐjī le.", "The computer froze."),
    ("重启一下试试。", "Chóngqǐ yíxià shìshi.", "Try restarting it."),
    ("这个软件很好用。", "Zhège ruǎnjiàn hěn hǎoyòng.", "This software is very user-friendly."),
    ("请下载这个应用。", "Qǐng xiàzài zhège yìngyòng.", "Please download this app."),
    ("扫码加我好友。", "Sǎo mǎ jiā wǒ hǎoyǒu.", "Scan the code to add me as a friend."),
    ("我们在群里说。", "Wǒmen zài qún lǐ shuō.", "Let's talk in the group chat."),
    ("视频通话更清楚。", "Shìpín tōnghuà gèng qīngchu.", "Video calls are clearer."),
    ("你的网速很快。", "Nǐ de wǎngsù hěn kuài.", "Your internet is fast."),
    ("我把照片发给你。", "Wǒ bǎ zhàopiàn fā gěi nǐ.", "I'll send you the photos."),
    ("别信陌生短信。", "Bié xìn mòshēng duǎnxìn.", "Don't trust texts from strangers."),
    ("记得备份文件。", "Jìde bèifèn wénjiàn.", "Remember to back up your files."),
    ("这个网站打不开。", "Zhège wǎngzhàn dǎ bu kāi.", "This website won't open."),
    ("换个浏览器试试。", "Huàn ge liúlǎnqì shìshi.", "Try a different browser."),
    ("科技改变生活。", "Kējì gǎibiàn shēnghuó.", "Technology changes life."),
]


def _sent_lines(sents):
    return "\n".join(
        "%d. %s\n   %s\n   %s" % (i + 1, c, p, e)
        for i, (c, p, e) in enumerate(sents))


# measure words for the record-11 demo: (measure, pinyin, used_with)
MEASURE_WORDS = [
    ("个", "ge", "general nouns: 一个人"),
    ("本", "běn", "bound volumes: 一本书"),
    ("张", "zhāng", "flat objects: 一张纸"),
    ("把", "bǎ", "handled objects: 一把伞"),
    ("只", "zhī", "animals: 一只猫"),
    ("条", "tiáo", "long thin things: 一条鱼"),
    ("件", "jiàn", "clothing: 一件衣服"),
    ("双", "shuāng", "pairs: 一双鞋"),
    ("辆", "liàng", "vehicles: 一辆车"),
    ("间", "jiān", "rooms: 一间房子"),
]

# restaurant bill data for the record-12 demo: (chars, pinyin, price_yuan)
DISHES = [
    ("宫保鸡丁", "gōngbǎo jīdīng", 38.0),
    ("麻婆豆腐", "mápó dòufu", 22.0),
    ("番茄炒蛋", "fānqié chǎo dàn", 18.0),
    ("米饭", "mǐfàn", 3.0),
    ("可乐", "kělè", 6.0),
]

# Q&A pairs for record 22: (q_chars, q_pinyin, q_en, a_chars, a_pinyin, a_en)
QA_PAIRS = [
    ("你叫什么名字？", "Nǐ jiào shénme míngzi?", "What is your name?",
     "我叫小明。", "Wǒ jiào Xiǎo Míng.", "My name is Xiaoming."),
    ("你是哪国人？", "Nǐ shì nǎ guó rén?", "Which country are you from?",
     "我是中国人。", "Wǒ shì Zhōngguó rén.", "I am Chinese."),
    ("你多大了？", "Nǐ duō dà le?", "How old are you?",
     "我二十岁。", "Wǒ èrshí suì.", "I am twenty."),
    ("你住在哪里？", "Nǐ zhù zài nǎlǐ?", "Where do you live?",
     "我住在北京。", "Wǒ zhù zài Běijīng.", "I live in Beijing."),
    ("你是学生吗？", "Nǐ shì xuésheng ma?", "Are you a student?",
     "是的，我是学生。", "Shì de, wǒ shì xuésheng.", "Yes, I am a student."),
    ("你喜欢中文吗？", "Nǐ xǐhuan Zhōngwén ma?", "Do you like Chinese?",
     "很喜欢。", "Hěn xǐhuan.", "I like it a lot."),
    ("你学了多久？", "Nǐ xué le duō jiǔ?", "How long have you studied?",
     "学了一年。", "Xué le yì nián.", "One year."),
    ("今天星期几？", "Jīntiān xīngqī jǐ?", "What day is it today?",
     "今天星期六。", "Jīntiān xīngqī liù.", "Today is Saturday."),
    ("现在几点？", "Xiànzài jǐ diǎn?", "What time is it now?",
     "现在三点。", "Xiànzài sān diǎn.", "It is three o'clock."),
    ("你去哪里？", "Nǐ qù nǎlǐ?", "Where are you going?",
     "我去学校。", "Wǒ qù xuéxiào.", "I am going to school."),
    ("你吃什么？", "Nǐ chī shénme?", "What are you eating?",
     "我吃面条。", "Wǒ chī miàntiáo.", "I am eating noodles."),
    ("谁是你的老师？", "Shéi shì nǐ de lǎoshī?", "Who is your teacher?",
     "王老师是我的老师。", "Wáng lǎoshī shì wǒ de lǎoshī.", "Teacher Wang is my teacher."),
    ("这个多少钱？", "Zhège duōshao qián?", "How much is this?",
     "五十块。", "Wǔshí kuài.", "Fifty yuan."),
    ("你为什么学中文？", "Nǐ wèishénme xué Zhōngwén?", "Why do you learn Chinese?",
     "因为我喜欢中国文化。", "Yīnwèi wǒ xǐhuan Zhōngguó wénhuà.", "Because I like Chinese culture."),
    ("你怎么来学校的？", "Nǐ zěnme lái xuéxiào de?", "How do you get to school?",
     "我坐地铁来。", "Wǒ zuò dìtiě lái.", "I come by subway."),
    ("你有兄弟姐妹吗？", "Nǐ yǒu xiōngdì jiěmèi ma?", "Do you have siblings?",
     "有一个妹妹。", "Yǒu yí ge mèimei.", "I have one younger sister."),
    ("明天有空吗？", "Míngtiān yǒu kòng ma?", "Are you free tomorrow?",
     "有空。", "Yǒu kòng.", "Yes, I am free."),
    ("你会说英语吗？", "Nǐ huì shuō Yīngyǔ ma?", "Can you speak English?",
     "会一点。", "Huì yìdiǎn.", "A little."),
    ("哪一本是你的？", "Nǎ yì běn shì nǐ de?", "Which one is yours?",
     "红色的是我的。", "Hóngsè de shì wǒ de.", "The red one is mine."),
    ("你觉得中文难吗？", "Nǐ juéde Zhōngwén nán ma?", "Do you find Chinese hard?",
     "有一点难，但是很有意思。", "Yǒu yìdiǎn nán, dànshì hěn yǒu yìsi.", "A bit hard, but very interesting."),
]

# commands for record 23: (chars, pinyin, english, register)
COMMANDS = [
    ("坐下。", "Zuò xia.", "Sit down.", "informal direct"),
    ("请坐。", "Qǐng zuò.", "Please sit.", "polite"),
    ("开门！", "Kāi mén!", "Open the door!", "direct"),
    ("请把门打开。", "Qǐng bǎ mén dǎkāi.", "Please open the door.", "polite"),
    ("快点！", "Kuài diǎn!", "Hurry!", "urgent informal"),
    ("麻烦您快一点。", "Máfan nín kuài yìdiǎn.", "Please hurry a little.", "polite"),
    ("别说话！", "Bié shuō huà!", "Do not talk!", "stern"),
    ("请安静。", "Qǐng ānjìng.", "Please be quiet.", "polite"),
    ("给我水。", "Gěi wǒ shuǐ.", "Give me water.", "blunt"),
    ("请给我一杯水。", "Qǐng gěi wǒ yì bēi shuǐ.", "Please give me a glass of water.", "polite"),
    ("过来！", "Guòlái!", "Come here!", "informal"),
    ("请过来一下。", "Qǐng guòlái yíxià.", "Please come here a moment.", "polite"),
    ("请小声一点。", "Qǐng xiǎo shēng yìdiǎn.", "Please lower your voice.", "polite"),
    ("帮我一下。", "Bāng wǒ yíxià.", "Help me.", "casual"),
    ("能帮我一个忙吗？", "Néng bāng wǒ yí ge máng ma?", "Could you do me a favor?", "polite"),
    ("写下来。", "Xiě xialai.", "Write it down.", "direct"),
    ("麻烦您写一下。", "Máfan nín xiě yíxià.", "Please write it down.", "polite"),
    ("等我！", "Děng wǒ!", "Wait for me!", "informal"),
    ("请稍等。", "Qǐng shāo děng.", "Please wait a moment.", "polite"),
    ("别客气，随便吃。", "Bié kèqi, suíbiàn chī.", "Do not stand on ceremony; eat freely.", "warm informal"),
]

# descriptions for record 24
DESCRIBE_SENT = [
    ("她有一头长长的黑发。", "Tā yǒu yì tóu chángcháng de hēi fà.", "She has long black hair."),
    ("他个子很高，戴着眼镜。", "Tā gèzi hěn gāo, dài zhe yǎnjìng.", "He is tall and wears glasses."),
    ("这座城市又大又热闹。", "Zhè zuò chéngshì yòu dà yòu rènao.", "This city is big and lively."),
    ("长城很长，很壮观。", "Chángchéng hěn cháng, hěn zhuàngguān.", "The Great Wall is long and magnificent."),
    ("今天的晚霞真美。", "Jīntiān de wǎnxiá zhēn měi.", "Tonight's sunset clouds are truly beautiful."),
    ("这件红色的裙子很漂亮。", "Zhè jiàn hóngsè de qúnzi hěn piàoliang.", "This red dress is very pretty."),
    ("他的声音很温柔。", "Tā de shēngyīn hěn wēnróu.", "His voice is very gentle."),
    ("小狗的眼睛又大又圆。", "Xiǎo gǒu de yǎnjing yòu dà yòu yuán.", "The puppy's eyes are big and round."),
    ("这家餐厅干净又安静。", "Zhè jiā cāntīng gānjìng yòu ānjìng.", "This restaurant is clean and quiet."),
    ("山顶的风景美极了。", "Shāndǐng de fēngjǐng měi jí le.", "The view from the mountaintop is extremely beautiful."),
    ("她笑起来有两个酒窝。", "Tā xiào qilai yǒu liǎng ge jiǔwō.", "She has two dimples when she smiles."),
    ("老人满头白发。", "Lǎorén mǎn tóu bái fà.", "The old man has a full head of white hair."),
    ("这个房间又宽敞又明亮。", "Zhège fángjiān yòu kuānchang yòu míngliàng.", "This room is spacious and bright."),
    ("夜晚的城市灯火辉煌。", "Yèwǎn de chéngshì dēnghuǒ huīhuáng.", "The city at night glitters with lights."),
    ("他的字写得很工整。", "Tā de zì xiě de hěn gōngzhěng.", "His handwriting is very neat."),
    ("这首歌旋律优美。", "Zhè shǒu gē xuánlǜ yōuměi.", "This song has a graceful melody."),
    ("小宝宝的脸胖乎乎的。", "Xiǎo bǎobao de liǎn pànghūhū de.", "The baby's face is chubby."),
    ("沙漠又干又热。", "Shāmò yòu gān yòu rè.", "The desert is dry and hot."),
    ("她的普通话说得很标准。", "Tā de pǔtōnghuà shuō de hěn biāozhǔn.", "Her Mandarin is very standard."),
    ("这是一个美丽而古老的国家。", "Zhè shì yí ge měilì ér gǔlǎo de guójiā.", "This is a beautiful and ancient country."),
]

# aspect groups for record 21: (label, sentences[(chars,pinyin,english)])
ASPECT_GROUPS = [
    ("Present and habitual (no particle; time words carry tense)", [
        ("我每天跑步。", "Wǒ měitiān pǎobù.", "I run every day."),
        ("他喜欢喝茶。", "Tā xǐhuan hē chá.", "He likes drinking tea."),
        ("我在看书。", "Wǒ zài kàn shū.", "I am reading a book."),
        ("她正在做饭。", "Tā zhèngzài zuò fàn.", "She is cooking right now."),
        ("我们学中文。", "Wǒmen xué Zhōngwén.", "We study Chinese."),
    ]),
    ("Past completed (了 le)", [
        ("我吃了早饭。", "Wǒ chī le zǎofàn.", "I ate breakfast."),
        ("他昨天来了。", "Tā zuótiān lái le.", "He came yesterday."),
        ("我们看完电影了。", "Wǒmen kàn wán diànyǐng le.", "We finished watching the movie."),
        ("她买了一本书。", "Tā mǎi le yì běn shū.", "She bought a book."),
        ("下雨了。", "Xià yǔ le.", "It started raining."),
    ]),
    ("Experiential past (过 guo: have done before)", [
        ("我去过北京。", "Wǒ qù guo Běijīng.", "I have been to Beijing."),
        ("你吃过饺子吗？", "Nǐ chī guo jiǎozi ma?", "Have you ever eaten dumplings?"),
        ("他看过这部电影。", "Tā kàn guo zhè bù diànyǐng.", "He has seen this movie."),
        ("我没坐过飞机。", "Wǒ méi zuò guo fēijī.", "I have never flown."),
        ("她学过钢琴。", "Tā xué guo gāngqín.", "She studied piano before."),
    ]),
    ("Ongoing state (着 zhe)", [
        ("门开着。", "Mén kāi zhe.", "The door is open."),
        ("他穿着红衣服。", "Tā chuān zhe hóng yīfu.", "He is wearing red."),
        ("墙上挂着画。", "Qiáng shang guà zhe huà.", "A painting hangs on the wall."),
        ("孩子们笑着跑着。", "Háizimen xiào zhe pǎo zhe.", "The children run along laughing."),
        ("灯亮着。", "Dēng liàng zhe.", "The light is on."),
    ]),
    ("Future (会 / 要 / 将)", [
        ("明天会下雨。", "Míngtiān huì xià yǔ.", "It will rain tomorrow."),
        ("我要去中国。", "Wǒ yào qù Zhōngguó.", "I am going to China."),
        ("他会说中文。", "Tā huì shuō Zhōngwén.", "He can speak Chinese."),
        ("我们将努力学习。", "Wǒmen jiāng nǔlì xuéxí.", "We will study hard."),
        ("火车要开了。", "Huǒchē yào kāi le.", "The train is about to leave."),
    ]),
]

# dialogues for records 31-33: (speaker, chars, pinyin, english)
DIALOG_MARKET = [
    ("A", "你好！", "Nǐ hǎo!", "Hello!"),
    ("B", "你好！买点什么？", "Nǐ hǎo! Mǎi diǎn shénme?", "Hello! What would you like to buy?"),
    ("A", "苹果怎么卖？", "Píngguǒ zěnme mài?", "How are the apples priced?"),
    ("B", "十块钱三斤。", "Shí kuài qián sān jīn.", "Ten yuan for three jin."),
    ("A", "有点贵，能便宜点吗？", "Yǒudiǎn guì, néng piányi diǎn ma?", "A bit pricey; can you go lower?"),
    ("B", "已经很便宜了，都是新鲜的。", "Yǐjīng hěn piányi le, dōu shì xīnxiān de.", "Already very cheap; all fresh."),
    ("A", "那我买三斤。", "Nà wǒ mǎi sān jīn.", "Then I will take three jin."),
    ("B", "好嘞！还要别的吗？", "Hǎo lei! Hái yào bié de ma?", "Great! Anything else?"),
    ("A", "香蕉多少钱一斤？", "Xiāngjiāo duōshao qián yì jīn?", "How much per jin for bananas?"),
    ("B", "六块。", "Liù kuài.", "Six yuan."),
    ("A", "来两斤香蕉。", "Lái liǎng jīn xiāngjiāo.", "Two jin of bananas."),
    ("B", "一共二十二块。", "Yígòng èrshíèr kuài.", "Twenty-two in total."),
    ("A", "能刷卡吗？", "Néng shuākǎ ma?", "Can I pay by card?"),
    ("B", "可以，也能手机支付。", "Kěyǐ, yě néng shǒujī zhīfù.", "Yes; phone pay works too."),
    ("A", "我手机支付。", "Wǒ shǒujī zhīfù.", "I will pay by phone."),
    ("B", "扫这个码。", "Sǎo zhège mǎ.", "Scan this code."),
    ("A", "好了，付完了。", "Hǎo le, fù wán le.", "Done, paid."),
    ("B", "给你袋子，拿好。", "Gěi nǐ dàizi, ná hǎo.", "Here is a bag; hold it well."),
    ("A", "谢谢！", "Xièxie!", "Thanks!"),
    ("B", "不客气，慢走！", "Bú kèqi, màn zǒu!", "You are welcome; take care!"),
]

DIALOG_FRIEND = [
    ("小明", "小红！好久不见！", "Xiǎo Hóng! Hǎo jiǔ bú jiàn!", "Xiaohong! Long time no see!"),
    ("小红", "小明！真的是你！", "Xiǎo Míng! Zhēn shì nǐ!", "Xiaoming! It is really you!"),
    ("小明", "你最近怎么样？", "Nǐ zuìjìn zěnmeyàng?", "How have you been lately?"),
    ("小红", "挺好的，你呢？", "Tǐng hǎo de, nǐ ne?", "Pretty good; and you?"),
    ("小明", "我也不错。对了，你还在那家公司吗？", "Wǒ yě búcuò. Duì le, nǐ hái zài nà jiā gōngsī ma?", "I am fine too. By the way, still at that company?"),
    ("小红", "在啊，已经三年了。", "Zài a, yǐjīng sān nián le.", "Yes, three years now."),
    ("小明", "真厉害！周末有空吗？", "Zhēn lìhai! Zhōumò yǒu kòng ma?", "Impressive! Free this weekend?"),
    ("小红", "有空，怎么了？", "Yǒu kòng, zěnme le?", "I am free; what is up?"),
    ("小明", "我们几个老同学聚一下。", "Wǒmen jǐ ge lǎo tóngxué jù yíxià.", "A few old classmates are getting together."),
    ("小红", "太好了！在哪儿？", "Tài hǎo le! Zài nǎr?", "Wonderful! Where?"),
    ("小明", "在市中心那家火锅店。", "Zài shì zhōngxīn nà jiā huǒguō diàn.", "At that hotpot place downtown."),
    ("小红", "几点？", "Jǐ diǎn?", "What time?"),
    ("小明", "周六晚上六点。", "Zhōu liù wǎnshang liù diǎn.", "Saturday at six in the evening."),
    ("小红", "没问题，我一定去。", "Méi wèntí, wǒ yídìng qù.", "No problem; I will be there."),
    ("小明", "对了，这是我电话。", "Duì le, zhè shì wǒ diànhuà.", "By the way, here is my number."),
    ("小红", "我存一下。", "Wǒ cún yíxià.", "Let me save it."),
    ("小明", "那周六见！", "Nà zhōu liù jiàn!", "See you Saturday!"),
    ("小红", "周六见！", "Zhōu liù jiàn!", "See you Saturday!"),
    ("小明", "路上小心！", "Lù shang xiǎoxīn!", "Be careful on the road!"),
    ("小红", "你也是，拜拜！", "Nǐ yě shì, báibái!", "You too; bye!"),
]

DIALOG_PROBLEM = [
    ("A", "糟了，水龙头一直在漏水。", "Zāo le, shuǐlóngtóu yìzhí zài lòu shuǐ.", "Oh no, the faucet keeps leaking."),
    ("B", "我看看。", "Wǒ kànkan.", "Let me look."),
    ("A", "从昨天晚上就开始了。", "Cóng zuótiān wǎnshang jiù kāishǐ le.", "It started last night."),
    ("B", "可能是垫圈坏了。", "Kěnéng shì diànquān huài le.", "Probably the washer is broken."),
    ("A", "那怎么办？", "Nà zěnme bàn?", "What should we do?"),
    ("B", "先把水阀关掉。", "Xiān bǎ shuǐfá guāndiào.", "First turn off the water valve."),
    ("A", "水阀在哪里？", "Shuǐfá zài nǎlǐ?", "Where is the valve?"),
    ("B", "在洗手池下面。", "Zài xǐshǒuchí xiamian.", "Under the sink."),
    ("A", "关掉了，现在不漏了。", "Guān diào le, xiànzài bú lòu le.", "Turned off; it is not leaking now."),
    ("B", "我们需要买个新垫圈。", "Wǒmen xūyào mǎi ge xīn diànquān.", "We need to buy a new washer."),
    ("A", "楼下就有五金店。", "Lóuxia jiù yǒu wǔjīn diàn.", "There is a hardware store downstairs."),
    ("B", "我去买，你在家等。", "Wǒ qù mǎi, nǐ zài jiā děng.", "I will go buy it; you wait at home."),
    ("A", "要我一起去吗？", "Yào wǒ yìqǐ qù ma?", "Want me to come along?"),
    ("B", "不用，十分钟就回来。", "Bú yòng, shí fēnzhōng jiù huílai.", "No need; back in ten minutes."),
    ("A", "好，路上小心。", "Hǎo, lù shang xiǎoxīn.", "OK, be careful on the road."),
    ("B", "买到了，还买了扳手。", "Mǎi dào le, hái mǎi le bānshou.", "Got it, and bought a wrench too."),
    ("A", "你会换吗？", "Nǐ huì huàn ma?", "Do you know how to replace it?"),
    ("B", "我看过视频，应该可以。", "Wǒ kàn guo shìpín, yīnggāi kěyǐ.", "I watched a video; should be fine."),
    ("A", "太好了，换好了！", "Tài hǎo le, huàn hǎo le!", "Great, it is replaced!"),
    ("B", "打开水阀试试——不漏了！", "Dǎkāi shuǐfá shìshi — bú lòu le!", "Turn on the valve and test — no leak!"),
]


def _qa_lines():
    return "\n".join(
        "%d. Q: %s\n   %s\n   %s\n   A: %s\n   %s\n   %s"
        % (i + 1, qc, qp, qe, ac, ap, ae)
        for i, (qc, qp, qe, ac, ap, ae) in enumerate(QA_PAIRS))


def _command_lines():
    return "\n".join(
        "%d. %s (%s) - %s [%s]" % (i + 1, c, p, e, r)
        for i, (c, p, e, r) in enumerate(COMMANDS))


def _aspect_lines():
    out = []
    for label, sents in ASPECT_GROUPS:
        out.append(label + ":")
        out.extend("   %d. %s (%s) - %s" % (i + 1, c, p, e)
                   for i, (c, p, e) in enumerate(sents))
    return "\n".join(out)


def _dialog_lines(d):
    return "\n".join(
        "%d. %s: %s\n   %s\n   %s" % (i + 1, s, c, p, e)
        for i, (s, c, p, e) in enumerate(d))

# entries 11-20: themed sentence sets (Compounded tier)
ENTRIES += [
    {
        "key": "home_family",
        "name": "Home and Family Sentences",
        "group": "Daily Life",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "ladder": 11,
        "description": (
            "Twenty sentences about home and family - rooms, furniture, "
            "and family members - each in simplified characters with "
            "pinyin and English. Home vocabulary anchors the learner: "
            "these are the words used every single day.\n"
            + _sent_lines(HOME_SENT)
        ),
        "how_it_works": (
            "Home sentences work by attaching vocabulary to the rooms the "
            "learner already knows. Location words pair with 在: 在客厅 "
            "(in the living room), 在厨房 (in the kitchen), 在卧室 (in "
            "the bedroom). Existence uses 有 with the place first: 桌子上"
            "有书 (on the table there is a book). Family terms are precise "
            "in Mandarin: 哥哥 is older brother, 弟弟 is younger brother - "
            "age order is built into the word, unlike English brother. "
            "Measure words appear naturally: 一间房子 (a room), 一张照片 "
            "(a photo), 一床被子 (a quilt). Read each sentence aloud in "
            "the room it describes; the house becomes a memory palace for "
            "the vocabulary."
        ),
        "key_points": [
            "Location phrases use 在 + place: 在客厅, 在厨房, 在卧室.",
            "Existence sentences put the place first: 桌子上有书.",
            "Family terms encode age order: 哥哥/弟弟, 姐姐/妹妹.",
            "Measure words ride along: 一间房子, 一张照片, 一床被子.",
            "Learn home words in the rooms themselves - the house is a memory palace.",
        ],
        "requirements": [
            "20 sentences on house, rooms, furniture, and family members, each translated.",
            "At least 3 在-location sentences and 3 有-existence sentences.",
            "Both older and younger sibling terms used.",
        ],
        "standards": ["Word selection cross-checked against HSK 1-2 lists."],
        "citations": [CIT_HSK, CIT_LI],
        "sig_lens": (
            "The Signature read: home is the first archive - every room a "
            "shelf, every family member a sealed record. The Signature "
            "Language Method files vocabulary where it lives, so the "
            "learner's own house becomes the database no one can take "
            "away."
        ),
    },
    {
        "key": "food_cooking",
        "name": "Food and Cooking Sentences",
        "group": "Daily Life",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "ladder": 12,
        "description": (
            "Twenty sentences about meals, ingredients, cooking actions, "
            "and restaurants - the vocabulary of eating, which in China is "
            "the vocabulary of caring.\n"
            + _sent_lines(FOOD_SENT)
        ),
        "how_it_works": (
            "Food sentences work through the restaurant script, the most "
            "practiced dialogue in any language: call the server (服务员), "
            "ask for the menu (菜单), order dishes (点菜), comment on "
            "taste (好吃, 太咸了, 有点辣), and close with thanks. Cooking "
            "verbs sequence with 先...然后: 先把油烧热，把菜切成小块. "
            "The 把 construction shines in kitchens - 把门关上, 把菜切成小"
            "块 - because cooking is all about acting on objects. Taste "
            "words pair as opposites: 咸/淡 (salty/bland), 甜/酸 (sweet/"
            "sour), 辣/不辣 (spicy/not). Dietary needs have fixed forms: "
            "我对花生过敏 (allergic to peanuts), 请少放盐 (less salt). "
            "吃了吗 is not about food at all - it is affection in "
            "question form."
        ),
        "key_points": [
            "The restaurant script: 服务员, 菜单, 点菜, comments on taste, thanks.",
            "Cooking sequences use 先 and 把: 先把油烧热, 把菜切成小块.",
            "Taste opposites: 咸/淡, 甜/酸, 辣; degree with 太...了 and 有点.",
            "Dietary needs: 我对...过敏, 请少放... .",
            "吃了吗 is a caring greeting, not a lunch invitation.",
        ],
        "requirements": [
            "20 sentences on meals, ingredients, cooking, and restaurants, each translated.",
            "At least one 把-construction cooking sentence and one allergy/dietary sentence.",
        ],
        "standards": ["Word selection cross-checked against HSK 1-3 lists."],
        "citations": [CIT_HSK, CIT_YIP],
        "sig_lens": (
            "The Signature read: food is the seal of care - every shared "
            "meal presses the family closer. The Signature Language "
            "Method teaches the kitchen first, because the sentences "
            "learned over rice are the ones the heart keeps."
        ),
    },
    {
        "key": "travel",
        "name": "Travel and Directions Sentences",
        "group": "Daily Life",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "ladder": 13,
        "description": (
            "Twenty sentences for moving through China - transport, asking "
            "directions, tickets, and lodging. The traveler's complete "
            "toolkit.\n"
            + _sent_lines(TRAVEL_SENT)
        ),
        "how_it_works": (
            "Travel sentences work on the 请问 opener: 请问，...在哪里？ "
            "unlocks every direction in the country. Direction answers "
            "use a fixed compass: 一直往前走 (straight), 左转/右转 (turn "
            "left/right), 在路口 (at the intersection), 在右边 (on the "
            "right). Distance and time estimates come with 大概 (about) "
            "and the transport word: 走路十分钟, 坐车半小时. Tickets name "
            "the destination with 去: 一张去北京的票. Taxis run on three "
            "lines: 去..., 请打表, 在这儿下车. Hotels run on four: 有空房"
            "吗, 我要住三天, 早餐包括在内吗, 我预订了. Every one of these "
            "is a complete transaction - learn the set and no journey "
            "stalls for language."
        ),
        "key_points": [
            "请问，...在哪里？ is the universal direction opener.",
            "Directions: 一直往前走, 左转/右转, 在路口, 在右边/左边.",
            "Tickets: 一张去...的票; ask time with 几点开.",
            "Taxis: 去..., 请打表, 在这儿下车.",
            "Hotels: 有空房吗, 住三天, 早餐包括在内吗.",
        ],
        "requirements": [
            "20 sentences covering transport, directions, tickets, and lodging, each translated.",
            "At least 3 direction-giving sentences and 2 ticket/hotel transaction sentences.",
        ],
        "standards": ["Word selection cross-checked against HSK 1-3 lists."],
        "citations": [CIT_HSK, CIT_YIP],
        "sig_lens": (
            "The Signature read: every journey is a sentence the traveler "
            "signs with their feet - direction words are the seals that "
            "stamp the route. The Signature Language Method teaches travel "
            "as transactions, each one complete, so the learner is never "
            "stranded mid-sentence."
        ),
    },
    {
        "key": "work_school",
        "name": "Work and School Sentences",
        "group": "Daily Life",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "ladder": 14,
        "description": (
            "Twenty sentences about jobs, the office, the classroom, and "
            "learning - the vocabulary of the working and studying day.\n"
            + _sent_lines(WORK_SENT)
        ),
        "how_it_works": (
            "Work sentences run on institutional nouns with 在: 在公司 "
            "(at the company), 在学校 (at school), 在会议室 (in the "
            "meeting room). Roles are 是 sentences: 他是工程师, 我是学生. "
            "Schedules stack time before the verb: 我们九点开会, 明天有考"
            "试. Requests in offices use 请 + 把: 请把报告发给我. School "
            "sentences orbit 作业, 考试, 成绩 - homework, exams, grades - "
            "with progress marked by 了: 成绩进步了, 他升职了. Questions "
            "about systems use 怎么: 这道题怎么做？ (how is this problem "
            "done?). Career moves use 申请 (apply) and 升职 (promote). "
            "The set covers the full day from 开会 to 下班, from 上课 to "
            "下课."
        ),
        "key_points": [
            "Institutions use 在: 在公司, 在学校; roles use 是: 他是工程师.",
            "Schedules put time before the verb: 我们九点开会.",
            "Office requests: 请 + 把: 请把报告发给我.",
            "Progress is marked with 了: 成绩进步了, 他升职了.",
            "System questions use 怎么: 这道题怎么做？",
        ],
        "requirements": [
            "20 sentences on jobs, office, classroom, and learning, each translated.",
            "At least 2 schedule sentences and 1 请+把 request sentence.",
        ],
        "standards": ["Word selection cross-checked against HSK 1-3 lists."],
        "citations": [CIT_HSK, CIT_LI],
        "sig_lens": (
            "The Signature read: work and study are the seals of the day "
            "- each meeting, each lesson pressed in order from morning to "
            "night. The Signature Language Method files the working day "
            "as a ladder: climb it in Mandarin and every rung is a raise."
        ),
    },
    {
        "key": "health_body",
        "name": "Health and Body Sentences",
        "group": "Daily Life",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "ladder": 15,
        "description": (
            "Twenty sentences about body parts, symptoms, the doctor's "
            "visit, and the pharmacy - the vocabulary that matters most "
            "when it matters most.\n"
            + _sent_lines(HEALTH_SENT)
        ),
        "how_it_works": (
            "Health sentences follow the body-report pattern: body part + "
            "疼 (hurts) - 头疼, 嗓子疼, 肚子疼 - or the symptom verb: 发烧 "
            "(have a fever), 感冒 (catch a cold). The doctor asks 你哪里不"
            "舒服？ and the patient answers with the pattern. Advice uses "
            "多 (more): 多喝水, 多休息, 多吃蔬菜 - and 请 + verb for "
            "prescriptions: 请按时吃药. Prevention is proverb-shaped: 早睡"
            "早起身体好, 小心别着凉. The pharmacy transaction is short: "
            "我想买感冒药. Injuries narrate with 把 or plain sequence: 他"
            "跑步扭伤了脚. Twenty sentences, and a learner can survive any "
            "clinic visit in China."
        ),
        "key_points": [
            "Pain pattern: body part + 疼: 头疼, 嗓子疼, 肚子疼.",
            "Symptom verbs: 发烧, 感冒; the doctor asks 你哪里不舒服？.",
            "Advice uses 多: 多喝水, 多休息; prescriptions use 请按时吃药.",
            "Prevention is proverb-shaped: 早睡早起身体好.",
            "Pharmacy: 我想买感冒药; well-wishing: 祝你早日康复.",
        ],
        "requirements": [
            "20 sentences on body parts, symptoms, doctor visits, and pharmacy, each translated.",
            "At least 3 pain-pattern sentences and 1 pharmacy transaction.",
        ],
        "standards": ["Word selection cross-checked against HSK 2-3 lists."],
        "citations": [CIT_HSK, CIT_YIP],
        "sig_lens": (
            "The Signature read: the body is the first seal everyone "
            "carries - and its distress signals are a language of their "
            "own. The Signature Language Method teaches health words as "
            "rescue seals: small, exact, and ready before they are needed."
        ),
    },
    {
        "key": "emotions",
        "name": "Emotions and Feelings Sentences",
        "group": "Daily Life",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "ladder": 16,
        "description": (
            "Twenty sentences for the inner life - happy, sad, angry, "
            "afraid, love, surprise - and for comforting others.\n"
            + _sent_lines(EMOTION_SENT)
        ),
        "how_it_works": (
            "Emotion sentences center on a small set of stative verbs: "
            "开心, 高兴, 难过, 生气, 紧张, 害怕, 惊讶. Feelings take 很 "
            "as their linker: 我很开心, 他很生气. Causes attach with "
            "clauses: 听到这个消息，他很高兴. Comforting others runs on "
            "imperatives of care: 别担心, 别害怕, 冷静一点, 放松一下吧. "
            "Love and pride use 为: 我为你感到骄傲, 我爱你 needs nothing "
            "at all. Degree scales with 有点 (a bit), 很 (very), 非常 "
            "(extremely): 我有点紧张 vs 我非常紧张. The resultative 得 "
            "shows emotion overflowing into action: 难过得哭了 (so sad "
            "she cried). With twenty sentences, a learner can name every "
            "major feeling and answer one."
        ),
        "key_points": [
            "Core emotion verbs: 开心, 高兴, 难过, 生气, 紧张, 害怕, 惊讶.",
            "Feelings take 很: 我很开心; degree scales with 有点/很/非常.",
            "Comfort imperatives: 别担心, 别害怕, 冷静一点, 放松一下吧.",
            "Resultative 得 shows overflow: 难过得哭了.",
            "Causes attach as clauses: 听到这个消息，他很高兴.",
        ],
        "requirements": [
            "20 sentences covering happy, sad, angry, afraid, love, surprise, each translated.",
            "At least 2 comforting sentences and 1 得-resultative sentence.",
        ],
        "standards": ["Word selection cross-checked against HSK 1-3 lists."],
        "citations": [CIT_HSK, CIT_LI],
        "sig_lens": (
            "The Signature read: feelings are seals pressed on the heart "
            "- invisible until the sentence reveals the impression. The "
            "Signature Language Method names each feeling exactly, "
            "because a feeling with a name can be carried, and a feeling "
            "carried can be comforted."
        ),
    },
    {
        "key": "nature_weather",
        "name": "Nature and Weather Sentences",
        "group": "Daily Life",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "ladder": 17,
        "description": (
            "Twenty sentences about animals, plants, seasons, and weather "
            "talk - the vocabulary of the world outside the window.\n"
            + _sent_lines(NATURE_SENT)
        ),
        "how_it_works": (
            "Weather sentences use 天气 as their hub: 天气很好, 今天多少"
            "度？. Weather verbs are beautifully simple: 下雨 (rain "
            "falls), 下雪 (snow falls), 刮风 (wind blows - literally blows "
            "wind). The sky's state is described with 出来了: 太阳出来了, "
            "彩虹出来了. Seasons pair with their signature events: 春天花"
            "开了, 秋天树叶黄了. Nature existence sentences use 有 with "
            "the place first: 山上有很多树, 河里有鱼. Animals take 只: "
            "一只鸟, 一只兔子. Small talk about weather follows the "
            "observation pattern - state the sky, ask the forecast: 今天天"
            "气很好，明天会下雪吗？. The set closes with the civic seal: "
            "保护环境，人人有责."
        ),
        "key_points": [
            "天气 is the hub: 天气很好; temperature asks 今天多少度？.",
            "Weather verbs: 下雨, 下雪, 刮风; sky changes use 出来了.",
            "Seasons pair with events: 春天花开了, 秋天树叶黄了.",
            "Nature existence: place + 有: 山上有很多树, 河里有鱼.",
            "Animals take 只: 一只鸟; weather small talk observes then forecasts.",
        ],
        "requirements": [
            "20 sentences on animals, plants, seasons, and weather, each translated.",
            "All four seasons represented; at least 2 weather-verb sentences.",
        ],
        "standards": ["Word selection cross-checked against HSK 1-3 lists."],
        "citations": [CIT_HSK, CIT_NORMAN],
        "sig_lens": (
            "The Signature read: nature is the oldest archive - every "
            "season a sealed record, every weather a fresh impression. "
            "The Signature Language Method reads the sky like a page, "
            "because the learner who can describe the weather can begin "
            "any conversation on earth."
        ),
    },
    {
        "key": "shopping_money",
        "name": "Shopping and Money Sentences",
        "group": "Daily Life",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "ladder": 18,
        "description": (
            "Twenty sentences for the market - prices, bargaining, trying "
            "on, and paying. The commercial Mandarin survival set.\n"
            + _sent_lines(SHOP_SENT)
        ),
        "how_it_works": (
            "Shopping sentences run on the price question: 这个多少钱？ "
            "or the short 多少？. The bargaining dance has fixed steps: "
            "太贵了 (too expensive), 便宜一点吧 (make it cheaper), 可以打"
            "折吗 (any discount?), 我再看看 (I'll keep looking - the walk-"
            "away line). Discounts speak in 折: 打八折 means 20 percent "
            "off (pay 80 percent) - the number names what you pay, the "
            "opposite of English. Money words: 块 (yuan, spoken), 元 "
            "(yuan, formal), 毛/角 (tenths). Payment options: 现金 (cash), "
            "刷卡 (card), 手机支付 (phone pay). Clothing adds the fitting "
            "script: 我想试穿一下, 试衣间在哪里, 有大号的吗. The "
            "transaction closes with 找您... (your change is...) and 谢谢"
            "光临."
        ),
        "key_points": [
            "Price question: 这个多少钱？; bargaining: 太贵了, 便宜一点吧, 可以打折吗.",
            "打八折 = pay 80 percent (20 percent off); the number names what you pay.",
            "Money: 块 (spoken yuan), 元 (formal), 毛/角 (tenths).",
            "Payment: 现金, 刷卡, 手机支付; receipt: 请给我发票.",
            "Fitting script: 试穿, 试衣间, 有大号的吗; walk-away: 我再看看.",
        ],
        "requirements": [
            "20 sentences on market, prices, bargaining, and paying, each translated.",
            "At least 3 bargaining sentences and the 折 discount pattern.",
        ],
        "standards": ["Word selection cross-checked against HSK 1-3 lists."],
        "citations": [CIT_HSK, CIT_YIP],
        "sig_lens": (
            "The Signature read: every purchase is a sealed contract - "
            "price, goods, and handshake pressed into one exchange. The "
            "Signature Language Method teaches the bargaining dance step "
            "by step, because the learner who can haggle in Mandarin can "
            "hold their own in any market on earth."
        ),
    },
    {
        "key": "friendship",
        "name": "Friendship and Social Life Sentences",
        "group": "Daily Life",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "ladder": 19,
        "description": (
            "Twenty sentences for meeting people, invitations, and "
            "celebrations - the social Mandarin that turns strangers into "
            "朋友.\n"
            + _sent_lines(FRIEND_SENT)
        ),
        "how_it_works": (
            "Friendship sentences open with 很高兴认识你 and run on "
            "invitations: 有空吗？, 我们一起...吧, 有空来我家玩. The "
            "invitation grammar is soft - 吧 turns a plan into a "
            "suggestion, 吗 turns it into a question. Accepting is short "
            "and warm: 好啊, 没问题, 一定去. Celebrations have fixed "
            "seals: 生日快乐, 恭喜, 谢谢你的礼物 with the reply 不客气，"
            "应该的. Reunions run on time phrases: 好久不见, 十年没见了, "
            "以后多聚聚. Contact exchange is ritual: 这是我的电话号码, "
            "常联系. The set teaches the full arc from first meeting to "
            "old friend, because Mandarin social life is built sentence "
            "by sentence."
        ),
        "key_points": [
            "Openers: 很高兴认识你; invitations: 有空吗？, 我们一起...吧.",
            "吧 softens plans into suggestions; accept with 好啊, 没问题.",
            "Celebrations: 生日快乐, 恭喜, 谢谢你的礼物.",
            "Reunions: 好久不见, 十年没见了, 以后多聚聚.",
            "Contact ritual: 这是我的电话号码, 常联系.",
        ],
        "requirements": [
            "20 sentences on meeting people, invitations, and celebrations, each translated.",
            "At least 2 invitation sentences and 2 celebration sentences.",
        ],
        "standards": ["Word selection cross-checked against HSK 1-2 lists."],
        "citations": [CIT_HSK, CIT_YIP],
        "sig_lens": (
            "The Signature read: friendship is a seal pressed over years "
            "- each shared meal, each kept promise deepening the "
            "impression. The Signature Language Method teaches the "
            "social sentences as the learner's own hand extended: press "
            "it warmly, and the world presses back."
        ),
    },
    {
        "key": "technology",
        "name": "Technology and Communication Sentences",
        "group": "Daily Life",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "ladder": 20,
        "description": (
            "Twenty sentences about phones, the internet, computers, and "
            "messaging - modern Mandarin for the digital day.\n"
            + _sent_lines(TECH_SENT)
        ),
        "how_it_works": (
            "Technology sentences name the device first: 手机, 电脑, "
            "无线网, 软件, 应用. Problem reports follow the symptom "
            "pattern: 手机没电了, 电脑死机了, 网站打不开 - then the fix "
            "as an imperative: 重启一下试试, 换个浏览器试试. Messaging "
            "verbs: 发消息, 收邮件, 扫码, 加好友 - China's social life "
            "runs through the QR code: 扫码加我好友. Requests use 请: 请"
            "下载这个应用, 请给我密码... no - passwords are asked with "
            "是多少: 密码是多少？. Safety sentences carry weight: 别信陌生"
            "短信, 记得备份文件. The set is deliberately practical: "
            "every sentence solves a real digital moment."
        ),
        "key_points": [
            "Devices: 手机, 电脑, 无线网, 软件, 应用.",
            "Problem pattern: symptom + fix: 电脑死机了 — 重启一下试试.",
            "Messaging verbs: 发消息, 收邮件, 扫码, 加好友.",
            "Wi-Fi ask: 这里有无线网吗？密码是多少？.",
            "Safety: 别信陌生短信, 记得备份文件.",
        ],
        "requirements": [
            "20 sentences on phone, internet, computer, and messaging, each translated.",
            "At least 2 problem/fix pairs and 1 safety sentence.",
        ],
        "standards": ["Word selection cross-checked against HSK 2-4 lists."],
        "citations": [CIT_HSK, CIT_GB18030],
        "sig_lens": (
            "The Signature read: technology is the newest seal-press in "
            "history - a billion thumbs stamping messages every hour. "
            "The Signature Language Method teaches the digital sentences "
            "as tools, because the learner's Mandarin must work on the "
            "phone as well as on the page."
        ),
    },
]

# entries 21-34: advanced tier
ENTRIES += [
    {
        "key": "aspect",
        "name": "Verb Aspect in Sentences: Past, Present, Future",
        "group": "Grammar in Use",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "ladder": 21,
        "description": (
            "Mandarin has no verb tenses - it has aspect: particles that "
            "show whether an action is completed, experienced, ongoing, or "
            "planned. Five groups, five sentences each, every one "
            "translated.\n"
            + _aspect_lines()
        ),
        "how_it_works": (
            "Aspect works by attaching small particles to the unchanging "
            "verb. 了 (le) marks completion or change: 我吃了 says the "
            "eating is done; 下雨了 says rain has begun. 过 (guo) marks "
            "life experience: 去过北京 means Beijing is in your past, "
            "whatever the year. 着 (zhe) holds a state open: 门开着 keeps "
            "the door open in the sentence the way it stands open in the "
            "room. Present time needs no particle at all - time words do "
            "the work: 我每天跑步, 我在看书 (在/正在 mark the progressive "
            "moment). Future uses 会 (will/probably), 要 (going to/want), "
            "将 (formal will): 明天会下雨, 我要去中国. Negation pairs by "
            "time: 不 for present and future (我不去), 没 for past (我没"
            "去). The learner's job is not conjugating - it is choosing "
            "the right small seal for the time-feeling of the sentence."
        ),
        "key_points": [
            "了 marks completion or change: 我吃了, 下雨了.",
            "过 marks life experience: 我去过北京 (have been, ever).",
            "着 holds an ongoing state: 门开着, 他穿着红衣服.",
            "Present needs no particle: time words and 在/正在 carry it.",
            "Future: 会 (will), 要 (going to), 将 (formal will); negate past with 没, present/future with 不.",
        ],
        "requirements": [
            "5+ translated sentences each for present, past-completed, experiential, ongoing-state, and future.",
            "Each aspect particle (了/过/着/在/会/要) shown in at least one sentence.",
        ],
        "standards": ["Aspect analysis follows Li and Thompson's functional grammar."],
        "citations": [CIT_LI, CIT_YIP, CIT_HSK],
        "sig_lens": (
            "The Signature read: time is not stamped on the verb - it is "
            "sealed around it with small perfect particles. The Signature "
            "Language Method teaches aspect as five time-seals: press 了 "
            "for done, 过 for lived, 着 for lasting, and let 会 and 要 "
            "sign the future."
        ),
    },
    {
        "key": "qa_pairs",
        "name": "Questions and Answers",
        "group": "Grammar in Use",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "ladder": 22,
        "description": (
            "Twenty question-and-answer pairs covering who, what, where, "
            "when, why, and how - the complete interrogative workout, "
            "every pair translated.\n"
            + _qa_lines()
        ),
        "how_it_works": (
            "Mandarin questions work three ways. Yes-no questions add 吗 "
            "to a statement: 你是学生吗？. Question-word questions keep "
            "the word in place: 你去哪里？ (where at the end), 谁是你的老"
            "师？ (who at the front because the subject is asked). Choice "
            "questions use 还是: 你要茶还是咖啡？ - and 吗 never appears "
            "with 还是. Answers are short: repeat the verb for yes (去不"
            "去？ - 去), use 不/没 for no, and answer question words "
            "directly with the asked piece. Tags like 好吗？ (okay?) and "
            "对吗？ (right?) soften any statement into a check. 呢 bounces "
            "questions back: 我很好，你呢？. Drill the twenty pairs aloud "
            "as dialogues - question, pause, answer - and interrogatives "
            "become reflex."
        ),
        "key_points": [
            "吗 turns statements into yes-no questions; question words stay in place.",
            "还是 offers alternatives; 吗 never appears with 还是.",
            "Short answers repeat the verb: 去不去？ - 去.",
            "好吗？ and 对吗？ soften statements into checks; 呢 bounces questions back.",
            "The twenty pairs cover who/what/where/when/why/how - drill them as dialogues.",
        ],
        "requirements": [
            "20 question/answer pairs covering who, what, where, when, why, how, each translated.",
            "All three question types (吗, question-word, 还是) represented.",
        ],
        "standards": ["Interrogative analysis follows Li and Thompson's functional grammar."],
        "citations": [CIT_LI, CIT_YIP],
        "sig_lens": (
            "The Signature read: a question is a seal pressed in reverse "
            "- it asks the other party to complete the impression. The "
            "Signature Language Method teaches questions as open seals: "
            "press 吗 for yes or no, leave the question word in its place, "
            "and let the answer sign itself."
        ),
    },
    {
        "key": "commands",
        "name": "Commands and Requests: Formal and Informal",
        "group": "Grammar in Use",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "ladder": 23,
        "description": (
            "Twenty imperative and polite-request sentences, each labeled "
            "formal, polite, casual, direct, or stern - the full volume "
            "knob of Mandarin commands.\n"
            + _command_lines()
        ),
        "how_it_works": (
            "Commands work on a politeness slider. The bare verb is the "
            "blunt end: 坐下, 开门, 快点 - fine for close friends and "
            "emergencies, rude elsewhere. Add 请 and the same verb becomes "
            "civilized: 请坐, 请把门打开. Add 一下 and it softens further: "
            "请过来一下, 麻烦您写一下 - 一下 shrinks the request to a "
            "moment. 麻烦您 (trouble you) is the polite pusher for "
            "strangers: 麻烦您快一点. Questions replace commands at the "
            "polite end: 能帮我一个忙吗？ never orders at all. Prohibitions "
            "use 别 or 不要: 别说话, 别客气. The stern end - 闭嘴 - is "
            "included once, labeled never-use, because a learner must "
            "recognize rudeness without speaking it. Read the room, pick "
            "the register, press the right seal."
        ),
        "key_points": [
            "Bare verb = blunt: 坐下; + 请 = polite: 请坐; + 一下 = softer: 请过来一下.",
            "麻烦您 is the polite pusher for strangers; 能...吗？ asks instead of ordering.",
            "Prohibitions: 别/不要: 别说话; the rude form is labeled, never used.",
            "Warm informal has its own register: 别客气，随便吃.",
            "Register choice is social grammar - wrong volume offends more than wrong tones.",
        ],
        "requirements": [
            "20 imperative/polite-request sentences with register labels, each translated.",
            "At least 5 polite (请/麻烦您) forms and 1 labeled impolite form.",
        ],
        "standards": ["Pragmatics follow the standard Putonghua prescription (PSC syllabus)."],
        "citations": [CIT_PSC, CIT_YIP],
        "sig_lens": (
            "The Signature read: a command is the heaviest seal in the "
            "language - it presses someone else's actions. The Signature "
            "Language Method teaches the whole volume knob, because the "
            "master signs softly: 请 first, 一下 always, and the bare verb "
            "kept for friends and fires."
        ),
    },
    {
        "key": "descriptions",
        "name": "Descriptions of People and Places",
        "group": "Grammar in Use",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "ladder": 24,
        "description": (
            "Twenty sentences describing people, places, and things in "
            "detail - the descriptive Mandarin that paints pictures.\n"
            + _sent_lines(DESCRIBE_SENT)
        ),
        "how_it_works": (
            "Descriptions work through two frames. The 又...又... frame "
            "pairs qualities: 又大又圆, 又宽敞又明亮, 干净又安静 - two "
            "seals pressed side by side. The degree frame scales one "
            "quality: 很 (very), 真 (truly), 极了 (extremely, after the "
            "adjective), 得-constructions for manner: 笑起来有两个酒窝, "
            "字写得很工整. Attributive chains stack with 的: 长长的黑发, "
            "红色的裙子, 美丽而古老的国家 - the longest description sits "
            "closest to the noun... actually before it, each 的-phrase a "
            "layer of paint. Body descriptions name the feature: 有一头黑"
            "发, 戴着眼镜, 满头白发. Place descriptions open wide then "
            "focus: 这座城市... then its lights, its streets. Twenty "
            "pictures in words; the learner's eye learns to narrate what "
            "it sees."
        ),
        "key_points": [
            "又...又... pairs qualities: 又大又圆, 又宽敞又明亮.",
            "Degree frames: 很, 真, 极了 (after adjective), 得 for manner.",
            "Attributive chains stack with 的 before the noun: 长长的黑发.",
            "Body features: 有一头..., 戴着..., 满头....",
            "Places open wide then focus: city first, then its lights.",
        ],
        "requirements": [
            "20 descriptive sentences on people, places, and things, each translated.",
            "At least 3 又...又... sentences and 2 得-manner sentences.",
        ],
        "standards": ["Descriptive patterns follow Li and Thompson's functional grammar."],
        "citations": [CIT_LI, CIT_YIP],
        "sig_lens": (
            "The Signature read: description is the seal of the eye - "
            "each observed detail pressed into words until the picture "
            "appears. The Signature Language Method teaches the learner "
            "to paint with 又...又... and 的, layering seals until the "
            "person, the place, the thing stands visible in the sentence."
        ),
    },
    {
        "key": "story1",
        "name": "Story I: A Day at the Park",
        "group": "Stories",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "ladder": 25,
        "description": (
            "A ten-sentence simple story in Mandarin - 小明的一天 in the "
            "park - with line-by-line English translation. Present-tense "
            "narration for first-story confidence.\n"
            + _story_lines(STORY1)
        ),
        "how_it_works": (
            "A first story works by staying inside known grammar: present "
            "time, simple subjects, one action per sentence. Ten sentences "
            "make a complete arc - setting (今天是星期天), weather (天气"
            "很好), action (小明去公园), discovery (他看见一只小狗), "
            "company (和朋友一起玩), closing (下午，他们回家). Each line "
            "reuses vocabulary from earlier records: 公园, 朋友, 苹果, "
            "开心 - so the story is a reunion, not a test. Read it three "
            "ways: first for the English, second reading the pinyin aloud, "
            "third reading characters only. Then retell it from memory - "
            "changing one detail (the dog becomes a cat) proves the story "
            "is owned, not memorized."
        ),
        "key_points": [
            "Ten sentences, one action each: setting, weather, action, discovery, company, closing.",
            "Present-tense narration reuses records 1-20 vocabulary - a reunion, not a test.",
            "Read three ways: English, pinyin aloud, characters only.",
            "Retell from memory changing one detail to prove ownership.",
            "First stories stay inside known grammar; confidence before complexity.",
        ],
        "requirements": [
            "A 10-sentence simple story in Mandarin with line-by-line English translation.",
            "Present-tense narration; vocabulary drawn from earlier records.",
        ],
        "standards": ["Narrative graded to HSK 1-2 vocabulary."],
        "citations": [CIT_HSK, CIT_LI],
        "sig_lens": (
            "The Signature read: a story is ten seals pressed in order - "
            "each sentence an impression, the whole a signed page. The "
            "Signature Language Method seals the first story simply, "
            "because the learner's signature must be legible before it "
            "can be flourish."
        ),
    },
    {
        "key": "story2",
        "name": "Story II: The Lost Umbrella",
        "group": "Stories",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "ladder": 26,
        "description": (
            "A ten-sentence story using past-tense forms - 小红 and the "
            "forgotten umbrella - with line-by-line English translation. "
            "The 了/过 workout in narrative form.\n"
            + _story_lines(STORY2)
        ),
        "how_it_works": (
            "A past-tense story works by chaining completed actions with "
            "了: 带了一把伞, 去了学校, 忘记了伞 - each 了 closes one "
            "event and opens the next. Time words anchor the chain: 昨天, "
            "下午, 回家以后, 从那以后. The experiential 过 appears at the "
            "moral: 再也没有丢过东西 (never lost anything again - in all "
            "her experience). Discovery verbs drive plot: 发现 (discover), "
            "不见了 (gone). Emotion closes the arc: 拿起伞笑了. Notice "
            "how Mandarin past narration needs no conjugation drills - "
            "the particles do all the time-work while the verbs stay "
            "still. Retell the story emphasizing each 了 aloud; the ear "
            "learns completion as a sound."
        ),
        "key_points": [
            "Past narration chains 了: 带了, 去了, 忘了 - each closes an event.",
            "Time words anchor the chain: 昨天, 下午, 回家以后, 从那以后.",
            "过 marks life experience at the moral: 再也没有丢过东西.",
            "Discovery verbs drive plot: 发现, 不见了.",
            "No conjugation drills needed - particles do the time-work.",
        ],
        "requirements": [
            "A 10-sentence story using past forms with line-by-line translation.",
            "At least 5 了-completions and 1 过-experiential.",
        ],
        "standards": ["Narrative graded to HSK 2-3 vocabulary."],
        "citations": [CIT_HSK, CIT_LI],
        "sig_lens": (
            "The Signature read: a past story is a sealed archive - each "
            "了 a stamp of completion, each 过 a stamp of experience. "
            "The Signature Language Method files the past in order, "
            "because a signed history is the foundation every future "
            "sentence stands on."
        ),
    },
    {
        "key": "story3",
        "name": "Story III: Tomorrow's Plan",
        "group": "Stories",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "ladder": 27,
        "description": (
            "A ten-sentence story using future and conditional forms - a "
            "birthday tomorrow - with line-by-line English translation. "
            "The 会/要/将 and 如果...就 workout.\n"
            + _story_lines(STORY3)
        ),
        "how_it_works": (
            "A future story works by planting 会, 要, and 将 before verbs: "
            "我会请朋友, 妈妈会做蛋糕, 我们将一起唱歌 - each one a "
            "promise sealed in advance. Conditionals branch the future: "
            "如果下雨，我们就在家里玩; 要是天气好，我们就去公园 - 如果/"
            "要是 opens the condition, 就 delivers the result. Certainty "
            "scales with 一定: 大家一定会很开心. Plans sequence with "
            "以后: 生日过后，我会写感谢信. The story teaches the future "
            "as intentions, not predictions - Mandarin's future is "
            "volitional, built from what the speaker will do. Retell it "
            "as your own tomorrow: change the birthday to your plan and "
            "the future becomes personal."
        ),
        "key_points": [
            "Future plants 会/要/将 before verbs: 我会请, 我要去, 我们将唱.",
            "Conditionals: 如果/要是...就... - condition opens, 就 delivers.",
            "Certainty scales with 一定: 一定会很开心.",
            "以后 sequences plans: 生日过后，我会写感谢信.",
            "Mandarin future is volitional - intentions, not predictions.",
        ],
        "requirements": [
            "A 10-sentence story using future/conditional forms with line-by-line translation.",
            "At least 3 future markers and 2 如果/要是...就... conditionals.",
        ],
        "standards": ["Narrative graded to HSK 2-3 vocabulary."],
        "citations": [CIT_HSK, CIT_LI],
        "sig_lens": (
            "The Signature read: a future story is a covenant signed in "
            "advance - every 会 a promise, every 如果 a guarded clause. "
            "The Signature Language Method teaches the learner to sign "
            "tomorrow's sentences today, because intentions written in "
            "Mandarin have a way of coming true."
        ),
    },
    {
        "key": "idioms",
        "name": "Mandarin Idioms and Proverbs",
        "group": "Idioms and Style",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "ladder": 28,
        "description": (
            "Twenty idioms and proverbs (成语 chéngyǔ and sayings) - each "
            "with pinyin, literal translation, real meaning, and an "
            "example sentence translated. Idioms are the deep water of "
            "Mandarin: four characters carrying two thousand years.\n"
            + _idiom_lines()
        ),
        "how_it_works": (
            "Idioms work as compressed stories: most 成语 are four "
            "characters summarizing a classical tale - 守株待兔 (the "
            "farmer who waited by a stump for rabbits), 叶公好龙 (Lord Ye "
            "who loved dragons until he met one). The literal translation "
            "is almost never the meaning: 对牛弹琴 is not about cows, it "
            "is about wasted effort. Learners meet idioms in three "
            "layers: recognize the four characters, know the story in one "
            "sentence, use it in one safe sentence of their own. Start "
            "with the transparent ones - 加油, 熟能生巧, 水滴石穿 - "
            "whose meanings show through the characters. Deploy idioms "
            "sparingly: one per conversation marks cultivation; five "
            "marks showing off. The twenty here are the highest-frequency "
            "idioms in modern speech and writing."
        ),
        "key_points": [
            "Most 成语 compress a classical tale into four characters.",
            "Literal translation is rarely the meaning: 对牛弹琴 = wasted effort, not cows.",
            "Learn in three layers: recognize, know the story, use in one safe sentence.",
            "Start transparent: 加油, 熟能生巧, 水滴石穿.",
            "One idiom per conversation marks cultivation; five marks showing off.",
        ],
        "requirements": [
            "20 idioms/proverbs with literal translation, real meaning, and translated example sentence.",
            "At least 10 classical four-character 成语.",
        ],
        "standards": ["Idiom selection follows HSK 5-6 and standard chéngyǔ dictionaries."],
        "citations": [CIT_HSK, CIT_NORMAN],
        "sig_lens": (
            "The Signature read: an idiom is the deepest seal in the "
            "language - four characters pressed with two thousand years "
            "of weight. The Signature Language Method teaches idioms as "
            "heirloom seals: handle with respect, press sparingly, and "
            "each impression marks the speaker as cultivated."
        ),
    },
    {
        "key": "registers",
        "name": "Formal and Polite Registers",
        "group": "Idioms and Style",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "ladder": 29,
        "description": (
            "Fifteen formal-vs-informal pairs for letters, business, and "
            "elders - each pair translated with a note on exactly when "
            "the formal form is required.\n"
            + _register_lines()
        ),
        "how_it_works": (
            "Registers work as a wardrobe: the same meaning dressed for "
            "different rooms. The informal set - 你好, 谢谢, 给我 - fits "
            "friends and family. The formal set upgrades three things: "
            "pronouns (你 -> 您), verbs (吃 -> 用餐, 看 -> 过目 in "
            "writing), and frames (add 请, 麻烦您, 恐怕). Business "
            "letters open with 尊敬的 (respected) and close with 此致敬礼 "
            "(with respect); spoken business softens refusals with 恐怕 "
            "(恐怕不行) and requests with 烦请. Elders receive 您, 请, "
            "and the host's farewell 慢走. The critical rule: formality "
            "flows upward - to elders, clients, officials - never "
            "downward to friends, where it sounds cold. The fifteen pairs "
            "are the minimum wardrobe; with them, no room is entered "
            "underdressed."
        ),
        "key_points": [
            "Formal upgrades three things: pronouns (你->您), verbs (吃->用餐), frames (请/麻烦您/恐怕).",
            "Business letters: open 尊敬的, close 此致敬礼; soften refusals with 恐怕.",
            "Elders get 您, 请, and the host's 慢走.",
            "Formality flows upward only - formal speech to friends sounds cold.",
            "The fifteen pairs are the minimum wardrobe for every room.",
        ],
        "requirements": [
            "15 formal vs informal pairs with translations and usage notes.",
            "Pronoun, verb, and frame upgrades each represented.",
        ],
        "standards": ["Pragmatics follow the standard Putonghua prescription (PSC syllabus)."],
        "citations": [CIT_PSC, CIT_YIP],
        "sig_lens": (
            "The Signature read: register is the seal of respect - the "
            "same meaning pressed deeper for elders, clients, and "
            "honored guests. The Signature Language Method teaches the "
            "formal wardrobe as armor: the learner who can dress a "
            "sentence for any room is welcome in every room."
        ),
    },
    {
        "key": "complex",
        "name": "Compound and Complex Sentences",
        "group": "Idioms and Style",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "ladder": 30,
        "description": (
            "Fifteen long sentences with clauses, connectors, and relative "
            "structures - each parsed and translated. The advanced "
            "assembly line.\n"
            + _complex_lines()
        ),
        "how_it_works": (
            "Complex sentences work by chaining the paired connectors: "
            "因为...所以 (cause), 虽然...但是 (concession), 如果...就 "
            "(condition), 不但...而且 (addition), 只有...才 (exclusive "
            "condition), 无论...都 (universal concession), 一...就 "
            "(immediacy), 越...越 (scaling). Each pair is a two-part "
            "seal: the first half opens the logic, the second half "
            "delivers it. Special structures reshape the line: 把 fronts "
            "the object for disposal actions, 被 marks the passive "
            "(usually unhappy), 是...的 frames a past detail for "
            "emphasis. Questions embed too: 还是 asks either-or without "
            "吗, 呢 adds wondering. The parse note under each sentence "
            "names the machinery - read the sentence, read the parse, "
            "then build one new sentence on the same frame. Fifteen "
            "frames mastered is fluency's skeleton."
        ),
        "key_points": [
            "Paired connectors: 因为...所以, 虽然...但是, 如果...就, 不但...而且, 只有...才, 无论...都, 一...就, 越...越.",
            "把 fronts objects; 被 marks (usually unhappy) passives; 是...的 emphasizes past details.",
            "还是 asks either-or without 吗; 呢 adds wondering.",
            "Each sentence carries a parse note naming the machinery.",
            "Build one new sentence per frame - fifteen frames is fluency's skeleton.",
        ],
        "requirements": [
            "15 long sentences with clauses/connectors/relative clauses, parsed and translated.",
            "At least 8 different paired connectors demonstrated.",
        ],
        "standards": ["Complex-sentence analysis follows Yip and Rimmington's comprehensive grammar."],
        "citations": [CIT_YIP, CIT_LI],
        "sig_lens": (
            "The Signature read: a complex sentence is a seal-press with "
            "many plates - each clause a plate, each connector the hinge "
            "that aligns them. The Signature Language Method teaches the "
            "fifteen frames as the master's toolkit: with every hinge "
            "oiled, the longest sentence presses true."
        ),
    },
    {
        "key": "dialog_market",
        "name": "Conversation: At the Market",
        "group": "Dialogues",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "ladder": 31,
        "description": (
            "A twenty-line bilingual market dialogue - customer (A) and "
            "vendor (B) bargaining over apples and bananas - fully "
            "annotated. The commercial conversation, start to finish.\n"
            + _dialog_lines(DIALOG_MARKET)
            + "\nAnnotations: 好嘞 is the vendor's cheerful 'coming right "
            "up'; 斤 (jīn, half a kilo) is the market weight unit; 打折 "
            "and 便宜点 drive the bargaining; 手机支付 closes the modern "
            "transaction; 慢走 is the vendor's polite farewell."
        ),
        "how_it_works": (
            "A market dialogue works as a transaction script with five "
            "acts: greeting (你好), price inquiry (怎么卖), bargaining "
            "(贵了/便宜点), quantity (买三斤/来两斤), payment and "
            "farewell (支付/谢谢/慢走). The customer drives with questions; "
            "the vendor answers with prices and warmth. Measure words do "
            "heavy lifting: 三斤, 两斤 - weight, not pieces. Numbers stay "
            "spoken-style: 十块, 六块, 二十二块. Perform the dialogue "
            "aloud with a partner, swapping roles; then improvise it with "
            "new goods (grapes, fish, shirts). The script is the skeleton "
            "- real markets add noise, and the trained ear holds the "
            "line."
        ),
        "key_points": [
            "Five acts: greeting, price inquiry, bargaining, quantity, payment/farewell.",
            "Market weight unit: 斤 (half a kilo); spoken prices: 十块, 二十二块.",
            "Bargaining lines: 贵了, 便宜点吗, 已经很便宜了.",
            "Modern close: 手机支付, 扫码; vendor farewell: 慢走.",
            "Perform aloud swapping roles, then improvise with new goods.",
        ],
        "requirements": [
            "A 20-line bilingual dialogue (Mandarin + English), annotated.",
            "Customer and vendor roles; bargaining and payment included.",
        ],
        "standards": ["Dialogue graded to HSK 2-3 vocabulary."],
        "citations": [CIT_HSK, CIT_YIP],
        "sig_lens": (
            "The Signature read: a market dialogue is commerce sealed in "
            "conversation - every price a pressed number, every bargain a "
            "tested seal. The Signature Language Method rehearses the "
            "whole transaction, because the learner who can close a deal "
            "in Mandarin owns the market."
        ),
    },
    {
        "key": "dialog_friend",
        "name": "Conversation: Meeting a Friend",
        "group": "Dialogues",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "ladder": 32,
        "description": (
            "A twenty-line bilingual dialogue - 小明 meets 小红 after "
            "years apart and plans a reunion dinner. The social "
            "conversation, warm and complete.\n"
            + _dialog_lines(DIALOG_FRIEND)
            + "\nAnnotations: 好久不见 opens reunions; 挺好的 is the "
            "warm casual 'pretty good'; 对了 pivots topics ('by the "
            "way'); 一定去 seals a promise; 路上小心 closes with care."
        ),
        "how_it_works": (
            "A reunion dialogue works on the warmth circuit: exclamation "
            "(好久不见！), wellbeing check (最近怎么样？), life update "
            "(还在那家公司吗？), invitation (聚一下), logistics (在哪儿？"
            "几点？), promise (一定去), contact (这是我电话), farewell "
            "(路上小心). 呢 bounces questions back: 你呢？. 对了 pivots "
            "without abruptness. Time and place lock with specifics: 周六"
            "晚上六点, 市中心那家火锅店 - vague plans die, specific plans "
            "live. Perform it with the reunion energy: loud hellos, fast "
            "questions, the promise pressed hard. Then run it as yourself "
            "- your friend, your plan, your city."
        ),
        "key_points": [
            "Warmth circuit: exclamation, wellbeing check, life update, invitation, logistics, promise, farewell.",
            "呢 bounces questions: 你呢？; 对了 pivots topics.",
            "Specific plans live: 周六晚上六点, 市中心那家火锅店.",
            "Promises press hard: 一定去; farewells carry care: 路上小心.",
            "Perform with reunion energy, then run it as yourself.",
        ],
        "requirements": [
            "A 20-line bilingual dialogue (Mandarin + English), annotated.",
            "Two named speakers; invitation with time and place.",
        ],
        "standards": ["Dialogue graded to HSK 2-3 vocabulary."],
        "citations": [CIT_HSK, CIT_YIP],
        "sig_lens": (
            "The Signature read: a reunion dialogue is friendship "
            "re-sealed - the old impression pressed fresh again. The "
            "Signature Language Method teaches the warmth circuit by "
            "heart, because every Mandarin friendship is renewed one "
            "好久不见 at a time."
        ),
    },
    {
        "key": "dialog_problem",
        "name": "Conversation: Solving a Problem",
        "group": "Dialogues",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "ladder": 33,
        "description": (
            "A twenty-line bilingual dialogue - two roommates discover a "
            "leaking faucet and fix it together. The problem-solving "
            "conversation: report, diagnose, act, verify.\n"
            + _dialog_lines(DIALOG_PROBLEM)
            + "\nAnnotations: 糟了 flags the problem; 可能是 hedges the "
            "diagnosis; 先... organizes the fix order; 把水阀关掉 shows "
            "把 in action; the final test - 打开试试,不漏了 - verifies "
            "the solution."
        ),
        "how_it_works": (
            "A problem-solving dialogue works in four moves: report the "
            "symptom (一直在漏水), diagnose the cause (可能是垫圈坏了), "
            "execute the fix (先把水阀关掉...我去买), verify the result "
            "(打开试试,不漏了). Hedging keeps it collaborative: 可能是 "
            "(probably), 应该可以 (should be fine) - nobody orders, "
            "everyone proposes. Sequencing words organize action: 先 "
            "(first), 然后 (then), imperfectly omitted when the order is "
            "obvious. Offers divide labor: 要我一起去吗？ / 不用. The "
            "verification line is the seal on the whole exchange - no "
            "fix is real until tested. Learners should practice this "
            "dialogue because real life is mostly this dialogue: "
            "something breaks, words fix it."
        ),
        "key_points": [
            "Four moves: report symptom, diagnose cause, execute fix, verify result.",
            "Hedge collaboratively: 可能是, 应该可以 - propose, do not order.",
            "先 sequences action; offers divide labor: 要我一起去吗？.",
            "The verification line seals the fix: 打开试试,不漏了.",
            "Real life is mostly this dialogue: something breaks, words fix it.",
        ],
        "requirements": [
            "A 20-line bilingual dialogue (Mandarin + English), annotated.",
            "Problem report, diagnosis, fix, and verification all present.",
        ],
        "standards": ["Dialogue graded to HSK 2-3 vocabulary."],
        "citations": [CIT_HSK, CIT_YIP],
        "sig_lens": (
            "The Signature read: a solved problem is a seal of competence "
            "- symptom reported, cause diagnosed, fix executed, result "
            "verified. The Signature Language Method drills the four "
            "moves until they are reflex, because the master signs the "
            "solution, not the complaint."
        ),
    },
    {
        "key": "mastery",
        "name": "Mastery Review and Full Reference",
        "group": "Mastery",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "ladder": 34,
        "description": (
            "The whole database in one teaching summary: the pinyin "
            "sound chart, the 200 core words, the key grammar rules, and "
            "the phrase tables - the consolidated quick-reference and "
            "final exam in one record.\n\nPINYIN SOUND CHART: Four tones "
            "plus neutral - first high flat (55), second rising (35), "
            "third dipping (214), fourth falling (51). Initials (21): b p "
            "m f, d t n l, g k h, j q x, zh ch sh r, z c s, y w. Finals "
            "include a o e i u ü, ai ei ao ou, an en ang eng ong, ia iao "
            "ian iang iong, ua uo uai uan uang ueng, üe üan ün. Tone-mark "
            "priority: a > o > e > i/u/ü. Sandhi: 你好 spoken ní hǎo; 不 "
            "becomes bú before fourth tones; 一 becomes yí/yì by rule.\n\n"
            "200 CORE WORDS:\n"
            + _core200_lines()
            + "\n\nKEY GRAMMAR (one-line each): Word order SVO with time "
            "and place before the verb. No conjugation, no gender, no "
            "number, no case. Aspect: 了 completed, 过 experienced, 着 "
            "ongoing, 在/正在 progressive, 会/要/将 future. Measure words "
            "mandatory with numbers: 一个人. Negation: 不 present/future, "
            "没 past. Questions: 吗 yes-no, question words in place, 还是 "
            "alternatives. 是 identity, 有 possession/existence, 在 "
            "location/progressive. 的 possessive/attributive, 地 adverbial, "
            "得 resultative. 把 fronts objects; 被 marks passive. "
            "Comparisons: 比; superlative: 最. Paired connectors: 因为..."
            "所以, 虽然...但是, 如果...就, 不但...而且, 只有...才, 无论..."
            "都, 一...就, 越...越.\n\nPHRASE TABLES: Greetings: 你好/您好/"
            "早上好/晚上好/再见/谢谢/不客气/对不起/没关系/请/请问. Time: "
            "点/分/半/刻; dates year-month-day. Shopping: 多少钱/太贵了/"
            "便宜一点/打八折/手机支付. Travel: 请问...在哪里/一直往前走/"
            "左转/右转/去机场多少钱. Health: 头疼/发烧/感冒/多喝水/祝你早日"
            "康复. Farewells: 再见/慢走/一路顺风/明天见."
        ),
        "how_it_works": (
            "The mastery review works as a final pass over the whole "
            "ladder: read the chart, recite the 200 words, rehearse the "
            "grammar lines, speak the phrase tables - then test. Cover "
            "the English column of the 200 words and translate upward; "
            "cover the Mandarin and translate downward; anything missed "
            "twice goes back to its record for a day. Speak the three "
            "stories from memory. Perform the three dialogues with a "
            "partner. Write ten new sentences using ten different paired "
            "connectors. Use three idioms in real conversation this week. "
            "The database marched from 你好 to 水滴石穿; the review "
            "proves the march. When all of it is comfortable, the "
            "learner is ready for the million-record archive beyond - "
            "and for real conversations with a billion speakers."
        ),
        "key_points": [
            "The full pinyin chart: 21 initials, all finals, 4 tones + neutral, sandhi rules.",
            "200 core words with pinyin and English - the working vocabulary floor.",
            "One-line grammar: word order, aspect, measure words, negation, questions, connectors.",
            "Phrase tables for greetings, time, shopping, travel, health, farewells.",
            "Test method: cover-and-translate both directions; misses go back to their record.",
        ],
        "requirements": [
            "Consolidated quick-reference: sound chart, 200 core words, key grammar, phrase tables.",
            "A self-test method with a remediation rule (misses return to their record).",
        ],
        "standards": [
            "Core-word list cross-checked against HSK 1-4 vocabulary.",
            "Pinyin chart follows ISO 7098:2015.",
        ],
        "citations": [CIT_ISO7098, CIT_HSK, CIT_LI, CIT_YIP],
        "sig_lens": (
            "The Signature read: the mastery review is the final seal on "
            "the learner's own archive - every lesson pressed, every "
            "sentence signed. The Signature Language Method ends where "
            "it began: stamp the sound, seal the character, sign the "
            "sentence - and the signature, by record thirty-four, is "
            "fluent."
        ),
    },
]
