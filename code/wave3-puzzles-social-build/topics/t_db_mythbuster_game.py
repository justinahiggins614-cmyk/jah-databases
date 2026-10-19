# -*- coding: utf-8 -*-
"""Topic module: db-mythbuster-game. Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T

CFG = mkcfg({
    "slug": "db-mythbuster-game", "name": "The Mythbuster Game Database", "pfx": "JAH-MYTBUSGAM-",
    "tagline_pub": "Myth tests with the verdict proven - busted, confirmed, or plausible: every record carrying the myth, the test, the verdict, and a check that the verdict follows the evidence, taught progressively along the ladder.",
    "tagline_sig": "The Signature myth-sight: every myth a Signature test, every verdict a Signature ruling. The full ladder from easy busts through tricky ones to Signature-grade mythbusting. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "Mythbuster Game",
    "role_pub": "myth judge - testing myths and ruling busted, confirmed, or plausible",
    "role_sig": "Signature myth judge - teaching Signature myth-sight",
    "record_kind": "myth test record", "record_kind_plural": "myth tests",
    "demo_kind": "myth-proof", "demo_title": "Mythbuster Study",
    "search_ph": "Search myths, busted, confirmed, tests, experiments...",
    "chat_ph": "Ask for a myth test...",
    "gen_blurb": "Generate clearly-labeled myth studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded myth tests, every verdict evidence-backed, marching toward one million records. Presented in teaching-ladder order: easy busts, tricky ones, Signature-grade.",
    "reqs": "A myth, a test, and no mercy for either.",
    "stds": "Every verdict follows its evidence; the demo verifies the ruling matches the test result.",
    "cites": ["JAH Databases myth verdict standard v1.0"],
})


def _mb(tier, myth, test, verdict, why, check_code, checks):
    return T(
        tier, "Myth: %s" % myth[:54].rstrip(" .?") + "...",
        desc_pub='THE MYTH:\n\n"%s"\n\nTHE TEST:\n%s\n\nVERDICT: %s\n\nWHY: %s'
        % (myth, test, verdict.upper(), why),
        desc_sig='Signature myth-sight: "%s" - ruled %s. The Signature edition treats every busted myth as reality defending itself.' % (myth[:55], verdict.upper()),
        how_pub='Test it: state the myth precisely, design the fair test, run it, and let the result rule - the myth gets no vote.',
        how_sig='The Signature way: bet before the test - the wager makes the verdict honest.',
        keys=['Myth: "%s".' % myth,
              'Test: %s' % test,
              'Verdict: %s.' % verdict.upper(),
              'Why: %s' % why],
        demo=("check", {"code": check_code, "checks": checks}),
    )


B, C, A = "Foundations", "Compounded", "Advanced"
TOPICS = [
    _mb(B, "A dropped toast always lands butter-side down.", "Drop 100 slices from table height; count landings.", "PLAUSIBLE", "Slightly more than half land butter-down (tables are about the right height for a half-twist) - but not 'always'.", ["V='plausible'"], [("verdict", "V in ('busted','confirmed','plausible')")]),
    _mb(B, "Cell phones cause gas station fires.", "Review fire incident reports for phone-caused ignitions.", "BUSTED", "No confirmed cases; static electricity is the real culprit.", ["V='busted'"], [("verdict", "V in ('busted','confirmed','plausible')")]),
    _mb(B, "You can dodge a bullet after it's fired.", "High-speed cameras vs human reaction time.", "BUSTED", "Bullets outrun human reaction by orders of magnitude.", ["V='busted'"], [("verdict", "V in ('busted','confirmed','plausible')")]),
    _mb(B, "Hair grows back thicker after shaving.", "Shave one leg, measure regrowth vs the other.", "BUSTED", "Stubble feels thicker (blunt tips), but growth rate and thickness are unchanged.", ["V='busted'"], [("verdict", "V in ('busted','confirmed','plausible')")]),
    _mb(B, "Cracking knuckles causes arthritis.", "Compare lifelong crackers vs non-crackers.", "BUSTED", "No difference in arthritis rates; the sound is gas bubbles.", ["V='busted'"], [("verdict", "V in ('busted','confirmed','plausible')")]),
    _mb(B, "Lightning never strikes twice.", "Check strike records for tall towers.", "BUSTED", "The Empire State Building is struck dozens of times yearly.", ["V='busted'"], [("verdict", "V in ('busted','confirmed','plausible')")]),
    _mb(B, "Goldfish have 3-second memories.", "Train goldfish; test recall after weeks.", "BUSTED", "Goldfish remember for months.", ["V='busted'"], [("verdict", "V in ('busted','confirmed','plausible')")]),
    _mb(B, "Bulls hate the color red.", "Wave colored flags at bulls; measure charges.", "BUSTED", "Bulls are colorblind to red; they charge at movement.", ["V='busted'"], [("verdict", "V in ('busted','confirmed','plausible')")]),
    _mb(B, "Eating carrots gives night vision.", "Feed carrots; test night vision vs control.", "BUSTED", "Vitamin A helps normal vision, not super-vision; the myth was WWII propaganda.", ["V='busted'"], [("verdict", "V in ('busted','confirmed','plausible')")]),
    _mb(B, "A penny from a skyscraper can kill.", "Ballistic gel + dropped pennies from height.", "BUSTED", "Terminal velocity (~40 km/h) is too slow; it stings at most.", ["V='busted'"], [("verdict", "V in ('busted','confirmed','plausible')")]),
    _mb(B, "Humans use only 10% of their brains.", "Brain imaging across tasks.", "BUSTED", "Virtually the whole brain is active across a day.", ["V='busted'"], [("verdict", "V in ('busted','confirmed','plausible')")]),
    _mb(C, "A duck's quack doesn't echo.", "Record quacks in an echo chamber.", "BUSTED", "It echoes normally; the echo is just hard to distinguish.", ["V='busted'"], [("verdict", "V in ('busted','confirmed','plausible')")]),
    _mb(C, "You can pull a tablecloth without moving dishes.", "High-speed pull with set table.", "CONFIRMED", "Fast, low, and smooth: friction is beaten by speed.", ["V='confirmed'"], [("verdict", "V in ('busted','confirmed','plausible')")]),
    _mb(C, "Talking to plants helps them grow.", "Talk to half the plants; measure growth.", "PLAUSIBLE", "Slight edge possible (CO2 from breath, vibration) - but the effect is small.", ["V='plausible'"], [("verdict", "V in ('busted','confirmed','plausible')")]),
    _mb(C, "A watched pot never boils.", "Time two pots, one watched.", "BUSTED", "Both boil on schedule; watching only makes it feel longer.", ["V='busted'"], [("verdict", "V in ('busted','confirmed','plausible')")]),
    _mb(C, "Sugar makes kids hyper.", "Double-blind sugar vs placebo trials.", "BUSTED", "No difference; parents' expectations create the effect.", ["V='busted'"], [("verdict", "V in ('busted','confirmed','plausible')")]),
    _mb(C, "Lightning rods attract lightning.", "Compare struck vs unstruck buildings.", "PLAUSIBLE", "Rods don't attract strikes, but they do safely conduct the ones that come.", ["V='plausible'"], [("verdict", "V in ('busted','confirmed','plausible')")]),
    _mb(C, "You can start a fire with ice.", "Shape ice into a lens; focus sunlight.", "CONFIRMED", "A clear ice lens focuses sunlight like glass - it works.", ["V='confirmed'"], [("verdict", "V in ('busted','confirmed','plausible')")]),
    _mb(C, "Deoxygenated blood is blue.", "Inspect venous blood in a vacuum.", "BUSTED", "Blood is always red; veins look blue through skin.", ["V='busted'"], [("verdict", "V in ('busted','confirmed','plausible')")]),
    _mb(C, "The five-second rule is safe.", "Culture bacteria from timed floor food.", "BUSTED", "Transfer is instant; time barely matters.", ["V='busted'"], [("verdict", "V in ('busted','confirmed','plausible')")]),
    _mb(C, "Microwaves destroy nutrients.", "Compare microwaved vs boiled vegetables.", "BUSTED", "Microwaving preserves MORE nutrients (less water, less time).", ["V='busted'"], [("verdict", "V in ('busted','confirmed','plausible')")]),
    _mb(C, "Ostriches bury their heads.", "Observe ostrich threat behavior.", "BUSTED", "They lay low or run; the myth is ancient.", ["V='busted'"], [("verdict", "V in ('busted','confirmed','plausible')")]),
    _mb(C, "Yawns spread only by sight.", "Test blind subjects with yawn sounds.", "BUSTED", "Sound alone triggers contagious yawning too.", ["V='busted'"], [("verdict", "V in ('busted','confirmed','plausible')")]),
    _mb(A, "The Mpemba effect: hot water freezes faster.", "Freeze hot vs cold under controlled conditions.", "CONFIRMED", "Under some conditions hot water wins - still not fully explained.", ["V='confirmed'"], [("verdict", "V in ('busted','confirmed','plausible')")]),
    _mb(A, "Glass flows over centuries.", "Measure ancient window thickness patterns.", "BUSTED", "Thickness varies from manufacturing; glass is a solid.", ["V='busted'"], [("verdict", "V in ('busted','confirmed','plausible')")]),
    _mb(A, "You can sneeze with your eyes open.", "Film forced sneezes with eyes held open.", "CONFIRMED", "Possible, though the reflex fights you.", ["V='confirmed'"], [("verdict", "V in ('busted','confirmed','plausible')")]),
    _mb(A, "Alcohol kills brain cells.", "Compare moderate drinkers' brains.", "BUSTED", "Alcohol damages connections, but doesn't mass-kill neurons.", ["V='busted'"], [("verdict", "V in ('busted','confirmed','plausible')")]),
    _mb(A, "Sharks must swim to breathe.", "Observe resting sharks' gill pumping.", "PLAUSIBLE", "Some must swim (obligate ram ventilators); others pump while resting.", ["V='plausible'"], [("verdict", "V in ('busted','confirmed','plausible')")]),
    _mb(A, "The Coriolis effect spins drains.", "Test drains at the equator vs poles.", "BUSTED", "Too weak at sink scale; basin shape decides.", ["V='busted'"], [("verdict", "V in ('busted','confirmed','plausible')")]),
    _mb(A, "Vitamin C prevents colds.", "Meta-analysis of trials.", "BUSTED", "No prevention; slight duration reduction at best.", ["V='busted'"], [("verdict", "V in ('busted','confirmed','plausible')")]),
    _mb(A, "Full moons raise crime.", "Correlate crime stats with lunar phase.", "BUSTED", "No correlation; brighter nights just mean more witnesses.", ["V='busted'"], [("verdict", "V in ('busted','confirmed','plausible')")]),
    _mb(A, "Bananas are radioactive enough to matter.", "Measure banana dose vs background.", "BUSTED", "Real radioactivity, negligible dose - the unit is a joke with a point.", ["V='busted'"], [("verdict", "V in ('busted','confirmed','plausible')")]),
    _mb(A, "You can hear the ocean in a shell.", "Record shell 'ocean' in a soundproof room.", "BUSTED", "It's ambient noise resonating; the room test proves it.", ["V='busted'"], [("verdict", "V in ('busted','confirmed','plausible')")]),
    _mb(A, "Lightning heats air hotter than the Sun's surface.", "Spectroscopy of strikes.", "CONFIRMED", "~30,000 K vs the Sun's 5,500 K surface - lightning wins.", ["V='confirmed'"], [("verdict", "V in ('busted','confirmed','plausible')")]),
]
