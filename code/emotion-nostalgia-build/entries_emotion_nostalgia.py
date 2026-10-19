#!/usr/bin/env python3
"""Entries for the Nostalgia Emotion databases (Manon's 2026-10-17 16:15 order,
emotion series batch 2).

Descriptive and educational ONLY - the database describes and simulates
nostalgia; it never diagnoses real people, never labels any real person with
an emotional state, and never offers therapeutic advice beyond general, safe,
everyday guidance. No clinical language, no diagnostic labels.

34 records, ordered by the teaching ladder (ladder_rank 1-10,
non-decreasing), following the shared emotion-template spec:
what nostalgia IS -> first-person simulation -> body signals -> facial
expression -> triggers -> behavior -> healthy expression -> recognizing it
in others -> related emotions and mixes -> complex behavioral simulation.

ID prefixes: JAH-EMNO- (public) and JAH-EMNOS- (signature), verified free
in the manifest id_prefix values and in all jah-databases-data-1 shard
index files (zero 'JAH-EMNO' substring hits), 2026-10-17.

Public records are real, fact-checked psychology knowledge (Sedikides,
Wildschut, Routledge, Davis, Boym, Batcho, APA Dictionary, Lazarus, Gross,
Damasio, Barrett, Scherer, Ekman, Izard). Signature editions are his
original Signature lens - nostalgia as the soul's time-hearth, the homeland
signal: treasure, anchor, and fuel - never presented as authentic public
record.

Never the words "bat belt" anywhere. No website references. No Facebook.
No religious talk. Nothing hate-adjacent, profane, or inappropriate.
"""

SIG_TAIL = ("Signature original - his original Signature lens: nostalgia as "
            "the soul's time-hearth, the homeland signal - treasure, anchor, "
            "and fuel for the road ahead. Signature editions frame every "
            "facet as a kept treasure put to work: never as a diagnosis, "
            "never labeling any real person, and never presented as "
            "authentic public record.")

CIT_SEDIKIDES_2008 = ("Sedikides C, Wildschut T, Arndt J, Routledge C. "
                      "Nostalgia: past, present, and future. Current Directions "
                      "in Psychological Science. 2008;17(5):304-307.")
CIT_WILDSCHUT_2006 = ("Wildschut T, Sedikides C, Arndt J, Routledge C. "
                      "Nostalgia: content, triggers, functions. Journal of "
                      "Personality and Social Psychology. 2006;91(5):975-993.")
CIT_ROUTLEDGE_2016 = ("Routledge C. Nostalgia: A Psychological Resource. "
                      "Routledge; 2016.")
CIT_DAVIS = ("Davis F. Yearning for Yesterday: A Sociology of Nostalgia. "
             "Free Press; 1979.")
CIT_BOYM = ("Boym S. The Future of Nostalgia. Basic Books; 2001.")
CIT_BATCHO = ("Batcho KI. Nostalgia: retreat or support in difficult times? "
              "American Journal of Psychology. 2013;126(3):355-367.")
CIT_APA = ("American Psychological Association. APA Dictionary of "
           "Psychology; current edition.")
CIT_LAZARUS = ("Lazarus RS. Emotion and Adaptation. Oxford University Press; "
               "1991.")
CIT_GROSS = ("Gross JJ, editor. Handbook of Emotion Regulation. 2nd ed. "
             "Guilford; 2014.")
CIT_DAMASIO = ("Damasio AR. Looking for Spinoza: Joy, Sorrow, and the "
               "Feeling Brain. Harcourt; 2003.")
CIT_BARRETT = ("Barrett LF. How Emotions Are Made: The Secret Life of the "
               "Brain. Houghton Mifflin Harcourt; 2017.")
CIT_SCHERER = ("Scherer KR, Wallbott HG. Evidence for universality and "
               "cultural variation of differential emotion response "
               "patterning. Journal of Personality and Social Psychology. "
               "1994;66(2):310-328.")
CIT_EKMAN = ("Ekman P. Emotions Revealed: Recognizing Faces and Feelings to "
             "Improve Communication and Emotional Life. Holt; 2003.")
CIT_IZARD = ("Izard CE. The Psychology of Emotions. Plenum; 1991.")
CIT_BOWER = ("Bower GH. Mood and memory. American Psychologist. "
             "1981;36(2):129-148.")

ENTRIES = [
# ---------------------------------------------------------------- 1-4: what nostalgia IS
dict(
    key="nostalgia_definition", name="What Nostalgia Is: A Plain-Language Definition",
    group="Foundations", ladder_rank=1, ladder_tier="foundations",
    description=(
        "Nostalgia is the bittersweet longing for what was. In everyday "
        "words: it is the warm, aching feeling that visits when a song, a "
        "smell, a photograph, or a place pulls you back to an earlier time "
        "in your life - and you find yourself smiling at the memory and "
        "hurting at its distance at the same time. Psychologists define "
        "nostalgia as a predominantly positive, self-relevant emotion: the "
        "mental replay of personally meaningful past experiences, usually "
        "shared with people who mattered. The word comes from the Greek "
        "nostos (homecoming) and algos (pain) - the ache of the return that "
        "cannot quite happen. Modern research has flipped the old view: "
        "nostalgia was once treated as a sickness of the homesick, but "
        "study after study now shows it is mostly a psychological resource - "
        "a way the mind steadies itself, reminds itself who it is, and "
        "borrows strength from good times to face hard ones. It is not a "
        "mood that drifts in uncaused; it arrives with a trigger and points "
        "at a specific past. It is not depression and not mere memory: "
        "memory is the recall, nostalgia is the feeling the recall "
        "carries."),
    how_it_works=(
        "The nostalgia sequence runs in three beats: cue, replay, and "
        "meaning. First, a cue - a song from a particular summer, the smell "
        "of a certain kitchen, an anniversary date, an old photograph - "
        "lands in awareness. Cues work because memory is associative: one "
        "sense impression can unlock a whole scene, and emotionally rich "
        "scenes are stored with the most detail. Second comes the replay: "
        "the mind re-inhabits the scene, often from a first-person view, "
        "re-experiencing the people, the place, the feeling of belonging. "
        "The replay is selective - the mind highlights the warmth, the "
        "laughter, the closeness - which is why nostalgic memories feel "
        "brighter than the days themselves felt. Third comes meaning: the "
        "replay feeds the present self. Researchers describe nostalgia as a "
        "meaning-making emotion - it reminds the person of continuity (I am "
        "still the person who lived that), of connection (I belonged, I was "
        "loved), and of worth (my life has had good chapters). That is why "
        "nostalgia so often follows loneliness, boredom, or "
        "meaninglessness: the mind reaches back for proof that life has "
        "mattered, and then carries that proof forward."),
    key_points=[
        "Nostalgia is bittersweet: warmth and ache together, with the warmth usually winning.",
        "It is self-relevant and social: the remembered past is populated by people who mattered.",
        "The old view treated it as sickness; modern research treats it as a psychological resource.",
        "Memory is the recall; nostalgia is the feeling the recall carries.",
        "It usually arrives with a trigger - song, smell, place, date, photograph - not out of nowhere.",
        "Its core function is meaning-making: continuity, connection, and self-worth.",
        "It tends to visit when the present feels lonely, dull, or uncertain.",
        "Nostalgic replay is selective - the mind brightens the warmth of the scene."],
    requirements=[
        "Use plain everyday language before introducing any technical term.",
        "Present the bittersweet quality as the defining trait.",
        "Distinguish nostalgia from mere memory and from depression.",
        "Ground claims in published nostalgia research."],
    standards=[
        "Descriptive and educational only; never diagnose or label any real person.",
        "Present the resource view of nostalgia with its research basis.",
        "Keep the tone warm and explanatory, never clinical."],
    citations=[CIT_SEDIKIDES_2008, CIT_WILDSCHUT_2006, CIT_APA],
    sig_lens=(
        "The Signature lens reads nostalgia as the soul's time-hearth: the "
        "fireplace the self keeps burning with the best of its past, so the "
        "present never has to be cold. A homecoming signal, not a sickness - "
        "the past kept as treasure, put to work as fuel for the road "
        "ahead.")),
dict(
    key="nostalgia_emotion_family", name="Where Nostalgia Sits in the Emotion Family",
    group="Foundations", ladder_rank=2, ladder_tier="foundations",
    description=(
        "Nostalgia is a complex, blended emotion - not a basic one like joy "
        "or fear. It sits at the crossing of several emotion families. Its "
        "parents are happiness and sadness: the warmth of a cherished memory "
        "blended with the ache of its distance, which is why the "
        "bittersweet label fits so exactly. Emotion researchers place it "
        "among the self-conscious, meaning-laden emotions rather than the "
        "fast survival reflexes: it needs a self, a past, and a story. It is "
        "closely related to longing (wanting what is absent), wistfulness "
        "(a gentle, dreamy sadness), sentimentality (tender feeling toward "
        "the past or the tender), and homesickness (longing for a place or "
        "people). Its near-opposites are anticipation (leaning into the "
        "future) and boredom's dull flatness (nothing matters). "
        "Understanding the family helps because each relative shades "
        "nostalgia differently: add more sadness and it leans toward grief; "
        "add more joy and it leans toward gratitude; add fear of loss and it "
        "leans toward homesickness. Nostalgia itself is the balanced blend - "
        "the one where the sweetness outweighs the bitter."),
    how_it_works=(
        "Blended emotions form when two or more basic affective ingredients "
        "fire together and the mind reads the combination as one named "
        "feeling. In nostalgia, the positive ingredient comes from "
        "reward-related remembering: recalling closeness, love, triumph, and "
        "belonging re-activates some of the warmth those moments carried. "
        "The negative ingredient comes from appraisal of absence: the mind "
        "notes that the moment is gone, the people are scattered, the place "
        "has changed. Appraisal theories of emotion explain the blend - the "
        "same past can be read as 'I had something wonderful' (joy) and 'it "
        "is behind me' (sadness) at once. Which ingredient dominates depends "
        "on context: among friends sharing stories, the joy dominates; alone "
        "on an anniversary, the sadness can swell. The blend is what makes "
        "nostalgia a resource rather than a wound: the positive ingredient "
        "keeps the person engaged with the memory instead of crushed by it, "
        "so the memory can do its meaning-making work."),
    key_points=[
        "Nostalgia is complex and blended, not a basic survival emotion.",
        "Its two parent ingredients are happiness (the cherished memory) and sadness (its distance).",
        "It is self-conscious and story-based: it needs a self, a past, and a narrative.",
        "Close relatives: longing, wistfulness, sentimentality, homesickness.",
        "Near-opposites: anticipation (future-leaning) and flat boredom.",
        "Context shifts the blend: company tips it toward joy, solitude toward ache.",
        "The positive ingredient is what lets nostalgia function as a resource.",
        "Naming the blend helps people recognize which shade they are feeling."],
    requirements=[
        "Explain blended emotions in plain language.",
        "Name the parent ingredients and the close relatives.",
        "Show how context shifts which ingredient dominates."],
    standards=[
        "Descriptive and educational only; never diagnose or label any real person.",
        "Keep family relationships accurate to published emotion theory."],
    citations=[CIT_LAZARUS, CIT_WILDSCHUT_2006, CIT_IZARD],
    sig_lens=(
        "The Signature lens places nostalgia at the hearth of the emotion "
        "family: the room where joy and sorrow sit together by the same "
        "fire. Its relatives are the household - longing, wistfulness, "
        "homesickness - and nostalgia is the eldest, the one that turns "
        "every visitor's story into warmth for the whole house.")),
dict(
    key="nostalgia_intensity_scale", name="How Strong Nostalgia Can Get: Mild to Intense",
    group="Foundations", ladder_rank=2, ladder_tier="foundations",
    description=(
        "Nostalgia comes in volumes, and it is the same emotion at every "
        "setting. At mild intensity, it is a passing warmth: a song on the "
        "radio tugs a smile, a familiar smell pauses you for a second, and "
        "then the day continues. The body barely registers it; the mind "
        "notes 'that was nice' and moves on. At moderate intensity, it "
        "settles in: an old photo album pulls you into the chair for twenty "
        "minutes, stories pour out at a reunion dinner, a childhood street "
        "walked again slows your steps and fills your chest. You feel the "
        "ache under the warmth now - the awareness that this was then and "
        "this is now. At high intensity, nostalgia can flood: an "
        "anniversary, a homecoming after years away, or the loss of someone "
        "central to the memories can bring tears, a hollow chest, hours "
        "lost in replay, and a pull so strong the present feels thin by "
        "comparison. The volume is set by three dials: how personally "
        "central the memory is, how strong the cue is, and how vulnerable "
        "the present moment feels. Loneliness, endings, and big transitions "
        "turn all three dials up."),
    how_it_works=(
        "Intensity scales with memory centrality, cue strength, and present "
        "need. Central memories - first love, childhood home, a lost parent "
        "- carry dense associative networks, so one cue can detonate a "
        "whole era; peripheral memories (a jingle from a commercial) make "
        "only a ripple. Cue strength follows the senses: smell and music are "
        "the strongest nostalgia triggers because olfactory and auditory "
        "memory bypass much of the usual verbal filtering and land "
        "directly in emotional memory. Present need acts as a multiplier: "
        "research finds nostalgia spikes when people feel lonely, bored, or "
        "existentially adrift - the mind reaches for the past as a "
        "counterweight. The same song at a happy barbecue is background "
        "warmth; the same song alone on the anniversary of a loss is a "
        "flood. Duration follows intensity: mild passes in seconds, "
        "moderate lingers for an hour, intense can color a whole evening - "
        "but even intense nostalgia typically resolves as the person "
        "re-engages with the present, often carrying renewed steadiness "
        "from the visit."),
    key_points=[
        "Same emotion at every volume: mild warmth, moderate settling-in, intense flooding.",
        "Mild: a passing smile from a song or smell, gone in seconds.",
        "Moderate: twenty minutes in a photo album, stories at a reunion, ache under the warmth.",
        "Intense: tears, hours of replay, the present feeling thin - usually around anniversaries, homecomings, loss.",
        "Three dials set the volume: memory centrality, cue strength, present vulnerability.",
        "Smell and music are the strongest cues; they bypass verbal filtering.",
        "Loneliness, boredom, and transitions multiply intensity.",
        "Even intense episodes typically resolve, often leaving renewed steadiness."],
    requirements=[
        "Give concrete lived examples at each of the three volumes.",
        "Explain the three dials in plain language.",
        "Note the typical resolution of intense episodes."],
    standards=[
        "Descriptive and educational only; never diagnose or label any real person.",
        "Keep intensity descriptions vivid but non-clinical."],
    citations=[CIT_WILDSCHUT_2006, CIT_ROUTLEDGE_2016, CIT_BOWER],
    sig_lens=(
        "The Signature lens reads the volume knob as the hearth's draft: "
        "mild is embers glowing, moderate is the fire catching, intense is "
        "the blaze that lights the whole room. Every setting burns the "
        "same wood - treasured time - and the wise keeper learns to tend "
        "the draft rather than fear the flame.")),
dict(
    key="nostalgia_myths", name="Common Myths and Misunderstandings About Nostalgia",
    group="Foundations", ladder_rank=3, ladder_tier="foundations",
    description=(
        "Myth one: nostalgia is just living in the past. In fact, researchers "
        "find nostalgia is forward-looking: it borrows the past's proof of "
        "meaning to steady the person for the future, and it reliably "
        "increases optimism and the motivation to pursue goals. Myth two: it "
        "is a sickness. The word began as a medical diagnosis of homesick "
        "soldiers centuries ago, but modern studies show nostalgic "
        "reflection is mostly positive and linked to well-being, not "
        "illness. Myth three: only sad or lonely people get nostalgic. "
        "Everyone does - it is a universal human capacity - though "
        "loneliness and boredom do invite it more often. Myth four: "
        "nostalgia means the past was better. Nostalgic memory is selective: "
        "the mind highlights the warmth and edits the hardship, so the past "
        "feels golden by design; the feeling is real, the highlight reel is "
        "not the whole film. Myth five: it makes you stuck and unproductive. "
        "Used as a visit rather than a residence, nostalgia restores a sense "
        "of continuity and connection that helps people act in the present. "
        "The grain of truth in each myth: unchecked, any emotion can become "
        "a rut - but that is true of nostalgia's misuse, not of nostalgia "
        "itself."),
    how_it_works=(
        "Myths persist because they mistake the signal for the malfunction. "
        "The 'living in the past' myth confuses the direction of travel: "
        "nostalgia's replay runs backward, but its function runs forward - "
        "studies show nostalgia increases perceived meaning in life, "
        "self-esteem, and optimism about the future, which are all "
        "future-facing resources. The sickness myth survives from history: "
        "the term was coined for a supposed disease, and the label outlived "
        "the diagnosis by two centuries. The 'past was better' myth mistakes "
        "a feature for a bug: memory's positive editing is exactly what "
        "lets the past serve as a resource - the mind is not filing an "
        "accurate archive, it is keeping a treasury. The stuckness myth "
        "confuses frequency with function: people who ruminate do feel "
        "worse, but rumination is a different process (repetitive, "
        "unresolved looping) from nostalgia (a meaningful visit with a "
        "return trip). Teaching the distinction matters because believing "
        "nostalgia is harmful can make people fight a feeling that was "
        "trying to help them."),
    key_points=[
        "Myth: living in the past. Reality: nostalgia is forward-looking; it boosts optimism and goal motivation.",
        "Myth: a sickness. Reality: an old medical label; modern research links it to well-being.",
        "Myth: only sad people feel it. Reality: universal; loneliness and boredom merely invite it more.",
        "Myth: the past was better. Reality: memory edits for warmth; the feeling is real, the reel is selective.",
        "Myth: it makes you stuck. Reality: as a visit, not a residence, it restores continuity and steadies action.",
        "Rumination (unresolved looping) is a different process from nostalgia (a meaningful visit).",
        "Believing nostalgia is harmful can make people fight a feeling that was trying to help."],
    requirements=[
        "State each myth plainly, then the finding that corrects it.",
        "Give the grain of truth where one exists.",
        "Distinguish nostalgia from rumination."],
    standards=[
        "Descriptive and educational only; never diagnose or label any real person.",
        "Attribute corrections to published research findings."],
    citations=[CIT_SEDIKIDES_2008, CIT_ROUTLEDGE_2016, CIT_DAVIS],
    sig_lens=(
        "The Signature lens treats the myths as smoke around a true fire: "
        "each myth mistakes the hearth for a house fire. The keeper's "
        "answer is not to douse the flame but to learn the difference "
        "between visiting the treasury and moving into it.")),
# ------------------------------------------------- 5-9: first-person simulation
dict(
    key="nostalgia_first_person", name="Inside the Feeling: A First-Person Passage of Nostalgia",
    group="Foundations", ladder_rank=3, ladder_tier="foundations",
    description=(
        "It starts with the smell - old paper, maybe, or rain on hot "
        "pavement - and suddenly I am not quite here anymore. I am ten "
        "again, or twenty, standing in a kitchen that does not exist in "
        "this city, hearing a voice I have not heard in years say my name "
        "the old way. My chest does two things at once: it warms, like "
        "someone just put a hand over my heart, and it hollows, like the "
        "hand is remembering rather than touching. I smile without deciding "
        "to. My eyes sting a little, not from grief exactly - from the "
        "sharpness of it, the way a beautiful chord can sting. Time goes "
        "soft at the edges. The room I am actually in feels far away and "
        "slightly thin, like a photograph of a room, while the remembered "
        "room feels solid under my feet. I want to stay and I want to go "
        "back, both at once. And underneath it all, quiet but unmistakable, "
        "is a kind of gratitude: this happened. I was there. I belonged to "
        "people who are woven into me, and no amount of years can unwoven "
        "that. That is the feeling from the inside - not sadness wearing a "
        "costume, but love with its hand on the doorknob of the past."),
    how_it_works=(
        "First-person simulation works by translating research findings "
        "into the grammar of lived experience. The dual chest sensation - "
        "warmth plus hollowness - mirrors the blended appraisal: positive "
        "affect from the rewarding memory running alongside the negative "
        "affect of recognized absence. The smile that arrives unchosen "
        "reflects nostalgia's predominantly positive tone: studies of "
        "nostalgic narratives find more positive than negative emotion "
        "words, and facial studies of recalled warmth show the soft, "
        "involuntary smile of genuine positive affect. The sting behind the "
        "eyes is the arousal spike of a vivid, self-relevant memory "
        "arriving all at once. The 'thin present, solid past' effect is "
        "attentional absorption: working memory has limited bandwidth, and "
        "a richly detailed replay temporarily outcompetes current "
        "surroundings for processing priority. The closing gratitude is "
        "the meaning-making function made conscious - continuity, "
        "connection, and worth surfacing as felt knowledge rather than "
        "abstract thought. Simulation passages like this are educational "
        "tools: they let a reader recognize the pattern in their own "
        "experience without anyone diagnosing them."),
    key_points=[
        "The signature sensation: warmth and hollowness in the chest at once.",
        "An unchosen soft smile - nostalgia's positive tone showing on the face.",
        "Eyes may sting from the sharpness and arousal of the vivid recall.",
        "Time softens at the edges; attention is absorbed by the replay.",
        "The remembered scene can feel more solid than the present room.",
        "Underneath: gratitude and belonging - continuity, connection, worth.",
        "The passage is a recognition tool, not a diagnosis of anyone."],
    requirements=[
        "Write in present-tense first person with concrete sensory detail.",
        "Carry the bittersweet blend through every paragraph.",
        "End on the meaning-making note, not on the ache."],
    standards=[
        "Descriptive and educational only; never diagnose or label any real person.",
        "Keep the passage universal - no specific real people, places, or brands."],
    citations=[CIT_WILDSCHUT_2006, CIT_DAMASIO],
    sig_lens=(
        "The Signature lens calls this the hearth-visit: the keeper steps "
        "through the remembered door, warms both hands at the old fire, and "
        "returns with the smell of smoke in their clothes - proof of "
        "belonging, carried back into the present as fuel.")),
dict(
    key="nostalgia_time_course", name="How Nostalgia Changes Over Time: Onset, Peak, Fading, Aftershock",
    group="Foundations", ladder_rank=4, ladder_tier="foundations",
    description=(
        "A nostalgia episode has a shape in time. Onset is fast and often "
        "uninvited: a cue lands - the first bars of a song, a particular "
        "light in late afternoon, a name spoken aloud - and within seconds "
        "the replay begins. There is a small intake of breath, a pause; the "
        "person may stop mid-step or mid-sentence. The rise takes seconds to "
        "a minute: the scene fills in, the people arrive, the feeling "
        "swells as detail accumulates. Peak is the full immersion: minutes "
        "where the past feels present, the chest is full, the eyes may "
        "shine, and the outside world recedes. Peak rarely lasts long - "
        "attention is expensive, and the present keeps knocking. Fading is "
        "gradual and usually gentle: the scene thins, the room returns, the "
        "ache softens into warmth. What remains is the aftershock, and this "
        "is nostalgia's gift: a lingering steadiness, a quieter kind of "
        "confidence, sometimes a resolve - to call someone, to keep "
        "something, to live the present more deliberately. The whole arc, "
        "for an ordinary episode, runs a few minutes; around strong "
        "triggers it can color an evening. The aftershock can last days, "
        "and that is the point: the visit ends, the strength stays."),
    how_it_works=(
        "The time course follows attention and appraisal dynamics. Onset is "
        "rapid because associative memory is rapid: a cue activates a "
        "memory network in milliseconds, and emotionally tagged networks "
        "activate fastest. The rise reflects elaboration: each retrieved "
        "detail cues further details (the song brings the car, the car "
        "brings the road, the road brings the passenger), and affect "
        "intensifies with elaboration. Peak corresponds to maximal "
        "attentional absorption, when the replay occupies most of working "
        "memory. Fading begins when present-tense demands compete "
        "successfully for attention - a voice, a task, a sensation - and "
        "the replay loses bandwidth. The aftershock is the functional "
        "payoff: research on nostalgia's effects finds increased meaning, "
        "self-esteem, optimism, and social connectedness after nostalgic "
        "reflection, which is why the episode's end often feels like a "
        "settling rather than a loss. When fading does not come - when the "
        "replay loops without resolution - the process has tipped from "
        "nostalgia into rumination, a different mechanism with different "
        "consequences."),
    key_points=[
        "Onset: fast, often uninvited; a cue lands and the replay begins in seconds.",
        "Rise: detail accumulates (song brings car brings road brings passenger); feeling swells.",
        "Peak: full immersion for minutes; past feels present; outside world recedes.",
        "Fading: gradual and usually gentle as present demands reclaim attention.",
        "Aftershock: lingering steadiness, confidence, sometimes resolve - the functional payoff.",
        "Ordinary episodes run minutes; strong triggers can color an evening; aftershock can last days.",
        "If the replay loops without resolution, it has tipped into rumination, not nostalgia."],
    requirements=[
        "Describe each phase with its felt markers and typical duration.",
        "Explain the mechanism behind the rise and the aftershock.",
        "Distinguish the fading of nostalgia from the looping of rumination."],
    standards=[
        "Descriptive and educational only; never diagnose or label any real person.",
        "Keep phase descriptions concrete and time-anchored."],
    citations=[CIT_SEDIKIDES_2008, CIT_BOWER, CIT_GROSS],
    sig_lens=(
        "The Signature lens reads the arc as the keeper's round: kindling "
        "(the cue), blaze (the peak), banking the coals (the fade) - and "
        "the warm room left behind (the aftershock). The visit is brief; "
        "the heat it leaves is the whole purpose.")),
dict(
    key="nostalgia_low_vs_high", name="Low Intensity vs High Intensity: Two Lived Snapshots",
    group="Foundations", ladder_rank=4, ladder_tier="foundations",
    description=(
        "Low intensity, Tuesday morning: the radio plays a song from "
        "fifteen years ago while coffee brews. I hum along without thinking "
        "about it. A small smile, a brief image - a dashboard, summer heat "
        "through a windshield - and it is gone before the coffee is poured. "
        "My shoulders stay loose, my breathing unchanged, my plans for the "
        "day untouched. It was pleasant the way sunlight through a window "
        "is pleasant: noticed, enjoyed, not pursued. High intensity, the "
        "same song at midnight on the anniversary of my father's death, "
        "driving past the house I grew up in: the first chord stops my "
        "breath. The dashboard is suddenly that dashboard; his laugh is "
        "suddenly in the passenger seat. My chest tightens and floods at "
        "once, tears come without permission, and I pull the car over "
        "because the road has gone blurry and the past has gone solid. For "
        "ten minutes I am not driving through my town; I am sitting in his "
        "kitchen while he tells a story I have heard a hundred times and "
        "would give anything to hear once more. When it passes, I sit "
        "quiet, emptied and somehow steadied, and drive home slower than I "
        "came. Same song, same memory network, same person - the difference "
        "is the dials: centrality of the loss, strength of the cue, and a "
        "present moment already tender with grief."),
    how_it_works=(
        "The two snapshots isolate the intensity dials. In the low case, all "
        "three dials sit near minimum: the memory is peripheral (a season, "
        "not a person), the cue is weak (background radio), and the present "
        "is neutral (a routine morning). Associative activation stays "
        "shallow - a fragment, not a scene - so affect stays mild and "
        "attention stays in the present. In the high case, all three dials "
        "sit near maximum: the memory is central (a lost parent, the "
        "childhood home), the cue is strong (the exact song, the actual "
        "street, the anniversary date stacking cues), and the present is "
        "already emotionally loaded. Deep activation recruits the full "
        "scene with sensory detail, affect spikes, and attention is captured "
        "- the driver pulls over because the replay is consuming the "
        "bandwidth driving needs. The steadied aftermath reflects the "
        "meaning function completing: the visit reaffirmed continuity and "
        "connection, so the person returns to the present resourced rather "
        "than depleted. Comparing the snapshots teaches the key lesson: "
        "intensity is information about the dials, not a verdict on the "
        "person."),
    key_points=[
        "Low: background song, brief smile, a passing image; day untouched.",
        "High: same song plus anniversary plus the old street; breath stops, tears, pulled over.",
        "Same memory network, same person - the dials make the difference.",
        "Centrality, cue strength, and present vulnerability set the volume.",
        "High intensity captures attention; the present genuinely recedes.",
        "The aftermath of a completed episode is steadiness, not depletion.",
        "Intensity is information about the dials, never a verdict on the person."],
    requirements=[
        "Write both snapshots in concrete first-person present tense.",
        "Use the same cue in both to isolate the dials.",
        "Close with the lesson the comparison teaches."],
    standards=[
        "Descriptive and educational only; never diagnose or label any real person.",
        "Keep both snapshots universal and unspecific about real identities."],
    citations=[CIT_WILDSCHUT_2006, CIT_ROUTLEDGE_2016],
    sig_lens=(
        "The Signature lens sees embers versus blaze from the same log: "
        "the Tuesday ember warms the hands in passing; the midnight blaze "
        "lights the whole room and shows the keeper, for a shining "
        "stretch, exactly who they are and where they come from.")),
dict(
    key="nostalgia_partner_blend", name="Nostalgia Mixed with Its Most Common Partner: The Bittersweet Blend",
    group="Foundations", ladder_rank=5, ladder_tier="foundations",
    description=(
        "Nostalgia's most constant companion is sadness - not the heavy, "
        "clinical kind, but the tender ache of absence. Together they make "
        "the bittersweet blend that everyone recognizes: the wedding photo "
        "that makes you beam and cry, the lullaby that soothes and stings, "
        "the hometown visit that fills and empties you in the same hour. In "
        "the blend, sadness does specific work: it marks the distance. "
        "Without it, the memory would be pure pleasant recollection, flat "
        "and museum-like. The ache is what makes the memory matter - it "
        "says 'this was precious and it is behind you,' and that "
        "preciousness is exactly what the warmth is celebrating. The two "
        "take turns leading: in the early seconds of a trigger, the joy of "
        "recognition often comes first (there it is!); the ache follows as "
        "the mind registers the gap (and it is gone). At reunions and "
        "anniversaries the blend can seesaw for hours - laughter tipping "
        "into tears and back, neither one winning, both true. People "
        "sometimes fear the sad half and try to feel only the sweet, but "
        "the blend is the point: research finds the sadness in nostalgia "
        "does not cancel its benefits - the mixture still raises meaning, "
        "connection, and optimism. The bitter is the proof of the sweet's "
        "value."),
    how_it_works=(
        "The blend forms through dual appraisal of the same memory content. "
        "One appraisal track reads the memory's intrinsic value - love, "
        "belonging, beauty, triumph - and generates positive affect. A "
        "parallel track reads the memory's temporal status - past, "
        "unrecoverable, changed - and generates the tender negative affect "
        "of loss. Because both appraisals target the same content "
        "simultaneously, the affects fuse into a single bittersweet "
        "feeling rather than alternating. Emotion research on mixed "
        "affective states shows that positive and negative affect are not "
        "opposite ends of one seesaw but partly independent channels that "
        "can run hot together - which is why 'happy and sad at once' is "
        "not a contradiction but a common human capacity, and why "
        "nostalgia is its clearest everyday example. The seesaw over time "
        "reflects attention shifting between the two appraisal tracks: "
        "focus on the people and the warmth rises; focus on the distance "
        "and the ache rises. Neither track needs to be suppressed for the "
        "blend to function - the benefits (meaning, self-esteem, optimism) "
        "emerge from the combination, not from either half alone."),
    key_points=[
        "Nostalgia's most common partner is tender sadness - the ache of absence.",
        "Sadness marks the distance; without it the memory would feel flat and museum-like.",
        "The ache proves the preciousness the warmth is celebrating.",
        "Joy of recognition usually arrives first; the ache follows as the gap registers.",
        "The blend can seesaw for hours at reunions - laughter tipping into tears and back.",
        "Positive and negative affect are partly independent channels; both can run hot together.",
        "The sadness does not cancel nostalgia's benefits - the mixture still raises meaning and optimism."],
    requirements=[
        "Name the partner emotion and the work it does in the blend.",
        "Explain the bittersweet mechanics in plain language.",
        "Show the blend over time, not just as a static mixture."],
    standards=[
        "Descriptive and educational only; never diagnose or label any real person.",
        "Keep the sadness described as tender and ordinary, never clinical."],
    citations=[CIT_WILDSCHUT_2006, CIT_LAZARUS, CIT_DAMASIO],
    sig_lens=(
        "The Signature lens names the blend the hearth's two woods: sweet "
        "wood for the flame, bitter bark for the smoke that makes the "
        "flame visible. Burn only the sweet and the fire gives no light; "
        "the bitter is what lets the keeper see by it.")),
dict(
    key="nostalgia_day_vignette", name="A Day in the Life: Nostalgia Running Through an Ordinary Day",
    group="Foundations", ladder_rank=5, ladder_tier="foundations",
    description=(
        "Morning: rain on the window smells like the summers at my "
        "grandmother's, and for half a minute I am shelling peas at her "
        "table while she hums. I smile into my coffee. The day begins a "
        "little warmer. Midday: a coworker mentions a street name from my "
        "old neighborhood, and the whole map of being nineteen unfolds "
        "behind my eyes - the bus route, the corner store, the friend who "
        "moved away. I am quiet for a moment, then I tell the story, and "
        "telling it feels like introducing two friends. Afternoon: cleaning "
        "a drawer, I find a ticket stub, a note in a hand I loved, a photo "
        "with the corners soft. I sit on the floor longer than the task "
        "needs. My chest does its two things - warmth, hollowness - and I "
        "let it. Evening: an old song comes on while I cook, and I sing the "
        "harmony part my sister always sang. I text her a line from it. She "
        "answers with three crying-laughing faces and a voice note, and "
        "suddenly the kitchen is full of us at fourteen and sixteen, "
        "arguing over the good verse. Night: the day's visits settle. I am "
        "not sad. If anything I feel more solid - as if the day kept "
        "showing me the receipts of a life that has held love, and the "
        "total keeps coming out in my favor. That is an ordinary nostalgic "
        "day: not an event, just the past walking alongside, keeping "
        "company."),
    how_it_works=(
        "The vignette demonstrates nostalgia's everyday ecology: it is not "
        "a rare flood but a frequent weather, arriving through ordinary "
        "cues. Each micro-episode follows the cue-replay-meaning arc on a "
        "small scale: a smell, a street name, a ticket stub, a song - each "
        "unlocks a fragment, each fragment carries its small charge of "
        "warmth and ache, each resolves into a steadier sense of self. "
        "The social sharing beats (telling the coworker, texting the "
        "sister) show nostalgia's interpersonal function: shared "
        "reminiscence converts private memory into social bonding, and "
        "research finds that sharing nostalgic memories increases "
        "closeness and perceived social support. The evening settling "
        "shows the cumulative aftershock: several small meaning-deposits "
        "across a day compound into an overall sense of continuity - the "
        "feeling that one's life hangs together as a story rather than a "
        "string of disconnected days. The vignette's lesson is dosage: "
        "nostalgia at this everyday volume is not an interruption of life "
        "but one of the ways life holds together."),
    key_points=[
        "Nostalgia is everyday weather, not a rare flood - it arrives through ordinary cues.",
        "Each micro-episode runs the cue-replay-meaning arc on a small scale.",
        "Sharing the memory (telling, texting) converts private recall into social bonding.",
        "Small meaning-deposits compound across a day into a sense of continuity.",
        "The day ends steadier, not sadder - the visits leave strength behind.",
        "Everyday-volume nostalgia is one of the ways a life holds together as a story."],
    requirements=[
        "Walk a full ordinary day with at least four distinct micro-episodes.",
        "Keep each episode small and recognizable.",
        "Show the social-sharing function and the cumulative settling."],
    standards=[
        "Descriptive and educational only; never diagnose or label any real person.",
        "Keep all characters and places generic and universal."],
    citations=[CIT_WILDSCHUT_2006, CIT_SEDIKIDES_2008],
    sig_lens=(
        "The Signature lens reads the ordinary day as the keeper's rounds: "
        "morning kindling, midday tending, afternoon stoking, evening "
        "banking the coals. Nothing dramatic - just the hearth kept lit, "
        "so the house of the self stays warm.")),
# ------------------------------------------------- 10-13: body signals
dict(
    key="nostalgia_body_signals", name="What Happens in the Body During Nostalgia",
    group="Compounded", ladder_rank=5, ladder_tier="compounded",
    description=(
        "Nostalgia is a quiet emotion in the body - there is no pounding "
        "heart, no clenched fist, no adrenaline surge. What happens instead "
        "is subtle and warm. The chest is the headquarters: a spreading "
        "warmth, sometimes described as a glow or a fullness, often paired "
        "with a gentle hollowness or tightness when the ache is strong. "
        "Breathing tends to slow and deepen - people take the involuntary "
        "sigh that marks a feeling landing, and the breath may catch for a "
        "beat at the onset of a strong cue. The heart does not race; if "
        "anything, the pulse steadies, and the body leans toward stillness "
        "rather than action. Muscles soften more than they tense: shoulders "
        "drop, the jaw unclenches, the hands go still - the body takes the "
        "posture of listening. The stomach is usually quiet; nostalgia "
        "rarely brings nausea or butterflies, though a strong wave can bring "
        "a flutter of the throat, the physical prelude to tears. Skin "
        "responses are the most visible: goosebumps along the arms when a "
        "song hits exactly right, a prickling at the scalp, eyes shining "
        "or spilling over. Energy does not spike - it settles. People "
        "describe feeling 'full,' 'soft,' 'held,' or 'heavy in a good way.' "
        "The overall bodily signature is one of tender activation: the "
        "nervous system is awake and moved, but the movement is inward, "
        "toward the memory, not outward toward the world."),
    how_it_works=(
        "The bodily profile follows from nostalgia's appraisal structure. "
        "High-arousal emotions (fear, anger) mobilize the sympathetic "
        "nervous system for action - faster heart, tensed muscles, shallow "
        "breath. Nostalgia's appraisal contains no threat and no demand for "
        "action; its core is valued past content held in attention. So the "
        "body shifts toward the parasympathetic-leaning state associated "
        "with safeness and social warmth: slower breath, softened muscle "
        "tone, steady heart. The chest warmth maps to interoceptive "
        "attention - when feeling is strong, awareness moves to the torso, "
        "and the brain reads that focused attention as sensation. "
        "Goosebumps and the throat flutter are brief sympathetic spikes "
        "riding on the calm base: moments of peak aesthetic or emotional "
        "intensity trigger piloerection, the same response music can cause, "
        "and the throat tightens as the tear response prepares. Tears "
        "themselves, when they come, are the body's pressure valve for "
        "overflow - not distress crying but the lacrimal system's response "
        "to being moved. The net effect is a body that is physiologically "
        "calm but emotionally full, which is why people can feel profoundly "
        "moved while sitting perfectly still."),
    key_points=[
        "The chest is headquarters: spreading warmth, sometimes paired with gentle hollowness.",
        "Breathing slows and deepens; the involuntary sigh marks the feeling landing.",
        "The heart steadies rather than races; the body leans toward stillness, not action.",
        "Muscles soften: shoulders drop, jaw unclenches, hands go still - the posture of listening.",
        "Goosebumps, scalp prickling, and shining eyes are the most visible signals.",
        "The throat flutter is the physical prelude to moved-tears, a pressure valve for overflow.",
        "Overall signature: tender activation - calm body, full heart, movement turned inward."],
    requirements=[
        "Cover heart, breath, muscles, stomach, skin, and energy in turn.",
        "Contrast the profile with high-arousal emotions.",
        "Keep all physiology ordinary and non-clinical."],
    standards=[
        "Descriptive and educational only; never diagnose or label any real person.",
        "Describe typical patterns, never universal claims about all bodies."],
    citations=[CIT_DAMASIO, CIT_SCHERER, CIT_WILDSCHUT_2006],
    sig_lens=(
        "The Signature lens reads the body as the hearth-room itself: the "
        "chest the fireplace, the slowed breath the bellows at rest, the "
        "goosebumps the sparks rising. The keeper's body does not brace or "
        "flee - it sits down by the fire, which is the whole posture of "
        "treasure kept well.")),
dict(
    key="nostalgia_posture_movement", name="Posture and Movement Signature of Nostalgia",
    group="Compounded", ladder_rank=6, ladder_tier="compounded",
    description=(
        "You can spot nostalgia in the body before a word is spoken. The "
        "signature posture is the lean-in of listening: head tilts slightly, "
        "chin may lower a fraction, gaze drifts up or to the middle "
        "distance - the classic 'looking inward' direction. The body goes "
        "still in a particular way - not the freeze of fear, but the "
        "settled stillness of someone who has stopped to receive something. "
        "Hands often find quiet occupations: cradling a mug, turning a "
        "photograph, tracing the edge of an object, or simply folding in "
        "the lap. At a song's first bars, people unconsciously close or "
        "half-close their eyes and may sway almost imperceptibly, the way "
        "bodies do when music takes the lead. Walking slows: the person "
        "revisiting an old street finds their steps shortening, pausing at "
        "corners, turning to look back. Touch becomes tender and "
        "exploratory - running fingers along a bookshelf, holding a letter "
        "a beat longer than reading requires. When the wave passes, there is "
        "often a small reset gesture: a deep breath, a shake of the head "
        "with a smile, a hand pressed briefly to the chest. None of this is "
        "performed; it is the body's honest choreography of attention "
        "turned backward while the feet stay planted in the present."),
    how_it_works=(
        "Posture follows attention. When the mind replays a scene, visual "
        "attention decouples from the environment - gaze drifts because the "
        "'seeing' is happening internally, and the eyes take the "
        "upward-or-inward angle long associated with visual recall. The "
        "head tilt and chin-lower are part of the listening set: the body "
        "treats the memory almost as a voice to be heard, orienting the "
        "senses toward it. Stillness serves the replay: movement generates "
        "sensory noise, and the brain quiets the body to give the memory "
        "bandwidth - the same reason people stop walking when a phone call "
        "gets important. The hand occupations are self-soothing and "
        "anchoring behaviors: touch provides a present-tense sensory "
        "anchor while the mind travels, keeping the person tethered. The "
        "sway with music is entrainment - the motor system locking to "
        "rhythm even at low amplitude. The reset gestures at the end (deep "
        "breath, head shake, hand to chest) are transition markers: the "
        "body signaling the shift of attention back to the present, often "
        "accompanied by the small smile of a completed visit."),
    key_points=[
        "Head tilts, chin lowers slightly, gaze drifts up or to middle distance - looking inward.",
        "Settled stillness: the body quiets to give the replay bandwidth, not a fear-freeze.",
        "Hands find quiet work: cradling, turning, tracing - touch as a present-tense anchor.",
        "Eyes half-close and the body may sway almost imperceptibly when music leads.",
        "Walking slows on old streets: shortened steps, pauses at corners, looking back.",
        "Reset gestures close the episode: deep breath, smiling head-shake, hand to chest.",
        "It is honest choreography of attention turned backward while the feet stay present."],
    requirements=[
        "Describe the head, gaze, torso, hands, and gait signatures concretely.",
        "Distinguish nostalgic stillness from fear-freeze.",
        "Include the closing reset gestures."],
    standards=[
        "Descriptive and educational only; never diagnose or label any real person.",
        "Present as typical patterns, not rules every body follows."],
    citations=[CIT_EKMAN, CIT_SCHERER],
    sig_lens=(
        "The Signature lens sees the keeper's stance: head bowed to the "
        "flame, hands busy with the treasures, feet planted at the "
        "hearth's edge. Every gesture says the same thing - I am here, "
        "and I am also there, and both places are mine.")),
dict(
    key="nostalgia_sleep_appetite_energy", name="Sleep, Appetite, and Energy Effects of Nostalgia",
    group="Compounded", ladder_rank=6, ladder_tier="compounded",
    description=(
        "Nostalgia's effects on the body's routines are gentle and mostly "
        "benign. Sleep: an evening of nostalgic reflection often precedes "
        "easy, warm sleep - the mind settles like an animal curling up, and "
        "people report drifting off with a sense of fullness rather than "
        "the buzzing of an overactive day. Intense episodes late at night "
        "can occasionally delay sleep, not from agitation but from "
        "absorption: one more song, one more page of the album, the replay "
        "too sweet to switch off. Dreams after nostalgic evenings often "
        "borrow the cast: old friends and old houses make cameo "
        "appearances. Appetite: nostalgia is famous for steering the hand "
        "toward comfort food - the dish from childhood, the recipe in a "
        "loved one's handwriting, the candy from a corner store that no "
        "longer exists. Eating becomes a form of time travel, and the food "
        "tastes of more than its ingredients. Energy: the net effect is "
        "usually restorative rather than draining. People emerge from a "
        "nostalgic spell feeling steadied and quietly replenished - the "
        "opposite of the exhaustion that follows rumination or grief. The "
        "exception is the intense, loss-centered wave, which can leave a "
        "pleasant heaviness, the way a long satisfying cry leaves the body "
        "loose and tired in a good way. None of this disrupts ordinary "
        "functioning; at everyday volume, nostalgia is one of the least "
        "physiologically costly emotions there is."),
    how_it_works=(
        "The sleep effect follows from arousal: nostalgia's calm, "
        "parasympathetic-leaning profile is compatible with sleep onset, "
        "unlike high-arousal emotions that delay it. The occasional delay "
        "is attentional, not physiological - the person chooses the replay "
        "over sleep, the way one chooses one more chapter of a good book. "
        "Dream incorporation reflects memory consolidation: the sleeping "
        "brain replays the day's salient material, and emotionally tagged "
        "nostalgic content qualifies as salient. The comfort-food pull is "
        "associative learning at its most literal: flavors encoded alongside "
        "love, safety, and belonging become cues for those feelings, so the "
        "dish functions as an edible time machine - taste and smell are "
        "among the strongest memory cues. The restorative energy effect "
        "matches the research findings: nostalgic reflection increases "
        "perceived meaning and self-esteem, and meaning is energizing - "
        "people act more readily when they feel their life hangs together. "
        "The pleasant heaviness after intense waves is the aftermath of "
        "sustained emotional processing plus tear-related parasympathetic "
        "rebound, the body's normal settling after being deeply moved."),
    key_points=[
        "Evenings of nostalgic reflection often precede easy, warm sleep.",
        "Intense late-night episodes can delay sleep through absorption, not agitation.",
        "Dreams may borrow the cast: old friends and old houses cameo.",
        "Nostalgia steers the hand toward comfort food - eating as time travel.",
        "Net energy effect is restorative: steadied and quietly replenished.",
        "Intense loss-centered waves can leave a pleasant heaviness, like after a good cry.",
        "At everyday volume it is among the least physiologically costly emotions."],
    requirements=[
        "Cover sleep onset, dreams, appetite, and energy in turn.",
        "Explain the comfort-food mechanism plainly.",
        "Note the benign overall profile with the honest exceptions."],
    standards=[
        "Descriptive and educational only; never diagnose or label any real person.",
        "No medical claims; describe typical everyday patterns only."],
    citations=[CIT_ROUTLEDGE_2016, CIT_BOWER, CIT_DAMASIO],
    sig_lens=(
        "The Signature lens counts these as the hearth's housekeeping: "
        "the keeper sleeps sound with the fire banked, eats from the old "
        "recipes without apology, and wakes restocked. The treasury does "
        "not tax the body; it feeds it.")),
dict(
    key="nostalgia_body_differences", name="How Body Signals Differ Between People",
    group="Compounded", ladder_rank=7, ladder_tier="compounded",
    description=(
        "No two bodies do nostalgia the same way. Some people are criers: "
        "the shine in the eyes arrives early and spills easily, at songs, "
        "speeches, even commercials. Others are stone-faced feelers - the "
        "chest is full but the face gives nothing away, and only the "
        "unusual stillness betrays them. Some get the goosebumps and scalp "
        "prickle strongly; others feel it almost entirely as warmth in the "
        "torso with no skin response at all. Age shades the pattern: "
        "children feel nostalgia in brief, bright flashes (last summer "
        "already glows); older adults often report the richest, most "
        "layered episodes, with decades of material and a practiced ease "
        "at the visit. Temperament matters: highly sensitive people tend "
        "toward stronger bodily responses across the board, while more "
        "reserved temperaments run the same emotion at lower physical "
        "volume. Culture shapes expression: in some families and "
        "communities, open tears at a memory are normal and expected; in "
        "others, the same feeling is carried privately with a steady face. "
        "Health and state matter too: exhaustion, illness, or hormonal "
        "shifts can turn the volume up or down on any given day. The "
        "constant across all this variation is the inner pattern - warmth, "
        "absorption, the bittersweet blend - wearing different bodily "
        "clothing in different people. There is no correct way for a body "
        "to do nostalgia."),
    how_it_works=(
        "Individual variation in emotional physiology comes from several "
        "sources. Expressivity - how much of inner feeling shows on the "
        "outside - varies as a stable trait; high-expressivity people show "
        "larger facial and autonomic responses to the same affective "
        "stimulus. Interoceptive sensitivity varies too: some people "
        "detect subtle bodily signals (the chest warmth, the throat "
        "flutter) vividly, others barely register them while feeling the "
        "emotion just as strongly - the feeling and the body-sensing are "
        "partly separate channels. Developmental stage changes the "
        "material: the depth and layering of nostalgic episodes grow with "
        "the stock of past to draw on, and emotion-regulation skill "
        "typically grows with age, which is why older adults often navigate "
        "intense episodes with more ease. Cultural display rules - the "
        "learned norms about which feelings may show - filter the outward "
        "signals without necessarily changing the inner feeling. State "
        "factors (fatigue, illness, stress load) modulate autonomic "
        "reactivity day to day. The educational point is anti-template: "
        "recognizing nostalgia in others, or in oneself, must allow for the "
        "full range, or the quiet feelers get missed and the criers get "
        "misread."),
    key_points=[
        "Criers vs stone-faced feelers: expressivity varies as a stable trait.",
        "Goosebumps people vs torso-warmth people: the channels differ, the feeling matches.",
        "Children: brief bright flashes. Older adults: richer, more layered episodes.",
        "Temperament sets the physical volume; culture sets the display rules.",
        "Fatigue, illness, and daily state modulate the volume day to day.",
        "The inner pattern (warmth, absorption, bittersweet blend) is the constant.",
        "There is no correct way for a body to do nostalgia - allow the full range."],
    requirements=[
        "Cover expressivity, age, temperament, culture, and state factors.",
        "Emphasize the constant inner pattern beneath the variation.",
        "End on the anti-template lesson."],
    standards=[
        "Descriptive and educational only; never diagnose or label any real person.",
        "Present variation as normal and expected, never as dysfunction."],
    citations=[CIT_SCHERER, CIT_EKMAN, CIT_BATCHO],
    sig_lens=(
        "The Signature lens honors every keeper's hearth-manners: some "
        "keep a roaring open fire, some a banked stove behind a closed "
        "door - the warmth inside is the same, and the wise visitor never "
        "mistakes a quiet house for a cold one.")),
# ------------------------------------------------- 14-17: facial expression
dict(
    key="nostalgia_face", name="The Face of Nostalgia: Eyes, Brows, Mouth, and Micro-Signs",
    group="Compounded", ladder_rank=7, ladder_tier="compounded",
    description=(
        "Nostalgia's face is soft and inward-turned - the opposite of a "
        "performed expression. The eyes are the center: they lose focus on "
        "the present, drifting to the middle distance or dropping to "
        "half-mast, and they shine - a brightness from moisture that has "
        "not yet become tears. The blink rate slows; the person looks like "
        "someone watching something only they can see, because they are. "
        "The brows rest in neutral or lift very slightly at the inner "
        "corners - the faint mark of tender feeling, not the knit of worry. "
        "The mouth holds the signature: a small, asymmetrical, unchosen "
        "smile, often just a lifting at one corner, sometimes pressed "
        "closed as if holding something in. It is not the broad social "
        "smile; it is private. The cheeks may lift slightly with it, but "
        "without the eye-crinkle of hearty laughter - the feeling is too "
        "tender for that. Micro-signs: a quick swallow as the throat "
        "flutters, a single slow blink that releases the shine, the lower "
        "lip drawn in for a moment, a breath taken through slightly parted "
        "lips at the onset. The whole face says 'I am somewhere else, and "
        "it is good there.' Because the expression is low-intensity and "
        "involuntary, it is easy to miss - but once you know it, you will "
        "see it across dinner tables, in car passenger seats, and in "
        "audiences when the old song starts."),
    how_it_works=(
        "The face follows the same attention logic as the body. Gaze "
        "decouples from the environment during internal replay, producing "
        "the unfocused middle-distance look and the slowed blink rate - "
        "blinking partially gates visual input, and less gating is needed "
        "when vision is not the active channel. The shine is lacrimal "
        "activation at low level: being moved triggers tear production "
        "before any spill, brightening the eyes. The inner-brow lift is "
        "the facial component long associated with tender and sad affect - "
        "a small, hard-to-fake movement that marks genuine feeling as "
        "opposed to social display. The small asymmetrical smile is the "
        "positive affect leaking through: genuine positive affect engages "
        "the mouth-corner lifters, but at nostalgia's low arousal the "
        "movement is partial and often one-sided. The swallow and the "
        "parted-lips breath are the body's management of the throat "
        "flutter described in the body-signals record. Together these form "
        "a coherent, low-energy, involuntary display - which is why "
        "nostalgia's face reads as authentic: it is difficult to produce "
        "deliberately in all its parts at once, and observers are good at "
        "sensing that coherence."),
    key_points=[
        "Eyes: unfocused, middle-distance or half-mast, shining with pre-tear moisture, slow blinking.",
        "Brows: neutral or a slight inner-corner lift - tender feeling, not worry.",
        "Mouth: small, asymmetrical, unchosen smile - private, not social.",
        "Micro-signs: quick swallow, single slow blink, lip drawn in, parted-lips breath at onset.",
        "Low-intensity and involuntary - easy to miss, hard to fake in all parts at once.",
        "The whole face reads: I am somewhere else, and it is good there."],
    requirements=[
        "Describe eyes, brows, mouth, and micro-signs in concrete visual terms.",
        "Explain the mechanism behind the gaze and the shine.",
        "Note why the expression reads as authentic."],
    standards=[
        "Descriptive and educational only; never diagnose or label any real person.",
        "Keep descriptions observable and behavioral, never interpretive of character."],
    citations=[CIT_EKMAN, CIT_SCHERER, CIT_WILDSCHUT_2006],
    sig_lens=(
        "The Signature lens calls this the hearth-face: the look of "
        "someone warmed from the inside. No performance in it - just the "
        "softened gaze of the keeper watching old flames dance, and the "
        "small smile of one who knows every story the fire is telling.")),
dict(
    key="nostalgia_face_intensity", name="How the Nostalgic Expression Changes with Intensity",
    group="Compounded", ladder_rank=7, ladder_tier="compounded",
    description=(
        "At mild intensity, nostalgia barely touches the face: perhaps a "
        "flicker at the mouth corner, a one-second softening around the "
        "eyes, gone before anyone notices. The person themselves may not "
        "realize they smiled. At moderate intensity, the full signature "
        "arrives: the gaze drifts and holds, the shine settles into the "
        "eyes, the small private smile stays for the length of a story, "
        "the head tilts. Observers can read it clearly now - the dinner "
        "table goes quiet for a beat, someone asks 'where did you just "
        "go?' At high intensity, the face opens further: the smile may "
        "widen and then crumple at the edges as the ache swells, tears "
        "spill or are blinked back hard, the hand comes up to the mouth or "
        "the eyes, the head may bow. The expression can oscillate visibly - "
        "smile, shine, swallow, smile again - as the bittersweet blend "
        "seesaws. After the peak, the face settles into a particular "
        "afterglow: relaxed, slightly luminous, the eyes soft, often with a "
        "lingering half-smile that can last many minutes. The progression "
        "is continuous, not stepped: each added increment of feeling adds "
        "amplitude to the same movements. Learning the scale matters "
        "because the mild end is where most everyday nostalgia lives - and "
        "it is the end most people miss, in others and in themselves."),
    how_it_works=(
        "Facial amplitude scales with affective intensity through the same "
        "dose-response relationship seen across emotions: stronger feeling "
        "recruits more muscle groups, holds expressions longer, and adds "
        "involuntary components (tears, throat movements) that mild levels "
        "do not reach. At the mild end, only the most automatic components "
        "fire - the micro-smile, the eye-softening - because they have the "
        "lowest activation threshold. Moderate intensity sustains the "
        "expression over time, which is what makes it readable: a fleeting "
        "micro-expression is missed, a held one is seen. High intensity "
        "adds the overflow components: lacrimal spillover (tears), the "
        "hand-to-face self-soothing gestures, the visible oscillation as "
        "attention shifts between the joy-track and the ache-track of the "
        "blend. The afterglow reflects the resolution phase: parasympathetic "
        "rebound plus the lingering positive affect of the meaning-making "
        "payoff, showing as relaxed features and the soft half-smile. The "
        "continuity of the scale - same movements, more amplitude - is "
        "itself informative: it confirms one emotion at different volumes "
        "rather than different emotions."),
    key_points=[
        "Mild: a flicker at the mouth corner, a one-second eye-softening; often unnoticed.",
        "Moderate: the full signature held over time - drifting gaze, shine, private smile, head tilt.",
        "High: smile widens then crumples, tears spill or are blinked back, hand to face, visible oscillation.",
        "Afterglow: relaxed, slightly luminous face with a lingering half-smile.",
        "Same movements at every level, more amplitude with more feeling - one emotion, many volumes.",
        "The mild end is where most everyday nostalgia lives, and the end most often missed."],
    requirements=[
        "Walk the face through mild, moderate, high, and afterglow.",
        "Explain the dose-response logic in plain language.",
        "Emphasize the continuity of the scale."],
    standards=[
        "Descriptive and educational only; never diagnose or label any real person.",
        "Keep the scale observational and concrete."],
    citations=[CIT_EKMAN, CIT_SCHERER],
    sig_lens=(
        "The Signature lens reads the scale as firelight on the keeper's "
        "face: ember-glow at mild, lamplight at moderate, full blaze at "
        "high - and afterward the warm after-image that lingers on the "
        "walls long after the telling is done.")),
dict(
    key="nostalgia_hiding_faking", name="Hiding or Faking Nostalgia: What Leaks Through",
    group="Compounded", ladder_rank=8, ladder_tier="compounded",
    description=(
        "People hide nostalgia more often than they fake it. The hiding "
        "happens for ordinary reasons: not wanting to cry in a meeting "
        "when a song leaks from someone's headphones, not wanting to seem "
        "sentimental in front of people who prize toughness, not wanting to "
        "explain a whole backstory for a two-second feeling. The cover is "
        "usually the neutral face: gaze pulled back to the present, mouth "
        "set, a small cough or a sip of water to manage the throat. What "
        "leaks: the shine does not obey - eyes can be brightened faster "
        "than they can be dulled. The swallow comes anyway. The stillness "
        "lingers a beat too long; the person rejoins the conversation half "
        "a second late, with the slightly too-bright 'sorry, what?' of "
        "someone returning from elsewhere. Faking nostalgia is rarer and "
        "harder: the social smile can be pasted on for the reunion photo, "
        "the 'oh, I remember!' performed for politeness - but the "
        "involuntary parts (the shine, the inner-brow lift, the "
        "throat-catch, the genuine gaze-drift) do not arrive on command, "
        "and their absence is readable. Performed nostalgia looks like "
        "acting; real nostalgia looks like absence. The practical lesson is "
        "gentle: if you suspect someone is hiding a nostalgic moment, the "
        "kind move is to give it room - a pause, a soft glance, no demand "
        "for explanation - because being caught mid-memory is tender, and "
        "tenderness deserves privacy unless it is offered."),
    how_it_works=(
        "Suppression of emotional expression works top-down: the person "
        "recruits voluntary facial control to override the involuntary "
        "display. It is partially effective - the large voluntary muscles "
        "of the mouth and the direction of gaze can be commanded - but the "
        "leakage points are the components with the least voluntary "
        "control: lacrimal brightness, the micro-movements of the inner "
        "brow, swallowing, and the timing of attentional return. Research "
        "on expressive suppression finds it reduces outward display more "
        "than inner feeling, and that it carries a small cognitive cost - "
        "the suppressor is slightly more distracted afterward, which is "
        "the 'sorry, what?' beat. Faking fails asymmetrically: voluntary "
        "muscles can be posed, but the involuntary markers of genuine "
        "affect (tear shine, authentic gaze decoupling, the specific timing "
        "of the throat-catch) require the actual affective state, so "
        "posed nostalgia reads as posed. Observers detect the mismatch "
        "holistically - the smile without the shine, the story without the "
        "drift - which is why 'performed nostalgia looks like acting' is "
        "not just a phrase but a perceptual fact."),
    key_points=[
        "Hiding is common (meetings, tough crowds, no time for the backstory); faking is rare.",
        "The cover: neutral face, gaze yanked present, cough or sip to manage the throat.",
        "What leaks: the shine, the swallow, the lingering stillness, the half-second-late return.",
        "Faked nostalgia shows the posed parts but misses the involuntary ones - and reads as acting.",
        "Suppression trims the display more than the feeling, at a small cognitive cost.",
        "The kind response to a caught moment: room, a soft glance, no demand for explanation."],
    requirements=[
        "Cover both hiding and faking with their distinct leakage points.",
        "Explain the voluntary/involuntary control difference plainly.",
        "Close with the practical gentle lesson."],
    standards=[
        "Descriptive and educational only; never diagnose or label any real person.",
        "Frame hiding as ordinary and understandable, never as deceit."],
    citations=[CIT_EKMAN, CIT_GROSS],
    sig_lens=(
        "The Signature lens respects the keeper's closed door: a banked "
        "fire still warms the room, and the wise visitor does not demand "
        "the damper be opened. What leaks - the shine, the pause - is the "
        "hearth's light under the door, and it asks only to be left in "
        "peace.")),
dict(
    key="nostalgia_expression_gallery", name="Expression Gallery Notes: Drawing and Playing Nostalgia",
    group="Compounded", ladder_rank=8, ladder_tier="compounded",
    description=(
        "For the artist: draw the eyes first. Nostalgia lives in a gaze "
        "that is not landing - pupils aimed at the middle distance, lids "
        "lowered to half-mast or just below the alert line, a highlight in "
        "each eye drawn a touch larger and wetter than neutral. Keep the "
        "brows quiet: level, or the inner ends lifted a hair - no knit, no "
        "arch of surprise. The mouth is the storytelling detail: lift one "
        "corner only, a few millimeters, and let the other corner rest or "
        "tremble downward a fraction - the two halves of bittersweet on "
        "one face. Soften everything: no hard lines at the nasolabial "
        "folds, the jaw unclenched, the whole face a few degrees less "
        "defined than a speaking face, as if seen through warm air. Add "
        "the head tilt - five to ten degrees - and, if the scene allows, "
        "a hand near the face or chest, not covering, just resting. For "
        "the actor: do not play sadness and do not play happiness - play "
        "listening. Let the eyes lose the room. Let the breath slow "
        "audibly once, at the top of the memory. Let the smile arrive late "
        "and unchosen, and let it be small. The voice, if there is one, "
        "drops half a register and slows; sentences trail rather than "
        "land. The audience will read it before they can name it - that "
        "is the test. What you are staging is not an emotion performed "
        "but attention relocated: a person briefly, visibly, somewhere "
        "else - and glad, and aching, to be there."),
    how_it_works=(
        "These notes translate the facial and postural research into craft "
        "instructions. The eye highlight and lid position encode the "
        "lacrimal shine and gaze decoupling; the quiet brows encode the "
        "absence of threat or effort appraisal; the asymmetrical mouth "
        "encodes the blended affect - positive and tender-negative "
        "affect showing simultaneously in the two mouth corners. Softening "
        "the line work encodes low muscle tension, the physiological "
        "correlate of nostalgia's calm profile. The head tilt encodes the "
        "listening orientation toward the internal replay. For the actor, "
        "'play listening' works because the observable core of nostalgia "
        "is attentional: the audience reads emotion from where attention "
        "has gone, and the slowed breath, late small smile, and trailing "
        "speech are the audible markers of that relocation. The 'read "
        "before they name it' test reflects how emotion perception works: "
        "observers process the coherent configuration holistically and "
        "feel recognition before verbal labeling catches up - which is "
        "why the notes aim at the whole pattern rather than a single "
        "'tell.'"),
    key_points=[
        "Artist: the gaze not landing, lids low, highlights drawn larger and wetter.",
        "Brows quiet - level or inner-lifted a hair; no knit, no arch.",
        "Mouth: one corner lifted millimeters, the other resting - bittersweet on one face.",
        "Soften all lines; jaw unclenched; head tilted five to ten degrees.",
        "Actor: play listening, not sadness or happiness - let the eyes lose the room.",
        "Breath slows audibly once; the smile arrives late, small, and unchosen; speech trails.",
        "The test: the audience reads it before they can name it."],
    requirements=[
        "Give separate concrete notes for the visual artist and the actor.",
        "Tie each instruction to the underlying signal it encodes.",
        "End on the recognition test."],
    standards=[
        "Descriptive and educational only; never diagnose or label any real person.",
        "Keep craft notes practical and specific."],
    citations=[CIT_EKMAN, CIT_SCHERER],
    sig_lens=(
        "The Signature lens hands the artist the keeper's portrait "
        "brief: paint the firelight, not the fire. The glow on the face "
        "tells the whole story - and the best portraits leave the memory "
        "itself unpainted, shining only in the eyes.")),
# ------------------------------------------------- 18-21: triggers
dict(
    key="nostalgia_classic_triggers", name="The Classic Triggers of Nostalgia",
    group="Compounded", ladder_rank=8, ladder_tier="compounded",
    description=(
        "Nostalgia has a well-known set of usual suspects. Music is the "
        "champion: a song from a particular era can summon the whole era - "
        "research consistently ranks music the single most common trigger, "
        "because songs get encoded alongside the emotional peak of the "
        "years they soundtracked. Smell is the runner-up: old books, rain, "
        "a specific cooking spice, sunscreen, cut grass - olfactory memory "
        "is ancient and direct, and one breath can open a decade. "
        "Photographs and home videos are the deliberate triggers, the ones "
        "people reach for on purpose. Places: the old street, the school, "
        "the house, the town - geography is memory's filing cabinet, and "
        "returning to a location replays everything filed there. Dates and "
        "anniversaries: birthdays of the absent, the day of the big game, "
        "the season when it all happened - the calendar itself becomes a "
        "cue. Objects: the ticket stub, the letter, the worn sweater, the "
        "toy on a shelf. Media: the film everyone watched that summer, the "
        "show with the theme song, the book with the cracked spine. Food: "
        "the dish that tastes like someone's kitchen. And people: running "
        "into an old friend, hearing a familiar laugh in a crowd, or simply "
        "gathering the old group in one room - other people are the richest "
        "triggers of all, because most nostalgic memories are social. "
        "Knowing the classics helps in two directions: you can arrange them "
        "on purpose (the playlist for the drive, the album for the quiet "
        "evening), and you can see them coming (the reunion will move you; "
        "plan for it)."),
    how_it_works=(
        "Triggers work through associative memory networks. An experience "
        "is not stored as a single file but as a web of linked features - "
        "sights, sounds, smells, emotions, people - and activating any node "
        "spreads activation to the rest. Music is potent because songs are "
        "replayed many times during emotionally intense periods (adolescence "
        "and early adulthood especially, the 'reminiscence bump' years), "
        "binding the song tightly to the era's network. Smell is potent "
        "because the olfactory bulb projects directly to the amygdala and "
        "hippocampus with minimal cortical filtering - the scent arrives "
        "with its feeling still attached. Places work through context "
        "reinstatement: returning to the encoding context reactivates the "
        "whole web at once, which is why the old street hits harder than "
        "the photograph of it. Dates work through temporal association: "
        "the calendar date was part of the original encoding context. "
        "People are the richest triggers because nostalgic memories are "
        "overwhelmingly social - the people were the emotional core of the "
        "encoded experience, so their presence re-activates the core "
        "directly. Deliberate triggering (playlists, albums, visits) works "
        "because the mechanism is the same whether the cue is sought or "
        "stumbled upon."),
    key_points=[
        "Music is the champion trigger; songs get bound to the emotional peaks of their era.",
        "Smell is the runner-up; olfactory memory arrives with its feeling still attached.",
        "Photographs, videos, and objects are the deliberate, reach-for-them triggers.",
        "Places reinstate the whole context at once - the old street hits harder than its photo.",
        "Dates and anniversaries turn the calendar itself into a cue.",
        "Food and media (films, shows, books) carry their eras with them.",
        "People are the richest triggers because nostalgic memory is overwhelmingly social.",
        "Knowing the classics lets you arrange them on purpose - or see them coming."],
    requirements=[
        "Catalog the major trigger families with a concrete example each.",
        "Explain the associative mechanism behind at least the top three.",
        "Close with the two-directional practical use."],
    standards=[
        "Descriptive and educational only; never diagnose or label any real person.",
        "Ground trigger claims in published findings where available."],
    citations=[CIT_WILDSCHUT_2006, CIT_BOWER, CIT_BATCHO],
    sig_lens=(
        "The Signature lens calls the classics the keeper's keys: each one "
        "cut to fit a different door of the treasury. The wise keeper "
        "knows where every key hangs - and knows better than to be "
        "surprised when a door swings open on its own.")),
dict(
    key="nostalgia_personal_triggers", name="Personal Triggers: Memories, Anniversaries, and Private Associations",
    group="Advanced", ladder_rank=9, ladder_tier="advanced",
    description=(
        "Beyond the classics, everyone carries a private set of triggers "
        "that would mean nothing to anyone else. The chipped mug from a "
        "first apartment. A phrase a friend always said, now heard in a "
        "stranger's mouth. The particular way light falls through a certain "
        "kind of blinds. A brand of soap. The sound of a screen door. These "
        "are the associations laid down without ceremony, in the background "
        "of a life being lived, and they are often stronger than the "
        "classics precisely because they are unshared - no one else can "
        "dilute them. Anniversaries form the calendar of the private set: "
        "not the public holidays but the personal ones - the day someone "
        "left, the day someone arrived, the date on the letter, the season "
        "a chapter closed. The mind keeps these dates with or without "
        "permission; people report the wave arriving before they have "
        "consciously registered what day it is. Private triggers cluster "
        "around the reminiscence bump - roughly the teens through the late "
        "twenties, when identity was forming and everything was being "
        "felt for the first time - but every decade lays down its own. "
        "The tenderness of the private set is that it is a map of what "
        "mattered: follow a person's inexplicable triggers and you are "
        "following the contour lines of their loves."),
    how_it_works=(
        "Private triggers form through incidental associative learning: "
        "when a neutral stimulus co-occurs repeatedly with an emotionally "
        "significant experience, the stimulus inherits some of the "
        "experience's affective charge. No ceremony is required - the "
        "mechanism runs in the background, which is why the chipped mug "
        "out-triggers the posed photograph: the mug was present for a "
        "thousand unguarded mornings, while the photograph was present for "
        "one arranged afternoon. Anniversary effects work through temporal "
        "context: the date is part of the memory's encoding context, and "
        "its return reinstates that context - often before conscious "
        "recognition, because temporal associations can operate implicitly. "
        "The reminiscence bump - the over-representation of late-adolescent "
        "and early-adult memories in the life story - reflects a period of "
        "dense firsts: first love, first independence, identity formation. "
        "Firsts are encoded richly because they are novel and "
        "self-defining, so they furnish a disproportionate share of later "
        "triggers. The 'map of what mattered' quality follows directly: "
        "private triggers mark the stimuli that co-occurred with the "
        "person's most emotionally significant experiences, which is why "
        "they read as a contour map of loves."),
    key_points=[
        "Everyone carries private triggers meaningless to anyone else - and often stronger than the classics.",
        "They form through incidental background association, no ceremony required.",
        "The chipped mug out-triggers the posed photo: a thousand unguarded mornings beat one arranged afternoon.",
        "Personal anniversaries form a private calendar the mind keeps with or without permission.",
        "The wave can arrive before conscious recognition of the date.",
        "Triggers cluster around the reminiscence bump years of dense firsts - but every decade contributes.",
        "Follow the inexplicable triggers and you follow the contour lines of a person's loves."],
    requirements=[
        "Give several concrete universal-feeling examples of private triggers.",
        "Explain incidental association and the anniversary effect plainly.",
        "Introduce the reminiscence bump in everyday terms."],
    standards=[
        "Descriptive and educational only; never diagnose or label any real person.",
        "Keep examples generic enough to fit many lives."],
    citations=[CIT_BOWER, CIT_BATCHO, CIT_WILDSCHUT_2006],
    sig_lens=(
        "The Signature lens treasures the private set above the classics: "
        "these are the keeper's secret drawers, the ones no visitor knows "
        "to open. The contour lines of loves, kept in chipped mugs and "
        "screen-door sounds - the truest map of the treasury ever drawn.")),
dict(
    key="nostalgia_surprise_triggers", name="Surprise Triggers: The Odd, Unexpected Things That Set Nostalgia Off",
    group="Advanced", ladder_rank=9, ladder_tier="advanced",
    description=(
        "Then there are the ambushes. A stranger's laugh, exactly like "
        "one you have not heard in twenty years, in a grocery aisle. The "
        "texture of a particular cheap carpet under your shoes in a rented "
        "room. A word misspelled the way a childhood friend always "
        "misspelled it. The smell of chlorine and cut grass arriving "
        "together through a car window. A song you did not even like at "
        "the time, now unbearable in its sweetness. The particular squeak "
        "of a shopping cart wheel. These triggers were never filed as "
        "important; they were background, set dressing, the stuff the mind "
        "was not supposed to keep. That is why they hit so hard: there is "
        "no preparation, no bracing, no decision to visit the past. The "
        "past simply walks up and taps your shoulder in the produce "
        "section. Surprise triggers are disproportionately sensory and "
        "disproportionately specific - never 'music' but that song, never "
        "'a smell' but chlorine-plus-cut-grass at dusk. They also fade "
        "fast as triggers: once the mind files the association consciously "
        "('that laugh reminds me of her'), the ambush quality dulls, "
        "though the warmth remains. People remember their ambushes for "
        "years and tell them as stories, because being time-traveled "
        "against your will is startling - and, usually, secretly welcome."),
    how_it_works=(
        "Surprise triggers exploit unattended encoding. Attention filters "
        "most background stimuli out of conscious memory, but the "
        "associative system records more than attention admits - "
        "especially stimuli that co-occurred with emotional arousal. The "
        "cheap carpet was underfoot during months that mattered; the brain "
        "bound it in without asking. Because these links were never "
        "consciously rehearsed, encountering the stimulus produces a "
        "mismatch: strong affective response with no prepared narrative, "
        "which the mind experiences as ambush. The specificity follows "
        "from the encoding: background details are stored as concrete "
        "sensory particulars, not as categories, so the trigger must match "
        "closely to fire. The dulling after conscious filing is a "
        "reconsolidation effect: once the association is brought into "
        "explicit awareness and labeled, the novelty component of the "
        "response drops - the feeling becomes expected rather than "
        "startling, though the affective core persists. The storytelling "
        "afterlife reflects the meaning-making function: the mind converts "
        "the startling visit into narrative capital, proof that the past "
        "is still alive in the present."),
    key_points=[
        "Ambushes: background details never filed as important, striking without preparation.",
        "Disproportionately sensory and specific - that song, chlorine-plus-cut-grass at dusk.",
        "The associative system records more than attention admits, especially around emotional arousal.",
        "Strong feeling with no prepared narrative is experienced as ambush.",
        "Once consciously filed, the ambush quality dulls but the warmth remains.",
        "People tell ambush stories for years - the mind converts the visit into narrative capital.",
        "Being time-traveled against your will is startling - and usually secretly welcome."],
    requirements=[
        "Give a gallery of concrete, universal-feeling ambush examples.",
        "Explain unattended encoding and the dulling-after-filing effect.",
        "Keep the tone delighted rather than clinical."],
    standards=[
        "Descriptive and educational only; never diagnose or label any real person.",
        "Keep examples generic and widely recognizable."],
    citations=[CIT_BOWER, CIT_BARRETT],
    sig_lens=(
        "The Signature lens loves the ambushes best: the treasury has "
        "hidden passages, and sometimes the past comes visiting on its "
        "own, tapping the keeper's shoulder in the produce section. The "
        "wise keeper does not bolt these doors - the uninvited visits are "
        "often the truest.")),
dict(
    key="nostalgia_chain_reactions", name="Chain Reactions: How One Trigger Cascades into Related Emotions",
    group="Advanced", ladder_rank=9, ladder_tier="advanced",
    description=(
        "Nostalgia rarely travels alone for long. One trigger opens the "
        "first door, and the rooms beyond open in sequence. The classic "
        "cascade: a song summons the summer, the summer summons the "
        "friends, the friends summon the one who is gone - and nostalgia "
        "shades into grief, tender and specific. Or the other direction: "
        "the photo album starts as nostalgia, the good years parade past, "
        "and by the last page the feeling has become gratitude - for "
        "having had it at all. Common chains: nostalgia into joy (the "
        "memory was happy and the remembering stays happy); into sadness "
        "(the distance swells and the ache takes the lead); into grief "
        "(the memory centers someone absent); into gratitude (the having "
        "outshines the losing); into longing (the wish to return grows "
        "teeth); into regret (the mind wanders to what was mishandled); "
        "into pride (the hard years reframe as survived years); into "
        "tenderness toward the present (the past's love spills forward "
        "onto the people here now). The cascade is not a malfunction - it "
        "is the associative network doing what networks do, each memory "
        "cueing its neighbors. The skill is not preventing the chain but "
        "riding it: noticing which room you have wandered into, and "
        "deciding whether to stay awhile or walk back toward the hearth."),
    how_it_works=(
        "Cascades follow spreading activation through the autobiographical "
        "memory network. Each retrieved memory activates its associates - "
        "the people, places, and feelings linked to it - and each of those "
        "activates its own associates, so a single cue can propagate "
        "across years in seconds. The emotional shading shifts as the "
        "content shifts: when activation reaches a lost person, the "
        "appraisal of absence strengthens and the blend tips toward grief; "
        "when it reaches evidence of having been loved, the appraisal of "
        "receipt strengthens and the blend tips toward gratitude. "
        "Appraisal theories explain the transitions: the feeling at each "
        "step is the mind's read of the currently active content, so as "
        "content changes, feeling changes with it. The cascade's speed "
        "reflects the density of the network - richly interconnected eras "
        "(the bump years) cascade fastest and farthest. 'Riding the chain' "
        "is metacognitive monitoring: the prefrontal systems tracking which "
        "content is active and applying regulation strategies (savoring, "
        "reframing, or shifting attention) rather than being passively "
        "carried. This is a learnable skill, and it is the core of the "
        "'visit, don't move in' principle."),
    key_points=[
        "One trigger opens the first door; the rooms beyond open in sequence through association.",
        "Common chains: into joy, sadness, grief, gratitude, longing, regret, pride, present-tense tenderness.",
        "The shading shifts as the active content shifts - feeling follows the mind's current read.",
        "Richly interconnected eras (the bump years) cascade fastest and farthest.",
        "The cascade is the network working normally, not a malfunction.",
        "The skill is riding it: noticing which room you are in and choosing whether to stay or return."],
    requirements=[
        "Name the common downstream emotions with a concrete chain example each.",
        "Explain spreading activation in plain language.",
        "Teach the riding-the-chain skill."],
    standards=[
        "Descriptive and educational only; never diagnose or label any real person.",
        "Present cascades as normal network behavior."],
    citations=[CIT_BOWER, CIT_LAZARUS, CIT_GROSS],
    sig_lens=(
        "The Signature lens walks the treasury's enfilade: door after "
        "door, each room opening onto the next, grief's chapel beside "
        "gratitude's gallery. The keeper does not fear the far rooms - "
        "they are all part of the house - but learns the hallways well "
        "enough to find the way back to the fire.")),
# ------------------------------------------------- 22-25: behavior
dict(
    key="nostalgia_behavior_actions", name="What People Do When They Feel Nostalgic",
    group="Advanced", ladder_rank=9, ladder_tier="advanced",
    description=(
        "Nostalgia moves people toward the past, and the actions show it. "
        "The signature behaviors: reaching - for the phone to call the old "
        "friend, for the photo album on the high shelf, for the playlist "
        "that holds the era. Revisiting - driving the old route, walking "
        "the old street, standing outside the old house a little longer "
        "than necessary. Keeping and curating - the ticket stubs, the "
        "letters, the boxes labeled in marker; nostalgia is the great "
        "patron of the shoebox archive. Recreating - cooking the dish, "
        "playing the game, organizing the reunion, teaching the next "
        "generation the song. Sharing - telling the story at dinner, "
        "sending the photo with 'remember this?', gathering the witnesses "
        "who were there. Collecting - the vinyl, the first editions, the "
        "memorabilia; the collector's shelf is often a nostalgia museum "
        "with the labels removed. And the quiet ones: pausing mid-task to "
        "stare out a window, saving rather than deleting, choosing the "
        "familiar over the novel. Underneath all of it is approach, not "
        "avoidance: unlike emotions that push people away from their "
        "objects, nostalgia pulls people toward - toward people, places, "
        "and artifacts of the valued past. The actions are the feeling "
        "made visible: a life reaching back to touch what shaped it."),
    how_it_works=(
        "The action tendencies follow directly from the appraisal. "
        "Nostalgia appraises the past as valuable and the present self as "
        "continuous with it, so the motivational direction is approach: "
        "restore contact with the valued content. Reaching behaviors "
        "(calls, albums, playlists) are contact-seeking with the social "
        "core of the memories. Revisiting is context reinstatement as "
        "action: the body returns to the encoding environment to maximize "
        "the replay. Keeping and curating serve the treasury function: "
        "artifacts are external memory cues, and preserving them preserves "
        "future access to the feeling. Recreating extends the past into the "
        "present - cooking the dish or teaching the song converts memory "
        "into living practice. Sharing converts private meaning into "
        "social bonding: joint reminiscence synchronizes the memory "
        "network across people and deepens the relationships that the "
        "nostalgia is about. The quiet behaviors (pausing, saving, "
        "choosing the familiar) are low-cost maintenance of continuity. "
        "All of these are approach behaviors, which is why nostalgia, "
        "unlike avoidance emotions, tends to increase social contact and "
        "engagement rather than withdrawal."),
    key_points=[
        "Signature actions: reaching (calls, albums, playlists), revisiting (old routes, old streets).",
        "Keeping and curating: the shoebox archive - artifacts as external memory cues.",
        "Recreating: cooking the dish, teaching the song - memory converted to living practice.",
        "Sharing: telling the story, sending the photo, gathering the witnesses.",
        "Collecting: the shelf as a nostalgia museum with the labels removed.",
        "Quiet ones: pausing, saving not deleting, choosing the familiar.",
        "The direction is approach, not avoidance - toward people, places, and artifacts of the valued past."],
    requirements=[
        "Catalog the major action families with concrete examples.",
        "Explain the approach direction and its social consequences.",
        "Show how each action serves the feeling's function."],
    standards=[
        "Descriptive and educational only; never diagnose or label any real person.",
        "Keep behaviors ordinary and recognizable."],
    citations=[CIT_WILDSCHUT_2006, CIT_SEDIKIDES_2008, CIT_BATCHO],
    sig_lens=(
        "The Signature lens reads the actions as the keeper's rounds: "
        "dusting the shelves, oiling the hinges, inviting old friends to "
        "see the collection, teaching the young ones the songs. The "
        "treasury is not a vault - it is a working library, and every "
        "action is a borrowing.")),
dict(
    key="nostalgia_speech_patterns", name="What People Say: Characteristic Phrases, Tone, and Speech Patterns",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "Nostalgic speech has a sound you can recognize blindfolded. The "
        "openers: 'Remember when...', 'Do you remember...?', 'That reminds "
        "me of...', 'Back in...', 'We used to...'. The intensifiers: "
        "'Oh, those were the days,' 'They don't make them like that "
        "anymore,' 'I would give anything to...', 'If I could go back for "
        "one day...'. The tender specifics: people do not say 'we had fun'; "
        "they say 'the way the light came through those windows at four in "
        "the afternoon' - nostalgia speaks in sensory close-ups. The tone "
        "drops and slows: speech gets quieter, warmer, less clipped, with "
        "pauses where the memory is being watched. Laughter changes "
        "quality - it comes softer, often through the nose, frequently "
        "with the shine in the eyes. Questions turn rhetorical: 'Wasn't she "
        "something?' expects no answer. Stories get longer and more "
        "detailed than their news value warrants, because the telling is "
        "the point. And there is the second-person pull: 'You remember, "
        "don't you?' - the speaker recruiting a witness, because a shared "
        "memory told alone is only half told. Listen for the tense "
        "slippage: people narrating the past in present tense ('so we're "
        "driving, and he says...') - the surest verbal sign the replay has "
        "taken over."),
    how_it_works=(
        "The speech patterns are the verbal overflow of the replay. "
        "'Remember when' openers function as joint-attention bids: the "
        "speaker is inviting the listener into the memory space, and "
        "research on shared reminiscence shows these bids are usually "
        "accepted - people enjoy co-remembering. Sensory close-ups reflect "
        "how the memories are stored: as rich perceptual detail, which "
        "surfaces in language as concrete imagery rather than summary. "
        "The slowed, warmed tone is the physiological profile made "
        "audible: the calm, tender body produces slower, softer speech, "
        "and listeners reliably hear the affect. Present-tense slippage "
        "marks maximal absorption - the narrator's deictic center has "
        "moved into the memory, so the grammar follows. The second-person "
        "pull ('you remember, don't you?') serves the social function: "
        "nostalgic memories are validated and amplified by witnesses, and "
        "soliciting confirmation converts private recall into shared "
        "reality. Story length beyond news value is savoring behavior: "
        "prolonging the telling prolongs the feeling, the verbal "
        "equivalent of turning the photograph slowly in the light."),
    key_points=[
        "Openers: 'Remember when...', 'We used to...', 'That reminds me of...' - joint-attention bids.",
        "Intensifiers: 'Those were the days,' 'They don't make them like that anymore.'",
        "Sensory close-ups over summaries: the light through the windows at four.",
        "Tone drops and slows; laughter softens; pauses where the memory is being watched.",
        "Present-tense slippage ('so we're driving...') - the surest sign the replay has taken over.",
        "The second-person pull ('You remember, don't you?') recruits a witness.",
        "Stories run long because the telling is the point - verbal savoring."],
    requirements=[
        "Quote the characteristic phrases verbatim.",
        "Describe tone, pace, laughter, and tense with concrete detail.",
        "Explain the social function of the second-person pull."],
    standards=[
        "Descriptive and educational only; never diagnose or label any real person.",
        "Keep quoted phrases generic and universal."],
    citations=[CIT_WILDSCHUT_2006, CIT_SCHERER],
    sig_lens=(
        "The Signature lens hears the keeper giving tours: 'Remember "
        "when' is the gallery door swinging open, the sensory close-ups "
        "are the spotlight on each treasure, and 'you remember, don't "
        "you?' is the invitation to every visitor - come stand closer, "
        "this one is worth seeing.")),
dict(
    key="nostalgia_decisions_judgment", name="How Nostalgia Changes Decisions and Judgment",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "Nostalgia quietly edits the decision-making machinery. It "
        "inflates the value of the familiar: the old brand, the old "
        "neighborhood, the old way of doing things all look better under "
        "its light - which is why marketers bottle it and politicians "
        "invoke it. It raises risk tolerance for continuity and lowers it "
        "for novelty: the nostalgic chooser prefers the known good over "
        "the unknown maybe-better. It softens judgments of the past's "
        "people: old grievances get reweighted, former adversaries get "
        "their rough edges sanded in retrospect - reunions are full of "
        "forgiven debts nobody mentions. It increases generosity: "
        "studies find nostalgic reflection makes people more prosocial, "
        "more willing to give and to connect, because the feeling "
        "spotlights social bonds as the currency that matters. It can "
        "distort: the rosy retrospective can make the past look like a "
        "better guide than it was - 'we've always done it this way' is "
        "nostalgia doing strategy, and not always well. And it steadies "
        "big life choices: people facing transitions (moves, career "
        "changes, endings) often report that a nostalgic spell clarified "
        "what they actually value, because the feeling is, at bottom, a "
        "highlight reel of what mattered. The wise use is to let nostalgia "
        "inform values while letting present evidence judge options."),
    how_it_works=(
        "The effects run through affect-as-information: feelings serve as "
        "quick summaries that the judgment system consults. Nostalgia's "
        "warm positive affect tags familiar options with a glow, producing "
        "the mere-exposure-like preference for the known - the affect is "
        "real, but it reports on the past's value, not the option's "
        "present merit, which is the distortion to watch. The generosity "
        "effect follows from content: nostalgic memories are "
        "overwhelmingly social, so the feeling foregrounds relationships, "
        "and foregrounded relationships shift choices toward prosocial "
        "ones - the mechanism behind the experimental findings. The "
        "grievance-softening is rosy retrospection applied to people: "
        "negative details fade faster than positive ones in autobiographical "
        "memory (the fading-affect bias), so the past's people literally "
        "improve in storage. The values-clarification effect is the "
        "meaning function at work: nostalgia surfaces what the person has "
        "most deeply valued, which is genuinely useful data for life "
        "choices - provided the person separates 'this is what I value' "
        "(valid) from 'therefore the old way was objectively better' "
        "(not necessarily valid). That separation is the whole skill."),
    key_points=[
        "Inflates the value of the familiar: old brands, old ways glow brighter than their merits.",
        "Raises risk tolerance for continuity, lowers it for novelty.",
        "Softens judgments of the past's people - old grievances get sanded in retrospect.",
        "Increases generosity and prosocial choice; relationships become the visible currency.",
        "Can distort: 'we've always done it this way' is nostalgia doing strategy.",
        "Steadies big life choices by surfacing what the person has most deeply valued.",
        "The skill: let nostalgia inform values; let present evidence judge options."],
    requirements=[
        "Cover familiarity bias, risk, social judgment, generosity, and values-clarification.",
        "Name the distortion honestly alongside the benefits.",
        "Teach the separation skill."],
    standards=[
        "Descriptive and educational only; never diagnose or label any real person.",
        "Present effects as tendencies, not determinism."],
    citations=[CIT_SEDIKIDES_2008, CIT_ROUTLEDGE_2016, CIT_LAZARUS],
    sig_lens=(
        "The Signature lens treats nostalgia as the keeper's counsel, not "
        "the keeper's commander: the treasury advises on what is precious, "
        "but the road ahead is walked with present-tense eyes. Counsel the "
        "values, command nothing - that is the keeper's discipline.")),
dict(
    key="nostalgia_escalation", name="Behavior Under Intensity: How Actions Escalate as the Feeling Grows",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "Watch what people do as nostalgia's volume rises, and the "
        "escalation has a readable shape. At mild levels, behavior barely "
        "shifts: a paused step, a longer look at the photograph, a song "
        "replayed once. The person stays in the day; the past is a "
        "postcard glanced at in passing. At moderate levels, the actions "
        "become deliberate: the album comes off the shelf, the call gets "
        "made, the drive takes the old route on purpose, the evening "
        "rearranges itself around the visit. Time and attention are now "
        "budgeted to the past - twenty minutes, an hour, the whole "
        "evening. At high intensity, behavior can take over the day: the "
        "person cancels plans, drives hours to the old town unplanned, "
        "spends the night in the archive boxes, writes the long letter, "
        "books the flight home. The present is not just backgrounded; it "
        "is postponed. This is still normal around the great triggers - "
        "anniversaries, homecomings, reunions, losses - and it resolves as "
        "the wave resolves. The line into unhealthy territory is not the "
        "intensity but the pattern: when the escalation stops resolving - "
        "when every evening rearranges itself, when the present is "
        "postponed indefinitely, when the visits stop being visits - the "
        "emotion is no longer serving the life; the life is serving the "
        "emotion. Intensity asks for respect and a return ticket; the "
        "return ticket is what keeps it healthy."),
    how_it_works=(
        "Escalation tracks attentional capture and motivational strength. "
        "Mild nostalgia produces orienting responses - brief, automatic, "
        "low-cost (the paused step). Moderate levels engage deliberate "
        "savoring: the person allocates time and effort because the "
        "reward value of the replay justifies the cost - this is normal "
        "reward-seeking, the same machinery that budgets an evening for a "
        "good film. High intensity reflects strong cue-stacking plus high "
        "present vulnerability: the reward value spikes while present-tense "
        "competing rewards look thin, so the behavior budget tips heavily "
        "toward the past. Around great triggers this is proportionate and "
        "self-limiting: the trigger passes, the budget rebalances. The "
        "unhealthy pattern is a regulation failure, not a feeling failure: "
        "the return mechanism - present-tense engagement reasserting itself "
        "- stops firing, often because the present has too little reward "
        "to compete (loneliness, depression, emptiness) or because the "
        "replay has become compulsive. The diagnostic distinction, kept "
        "strictly educational here, is temporal: healthy escalation "
        "resolves; unhealthy escalation repeats without resolution. The "
        "'return ticket' framing captures the regulation skill: entering "
        "the visit with the present kept warm - a plan, a person, a "
        "morning commitment - so the way back stays lit."),
    key_points=[
        "Mild: orienting responses - a paused step, a replayed song; the day continues.",
        "Moderate: deliberate savoring - the album, the call, the old route; time budgeted to the past.",
        "High: the day rearranges - unplanned drives, nights in the archive boxes, the flight home.",
        "Around great triggers this is normal and self-limiting; the wave resolves.",
        "The line is the pattern, not the intensity: healthy escalation resolves, unhealthy repeats.",
        "The regulation skill is the return ticket: enter the visit with the present kept warm."],
    requirements=[
        "Walk the escalation through mild, moderate, and high with concrete behaviors.",
        "Draw the healthy/unhealthy line on pattern, not intensity.",
        "Teach the return-ticket skill."],
    standards=[
        "Descriptive and educational only; never diagnose or label any real person.",
        "Keep the unhealthy description behavioral and non-clinical."],
    citations=[CIT_GROSS, CIT_ROUTLEDGE_2016, CIT_SEDIKIDES_2008],
    sig_lens=(
        "The Signature lens measures the visit by the door left open: "
        "the keeper may wander the far galleries for hours, even days "
        "around the great anniversaries - but the lamp is left burning in "
        "the front hall, and the keeper always knows the way home.")),
# ------------------------------------------------- 26-31: expression + recognition
dict(
    key="nostalgia_healthy_expression", name="Healthy Expression: Saying It, Showing It, Channeling It Well",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "Healthy nostalgia is a visit, not a residence - and it shows in "
        "how it is expressed. Saying it: telling the story, naming the "
        "feeling out loud ('this song takes me back'), letting the shine "
        "show without apology. Shared nostalgia multiplies: the story told "
        "at the table, the photo sent with the caption, the playlist made "
        "for the old friend - expression converts private warmth into "
        "social bond. Showing it: keeping the artifacts with intention "
        "rather than clutter - the framed photo, the recipe box in use, "
        "the shelf of treasures that gets dusted. Tears when they come "
        "are let come; they are the overflow of being moved, not a "
        "problem to solve. Channeling it: this is where nostalgia becomes "
        "fuel. The visit clarifies values - so the healthy expression "
        "carries something back: the call that reconnects, the tradition "
        "restarted, the letter written, the lesson from the hard years "
        "applied to the present challenge, the gratitude converted into "
        "generosity. Creative channeling counts too: the memoir page, the "
        "song learned, the garden planted like the old one. The test of "
        "healthy expression is the return: after the saying, showing, and "
        "channeling, the person is more present, not less - steadier, "
        "kinder, clearer about what matters. The past has been visited, "
        "honored, and put to work."),
    how_it_works=(
        "Healthy expression works through three mechanisms. Disclosure "
        "(saying it) externalizes the feeling, which reduces its "
        "pressure: named and shared affect is easier to hold than "
        "suppressed affect, and sharing recruits social support - the "
        "listener's warmth becomes part of the experience. Intentional "
        "keeping (showing it) turns cues into tools: the framed photo or "
        "recipe box becomes a controllable trigger, available on purpose "
        "rather than only by ambush, which increases the person's sense "
        "of agency over the emotion. Channeling converts the meaning "
        "payoff into action: nostalgia surfaces values (connection, "
        "craft, perseverance), and acting on a surfaced value completes "
        "the arc - the feeling was information about what matters, and "
        "the action honors the information. The 'more present, not less' "
        "test reflects the function: nostalgia's job is resourcing the "
        "present self, so expression that ends in greater presence is "
        "expression aligned with the function. Creative channeling adds "
        "generativity: the past is not just revisited but continued - the "
        "garden planted like the old one extends the lineage forward, "
        "which is the deepest form of honoring."),
    key_points=[
        "Saying it: tell the story, name the feeling, let the shine show - shared nostalgia multiplies.",
        "Showing it: keep artifacts with intention - framed, in use, dusted - not as clutter.",
        "Tears are overflow of being moved, not a problem to solve; let them come.",
        "Channeling it: carry something back - the call, the restarted tradition, the applied lesson.",
        "Creative channeling: the memoir page, the learned song, the garden planted like the old one.",
        "The test: after expression, the person is more present, not less - steadier, kinder, clearer.",
        "The past visited, honored, and put to work."],
    requirements=[
        "Organize around saying, showing, and channeling with concrete examples.",
        "Explain the mechanism behind each mode.",
        "Give the 'more present' test as the closing criterion."],
    standards=[
        "Descriptive and educational only; general safe guidance, never therapy.",
        "Keep all guidance ordinary and everyday."],
    citations=[CIT_GROSS, CIT_SEDIKIDES_2008, CIT_WILDSCHUT_2006],
    sig_lens=(
        "The Signature lens calls this the keeper's commerce: the "
        "treasury is not for hoarding - its wealth is meant to circulate. "
        "Tell the stories, lend the treasures, plant the gardens. A "
        "treasury that only accumulates is a vault; one that circulates "
        "is a hearth.")),
dict(
    key="nostalgia_unhealthy_expression", name="Unhealthy Expression: Getting Stuck in the Past or Denying It",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "Nostalgia turns unhealthy in two opposite directions. The first "
        "is getting stuck: the visits stop being visits. The signs are "
        "behavioral and readable - every evening in the archive boxes, the "
        "present's invitations declined as a habit, new people and new "
        "places held at arm's length because they are not the old ones, "
        "the past invoked not as treasure but as evidence that nothing "
        "now can measure up. The feeling that was a resource becomes a "
        "refuge, and then a residence. The cost is the present: "
        "relationships thin, opportunities pass unseized, and the life "
        "narrows to the size of the replay. The second direction is "
        "denial: the person treats nostalgia as weakness and suppresses "
        "it - no old songs, no visits, no looking back, the past kept "
        "under lock. The cost here is subtler: the treasury stays closed, "
        "and with it the meaning, continuity, and steadiness it holds. "
        "Suppressed nostalgia tends to leak anyway - in irritability, in "
        "the ambush that finally breaks through, in a flatness the person "
        "cannot name. Both directions share a root error: treating the "
        "past as either the only home or no home at all. The middle way - "
        "the visit with a return ticket - keeps the treasury open and the "
        "front door open too. Anyone finding themselves stuck or locked "
        "down for a long time, with daily life suffering, is dealing with "
        "something bigger than an emotion-education page can address, and "
        "talking with a trusted person or a professional is the sensible "
        "next step."),
    how_it_works=(
        "Getting stuck is a regulation pattern, not a feeling intensity: "
        "the replay loop runs without the resolution phase, usually "
        "because present-tense rewards have thinned (loneliness, loss, "
        "disappointment) so the past wins every comparison by default. "
        "Each unopposed visit strengthens the associative pathways "
        "(rehearsal strengthens memory), making the past progressively "
        "more vivid and the present progressively thinner - a feedback "
        "loop. The 'nothing measures up' judgment is partly an artifact "
        "of the loop: rosy retrospection brightens the stored past while "
        "the unvisited present gets no such editing. Denial works through "
        "expressive suppression and avoidance: the person blocks cues and "
        "strangles expression, which research shows trims the display "
        "more than the feeling - the affect persists and, unprocessed, "
        "surfaces as irritability or flatness. Both patterns abandon the "
        "visit structure: stuckness never returns, denial never visits. "
        "The middle way preserves both phases - entry and return - which "
        "is why the 'return ticket' skill from the escalation record is "
        "the practical core. The closing guidance note follows the "
        "educational boundary: this database describes emotions; "
        "persistent life-impairing patterns belong with real human help."),
    key_points=[
        "Two unhealthy directions: getting stuck (visits become residence) and denial (the treasury locked).",
        "Stuck signs: every evening in the archive, present invitations declined, the past as evidence nothing measures up.",
        "The cost of stuckness is the present: thinning relationships, unseized opportunities, a narrowing life.",
        "Denial's cost is subtler: the meaning and steadiness stay locked up; the feeling leaks as irritability or flatness.",
        "Stuckness is a feedback loop: rehearsal brightens the past while the unvisited present gets no editing.",
        "Both share the root error: the past as the only home, or no home at all.",
        "The middle way: the visit with a return ticket; persistent impairment deserves real human help."],
    requirements=[
        "Describe both directions with readable behavioral signs.",
        "Name the cost of each honestly.",
        "Explain the feedback loop and end with the boundary-respecting guidance note."],
    standards=[
        "Descriptive and educational only; general safe guidance, never therapy or diagnosis.",
        "Keep unhealthy patterns behavioral and non-clinical; include the help-seeking note."],
    citations=[CIT_GROSS, CIT_ROUTLEDGE_2016, CIT_BOWER],
    sig_lens=(
        "The Signature lens warns the keeper two ways: do not move into "
        "the treasury and abandon the house, and do not brick up the "
        "treasury and live in an empty house. The hearth is for visiting "
        "daily and living presently - that is the whole discipline.")),
dict(
    key="nostalgia_everyday_practices", name="Everyday Practices: Small Habits That Keep Nostalgia in Balance",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "Balance is maintained by small habits, not grand resolutions. "
        "Keep a deliberate trigger shelf: one playlist, one album, one "
        "box - curated on purpose, so the visits happen by invitation as "
        "well as by ambush. Tell one story a week: at dinner, on a call, "
        "to someone who was there or someone who was not - the telling "
        "keeps the memories alive and the bonds warm. Write things down: "
        "the sensory details fade fastest, and a few lines in a notebook "
        "preserve the light through the windows at four better than any "
        "photograph. Practice the return ticket: before a planned visit "
        "to the past (the album evening, the hometown drive), set the "
        "next morning's plan - the walk, the work, the person - so the "
        "way back is lit. Convert one visit a month into action: the call, "
        "the recipe cooked, the tradition restarted, the thank-you sent to "
        "someone the memory features. Share the treasury: teach the young "
        "ones the song, show them the places, tell them who the people "
        "were - nostalgia kept only for oneself is a closed room. And "
        "keep the front door open: say yes to the new invitation, the new "
        "street, the unfamiliar song - the present needs its own deposits "
        "if it is ever to become someone's good old days. None of these "
        "take more than minutes; together they keep the hearth tended and "
        "the house lived in."),
    how_it_works=(
        "Each practice targets a mechanism. The curated trigger shelf "
        "converts ambush cues into controllable ones, increasing agency: "
        "the person chooses when to visit, which prevents both avoidance "
        "and compulsive replay. Weekly telling exploits the social "
        "amplification of shared reminiscence - memories rehearsed "
        "socially are retained better and carry more warmth. Writing "
        "preserves the sensory detail that decay takes first: encoding "
        "specificity means the written close-up will re-cue the scene "
        "years later when the bare fact would not. The return ticket is "
        "implementation intention applied to emotion regulation: a "
        "pre-committed present-tense plan makes the attentional return "
        "automatic rather than effortful. Monthly conversion (visit into "
        "action) completes the meaning-action arc, so the feeling's "
        "information gets used instead of merely felt. Teaching the young "
        "ones adds generativity, the forward extension of the lineage. "
        "Saying yes to the new ensures the present accumulates its own "
        "associative wealth - today's unfamiliar song is tomorrow's "
        "trigger, but only if it gets lived. Small and repeated beats big "
        "and occasional because regulation is a habit system, not an "
        "event."),
    key_points=[
        "Curate a deliberate trigger shelf: playlist, album, box - visits by invitation, not only ambush.",
        "Tell one story a week; shared telling keeps memories alive and bonds warm.",
        "Write down sensory details; the close-ups fade first and writing preserves them.",
        "Practice the return ticket: set tomorrow's plan before tonight's visit to the past.",
        "Convert one visit a month into action: the call, the recipe, the restarted tradition.",
        "Share the treasury: teach the songs, show the places, name the people.",
        "Keep the front door open: the present needs deposits too - today's song is tomorrow's trigger."],
    requirements=[
        "Give seven or so concrete practices, each doable in minutes.",
        "Explain the mechanism each practice serves.",
        "Close on the present's need for its own deposits."],
    standards=[
        "Descriptive and educational only; general safe everyday guidance, never therapy.",
        "Keep every practice small, ordinary, and cost-free."],
    citations=[CIT_GROSS, CIT_SEDIKIDES_2008, CIT_BOWER],
    sig_lens=(
        "The Signature lens gives the keeper a daily round: dust one "
        "shelf, tell one story, write one line, light tomorrow's lamp, "
        "carry one treasure into action, teach one song, open one new "
        "door. Minutes a day - and the hearth never goes out, nor the "
        "house un-lived-in.")),
dict(
    key="nostalgia_reading_others", name="Reading the Signs: Nostalgia in Other People",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "Reading nostalgia in others is reading a quiet emotion, so the "
        "signs are quiet too. On the face: the drifting gaze, the shine, "
        "the small unchosen smile, the head tilt - the signature from the "
        "facial records, now seen from across the table. In the body: the "
        "settled stillness, the slowed pace, the hand resting on the "
        "photograph a beat too long, the deep breath taken for no obvious "
        "reason. In the voice: the drop in register, the slowing, the "
        "'remember when' openers, the present-tense slippage, the story "
        "running longer than its news value. In behavior: the reaching for "
        "the album, the old route chosen, the text sent out of the blue "
        "with a photo attached, the lingering at the doorway of the old "
        "place. Context is the great clarifier: the same soft smile at a "
        "reunion, an anniversary, a hometown visit, or when the old song "
        "starts is nostalgia with high probability; the same smile at a "
        "promotion party is probably something else. The most common "
        "misread is mistaking it for sadness: the shine and the quiet can "
        "look like distress, but nostalgic quiet has a warmth in it - the "
        "small smile, the tenderness in the voice - that distressed quiet "
        "lacks. When in doubt, do not label; notice, give room, and let "
        "them name it if they want to."),
    how_it_works=(
        "Reading others runs on cue integration: no single sign is "
        "diagnostic, but the configuration - face plus body plus voice "
        "plus context - is highly informative. This matches how emotion "
        "perception actually works: observers process coherent "
        "multi-channel patterns holistically rather than decoding single "
        "'tells.' Context does the heaviest lifting through base rates: "
        "reunions, anniversaries, homecomings, and old songs playing make "
        "nostalgia the prior probability, so the quiet signs are read "
        "correctly; without such context the same signs are ambiguous. "
        "The sadness misread happens because the two share channels "
        "(shine, quiet, stillness); the discriminator is the positive "
        "affect leakage - the small smile, the warm tone - which "
        "distress does not produce. The 'do not label' guidance reflects "
        "both accuracy and ethics: labeling someone else's inner state "
        "from the outside is error-prone, and being labeled can feel "
        "intrusive - especially for a tender emotion. Noticing plus room "
        "is the accurate and kind alternative: it keeps perception open "
        "while respecting the other person's authority over their own "
        "feeling."),
    key_points=[
        "Face: drifting gaze, shine, small unchosen smile, head tilt - seen from across the table.",
        "Body: settled stillness, slowed pace, the hand lingering, the uncaused deep breath.",
        "Voice: dropped register, slowing, 'remember when' openers, present-tense slippage.",
        "Behavior: reaching for the album, the old route, the out-of-the-blue photo text.",
        "Context clarifies: reunion, anniversary, homecoming, old song = nostalgia highly probable.",
        "The common misread is sadness; the discriminator is the warmth - the small smile, the tender tone.",
        "Do not label from the outside; notice, give room, let them name it."],
    requirements=[
        "Cover face, body, voice, and behavior cues plus the role of context.",
        "Teach the sadness-vs-nostalgia discriminator.",
        "End on the do-not-label guidance."],
    standards=[
        "Descriptive and educational only; never diagnose or label any real person.",
        "Emphasize the other person's authority over their own feeling."],
    citations=[CIT_EKMAN, CIT_SCHERER, CIT_WILDSCHUT_2006],
    sig_lens=(
        "The Signature lens teaches the visitor's manners: you will know "
        "the keeper is at the hearth by the firelight on their face - "
        "but you do not announce what room someone is in. You notice, you "
        "wait, and if they open the door, you step in gently.")),
dict(
    key="nostalgia_supportive_responses", name="Supportive Responses: What to Say and Do When Someone Feels Nostalgic",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "When someone near you goes nostalgic, the supportive moves are "
        "simple. First, do not rush them: the pause, the drift, the story "
        "running long - these are the feeling doing its work, and "
        "hurrying it is like closing a book someone is still reading. "
        "Second, receive the story: listen all the way through, ask the "
        "follow-up question ('what happened next?', 'what did she say?'), "
        "laugh and shine with them. Shared reminiscence is one of the "
        "fastest bonding agents known - receiving it well is a gift that "
        "costs only attention. Third, witness without fixing: if tears "
        "come, they are moved-tears, not a problem; a hand on the arm, a "
        "nod, and room are better than 'are you okay?' (they are more "
        "than okay - they are somewhere precious). Fourth, add your own "
        "thread if you were there: 'I remember that day - you...'; "
        "co-remembering validates the memory and deepens the bond. If you "
        "were not there, ask to be shown: 'tell me about him' turns the "
        "private treasury into shared wealth. Fifth, help the return: when "
        "the story ends and the quiet settles, a gentle bridge back - the "
        "meal, the walk, the plan - keeps the visit a visit. What you are "
        "doing, underneath all of it, is honoring: treating their past as "
        "real and precious, which is what the feeling itself is doing. "
        "People remember for years who received their nostalgia well."),
    how_it_works=(
        "Each move serves a mechanism. Not rushing protects the replay: "
        "interruption collapses attentional absorption and aborts the "
        "meaning-making before the payoff, leaving the feeling unresolved. "
        "Receiving the story with follow-up questions extends savoring and "
        "converts private recall into social reality - memories validated "
        "by a witness are retained more strongly and carry more warmth. "
        "Witnessing without fixing avoids the common error of treating "
        "moved-tears as distress: misapplied comforting ('don't cry') "
        "signals that the feeling is a problem, which can shame a tender "
        "emotion. Co-remembering synchronizes the memory network across "
        "people: shared details get reinforced in both parties, which is "
        "the bonding mechanism behind the research findings on joint "
        "reminiscence. Inviting the telling ('tell me about him') extends "
        "the treasury's social function to non-witnesses, building new "
        "closeness from old material. The gentle bridge back supports the "
        "regulation both parties benefit from: the visit completes, the "
        "aftershock's steadiness transfers into the shared present, and "
        "the interaction ends warm rather than stranded."),
    key_points=[
        "Do not rush them: the pause and the long story are the feeling doing its work.",
        "Receive the story fully; ask the follow-up question; laugh and shine with them.",
        "Witness without fixing: moved-tears are not a problem - room and a nod beat 'are you okay?'",
        "Add your thread if you were there; if not, ask to be shown: 'tell me about him.'",
        "Help the return with a gentle bridge back to the present - the meal, the walk, the plan.",
        "Underneath it all: honor their past as real and precious, as the feeling itself does.",
        "People remember for years who received their nostalgia well."],
    requirements=[
        "Give five concrete supportive moves with the phrasing to use.",
        "Explain why 'are you okay?' can misfire.",
        "Close on the honoring principle."],
    standards=[
        "Descriptive and educational only; general safe guidance, never therapy.",
        "Keep all moves ordinary, cost-free, and non-intrusive."],
    citations=[CIT_WILDSCHUT_2006, CIT_SEDIKIDES_2008],
    sig_lens=(
        "The Signature lens calls this being a good guest at the hearth: "
        "do not hurry the tour, admire the treasures sincerely, share "
        "your own stories when you have them, and when the evening ends, "
        "walk the keeper gently back to the front door. Good guests are "
        "remembered as long as the treasures.")),
dict(
    key="nostalgia_mistakes_to_avoid", name="What Not to Do: Common Mistakes That Make Nostalgia Worse",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "The mistakes people make around nostalgia are well-meaning and "
        "common. Mistake one: mocking it - 'living in the past,' 'okay, "
        "grandpa,' the eye-roll at the story. Mockery shames a tender "
        "emotion and teaches the person to hide the visits, which helps "
        "nobody. Mistake two: correcting the memory - 'that's not how it "
        "happened' fact-checks a feeling. Nostalgic memory is selective "
        "by design; the warmth is the point, and litigating details "
        "collapses the visit into an argument. Mistake three: rushing or "
        "interrupting - checking the phone mid-story, changing the "
        "subject, 'anyway...' - which strands the feeling mid-arc. "
        "Mistake four: pathologizing - treating the tears or the long "
        "evening with the album as a symptom of something wrong. It is "
        "usually not; treating it as illness can make a healthy visit "
        "feel shameful. Mistake five: feeding the stuckness - if someone "
        "is sliding from visits into residence, the unhelpful moves are "
        "joining the permanent retrospective ('the world really has gone "
        "downhill') or, opposite, staging an intervention-style "
        "confrontation. The helpful move is gentle present-tense "
        "invitation, repeated: the walk, the project, the new thing to "
        "look forward to. Mistake six: hijacking - turning their memory "
        "into your story before theirs is finished. The common thread: "
        "all six mistakes treat the feeling as a problem to manage rather "
        "than a visit to honor."),
    how_it_works=(
        "Each mistake disrupts a mechanism. Mockery applies social "
        "punishment to an affiliative emotion: nostalgia's function is "
        "bonding and meaning, and ridicule converts the sharing impulse "
        "into shame, suppressing future sharing without reducing the "
        "feeling. Correcting the memory mistakes the target: the visit's "
        "value is affective (warmth, meaning), not archival (accuracy), so "
        "fact-checking attacks the wrong layer and reads as dismissal. "
        "Interruption aborts the arc mid-replay, leaving activated affect "
        "without its meaning-making resolution - the emotional equivalent "
        "of hanging up mid-sentence. Pathologizing misapplies a clinical "
        "frame to a normal process; the labeled person may then monitor "
        "and suppress a healthy emotion, losing its benefits. Feeding the "
        "stuckness (joining the permanent retrospective) reinforces the "
        "feedback loop by validating the 'nothing measures up' appraisal; "
        "confrontation triggers defensiveness that entrenches the pattern - "
        "while gentle repeated present-tense invitation works by "
        "rebuilding the present's reward value, giving the return "
        "mechanism something to return to. Hijacking violates the "
        "speaker's narrative ownership at the moment of maximum "
        "vulnerability. The thread - treating the visit as a problem - "
        "explains why good intentions misfire: the feeling was never the "
        "problem."),
    key_points=[
        "Do not mock it: ridicule shames a tender emotion and teaches hiding.",
        "Do not correct the memory: fact-checking attacks the wrong layer - the warmth is the point.",
        "Do not rush or interrupt: it strands the feeling mid-arc.",
        "Do not pathologize: treating a healthy visit as illness makes it feel shameful.",
        "Do not feed stuckness with permanent-retrospective talk - or with confrontation; use gentle present-tense invitation.",
        "Do not hijack their story with yours before theirs is finished.",
        "The thread: all six treat the feeling as a problem rather than a visit to honor."],
    requirements=[
        "Name six concrete mistakes with what each one disrupts.",
        "Give the helpful alternative for the stuckness case.",
        "Close on the common thread."],
    standards=[
        "Descriptive and educational only; general safe guidance, never therapy.",
        "Keep the tone instructive, never scolding."],
    citations=[CIT_GROSS, CIT_WILDSCHUT_2006],
    sig_lens=(
        "The Signature lens posts the guest-rules at the treasury door: "
        "no mocking the exhibits, no arguing with the catalog, no "
        "rushing the tour, no calling the hearth a hazard, no moving into "
        "the far rooms with the keeper, no hanging your own portraits "
        "over theirs. Honor the visit - it is the whole of the law.")),
# ------------------------------------------------- 32-34: related + simulation
dict(
    key="nostalgia_related_emotions", name="The Nostalgia Neighborhood: Related Emotions and How to Tell Them Apart",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "Nostalgia lives in a crowded neighborhood; here is the map. "
        "Longing: wanting what is absent - the ache without the warmth of "
        "the replay; longing reaches forward toward the missing thing, "
        "nostalgia dwells in the having-had. Wistfulness: nostalgia's "
        "gentler, dreamier sibling - softer, less detailed, more "
        "atmosphere than scene; if nostalgia is the album, wistfulness is "
        "the blurred photograph. Sentimentality: the tender response to "
        "the tender - it can attach to anything touching (a stranger's "
        "kindness, a film scene), while nostalgia attaches specifically to "
        "one's own past. Homesickness: nostalgia with a forwarding address "
        "- the ache aimed at a place or people, wanting return; nostalgia "
        "wants the time back, homesickness wants the place back. Grief: "
        "the aching response to loss - grief's center is the absence "
        "itself, while nostalgia's center is the preciousness of what was "
        "had; they overlap when the memory features someone gone, and the "
        "telltale is which dominates - the warmth of the having or the "
        "pain of the missing. Regret: the backward look at what was done "
        "wrong - regret appraises the past as mistaken, nostalgia appraises "
        "it as precious. Gratitude: the warm response to having received "
        "good - gratitude lives in the present tense of the gift, nostalgia "
        "in the past tense of the era; they meet when the nostalgic visit "
        "ends in thankfulness. Melancholy: a diffuse, lingering sadness "
        "without nostalgia's specific content - the weather versus the "
        "photograph. The practical use of the map: when the feeling is "
        "muddled, asking 'is the center the preciousness or the absence? "
        "the time or the place? the having or the mistake?' usually "
        "locates you within a street or two - and each neighbor answers "
        "to slightly different handling."),
    how_it_works=(
        "The neighbors are distinguished by appraisal: each emotion is the "
        "mind's read of a slightly different relational content. "
        "Nostalgia's appraisal is 'precious past, mine, gone but had'; "
        "longing's is 'valued absent, wanted now'; homesickness's is "
        "'valued place/people, separated'; grief's is 'irrevocable loss, "
        "the absence itself'; regret's is 'past action, judged mistaken'; "
        "gratitude's is 'good received, source acknowledged.' Because "
        "appraisals can stack - a memory can be simultaneously precious, "
        "absent, and located - the emotions blend at the borders, which is "
        "why the neighborhood feels crowded and why people report "
        "muddled feelings. The discriminator questions work by isolating "
        "the dominant appraisal: 'preciousness or absence?' separates "
        "nostalgia from grief; 'time or place?' separates it from "
        "homesickness; 'having or mistake?' separates it from regret. "
        "Each neighbor's handling differs slightly because each "
        "appraisal implies a different need: grief needs mourning, regret "
        "needs repair, homesickness needs connection or return, nostalgia "
        "needs the visit-and-return. Mapping them is therefore not "
        "taxonomy for its own sake but a practical routing system for "
        "response - including the response of simply letting the visit "
        "be what it is."),
    key_points=[
        "Longing: the ache without the replay - reaches for the missing; nostalgia dwells in the having-had.",
        "Wistfulness: the dreamier sibling - atmosphere over scene; the blurred photograph to nostalgia's album.",
        "Sentimentality: attaches to anything tender; nostalgia attaches to one's own past.",
        "Homesickness: wants the place back; nostalgia wants the time back.",
        "Grief: center is the absence; nostalgia's center is the preciousness of what was had.",
        "Regret: appraises the past as mistaken; nostalgia appraises it as precious.",
        "Gratitude: present tense of the gift; nostalgia: past tense of the era.",
        "Discriminator questions ('preciousness or absence? time or place?') locate you within a street or two."],
    requirements=[
        "Map at least seven neighbors with a crisp discriminator for each.",
        "Explain the appraisal logic behind the distinctions.",
        "Give the practical discriminator questions."],
    standards=[
        "Descriptive and educational only; never diagnose or label any real person.",
        "Keep discriminators behavioral and content-based, never clinical."],
    citations=[CIT_LAZARUS, CIT_WILDSCHUT_2006, CIT_APA],
    sig_lens=(
        "The Signature lens draws the neighborhood around the hearth: "
        "longing at the window, wistfulness in the armchair, homesickness "
        "at the door, grief in the chapel, regret at the desk, gratitude "
        "at the table. Every neighbor welcome, every house distinct - and "
        "the keeper knows each door by heart.")),
dict(
    key="nostalgia_emotion_mixes", name="Nostalgia Blends: Emotion Mixes, Plutchik-Style",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "Nostalgia blends the way colors do - here are the named mixtures. "
        "Nostalgia + joy = celebration: the reunion toast, the anniversary "
        "party, the old friends laughing until it hurts - the past's "
        "warmth amplified by present company; the blend of the golden "
        "evenings. Nostalgia + sadness = the classic bittersweet: the "
        "wedding photo that beams and stings, the lullaby that soothes "
        "and aches - the blend this whole database is built on. Nostalgia "
        "+ grief = mourning-with-memories: the memorial slideshow, the "
        "first holiday without them - the preciousness and the absence "
        "both at full volume, tender and heavy together. Nostalgia + "
        "gratitude = thanksgiving: the visit that ends in 'I was lucky' - "
        "the retired teacher reading old student letters, the feeling "
        "settling into quiet thankfulness. Nostalgia + pride = legacy: "
        "the hard years reframed as survived years, the old uniform, the "
        "diploma on the wall - 'we did that' warming the chest. Nostalgia "
        "+ longing = homesickness proper: the expatriate's ache, the song "
        "from home in a foreign city - the wish to return grown teeth. "
        "Nostalgia + regret = the backward audit: the reunion that "
        "surfaces the mishandled friendship, the 'if I had known then' - "
        "preciousness mixed with the sting of the mistake. Nostalgia + "
        "calm = reverie: the porch evening, the familiar view, the past "
        "resting lightly on the present like late sun - the gentlest "
        "blend, asking nothing. Each blend feels different, behaves "
        "differently, and asks for different handling - but all of them "
        "are nostalgia at the center, wearing the colors of its company."),
    how_it_works=(
        "Plutchik-style dyads treat complex emotions as combinations of "
        "primaries; nostalgia, itself already a blend, forms second-order "
        "blends when its appraisal ('precious past, mine') co-fires with "
        "another emotion's appraisal. The partner's appraisal adds its "
        "content: grief's 'irrevocable absence' intensifies the ache-track "
        "into mourning-with-memories; gratitude's 'good received' tips "
        "the meaning-track into thankfulness; pride's 'valued achievement, "
        "mine' reframes the past as legacy; longing's 'valued absent, "
        "wanted now' sharpens the wish into homesickness. The blends are "
        "not averages but interactions: each partner changes what the "
        "nostalgia does - celebration-nostalgia seeks company, "
        "grief-nostalgia seeks the memorial, reverie-nostalgia seeks the "
        "porch. This is why the 'handling' differs per blend: the response "
        "must answer the partner's need as well as nostalgia's. The "
        "educational value of the mixer is recognition: naming 'this is "
        "nostalgia plus regret' tells the person both what is happening "
        "(the precious past, visited) and what the extra sting is (the "
        "mistake, asking for repair or release) - and the two answers "
        "suggest the two-part response."),
    key_points=[
        "Nostalgia + joy = celebration: the reunion toast, golden evenings with present company.",
        "Nostalgia + sadness = the classic bittersweet this database is built on.",
        "Nostalgia + grief = mourning-with-memories: preciousness and absence at full volume.",
        "Nostalgia + gratitude = thanksgiving: the visit ending in 'I was lucky.'",
        "Nostalgia + pride = legacy: the hard years reframed as survived years.",
        "Nostalgia + longing = homesickness proper: the wish to return grown teeth.",
        "Nostalgia + regret = the backward audit: preciousness mixed with the sting of the mistake.",
        "Nostalgia + calm = reverie: the past resting lightly on the present like late sun.",
        "Blends are interactions, not averages - each partner changes what the nostalgia does."],
    requirements=[
        "Name and describe at least seven blends with concrete scenes.",
        "Explain the dyad logic in plain language.",
        "Show how the partner changes the handling."],
    standards=[
        "Descriptive and educational only; never diagnose or label any real person.",
        "Keep every blend scene universal and ordinary."],
    citations=[CIT_LAZARUS, CIT_WILDSCHUT_2006, CIT_IZARD],
    sig_lens=(
        "The Signature lens keeps the blending room behind the hearth: "
        "the keeper knows every mixture by color - celebration gold, "
        "bittersweet amber, mourning violet, thanksgiving honey, legacy "
        "bronze, homesick blue, audit grey, reverie rose. Same fire, "
        "different light on the walls.")),
dict(
    key="nostalgia_full_simulation", name="Full Behavioral Simulation: Nostalgia from Trigger Through Peak to Resolution",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "Scene one, the trigger - 6:40 p.m., a Tuesday in October. She is "
        "driving home when the radio plays the song from the summer she "
        "was nineteen - the summer of the lake house, the summer before "
        "everything changed. The first chord lands like a hand on her "
        "shoulder. Her breath catches; her hands tighten once on the "
        "wheel, then loosen. She does not change the station. Scene two, "
        "the rise - 6:43. The second verse opens the rooms in sequence: "
        "the dock, the screen door's squeak, her brother's laugh, the "
        "smell of sunscreen and pine. Her gaze goes soft on the road "
        "ahead - still driving safely, but the seeing is happening "
        "elsewhere. The small smile arrives unchosen. Her chest warms and "
        "hollows at once. Scene three, the peak - 6:51, parked in her own "
        "driveway, engine off, song on repeat. The tears come without "
        "permission - not sobs, just the shine spilling over. She sees "
        "the last evening at the lake house with terrible clarity: the "
        "lanterns, the promises they all made, her grandmother's hand in "
        "hers. The ache swells until it is almost too much - and then, "
        "underneath it, the gratitude surfaces: this happened. I was "
        "there. I was loved like that. Scene four, the turn - 6:58. The "
        "song ends. She sits in the sudden quiet and takes the deep "
        "breath - the reset. Her hand presses her chest once, briefly. "
        "She reaches for her phone. Scene five, the channeling - 7:05. "
        "She texts her brother three words from the chorus. He answers in "
        "seconds: a photo she has never seen - the four of them on the "
        "dock, sun-struck and laughing. She laughs through the shine. "
        "Scene six, the resolution - 8:30. Dinner tastes better than "
        "usual. She tells her partner about the lake house summer - the "
        "long version, the sensory close-ups - and he asks what happened "
        "next, and she tells that too. Later she writes four lines in a "
        "notebook: the lanterns, the squeak of the screen door, her "
        "grandmother's hand. She sleeps easily. The visit is over. What "
        "remains is the aftershock: for days, a steadiness, as if the "
        "summer of nineteen reached forward and steadied the autumn of "
        "now. That is the full arc - trigger, rise, peak, turn, "
        "channeling, resolution - the archive's showcase of nostalgia "
        "doing exactly what it is for."),
    how_it_works=(
        "The simulation strings the database's mechanisms into one "
        "continuous arc. The trigger (song + October light + the drive "
        "home) stacks cues for maximal associative activation. The rise "
        "shows spreading activation room-by-room and the attentional "
        "absorption that softens the gaze while preserving driving "
        "safety - absorption is partial, not total. The peak stages the "
        "bittersweet blend at high intensity: the ache-track (the last "
        "evening, the promises, the grandmother's hand) and the "
        "meaning-track (gratitude: this happened, I was loved) running "
        "together, with lacrimal overflow marking the crest. The turn "
        "demonstrates the regulation beat: the song's end provides a "
        "natural boundary, the deep breath and hand-to-chest are the "
        "body's transition markers, and the phone reach is the first "
        "channeling impulse. The channeling scene shows the social "
        "mechanism - shared reminiscence converting private warmth into "
        "bonding, with the unseen photo as the treasury paying interest. "
        "The resolution completes the meaning-action arc: the telling "
        "(savoring, extended), the notebook lines (encoding specificity "
        "preserved), the easy sleep (calm arousal profile), and the "
        "multi-day aftershock (meaning, continuity, and steadiness "
        "compounding). Every beat is drawn from the preceding 33 records; "
        "the simulation is the database demonstrating itself."),
    key_points=[
        "Trigger: stacked cues (song, season, drive home) for maximal associative activation.",
        "Rise: room-by-room spreading activation; gaze softens while safety holds.",
        "Peak: bittersweet at high intensity - ache-track and gratitude-track together; shine spills.",
        "Turn: the song's end as natural boundary; breath and hand-to-chest as transition markers.",
        "Channeling: the text to her brother; shared reminiscence; the unseen photo as interest paid.",
        "Resolution: the long telling, four notebook lines, easy sleep, days of steadiness.",
        "The full arc: trigger, rise, peak, turn, channeling, resolution - nostalgia doing what it is for."],
    requirements=[
        "Walk at least six timestamped scenes from trigger to resolution.",
        "Show the bittersweet blend, the body signals, the speech, and the channeling in-scene.",
        "End on the aftershock and the function fulfilled."],
    standards=[
        "Descriptive and educational only; never diagnose or label any real person.",
        "Keep all characters and details generic and universal."],
    citations=[CIT_WILDSCHUT_2006, CIT_SEDIKIDES_2008, CIT_ROUTLEDGE_2016, CIT_BOWER],
    sig_lens=(
        "The Signature lens stages the keeper's perfect round: the "
        "uninvited knock at 6:40, the tour through every lit room, the "
        "blaze at its brightest, the banking of the coals, the treasure "
        "lent to the brother, the four lines entered in the log, the "
        "warm house at 8:30. Trigger to resolution, every mechanism "
        "singing - the treasury demonstrating itself.")),
]

assert len(ENTRIES) == 34, "expected 34 entries, got %d" % len(ENTRIES)
ranks = [e["ladder_rank"] for e in ENTRIES]
assert ranks == sorted(ranks), "entries not in ladder order"
assert all(1 <= r <= 10 for r in ranks)
tiers = [e["ladder_tier"] for e in ENTRIES]
assert set(tiers) <= {"foundations", "compounded", "advanced"}
