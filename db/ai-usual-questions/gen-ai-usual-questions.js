(function(){'use strict';
/* AI Responses to Usual Questions Database generator — jahdb-ai-usual-questions-1.0.
   Property of Justin Addam Higgins (JAH).
   One record = one usual everyday question + a thorough, genuinely helpful AI answer.
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-AUQ-';
var CATS=[
 ['technology','Technology'],
 ['health-wellness','Health & Wellness'],
 ['money-finance','Money & Finance'],
 ['home-diy','Home & DIY'],
 ['work-career','Work & Career'],
 ['relationships','Relationships'],
 ['learning-study','Learning & Study'],
 ['food-cooking','Food & Cooking'],
 ['travel','Travel'],
 ['everyday-life','Everyday Life']
];
var CATSLUGS=CATS.map(function(c){return c[0];});
/* Each family: cat, label, q (question templates), s (slot pools), a (answer paragraphs).
   {slots} are filled once per record so question and answer stay consistent. */
var FAMS=[
/* ============ TECHNOLOGY ============ */
{cat:'technology',label:'Wi-Fi troubleshooting',
 q:['Why does my Wi-Fi keep {issue}?','How do I fix Wi-Fi that keeps {issue}?','My Wi-Fi {issue} every evening — what should I check first?','What is the first thing to try when the Wi-Fi {issue}?'],
 s:{issue:['dropping out','slowing to a crawl','disconnecting my laptop','dropping my video calls']},
 a:['Start with the simplest fix, because it resolves most cases: unplug your router, wait a full 30 seconds, and plug it back in. While it restarts, restart the device that {issue} too. About half of all Wi-Fi complaints end right here — routers are small computers and they get confused just like any other.',
 'If the problem comes back, look at placement. Your router should sit out in the open, roughly in the middle of your home, and up high — on a shelf, not on the floor behind the TV. Walls, mirrors, microwaves and baby monitors all weaken the signal. Moving a router even a few feet can end a problem that {issue} for months.',
 'Next, check for congestion. If your neighbors all broadcast on the same Wi-Fi channel, everyone slows down. Log into your router (usually an address like 192.168.1.1 printed on its sticker) and switch the 2.4 GHz band to channel 1, 6 or 11, whichever is least used. If your router offers a 5 GHz network, use it for the room the router is in — it is faster over short distances.',
 'When none of that helps, call your internet provider and ask them to check the line coming into your home and the health of your modem. Tell them exactly when it {issue} and what you already tried. If the line is fine and the router is more than five years old, replacing the router itself is usually the real fix.']},
{cat:'technology',label:'Phone storage full',
 q:['My phone says storage is full — what should I delete first?','How do I free up space on my phone without losing anything?','My phone storage is full and I cannot take photos — what now?','What eats the most storage on a phone?','How do I stop my phone from running out of space?','Which apps usually take up the most space?'],
 s:{app:['social media apps','the photos app','downloaded videos','old podcasts']},
 a:['The biggest space hogs on almost every phone are {app}, cached data, and videos you forgot you saved. Start in your phone\u2019s storage settings, which shows exactly what is using space, biggest first. Delete with information instead of guessing — the list usually surprises people.',
 'Photos and videos are the usual culprit. Turn on your phone\u2019s cloud backup for photos, wait until it confirms everything is uploaded, then use the "free up space" option that removes the local copies while keeping them in the cloud. This alone recovers gigabytes for most people without losing a single memory.',
 'Next, clear out what you do not use: apps you have not opened in months, downloaded episodes and playlists, old message threads with lots of photos, and offline maps. For {app} specifically, clearing its cache (in the app\u2019s settings, not by deleting the app) often frees a shocking amount of space.',
 'To keep it from filling again, turn on automatic offloading of unused apps and set downloads to expire. And make it a habit: once a month, spend five minutes in storage settings. A phone with breathing room runs noticeably faster and stops nagging you at the worst moments.']},
{cat:'technology',label:'Strong passwords',
 q:['How do I make passwords I can actually remember?','What is the best way to create a strong password?','I keep forgetting my passwords — what should I do?','Are password managers safe to use?','Should I use the same password everywhere?','How often should I change my passwords?'],
 s:{method:['a passphrase','a password manager','a written backup kept somewhere safe']},
 a:['The honest answer is that nobody should be memorizing dozens of strong passwords — human memory was never built for that. The strongest approach most people can actually stick with is {method}, and here is why each works.',
 'If you choose a passphrase, pick four random words and join them with a number or symbol, like "correct-horse-battery-9". It is long, which is what defeats guessing, but it reads like a tiny story so your brain keeps it. Never reuse it anywhere else — one password per important account, always.',
 'If you choose a password manager, you only memorize one master passphrase and the manager creates and remembers a unique random password for every site. This is what security professionals actually do. Pick a well-known manager, turn on two-factor authentication for the manager itself, and you are safer than 95 percent of people online.',
 'Whatever you choose, turn on two-factor authentication for your email first — your email is the master key to every other account. And never "remember" passwords by reusing one everywhere: one leaked site then hands attackers the key to your bank, your email and your social accounts all at once.']},
{cat:'technology',label:'Slow computer',
 q:['Why is my computer so slow and how do I fix it?','My {device} takes forever to start — what can I do?','How do I speed up an old {device}?','My computer was fast and now it crawls — what happened?'],
 s:{device:['laptop','desktop','computer']},
 a:['A {device} that slows down over time is almost never broken — it is usually just overloaded. The most common cause is too many programs launching at startup. Open your startup settings and turn off everything you do not need the second the machine turns on. This single change can cut boot time in half.',
 'Second, check your storage. When a drive gets more than about 85 percent full, everything slows down because the system has nowhere to work. Delete what you do not need, move big files to an external drive or cloud storage, and empty the trash. Aim to keep at least 15 to 20 percent of the drive free.',
 'Third, look at what is running right now. Browsers with dozens of tabs are the classic hidden hog — each tab uses memory. Close what you are not using, and consider an ad blocker, which measurably speeds up web pages. If your {device} still has a spinning hard drive, upgrading to a solid-state drive is the single biggest speed upgrade money can buy on an old machine.',
 'If it is still slow after all that, run a malware scan — unwanted software running in the background is a real cause of sudden slowdowns. And be honest about age: a ten-year-old {device} running modern software will always struggle. At that point the kindest fix is a fresh operating-system install or a newer machine.']},
{cat:'technology',label:'Spotting scams',
 q:['How do I tell if an email or text is a scam?','I got a strange text about my {account} — is it real?','How do scammers trick people over the phone?','What are the signs of a phishing message?'],
 s:{account:['bank account','package delivery','streaming subscription']},
 a:['Scams work by rushing you. Any message that demands you act right now — your {account} will be locked, you owe money, a package is stuck — is trying to stop you from thinking. Real companies almost never pressure you this way. Urgency is the single biggest red flag; when you feel it, slow down on purpose.',
 'Second, check the sender independently. Scam texts about a {account} include a link they want you to tap — do not tap it. Instead, open the company\u2019s real app or type its real website yourself and check there. If the message claims to be your bank, call the number on the back of your card, not any number in the message.',
 'Third, look for the tells: generic greetings like "Dear customer", spelling mistakes, email addresses that almost-but-not-quite match the real company, and requests for passwords, codes or gift cards. No legitimate company asks you to pay in gift cards or wire money to fix a problem — that is always a scam, every time.',
 'If you already clicked or replied, act fast: change that password from the real site, turn on two-factor authentication, and watch your statements. And tell someone — reporting the message to your phone carrier (forward spam texts to 7726) helps protect the next person. Being scammed is not a sign of foolishness; these operations fool smart people every day.']},
/* ============ HEALTH & WELLNESS ============ */
{cat:'health-wellness',label:'Falling asleep faster',
 q:['How can I fall asleep faster?','I lie awake for hours — how do I fall asleep?','What actually helps you fall asleep quickly?','How do I stop my mind racing at bedtime?','Does reading before bed help you sleep?','What time should I go to bed?'],
 s:{habit:['scrolling your phone','drinking caffeine late','an irregular bedtime']},
 a:['The biggest lever is consistency, not tricks. Going to bed and waking up at the same time every day — weekends included — trains your body\u2019s clock, and most people who fix only this one thing start falling asleep noticeably faster within two weeks. Your brain learns when sleep is coming and starts preparing for it.',
 'The second lever is cutting the biggest sleep thief: {habit}. Screens keep your brain alert with light and novelty right when it needs to wind down. Put the phone to charge across the room an hour before bed. If your mind races, keep a notepad by the bed and write the looping thoughts down — getting them out of your head and onto paper genuinely helps.',
 'Make the room itself boring for sleeping: cool, dark and quiet. A cool room (around 18°C / 65°F) matches the drop in body temperature that triggers sleepiness. If you cannot make it dark, a sleep mask costs little and works well; if noise is the issue, steady white noise beats silence-with-surprises.',
 'If you are still awake after about 20 minutes, get up, go to another room, and do something dull in dim light until you feel sleepy — then return to bed. Lying awake trains your brain to associate bed with frustration. And if sleeplessness persists for weeks and affects your days, talk to a doctor: chronic insomnia is a medical issue with real treatments, not a willpower problem.']},
{cat:'health-wellness',label:'Daily water intake',
 q:['How much water should I really drink each day?','Do I actually need eight glasses of water a day?','How do I know if I am drinking enough water?','What counts toward daily water intake?','Can you drink too much water?','Does coffee count toward water intake?'],
 s:{drink:['coffee','herbal tea','sparkling water']},
 a:['The "eight glasses" rule is a myth — nobody\u2019s body runs on a fixed number. A better guide is your own signals: pale yellow urine and rarely feeling thirsty means you are doing fine; dark yellow urine, headaches and afternoon slumps suggest you need more. Your needs shift with heat, exercise and body size, so a fixed number was never going to be right anyway.',
 'Most of your water does not have to come from a glass. Fruits, vegetables, soups and even {drink} all count toward hydration. {drink} in normal amounts hydrates you just fine — the old claim that coffee dehydrates you has been debunked for everyday drinkers. What matters is total fluid across the day, not the source.',
 'The practical system that works for most people: keep water where you already are. A bottle on your desk, a glass by the sink you pass, water with every meal. People do not fail at hydration from ignorance — they fail because water is not within arm\u2019s reach when the mild thirst hits.',
 'Two honest caveats. First, forcing huge volumes of water does not "detox" anything — your kidneys handle that, and overdoing it can actually dilute your blood sodium. Second, if you are suddenly extremely thirsty all the time or urinating far more than usual, that is worth mentioning to a doctor rather than just drinking more.']},
{cat:'health-wellness',label:'Lower back pain from sitting',
 q:['What helps with lower back pain from sitting all day?','My lower back aches after sitting — what should I do?','How do I fix back pain from my desk job?','Is walking good for lower back pain?','Should I see a doctor for lower back pain?','Is heat or ice better for back pain?'],
 s:{stretch:['the knee-to-chest stretch','a gentle cat-cow stretch','a standing back extension']},
 a:['For the achy, stiff kind of back pain that comes from sitting, movement is the medicine — bed rest actually makes it worse. Start with short, frequent motion: stand up and walk for two or three minutes every half hour. It sounds too simple, but breaking up sitting time is the single most effective habit for desk-related back pain.',
 'Add one gentle stretch, done daily: {stretch}. Hold each position for 20 to 30 seconds, breathe normally, and never push into sharp pain — mild pulling is fine, stabbing is not. Done consistently for two weeks, most people feel a real difference. Strength matters too: a few minutes of core work (planks, bird-dogs) a few times a week protects the back far better than any chair.',
 'Fix the setup that caused it. Your screen should be at eye level, your feet flat on the floor, and your lower back supported — a rolled towel works as well as an expensive lumbar pillow. The "perfect posture" matters less than changing position often; even the best chair becomes a problem after three unmoving hours.',
 'Know the red flags that mean "see a doctor promptly": pain shooting down a leg, numbness or weakness in a foot, loss of bladder control, or pain after a real injury or fall. Those are not sit-it-out situations. Ordinary muscular ache from sitting, though, almost always improves with movement, stretching and a better setup — give it two consistent weeks.']},
{cat:'health-wellness',label:'Cold vs flu',
 q:['How do I tell a cold from the flu?','Do I have a cold or the flu?','What is the difference between cold and flu symptoms?','How do I know if I need a doctor for the flu?','How long does the flu usually last?','When should I stay home sick?'],
 s:{symptom:['a sudden high fever','crushing body aches','a mild runny nose']},
 a:['The fastest way to tell is the onset and the fever. Flu hits like a truck — you feel fine at lunch and flattened by dinner — with {symptom} and real exhaustion. A cold creeps in over a couple of days and centers on the nose and throat: {symptom} is classic cold, while flu rarely bothers with much of a runny nose at all.',
 'Treat them differently. For a cold, rest, fluids and patience do most of the work; decongestants and honey-and-warm-drinks help the symptoms. For flu, the same basics apply, but antiviral medication from a doctor can shorten it if started within the first day or two — so calling early matters more than toughing it out.',
 'Watch for the signs that mean a doctor visit: trouble breathing, chest pain, a fever that will not come down after three days, dehydration (very little urine, dizziness), or symptoms that improve and then suddenly get much worse — that rebound can signal a secondary infection. The very young, the elderly and pregnant people should call sooner rather than later.',
 'Prevention is unglamorous but real: wash your hands, do not touch your face, and get the flu shot each fall. It does not guarantee you will dodge flu season, but it makes a severe case far less likely — which is the whole point.']},
{cat:'health-wellness',label:'Starting exercise',
 q:['I hate exercise — how do I actually start?','How do I start working out when I am completely out of shape?','What is the easiest exercise to start with?','How do beginners stick with exercise?','How many days a week should a beginner exercise?','What is a good 10-minute workout?'],
 s:{activity:['brisk walking','bodyweight exercises at home','swimming']},
 a:['The reason most people quit is that they start with someone else\u2019s program instead of their own life. Forget the ideal routine. Pick {activity} — something you dislike the least, that fits into a day you already have, and that you could do even when tired. The best exercise program is the one you will repeat, and repeatability beats intensity every time for beginners.',
 'Start embarrassingly small. Ten minutes counts. A walk around the block counts. The goal of the first month is not fitness — it is building the identity of "someone who does this regularly." Add five minutes a week and you will be at a real workout before you notice, without ever having a day so awful you dread the next one.',
 'Attach it to something you already do: walk right after lunch, stretch while the coffee brews, do squats during TV commercials. Habits stick when they ride on existing routines instead of floating in your schedule. And track it somewhere visible — a wall calendar with X marks is weirdly powerful motivation.',
 'Expect the dip around week three, when novelty fades. Plan for it now: a backup indoor option for bad weather, a friend to go with, or simply permission to do the tiny version on bad days. Missing one day is nothing; missing one day and then quitting is the actual enemy. Ten minutes done beats an hour skipped.']},
/* ============ MONEY & FINANCE ============ */
{cat:'money-finance',label:'Making a budget',
 q:['How do I make a budget that actually works?','What is the simplest way to budget my money?','How do I start budgeting when I have never done it?','Why do budgets never work for me?','How do I track my spending?','What percentage of income should go to savings?'],
 s:{method:['the 50/30/20 rule','a zero-based budget','the envelope method']},
 a:['Budgets fail for one reason: they are built from wishes instead of reality. Before you plan a single dollar, look at the last two months of actual spending — bank statements, not memory. Most people discover they are spending far more than they think on two or three categories, and that discovery is the whole foundation. You cannot fix what you have not measured.',
 'Then pick a structure simple enough to survive a busy month. {method} works because it has few enough buckets to remember: the classic version puts roughly half of take-home pay to needs, a third to wants, and a fifth to savings and debt. Adjust the percentages to your life — the structure matters more than the exact numbers.',
 'Automate the good decisions so willpower is not involved. Set up an automatic transfer to savings for the day after payday, before you can spend it. What you do not see, you do not miss. Then give yourself a guilt-free spending allowance inside the budget — a budget with zero fun in it is a budget you will abandon by week three.',
 'Review once a month for fifteen minutes, not daily. Ask one question: which category surprised me? Adjust that one thing and move on. A budget is not a punishment for past spending — it is a plan that makes future spending match what you actually want your money to do.']},
{cat:'money-finance',label:'Emergency savings',
 q:['How much should I keep in emergency savings?','How do I build an emergency fund from zero?','Where should I keep my emergency fund?','Is three months of expenses enough for emergencies?','Should I keep emergency savings in cash?','How do I rebuild savings after an emergency?'],
 s:{amount:['three to six months','at least one month','six months']},
 a:['The standard target is {amount} of essential expenses — not income, expenses: rent, food, utilities, transport, minimum debt payments. Three months is the minimum that handles a job loss or a big car repair; six is the cushion that lets you sleep well. If that number feels impossible, ignore it for now and aim at the first $1,000 — that alone covers most of life\u2019s ordinary surprises.',
 'Build it the boring way: automatic and separate. Open a savings account at a different bank from your checking, and set an automatic transfer for payday — even $25 a week becomes $1,300 in a year. "Pay yourself first" sounds like a slogan, but it works because money you never see does not get spent. Raise the amount whenever you get a raise, before your lifestyle absorbs it.',
 'Keep it boring and reachable: a plain high-yield savings account. Not invested in the market (emergencies do not wait for recoveries), not in cash at home (it earns nothing and tempts spending), and not mixed into checking where it silently becomes spending money. It should take a day or two to reach — close enough for real emergencies, far enough to stop impulse raids.',
 'Define "emergency" in advance, in writing: job loss, medical bills, urgent car or home repairs. A sale, a vacation and a rough month are not emergencies — that is what the regular budget is for. Every time you are tempted, read your own definition. People who write the rule down raid the fund far less.']},
{cat:'money-finance',label:'Raising a credit score',
 q:['How do I raise my credit score?','What is the fastest way to improve bad credit?','Why is my credit score low?','How long does it take to build credit?','Does checking my credit hurt my score?','How do I fix errors on my credit report?'],
 s:{factor:['payment history','how much of your credit you use','the age of your accounts']},
 a:['Your score is mostly a report card on three behaviors, and {factor} is the heavyweight. One late payment can undo months of progress, while a long streak of on-time payments is the single most powerful builder. Set every bill to autopay at least the minimum — not because minimums are good, but because "never late" matters more than anything else.',
 'The second lever is utilization: the percentage of your available credit you are using. Keep it under 30 percent, and under 10 is better. If your limit is $1,000, owing $800 looks risky even if you pay it off monthly. Ask for a limit increase or spread spending across cards — the same spending looks safer against a bigger limit.',
 'Be patient with the rest. Do not close your oldest card (it shortens your history), do not open five new accounts at once (each application dings you slightly), and dispute genuine errors on your reports — you can check all three bureaus free every year. Real mistakes on reports are common and fixable.',
 'Honest timeline: with consistent on-time payments and low utilization, most people see meaningful improvement in six to twelve months. There is no legitimate overnight fix — anyone selling "rapid rescoring" or asking you to dispute accurate debts is selling a scam. Slow, boring and consistent is the entire strategy.']},
{cat:'money-finance',label:'Debt vs saving',
 q:['Should I pay off debt or save money first?','I have debt and no savings — which comes first?','Is it better to invest or pay off my credit cards?','How do I decide between saving and debt payoff?','What is the debt snowball method?','Should I pay off my car loan early?'],
 s:{rate:['high-interest','any','low-interest']},
 a:['Do both, but in order: first save a small starter cushion of about $1,000, then attack the {rate} debt hard. The starter fund exists so the next surprise does not go straight onto a credit card and erase your progress. It feels backwards to save while in debt, but skipping it is how people end up borrowing again the moment life happens.',
 'Then compare interest rates honestly. Credit card debt at 20-plus percent costs you far more than any safe investment earns, so {rate} debt almost always wins the race against investing. Pay minimums on everything, throw every extra dollar at the highest-rate balance first, and roll each paid-off payment into the next. That avalanche order saves the most money in total interest.',
 'The exception is free money: if your employer matches retirement contributions, contribute enough to get the full match even while paying debt — that is an instant 100 percent return nothing else beats. And keep making minimum payments on everything, always; a missed payment\u2019s damage to your credit costs more than the interest you would save.',
 'Once the {rate} debt is gone, redirect the exact same monthly amount into savings and investing before your lifestyle expands to eat it. The habit you built while paying debt — living on less than you earn — is the real prize. Most people who clear debt and immediately inflate spending end up right back where they started within two years.']},
{cat:'money-finance',label:'Starting to invest',
 q:['How do I start investing with little money?','What is the simplest way to begin investing?','How much money do I need to start investing?','Is investing risky for beginners?','What is an index fund?','When should I start saving for retirement?'],
 s:{vehicle:['a low-cost index fund','your workplace retirement plan','a target-date fund']},
 a:['You can start with the price of a pizza — the barrier is knowledge, not money. The simplest beginner path is {vehicle}: it spreads your money across hundreds of companies at once, charges tiny fees, and requires no stock-picking skill. One fund, automatic monthly contributions, and you are genuinely investing.',
 'The order matters more than the amount. First, kill high-interest debt and hold that small emergency cushion — investing while paying 24 percent on a card is swimming upstream. Then, if your job offers a retirement match, take it before anything else. After that, a plain taxable or retirement account with automatic contributions beats clever strategies every time.',
 'Understand the real risk: the market goes down sometimes, and that is normal, not failure. Money you need within five years should not be invested — keep it in savings. Money you will not touch for decades can ride out every dip in history so far. Beginners lose money by panic-selling during drops, not by the drops themselves; the plan only works if you leave it alone.',
 'Ignore stock tips, hot trends and anyone promising fast returns. Boring is the strategy: same amount, same fund, every month, for years. Check it twice a year, not twice a day. Time in the market beats timing the market — that sentence has survived every crash, and it is the whole game for beginners.']},
/* ============ HOME & DIY ============ */
{cat:'home-diy',label:'Unclogging a drain',
 q:['How do I unclog a drain without chemicals?','My {drain} is draining slowly — what do I do?','How do you clear a clogged drain naturally?','What is the safest way to unclog a drain?'],
 s:{drain:['bathroom sink','kitchen sink','shower drain','tub']},
 a:['Skip the harsh chemical cleaners — they can damage pipes and rarely beat a mechanical fix. Start with the free method: pour a kettle of near-boiling water down the {drain} (skip this step for PVC pipes, which can soften — use very hot tap water instead). Often that alone melts the grease or soap holding the clog.',
 'Next, the classic fizzy combo: half a cup of baking soda followed by half a cup of white vinegar. Cover the drain for 15 minutes while it fizzes, then flush with hot water. It will not dissolve a serious blockage, but it clears the slow, gunky kind that makes a {drain} drain lazily.',
 'For the real clog, use a plunger — but the right way. Seal any overflow opening with a wet rag, fill the basin with a few inches of water so the cup is submerged, and plunge vigorously for 20 seconds. The seal is the whole trick; most people plunge with air leaking around the edges and wonder why nothing happens. A $5 hair snake (a long plastic strip with teeth) pulled from a {drain} will horrify and delight you with what it retrieves.',
 'If two fixtures clog at once, or water backs up in odd places, stop — that can mean a main-line blockage, which is plumber territory, not DIY. And never mix chemical cleaners, especially bleach with anything acidic: the fumes are genuinely dangerous. Mechanical beats chemical for almost every household clog.']},
{cat:'home-diy',label:'Painting a room',
 q:['How do I paint a room like a pro?','What is the right order to paint a room?','How do I get clean lines when painting?','What mistakes do beginners make painting walls?','How much paint do I need for a room?','Should I use a roller or a brush?'],
 s:{tool:['a quality roller','an angled sash brush','painter\u2019s tape']},
 a:['Pros get clean results from preparation, not talent. Move furniture out or to the center and cover it, lay drop cloths (plastic sheeting slips; canvas stays put), and clean the walls — paint sticks poorly to dust and kitchen grease. Fill holes with spackle, sand smooth when dry, and wipe the dust off. An hour of prep saves three hours of fixing.',
 'The order that avoids rework: ceiling first, then walls, then trim. Use {tool} for cutting in — that careful edge line along ceilings and trim — and do the edges of one wall before rolling that same wall, so everything blends while wet. Work in sections about three feet wide, keeping a "wet edge" so roller marks disappear.',
 'Two thin coats beat one thick coat every time. Thick paint drips, sags and shows every flaw; thin coats dry evenly and cover better. Wait for the first coat to fully dry (check the can, usually a few hours) before the second — painting over tacky paint pulls it right back off. And buy better paint than you think you need: it covers in fewer coats and the color stays true.',
 'The beginner mistakes to dodge: skipping primer on repaired spots or dark colors (they will flash through), painting in a closed-up room (ventilate — fumes are real), and pulling {tool} off while the paint is fully dry (score the edge first or it tears the paint line). Peel tape while the last coat is still slightly tacky for the crispest lines.']},
{cat:'home-diy',label:'Fixing a squeaky door',
 q:['How do I fix a squeaky door?','My door squeaks every time it moves — how do I stop it?','What is the best lubricant for door hinges?','How do you silence a squeaky hinge?','Can I use cooking oil on a squeaky hinge?','Why do doors squeak in winter?'],
 s:{lube:['a few drops of household oil','white lithium grease','even bar soap in a pinch']},
 a:['A squeak is just metal rubbing on metal, so the fix is lubrication — but where you put it matters. Open and close the door slowly to find which hinge sings; it is usually only one. Then work {lube} into the pin: lift the pin slightly with a screwdriver and hammer tap, or just dribble oil along the top of the hinge and swing the door to work it in.',
 'Wipe the excess, then swing the door a dozen times to distribute it. If the squeak persists, the pin itself may be dirty or bent — pop it fully out, clean it with a rag, apply fresh lubricant, and tap it back in. Ninety percent of squeaks die at this step.',
 'If oil does not fix it, the hinge may be loose rather than dry. Tighten every screw on the noisy hinge; if a screw spins without gripping, the hole is stripped — drive in a longer screw that bites into the framing behind the jamb, or pack the hole with wooden toothpicks and glue first. A door that moved on loose hinges will squeak no matter how much oil you use.',
 'Avoid the tempting shortcut of spraying everything with penetrating oil like WD-40 as a permanent fix: it is a solvent, not a lasting lubricant, and the squeak returns in weeks. Use it to clean, then follow with real oil or grease. Five minutes and the right lubricant beats a year of wincing.']},
{cat:'home-diy',label:'Recaulking a bathtub',
 q:['How do I recaulk a bathtub?','My bathtub caulk is moldy — how do I replace it?','How do you get a smooth caulk line?','What kind of caulk should I use in a bathroom?','How often should bathroom caulk be replaced?','Can I caulk over old caulk?'],
 s:{caulk:['100% silicone','a siliconized acrylic']},
 a:['Old, moldy caulk is not just ugly — it lets water behind the tub where it rots things quietly. Use {caulk} labeled kitchen-and-bath (it has mildew resistance built in). And do not caulk over the old stuff: new caulk sticks to old caulk poorly, and the mold underneath just keeps growing. Removal is the real job.',
 'Remove every bit of the old caulk with a utility knife and a plastic scraper, then clean the joint with rubbing alcohol and let it dry completely. This is tedious and it is also the step that determines whether your new caulk lasts five years or five months. Tape both sides of the joint with painter\u2019s tape, leaving a narrow gap — this is what gives you those crisp professional lines.',
 'Cut the tube nozzle small — you can always cut bigger, never smaller — and squeeze a steady, continuous bead in one pass per side. Then smooth it immediately with a wet finger or a caulk tool in one smooth motion. Pull the tape off right away, while the caulk is still wet, pulling away from the joint at an angle.',
 'Let it cure the full time on the tube (usually 24 hours) before running water on it. Fill the tub with water before caulking if you want to be thorough: the weight opens the joint slightly, so the caulk cures in the stretched position instead of cracking the first time someone takes a bath.']},
{cat:'home-diy',label:'Getting rid of ants',
 q:['How do I get rid of ants in the kitchen?','Ants keep coming back — how do I stop them?','What is the best way to kill an ant colony?','How do I find where ants are coming from?','Are ant traps safe around pets?','How do I keep ants out of the house?'],
 s:{bait:['borax-based bait stations','a borax-sugar mixture']},
 a:['Spraying the ants you see is satisfying and useless — those are foragers, maybe five percent of the colony. The colony just sends more. The fix that actually works is {bait}: worker ants carry the slow poison home and feed it to the queen. Kill the queen and the colony collapses; kill foragers and you have treated a symptom.',
 'Place the bait right on their trail and then — this is the hard part — leave them alone for a few days. You will see more ants at first, and that is good: it means they are taking the bait home. Do not spray insecticide near the bait or you will scatter the colony into multiple new ones, which is the classic way a small ant problem becomes a house-wide one.',
 'While the bait works, find and follow the trail to where they enter — usually a gap around a pipe, window or door. Seal it with caulk. Then remove what invited them: wipe up crumbs and sticky spills, store sugar, cereal and pet food in sealed containers, and take trash out nightly. Ants follow food; no food, no scouts, no trail.',
 'If bait plus sealing does not end it in two weeks, you may be dealing with carpenter ants (they nest in damp wood — a structural issue) or multiple colonies, and that is exterminator territory. But for ordinary kitchen ants, bait, patience and sealing solve it for the vast majority of homes.']},
/* ============ WORK & CAREER ============ */
{cat:'work-career',label:'Writing a resume',
 q:['What makes a resume actually get read?','How do I write a resume with no experience?','How long should my resume be?','What do hiring managers look for on a resume?','Should I include a photo on my resume?','What should I leave off my resume?'],
 s:{length:['one page','two pages at most']},
 a:['A resume gets about seven seconds on first glance, so design for scanning, not reading. Put your name, one clear job target, and your three strongest proof points where eyes land first — top third of the page. Dense paragraphs get skipped; short bullets with numbers get read. "Increased sales 22% in one year" beats "responsible for sales growth" every time.',
 'Keep it to {length}: cut everything that does not argue for this specific job. Hiring managers do not need your full history — they need the three reasons you fit this role. Tailor the top bullets to the job posting\u2019s own words; many companies filter with software before a human ever sees it, and matching their keywords gets you past the filter.',
 'With no experience, lead with what you do have: projects, coursework, volunteer work, freelance gigs — anything where you made something happen. A student who "built a scheduling app used by 40 classmates" outshines a graduate with a blank page. Employers hire evidence of ability, and evidence does not require a job title.',
 'The fastest rejections come from sloppiness: typos, a jokey email address, walls of text, or lying about anything checkable. Have one careful person proofread it. And save and send it as a PDF named YourName-Resume.pdf — "resume_final_v7.pdf" tells the hiring manager nothing and looks careless.']},
{cat:'work-career',label:'Answering interview questions',
 q:['How do I answer "tell me about yourself" in an interview?','What is the best way to answer interview questions?','How do I talk about my weaknesses in an interview?','How should I prepare for a job interview?','How do I answer ‘why should we hire you’?','What questions should I ask the interviewer?'],
 s:{story:['a 60-second story','a two-minute story','a tight one-minute story']},
 a:['"Tell me about yourself" is not an invitation to your life story — it is "why are you here, in 60 seconds." Prepare {story} with a shape: where you are now, the two or three experiences that built the skills for this job, and why this role is the obvious next step. End looking forward, not backward. Practice it out loud until it sounds conversational, not recited.',
 'For "what is your greatest weakness," skip the fake strengths ("I work too hard") — interviewers have heard it a thousand times. Name a real, non-fatal weakness and, crucially, what you are doing about it: "I used to avoid difficult conversations, so I took a feedback workshop and now I address issues within a week." A weakness with a fix in progress reads as self-awareness, which is what they are actually testing.',
 'For behavioral questions ("tell me about a time when…"), use the STAR shape: Situation, Task, Action, Result — with most of your time on Action and a measurable Result. Prepare five stories from your past that can flex to cover teamwork, conflict, failure, leadership and pressure. Five good stories answer fifty questions.',
 'Prepare for them as much as for yourself: research the company\u2019s recent news, understand the role\u2019s real problems, and bring three smart questions — about the team\u2019s challenges, what success looks like in six months, and why the role is open. Candidates who ask sharp questions are remembered; candidates with no questions signal they do not care.']},
{cat:'work-career',label:'Asking for a raise',
 q:['How do I ask for a raise?','When is the right time to ask for a raise?','How do I negotiate salary without seeming greedy?','What do I say when asking for more money?','How much of a raise should I ask for?','What if my raise request is denied?'],
 s:{evidence:['a one-page list of your wins','your measurable results','market salary data for your role']},
 a:['You do not ask for a raise — you make a business case for one. Weeks before the conversation, gather {evidence}: projects completed, revenue influenced, problems solved, responsibilities you absorbed that were not in your original job. "I feel underpaid" is a feeling; "here is what I delivered" is a case. Managers approve cases.',
 'Time it to strength: after a visible win, during performance reviews, or when you take on new scope — not when the company just announced cuts or your boss is firefighting. And know your number from {evidence} before you walk in: a specific figure ("$X, based on these results and market data") beats "whatever you think is fair," which invites the lowest number they can defend.',
 'In the room, be direct and brief: state the case, name the number, then stop talking. Silence feels awful and it is your best tool — do not negotiate against yourself by filling it. If the answer is no, ask what specifically would make it yes, and by when: "What would I need to deliver in the next six months to earn that?" A no with a roadmap is a delayed yes.',
 'Have a walk-away line in mind before you start — not as a threat, but as clarity. If the gap between your value and your pay is large and the company will not move, the market will: changing jobs remains the fastest raise most people ever get. Asking well either gets you more here or gives you the clarity to get it elsewhere.']},
{cat:'work-career',label:'Dealing with burnout',
 q:['How do I deal with burnout at work?','I feel burned out — what should I do?','How do you recover from job burnout?','What are the signs of burnout?','How long does burnout recovery take?','Should I quit my job if I am burned out?'],
 s:{sign:['dreading Mondays on Sunday night','feeling exhausted no matter how much you sleep','caring less about work you used to like']},
 a:['Name it honestly first. Burnout is not laziness and it is not fixed by a weekend: the classic signs are {sign}. If that sounds like you, stop treating it as a motivation problem. It is a depletion problem — you have been spending energy faster than you recover it, and no pep talk refills that tank.',
 'Recover with rest that is actually rest. A vacation where you answer email is not recovery. Take real time off if you can, and protect sleep ruthlessly — exhaustion masquerades as every other problem. Then do one small thing that is only for you, daily: a walk, a hobby, anything where nobody needs anything from you. Recovery is boring and slow, which is why people skip it and stay burned out.',
 'Then address the source, because rest without change just refills a leaking bucket. Burnout comes from workload, lack of control, or values mismatch — figure out which is yours. Can you renegotiate deadlines, drop a commitment, or set one boundary (no email after 7pm)? One structural change beats ten coping techniques.',
 'If exhaustion comes with hopelessness that does not lift, or it has lasted months despite real rest, talk to a doctor or counselor — burnout and depression overlap heavily, and professionals can tell them apart. Asking for help is not weakness; it is what competent people do when the data says the current approach is not working.']},
{cat:'work-career',label:'Remote work productivity',
 q:['How do I stay productive working from home?','How do I focus when working remotely?','What is the best routine for remote work?','How do I separate work and life when working from home?','How do I avoid distractions working from home?','What equipment do I need for remote work?'],
 s:{ritual:['a fake commute — a walk around the block','changing into real clothes','a specific startup playlist']},
 a:['The remote workers who thrive treat the day like it has edges. Start with {ritual} that tells your brain "work begins": without a commute, the day blurs, and blurred days feel both endless and unproductive. Same start time, same shutdown time, and a real end-of-day ritual — close the laptop, change clothes, go outside — so evenings belong to you again.',
 'Design the environment before relying on discipline. A dedicated spot, even just one end of the table, beats working from the couch where your brain associates the space with rest. Phone in another room during focus blocks. Noise-canceling headphones are the remote worker\u2019s closed office door — put them on and housemates learn what it means.',
 'Work in visible blocks, not vibes. Two or three 90-minute deep-work sessions with real breaks outperform eight distracted hours. Tell your team when you are in focus mode and when you are reachable; most remote friction is not laziness, it is unclear expectations. Over-communicate progress in writing — remote work runs on written proof, not presence.',
 'Protect the social part deliberately. Loneliness is the quiet killer of remote work: schedule the coffee chats, join the optional calls, get out of the house. And watch the fridge-to-desk drift — without colleagues, days can pass with zero human contact. The most productive remote workers are the ones who treat connection as part of the job, not a distraction from it.']},
/* ============ RELATIONSHIPS ============ */
{cat:'relationships',label:'Apologizing well',
 q:['How do I apologize without making it worse?','What makes a good apology?','How do I say sorry and actually mean it?','Why do my apologies always backfire?','How do I apologize to someone who will not talk to me?','When is it too late to apologize?'],
 s:{mistake:['saying "I\u2019m sorry you feel that way"','explaining your reasons at length','asking them to comfort you']},
 a:['Most apologies backfire because of {mistake} — the classic non-apology that defends instead of owns. A real apology has three parts and only three: name what you did ("I was late and I didn\u2019t text"), name the impact ("that left you waiting and worried"), and say what changes ("I\u2019ll text if I\u2019m ever running behind"). No "but." The word "but" deletes everything before it.',
 'Keep it short and about them, not you. {mistake} shifts the spotlight to your feelings, which asks the hurt person to manage your guilt on top of their hurt. Say the apology, then stop talking and let them respond — silence after an apology is respect, not awkwardness. Do not ask "are we good now?" on the spot; that pressures them to forgive before they are ready.',
 'Match the repair to the damage. Small hurts need a sincere sentence; big hurts need changed behavior over time. If you keep apologizing for the same thing, the words have expired — only a visible pattern change counts now. People forgive slowly but they watch closely; consistent new behavior is the only apology that compounds.',
 'And know what an apology cannot do: it cannot force forgiveness, erase consequences, or work if you do not actually think you were wrong. If you are not sorry, do not perform sorry — address the real disagreement instead. A fake apology insults twice; an honest conversation, even a hard one, respects the other person.']},
{cat:'relationships',label:'Difficult conversations',
 q:['How do I bring up something hard with my partner?','How do you start a difficult conversation?','How do I tell someone something they do not want to hear?','What is the best way to raise a sensitive topic?','How do I tell my partner I am unhappy?','Should difficult conversations happen in person?'],
 s:{opener:['"I\u2019ve been thinking about something and I\u2019d like to talk it through"','"Can we talk about something that\u2019s been on my mind?"']},
 a:['Do not ambush. Start with {opener} — and mean it as an invitation, not a warning siren. Pick a calm moment, not bedtime, not during a fight, not five minutes before they leave. The setting is half the message: "I chose a good time because this matters" already says you respect them.',
 'Lead with your experience, not their crimes. "I feel lonely when we spend evenings on separate screens" opens a conversation; "you never pay attention to me" opens a trial. Describe the specific behavior and its effect on you, then ask for what you need — people can respond to a request, but they can only defend against an accusation.',
 'Then actually listen, which is the part everyone skips while rehearsing their next point. Repeat back what you heard before answering it: "So you feel criticized when I bring this up — did I get that right?" Most difficult conversations fail not because the topic is hard but because both people leave feeling unheard. Being heard first makes people dramatically more willing to hear you.',
 'End with something concrete, even small: one change, one experiment, one check-in next week. Vague agreements ("we\u2019ll try harder") evaporate; specific ones ("phones away after 9pm on weeknights") can be kept or honestly renegotiated. And if a conversation keeps exploding despite your best skills, that is information — some topics need a counselor\u2019s room, and asking for one is strength, not failure.']},
{cat:'relationships',label:'Setting boundaries',
 q:['How do I set boundaries with family?','How do you say no without feeling guilty?','What are healthy boundaries in relationships?','How do I enforce a boundary I set?','Is it selfish to set boundaries?','How do I say no to family obligations?'],
 s:{boundary:['not answering work calls at dinner','one visit per month instead of every weekend','ending phone calls that turn into shouting']},
 a:['A boundary is not a wall and it is not a punishment — it is information about what you need to stay well, like {boundary}. The guilt you feel setting one is not evidence it is wrong; it is just the discomfort of doing something new. People who love you can survive your boundaries. People who cannot were benefiting from you having none.',
 'State it plainly, kindly, once: what you will do, not what they must do. "I won\u2019t be answering calls after 8pm — I\u2019ll catch up in the morning" works; a long justification invites debate about each reason. You do not need their agreement for your boundary to be valid. "No" is a complete sentence, and "let me think about it" buys you time when pressure is high.',
 'Expect a test. When you set {boundary}, the other person will often push once to see if it holds — that is normal, not proof it failed. Enforce calmly and identically every time: restate the boundary, then follow through. Consistency is the entire enforcement mechanism; a boundary you drop under pressure teaches people that pressure works.',
 'Start small if big ones terrify you. Practice on low-stakes requests first and notice that the world does not end. And keep one honest check: boundaries protect your energy so you can show up better for people — if yours are isolating you entirely, that is worth examining with a counselor. The goal is healthier connection, not fewer people.']},
{cat:'relationships',label:'Making friends as an adult',
 q:['How do adults make new friends?','Why is it so hard to make friends as an adult?','How do I meet people after moving to a new city?','Where do adults actually meet friends?','How do I turn an acquaintance into a friend?','Is it normal to feel lonely as an adult?'],
 s:{place:['a recreational sports league','a volunteer shift','a class — cooking, climbing, language']},
 a:['It feels hard because the machinery of childhood friendship — forced proximity, no schedules, endless unstructured time — is gone. Adult friendship runs on a different fuel: repeated, unplanned interaction plus shared effort. That means {place} beats parties and apps, because you see the same people weekly doing something side by side. Proximity plus repetition is the whole formula.',
 'So optimize for repetition, not intensity. Join the thing that meets weekly, sit near the same people, and stay after for ten minutes. Research on friendship formation suggests it takes dozens of hours together to become real friends — which sounds discouraging until you realize a weekly {place} gets you there in months without any single interaction needing to be magical.',
 'Be the one who suggests the second meeting. Everyone is waiting for someone else to do it — that is the actual bottleneck of adult friendship. "I\u2019m grabbing coffee Saturday, want to come?" is low-pressure and clear. Expect a two-to-one ratio of invitations to acceptances; that is normal, not rejection. The people who make friends are simply the people who keep inviting.',
 'Lower the bar for what counts. You do not need a best friend; you need a few people you see regularly and enjoy. And give it time without auditing: show up for three months before deciding "this isn\u2019t working." Most adult friendships that exist today started with someone who kept showing up long after it felt awkward.']},
{cat:'relationships',label:'Being a better listener',
 q:['How do I become a better listener?','Why do people say I do not listen?','How can I listen instead of just waiting to talk?','What is active listening?','How do I listen without interrupting?','What do you do when someone will not stop talking?'],
 s:{habit:['planning your reply while they talk','jumping in with your own story','checking your phone mid-conversation']},
 a:['The reason people feel unheard is usually {habit} — the listener is technically present but mentally elsewhere, and humans detect it instantly. Real listening starts with a decision: for the next few minutes, your only job is to understand, not to respond, fix, or relate. That single shift changes everything that follows.',
 'Then make it visible. Put the phone away — face-down on the table still signals "you are second priority." Make eye contact, nod, and use tiny encouragers: "mm-hm," "then what happened?" When they pause, do not rush to fill it; the most important sentence often comes after the silence. And reflect back what you heard: "It sounds like you felt blindsided by that" — being accurately understood is what "good listener" actually means.',
 'Resist the fix reflex. When someone shares a problem, your brain offers solutions — but most people want understanding first and advice only if asked. Try: "Do you want ideas, or do you want me to just listen?" That one question prevents the classic mismatch where you proudly solve a problem they never asked you to solve.',
 'Practice on low-stakes conversations so it is there for the hard ones. And notice your own urge to top their story with yours — {habit} is the most common way good listeners slip. Their story is not your cue; it is their moment. Curiosity is the whole technique: genuinely wonder what it was like for them, and the listening takes care of itself.']},
/* ============ LEARNING & STUDY ============ */
{cat:'learning-study',label:'Studying effectively',
 q:['How do I study so I actually remember?','What is the best way to study for exams?','Why do I forget everything I study?','How do top students study?','How many hours should I study per day?','Is it better to study alone or with others?'],
 s:{method:['active recall','spaced repetition','the Feynman technique']},
 a:['Re-reading and highlighting feel productive and barely work — that is the trap. Your brain remembers what it works to retrieve, not what it passively sees. The single most powerful study method is {method}: close the book and force yourself to recall the material from memory. Flashcards, blank-page summaries, practice questions — anything that makes your brain fetch the answer instead of recognizing it.',
 'Space it out. Cramming the night before puts facts in short-term memory, which is why they vanish a week later. Studying the same material in shorter sessions spread over days — {method} in practice — moves it to long-term memory. Thirty minutes today, thirty in three days, beats three hours the night before, for both the exam and actually keeping the knowledge.',
 'Teach it simply. If you cannot explain a concept in plain words, you do not know it yet — that is {method}, and it exposes gaps instantly. After each study session, write a two-minute summary as if explaining to a friend. The parts you stumble on are exactly what to study next.',
 'Protect the machinery: sleep consolidates memory, so an all-nighter before an exam literally impairs the recall you are cramming for. Study in focused 25-minute blocks with real breaks, in the same quiet spot when possible. And test yourself under exam-like conditions at least once — familiarity with the pressure is part of what you are studying.']},
{cat:'learning-study',label:'Learning a language',
 q:['What is the fastest way to learn a language?','How do I actually become fluent in a language?','How long does it take to learn a language?','What is the best method to learn a language as an adult?','Are language apps enough to become fluent?','How do I practice speaking a language alone?'],
 s:{language:['Spanish','French','Japanese']},
 a:['There is no fast way, but there is a way that works: daily contact with the language, mostly listening and speaking, from week one. Apps are fine for vocabulary, but fluency in {language} comes from understanding real speech and producing your own sentences — the earlier you start talking badly, the sooner you talk well. Embarrassment is the tuition.',
 'Front-load the highest-frequency material. The most common 1,000 words cover the vast majority of everyday conversation, so learn those before rare vocabulary. Pair them with the core grammar patterns — in {language}, that means the present tense and basic sentence order first — and you can say useful things within a month. Depth on the common beats breadth on the rare.',
 'Make input unavoidable: change your phone\u2019s language, listen to {language} podcasts during commutes, watch shows you already know with {language} subtitles. Fifteen focused minutes daily beats a three-hour weekend binge — consistency builds the neural pathways, intensity just tires you out. And speak to a real human weekly, even a tutor for 30 minutes; nothing else forces your brain to assemble language in real time.',
 'Realistic timeline: a few hundred hours of real engagement for conversational ability, which at 30 minutes a day is about two years. That sounds long until you notice the people who "tried and failed" usually quit in month two. The method matters less than the streak — pick the approach you will actually do daily, and protect it like an appointment.']},
{cat:'learning-study',label:'Beating procrastination',
 q:['How do I stop procrastinating on assignments?','Why do I procrastinate even when I care?','How do I start a task I keep avoiding?','What actually works against procrastination?','Why do I procrastinate on easy tasks too?','How do I stop doomscrolling instead of working?'],
 s:{task:['an essay','a big project','studying for finals']},
 a:['Procrastination is not laziness — it is mood management. You avoid {task} because thinking about it feels bad (boring, hard, scary), and your brain picks short-term relief. That reframe matters: you do not need more discipline, you need to make starting feel less awful. Shame about procrastinating just adds more bad feeling, which fuels more avoidance.',
 'Shrink the start until it is laughable. Not "write the essay" — "open the document and write one bad sentence." Not "study for finals" — "read one page." Your brain resists big vague tasks and cooperates with tiny specific ones. Once you start, momentum usually carries you further than the tiny step — but the tiny step is the whole trick, because starting is the entire battle.',
 'Change the environment, not just your intentions. Phone in another room, website blockers on, a clear desk, a timer for 25 minutes. Willpower is unreliable; friction is reliable — make distraction slightly harder and starting slightly easier, and behavior follows. Tell someone your plan for today, too: a little social accountability beats pure self-promise.',
 'If you procrastinate on everything, including things you like, or it comes with persistent low mood and exhaustion, look deeper — chronic procrastination overlaps with anxiety, depression and attention issues, all of which have real help available. For ordinary {task}-avoidance, though: tiny start, clean environment, timer on. Today, not "tomorrow."']},
{cat:'learning-study',label:'Learning a new skill as an adult',
 q:['How do adults learn a new skill from scratch?','Is it too late to learn {skill}?','How do I learn something completely new as an adult?','What is the best way to pick up a new skill?'],
 s:{skill:['an instrument','a new language','coding','drawing']},
 a:['It is not too late — adult brains learn {skill} fine; they just learn differently than children\u2019s. Adults need to understand the why before the how, and they learn fastest from doing, not from consuming tutorials. The rule: spend at most a third of your time learning about it, and two thirds doing it badly. Tutorial paralysis, where you watch the tenth video instead of practicing, is the adult beginner\u2019s trap.',
 'Break {skill} into its smallest real piece and master that first. Not "learn guitar" — "switch cleanly between two chords." Not "learn to code" — "make a button that does something." Small wins build the only motivation that lasts: evidence that you are improving. Track the wins visibly — a practice log turns invisible progress into proof.',
 'Get feedback early and often. A teacher, a community, even recording yourself — anything that shows you what you cannot see. Solo practice without feedback engraves mistakes; ten minutes with someone knowledgeable can fix what ten hours alone cannot. And embrace being bad publicly: every expert at {skill} was once embarrassing at it, and the ones who improved fastest were the ones who asked the "dumb" questions.',
 'Expect the plateau around month two or three, when easy gains stop and it feels like nothing is improving. This is normal and it is where most adults quit — right before the breakthrough. Push through with slightly harder challenges (not repetition of what is easy), and one day the thing that was impossible is simply something you do.']},
{cat:'learning-study',label:'Improving focus',
 q:['How do I focus when everything distracts me?','How can I concentrate for longer?','My attention span feels broken — how do I fix it?','How do I stop getting distracted every five minutes?','Does multitasking actually work?','How long can the brain focus at once?'],
 s:{distraction:['your phone','social media','background noise']},
 a:['Your attention is not broken — it is responding exactly as designed to an environment engineered to fragment it. The fix starts with {distraction}: put the phone in another room during focus time, not face-down beside you. Studies show even its silent presence drains attention. You cannot out-willpower an environment built by thousands of engineers to interrupt you.',
 'Work in single-task blocks. Multitasking is a myth — what you are doing is rapid switching, and each switch costs minutes of depth. Pick one task, set a timer for 25 to 50 minutes, and do only that. When the urge to check something hits, write it on a pad beside you and keep going; the urge passes in about a minute if you do not feed it.',
 'Prime your brain first. A clear, written next step ("draft the intro paragraph") focuses you faster than sitting down to "work on the project." Vague goals invite drifting; specific ones invite starting. And match tasks to energy: hard creative work in your sharpest hours, admin when you are dull. Fighting your own rhythm all day is exhausting and unnecessary.',
 'Rebuild the muscle gradually. If you currently focus for ten minutes, aim for fifteen — not two hours. Boredom tolerance is trainable: sit with the itch to check {distraction} and let it pass, and each rep makes the next easier. Sleep, exercise and daylight all measurably improve focus too — attention is a whole-body system, not just a mindset.']},
/* ============ FOOD & COOKING ============ */
{cat:'food-cooking',label:'Weekly meal prep',
 q:['How do I meal prep for the week?','What is the easiest way to start meal prepping?','How do I plan meals for a whole week?','What foods are best for meal prep?','How do I keep meal prep from getting boring?','What containers are best for meal prep?'],
 s:{protein:['chicken thighs','ground turkey','lentils','salmon']},
 a:['Meal prep fails when people try to cook seven different dinners on Sunday and burn out by week two. The sustainable version is component prep: cook {protein}, a big batch of a grain, two roasted vegetables, and one sauce. Mix and match through the week and you get variety without cooking seven recipes. Boring components, endless combinations.',
 'Pick foods that actually survive the week. {protein} reheats well; delicate fish and crispy things do not. Grains like rice, quinoa and farro hold for five days refrigerated; roasted root vegetables and broccoli stay good; leafy salads go soggy — store dressing separately and assemble fresh. Cook once, eat well all week, because you chose survivors.',
 'The system that sticks: same prep day, same simple formula. Protein plus grain plus vegetable plus sauce, in containers you can see through (out of sight is out of mind, then out to the trash). Label with the day you cooked it. And start with just lunches, or just three days — a small prep you repeat beats a heroic prep you abandon.',
 'Food safety is the non-negotiable part: cool cooked food within two hours, refrigerate promptly, and eat refrigerated preps within four days (freeze the rest). Reheat until steaming throughout, not just warm on the edges. When in doubt, throw it out — no money saved is worth a week of food poisoning.']},
{cat:'food-cooking',label:'Leftover safety',
 q:['How long do leftovers actually last?','How do I know if leftovers are still good?','Can I eat week-old leftovers?','How long can cooked food sit out?','Can you reheat leftovers more than once?','How do I store leftovers properly?'],
 s:{food:['cooked chicken','pasta','rice','soup']},
 a:['The rule to memorize: {food} and nearly all cooked leftovers last 3 to 4 days in the fridge, full stop. Not a week, not "until it smells funny" — four days max. The bacteria that cause food poisoning are invisible and odorless; "it smells fine" is not a safety test. When day five arrives, it goes out.',
 'The clock starts fast: cooked food should be refrigerated within two hours of cooking (one hour if the room is hot). Divide big batches into shallow containers so they cool quickly — a deep pot of soup stays warm in the middle for hours, which is exactly how bacteria thrive. Label with the date; future-you will not remember when "Tuesday" was.',
 'Reheating has its own rule: heat until steaming all the way through, around 74°C/165°F, stirring midway so there are no cold pockets. Microwaves heat unevenly, which is why the stir matters. And reheat only once — each cool-down and warm-up cycle is another window for bacteria. Take what you will eat, heat that.',
 'Freezing pauses the clock: most cooked foods freeze well for two to three months. Thaw in the fridge overnight, never on the counter all day. And trust the clear signs — mold, slime, off smells, fizzy textures mean discard immediately, no tasting to check. Your nose knows the obvious cases; the calendar handles the rest.']},
{cat:'food-cooking',label:'Cooking perfect rice',
 q:['How do I cook perfect rice every time?','Why does my rice always come out {problem}?','What is the secret to fluffy rice?','How do you cook rice on the stove?'],
 s:{problem:['mushy','sticky','burnt on the bottom','crunchy']},
 a:['{problem} rice almost always comes from the same two mistakes: wrong water ratio and peeking. For standard long-grain white rice, the ratio is 1 cup rice to 1.5 cups water (not 2 — that is the mush-maker). Rinse the rice first until the water runs mostly clear; that washes off the surface starch that causes gumminess.',
 'Then: bring to a boil, stir once, clamp the lid on, drop to the lowest heat, and do not touch it for 15 minutes. No peeking — lifting the lid releases the steam doing the actual cooking, and every peek adds minutes and unevenness. When the time is up, turn off the heat and let it rest, lid on, for 10 more minutes. The rest is not optional; it finishes the grains gently.',
 'Fluff with a fork, never a spoon — a spoon mashes, a fork separates. If the bottom still catches, your burner runs hot: use a diffuser, a heavier pot, or simply lower heat sooner. And salt the water lightly; unsalted rice tastes flat no matter how perfect the texture.',
 'Different rices, different rules, so stop using one method for all: brown rice needs more water and about 45 minutes; basmati wants a soak first; sushi rice wants slightly less water and a vinegar seasoning after. Master one type completely before branching out — perfect everyday white rice beats mediocre attempts at five varieties.']},
{cat:'food-cooking',label:'Keeping knives sharp',
 q:['How do I keep kitchen knives sharp?','How often should I sharpen kitchen knives?','What is the best way to sharpen a knife at home?','Why do my knives get dull so fast?','How do I use a honing steel?','Are expensive knives worth it?'],
 s:{surface:['a glass cutting board','the ceramic plate','the countertop']},
 a:['Knives go dull fast for one preventable reason: what they cut on. {surface} is harder than the blade and folds the edge over with every slice — switch to wood or soft plastic boards and your knives stay sharp dramatically longer. Never put good knives in the dishwasher either: the rattling, heat and detergent all dull and can loosen handles.',
 'Understand the two different jobs: honing and sharpening. A honing steel does not remove metal — it straightens the edge that folds over with use. A few light strokes before each cooking session keeps a sharp knife sharp. Actual sharpening (whetstone or a good pull-through) removes metal to create a new edge, and most home cooks need it only a few times a year.',
 'For sharpening at home, a whetstone gives the best edge but takes practice; a quality pull-through sharpener is nearly foolproof for beginners. Whatever you use, keep a consistent angle (about 20 degrees for most kitchen knives — picture two stacked coins under the spine) and work both sides evenly. Test on paper: a sharp knife slices newsprint cleanly.',
 'Store them so edges never touch anything hard: a magnetic strip, blade guards, or a block with slots — not loose in a drawer where they bang against everything. A sharp knife is genuinely safer than a dull one: it goes where you aim it instead of slipping. If a knife will not take an edge anymore, a professional sharpening service costs little and returns it like new.']},
{cat:'food-cooking',label:'Busy weeknight dinners',
 q:['What can I cook on a busy weeknight?','How do I make dinner fast on work nights?','What are easy meals for tired weeknights?','How do I cook when I have no energy?','How do I cook dinner in 15 minutes?','What should I always keep in the pantry?'],
 s:{meal:['stir-fry','sheet-pan dinner','tacos','pasta']},
 a:['The weeknight answer is a formula, not a recipe: {meal} built from what you have. Every fast dinner is protein plus vegetable plus starch plus a punchy sauce — and the sauce is what makes it taste intentional instead of desperate. Keep three bottled sauces you love on hand and weeknights transform.',
 'A {meal} works because everything cooks at once in one vessel. Toss chopped vegetables and protein with oil and seasoning on a sheet pan, roast at 220°C/425°F for 20 minutes, and dinner is done with one pan to wash. The real weeknight skill is not cooking — it is having the components: frozen vegetables, eggs, canned beans, pasta, and a protein that thaws fast.',
 'Lower the bar on purpose. A weeknight dinner needs to be fed, not impressive — a fried egg on rice with soy sauce, or beans and cheese in a tortilla, is a legitimate dinner. Save the ambitious cooking for weekends when you have energy to enjoy it. The people who cook on weeknights consistently are the ones who stopped trying to impress on weeknights.',
 'Build a tiny rotation: five to seven meals your household likes, that you can make half-asleep, with ingredients you always stock. Decision fatigue kills weeknight cooking more than lack of skill — "it\u2019s Tuesday, so it\u2019s tacos" removes the 6pm "what\u2019s for dinner" paralysis entirely. New recipes are for Sundays.']},
/* ============ TRAVEL ============ */
{cat:'travel',label:'Packing light',
 q:['How do I pack light for a week trip?','What is the secret to packing carry-on only?','How do I fit a week of clothes in a small bag?','What should I actually pack for a trip?','Should I check a bag or go carry-on only?','How do I pack toiletries for a flight?'],
 s:{days:['seven','five','ten']},
 a:['The secret is arithmetic, not willpower: for {days} days you do not need {days} outfits. Pack for half the trip and plan to do laundry once — every hotel has a sink, and a travel clothesline weighs nothing. Three bottoms, five tops, and layers beat a separate outfit per day in both weight and sanity.',
 'Choose a color palette where everything matches everything: dark neutrals plus one accent. Then every top works with every bottom and you stop packing "just in case" pieces that match nothing. Wear your bulkiest items on the plane — boots, jacket — and pack the light stuff. Shoes are the hidden weight killer: two pairs max, worn plus one.',
 'Roll clothes instead of folding — it genuinely saves space and reduces wrinkles. Use the inside of shoes for socks and chargers. Decant toiletries into small bottles; full-size bottles are the most common packing regret. And put a change of clothes plus essentials in your personal item, because bags get delayed and day one in yesterday\u2019s clothes is miserable.',
 'The mindset shift: you are packing for the trip you will actually take, not every hypothetical. "What if there\u2019s a fancy dinner?" — there will not be, or you will buy something there. Lay everything out, then remove a third. Nobody ever returned wishing they had packed more; everyone has wished they packed less.']},
{cat:'travel',label:'Finding cheap flights',
 q:['How do I find cheap flights?','When is the best time to book flights?','How do airlines price tickets?','What are the tricks to cheaper airfare?','Are budget airlines worth it?','Should I book flights directly or through a site?'],
 s:{tool:['a fare-comparison site','price alerts','an incognito browser window']},
 a:['Airline pricing is demand-based, so flexibility is the entire game. Flying midweek (Tuesday, Wednesday) and at odd hours is consistently cheaper than Friday evening and Sunday. If your dates can shift by even a day or two, use {tool} with a flexible-dates view — the cheapest day in a week is often dramatically cheaper than the most expensive.',
 'Book in the sweet spot: for domestic trips, roughly 1 to 3 months ahead; for international, 2 to 5 months. Booking a year out rarely helps and last-minute almost always hurts. Set {tool} and buy when the price drops into your target range instead of trying to time the absolute bottom — nobody catches that, and waiting usually costs more.',
 'Check the details that erase "cheap": budget fares with $60 bags each way, distant airports with $40 transfers, and basic-economy tickets that forbid changes. A $20 cheaper fare that cannot be changed is expensive insurance to skip. And clear cookies or use {tool} when searching repeatedly — prices have been observed creeping up on watched routes.',
 'The honest truth: the biggest savings come from where and when, not how. A flexible traveler going somewhere slightly off-peak beats a rigid traveler with every trick. If the fare will not budge, change the trip a little — nearby airport, shifted by two days — before paying peak prices out of stubbornness.']},
{cat:'travel',label:'Solo travel safety',
 q:['How do I stay safe traveling alone?','Is solo travel safe?','What should solo travelers watch out for?','How do I travel alone as a {traveler}?'],
 s:{traveler:['a woman','a first-timer','a young traveler']},
 a:['Solo travel is as safe as your habits make it, and {traveler} or not, the habits are the same. The core rule: look like you know where you are going even when you do not. Walk with purpose, check maps discreetly (step into a shop, not the middle of the sidewalk), and arrive in new places during daylight when possible. Confidence is camouflage.',
 'Share your itinerary with someone home: where you are sleeping each night and roughly what you are doing. Check in on a schedule. Keep your accommodation\u2019s address written down offline, carry a backup card separate from your wallet, and know the local emergency number before you need it. These take ten minutes and cover the scenarios that actually worry people.',
 'Trust your instincts aggressively — they are better data than politeness. If a situation, person or street feels wrong, leave; you never owe anyone your continued presence. Common sense covers most of the rest: watch your drink, do not flash expensive gear, learn the local scams for your destination (every place has two or three classics).',
 'And balance caution with openness, because the joy of solo travel is the people you meet. Stay in social hostels, take a walking tour on day one, eat at the bar — structured social settings are where solo travelers connect safely. Millions travel alone every year and come home with the best stories of their lives; preparation just makes sure yours is one of them.']},
{cat:'travel',label:'Beating jet lag',
 q:['How do I beat jet lag?','What is the fastest way to recover from jet lag?','How do I sleep on a long flight?','How do I adjust to a new time zone quickly?','Does melatonin help with jet lag?','How do I sleep on a plane?'],
 s:{direction:['east','west']},
 a:['Jet lag is your body clock disagreeing with the local clock, and light is what resets it — not pills, not willpower. Flying {direction}, the strategy differs: after flying east, get bright morning light at your destination; after flying west, seek afternoon light. Light at the wrong time pushes your clock the wrong way, which is why "just get sunlight" needs the timing right.',
 'Start before you board: three days out, shift sleep by an hour a day toward destination time, and set your watch to destination time when you board. On the plane, sleep if it is night at your destination, stay awake if it is day — eat and move on destination schedule. Hydrate aggressively; cabin air dehydrates you, and dehydration mimics and worsens jet-lag fatigue.',
 'On arrival, anchor to the new day immediately. Get outside in daylight, eat meals at local times, and resist the 4pm nap — if you must nap, 20 minutes max with an alarm. Caffeine is fine before noon local time, a bad idea after. Melatonin (a small dose at local bedtime for a few nights) helps many travelers fall asleep on the new schedule.',
 'Expect roughly one day of adjustment per time zone crossed — that is biology, not failure. Plan important meetings for day two or three, not day one. And be kind to yourself on arrival day: you are not lazy, you are literally in the wrong time. The travelers who recover fastest are the ones who commit fully to the new clock from touchdown.']},
{cat:'travel',label:'Planning a road trip',
 q:['How do I plan a road trip?','What should I pack for a road trip?','How do you plan road trip stops?','How long should you drive each day on a road trip?','What should I pack for a long drive?','How do I find good stops on a road trip?'],
 s:{hours:['six to eight','five to seven']},
 a:['Plan the skeleton, not every minute: your overnight stops and the must-see anchors, with the hours between left open. Driving {hours} hours a day is the sweet spot — enough to cover ground, short enough to actually enjoy a stop. More than that turns the trip into a driving job; the memories come from the unplanned two-hour detour, so leave room for it.',
 'Prep the car like it matters, because it does: check tires (including the spare), oil, coolant and wipers before you leave, not on day three in nowhere. Pack a real emergency kit — water, snacks, blanket, flashlight, basic tools, jumper cables, phone charger. Most road trip disasters are small problems far from help; the kit turns them into stories instead of ordeals.',
 'Budget honestly: fuel, food, lodging and a cushion for the thing you did not expect. Food is the sneaky cost — a cooler with drinks and sandwich supplies halves it and is healthier than gas-station roulette. Download offline maps for your whole route; cell signal dies exactly where you need directions most.',
 'Share driving if you can, and switch every couple of hours — fatigue is the real danger on long drives, not boredom. Plan one great stop per day rather than five rushed ones. And build in a buffer day: the trip always takes longer than the map says, and arriving home frazzled instead of rested ruins the afterglow. The best road trips feel unhurried, and unhurried is a planning choice.']},
/* ============ EVERYDAY LIFE ============ */
{cat:'everyday-life',label:'Building a morning routine',
 q:['What is a good morning routine?','How do I build a morning routine that sticks?','What should I do every morning?','How do I stop snoozing and get up?','How do I become a morning person?','Should I work out in the morning?'],
 s:{anchor:['making the bed','drinking a glass of water','opening the curtains']},
 a:['Forget the influencer version with ice baths and journaling marathons. A routine that sticks has three parts: an anchor, a body mover, and a day starter. The anchor is one tiny automatic action — {anchor} — that signals "the day has begun." Small and physical beats ambitious and mental; you need a win in the first two minutes.',
 'Then move your body for five to ten minutes: stretch, walk, a few push-ups — anything that raises your heart rate slightly. It wakes you more reliably than a second coffee. Then the day starter: glance at your calendar and pick the one thing that would make today a win. Three steps, fifteen minutes, done before the phone gets its hooks in.',
 'Protect it by preparing the night before: clothes out, bag packed, coffee set. Morning-you has no willpower; night-you is generous — let night-you do the favors. And put the alarm across the room. The snooze button is not rest, it is fragmented almost-sleep that makes you groggier; one alarm, feet on floor, lights on.',
 'Start with just the anchor for two weeks. When it is automatic, add the next piece. Routines built all at once collapse all at once; routines built one layer at a time survive bad weeks, travel and winter. The goal is not a perfect morning — it is a morning that starts itself.']},
{cat:'everyday-life',label:'Managing time better',
 q:['How do I manage my time better?','I never have enough time — what should I do?','How do productive people manage their day?','How do I stop wasting time?','How do I prioritize my tasks?','What is time-blocking?'],
 s:{method:['time-blocking','the "top three" list','the two-minute rule']},
 a:['You do not have a time problem — you have a clarity problem. Most "wasted" time is spent half-working on unclear priorities. The fix is {method}: each evening or morning, write the three things that would make today count, and do them before anything optional. Everything else is bonus. People who do this report the strangest thing: days feel longer.',
 'Give big tasks a home on the calendar. "Work on the report" floats forever; "report draft, Tuesday 10–11:30" gets done. {method} works because a vague intention loses to every distraction, but an appointment with yourself holds like any other meeting. Protect the first block of the day for your hardest thinking — willpower and focus genuinely decline as the day wears on.',
 'Shrink the small stuff with {method}: if it takes under two minutes, do it now instead of tracking it. Batch the rest — email twice a day, errands one trip, calls in a row. Every context switch costs attention; batching is how you buy it back. And audit one ordinary week: most people find two to three hours daily going to reflexive phone-checking they do not even enjoy.',
 'Finally, schedule rest like work. An unscheduled break becomes an hour of scrolling; a planned walk is recovery. Time management is not about cramming more in — it is about making sure the important things happen before the urgent things eat the day. Review weekly for ten minutes: what worked, what leaked, one fix. That loop is the whole system.']},
{cat:'everyday-life',label:'Staying motivated',
 q:['How do I stay motivated on long projects?','I lose motivation after a week — how do I keep going?','How do I motivate myself when I do not feel like it?','What do you do when motivation runs out?','How do I get motivated when I feel lazy?','Do vision boards actually work?'],
 s:{project:['a big project','learning something hard','a fitness goal']},
 a:['Here is the uncomfortable truth: motivation is unreliable, and every system built on "feeling like it" fails. The people who finish {project} do not have more motivation — they have systems that work without it. Stop trying to feel motivated and start designing for your unmotivated days: smaller steps, set times, removed friction.',
 'Make progress visible. A wall calendar with X marks, a progress bar, a journal of what you did — seeing the chain grow is motivating in a way that abstract goals never are. Break {project} into steps so small they feel silly; each completed step is a hit of "I am someone who does this," and identity is far more durable than mood.',
 'Reconnect with the why on a schedule, not just when struggling. Write down why {project} matters to you and read it weekly. Better: connect it to a person — who benefits when you finish? Abstract goals fade; "I promised my kid" or "my team is counting on this" endures. And tell someone your plan; social commitment quietly doubles follow-through.',
 'Plan for the dip instead of being surprised by it. Around week three, novelty dies — that is biology, not failure. Have a minimum version ready for bad days (ten minutes counts), and a rule: never miss twice. One missed day is life; two is the start of quitting. Motivation starts the engine, but systems, visibility and never-miss-twice are what arrive.']},
{cat:'everyday-life',label:'Decluttering the house',
 q:['Where do I start decluttering my house?','How do I declutter without getting overwhelmed?','What is the best method to declutter?','How do I get rid of stuff I might need later?','How do I declutter sentimental items?','Where can I donate old clothes?'],
 s:{area:['the kitchen counters','one closet','the junk drawer']},
 a:['Start with {area} — one small, visible, completable zone, not "the whole house." A single clear surface gives you a visible win in an hour, and that win fuels the next zone. Starting with the garage or attic is how decluttering dies on day one; starting small is how it finishes.',
 'Use the four-box method: Keep, Donate, Trash, Relocate. Touch each item once and decide — the "maybe" pile is just clutter with extra steps. For "I might need it later": if you have not used it in a year and it costs under $20 to replace, let it go. The storage cost of "maybe" across a whole house is enormous, and you will almost never rebuy it.',
 'Work in timed bursts: 30 minutes, timer on, music on. Decision fatigue is real — after about an hour your judgment degrades and everything becomes "keep." Short sessions over several days beat one exhausting marathon that ends with you sitting sadly among half-sorted boxes. And get donations out of the house the same day; bags that sit "to donate" migrate back onto shelves.',
 'Then stop the inflow, or you will redo this yearly. A one-in-one-out rule, a 30-day list for non-essential wants, and unsubscribing from sale emails do more long-term than any purge. Clutter is delayed decisions plus easy acquiring — fix both ends. A calmer house is not about minimalism; it is about everything you own earning its space.']},
{cat:'everyday-life',label:'Making small talk',
 q:['How do I make small talk less awkward?','I am bad at small talk — how do I get better?','What do you talk about with strangers?','How do I start conversations with people I do not know?','How do I join a conversation already in progress?','What topics should I avoid in small talk?'],
 s:{setting:['at a work event','at a party','in a waiting room']},
 a:['Small talk feels awkward because people treat it as a performance. It is not — it is a search: you are trading light topics until you find a shared thread, then following it. {setting}, the opener barely matters; "what brings you here?" or a genuine comment about the shared situation works. The goal of the first minute is not brilliance, it is giving them something easy to answer.',
 'Then ask open questions and actually listen: "How did you get into that?" beats "do you like your job?" because it invites a story. Follow the interesting thread — when their eyes light up on a detail, ask about that detail. People love talking about what they love; your job is just to find it and get out of the way. Two good questions beat ten clever statements.',
 'Have three pocket topics ready: something you did recently, something you are looking forward to, and a question about the event itself. This ends the panic-blank mind. And use names — remembering and using someone\u2019s name in conversation is the simplest warmth hack there is.',
 'Exit gracefully instead of fading: "It was great talking with you — I\u2019m going to grab a drink" is kind and clear. And reframe the whole thing: small talk is not shallow, it is the doorway. Every deep friendship started with an awkward first five minutes {setting}. The people who are "good at it" just practiced the doorway more.']}
];
/* ---------------- engine ---------------- */
function normCategory(g){
 if(!g) return null;
 var t=String(g).toLowerCase().trim().replace(/[^a-z0-9]+/g,'-').replace(/^-+|-+$/g,'');
 if(CATSLUGS.indexOf(t)>=0) return t;
 for(var i=0;i<CATSLUGS.length;i++){ if(CATSLUGS[i].indexOf(t)>=0||t.indexOf(CATSLUGS[i])>=0) return CATSLUGS[i]; }
 return null;
}
function famsOf(cat){ return FAMS.filter(function(f){return f.cat===cat;}); }
function fill(str,vals){
 return String(str).replace(/\{([a-z]+)\}/g,function(m,k){ return (k in vals)?vals[k]:m; });
}
function firstVals(fam){
 var v={};
 Object.keys(fam.s).forEach(function(k){ v[k]=fam.s[k][0]; });
 return v;
}
function relatedFor(fam,rnd){
 var others=FAMS.filter(function(f){return f!==fam;});
 var out=[],used={},i,f;
 for(i=0;i<others.length&&out.length<3;i++){
  f=pick(others,rnd);
  if(used[f.label]) continue; used[f.label]=1;
  out.push(fill(pick(f.q,rnd),firstVals(f)));
 }
 return out;
}
function familyForTopic(topic){
 var words=String(topic).toLowerCase().split(/[^a-z0-9]+/).filter(function(w){return w.length>2;});
 var best=null,bs=0,i,f,hay,s;
 for(i=0;i<FAMS.length;i++){
  f=FAMS[i]; hay=(f.label+' '+f.q.join(' ')).toLowerCase(); s=0;
  words.forEach(function(w){ if(hay.indexOf(w)>=0) s++; });
  if(s>bs){bs=s;best=f;}
 }
 return bs>0?best:null;
}
function generate(seed,opts,rnd){
 opts=opts||{}; rnd=rnd||prng(seed);
 var topic=(opts.topic||'').toString().trim().slice(0,120);
 var cat=normCategory(opts.genre||opts.category);
 var fam=null;
 if(topic){ fam=familyForTopic(topic); if(fam) cat=fam.cat; }
 if(!cat) cat=pick(CATSLUGS,rnd);
 var list=famsOf(cat);
 if(!fam) fam=pick(list,rnd);
 var vals={};
 Object.keys(fam.s).forEach(function(k){ vals[k]=pick(fam.s[k],rnd); });
 var question=fill(pick(fam.q,rnd),vals);
 if(topic && question.toLowerCase().indexOf(topic.toLowerCase().split(' ')[0])<0){
  question=question.replace(/\?$/,'')+' — asking about "'+topic+'"?';
 }
 var paras=fam.a.map(function(p){return fill(p,vals);});
 var answer=paras.join('\n\n');
 var summary=paras[0].length>160?paras[0].slice(0,157)+'...':paras[0];
 var id=PREFIX+String(seed).padStart(6,'0');
 return {
  id:id,
  title:question,
  question:question,
  category:cat,
  category_name:(CATS.filter(function(c){return c[0]===cat;})[0]||['',''])[1]||cat,
  description:summary,
  answer:answer,
  related_questions:relatedFor(fam,rnd),
  src:'signature',
  _seed:seed,
  topic:topic||undefined
 };
}
function validate(r){
 var e=[];
 if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
 if(!/^JAH-AUQ-\d{6}$/.test(r.id||''))e.push('id');
 if(typeof r.question!=='string'||r.question.length<10)e.push('question');
 if(typeof r.answer!=='string'||r.answer.length<400)e.push('answer');
 if(CATSLUGS.indexOf(r.category)<0)e.push('category');
 if(!Array.isArray(r.related_questions)||r.related_questions.length<2)e.push('related_questions');
 if(r.src!=='signature')e.push('src');
 return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
 var dups=(sample||[]).filter(function(r){return r&&r.title===record.title;});
 return dups.length?{ok:false,errors:['duplicate title in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-ai-usual-questions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,categories:CATSLUGS,families:FAMS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('ai-usual-questions',gen);
/* ---------------- indexed generation (archive seeding) ----------------
   Maps an ordinal j (0-based within a category) to a GUARANTEED-DISTINCT
   question by enumerating (template, slot-combination) pairs per family.
   Deterministic: same (catSlug, j, seed) always makes the same record. */
function slotsIn(tpl){
 var out=[],seen={};
 String(tpl).replace(/\{([a-z]+)\}/g,function(m,k){ if(!seen[k]){seen[k]=1;out.push(k);} return m; });
 return out;
}
function comboVals(fam,tpl,idx){
 var names=slotsIn(tpl),vals={},i,name,pool;
 for(i=names.length-1;i>=0;i--){
  name=names[i]; pool=fam.s[name]||[''];
  vals[name]=pool[idx%pool.length];
  idx=(idx/pool.length)|0;
 }
 return vals;
}
function distinctCount(fam){
 var n=0,i,names,prod;
 for(i=0;i<fam.q.length;i++){
  names=slotsIn(fam.q[i]); prod=1;
  names.forEach(function(k){ prod*=(fam.s[k]||['']).length; });
  n+=prod;
 }
 return n;
}
function generateIndexed(catSlug,j,seed){
 var list=famsOf(catSlug);
 if(!list.length) return null;
 var fam=list[j%list.length];
 var k=((j/list.length)|0),ti=0,rem=k,names,prod;
 for(ti=0;ti<fam.q.length;ti++){
  names=slotsIn(fam.q[ti]); prod=1;
  names.forEach(function(k2){ prod*=(fam.s[k2]||['']).length; });
  if(rem<prod) break;
  rem-=prod;
 }
 if(ti>=fam.q.length) return null;
 var vals=comboVals(fam,fam.q[ti],rem);
 var rnd=prng(seed*7919+13);
 Object.keys(fam.s).forEach(function(k2){ if(!(k2 in vals)) vals[k2]=pick(fam.s[k2],rnd); });
 var question=fill(fam.q[ti],vals);
 var paras=fam.a.map(function(p){return fill(p,vals);});
 var answer=paras.join('\n\n');
 var summary=paras[0].length>160?paras[0].slice(0,157)+'...':paras[0];
 var id=PREFIX+String(seed).padStart(6,'0');
 return {
  id:id,
  title:question,
  question:question,
  category:catSlug,
  category_name:(CATS.filter(function(c){return c[0]===catSlug;})[0]||['',''])[1]||catSlug,
  description:summary,
  answer:answer,
  related_questions:relatedFor(fam,rnd),
  src:'signature',
  _seed:seed
 };
}
gen.generateIndexed=generateIndexed;
gen.distinctCount=distinctCount;
gen.families=FAMS;
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();