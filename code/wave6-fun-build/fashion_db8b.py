"""Fashion db8 top-ups: cultural-dress +4, workwear-style +6."""
from music_db import T, list_demo
from fashion_db8 import ITEMS

def X(F, title, g, s1, s2, pts, keys, ca, cb):
    return T(title, g, [s1, s2], pts, keys, [ca, cb],
             demo=list_demo(title, [p[:30] for p in pts] + ['The done'], title + ':'))

_cd = [it for it in ITEMS if it['slug'] == 'cultural-dress'][0]
F = _cd['fields']
_cd['topics'] += [
X(F, 'The Textile Pilgrimage', F[2], 'The pilgrimage: the sourced - the markets, the makers. The pilgrimage is the journey.', 'The journeying: the world.', ['The sourced.', 'The journey.', 'Marketed.', 'World.', 'The pilgrimage.'], ['Textile pilgrimage.', 'The pilgrimaged.', 'Journey, sourced.', 'The pilgrimage.', 'The makers.'], 'Culture references: textile travel.', 'Practice references: the journey.'),
X(F, 'The Craft Preservation', F[2], 'The preservation: the kept - the taught, the funded. The preservation is the future.', 'The futuring: the hands.', ['The kept.', 'The future.', 'Taught.', 'Hands.', 'The preservation.'], ['Craft preservation.', 'The preserved.', 'Future, taught.', 'The preservation.', 'The funded.'], 'Ethics references: craft preservation.', 'Culture references: the future.'),
X(F, 'The Respectful Wearing', F[2], 'The wearing: the invited - the gifted, the occasioned. The wearing is the honor.', 'The honoring: the moment.', ['The invited.', 'The honor.', 'Gifted.', 'Moment.', 'The wearing.'], ['Respectful wearing.', 'The worn.', 'Honor, gifted.', 'The wearing.', 'The occasioned.'], 'Ethics references: respectful wearing.', 'Culture references: the honor.'),
X(F, 'The Global Closet', F[2], 'The closet: the world, folded - the collected, the loved. The closet is the museum.', 'The museuming: the home.', ['The folded.', 'The museum.', 'Collected.', 'Home.', 'The global closet.'], ['Global closet.', 'The closeted.', 'Museum, folded.', 'The global closet.', 'The loved.'], 'Culture references: the global closet.', 'Practice references: the museum.'),
]

_ww = [it for it in ITEMS if it['slug'] == 'workwear-style'][0]
F = _ww['fields']
_ww['topics'] += [
X(F, 'The Union Suit', F[1], 'The suit: the one-piece - the thermal, the vintage. The suit is the base.', 'The basing: the long.', ['The pieced.', 'The base.', 'Thermaled.', 'Long.', 'The union suit.'], ['Union suit.', 'The suited.', 'Base, thermaled.', 'The union suit.', 'The vintage.'], 'History references: union suits.', 'Style references: the base.'),
X(F, 'The Watch Cap', F[1], 'The cap: the knit - the navy, the rolled. The cap is the sailor.', 'The sailing: the cold.', ['The knitted.', 'The sailor.', 'Navied.', 'Cold.', 'The watch cap.'], ['Watch cap.', 'The capped.', 'Sailor, navied.', 'The watch cap.', 'The rolled.'], 'Style references: watch caps.', 'History references: the sailor.'),
X(F, 'The Suspenders', F[2], 'The braces: the held-up - the buttoned, the striped. The braces are the classic.', 'The classicking: the waist.', ['The held.', 'The classic.', 'Buttoned.', 'Waist.', 'The suspenders.'], ['Suspenders.', 'The suspended.', 'Classic, buttoned.', 'The suspenders.', 'The striped.'], 'Style references: suspenders.', 'History references: the classic.'),
X(F, 'The Bandana', F[2], 'The cloth: the neck - the paisley, the dust. The cloth is the worker.', 'The working: the neck.', ['The clothed.', 'The worker.', 'Paisleyed.', 'Neck.', 'The bandana.'], ['Bandana.', 'The bandanaed.', 'Worker, paisleyed.', 'The bandana.', 'The dust.'], 'Style references: bandanas.', 'History references: the worker.'),
X(F, 'The Tool Belt Style', F[2], 'The belt: the carried - the pouches, the hammer. The belt is the ready.', 'The readying: the job.', ['The carried.', 'The ready.', 'Pouched.', 'Job.', 'The tool belt.'], ['Tool belt style.', 'The belted.', 'Ready, pouched.', 'The tool belt.', 'The hammer.'], 'Style references: tool belts.', 'Practice references: the ready.'),
X(F, 'The Hi-Vis Pop', F[2], 'The pop: the neon - the reflective, the safety. The pop is the seen.', 'The seeing: the site.', ['The popped.', 'The seen.', 'Neoned.', 'Site.', 'The hi-vis pop.'], ['Hi-vis pop.', 'The popped.', 'Seen, neon.', 'The hi-vis pop.', 'The reflective.'], 'Style references: hi-vis.', 'Practice references: the seen.'),
]
