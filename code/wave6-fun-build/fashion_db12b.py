"""Fashion db12 top-ups: swimwear-guide +8, maternity-style +8."""
from music_db import T, list_demo
from fashion_db12 import ITEMS

def X(F, title, g, s1, s2, pts, keys, ca, cb):
    return T(title, g, [s1, s2], pts, keys, [ca, cb],
             demo=list_demo(title, [p[:30] for p in pts] + ['The done'], title + ':'))

_sw = [it for it in ITEMS if it['slug'] == 'swimwear-guide'][0]
F = _sw['fields']
_sw['topics'] += [
X(F, 'The Swim Dress', F[1], 'The dress: the swum - the skirted, the vintage. The dress is the retro.', 'The retroing: the pool.', ['The dressed.', 'The retro.', 'Skirted.', 'Pool.', 'The swim dress.'], ['Swim dress.', 'The dressed.', 'Retro, skirted.', 'The swim dress.', 'The vintage.'], 'Style references: swim dresses.', 'History references: the retro.'),
X(F, 'The Surf Suit', F[1], 'The suit: the surfed - the zipped, the warm. The suit is the wave.', 'The waving: the break.', ['The suited.', 'The wave.', 'Zipped.', 'Break.', 'The surf suit.'], ['Surf suit.', 'The suited.', 'Wave, zipped.', 'The surf suit.', 'The warm.'], 'Style references: surf suits.', 'Practice references: the wave.'),
X(F, 'The Swim Legging', F[1], 'The legging: the swum - the UPF, the sporty. The legging is the covered.', 'The covering: the sun.', ['The legged.', 'The covered.', 'UPFed.', 'Sun.', 'The swim legging.'], ['Swim legging.', 'The legged.', 'Covered, UPFed.', 'The swim legging.', 'The sporty.'], 'Style references: swim leggings.', 'Practice references: the covered.'),
X(F, 'The Mix and Match', F[1], 'The mix: the matched - the tops, the bottoms. The mix is the personal.', 'The personalizing: the drawer.', ['The mixed.', 'The personal.', 'Topped.', 'Drawer.', 'The mix and match.'], ['Mix and match.', 'The mixed.', 'Personal, topped.', 'The mix and match.', 'The bottoms.'], 'Style references: mix-and-match swim.', 'Practice references: the personal.'),
X(F, 'The Poolside Style', F[2], 'The style: the lounged - the hat, the sandal. The style is the resort.', 'The resorting: the chair.', ['The styled.', 'The resort.', 'Hatted.', 'Chair.', 'The poolside style.'], ['Poolside style.', 'The styled.', 'Resort, hatted.', 'The poolside style.', 'The sandal.'], 'Style references: poolside.', 'Practice references: the resort.'),
X(F, 'The Waterpark Ready', F[2], 'The ready: the slided - the secure, the fun. The ready is the splash.', 'The splashing: the ride.', ['The readied.', 'The splash.', 'Secured.', 'Ride.', 'The waterpark ready.'], ['Waterpark ready.', 'The readied.', 'Splash, secured.', 'The waterpark ready.', 'The fun.'], 'Style references: waterpark swim.', 'Practice references: the splash.'),
X(F, 'The Honeymoon Swim', F[2], 'The swim: the wedded - the white, the new. The swim is the romantic.', 'The romancing: the sea.', ['The swum.', 'The romantic.', 'Wedded.', 'Sea.', 'The honeymoon swim.'], ['Honeymoon swim.', 'The swum.', 'Romantic, wedded.', 'The honeymoon swim.', 'The white.'], 'Style references: honeymoon swim.', 'Culture references: the romantic.'),
X(F, 'The Swim Confidence Oath', F[2], 'The oath: the body, honored - the swum, the joyful. The oath is the brave.', 'The braving: the water.', ['The honored.', 'The brave.', 'Swum.', 'Water.', 'The oath.'], ['Swim confidence oath.', 'The oathed.', 'Brave, swum.', 'The oath.', 'The joyful.'], 'Style references: the swim oath.', 'Practice references: the brave.'),
]

_mt = [it for it in ITEMS if it['slug'] == 'maternity-style'][0]
F = _mt['fields']
_mt['topics'] += [
X(F, 'The Bump Loungewear', F[1], 'The lounge: the soft - the jogger, the bump. The lounge is the home.', 'The homing: the couch.', ['The lounged.', 'The home.', 'Joggered.', 'Couch.', 'The bump loungewear.'], ['Bump loungewear.', 'The lounged.', 'Home, joggered.', 'The bump loungewear.', 'The soft.'], 'Style references: maternity loungewear.', 'Practice references: the home.'),
X(F, 'The Bump Sleep', F[1], 'The sleep: the rested - the pillow, the soft. The sleep is the needed.', 'The needing: the night.', ['The slept.', 'The needed.', 'Pillowed.', 'Night.', 'The bump sleep.'], ['Bump sleep.', 'The slept.', 'Needed, pillowed.', 'The bump sleep.', 'The soft.'], 'Style references: maternity sleep.', 'Practice references: the needed.'),
X(F, 'The Grandma Style', F[2], 'The style: the borrowed - the oversized, the comfy. The style is the secret.', 'The secreting: the closet.', ['The borrowed.', 'The secret.', 'Oversized.', 'Closet.', 'The grandma style.'], ['Grandma style.', 'The borrowed.', 'Secret, oversized.', 'The grandma style.', 'The comfy.'], 'Style references: borrowed style.', 'Practice references: the secret.'),
X(F, 'The Bump on Budget', F[2], 'The budget: the thrifty - the few pieces, the stretched. The budget is the wise.', 'The wising: the wallet.', ['The budgeted.', 'The wise.', 'Thrifty.', 'Wallet.', 'The bump on budget.'], ['Bump on budget.', 'The budgeted.', 'Wise, thrifty.', 'The bump on budget.', 'The stretched.'], 'Practice references: maternity budgets.', 'Style references: the wise.'),
X(F, 'The Hand-Me-Down Bump', F[2], 'The down: the passed - the sister, the friend. The down is the circular.', 'The circling: the bump.', ['The passed.', 'The circular.', 'Sistered.', 'Bump.', 'The hand-me-down bump.'], ['Hand-me-down bump.', 'The passed.', 'Circular, sistered.', 'The hand-me-down bump.', 'The friend.'], 'Style references: hand-me-downs.', 'Practice references: the circular.'),
X(F, 'The Bump Flat Lay', F[2], 'The lay: the styled - the weekly, the documented. The lay is the memory.', 'The remembering: the gram.', ['The laid.', 'The memory.', 'Styled.', 'Gram.', 'The bump flat lay.'], ['Bump flat lay.', 'The laid.', 'Memory, styled.', 'The bump flat lay.', 'The weekly.'], 'Style references: bump documentation.', 'Practice references: the memory.'),
X(F, 'The Name Reveal', F[2], 'The reveal: the named - the announced, the celebrated. The reveal is the joy.', 'The joying: the family.', ['The revealed.', 'The joy.', 'Named.', 'Family.', 'The name reveal.'], ['Name reveal.', 'The revealed.', 'Joy, named.', 'The name reveal.', 'The announced.'], 'Culture references: name reveals.', 'Practice references: the joy.'),
X(F, 'The Going-Home Outfit', F[2], 'The outfit: the headed-home - the soft, the photographed. The outfit is the first.', 'The firsting: the carseat.', ['The outfitted.', 'The first.', 'Soft.', 'Carseat.', 'The going-home outfit.'], ['Going-home outfit.', 'The outfitted.', 'First, soft.', 'The going-home outfit.', 'The photographed.'], 'Style references: going-home outfits.', 'Culture references: the first.'),
]
