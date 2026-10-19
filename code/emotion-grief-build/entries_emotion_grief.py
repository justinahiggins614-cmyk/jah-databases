#!/usr/bin/env python3
"""Seed entries for The Grief Emotion Database (public) and
The Grief Emotion Signature Database (Signature edition).

34 ladder-ordered records each, following the shared emotion template:
what grief IS -> first-person simulation -> body signals -> facial
expression -> triggers -> behavior -> healthy expression -> recognizing
it in others -> related emotions and mixes -> complex behavioral simulation.

Public records are real, fact-checked psychology knowledge, descriptive
and educational only: the archive describes and simulates the emotion of
grief; it never diagnoses real people and never labels any real person
with an emotional state. Guidance stays general, safe, and everyday.

Signature records are the same ladder through the Signature lens -
his original Signature interpretation of grief: the covenant paid in
full measure, the torn thread and the reweaving, every loss honored as
a making. Titles are suffixed " (Signature Edition)", src is
"signature", and SIG_TAIL marks them as Signature-made, never
presented as authentic public record.

Tiers: Foundations (records 1-6), Compounded (records 7-18),
Advanced (records 19-34). ladder_rank runs 1-10 non-decreasing.

Citations below are landmark psychology references cited per record.
Handled with exceptional care, warmth, and respect throughout.
"""

CIT_KUBLER = ("Kubler-Ross E. On Death and Dying. Macmillan; 1969. "
              "Described five commonly observed patterns in response to loss "
              "(denial, anger, bargaining, depression, acceptance), originally "
              "studied in people facing terminal illness and later observed "
              "more broadly in grief.")
CIT_BOWLBY = ("Bowlby J. Attachment and Loss, Vol. 3: Loss - Sadness and "
              "Depression. Basic Books; 1980. Attachment behavior and the "
              "protest-despair-detachment sequence observed after separation "
              "and loss.")
CIT_DUAL = ("Stroebe M, Schut H. The dual process model of coping with "
            "bereavement: rationale and description. Death Studies; 1999. "
            "Oscillation between loss-oriented and restoration-oriented "
            "coping.")
CIT_WORDEN = ("Worden JW. Grief Counseling and Grief Therapy. 4th ed. "
              "Springer; 2008. The four tasks of mourning: accept the "
              "reality of the loss, process the pain, adjust to a world "
              "without the deceased, and find an enduring connection while "
              "embarking on a new life.")
CIT_BONANNO = ("Bonanno GA. The Other Side of Sadness. Basic Books; 2009. "
               "Documents resilience as the most common response to loss, "
               "with varied grief trajectories over time.")
CIT_NEIMEYER = ("Neimeyer RA, editor. Meaning Reconstruction and the "
                "Experience of Loss. American Psychological Association; "
                "2001. Grief as the work of reconstructing meaning after "
                "loss.")
CIT_PARKES = ("Parkes CM. Bereavement: Studies of Grief in Adult Life. 3rd "
              "ed. Routledge; 1996. Phases of grief and the psychosocial "
              "transition of bereavement.")
CIT_SHEAR = ("Shear MK. Complicated grief. New England Journal of Medicine; "
             "2015. Reviews persistent, impairing grief and its features, "
             "described here for educational context only.")
CIT_APA = ("American Psychological Association. APA Dictionary of "
           "Psychology. 2nd ed. American Psychological Association; 2015. "
           "Definitions of grief, mourning, and bereavement.")
CIT_EKMAN = ("Ekman P. Emotions Revealed: Recognizing Faces and Feelings to "
             "Improve Communication and Emotional Life. Times Books; 2003. "
             "Facial expressions of sadness and distress and their "
             "universal features.")
CIT_PLUTCHIK = ("Plutchik R. Emotion: A Psychoevolutionary Synthesis. "
                "Harper and Row; 1980. The wheel of emotions: basic "
                "emotions, intensities, and dyads of mixed emotions.")
CIT_DSM = ("American Psychiatric Association. Diagnostic and Statistical "
           "Manual of Mental Disorders. 5th ed., text revision. American "
           "Psychiatric Association; 2022. Describes prolonged grief "
           "disorder criteria; included here for educational context only, "
           "never for diagnosing any person.")
CIT_STROEBE_HB = ("Stroebe MS, Hansson RO, Schut H, Stroebe W, editors. "
                  "Handbook of Bereavement Research and Practice: Advances "
                  "in Theory and Intervention. American Psychological "
                  "Association; 2008.")
CIT_RANDO = ("Rando TA. Treatment of Complicated Mourning. Research Press; "
             "1993. The six R processes of mourning and complications of "
             "grief, described here for educational context only.")

SIG_TAIL = ("Signature original - his original Signature interpretation of "
            "grief: every loss a torn thread in the weave, every grief the "
            "price of a covenant kept, every healing a reweaving. Clearly "
            "labeled Signature-made, never presented as authentic public "
            "record.")

ENTRIES = [
    {
        "key": "what_grief_is",
        "name": "What Grief Is: A Plain-Language Definition",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Grief is the whole-body response to loss. It is what happens "
            "inside a person when something or someone that mattered is gone: "
            "a death, the end of a relationship, a lost home, a lost ability, "
            "a lost dream. Grief is not one single feeling - it is a whole "
            "weather system of feelings, body signals, thoughts, and behaviors "
            "that arrive together after a loss. Sadness is the most familiar "
            "part, but grief also carries shock, numbness, anger, guilt, "
            "longing, fear, and sometimes even relief, all in shifting "
            "mixtures. Psychologists distinguish three close words. "
            "Bereavement is the state of having lost someone or something. "
            "Mourning is the outward, often culturally shaped expression of "
            "that loss - the rituals, the clothes, the gatherings, the ways "
            "a community shows what happened. Grief is the inner experience "
            "itself: the thoughts, feelings, and body sensations of the person "
            "going through the loss. Grief is a normal human response, not a "
            "disorder and not a failure. It shows up because the lost thing "
            "mattered, and the depth of the grief usually matches the depth "
            "of the attachment. A person can grieve things that are not "
            "deaths: a marriage ending, a career lost, a friendship faded, a "
            "hometown left behind, health changed by illness or injury, a "
            "future that will not happen now. These are all real losses, and "
            "the grief they bring is real too. Grief is also different from "
            "depression in an important way: grief comes in waves tied to the "
            "loss, with moments of warmth and even laughter between the hard "
            "parts, and it centers on missing what is gone. Perhaps the most "
            "useful single sentence about grief is this: grief is love with "
            "nowhere to go, still looking for the person or thing it loved. "
            "This database describes and simulates that experience for "
            "learning. It never diagnoses anyone, and reading about grief is "
            "not the same as judging a real persons state."),
        "sig_lens": (
            "In the Signature view, grief is the covenant paid in full "
            "measure: every loss proves a bond was real, and the weight of "
            "the grief is the exact weight of what was loved. His Signature "
            "science treats grief not as a breakdown but as the loom at "
            "work - the torn thread named, honored, and rewoven into a new "
            "pattern that still carries the old colors."),
        "how_it_works": (
            "Grief works through the attachment system. Humans bond deeply "
            "with people, places, roles, and dreams, and the brain builds "
            "its daily expectations around those bonds: the person will be "
            "there, the routine will continue, the future will arrive. A "
            "loss breaks those expectations, and the mind keeps reaching "
            "for what is gone - expecting the familiar voice, planning "
            "around the familiar presence - and each reach meets absence. "
            "That repeated meeting of absence is the engine of grief. "
            "Attachment researcher John Bowlby described the sequence "
            "often observed after separation: protest (searching, anger, "
            "restlessness), despair (withdrawal, sadness, disorganization), "
            "and eventually reorganization (new patterns forming). Modern "
            "grief research, including the dual process model, describes "
            "grieving people oscillating between loss-oriented coping "
            "(feeling the pain, remembering, yearning) and "
            "restoration-oriented coping (handling new tasks, building a "
            "changed life). Healing is not forgetting; it is the slow "
            "building of a life in which the loss has a place. The body "
            "joins in because emotion is embodied: stress hormones rise, "
            "sleep and appetite shift, and the immune and cardiovascular "
            "systems feel the strain. All of this is the machinery of a "
            "normal response doing its work."),
        "key_points": [
            "Grief is the whole-body response to loss: feelings, body signals, thoughts, and behaviors arriving together.",
            "Bereavement is the state of loss, mourning is its outward expression, grief is the inner experience.",
            "Grief follows any deep loss, not only death: relationships, homes, health, roles, and futures can all be grieved.",
            "Grief is a normal human response, not a disorder and not a personal failure.",
            "The engine of grief is attachment: the mind keeps reaching for what is gone and meeting absence.",
        ],
        "requirements": [
            "No special equipment; this record is for reading and reflection",
            "A quiet moment to take in a careful definition",
            "Willingness to treat grief as normal rather than pathological",
            "No diagnosing of any real person from these descriptions",
        ],
        "standards": [
            "Descriptive and educational language only; no diagnostic claims",
            "Follows the bereavement/mourning/grief terminology of the APA Dictionary of Psychology",
        ],
        "citations": [CIT_APA, CIT_BOWLBY, CIT_WORDEN],
    },
    {
        "key": "emotion_family",
        "name": "Where Grief Sits in the Emotion Family",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Grief is not one of the simplest basic emotions; it is a "
            "complex emotion built from simpler ones. Emotion researchers "
            "usually list a small set of basic emotions - joy, sadness, "
            "anger, fear, surprise, disgust - that appear across cultures, "
            "show in the face early in life, and serve clear survival "
            "functions. Grief grows mainly out of sadness, the basic "
            "emotion of loss, but it recruits several others as it unfolds. "
            "From sadness it takes the heaviness, the tears, the low "
            "energy, the inward turn. From anger it takes protest: the "
            "furious why, the restlessness, the searching. From fear it "
            "takes the dread of a changed world and the anxiety about "
            "facing it alone. From love - which feeds emotion but is "
            "itself more than an emotion - it takes the longing, the "
            "continued attachment that refuses to let go. On Plutchiks "
            "wheel of emotions, grief sits in the sadness family at higher "
            "intensity and longer duration: pensiveness deepens to sadness, "
            "sadness deepens to grief. Think of grief as a chord rather "
            "than a single note. Sadness is the root note, always present. "
            "Around it sound the other notes - anger, guilt, fear, longing, "
            "sometimes relief - and which notes are loudest changes from "
            "day to day and person to person. That is why two grieving "
            "people can look so different: one plays mostly the anger "
            "string, another mostly the longing string, both are playing "
            "grief. Grief is also closely related to its neighbors. "
            "Mourning is its public performance. Nostalgia is griefs "
            "gentler cousin, sweetened by distance. Melancholy is a longer, "
            "quieter, more philosophical sadness without a single sharp "
            "loss. Regret looks backward at choices; grief looks at absence. "
            "Knowing griefs family helps a learner recognize it in its "
            "many disguises - including the angry, numb, or oddly cheerful "
            "ones - and helps keep it distinct from its neighbors."),
        "sig_lens": (
            "His Signature science draws the emotion family as a tapestry "
            "of threads: grief is the dark thread that runs through many "
            "colors, borrowing sadness for its depth, anger for its edge, "
            "and love for its refusal to fade. In the Signature view the "
            "complex emotions are the master weavings - and grief is among "
            "the most intricate, because it weaves nearly the whole loom."),
        "how_it_works": (
            "Complex emotions form when basic emotion programs combine "
            "with appraisal - the minds judgment about what happened and "
            "what it means. A loss is appraised as important, irreversible, "
            "and personal, and that appraisal summons sadness first. But "
            "appraisal keeps working: if the loss feels unfair, anger "
            "joins; if the person feels they could have prevented it, "
            "guilt joins; if the future feels uncertain, fear joins; if "
            "attachment remains strong, longing joins. Each recruited "
            "emotion brings its own body program - anger brings heat and "
            "tension, fear brings alertness, sadness brings heaviness - so "
            "griefs physical signature is a blend, which is why it feels "
            "so different from plain sadness and so different from person "
            "to person. Duration also matters: basic emotions are brief "
            "programs measured in minutes, while grief is a mood-scale "
            "process measured in months, because the appraisal (something "
            "irreplaceable is gone) does not expire. The chord keeps "
            "sounding until the mind builds a new model of the world that "
            "includes the absence - what researchers call reorganization "
            "or meaning reconstruction."),
        "key_points": [
            "Grief is a complex emotion built mainly from sadness, with anger, fear, guilt, and longing recruited as it unfolds.",
            "Think of grief as a chord: sadness is the root note, other emotions sound around it in changing mixtures.",
            "Grief is distinguished from neighbors: mourning (outward), nostalgia (sweetened), melancholy (diffuse), regret (about choices).",
            "Basic emotions last minutes; grief lasts months because its appraisal - something irreplaceable is gone - does not expire.",
            "Two grieving people can look very different because different notes of the chord sound loudest.",
        ],
        "requirements": [
            "Familiarity with the basic emotions: joy, sadness, anger, fear, surprise, disgust",
            "No special equipment; this record is for reading and reflection",
            "Openness to grief as a blend rather than a single pure feeling",
            "No diagnosing of any real person from these descriptions",
        ],
        "standards": [
            "Emotion-family framing follows Plutchiks wheel of emotions",
            "Descriptive and educational language only; no diagnostic claims",
        ],
        "citations": [CIT_PLUTCHIK, CIT_EKMAN, CIT_APA],
    },
    {
        "key": "intensity_volumes",
        "name": "The Same Grief at Different Volumes: Mild, Moderate, and Intense",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The same grief can play at very different volumes, and the "
            "volume changes what the grief feels like and what it asks of "
            "the person. At mild volume, grief is a background hum. The "
            "person functions, works, laughs, and mostly feels steady, but "
            "the loss surfaces in small waves: a pang at a familiar song, "
            "a quiet moment staring out a window, a brief catch in the "
            "throat when the absent one is mentioned. Daily life continues "
            "almost normally; the grief is present the way a healed "
            "fracture aches before rain - noticeable, real, but not "
            "stopping anything. At moderate volume, grief takes the front "
            "of the mind several times a day. Concentration slips. The "
            "person may cry without full warning, feel suddenly exhausted "
            "in the afternoon, snap at small frustrations, or find social "
            "gatherings draining. Sleep may be lighter and mornings "
            "heavier. Life continues, but it costs more effort, and the "
            "person often describes feeling like they are moving through "
            "thicker air. At intense volume, grief fills the whole field "
            "of awareness. The body feels leaden or hollow; appetite and "
            "sleep are disrupted; simple tasks like answering messages or "
            "making food feel enormous. Waves of crying, shaking, or "
            "numbness can arrive with little warning, and the person may "
            "feel disoriented, forgetful, or unlike themselves. Intense "
            "grief is exhausting in the way a long illness is exhausting. "
            "The volume usually follows the shape of the loss and its "
            "circumstances - sudden, violent, or ambiguous losses tend "
            "louder; losses with time to prepare and strong support tend "
            "quieter - but there are no rules, and the same person moves "
            "between volumes across a single week. Volume is not a measure "
            "of love: quiet grief can hold enormous love, and loud grief "
            "is not more virtuous. It is simply how this loss is sounding "
            "in this person at this time. Recognizing the volume helps "
            "everyone involved respond with the right scale of care: mild "
            "grief wants gentle acknowledgment, moderate grief wants "
            "patience and practical help, intense grief wants steady "
            "presence and, when the person asks, professional support."),
        "sig_lens": (
            "His Signature science reads the volumes as the depth of the "
            "well: mild grief ripples the surface, moderate grief stirs "
            "the middle waters, intense grief reaches the cold deep where "
            "the light barely goes. In the Signature view every volume is "
            "honest work - the shallow ripple and the deep dive are both "
            "the loom measuring what was lost, and no depth is more noble "
            "than another."),
        "how_it_works": (
            "Intensity in grief tracks several dials at once. The first is "
            "attachment strength: the more central the lost person or thing "
            "was to daily life and identity, the louder the grief. The "
            "second is the suddenness and nature of the loss: sudden and "
            "traumatic losses spike the volume because the mind had no "
            "time to begin its slow updating. The third is secondary "
            "losses: a death that also removes income, housing, or daily "
            "companionship stacks losses, and each adds volume. The fourth "
            "is support and rest: exhaustion, isolation, and new stress "
            "turn the volume up, while sleep, food, trusted company, and "
            "manageable days turn it down. The fifth is time and triggers: "
            "fresh losses are louder, anniversaries and reminders spike "
            "the volume temporarily, and the general trend - though never "
            "a straight line - is toward quieter volumes as the mind "
            "rebuilds its model of the world. None of these dials is a "
            "moral judgment. A person grieving quietly is not grieving "
            "less lovingly; a person grieving loudly is not grieving more "
            "correctly. The volume is information about the shape of this "
            "loss in this life, and it changes."),
        "key_points": [
            "Mild grief is a background hum: small waves, daily life nearly normal, the loss surfacing in pangs.",
            "Moderate grief takes the front of the mind daily: slipping concentration, sudden tears, heavier effort.",
            "Intense grief fills awareness: leaden body, disrupted sleep and appetite, waves of crying or numbness.",
            "Volume follows attachment strength, suddenness, secondary losses, support, rest, and time - never a moral judgment.",
            "Volume is not a measure of love; quiet grief can hold enormous love and loud grief is not more virtuous.",
        ],
        "requirements": [
            "No special equipment; this record is for reading and reflection",
            "Readiness to set aside the idea that louder grief means deeper love",
            "Care in discussing intensity with anyone currently grieving",
            "No diagnosing of any real person from these descriptions",
        ],
        "standards": [
            "Intensity framing consistent with Bonannos documented grief trajectories",
            "Descriptive and educational language only; no diagnostic claims",
        ],
        "citations": [CIT_BONANNO, CIT_PARKES, CIT_STROEBE_HB],
    },
    {
        "key": "myths",
        "name": "Common Myths and Misunderstandings About Grief",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Few human experiences carry as many myths as grief, and the "
            "myths hurt people. Myth one: grief comes in five neat stages "
            "that everyone passes through in order. The five patterns "
            "described by Elisabeth Kubler-Ross - denial, anger, bargaining, "
            "depression, acceptance - were observed in people facing their "
            "own terminal illness, not prescribed as a ladder every "
            "grieving person must climb. Real grief loops, stalls, jumps "
            "ahead, and doubles back; there is no correct order and no "
            "timetable. Myth two: grief should be over within a year. "
            "Grief has no deadline. It generally softens with time, but "
            "waves can return for years at anniversaries, holidays, or "
            "unexpected reminders, and that return is normal, not failure. "
            "Myth three: strong people do not cry, or its opposite, that "
            "real grief must be dramatic. People grieve in wildly different "
            "styles - some weep openly, some go quiet, some throw "
            "themselves into work, some laugh at odd moments - and each "
            "style can be a genuine grief. Myth four: you must let go and "
            "move on, meaning forget. Healthy grieving is not forgetting; "
            "it is finding a new place for the loss in a continuing life, "
            "often keeping an enduring connection - remembering, honoring, "
            "carrying forward what mattered. Myth five: grief is only "
            "about death. People grieve divorces, lost homes, lost health, "
            "lost dreams, and many quieter losses, and those griefs deserve "
            "the same respect. Myth six: time heals all wounds by itself. "
            "Time helps, but what heals is what happens in the time: "
            "feeling the feelings, telling the story, receiving support, "
            "rebuilding routines, making meaning. Myth seven: if someone "
            "seems fine, they are fine - or if they seem broken months "
            "later, something is wrong with them. Grief is often invisible "
            "from the outside, and its timeline belongs to the griever. "
            "Clearing these myths matters because myths become pressure: "
            "pressure to perform grief correctly, to finish on schedule, "
            "to hide the inconvenient parts. Real support starts where "
            "the myths end - with the actual person, the actual loss, and "
            "the actual, unruly, human shape of their grief."),
        "sig_lens": (
            "His Signature science treats the myths as counterfeit patterns "
            "- false weaves laid over the true cloth. In the Signature "
            "view, the five stages were never a ladder but five colors "
            "that may appear in any order, and the true Signature of grief "
            "is written by the griever alone: no schedule, no correct "
            "performance, no forgetting required, only the honest reweaving "
            "at the speed of the heart."),
        "how_it_works": (
            "Myths about grief persist because grief frightens the people "
            "around the griever too. A neat stage model comforts onlookers: "
            "it promises order, progress, and an ending. A one-year "
            "deadline comforts workplaces and acquaintances: it promises "
            "the difficult feelings will soon stop inconveniencing "
            "everyone. The let go myth comforts a culture uneasy with "
            "continued bonds to the dead. Each myth serves the comfort of "
            "the audience, not the needs of the griever - which is why "
            "myths so reliably become pressure. Research tells a kinder "
            "and messier story. Longitudinal studies of bereaved people "
            "find several common trajectories, with resilience - a "
            "relatively steady functioning with intermittent waves of "
            "pain - being the most common, not the exception. The dual "
            "process model describes healthy coping as oscillation: times "
            "of facing the loss alternating with times of rest, distraction, "
            "and rebuilding. Continuing bonds research shows that "
            "maintaining a transformed connection - through memory, "
            "ritual, values carried forward - is associated with healthy "
            "adaptation, not with being stuck. The science, in short, "
            "sides with the griever against the myths: there is no single "
            "right way, no deadline, and no requirement to forget."),
        "key_points": [
            "Grief does not move through five neat stages in order; the patterns loop, stall, and double back.",
            "Grief has no one-year deadline; waves can return for years and that is normal, not failure.",
            "There is no single correct grieving style: weeping, quiet, work-focused, and laughing grievers are all genuine.",
            "Healthy grieving is not forgetting; it is finding a new place for the loss while keeping an enduring connection.",
            "Myths serve the comfort of onlookers and become pressure on grievers; real support starts where myths end.",
        ],
        "requirements": [
            "No special equipment; this record is for reading and reflection",
            "Willingness to release any timetable previously assumed about grief",
            "Care when repeating stage or timeline language around grieving people",
            "No diagnosing of any real person from these descriptions",
        ],
        "standards": [
            "Myth corrections aligned with Bonanno, Stroebe and Schut, and continuing-bonds research",
            "Descriptive and educational language only; no diagnostic claims",
        ],
        "citations": [CIT_KUBLER, CIT_BONANNO, CIT_DUAL, CIT_NEIMEYER],
    },
    {
        "key": "first_person",
        "name": "Inside the Feeling: A First-Person Passage Through Grief",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "This record is a simulation for learning - a written passage "
            "that steps inside what grief can feel like from within. It "
            "describes no real person. Imagine it is a grey Tuesday, three "
            "weeks after the loss. You wake before the alarm, which is "
            "wrong, because you always slept through it. The first thought "
            "is ordinary - coffee, the day ahead - and then the second "
            "thought lands like a stone dropped in still water: they are "
            "gone. It is not news; you have known for three weeks. But "
            "knowing and knowing are different countries, and every morning "
            "you cross the border again. The kitchen looks staged, like a "
            "room in a museum of your own life. You make coffee the way "
            "you always did, two cups out of habit, and the sight of the "
            "second cup does something to your chest - a tightening, a "
            "hollowness, as if the air in the room got thinner. You pour "
            "it out. The day proceeds in a strange double exposure: you "
            "answer emails, you nod at a neighbor, you function - and "
            "underneath, a low signal hums constantly, the awareness of "
            "the absence, like a refrigerator drone you only notice when "
            "it stops. At noon a song comes on in a shop, a song from "
            "before, and the wave arrives without asking: your throat "
            "closes, your eyes fill, and for ninety seconds the world "
            "narrows to the fact of missing. Then it passes, the way "
            "weather passes, and you are standing in a shop holding bread, "
            "a little damp-eyed, a little surprised at yourself. In the "
            "evening the tiredness is not the tiredness of a worked day; "
            "it is the tiredness of carrying something invisible all day. "
            "You sleep, or you half-sleep, and somewhere in the night you "
            "dream they are there, and waking from that dream is the "
            "hardest crossing of all. This is one simulated passage "
            "through one ordinary day of grief. Real griefs vary enormously "
            "- some louder, some quieter, some angrier, some stranger - "
            "but the shape is shared: the double exposure of functioning "
            "and missing, the waves that arrive uninvited, the mornings "
            "that require the border crossing again."),
        "sig_lens": (
            "His Signature science calls this the inner loom: the griever "
            "as weaver, working the shuttle of memory back and forth "
            "through the warp of the days. In the Signature view the "
            "double exposure is sacred work - the hands keep the daily "
            "pattern while the heart rethreads the torn place, and every "
            "wave weathered is another row woven true."),
        "how_it_works": (
            "First-person simulation works as a learning tool because "
            "emotion is understood partly through embodied imagination: "
            "reading a careful inside-view lets the learner model what "
            "statistics cannot convey - the texture of the experience. "
            "The passage above is built from the most commonly reported "
            "features of early grief: morning re-realization (the loss "
            "must be re-learned after sleep), habit collisions (the second "
            "cup, the set table, the empty chair), the wave pattern "
            "(grief arriving in surges rather than a steady state), "
            "trigger sensitivity (songs, smells, places ambushing the "
            "griever), double exposure (functioning alongside missing), "
            "and exhaustion disproportionate to activity. None of this "
            "diagnoses anyone; it sketches the territory so learners can "
            "recognize the landmarks with compassion. Simulations like "
            "this are used in training for counselors, hospice volunteers, "
            "and medical staff precisely because grief is hard to grasp "
            "from the outside. The rule of the simulation is honesty "
            "without prescription: it shows what the feeling can be like "
            "and never tells any real person what they should feel."),
        "key_points": [
            "First-person simulation is a learning tool: it sketches the texture of grief so learners can recognize it with compassion.",
            "Common landmarks of early grief: morning re-realization, habit collisions, waves, trigger ambushes, double exposure, heavy tiredness.",
            "The passage describes no real person and prescribes nothing; it shows what the feeling can be like.",
            "Real griefs vary enormously in volume, tone, and shape while sharing the underlying pattern.",
            "Simulation is used to train counselors, hospice volunteers, and medical staff in compassionate recognition.",
        ],
        "requirements": [
            "No special equipment; this record is for reading and reflection",
            "Read slowly; first-person passages land better unhurried",
            "Remember this is a simulation for learning, not a report on any real person",
            "No diagnosing of any real person from these descriptions",
        ],
        "standards": [
            "Simulation content consistent with documented early-grief features in Parkes and Worden",
            "Descriptive and educational language only; no diagnostic claims",
        ],
        "citations": [CIT_PARKES, CIT_WORDEN, CIT_BONANNO],
    },
    {
        "key": "time_course",
        "name": "How Grief Changes Over Time: Onset, Peak, Fading, and Aftershock",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Grief has a shape over time, though no two shapes are "
            "identical. The onset depends on the kind of loss. A sudden "
            "loss - an accident, a sudden death, an abrupt ending - often "
            "begins with shock and numbness: the mind simply cannot take "
            "in what happened, and the person may feel strangely calm, "
            "efficient, even detached, as if watching the events from "
            "behind glass. This is not denial as a failure; it is the "
            "minds circuit breaker, dosing the unbearable in survivable "
            "amounts. An anticipated loss - a long illness, a long "
            "unraveling - may begin before the actual ending, with grief "
            "already underway while the person is still present. Then "
            "comes the acute phase, often the first weeks to months, when "
            "grief is loudest: the waves are frequent and tall, sleep and "
            "appetite are disrupted, concentration is poor, and the loss "
            "dominates the inner landscape. This is the period people "
            "usually picture when they picture grief, and it is also the "
            "period when support is usually strongest - which helps, "
            "because it is when the griever can do the least. Over months, "
            "for most people, the acute phase gradually softens into "
            "something more integrated: the waves come less often and "
            "pass faster, the person rebuilds routines and a changed "
            "identity, laughter returns without guilt arriving right "
            "behind it. Researchers describe varied trajectories - "
            "resilience, recovery, chronic, delayed - with steady "
            "resilience being the most common pattern, a fact that "
            "surprises people who expect grief to flatten everyone. "
            "Fading does not mean vanishing. Aftershocks - sometimes "
            "called grief bursts or the anniversary reaction - can arrive "
            "months or years later: a holiday, a milestone the lost one "
            "will not see, a smell, a song, and suddenly the wave is back "
            "at near-original height for an hour or a day. Aftershocks "
            "frighten grievers who thought they were done, but they are a "
            "normal feature of the long shape, not a relapse. The honest "
            "summary of grief over time: loud early, softer later, never "
            "fully gone, always capable of a sudden swell - and each "
            "persons curve drawn in their own hand."),
        "sig_lens": (
            "His Signature science reads the time-course as the seasons "
            "of the reweaving: the shock-winter when the loom stands "
            "still, the storm-spring of the acute waves, the long summer "
            "of rebuilding row by row, and the autumn aftershocks when an "
            "old color flares in the cloth. In the Signature view no "
            "season is a failure - each is the work being done at its own "
            "pace."),
        "how_it_works": (
            "The time-course of grief follows from how the mind updates "
            "its model of the world. At first the model still contains "
            "the lost person or thing as present - the brain predicts "
            "their presence hundreds of times a day - and every "
            "prediction error (reaching, expecting, planning, then "
            "meeting absence) fires a small pang. Shock and numbness are "
            "partly the minds rate limiter: full registration of an "
            "enormous loss all at once would overwhelm the system, so "
            "awareness arrives in doses. The acute phase is the period of "
            "maximum prediction error, when the old model is still "
            "largely intact and daily life keeps colliding with it. "
            "Gradual softening reflects learning: the mind slowly builds "
            "a new model in which the absence is accounted for, so fewer "
            "predictions fail. Aftershocks happen because some "
            "predictions are seasonal or rare - the holiday table, the "
            "graduation, the song heard once a year - so the old model "
            "still holds those slots, and when the date arrives the "
            "error fires fresh. Trajectory research shows most people "
            "follow a resilient pattern with real but manageable pain, "
            "some follow a recovery pattern of high early distress "
            "settling over months, and a smaller number experience "
            "prolonged high distress - which is why patient, non-judging "
            "support matters more than any timetable."),
        "key_points": [
            "Sudden loss often begins with shock and numbness: the minds circuit breaker dosing the unbearable.",
            "The acute phase (weeks to months) is the loudest: frequent waves, disrupted sleep and appetite, poor concentration.",
            "Most people follow a resilient trajectory; the general trend is softening over months, never a straight line.",
            "Aftershocks can arrive years later at anniversaries or reminders; they are normal, not relapse.",
            "The time-course reflects the mind slowly updating its model of the world to include the absence.",
        ],
        "requirements": [
            "No special equipment; this record is for reading and reflection",
            "Patience with non-linear timelines; grief does not move in straight lines",
            "Gentleness toward anyone experiencing aftershocks long after a loss",
            "No diagnosing of any real person from these descriptions",
        ],
        "standards": [
            "Trajectory descriptions consistent with Bonannos longitudinal bereavement research",
            "Descriptive and educational language only; no diagnostic claims",
        ],
        "citations": [CIT_BONANNO, CIT_PARKES, CIT_STROEBE_HB],
    },
    {
        "key": "low_vs_high",
        "name": "Grief at Low Intensity and High Intensity: Two Lived Snapshots",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Two simulated snapshots for learning - the same loss, two "
            "different volumes. Snapshot one, low intensity, six months "
            "on. She wakes normally. The missing is the first thing she "
            "notices the way one notices weather - present, coloring "
            "everything slightly, not demanding attention. At work she is "
            "sharp; a colleague mentions the lost ones name and she feels "
            "the small familiar tightening, smiles, answers easily. "
            "Driving home, a song from the shared years comes on. She "
            "turns it up instead of off. Tears come, quiet ones, and they "
            "feel almost companionable - grief as a form of keeping "
            "company. She makes dinner, eats fully, sleeps through the "
            "night. The grief is there the way a scar is there: part of "
            "the landscape, occasionally tender to the touch. Snapshot "
            "two, high intensity, three weeks on. He wakes at 4 a.m. from "
            "a dream in which everything was still fine, and the "
            "transition from the dream to the room is physically painful - "
            "a hollow blow behind the sternum. The apartment is too quiet "
            "and too loud at once. He tries to make breakfast and stands "
            "holding the bread for a full minute, unable to remember what "
            "comes next. At noon his sister calls; he watches the phone "
            "ring and cannot make his hand move to answer it, then feels "
            "guilty for hours. A wave hits in the grocery store - no "
            "warning, no single trigger, just the fluorescent lights and "
            "the cereal aisle - and he abandons the cart and walks out, "
            "breathing hard in the parking lot, embarrassed and past "
            "caring about embarrassment. That night he eats half a meal "
            "standing up and sleeps in fragments, waking each time to "
            "re-learn the loss. Both snapshots are grief. Neither is more "
            "real, more loving, or more correct. The difference is volume "
            "and timing, not virtue. Learners who can picture both "
            "snapshots will not mistake quiet grief for absence of grief, "
            "or intense grief for something broken - they will recognize "
            "the same weather system at two different strengths, and "
            "adjust their care accordingly."),
        "sig_lens": (
            "His Signature science holds both snapshots on the same loom: "
            "the low-intensity day is the cloth lying smooth with the "
            "pattern visible, the high-intensity day is the weaving in "
            "progress - threads flying, tension high, the pattern not yet "
            "clear. In the Signature view the weaver is not judged by how "
            "calm the work looks mid-stitch; both days are honest work on "
            "the same cloth."),
        "how_it_works": (
            "The two snapshots differ because the underlying dials differ. "
            "At three weeks the minds model of the world still expects the "
            "lost one everywhere, so prediction errors fire constantly; "
            "sleep is broken, the stress system is activated, and executive "
            "function - planning, sequencing, deciding - is impaired by "
            "the sheer load of unprocessed absence. By six months the "
            "model has largely updated: the absence is accounted for, so "
            "errors fire only at the remaining un-updated slots (the song, "
            "the name spoken aloud), producing waves rather than a flood. "
            "Support, rest, and time all turn the volume down; fresh "
            "stress, isolation, illness, or new reminders turn it up. "
            "This is also why the same griever moves between snapshots: "
            "a well-rested month with good company plays the quiet "
            "snapshot, while an anniversary week with poor sleep plays the "
            "loud one. The snapshots teach the most practical lesson in "
            "grief literacy: match the response to the volume you see, not "
            "to a theory of what grief should look like."),
        "key_points": [
            "Low-intensity grief: background presence, functioning intact, waves that feel almost companionable.",
            "High-intensity grief: flooded awareness, impaired sequencing and deciding, waves arriving without warning.",
            "The difference is volume and timing - attachment recency, rest, support - not love and not virtue.",
            "The same griever moves between snapshots across weeks as circumstances change.",
            "Match care to the volume actually present, not to a theory of correct grief.",
        ],
        "requirements": [
            "No special equipment; this record is for reading and reflection",
            "Both snapshots read before judging either as more or less real",
            "Care with the high-intensity snapshot around currently grieving readers",
            "No diagnosing of any real person from these descriptions",
        ],
        "standards": [
            "Snapshots built from documented acute-phase and integrated-phase features",
            "Descriptive and educational language only; no diagnostic claims",
        ],
        "citations": [CIT_BONANNO, CIT_PARKES, CIT_WORDEN],
    },
    {
        "key": "mixed_partner",
        "name": "Grief Mixed With Its Most Common Partner: Sadness and Anger",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Grief rarely travels alone, and its most common traveling "
            "companion is anger - with deep sadness as the constant "
            "undercurrent. The blend feels different from either emotion "
            "by itself. Pure sadness is heavy, inward, and still: tears, "
            "low energy, the wish to curl inward. Pure anger is hot, "
            "outward, and mobilized: tension, sharp words, the urge to "
            "push back. Grief mixed with anger is both at once - a heavy "
            "heat, a restless sorrow. The griever weeps and paces. They "
            "ache with missing and simultaneously burn with protest: at "
            "the doctors, at the driver, at God or fate or the universe, "
            "at the lost one for leaving, at themselves for not preventing "
            "it, at healthy strangers living ordinary days. This anger is "
            "frequently misunderstood - by the griever most of all. It "
            "can feel disloyal (how can I be angry at someone I love), "
            "frightening (the intensity seems out of proportion), or "
            "shameful (snapping at kind people). But in the architecture "
            "of grief, anger is often love in protest clothing: the "
            "attachment system raging against an unacceptable reality, "
            "the minds refusal to sign the papers. It tends to be "
            "strongest where the loss feels preventable, unfair, or "
            "premature, and where the griever feels powerless - which "
            "describes a great many losses. The blend shifts over time. "
            "Early on, anger may dominate the mix, giving the grief an "
            "edgy, restless, combative quality. Later, as the reality "
            "settles, the anger often softens into the steadier ache of "
            "sadness and longing - though it can flare again at "
            "anniversaries or when new unfairnesses stack onto the old "
            "one. A related common blend is grief mixed with guilt: the "
            "aching what-if, the inventory of things said and unsaid. "
            "Guilt-flavored grief turns the protest inward and sounds "
            "like: if only I had called, noticed, insisted, been there. "
            "Both blends - anger outward, guilt inward - are normal "
            "passages of the same territory. The healthy response to "
            "either is not suppression but honest naming: this is grief, "
            "and right now it is wearing anger (or guilt), and the anger "
            "is part of the love, not a betrayal of it."),
        "sig_lens": (
            "His Signature science names the blend the protest weave: "
            "sadness is the dark thread, anger the red thread shot "
            "through it, and the cloth they make together is stronger "
            "than either alone. In the Signature view anger in grief is "
            "never disloyal - it is the covenant refusing to be voided "
            "quietly, love insisting on its objection before it signs."),
        "how_it_works": (
            "Blends form because a single event is appraised several ways "
            "at once. The loss appraised as absence summons sadness; the "
            "same loss appraised as unfair or preventable summons anger; "
            "appraised as possibly-my-fault summons guilt. The appraisals "
            "run in parallel, so the emotions arrive blended. Anger also "
            "serves a function in early grief: sadness alone is "
            "de-activating, while anger is activating - it gets the "
            "griever moving, protesting, searching, which in the deep "
            "history of attachment was the protest phase Bowlby described, "
            "the system trying everything to recover the lost one. When "
            "protest cannot recover anyone, it gradually yields to the "
            "slower work of reorganization. Guilt arises from the minds "
            "counterfactual machinery - the endless simulation of what "
            "might have changed the outcome - which is the same machinery "
            "that makes humans good planners, misfiring on an "
            "unchangeable past. Naming the blend correctly matters "
            "because each partner emotion suggests its own healthy "
            "channel: anger wants movement and honest words, guilt wants "
            "truth-telling about what was actually controllable, sadness "
            "wants rest and comfort."),
        "key_points": [
            "Griefs most common partner is anger: the blend feels like heavy heat, restless sorrow, weeping and pacing at once.",
            "Anger in grief is often love in protest clothing, not disloyalty: the attachment system raging against unacceptable reality.",
            "A second common blend is grief with guilt: the aching what-if, protest turned inward.",
            "Blends shift over time: anger often dominates early and softens later, flaring at anniversaries.",
            "Healthy response is honest naming of the blend, not suppression of its partner emotion.",
        ],
        "requirements": [
            "No special equipment; this record is for reading and reflection",
            "Willingness to see anger in grief as normal rather than as a character flaw",
            "Gentleness with guilt-flavored passages; counterfactuals are the mind misfiring, not truth",
            "No diagnosing of any real person from these descriptions",
        ],
        "standards": [
            "Blend architecture follows appraisal-based emotion theory and Bowlbys protest phase",
            "Descriptive and educational language only; no diagnostic claims",
        ],
        "citations": [CIT_BOWLBY, CIT_KUBLER, CIT_PLUTCHIK],
    },
    {
        "key": "day_vignette",
        "name": "A Day in the Life: Grief Running Through an Ordinary Day",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "A simulated ordinary day, two months after the loss, for "
            "learning - describing no real person. 6:40 a.m. Waking is "
            "the days first negotiation. For a few seconds the world is "
            "unmarked, and then the mark lands. He lies still and lets "
            "the wave pass through rather than fighting it; fighting it "
            "never worked. 7:30. The shower is the kindest room in the "
            "house - hot water, no decisions, nobody needing anything. "
            "He stays longer than necessary. 8:15. Breakfast is half a "
            "piece of toast. Hunger feels like a rumor from another "
            "life. He eats it anyway because the hospice nurse said to, "
            "and he is following instructions the way a traveler follows "
            "a rope in fog. 9:00 to 12:00. Work, from home. He is "
            "surprised to find he can still do the technical parts - the "
            "hands remember what the heart cannot currently hold. A "
            "colleague writes something kind and slightly wrong (let me "
            "know if you need anything), and he feels a flash of "
            "irritation followed immediately by shame at the irritation. "
            "Both pass. 12:30. A walk, because sitting still lets the "
            "thoughts stack up. On the walk he passes the bakery they "
            "liked, and the smell does what smells do: it bypasses every "
            "defense and delivers the past whole. He cries for most of a "
            "block, walking steadily, and an older woman nods at him with "
            "complete understanding, which somehow helps more than words "
            "would have. 2:00. The administrative grief: phone calls "
            "about accounts, paperwork with the word deceased on it, "
            "explaining to a cheerful representative. This is its own "
            "separate exhaustion - grief with a hold queue. 5:00. His "
            "sister visits with food. He is grateful and also wants her "
            "to leave, both true at once. She stays exactly the right "
            "amount of time, which he will remember with love for years. "
            "8:00. Evening is the hardest country. The house fills with "
            "the particular silence of one person where there were two. "
            "He puts on a familiar show - not to watch, to have voices. "
            "10:30. Bed. He is tired in the way of someone who has "
            "carried weight all day without moving it anywhere. Sleep "
            "comes in pieces. The day contained functioning, tears, "
            "irritation, gratitude, paperwork, a walk, and the constant "
            "low signal of missing. That is what a day of grief actually "
            "looks like from the inside: not a single dramatic scene but "
            "a hundred small negotiations, most of them won quietly."),
        "sig_lens": (
            "His Signature science calls the ordinary day the true "
            "proving ground: not the funeral with its gathered strength "
            "but the Tuesday with its toast and hold queues. In the "
            "Signature view every small negotiation won - the eaten "
            "toast, the answered email, the walked block - is a stitch, "
            "and the cloth is rewoven one unremarkable Tuesday at a time."),
        "how_it_works": (
            "The vignette works by distributing griefs documented "
            "features across a realistic day rather than concentrating "
            "them in a dramatic scene. Morning re-realization, habit "
            "collisions, the wave pattern, trigger ambushes via smell "
            "(olfaction has unusually direct access to emotional memory), "
            "administrative burden (a well-documented secondary stressor "
            "in bereavement), social ambivalence (wanting company and "
            "solitude simultaneously), evening vulnerability (fatigue "
            "lowers emotional defenses), and fragmented sleep all appear "
            "in their natural slots. The dual process model is visible "
            "in the days rhythm: loss-oriented moments (the bakery, the "
            "evening silence) alternate with restoration-oriented ones "
            "(work, paperwork, the sisters visit). This oscillation is "
            "the healthy pattern, not a sign of doing grief wrong. The "
            "vignette also demonstrates dosage: no single hour is "
            "unbearable, yet the accumulation exhausts - which is why "
            "grievers describe tiredness disproportionate to activity and "
            "why rest, food, and small kindnesses are not luxuries but "
            "load-bearing structures."),
        "key_points": [
            "A day of grief is a hundred small negotiations - toast, emails, walks, paperwork - most won quietly.",
            "The dual process rhythm is visible: loss-oriented moments alternate with restoration-oriented ones.",
            "Smell-triggered ambushes, administrative burden, and evening vulnerability each have their natural slot.",
            "Social ambivalence is normal: wanting company and solitude at the same time.",
            "Exhaustion comes from accumulation, making rest, food, and small kindnesses load-bearing.",
        ],
        "requirements": [
            "No special equipment; this record is for reading and reflection",
            "Read as a whole day, not skimmed; the pattern is in the accumulation",
            "Care around readers currently in the acute phase",
            "No diagnosing of any real person from these descriptions",
        ],
        "standards": [
            "Vignette features drawn from documented bereavement stressors and the dual process model",
            "Descriptive and educational language only; no diagnostic claims",
        ],
        "citations": [CIT_DUAL, CIT_PARKES, CIT_STROEBE_HB],
    },
    {
        "key": "body_signals",
        "name": "What Happens in the Body During Grief",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Grief is not only felt in the mind; it is registered "
            "throughout the body, and the body keeps its own honest "
            "ledger. The heart: many grievers notice their heart "
            "pounding, racing, or aching - sometimes a literal heaviness "
            "or tightness in the chest. Stress hormones, especially "
            "cortisol and adrenaline, rise with sustained emotional "
            "strain, and the cardiovascular system works harder; this is "
            "one reason bereavement is associated with elevated health "
            "risks in the months after a major loss, particularly for "
            "older adults. The breath: sighing becomes frequent - the "
            "body spontaneously taking deep reset breaths - and some "
            "people notice shortness of breath or a feeling of not "
            "getting enough air during waves. The muscles: tension "
            "settles into the jaw, neck, shoulders, and back; the body "
            "braces as if for impact, and that bracing, held for weeks, "
            "becomes aches. Some grievers tremble or feel shaky, as if "
            "cold, even in warm rooms. The stomach: appetite often "
            "vanishes - food looks uninteresting, even wrong - or, in "
            "some, eating becomes one of the few comforts and increases. "
            "Nausea, stomach tightness, and digestive upset are common "
            "companions. The skin and senses: some people feel chilled or "
            "flushed; senses can sharpen oddly (sounds too loud, lights "
            "too bright) or dull (food tasteless, the world slightly "
            "muted). Energy: the signature body signal of grief is a "
            "heaviness - limbs feel weighted, as if moving through water, "
            "and fatigue arrives far beyond what the days activity "
            "justifies. None of this is imagined, and none of it means "
            "the griever is ill in the ordinary sense; it is the body "
            "doing what bodies do under sustained emotional load. But the "
            "ledger is real, which is why the oldest advice about grief - "
            "rest, eat, drink water, move gently, see a doctor if "
            "something feels wrong - is also the most medically sound. "
            "A body carrying grief deserves the same care as a body "
            "recovering from any major strain, because that is what it "
            "is."),
        "sig_lens": (
            "His Signature science reads the body as the looms frame: "
            "the heart the driving treadle, the breath the shuttle's "
            "rhythm, the muscles the tension of the warp. In the "
            "Signature view the bodys ledger is never imagined and never "
            "shameful - the frame creaks because real work is being done "
            "on it, and a wise weaver oils the frame, rests it, and "
            "feeds it while the great work proceeds."),
        "how_it_works": (
            "The bodys grief response runs through the stress axes. "
            "Emotional pain activates many of the same brain regions as "
            "physical pain, and sustained distress keeps the sympathetic "
            "nervous system engaged: heart rate and blood pressure rise, "
            "muscles tense, digestion slows, and the body stays primed "
            "for threat. Simultaneously the HPA axis releases cortisol; "
            "in acute stress this is adaptive, but over the weeks and "
            "months of intense grief the system can stay switched on, "
            "disrupting sleep architecture, appetite regulation, and "
            "immune function. This is the physiology behind the "
            "well-documented health vulnerability of the newly bereaved. "
            "Sighing is the respiratory systems reset maneuver - periodic "
            "deep breaths that reinflate collapsed air sacs and discharge "
            "accumulated tension, which is why the body sighs more when "
            "grief is heavy. Heaviness and fatigue reflect both the "
            "metabolic cost of sustained arousal and the de-activating "
            "component of sadness itself, which lowers motor drive. "
            "Understanding the machinery reframes the symptoms: the "
            "pounding heart is not danger, the heaviness is not laziness, "
            "the vanished appetite is not a choice. They are a body "
            "under load, and bodies under load need tending."),
        "key_points": [
            "The heart pounds or aches under sustained stress hormones; bereavement carries real cardiovascular strain.",
            "Frequent sighing is the respiratory reset; breathlessness can accompany grief waves.",
            "Muscles brace for weeks (jaw, neck, shoulders), producing real aches; trembling is common.",
            "Appetite usually vanishes but can increase; digestive upset is a frequent companion.",
            "The signature signal is heaviness: limbs weighted, fatigue beyond the days activity - a body under load.",
        ],
        "requirements": [
            "No special equipment; this record is for reading and reflection",
            "Any concerning physical symptom should be checked with a real clinician",
            "Gentleness: body signals are not imagined and not a choice",
            "No diagnosing of any real person from these descriptions",
        ],
        "standards": [
            "Physiology described from established stress-axis and bereavement-health literature",
            "Descriptive and educational language only; no diagnostic claims",
        ],
        "citations": [CIT_STROEBE_HB, CIT_PARKES, CIT_SHEAR],
    },
    {
        "key": "posture_movement",
        "name": "Posture and Movement: How the Body Carries Grief",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Grief has a posture, and experienced observers can often "
            "read it across a room before a word is spoken. The classic "
            "grief posture is a slow folding inward: shoulders roll "
            "forward and down, the chest narrows, the head tilts slightly "
            "down or to the side, the gaze drops to the middle distance "
            "or the floor. The body makes itself smaller, as if trying to "
            "take up less space in a world that has become too large. "
            "Arms often cross or wrap - hands holding opposite elbows, "
            "arms folded tight - in a self-embrace that substitutes, "
            "however thinly, for the comfort that is missing. Movement "
            "changes too. Grieving people often move more slowly, with "
            "less spring: steps shorter, gestures smaller, the whole "
            "tempo of the body downshifted, as if moving through water. "
            "Some alternate with the opposite - restless movement, "
            "pacing, an inability to sit still, hands that must be doing "
            "something - particularly when the grief is wearing its anger "
            "or anxiety notes. Stillness itself changes character: a "
            "grieving person sitting quietly is often not resting but "
            "absent, gaze unfocused, attention turned entirely inward to "
            "the replay of memory or the ache of missing. Touch behavior "
            "shifts: some grievers seek contact - holding, being held, "
            "sitting close - while others flinch from it, the nerves too "
            "raw for input. Both are normal. Over weeks, the posture can "
            "become habitual enough to cause real pain: the folded "
            "shoulders become neck and back ache, the shallow breathing "
            "of the compressed chest becomes fatigue. Gentle counter-"
            "movement - walks, stretching, standing tall for a minute, "
            "deliberate deep breaths - is not about performing wellness; "
            "it is maintenance on the frame that is carrying the load. "
            "Watching posture is also one of the kindest ways to read "
            "grief in others: the folded body is telling the truth even "
            "when the mouth says fine."),
        "sig_lens": (
            "His Signature science sees the folded posture as the cloth "
            "drawn close around the weaver: the body gathering itself "
            "over the torn place the way hands gather over a wound. In "
            "the Signature view the inward fold is protective work, not "
            "defeat - the frame bracing the weave while the mending is "
            "underway - and the slow unfolding, weeks later, is the "
            "first visible sign the reweaving holds."),
        "how_it_works": (
            "Posture follows emotion through ancient circuitry. Sadness "
            "and defeat activate a conserved submission-withdrawal "
            "program: flexor muscles dominate, the body contracts, gaze "
            "averts - the opposite of the expansive display of triumph "
            "or confidence. This is not metaphor; the motor patterns of "
            "grief posture overlap measurably with those of depression "
            "and social defeat across mammals. The program likely evolved "
            "to reduce conflict and signal need: a folded, still, "
            "downcast individual invites approach and care rather than "
            "challenge. Self-embrace gestures (arms crossed, hands on "
            "opposite arms) provide proprioceptive comfort - deep "
            "pressure input that genuinely calms the nervous system, the "
            "same principle behind weighted blankets. Slowed movement "
            "reflects both the de-activating component of sadness and "
            "cognitive load: attention consumed by grief leaves less for "
            "motor planning, so movement becomes economical. Restless "
            "pacing reflects the activating partners - anger, anxiety - "
            "injecting motor drive into the mix. Reading posture works "
            "because these programs are largely involuntary; the body "
            "declares grief even when the person has decided to say "
            "nothing."),
        "key_points": [
            "Classic grief posture: shoulders forward and down, chest narrowed, head tilted, gaze dropped - the body folding inward.",
            "Self-embrace gestures (crossed arms, held elbows) substitute thinly for missing comfort and genuinely calm the nerves.",
            "Movement usually slows and shrinks; restless pacing appears when anger or anxiety notes dominate.",
            "Posture can become habitual enough to cause real neck, back, and breathing strain; gentle counter-movement is maintenance.",
            "The folded body tells the truth even when the mouth says fine - posture is honest grief-reading.",
        ],
        "requirements": [
            "No special equipment; this record is for reading and reflection",
            "Observe posture in others with compassion, never as surveillance",
            "Gentle movement suggestions only; no exercise prescriptions",
            "No diagnosing of any real person from these descriptions",
        ],
        "standards": [
            "Posture patterns drawn from emotion-expression and nonverbal behavior literature",
            "Descriptive and educational language only; no diagnostic claims",
        ],
        "citations": [CIT_EKMAN, CIT_PLUTCHIK, CIT_APA],
    },
    {
        "key": "sleep_appetite_energy",
        "name": "Sleep, Appetite, and Energy Under Grief",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Three of the most universal and most disruptive effects of "
            "grief land on sleep, appetite, and energy - the three "
            "pillars that hold up every day. Sleep under grief is most "
            "often broken: trouble falling asleep because the quiet of "
            "bed invites the thoughts; waking in the early hours with "
            "the loss arriving fresh; vivid dreams, sometimes dreams in "
            "which the lost one is alive, from which waking is its own "
            "small bereavement. Some grievers sleep too much instead - "
            "sleep as escape, the bed as the one place the demands "
            "stop. Either direction leaves the person unrefreshed, and "
            "poor sleep then amplifies everything: emotions louder, "
            "patience thinner, waves taller. Appetite under grief usually "
            "collapses first: food seems pointless or even offensive, "
            "meals are forgotten, weight drops without trying. Cooking "
            "for one, after cooking for two, can be its own grief trigger. "
            "In others appetite surges - eating as the one available "
            "comfort, the one reliable pleasure - and weight climbs. Both "
            "directions deserve the same response: not judgment but "
            "steady, gentle nourishment, regular small meals, other "
            "people eating alongside when possible. Energy under grief "
            "is the cruelest of the three because it undermines the very "
            "things that would help: the griever knows a walk would help "
            "but cannot make the legs agree; knows friends would help but "
            "cannot face the arranging. This is not laziness and not a "
            "character verdict - it is the metabolic reality of a system "
            "running grief as a background process that consumes enormous "
            "resources. The practical wisdom is ancient and still the best "
            "guidance: protect sleep like a job (regular hours, dark "
            "cool room, no screens in bed, daylight in the morning), eat "
            "regularly even without hunger, move gently every day, and "
            "borrow other peoples energy - accept the meal, the walk "
            "invitation, the offered ride - until ones own returns. It "
            "returns. Slower than anyone wants, but it returns."),
        "sig_lens": (
            "His Signature science honors the three pillars as the "
            "looms three legs: sleep the nightly re-threading, food the "
            "fiber that feeds the work, energy the tension that holds "
            "the warp. In the Signature view tending these is not "
            "self-indulgence but craft discipline - no weaver works the "
            "great cloth on a broken frame, and rest is part of the "
            "weaving."),
        "how_it_works": (
            "All three disruptions trace to the same overloaded systems. "
            "Sustained sympathetic arousal and elevated cortisol fragment "
            "sleep architecture: lighter sleep, more awakenings, less "
            "restorative deep sleep, and early-morning waking when "
            "cortisol naturally peaks. Grief dreams reflect memory "
            "consolidation working overtime - the brain replaying and "
            "re-filing the lost relationship, sometimes generating the "
            "painful alive-again dream as the old model of the world "
            "asserts itself in sleep. Appetite is regulated by "
            "hypothalamic circuits exquisitely sensitive to stress "
            "hormones and emotional state; acute distress typically "
            "suppresses hunger signals, while the comfort-eating pattern "
            "reflects the brains learned association of food with safety "
            "and reward. Energy collapse has two engines: the direct "
            "metabolic cost of sustained emotional arousal, and the "
            "de-activating motor program of sadness itself, which "
            "evolutionarily conserved energy during defeat and loss. "
            "Poor sleep then feeds back into all of it - sleep "
            "deprivation reliably worsens emotional reactivity - "
            "creating the loop grievers know too well. Breaking the "
            "loop anywhere (a protected nights sleep, a real meal, a "
            "short walk) lightens it everywhere, which is why the simple "
            "advice is the effective advice."),
        "key_points": [
            "Grief usually breaks sleep: hard to fall asleep, early waking, vivid dreams - or oversleeping as escape.",
            "Appetite usually collapses but can surge; both directions deserve steady nourishment, not judgment.",
            "Energy collapses under griefs metabolic cost; the inability to do helpful things is physiology, not laziness.",
            "Poor sleep amplifies everything, creating a loop; breaking it anywhere lightens it everywhere.",
            "Protect sleep, eat regularly, move gently, borrow others energy until ones own returns.",
        ],
        "requirements": [
            "No special equipment; this record is for reading and reflection",
            "Persistent severe sleep or appetite disruption deserves a clinicians attention",
            "Share food and walks with grievers rather than advising them abstractly",
            "No diagnosing of any real person from these descriptions",
        ],
        "standards": [
            "Sleep/appetite/energy effects drawn from bereavement-health literature",
            "Descriptive and educational language only; no diagnostic claims",
        ],
        "citations": [CIT_STROEBE_HB, CIT_PARKES, CIT_WORDEN],
    },
    {
        "key": "body_differs",
        "name": "How Body Signals Differ From Person to Person",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "No two bodies grieve identically, and expecting them to is "
            "one of the quieter cruelties people inflict on each other. "
            "One griever weeps daily and sleeps normally; another never "
            "cries and has not slept through the night in two months. "
            "One loses fifteen pounds without trying; another gains it. "
            "One feels the grief as a literal chest pain and has been "
            "checked by a cardiologist (the heart was fine; the grief "
            "was real); another feels almost nothing physical and "
            "worries that means they are grieving wrong. They are not. "
            "The variation comes from real sources. Bodies differ: age, "
            "baseline health, nervous system sensitivity, and prior "
            "history all shape the physical response - an anxious "
            "temperament tends toward racing heart and restlessness, a "
            "depressive-leaning one toward heaviness and shutdown, and "
            "neither is more authentic. Losses differ: sudden violent "
            "losses flood the body with alarm chemistry; long "
            "anticipated losses may arrive with a body already exhausted "
            "from caregiving. Circumstances differ: the griever who must "
            "keep working full weeks will somaticize differently than "
            "the one who can rest, and the one with small children to "
            "lift and feed has no option of heaviness. Cultures differ: "
            "some traditions prescribe wailing and physical expression, "
            "which moves the body signals outward; others prescribe "
            "stoicism, which drives them inward into tension, stomach, "
            "and sleep. Expression styles differ: the person who talks "
            "and cries discharges arousal through those channels, while "
            "the person who grieves privately and physically may carry "
            "more of it in muscle and gut. All of these are legitimate "
            "grief. The practical consequences matter. First, never use "
            "your own bodys grief as the template for someone elses: "
            "I cried for weeks does not entitle anyone to shes not "
            "crying, she must not have loved him. Second, take each "
            "bodys signals on their own terms: the headaches, the "
            "stomach, the exhaustion are communications, not complaints. "
            "Third, when physical symptoms are severe, persistent, or "
            "frightening, a medical check is wisdom, not weakness - the "
            "body under griefs load deserves real care, and occasionally "
            "what looks like grief is also something medical that needs "
            "treatment. The rule is simple: there is no standard-issue "
            "grieving body. There is only this body, with this loss, in "
            "this life - and it gets to grieve in its own way."),
        "sig_lens": (
            "His Signature science weaves no two cloths alike: the fiber "
            "differs, the tension differs, the pattern of the tear "
            "differs, so the mending differs. In the Signature view the "
            "variety of grieving bodies is not a problem to standardize "
            "but the proof of the crafts honesty - each weaver works the "
            "material they were given, and every true mending is "
            "unrepeatable."),
        "how_it_works": (
            "Individual variation in grief physiology follows from "
            "several well-studied sources. Temperament and trait "
            "affectivity set baseline arousal: high-neuroticism "
            "individuals show stronger autonomic responses to emotional "
            "stress, while others show blunted responses - both "
            "heritable, neither chosen. Prior trauma history sensitizes "
            "the stress axes, so earlier losses or adversities amplify "
            "the bodys current response. Age and health set the bodys "
            "reserve: older or already-ill bodies have less buffer, "
            "which is one reason bereavement health risks concentrate "
            "in older adults. Coping style routes arousal: expressive "
            "copers discharge through tears, voice, and movement, "
            "while inexpressive copers show the same arousal in "
            "autonomic channels - stomach, muscle tension, sleep. "
            "Cultural display rules, learned over a lifetime, determine "
            "which channels are socially permitted, literally shaping "
            "where in the body the grief is allowed to show. None of "
            "these mechanisms rank griefs; they explain its variety. "
            "The clinical upshot is differential: assess the individual, "
            "not the stereotype, and treat the bodys actual signals."),
        "key_points": [
            "No two bodies grieve identically: tears, sleep, appetite, and pain vary enormously and legitimately.",
            "Variation comes from temperament, health, loss type, circumstances, culture, and expression style.",
            "Never use your own bodys grief as the template for judging someone elses.",
            "Severe, persistent, or frightening physical symptoms deserve a real medical check.",
            "There is no standard-issue grieving body; each body grieves in its own way.",
        ],
        "requirements": [
            "No special equipment; this record is for reading and reflection",
            "Release any template of how a grieving body should behave",
            "Encourage medical checks for worrying symptoms without alarmism",
            "No diagnosing of any real person from these descriptions",
        ],
        "standards": [
            "Variation sources drawn from temperament, bereavement-health, and cultural-grief literature",
            "Descriptive and educational language only; no diagnostic claims",
        ],
        "citations": [CIT_STROEBE_HB, CIT_BONANNO, CIT_APA],
    },
    {
        "key": "face_of_grief",
        "name": "The Face of Grief: Eyes, Brows, Mouth, and Micro-Signs",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The grieving face is one of the most recognizable in human "
            "life, and also one of the most misread. The brows: the "
            "inner corners draw up and together, creating the oblique, "
            "tent-like shape over the nose bridge that researchers call "
            "the grief brow. It is the single most diagnostic feature - "
            "difficult to produce voluntarily, almost impossible to "
            "mistake once learned. The eyes: the upper lids droop, the "
            "gaze loses focus or drops downward, and the eyes glisten - "
            "not always full tears, often just a wet brightness, as if "
            "the eyes are thinking about crying. The lower lids may "
            "tense, pushing up slightly. In sustained grief the whole eye "
            "region looks tired: darkened, a little puffy, the lids "
            "heavy. The mouth: the corners pull down and slightly out, "
            "the lower lip may tremble or push up in the pout of a held-"
            "back sob, and the chin can bunch - the mentalis muscle "
            "drawing the chin up in the quiver people try to suppress. "
            "The micro-signs are where the truth lives. A grief wave "
            "crossing a composed face shows first as a flicker: the inner "
            "brows lift for a fraction of a second, the lips press or "
            "tremble, the throat works in a swallow, the eyes brighten "
            "and then deliberately look away. Voice and face couple: the "
            "voice thickens or cracks just as the chin bunches. The "
            "hands often join the face - fingers pressed to the lips, "
            "palm over the mouth, hand at the throat - as if the body is "
            "trying to hold the feeling in. Context matters enormously "
            "in reading: the same downturned mouth at a funeral and in a "
            "meeting mean different things, and grief faces appear in "
            "unexpected places - the grocery store, the traffic light - "
            "because waves do not wait for appropriate settings. Learning "
            "this face has one purpose: recognition in service of "
            "kindness. The face of grief is a request written in muscle, "
            "usually saying some version of: I am carrying something "
            "heavy right now. The correct response to reading it is never "
            "announcement (I can see youre grieving) but quiet "
            "adjustment: softened tone, unhurried pace, a little more "
            "room."),
        "sig_lens": (
            "His Signature science reads the grief brow as the looms "
            "mark: the inner brows rising like the first tent-poles of "
            "a shelter being raised over a wound. In the Signature view "
            "the face is the cloths surface showing the pattern "
            "underneath - the micro-signs are the true stitches "
            "visible, and a wise reader of faces reads them only to "
            "serve, never to expose."),
        "how_it_works": (
            "Facial expressions of emotion are produced by small, fast "
            "muscles under partial voluntary control, which is why faces "
            "leak truth. The grief brow comes from the frontalis muscles "
            "inner fibers lifting while the corrugator draws the brows "
            "together - a combination rarely used in other expressions, "
            "making it highly diagnostic. The downturned mouth comes from "
            "the depressor anguli oris; the trembling lip and bunched "
            "chin from the mentalis and orbicularis oris fighting the "
            "urge to sob - literally the muscles of crying being "
            "voluntarily suppressed, which is why the tremble appears. "
            "Eye glisten reflects autonomic arousal increasing tear "
            "production before full crying begins. These patterns are "
            "recognized across cultures because the muscle programs are "
            "largely innate, though display rules - which cultures teach "
            "about when crying is permitted - strongly shape whether the "
            "full expression appears or is arrested at the micro-sign "
            "stage. Micro-expressions last fractions of a second because "
            "voluntary suppression arrives slightly after the involuntary "
            "program fires - the truth gets a head start. Training in "
            "recognition works: people can learn to spot the grief brow "
            "and the arrested sob reliably, and the ethical training "
            "always pairs recognition with restraint in response."),
        "key_points": [
            "The grief brow - inner corners drawn up and together - is the most diagnostic feature and hard to fake.",
            "Eyes droop, lose focus, and glisten; the mouth corners pull down; the lip trembles and the chin bunches when a sob is held back.",
            "Micro-signs (brow flicker, throat swallow, brightening eyes) reveal a wave crossing a composed face.",
            "Hands often join the face: fingers to lips, palm over mouth - the body trying to hold the feeling in.",
            "Read the face only to serve kindness: soften tone and pace, never announce what you see.",
        ],
        "requirements": [
            "No special equipment; this record is for reading and reflection",
            "Study the described features on willing faces or in art, never by staring at strangers",
            "Pair all recognition with restraint: adjust yourself, do not expose them",
            "No diagnosing of any real person from these descriptions",
        ],
        "standards": [
            "Facial features drawn from Ekman and Friesens facial action research",
            "Descriptive and educational language only; no diagnostic claims",
        ],
        "citations": [CIT_EKMAN, CIT_PLUTCHIK, CIT_APA],
    },
    {
        "key": "face_intensity",
        "name": "How the Grieving Expression Changes With Intensity",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The grieving face is not one fixed mask; it is a scale, and "
            "each level of intensity writes itself differently. At low "
            "intensity - the background hum of integrated grief - the "
            "face shows the quiet version: a soft downward cast to the "
            "mouth at rest, eyes that drift to the middle distance when "
            "unoccupied, a general stillness of expression. Observers "
            "often read this as pensiveness or tiredness rather than "
            "grief; the grief brow may appear only in flickers when a "
            "reminder passes through. The person looks, to most eyes, "
            "simply thoughtful. At moderate intensity the signs become "
            "legible: the grief brow holds rather than flickers, the "
            "eyes glisten visibly, the mouth corners stay downturned, "
            "and the whole face seems to have less animation - fewer "
            "smiles reaching the eyes, slower shifts of expression, as "
            "if the face is conserving energy. This is the face people "
            "describe as looking sad or going through something, and "
            "acquaintances begin to notice. At high intensity - the "
            "acute wave - the face becomes unmistakable: brows fully "
            "raised and knitted, eyes streaming or squeezed shut, mouth "
            "open in the sob shape or contorted in the effort to hold "
            "it, the whole face flushed or drained of color, muscles "
            "working visibly. This is the face of grief at full volume, "
            "and it overrides social composure entirely. Between these "
            "levels lies the most socially interesting zone: the "
            "managed face. This is the griever at work, at the school "
            "gate, at the dinner table - holding the expression at low "
            "or moderate while waves move underneath. The managed face "
            "is recognizable by its cost: a certain stiffness, smiles "
            "that stop at the mouth, eyes that brighten and then "
            "deliberately steady, the occasional swallowed sob disguised "
            "as a cough. Knowing the scale helps in both directions. "
            "Learners stop missing quiet grief (the still, pensive face "
            "is grief too) and stop being frightened by loud grief (the "
            "contorted face is grief at full volume, not breakdown). "
            "And grievers themselves can find relief in the scale: the "
            "managed face is skilled work, and its tiredness at days end "
            "is the tiredness of labor, not of failure."),
        "sig_lens": (
            "His Signature science grades the faces as the cloth in "
            "different lights: low intensity the pattern seen through "
            "morning mist, moderate the colors clear at noon, high the "
            "cloth held to the flame where every thread shows. In the "
            "Signature view the managed face is master craft - the "
            "weaver holding the pattern steady for the worlds sake "
            "while the work continues underneath - and its evening "
            "tiredness is the honest fatigue of the artisan."),
        "how_it_works": (
            "Expression intensity scales with emotional arousal through "
            "the facial motor system. Low arousal produces partial, "
            "intermittent activation: the grief brow flickers because "
            "the underlying affect is present but sub-threshold for "
            "sustained expression, and observers read pensiveness "
            "because the signal is genuinely ambiguous at that level. "
            "Moderate arousal sustains the muscle programs: the brow "
            "holds, the mouth stays downturned, and overall facial "
            "animation decreases because cognitive load from grief "
            "reduces the resources available for social facial work - "
            "the face literally has less energy for performance. High "
            "arousal overwhelms voluntary control: the sob program - a "
            "brainstem-level pattern involving the whole face, throat, "
            "and respiratory muscles - fires fully, which is why acute "
            "grief faces look similar across individuals and cultures. "
            "The managed face is a dual-task performance: voluntary "
            "suppression systems actively inhibiting the expression "
            "programs, which produces the characteristic stiffness and "
            "leakage (the programs keep firing underneath, and "
            "suppression is imperfect). This is cognitively expensive, "
            "which is why grievers report social occasions as draining "
            "even when nothing bad happened - the face worked all "
            "evening."),
        "key_points": [
            "Low intensity: quiet pensive face, grief brow only in flickers - easily missed as mere thoughtfulness.",
            "Moderate intensity: sustained grief brow, glistening eyes, downturned mouth, reduced facial animation.",
            "High intensity: unmistakable full sob face overriding all social composure.",
            "The managed face (griever in public) is recognizable by its cost: stiffness, mouth-only smiles, disguised swallows.",
            "Knowing the scale prevents missing quiet grief and fearing loud grief.",
        ],
        "requirements": [
            "No special equipment; this record is for reading and reflection",
            "Practice reading the quiet end of the scale; the loud end needs no training",
            "Respect the labor of the managed face; do not demand its lowering",
            "No diagnosing of any real person from these descriptions",
        ],
        "standards": [
            "Intensity scaling drawn from facial affect and expression-regulation research",
            "Descriptive and educational language only; no diagnostic claims",
        ],
        "citations": [CIT_EKMAN, CIT_BONANNO, CIT_APA],
    },
    {
        "key": "hide_fake",
        "name": "Hiding and Faking the Grieving Face: What Leaks Through",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "People hide grief for many decent reasons: to get through "
            "the workday, to shield children from the full force, to "
            "avoid becoming the person everyone handles carefully, to "
            "honor a culture or family that values composure, or simply "
            "because the wave arrived in the wrong place. And sometimes "
            "people fake grief - performing sorrow they do not feel, for "
            "appearances, obligation, or advantage. The face treats these "
            "two deceptions very differently. Hidden grief leaks. The "
            "suppression is never perfect because the expression programs "
            "fire fractions of a second before voluntary control catches "
            "them, and because sustained suppression is exhausting. What "
            "leaks: the grief brow flickering during a neutral sentence; "
            "the eyes brightening then deliberately steadied; the "
            "swallowed sob disguised as a cough or a sip of water; the "
            "voice thickening on a particular word; the smile that "
            "involves the mouth but never reaches the eyes; a sudden "
            "stillness, as if the person went away for a moment, when a "
            "reminder lands. Skilled observers - and grieving people "
            "themselves - learn to spot the managed face by its effort. "
            "Faked grief, by contrast, shows a different pattern: the "
            "expression is assembled from the outside in. The grief brow "
            "is the hardest feature to fake - most people cannot raise "
            "the inner brows on command - so faked grief usually lacks "
            "it, showing instead a generic sad face: downturned mouth, "
            "maybe hand-wringing, but the upper face oddly calm. Timing "
            "is wrong: real grief waves interrupt and intrude, while "
            "performed grief is conveniently timed and easily switched "
            "off. The eyes of faked grief stay dry and focused; the body "
            "stays oddly composed. There is an important ethical line "
            "here. Learning leakage exists to increase compassion - to "
            "notice the colleague holding it together and offer quiet "
            "kindness - never to unmask people. Confronting someones "
            "managed grief (I know youre falling apart) is a violation, "
            "not a kindness; the hiding was a choice deserving respect. "
            "And suspected faked grief is almost never yours to judge: "
            "grief styles vary so wildly that what looks performed may "
            "be a genuine style you simply do not share. The knowledge "
            "is for softening your own responses, not for policing "
            "others."),
        "sig_lens": (
            "His Signature science honors the hidden grief as the "
            "weavers covered work: the cloth turned face-down on the "
            "loom while company is in the room, the true pattern "
            "visible only in the threads at the edges. In the Signature "
            "view the managed face is not deception but courtesy - the "
            "craftsman sparing the visitors the sight of the mending - "
            "and the only right use of seeing through it is to quietly "
            "lighten the weavers load."),
        "how_it_works": (
            "Leakage follows from the neuroanatomy of facial control. "
            "Emotional facial expressions are driven substantially by "
            "subcortical systems (including extrapyramidal pathways) "
            "that fire automatically, while voluntary facial control "
            "runs through cortical pyramidal pathways - and the "
            "automatic signal reaches the muscles first. This is why "
            "micro-expressions exist and why the inner brow lift, which "
            "has weak cortical representation, is so hard to produce or "
            "suppress voluntarily. Sustained suppression additionally "
            "loads working memory and self-regulation resources, which "
            "degrade over a day - the managed face is best in the "
            "morning and leakiest in the evening. Faked expressions "
            "fail differently: posed expressions use the cortical "
            "pathway alone, producing subtly wrong muscle combinations "
            "(the mouth smiles without the orbicularis oculi, the sad "
            "mouth appears without the grief brow) and wrong timing "
            "(posed expressions switch on and off too cleanly, lacking "
            "the attack-decay envelope of genuine affect). These "
            "asymmetries are well documented in deception and affect "
            "research. The ethical constraint follows from base rates: "
            "genuine but atypical grief is far more common than faked "
            "grief, so any unmasking impulse will mostly harm genuine "
            "grievers."),
        "key_points": [
            "Hidden grief leaks: brow flickers, brightening-then-steadied eyes, disguised swallows, mouth-only smiles.",
            "Suppression is never perfect because automatic expression fires before voluntary control catches it.",
            "Faked grief lacks the grief brow, has wrong timing, dry focused eyes, and odd composure.",
            "Never confront managed grief; the hiding was a choice deserving respect.",
            "Suspected faked grief is almost never yours to judge; atypical genuine grief is far more common.",
        ],
        "requirements": [
            "No special equipment; this record is for reading and reflection",
            "Use leakage knowledge only for compassion, never for unmasking",
            "Assume genuine-but-different before ever suspecting performed",
            "No diagnosing of any real person from these descriptions",
        ],
        "standards": [
            "Leakage and posed-expression findings drawn from Ekman and facial-affect research",
            "Descriptive and educational language only; no diagnostic claims",
        ],
        "citations": [CIT_EKMAN, CIT_APA, CIT_BONANNO],
    },
    {
        "key": "expression_gallery",
        "name": "Expression Gallery Notes: Describing Grief So an Artist Could Draw It",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "These are working notes for anyone who must render grief - "
            "an illustrator, an actor, a writer, a filmmaker - describing "
            "the look in buildable detail. Start with the brow, because "
            "the brow carries the emotion: draw the inner third of each "
            "eyebrow lifted and pulled toward the center, so the brows "
            "form a shallow inverted V - a tent shape - over the bridge "
            "of the nose, with short vertical worry lines between them. "
            "This is the non-negotiable feature; without it the face "
            "reads as merely tired. The eyes: upper lids lowered to "
            "half-mast, the gaze directed down or past the viewer, never "
            "meeting the eye directly. Add a highlight of wetness along "
            "the lower lid - grief glistens before it streams. For the "
            "acute wave, draw the lids squeezed or the eyes streaming, "
            "the lower lids pushed up by the cheek muscles. The nose and "
            "cheeks: in held grief the nostrils may flare slightly with "
            "the suppressed breath; in open grief the whole midface "
            "flushes. The mouth: corners drawn down and outward, the "
            "lower lip full and trembling or pressed thin in suppression, "
            "and for the held-back sob, bunch the chin - small dimpling "
            "of the chin boss as the mentalis fights the cry. The jaw: "
            "in quiet grief slightly slack, mouth barely open, as if the "
            "face has forgotten its posture; in the wave, jaw working, "
            "throat visibly swallowing. The whole head: tilted a few "
            "degrees down or to one side - grief rarely holds the head "
            "level. Lighting and context for the artist: grief reads "
            "best in soft or low light, the face slightly turned away, "
            "the body folded. For the actor: the fastest route into the "
            "physicality is the breath - take the breath high and short, "
            "let the exhales shudder, and keep the gaze unfocused; the "
            "face will follow the breath more honestly than willpower "
            "follows intention. For the writer: the telling details are "
            "small and involuntary - the throat working, the second "
            "swallow, the eyes brightening at a word - never the grand "
            "gesture. A final note for all three crafts: the most "
            "truthful grief on the page, stage, or canvas is often the "
            "managed kind - the character holding it together with the "
            "leakage showing - because that is how grief most often "
            "appears in the world."),
        "sig_lens": (
            "His Signature science gives the artist the weavers brief: "
            "draw not the tear but the thread - the brow as tent-poles "
            "over the wound, the gaze as the shuttle paused mid-pass, "
            "the mouth as the pattern held but not finished. In the "
            "Signature view the truest portrait of grief shows the work "
            "in progress: the mending visible, the weavers hands still "
            "moving, the cloth not yet smooth."),
        "how_it_works": (
            "These notes are reverse-engineered from facial action "
            "coding: each described feature maps to specific muscle "
            "actions (inner frontalis plus corrugator for the grief "
            "brow; depressor anguli oris for the downturned mouth; "
            "mentalis for the bunched chin; orbicularis oculi for the "
            "squeezed lids). Artists and actors work best from muscle-"
            "level description because it is buildable - a brow shape "
            "can be drawn, a breath pattern can be performed - while "
            "emotion words (draw sadness) are not. The breath-first "
            "advice for actors follows from the physiology: respiratory "
            "patterns drive autonomic state more directly than facial "
            "posing does, so adopting griefs breath tends to recruit the "
            "genuine facial program rather than a posed imitation. The "
            "recommendation of the managed kind as most truthful "
            "reflects base rates in real life: full sob faces are rare "
            "and brief, while composed-with-leakage is the modal public "
            "appearance of grief. Writers are directed to involuntary "
            "details because readers recognize truth in the small "
            "uncontrolled signs - the grand gesture reads as melodrama "
            "precisely because real grief rations its grand gestures."),
        "key_points": [
            "The grief brow (inner brows lifted and drawn together, tent shape) is the non-negotiable feature.",
            "Build from muscle level: glistening lower lids, downturned mouth corners, trembling lip, bunched chin in suppression.",
            "The head tilts down or sideways; grief rarely holds the head level.",
            "For actors: start with the breath (high, short, shuddering exhales); the face follows the breath.",
            "The most truthful rendering is often managed grief with leakage showing - the modal real-world appearance.",
        ],
        "requirements": [
            "No special equipment; these notes are for artists, actors, and writers",
            "Study willing subjects or mirrors; never stare at grieving strangers for reference",
            "Render with dignity; grief is not a costume",
            "No diagnosing of any real person from these descriptions",
        ],
        "standards": [
            "Feature notes mapped from facial action coding research",
            "Descriptive and educational language only; no diagnostic claims",
        ],
        "citations": [CIT_EKMAN, CIT_PLUTCHIK, CIT_APA],
    },
    {
        "key": "classic_triggers",
        "name": "The Classic Triggers of Grief",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Grief triggers are the things that summon the wave, and the "
            "classic ones are classic because nearly every griever meets "
            "them. Places: the empty chair, the side of the bed, the "
            "restaurant, the hospital corridor, the cemetery, the house "
            "itself - any space the lost one filled now stages the "
            "absence. Objects: clothing that still carries a shape, the "
            "phone with the number still saved, photographs, the "
            "unfinished project, the favorite mug. Senses: songs are the "
            "most famous trigger - music binds to emotional memory more "
            "tightly than almost anything - but smells (cooking, "
            "cologne, rain on a particular street), tastes, and even "
            "textures ambush just as surely. Dates: anniversaries of the "
            "death or the loss, birthdays, holidays, the season it "
            "happened - the calendar itself becomes a minefield, and "
            "many grievers feel the dread building weeks before the date "
            "without knowing why. Milestones: graduations, weddings, "
            "births, promotions the lost one will not witness - grief "
            "for the future that will not include them. Words and news: "
            "someone asking how many children you have, a form asking "
            "marital status, hearing the name spoken casually by a "
            "stranger. Other peoples happiness: a couple laughing in the "
            "park can detonate grief not from bitterness but from the "
            "sudden vivid contrast. The triggers share a mechanism: each "
            "is a moment when the minds updated model collides with an "
            "un-updated slot - the brain predicted their presence, and "
            "reality delivered absence. Knowing the classics helps in "
            "three ways. Grievers can anticipate and prepare rather than "
            "be perpetually ambushed - drive a different route for a "
            "while, keep the first holiday simple, have an exit plan. "
            "Supporters can stop accidentally triggering - think before "
            "the well-meaning but loaded question. And everyone can "
            "normalize the wave: a trigger is not a setback, it is the "
            "grief doing its scheduled work at a scheduled reminder."),
        "sig_lens": (
            "His Signature science calls the triggers the loose threads: "
            "every place, object, song, and date where the lost ones "
            "thread still hangs unbound from the cloth, catching the "
            "hand that passes. In the Signature view the griever does "
            "not cut these threads but binds them one by one - the song "
            "reclaimed, the chair re-sat, the date re-marked - until "
            "each loose thread is woven back into the pattern as "
            "memory instead of wound."),
        "how_it_works": (
            "Triggers work through associative memory and prediction "
            "error. Emotional memories are stored with their sensory "
            "context, and a matching cue - the song, the smell - "
            "reactivates the whole network, including the attachment "
            "system, which then fires its expectation of the persons "
            "presence. The mismatch between expectation and reality is "
            "registered as a prediction error, and prediction errors "
            "drive both the pang and the wave. Music is an especially "
            "potent cue because it engages emotional and autobiographical "
            "memory systems simultaneously and unfolds over time, "
            "sustaining the reactivation. Anniversary reactions occur "
            "because temporal context is itself a memory cue: the brain "
            "encodes seasons and dates, and as the date approaches the "
            "associated network pre-activates - which is why dread can "
            "precede conscious recognition of the date. Anticipation "
            "helps because coping resources can be mobilized in advance: "
            "the wave is the same size, but the griever meets it braced "
            "rather than ambushed, and braced waves pass faster."),
        "key_points": [
            "Classic triggers: places, objects, songs and smells, dates and anniversaries, milestones, loaded questions, others happiness.",
            "Each trigger is a collision between the minds updated model and an un-updated slot predicting their presence.",
            "Music binds to emotional memory tightly; anniversary dread can precede conscious recognition of the date.",
            "Grievers can anticipate and prepare: alternate routes, simple holidays, exit plans.",
            "A triggered wave is not a setback; it is the grief doing scheduled work at a scheduled reminder.",
        ],
        "requirements": [
            "No special equipment; this record is for reading and reflection",
            "Map personal triggers gently; the list is for preparation, not avoidance forever",
            "Supporters: think before asking loaded questions of the bereaved",
            "No diagnosing of any real person from these descriptions",
        ],
        "standards": [
            "Trigger mechanisms drawn from associative memory and anniversary-reaction literature",
            "Descriptive and educational language only; no diagnostic claims",
        ],
        "citations": [CIT_PARKES, CIT_WORDEN, CIT_APA],
    },
    {
        "key": "personal_triggers",
        "name": "Personal Triggers: Memories, Anniversaries, and Private Associations",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Beyond the classic triggers lies a private minefield no one "
            "else can map: the triggers only this griever has. A brand of "
            "tea nobody else would notice. The particular way light fell "
            "across a kitchen table on Sunday mornings. A joke with a "
            "punchline only two people knew. The voicemail still saved, "
            "listened to on hard days like medicine that is also poison. "
            "The route to the hardware store. The password that was their "
            "birthday. These private associations are powerful precisely "
            "because they are unshared: there is no cultural script for "
            "them, no one else anticipates them, and the griever is "
            "ambushed in solitude. Anniversaries deserve special "
            "attention because they operate on two levels. The marked "
            "anniversaries - the death date, the birthday, the wedding "
            "date - are at least known; the griever can prepare, "
            "simplify the day, gather people or arrange solitude. The "
            "unmarked anniversaries are sneakier: the day the diagnosis "
            "came, the last ordinary Tuesday, the season when it "
            "happened, the first warm day of the year they will not see. "
            "Many grievers report a heavy, restless feeling arriving days "
            "before they consciously realize what date is coming - the "
            "body keeping the calendar the mind tried to discard. "
            "Memories as triggers have their own texture. Early grief "
            "memories are often intrusive and sensory: the hospital room, "
            "the last conversation replayed for the thing unsaid. Later, "
            "memories become more voluntary and more bittersweet: the "
            "vacation, the laugh, the ordinary evening that has become "
            "precious precisely because it was ordinary. Both kinds can "
            "trigger waves; the difference is that the later kind is "
            "increasingly survivable, sometimes even welcome - grief "
            "transforming, by slow degrees, from ambush into visitation. "
            "The practical art of personal triggers is mapping without "
            "obsessing: noticing which ones reliably detonate, deciding "
            "which to temporarily avoid (the voicemail can wait), which "
            "to approach deliberately (listening on the anniversary, on "
            "purpose, with support), and which to reclaim (their recipe, "
            "cooked now as honor rather than wound). Over time the map "
            "changes: triggers fade, new ones surface, and eventually "
            "some become treasures - the tea brand bought deliberately, "
            "with love, because it was theirs."),
        "sig_lens": (
            "His Signature science treats the private triggers as the "
            "hidden knots in the cloth: only the weaver knows where each "
            "one lies, because only the weaver tied them. In the "
            "Signature view the mapping of these knots is sacred "
            "cartography - the griever charting their own territory - "
            "and each knot patiently untied and rewoven becomes not a "
            "snare but a signature: this tea, this light, this joke, "
            "kept on purpose as the enduring pattern of love."),
        "how_it_works": (
            "Private triggers work through the same associative machinery "
            "as classic ones, but with idiosyncratic cue sets: the "
            "grievers unique shared history created thousands of paired "
            "associations (tea brand plus morning plus person) that no "
            "generic list can predict. Unmarked anniversary reactions "
            "demonstrate implicit temporal memory: the brain encodes "
            "seasonal and date context alongside emotional events, and "
            "the approaching context reactivates the network before "
            "declarative memory names the date - hence dread preceding "
            "recognition. The transformation from ambush to visitation "
            "reflects memory reconsolidation: each time a memory is "
            "retrieved in a safe context and re-stored, its emotional "
            "charge can update slightly, so deliberately revisited "
            "memories gradually lose their detonating quality while "
            "keeping their meaning. This is the mechanism behind the "
            "advice to approach some triggers on purpose: controlled "
            "retrieval with support rewrites the association from "
            "threat to tribute. Avoidance has its place - a raw trigger "
            "need not be faced daily - but total permanent avoidance "
            "prevents reconsolidation and freezes the trigger at full "
            "power, which is why gentle, paced reclamation works better "
            "than either constant exposure or eternal evasion."),
        "key_points": [
            "Private triggers are idiosyncratic: a tea brand, a light pattern, a password - unshared and unscripted.",
            "Unmarked anniversaries ambush via implicit temporal memory; dread can precede conscious recognition of the date.",
            "Early memories intrude; later memories can become voluntary and bittersweet - ambush transforming into visitation.",
            "Map triggers to prepare: temporarily avoid some, deliberately approach others, reclaim the rest over time.",
            "Deliberate revisiting with support rewrites associations from threat to tribute via reconsolidation.",
        ],
        "requirements": [
            "No special equipment; this record is for reading and reflection",
            "Map gently and privately; this territory belongs to the griever alone",
            "Reclaim at the grievers pace; no schedule for turning wounds into treasures",
            "No diagnosing of any real person from these descriptions",
        ],
        "standards": [
            "Anniversary and reconsolidation mechanisms drawn from memory and bereavement literature",
            "Descriptive and educational language only; no diagnostic claims",
        ],
        "citations": [CIT_PARKES, CIT_NEIMEYER, CIT_APA],
    },
    {
        "key": "surprise_triggers",
        "name": "Surprise Triggers: The Unexpected Things That Set Off Grief",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The strangest feature of griefs trigger system is how "
            "utterly unreasonable it can be. Grievers report being "
            "undone by things that have no logical connection to the "
            "loss: a stranger on the bus laughing exactly the way they "
            "laughed. A perfectly ripe peach. The smell of cut grass on "
            "a day they would have loved. A cartoon from childhood. The "
            "sound of a key in a lock. A sale on socks. None of these "
            "are about the person, and all of them are entirely about "
            "the person - because grief sensitizes the whole meaning-"
            "system, and anything vivid can complete the circuit. "
            "Happiness itself becomes a trigger: a beautiful sunset, a "
            "childs delight, a moment of genuine laughter - and then the "
            "guilt-laced pang, I am happy and they are not here, or the "
            "simple unbearable contrast. Good news becomes a trigger: "
            "the promotion, the acceptance letter, the pregnancy - every "
            "joy arrives with an empty chair beside it. Other peoples "
            "ordinary lives become triggers: the old couple holding "
            "hands, the father teaching the bike, the family arguing "
            "about nothing in the checkout line - the unbearable "
            "visibility of what continues. Even relief becomes a "
            "trigger: the end of a long caregiving ordeal brings rest, "
            "and then rest brings guilt about the rest, and the guilt "
            "reopens the grief. Physical states trigger too: "
            "exhaustion, hunger, illness, and hormonal shifts all lower "
            "the threshold, so the wave that would have been a ripple on "
            "a rested day becomes a flood on a depleted one. The "
            "important reframe: surprise triggers are not signs of "
            "going crazy, not evidence of doing grief wrong, not "
            "setbacks. They are evidence that the attachment was woven "
            "through everything - the love was not confined to the "
            "person but distributed across a whole lived world, so the "
            "whole lived world now reports the absence. Grievers find "
            "comfort in simply knowing this is normal: the peach, the "
            "socks, the cartoon are all standard equipment of the "
            "territory. The wave passes, the griever is not broken, and "
            "life - strangely, faithfully - keeps offering both the "
            "triggers and, in time, the healing."),
        "sig_lens": (
            "His Signature science calls these the far threads: the "
            "weave of love was wider than anyone knew, its threads "
            "running out into peaches and sunsets and checkout lines, "
            "so the tear runs wider too. In the Signature view the "
            "surprise trigger is a compliment to the love - proof of "
            "how thoroughly it had furnished the world - and each far "
            "thread, once startled, can be gently gathered back into "
            "the pattern as gratitude."),
        "how_it_works": (
            "Surprise triggers work through spreading activation in an "
            "emotionally sensitized network. After a major loss the "
            "attachment and threat systems rest at higher baseline "
            "arousal, which lowers the activation threshold across the "
            "associative network: cues with only distant links to the "
            "loss can now complete the circuit. Mood-congruent processing "
            "adds a second engine: a grieving mind preferentially "
            "notices, remembers, and elaborates loss-relevant meanings, "
            "so the old couple or the ripe peach is not neutrally "
            "perceived but immediately routed through the absence. "
            "Contrast effects explain why happiness triggers: the minds "
            "comparison machinery registers the gap between the present "
            "good moment and the absent person who should share it, and "
            "the gap itself becomes the pang. Depletion effects (hunger, "
            "exhaustion, illness) lower prefrontal regulation, so "
            "affect that would be contained on a resourced day floods on "
            "a depleted one - the same trigger, different thresholds. "
            "None of this indicates pathology; it indicates a normally "
            "functioning associative memory system operating under "
            "abnormal load. Normalizing the mechanism is itself the "
            "intervention: the griever stops fearing their own mind, "
            "which lowers the secondary distress that amplifies every "
            "wave."),
        "key_points": [
            "Surprise triggers have no logical link to the loss: a peach, socks, a cartoon - yet all complete the circuit.",
            "Happiness, good news, others ordinary lives, and even relief can all trigger waves.",
            "Depletion (hunger, exhaustion, illness) lowers the threshold; the same cue floods on a depleted day.",
            "Surprise triggers prove the love was distributed across a whole lived world, not confined to the person.",
            "They are normal equipment of the territory, not signs of going crazy or doing grief wrong.",
        ],
        "requirements": [
            "No special equipment; this record is for reading and reflection",
            "Reassure freely: the unreasonable trigger is one of griefs most normal features",
            "Tend the bodys resources; depletion turns ripples into floods",
            "No diagnosing of any real person from these descriptions",
        ],
        "standards": [
            "Mechanisms drawn from associative network and affect-regulation literature",
            "Descriptive and educational language only; no diagnostic claims",
        ],
        "citations": [CIT_APA, CIT_PARKES, CIT_STROEBE_HB],
    },
    {
        "key": "chain_reactions",
        "name": "Chain Reactions: How One Grief Trigger Sets Off a Cascade",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Grief waves rarely arrive as single events; they arrive as "
            "cascades, one trigger setting off the next in a chain that "
            "can run for hours. A simulated cascade for learning: it "
            "starts innocently - a song in a coffee shop (trigger one). "
            "The song opens the memory of the road trip (trigger two, "
            "internal). The memory brings the realization that there "
            "will be no more road trips (trigger three: the future-"
            "absence pang). That thought summons the hospital months "
            "(trigger four), which summons the guilt about the sharp "
            "words spoken in exhaustion that week (trigger five), which "
            "summons the general verdict I was not enough (trigger six: "
            "the global self-attack). By now the griever is crying in "
            "the coffee shop, and a well-meaning stranger asks if they "
            "are okay (trigger seven: shame at public tears), which "
            "collapses into I cannot even go for coffee like a normal "
            "person (trigger eight). Ninety minutes later the wave "
            "passes, leaving exhaustion and the bewildered question: "
            "what just happened? What happened was a chain reaction - "
            "each link lowering the threshold for the next, the minds "
            "associative network running downhill. Cascades have a "
            "recognizable anatomy. The spark is usually small and "
            "sensory. The middle links are interpretive: memories, "
            "counterfactuals, global verdicts about self and world. The "
            "late links are meta: shame about the grief itself, despair "
            "about ever recovering. The whole chain is fueled by "
            "depletion and isolation - it runs longest at night, alone, "
            "tired, hungry. Interrupting a cascade is a learnable skill, "
            "and it works at any link. At the spark: notice and name "
            "(thats a trigger, not a verdict). At the middle: challenge "
            "the global verdicts gently (tired minds exaggerate; I was "
            "not enough is the exhaustion talking). At the late stage: "
            "refuse the meta-shame (crying in a coffee shop is allowed; "
            "grief has no dress code). Across the whole chain: change "
            "the body state - stand, walk, drink water, eat something, "
            "call someone, step into daylight - because cascades are "
            "embodied, and the body is the fastest lever. The most "
            "important thing to know about cascades: they always end. "
            "Every cascade in the history of grief has ended. Knowing "
            "that, in the middle of one, is a rope."),
        "sig_lens": (
            "His Signature science names the cascade the runaway row: "
            "one pulled thread snagging the next until the whole edge "
            "ravels. In the Signature view the weavers skill is the "
            "catch - the practiced hand that stops the run at any "
            "thread, ties it off with a named knot (this is a trigger, "
            "not a verdict), and returns the shuttle to its rhythm. "
            "Every caught cascade is mastery, and mastery compounds."),
        "how_it_works": (
            "Cascades are spreading activation with positive feedback. "
            "Each activated node (song, memory, guilt) primes its "
            "associates, lowering their firing thresholds, so the "
            "network runs downhill: activation begets activation. "
            "Interpretive links (counterfactuals, global verdicts) add "
            "fuel because they recruit additional emotion systems - "
            "guilt recruits self-punishment circuitry, global verdicts "
            "recruit hopelessness - each adding arousal that further "
            "lowers thresholds. Meta-links (shame about grieving) add a "
            "second-order loop: distress about distress, which "
            "research on emotion regulation identifies as a key "
            "amplifier. Depletion removes the brakes: prefrontal "
            "regulation, which could damp the spread, is impaired by "
            "fatigue, hunger, and sustained arousal. Interruption works "
            "by breaking the feedback at any point: naming recruits "
            "prefrontal labeling, which measurably reduces amygdala "
            "reactivity; challenging global verdicts cuts the "
            "interpretive fuel; changing body state alters the arousal "
            "substrate the cascade runs on. The always-ends property "
            "reflects neural habituation and resource limits: no "
            "affective cascade can sustain peak indefinitely, so every "
            "wave, however tall, is time-limited by the machinery "
            "itself."),
        "key_points": [
            "Grief waves arrive as cascades: spark (sensory) -> middle links (memories, counterfactuals, verdicts) -> late links (meta-shame).",
            "Each link lowers the threshold for the next; depletion and isolation make chains run longest.",
            "Interrupt at any link: name the trigger, challenge global verdicts gently, refuse meta-shame.",
            "Change the body state - walk, water, food, daylight, contact - cascades are embodied and the body is the fastest lever.",
            "Every cascade ends; knowing that in the middle of one is a rope.",
        ],
        "requirements": [
            "No special equipment; this record is for reading and reflection",
            "Practice interruption on small cascades first; the skill compounds",
            "If cascades feel unmanageable, a grief counselor can teach the skill directly",
            "No diagnosing of any real person from these descriptions",
        ],
        "standards": [
            "Cascade mechanics drawn from associative network and emotion-regulation research",
            "Descriptive and educational language only; no diagnostic claims",
        ],
        "citations": [CIT_APA, CIT_STROEBE_HB, CIT_WORDEN],
    },
    {
        "key": "behavior_actions",
        "name": "What People Do When They Feel Grief",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Grief is visible in what people do long before they name "
            "what they feel. The searching behaviors come first and are "
            "the most poignant: the griever scans crowds for the face, "
            "reaches for the phone to call, sets the extra plate, buys "
            "the favorite food on autopilot, drives the old route. These "
            "are not confusion; they are the attachment system running "
            "its ancient program - seek the lost one - on a modern loss "
            "it cannot solve. The withdrawing behaviors follow: "
            "canceling plans, letting calls go to voicemail, leaving "
            "gatherings early or not going, spending long hours alone. "
            "Withdrawal in grief is usually not rejection of others; "
            "it is conservation - social performance costs energy the "
            "griever does not have, and solitude is where the waves can "
            "come without management. The preserving behaviors: keeping "
            "the room exactly as it was, wearing their clothing, "
            "maintaining the rituals (the Sunday call now made to no "
            "one), tending the grave or the memorial, keeping every "
            "voicemail. Preservation is the minds way of keeping a "
            "place for what is gone while it learns the new shape of "
            "the world. The restless behaviors: pacing, cleaning "
            "frenzies, sudden urges to rearrange furniture or give "
            "everything away or keep everything, midnight organizing of "
            "drawers. Restlessness is protest energy with nowhere to "
            "go. The numbing behaviors: long hours of television, "
            "scrolling, overwork, overeating or overdrinking - any "
            "activity that fills the hours without requiring feeling. "
            "Some numbing is ordinary rest; persistent heavy numbing is "
            "the grief asking for help through the side door. The "
            "reaching behaviors, healthiest of all: telling the story "
            "repeatedly to patient listeners, writing letters never "
            "sent, creating memorials, carrying forward a value or "
            "project of the lost one, seeking out others who understand. "
            "Reading someones grief behavior is reading their coping: "
            "searching means the bond is still mapped as present, "
            "withdrawing means the battery is low, preserving means the "
            "mind is keeping a place, restlessness means protest energy "
            "needs a channel, numbing means the pain needs a safer "
            "container, reaching means the grief is finding its way "
            "toward meaning. All of these are normal passages. The "
            "compassionate response is never to correct the behavior "
            "but to meet the need underneath it."),
        "sig_lens": (
            "His Signature science reads each behavior as the weavers "
            "hands at work: searching is the hand reaching for the "
            "missing thread, withdrawing is the weaver turning the loom "
            "to the wall for quiet work, preserving is the careful "
            "keeping of the pattern, restlessness the shuttle with "
            "nowhere to land, and reaching - the telling, the making, "
            "the carrying-forward - is the new row begun. In the "
            "Signature view every behavior is the craft continuing."),
        "how_it_works": (
            "Grief behaviors map onto the underlying systems. Searching "
            "is Bowlbys protest phase made visible: the attachment "
            "system, evolved to recover separated young, runs its "
            "seeking program regardless of the loss type - the "
            "absurdity of setting the extra plate is the programs "
            "age showing, not the grievers. Withdrawal reflects both "
            "the de-activating motor program of sadness and rational "
            "energy economics: social interaction demands facial work, "
            "conversation tracking, and emotion management, all "
            "expensive under griefs cognitive load. Preservation "
            "behaviors serve the continuing bond: maintaining connection "
            "through objects and rituals while the internal model "
            "updates, a documented healthy pattern when it coexists "
            "with rebuilding. Restlessness channels the activating "
            "partners (anger, anxiety) into motor output - the body "
            "discharging arousal it cannot otherwise use. Numbing is "
            "avoidance coping: effective short-term (the system gets "
            "rest), costly long-term if it becomes the only strategy, "
            "because avoided material is never reconsolidated. Reaching "
            "behaviors - storytelling, memorializing, carrying forward - "
            "are meaning-reconstruction in action, the mechanisms "
            "research links most strongly to healthy adaptation."),
        "key_points": [
            "Searching behaviors (scanning crowds, setting the plate) are the ancient attachment program running its seeking routine.",
            "Withdrawing is usually energy conservation, not rejection; solitude is where waves come without management.",
            "Preserving (rooms, rituals, voicemails) keeps a place for what is gone while the mind learns the new shape.",
            "Restlessness is protest energy needing a channel; persistent heavy numbing is grief asking for help sideways.",
            "Reaching behaviors - storytelling, memorializing, carrying forward - are meaning-reconstruction in action.",
        ],
        "requirements": [
            "No special equipment; this record is for reading and reflection",
            "Read behavior as communication of need, never as misbehavior to correct",
            "Meet the need underneath the behavior, not the behavior itself",
            "No diagnosing of any real person from these descriptions",
        ],
        "standards": [
            "Behavior patterns drawn from Bowlby, Worden, and continuing-bonds research",
            "Descriptive and educational language only; no diagnostic claims",
        ],
        "citations": [CIT_BOWLBY, CIT_WORDEN, CIT_NEIMEYER],
    },
    {
        "key": "speech_patterns",
        "name": "What People Say: Grief in Words, Tone, and Speech Patterns",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Grief has a voice, and those who listen carefully can hear "
            "it. The characteristic phrases repeat across grievers like "
            "a shared vocabulary: I cant believe theyre gone (the mind "
            "still updating). It doesnt feel real (derealization, the "
            "world slightly staged). I keep expecting them to walk "
            "through the door (the prediction error, spoken plainly). If "
            "only I had... (the counterfactual machinery). I dont know "
            "who I am anymore (identity disruption - the self was built "
            "around the bond). Whats the point (the meaning system under "
            "load). Im fine, really (the managed face, in words). And "
            "the one supporters most need to hear accurately: I just "
            "miss them - the whole of grief in four words. Tone carries "
            "as much as content. Grieving speech is often quieter, "
            "slower, flatter - less melodic variation, longer pauses, "
            "sentences that trail off unfinished because the thought "
            "dissolved or the feeling arrived mid-sentence. The voice "
            "may thicken or crack on particular words (names, love, "
            "home), and some grievers develop a characteristic catch - "
            "a small swallowed sob - that regular listeners learn to "
            "recognize as the wave passing through. Speech patterns "
            "shift in recognizable ways. Repetition: the same story told "
            "again and again, often with identical phrasing - this is "
            "not forgetfulness but processing; each retelling files the "
            "event slightly deeper. Present tense slips: speaking of the "
            "lost one in present tense months later (he loves this "
            "restaurant) - the old model asserting itself, usually "
            "followed by a pained correction. Negation-heavy language: "
            "cant, dont, wont, never - the vocabulary of absence. "
            "Concrete smallness: grievers often talk in small concrete "
            "details (the socks, the toast, the parking spot) rather "
            "than abstractions, because the loss is stored in the "
            "concrete. Listening to grief speech well is a skill: do "
            "not correct the present tense, do not hurry the repetition, "
            "do not fill the pauses - the pauses are where the feeling "
            "is. The grievers words are not a problem to solve; they "
            "are the work being done aloud."),
        "sig_lens": (
            "His Signature science hears grief speech as the weaver "
            "counting threads aloud: the repetition the counting, the "
            "pauses the fingers finding the next thread, the small "
            "concrete details the individual fibers named one by one. "
            "In the Signature view every retold story is a row rewoven, "
            "and the patient listener is the apprentice holding the "
            "frame steady while the master works."),
        "how_it_works": (
            "Grief speech patterns follow from cognitive load and "
            "memory structure. Slower, flatter, pause-filled speech "
            "reflects reduced cognitive resources: grief consumes "
            "working memory, leaving less for speech planning, so "
            "utterances simplify and stall. Repetition serves memory "
            "consolidation: each retelling reactivates the event "
            "memory and re-stores it with slightly updated emotional "
            "marking - the mechanism of narrative processing that "
            "research links to adaptation. Present-tense slips reveal "
            "the predictive model: language production draws on the "
            "brains world-model, and where the model still contains "
            "the person as present, present tense emerges naturally; "
            "the pained correction marks the moment the updated model "
            "overrides. Concrete smallness reflects how autobiographical "
            "memory is actually stored - in sensory specifics, not "
            "abstractions - so authentic grief speech gravitates to "
            "the concrete. The voice thickening on trigger words is "
            "autonomic arousal (increased muscle tension in the vocal "
            "tract, altered respiration) breaking through the speech "
            "plan. Listening without correcting works because "
            "interruption breaks the consolidation process the "
            "repetition is performing."),
        "key_points": [
            "Characteristic phrases map to mechanisms: disbelief (updating), unreality (derealization), if only (counterfactuals).",
            "Grieving speech is quieter, slower, flatter, with long pauses and trailing sentences.",
            "Repetition is processing, not forgetfulness; each retelling files the event deeper.",
            "Present-tense slips reveal the old world-model; never correct them aloud.",
            "Listen without hurrying or filling pauses; the words are the work being done aloud.",
        ],
        "requirements": [
            "No special equipment; this record is for reading and reflection",
            "When listening to grievers: do not correct, hurry, or fill pauses",
            "Learn the catch in familiar voices as the wave passing through",
            "No diagnosing of any real person from these descriptions",
        ],
        "standards": [
            "Speech patterns drawn from narrative-processing and bereavement literature",
            "Descriptive and educational language only; no diagnostic claims",
        ],
        "citations": [CIT_NEIMEYER, CIT_WORDEN, CIT_APA],
    },
    {
        "key": "decisions_judgment",
        "name": "How Grief Changes Decisions and Judgment",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Grief changes the mind that makes the decisions, which is "
            "why the old advice - dont make big decisions in the first "
            "year - exists and mostly deserves respect. Risk judgment "
            "shifts: some grievers become strikingly risk-averse, "
            "unable to tolerate any further uncertainty - the world has "
            "proven it can take things away, so every choice is scanned "
            "for what else could be lost. Others swing the opposite way "
            "into recklessness: the worst has happened, so caution feels "
            "pointless; this is the griever driving too fast, spending "
            "too freely, or taking chances their pre-loss self would "
            "never have taken. Time horizon shortens: the future feels "
            "unreal or unplannable, so decisions collapse into the "
            "immediate - what gets through today - and long-term "
            "planning feels absurd or disloyal (how can I plan a future "
            "they are not in). Cognitive bandwidth narrows: working "
            "memory is consumed by grief processing, leaving less for "
            "comparing options, reading fine print, or holding multiple "
            "scenarios - so grievers satisfice, decide impulsively, or "
            "freeze entirely. Values clarify and scramble simultaneously: "
            "many grievers report sudden clarity about what matters "
            "(time with people, not things) alongside total confusion "
            "about practical direction. Social decisions distort: saying "
            "yes to everything from guilt and exhaustion, or no to "
            "everything from depletion. Financial decisions are the "
            "classic danger zone: the newly widowed pressured to sell "
            "the house, move cities, quit the job, give away large sums "
            "- all while the decision machinery is at its weakest. The "
            "practical guidance is well-established and kind: postpone "
            "reversible-big decisions when possible (the house will "
            "still be there in a year); for unavoidable decisions, "
            "borrow other peoples prefrontal cortex - a trusted friend, "
            "advisor, or family member to hold the options steady while "
            "you feel the feelings; make lists, because the impaired "
            "working memory cannot hold what paper can; and treat the "
            "urge for dramatic change with curiosity rather than "
            "obedience (the urge to move, quit, or give everything away "
            "is often the protest system demanding action - any action - "
            "and it usually quiets once named). Grief does not make "
            "people stupid; it makes them temporarily cognitively "
            "loaded, emotionally flooded, and future-blind - a bad "
            "combination for irreversible choices, and a fully "
            "understandable one."),
        "sig_lens": (
            "His Signature science counsels the weaver mid-mending: do "
            "not cut the cloth while the tear is still being measured. "
            "In the Signature view the first year is for reweaving, "
            "not for redesigning the whole tapestry - the big cuts "
            "wait until the hands are steady and the pattern clear, "
            "and borrowing anothers steady hands meanwhile is craft "
            "wisdom, not weakness."),
        "how_it_works": (
            "Decision changes follow from three loaded systems. "
            "Affect-as-information: the brain uses current feeling as "
            "data about the world, so a griever awash in loss-feeling "
            "systematically overestimates further loss probability - "
            "driving risk aversion - while the numb/defiant variant "
            "underestimates it, driving recklessness. Cognitive load: "
            "grief processing occupies working memory and executive "
            "function measurably (bereaved people show impaired "
            "attention and decision performance), forcing simpler "
            "strategies - satisficing, impulsivity, or paralysis. "
            "Future-simulation damage: prospection (imagining futures) "
            "draws on the same episodic machinery that grief has "
            "flooded with loss content, so simulated futures come back "
            "empty or painful, collapsing the time horizon. The "
            "borrowed-cortex strategy works because social cognition "
            "can literally offload executive function: a trusted "
            "other holding the options compensates for the impaired "
            "working memory. The one-year guideline is heuristic, not "
            "law - it marks the period when these impairments are "
            "typically strongest - and unavoidable decisions made with "
            "support and lists fare far better than delayed ones made "
            "in crisis."),
        "key_points": [
            "Grief shifts risk judgment: toward risk aversion (the world takes things) or recklessness (the worst happened).",
            "Time horizon shortens; long-term planning can feel absurd or disloyal.",
            "Working memory consumed by grief forces simpler strategies: satisficing, impulsivity, or freezing.",
            "Financial and other irreversible decisions are the classic danger zone in early grief.",
            "Postpone what can wait; borrow trusted others thinking, make lists, treat dramatic urges with curiosity.",
        ],
        "requirements": [
            "No special equipment; this record is for reading and reflection",
            "Never pressure a griever into big irreversible decisions",
            "Offer to hold options steady rather than deciding for them",
            "No diagnosing of any real person from these descriptions",
        ],
        "standards": [
            "Decision effects drawn from affect-cognition and bereavement literature",
            "Descriptive and educational language only; no diagnostic claims",
        ],
        "citations": [CIT_APA, CIT_STROEBE_HB, CIT_WORDEN],
    },
    {
        "key": "intensity_escalation",
        "name": "Behavior Under Intensity: How Grief-Driven Actions Escalate",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "As griefs volume rises, behavior escalates along a "
            "recognizable ladder - and knowing the rungs helps grievers "
            "and supporters recognize where things stand. Rung one, "
            "quiet coping: the griever functions with effort, uses "
            "healthy channels (talking, walking, resting), waves come "
            "and pass. Support needed: ordinary kindness, patience. Rung "
            "two, strained coping: functioning frays - missed "
            "appointments, snapped words, heavier numbing (longer "
            "screen hours, more drinking), withdrawal deepening. The "
            "griever knows they are struggling but can still steer. "
            "Support needed: practical help offered concretely (Ill bring "
            "dinner Thursday beats let me know), gentle check-ins. Rung "
            "three, overwhelmed: daily functioning breaks down - not "
            "eating, not sleeping, not answering, hygiene slipping, "
            "work impossible. Waves are near-constant or numbness is "
            "total. The griever cannot steer alone. Support needed: "
            "steady presence, help with basics (food, bills, children), "
            "and a bridge to professional support - a grief counselor, "
            "support group, or clinician - offered warmly, not as "
            "alarm. Rung four, crisis: the griever expresses being "
            "unable to go on, shows signs of harming themselves, or "
            "completely stops functioning (not eating for days, unable "
            "to get out of bed for weeks). This rung needs immediate, "
            "loving, direct action: stay with them, contact crisis "
            "resources or emergency services, do not leave them alone "
            "with the crisis. The escalation is not a character arc; it "
            "is usually driven by load exceeding resources - more loss, "
            "less sleep, less support, new stressors stacking. Which "
            "means de-escalation is usually possible by reversing the "
            "equation: sleep, food, company, reduced demands, "
            "professional help. Two things matter enormously. First, "
            "rungs are not judgments: needing rung-three help is not "
            "failure, it is arithmetic. Second, movement between rungs "
            "goes both ways and often quickly - a griever at rung three "
            "on Tuesday can be at rung one by Sunday with rest and "
            "support, and that is normal. The practical skill is rung-"
            "recognition without panic: see clearly, match the response "
            "to the rung, escalate care as the rung rises, and always "
            "preserve the grievers dignity - help that humiliates is "
            "not help."),
        "sig_lens": (
            "His Signature science reads the rungs as the tension gauge "
            "on the loom: rung one the warp humming true, rung two the "
            "threads straining, rung three the frame groaning under "
            "the load, rung four the cloth about to tear free. In the "
            "Signature view the wise response at every rung is the same "
            "craft: ease the tension, brace the frame, never blame the "
            "weaver for the weight of the work."),
        "how_it_works": (
            "Escalation follows the load-resources equation from stress "
            "theory: distress rises as demands exceed coping resources, "
            "and each rung marks a wider gap. Rung two (strained coping) "
            "appears when arousal chronically exceeds recovery - the "
            "physiology of allostatic load. Rung three (overwhelmed) "
            "marks executive function failure under sustained load: the "
            "prefrontal systems that organize eating, sleeping, and "
            "working go offline when resources are fully consumed by "
            "affect processing. Rung four (crisis) reflects the collapse "
            "of future simulation: when prospection returns only pain, "
            "the motivation system loses its forward anchor. De-"
            "escalation works by restoring the equation from either "
            "side - reducing demands (fewer decisions, fewer "
            "obligations) or increasing resources (sleep, nutrition, "
            "social support, professional intervention). Professional "
            "support at rung three and above is indicated because "
            "trained counselors provide what depleted systems cannot "
            "self-generate: regulated co-presence, structured processing "
            "of stuck material, and monitoring for the transition to "
            "rung four. The both-directions property reflects that rungs "
            "track current load, not trait: change the load and the "
            "rung changes."),
        "key_points": [
            "Rung one (quiet coping): functioning with effort, healthy channels; needs ordinary kindness.",
            "Rung two (strained): fraying function, heavier numbing; needs concrete practical help.",
            "Rung three (overwhelmed): daily functioning breaks; needs steady presence and a bridge to professional support.",
            "Rung four (crisis): unable to go on or self-harm signs; needs immediate loving direct action and crisis resources.",
            "Rungs track load versus resources and move both ways; match care to the rung without panic or judgment.",
        ],
        "requirements": [
            "No special equipment; this record is for reading and reflection",
            "Learn crisis resources for your area before ever needing them",
            "Escalate care with the rung; never shame any rung",
            "No diagnosing of any real person from these descriptions",
        ],
        "standards": [
            "Escalation framing drawn from stress-load and bereavement-care literature",
            "Descriptive and educational language only; no diagnostic claims",
        ],
        "citations": [CIT_STROEBE_HB, CIT_WORDEN, CIT_SHEAR],
    },
    {
        "key": "healthy_expression",
        "name": "Expressing Grief Healthily: Saying It, Showing It, Channeling It",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Healthy expression of grief is not one technique but a "
            "repertoire - many channels, used in rotation, matched to "
            "the moment. Saying it: telling the story, out loud, to "
            "patient listeners, as many times as it needs telling. The "
            "repetition that bores the impatient is the processing that "
            "heals the griever; each telling files the event deeper. "
            "Naming the feeling precisely - this is missing, this is "
            "anger, this is guilt about the last week - recruits the "
            "brains labeling systems and measurably quiets reactivity. "
            "Writing unsent letters, keeping a grief journal, even "
            "talking aloud to the lost one (a practice as old as "
            "humanity and as normal as prayer) all count as saying it. "
            "Showing it: letting the tears come when they come, without "
            "apology or scheduling. Crying is the bodys discharge "
            "system for emotional arousal - not weakness but physiology. "
            "Showing it also means letting the face show, the posture "
            "fold, the voice crack: dropping the managed face in safe "
            "company is rest for the suppression systems. Channeling it: "
            "giving the griefs energy somewhere to go. Movement - "
            "walking, running, swimming, dancing, chopping wood - "
            "discharges the arousal the body is holding; grievers "
            "across cultures and centuries have walked their grief. "
            "Making - cooking their recipes, building the memorial, "
            "planting the garden, finishing their unfinished project, "
            "making art from the ache - converts protest energy into "
            "tribute. Ritual - lighting the candle, visiting the place, "
            "marking the date, the annual toast - gives the grief a "
            "container: instead of ambushing at random, it is invited "
            "at appointed times, which paradoxically reduces its power "
            "to ambush. Serving - helping other grievers, volunteering, "
            "carrying forward their cause - transforms the private ache "
            "into shared meaning, the mechanism research links most "
            "strongly to growth after loss. The repertoire matters "
            "because no single channel works every day: some days the "
            "griever can talk, some days only walk, some days only cry, "
            "some days only sit. Healthy expression is not expression "
            "without pain - it is expression that moves the grief "
            "through rather than storing it. The test is simple: after "
            "this channel, do I feel even slightly more like myself? "
            "Channels that pass the test, repeated over months, are the "
            "reweaving."),
        "sig_lens": (
            "His Signature science names the channels the shuttles: "
            "saying it the shuttle of the voice, showing it the "
            "shuttle of the body, channeling it the shuttle of the "
            "hands - and the wise weaver keeps all three flying. In "
            "the Signature view the told story, the walked mile, the "
            "planted garden, and the lit candle are all the same work "
            "in different fibers: the grief given somewhere true to "
            "go, row by honest row."),
        "how_it_works": (
            "Each channel works through documented mechanisms. "
            "Narrative telling drives memory reconsolidation: "
            "retrieval plus re-storage in a safe context gradually "
            "updates the events emotional marking. Affect labeling "
            "(naming the feeling) measurably reduces amygdala "
            "reactivity via prefrontal recruitment - putting feelings "
            "into words is literally calming at the neural level. "
            "Crying discharges autonomic arousal and triggers "
            "parasympathetic rebound plus social support elicitation - "
            "tears are both physiology and signal. Movement metabolizes "
            "stress chemistry: sustained aerobic activity clears "
            "cortisol and adrenaline while generating the neurochemistry "
            "of mild reward. Making and ritual externalize the internal: "
            "the grief given durable form becomes an object that can be "
            "visited rather than an ambush that visits - this is the "
            "continuing-bond mechanism made tangible. Serving recruits "
            "meaning-reconstruction, the strongest documented predictor "
            "of post-loss growth. Rotation matters because channels "
            "fatigue: talking helps until the words run dry, then the "
            "body needs the walk. The repertoire is the medicine "
            "cabinet; wisdom is knowing which shelf today needs."),
        "key_points": [
            "Saying it: telling the story repeatedly, naming feelings precisely, writing, journaling, talking aloud.",
            "Showing it: letting tears come, dropping the managed face in safe company - rest for suppression systems.",
            "Channeling it: movement discharges arousal; making converts protest into tribute; ritual contains; serving builds meaning.",
            "No single channel works every day; keep the whole repertoire in rotation.",
            "The test: after this channel, do I feel even slightly more like myself?",
        ],
        "requirements": [
            "No special equipment; these channels use voice, body, and hands",
            "Patient listeners for the telling; safe company for the showing",
            "Time and repetition; the repertoire works over months, not days",
            "No diagnosing of any real person from these descriptions",
        ],
        "standards": [
            "Channel mechanisms drawn from narrative, affect-labeling, and meaning-reconstruction research",
            "Descriptive and educational language only; no diagnostic claims",
        ],
        "citations": [CIT_NEIMEYER, CIT_WORDEN, CIT_APA],
    },
    {
        "key": "unhealthy_expression",
        "name": "Bottling Up or Exploding: What Unhealthy Expression Costs",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Grief must go somewhere; the only choice is where. The two "
            "classic unhealthy routings are bottling up and exploding, "
            "and both charge interest. Bottling up - suppression, "
            "stoicism as a permanent address, Im fine as a wall - feels "
            "like control. What it actually does is store the arousal "
            "in the body: the tension held in the jaw becomes the "
            "headache, the unshed tears become the stomach trouble and "
            "the 3 a.m. waking, the unfelt feelings become irritability "
            "that leaks sideways onto the people the griever loves "
            "most. Suppression is cognitively expensive - the managed "
            "face all day is exhausting - and it blocks reconsolidation: "
            "material never retrieved is never re-stored, so the grief "
            "stays frozen at full power instead of gradually updating. "
            "Bottled grief also isolates: people cannot comfort what "
            "they cannot see, so the suppressor grieves alone in a "
            "crowd, which deepens the loneliness that deepens the "
            "grief. Exploding - rage at small provocations, sobbing "
            "that cannot be steered, dramatic gestures, picking fights, "
            "burning bridges - feels like honesty. What it actually "
            "does is add secondary damage to the primary loss: the "
            "relationships scorched in the explosion become new losses "
            "to grieve, the shame after the outburst becomes a new "
            "wound, and the people whose support is most needed learn "
            "to keep their distance. Exploding also frightens the "
            "griever themselves - the loss of self-control on top of "
            "the loss that started everything. Both patterns usually "
            "come from the same root: no safe channel. The bottler "
            "never learned or never found where feelings are allowed; "
            "the exploder never learned the dosing - of feeling in manageable amounts."
            "of feeling in manageable amounts. The compassionate "
            "reframe, for self or others: these are not character "
            "verdicts but skill gaps, and skills can be built at any "
            "age. The way out of bottling is titrated expression - "
            "small, safe doses: ten minutes of writing, one honest "
            "conversation, a walk with the feelings instead of the "
            "screens. The way out of exploding is containment with "
            "dignity - not suppression but scheduling: the feelings get "
            "their full voice in the journal, the therapy room, the "
            "long walk, the trusted friends kitchen, and the rest of "
            "life gets the managed version. Both ways out honor the "
            "same truth: the grief is real, it deserves expression, "
            "and expression works best aimed, not sprayed or sealed."),
        "sig_lens": (
            "His Signature science warns of the two false weavings: "
            "the sealed cloth, where the tear is covered but never "
            "mended and rots underneath, and the wild unraveling, "
            "where the threads are yanked and the damage spreads. In "
            "the Signature view the master weaver does neither - the "
            "tear is faced steadily, worked in measured rows, each "
            "stitch placed with intention until the mending holds."),
        "how_it_works": (
            "Suppression backfires through ironic process theory: the "
            "effort to not feel requires monitoring the forbidden "
            "feeling, which keeps it activated - the classic rebound "
            "effect, where suppressed thoughts return more strongly. "
            "Physiologically, suppression increases sympathetic arousal "
            "rather than reducing it; the body works harder to hold the "
            "feeling down than to feel it. Socially, suppression blocks "
            "the support-elicitation function of emotional expression - "
            "visible distress is the signal that summons help, and the "
            "signal switched off leaves the griever unsupported. "
            "Exploding backfires through consequence accumulation and "
            "shame loops: each uncontrolled outburst creates "
            "interpersonal damage requiring repair, and the shame "
            "response adds a second-order distress that amplifies the "
            "original. Both patterns also freeze processing: suppression "
            "by preventing retrieval, explosion by flooding the system "
            "past the point where reconsolidation can occur - "
            "therapists call the optimal zone the window of tolerance, "
            "and both patterns live outside it in opposite directions. "
            "Titrated expression and scheduled containment both work by "
            "returning the system to the window: enough activation to "
            "process, enough structure to stay safe."),
        "key_points": [
            "Bottling up stores arousal in the body, blocks reconsolidation, exhausts the suppressor, and isolates them in a crowd.",
            "Exploding adds secondary damage: scorched relationships, shame, frightened supporters keeping distance.",
            "Both usually come from the same root: no safe channel - a skill gap, not a character verdict.",
            "Out of bottling: titrated expression in small safe doses. Out of exploding: containment with dignity, feelings fully voiced in safe settings.",
            "Expression works best aimed, not sprayed or sealed.",
        ],
        "requirements": [
            "No special equipment; this record is for reading and reflection",
            "Replace judgment of either pattern with curiosity about the missing channel",
            "Professional support if either pattern feels entrenched",
            "No diagnosing of any real person from these descriptions",
        ],
        "standards": [
            "Suppression and dysregulation costs drawn from emotion-regulation research",
            "Descriptive and educational language only; no diagnostic claims",
        ],
        "citations": [CIT_APA, CIT_STROEBE_HB, CIT_WORDEN],
    },
    {
        "key": "everyday_practices",
        "name": "Everyday Practices That Keep Grief in Balance",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Grief is carried in days, so it is steadied by days - by "
            "small practices, repeated, that keep the system in its "
            "window. The body practices: a daily walk, even a short one - "
            "movement is the most reliable grief medicine ever found, "
            "metabolizing the stress chemistry and returning the world "
            "to a manageable size. Regular sleep hours, guarded like "
            "appointments. Real meals at real times, even small ones. "
            "Daylight in the morning, which steadies the body clock that "
            "grief disrupts. The mind practices: ten minutes of writing - "
            "unsorted, unjudged, unshared if preferred - which gives the "
            "looping thoughts somewhere to land outside the head. Naming "
            "the days weather each morning (today is a wave day, today "
            "is a flat day), which turns ambush into forecast. One small "
            "planned pleasure daily - the good coffee, the familiar "
            "show, the hot bath - not as denial but as proof that the "
            "world still contains bearable things. The heart practices: "
            "one act of connection daily - a text, a call, sitting near "
            "another human - because isolation is griefs favorite "
            "accomplice. Speaking the lost ones name aloud sometimes, "
            "which keeps the bond ventilated instead of sealed. Letting "
            "one wave be fully felt without fighting it, which teaches "
            "the nervous system that waves end. The structure practices: "
            "a loose daily rhythm - wake, walk, work, rest - because "
            "decision fatigue is real and routine removes a hundred "
            "small choices. One manageable task completed daily, which "
            "rebuilds the sense of agency grief erodes. Saying no to one "
            "thing weekly, which protects the depleted battery. The "
            "meaning practices: the small ritual - candle, visit, "
            "annual toast - that gives grief its appointed times. "
            "Noticing one thing the loss clarified (what matters now), "
            "which lets meaning accrue without forcing it. None of "
            "these are dramatic, and that is the point: grief is not "
            "steadied by breakthroughs but by the accumulation of small "
            "steadinesses. The griever who walks, sleeps, eats, writes, "
            "connects, and rituals - imperfectly, most days - is doing "
            "the most evidence-aligned grief care that exists. And on "
            "the days when none of it happens, the practice is "
            "self-compassion: the routine will be there tomorrow; today "
            "the wave gets the day, and that is allowed too."),
        "sig_lens": (
            "His Signature science calls these the daily rows: the "
            "walk, the meal, the writing, the candle - each a single "
            "row woven, none spectacular, all load-bearing. In the "
            "Signature view the great reweaving is never accomplished "
            "in a heroic sitting but in ten thousand ordinary rows, "
            "and the weaver who shows up for the daily row, however "
            "uneven, is doing master work."),
        "how_it_works": (
            "Each practice targets a documented mechanism. Movement "
            "clears stress chemistry and restores neurochemical balance; "
            "it is the single best-supported behavioral intervention "
            "for low mood. Sleep regularity stabilizes the HPA axis and "
            "emotional reactivity - the body clock is a mood regulator. "
            "Writing externalizes looping cognition, freeing working "
            "memory (the expressive-writing literature shows reliable "
            "benefits). Naming the days weather is affect labeling plus "
            "forecasting, both of which reduce amygdala reactivity and "
            "the ambush quality of waves. Daily connection counters the "
            "isolation spiral: loneliness amplifies grief physiology, "
            "and even minimal contact down-regulates threat systems. "
            "Routine reduces decision load on depleted executive "
            "function; completed tasks rebuild self-efficacy, which "
            "grief erodes. Rituals provide the continuing bond a "
            "durable, bounded form. Self-compassion on missed days "
            "prevents the meta-shame cascade that turns one bad day "
            "into a bad week. Together the practices keep the system "
            "in the window of tolerance - activated enough to process, "
            "resourced enough to stay safe - which is the physiological "
            "definition of grief in balance."),
        "key_points": [
            "Body: daily walk, guarded sleep hours, real meals, morning daylight.",
            "Mind: ten minutes of writing, naming the days weather, one small planned pleasure.",
            "Heart: one act of connection daily, speaking their name, letting one wave be fully felt.",
            "Structure: loose daily rhythm, one manageable task, saying no weekly to protect the battery.",
            "Grief is steadied by accumulated small steadinesses, not breakthroughs; missed days get self-compassion.",
        ],
        "requirements": [
            "No special equipment; these practices use the ordinary day",
            "Start with one or two practices; add as capacity returns",
            "Self-compassion on the days none of it happens",
            "No diagnosing of any real person from these descriptions",
        ],
        "standards": [
            "Practices aligned with behavioral, sleep, and expressive-writing evidence",
            "Descriptive and educational language only; no diagnostic claims",
        ],
        "citations": [CIT_WORDEN, CIT_STROEBE_HB, CIT_APA],
    },
    {
        "key": "reading_signs",
        "name": "Reading the Signs: Recognizing Grief in Others",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Recognizing grief in others is a kindness skill, and like "
            "all skills it can be learned. The face: the grief brow "
            "(inner brows lifted and drawn together), the downcast or "
            "unfocused gaze, the glistening eyes, the mouth corners held "
            "down, the swallowed sob disguised as a cough. These signs "
            "are most visible in the unguarded moment - arriving at the "
            "desk, in the elevator, when they think no one is watching. "
            "The body: the folded posture, the slowed movement, the "
            "self-embrace arms, the tiredness that exceeds the day. The "
            "voice: quieter, flatter, slower; the thickening on certain "
            "words; the long pauses. The behavior: the canceled plans, "
            "the declined invitations, the work that slipped, the "
            "uncharacteristic irritability or tearfulness, the "
            "preserving (the desk photo now prominent) or the searching "
            "(mentioning them constantly, or never mentioning them at "
            "all - both can signal). The calendar: grief has dates - "
            "the recent loss, the upcoming anniversary - and a person "
            "struggling in the weeks around a known date is usually "
            "struggling with the date. The discrepancies: the mouth "
            "saying fine while the body says otherwise; the cheerful "
            "performance that drops the instant the audience leaves; "
            "the laugh that arrives a beat too fast and ends too "
            "abruptly. Reading well means reading gently. The signs are "
            "for adjusting yourself, not for announcing your diagnosis: "
            "you soften your pace, offer the easier option, make room, "
            "check in later - you do not say I can tell youre grieving. "
            "Reading well also means holding uncertainty: tiredness can "
            "be illness, withdrawal can be depression, irritability can "
            "be a hundred things. The signs suggest, they never prove, "
            "and the respectful move is always to respond to the "
            "apparent need (rest, space, kindness) rather than to a "
            "label. And reading well means minding the cultural lens: "
            "some grievers wail, some go silent, some laugh - the "
            "recognition skill must stretch across styles, not just "
            "match your own. Done right, recognition is invisible: the "
            "griever simply finds the world slightly gentler that day, "
            "without knowing why."),
        "sig_lens": (
            "His Signature science trains the reader of signs as the "
            "apprentice learning to see the cloth: the brow the "
            "tent-poles, the posture the gathered weave, the voice the "
            "shuttles rhythm faltering. In the Signature view the "
            "skilled reader never announces the pattern - they simply "
            "adjust their own hands to lighten the weavers work, and "
            "the kindness lands without a name."),
        "how_it_works": (
            "Recognition works by pattern-matching against the "
            "involuntary programs: the grief brow, the folded posture, "
            "the flattened voice are substantially automatic, so they "
            "are more reliable than words, which are fully voluntary. "
            "The unguarded moment matters because suppression is "
            "resource-limited - the managed face slips when attention "
            "is elsewhere, revealing the underlying program. "
            "Discrepancy detection (mouth says fine, body says grief) "
            "works because different channels have different voluntary "
            "control: the verbal channel is easiest to manage, the "
            "facial and postural channels hardest, so truth concentrates "
            "in the harder channels. Calendar awareness adds Bayesian "
            "context: the same signs mean more in the weeks after a "
            "known loss. Uncertainty must be held because every sign "
            "has multiple causes - the recognition skill is "
            "probabilistic, not diagnostic, and acting on needs rather "
            "than labels is robust to that uncertainty: offering rest, "
            "space, or kindness helps whether the cause is grief, "
            "illness, or exhaustion. Cultural stretching matters "
            "because display rules vary enormously; a recognition "
            "system trained only on ones own culture will miss most of "
            "the worlds grief."),
        "key_points": [
            "Read the face (grief brow, glistening eyes), body (folded posture), voice (quieter, flatter), behavior (withdrawal, preserving), and calendar.",
            "Signs show most in unguarded moments; discrepancies between words and body are the most honest channel.",
            "Adjust yourself - soften pace, offer easier options, check in later - never announce a diagnosis.",
            "Signs suggest, never prove; respond to the apparent need, not a label.",
            "Stretch recognition across cultures and styles; done right, it is invisible kindness.",
        ],
        "requirements": [
            "No special equipment; this record trains observation",
            "Observe to serve, never to expose or label",
            "Hold uncertainty; every sign has multiple possible causes",
            "No diagnosing of any real person from these descriptions",
        ],
        "standards": [
            "Recognition cues drawn from facial-affect and nonverbal behavior research",
            "Descriptive and educational language only; no diagnostic claims",
        ],
        "citations": [CIT_EKMAN, CIT_APA, CIT_PARKES],
    },
    {
        "key": "supportive_responses",
        "name": "What to Say and Do When Someone Near You Is Grieving",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Most people want to help the grieving and fear doing it "
            "wrong; the fear itself becomes the failure when it produces "
            "silence and distance. The core principle is simple: show up, "
            "shut up a little, and stay. What to say: the honest small "
            "things. Im so sorry. I was sad to hear. Ive been thinking "
            "of you. Tell me about them, if youd like. I dont know what "
            "to say, but Im here. What not to say is covered in the next "
            "record; the short version is nothing that grades, hurries, "
            "explains, or silver-lines their grief. Listening is the "
            "main event: let them tell the story again, do not redirect "
            "to cheerful topics, tolerate the silences, do not cry-shame "
            "or fix. What to do matters more than what to say. The "
            "concrete beats the abstract every time: Ill bring dinner "
            "Thursday beats let me know if you need anything (which "
            "puts the organizing burden on the depleted griever). Show "
            "up with food, handle a chore, drive the airport run, sit "
            "with them while they make the hard phone calls. Remember "
            "the calendar: check in at three weeks, three months, the "
            "first holiday, the anniversary - when everyone elses "
            "support has faded and the grievers need is greatest. "
            "Include, dont pressure: keep inviting them, accept the "
            "declines gracefully, keep the door open. Speak the lost "
            "ones name: grievers fear the world forgetting, and hearing "
            "the name is a gift. Follow their lead on faith, meaning, "
            "and advice: do not theologize uninvited, do not prescribe "
            "stages, do not share your own loss as competition (my loss "
            "was worse is never helpful; brief shared experience offered "
            "as solidarity sometimes is). With children grieving: tell "
            "the truth simply, let them see your tears (it teaches "
            "feelings are allowed), keep routines, and answer the same "
            "question as many times as asked. With the long grieving - "
            "months and years on: do not expire your compassion; the "
            "griever at month eight often needs more than at week two, "
            "because the world has moved on and they have not. The "
            "measure of good support is not eloquence but persistence: "
            "the people grievers remember, years later, are rarely the "
            "ones who said the perfect thing. They are the ones who "
            "kept showing up."),
        "sig_lens": (
            "His Signature science describes the supporter as the second "
            "pair of hands on the loom: not weaving the grievers cloth "
            "for them - no one can - but holding the frame steady, "
            "fetching thread, keeping the lamp lit. In the Signature "
            "view the great support is quiet and durable: the dinner "
            "brought, the name spoken, the anniversary remembered, the "
            "showing up that outlasts the casseroles of the first week."),
        "how_it_works": (
            "Support works through several mechanisms at once. Presence "
            "down-regulates threat: the nervous system co-regulates with "
            "trusted others, measurably reducing stress physiology - "
            "this is why sitting-with helps even in silence. Concrete "
            "help reduces allostatic load directly: every chore handled "
            "is demand removed from the load-resources equation. "
            "Listening facilitates the narrative processing that drives "
            "reconsolidation; being heard is not passive but active "
            "medicine. Speaking the name maintains the continuing bond "
            "socially, countering the grievers fear of erasure. "
            "Calendar-remembering counters the support fade documented "
            "in bereavement research: natural support peaks early and "
            "declines just as the grievers need persists, so scheduled "
            "later check-ins fill the structural gap. What to avoid "
            "matters because misattuned responses (minimizing, "
            "silver-lining, theologizing) increase the grievers sense "
            "of isolation - the feeling of being alone with the grief "
            "even among people - which amplifies distress. Persistence "
            "outperforms eloquence because grief is long and the "
            "support that matters is the support still there in month "
            "eight."),
        "key_points": [
            "Core principle: show up, speak honestly and briefly, listen more than talk, stay.",
            "Concrete beats abstract: bring dinner Thursday beats let me know if you need anything.",
            "Remember the calendar: check in at three weeks, three months, holidays, anniversaries.",
            "Speak the lost ones name; keep inviting without pressuring; follow their lead on faith and advice.",
            "The measure of support is persistence, not eloquence; be there in month eight.",
        ],
        "requirements": [
            "No special equipment; this record trains supporters",
            "Show up repeatedly; one visit is a gesture, many visits are support",
            "Let the griever lead on meaning, faith, and how much to share",
            "No diagnosing of any real person from these descriptions",
        ],
        "standards": [
            "Support guidance drawn from bereavement support and social-support literature",
            "Descriptive and educational language only; no diagnostic claims",
        ],
        "citations": [CIT_WORDEN, CIT_STROEBE_HB, CIT_PARKES],
    },
    {
        "key": "what_not_to_do",
        "name": "What Not to Do: The Mistakes That Make Grief Worse",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Good intentions cause most of the damage around grief, so "
            "this record names the classic mistakes plainly - for "
            "learning, without shaming anyone who has made them. The "
            "silver lining reflex: at least theyre not suffering, at "
            "least you had so many years, look on the bright side. It "
            "aims to comfort and lands as erasure: the griever hears "
            "your pain is excessive, please be sad more efficiently. The "
            "theology ambush: theyre in a better place, God needed "
            "another angel, everything happens for a reason - offered "
            "uninvited to grievers who may not share the faith, or who "
            "do and are furious with it right now. Comfort about the "
            "afterlife is the grievers to choose, not yours to "
            "prescribe. The comparison: I know exactly how you feel "
            "(you do not), my loss was worse (competition helps no "
            "one), youll find someone else (the griever is mourning a "
            "person, not a vacancy). The timetable: arent you over this "
            "yet, its been months, you need to move on - the myth of "
            "the deadline, weaponized. The disappearance: the friends "
            "who vanish because they dont know what to say - silence "
            "intended as respect, received as abandonment. The "
            "pathologizing: you should see someone (said with alarm at "
            "normal grief), or the reverse - dismissing real stuckness "
            "as just grief when professional help is needed. The advice "
            "avalanche: you should travel, date, move, throw their "
            "things out, keep everything exactly - a barrage of shoulds "
            "at a person whose decision system is already down. The "
            "spotlight theft: making their loss about your feelings, "
            "your story, your tears needing their comfort. The "
            "efficiency audit: criticizing how they grieve - too much, "
            "too little, too long, too angry, too composed. Underneath "
            "every mistake is the same root: discomfort with the "
            "grievers pain, converted into an attempt to manage it. "
            "The correction is equally singular: tolerate the pain "
            "without fixing it. If you catch yourself silver-lining, "
            "theologizing, comparing, timetabling, advising, or "
            "auditing - stop, and substitute the only reliably safe "
            "moves: Im sorry, Im here, tell me about them, and then "
            "listen. Everyone has made one of these mistakes; the "
            "grievers in your life will forgive the past ones the "
            "moment you show up differently. What matters is not a "
            "perfect record but a learning curve."),
        "sig_lens": (
            "His Signature science frames each mistake as a hand on the "
            "weavers shuttle: the silver-liner pulling the thread, the "
            "timetabler hurrying the row, the theologian repatterning "
            "unasked. In the Signature view the supporters craft is "
            "restraint - hands off the shuttle, steady on the frame - "
            "trusting the weaver to know their own cloth."),
        "how_it_works": (
            "Each mistake backfires through a specific mechanism. "
            "Silver-lining and minimizing invalidate the emotional "
            "signal: the griever learns this person is unsafe for true "
            "feeling and stops sharing, increasing isolation. Uninvited "
            "theology creates meaning-conflict: imposed meanings clash "
            "with the grievers own meaning-reconstruction, adding a "
            "second struggle atop the grief. Comparisons and "
            "competition shift the frame from the grievers loss to the "
            "speakers experience, which reads as the support being "
            "about the supporter. Timetables import the deadline myth, "
            "producing shame about normal waves. Disappearance removes "
            "support precisely as need persists - the documented "
            "support fade, here accelerated by avoidance. Advice "
            "avalanches overload depleted executive function and imply "
            "the griever is grieving incorrectly. Pathologizing either "
            "alarms unnecessarily or misses real need. All share the "
            "invalidation core: responses that cannot tolerate the "
            "pain communicate, however unintentionally, that the pain "
            "itself is the problem - when the pain is the work. The "
            "safe substitutes work because they do the opposite: they "
            "witness without grading, accompany without directing, and "
            "leave the grievers meaning-making sovereign."),
        "key_points": [
            "Classic mistakes: silver-lining, uninvited theology, comparisons, timetables, disappearance, advice avalanches, spotlight theft, grief auditing.",
            "Every mistake shares one root: discomfort with the grievers pain, converted into managing it.",
            "Invalidation is the core harm: the griever learns this person is unsafe for true feeling.",
            "Substitute the safe moves: Im sorry, Im here, tell me about them - then listen.",
            "A perfect record is not required; what matters is a learning curve.",
        ],
        "requirements": [
            "No special equipment; this record trains supporters",
            "Review honestly which mistakes you have made; then show up differently",
            "Tolerate pain without fixing it",
            "No diagnosing of any real person from these descriptions",
        ],
        "standards": [
            "Mistake mechanisms drawn from social-support and invalidation literature",
            "Descriptive and educational language only; no diagnostic claims",
        ],
        "citations": [CIT_WORDEN, CIT_STROEBE_HB, CIT_APA],
    },
    {
        "key": "related_emotions_map",
        "name": "The Related Emotions Map: Griefs Nearest Neighbors and Opposites",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Grief sits in a crowded neighborhood, and learners need "
            "the map - because the neighbors are easily confused, and "
            "confusion leads to wrong responses. Nearest neighbors "
            "first. Sadness: griefs root note and closest kin. The "
            "difference is scope and cause - sadness is the feeling, "
            "grief is the whole response to loss including the body, "
            "behavior, and time-course. All grief contains sadness; not "
            "all sadness is grief. Mourning: griefs public twin - the "
            "outward rituals and expressions. Grief is what you feel; "
            "mourning is what you (and your culture) do. Melancholy: a "
            "longer, quieter, more philosophical sadness, often without "
            "a single sharp loss - grief diffused into temperament. "
            "Nostalgia: griefs sweetened cousin - longing for a past "
            "that is gone, but filtered through warmth; when nostalgia "
            "turns sharp and aching it is crossing into grief. Regret: "
            "looks backward at choices (if only I had); grief looks at "
            "absence (they are gone). They often travel together - "
            "regret is griefs guilt-flavored neighbor - but the core "
            "ache differs. Longing/yearning: griefs engine made visible "
            "- the reach for what is gone. Intense longing without "
            "acceptance of absence is griefs acute phase; longing that "
            "has made peace with absence becomes remembrance. Despair: "
            "griefs dangerous neighbor - the loss of the sense that the "
            "future can hold anything good. Grief says they are gone; "
            "despair says nothing will ever matter. Despair layered on "
            "grief is the sign to bring professional help promptly. "
            "Then the opposites, which clarify by contrast. Acceptance "
            "(in the grief sense): not approval of the loss but the "
            "settled recognition that it is real - griefs destination, "
            "not its enemy. Joy: not griefs enemy either - grievers "
            "often feel guilty about laughter, but joy and grief "
            "coexist throughout healthy grieving (the dual process "
            "models restoration side). Relief: the most guilt-inducing "
            "neighbor - relief after a long suffering or a difficult "
            "relationship is normal and does not cancel love. "
            "Gratitude: griefs eventual companion - thankfulness for "
            "what was, which can sit beside missing it. The map has one "
            "practical use above all: correct naming. The griever who "
            "can say this is regret, not grief or this has tipped from "
            "grief into despair can respond to each accurately - "
            "amends or self-forgiveness for regret, urgent support for "
            "despair, patience for grief itself. And the supporter who "
            "can tell them apart stops offering grief-comfort for "
            "despair (which needs more) and stops pathologizing "
            "nostalgia (which needs nothing but a smile)."),
        "sig_lens": (
            "His Signature science draws the neighborhood as adjacent "
            "panels in the great tapestry: sadness the panel grief is "
            "woven from, mourning its public face, nostalgia the "
            "softened reweave of old colors, regret the snagged thread "
            "of what was done, despair the panel gone dark at the "
            "edges. In the Signature view the master weaver knows "
            "every neighboring panel by touch - and knows exactly "
            "which one the hands are working, so the right care "
            "reaches the right place."),
        "how_it_works": (
            "Neighbor distinctions follow from appraisal and temporal "
            "structure. Sadness versus grief: same core affect, "
            "different scope - grief adds the attachment-system "
            "machinery (searching, protest, reorganization) and the "
            "extended time-course. Mourning versus grief: internal "
            "experience versus culturally scripted expression - "
            "different systems, which is why they can diverge "
            "(deep grief with restrained mourning, or elaborate "
            "mourning with complicated inner grief). Nostalgia versus "
            "grief: both involve loss of the past, but nostalgia "
            "appraises the past as warmly distant while grief "
            "appraises the absence as presently wounding - the "
            "affective tone differs. Regret versus grief: "
            "counterfactual self-blame versus absence-pain; different "
            "appraisals, different remedies. Despair versus grief: "
            "grief is loss-focused with the future still imaginable; "
            "despair is future-collapse - the prospection system "
            "returning nothing, which is why it predicts stuckness "
            "and needs professional support. Opposites clarify "
            "because emotions are partly defined by contrast: "
            "acceptance is grief with the reality-appraisal settled; "
            "joy coexists because the affect systems are parallel, "
            "not a single dial - the brain can run grief and "
            "gladness on different channels at once."),
        "key_points": [
            "Nearest neighbors: sadness (root note), mourning (public twin), melancholy (diffuse), nostalgia (sweetened), regret (choices), longing (engine), despair (dangerous).",
            "Grief says they are gone; despair says nothing will ever matter - despair layered on grief needs professional help promptly.",
            "Opposites clarify: acceptance is griefs destination, joy coexists with grief, relief does not cancel love.",
            "Correct naming enables correct response: amends for regret, urgent support for despair, patience for grief.",
            "Supporters who can tell neighbors apart stop under-responding to despair and over-pathologizing nostalgia.",
        ],
        "requirements": [
            "No special equipment; this record is for reading and reflection",
            "Practice naming: which neighbor is actually present right now",
            "Treat despair-on-grief as the prompt for professional help, not for waiting",
            "No diagnosing of any real person from these descriptions",
        ],
        "standards": [
            "Neighbor distinctions drawn from appraisal theory and bereavement literature",
            "Descriptive and educational language only; no diagnostic claims",
        ],
        "citations": [CIT_APA, CIT_PLUTCHIK, CIT_SHEAR],
    },
    {
        "key": "emotion_mixes",
        "name": "Emotion Mixes: Grief Blended With Sadness, Anger, Guilt, and Love",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Following the classic dyad tradition - pairs of emotions "
            "blended into named compounds - this record maps griefs "
            "four most important blends as simulated portraits for "
            "learning. Blend one: grief plus sadness, the deepened "
            "sorrow. This is grief at its most distilled - the other "
            "partners quiet, the root note sounding alone and low. It "
            "feels like sinking: heavy limbs, slow tears, the world "
            "muted, a tenderness toward everything fragile. It looks "
            "like stillness - the griever motionless by the window, "
            "grief as weather settled in. This blend dominates the "
            "later, integrated phases, and it is the blend most people "
            "picture when they picture grief. Blend two: grief plus "
            "anger, the protest sorrow. Heavy heat, as described in the "
            "mixes record: weeping and pacing, aching and burning, the "
            "furious why alongside the hollow missing. It looks like "
            "restlessness - the griever in motion, cleaning frenzies, "
            "sharp words regretted instantly. This blend dominates early "
            "grief and unfair losses. Blend three: grief plus guilt, "
            "the accusing sorrow. The ache turns inward and becomes a "
            "courtroom: the what-ifs paraded, the last week "
            "re-litigated, the verdict always insufficient. It feels "
            "like carrying the loss plus carrying the blame for the "
            "loss - double weight. It looks like rumination made "
            "visible: the griever going over and over the same ground, "
            "apologizing to people who need no apology. The healthy "
            "solvent for this blend is truth-telling about control: "
            "sorting what was actually choosable from what was never in "
            "anyones hands. Blend four: grief plus love, the enduring "
            "sorrow - and the most hopeful blend in the set. This is "
            "grief that has found its continuing bond: the missing "
            "braided with gratitude, the tears arriving alongside the "
            "smile at the memory, the lost one carried forward as "
            "values, stories, and the recipe still cooked. It feels "
            "bittersweet in the truest sense - both bitter and sweet, "
            "fully. It looks like the griever at the anniversary "
            "telling the funny story through tears and meaning every "
            "drop of both. Researchers of post-loss growth describe "
            "exactly this blend as the characteristic texture of "
            "integrated grief: not the absence of pain but the "
            "presence of love alongside it. The four blends are not "
            "stages and not a sequence; they are the palette. A single "
            "griever moves among them across a week - protest sorrow "
            "in the morning, accusing sorrow at noon, deepened sorrow "
            "in the evening, enduring sorrow at the anniversary. "
            "Learning the palette means never mistaking one blend for "
            "the whole of grief, and never telling a griever wearing "
            "anger that they are grieving wrong when they are simply "
            "wearing a different blend today."),
        "sig_lens": (
            "His Signature science names the four blends the four "
            "weavings: deepened sorrow the cloth in indigo, protest "
            "sorrow the red thread shot through, accusing sorrow the "
            "knot picked at too long, enduring sorrow the gold thread "
            "of love woven back through the mended tear. In the "
            "Signature view the master weaver learns all four - and "
            "the enduring sorrow is the masterwork: the tear not "
            "hidden but honored, the gold visible in the mending."),
        "how_it_works": (
            "Blends form through parallel appraisal, as mapped in the "
            "partner-emotion record: each blend is griefs core program "
            "(attachment disruption plus absence-pain) running "
            "simultaneously with a partner program recruited by a "
            "co-occurring appraisal. Grief plus sadness is the minimal "
            "blend - the partner adding only depth to the root note, "
            "which is why it characterizes integrated phases when the "
            "secondary appraisals (unfairness, self-blame) have "
            "settled. Grief plus anger adds the approach-motivated "
            "protest system: high arousal, motor activation, other-"
            "blame - the blend of unfair or premature loss. Grief plus "
            "guilt adds counterfactual simulation and self-blame: the "
            "planning machinery misfiring on the unchangeable past, "
            "doubling the felt weight. Grief plus love is the "
            "continuing-bond blend: attachment maintained in "
            "transformed form (memory, values, ritual) alongside "
            "accepted absence - the configuration research associates "
            "with healthy adaptation and post-loss growth. Movement "
            "among blends across a week reflects the appraisal system "
            "updating moment to moment: a reminder of unfairness "
            "recruits anger, a what-if recruits guilt, a warm memory "
            "recruits love. The palette framing matters because "
            "single-blend theories of grief (grief is anger, grief is "
            "acceptance) mistake one color for the painting."),
        "key_points": [
            "Grief plus sadness: the deepened sorrow - distilled, still, heavy; the blend of integrated phases.",
            "Grief plus anger: the protest sorrow - heavy heat, restlessness; the blend of early and unfair grief.",
            "Grief plus guilt: the accusing sorrow - double weight; eased by truth-telling about what was actually controllable.",
            "Grief plus love: the enduring sorrow - bittersweet, continuing bond; the texture of integrated grief.",
            "The blends are a palette, not stages; grievers move among them across a single week.",
        ],
        "requirements": [
            "No special equipment; this record is for reading and reflection",
            "Learn the palette; never mistake one blend for the whole of grief",
            "Never tell an angry griever they are grieving wrong; they are wearing a different blend",
            "No diagnosing of any real person from these descriptions",
        ],
        "standards": [
            "Blend architecture follows Plutchiks dyad tradition and appraisal theory",
            "Descriptive and educational language only; no diagnostic claims",
        ],
        "citations": [CIT_PLUTCHIK, CIT_NEIMEYER, CIT_BONANNO],
    },
    {
        "key": "full_simulation",
        "name": "Full Behavioral Simulation: Grief From Trigger to Resolution",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The archives showcase simulation: grief walked from "
            "trigger through peak to resolution across one full arc, "
            "in scenes, for learning. It describes no real person. "
            "Scene one, the trigger. Saturday morning, eleven months "
            "after the loss. Mara is repotting a plant when the radio "
            "plays their song - not a song about loss, their song, the "
            "kitchen-dancing one. Her hands stop. The grief brow "
            "flickers, the throat works. Inner monologue: oh. Oh no, "
            "not now - then, with practiced gentleness: its just the "
            "song. Let it come. Body: the familiar chest-tightening, "
            "eyes brightening. She does not turn it off. Scene two, "
            "the cascade. The song opens the kitchen memory, the memory "
            "opens the last birthday, the birthday opens the hospital "
            "weeks, the hospital opens the guilt about the sharp words. "
            "Four links in ninety seconds - the chain reaction running. "
            "She recognizes it: cascade. Name it. Hands in soil, feet "
            "on floor, breathe. She interrupts at the guilt link with "
            "the practiced truth: I was exhausted and I loved her; both "
            "were true. The chain stops. The wave itself - the pure "
            "missing - she lets through: two minutes of tears into her "
            "sleeve, the plant waiting. Scene three, the expression. "
            "Her partner finds her damp-eyed and does everything right: "
            "sits nearby, doesnt fix, says tell me if you want. She "
            "talks - the song, the kitchen, the missing - in the small "
            "concrete details, voice thickening once. He listens "
            "without redirecting. The telling files the memory a "
            "little deeper; the being-heard steadies the physiology. "
            "Scene four, the channeling. After lunch she does the "
            "anniversary-adjacent ritual they built: cooks her mothers "
            "soup recipe - the one her mother taught her, the kitchen "
            "filling with the smell that used to mean home. Cooking is "
            "the making-channel: protest energy become tribute. She "
            "cries once more, briefly, stirring - and smiles at the "
            "same time, the enduring-sorrow blend, grief plus love. "
            "Scene five, the reweaving. Evening. She writes ten minutes "
            "in the journal: the song, the cascade caught, the soup, "
            "the smile-through-tears. She notes the date - eleven "
            "months - and the observation that this wave, though tall, "
            "passed faster than the ones at three months. The data "
            "accumulates: waves still come, recovery quickens, the "
            "cloth holds. She sleeps. The simulation demonstrates the "
            "whole curriculum in one arc: trigger recognized, cascade "
            "interrupted, wave allowed, story told and heard, grief "
            "channeled into ritual making, meaning noted, rest taken. "
            "No scene required heroism - only the practiced small "
            "skills, which is the honest truth about grieving well: it "
            "is not a single brave act but ten thousand small "
            "recognitions, interruptions, tellings, and makings, "
            "compounded. The archive offers this simulation so learners "
            "can watch the full machinery move - and so grievers can "
            "see, from the outside, what their own brave ordinary work "
            "looks like."),
        "sig_lens": (
            "His Signature science presents this arc as the master "
            "demonstration of the craft: the trigger the loose thread "
            "caught, the cascade the run stopped by the practiced hand, "
            "the telling the row counted aloud, the soup the gold "
            "thread of love rewoven, the journal the pattern recorded. "
            "In the Signature view Mara is every weaver at eleven "
            "months - the cloth not finished, the tear not hidden, "
            "the mending unmistakably holding."),
        "how_it_works": (
            "The simulation is engineered to exercise every mechanism "
            "in the curriculum in sequence. Scene one demonstrates "
            "cue-triggered reactivation (music plus autobiographical "
            "memory) with the practiced response of allowing rather "
            "than suppressing - affect tolerance in action. Scene two "
            "demonstrates cascade anatomy (sensory spark through "
            "interpretive links) and interruption via naming, grounding, "
            "and countering the global verdict - the full interruption "
            "toolkit at one link. Scene three demonstrates narrative "
            "processing plus co-regulation: telling drives "
            "reconsolidation while the partners regulated presence "
            "down-regulates the tellers arousal. Scene four "
            "demonstrates channeling (making as tribute) and the "
            "continuing bond in its healthiest form - the recipe as "
            "durable connection - plus the grief-plus-love blend as "
            "the texture of integrated grief. Scene five demonstrates "
            "the journaling mechanism and, crucially, the learners "
            "evidence: comparing wave duration across months makes the "
            "gradual adaptation visible, countering the grievers "
            "common illusion that nothing is changing. The arc as a "
            "whole demonstrates the dual process rhythm (loss-oriented "
            "scenes alternating with restoration-oriented ones) and "
            "the central thesis of the database: grieving well is a "
            "repertoire of small skills, compounded over time."),
        "key_points": [
            "Scene one: trigger recognized and allowed - the song, the practiced gentleness, hands staying with the plant.",
            "Scene two: cascade named and interrupted at the guilt link with the practiced truth; the pure wave let through.",
            "Scene three: story told in small concrete details and heard without fixing - narrative processing plus co-regulation.",
            "Scene four: grief channeled into ritual making - the soup, the enduring-sorrow blend of grief plus love.",
            "Scene five: the arc recorded; waves still come but pass faster - the reweaving visibly holding.",
        ],
        "requirements": [
            "No special equipment; this record is for reading and reflection",
            "Read the full arc in order; the curriculum compounds scene by scene",
            "Share with grievers only if welcome; simulations comfort some and overwhelm others",
            "No diagnosing of any real person from these descriptions",
        ],
        "standards": [
            "Simulation integrates the databases full mechanism set: triggers, cascades, expression, support, ritual, reconsolidation",
            "Descriptive and educational language only; no diagnostic claims",
        ],
        "citations": [CIT_WORDEN, CIT_NEIMEYER, CIT_DUAL, CIT_BONANNO],
    },
]
