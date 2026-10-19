"""Fashion db11 top-ups: knitwear-guide +9, outerwear-guide +8."""
from music_db import T, list_demo
from fashion_db11 import ITEMS

def X(F, title, g, s1, s2, pts, keys, ca, cb):
    return T(title, g, [s1, s2], pts, keys, [ca, cb],
             demo=list_demo(title, [p[:30] for p in pts] + ['The done'], title + ':'))

_kw = [it for it in ITEMS if it['slug'] == 'knitwear-guide'][0]
F = _kw['fields']
_kw['topics'] += [
X(F, 'The Turtleneck Dress', F[1], 'The dress: the turtled - the ribbed, the elegant. The dress is the winter.', 'The wintering: the boot.', ['The dressed.', 'The winter.', 'Turtled.', 'Boot.', 'The turtleneck dress.'], ['Turtleneck dress.', 'The dressed.', 'Winter, turtled.', 'The turtleneck dress.', 'The ribbed.'], 'Style references: turtleneck dresses.', 'Practice references: the winter.'),
X(F, 'The Knit Skirt', F[1], 'The skirt: the knitted - the ribbed, the midi. The skirt is the cozy.', 'The cozying: the tight.', ['The skirted.', 'The cozy.', 'Knitted.', 'Tight.', 'The knit skirt.'], ['Knit skirt.', 'The skirted.', 'Cozy, knitted.', 'The knit skirt.', 'The ribbed.'], 'Style references: knit skirts.', 'Practice references: the cozy.'),
X(F, 'The Shrug', F[1], 'The wrap: the shrugged - the cropped, the bolero. The wrap is the evening.', 'The evening: the shoulders.', ['The shrugged.', 'The evening.', 'Cropped.', 'Shoulders.', 'The shrug.'], ['Shrug.', 'The shrugged.', 'Evening, cropped.', 'The shrug.', 'The bolero.'], 'Style references: shrugs.', 'Practice references: the evening.'),
X(F, 'The Knit Poncho', F[1], 'The wrap: the ponchoed - the cozy, the draped. The wrap is the fireside.', 'The firing: the couch.', ['The ponchoed.', 'The fireside.', 'Cozy.', 'Couch.', 'The knit poncho.'], ['Knit poncho.', 'The ponchoed.', 'Fireside, cozy.', 'The knit poncho.', 'The draped.'], 'Style references: knit ponchos.', 'Practice references: the fireside.'),
X(F, 'The Balaclava', F[2], 'The hood: the knitted - the warm, the full. The hood is the arctic.', 'The arcticking: the wind.', ['The hooded.', 'The arctic.', 'Knitted.', 'Wind.', 'The balaclava.'], ['Balaclava.', 'The balaclavaed.', 'Arctic, knitted.', 'The balaclava.', 'The warm.'], 'Style references: balaclavas.', 'Practice references: the arctic.'),
X(F, 'The Knit Scarf', F[2], 'The scarf: the knitted - the chunky, the wrapped. The scarf is the classic.', 'The classicking: the neck.', ['The scarfed.', 'The classic.', 'Knitted.', 'Neck.', 'The knit scarf.'], ['Knit scarf.', 'The scarfed.', 'Classic, knitted.', 'The knit scarf.', 'The chunky.'], 'Style references: knit scarves.', 'Practice references: the classic.'),
X(F, 'The Knit Hat', F[2], 'The hat: the knitted - the beanie, the cuffed. The hat is the warm.', 'The warming: the head.', ['The hatted.', 'The warm.', 'Beanie.', 'Head.', 'The knit hat.'], ['Knit hat.', 'The hatted.', 'Warm, beanie.', 'The knit hat.', 'The cuffed.'], 'Style references: knit hats.', 'Practice references: the warm.'),
X(F, 'The Knit Gloves', F[2], 'The gloves: the knitted - the fingered, the warm. The gloves are the hands.', 'The handing: the cold.', ['The gloved.', 'The hands.', 'Knitted.', 'Cold.', 'The knit gloves.'], ['Knit gloves.', 'The gloved.', 'Hands, knitted.', 'The knit gloves.', 'The fingered.'], 'Style references: knit gloves.', 'Practice references: the hands.'),
X(F, 'The Knit Socks', F[2], 'The socks: the knitted - the wool, the cozy. The socks are the feet.', 'The footing: the boot.', ['The socked.', 'The feet.', 'Knitted.', 'Boot.', 'The knit socks.'], ['Knit socks.', 'The socked.', 'Feet, knitted.', 'The knit socks.', 'The wool.'], 'Style references: knit socks.', 'Practice references: the feet.'),
]

_ow = [it for it in ITEMS if it['slug'] == 'outerwear-guide'][0]
F = _ow['fields']
_ow['topics'] += [
X(F, 'The Anorak', F[1], 'The jacket: the pullover - the hooded, the kangaroo. The jacket is the trail.', 'The trailing: the wind.', ['The anoraked.', 'The trail.', 'Hooded.', 'Wind.', 'The anorak.'], ['Anorak.', 'The anoraked.', 'Trail, hooded.', 'The anorak.', 'The kangaroo.'], 'Style references: anoraks.', 'Practice references: the trail.'),
X(F, 'The Duffle Coat', F[1], 'The coat: the toggled - the horned, the hooded. The coat is the collegiate.', 'The colleging: the campus.', ['The coated.', 'The collegiate.', 'Toggled.', 'Campus.', 'The duffle coat.'], ['Duffle coat.', 'The coated.', 'Collegiate, toggled.', 'The duffle coat.', 'The horned.'], 'Style references: duffle coats.', 'History references: the collegiate.'),
X(F, 'The Shearling', F[1], 'The coat: the sheared - the aviator, the warm. The coat is the luxe.', 'The luxing: the cockpit.', ['The sheared.', 'The luxe.', 'Aviator.', 'Cockpit.', 'The shearling.'], ['Shearling.', 'The sheared.', 'Luxe, aviator.', 'The shearling.', 'The warm.'], 'Style references: shearling.', 'History references: the luxe.'),
X(F, 'The Quilted Jacket', F[1], 'The jacket: the quilted - the diamond, the country. The jacket is the equestrian.', 'The equestring: the field.', ['The jacketed.', 'The equestrian.', 'Quilted.', 'Field.', 'The quilted jacket.'], ['Quilted jacket.', 'The jacketed.', 'Equestrian, quilted.', 'The quilted jacket.', 'The diamond.'], 'Style references: quilted jackets.', 'Culture references: the equestrian.'),
X(F, 'The Cocoon Coat', F[2], 'The coat: the cocooned - the rounded, the modern. The coat is the sculptural.', 'The sculpting: the city.', ['The coated.', 'The sculptural.', 'Cocooned.', 'City.', 'The cocoon coat.'], ['Cocoon coat.', 'The coated.', 'Sculptural, cocooned.', 'The cocoon coat.', 'The rounded.'], 'Style references: cocoon coats.', 'Practice references: the sculptural.'),
X(F, 'The Wrap Coat', F[2], 'The coat: the wrapped - the belted, the fluid. The coat is the elegant.', 'The elegancing: the tie.', ['The coated.', 'The elegant.', 'Wrapped.', 'Tie.', 'The wrap coat.'], ['Wrap coat.', 'The coated.', 'Elegant, wrapped.', 'The wrap coat.', 'The belted.'], 'Style references: wrap coats.', 'Practice references: the elegant.'),
X(F, 'The Storm Flap', F[2], 'The flap: the stormed - the snapped, the sealed. The flap is the dry.', 'The drying: the rain.', ['The flapped.', 'The dry.', 'Stormed.', 'Rain.', 'The storm flap.'], ['Storm flap.', 'The flapped.', 'Dry, stormed.', 'The storm flap.', 'The sealed.'], 'Craft references: storm flaps.', 'Practice references: the dry.'),
X(F, 'The Packable Down', F[2], 'The down: the packed - the stuffed, the traveled. The down is the portable.', 'The portabling: the suitcase.', ['The packed.', 'The portable.', 'Stuffed.', 'Suitcase.', 'The packable down.'], ['Packable down.', 'The packed.', 'Portable, stuffed.', 'The packable down.', 'The traveled.'], 'Style references: packable down.', 'Practice references: the portable.'),
]
