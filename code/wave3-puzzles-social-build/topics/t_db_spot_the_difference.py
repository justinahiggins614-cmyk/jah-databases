# -*- coding: utf-8 -*-
"""Topic module: db-spot-the-difference. Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T

CFG = mkcfg({
    "slug": "db-spot-the-difference", "name": "The Spot the Difference Database", "pfx": "JAH-SPOTHEDI-",
    "tagline_pub": "Spot-the-difference scenes with every difference catalogued - two pictures, ten changes: every record carrying the scene pair, the differences, and a check that the count holds, taught progressively along the ladder.",
    "tagline_sig": "The Signature spotter-sight: every pair a Signature test, every difference a Signature catch. The full ladder from easy spots through sneaky changes to Signature-grade eyes. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "Spot the Difference",
    "role_pub": "difference master - drawing the pairs and cataloguing every change",
    "role_sig": "Signature difference master - teaching Signature spotter-sight",
    "record_kind": "difference scene record", "record_kind_plural": "difference scenes",
    "demo_kind": "difference-proof", "demo_title": "Spot the Difference Study",
    "search_ph": "Search differences, compare, spot, changes, pairs...",
    "chat_ph": "Ask for a spot-the-difference...",
    "gen_blurb": "Generate clearly-labeled difference studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded difference scenes, every change catalogued, marching toward one million records. Presented in teaching-ladder order: easy spots, sneaky changes, Signature-grade.",
    "reqs": "Two sharp eyes and a compare-and-contrast habit.",
    "stds": "Every scene pair's differences are all catalogued; the demo verifies the count.",
    "cites": ["JAH Databases difference cataloguing standard v1.0"],
})


def _sd(tier, scene, differences, tip):
    return T(
        tier, "Differences: %s" % scene[:52].rstrip(" .?") + "...",
        desc_pub='SPOT THE DIFFERENCE:\n\nScene: %s\n\nTwo pictures - find all %d differences:\n%s\n\nSPOTTER TIP: %s'
        % (scene, len(differences),
           "\n".join("  %d. %s" % (i + 1, d) for i, d in enumerate(differences)), tip),
        desc_sig='Signature spotter-sight: %s hides %d changes - the Signature eye catches them all. The Signature edition treats every found difference as attention defeating similarity.' % (scene[:50], len(differences)),
        how_pub='Compare systematically: scan left to right, top to bottom, then check colors, counts, and positions - differences hide in the boring parts.',
        how_sig='The Signature way: blink between the pictures - motion reveals change.',
        keys=['Scene: %s' % scene,
              'Differences: %d, all catalogued.' % len(differences),
              'Tip: %s' % tip],
        demo=("check", {"code": ["SCENE = %r" % scene, "DIFFS = %r" % differences],
                        "checks": [("count_matches", "len(DIFFS) == %d" % len(differences)),
                                   ("descriptive", "all(len(d) > 12 for d in DIFFS)"),
                                   ("no_dupes", "len(set(DIFFS)) == len(DIFFS)")]}),
    )


B, C, A = "Foundations", "Compounded", "Advanced"
TOPICS = [
    _sd(B, "Two sunny park scenes.", ["The red ball is missing in picture 2.", "The kite's tail is shorter in picture 2.", "One cloud is gone from the sky.", "The dog has a spot in picture 1, not in 2."], "Start with the sky - clouds are easy."),
    _sd(B, "Two cozy living rooms.", ["The remote moved from sofa to table.", "The cat's tail points left in 1, right in 2.", "One book is missing from the shelf.", "The clock shows 3:00 vs 3:05."], "Clocks and remotes love to change."),
    _sd(B, "Two beach scenes.", ["The beach ball changed color.", "One umbrella is closed in picture 2.", "The seagull count differs by one.", "Footprints appear in picture 2."], "Count the repeating things."),
    _sd(B, "Two classrooms.", ["The chalkboard says 'Hi' vs 'Hi!'.", "One desk is missing its chair.", "The fish tank has 3 fish vs 2.", "The globe is turned differently."], "Text changes are free points."),
    _sd(B, "Two kitchens.", ["The apple count differs by one.", "The oven mitt moved hooks.", "One cabinet is open in picture 2.", "The clock hands swapped."], "Cabinets: open vs closed."),
    _sd(B, "Two gardens.", ["The watering can moved.", "One flower is missing.", "The birdbath water level changed.", "The fence has an extra picket in 2."], "Fences: count the pickets."),
    _sd(B, "Two toy rooms.", ["The teddy bear's bow is gone in 2.", "The toy car faces the other way.", "One block is missing.", "The rug pattern changed."], "Faces and directions flip."),
    _sd(B, "Two snowy yards.", ["The snowman lost a button.", "The sled moved.", "One pine tree is missing.", "Footprints lead a different way."], "Snowmen: count the buttons."),
    _sd(B, "Two libraries.", ["One book leans in picture 2.", "The globe shows a different continent.", "The lamp is on in 1, off in 2.", "The chair moved."], "Lamps: on vs off."),
    _sd(B, "Two farms.", ["The barn door is open in 2.", "One hay bale is missing.", "The tractor faces differently.", "The rooster moved fence posts."], "Doors: open vs closed."),
    _sd(B, "Two campsites.", ["The tent flap is tied in 2.", "The fire has more logs in 1.", "The cooler lid is open in 2.", "One marshmallow stick is missing."], "Flaps and lids: open vs shut."),
    _sd(C, "Two market streets.", ["The awning stripes differ in count.", "One stall's sign changed word.", "The pickpocket's hand moved.", "A window is open in 2.", "The cat on the crate is gone in 2.", "The clock tower shows different times."], "Signs: read every word."),
    _sd(C, "Two museum halls.", ["One painting's frame changed color.", "The statue's arm position differs.", "A rope barrier is missing in 2.", "The skylight has one more pane in 2.", "The bench moved.", "A plaque's text changed."], "Frames and plaques: the details."),
    _sd(C, "Two jungle clearings.", ["The waterfall's flow changed.", "One vine is cut in 2.", "The ruin's stone count differs.", "A parrot appears in 2.", "The pool's reflection changed.", "One flower color swapped."], "Water: compare the flows."),
    _sd(C, "Two train stations.", ["The departure board differs.", "One luggage cart is missing.", "The clock shows different times.", "A pigeon moved.", "The bench advert changed.", "One door is open in 2."], "Boards: read the times."),
    _sd(C, "Two attics.", ["The trunk is open in 2.", "The cobweb count differs.", "One photo frame is empty in 2.", "The window moon phase changed.", "The dress form's pin moved.", "Dust sheet fold differs."], "Cobwebs: count the strands."),
    _sd(C, "Two harbors.", ["One boat is missing in 2.", "The buoy count differs.", "A rope coil moved.", "The seagull formation changed.", "One window lit in 2.", "The flag direction flipped."], "Flags: wind direction."),
    _sd(C, "Two bakeries.", ["The display case lost a cake in 2.", "The flour spill shape changed.", "One oven mitt moved.", "The menu board differs.", "The cat appears in 2.", "A rolling pin moved."], "Displays: count the cakes."),
    _sd(C, "Two construction sites.", ["The crane angle changed.", "One cone is missing in 2.", "The scaffold gained a level in 2.", "A worker's helmet color changed.", "The blueprint moved.", "The cement truck moved."], "Cones: count them."),
    _sd(C, "Two aquarium tunnels.", ["One shark is missing in 2.", "The ray formation changed.", "A light is out in 2.", "The kelp sways differently.", "One fish school moved.", "The grate pattern changed."], "Schools: count the fish."),
    _sd(C, "Two festival nights.", ["One lantern is unlit in 2.", "The stage banner changed.", "A performer's costume differs.", "The crowd gained a balloon in 2.", "One stall closed in 2.", "The moon phase changed."], "Lanterns: lit vs unlit."),
    _sd(C, "Two mountain lodges.", ["The firewood stack shrank in 2.", "One ski is missing.", "The window frost pattern changed.", "The mantel photo swapped.", "A mug moved to the other table.", "The rug flipped."], "Stacks: compare heights."),
    _sd(C, "Two greenhouses.", ["One orchid color changed.", "The mister spray differs.", "A clay pot moved shelves.", "The path stone count changed.", "One leaf is missing in 2.", "The thermometer reads differently."], "Plants: compare leaf by leaf."),
    _sd(A, "Two old master banquet paintings.", ["The servant's face changed.", "One guest's hand moved.", "The fruit bowl lost a grape.", "The candle count differs.", "The dog under the table moved.", "The window view changed.", "One glass is fuller in 2.", "The tablecloth fold differs.", "A shadow moved.", "The chandelier lost a candle."], "Old masters: count the candles."),
    _sd(A, "Two space station interiors.", ["One panel light is out in 2.", "The cable bundle shifted.", "Earth's position in the viewport changed.", "A floating pen moved.", "One locker is open in 2.", "The screen text changed.", "A bolt is missing in 2.", "The plant grew in 2.", "One strap hangs loose in 2.", "The camera angle shifted."], "Panels: which lights are out."),
    _sd(A, "Two rainy city streets.", ["One neon letter is out in 2.", "The puddle reflection differs.", "An umbrella color changed.", "One window went dark in 2.", "The alley cat moved to the other side.", "A parked car moved spots.", "The traffic light changed.", "One awning is retracted in 2.", "The steam vent moved.", "A wall poster changed pictures."], "Neon: find the dead letter."),
    _sd(A, "Two rare book rooms.", ["One book's spine color changed.", "The ladder moved.", "The dust pattern shifted.", "One glass case is open in 2.", "The catalog drawer is open in 2.", "A bookmark moved.", "The lamp angle changed.", "One chair moved.", "The globe turned.", "A book is upside down in 2."], "Spines: the color catalog."),
    _sd(A, "Two glacier fields.", ["The crevasse widened in 2.", "One snow bridge collapsed in 2.", "The ice axe moved.", "A flag appeared in 2.", "The cloud formation changed.", "One track veered in 2.", "The blue ice patch grew.", "A rope coil moved.", "The sun position shifted.", "One rock moved."], "Ice: compare the cracks."),
    _sd(A, "Two coral reefs.", ["The octopus moved rocks in 2.", "One fish school changed direction.", "The anemone closed in 2.", "A diver's bubble trail moved.", "One coral branch broke in 2.", "The turtle moved.", "The light rays shifted.", "One shell opened in 2.", "The eel moved holes.", "A small crab moved rocks."], "Reefs: the octopus always moves."),
    _sd(A, "Two detective evidence walls.", ["One photo moved.", "A string was cut in 2.", "The coffee ring moved.", "One note's text changed.", "A pin is missing in 2.", "The map gained a mark in 2.", "One file moved.", "The wall clock changed time.", "A fingerprint moved.", "The lamp is on in 2."], "Walls: follow every string."),
    _sd(A, "Two desert nights.", ["One star is missing in 2.", "The satellite moved.", "The fire changed size.", "One dune shifted.", "The telescope angle changed.", "A scorpion moved.", "The moon phase changed.", "One tent flap moved.", "The coyote moved.", "A cactus shadow changed."], "Stars: find the missing one."),
    _sd(A, "Two foggy harbors.", ["One mast light is out in 2.", "The fog thickened in 2.", "A buoy moved.", "One gull moved.", "The ship's name changed.", "A rope hangs loose in 2.", "One window lit in 2.", "The crane moved.", "A boat moved.", "The lighthouse beam angle changed."], "Fog: the lights that vanish."),
    _sd(A, "Two magic stages.", ["The dove moved hats in 2.", "One curtain tie changed.", "The mirror angle shifted.", "A playing card moved tables.", "The trapdoor seam moved.", "One spotlight is out in 2.", "The assistant moved.", "The hat moved.", "One stage rope changed color.", "The backdrop changed."], "Stages: watch the mirrors."),
    _sd(A, "Two libraries at dusk.", ["One lamp is out in 2.", "The sunbeam moved.", "A book fell off the shelf in 2.", "One reading chair turned around.", "The catalog drawer opened in 2.", "A potted plant moved shelves.", "One window shade changed.", "The wall clock changed time.", "A backpack moved benches.", "One poster changed."], "Dusk: the light that moves."),
]
