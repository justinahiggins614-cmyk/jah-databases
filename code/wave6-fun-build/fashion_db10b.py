"""Fashion db10 top-ups: shoe-guide +8, denim-guide +9."""
from music_db import T, list_demo
from fashion_db10 import ITEMS

def X(F, title, g, s1, s2, pts, keys, ca, cb):
    return T(title, g, [s1, s2], pts, keys, [ca, cb],
             demo=list_demo(title, [p[:30] for p in pts] + ['The done'], title + ':'))

_sg = [it for it in ITEMS if it['slug'] == 'shoe-guide'][0]
F = _sg['fields']
_sg['topics'] += [
X(F, 'The Mule', F[1], 'The shoe: the backless - the slipped, the chic. The shoe is the ease.', 'The easing: the heel.', ['The muled.', 'The ease.', 'Backless.', 'Heel.', 'The mule.'], ['Mule.', 'The muled.', 'Ease, backless.', 'The mule.', 'The chic.'], 'Style references: mules.', 'Practice references: the ease.'),
X(F, 'The Espadrille', F[1], 'The shoe: the juted - the summer, the canvas. The shoe is the vacation.', 'The vacationing: the sole.', ['The espadrilled.', 'The vacation.', 'Juted.', 'Sole.', 'The espadrille.'], ['Espadrille.', 'The espadrilled.', 'Vacation, juted.', 'The espadrille.', 'The canvas.'], 'Style references: espadrilles.', 'Practice references: the vacation.'),
X(F, 'The Wedge', F[1], 'The shoe: the wedged - the lifted, the stable. The shoe is the height.', 'The heighting: the summer.', ['The wedged.', 'The height.', 'Lifted.', 'Summer.', 'The wedge.'], ['Wedge.', 'The wedged.', 'Height, lifted.', 'The wedge.', 'The stable.'], 'Style references: wedges.', 'Practice references: the height.'),
X(F, 'The Platform', F[1], 'The shoe: the raised - the bold, the retro. The shoe is the statement.', 'The stating: the sole.', ['The platformed.', 'The statement.', 'Raised.', 'Sole.', 'The platform.'], ['Platform.', 'The platformed.', 'Statement, raised.', 'The platform.', 'The retro.'], 'Style references: platforms.', 'Practice references: the statement.'),
X(F, 'The Slipper', F[2], 'The shoe: the housed - the velvet, the cozy. The shoe is the home.', 'The homing: the evening.', ['The slippered.', 'The home.', 'Velvet.', 'Evening.', 'The slipper.'], ['Slipper.', 'The slippered.', 'Home, velvet.', 'The slipper.', 'The cozy.'], 'Style references: slippers.', 'Practice references: the home.'),
X(F, 'The Rain Boot', F[2], 'The boot: the puddled - the rubber, the tall. The boot is the dry.', 'The drying: the storm.', ['The booted.', 'The dry.', 'Rubbered.', 'Storm.', 'The rain boot.'], ['Rain boot.', 'The booted.', 'Dry, rubbered.', 'The rain boot.', 'The tall.'], 'Style references: rain boots.', 'Practice references: the dry.'),
X(F, 'The Hiking Boot', F[2], 'The boot: the trailed - the lugged, the ankle. The boot is the summit.', 'The summiting: the trail.', ['The booted.', 'The summit.', 'Lugged.', 'Trail.', 'The hiking boot.'], ['Hiking boot.', 'The booted.', 'Summit, lugged.', 'The hiking boot.', 'The ankle.'], 'Style references: hiking boots.', 'Practice references: the summit.'),
X(F, 'The Shoe Donation', F[2], 'The donation: the passed - the wearable, the boxed. The donation is the circular.', 'The circling: the closet.', ['The donated.', 'The circular.', 'Wearable.', 'Closet.', 'The shoe donation.'], ['Shoe donation.', 'The donated.', 'Circular, wearable.', 'The shoe donation.', 'The boxed.'], 'Practice references: donating shoes.', 'Ethics references: the circular.'),
]

_dg = [it for it in ITEMS if it['slug'] == 'denim-guide'][0]
F = _dg['fields']
_dg['topics'] += [
X(F, 'The Mom Jean', F[1], 'The jean: the highed-tapered - the retro, the comfy. The jean is the return.', 'The returning: the 90s.', ['The mommed.', 'The return.', 'Tapered.', '90s.', 'The mom jean.'], ['Mom jean.', 'The mommed.', 'Return, tapered.', 'The mom jean.', 'The retro.'], 'Style references: mom jeans.', 'Culture references: the return.'),
X(F, 'The Boyfriend Jean', F[1], 'The jean: the borrowed - the slouchy, the cuffed. The jean is the ease.', 'The easing: the borrowed.', ['The friended.', 'The ease.', 'Slouchy.', 'Borrowed.', 'The boyfriend jean.'], ['Boyfriend jean.', 'The friended.', 'Ease, slouchy.', 'The boyfriend jean.', 'The cuffed.'], 'Style references: boyfriend jeans.', 'Practice references: the ease.'),
X(F, 'The Flare Return', F[1], 'The flare: the seventies - the long, the heeled. The flare is the groove.', 'The grooving: the hem.', ['The flared.', 'The groove.', 'Long.', 'Hem.', 'The flare return.'], ['Flare return.', 'The flared.', 'Groove, long.', 'The flare return.', 'The heeled.'], 'Style references: flares.', 'History references: the groove.'),
X(F, 'The Denim Skirt', F[1], 'The skirt: the jeaned - the mini, the midi. The skirt is the casual.', 'The casualing: the leg.', ['The skirted.', 'The casual.', 'Mini.', 'Leg.', 'The denim skirt.'], ['Denim skirt.', 'The skirted.', 'Casual, mini.', 'The denim skirt.', 'The midi.'], 'Style references: denim skirts.', 'Practice references: the casual.'),
X(F, 'The Denim Shorts', F[1], 'The shorts: the cut - the frayed, the summer. The shorts are the heat.', 'The heating: the thigh.', ['The shorted.', 'The heat.', 'Frayed.', 'Thigh.', 'The denim shorts.'], ['Denim shorts.', 'The shorted.', 'Heat, frayed.', 'The denim shorts.', 'The summer.'], 'Style references: denim shorts.', 'Practice references: the heat.'),
X(F, 'The Overdyed Denim', F[2], 'The dyed: the black-over - the coated, the deep. The dyed is the dark.', 'The darking: the vat.', ['The dyed.', 'The dark.', 'Overdyed.', 'Vat.', 'The overdyed denim.'], ['Overdyed denim.', 'The dyed.', 'Dark, overdyed.', 'The overdyed denim.', 'The coated.'], 'Textile references: overdyeing.', 'Style references: the dark.'),
X(F, 'The Stretch Question', F[2], 'The question: the elastane - the comfort, the bag. The question is the trade.', 'The trading: the knee.', ['The questioned.', 'The trade.', 'Stretched.', 'Knee.', 'The stretch question.'], ['Stretch question.', 'The questioned.', 'Trade, stretched.', 'The stretch question.', 'The comfort.'], 'Textile references: stretch denim.', 'Practice references: the trade.'),
X(F, 'The Japanese Mills', F[2], 'The mills: the revered - the Okayama, the shuttle. The mills are the temple.', 'The templing: the loom.', ['The milled.', 'The temple.', 'Okayama.', 'Loom.', 'The Japanese mills.'], ['Japanese mills.', 'The milled.', 'Temple, Okayama.', 'The Japanese mills.', 'The shuttle.'], 'Textile references: Japanese mills.', 'Culture references: the temple.'),
X(F, 'The Denim Archive', F[2], 'The archive: the kept - the vintage pairs, the deadstock. The archive is the museum.', 'The museuming: the closet.', ['The archived.', 'The museum.', 'Kept.', 'Closet.', 'The denim archive.'], ['Denim archive.', 'The archived.', 'Museum, kept.', 'The denim archive.', 'The deadstock.'], 'Culture references: denim archives.', 'Practice references: the museum.'),
]
