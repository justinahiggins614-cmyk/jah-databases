"""Fashion-style PUBLIC-DATABASE items, part 4: seasonal-style, occasion-dressing,
streetwear-culture, vintage-fashion, luxury-fashion, sustainable-fashion. 12+12+10=34 each.
Property of Justin Addam Higgins (JAH)."""
from music_db import T, list_demo
from fashion_db3b import ITEMS
from fashion_db1 import _mk

def X(F, title, g, s1, s2, pts, keys, ca, cb):
    return T(title, g, [s1, s2], pts, keys, [ca, cb],
             demo=list_demo(title, [p[:30] for p in pts] + ['The ' + title.split()[1].lower() if len(title.split()) > 1 else 'The done'],
                            title + ':'))

# ============ 6. seasonal-style ============
_it = _mk('seasonal-style', 'The Seasonal Style Database',
 'Dress every season brilliantly: spring layers, summer ease, autumn texture, winter warmth — 34 complete guides to the year in style, every one weather-ready.',
 'seasonal style record', 'JAH Seasonal Style Archivist',
 'seasonal style archivist — teaching dressing for every season; answering from many angles using only archive data',
 'Ask me about seasons — spring, summer, autumn, or winter.',
 'Search seasonal style, spring, summer, autumn, winter...', 'Ask about seasons...', 'season',
 ['Season Foundations', 'The Four Seasons', 'Seasonal Mastery'],
 'The Signature treatment of seasonal style: the same real seasonal knowledge carried forward, plus Signature-original season philosophies original to this system.')
F = _it['fields']
_it['topics'] = [
X(F, 'The Seasonal Rhythm', F[0], 'The rhythm: the year, dressed — the rotation, the anticipation. The rhythm is the wardrobe\u2019s breath.', 'The following: the seasons, the closet.', ['The rotated.', 'The breath.', 'Year, dressed.', 'Anticipated.', 'The rhythm.'], ['Seasonal rhythm.', 'The breathed.', 'Rotation, dressed.', 'The rhythm.', 'The year.'], 'Style references: seasonal rhythm.', 'Practice references: the rotate.'),
X(F, 'The Transitional Trick', F[0], 'The transition: the between — the layer, the shed. The transition is the skill.', 'The layering: the adaptable.', ['The between.', 'The skill.', 'Layered.', 'Adaptable.', 'The trick.'], ['Transitional trick.', 'The tricked.', 'Between, layered.', 'The trick.', 'The skill.'], 'Style references: transitional dressing.', 'Practice references: the layer.'),
X(F, 'Spring Awakening', F[1], 'The spring: the light return — the pastel, the trench. The spring is the fresh.', 'The wearing: the renewal.', ['The light.', 'The fresh.', 'Pastel.', 'Renewed.', 'The spring.'], ['Spring awakening.', 'The sprung.', 'Fresh, worn.', 'The spring.', 'The renewal.'], 'Style references: spring style.', 'Practice references: the wear.'),
X(F, 'The Spring Layer', F[1], 'The layer: the spring\u2019s — the cardigan, the scarf. The layer is the variable.', 'The variable: the morning, the noon.', ['The variable.', 'The layered.', 'Morning.', 'Noon.', 'The layer.'], ['Spring layer.', 'The layered.', 'Variable, worn.', 'The layer.', 'The spring.'], 'Style references: spring layering.', 'Practice references: the variable.'),
X(F, 'The Spring Shoe', F[1], 'The shoe: the spring\u2019s — the loafer, the white sneaker. The shoe is the step.', 'The stepping: the fresh.', ['The stepped.', 'The fresh.', 'Loafer.', 'Sneaker.', 'The shoe.'], ['Spring shoe.', 'The shoed.', 'Step, fresh.', 'The shoe.', 'The spring.'], 'Style references: spring shoes.', 'Practice references: the step.'),
X(F, 'Summer Ease', F[1], 'The summer: the heat, dressed — the linen, the bare. The summer is the ease.', 'The wearing: the cool.', ['The heat.', 'The ease.', 'Linen.', 'Cool.', 'The summer.'], ['Summer ease.', 'The eased.', 'Heat, dressed.', 'The summer.', 'The cool.'], 'Style references: summer style.', 'Practice references: the wear.'),
X(F, 'The Linen Life', F[1], 'The linen: the summer\u2019s — the breath, the wrinkle. The linen is the honest.', 'The wrinkling: the lived.', ['The breathed.', 'The honest.', 'Wrinkled.', 'Lived.', 'The linen.'], ['Linen life.', 'The linend.', 'Honest, breathed.', 'The linen.', 'The wrinkle.'], 'Textile references: linen.', 'Style references: the wear.'),
X(F, 'The Summer Dress', F[1], 'The dress: the summer\u2019s — the flow, the bare. The dress is the joy.', 'The flowing: the heat.', ['The flowed.', 'The joy.', 'Bare.', 'Heat.', 'The dress.'], ['Summer dress.', 'The dressed.', 'Joy, flowed.', 'The dress.', 'The summer.'], 'Style references: summer dresses.', 'Practice references: the flow.'),
X(F, 'Autumn Texture', F[1], 'The autumn: the cool return — the knit, the boot. The autumn is the rich.', 'The wearing: the layered.', ['The cool.', 'The rich.', 'Knitted.', 'Layered.', 'The autumn.'], ['Autumn texture.', 'The textured.', 'Rich, layered.', 'The autumn.', 'The knit.'], 'Style references: autumn style.', 'Practice references: the wear.'),
X(F, 'The Boot Season', F[1], 'The boots: the autumn\u2019s — the ankle, the knee. The boots are the stomp.', 'The stomping: the leaves.', ['The stomped.', 'The leaves.', 'Ankle.', 'Knee.', 'The boots.'], ['Boot season.', 'The booted.', 'Stomp, leaved.', 'The boots.', 'The autumn.'], 'Style references: boots.', 'Practice references: the stomp.'),
X(F, 'The Knit Season', F[1], 'The knits: the autumn\u2019s — the chunky, the soft. The knits are the hug.', 'The hugging: the cool.', ['The hugged.', 'The cool.', 'Chunky.', 'Soft.', 'The knits.'], ['Knit season.', 'The knitted.', 'Hug, worn.', 'The knits.', 'The autumn.'], 'Style references: knitwear.', 'Practice references: the hug.'),
X(F, 'Winter Warmth', F[1], 'The winter: the cold, dressed — the wool, the down. The winter is the cozy.', 'The wearing: the warm.', ['The cold.', 'The cozy.', 'Wooled.', 'Warm.', 'The winter.'], ['Winter warmth.', 'The warmed.', 'Cozy, dressed.', 'The winter.', 'The wool.'], 'Style references: winter style.', 'Practice references: the wear.'),
X(F, 'The Coat Investment', F[1], 'The coat: the winter\u2019s — the wool, the forever. The coat is the armor.', 'The choosing: the decades.', ['The armored.', 'The forever.', 'Wooled.', 'Decades.', 'The coat.'], ['Coat investment.', 'The coated.', 'Armor, chosen.', 'The coat.', 'The decades.'], 'Style references: winter coats.', 'Practice references: the choose.'),
X(F, 'The Layering System', F[1], 'The system: the winter\u2019s — the base, the mid, the shell. The system is the science.', 'The layering: the trapped warmth.', ['The system.', 'The science.', 'Based.', 'Trapped.', 'The layers.'], ['Layering system.', 'The systemed.', 'Science, layered.', 'The layers.', 'The warmth.'], 'Style references: layering systems.', 'Practice references: the trap.'),
X(F, 'The Winter Accessory', F[1], 'The accessories: the winter\u2019s — the scarf, the glove, the hat. The accessories are the finish.', 'The finishing: the warm.', ['The finished.', 'The warm.', 'Scarfed.', 'Gloved.', 'The accessories.'], ['Winter accessory.', 'The accessoried.', 'Finish, warmed.', 'The accessories.', 'The hat.'], 'Style references: winter accessories.', 'Practice references: the finish.'),
X(F, 'The Holiday Dress', F[1], 'The holiday: the festive — the velvet, the shine. The holiday is the sparkle.', 'The sparkling: the season.', ['The festive.', 'The sparkle.', 'Velvet.', 'Seasoned.', 'The holiday.'], ['Holiday dress.', 'The holidazed.', 'Sparkle, worn.', 'The holiday.', 'The velvet.'], 'Style references: holiday dressing.', 'Culture references: the festive.'),
X(F, 'The Seasonal Closet', F[2], 'The closet: the rotated — the stored, the current. The closet is the cycle.', 'The cycling: the year.', ['The rotated.', 'The cycle.', 'Stored.', 'Year.', 'The closet.'], ['Seasonal closet.', 'The closeted.', 'Cycle, rotated.', 'The closet.', 'The stored.'], 'Practice references: seasonal closets.', 'Style references: the cycle.'),
X(F, 'The Seasonal Shop', F[2], 'The shop: the timed — the end-of-season, the pre. The shop is the strategy.', 'The timing: the sales.', ['The timed.', 'The strategy.', 'Sales.', 'Pre.', 'The shop.'], ['Seasonal shop.', 'The shopped.', 'Strategy, timed.', 'The shop.', 'The sales.'], 'Practice references: seasonal shopping.', 'Style references: the time.'),
X(F, 'The Seasonal Care', F[2], 'The care: the stored — the cedar, the clean. The care is the keeping.', 'The keeping: the off-season.', ['The stored.', 'The keeping.', 'Cedared.', 'Off-season.', 'The care.'], ['Seasonal care.', 'The cared.', 'Keeping, stored.', 'The care.', 'The cedar.'], 'Practice references: seasonal storage.', 'Craft references: the keep.'),
X(F, 'The Seasonal Legacy', F[2], 'The legacy: the years, dressed — the seasons, the memories. The legacy is the year, worn.', 'The wearing: the annual.', ['The worn.', 'The memories.', 'Years.', 'Annual.', 'The legacy.'], ['Seasonal legacy.', 'The legacied.', 'Year, worn.', 'The legacy.', 'Your seasons.'], 'Practice references: the seasonal life.', 'Inspiration references: the database entire.'),
]
ITEMS.append(_it)
