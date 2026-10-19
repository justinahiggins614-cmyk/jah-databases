"""Fashion db5 top-ups: occasion-dressing +7, streetwear-culture +7."""
from music_db import T, list_demo
from fashion_db5 import ITEMS

def X(F, title, g, s1, s2, pts, keys, ca, cb):
    return T(title, g, [s1, s2], pts, keys, [ca, cb],
             demo=list_demo(title, [p[:30] for p in pts] + ['The done'], title + ':'))

_od = [it for it in ITEMS if it['slug'] == 'occasion-dressing'][0]
F = _od['fields']
_od['topics'] += [
X(F, 'The Housewarming', F[1], 'The warming: the home, celebrated — the cozy, the chic. The warming is the welcome.', 'The welcoming: the host.', ['The celebrated.', 'The welcome.', 'Cozy.', 'Host.', 'The warming.'], ['Housewarming.', 'The warmed.', 'Welcome, cozy.', 'The warming.', 'The chic.'], 'Style references: housewarmings.', 'Culture references: the welcome.'),
X(F, 'The Occasion Kit', F[2], 'The kit: the bag, packed — the flats, the blot. The kit is the saved.', 'The saving: the night.', ['The packed.', 'The saved.', 'Flats.', 'Night.', 'The kit.'], ['Occasion kit.', 'The kitted.', 'Saved, packed.', 'The kit.', 'The blot.'], 'Practice references: occasion kits.', 'Style references: the save.'),
X(F, 'The Plus-One Rule', F[2], 'The rule: the guest\u2019s guest — the coordinated, the kind. The rule is the harmony.', 'The harmonizing: the pair.', ['The coordinated.', 'The harmony.', 'Guest.', 'Pair.', 'The rule.'], ['Plus-one rule.', 'The ruled.', 'Harmony, coordinated.', 'The rule.', 'The kind.'], 'Culture references: plus-ones.', 'Practice references: the coordinate.'),
X(F, 'The Dress Code Ask', F[2], 'The ask: the clarified — the text, the host. The ask is the smart.', 'The smarting: the sure.', ['The clarified.', 'The smart.', 'Texted.', 'Sure.', 'The ask.'], ['Dress code ask.', 'The asked.', 'Smart, clarified.', 'The ask.', 'The host.'], 'Practice references: asking dress codes.', 'Style references: the smart.'),
X(F, 'The Occasion Budget', F[2], 'The budget: the event, afforded — the rent, the rewear. The budget is the wise.', 'The wising: the wallet.', ['The afforded.', 'The wise.', 'Rented.', 'Wallet.', 'The budget.'], ['Occasion budget.', 'The budgeted.', 'Wise, afforded.', 'The budget.', 'The rewear.'], 'Practice references: occasion budgets.', 'Style references: the wise.'),
X(F, 'The Rewear Pride', F[2], 'The pride: the repeated — the loved, the known. The pride is the sustainable.', 'The sustaining: the favorite.', ['The repeated.', 'The sustainable.', 'Loved.', 'Favorite.', 'The pride.'], ['Rewear pride.', 'The prided.', 'Sustainable, repeated.', 'The pride.', 'The known.'], 'Style references: rewearing.', 'Culture references: the sustainable.'),
X(F, 'The Occasion Oath', F[2], 'The oath: the moments, honored — the dressed, the present. The oath is the showing up.', 'The showing: the life.', ['The honored.', 'The showing.', 'Dressed.', 'Life.', 'The oath.'], ['Occasion oath.', 'The oathed.', 'Showing up, honored.', 'The oath.', 'Your moments.'], 'Style references: the occasion oath.', 'Practice references: the show.'),
]

_sw = [it for it in ITEMS if it['slug'] == 'streetwear-culture'][0]
F = _sw['fields']
_sw['topics'] += [
X(F, 'The Skate Park Fit', F[1], 'The fit: the session — the durable, the loose. The fit is the ride.', 'The riding: the park.', ['The sessioned.', 'The ride.', 'Durable.', 'Park.', 'The fit.'], ['Skate park fit.', 'The fitted.', 'Ride, sessioned.', 'The fit.', 'The loose.'], 'Style references: skate fits.', 'Culture references: the park.'),
X(F, 'The Drop Calendar', F[2], 'The calendar: the releases — the Thursdays, the alarms. The calendar is the hunt.', 'The hunting: the drop.', ['The released.', 'The hunt.', 'Thursdays.', 'Drop.', 'The calendar.'], ['Drop calendar.', 'The calendared.', 'Hunt, released.', 'The calendar.', 'The alarms.'], 'Practice references: drop calendars.', 'Culture references: the hunt.'),
X(F, 'The Legit Check', F[2], 'The check: the real — the stitch, the tag. The check is the smart.', 'The smarting: the fake-spot.', ['The real.', 'The smart.', 'Stitched.', 'Fake-spot.', 'The check.'], ['Legit check.', 'The checked.', 'Smart, stitched.', 'The check.', 'The tag.'], 'Practice references: legit checks.', 'Culture references: the real.'),
X(F, 'The Rotation Plan', F[2], 'The plan: the kicks, cycled — the worn, the deadstock. The plan is the care.', 'The caring: the collection.', ['The cycled.', 'The care.', 'Worn.', 'Collection.', 'The plan.'], ['Rotation plan.', 'The planned.', 'Care, cycled.', 'The plan.', 'The deadstock.'], 'Practice references: sneaker rotations.', 'Culture references: the care.'),
X(F, 'The Custom Piece', F[2], 'The custom: the one-of-one — the painted, the sewn. The custom is the you.', 'The youing: the hands.', ['The one-of-one.', 'The you.', 'Painted.', 'Hands.', 'The custom.'], ['Custom piece.', 'The customed.', 'You, painted.', 'The custom.', 'The sewn.'], 'Culture references: customs.', 'Practice references: the hands.'),
X(F, 'The Hand-Me-Down', F[2], 'The down: the passed — the older sibling\u2019s grail. The down is the lineage.', 'The lineaging: the family.', ['The passed.', 'The lineage.', 'Sibling.', 'Family.', 'The down.'], ['Hand-me-down.', 'The downed.', 'Lineage, passed.', 'The down.', 'The grail.'], 'Culture references: hand-me-downs.', 'Practice references: the pass.'),
X(F, 'The First Cop', F[2], 'The cop: the first — the line, the box. The cop is the memory.', 'The remembering: the grail.', ['The first.', 'The memory.', 'Lined.', 'Grail.', 'The cop.'], ['First cop.', 'The copped.', 'Memory, first.', 'The cop.', 'The box.'], 'Culture references: first cops.', 'Practice references: the remember.'),
]
