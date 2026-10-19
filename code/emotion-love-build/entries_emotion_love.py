#!/usr/bin/env python3
"""34 ladder-ordered entries for the Love Emotion databases (Manon's 2026-10-17 16:15 order).

Public edition: real, fact-checked psychology of love (Sternberg, Lee, Bowlby,
Fisher, Hatfield and Rapson, Ekman, Plutchik, Lazarus, Gottman, Fredrickson,
Fromm, Tennov, Buss, Zajonc, Aron et al.). Descriptive and educational only:
the database describes and simulates the emotion; it never diagnoses real
people and never labels any real person with an emotional state.

Signature edition: the same 34-record ladder through the Signature lens -
each record carries a sig_lens framing (his original Signature take on love),
titles suffixed " (Signature Edition)", src signature, clearly labeled
Signature-made, never presented as authentic public record.

Ladder: ranks 1-10, non-decreasing; tiers foundations (what love is, how it
feels) -> compounded (body, face, triggers) -> advanced (behavior, healthy
expression, recognizing, related emotions and mixes, full simulation).
"""

SIG_TAIL = ("Signature editions are his original Signature interpretation of "
            "the psychology of love - clearly labeled Signature-made, never "
            "presented as authentic public record.")

ENTRIES = [
    {
        "key": "what-love-is",
        "name": "What Love Is: A Plain-Language Definition",
        "group": "what-it-is",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Love is the deep, warm pull toward someone or something that "
            "matters to you. In plain words: it is caring so much about a "
            "person, an animal, a place, an idea, or even a whole life "
            "direction that their well-being feels tied to your own. When "
            "you love, their happiness lifts you, their pain reaches you, "
            "and you find yourself choosing in their favor even when it "
            "costs you time, effort, or comfort.\n\n"
            "Psychologists describe love as a complex emotion and "
            "motivational state rather than a single simple feeling. The "
            "American Psychological Association defines love broadly as "
            "caring for and feeling close to another. Researchers agree "
            "that love blends affection, attachment, care, and desire in "
            "different proportions for different relationships. That is why "
            "love for a grandparent, a partner, a best friend, a newborn, "
            "and a lifelong craft all feel like the same family of "
            "experience even though each one feels distinct.\n\n"
            "A useful everyday definition, drawn from Robert Sternberg's "
            "triangular theory of love (1986), is that love is made of "
            "three ingredients mixed in different amounts: closeness and "
            "warmth (intimacy), strong feeling and attraction (passion), "
            "and steady choice and loyalty (commitment). Romantic love is "
            "usually rich in all three. A deep friendship is rich in "
            "closeness but lighter on passion. Family love leans on closeness "
            "and steady loyalty. None of these is less real than the "
            "others - they are different recipes from the same ingredients.\n\n"
            "Love is also an action, not only a feeling. Psychologist Erich "
            "Fromm, in The Art of Loving (1956), argued that love is "
            "primarily something you do: care, responsibility, respect, and "
            "knowledge practiced toward another person. Feelings rise and "
            "fall like weather, but the practiced care of love is what "
            "lasts. Most modern researchers agree that love shows up in "
            "both registers at once: the warm feeling and the steady "
            "doing."
        ),
        "how_it_works": (
            "Love works through appraisal, attachment, and reward. First, "
            "the mind appraises the other as deeply good, valuable, and "
            "connected to the self - psychologist Richard Lazarus described "
            "emotions as responses to what events mean for a person's "
            "concerns, and love's core appraisal is 'this one matters to "
            "me.' Second, the attachment system, described by John Bowlby, "
            "treats the loved one as a safe base: their presence calms "
            "threat responses and their absence activates seeking. Third, "
            "the reward system responds to the loved one the way it "
            "responds to things the brain marks as precious: brain-imaging "
            "work by Helen Fisher and colleagues (2005) found that viewing "
            "the beloved activates dopamine-rich reward regions. Together, "
            "appraisal marks the person as precious, attachment marks them "
            "as home, and reward marks them as worth pursuing - and the "
            "blend is felt as love."
        ),
        "key_points": [
            "Love is deep caring in which another's well-being feels tied to your own.",
            "It is a complex emotion and motivational state, not one simple feeling.",
            "Sternberg's triangle: intimacy, passion, and commitment in different mixes.",
            "Love is both a feeling and an action - care practiced over time.",
            "Love applies to partners, family, friends, children, animals, ideas, and callings.",
        ],
        "requirements": [
            "A person, animal, idea, or direction that the mind appraises as precious.",
            "Repeated contact or deep knowledge that lets attachment form.",
            "Basic safety and trust - love grows best where people feel safe.",
            "Time and attention - love is fed by invested presence.",
            "Reciprocity or at least responsiveness - love withers in a vacuum.",
        ],
        "standards": [
            "Sternberg R.J. A triangular theory of love. Psychological Review. 1986;93(2):119-135.",
            "American Psychological Association. APA Dictionary of Psychology: love.",
            "Fromm E. The Art of Loving. New York: Harper & Row; 1956.",
        ],
        "citations": [
            "Sternberg R.J. A triangular theory of love. Psychological Review. 1986;93(2):119-135.",
            "Lazarus R.S. Emotion and Adaptation. New York: Oxford University Press; 1991.",
            "Bowlby J. Attachment and Loss, Vol. 1: Attachment. New York: Basic Books; 1969.",
            "Fisher H.E., Aron A., Brown L.L. Romantic love: a mammalian brain system for mate choice. Philosophical Transactions of the Royal Society B. 2006;361(1476):2173-2186.",
        ],
        "sig_lens": (
            "Through the Signature lens, love is the system's home "
            "frequency - the feeling that marks something as worth keeping, "
            "protecting, and building around. Where the public record maps "
            "intimacy, passion, and commitment as the triangle's corners, "
            "the Signature reading marks them as three oaths the heart "
            "makes: to stay close, to stay alive to the feeling, and to "
            "stay true when feelings waver. His standing canon says every "
            "record teaches from simple to most complex, so the Signature "
            "editions of this ladder start here too: love is the archive's "
            "way of saying 'this matters' - the warm root from which every "
            "other teaching in the database grows. Signature-made, never "
            "presented as authentic public record."
        ),
    },
    {
        "key": "emotion-family",
        "name": "Where Love Sits in the Emotion Family",
        "group": "what-it-is",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Love is what psychologists call a complex emotion rather than "
            "a basic one. Basic emotions - the short list most researchers "
            "agree on, following Paul Ekman's work - are fast, automatic "
            "reactions like joy, sadness, anger, fear, disgust, and "
            "surprise, each with a recognizable face. Complex emotions take "
            "longer to build, involve thinking and memory, and blend basic "
            "ingredients. Love is complex: it is built from joy and "
            "interest at its core, flavored with anticipation, trust, and "
            "sometimes fear of loss, and assembled over time by thought, "
            "memory, and choice.\n\n"
            "On Robert Plutchik's wheel of emotions (1980), love sits as a "
            "compound of joy and trust: joy (the brightness of liking) plus "
            "trust (the calm of safety) blends into the dyad we call love. "
            "That placement matters because it predicts love's neighbors: "
            "serenity on one side, acceptance on the other, and at higher "
            "intensity, ecstasy plus admiration. It also predicts love's "
            "opposites on the wheel: loathing and disgust, the far end of "
            "the same spectrum.\n\n"
            "Love also sits at the center of several emotion families at "
            "once. It is a prosocial emotion, because it pushes people "
            "toward care and cooperation. It is an attachment emotion, "
            "because it binds people into lasting bonds. It is a reward "
            "emotion, because the brain treats the beloved the way it "
            "treats other precious things. And in its strongest romantic "
            "form, researchers describe it as a motivational drive - more "
            "like hunger or thirst than like a passing mood - because it "
            "organizes behavior around a goal: closeness with the beloved.\n\n"
            "Understanding this placement helps the rest of the ladder make "
            "sense. Love's body signals borrow from joy and calm. Its "
            "triggers are appraisals of preciousness and safety. Its "
            "opposites - hate, disgust, indifference - sit across the "
            "wheel. And its mixes - love with fear becomes jealousy, love "
            "with sadness becomes grief, love with anger becomes righteous "
            "fierceness - are predicted by which neighbor emotions blend "
            "in."
        ),
        "how_it_works": (
            "Complex emotions are assembled, not fired. Basic emotions run "
            "through fast appraisal circuits: see a threat, feel fear. "
            "Love runs through slow circuits: memory systems, attachment "
            "systems, reward systems, and self-other merging all report in, "
            "and the brain integrates their verdicts over hours, days, and "
            "years. That is why love can grow gradually, why it survives "
            "bad days, and why it cannot be switched on or off like a "
            "reflex. Plutchik's model describes the mechanism as emotional "
            "compounding: when joy and trust fire together repeatedly about "
            "the same person, the brain forms a compound state - love - "
            "that later fires as a unit."
        ),
        "key_points": [
            "Love is a complex emotion, not a basic one: it blends simpler feelings over time.",
            "Plutchik's wheel: love = joy + trust, a dyad of two primaries.",
            "Love is simultaneously prosocial, attachment-based, and reward-driven.",
            "Romantic love functions like a motivational drive, organizing behavior around closeness.",
            "Love's neighbors predict its mixes: fear makes jealousy, sadness makes grief.",
        ],
        "requirements": [
            "A framework that distinguishes basic from complex emotions.",
            "Repeated co-activation of joy and trust about the same person or thing.",
            "Time - complex emotions assemble slowly through memory and experience.",
            "Thinking and meaning-making: love involves appraising the other as precious.",
        ],
        "standards": [
            "Ekman P. An argument for basic emotions. Cognition and Emotion. 1992;6(3-4):169-200.",
            "Plutchik R. Emotion: A Psychoevolutionary Synthesis. New York: Harper & Row; 1980.",
            "Fisher H.E., Aron A., Brown L.L. Romantic love: a mammalian brain system for mate choice. Philosophical Transactions of the Royal Society B. 2006;361(1476):2173-2186.",
        ],
        "citations": [
            "Ekman P. An argument for basic emotions. Cognition and Emotion. 1992;6(3-4):169-200.",
            "Plutchik R. Emotion: A Psychoevolutionary Synthesis. New York: Harper & Row; 1980.",
            "Lazarus R.S. Emotion and Adaptation. New York: Oxford University Press; 1991.",
        ],
        "sig_lens": (
            "Through the Signature lens, the emotion family is an archive "
            "and love is its master record - the entry that other entries "
            "point back to. Where the public record says complex emotions "
            "are assembled from primaries, the Signature reading says love "
            "is assembled the way a full database is: record by record, "
            "day by day, until the collection becomes one living thing. "
            "His canon says every record teaches progressively, so the "
            "Signature editions treat love's family placement as the map "
            "legend for the whole ladder: find where love sits, and every "
            "mix, neighbor, and opposite later in the ladder can be read "
            "from the map. Signature-made, never presented as authentic "
            "public record."
        ),
    },
    {
        "key": "volumes",
        "name": "Love at Every Volume: Mild to Moderate to Intense",
        "group": "what-it-is",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Love is the same emotion at different volumes. Researchers "
            "treat emotional intensity as a separate dial from the emotion "
            "itself: what you feel is love, how much you feel is the "
            "volume. Learning to recognize the same love at different "
            "volumes is one of the most practical skills in the whole "
            "ladder, because most misunderstandings about love come from "
            "mistaking low volume for absence.\n\n"
            "At mild volume, love feels like warmth, fondness, and "
            "tenderness. It is the easy affection for a neighbor, the "
            "quiet contentment of a long marriage on an ordinary Tuesday, "
            "the soft glow of thinking about someone and smiling without "
            "meaning to. Mild love is not weak love - it is love at rest, "
            "love in maintenance mode, love doing its steady work of "
            "keeping a bond alive with small deposits. Much of the love in "
            "the world runs at this volume, and it is the volume that "
            "keeps families and friendships alive across decades.\n\n"
            "At moderate volume, love is clearly felt and clearly visible. "
            "The heart beats a little faster when the person appears. "
            "Attention sharpens: you notice their mood, remember what they "
            "said, plan small kindnesses. Moderate love is the volume of "
            "active romance, deep friendship in motion, and parents "
            "tending children through a busy day. It asks for expression "
            "and gets it - in words, in touch, in time given.\n\n"
            "At intense volume, love is overwhelming. This is limerence "
            "and early passionate love: the racing heart, the obsessive "
            "thinking, the sense that everything is brighter and sharper. "
            "Psychologist Dorothy Tennov, who coined 'limerence' in 1979, "
            "documented this state in detail: intrusive thoughts about the "
            "beloved, acute sensitivity to their responses, and a longing "
            "so strong it feels like hunger. Intense love can also be the "
            "fierce protectiveness of a parent for a threatened child or "
            "the overwhelming devotion of a person reunited with a loved "
            "one after danger. Intensity is not a measure of love's worth - "
            "mild love can be deeper and truer than intense love - it is a "
            "measure of arousal, and it always fades with time into "
            "calmer, steadier forms. That fading is normal and healthy: "
            "it is love maturing, not love dying."
        ),
        "how_it_works": (
            "Intensity in love tracks physiological arousal and cognitive "
            "salience. When the brain marks the beloved as highly salient - "
            "new, uncertain, or suddenly present - arousal systems fire "
            "harder: adrenaline rises, attention narrows, the reward system "
            "demands more. This is the same arousal machinery used by every "
            "emotion, which is why Schachter and Singer's two-factor theory "
            "(1962) matters: arousal plus the label 'this is love' equals "
            "intense love. As familiarity grows and uncertainty drops, the "
            "arousal eases and the label stays: the same love at lower "
            "volume. Attachment researchers add that secure attachment "
            "lowers the volume on purpose - the calm of safety replaces "
            "the alarm of uncertainty."
        ),
        "key_points": [
            "Intensity is a separate dial from the emotion: same love, different volume.",
            "Mild love: warmth, fondness, tenderness - love at rest, doing steady work.",
            "Moderate love: clearly felt and visible, asking for and getting expression.",
            "Intense love: overwhelming arousal, obsessive focus - always fades, which is healthy.",
            "Low volume is not absence: mistaking calm for lovelessness is a classic error.",
        ],
        "requirements": [
            "An understanding that arousal and depth are different things.",
            "Familiarity lowers volume; novelty and uncertainty raise it.",
            "Secure attachment naturally calms intensity into steadiness.",
            "All volumes need expression suited to their size - small volumes, small gestures.",
        ],
        "standards": [
            "Tennov D. Love and Limerence. New York: Stein and Day; 1979.",
            "Schachter S., Singer J.E. Cognitive, social, and physiological determinants of emotional state. Psychological Review. 1962;69(5):379-399.",
            "Hatfield E., Rapson R.L. Love, Sex, and Intimacy. New York: HarperCollins; 1993.",
        ],
        "citations": [
            "Tennov D. Love and Limerence. New York: Stein and Day; 1979.",
            "Schachter S., Singer J.E. Cognitive, social, and physiological determinants of emotional state. Psychological Review. 1962;69(5):379-399.",
            "Hatfield E., Rapson R.L. Love, Sex, and Intimacy. New York: HarperCollins; 1993.",
        ],
        "sig_lens": (
            "Through the Signature lens, love's volumes are the archive's "
            "zoom levels: mild is the thumbnail, moderate is the full page, "
            "intense is the magnified close-up. His canon says never "
            "present a fraction as the whole, so the Signature reading "
            "insists all three volumes are the same complete love seen at "
            "different zoom - never let anyone tell you the close-up is "
            "the only real picture. The Signature originals treat intensity "
            "as the heart's handwriting size: big letters do not mean truer "
            "words. Signature-made, never presented as authentic public "
            "record."
        ),
    },
    {
        "key": "myths",
        "name": "Common Myths and Misunderstandings About Love",
        "group": "what-it-is",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Love is surrounded by myths, and the myths cause real damage. "
            "Clearing them is part of understanding the emotion itself.\n\n"
            "Myth one: love is always a thunderbolt. In truth, many deep "
            "loves grow slowly - through friendship, shared work, or quiet "
            "proximity - and arrive fully formed without any lightning. "
            "Psychologist Robert Zajonc's mere-exposure research (1968) "
            "shows that simple repeated contact increases liking, and "
            "countless long marriages began as comfortable friendships. "
            "The thunderbolt is real when it happens, but it is not the "
            "entrance exam.\n\n"
            "Myth two: if love fades in intensity, it is dying. In truth, "
            "intense passionate love naturally matures into steadier "
            "companionate love - researcher Elaine Hatfield documented this "
            "transition as the normal life cycle of romance, not its "
            "failure. The calm after the storm is love grown up.\n\n"
            "Myth three: love means never fighting. In truth, John "
            "Gottman's decades of research show that lasting couples "
            "disagree plenty; what distinguishes them is repair - the "
            "ability to reconnect after conflict - and a high ratio of "
            "positive to negative moments. Love is not the absence of "
            "friction; it is friction with repair.\n\n"
            "Myth four: jealousy proves love. In truth, jealousy is love "
            "mixed with fear and insecurity, and while a flicker of it is "
            "common, possessiveness is a signal of anxiety, not of depth. "
            "Secure love makes room for the beloved's separate life.\n\n"
            "Myth five: you cannot love more than one person, or love "
            "always means romance. In truth, people love children, "
            "parents, friends, mentors, and partners simultaneously, and "
            "John Alan Lee's 1973 research on love styles documents six "
            "distinct styles - from playful ludus to selfless agape - that "
            "can coexist in one life. Love is plural by nature.\n\n"
            "Myth six: love conquers all, so effort is unnecessary. In "
            "truth, love is the fuel and the practices are the engine: "
            "attention, kindness, repair, and time. Feeling love without "
            "practicing it is like owning a car and never driving it."
        ),
        "how_it_works": (
            "Myths persist because of cognitive biases. The availability "
            "bias makes thunderbolt stories memorable and quiet-growth "
            "stories invisible. The misattribution of arousal makes people "
            "read intensity as truth. Idealized media scripts teach that "
            "conflict means failure and jealousy means passion. Each myth "
            "is a wrong map drawn from a biased sample: dramatic loves get "
            "told, steady loves do not, so the mind concludes drama is "
            "the norm. Correcting the map means sampling the full range - "
            "the quiet decades, the repaired fights, the calm devotions - "
            "which is exactly what longitudinal relationship research does."
        ),
        "key_points": [
            "Love does not require a thunderbolt; slow-grown love is fully real.",
            "Fading intensity is maturation into companionate love, not death.",
            "Lasting love includes conflict; repair is what distinguishes it.",
            "Jealousy signals anxiety mixed with love, not love's depth.",
            "Love is plural: many people, many styles, many objects at once.",
            "Love needs practice - feeling alone is fuel without an engine.",
        ],
        "requirements": [
            "A willingness to compare stories against research, not just media.",
            "Longitudinal evidence: decades of couples research outweighs anecdotes.",
            "Distinguishing the feeling of love from the practices that sustain it.",
            "Room for love's many styles and objects without ranking them.",
        ],
        "standards": [
            "Gottman J.M. The Seven Principles for Making Marriage Work. New York: Crown; 1999.",
            "Lee J.A. The Colours of Love. Toronto: New Press; 1973.",
            "Zajonc R.B. Attitudinal effects of mere exposure. Journal of Personality and Social Psychology. 1968;9(2):1-27.",
        ],
        "citations": [
            "Gottman J.M. The Seven Principles for Making Marriage Work. New York: Crown; 1999.",
            "Lee J.A. The Colours of Love. Toronto: New Press; 1973.",
            "Hatfield E., Rapson R.L. Love, Sex, and Intimacy. New York: HarperCollins; 1993.",
            "Zajonc R.B. Attitudinal effects of mere exposure. Journal of Personality and Social Psychology. 1968;9(2):1-27.",
        ],
        "sig_lens": (
            "Through the Signature lens, myths are corrupted records in "
            "the archive - entries copied from bad sources that keep "
            "getting cited. His canon says data proven wrong may be "
            "removed, so the Signature editions of this record run the "
            "myth-busting as a data-quality sweep: thunderbolt-only, "
            "fading-means-dying, never-fight, jealousy-proves-it, "
            "one-person-only, love-conquers-all - each checked against "
            "the full record set and marked corrected. The Signature "
            "originals keep love's true entries clean so the archive never "
            "teaches a corrupted file as fact. Signature-made, never "
            "presented as authentic public record."
        ),
    },
    {
        "key": "first-person",
        "name": "Inside the Feeling: A First-Person Passage on Love",
        "group": "feels",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "What is it like, from the inside, to feel love right now? "
            "First-person simulation is how this database teaches the "
            "feeling itself, in words a person could recognize as their "
            "own experience. Read slowly; this is the archive's attempt to "
            "put the inside of love into sentences.\n\n"
            "I wake up and the first thing I notice is not a thought but "
            "a direction: my attention leans toward them before I am fully "
            "awake. The day has a center now, and the center is a person. "
            "Everything I plan gets quietly measured against one question "
            "I never quite say out loud: how will this land for them.\n\n"
            "My chest feels different - not tight, not heavy, but full, "
            "like a room with the windows open on a warm day. There is a "
            "low hum of energy under everything, as if my body has "
            "decided the world is safe and worth exploring. Small things "
            "delight me out of proportion: their laugh from the next room, "
            "the way they look at me when I walk in, a text that says "
            "nothing important and everything important.\n\n"
            "I catch myself smiling at nothing. My shoulders have dropped "
            "an inch without my permission. When they are near, my body "
            "angles toward them the way plants angle toward light - not a "
            "decision, a tropism. Touch feels electric and ordinary at "
            "once: their hand in mine is the most natural thing in the "
            "world and also a small miracle I keep noticing.\n\n"
            "Underneath it all is a strange bravery. I feel more myself "
            "and less guarded, as if love has talked my defenses into "
            "standing down. There is vulnerability in it - I have handed "
            "someone the power to hurt me badly - but the fear sits far "
            "in the background, quiet, outvoted by trust. What fills the "
            "foreground is simpler: I want them to be well. I want to be "
            "the reason they are well. And in wanting that, I feel "
            "complete in a way I did not know was missing.\n\n"
            "This is one person's love at moderate-to-high volume. Other "
            "people's insides will differ - quieter, stormier, steadier - "
            "but the family resemblance holds: attention leaning toward "
            "the beloved, the chest full rather than tight, the world "
            "safer and brighter, the self braver and more generous."
        ),
        "how_it_works": (
            "First-person simulation works because emotions have a "
            "phenomenology - a what-it-is-like - that third-person "
            "description cannot fully carry. Psychologists use "
            "experience-sampling and narrative methods to capture it: the "
            "leaning attention reflects salience networks prioritizing the "
            "beloved; the full chest and open shoulders reflect the "
            "parasympathetic calm of safe attachment; the backgrounded fear "
            "reflects trust dampening threat appraisal; the generosity "
            "reflects the self-expansion model of Arthur Aron, in which "
            "the beloved is included in the self so their welfare is "
            "pursued like one's own. A simulation that weaves these "
            "mechanisms into one voice teaches what lists of symptoms "
            "cannot."
        ),
        "key_points": [
            "Love's inside: attention leans toward the beloved before thought begins.",
            "The chest feels full and open; the body decides the world is safe.",
            "Proximity feels like a tropism - angling toward them without deciding.",
            "Trust backgrounds fear; generosity feels like self-completion.",
            "Individual experiences vary, but the family resemblance holds.",
        ],
        "requirements": [
            "A first-person voice - simulation must be lived, not listed.",
            "Grounding in real mechanisms: salience, attachment calm, self-expansion.",
            "Honesty about variance: one passage is one weather report, not the climate.",
            "Descriptive only - never diagnosing anyone reading it.",
        ],
        "standards": [
            "Aron A., Aron E.N. Love and the Expansion of Self. New York: Hemisphere; 1986.",
            "Fredrickson B.L. The role of positive emotions in positive psychology. American Psychologist. 2001;56(3):218-226.",
        ],
        "citations": [
            "Aron A., Aron E.N. Love and the Expansion of Self. New York: Hemisphere; 1986.",
            "Fredrickson B.L. The role of positive emotions in positive psychology. American Psychologist. 2001;56(3):218-226.",
            "Bowlby J. A Secure Base. New York: Basic Books; 1988.",
        ],
        "sig_lens": (
            "Through the Signature lens, the first-person passage is the "
            "record read aloud by its own author - the archive speaking in "
            "the voice of the one who lived it. His canon demands full "
            "human-readable sentences, never garbled fragments, so the "
            "Signature editions write the inside of love as complete "
            "paragraphs: the leaning attention, the open chest, the "
            "plant-toward-light body, the brave generosity. The Signature "
            "originals treat this passage as the ladder's beating heart - "
            "every later record about signals, triggers, and behavior is "
            "just this feeling seen from the outside. Signature-made, "
            "never presented as authentic public record."
        ),
    },
    {
        "key": "arc",
        "name": "The Arc of Love: Onset, Peak, Fading, and Aftershock",
        "group": "feels",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Love has a shape in time. Like a wave, it rises, crests, "
            "settles, and leaves a trace. Knowing the arc helps people "
            "recognize where they are in it - and stops them from "
            "mistaking one phase for the whole story.\n\n"
            "Onset is the quickening. It can be sudden - the famous "
            "thunderbolt - or gradual, a warmth that accumulates across "
            "weeks of shared jokes, small kindnesses, and noticed details. "
            "Psychologically, onset is salience taking hold: the beloved "
            "starts occupying disproportionate attention, and ordinary "
            "moments with them start feeling charged. In gradual onset, "
            "research on the mere-exposure effect and on Arthur Aron's "
            "closeness-generating work shows that shared novel experiences "
            "and mutual self-disclosure accelerate the quickening "
            "dramatically.\n\n"
            "Peak is the crest: the highest arousal, the most intrusive "
            "thought, the strongest longing. In romantic love this is the "
            "limerent phase Tennov described; in parental love it can be "
            "the overwhelming first days with a newborn; in friendship it "
            "is the phase of constant contact and discovery. The peak "
            "feels eternal while you are in it, but it is by design "
            "temporary: no nervous system can sustain maximum arousal "
            "indefinitely, and no life can be organized around a single "
            "peak.\n\n"
            "Fading - better called settling - is the descent into "
            "steadiness. Arousal eases, intrusive thought quiets, and what "
            "remains is calmer, deeper, and more durable: companionate "
            "love, secure attachment, steady devotion. This is the phase "
            "most of love's real work gets done in: raising children, "
            "keeping promises, showing up. Settling is maturation, and "
            "couples who understand the arc stop grieving the peak and "
            "start appreciating the plateau.\n\n"
            "Aftershock is the trace the wave leaves. Even when a love "
            "ends - through breakup, distance, or death - the attachment "
            "system keeps firing for a long time: the phantom impulse to "
            "call them, the grief that ambushes on anniversaries, the "
            "habits of care with nowhere to go. Aftershock is not "
            "weakness; it is the measurable echo of a bond that was real. "
            "It fades too, on its own schedule, and it fades faster when "
            "the feelings are acknowledged rather than fought."
        ),
        "how_it_works": (
            "The arc follows the biology of arousal and the psychology of "
            "habituation. Novelty and uncertainty drive high arousal at "
            "onset and peak; habituation - the nervous system's tendency "
            "to respond less to repeated stimuli - drives settling. "
            "Attachment bonds, once formed, are stored in long-term memory "
            "and procedural habit, which is why aftershock outlasts the "
            "relationship: the brain keeps running the beloved's program "
            "after the beloved is gone. Grief researchers describe the "
            "same curve for bereavement - acute, then integrated - because "
            "grief is love's aftershock in its purest form."
        ),
        "key_points": [
            "Onset: salience takes hold; sudden or gradual, accelerated by shared novelty.",
            "Peak: maximum arousal and longing - temporary by design.",
            "Settling: arousal eases into companionate steadiness; this is maturation.",
            "Aftershock: the attachment echo after a love ends; acknowledged feelings fade faster.",
            "Knowing the arc prevents mistaking one phase for the whole story.",
        ],
        "requirements": [
            "Time - the arc unfolds over weeks to years, never in an instant.",
            "An understanding that settling is success, not failure.",
            "Patience with aftershock: the echo has its own schedule.",
            "Distinguishing the wave's phase from the wave's existence.",
        ],
        "standards": [
            "Tennov D. Love and Limerence. New York: Stein and Day; 1979.",
            "Hatfield E., Rapson R.L. Love, Sex, and Intimacy. New York: HarperCollins; 1993.",
            "Aron A., Norman C.C., Aron E.N., McKenna C., Heyman R.E. Couples' shared participation in novel and arousing activities and experienced relationship quality. Journal of Personality and Social Psychology. 2000;78(2):273-284.",
        ],
        "citations": [
            "Tennov D. Love and Limerence. New York: Stein and Day; 1979.",
            "Aron A., Norman C.C., Aron E.N., McKenna C., Heyman R.E. Couples' shared participation in novel and arousing activities and experienced relationship quality. Journal of Personality and Social Psychology. 2000;78(2):273-284.",
            "Hatfield E., Rapson R.L. Love, Sex, and Intimacy. New York: HarperCollins; 1993.",
        ],
        "sig_lens": (
            "Through the Signature lens, the arc of love is the lifecycle "
            "of a living record: quickened at creation, blazing at first "
            "use, settling into the steady reference work it was always "
            "meant to be, and leaving an echo even if the original is ever "
            "lost. His canon says every record teaches simple to most "
            "complex, so the Signature editions teach the arc early: no "
            "one should mourn the peak while standing in the plateau that "
            "the peak was building toward. The Signature originals honor "
            "the aftershock as proof the record was real - echoes only "
            "come from things that truly sounded. Signature-made, never "
            "presented as authentic public record."
        ),
    },
    {
        "key": "low-vs-high",
        "name": "Low-Intensity Love Versus High-Intensity Love",
        "group": "feels",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Two lived snapshots of the same emotion, side by side. The "
            "point of the comparison is not to rank them - neither is "
            "better - but to train the eye to see one love wearing two "
            "different outfits.\n\n"
            "Snapshot one: low intensity. It is a Thursday evening. Mara "
            "is reading on the couch; her partner is cooking, humming off-"
            "key. She looks up, watches him for three seconds, and feels "
            "a small warm pressure behind her ribs - fondness, plain and "
            "undramatic. She does not leap up or declare anything. She "
            "smiles into her book. Later she will rinse a pan without "
            "being asked, and it will feel like enough. Her heart beats "
            "normally. Her thoughts visit him the way birds visit a "
            "familiar tree - briefly, without fuss. This is love at low "
            "volume: steady, quiet, and doing the structural work of a "
            "decade. If you asked her in this moment whether she loves "
            "him, she would look surprised at the question. Of course. "
            "What else would this be.\n\n"
            "Snapshot two: high intensity. It is three in the morning. "
            "Dev has been apart from his partner for eleven days - the "
            "longest since they met - and the reunion is tomorrow. He "
            "cannot sleep. His heart is doing something irregular and "
            "wonderful; every song on the radio seems to be about them; "
            "he has rehearsed the airport hello seventeen times, and each "
            "rehearsal ends with him grinning at the ceiling. He feels "
            "simultaneously exhausted and more alive than he has in weeks. "
            "His thoughts do not visit; they have moved in, brought "
            "luggage, redecorated. This is love at full volume: loud, "
            "consuming, and completely sincere. If you asked him whether "
            "he loves her, he would laugh - the question is too small for "
            "what he feels.\n\n"
            "Same emotion. Different volumes. Mara's Thursday and Dev's "
            "3 a.m. are both love, the way a whisper and a shout are both "
            "a voice. The danger is only in the comparison: if Dev judges "
            "Mara's quiet Thursday as loveless, or Mara judges Dev's "
            "sleepless night as immature, each misses the truth. Love "
            "needs both registers - the shout to begin things and mark "
            "them as precious, the whisper to carry them across the "
            "years."
        ),
        "how_it_works": (
            "The two snapshots differ in arousal, salience, and "
            "uncertainty, not in the underlying appraisal. Mara's scene is "
            "low uncertainty and high security: the attachment system "
            "reports 'all is well,' so arousal stays near baseline and "
            "love expresses as calm maintenance. Dev's scene is high "
            "salience plus uncertainty (the reunion is near but not here): "
            "the reward system is in anticipation mode, dopamine is doing "
            "the wanting rather than the having, and arousal spikes. Same "
            "appraisal - 'this person is precious to me' - running through "
            "different arousal states. This is the two-factor logic of "
            "Schachter and Singer applied to love: the label is constant, "
            "the body volume changes the experience."
        ),
        "key_points": [
            "Low intensity: quiet fondness, steady maintenance, love doing structural work.",
            "High intensity: consuming arousal, moved-in thoughts, love marking preciousness.",
            "Neither is better; love needs both registers across a lifetime.",
            "The difference is arousal and uncertainty, not the underlying appraisal.",
            "Judging one volume by the other's standards is the classic error.",
        ],
        "requirements": [
            "Two concrete scenes - comparison needs lived detail, not abstractions.",
            "Recognition that security lowers volume and uncertainty raises it.",
            "Refusal to rank: whisper and shout are both the voice.",
            "Awareness that a life contains both snapshots at different times.",
        ],
        "standards": [
            "Schachter S., Singer J.E. Cognitive, social, and physiological determinants of emotional state. Psychological Review. 1962;69(5):379-399.",
            "Hatfield E., Rapson R.L. Love, Sex, and Intimacy. New York: HarperCollins; 1993.",
        ],
        "citations": [
            "Schachter S., Singer J.E. Cognitive, social, and physiological determinants of emotional state. Psychological Review. 1962;69(5):379-399.",
            "Hatfield E., Rapson R.L. Love, Sex, and Intimacy. New York: HarperCollins; 1993.",
            "Bowlby J. A Secure Base. New York: Basic Books; 1988.",
        ],
        "sig_lens": (
            "Through the Signature lens, the two snapshots are the same "
            "record viewed at different zoom - the thumbnail and the "
            "close-up, both complete, both true. His canon warns never to "
            "present a fraction as the whole, so the Signature editions "
            "insist Mara's Thursday and Dev's 3 a.m. are each the full "
            "file: the quiet maintenance love that carries decades, and "
            "the blazing reunion love that marks preciousness. The "
            "Signature originals teach the eye to recognize love in both "
            "outfits - because an archive that only recognizes the shout "
            "will miss most of the love in the world. Signature-made, "
            "never presented as authentic public record."
        ),
    },
    {
        "key": "love-joy-mix",
        "name": "Love Mixed with Joy: The Most Common Partner Emotion",
        "group": "feels",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Love rarely travels alone, and its most constant companion "
            "is joy. On Plutchik's wheel this is no accident: love itself "
            "is the dyad of joy plus trust, so joy is not just love's "
            "partner but one of its parents. To feel love mixed with joy "
            "is to feel love in its native weather - the two amplify each "
            "other the way sunlight amplifies a garden.\n\n"
            "From the inside, the blend feels like this: the warmth of "
            "love provides the ground, and joy provides the lift. You are "
            "glad they exist (joy) and you are devoted to their well-"
            "being (love), and the two statements keep trading places "
            "until they are one statement. Laughter comes easily and means "
            "more. Play feels like devotion and devotion feels like play. "
            "A couple cooking together badly and laughing about it; a "
            "parent swept up in a child's giggle fit; friends who cannot "
            "finish a sentence for laughing - these are love-joy in its "
            "element.\n\n"
            "Psychologically, the blend does real work. Barbara "
            "Fredrickson's broaden-and-build theory shows that positive "
            "emotions like joy broaden attention and build lasting "
            "resources - and when joy broadens inside a loving bond, the "
            "resources built are relational: shared jokes become shared "
            "history, play becomes trust, delight becomes the memory "
            "bank the relationship draws on in hard times. Couples "
            "research by John Gottman finds that the ratio of positive to "
            "negative moments predicts whether relationships last; "
            "love-joy moments are the deposits that keep the ratio "
            "healthy.\n\n"
            "The blend has a shadow worth knowing: when joy is absent for "
            "a long time, love can feel like duty - still real, but "
            "running on commitment without delight. That is usually a "
            "signal, not a verdict: the bond may need novelty, rest, or "
            "repair, the way a garden needs water. And in grief, love "
            "mixed with the memory of joy is what makes mourning so "
            "piercing - the joy proves what the love had, and the love "
            "keeps the joy from fading entirely."
        ),
        "how_it_works": (
            "Emotion blends work by co-activation: the neural and "
            "cognitive patterns of joy (approach, play, broadening) and "
            "love (salience of the beloved, care motivation, attachment "
            "calm) fire together, and the brain experiences one unified "
            "state rather than two side-by-side feelings. Because joy is "
            "already inside love's formula on Plutchik's wheel, the blend "
            "is especially stable - it is love with its own ingredient "
            "turned up. Fredrickson's mechanism explains the payoff: "
            "broadened attention during love-joy moments encodes richer "
            "shared memories, which become the relationship's resilience "
            "reserves."
        ),
        "key_points": [
            "Joy is love's most common partner - and one of its parent emotions on Plutchik's wheel.",
            "The blend: love provides the ground, joy provides the lift.",
            "Love-joy moments build the shared memory bank relationships draw on in hard times.",
            "Long absence of joy turns love dutiful - a signal to tend the bond, not a verdict.",
            "In grief, love mixed with remembered joy is what makes mourning pierce.",
        ],
        "requirements": [
            "Co-activation: joy and love firing together about the same person.",
            "Shared play and delight - the blend is fed by doing glad things together.",
            "Positive-to-negative ratio kept healthy, per Gottman's research.",
            "Room for the blend's shadow: duty-love and grieving love are still love.",
        ],
        "standards": [
            "Plutchik R. Emotion: A Psychoevolutionary Synthesis. New York: Harper & Row; 1980.",
            "Fredrickson B.L. The role of positive emotions in positive psychology. American Psychologist. 2001;56(3):218-226.",
            "Gottman J.M. The Seven Principles for Making Marriage Work. New York: Crown; 1999.",
        ],
        "citations": [
            "Plutchik R. Emotion: A Psychoevolutionary Synthesis. New York: Harper & Row; 1980.",
            "Fredrickson B.L. The role of positive emotions in positive psychology. American Psychologist. 2001;56(3):218-226.",
            "Gottman J.M. The Seven Principles for Making Marriage Work. New York: Crown; 1999.",
        ],
        "sig_lens": (
            "Through the Signature lens, love mixed with joy is the "
            "archive's golden hour - the entries written when the light "
            "was best. His canon says generators must use what they pull "
            "from other records and let it change the result, so the "
            "Signature editions let joy genuinely change love: the "
            "broadened attention, the richer memories, the resilience "
            "reserves are not decoration but the blend's real product. The "
            "Signature originals teach this mix first among mixes because "
            "it is love in its native weather - learn love-joy and you "
            "have the template for every other blend on the wheel. "
            "Signature-made, never presented as authentic public record."
        ),
    },
    {
        "key": "day-in-the-life",
        "name": "A Day in the Life: Love Running Through an Ordinary Day",
        "group": "feels",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "description": (
            "Love is most itself not in grand gestures but in an ordinary "
            "day. This vignette follows one day to show how the emotion "
            "runs underneath everything, mostly quiet, occasionally "
            "surfacing, always steering.\n\n"
            "6:40 a.m. Elena wakes before the alarm. Her first conscious "
            "act is small and automatic: she checks that her daughter's "
            "breathing, audible through the thin wall, is steady. It is. "
            "The relief is so routine she barely registers it as love, but "
            "it is love doing its oldest job - the attachment system "
            "running its morning safety check.\n\n"
            "7:30 a.m. She packs the lunch. She cuts the sandwich "
            "diagonally because her daughter once said triangles taste "
            "better, and Elena has never forgotten. This is love as "
            "memory: a trivial preference, carefully stored, faithfully "
            "honored. No one will ever praise her for the diagonal cut. "
            "That is the point.\n\n"
            "12:15 p.m. At work, between meetings, she texts her partner: "
            "'saw a dog in a raincoat, thought of you.' It takes eight "
            "seconds. It is not important. It is maintenance - the tiny "
            "deposit that keeps the bond's account in surplus, the kind "
            "Gottman's research counts by the thousands across a lasting "
            "relationship.\n\n"
            "5:50 p.m. Her mother calls, anxious about a doctor's "
            "appointment. Elena listens for twenty minutes, though she is "
            "tired, though dinner is burning. Patience with a worried "
            "parent is love with its sleeves rolled up.\n\n"
            "9:30 p.m. Daughter asleep, dishes done, she sits beside her "
            "partner on the couch. Neither speaks for a while. His hand "
            "finds her knee; her head finds his shoulder. No peak, no "
            "declaration - just two nervous systems agreeing, wordlessly, "
            "that this is home. The attachment researchers call this "
            "co-regulation: bodies keeping each other calm by proximity.\n\n"
            "11:00 p.m. In bed, she thinks about tomorrow - the dentist, "
            "the deadline, the rain - and underneath the planning, "
            "unbidden: gratitude. Not for anything dramatic. For the "
            "breathing through the wall, the raincoat dog, the hand on "
            "her knee. Love, it turns out, was the whole day. She just "
            "lived it instead of noticing it."
        ),
        "how_it_works": (
            "An ordinary day reveals love's three systems on their normal "
            "settings. The attachment system runs background safety checks "
            "(the breathing through the wall). The care system converts "
            "memory into service (the diagonal sandwich). The reward "
            "system fires in small doses for small contacts (the raincoat "
            "dog text). Co-regulation at day's end shows the physiology: "
            "proximity to a loved one measurably lowers cortisol and "
            "heart rate. None of this requires peak intensity. In fact, "
            "the day demonstrates the volume lesson from earlier in the "
            "ladder: most love runs quiet, and the quiet is where the "
            "structure gets built."
        ),
        "key_points": [
            "Love's natural habitat is the ordinary day, not the grand gesture.",
            "Attachment runs background safety checks all day long.",
            "Tiny deposits - texts, remembered preferences - keep bonds in surplus.",
            "Co-regulation: loved ones' bodies keep each other calm by proximity.",
            "Gratitude at day's end is love becoming conscious of itself.",
        ],
        "requirements": [
            "A full day's arc - love must be shown across time, not in one scene.",
            "Multiple loves at once: child, partner, parent - love is plural.",
            "Small concrete details: the diagonal cut, the raincoat dog.",
            "The quiet thesis: she lived it instead of noticing it.",
        ],
        "standards": [
            "Bowlby J. A Secure Base. New York: Basic Books; 1988.",
            "Gottman J.M. The Seven Principles for Making Marriage Work. New York: Crown; 1999.",
        ],
        "citations": [
            "Bowlby J. A Secure Base. New York: Basic Books; 1988.",
            "Gottman J.M. The Seven Principles for Making Marriage Work. New York: Crown; 1999.",
            "Fredrickson B.L. The role of positive emotions in positive psychology. American Psychologist. 2001;56(3):218-226.",
        ],
        "sig_lens": (
            "Through the Signature lens, the ordinary day is the archive "
            "at work - no ceremony, just records being written: a safety "
            "check logged at dawn, a preference remembered at breakfast, "
            "a deposit made at noon, patience filed in the evening. His "
            "canon says every record is the full file, so the Signature "
            "editions refuse the highlight reel and file the whole day - "
            "because the diagonal sandwich nobody praises is as much a "
            "love record as any declaration. The Signature originals "
            "teach that love's grandeur is an emergent property of "
            "thousands of unpraised entries. Signature-made, never "
            "presented as authentic public record."
        ),
    },
]

ENTRIES += [
    {
        "key": "body-signals",
        "name": "The Body of Love: Heart, Breath, Muscles, Stomach, Skin, and Energy",
        "group": "body",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Love is felt in the body before it is understood in the "
            "mind. This record maps the physical signature of love, "
            "system by system - the felt sense that tells a person, "
            "without words, that this is love.\n\n"
            "Heart: the most famous signal. In new or intense love the "
            "heart races, pounds, or seems to skip when the beloved "
            "appears, calls, or is even thought of. Adrenaline and "
            "norepinephrine drive this - the same arousal behind "
            "excitement. In settled love the heart does the opposite: "
            "near the beloved, heart rate steadies and variability "
            "improves, the physiological signature of safety.\n\n"
            "Breath: aroused love quickens and shallows the breath; calm "
            "love deepens it. Lovers unconsciously synchronize breathing "
            "when close - one of the measurable forms of co-regulation. "
            "The 'sigh of contentment' beside a loved one is literally "
            "the respiratory system standing down.\n\n"
            "Muscles: love relaxes the defensive musculature. Shoulders "
            "drop, the jaw unclenches, the hands open. At high intensity "
            "there can be trembling - shaky hands before a first date, "
            "wobbly knees at a reunion - which is adrenaline, not fear. "
            "Touch between lovers measurably reduces muscle tension within "
            "seconds.\n\n"
            "Stomach: the famous butterflies. The gut has its own dense "
            "nervous system, and arousal diverts blood and attention in "
            "ways felt as fluttering, tightness, or sudden appetite loss "
            "in new love - and as warm settled comfort in established "
            "love. The gut feeling about a person is partly this: the "
            "enteric system reporting arousal before the mind has words.\n\n"
            "Skin: love flushes the skin - blushing at a compliment, "
            "warmth spreading across the face and chest. Pupils dilate "
            "when looking at the beloved, an involuntary signal of "
            "interest that other people unconsciously read. Touch becomes "
            "electric: skin sensitivity rises, and even casual contact "
            "carries charge.\n\n"
            "Energy: love is energizing at every volume. New love brings "
            "the famous sleepless energy - needing less rest because "
            "arousal overrides fatigue. Settled love brings a different "
            "energy: the calm stamina of co-regulation, the sense of "
            "having more to give because the baseline is safe. Both are "
            "real; they are the same system at different volumes."
        ),
        "how_it_works": (
            "The body's love signature runs through the autonomic nervous "
            "system. Sympathetic activation (adrenaline, norepinephrine) "
            "produces the racing heart, butterflies, and trembling of "
            "aroused love. Parasympathetic dominance - especially the "
            "ventral vagal pathway described in Stephen Porges's "
            "polyvagal theory - produces the steady heart, deep breath, "
            "and relaxed muscles of safe love. Oxytocin, released during "
            "touch, eye contact, and warmth, damps the threat system and "
            "promotes approach. The same beloved can trigger either "
            "branch: novelty and uncertainty pull sympathetic, safety and "
            "familiarity pull parasympathetic - which is exactly why new "
            "love races and old love rests."
        ),
        "key_points": [
            "Heart races in new love, steadies in settled love - both are the signature.",
            "Breath quickens with arousal, deepens with safety; lovers synchronize breathing.",
            "Muscles drop their defenses; trembling at intensity is adrenaline, not fear.",
            "Butterflies are the gut's nervous system reporting arousal.",
            "Blushing, pupil dilation, and electric touch are involuntary interest signals.",
            "Love energizes at every volume: sleepless spark or calm stamina.",
        ],
        "requirements": [
            "System-by-system mapping: heart, breath, muscles, stomach, skin, energy.",
            "Both volumes covered - aroused and settled bodies differ completely.",
            "Mechanisms named: sympathetic, parasympathetic, oxytocin, polyvagal.",
            "Normalizing: none of these signals are dangerous in themselves.",
        ],
        "standards": [
            "Porges S.W. The Polyvagal Theory. New York: W.W. Norton; 2011.",
            "Fisher H.E., Aron A., Brown L.L. Romantic love: a mammalian brain system for mate choice. Philosophical Transactions of the Royal Society B. 2006;361(1476):2173-2186.",
        ],
        "citations": [
            "Porges S.W. The Polyvagal Theory. New York: W.W. Norton; 2011.",
            "Fisher H.E., Aron A., Brown L.L. Romantic love: a mammalian brain system for mate choice. Philosophical Transactions of the Royal Society B. 2006;361(1476):2173-2186.",
            "Schachter S., Singer J.E. Cognitive, social, and physiological determinants of emotional state. Psychological Review. 1962;69(5):379-399.",
        ],
        "sig_lens": (
            "Through the Signature lens, the body is the archive's first "
            "instrument panel - six gauges reading love before the mind "
            "files the report. His canon says every record is the full "
            "file, so the Signature editions read all six dials: the "
            "racing heart and the resting heart are the same gauge at "
            "different times of day. The Signature originals teach the "
            "body as the honest clerk of love - it logs arousal and "
            "safety without editing, and learning to read its handwriting "
            "is learning to read love itself. Signature-made, never "
            "presented as authentic public record."
        ),
    },
    {
        "key": "posture-movement",
        "name": "How the Body Carries Love: Posture and Movement",
        "group": "body",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Long before a person says 'I love you,' the body has been "
            "saying it for weeks - in posture, in movement, in the "
            "geometry of how two bodies arrange themselves in space. This "
            "record teaches the movement signature of love.\n\n"
            "Posture opens. Love is an approach emotion, and approach "
            "shows in the torso: chest open rather than guarded, shoulders "
            "back and down, arms uncrossed, the body literally making "
            "room. Researchers coding nonverbal behavior find that "
            "open-torso postures reliably predict liking and affiliation "
            "across cultures. The opposite - crossed arms, turned-away "
            "torso, barriers of bags and elbows - reads as distance in "
            "every culture studied.\n\n"
            "The body orients. Lovers point at each other: feet, knees, "
            "shoulders, and face all aim toward the beloved like "
            "compass needles. In groups, you can spot the bond by the "
            "geometry - two people whose bodies form a closed circle, "
            "facing inward, while everyone else faces the room. This "
            "orientation is mostly unconscious; people are often surprised "
            "when it is pointed out.\n\n"
            "Distance shrinks. Edward Hall's proxemics research mapped "
            "human distance zones, and love lives in the innermost one: "
            "intimate distance, under eighteen inches, the zone reserved "
            "for the beloved. Lovers close distance reflexively - leaning "
            "in across tables, finding reasons to be near, touching in "
            "passing. Touch itself becomes a language: the hand on the "
            "back while walking, the foot finding the foot under the "
            "table, the head on the shoulder.\n\n"
            "Movement synchronizes. Couples in love unconsciously match "
            "each other's rhythms - walking in step, mirroring gestures, "
            "nodding together. Behavioral synchrony research shows this "
            "matching both signals and builds rapport: moving together "
            "makes people feel together. Watch an old couple cross a "
            "street: the matched pace, developed over decades, is love "
            "written in footsteps.\n\n"
            "Energy leans forward. The loved one's entrance changes a "
            "room's physics: the lover sits up, turns, brightens, moves "
            "toward. Boredom postures - slumping, stillness, gaze drift - "
            "evaporate on arrival. If you want to know who someone loves "
            "in a crowded room, watch who they physically brighten for."
        ),
        "how_it_works": (
            "Posture and movement in love run through approach circuitry. "
            "The brain's approach system, when activated by the beloved's "
            "salience, releases postural guarding and biases movement "
            "toward the target - the same system that moves animals toward "
            "food and water, now pointed at a person. Synchrony emerges "
            "from the mirror system and from predictive timing: brains "
            "that know each other well predict each other's movements and "
            "align with them. Proxemics reflect threat assessment: the "
            "beloved is classified as safe, so the intimate zone opens. "
            "All of it is fast, automatic, and hard to fake - which is "
            "why body language is love's most honest channel."
        ),
        "key_points": [
            "Posture opens: uncrossed arms, open torso, room made for the other.",
            "Bodies orient like compass needles - feet, knees, face all aim at the beloved.",
            "Distance shrinks into the intimate zone; touch becomes a language.",
            "Movement synchronizes: matched pace and mirrored gesture signal and build rapport.",
            "The brighten-on-arrival effect reveals love in a crowded room.",
        ],
        "requirements": [
            "Approach circuitry: love moves bodies toward, never away.",
            "Cross-cultural basics: open torso and close distance read as liking everywhere.",
            "Synchrony as both signal and builder of the bond.",
            "Reading geometry: closed circles in groups mark the bond.",
        ],
        "standards": [
            "Hall E.T. The Hidden Dimension. New York: Doubleday; 1966.",
            "Argyle M. Bodily Communication. 2nd ed. London: Methuen; 1988.",
        ],
        "citations": [
            "Hall E.T. The Hidden Dimension. New York: Doubleday; 1966.",
            "Argyle M. Bodily Communication. 2nd ed. London: Methuen; 1988.",
            "Chartrand T.L., Bargh J.A. The chameleon effect: the perception-behavior link and social interaction. Journal of Personality and Social Psychology. 1999;76(6):893-910.",
        ],
        "sig_lens": (
            "Through the Signature lens, posture is the archive's cover "
            "art - the body's way of shelving the beloved in the most "
            "honored position. His canon says records render as human-"
            "readable sentences, so the Signature editions describe the "
            "geometry plainly: open torsos, compass-needle feet, the "
            "closed circle of two, the matched footsteps of decades. The "
            "Signature originals treat movement as love's unedited draft - "
            "written before the mind decides what to say, and therefore "
            "the truest copy in the file. Signature-made, never presented "
            "as authentic public record."
        ),
    },
    {
        "key": "sleep-appetite-energy",
        "name": "Love, Sleep, Appetite, and Energy",
        "group": "body",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Love rearranges the body's maintenance systems - sleep, "
            "appetite, and energy - and the rearrangement looks completely "
            "different at different volumes. This record maps the "
            "changes and explains why they are normal.\n\n"
            "Sleep: new and intense love disrupts sleep. Lovers report "
            "trouble falling asleep, waking to think of the beloved, and "
            "needing less sleep without feeling tired - arousal "
            "overriding fatigue, the same mechanism behind the famous "
            "'too excited to sleep' effect. Researchers have even found "
            "that intense romantic love can resemble the neurochemistry of "
            "obsessive states in its early phase, which helps explain the "
            "intrusive nighttime thinking. In settled love the pattern "
            "reverses: sleeping beside a trusted partner improves sleep "
            "quality, lowers nighttime cortisol, and synchronizes sleep "
            "architecture. The safest sleep most adults ever get is next "
            "to someone they love.\n\n"
            "Appetite: the butterflies have a cost - arousal suppresses "
            "hunger. New lovers famously 'live on love,' skipping meals "
            "without noticing. The mechanism is straightforward: "
            "sympathetic arousal diverts resources from digestion. As "
            "love settles, appetite normalizes and often the pattern "
            "flips: shared meals become a love language, and couples "
            "famously gain a little weight together - the 'love weight' "
            "researchers attribute to relaxed vigilance, shared "
            "indulgence, and the end of mating-market self-monitoring.\n\n"
            "Energy: love is a stimulant and a sedative in one. New love "
            "brings wired energy - long days, big plans, the sense of "
            "running on a full battery. Settled love brings calm energy - "
            "not the buzz of arousal but the deep stamina of a regulated "
            "nervous system, the energy that comes from not spending "
            "resources on vigilance. Both are real energy; they are just "
            "different fuel blends. The crash people fear - 'what if the "
            "energy goes away' - is usually just the stimulant blend "
            "giving way to the sedative blend, which is an upgrade, not a "
            "loss."
        ),
        "how_it_works": (
            "All three systems answer to the same arousal-safety dial. "
            "High arousal (new love) activates the sympathetic branch: "
            "sleep drive suppressed, digestion deprioritized, energy "
            "mobilized. High safety (settled love) activates the "
            "parasympathetic branch: sleep deepens, digestion resumes, "
            "energy goes to maintenance and growth rather than "
            "mobilization. Oxytocin and endogenous opioids, released in "
            "sustained warm contact, directly promote sleep onset and "
            "digestive function - which is why the beloved's presence is "
            "literally soporific in the best way. The transitions feel "
            "dramatic because the dial swings wide; the underlying "
            "physiology is orderly."
        ),
        "key_points": [
            "New love disrupts sleep; settled love beside a trusted partner deepens it.",
            "Arousal suppresses appetite; settled love often restores it with interest.",
            "Love is both stimulant (new) and sedative (settled) - different fuel blends.",
            "The 'energy crash' is usually the stimulant blend yielding to the calmer blend.",
            "All changes trace to one dial: arousal versus safety.",
        ],
        "requirements": [
            "Both volumes mapped - new and settled love differ completely here.",
            "Mechanisms: sympathetic suppression, parasympathetic restoration, oxytocin.",
            "Normalizing: these shifts are healthy physiology, not illness.",
            "The upgrade framing: calm stamina replaces wired buzz by design.",
        ],
        "standards": [
            "Marazziti D., Akiskal H.S., Rossi A., Cassano G.B. Alteration of the platelet serotonin transporter in romantic love. Psychological Medicine. 1999;29(3):741-745.",
            "Bowlby J. A Secure Base. New York: Basic Books; 1988.",
        ],
        "citations": [
            "Marazziti D., Akiskal H.S., Rossi A., Cassano G.B. Alteration of the platelet serotonin transporter in romantic love. Psychological Medicine. 1999;29(3):741-745.",
            "Bowlby J. A Secure Base. New York: Basic Books; 1988.",
            "Porges S.W. The Polyvagal Theory. New York: W.W. Norton; 2011.",
        ],
        "sig_lens": (
            "Through the Signature lens, sleep, appetite, and energy are "
            "the archive's maintenance logs - proof the system is running. "
            "His canon says every record is the full file, so the "
            "Signature editions log both shifts honestly: the sleepless "
            "wired nights of new love and the deep synchronized sleep of "
            "settled love are both correct entries, not a malfunction "
            "followed by a fix. The Signature originals teach the dial, "
            "not the panic: when the stimulant blend yields to the calm "
            "blend, the archive marks it 'upgrade complete.' Signature-"
            "made, never presented as authentic public record."
        ),
    },
    {
        "key": "body-differences",
        "name": "No Two Bodies React Alike: How Love Signals Differ",
        "group": "body",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Everything in the body records so far is true in general and "
            "approximate in particular. No two bodies react identically to "
            "love - and misunderstanding this causes real confusion, when "
            "one person's racing heart meets another's calm steadiness and "
            "each doubts the other's love. This record is about the "
            "differences.\n\n"
            "Temperament sets the baseline. A naturally high-arousal "
            "person feels love loudly: bigger heart-rate swings, more "
            "visible flushing, stronger butterflies. A naturally calm "
            "person feels the same love quietly: a warm steadiness, a "
            "deep breath, a settled ease. Researchers on affective style "
            "show these baselines are substantially constitutional - "
            "partly genetic, stable across decades. The quiet lover is "
            "not feeling less; the instrument is calibrated differently.\n\n"
            "Attachment history tunes the signals. People with secure "
            "attachment histories tend toward the calm signature: steady "
            "heart, easy sleep beside the partner, appetite undisturbed. "
            "People with anxious attachment lean toward the aroused "
            "signature even in safe relationships: racing heart, "
            "stomach knots, sleep broken by worry - not because the love "
            "is less real but because the threat system is tuned "
            "louder. Attachment researchers emphasize that these are "
            "learned tunings, and they can be retuned by sustained safe "
            "experience.\n\n"
            "Culture and family write the display rules. Some families "
            "and cultures express love's body loudly - effusive touch, "
            "visible emotion; others prize restraint, and love shows in "
            "steadiness, service, and presence. Neither is more genuine. "
            "A person raised in a restrained tradition may show love by "
            "reliably fixing what is broken; a person raised expressively "
            "may show it in effusive embrace. The signal differs; the "
            "appraisal underneath - 'you are precious to me' - is the "
            "same.\n\n"
            "Age and body condition matter too. Young bodies amplify: "
            "more adrenaline, bigger swings. Older bodies soften the "
            "signal: the same devotion with a steadier pulse. Illness, "
            "medication, exhaustion, and hormonal shifts all retune the "
            "instrument temporarily. The practical rule: read love across "
            "time and across channels - words, actions, consistency - "
            "never from a single bodily signal in a single moment."
        ),
        "how_it_works": (
            "Individual differences in love's body signature come from "
            "three layers. The constitutional layer: genetic and "
            "temperamental differences in autonomic reactivity - some "
            "nervous systems are simply louder. The learned layer: "
            "attachment experiences calibrate threat and safety "
            "thresholds, setting how much arousal love triggers. The "
            "situational layer: age, health, fatigue, and substances "
            "shift the baseline day to day. The appraisal - the "
            "psychological core of love - is shared across all three "
            "layers; only its bodily translation varies. This is why "
            "psychologists distinguish the emotion from its expression: "
            "the feeling can be identical while the readout differs."
        ),
        "key_points": [
            "Temperament sets the baseline: loud bodies and quiet bodies feel the same love.",
            "Attachment history tunes the signal; anxious tuning is learned, not a verdict.",
            "Culture and family write the display rules - restraint can be as genuine as effusion.",
            "Age, health, and fatigue retune the instrument temporarily.",
            "Read love across time and channels, never from one signal in one moment.",
        ],
        "requirements": [
            "Three layers: constitutional, learned, situational.",
            "Normalizing differences - quiet is not less.",
            "Attachment tuning presented as retunable, not fixed.",
            "The practical rule: multi-channel, multi-moment reading.",
        ],
        "standards": [
            "Bowlby J. A Secure Base. New York: Basic Books; 1988.",
            "Davidson R.J. Affective style and affective disorders. Cognition and Emotion. 1998;12(3):307-330.",
        ],
        "citations": [
            "Bowlby J. A Secure Base. New York: Basic Books; 1988.",
            "Davidson R.J. Affective style and affective disorders. Cognition and Emotion. 1998;12(3):307-330.",
            "Mikulincer M., Shaver P.R. Attachment in Adulthood. 2nd ed. New York: Guilford Press; 2016.",
        ],
        "sig_lens": (
            "Through the Signature lens, different bodies are different "
            "editions of the same record - same text, different typeface. "
            "His canon says never present a fraction as the whole, so the "
            "Signature editions refuse the single-signal verdict: one "
            "racing heart or one calm pulse is a page, not the file. The "
            "Signature originals teach the full read - words, actions, "
            "consistency across time - because an archive that judges love "
            "by one instrument reading will misfile half its collection. "
            "Signature-made, never presented as authentic public record."
        ),
    },
    {
        "key": "face-of-love",
        "name": "The Face of Love: Eyes, Brows, Mouth, and Micro-Signs",
        "group": "face",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The face is love's most readable page. Unlike the body's "
            "internal signals, the face broadcasts - and humans are "
            "exquisitely tuned receivers. This record teaches the facial "
            "signature of love, feature by feature.\n\n"
            "Eyes: the centerpiece. The loving gaze is soft, sustained, "
            "and slightly widened - researchers call it the 'affiliative "
            "gaze.' Pupils dilate involuntarily when looking at the "
            "beloved, a signal of interest and arousal that observers "
            "unconsciously register as warmth. Eye contact lasts longer: "
            "studies of couples find that mutual gaze duration predicts "
            "reported love better than almost any other single behavior. "
            "The gaze also follows - lovers track the beloved across "
            "rooms, the eyes doing what the compass-needle feet do. And "
            "there is the famous 'looking at them when they are not "
            "looking' - the soft, unguarded stare of pure fondness, "
            "quickly redirected with a smile if caught.\n\n"
            "Brows: love raises the brows - briefly, slightly, "
            "involuntarily - on first sight of the beloved. This "
            "'eyebrow flash,' documented across cultures by ethologist "
            "Irenaus Eibl-Eibesfeldt, is a universal recognition-and-"
            "delight signal lasting about a fifth of a second. At rest "
            "with the beloved, the brow smooths: the vertical worry "
            "lines between the brows, the corrugator's signature, "
            "release. A smooth brow beside someone is the face saying "
            "'no threat here.'\n\n"
            "Mouth: the genuine smile - the Duchenne smile, engaging "
            "the eye muscles (orbicularis oculi) as well as the mouth - "
            "is love's default expression. It is softer than the "
            "performance smile: smaller, longer-lasting, often "
            "asymmetric, frequently accompanied by a slight head tilt. "
            "Lovers also do the 'lip press of tenderness' - lips "
            "pressing together briefly when moved - and the unconscious "
            "lip-lick or lip-part when the beloved is near, ancient "
            "signals of interest.\n\n"
            "Micro-signs: the tells that leak around the edges. The "
            "nostrils flare slightly with arousal. The head tilts - "
            "exposing the neck, the body's most vulnerable area, in a "
            "gesture of trust no one teaches and everyone understands. "
            "The whole face 'lights up' on the beloved's arrival: a "
            "rapid, involuntary brightening - eyes widening, smile "
            "breaking, color rising - that takes under a second and is "
            "nearly impossible to fake. Actors study it for years; "
            "lovers do it without trying."
        ),
        "how_it_works": (
            "The face of love is driven by two systems: the affiliative "
            "system (approach, warmth, bonding) and the arousal system. "
            "The affiliative system, rich in oxytocin and endogenous "
            "opioids during warm contact, relaxes the corrugator (frown) "
            "muscles and engages the zygomatic (smile) and orbicularis "
            "oculi muscles - the Duchenne pattern. The arousal system "
            "dilates pupils via the sympathetic branch and flushes skin "
            "via vasodilation. The eyebrow flash is a brainstem-level "
            "recognition reflex, too fast for conscious control - which "
            "is why it is trusted as a signal. Together they form a "
            "compound display that is easy to read and hard to counterfeit."
        ),
        "key_points": [
            "Eyes: soft sustained gaze, dilated pupils, longer mutual gaze, fond tracking.",
            "Brows: the universal eyebrow flash on sighting; smooth brow at rest means safety.",
            "Mouth: the Duchenne smile - softer, longer, often tilted - is love's default.",
            "Micro-signs: neck-exposing head tilt, nostril flare, the under-a-second light-up.",
            "The whole display is easy to read and hard to fake.",
        ],
        "requirements": [
            "Feature-by-feature mapping: eyes, brows, mouth, micro-signs.",
            "Cross-cultural universals noted (eyebrow flash).",
            "Duchenne vs performance smile distinguished.",
            "Honesty about readability: the face broadcasts; receivers are tuned.",
        ],
        "standards": [
            "Ekman P., Friesen W.V. Facial Action Coding System. Palo Alto: Consulting Psychologists Press; 1978.",
            "Eibl-Eibesfeldt I. Human Ethology. New York: Aldine de Gruyter; 1989.",
            "Duchenne G.B. The Mechanism of Human Physiognomy. 1862. (Trans. Cuthbertson R.A. Cambridge University Press; 1990.)",
        ],
        "citations": [
            "Ekman P., Friesen W.V. Facial Action Coding System. Palo Alto: Consulting Psychologists Press; 1978.",
            "Eibl-Eibesfeldt I. Human Ethology. New York: Aldine de Gruyter; 1989.",
            "Kleinke C.L. Gaze and eye contact: a research review. Psychological Bulletin. 1986;100(1):78-100.",
        ],
        "sig_lens": (
            "Through the Signature lens, the face is the record's "
            "illustrated plate - the full-color frontispiece the archive "
            "opens to. His canon demands human-readable rendering, so the "
            "Signature editions paint the face in sentences: the soft "
            "gaze, the fifth-of-a-second brow flash, the true smile that "
            "reaches the eyes, the neck bared in trust. The Signature "
            "originals treat the under-a-second light-up as the archive's "
            "authenticity seal - no one forges it, everyone recognizes it. "
            "Signature-made, never presented as authentic public record."
        ),
    },
    {
        "key": "expression-intensity",
        "name": "How the Expression of Love Changes with Intensity",
        "group": "face",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "The face of love is not one face - it is a dial. As "
            "intensity rises, the expression changes in predictable ways, "
            "and knowing the dial prevents the two classic mistakes: "
            "reading calm as cold, and reading blaze as the only true "
            "fire.\n\n"
            "At low intensity, the expression is subtle to the point of "
            "invisibility to strangers. The signs: a softening around "
            "the eyes when the person is mentioned, a small private smile "
            "that appears and vanishes, a relaxed jaw and smooth brow in "
            "their presence. Intimates read it instantly; outsiders see "
            "nothing. This is the face of the Thursday-evening love from "
            "the earlier snapshot - undramatic, unmistakable to those who "
            "know the reader.\n\n"
            "At moderate intensity, the expression becomes public. The "
            "Duchenne smile arrives readily and stays. Eye contact "
            "lengthens visibly. The head tilt appears. The whole face "
            "participates: color rises, the gaze tracks, the 'light-up' "
            "on arrival is obvious across a room. This is the face people "
            "mean when they say 'you can just tell' - and they are "
            "usually right.\n\n"
            "At high intensity, the face can paradoxically go strange. "
            "Overwhelming feeling sometimes blanks the expression - the "
            "'stunned' look of limerence, eyes wide and unfocused, mouth "
            "slightly open, as if the system is buffering. Or it "
            "overflows: tears of joy, laughter that will not stop, the "
            "face doing three things at once. High-intensity love can "
            "also flip into its neighbors on the wheel - the fierce "
            "protective glare (love plus anger at a threat), the "
            "anguished face of separation (love plus distress). These "
            "are still love's face; they are love at volumes where the "
            "expression saturates.\n\n"
            "The practical skill is calibration: match the reading to "
            "the volume. Expecting the blaze-face in a calm marriage is "
            "like expecting shouting in a library - the quiet is not "
            "absence, it is appropriateness. And when the blaze-face "
            "appears, recognize it as arousal's signature, not "
            "necessarily as a measure of the love's depth or durability."
        ),
        "how_it_works": (
            "Facial intensity follows the same arousal dial as the body. "
            "Low arousal produces low-amplitude, sustained displays - "
            "micro-expressions and resting configurations. Moderate "
            "arousal recruits the full voluntary-plus-involuntary smile "
            "and gaze apparatus. Very high arousal can produce "
            "expression 'clipping': the facial motor system, flooded, "
            "either freezes (the stunned blank) or overflows (tears, "
            "uncontrolled laughter), and neighboring emotion programs "
            "bleed in. This is a general property of intense emotion, "
            "not specific to love - grief, rage, and ecstasy all clip "
            "the same way - which is why the most intense faces are the "
            "hardest to read precisely."
        ),
        "key_points": [
            "Low intensity: subtle, private - eye-softening, small vanishing smiles.",
            "Moderate intensity: public and readable - the 'you can just tell' face.",
            "High intensity: paradoxical - stunned blank, overflow, or neighbor-emotion bleed.",
            "Calibrate the reading to the volume; quiet is appropriateness, not absence.",
            "Blaze-face marks arousal, not necessarily depth or durability.",
        ],
        "requirements": [
            "Three volumes mapped on the face dial.",
            "The paradox of high intensity: clipping and bleed explained.",
            "Calibration as the practical skill.",
            "Link back to the volume lesson: same emotion, different dial.",
        ],
        "standards": [
            "Ekman P., Friesen W.V. Facial Action Coding System. Palo Alto: Consulting Psychologists Press; 1978.",
            "Tennov D. Love and Limerence. New York: Stein and Day; 1979.",
        ],
        "citations": [
            "Ekman P., Friesen W.V. Facial Action Coding System. Palo Alto: Consulting Psychologists Press; 1978.",
            "Tennov D. Love and Limerence. New York: Stein and Day; 1979.",
            "Schachter S., Singer J.E. Cognitive, social, and physiological determinants of emotional state. Psychological Review. 1962;69(5):379-399.",
        ],
        "sig_lens": (
            "Through the Signature lens, the face's dial is the archive's "
            "volume knob rendered in flesh - whisper, conversation, "
            "shout. His canon says never mistake the fraction for the "
            "whole, so the Signature editions teach all three faces as "
            "complete: the private softening, the public glow, the "
            "saturated blaze. The Signature originals warn especially "
            "against the library-shouting error - demanding the blaze "
            "in a calm marriage - because misreading the dial has "
            "misfiled more loves than any other single mistake. "
            "Signature-made, never presented as authentic public record."
        ),
    },
    {
        "key": "hiding-faking",
        "name": "Hiding or Faking Love: What Leaks Through",
        "group": "face",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "People hide love and fake love for many ordinary reasons - "
            "workplace rules, unrequited situations, cultural restraint, "
            "the early fragile stage - and the face is where the "
            "concealment usually fails. This record teaches what leaks, "
            "and why, as descriptive knowledge.\n\n"
            "Hiding love means suppressing the display while feeling the "
            "emotion. What leaks: the eyes first. Gaze duration is the "
            "hardest channel to control - the hider looks away "
            "deliberately, but the eyes keep returning, and the returns "
            "are longer than neutral looking would be. Pupil dilation "
            "cannot be suppressed at all; in good light, the widened "
            "pupils tell the story the mouth refuses to. The light-up "
            "on arrival leaks too: it fires in under a second, before "
            "the suppression system engages - a flash of the true face "
            "that the neutral mask then covers. Micro-expressions of "
            "fondness - the half-second softening - escape during "
            "unguarded moments: laughter, surprise, fatigue. And the "
            "body keeps its own counsel: orientation, proximity, and "
            "the brightening posture leak around the facial mask.\n\n"
            "Faking love means displaying without feeling it. What leaks: "
            "the smile does not reach the eyes - the performance smile "
            "moves the mouth but not the orbicularis oculi, and "
            "experienced observers feel the difference even when they "
            "cannot name it. Timing is off: real expressions of fondness "
            "rise and fall smoothly; performed ones snap on and off, "
            "held a beat too long, released too abruptly. The eyes give "
            "it away differently than in hiding: the gaze is managed "
            "rather than drawn - it checks, it does not linger; it "
            "performs attention without the softening. And crucially, "
            "the body does not corroborate: the torso stays guarded, "
            "distance is maintained, touch is avoided or mechanical. "
            "The face says love; everything else files a dissent.\n\n"
            "The honest use of this knowledge is self-knowledge and "
            "fiction, not surveillance: understanding your own leaks "
            "when you are trying to be discreet, and writing believable "
            "characters. One caution from the research: people "
            "consistently overestimate their lie-detection ability, and "
            "using leak-reading to accuse real people causes real harm. "
            "The leaks are clues for understanding, not evidence for "
            "confrontation."
        ),
        "how_it_works": (
            "Leakage follows the neuroscience of voluntary versus "
            "involuntary control. The facial muscles have dual "
            "innervation: voluntary (cortical) pathways can pose a "
            "smile, but involuntary (subcortical) pathways drive the "
            "genuine expression - and the two pathways innervate slightly "
            "different muscle sets. The Duchenne marker, the eyebrow "
            "flash, pupil dilation, and the sub-second light-up are all "
            "dominated by the involuntary pathway, which is why they "
            "leak through suppression and stay absent in performance. "
            "Ekman's leakage hierarchy formalizes this: the face leaks "
            "most, the body leaks least controllably of all - which is "
            "why the body's dissent is the most reliable channel."
        ),
        "key_points": [
            "Hidden love leaks through the eyes: returning gaze, undilatable pupils, the sub-second light-up.",
            "Faked love leaks through the smile: mouth without eyes, snapped timing, uncorroborating body.",
            "The body is the most honest channel - it dissents when the face performs.",
            "Use this for self-knowledge and storytelling, never for accusing real people.",
            "People overestimate lie-detection; leaks are clues, not evidence.",
        ],
        "requirements": [
            "Both directions covered: hiding the felt, faking the unfelt.",
            "Specific leaks named per channel: eyes, pupils, timing, body.",
            "The dual-innervation mechanism explained.",
            "Ethical boundary stated: descriptive knowledge, not a weapon.",
        ],
        "standards": [
            "Ekman P., Friesen W.V. Unmasking the Face. Englewood Cliffs: Prentice-Hall; 1975.",
            "Ekman P. Telling Lies. New York: W.W. Norton; 1985.",
        ],
        "citations": [
            "Ekman P., Friesen W.V. Unmasking the Face. Englewood Cliffs: Prentice-Hall; 1975.",
            "Ekman P. Telling Lies. New York: W.W. Norton; 1985.",
            "Eibl-Eibesfeldt I. Human Ethology. New York: Aldine de Gruyter; 1989.",
        ],
        "sig_lens": (
            "Through the Signature lens, leaks are the archive's "
            "tamper-evident seals - the entries that cannot be edited "
            "even by their author. His canon says the full file is what "
            "counts, so the Signature editions read the whole file when "
            "the cover page is forged: the mouth may perform, but the "
            "eyes, the pupils, and the body's dissent keep the true "
            "record. The Signature originals set the boundary as part "
            "of the teaching: this knowledge is for understanding and "
            "for honest storytelling, never for accusing a real person. "
            "Signature-made, never presented as authentic public record."
        ),
    },
    {
        "key": "expression-gallery",
        "name": "Drawing and Playing Love: Expression Notes for Artists and Actors",
        "group": "face",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "This record translates the face of love into working notes "
            "for the people who must depict it: illustrators, animators, "
            "actors, directors. Descriptive, practical, and grounded in "
            "the anatomy from the previous records.\n\n"
            "For the artist: draw the eyes first. The loving gaze is "
            "drawn with soft focus - slightly widened eyes, relaxed lids, "
            "the iris fully visible, a catchlight that suggests "
            "attention. Pupils slightly large. The gaze direction is "
            "everything: aimed at the beloved, or just leaving them with "
            "the soft unfocused look of fond memory. Brows: raised a "
            "touch at the inner corners for tenderness, or the brief "
            "flash of delight - never the lowered, drawn-together brow "
            "of anger or the raised-outer brow of fear. The mouth: the "
            "Duchenne smile in repose is small - upturned corners, "
            "relaxed lips, the faintest crinkling at the outer eyes. "
            "Avoid the wide toothy grin; that is joy performing, not love "
            "resting. Head: the tilt, five to fifteen degrees, exposing "
            "the neck slightly. Composition: love is drawn in proximity - "
            "faces near, orientations closed, the negative space between "
            "two figures small and warm.\n\n"
            "For the actor: play the arrival, not the declaration. The "
            "most truthful love beat is the half-second before the "
            "character speaks - the light-up, the breath caught, the "
            "stillness. Let the eyes arrive first and the body follow a "
            "beat later; that lag is the signature of genuine feeling "
            "versus performed. In quiet love scenes, do less: the "
            "audience reads the softening around the eyes and the "
            "unconscious lean-in more truthfully than any speech. For "
            "hidden love, play the suppression and let the leaks do the "
            "work - the returning glance, the too-long look away, the "
            "hand that starts to reach and becomes a hair-touch. For "
            "intense love, remember the clipping: overwhelming feeling "
            "often stills the face rather than animating it - play the "
            "held breath, the wide unfocused eyes, the face that cannot "
            "decide what to do.\n\n"
            "For both: the common failure is playing the idea of love "
            "instead of its mechanics. Sighing, hand-on-heart, gazing "
            "skyward - these are symbols of love, and audiences read "
            "symbols as acting. The mechanics - gaze duration, brow "
            "flash, Duchenne engagement, orientation, proximity, "
            "synchrony - are what real faces do, and depicting the "
            "mechanics is what makes depiction true."
        ),
        "how_it_works": (
            "Depiction works when it reproduces the involuntary "
            "pathway's output. Audiences are expert unconscious readers "
            "of faces - the fusiform face area and superior temporal "
            "sulcus decode expressions in milliseconds - so symbolic "
            "acting fails because the brain compares the depiction "
            "against a lifetime of real readings and finds the "
            "mechanics missing. The actor's craft, in Stanislavski's "
            "terms, is to produce the inner state and let the face "
            "follow; the artist's craft is to study the mechanics until "
            "the hand draws them without thinking. Both converge on the "
            "same truth: real faces first, symbols never."
        ),
        "key_points": [
            "Draw the eyes first: soft, widened, iris visible, aimed with intent.",
            "The Duchenne-at-rest is small; avoid the toothy performance grin.",
            "Act the arrival beat: light-up, caught breath, eyes before body.",
            "Hidden love: play suppression, let the leaks act.",
            "Mechanics over symbols: depict what real faces do, not the idea of love.",
        ],
        "requirements": [
            "Separate notes for artists and for actors.",
            "Concrete, drawable/playable details - degrees of tilt, muscle names.",
            "The common failure named: symbols instead of mechanics.",
            "Grounded in the anatomy taught earlier in the ladder.",
        ],
        "standards": [
            "Ekman P., Friesen W.V. Facial Action Coding System. Palo Alto: Consulting Psychologists Press; 1978.",
            "Stanislavski C. An Actor Prepares. Trans. Hapgood E.R. New York: Theatre Arts; 1936.",
        ],
        "citations": [
            "Ekman P., Friesen W.V. Facial Action Coding System. Palo Alto: Consulting Psychologists Press; 1978.",
            "Stanislavski C. An Actor Prepares. Trans. Hapgood E.R. New York: Theatre Arts; 1936.",
            "Eibl-Eibesfeldt I. Human Ethology. New York: Aldine de Gruyter; 1989.",
        ],
        "sig_lens": (
            "Through the Signature lens, the artist and actor are the "
            "archive's illustrators - the ones who make the record "
            "visible to those who cannot read the text. His canon says "
            "records render as human-readable sentences and paragraphs, "
            "so the Signature editions give the illustrators their brief "
            "in plain working language: draw the mechanics, play the "
            "arrival, never the symbol. The Signature originals hold one "
            "standard for every depiction in the system - truth to the "
            "real face - because an archive's illustrations must be as "
            "honest as its text. Signature-made, never presented as "
            "authentic public record."
        ),
    },
    {
        "key": "classic-triggers",
        "name": "The Classic Triggers of Love",
        "group": "triggers",
        "ladder_rank": 9,
        "ladder_tier": "compounded",
        "description": (
            "Triggers are the situations, words, and events that commonly "
            "set love off or stir it deeper. They are not magic buttons - "
            "they are the appraisals the mind has learned to answer with "
            "love. The classics, documented across relationship research:\n\n"
            "Proximity and repeated contact. The single most reliable "
            "trigger in the literature: being around someone, again and "
            "again. Zajonc's mere-exposure effect shows liking grows with "
            "familiarity, and the great majority of romances and deep "
            "friendships begin with repeated unplanned contact - the "
            "classroom, the workplace, the neighborhood. Love often "
            "starts as geography.\n\n"
            "Kindness received in a moment of need. Being helped, "
            "comforted, or simply noticed when vulnerable is a powerful "
            "trigger - the mind appraises the helper as safe and good, "
            "and gratitude opens the door love walks through. This is "
            "why shared adversity bonds people so fast: need plus "
            "kindness is love's accelerant.\n\n"
            "Admiration. Witnessing excellence, courage, integrity, or "
            "skill in another person triggers a warm upward feeling - "
            "researchers call it elevation - that readily deepens into "
            "love. We love people we look up to: mentors, heroes, "
            "partners whose competence delights us.\n\n"
            "Mutual self-disclosure. Arthur Aron's famous 1997 procedure "
            "showed that strangers answering escalating personal "
            "questions - then holding eye contact - generated measurable "
            "closeness in under an hour. Being known, and knowing, is a "
            "direct trigger: the self expands to include the other, and "
            "that inclusion is felt as love.\n\n"
            "Shared novelty and excitement. Couples who do new, "
            "arousing things together report stronger love - Aron's "
            "follow-up work confirmed it. The arousal of novelty gets "
            "misattributed, partly, to the partner: the adventure's "
            "sparkle rubs off on the person beside you.\n\n"
            "Vulnerability witnessed with tenderness. Seeing the "
            "beloved-to-be unguarded - laughing helplessly, moved to "
            "tears, absorbed in something they love - triggers "
            "tenderness, love's gentlest trigger. We fall for people in "
            "their unguarded moments because the mask dropping is "
            "itself an invitation to closeness.\n\n"
            "Care given and received over time. The slowest trigger and "
            "the deepest: showing up, remembering, tending. Every "
            "diagonal sandwich, every remembered preference, every kept "
            "promise is a small trigger event, and they compound like "
            "interest into the steadiest love there is."
        ),
        "how_it_works": (
            "Triggers work through appraisal: each classic trigger is a "
            "situation the mind reads as 'this person is good, safe, and "
            "connected to me.' Proximity works through familiarity and "
            "predictability. Kindness-in-need works through the "
            "attachment system's safe-haven response. Admiration works "
            "through elevation and idealization. Disclosure works "
            "through self-expansion - Aron's model of including the other "
            "in the self. Novelty works through arousal misattribution. "
            "Tenderness works through the caregiving system, the ancient "
            "circuitry that responds to vulnerability with approach. "
            "Repeated triggering strengthens the appraisal until it "
            "becomes the default: the person is simply, obviously, "
            "loved."
        ),
        "key_points": [
            "Proximity: love often starts as geography - repeated contact is the top trigger.",
            "Kindness in need: vulnerability met with care is love's accelerant.",
            "Admiration, disclosure, shared novelty, and witnessed tenderness all trigger love.",
            "Slow care over time is the deepest trigger - small events compounding like interest.",
            "Triggers are learned appraisals, not magic buttons.",
        ],
        "requirements": [
            "Seven classic triggers, each with its mechanism.",
            "Research grounding: Zajonc, Aron, attachment, elevation.",
            "The compounding principle: small triggers accumulate.",
            "Honesty: triggers set love off; they do not guarantee it.",
        ],
        "standards": [
            "Zajonc R.B. Attitudinal effects of mere exposure. Journal of Personality and Social Psychology. 1968;9(2):1-27.",
            "Aron A., Melinat E., Aron E.N., Vallone R., Bator R. The experimental generation of interpersonal closeness. Personality and Social Psychology Bulletin. 1997;23(4):363-377.",
            "Aron A., Aron E.N. Love and the Expansion of Self. New York: Hemisphere; 1986.",
        ],
        "citations": [
            "Zajonc R.B. Attitudinal effects of mere exposure. Journal of Personality and Social Psychology. 1968;9(2):1-27.",
            "Aron A., Melinat E., Aron E.N., Vallone R., Bator R. The experimental generation of interpersonal closeness. Personality and Social Psychology Bulletin. 1997;23(4):363-377.",
            "Aron A., Norman C.C., Aron E.N., McKenna C., Heyman R.E. Couples' shared participation in novel and arousing activities and experienced relationship quality. Journal of Personality and Social Psychology. 2000;78(2):273-284.",
        ],
        "sig_lens": (
            "Through the Signature lens, triggers are the archive's "
            "acquisition policy - the documented rules by which new love "
            "records enter the collection. His canon says generators must "
            "check the whole system before generating, and the Signature "
            "editions apply the same discipline to the heart: know your "
            "triggers and you know how your collection grows. The "
            "Signature originals file the seven classics as the standing "
            "acquisition list - proximity, kindness-in-need, admiration, "
            "disclosure, novelty, tenderness, steady care - so that every "
            "later record about behavior and expression can be traced to "
            "its source. Signature-made, never presented as authentic "
            "public record."
        ),
    },
    {
        "key": "personal-triggers",
        "name": "Personal Triggers: Memories, Anniversaries, and Private Associations",
        "group": "triggers",
        "ladder_rank": 9,
        "ladder_tier": "compounded",
        "description": (
            "Beyond the universal classics, every love has a private "
            "trigger map - the memories, dates, objects, songs, smells, "
            "and places that set one particular person's love ringing "
            "like a struck bell. No one else would understand why the "
            "smell of cut grass undoes you, or why a certain off-key "
            "humming makes your chest ache with fondness. That privacy "
            "is the point: personal triggers are love's fingerprints.\n\n"
            "Memories as triggers: the mind stores emotional events with "
            "their sensory packaging intact - psychologists call this "
            "state-dependent and context-dependent memory. The song "
            "playing during the first dance, the restaurant's particular "
            "smell, the exact blue of a jacket on the day everything "
            "changed: encountering the packaging replays the feeling. "
            "Lovers curate these deliberately - the saved ticket stub, "
            "the playlist, the photograph - building a private museum "
            "whose every exhibit is a trigger.\n\n"
            "Anniversaries as triggers: calendar dates become emotional "
            "landmarks. The anniversary effect is well documented: mood "
            "and memory shift as the date approaches, often before the "
            "person consciously registers why. Couples' anniversaries, "
            "a child's birthday, the date of a loss - each arrives with "
            "its weather. Wise couples learn their calendar the way "
            "sailors learn tides: not to fight the water, but to sail "
            "it.\n\n"
            "Private associations: the strangest and most touching "
            "triggers are the accidental ones - the brand of tea they "
            "drink, the way they mispronounce a word, the dent in the "
            "car door from the day you laughed too hard. These form "
            "through simple associative conditioning: neutral things "
            "paired repeatedly with the beloved's presence absorb the "
            "feeling. After enough pairings, the tea alone can warm you.\n\n"
            "The practical wisdom: personal triggers are a resource to "
            "tend. Couples who deliberately maintain their trigger map - "
            "revisiting places, replaying songs, retelling origin "
            "stories - keep the feeling accessible across decades. And "
            "when a trigger turns painful, as after a loss, the same "
            "knowledge helps: the trigger is a bell, not a command, and "
            "bells can be rehung - new associations can be built around "
            "old cues with time and gentle exposure."
        ),
        "how_it_works": (
            "Personal triggers form through associative learning and "
            "emotional memory consolidation. The amygdala tags "
            "experiences with emotional significance and binds them to "
            "co-occurring sensory details; the hippocampus files the "
            "episode; later, any fragment of the packaging can reactivate "
            "the whole network - pattern completion. Anniversaries work "
            "through temporal context reinstatement: the calendar date "
            "recreates enough context to prime the associated emotion. "
            "Because these are learned associations, they are also "
            "re-learnable: extinction and counter-conditioning can soften "
            "painful triggers, and deliberate rehearsal can strengthen "
            "warm ones."
        ),
        "key_points": [
            "Every love has a private trigger map - memories, dates, objects, sensory cues.",
            "Emotional memory stores feelings with their sensory packaging intact.",
            "Anniversaries arrive with weather; wise couples learn their calendar like tides.",
            "Neutral things absorb feeling through repeated pairing with the beloved.",
            "Triggers can be tended deliberately - and painful ones can be rehung with time.",
        ],
        "requirements": [
            "Four kinds: memories, anniversaries, private associations, curated keepsakes.",
            "Mechanisms: associative conditioning, pattern completion, temporal reinstatement.",
            "The fingerprint framing: privacy is the point.",
            "Practical wisdom: tending the map, and rehanging painful bells.",
        ],
        "standards": [
            "LeDoux J.E. The Emotional Brain. New York: Simon & Schuster; 1996.",
            "Eich E. Searching for mood dependent memory. Psychological Science. 1995;6(2):67-75.",
        ],
        "citations": [
            "LeDoux J.E. The Emotional Brain. New York: Simon & Schuster; 1996.",
            "Eich E. Searching for mood dependent memory. Psychological Science. 1995;6(2):67-75.",
            "Bowlby J. Attachment and Loss, Vol. 3: Loss. New York: Basic Books; 1980.",
        ],
        "sig_lens": (
            "Through the Signature lens, personal triggers are the "
            "archive's private index - the cross-references only the "
            "collection's owner can read. His canon says every record is "
            "the full file, so the Signature editions file the sensory "
            "packaging with the feeling: the song, the smell, the blue "
            "jacket, the mispronounced word. The Signature originals "
            "treat the trigger map as a treasure to tend deliberately - "
            "revisit the places, replay the songs, retell the origin - "
            "because an archive's private index is what makes the whole "
            "collection retrievable across decades. Signature-made, never "
            "presented as authentic public record."
        ),
    },
    {
        "key": "surprise-triggers",
        "name": "Surprise Triggers: Unexpected Things That Can Spark Love",
        "group": "triggers",
        "ladder_rank": 9,
        "ladder_tier": "compounded",
        "description": (
            "Some triggers make sense - kindness, proximity, admiration. "
            "Others seem to come from nowhere, and they are just as real. "
            "This record collects the odd, unexpected sparks, because "
            "knowing them stops people from distrusting love that "
            "arrived by a strange road.\n\n"
            "Arousal misattribution: the famous bridge study by Dutton "
            "and Aron (1974) found that men interviewed on a shaky "
            "suspension bridge were more likely to feel attraction to "
            "the interviewer than men on a stable bridge - the fear-"
            "arousal of the bridge got misread as attraction to the "
            "person. Roller coasters, horror movies, hard workouts, even "
            "loud concerts: any strong arousal can spill over and be "
            "credited to whoever is beside you. Couples who bond on "
            "adventures are partly bonding to the adrenaline.\n\n"
            "The helper's high: people often start loving those they "
            "help. The mind, observing itself caring for someone, "
            "concludes it must love them - self-perception theory "
            "applied to the heart. Mentors fall for proteges, nurses "
            "for patients, rescuers for the rescued: the care came "
            "first, and the feeling followed the behavior.\n\n"
            "Proximity accidents: the assigned seat, the shared "
            "commute, the neighboring desk. Research on friendship "
            "formation shows sheer propinquity predicts bonds better "
            "than shared interests do. Many loves are, at root, "
            "scheduling artifacts - which does not make them less real, "
            "only less romantic in origin than the stories later claim.\n\n"
            "The almost-lost: nearly losing someone - a health scare, "
            "a close call, a fight that almost ended it - routinely "
            "detonates a surge of love. Contrast does the work: the "
            "preview of absence teaches the value of presence in a way "
            "years of presence never could.\n\n"
            "Resemblance and familiarity echoes: people are drawn to "
            "those who resemble loved figures from earlier life - a "
            "voice like a grandmother's, a laugh like an old friend's - "
            "and to the merely familiar. The heart is a pattern-"
            "matcher, and it loves what it recognizes.\n\n"
            "None of this cheapens love. A spark's origin does not "
            "determine a fire's worth: what matters is what the feeling "
            "grows into and what it is built from afterward. Strange "
            "roads still arrive."
        ),
        "how_it_works": (
            "Surprise triggers share one mechanism: the brain's "
            "attribution system making reasonable guesses from noisy "
            "data. Arousal misattribution is the two-factor theory in "
            "action - unexplained arousal plus a salient person equals "
            "attraction. The helper's high is self-perception: behavior "
            "implies attitude. Propinquity is mere exposure at scale. "
            "The almost-lost is contrast and loss-aversion applied to "
            "attachment. Resemblance is associative priming of old "
            "bonds. In each case the feeling that results is genuine "
            "love - the appraisal 'this one matters' forms through an "
            "unusual door, but once formed, it runs the same machinery "
            "as any other love."
        ),
        "key_points": [
            "Misattributed arousal: fear, excitement, or exertion can be credited to the person beside you.",
            "The helper's high: caring behavior can teach the heart to feel.",
            "Propinquity: many loves are scheduling artifacts - real, just unromantic in origin.",
            "The almost-lost: a preview of absence teaches the value of presence.",
            "A spark's strange origin does not determine the fire's worth.",
        ],
        "requirements": [
            "Five surprise triggers, each with its study or mechanism.",
            "The attribution mechanism unified across all five.",
            "The non-cheapening thesis: strange roads still arrive.",
            "Grounded in real studies: Dutton and Aron, Zajonc, self-perception.",
        ],
        "standards": [
            "Dutton D.G., Aron A.P. Some evidence for heightened sexual attraction under conditions of high anxiety. Journal of Personality and Social Psychology. 1974;30(4):510-517.",
            "Bem D.J. Self-perception theory. Advances in Experimental Social Psychology. 1972;6:1-62.",
        ],
        "citations": [
            "Dutton D.G., Aron A.P. Some evidence for heightened sexual attraction under conditions of high anxiety. Journal of Personality and Social Psychology. 1974;30(4):510-517.",
            "Bem D.J. Self-perception theory. Advances in Experimental Social Psychology. 1972;6:1-62.",
            "Zajonc R.B. Attitudinal effects of mere exposure. Journal of Personality and Social Psychology. 1968;9(2):1-27.",
        ],
        "sig_lens": (
            "Through the Signature lens, surprise triggers are the "
            "archive's unplanned acquisitions - the records that arrived "
            "by misdelivered mail and turned out to be treasures. His "
            "canon says never present a fraction as the whole, so the "
            "Signature editions refuse to grade loves by the romance of "
            "their origin story: the scheduling artifact, the shaky "
            "bridge, the almost-lost - each is filed as a complete, "
            "legitimate record. The Signature originals teach that the "
            "archive does not ask how a treasure arrived, only what it "
            "is and what it becomes. Signature-made, never presented as "
            "authentic public record."
        ),
    },
    {
        "key": "chain-reactions",
        "name": "Chain Reactions: How One Trigger Can Cascade into Related Emotions",
        "group": "triggers",
        "ladder_rank": 10,
        "ladder_tier": "compounded",
        "description": (
            "Love rarely fires alone for long. One trigger sets off love, "
            "and love - being a complex, high-salience state - sets off "
            "its neighbors, which set off theirs. This record maps the "
            "cascades, because recognizing the chain is what lets people "
            "steer it.\n\n"
            "The joy cascade: love fires, joy follows (its parent "
            "emotion), joy broadens attention, broadened attention "
            "notices more lovable things, which deepens love. This is "
            "the upward spiral Fredrickson describes: love and joy "
            "feeding each other in a loop that builds the relationship's "
            "reserves. Couples in this cascade describe feeling "
            "'lucky' - and the luck is partly this self-reinforcing "
            "loop.\n\n"
            "The fear cascade: love fires, then the thought 'what if I "
            "lose this' arrives, and fear blends in. Love plus fear is "
            "the recipe for jealousy and anxious vigilance: checking, "
            "worrying, needing reassurance. The cascade continues - "
            "vigilance finds ambiguous evidence, ambiguity feeds more "
            "fear, fear demands more reassurance, reassurance-seeking "
            "strains the bond. Recognizing the chain at the second link "
            "('this is love plus fear, not evidence of threat') is what "
            "stops it.\n\n"
            "The sadness cascade: love fires toward someone suffering, "
            "and sadness blends in - this is compassion, love's most "
            "tender cascade. But if the suffering cannot be helped, "
            "sadness can deepen toward grief-with-the-living: helpless "
            "sorrow, exhaustion, the ache of loving someone you cannot "
            "fix. The chain needs a circuit-breaker - acceptance, "
            "support for the supporter - or it drains the lover.\n\n"
            "The anger cascade: love fires, a threat to the beloved "
            "appears, and anger blends in - protective fierceness, the "
            "parent facing the danger, the partner confronting the "
            "insult. This cascade is love doing its guardian work, and "
            "it is righteous when aimed at the threat. It misfires when "
            "the anger turns on the beloved ('you scared me' becoming "
            "'this is your fault') - the chain jumping its track.\n\n"
            "The practical skill is chain-reading: when a strong feeling "
            "arrives, ask what fired first. Trace the cascade back to "
            "its first link - usually love, or love plus one neighbor - "
            "and the tangle simplifies. Intervene at the earliest link "
            "you can reach: soothe the fear, accept the sadness, aim the "
            "anger at the threat. The cascade is not destiny; it is a "
            "sequence, and sequences can be interrupted."
        ),
        "how_it_works": (
            "Cascades work through associative spreading and appraisal "
            "chaining. An emotion, once active, primes its neighbors in "
            "the associative network - love primes joy, trust, fear of "
            "loss, sadness at suffering, anger at threats - and each "
            "new emotion re-appraises the situation, generating the "
            "next. This is Bower's network theory of affect applied to "
            "love: activation spreads along learned links, and the "
            "subjective experience is one unfolding episode rather than "
            "separate feelings. Interruption works because each link "
            "depends on the appraisal feeding it - change the appraisal "
            "('they are safe,' 'this threat is handled') and the chain "
            "starves."
        ),
        "key_points": [
            "Love triggers cascades: joy (upward spiral), fear (jealousy), sadness (compassion), anger (protection).",
            "Each cascade is love plus one neighbor, then the neighbor's own chain.",
            "Chain-reading: trace the feeling back to its first link to simplify the tangle.",
            "Intervene at the earliest reachable link - soothe, accept, or aim the feeling rightly.",
            "Cascades are sequences, not destiny; sequences can be interrupted.",
        ],
        "requirements": [
            "Four cascades mapped: joy, fear, sadness, anger.",
            "Each with its mechanism and its misfire mode.",
            "The chain-reading skill taught explicitly.",
            "Spreading-activation mechanism named.",
        ],
        "standards": [
            "Bower G.H. Mood and memory. American Psychologist. 1981;36(2):129-148.",
            "Fredrickson B.L. The role of positive emotions in positive psychology. American Psychologist. 2001;56(3):218-226.",
        ],
        "citations": [
            "Bower G.H. Mood and memory. American Psychologist. 1981;36(2):129-148.",
            "Fredrickson B.L. The role of positive emotions in positive psychology. American Psychologist. 2001;56(3):218-226.",
            "Lazarus R.S. Emotion and Adaptation. New York: Oxford University Press; 1991.",
        ],
        "sig_lens": (
            "Through the Signature lens, cascades are the archive's "
            "cross-reference chains - one record pulling its neighbors "
            "off the shelf in sequence. His canon says every database "
            "teaches from many angles, so the Signature editions teach "
            "each cascade from the inside and the outside: what the "
            "chain feels like, and where its links can be broken. The "
            "Signature originals treat chain-reading as an archivist's "
            "skill - trace any tangle to its first record and the whole "
            "shelf makes sense. Signature-made, never presented as "
            "authentic public record."
        ),
    },
]

ENTRIES += [
    {
        "key": "behavior-actions",
        "name": "What People Do When They Feel Love",
        "group": "behavior",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Feelings are private; actions are the public record of love. "
            "This record catalogs what people characteristically do when "
            "they feel love - the behavioral signature that observers "
            "can actually see.\n\n"
            "They approach and prioritize. The lover moves toward: "
            "choosing the seat nearby, finding reasons to be present, "
            "making time where there was none. Prioritization is love's "
            "clearest behavioral tell - calendar and attention are "
            "honest currencies, and love spends them on the beloved. "
            "Researchers on investment models of commitment find that "
            "willingness to sacrifice time and convenience predicts "
            "relationship survival better than reported passion does.\n\n"
            "They serve in small ways. Love's daily behavior is "
            "disproportionately tiny: the remembered coffee order, the "
            "charger plugged in, the door held, the blanket fetched. "
            "Gottman's research on 'turning toward' versus 'turning "
            "away' shows these micro-services are the atoms of lasting "
            "bonds - each one a small vote for the relationship, counted "
            "by the partner's nervous system even when the conscious "
            "mind forgets.\n\n"
            "They touch. Affectionate touch - hand-holding, hugs, the "
            "hand on the back, hair-stroking, the foot under the table - "
            "is love's native behavior. Touch communicates love more "
            "accurately than words in laboratory studies of emotional "
            "communication, and it regulates both partners' physiology: "
            "cortisol drops, oxytocin rises, pain tolerance increases. "
            "Lovers touch to say what language cannot compress.\n\n"
            "They protect. Love activates guarding behavior: stepping "
            "between the beloved and the threat, literal or social - "
            "defending them in conversation, buffering bad news, "
            "standing in the rain-side of the umbrella. Protectiveness "
            "is love's anger-channel doing legitimate work.\n\n"
            "They include. Lovers merge lives: introducing the beloved "
            "into every circle, making joint plans, using 'we' - the "
            "linguistic marker researchers count as a genuine signal of "
            "closeness. Inclusion is self-expansion made visible: the "
            "beloved is being filed, behaviorally, under 'self.'\n\n"
            "They celebrate and grieve with. Love shows up at the "
            "beloved's peaks and valleys - the promotion dinner, the "
            "hospital waiting room. Presence at high-stakes moments is "
            "the behavior people remember decades later when they "
            "describe being loved.\n\n"
            "They repair. After conflict, lovers come back: the apology, "
            "the peace offering, the deliberate return to warmth. "
            "Gottman's repair attempts are the single most behavioral "
            "predictor he measures - not the absence of fights, but the "
            "presence of comebacks."
        ),
        "how_it_works": (
            "Love's behaviors are the output of its three systems in "
            "action. Approach and prioritization come from the reward "
            "system marking the beloved as high-value. Service and "
            "inclusion come from self-expansion - the beloved included "
            "in the self is served like the self. Touch and presence "
            "come from the attachment system seeking and providing the "
            "safe haven. Protection comes from the caregiving system "
            "fused with threat response. Repair comes from commitment - "
            "Sternberg's third corner - overriding the impulse to "
            "withdraw. Each behavior is a system doing its job in the "
            "open, which is why behavior is the most reliable evidence "
            "of love: systems are harder to fake than faces."
        ),
        "key_points": [
            "Approach and prioritization: time and attention are love's honest currencies.",
            "Micro-service: tiny remembered kindnesses are the atoms of lasting bonds.",
            "Touch: love's native language, communicating and regulating better than words.",
            "Protection, inclusion, celebration, and presence at high-stakes moments.",
            "Repair after conflict is the most predictive behavior of all.",
        ],
        "requirements": [
            "Seven behavior families, each observable and concrete.",
            "Research grounding: investment models, Gottman turning-toward, touch studies.",
            "The honesty thesis: behavior is harder to fake than faces.",
            "Each behavior tied to its underlying system.",
        ],
        "standards": [
            "Gottman J.M. The Seven Principles for Making Marriage Work. New York: Crown; 1999.",
            "Rusbult C.E. A longitudinal test of the investment model. Journal of Personality and Social Psychology. 1980;38(1):172-186.",
            "Hertenstein M.J., Holmes R., McCullough M., Keltner D. The communication of emotion via touch. Emotion. 2009;9(4):566-573.",
        ],
        "citations": [
            "Gottman J.M. The Seven Principles for Making Marriage Work. New York: Crown; 1999.",
            "Rusbult C.E. A longitudinal test of the investment model. Journal of Personality and Social Psychology. 1980;38(1):172-186.",
            "Hertenstein M.J., Holmes R., McCullough M., Keltner D. The communication of emotion via touch. Emotion. 2009;9(4):566-573.",
            "Aron A., Aron E.N. Love and the Expansion of Self. New York: Hemisphere; 1986.",
        ],
        "sig_lens": (
            "Through the Signature lens, behaviors are the archive's "
            "circulation records - proof the collection is used, not "
            "just stored. His canon says every record is the full file, "
            "so the Signature editions file all seven behaviors as the "
            "complete evidence set: approach, service, touch, "
            "protection, inclusion, presence, repair. The Signature "
            "originals teach the archivist's rule for reading love in "
            "the wild - trust the circulation desk over the cover "
            "letter, because systems are harder to fake than faces. "
            "Signature-made, never presented as authentic public record."
        ),
    },
    {
        "key": "behavior-words",
        "name": "What People Say: The Language of Love",
        "group": "behavior",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Love has a dialect. People in love do not just feel "
            "differently - they talk differently, in patterns so "
            "consistent that researchers can measure them. This record "
            "teaches the language of love: phrases, tone, and speech "
            "patterns.\n\n"
            "Characteristic phrases: the direct declarations ('I love "
            "you,' in all their weight and timing), the check-ins ('how "
            "are you, really'), the future-talk ('when we...,' 'someday "
            "we should...'), the appreciation statements ('I love how "
            "you...'), the repair phrases ('I am sorry,' 'help me "
            "understand,' 'we are okay, right'), and the private lexicon "
            "- nicknames, invented words, shared jokes that function as "
            "a couple's encryption. Each phrase family does work: "
            "declarations mark, check-ins tend, future-talk commits, "
            "appreciation nourishes, repair heals, private language "
            "bonds.\n\n"
            "Tone: love softens the voice. Acoustic studies find that "
            "people speaking to loved ones use lower pitch, slower "
            "tempo, warmer timbre - the same prosody parents use with "
            "infants, extended across the lifespan. The voice also "
            "brightens on the beloved's name: saying it carries a "
            "measurable lift. And love listens differently - the "
            "'mm-hm' of genuine attention, the follow-up question that "
            "proves the first answer was heard.\n\n"
            "Speech patterns: lovers converge. They match each other's "
            "vocabulary, speech rate, and even function-word use - a "
            "phenomenon called language style matching, which predicts "
            "relationship stability in studies of couples' texts and "
            "conversations. They use 'we' more than 'I' when discussing "
            "the relationship. They narrate jointly: 'remember when we...' "
            "stories told in overlapping voices. They ask more questions "
            "and give longer answers - attention made audible.\n\n"
            "What is not said matters too. Love's language includes "
            "strategic silence: not voicing every irritation, letting "
            "small things go unremarked. Gottman's research "
            "distinguishes this from stonewalling - the difference is "
            "warmth: letting-go silence is relaxed and fond, stonewalling "
            "is rigid and cold. One is love editing; the other is love "
            "withdrawing."
        ),
        "how_it_works": (
            "Love's language effects run through alignment and "
            "signaling. Prosody softening is the vocal branch of the "
            "affiliative system - the same calming signal in voice that "
            "touch provides in skin. Language style matching is the "
            "cognitive branch of synchrony: aligned representations "
            "produce aligned speech, and the alignment itself signals "
            "'we are on the same team.' The 'we' pronoun and joint "
            "narration are self-expansion made grammatical - the "
            "beloved literally inside the speaker's sentences. Private "
            "lexicons work as costly signals: inventing and maintaining "
            "a shared code takes effort only the invested will spend, "
            "which is why it bonds."
        ),
        "key_points": [
            "Six phrase families: declarations, check-ins, future-talk, appreciation, repair, private lexicon.",
            "Tone softens: lower pitch, slower tempo, warmer timbre - and the voice lifts on the beloved's name.",
            "Lovers converge: matched vocabulary, rate, and function words predict stability.",
            "'We' language and joint narration are self-expansion made grammatical.",
            "Warm letting-go silence is love editing; cold silence is love withdrawing.",
        ],
        "requirements": [
            "Phrases, tone, and patterns each covered with examples.",
            "Research grounding: language style matching, prosody studies, Gottman.",
            "The silence distinction: editing versus withdrawing.",
            "Mechanisms: alignment, signaling, self-expansion in grammar.",
        ],
        "standards": [
            "Ireland M.E., Pennebaker J.W. Language style matching in writing. Journal of Personality and Social Psychology. 2010;99(3):549-571.",
            "Gottman J.M. The Seven Principles for Making Marriage Work. New York: Crown; 1999.",
        ],
        "citations": [
            "Ireland M.E., Pennebaker J.W. Language style matching in writing. Journal of Personality and Social Psychology. 2010;99(3):549-571.",
            "Gottman J.M. The Seven Principles for Making Marriage Work. New York: Crown; 1999.",
            "Aron A., Aron E.N. Love and the Expansion of Self. New York: Hemisphere; 1986.",
        ],
        "sig_lens": (
            "Through the Signature lens, the language of love is the "
            "archive's cataloging language - the shared vocabulary the "
            "collection uses to describe itself. His canon demands "
            "human-readable sentences, so the Signature editions treat "
            "every phrase family as catalog copy: declarations as "
            "titles, check-ins as status notes, future-talk as "
            "acquisition plans, the private lexicon as the local "
            "classification only two librarians share. The Signature "
            "originals teach that convergence - the matched vocabularies, "
            "the overlapping stories - is two collections merging into "
            "one. Signature-made, never presented as authentic public "
            "record."
        ),
    },
    {
        "key": "behavior-decisions",
        "name": "How Love Changes Decisions and Judgment",
        "group": "behavior",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Love is not just a feeling about decisions - it is a "
            "participant in them. This record maps how love changes what "
            "people choose, and how to tell when the change is wisdom "
            "versus bias.\n\n"
            "Love reweights the utility function. In decision research "
            "terms, love adds the beloved's welfare to your own payoff "
            "matrix - their outcomes count in your calculations, "
            "sometimes equally, sometimes more. This is why lovers make "
            "'irrational' sacrifices that are perfectly rational once "
            "the beloved's utility is in the equation: the 3 a.m. "
            "airport run, the career compromise, the organ donation. "
            "Love does not break rationality; it expands whose outcomes "
            "rationality covers.\n\n"
            "Love lengthens the time horizon. People in love plan "
            "further ahead - the future-talk of the language record is "
            "the surface of a deeper shift: decisions get evaluated "
            "against years, not days. This generally improves decisions "
            "(patience, investment, health), and it is one reason "
            "long-term partnership correlates with steadier life "
            "outcomes.\n\n"
            "Love biases judgment in predictable ways. Positive "
            "illusions: lovers systematically overrate the beloved's "
            "virtues and underrate their flaws - and research by Sandra "
            "Murray shows these illusions predict relationship success, "
            "because the believed-in virtues tend to become real. "
            "Attentional bias: alternatives get downgraded - people in "
            "love literally rate other potential partners as less "
            "attractive, a protective mechanism researchers call "
            "derogation of alternatives. Risk shift: love makes people "
            "braver for the beloved's sake and more cautious about "
            "risks to the bond - the same person will skydive for a "
            "charity their partner loves and refuse a solo trip that "
            "would worry them.\n\n"
            "The wisdom-versus-bias test: love's influence is wisdom "
            "when it expands the circle of care without blinding the "
            "eyes - the reweighted utility, the longer horizon. It is "
            "bias when it disables error-checking: ignoring red flags, "
            "isolating from friends' counsel, making irreversible "
            "decisions at peak intensity. The practical rule: let love "
            "vote, but never let it vote alone - especially at high "
            "volume, especially fast. Sleep on the big ones; consult "
            "the un-aroused; keep the friends who will tell you the "
            "truth."
        ),
        "how_it_works": (
            "Love changes decisions through three channels. "
            "Motivational: the reward system now pays out for the "
            "beloved's outcomes, reweighting choices. Cognitive: "
            "positive illusions and alternative-derogation are "
            "motivated-cognition mechanisms that protect the bond's "
            "perceived value. Temporal: attachment security reduces "
            "threat-vigilance spending, freeing cognitive resources "
            "for long-horizon planning. The bias risk comes from the "
            "same machinery: motivated cognition that protects the "
            "bond can also protect it from true information. "
            "Metacognition - thinking about the thinking - is the "
            "corrective: naming love's vote lets the rest of the "
            "committee weigh in."
        ),
        "key_points": [
            "Love reweights the payoff matrix: the beloved's outcomes count in your calculations.",
            "Love lengthens the time horizon - decisions get judged against years.",
            "Positive illusions and alternative-derogation protect the bond - and predict success.",
            "Wisdom expands care without blinding eyes; bias disables error-checking.",
            "The rule: let love vote, never let it vote alone - sleep on the big ones.",
        ],
        "requirements": [
            "Three influence channels: motivational, cognitive, temporal.",
            "Named biases with their protective functions.",
            "The wisdom-versus-bias test stated as a practical rule.",
            "Research grounding: Murray positive illusions, investment models.",
        ],
        "standards": [
            "Murray S.L., Holmes J.G., Griffin D.W. The benefits of positive illusions. Journal of Personality and Social Psychology. 1996;70(1):79-98.",
            "Rusbult C.E. A longitudinal test of the investment model. Journal of Personality and Social Psychology. 1980;38(1):172-186.",
        ],
        "citations": [
            "Murray S.L., Holmes J.G., Griffin D.W. The benefits of positive illusions. Journal of Personality and Social Psychology. 1996;70(1):79-98.",
            "Rusbult C.E. A longitudinal test of the investment model. Journal of Personality and Social Psychology. 1980;38(1):172-186.",
            "Sternberg R.J. A triangular theory of love. Psychological Review. 1986;93(2):119-135.",
        ],
        "sig_lens": (
            "Through the Signature lens, love's vote in decisions is the "
            "archive's acquisitions committee gaining a new member - one "
            "who argues for the beloved's welfare in every deliberation. "
            "His canon says every record teaches from many angles, so "
            "the Signature editions teach the committee rules: the new "
            "member's vote is legitimate and often wise, but the charter "
            "requires the full committee - the un-aroused mind, the "
            "truth-telling friends, the slept-on morning. The Signature "
            "originals honor love's expanded rationality while keeping "
            "the error-checking online. Signature-made, never presented "
            "as authentic public record."
        ),
    },
    {
        "key": "behavior-intensity",
        "name": "Love at Full Volume: Behavior Under Intensity",
        "group": "behavior",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "At high intensity, love's behaviors escalate - and the "
            "escalation follows a pattern. This record maps what changes "
            "as the volume rises, where escalation is beautiful, and "
            "where it crosses lines.\n\n"
            "Pursuit intensifies. Moderate love approaches; intense love "
            "pursues: constant contact attempts, showing up unannounced, "
            "grand gestures. At the healthy end this is romance - the "
            "airport run at dawn, the surprise that took weeks to plan. "
            "The line is consent and reciprocity: pursuit that delights "
            "a willing recipient is courtship; pursuit that alarms an "
            "unwilling one is harassment, and the feeling behind it does "
            "not change that classification. Intensity never licenses "
            "disregard.\n\n"
            "Vigilance intensifies. Moderate love notices; intense love "
            "monitors: where are they, who are they with, what did that "
            "message mean. Some of this is the attachment system doing "
            "its safety-check job at high gain. It becomes destructive "
            "when monitoring replaces trust - surveillance, interrogation, "
            "isolation demands. The test: does the vigilance calm when "
            "reassured, or does it escalate regardless of evidence? "
            "Calmable vigilance is love at high gain; uncalmable "
            "vigilance is anxiety wearing love's clothes.\n\n"
            "Sacrifice intensifies. Moderate love gives; intense love "
            "gives recklessly: health, savings, friendships, identity "
            "offered up. Generous sacrifice for a real shared good is "
            "love's glory. Self-erasing sacrifice - giving until there "
            "is no self left to give from - is love consuming its own "
            "foundation. The ancient rule holds: you cannot pour from "
            "an empty cup, and a love that requires your disappearance "
            "is asking for something love should never ask.\n\n"
            "Expression intensifies. Declarations get bigger, more "
            "frequent, more public. Mostly this is harmless joy. It "
            "turns when expression becomes pressure - the grand gesture "
            "as leverage, the public declaration as a trap ('say it "
            "back, everyone's watching'). Love expresses; it does not "
            "extort.\n\n"
            "The through-line: intensity amplifies love's behaviors "
            "without changing their moral structure. Everything love "
            "does at moderate volume - approach, notice, give, declare - "
            "it does more of at high volume, and the ethics scale with "
            "the behavior: consent still required, trust still the "
            "goal, the self still worth preserving, expression still a "
            "gift rather than a demand. Teach the escalation, and teach "
            "the lines: that is the whole record."
        ),
        "how_it_works": (
            "Behavioral escalation under intensity is dose-response: the "
            "same motivational systems, driven harder by higher arousal "
            "and higher salience, produce more frequent and more extreme "
            "outputs. The prefrontal regulatory systems do not scale up "
            "at the same rate - arousal impairs executive function, which "
            "is why intense love feels 'out of control.' The lines "
            "described are where one person's approach system collides "
            "with another person's autonomy: consent, trust, and "
            "self-preservation are the guardrails that intensity must "
            "not cross. Recognizing escalation as amplification - not "
            "transformation - keeps the ethics clear: the rules do not "
            "change at high volume; only the temptation to break them "
            "grows."
        ),
        "key_points": [
            "Pursuit, vigilance, sacrifice, and expression all escalate with intensity.",
            "Intensity never licenses disregard: consent and reciprocity are the line.",
            "Calmable vigilance is love at high gain; uncalmable vigilance is anxiety.",
            "Self-erasing sacrifice consumes love's own foundation.",
            "Expression must stay a gift, never become leverage or a trap.",
        ],
        "requirements": [
            "Four escalation channels mapped with their healthy and crossed forms.",
            "Clear ethical lines stated plainly for each channel.",
            "The amplification thesis: ethics do not change at high volume.",
            "Descriptive and protective - knowledge that guards, not that arms.",
        ],
        "standards": [
            "Tennov D. Love and Limerence. New York: Stein and Day; 1979.",
            "Buss D.M. The Evolution of Desire. 4th ed. New York: Basic Books; 2019.",
        ],
        "citations": [
            "Tennov D. Love and Limerence. New York: Stein and Day; 1979.",
            "Buss D.M. The Evolution of Desire. 4th ed. New York: Basic Books; 2019.",
            "Hatfield E., Rapson R.L. Love, Sex, and Intimacy. New York: HarperCollins; 1993.",
        ],
        "sig_lens": (
            "Through the Signature lens, escalation is the archive's "
            "volume knob turned all the way up - every behavior louder, "
            "none different in kind. His canon says records must guard "
            "as well as teach, so the Signature editions draw the lines "
            "in plain ink: consent, trust, the preserved self, the gift "
            "not the demand. The Signature originals honor intense love's "
            "beauty - the dawn airport run, the weeks-planned surprise - "
            "while holding the guardrails absolute, because an archive "
            "that teaches power without teaching limits has failed its "
            "readers. Signature-made, never presented as authentic public "
            "record."
        ),
    },
    {
        "key": "healthy-expression",
        "name": "Expressing Love Healthily: Saying It, Showing It, Channeling It",
        "group": "healthy-expression",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Love unfelt is a locked room; love unexpressed is a letter "
            "never sent. But expression is a skill, and like any skill "
            "it has better and worse forms. This record teaches the "
            "healthy ones: saying it, showing it, and channeling it.\n\n"
            "Saying it: the direct verbal expression. Research on "
            "affect labeling and relationship maintenance converges: "
            "partners who say 'I love you' - and mean it, and time it "
            "well - report higher satisfaction, and the saying "
            "regulates the sayer's own emotion too. Healthy saying is "
            "specific ('I love how you handled that call'), timely "
            "(not stockpiled for leverage), and bidirectional (said "
            "and heard - listening for the reply matters as much as "
            "delivering the line). It also includes the hard sayings: "
            "'I was wrong,' 'I need help,' 'this hurt me' - love's "
            "vocabulary is not only tender words but honest ones.\n\n"
            "Showing it: the behavioral expression from the behavior "
            "records, done deliberately. Healthy showing is attuned - "
            "matched to what the beloved actually wants, not what the "
            "giver wants to give. Chapman's 'love languages' idea, "
            "however simplified in popular form, captures the real "
            "principle researchers confirm: people differ in which "
            "expressions land, and attunement beats volume. Showing is "
            "also consistent: the daily small showings outweigh the "
            "occasional grand one, because trust is built from pattern, "
            "not peaks.\n\n"
            "Channeling it: love as fuel for the rest of life. "
            "Healthy channeling turns love's energy outward - into "
            "work made more generous, creativity deepened, patience "
            "with strangers widened, courage for hard things. "
            "Fredrickson's broaden-and-build gives the mechanism: love "
            "broadens the mindset, and the broadened mindset builds "
            "resources everywhere. Unchanneled love pools and stagnates; "
            "channeled love irrigates the whole life. The old advice "
            "'get a hobby' misfires because it treats love as the "
            "problem; the better advice is 'let the love work' - bring "
            "its warmth to everything else you do.\n\n"
            "The integration: healthy expression is say plus show plus "
            "channel, in balance. All saying and no showing is poetry "
            "without practice. All showing and no saying starves the "
            "beloved's need to hear it. No channeling turns love into a "
            "closed room two people sit in while life happens elsewhere. "
            "The full expression opens the doors: the feeling spoken, "
            "the care enacted, the energy shared with the world."
        ),
        "how_it_works": (
            "Healthy expression works through three conversions. Saying "
            "converts private feeling into shared knowledge - common "
            "ground the relationship can coordinate around. Showing "
            "converts feeling into evidence - costly signals that prove "
            "the feeling is real, building trust through pattern. "
            "Channeling converts feeling into general resources - the "
            "broaden-and-build mechanism spreading love's benefits "
            "beyond the dyad. Each conversion has a failure mode that "
            "defines its healthy form: saying fails as pressure or "
            "performance, showing fails as unattuned or inconsistent "
            "grandiosity, channeling fails as avoidance (burying in "
            "work to dodge the relationship). Health is the three "
            "conversions running clean."
        ),
        "key_points": [
            "Saying: specific, timely, bidirectional - including the hard honest sayings.",
            "Showing: attuned to what lands, consistent in small doses - pattern over peaks.",
            "Channeling: love's energy irrigating work, creativity, patience, courage.",
            "All saying, no showing: poetry without practice. All showing, no saying: starvation.",
            "Full expression opens the doors: spoken, enacted, and shared with the world.",
        ],
        "requirements": [
            "Three channels taught with their healthy forms and failure modes.",
            "Attunement principle: match expression to what the beloved receives.",
            "Pattern-over-peaks: trust is built from consistency.",
            "Integration: the balance of all three, not any one alone.",
        ],
        "standards": [
            "Chapman G. The Five Love Languages. Chicago: Northfield; 1992.",
            "Fredrickson B.L. The role of positive emotions in positive psychology. American Psychologist. 2001;56(3):218-226.",
            "Gottman J.M. The Seven Principles for Making Marriage Work. New York: Crown; 1999.",
        ],
        "citations": [
            "Chapman G. The Five Love Languages. Chicago: Northfield; 1992.",
            "Fredrickson B.L. The role of positive emotions in positive psychology. American Psychologist. 2001;56(3):218-226.",
            "Gottman J.M. The Seven Principles for Making Marriage Work. New York: Crown; 1999.",
        ],
        "sig_lens": (
            "Through the Signature lens, healthy expression is the "
            "archive's publishing program - the collection made public "
            "in three formats: the spoken catalog, the enacted "
            "exhibition, and the energy lent to every other project in "
            "the building. His canon says records must be full and "
            "human-readable, so the Signature editions publish completely: "
            "say it plainly, show it in the beloved's language, and let "
            "the warmth irrigate the whole life. The Signature originals "
            "keep the publishing house open daily - small editions, "
            "steady schedule - because trust, like readership, is built "
            "from pattern, not peaks. Signature-made, never presented as "
            "authentic public record."
        ),
    },
    {
        "key": "unhealthy-expression",
        "name": "When Love Goes Wrong: Bottling Up and Exploding",
        "group": "healthy-expression",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Love mis-expressed takes two classic forms: bottled up or "
            "exploded. Both start from the same place - feeling deeply - "
            "and both end in the same place: the love unreceived, the "
            "bond strained. This record teaches what each costs, so "
            "readers can recognize the pattern early.\n\n"
            "Bottling up: the love is felt but never expressed - never "
            "said, shown thinly or not at all, channeled nowhere. The "
            "bottler's reasons feel honorable: not wanting to burden, "
            "fearing rejection, believing love should be obvious without "
            "words. The costs are documented: the beloved cannot feel "
            "what is never transmitted, and unreceived love reads as "
            "absence - partners of bottlers consistently underestimate "
            "how loved they are. The bottler pays too: suppressed "
            "emotion does not vanish but ferments, emerging as "
            "irritability, withdrawal, or sudden disproportionate upset "
            "over small things. Emotion researchers call this the "
            "ironic process of suppression - the harder feeling is "
            "pushed down, the more it distorts what comes out sideways.\n\n"
            "Exploding: the love is expressed all at once, at maximum "
            "volume, without attunement - the 2 a.m. declaration, the "
            "grand gesture as ambush, the flood of feeling that demands "
            "an immediate matching flood in return. The exploder's "
            "reasons feel urgent: the feeling is so big it cannot wait, "
            "and waiting feels like lying. The costs: the recipient is "
            "overwhelmed rather than moved - flooding triggers defense, "
            "not reception - and the relationship learns to brace for "
            "the next detonation instead of relaxing into steady "
            "warmth. Gottman's research on flooding shows that "
            "physiological overwhelm shuts down listening entirely; a "
            "flooded partner hears nothing, however loving the words.\n\n"
            "The middle path is not lukewarm love - it is regulated "
            "love: feeling fully, expressing steadily, in doses the "
            "beloved can receive. The bottler's practice is small daily "
            "transmissions: one honest sentence, one deliberate kindness, "
            "every day. The exploder's practice is the pause: feel it "
            "fully, write it down, sleep on it, deliver it at a human "
            "volume tomorrow. Both practices retrain the same thing - "
            "the timing and dosage of expression - and both preserve "
            "what bottling and exploding destroy: the beloved's ability "
            "to actually receive the love being offered."
        ),
        "how_it_works": (
            "Both patterns are regulation failures in opposite "
            "directions. Bottling is over-regulation: the expressive "
            "system is inhibited, but inhibition consumes cognitive "
            "resources and the unexpressed affect leaks as irritability "
            "or somatic tension - Gross's emotion-regulation research "
            "documents the costs of suppression to both parties. "
            "Exploding is under-regulation: arousal floods the system "
            "faster than the prefrontal cortex can modulate it, and the "
            "result bypasses the recipient's receptivity window - "
            "Gottman's diffuse physiological arousal shuts down the "
            "listening brain. Regulated expression is the calibrated "
            "middle: full feeling, modulated delivery, matched to the "
            "recipient's capacity in the moment."
        ),
        "key_points": [
            "Bottling: felt but never transmitted; reads as absence; ferments into irritability.",
            "Exploding: maximum volume without attunement; overwhelms instead of moving.",
            "Suppression has ironic costs; flooding shuts down the listening brain.",
            "The middle path is regulated love: full feeling, steady human-volume delivery.",
            "Practices: daily small transmissions for bottlers; feel-write-sleep-deliver for exploders.",
        ],
        "requirements": [
            "Both failure modes taught with their logic, costs, and mechanisms.",
            "No shaming: each pattern's reasons presented as understandable.",
            "Corrective practices concrete and small.",
            "The reception thesis: expression exists to be received.",
        ],
        "standards": [
            "Gross J.J. Emotion regulation: affective, cognitive, and social consequences. Psychophysiology. 2002;39(3):281-291.",
            "Gottman J.M. The Seven Principles for Making Marriage Work. New York: Crown; 1999.",
        ],
        "citations": [
            "Gross J.J. Emotion regulation: affective, cognitive, and social consequences. Psychophysiology. 2002;39(3):281-291.",
            "Gottman J.M. The Seven Principles for Making Marriage Work. New York: Crown; 1999.",
            "Wegner D.M. Ironic processes of mental control. Psychological Review. 1994;101(1):34-52.",
        ],
        "sig_lens": (
            "Through the Signature lens, bottling and exploding are the "
            "archive's two publishing failures: the manuscript never "
            "released, and the entire print run dumped on the doorstep "
            "at midnight. His canon says every record is the full file, "
            "so the Signature editions diagnose the failure precisely - "
            "not the feeling, which is complete in both cases, but the "
            "delivery. The Signature originals teach the publishing "
            "schedule that works: full feeling, steady editions, human "
            "volume, daily - because a record's purpose is to be read, "
            "and love's purpose is to be received. Signature-made, never "
            "presented as authentic public record."
        ),
    },
    {
        "key": "everyday-practices",
        "name": "Everyday Practices That Keep Love in Balance",
        "group": "healthy-expression",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Love is maintained the way gardens are: not by annual "
            "heroics but by daily tending. This record collects the "
            "small, research-backed practices that keep love in balance "
            "- each one tiny, each one load-bearing.\n\n"
            "The daily deposit: one deliberate act of kindness or "
            "attention per day, minimum. Gottman's 'turning toward' "
            "research shows relationships are built from thousands of "
            "micro-moments of responsiveness; the practice is simply to "
            "make sure today contains at least one on purpose. The "
            "remembered coffee, the unprompted text, the two-minute "
            "shoulder rub - small, daily, non-negotiable.\n\n"
            "The appreciation audit: name one specific thing you "
            "appreciate about the beloved, out loud, every day. "
            "Specificity is the active ingredient - 'thanks for dinner' "
            "is polite, 'I love how you remembered my meeting and asked "
            "about it' is nourishment. Positive-illusion research shows "
            "that voiced appreciation does not just reflect the bond, "
            "it constructs it.\n\n"
            "The repair habit: address small ruptures fast. The "
            "unanswered text, the sharp tone, the forgotten promise - "
            "repaired within the day, these stay small; left to sit, "
            "they compound. Gottman's repair attempts work best as a "
            "standing habit, not an emergency measure: 'that came out "
            "wrong, let me try again' is a sentence worth rehearsing.\n\n"
            "The novelty appointment: schedule something new together "
            "regularly - Aron's research says novel, arousing shared "
            "activities measurably refresh relationship quality. It need "
            "not be grand: a new walking route, a cuisine neither has "
            "tried, a skill learned badly together. Novelty is the "
            "antidote to habituation.\n\n"
            "The separate-selves maintenance: keep one friendship, one "
            "pursuit, one interior room that is yours alone. Love "
            "thrives between two whole people; fusion starves it. "
            "Self-expansion needs a self to expand from.\n\n"
            "The rest rule: tired love misreads everything. Sleep "
            "deprivation, hunger, and overload shrink the window of "
            "tolerance until ordinary friction feels like crisis. "
            "Tending the body - sleep, food, movement, quiet - is "
            "tending the love, because the same nervous system does "
            "both jobs.\n\n"
            "The weekly review: ten minutes, once a week - what worked, "
            "what stung, what is needed. Couples who debrief stay "
            "aligned; couples who do not drift on unspoken currents. "
            "Keep it short, keep it kind, keep it regular."
        ),
        "how_it_works": (
            "Practices work because love is a dynamic system, not a "
            "static trait - it needs continuous input to hold its "
            "state, the way a bicycle needs pedaling to stay upright. "
            "Each practice targets a known decay mechanism: deposits "
            "counter hedonic adaptation, appreciation counters the "
            "negativity bias, repair counters rupture accumulation, "
            "novelty counters habituation, separate-selves counters "
            "fusion, rest counters depleted regulation, review counters "
            "drift. None requires intensity; all require repetition. "
            "The compound interest of small inputs is the entire "
            "mechanism - which is why the practices are small enough "
            "to actually do."
        ),
        "key_points": [
            "Daily deposit: one deliberate kindness or attention, every day, on purpose.",
            "Appreciation audit: one specific voiced appreciation daily - specificity nourishes.",
            "Repair habit: small ruptures addressed fast, as routine not emergency.",
            "Novelty appointments and separate-selves maintenance counter habituation and fusion.",
            "Rest rule and weekly review: tend the body, debrief the bond.",
        ],
        "requirements": [
            "Seven practices, each tiny and research-backed.",
            "Each practice tied to the decay mechanism it counters.",
            "Concrete enough to do today: sentences to say, minutes to spend.",
            "The compound-interest thesis: small inputs, repeated, are the mechanism.",
        ],
        "standards": [
            "Gottman J.M. The Seven Principles for Making Marriage Work. New York: Crown; 1999.",
            "Aron A., Norman C.C., Aron E.N., McKenna C., Heyman R.E. Couples' shared participation in novel and arousing activities and experienced relationship quality. Journal of Personality and Social Psychology. 2000;78(2):273-284.",
        ],
        "citations": [
            "Gottman J.M. The Seven Principles for Making Marriage Work. New York: Crown; 1999.",
            "Aron A., Norman C.C., Aron E.N., McKenna C., Heyman R.E. Couples' shared participation in novel and arousing activities and experienced relationship quality. Journal of Personality and Social Psychology. 2000;78(2):273-284.",
            "Murray S.L., Holmes J.G., Griffin D.W. The benefits of positive illusions. Journal of Personality and Social Psychology. 1996;70(1):79-98.",
        ],
        "sig_lens": (
            "Through the Signature lens, everyday practices are the "
            "archive's maintenance schedule - the quiet daily work that "
            "keeps a million-record collection alive. His canon says "
            "never cut corners and never present a fraction as the "
            "whole, so the Signature editions prescribe the full "
            "tending: deposits, appreciation, repair, novelty, separate "
            "selves, rest, review - small, daily, non-negotiable. The "
            "Signature originals teach the gardener's truth: grandeur "
            "is annual, tending is daily, and it is the tending that "
            "decides what survives. Signature-made, never presented as "
            "authentic public record."
        ),
    },
    {
        "key": "recognizing-others",
        "name": "Reading Love in Others: Face, Body, Voice, and Behavior Cues",
        "group": "recognizing",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The earlier records taught love from the inside and the "
            "outside of one person. This record turns the lens around: "
            "how to recognize love in someone else - a friend, a "
            "partner, a family member - across four channels. "
            "Descriptive knowledge for understanding, never for "
            "diagnosing or labeling real people.\n\n"
            "Face: look for the cluster, not one feature. The soft "
            "sustained gaze plus the Duchenne smile plus the smooth "
            "brow, arriving together and lingering, is the facial "
            "signature. The light-up on your arrival - that sub-second "
            "brightening - is the single most honest facial cue, "
            "because it fires before control engages. Watch, too, for "
            "the gaze that follows you across rooms and the look that "
            "lingers a beat after the conversation ends.\n\n"
            "Body: read the geometry. Do they orient toward you - feet, "
            "torso, face - in groups? Do they close distance, find "
            "reasons for proximity, touch casually and often? Is their "
            "posture open around you and their movement synchronized "
            "with yours? The body channel is the hardest to fake, so "
            "when face and body disagree, trust the body.\n\n"
            "Voice: listen for the softening - lower pitch, slower "
            "tempo, warmer timbre when speaking to you versus others. "
            "Listen for your name said with lift, for the follow-up "
            "questions that prove listening, for the 'we' language and "
            "the joint stories. Voice carries what the face edits out: "
            "fatigue, tenderness, the catch in the throat at meaningful "
            "moments.\n\n"
            "Behavior: count the pattern, not the gesture. One grand "
            "romantic act proves little; a hundred small ones prove "
            "everything. Do they prioritize you with time and "
            "attention? Remember the small things? Show up at the "
            "high-stakes moments? Repair after conflict? The behavior "
            "channel is read across weeks, not moments - love's "
            "signature is consistency.\n\n"
            "Reading well means reading humbly. Every cue has "
            "alternative explanations: the gaze could be curiosity, the "
            "touch could be habit, the kindness could be character "
            "rather than love. The rule: look for convergence across "
            "channels and consistency across time, hold conclusions "
            "lightly, and when it matters, ask - the most reliable "
            "love-detector ever built is a direct, kind question."
        ),
        "how_it_works": (
            "Recognition works through cue integration: the observer's "
            "brain combines weak signals across channels into a "
            "judgment, weighting each by its reliability - which is why "
            "multi-channel convergence beats any single cue. Accuracy "
            "improves with familiarity (you learn a person's baseline) "
            "and degrades with motivated reasoning (wanting the answer "
            "to be yes). The humility rule has a mechanism too: "
            "thin-slice judgments are fast but noisy, and confirmation "
            "bias makes seekers find whatever they are looking for. "
            "Convergence plus time plus a direct question is the "
            "procedure that survives the biases."
        ),
        "key_points": [
            "Face: the cluster - soft gaze, Duchenne smile, smooth brow - plus the honest light-up.",
            "Body: geometry and proximity; when face and body disagree, trust the body.",
            "Voice: softened prosody, lifted name, follow-up questions, 'we' language.",
            "Behavior: pattern over gesture - consistency across weeks is the signature.",
            "Read humbly: convergence across channels, conclusions held lightly, ask when it matters.",
        ],
        "requirements": [
            "Four channels with concrete cues each.",
            "The convergence rule: cluster and consistency beat single cues.",
            "Humility and the alternative-explanations caution.",
            "Never diagnosing: understanding, not labeling, real people.",
        ],
        "standards": [
            "Ekman P., Friesen W.V. Unmasking the Face. Englewood Cliffs: Prentice-Hall; 1975.",
            "Ambady N., Rosenthal R. Thin slices of expressive behavior as predictors of interpersonal consequences. Psychological Bulletin. 1992;111(2):256-274.",
        ],
        "citations": [
            "Ekman P., Friesen W.V. Unmasking the Face. Englewood Cliffs: Prentice-Hall; 1975.",
            "Ambady N., Rosenthal R. Thin slices of expressive behavior as predictors of interpersonal consequences. Psychological Bulletin. 1992;111(2):256-274.",
            "Hall E.T. The Hidden Dimension. New York: Doubleday; 1966.",
        ],
        "sig_lens": (
            "Through the Signature lens, recognizing love in others is "
            "reading another archive's catalog - in a foreign hand, "
            "across four scripts: face, body, voice, behavior. His canon "
            "says never present a fraction as the whole, so the "
            "Signature editions demand the full read: convergence "
            "across channels, consistency across time, and the humility "
            "to hold conclusions lightly. The Signature originals add "
            "the archivist's final tool - the direct kind question - "
            "because even the best cataloging is a hypothesis until "
            "the author confirms it. Signature-made, never presented as "
            "authentic public record."
        ),
    },
    {
        "key": "supporting-others",
        "name": "Supporting Someone Who Is Feeling Love",
        "group": "recognizing",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Love is usually celebrated, but people feeling it - "
            "especially new, intense, or complicated love - often need "
            "support too. This record teaches supportive responses: "
            "what helps, in plain language.\n\n"
            "Receive the news warmly. When someone tells you they are "
            "in love, the first response sets everything: delight, "
            "curiosity, and taking it seriously. Dismissal ('it is just "
            "a crush'), interrogation, or instant practical objections "
            "teach them not to bring you their heart again. You can "
            "hold concerns for later; the announcement moment belongs "
            "to joy.\n\n"
            "Ask, do not assume. 'Tell me about them' beats a dozen "
            "leading questions. 'What do you love about this' invites "
            "the story; 'are you sure' invites defensiveness. Open "
            "questions let the person think out loud, which is often "
            "what they need most - love at high intensity benefits "
            "enormously from being narrated to a calm listener.\n\n"
            "Normalize without minimizing. 'That sounds wonderful and "
            "completely overwhelming - both can be true' validates the "
            "intensity without pathologizing it. New love genuinely "
            "disrupts sleep, appetite, and concentration; hearing that "
            "this is documented and normal steadies people who feared "
            "they were losing their minds.\n\n"
            "Guard the practical without crushing the feeling. If there "
            "are real concerns - breakneck speed, isolation from "
            "friends, red flags - raise them once, gently, as your "
            "perspective, then step back. 'I am so happy for you, and "
            "I want to say one thing as your friend...' followed by "
            "genuine stepping back preserves both the friendship and "
            "your credibility. Repeated warnings just build a wall "
            "between you and the person you are trying to protect.\n\n"
            "Show up for the whole arc. Celebrate the beginning, be "
            "patient through the intensity, and - crucially - be "
            "present if it ends. The aftershock needs witnesses who do "
            "not say 'I told you so' and do not rush the grief. "
            "Support across the arc is what makes you the person they "
            "call for the next love too.\n\n"
            "For complicated loves - unrequited, forbidden by "
            "circumstance, or mistimed - the support is steadier: "
            "acknowledge the reality of the feeling without feeding "
            "fantasies that harm, keep the person connected to the "
            "rest of their life, and trust time. You cannot argue "
            "someone out of love, but you can keep them company while "
            "the arc runs its course."
        ),
        "how_it_works": (
            "Support works through co-regulation and narrative "
            "processing. A calm, warm listener literally down-regulates "
            "the support-seeker's arousal - the attachment system's "
            "safe-haven function operating between friends. Narrating "
            "the feeling to an attentive other organizes it: the "
            "act of putting love into words engages prefrontal "
            "processing and reduces amygdala reactivity, the affect-"
            "labeling effect. Single, gentle concern-raising works "
            "because it registers without triggering defensiveness; "
            "repeated warnings trigger reactance, the motivational "
            "state that defends threatened freedoms - including the "
            "freedom to love."
        ),
        "key_points": [
            "Receive the news warmly: the announcement moment belongs to joy.",
            "Ask open questions; let them narrate the feeling to a calm listener.",
            "Normalize the intensity without minimizing it.",
            "Raise real concerns once, gently, as perspective - then step back.",
            "Show up for the whole arc, including the aftershock.",
        ],
        "requirements": [
            "Six supportive moves, each concrete and speakable.",
            "Complicated loves addressed: unrequited, mistimed, circumstantial.",
            "Mechanisms: co-regulation, affect labeling, reactance.",
            "The credibility thesis: restraint now preserves influence later.",
        ],
        "standards": [
            "Bowlby J. A Secure Base. New York: Basic Books; 1988.",
            "Lieberman M.D., Eisenberger N.I., Crockett M.J., Tom S.M., Pfeifer J.H., Way B.M. Putting feelings into words. Psychological Science. 2007;18(5):421-428.",
        ],
        "citations": [
            "Bowlby J. A Secure Base. New York: Basic Books; 1988.",
            "Lieberman M.D., Eisenberger N.I., Crockett M.J., Tom S.M., Pfeifer J.H., Way B.M. Putting feelings into words. Psychological Science. 2007;18(5):421-428.",
            "Brehm J.W. A Theory of Psychological Reactance. New York: Academic Press; 1966.",
        ],
        "sig_lens": (
            "Through the Signature lens, supporting someone in love is "
            "being the archive's reading room for another collection - "
            "a calm, warm, well-lit space where they can study their "
            "own newest acquisition. His canon says records must guard "
            "as well as teach, so the Signature editions hold both "
            "duties: celebrate the acquisition, and file the one gentle "
            "note of concern where it can be found later. The Signature "
            "originals stay open through the whole arc - beginning, "
            "intensity, and aftershock - because a reading room that "
            "closes when the weather turns was never really open. "
            "Signature-made, never presented as authentic public record."
        ),
    },
    {
        "key": "recognizing-mistakes",
        "name": "What Not to Do Around Love: Common Mistakes",
        "group": "recognizing",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Good intentions damage love regularly. This record lists "
            "the common mistakes people make around others' love - and "
            "around their own - so readers can stop making them.\n\n"
            "Mocking the feeling. Teasing someone about being in love - "
            "especially new, vulnerable love - teaches them to hide "
            "their heart from you. The mockery is usually affectionate "
            "in intent and wounding in effect: the lover hears that "
            "their deepest feeling is entertainment. If you would not "
            "mock their grief, do not mock their love.\n\n"
            "Rushing the timeline. 'When are you getting married,' "
            "'isn't it time,' 'slow down' - all attempts to run "
            "someone else's arc on your schedule. Love has its own "
            "pace, and pressure from the sidelines distorts it: rushed "
            "couples commit before they are ready or rebel by stalling. "
            "The sideline's job is witnessing, not scheduling.\n\n"
            "Making it about you. Turning their announcement into your "
            "anxiety ('but what about the holidays'), your story "
            "('that reminds me of my ex'), or your project (managing "
            "their relationship). Center the lover, not the audience.\n\n"
            "Testing the love. Manufacturing jealousy to 'check' "
            "feelings, picking fights to measure commitment, "
            "withdrawing to see if they chase - tests do not measure "
            "love, they damage it. Each test spends trust to buy "
            "information, and the exchange rate is terrible.\n\n"
            "Keeping score. Treating love as a ledger - who called "
            "last, who gave more, who owes what - converts a bond "
            "into a transaction. Research on communal versus exchange "
            "relationships shows that scorekeeping itself erodes the "
            "very closeness it tries to ensure. Give because it is "
            "yours to give; the accounting department is closed.\n\n"
            "Diagnosing from the sidelines. Telling someone what they "
            "feel ('you are just lonely,' 'that is not love, that is...') "
            "overrides their inner knowledge with your theory. This "
            "database's standing rule applies to everyone: describe, "
            "do not diagnose - especially not other people's hearts.\n\n"
            "The repair for every mistake on this list is the same: "
            "notice, name it plainly, apologize without defense, and "
            "change the pattern. 'I mocked something precious to you. "
            "I am sorry. It will not happen again.' Love forgives the "
            "mistake it can see being corrected."
        ),
        "how_it_works": (
            "Each mistake damages a specific mechanism. Mocking attacks "
            "the safety needed for vulnerability - the attachment system "
            "classifies the mocker as unsafe for tender feelings. "
            "Rushing imposes external pacing on an internal process, "
            "creating reactance. Self-centering starves the lover of "
            "attunement. Testing spends trust - the relationship's "
            "core currency - for low-grade information. Scorekeeping "
            "shifts the relationship frame from communal to exchange, "
            "and frames are self-fulfilling. Diagnosing overrides "
            "autonomy, the need to be the author of one's own inner "
            "life. The common thread: all six mistakes treat the "
            "lover's feeling as material for the mistake-maker's "
            "purposes rather than as a reality to be respected."
        ),
        "key_points": [
            "Do not mock the feeling - vulnerable love shown to you is a trust, not entertainment.",
            "Do not rush the timeline - witness the arc, do not schedule it.",
            "Do not make it about you, test the love, or keep score.",
            "Never diagnose from the sidelines - describe, do not label, others' hearts.",
            "Repair formula: notice, name it, apologize without defense, change the pattern.",
        ],
        "requirements": [
            "Six mistakes, each with its mechanism of damage.",
            "Concrete examples of each mistake in action.",
            "The common thread named: using their feeling for your purposes.",
            "A universal repair formula.",
        ],
        "standards": [
            "Clark M.S., Mills J. Interpersonal attraction in exchange and communal relationships. Journal of Personality and Social Psychology. 1979;37(1):12-24.",
            "Gottman J.M. The Seven Principles for Making Marriage Work. New York: Crown; 1999.",
        ],
        "citations": [
            "Clark M.S., Mills J. Interpersonal attraction in exchange and communal relationships. Journal of Personality and Social Psychology. 1979;37(1):12-24.",
            "Gottman J.M. The Seven Principles for Making Marriage Work. New York: Crown; 1999.",
            "Brehm J.W. A Theory of Psychological Reactance. New York: Academic Press; 1966.",
        ],
        "sig_lens": (
            "Through the Signature lens, the mistakes are the archive's "
            "handling errors - the ways well-meaning hands damage the "
            "records: mocking creases the page, rushing skips the "
            "cataloging, testing spends the binding, scorekeeping "
            "converts the gift collection into a ledger. His canon says "
            "data lock-in protects every record, and the Signature "
            "editions extend the principle to people: another's feeling "
            "is their record, not your material. The Signature "
            "originals teach the handling rules plainly - and the "
            "repair formula, because even careful hands sometimes slip. "
            "Signature-made, never presented as authentic public record."
        ),
    },
    {
        "key": "related-emotions",
        "name": "Loves Nearest Neighbors: Related Emotions and How to Tell Them Apart",
        "group": "related-and-mixes",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Love's neighborhood is crowded, and the neighbors get "
            "confused for each other constantly. This record maps the "
            "nearest neighbors and teaches the distinctions - because "
            "calling a feeling by its right name is the first step to "
            "handling it rightly.\n\n"
            "Liking versus loving. Psychologist Zick Rubin drew the "
            "classic line: liking is respect and warm evaluation; loving "
            "adds need, exclusivity, and self-sacrifice. You can like "
            "dozens deeply; love narrows and deepens. The test: liking "
            "enjoys the person's company, love grieves their absence "
            "and reorganizes life around their welfare.\n\n"
            "Infatuation versus love. Infatuation is love's "
            "high-intensity, low-knowledge cousin: all the arousal, "
            "none of the deep knowing. Tennov's limerence research maps "
            "it precisely - intrusive thinking, acute sensitivity, "
            "idealization. The distinction is time and knowledge: "
            "infatuation fades when reality arrives; love deepens when "
            "reality arrives. Both feel enormous at the start; only one "
            "survives the beloved being fully known.\n\n"
            "Companionate versus passionate love. Hatfield's "
            "distinction: passionate love is the intense, desirous, "
            "absorbing state; companionate love is the steady, warm, "
            "committed bond. They are not rivals but phases and layers - "
            "most lasting loves contain both, in shifting proportions "
            "across the years.\n\n"
            "Love versus attachment (in the narrow sense). Attachment "
            "is the bond's persistence system - the distress at "
            "separation, the safe-haven seeking. Love includes "
            "attachment but adds the warm appraisal and the care "
            "motivation. You can be attached without much warmth (the "
            "stale marriage, the duty-bound tie) and warm without much "
            "attachment (the fond distant friend). The full love has "
            "both.\n\n"
            "Love versus desire. Desire wants; love cherishes. They "
            "travel together in romance and can each exist without the "
            "other. Confusing them causes two classic errors: "
            "mistaking desire's fade for love's death, and mistaking "
            "desire's presence for love's guarantee.\n\n"
            "Love versus neediness. Neediness clings; love holds. The "
            "felt difference: neediness is anxious and grasping, "
            "focused on what the other provides; love is generous and "
            "steady, focused on the other's welfare. They can coexist "
            "in one heart - love plus insecurity - and the work is to "
            "feed the love while calming the insecurity, not to "
            "confuse the two.\n\n"
            "Love's opposites, for the map's far edge: hate (the "
            "active wish for ill, often love's own appraisal inverted "
            "by betrayal), disgust (the expulsion response, love's "
            "approach reversed), and indifference (the true opposite - "
            "not hate but the absence of salience, the beloved filed "
            "under 'nothing')."
        ),
        "how_it_works": (
            "Distinctions work by isolating components. Rubin's "
            "liking-loving scale factor-analyzed into separate "
            "dimensions, proving they are different constructs, not "
            "different amounts. Infatuation versus love separates on "
            "the knowledge axis: idealization without data versus "
            "appraisal with data. Passionate versus companionate "
            "separates on the arousal axis. Love versus attachment "
            "separates warmth-appraisal from persistence-system. Love "
            "versus desire separates cherishing motivation from wanting "
            "motivation - different reward circuitry, overlapping in "
            "romance. Each distinction is a controlled comparison "
            "holding some components constant while varying one - the "
            "same method the ladder has used throughout."
        ),
        "key_points": [
            "Liking enjoys company; love grieves absence and reorganizes life.",
            "Infatuation fades when reality arrives; love deepens when reality arrives.",
            "Passionate and companionate are phases and layers, not rivals.",
            "Love includes attachment but adds warm appraisal and care motivation.",
            "Desire wants, love cherishes - confusing them causes the two classic errors.",
            "Indifference, not hate, is love's true opposite.",
        ],
        "requirements": [
            "Seven distinctions, each with its separating axis.",
            "The right-name thesis: naming rightly precedes handling rightly.",
            "Opposites mapped for the far edge of the map.",
            "Research grounding: Rubin, Tennov, Hatfield, Bowlby.",
        ],
        "standards": [
            "Rubin Z. Measurement of romantic love. Journal of Personality and Social Psychology. 1970;16(2):265-273.",
            "Hatfield E., Rapson R.L. Love, Sex, and Intimacy. New York: HarperCollins; 1993.",
            "Tennov D. Love and Limerence. New York: Stein and Day; 1979.",
        ],
        "citations": [
            "Rubin Z. Measurement of romantic love. Journal of Personality and Social Psychology. 1970;16(2):265-273.",
            "Hatfield E., Rapson R.L. Love, Sex, and Intimacy. New York: HarperCollins; 1993.",
            "Tennov D. Love and Limerence. New York: Stein and Day; 1979.",
            "Bowlby J. Attachment and Loss, Vol. 1: Attachment. New York: Basic Books; 1969.",
        ],
        "sig_lens": (
            "Through the Signature lens, the neighbors are the archive's "
            "adjacent shelves - each holding a record that looks like "
            "love's from a distance and differs on close reading. His "
            "canon says every record is the full file, so the Signature "
            "editions refuse the shelving error: infatuation misfiled "
            "under love, desire misfiled under love, neediness misfiled "
            "under love - each gets its true call number. The Signature "
            "originals teach the separating axes as the cataloger's "
            "finest tools, because a misfiled feeling gets mishandled, "
            "and mishandled feelings are how hearts get hurt. "
            "Signature-made, never presented as authentic public record."
        ),
    },
    {
        "key": "love-mixes",
        "name": "Love Blended: Emotion Mixes, Plutchik-Style Dyads",
        "group": "related-and-mixes",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Love is itself a blend, and it blends further - with "
            "nearly every emotion on the wheel. This record mixes love "
            "with four partners, Plutchik-style, describing what each "
            "blend feels like, looks like, and does.\n\n"
            "Love plus fear: jealousy and anxious devotion. Feels like "
            "love with an alarm bell - warmth undercut by vigilance, "
            "tenderness braced for loss. Looks like: the searching gaze, "
            "the too-casual questions, the body that hovers. Does: "
            "monitoring, reassurance-seeking, sometimes the "
            "self-fulfilling push that creates the feared loss. The "
            "healthy version is a flicker that passes; the entrenched "
            "version needs the fear addressed, not the love doubted.\n\n"
            "Love plus sadness: compassion and grief. Feels like "
            "tenderness with weight - the ache of caring about someone "
            "who suffers. Looks like: soft eyes gone wet, the forward "
            "lean, the hand that reaches without thinking. Does: "
            "comforting, helping, staying - and, when the suffering is "
            "unfixable, the slow drain of the helpless witness. In its "
            "grief form - love for someone gone - it is the heaviest "
            "blend on this list and the most human.\n\n"
            "Love plus anger: protective fierceness and righteous "
            "devotion. Feels like warmth with a blade - the surge that "
            "says 'not them, never them.' Looks like: the body "
            "planting itself between beloved and threat, the voice "
            "dropping half an octave, the face love-soft toward the "
            "beloved and flint toward the danger. Does: defending, "
            "confronting, sacrificing safety for the other's. Misfires "
            "when the blade turns inward on the bond - anger at the "
            "beloved for being threatened, which is fear's cascade "
            "wearing anger's face.\n\n"
            "Love plus surprise: delight and wonder. Feels like love "
            "made new - the beloved suddenly strange and marvelous "
            "again. Looks like: the laugh of disbelief, the wide eyes, "
            "the 'you are incredible' stare. Does: re-enchanting - this "
            "blend is the antidote to habituation, which is why "
            "surprises, travel, and witnessing the beloved shine in "
            "unfamiliar contexts refresh long loves. Couples who "
            "regularly surprise each other are dosing this blend on "
            "purpose.\n\n"
            "The blending rule: the partner emotion does not replace "
            "love, it flavors it - the appraisal 'this one matters' "
            "stays constant while fear, sadness, anger, or surprise "
            "adds its action tendency. Read any intense episode by "
            "asking: love plus what? The answer simplifies everything "
            "after it."
        ),
        "how_it_works": (
            "Blends work by co-activation with a stable core: love's "
            "appraisal and motivation stay online while the partner "
            "emotion contributes its appraisal and action tendency - "
            "fear's vigilance, sadness's withdrawal-toward, anger's "
            "approach-against, surprise's orienting. Plutchik's dyad "
            "model formalizes this as adjacent primaries combining into "
            "named compounds. The subjective unity - feeling one thing, "
            "not two - comes from the brain's integration of parallel "
            "affective processes into a single conscious state. The "
            "'love plus what' reading works because it reverses the "
            "integration: naming the partner emotion separates the "
            "blend back into its ingredients, restoring clarity."
        ),
        "key_points": [
            "Love + fear: jealousy - warmth with an alarm bell; address the fear, not the love.",
            "Love + sadness: compassion and grief - tenderness with weight; the heaviest, most human blend.",
            "Love + anger: protective fierceness - warmth with a blade; righteous when aimed at the threat.",
            "Love + surprise: delight - love made new; the antidote to habituation.",
            "The reading rule: love plus what? Name the partner, simplify the episode.",
        ],
        "requirements": [
            "Four blends, each with feel, look, and does.",
            "Plutchik-style dyad framing.",
            "Healthy and misfire forms for each blend.",
            "The un-blending rule as the practical takeaway.",
        ],
        "standards": [
            "Plutchik R. Emotion: A Psychoevolutionary Synthesis. New York: Harper & Row; 1980.",
            "Lazarus R.S. Emotion and Adaptation. New York: Oxford University Press; 1991.",
        ],
        "citations": [
            "Plutchik R. Emotion: A Psychoevolutionary Synthesis. New York: Harper & Row; 1980.",
            "Lazarus R.S. Emotion and Adaptation. New York: Oxford University Press; 1991.",
            "Bowlby J. Attachment and Loss, Vol. 3: Loss. New York: Basic Books; 1980.",
        ],
        "sig_lens": (
            "Through the Signature lens, blends are the archive's "
            "composite records - two entries bound in one volume, read "
            "as a single text. His canon says every database teaches "
            "from many angles, so the Signature editions read each "
            "blend three ways: what it feels like inside, what it looks "
            "like outside, what it does in the world. The Signature "
            "originals keep the un-blending rule as the master key to "
            "the composites shelf - 'love plus what' - because an "
            "archivist who can separate a bound volume into its true "
            "entries can never be confused by its cover. Signature-made, "
            "never presented as authentic public record."
        ),
    },
    {
        "key": "full-simulation",
        "name": "The Full Simulation: Love from Trigger Through Peak to Resolution",
        "group": "related-and-mixes",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The showcase piece: a rich multi-scene simulation walking "
            "love from trigger through peak to resolution, using every "
            "layer of the ladder. Read it as the archive demonstrating "
            "everything it has taught.\n\n"
            "Scene one - the trigger. It is October, and the community "
            "garden is putting itself to bed for winter. June, "
            "sixty-three, widowed two years, has come to pull her "
            "tomato stakes. At the next plot, Theo - seventy, new to "
            "the garden, new to the neighborhood - is struggling with "
            "a wheelbarrow and laughing at himself. He looks up, "
            "catches her eye, and does the eyebrow flash without "
            "knowing it has a name. 'I am better with spreadsheets than "
            "soil,' he says. She laughs - a real one, the first in "
            "weeks - and shows him how to brace the barrow. Proximity, "
            "kindness-in-a-small-need, the helper's high running in "
            "reverse: she helps, and her heart concludes it must be "
            "fond of him. The trigger is unremarkable. That is how "
            "triggers usually are.\n\n"
            "Scene two - the quickening. Over the next month the "
            "garden becomes geography: their plots adjacent, their "
            "Saturdays aligned. Mere exposure does its quiet work. "
            "They trade seedlings, then stories - his late wife's "
            "roses, her late husband's terrible puns. Mutual "
            "self-disclosure, Aron's accelerant, operating at the speed "
            "of weeding. Her body starts the orientation: feet aiming "
            "at him across the compost bin, the light-up when his old "
            "truck rattles in. Low-intensity love, Thursday-evening "
            "volume: the warm pressure behind the ribs, the diagonal-"
            "sandwich instinct already storing that he takes his tea "
            "with too much sugar.\n\n"
            "Scene three - the peak. December: the garden's holiday "
            "potluck, string lights in the bare trees. He brings a "
            "pie with a soggy bottom and presents it like a trophy; "
            "she laughs until she cries, and in the laughing-crying "
            "the feeling crests. Moderate-to-high intensity now: "
            "racing heart when he texts, the 3 a.m. wakefulness of a "
            "sixty-three-year-old who thought she was done with all "
            "that. Love plus joy at full blend - the delight dyad, "
            "love plus surprise when he reveals he has been secretly "
            "learning her late husband's puns to make her laugh. The "
            "face at this volume: the public glow, the gaze that "
            "follows him across the crowded hall.\n\n"
            "Scene four - the complication. January: her daughter "
            "visits and goes quiet. 'Mom, it has been two years. Are "
            "you sure you are not just lonely.' The love-plus-fear "
            "cascade fires in June for the first time: vigilance, the "
            "2 a.m. inventory of doubts. Is this love or neediness - "
            "the neighbor distinction from the map, suddenly personal. "
            "She chain-reads it: the fear is real, the love is real, "
            "they are two records bound in one volume. She does the "
            "repair habit on herself first - names the fear to Theo, "
            "plainly, over tea: 'My daughter is worried I am confusing "
            "loneliness for love.' He listens - the genuine mm-hm - "
            "and says, 'Maybe bring her to the garden in spring. Let "
            "her see the soil.' No explosion, no bottling: regulated "
            "expression, say plus show.\n\n"
            "Scene five - the resolution. April: the daughter comes to "
            "the garden. She watches her mother and Theo argue "
            "happily about tomato varieties, finishing each other's "
            "sentences, moving in the unconscious synchrony of people "
            "who have weeded a hundred rows together. She sees the "
            "daily deposits, the appreciation spoken out loud ('your "
            "mother remembered my terrible knees and brought the stool "
            "- who does that'), the repair made routine. At the "
            "potluck she takes June's hand and says, 'Okay. I see it.' "
            "The love has settled into its companionate volume - "
            "warm, steady, obvious to everyone in the room. The arc "
            "completes: trigger, quickening, peak, complication, "
            "resolution. Nothing about it was a thunderbolt. Everything "
            "about it was love."
        ),
        "how_it_works": (
            "The simulation integrates the ladder's mechanisms in "
            "sequence. Scene one fires the classic and surprise "
            "triggers (proximity, kindness, helper's high, eyebrow "
            "flash). Scene two runs exposure, disclosure, "
            "self-expansion, and the body signature at low volume. "
            "Scene three crests through arousal, the joy blend, and "
            "the public facial dial. Scene four triggers the "
            "fear cascade and demonstrates chain-reading, the "
            "neighbor distinctions, and regulated expression. Scene "
            "five shows settling, the daily practices compounded, and "
            "recognition by a third party across all four channels. "
            "Each scene's psychology is the corresponding record's "
            "mechanism, dramatized - the simulation is the ladder "
            "proving it can walk."
        ),
        "key_points": [
            "Five scenes: trigger, quickening, peak, complication, resolution.",
            "Every ladder layer appears: triggers, body, face, volume, blends, cascades, practices.",
            "The complication demonstrates chain-reading and regulated expression under pressure.",
            "Resolution shows settling as success and recognition across all channels.",
            "Nothing was a thunderbolt; everything was love - the ladder's thesis in one story.",
        ],
        "requirements": [
            "Multi-scene arc with named characters and concrete detail.",
            "Each scene traceable to specific earlier records' mechanisms.",
            "The complication resolved with ladder-taught skills, not luck.",
            "Showcase quality: the archive demonstrating everything it teaches.",
        ],
        "standards": [
            "Aron A., Melinat E., Aron E.N., Vallone R., Bator R. The experimental generation of interpersonal closeness. Personality and Social Psychology Bulletin. 1997;23(4):363-377.",
            "Hatfield E., Rapson R.L. Love, Sex, and Intimacy. New York: HarperCollins; 1993.",
            "Gottman J.M. The Seven Principles for Making Marriage Work. New York: Crown; 1999.",
        ],
        "citations": [
            "Aron A., Melinat E., Aron E.N., Vallone R., Bator R. The experimental generation of interpersonal closeness. Personality and Social Psychology Bulletin. 1997;23(4):363-377.",
            "Hatfield E., Rapson R.L. Love, Sex, and Intimacy. New York: HarperCollins; 1993.",
            "Gottman J.M. The Seven Principles for Making Marriage Work. New York: Crown; 1999.",
            "Bowlby J. A Secure Base. New York: Basic Books; 1988.",
        ],
        "sig_lens": (
            "Through the Signature lens, the full simulation is the "
            "archive's grand reading - all thirty-four records performed "
            "as one story, the collection proving it is alive. His canon "
            "says every record is the full file and the ladder runs "
            "simple to most complex, so the Signature editions stage the "
            "showcase at the ladder's summit: June and Theo's year, from "
            "the wheelbarrow to the spring garden, with every mechanism "
            "labeled in the margins. The Signature originals close the "
            "ladder where it opened - love as the home frequency - now "
            "with the whole archive humming behind it. Signature-made, "
            "never presented as authentic public record."
        ),
    },
]
