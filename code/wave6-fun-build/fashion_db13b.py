"""Fashion db13 top-ups: petite-style +8, plus-size-style +8."""
from music_db import T, list_demo
from fashion_db13 import ITEMS

def X(F, title, g, s1, s2, pts, keys, ca, cb):
    return T(title, g, [s1, s2], pts, keys, [ca, cb],
             demo=list_demo(title, [p[:30] for p in pts] + ['The done'], title + ':'))

_ps = [it for it in ITEMS if it['slug'] == 'petite-style'][0]
F = _ps['fields']
_ps['topics'] += [
X(F, 'The Petite Coat', F[1], 'The coat: the scaled - the knee-hit, the belted. The coat is the proportion.', 'The proportioning: the winter.', ['The coated.', 'The proportion.', 'Scaled.', 'Winter.', 'The petite coat.'], ['Petite coat.', 'The coated.', 'Proportion, scaled.', 'The petite coat.', 'The belted.'], 'Style references: petite coats.', 'Practice references: the proportion.'),
X(F, 'The Petite Boot', F[1], 'The boot: the shafted-right - the ankle, the knee. The boot is the leg.', 'The legging: the calf.', ['The booted.', 'The leg.', 'Shafted.', 'Calf.', 'The petite boot.'], ['Petite boot.', 'The booted.', 'Leg, shafted.', 'The petite boot.', 'The ankle.'], 'Style references: petite boots.', 'Practice references: the leg.'),
X(F, 'The Petite Dress', F[1], 'The dress: the hemmed-right - the above-knee, the mini. The dress is the leg.', 'The legging: the hem.', ['The dressed.', 'The leg.', 'Hemmed.', 'Hem.', 'The petite dress.'], ['Petite dress.', 'The dressed.', 'Leg, hemmed.', 'The petite dress.', 'The mini.'], 'Style references: petite dresses.', 'Practice references: the leg.'),
X(F, 'The Petite Skirt', F[1], 'The skirt: the shortened - the mini, the high-waisted. The skirt is the leg.', 'The legging: the thigh.', ['The skirted.', 'The leg.', 'Shortened.', 'Thigh.', 'The petite skirt.'], ['Petite skirt.', 'The skirted.', 'Leg, shortened.', 'The petite skirt.', 'The mini.'], 'Style references: petite skirts.', 'Practice references: the leg.'),
X(F, 'The Petite Blazer', F[2], 'The blazer: the scaled - the nipped, the cropped. The blazer is the sharp.', 'The sharping: the office.', ['The blazered.', 'The sharp.', 'Scaled.', 'Office.', 'The petite blazer.'], ['Petite blazer.', 'The blazered.', 'Sharp, scaled.', 'The petite blazer.', 'The nipped.'], 'Style references: petite blazers.', 'Practice references: the sharp.'),
X(F, 'The Petite Swim', F[2], 'The swim: the proportioned - the high-cut, the scaled. The swim is the confident.', 'The confiding: the water.', ['The swum.', 'The confident.', 'Proportioned.', 'Water.', 'The petite swim.'], ['Petite swim.', 'The swum.', 'Confident, proportioned.', 'The petite swim.', 'The high-cut.'], 'Style references: petite swim.', 'Practice references: the confident.'),
X(F, 'The Petite Loungewear', F[2], 'The lounge: the scaled - the jogger, the cropped. The lounge is the cozy.', 'The cozying: the home.', ['The lounged.', 'The cozy.', 'Scaled.', 'Home.', 'The petite loungewear.'], ['Petite loungewear.', 'The lounged.', 'Cozy, scaled.', 'The petite loungewear.', 'The jogger.'], 'Style references: petite loungewear.', 'Practice references: the cozy.'),
X(F, 'The Petite Confidence', F[2], 'The confidence: the owned - the stood-tall, the styled. The confidence is the wearer.', 'The wearing: the day.', ['The owned.', 'The wearer.', 'Stood-tall.', 'Day.', 'The petite confidence.'], ['Petite confidence.', 'The owned.', 'Wearer, stood-tall.', 'The petite confidence.', 'The styled.'], 'Style references: petite confidence.', 'Practice references: the wearer.'),
]

_pl = [it for it in ITEMS if it['slug'] == 'plus-size-style'][0]
F = _pl['fields']
_pl['topics'] += [
X(F, 'The Jumpsuit Plus', F[1], 'The suit: the jumped - the one-piece, the cinched. The suit is the easy.', 'The easing: the zip.', ['The suited.', 'The easy.', 'Jumped.', 'Zip.', 'The jumpsuit plus.'], ['Jumpsuit plus.', 'The suited.', 'Easy, jumped.', 'The jumpsuit plus.', 'The cinched.'], 'Style references: plus jumpsuits.', 'Practice references: the easy.'),
X(F, 'The Wide-Leg Plus', F[1], 'The leg: the widened - the palazzo, the flow. The leg is the drama.', 'The dramaing: the hem.', ['The legged.', 'The drama.', 'Widened.', 'Hem.', 'The wide-leg plus.'], ['Wide-leg plus.', 'The legged.', 'Drama, widened.', 'The wide-leg plus.', 'The palazzo.'], 'Style references: plus wide-leg.', 'Practice references: the drama.'),
X(F, 'The Midi Magic', F[1], 'The magic: the mided - the swished, the perfect-length. The magic is the twirl.', 'The twirling: the knee.', ['The magicked.', 'The twirl.', 'Mided.', 'Knee.', 'The midi magic.'], ['Midi magic.', 'The magicked.', 'Twirl, mided.', 'The midi magic.', 'The swished.'], 'Style references: midi dresses.', 'Practice references: the twirl.'),
X(F, 'The Duster Coat', F[1], 'The coat: the dustered - the long, the layered. The coat is the line.', 'The lining: the vertical.', ['The coated.', 'The line.', 'Dustered.', 'Vertical.', 'The duster coat.'], ['Duster coat.', 'The coated.', 'Line, dustered.', 'The duster coat.', 'The layered.'], 'Style references: duster coats.', 'Practice references: the line.'),
X(F, 'The Kimono Layer', F[2], 'The layer: the kimonoed - the flowing, the printed. The layer is the art.', 'The arting: the drape.', ['The layered.', 'The art.', 'Kimonoed.', 'Drape.', 'The kimono layer.'], ['Kimono layer.', 'The layered.', 'Art, kimonoed.', 'The kimono layer.', 'The printed.'], 'Style references: kimono layers.', 'Practice references: the art.'),
X(F, 'The Co-ord Set', F[2], 'The set: the matched - the top-bottom, the intentional. The set is the put-together.', 'The togethering: the print.', ['The set.', 'The put-together.', 'Matched.', 'Print.', 'The co-ord set.'], ['Co-ord set.', 'The set.', 'Put-together, matched.', 'The co-ord set.', 'The intentional.'], 'Style references: co-ords.', 'Practice references: the put-together.'),
X(F, 'The Vacation Plus', F[2], 'The vacation: the packed - the resort, the bold. The vacation is the celebrated.', 'The celebrating: the sun.', ['The vacationed.', 'The celebrated.', 'Resorted.', 'Sun.', 'The vacation plus.'], ['Vacation plus.', 'The vacationed.', 'Celebrated, resorted.', 'The vacation plus.', 'The bold.'], 'Style references: vacation plus.', 'Practice references: the celebrated.'),
X(F, 'The Date Night Plus', F[2], 'The night: the dressed - the sleek, the confident. The night is the allure.', 'The alluring: the evening.', ['The nighted.', 'The allure.', 'Dressed.', 'Evening.', 'The date night plus.'], ['Date night plus.', 'The nighted.', 'Allure, dressed.', 'The date night plus.', 'The sleek.'], 'Style references: date night plus.', 'Practice references: the allure.'),
]
