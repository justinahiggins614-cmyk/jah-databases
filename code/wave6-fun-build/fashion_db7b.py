"""Fashion db7 completion: fashion-history top-up +8 topics (26 -> 34)."""
from music_db import T, list_demo
from fashion_db7 import ITEMS

def X(F, title, g, s1, s2, pts, keys, ca, cb):
    return T(title, g, [s1, s2], pts, keys, [ca, cb],
             demo=list_demo(title, [p[:30] for p in pts] + ['The done'], title + ':'))

_fh = [it for it in ITEMS if it['slug'] == 'fashion-history'][0]
F = _fh['fields']
_fh['topics'] += [
X(F, 'The Menswear Revolution', F[1], 'The revolution: the suit, loosened - the casual, the sneaker. The revolution is the ease.', 'The easing: the office.', ['The loosened.', 'The ease.', 'Suited.', 'Office.', 'The menswear revolution.'], ['Menswear revolution.', 'The revolutioned.', 'Ease, loosened.', 'The menswear revolution.', 'The sneaker.'], 'History references: menswear.', 'Culture references: the ease.'),
X(F, 'The Denim Story', F[1], 'The story: the workwear - the mines, the streets. The story is the democratic.', 'The democratizing: the rivet.', ['The worked.', 'The democratic.', 'Mined.', 'Rivet.', 'The denim story.'], ['Denim story.', 'The storied.', 'Democratic, mined.', 'The denim story.', 'The streets.'], 'History references: denim.', 'Culture references: the democratic.'),
X(F, 'The Sneaker Century', F[1], 'The century: the rubber - the court, the street. The century is the casual.', 'The casualing: the sole.', ['The rubbered.', 'The casual.', 'Courted.', 'Sole.', 'The sneaker century.'], ['Sneaker century.', 'The centuried.', 'Casual, rubbered.', 'The sneaker century.', 'The street.'], 'History references: sneakers.', 'Culture references: the casual.'),
X(F, 'The Underwear Unseen', F[2], 'The unseen: the beneath - the corset, the brief. The unseen is the foundation.', 'The founding: the silhouette.', ['The b.eneath.', 'The foundation.', 'Corseted.', 'Silhouette.', 'The unseen.'], ['Unseen underwear.', 'The b.eneath.', 'Foundation, corseted.', 'The unseen.', 'The brief.'], 'History references: underwear.', 'Culture references: the foundation.'),
X(F, 'The Hat Eras', F[2], 'The hats: the crowned - the top, the cloche. The hats are the eras.', 'The eraing: the head.', ['The crowned.', 'The eras.', 'Topped.', 'Head.', 'The hat eras.'], ['Hat eras.', 'The hatted.', 'Eras, crowned.', 'The hat eras.', 'The cloche.'], 'History references: hats.', 'Culture references: the eras.'),
X(F, 'The Bag Timeline', F[2], 'The timeline: the carried - the reticule, the it-bag. The timeline is the held.', 'The holding: the arm.', ['The carried.', 'The held.', 'Reticuled.', 'Arm.', 'The bag timeline.'], ['Bag timeline.', 'The timelined.', 'Held, carried.', 'The bag timeline.', 'The it-bag.'], 'History references: handbags.', 'Culture references: the held.'),
X(F, 'The Textile Revolutions', F[2], 'The revolutions: the looms - the cotton gin, the synthetic. The revolutions are the changed.', 'The changing: the mill.', ['The loomed.', 'The changed.', 'Ginned.', 'Mill.', 'The textile revolutions.'], ['Textile revolutions.', 'The revolutioned.', 'Changed, loomed.', 'The textile revolutions.', 'The synthetic.'], 'History references: textile revolutions.', 'Craft references: the changed.'),
X(F, 'The Future of Fashion', F[2], 'The future: the coming - the tech, the circular. The future is the unwritten.', 'The unwriting: the now.', ['The coming.', 'The unwritten.', 'Teched.', 'Now.', 'The future.'], ['Future of fashion.', 'The futured.', 'Unwritten, teched.', 'The future.', 'The circular.'], 'Culture references: fashion futures.', 'History references: the unwritten.'),
]
