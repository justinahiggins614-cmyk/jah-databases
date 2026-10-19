# -*- coding: utf-8 -*-
"""Topic module: db-fact-or-fiction-challenge. Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T

CFG = mkcfg({
    "slug": "db-fact-or-fiction-challenge", "name": "The Fact or Fiction Challenge", "pfx": "JAH-FACORFIC-",
    "tagline_pub": "Fact or fiction verdicts with the evidence shown - surprising truths and plausible lies: every record carrying the claim, the verdict, the evidence, and why it fools people, taught progressively along the ladder.",
    "tagline_sig": "The Signature truth-sight: every claim a Signature test, every verdict earned by evidence. The full ladder from easy calls through plausible lies to Signature-grade deceivers. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "Fact or Fiction Challenge",
    "role_pub": "verdict referee - judging claims and showing the evidence for every call",
    "role_sig": "Signature verdict referee - teaching Signature truth-sight",
    "record_kind": "fact-or-fiction record", "record_kind_plural": "fact-or-fiction challenges",
    "demo_kind": "verdict-proof", "demo_title": "Fact or Fiction Study",
    "search_ph": "Search fact, fiction, verdicts, myths, true or false...",
    "chat_ph": "Ask fact or fiction...",
    "gen_blurb": "Generate clearly-labeled verdict studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded fact-or-fiction challenges, every verdict evidence-backed, marching toward one million records. Presented in teaching-ladder order: easy calls, plausible lies, deceivers.",
    "reqs": "Curiosity and a habit of checking.",
    "stds": "Every verdict carries its evidence; the demo verifies the verdict matches the evidence rule.",
    "cites": ["JAH Databases verdict verification standard v1.0"],
})


def _ff(tier, claim, verdict, evidence, why_tricky, check_expr):
    return T(
        tier, "Fact or fiction: %s" % claim[:56].rstrip(" .?") + "...",
        desc_pub='FACT OR FICTION?\n\nClaim: "%s"\n\nVERDICT: %s\n\nEvidence: %s\n\nWhy it fools people: %s'
        % (claim, verdict.upper(), evidence, why_tricky),
        desc_sig='Signature truth-sight: "%s" - judged %s by the evidence. The Signature edition treats every correct verdict as a small victory for reality.' % (claim[:60], verdict.upper()),
        how_pub='Judge it yourself: ask what would prove it wrong (falsifiability), then look for that evidence. The verdict follows the evidence, never the feeling.',
        how_sig='The Signature way: state your gut verdict first, then let the evidence overrule it without mercy.',
        keys=['Claim: "%s".' % claim,
              'Verdict: %s.' % verdict.upper(),
              'Evidence: %s' % evidence,
              'Why tricky: %s' % why_tricky],
        demo=("check", {"code": ["VERDICT = %r" % verdict, "EVIDENCE = %r" % evidence],
                        "checks": [("verdict_is_binary", "VERDICT in ('FACT', 'FICTION')"),
                                   ("evidence_present", "len(EVIDENCE) > 20"),
                                   ("evidence_supports_verdict", check_expr)]}),
    )


B, C, A = "Foundations", "Compounded", "Advanced"
TOPICS = [
    _ff(B, "Water boils at 100 degrees Celsius.", "FACT", "At sea-level standard pressure, pure water boils at 100 C - the definition of the Celsius scale's upper fixed point.", "It feels too neat to be true - but some facts are just definitions.", "'100' in EVIDENCE"),
    _ff(B, "Bats are blind.", "FICTION", "Bats see quite well; most also use echolocation. 'Blind as a bat' is a myth.", "The saying is so common it feels factual.", "'echolocation' in EVIDENCE"),
    _ff(B, "The Great Wall of China is visible from the Moon.", "FICTION", "No human structure is visible from the Moon with the naked eye; the Wall is barely visible from low orbit.", "It sounds like the kind of thing that would be true.", "'Moon' in EVIDENCE"),
    _ff(B, "Goldfish have a 3-second memory.", "FICTION", "Goldfish remember for months - they learn mazes and recognize keepers.", "Everyone 'knows' this, and everyone is wrong.", "'months' in EVIDENCE"),
    _ff(B, "Lightning never strikes the same place twice.", "FICTION", "Lightning strikes the same tall structures repeatedly - the Empire State Building is hit dozens of times a year.", "The proverb confuses wisdom with physics.", "'dozens' in EVIDENCE"),
    _ff(B, "Humans use only 10% of their brains.", "FICTION", "Brain imaging shows virtually all of the brain active across a day; the myth came from a misquote.", "It flatters us: imagine the untapped 90%.", "'misquote' in EVIDENCE"),
    _ff(B, "Ostriches bury their heads in the sand.", "FICTION", "Ostriches do not bury their heads; they lay low or run. The myth came from ancient writers.", "The image is too funny to fact-check.", "'ancient' in EVIDENCE"),
    _ff(B, "A penny dropped from a skyscraper can kill.", "FICTION", "A penny reaches terminal velocity (~40 km/h) and cannot kill; it would sting at most.", "Movies love this one.", "'terminal velocity' in EVIDENCE"),
    _ff(B, "Cracking knuckles causes arthritis.", "FICTION", "Studies find no link between knuckle-cracking and arthritis; the sound is gas bubbles popping.", "Parents everywhere disagree, but the studies are clear.", "'no link' in EVIDENCE"),
    _ff(B, "The five-second rule keeps food safe.", "FICTION", "Bacteria transfer instantly on contact; time on the floor barely matters versus the surface.", "Wishful thinking, deliciously.", "'instantly' in EVIDENCE"),
    _ff(B, "Mount Everest is the tallest mountain on Earth.", "FACT", "Everest (8,849 m above sea level) is the highest point on Earth - Mauna Kea is taller base-to-peak but mostly underwater.", "The Mauna Kea technicality fools trivia nights.", "'8,849' in EVIDENCE"),
    _ff(C, "Honey never spoils.", "FACT", "Archaeologists have tasted 3,000-year-old honey from Egyptian tombs - still good. Low water and acidity preserve it.", "Food that outlives civilizations sounds fictional.", "'3,000-year-old' in EVIDENCE"),
    _ff(C, "There are more possible chess games than atoms in the universe.", "FACT", "The Shannon number (~10^120) dwarfs the ~10^80 atoms in the observable universe.", "The numbers are too big to feel real.", "'10^120' in EVIDENCE"),
    _ff(C, "Sharks get cancer.", "FACT", "Sharks do get cancer - the 'shark cartilage cures cancer' myth is the fiction; the animals themselves are not immune.", "The myth inverted the truth.", "'myth' in EVIDENCE"),
    _ff(C, "The Eiffel Tower grows taller in summer.", "FACT", "Thermal expansion adds about 15 cm in summer heat - the tower literally grows.", "Buildings are not supposed to do that.", "'15 cm' in EVIDENCE"),
    _ff(C, "Bananas are radioactive.", "FACT", "Bananas contain potassium-40; the 'banana equivalent dose' is a real radiation unit.", "Radioactive fruit sounds like fiction.", "'potassium-40' in EVIDENCE"),
    _ff(C, "Glass is a slow-moving liquid.", "FICTION", "Glass is an amorphous solid; old windows are thicker at the bottom from manufacturing, not flow.", "The old-window story fooled generations.", "'amorphous solid' in EVIDENCE"),
    _ff(C, "You can see the Great Wall from space with the naked eye.", "FICTION", "Astronauts confirm: the Wall is not visible to the naked eye from orbit - cities' lights are, the Wall is not.", "Even astronauts had to check.", "'Astronauts' in EVIDENCE"),
    _ff(C, "Walt Disney is frozen.", "FICTION", "Disney was cremated; the cryonics myth started as a joke that escaped.", "A joke that became 'history'.", "'cremated' in EVIDENCE"),
    _ff(C, "Napoleon was short.", "FICTION", "Napoleon was ~5'7', average for his era; the myth came from British propaganda and unit confusion.", "Propaganda outlives its target by centuries.", "'propaganda' in EVIDENCE"),
    _ff(C, "Vikings wore horned helmets.", "FICTION", "No horned Viking helmet has ever been found; the image came from 19th-century opera costumes.", "Opera invented history.", "'opera' in EVIDENCE"),
    _ff(C, "A duck's quack does not echo.", "FICTION", "A duck's quack echoes like any sound; the myth persisted because the echo is hard to distinguish.", "Tested and busted.", "'echoes' in EVIDENCE"),
    _ff(C, "Humans and dinosaurs coexisted.", "FICTION", "Non-avian dinosaurs died out 66 million years before humans appeared.", "Movies keep reuniting them.", "'66 million' in EVIDENCE"),
    _ff(A, "Cleopatra lived closer in time to the iPhone than to the pyramids' construction.", "FACT", "Cleopatra (69-30 BCE) is ~2,000 years from the iPhone and ~2,500 years from the Great Pyramid's completion.", "Time is deeper than it feels.", "'2,500 years' in EVIDENCE"),
    _ff(A, "Oxford University is older than the Aztec Empire.", "FACT", "Oxford taught from 1096; the Aztec Empire began ~1428 - Oxford is 300+ years older.", "The mental timeline shuffles everything.", "'1096' in EVIDENCE"),
    _ff(A, "There are more trees on Earth than stars in the Milky Way.", "FACT", "~3 trillion trees vs ~100-400 billion stars - trees win by an order of magnitude.", "The sky feels bigger than the forest.", "'3 trillion' in EVIDENCE"),
    _ff(A, "Woolly mammoths were still alive while the pyramids were built.", "FACT", "The last mammoths died ~1700 BCE; the Great Pyramid was completed ~2560 BCE - overlap of nearly a millennium.", "Two 'ancient' things being contemporary breaks the timeline.", "'millennium' in EVIDENCE"),
    _ff(A, "The first oranges were not orange.", "FACT", "Southeast Asian oranges were green; 'orange' the color is named for the fruit, not vice versa.", "The color is named after the fruit - reality runs backward here.", "'named for the fruit' in EVIDENCE"),
    _ff(A, "Nintendo was founded when Jack the Ripper was active.", "FACT", "Nintendo (1889) and the Ripper murders (1888) overlap - the game company is Victorian.", "Two facts from different universes colliding.", "'1889' in EVIDENCE"),
    _ff(A, "Shakespeare and Pocahontas died in the same year.", "FICTION", "Shakespeare died 1616; Pocahontas died 1617 - one year apart, not the same. (Close enough to fool.)", "Off by one: the cruelest trivia margin.", "'1617' in EVIDENCE"),
    _ff(A, "The sun is a green star.", "FACT", "The Sun's peak emission is in the green part of the spectrum; it looks white/yellow because it emits all colors.", "Green sun sounds absurd - physics disagrees.", "'green' in EVIDENCE"),
    _ff(A, "Hot water can freeze faster than cold water.", "FACT", "The Mpemba effect: under some conditions hot water freezes first - still not fully explained.", "Thermodynamics with a sense of humor.", "'Mpemba' in EVIDENCE"),
    _ff(A, "There is a giant water reservoir in space holding 140 trillion oceans.", "FACT", "A quasar 12 billion light-years away holds ~140 trillion times Earth's ocean water as vapor.", "The universe's plumbing is extravagant.", "'140 trillion' in EVIDENCE"),
    _ff(A, "The dot over the letter i has a name.", "FACT", "It is called a tittle - the smallest named part of writing.", "Tiny things have names too.", "'tittle' in EVIDENCE"),
]
