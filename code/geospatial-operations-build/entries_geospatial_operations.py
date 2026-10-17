#!/usr/bin/env python3
"""Entries for the Geospatial Operations databases (missing-115 program, Wave 1).

Verified 2026-10-17 (missing-115 Wave 1): RAW SWEEP over the full manifest
(2,390 databases) PLUS every shard index title in jah-databases-data-1:
zero 'geospatial-operations' slugs/names; zero title collisions for the 34
planned titles. The one keyword near-hit, 'geospatial-databases'
(JAH-GSP-), is a meta-database of database TYPES for the planet
(record_kind 'geospatial database type record': GIS, terrain, weather,
oceans, environmental sensing taxonomies) - NOT operational geospatial
computation. It has no routing algorithms, spatial indexes, error budgets,
projection math, or map-matching. The paste's rule was applied by
name/purpose/record schema/capabilities: operational geospatial
computation (routes, coordinates, boundaries, terrain, proximity, spatial
joins, location uncertainty) is a distinct capability - BUILD NEW is the
verdict.

So this build creates two NEW databases, 34 ladder-ordered records each:

  geospatial-operations            - The Geospatial Operations Database
                                     (public-harvest: real, fact-checked
                                     operational geospatial computation -
                                     routes, coordinates, boundaries,
                                     terrain, proximity, spatial joins,
                                     location uncertainty; map projections,
                                     geohashing and spatial indexes, routing
                                     algorithms, map-matching, GPS error
                                     budgets, coordinate systems, spatial
                                     query patterns; standard references
                                     NIMA TR8350.2 WGS84; OGC 06-103r4
                                     Simple Features; OGC 18-010r7 WKT2;
                                     EPSG Geodetic Parameter Dataset;
                                     PROJ; GDAL; PostGIS; Vincenty 1975;
                                     Karney 2013; Dijkstra 1959; Hart et
                                     al. 1968; Geisberger et al. 2008;
                                     Newson and Krumm 2009; Kaplan and
                                     Hegarty 2017; Parkinson and Spilker
                                     1996; Kalman 1960; FGDC NSSDA;
                                     ASPRS 2014; and the other landmarks
                                     cited per record)
  geospatial-operations-signature  - The Geospatial Operations Signature
                                     Database
                                     (his original Signature Survey Method:
                                     every coordinate a sworn witness, the
                                     map the testimony, the route the sworn
                                     path, uncertainty the honest margin;
                                     src signature, titles suffixed
                                     " (Signature Edition)", never
                                     presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-GEOP- (public) and JAH-GEOPS- (signature), verified free
in the manifest (2,390 databases; JAH-GEO- belongs to the Geography Atlas,
JAH-GEO2- to Geology, JAH-GEOG-PUB/SIG to the public/signature geography
databases) and in every shard index (zero hits for either prefix).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_geospatial_operations.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

Civilian operational scope only. Never the words "bat belt" anywhere.
No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Survey Method: "
            "every coordinate a sworn witness, the map the testimony, the "
            "route the sworn path, and uncertainty the honest margin. "
            "Clearly labeled Signature-made, never presented as authentic "
            "public record.")

CIT_WGS84 = ("NIMA Technical Report TR8350.2. Department of Defense World "
             "Geodetic System 1984, Its Definition and Relationships with "
             "Local Geodetic Systems. 3rd ed.; 2000 (amended 2004).")
CIT_OGC_SFS = ("OGC 06-103r4. OpenGIS Implementation Standard for "
               "Geographic information - Simple feature access - Common "
               "architecture; 2011.")
CIT_WKT2 = ("OGC 18-010r7 / ISO 19162:2019. Geographic information - "
            "Well-known text representation of coordinate reference "
            "systems.")
CIT_EPSG = ("EPSG Geodetic Parameter Dataset, maintained by the IOGP "
            "Geomatics Committee (epsg.org).")
CIT_PROJ = ("PROJ contributors. PROJ coordinate transformation software "
            "library (proj.org).")
CIT_GDAL = ("GDAL/OGR contributors. GDAL - Geospatial Data Abstraction "
            "Library (gdal.org).")
CIT_POSTGIS = ("PostGIS Project. PostGIS spatial database extender "
            "documentation (postgis.net).")
CIT_VINCENTY = ("Vincenty T. Direct and inverse solutions of geodesics on "
                "the ellipsoid with application of nested equations. "
                "Survey Review 23(176); 1975.")
CIT_KARNEY = ("Karney CFF. Algorithms for geodesics. Journal of Geodesy "
              "87(1); 2013.")
CIT_DIJKSTRA = ("Dijkstra EW. A note on two problems in connexion with "
                "graphs. Numerische Mathematik 1; 1959.")
CIT_ASTAR = ("Hart PE, Nilsson NJ, Raphael B. A formal basis for the "
             "heuristic determination of minimum cost paths. IEEE "
             "Transactions on Systems Science and Cybernetics 4(2); 1968.")
CIT_CH = ("Geisberger R, Sanders P, Schultes D, Delling D. Contraction "
          "hierarchies: faster and simpler hierarchical routing in road "
          "networks. WEA 2008, LNCS 5038.")
CIT_MAPMATCH = ("Newson P, Krumm J. Hidden Markov map matching through "
                "noise and sparseness. Proc. ACM SIGSPATIAL GIS; 2009.")
CIT_GPS = ("Kaplan ED, Hegarty CJ (eds). Understanding GPS/GNSS: "
           "Principles and Applications. 3rd ed. Artech House; 2017.")
CIT_PARKINSON = ("Parkinson BW, Spilker JJ (eds). Global Positioning "
                 "System: Theory and Applications, vols. I-II. AIAA; 1996.")
CIT_KALMAN = ("Kalman RE. A new approach to linear filtering and "
              "prediction problems. J. Basic Engineering 82(1); 1960.")
CIT_NSSDA = ("FGDC-STD-007.3-1998. Geospatial Positioning Accuracy "
             "Standards, Part 3: National Standard for Spatial Data "
             "Accuracy.")
CIT_ASPRS = ("ASPRS. ASPRS Positional Accuracy Standards for Digital "
             "Geospatial Data, Edition 1, Version 1.0; 2014.")
CIT_RTR = ("Guttman A. R-trees: a dynamic index structure for spatial "
           "searching. Proc. ACM SIGMOD; 1984.")
CIT_QUAD = ("Finkel RA, Bentley JL. Quad trees: a data structure for "
            "retrieval on composite keys. Acta Informatica 4; 1974.")
CIT_H3 = ("Uber Technologies. H3: Uber's Hexagonal Hierarchical Spatial "
          "Index (h3geo.org).")
CIT_GEOHASH = ("Niemeyer G. Geohash (geohash.org); 2008.")
CIT_ISO19115 = ("ISO 19115-1:2014. Geographic information - Metadata - "
                "Part 1: Fundamentals.")
CIT_TOBLER = ("Tobler W. A computer movie simulating urban growth in the "
              "Detroit region. Economic Geography 46; 1970.")
CIT_DE9IM = ("Egenhofer MJ, Franzosa RD. Point-set topological spatial "
             "relations. Int. J. Geographical Information Systems 5(2); "
             "1991.")
CIT_HORN = ("Horn BKP. Hill shading and the reflectance map. Proc. IEEE "
            "69(1); 1981.")
CIT_GOODCHILD = ("Zhang J, Goodchild MF. Uncertainty in Geographical "
                 "Information. Taylor and Francis; 2002.")

ENTRIES = [
    {
        "key": "what_coordinate",
        "name": "What a Coordinate Is",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "A coordinate is an address for a point on the Earth, written as "
            "numbers that only mean something inside a stated system. The "
            "most familiar form is latitude and longitude: latitude measures "
            "degrees north or south of the equator, from -90 at the South "
            "Pole to +90 at the North Pole, and longitude measures degrees "
            "east or west of the prime meridian through Greenwich, from -180 "
            "to +180. A pair like 40.7128, -74.0060 names a point in lower "
            "Manhattan - but only because the numbers are read inside the "
            "WGS84 datum, the reference frame nearly every GPS receiver and "
            "web map uses. Change the datum and the same two numbers point "
            "somewhere else, by meters or more. Coordinates come in three "
            "common notations: decimal degrees (40.7128), degrees and decimal "
            "minutes (40 42.768'), and degrees-minutes-seconds "
            "(40 42' 46.08\"). They are all the same address in different "
            "handwriting. The first operational rule of this database is the "
            "one everything else builds on: a coordinate without its "
            "coordinate system is not a location, it is just two numbers."
        ),
        "how_it_works": (
            "A coordinate works by anchoring numbers to a physical model of "
            "the Earth. Latitude and longitude are angles measured from the "
            "center of the reference ellipsoid: latitude is the angle "
            "between the equatorial plane and the line perpendicular to the "
            "ellipsoid surface at the point, and longitude is the angle "
            "around the polar axis from the prime meridian. The WGS84 "
            "ellipsoid that defines these angles has a semi-major axis of "
            "exactly 6,378,137 meters and a flattening of 1/298.257223563, "
            "which makes the Earth about 21 kilometers wider than it is "
            "tall. To convert between notations, divide: 40 degrees, 42 "
            "minutes, 46.08 seconds becomes 40 + 42/60 + 46.08/3600 = "
            "40.7128 degrees. Southern latitudes and western longitudes take "
            "the negative sign. Software stores coordinates as decimal "
            "degrees in double precision, which resolves far below a "
            "millimeter, and every honest dataset names its datum alongside "
            "the numbers so the address can actually be found."
        ),
        "key_points": [
            "Latitude runs -90 to +90 from the equator and longitude runs -180 to +180 from the prime meridian; together they name any point on the globe.",
            "The same two numbers point to different ground in different datums - the datum is part of the address, and WGS84 is the default for GPS and web maps.",
            "Decimal degrees, degrees-decimal-minutes, and degrees-minutes-seconds are three notations for one address; convert by dividing minutes by 60 and seconds by 3600.",
            "The WGS84 ellipsoid is defined by a semi-major axis of exactly 6,378,137 meters and a flattening of 1/298.257223563.",
            "A coordinate without a stated coordinate system is not a location - it is just two numbers waiting to be misread.",
        ],
        "requirements": [
            "Two numeric values with their order stated explicitly (latitude-first or longitude-first), because the two orders are both in wide use.",
            "A named datum or coordinate reference system, WGS84 unless there is a documented reason otherwise.",
            "A stated notation and unit: decimal degrees are the working standard for computation.",
            "Enough decimal places for the task: five decimals resolve about a meter, seven about a centimeter.",
            "A sign convention: negative latitude is south, negative longitude is west.",
        ],
        "standards": [
            "WGS84 (NIMA TR8350.2) is the reference datum for GPS coordinates and the default datum of this database.",
            "Coordinates are exchanged in decimal degrees per the OGC simple-features and WKT conventions.",
            "The prime meridian is Greenwich and angular units are degrees unless a CRS definition states otherwise.",
        ],
        "citations": [CIT_WGS84, CIT_OGC_SFS, CIT_WKT2],
        "sig_lens": (
            "The Signature read: a coordinate is a sworn witness - two "
            "numbers that testify where a point stands, and the datum is the "
            "oath they swear it under. The Signature Survey Method treats "
            "every coordinate as testimony given under a named system, "
            "because a witness who will not name their oath cannot be "
            "trusted on the stand."
        ),
    },
    {
        "key": "geographic_vs_projected",
        "name": "Geographic Versus Projected Coordinates",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Coordinates come in two great families, and confusing them is "
            "the most expensive beginner mistake in geospatial work. "
            "Geographic coordinates are angles - latitude and longitude in "
            "degrees on the curved Earth, the family every GPS receiver "
            "speaks. Projected coordinates are flat-map positions, usually "
            "in meters east and north from a stated origin, produced by "
            "mathematically unrolling a patch of the curved Earth onto a "
            "plane. The Universal Transverse Mercator system is the famous "
            "example: the world is cut into 60 zones, each 6 degrees of "
            "longitude wide, and inside a zone every point gets an easting "
            "and northing in meters. A survey crew measuring a building site "
            "wants meters they can tape-measure, so they work projected; a "
            "ship crossing an ocean wants angles that stay true over long "
            "distances, so it works geographic. Neither family is better - "
            "each is the right tool for its range - but every distance, "
            "area, and buffer computed in the wrong family comes out wrong, "
            "sometimes spectacularly."
        ),
        "how_it_works": (
            "The two families connect through map projections, which are "
            "functions from angle pairs to plane pairs. Take UTM zone 18N, "
            "which covers New York: its central meridian is 75 degrees west, "
            "assigned a false easting of 500,000 meters so no easting goes "
            "negative, and the equator gets a false northing of 0 in the "
            "northern hemisphere. A point at 40.7128 N, 74.0060 W converts "
            "to roughly 583,960 meters east and 4,507,350 meters north in "
            "that zone. Inside the zone, a meter on the map is very nearly a "
            "meter on the ground - the central meridian carries a scale "
            "factor of 0.9996, a deliberate 1-in-2500 shrink that balances "
            "distortion across the zone's width. Step outside the zone and "
            "the error grows fast, which is why software must check the "
            "zone before trusting the meters. Geographic coordinates skip "
            "all of this: one degree of latitude is always about 111,132 "
            "meters, while one degree of longitude shrinks with the cosine "
            "of latitude, from about 111,320 meters at the equator to zero "
            "at the poles."
        ),
        "key_points": [
            "Geographic coordinates are angles in degrees on the curved Earth; projected coordinates are flat-plane positions, usually meters east and north.",
            "UTM cuts the world into 60 six-degree zones with a 0.9996 central-meridian scale factor and a 500,000-meter false easting - meters you can trust inside the zone.",
            "One degree of latitude is always about 111,132 meters, but one degree of longitude is 111,320 meters times the cosine of latitude.",
            "Short-range measurement belongs in a projected system; long-range and global work belongs in geographic coordinates.",
            "Projected coordinates used outside their zone, or mixed across zones, produce silently wrong distances and areas.",
        ],
        "requirements": [
            "A stated family for every dataset: geographic (degrees) or projected (meters), never assumed.",
            "For projected data, the exact projection and zone - UTM zone 18N is not interchangeable with UTM zone 17N.",
            "For geographic data, the datum - WGS84 unless documented otherwise.",
            "Distance routines that know which family they are in: planar math for projected, spherical or ellipsoidal math for geographic.",
            "A zone-validity check before trusting projected meters near any zone edge.",
        ],
        "standards": [
            "UTM follows the standard 60-zone, 6-degree definition with k0 = 0.9996 and 500,000 m false easting.",
            "Projected coordinates are exchanged in meters; geographic coordinates in decimal degrees.",
            "CRS definitions follow the EPSG registry and WKT2 so the family, zone, and datum travel with the data.",
        ],
        "citations": [CIT_EPSG, CIT_WKT2, CIT_PROJ],
        "sig_lens": (
            "The Signature read: the two families are two languages of "
            "testimony - the curved tongue of angles for the long voyage "
            "and the flat tongue of meters for the building site. The "
            "Signature Survey Method swears every dataset to one language "
            "and translates on purpose, never by accident."
        ),
    },
    {
        "key": "curved_earth_distance",
        "name": "Distance on a Curved Earth",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The shortest path between two points on the Earth is not a "
            "straight line on a flat map - it is a great-circle arc, the "
            "path a plane actually flies. New York to London looks like a "
            "straight line on a Mercator wall map, but the true shortest "
            "route arcs far north over the Atlantic, and it is shorter than "
            "the straight-looking line by hundreds of kilometers. Three "
            "levels of distance math serve three ranges. For quick estimates "
            "the haversine formula treats the Earth as a sphere and gets "
            "within about 0.5 percent, which is plenty for finding the "
            "nearest store. For surveying and geodesy, Vincenty's formulae "
            "and Karney's algorithms work on the WGS84 ellipsoid itself and "
            "reach millimeter accuracy - Karney's method also converges for "
            "nearly antipodal points where Vincenty's iteration can fail. "
            "For points a few kilometers apart, flat-plane math on "
            "projected coordinates is fine. The operational rule is range "
            "discipline: pick the formula that matches the distance, because "
            "a sphere is a fine Earth for a delivery radius and a terrible "
            "Earth for a property boundary."
        ),
        "how_it_works": (
            "The haversine formula converts two latitude-longitude pairs "
            "into a central angle: take the differences in latitude and "
            "longitude, halve them, square their sines, combine with the "
            "cosines of the latitudes, and take twice the arcsine of the "
            "square root. Multiply that angle by the Earth's mean radius "
            "(6,371,008.8 meters per IUGG) and the result is the great-circle "
            "distance. New York (40.7128, -74.0060) to London (51.5074, "
            "-0.1278) comes out near 5,570 kilometers. Ellipsoidal methods "
            "refine this by iterating on the ellipsoid's actual curvature: "
            "Vincenty's inverse formula solves for the geodesic between the "
            "points, usually agreeing with the haversine to a few "
            "kilometers on intercontinental routes and diverging where "
            "precision matters. For short hops under a few kilometers, the "
            "equirectangular approximation - treating degrees as flat with "
            "longitude scaled by the cosine of latitude - is accurate to "
            "meters and far cheaper to compute. Routing engines and spatial "
            "databases choose per query: sphere for the fast filter, "
            "ellipsoid for the final answer."
        ),
        "key_points": [
            "The shortest path on Earth is a great-circle arc, not a straight line on a flat map - the true New York to London route arcs north.",
            "Haversine on a sphere is accurate to about 0.5 percent: the fast estimate for search radii and nearest-neighbor filters.",
            "Vincenty and Karney solve on the WGS84 ellipsoid for millimeter accuracy; Karney converges where Vincenty can fail near antipodal points.",
            "Under a few kilometers, flat-plane math with longitude scaled by cosine of latitude is accurate and cheap.",
            "Range discipline decides the formula: sphere for the fast filter, ellipsoid for the final surveyed answer.",
        ],
        "requirements": [
            "Both endpoints in the same datum, stated up front - mixing datums corrupts every distance.",
            "A chosen Earth model per computation: mean sphere for estimates, WGS84 ellipsoid for precision.",
            "Angles in radians inside the math, degrees at the human interface - convert deliberately.",
            "A documented accuracy target so the formula matches the tolerance: 0.5 percent, meters, or millimeters.",
            "Antipodal handling: use Karney-class algorithms when points can be nearly opposite on the globe.",
        ],
        "standards": [
            "The IUGG mean Earth radius 6,371,008.8 m is the standard sphere for haversine estimates.",
            "Ellipsoidal geodesics follow Vincenty 1975 or Karney 2013 on the WGS84 ellipsoid.",
            "Published distances state the model used - sphere, ellipsoid, or planar - so results are reproducible.",
        ],
        "citations": [CIT_VINCENTY, CIT_KARNEY, CIT_WGS84],
        "sig_lens": (
            "The Signature read: distance is the oath between two witnesses "
            "- and the Earth keeps its own shape regardless of the map's "
            "flattery. The Signature Survey Method measures along the "
            "planet's true curve for far journeys and the honest flat patch "
            "for near ones, swearing each measurement to the model that "
            "earned it."
        ),
    },
    {
        "key": "coordinate_precision",
        "name": "Coordinate Precision and Significant Digits",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Every decimal place in a coordinate is a promise about how well "
            "the position is known, and the promises have fixed sizes. One "
            "decimal place of latitude spans about 11.1 kilometers; two "
            "span 1.11 kilometers; three span 111 meters; four span 11.1 "
            "meters; five span 1.11 meters; six span 11 centimeters; seven "
            "span about a centimeter. Writing seven decimals for a position "
            "measured with a phone GPS - which is honestly uncertain by "
            "several meters - is not precision, it is fiction with extra "
            "digits. The reverse trap is truncation: rounding a survey-grade "
            "measurement to four decimals throws away real accuracy the "
            "instrument actually earned. Longitude digits shrink with the "
            "cosine of latitude, so the same decimal count means finer "
            "ground resolution near the poles, but the ladder of promises "
            "holds everywhere. Operational rule: store full double "
            "precision, display and publish only the digits the measurement "
            "honestly supports, and never let a formatted string be the "
            "system of record."
        ),
        "how_it_works": (
            "The digit ladder comes from dividing the meters-per-degree by "
            "powers of ten. A degree of latitude is about 111,132 meters, "
            "so each added decimal place divides the ground footprint by "
            "ten: 0.1 degrees is 11,113 meters, 0.01 is 1,111 meters, down "
            "to 0.0000001 degrees at about 1.1 centimeters. Double-precision "
            "floating point carries about 15 to 16 significant decimal "
            "digits, which resolves position far below an atom - the "
            "storage is never the limit; the measurement always is. A "
            "consumer GPS fix honestly supports about four to five decimals "
            "(ten meters to one meter); a survey RTK fix supports seven or "
            "eight. When coordinates pass through text - CSV exports, URLs, "
            "printed reports - the formatter must be told how many digits "
            "to keep, because the default six decimals of many tools "
            "quietly promise 11-centimeter knowledge the data may not have. "
            "Databases therefore store the raw doubles plus a separate "
            "accuracy field, so the digits and the honesty travel together."
        ),
        "key_points": [
            "Each decimal place of latitude divides the ground footprint by ten: 1 decimal is 11.1 km, 5 decimals is 1.11 m, 7 decimals is about 1.1 cm.",
            "Digits beyond the measurement's honesty are fiction - a phone GPS fix does not become survey-grade by printing seven decimals.",
            "Truncation is the reverse trap: rounding survey-grade data to four decimals discards accuracy the instrument actually earned.",
            "Double precision stores position far below a millimeter; the measurement, not the storage, is always the limit.",
            "Store raw doubles plus a separate accuracy field, and format display digits to match the honest accuracy.",
        ],
        "requirements": [
            "A documented honest accuracy for every coordinate source: phone GPS, survey RTK, digitized map, or unknown.",
            "Storage in double precision, never in formatted text as the system of record.",
            "Display formatting matched to honest accuracy: 4-5 decimals for consumer GPS, 7-8 for survey RTK.",
            "Longitude awareness: the same decimal count resolves finer ground near the poles via the cosine of latitude.",
            "An accuracy or uncertainty attribute carried alongside every stored coordinate.",
        ],
        "standards": [
            "Positional accuracy is reported at 95 percent confidence per the NSSDA (RMSE times 1.7308 horizontally).",
            "ASPRS 2014 accuracy classes tie decimal-worthy precision to tested RMSE values.",
            "Metadata records the source accuracy per ISO 19115 so digits are never read as promises.",
        ],
        "citations": [CIT_NSSDA, CIT_ASPRS, CIT_ISO19115],
        "sig_lens": (
            "The Signature read: digits are vows, and a vow beyond your "
            "knowledge is a false oath. The Signature Survey Method prints "
            "only the decimals its instruments have earned, and keeps the "
            "rest sheathed - because honest testimony names exactly what "
            "it knows and not one digit more."
        ),
    },
    {
        "key": "map_projections",
        "name": "Map Projections and What They Preserve",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "A map projection is a mathematical bargain with the impossible: "
            "the curved Earth cannot be flattened without distortion, so "
            "every projection chooses what to preserve and what to "
            "sacrifice. Conformal projections like Mercator preserve local "
            "angles and shapes - a small circle stays a small circle - which "
            "is why Mercator ruled navigation for four centuries, but they "
            "inflate areas brutally toward the poles. Equal-area projections "
            "like the Albers conic or Mollweide preserve area at the cost of "
            "stretching shapes, which is what thematic maps of population "
            "or crops need. Equidistant projections preserve distances from "
            "one or two points, and compromise projections like Robinson or "
            "Winkel Tripel - the one National Geographic used for decades - "
            "balance all distortions so nothing looks absurd. The famous "
            "classroom shock is Mercator's Greenland: on a Mercator wall map "
            "Greenland looks about the size of Africa, but Africa is more "
            "than fourteen times larger in reality, and the projection "
            "inflated Greenland because area distortion grows with the "
            "square of the secant of latitude. Operational rule: match the "
            "projection to the question - angles for navigation, area for "
            "statistics, compromise for display - and never measure area on "
            "a conformal map."
        ),
        "how_it_works": (
            "A projection is a pair of functions from latitude and longitude "
            "to x and y. Mercator's are the classic example: x equals the "
            "radius times the longitude offset from the central meridian, "
            "and y equals the radius times the natural log of the tangent of "
            "(pi over 4 plus half the latitude). That logarithm is what "
            "stretches the poles to infinity - the map can never show them. "
            "The local scale factor at latitude phi is the secant of phi, "
            "so at 60 degrees north everything is drawn twice as large as "
            "reality in every direction, and area - scale squared - is "
            "inflated fourfold; at 80 degrees the area inflation passes "
            "thirtyfold. Tissot's indicatrix makes this visible: draw a tiny "
            "circle on the globe and watch what the projection does to it - "
            "conformal maps keep it a circle but change its size, equal-area "
            "maps keep its area but stretch it into an ellipse. Modern "
            "software holds hundreds of projections in the PROJ library, and "
            "choosing one is choosing which lie the map will tell: every "
            "projection lies about something, and the professional picks the "
            "lie that does not matter for the task."
        ),
        "key_points": [
            "No flat map preserves everything: conformal keeps angles and shapes, equal-area keeps area, equidistant keeps distances from select points, compromise balances all three.",
            "Mercator's area distortion grows with secant-squared of latitude - Greenland looks Africa-sized though Africa is over fourteen times larger.",
            "Tissot's indicatrix reveals any projection's bargain: watch what happens to a small circle drawn on the globe.",
            "Match the projection to the question: angles for navigation, area for statistics, compromise for general display.",
            "Never measure area on a conformal map or angles on an equal-area map - the projection's sacrificed property is exactly what you would be measuring.",
        ],
        "requirements": [
            "A named projection with its parameters (central meridian, standard parallels, false easting/northing) for every flat dataset.",
            "A stated purpose that justifies the projection choice: navigation, statistics, display, or measurement.",
            "Distortion awareness at the working latitudes: know the scale factor where the work happens.",
            "Area and distance measurements performed in a projection that preserves that property, or computed on the ellipsoid directly.",
            "PROJ-class tooling (or equivalent) for the actual math - hand-rolled projection code is a distortion bug waiting to happen.",
        ],
        "standards": [
            "Projection definitions follow the EPSG registry and are exchanged as WKT2.",
            "Web Mercator (EPSG:3857) is a display projection; measurements on it require ellipsoid math, not planar math.",
            "Equal-area analysis uses an appropriate equal-area projection for the region (e.g., Albers conic for mid-latitude continents).",
        ],
        "citations": [CIT_EPSG, CIT_WKT2, CIT_PROJ],
        "sig_lens": (
            "The Signature read: every map is a testimony, and every "
            "projection swears to tell one truth by admitting which truth "
            "it bends. The Signature Survey Method names the bargain out "
            "loud - this map keeps shapes and sacrifices area - because an "
            "honest witness declares their limits before they speak."
        ),
    },
    {
        "key": "datums_move",
        "name": "Datums: Why Coordinates Move",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Coordinates move even when nothing on the ground does, because "
            "the datum - the reference frame the coordinates are measured "
            "in - is itself attached to a moving planet. Tectonic plates "
            "drift centimeters per year, so a coordinate measured in North "
            "America in 1990 names a point that has since ridden the North "
            "American plate a meter or more from where the numbers say. "
            "Older national datums like NAD27 were fit to one continent and "
            "can disagree with WGS84 by tens of meters; even NAD83, the "
            "modern North American datum, has drifted about two meters from "
            "WGS84 because NAD83 is fixed to the plate while WGS84 follows "
            "the whole Earth. Surveyors handle this with datum epochs - a "
            "coordinate plus the date it was true - and modern frames like "
            "the International Terrestrial Reference Frame publish station "
            "velocities so any coordinate can be propagated to today's date. "
            "The operational rule is blunt: coordinates without a datum "
            "epoch are stale the moment the plate moves, and mixing datums "
            "across a project boundary creates phantom shifts that look "
            "exactly like real ground movement."
        ),
        "how_it_works": (
            "A datum ties coordinates to the Earth through a network of "
            "monumented control stations whose positions are measured to "
            "millimeters. When a new survey ties into those stations, its "
            "coordinates inherit the datum's frame and epoch. Transforming "
            "between datums uses a Helmert transformation - three "
            "translations, three rotations, and a scale factor, the famous "
            "seven parameters - sometimes with time derivatives that carry "
            "plate velocity. The NAD83-to-WGS84 story shows why this "
            "matters: NAD83(2011) epoch 2010.00 coordinates in California "
            "differ from WGS84(G2139) by roughly a meter horizontally, and "
            "the gap grows with time because the plate keeps moving. "
            "Software like PROJ chains these transformations as pipelines - "
            "NAD83 to ITRF at epoch, propagate by velocity to today, then "
            "to WGS84 - so each step's error budget stays visible. "
            "High-accuracy work therefore stamps every coordinate with "
            "frame, epoch, and transformation path; anything less is a "
            "number with an unknown birthday."
        ),
        "key_points": [
            "Tectonic plates move centimeters per year, so coordinates age: a 1990 North American coordinate has ridden the plate a meter or more.",
            "NAD27 can disagree with WGS84 by tens of meters; NAD83 and WGS84 differ by about two meters and the gap grows with time.",
            "Datum transformations use the seven-parameter Helmert model (three translations, three rotations, one scale), sometimes with velocity terms.",
            "Modern frames like ITRF publish station velocities so coordinates carry an epoch and can be propagated to any date.",
            "Coordinates need a frame plus an epoch plus a transformation path - a number with an unknown birthday cannot be trusted at survey grade.",
        ],
        "requirements": [
            "A named datum or reference frame for every coordinate, not just a bare lat/lon pair.",
            "An epoch (date) for survey-grade coordinates in tectonically active regions.",
            "A documented transformation path when converting between datums, with each step's parameters stated.",
            "Plate-velocity awareness for long-lived control: monuments move and the frame must say how fast.",
            "PROJ-class transformation pipelines rather than ad-hoc shifts, so error budgets stay visible per step.",
        ],
        "standards": [
            "WGS84 realizations (G-series) and ITRF realizations are the global frames; national datums document their tie to ITRF.",
            "Datum transformations follow published Helmert parameters with stated epochs.",
            "NAD83 modernizations document epoch 2010.00 coordinates and their relationship to WGS84/ITRF.",
        ],
        "citations": [CIT_WGS84, CIT_PROJ, CIT_EPSG],
        "sig_lens": (
            "The Signature read: the ground itself walks, and an honest "
            "witness says when they saw it. The Signature Survey Method "
            "stamps every coordinate with its epoch the way a testimony "
            "carries its date - because the Earth that swore the oath in "
            "1990 is not standing in the same place today."
        ),
    },
    {
        "key": "crs_epsg",
        "name": "Coordinate Reference Systems and the EPSG Registry",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "A coordinate reference system is the complete contract behind "
            "a coordinate: the datum, the ellipsoid, the projection (if "
            "any), the units, and the axis order, all in one definition. "
            "The EPSG registry - maintained by the IOGP Geomatics Committee "
            "- is the world's agreed catalog of these contracts, where "
            "EPSG:4326 means WGS84 latitude-longitude, EPSG:3857 means Web "
            "Mercator meters, and EPSG:26918 means NAD83 UTM zone 18N. The "
            "registry holds thousands of entries because every country, and "
            "many counties, needed its own best-fit frame before satellites "
            "made global frames practical. Two traps catch nearly everyone. "
            "First, EPSG:4326 is formally latitude-first, longitude-second - "
            "but a generation of software wrote longitude-first, so every "
            "data exchange must state the order or risk plotting points in "
            "the wrong hemisphere. Second, the registry is versioned: "
            "datums get new realizations, and EPSG:4326 today is not "
            "byte-identical to EPSG:4326 from 1995. The modern exchange "
            "format is WKT2, a structured text that spells out every part "
            "of the contract so software stops guessing."
        ),
        "how_it_works": (
            "A CRS definition is built in layers. At the bottom sits the "
            "ellipsoid (semi-major axis and flattening), above it the datum "
            "(which ellipsoid, anchored where and when), above that the "
            "coordinate system (ellipsoidal angles in degrees, or Cartesian "
            "meters east-north-up), and optionally a map projection "
            "converting between them. WKT2 writes this stack as nested "
            "text: GEODCRS for the geographic system, DATUM and ELLIPSOID "
            "inside it, CS and AXIS entries naming latitude then longitude, "
            "and for projected systems a CONVERSION block with the "
            "projection method and parameters. Software like PROJ reads "
            "the WKT2, builds the mathematical pipeline, and transforms "
            "coordinates between any two registered systems - but only if "
            "the definition is complete. A dataset that says 'WGS84' "
            "without saying 4326-vs-3857, or degrees-vs-meters, or "
            "lat-first-vs-lon-first, has handed you half a contract. The "
            "registry's job is to make the other half one lookup away: "
            "cite the EPSG code and the full definition is settled, "
            "versioned, and machine-readable."
        ),
        "key_points": [
            "A CRS is the complete contract: datum, ellipsoid, projection, units, and axis order - the coordinate is meaningless without it.",
            "The EPSG registry catalogs thousands of systems: 4326 is WGS84 lat/lon, 3857 is Web Mercator meters, 26918 is NAD83 UTM 18N.",
            "EPSG:4326 is formally latitude-first, but much software writes longitude-first - state the order at every exchange or risk the wrong hemisphere.",
            "WKT2 is the modern exchange format: structured text spelling out every layer of the contract so software stops guessing.",
            "The registry is versioned - cite the realization and date, because datums get refined and codes evolve.",
        ],
        "requirements": [
            "An EPSG code or full WKT2 definition attached to every dataset, not a bare datum nickname.",
            "Explicit axis order at every handoff: latitude-first per the standard, or a documented longitude-first convention.",
            "Units stated with the CRS: degrees for geographic systems, meters (or feet, where legally required) for projected.",
            "Version awareness: note the datum realization and registry date for long-lived archives.",
            "PROJ-class CRS parsing in software - never hand-roll axis or unit handling.",
        ],
        "standards": [
            "CRS definitions follow the EPSG Geodetic Parameter Dataset and are exchanged as WKT2 per OGC 18-010r7 / ISO 19162.",
            "Axis order follows the registered definition: EPSG:4326 is latitude, longitude.",
            "Transformations between registered systems use published parameters, not local folklore.",
        ],
        "citations": [CIT_EPSG, CIT_WKT2, CIT_PROJ],
        "sig_lens": (
            "The Signature read: a coordinate reference system is the full "
            "oath, written out where all can read it - datum, units, order, "
            "and all. The Signature Survey Method accepts no half-spoken "
            "contracts: cite the code, show the WKT2, and let the registry "
            "settle what the numbers mean."
        ),
    },
    {
        "key": "vector_boundaries",
        "name": "Vector Boundaries: Points, Lines, and Polygons",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Vector data draws the world with three shapes, and nearly "
            "every boundary dispute in geospatial work is a disagreement "
            "about which shape was meant. Points mark discrete locations - "
            "wells, addresses, cell towers. Lines (linestrings) trace "
            "connections and paths - roads, rivers, flight paths - as "
            "ordered sequences of vertices. Polygons enclose areas - "
            "parcels, lakes, counties - as closed rings, with optional "
            "holes for enclaves like a park inside a city block. The OGC "
            "Simple Features standard fixes the vocabulary: Point, "
            "LineString, Polygon, their Multi- versions for scattered "
            "collections, and GeometryCollection for mixed bags. But a "
            "polygon is only as good as its validity: the ring must close "
            "(first point equals last), must not cross itself, holes must "
            "sit fully inside the outer ring, and rings must not touch in "
            "ways that confuse inside from outside. Invalid polygons are "
            "the number-one cause of spatial joins that silently return "
            "wrong answers, so professional pipelines validate geometry on "
            "ingest and repair or reject what fails."
        ),
        "how_it_works": (
            "A polygon answers 'inside or outside' with the ray-casting "
            "rule: draw a ray from the test point in any direction and "
            "count how many times it crosses the ring - odd means inside, "
            "even means outside. A square from (0,0) to (1,1) contains "
            "(0.5, 0.5) with one crossing and excludes (2, 2) with none. "
            "Validity checking walks the ring testing the OGC rules: the "
            "first and last vertices must be identical, no segment may "
            "cross another except at shared endpoints, spikes (a segment "
            "that goes out and back) are forbidden, and each hole must be "
            "a valid ring fully contained by the exterior. The DE-9IM "
            "model (Egenhofer and Franzosa) formalizes every possible "
            "relationship between two geometries as a nine-character "
            "pattern of interior/boundary/exterior intersections, which is "
            "how databases implement predicates like contains, touches, "
            "crosses, and overlaps with mathematical rigor. Repair tools "
            "fix common sins - unclosed rings get closed, self-intersections "
            "get split - but a bowtie polygon (a figure-eight ring) has no "
            "well-defined inside, and the honest pipeline flags it for a "
            "human rather than guessing."
        ),
        "key_points": [
            "Vector data is three shapes: points for locations, linestrings for paths, polygons for areas - plus Multi- collections of each.",
            "Polygon validity is non-negotiable: rings must close, must not self-cross, and holes must sit fully inside the outer ring.",
            "Ray casting decides inside vs outside: an odd number of ring crossings means inside, even means outside.",
            "The DE-9IM model formalizes every spatial relationship (contains, touches, crosses, overlaps) as an intersection pattern.",
            "Invalid geometry is the top cause of silently wrong spatial joins - validate on ingest, repair or reject what fails.",
        ],
        "requirements": [
            "Geometry typed per OGC Simple Features: Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon, GeometryCollection.",
            "Validity enforced at ingest: closed rings, no self-intersections, proper hole containment.",
            "A repair-or-reject policy for invalid geometry, with bowties and spikes flagged for human review.",
            "Ring orientation documented where consumers care (exterior counterclockwise is the common convention).",
            "Spatial predicates implemented on the DE-9IM model so contains, within, touches, and overlaps mean the same thing everywhere.",
        ],
        "standards": [
            "Geometry types and validity rules follow OGC 06-103r4 Simple Features.",
            "Topological predicates follow the DE-9IM dimensionally-extended nine-intersection model.",
            "Geometries are exchanged as WKT/WKB with the CRS carried alongside.",
        ],
        "citations": [CIT_OGC_SFS, CIT_DE9IM, CIT_WKT2],
        "sig_lens": (
            "The Signature read: a boundary is a sworn line - it declares "
            "what is in and what is out, and a line that crosses itself "
            "swears two oaths at once. The Signature Survey Method admits "
            "only whole, closed, honest rings to the record, and sends the "
            "tangled ones back to be sworn again properly."
        ),
    },
    {
        "key": "terrain_basics",
        "name": "Terrain Basics: Elevation, Slope, and Aspect",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Terrain is the Earth's surface measured as numbers, and the "
            "workhorse representation is the digital elevation model: a "
            "raster grid where every cell holds the ground height at that "
            "spot. From that one grid, two derived surfaces answer most "
            "practical questions. Slope is the steepness - the rate height "
            "changes with horizontal distance, reported in degrees or "
            "percent - and it decides where water runs, where landslides "
            "threaten, and where a road can be built. Aspect is the compass "
            "direction the slope faces, and it decides sun exposure: in the "
            "northern hemisphere a south-facing slope gets far more solar "
            "energy than a north-facing one, which matters for farming, "
            "solar panels, and snowmelt. Both are computed from each cell's "
            "neighbors with Horn's method, the standard 3-by-3 window that "
            "estimates the surface gradient. The honest caveats travel with "
            "the grid: the cell size sets the smallest hill the model can "
            "see, the vertical accuracy (often a meter or several) limits "
            "what slope differences are real, and a DEM of the bare earth "
            "differs from a surface model that includes trees and buildings."
        ),
        "how_it_works": (
            "Horn's method estimates the east-west and north-south gradients "
            "at a cell from its eight neighbors, weighting the edge-adjacent "
            "neighbors twice the corner ones. With cell size c and neighbor "
            "heights, dz/dx = ((z3 + 2*z6 + z9) - (z1 + 2*z4 + z7)) / (8*c) "
            "and dz/dy similarly; slope is the arctangent of the gradient "
            "magnitude, and aspect is the arctangent2 of the gradient "
            "components mapped to compass bearing. A perfect tilted plane "
            "rising 1 meter per 10 meters east gives dz/dx = 0.1, slope = "
            "arctan(0.1) = 5.71 degrees, aspect = 90 degrees (east). Flat "
            "cells get an aspect convention (often -1 or 0) because a level "
            "surface faces no direction - software must handle that case "
            "rather than dividing by zero. Resolution rules everything: a "
            "30-meter DEM smooths away gullies a 1-meter lidar DEM resolves, "
            "so slope from coarse grids systematically understates real "
            "steepness. Bare-earth DEMs (ground returns only) versus digital "
            "surface models (treetops and rooftops included) answer "
            "different questions, and mixing them corrupts flood and "
            "viewshed analysis alike."
        ),
        "key_points": [
            "A digital elevation model is a raster grid of ground heights; slope (steepness) and aspect (facing direction) are derived from each cell's neighbors.",
            "Horn's method estimates the surface gradient with a weighted 3-by-3 window: edge neighbors count double, corners single.",
            "Slope is arctan of the gradient magnitude; aspect is the compass bearing of the downhill direction, undefined on flat ground.",
            "Cell size sets the smallest visible hill - coarse DEMs systematically understate real steepness.",
            "Bare-earth DEMs and surface models (with trees and buildings) answer different questions and must never be mixed silently.",
        ],
        "requirements": [
            "A stated cell size and vertical accuracy for every elevation grid, because both bound what the derivatives can honestly claim.",
            "Slope in documented units: degrees or percent, never ambiguous.",
            "A flat-cell aspect convention (commonly -1) handled explicitly in code.",
            "Bare-earth vs surface-model labeling on every DEM so flood and visibility work uses the right one.",
            "Gradient math on projected (meter) grids, or longitude scaled by cosine of latitude on geographic grids.",
        ],
        "standards": [
            "Slope and aspect follow Horn's 3-by-3 gradient method as the standard estimator.",
            "Elevation vertical datums (e.g., NAVD88, EGM2008 geoid) are stated alongside the horizontal CRS.",
            "Vertical accuracy is reported at 95 percent confidence per NSSDA principles.",
        ],
        "citations": [CIT_HORN, CIT_NSSDA, CIT_GDAL],
        "sig_lens": (
            "The Signature read: terrain is the Earth's own testimony, "
            "written in height - and slope and aspect are the reading of "
            "it. The Signature Survey Method reads the ground the way a "
            "witness reads a face: which way it leans, where it looks, and "
            "what it cannot see at its own resolution."
        ),
    },
    {
        "key": "proximity_queries",
        "name": "Proximity Queries: Near, Within, and K-Nearest",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Proximity is the question 'what is close to here,' and it is "
            "the most-asked question in all of geospatial operations. It "
            "comes in three standard forms. 'Within' asks for everything "
            "inside a distance - all pharmacies within 2 kilometers - which "
            "is a buffer (the region within the distance of a geometry) "
            "tested against candidates. 'Nearest' asks for the single "
            "closest feature, and 'k-nearest' asks for the k closest in "
            "order, the query behind every 'nearest gas station' screen. "
            "The naive implementation measures the distance to every "
            "candidate, which is fine for hundreds of points and hopeless "
            "for hundreds of millions - so production systems filter first "
            "with a spatial index (bounding boxes are cheap to test) and "
            "measure exactly only the survivors. Two subtleties decide "
            "correctness: distance must be computed in the right model "
            "(planar meters for projected data, great-circle or geodesic "
            "for geographic), and 'nearest' in a road network means nearest "
            "by travel, not nearest as the crow flies - the closest "
            "restaurant by straight line can be across an uncrossable river."
        ),
        "how_it_works": (
            "A within-distance query builds the buffer polygon - for a "
            "point, the disc of radius r - and tests candidates against it, "
            "or equivalently tests distance(p, candidate) <= r directly. "
            "The index-assisted version first queries the spatial index for "
            "bounding boxes overlapping the buffer's bounding box, which "
            "eliminates the vast majority of candidates with a few integer "
            "comparisons, then runs the exact distance only on the few that "
            "remain. K-nearest search walks the index in order of increasing "
            "minimum possible distance (best-first traversal of an R-tree), "
            "keeping the k best exact distances found so far and pruning any "
            "index branch whose closest possible point is farther than the "
            "kth best - which guarantees the true k nearest without scanning "
            "everything. On geographic coordinates the exact step uses "
            "haversine or ellipsoidal distance; on projected coordinates it "
            "uses planar distance. Network proximity is a different animal: "
            "it runs Dijkstra from the origin on the road graph and reports "
            "nodes by travel distance, which is why the riverside restaurant "
            "loses to the one with the bridge."
        ),
        "key_points": [
            "Proximity has three forms: within-distance (buffer test), nearest, and k-nearest in ranked order.",
            "Index-first, measure-second is the production pattern: bounding-box filtering eliminates nearly everything before any exact distance runs.",
            "Best-first R-tree traversal with pruning guarantees the true k nearest without scanning the whole dataset.",
            "Distance must match the data family: planar for projected coordinates, great-circle or geodesic for geographic.",
            "Network nearest means nearest by travel - straight-line proximity can name a destination across an uncrossable barrier.",
        ],
        "requirements": [
            "A stated distance model for the query: planar, great-circle, ellipsoidal, or network travel.",
            "A spatial index over the candidate set before the dataset grows past trivial size.",
            "Units declared on the distance threshold - meters, kilometers, miles - never bare numbers.",
            "Tie-breaking rules for k-nearest when candidates sit at equal distance.",
            "A documented choice between straight-line and network proximity, because the answers differ.",
        ],
        "standards": [
            "Within-distance predicates follow the OGC simple-features distance semantics (ST_DWithin in PostGIS).",
            "K-nearest ordering is by the same distance model used for the threshold test.",
            "Results state the distance model so a planar answer is never mistaken for a geodesic one.",
        ],
        "citations": [CIT_OGC_SFS, CIT_POSTGIS, CIT_RTR],
        "sig_lens": (
            "The Signature read: proximity is the testimony of neighbors - "
            "who stands close, who stands closest, and by what road they "
            "would walk to you. The Signature Survey Method asks the "
            "question three honest ways and measures each answer in the "
            "model the ground itself would use."
        ),
    },
    {
        "key": "spatial_joins",
        "name": "Spatial Joins: Points in Polygons at Scale",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "A spatial join matches two datasets by location instead of by "
            "a shared key: which delivery addresses fall inside which sales "
            "territories, which crime reports happened inside which police "
            "precincts, which sensor readings belong to which watershed. "
            "The classic form is points-in-polygons, and its cost is what "
            "makes it an operations problem rather than a trivial loop: a "
            "million points against ten thousand polygons is ten billion "
            "candidate tests if done naively. The professional pipeline "
            "runs in two phases. The filter phase uses a spatial index to "
            "find, for each point, only the polygons whose bounding boxes "
            "contain it - usually a handful. The refine phase runs the "
            "exact point-in-polygon test on those few. Partitioning "
            "strategies carry this to cluster scale: both datasets are cut "
            "into matching spatial tiles so each tile's join runs "
            "independently. The silent killers are invalid polygons (which "
            "make inside/outside undefined), mismatched CRS (joining WGS84 "
            "points against Web Mercator polygons tests nonsense), and "
            "boundary semantics - a point exactly on a precinct border must "
            "have a documented owner, or the counts will never reconcile."
        ),
        "how_it_works": (
            "The two-phase join works because bounding-box tests are "
            "orders of magnitude cheaper than exact geometry tests. Each "
            "polygon's minimum bounding rectangle is stored in the spatial "
            "index; each point probes the index for rectangles containing "
            "it, typically returning zero to a few candidates. Only those "
            "go to the exact ray-casting test, which decides inside vs "
            "outside definitively. For the tiled distributed version, a "
            "global grid (or a partitioner like a quadtree over the data "
            "extent) assigns every point and every polygon - replicated to "
            "each tile its bounding box touches - to tiles, and each tile "
            "runs the two-phase join locally; boundary replication "
            "guarantees no point-polygon pair is missed at a tile edge. "
            "Aggregation then rolls up: count of points per polygon, sum of "
            "a value per territory. Correctness rests on three preconditions "
            "checked before the join runs: both sides in one CRS, all "
            "polygons valid, and a documented boundary rule (contains vs "
            "covers vs intersects) so edge points land deterministically."
        ),
        "key_points": [
            "A spatial join matches datasets by location: the classic form assigns points to their containing polygons.",
            "Two phases make it scale: the index filter finds candidate polygons by bounding box, the refine phase tests exactly only those.",
            "Tiled partitioning carries joins to cluster scale: matching tiles join independently, with boundary replication so edge pairs are never missed.",
            "Invalid polygons make inside/outside undefined - validate before joining, or the counts will never reconcile.",
            "Boundary points need a documented rule (contains vs covers vs intersects); CRS must match on both sides.",
        ],
        "requirements": [
            "One common CRS for both join inputs, verified before the join runs.",
            "Valid polygons on the area side - validity-checked at ingest.",
            "A spatial index on at least the polygon side (both sides at scale).",
            "A stated predicate: contains, covers, intersects, or within - each assigns boundary points differently.",
            "A tiling or partitioning strategy once either side outgrows single-machine memory.",
        ],
        "standards": [
            "Join predicates follow OGC simple-features / DE-9IM semantics so 'contains' means the same thing in every engine.",
            "Point-in-polygon refinement uses the exact ray-casting or winding test, not bounding-box approximation, for final assignment.",
            "Tiled joins document the partitioner and replication rule so results are reproducible across engines.",
        ],
        "citations": [CIT_OGC_SFS, CIT_DE9IM, CIT_POSTGIS],
        "sig_lens": (
            "The Signature read: a spatial join is the census of testimony "
            "- every point sworn into the territory that holds it. The "
            "Signature Survey Method counts each witness once, in exactly "
            "one territory, under one shared oath of coordinates - because "
            "a census that double-counts the border is no census at all."
        ),
    },
    {
        "key": "geohashing",
        "name": "Geohashing: Location as a String",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "A geohash turns a latitude-longitude pair into a short string "
            "like 'dqcjqc' where each added character zooms the location "
            "into a smaller rectangle - a brilliant trick that makes "
            "proximity searchable with plain text indexes. The algorithm "
            "interleaves the bits of latitude and longitude, then encodes "
            "groups of five bits as base-32 characters; neighbors on the "
            "map usually share a prefix, so 'everything near here' becomes "
            "'everything whose geohash starts with these characters,' a "
            "query any database can answer with a string range scan. Cell "
            "sizes shrink predictably: one character covers roughly "
            "5,000 by 5,000 kilometers, five characters about 4.9 by 4.9 "
            "kilometers, seven characters about 153 by 153 meters, and nine "
            "characters under 5 meters. The honest limitations are two: "
            "edge cases where true neighbors sit across a cell boundary and "
            "share no prefix (the fix is to query the eight neighboring "
            "cells too), and the rectangle distortion near the poles where "
            "cells get extremely wide relative to their height. Geohashes "
            "power URL-shortening for maps, proximity caching, and any "
            "system that needs 'nearby' without a spatial database - but "
            "they are an approximation for filtering, never the final "
            "exact distance."
        ),
        "how_it_works": (
            "Encoding starts with the full ranges: latitude -90 to +90, "
            "longitude -180 to +180. Each bit halves one range - first a "
            "longitude bit, then latitude, alternating - choosing the upper "
            "or lower half containing the point and recording 1 or 0. After "
            "enough bits, the interleaved bit string is split into 5-bit "
            "chunks, each mapped through the base-32 alphabet "
            "'0123456789bcdefghjkmnpqrstuvwxyz' (deliberately omitting a, "
            "i, l, o to avoid confusion). Decoding reverses it: each "
            "character restores five bits, the bits re-split into "
            "longitude and latitude halves, and each half narrows its range "
            "to a final interval whose center is the decoded point and "
            "whose width is the cell's uncertainty. A 6-character geohash "
            "carries 30 bits - 15 per axis - resolving to about 1.2 by 0.6 "
            "kilometers. Neighbors are computed by moving the decoded cell "
            "in the eight compass directions at the same precision, which "
            "handles the boundary-crossing cases where prefixes diverge. "
            "The whole scheme needs no tables and no server - just "
            "arithmetic - which is why it spread everywhere from map URLs "
            "to delivery dispatch."
        ),
        "key_points": [
            "A geohash interleaves latitude and longitude bits and encodes them as base-32: each character zooms into a smaller rectangle.",
            "Shared prefixes mean nearby: proximity becomes a string-prefix range scan any database can answer.",
            "Precision is fixed by length: 5 characters is about 5 km, 7 is about 150 m, 9 is under 5 m.",
            "Boundary-crossing neighbors share no prefix - robust queries check the eight neighboring cells as well.",
            "Geohashes filter candidates brilliantly but never replace the exact final distance computation.",
        ],
        "requirements": [
            "A chosen geohash length matched to the use: 5-6 for city-scale buckets, 7-9 for street-scale precision.",
            "Neighbor-cell expansion (the eight surrounding cells) in every proximity query to catch boundary crossings.",
            "Decoding awareness: a geohash names a cell with a center and an uncertainty, not an exact point.",
            "Polar caution: cells distort badly near the poles, where rectangles become extremely wide.",
            "Exact distance as the final arbiter - the geohash is the filter, not the verdict.",
        ],
        "standards": [
            "Geohash follows Niemeyer's base-32 specification with the a/i/l/o-excluding alphabet.",
            "Published cell sizes state the precision length so consumers know the uncertainty.",
            "Geohash-indexed systems document the neighbor-expansion rule used for proximity queries.",
        ],
        "citations": [CIT_GEOHASH, CIT_OGC_SFS, CIT_TOBLER],
        "sig_lens": (
            "The Signature read: a geohash is testimony compressed to a "
            "whisper - each letter a smaller room the witness stands in. "
            "The Signature Survey Method speaks the whisper to find the "
            "neighborhood, then walks the street itself for the exact "
            "door, because a whisper locates but only footsteps confirm."
        ),
    },
    {
        "key": "spatial_indexes",
        "name": "Spatial Indexes: Quadtrees and R-Trees",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "A spatial index is what makes 'find everything near here' "
            "fast, and it works on one insight: testing bounding boxes is "
            "cheap, testing exact geometry is expensive, so organize the "
            "boxes into a tree and prune whole branches that cannot "
            "match. The quadtree recursively divides space itself into "
            "four squares (eight cubes for the octree in 3D), subdividing "
            "only where data is dense - elegant for points, but it indexes "
            "empty space too and struggles with large overlapping objects. "
            "The R-tree, the workhorse of PostGIS and nearly every spatial "
            "database, instead groups the objects: each node holds the "
            "minimum bounding rectangle of its children, leaves hold the "
            "actual geometries, and a query descends only into rectangles "
            "overlapping the search area. Guttman's 1984 R-tree and its "
            "successors (R-star with its forced reinsertion, the packed "
            "Hilbert R-tree for static data) turn million-row spatial "
            "queries from minutes into milliseconds. The operational "
            "choices are: quadtree-family for simple in-memory point "
            "work, R-tree-family for general geometry in databases, and "
            "bulk-loading (Sort-Tile-Recursive packing) whenever the data "
            "is static, because a packed tree queries dramatically faster "
            "than an incrementally built one."
        ),
        "how_it_works": (
            "An R-tree query for 'points within this rectangle' starts at "
            "the root and tests the search rectangle against each child's "
            "bounding rectangle; only children that overlap are descended "
            "into, and whole subtrees are pruned the moment their rectangle "
            "misses. At the leaves, the few surviving candidates get the "
            "exact geometry test. Insertion picks the leaf whose rectangle "
            "needs the least enlargement to hold the new object, splitting "
            "overfull nodes; the R-star variant additionally reinserts a "
            "fraction of entries on overflow, which keeps rectangles tight "
            "and queries fast under updates. A quadtree works differently: "
            "it splits the space, not the objects - a node covering a "
            "square divides into four children when it holds more than the "
            "capacity, and a point query walks down the single chain of "
            "squares containing the point. Range queries visit every node "
            "square overlapping the range. Both structures answer the same "
            "question - which objects could possibly interact with this "
            "region - and both exist to make the expensive exact test rare. "
            "Bulk loading sorts static data along a space-filling curve "
            "and packs leaves bottom-up, producing near-optimal trees "
            "without a single insertion split."
        ),
        "key_points": [
            "Spatial indexes prune by bounding box: whole tree branches are skipped when their rectangle cannot match the query.",
            "Quadtrees subdivide space into four squares where data is dense - simple and elegant for points, weak for large overlapping objects.",
            "R-trees group objects by minimum bounding rectangle and are the workhorse of spatial databases (PostGIS, and most GIS engines).",
            "Bulk-loading static data with Sort-Tile-Recursive packing builds dramatically faster-querying trees than incremental insertion.",
            "The index is the filter, never the verdict: surviving candidates always get the exact geometry test.",
        ],
        "requirements": [
            "An index matched to the workload: R-tree family for general geometry, quadtree family for simple in-memory point sets.",
            "Bulk loading (packed/Hilbert order) for static datasets; R-star behavior for heavy-update workloads.",
            "Bounding rectangles maintained honestly on every insert, update, and delete - a stale rectangle corrupts pruning.",
            "Exact geometry refinement after every index query - the index returns candidates, not answers.",
            "Capacity and split tuning exposed, because node size trades tree depth against per-node test cost.",
        ],
        "standards": [
            "R-tree behavior follows Guttman 1984 with documented variant (R-star, packed) for the implementation in use.",
            "Quadtree implementations follow the Finkel-Bentley subdivision model with stated capacity.",
            "Spatial database indexes expose the two-phase contract: index filter, then exact refinement.",
        ],
        "citations": [CIT_RTR, CIT_QUAD, CIT_POSTGIS],
        "sig_lens": (
            "The Signature read: a spatial index is the usher of testimony "
            "- it waves away the crowds who cannot possibly be witnesses "
            "and brings forward only the few who might. The Signature "
            "Survey Method honors the usher's speed but takes every "
            "survivor's full statement, because pruning is judgment about "
            "possibility, never about truth."
        ),
    },
    {
        "key": "h3_hex_grids",
        "name": "Hexagonal Grids and the H3 Index",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Square grids have an old annoyance: diagonal neighbors are "
            "farther than edge neighbors, so 'nearby' depends on direction. "
            "Hexagonal grids fix this - every neighbor of a hexagon is the "
            "same distance away, and hexagons tile the plane with the "
            "least perimeter per area of any regular tiling. Uber's H3 "
            "index carries this idea onto the whole planet: a discrete "
            "global grid of hexagonal (plus twelve pentagonal) cells in 16 "
            "resolutions, from resolution 0 cells averaging 4.25 million "
            "square kilometers down to resolution 15 cells near one square "
            "meter. Each cell has a 64-bit integer ID that encodes its "
            "resolution, base cell, and digit path down the hierarchy, so "
            "parent, children, and neighbors are pure integer arithmetic - "
            "no geometry needed. H3 powers ride-share dispatch, surge "
            "pricing zones, and movement analytics because 'aggregate "
            "demand by cell' and 'find the k-ring of neighbors' are single "
            "cheap operations. The honest limits: the twelve pentagons per "
            "resolution have only five neighbors and slightly distorted "
            "geometry, cell areas vary modestly with latitude, and hexagons "
            "approximate circles - a k-ring is a hexagonal 'disc,' not a "
            "true radius."
        ),
        "how_it_works": (
            "H3 projects the icosahedron's 122 base cells onto the sphere "
            "with a gnomonic projection per face, then subdivides each "
            "hexagon into seven children (one central, six around) at each "
            "finer resolution - the aperture-7 hierarchy. A cell ID packs "
            "mode bits, 4 bits of resolution, 7 bits of base cell, and 3 "
            "bits per resolution level into 64 bits. Converting a "
            "lat/lon to a cell ID means finding the containing face, "
            "projecting to face coordinates, and walking the digit path; "
            "converting back yields the cell center and boundary. The "
            "k-ring operation returns all cells within k steps - the "
            "hexagonal neighborhood - by walking the grid digits, and "
            "hex distance between two cells is computed on cube "
            "coordinates in constant time. Aggregation is the killer use: "
            "every GPS ping becomes a cell ID, and counting pings per cell "
            "per time bucket is a group-by on integers, which databases do "
            "at enormous speed. Compaction then merges runs of sibling "
            "cells into their parent where the data is uniform, shrinking "
            "storage for sparse regions without losing the dense ones."
        ),
        "key_points": [
            "Hexagons give uniform neighbor distance in all six directions - the property square grids lack on diagonals.",
            "H3 tiles the planet in 16 resolutions, from 4.25M sq km cells down to ~1 sq m, with 64-bit integer cell IDs.",
            "Parent, children, k-ring neighbors, and hex distance are pure integer arithmetic - no geometry engine required.",
            "Aggregation by cell ID is a group-by on integers: the fast path for demand heatmaps, movement analytics, and dispatch zones.",
            "Limits are honest: twelve pentagons per resolution, modest area variation with latitude, and k-rings are hexagonal discs, not true circles.",
        ],
        "requirements": [
            "A chosen resolution matched to the analysis scale: city dispatch at 8-9, street analytics at 10-11, meter work at 13-15.",
            "Pentagon awareness: the twelve pentagonal cells per resolution have five neighbors and distorted shapes.",
            "K-ring results treated as hexagonal neighborhoods, refined by exact distance where true radius matters.",
            "Integer cell IDs stored natively (64-bit) rather than as strings, for aggregation speed.",
            "Latitude-variation disclosure when comparing cell counts across regions as if cells were equal-area.",
        ],
        "standards": [
            "H3 cell IDs follow Uber's H3 specification: mode, resolution, base cell, and digit path bit layout.",
            "Resolution choices document the average cell area so consumers know the spatial precision.",
            "Hex-grid analytics state the grid system and resolution alongside every published count or heatmap.",
        ],
        "citations": [CIT_H3, CIT_TOBLER, CIT_OGC_SFS],
        "sig_lens": (
            "The Signature read: hexagons are the honeycomb of testimony - "
            "every cell equidistant from its kin, none favored by "
            "direction. The Signature Survey Method gathers witnesses by "
            "the honeycomb and counts them honestly, naming the twelve "
            "odd cells out loud rather than pretending the comb is perfect."
        ),
    },
    {
        "key": "dijkstra_routing",
        "name": "Routing Algorithms: Dijkstra on Road Networks",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Every turn-by-turn direction ever computed starts with one "
            "idea from 1959: model the road network as a graph - "
            "intersections are nodes, road segments are edges with travel "
            "costs - and grow the shortest path outward from the origin "
            "like a ripple. Dijkstra's algorithm maintains a frontier of "
            "candidate nodes in a priority queue, always expanding the "
            "unvisited node with the smallest known distance; the first "
            "time the destination leaves the queue, its distance is "
            "provably optimal. It is beautifully simple and completely "
            "general - it works for time, distance, fuel, or any additive "
            "cost - but it explores in all directions equally, which means "
            "a cross-country route settles millions of nodes it will never "
            "use. Real road graphs are directed (one-way streets are "
            "edges that exist in one direction only), carry turn costs and "
            "restrictions as edge-to-edge penalties, and change with "
            "traffic - so production systems run Dijkstra on time-dependent "
            "costs, or use it as the exact core inside faster hierarchical "
            "methods. The algorithm's contract is strict: all edge costs "
            "must be non-negative, or the optimality proof collapses."
        ),
        "how_it_works": (
            "Dijkstra keeps two structures: a distance map (best known "
            "cost to each node, infinity at start) and a priority queue "
            "ordered by that distance. The origin is seeded at distance "
            "zero; repeatedly, the smallest-distance node is popped, and "
            "each outgoing edge relaxes its target - if origin-dist plus "
            "edge cost beats the target's known distance, the target is "
            "updated and pushed. Because edge costs are non-negative, a "
            "popped node's distance can never be improved later, which is "
            "the whole proof: the destination's distance is final the "
            "moment it is popped. With a binary heap the running time is "
            "O((V + E) log V) - fast per node, but continental graphs have "
            "tens of millions of nodes, so a naive query still settles an "
            "enormous disc. One-way streets are simply missing reverse "
            "edges; turn restrictions become expanded-graph edges (node = "
            "arriving via a specific incoming edge) so forbidden turns "
            "have no edge to traverse. Predecessor pointers recorded during "
            "relaxation reconstruct the actual path once the destination "
            "settles."
        ),
        "key_points": [
            "Roads become a directed graph: intersections are nodes, segments are edges with non-negative travel costs.",
            "Dijkstra expands the smallest-known-distance node first from a priority queue; the destination's distance is optimal the moment it is popped.",
            "The contract is strict: non-negative edge costs only - negative costs void the optimality proof.",
            "One-way streets are missing reverse edges; turn restrictions are modeled by expanding nodes to include the arrival edge.",
            "Plain Dijkstra explores in all directions, so continental queries settle millions of unused nodes - the motivation for every faster method.",
        ],
        "requirements": [
            "A routable graph: connected enough that origins reach destinations, with directionality matching the real streets.",
            "Non-negative additive edge costs in stated units: seconds, meters, or a weighted combination.",
            "Turn costs and restrictions modeled explicitly - ignoring them produces illegal routes.",
            "Predecessor tracking so the path itself (not just its cost) is recoverable.",
            "A stated cost model, because 'shortest' by time and 'shortest' by distance are different routes.",
        ],
        "standards": [
            "Shortest-path correctness follows Dijkstra 1959: non-negative weights, priority-queue expansion, settle-on-pop.",
            "Road graphs are directed multigraphs per standard network modeling practice.",
            "Published routes state the cost model (time/distance/energy) and the graph vintage.",
        ],
        "citations": [CIT_DIJKSTRA, CIT_POSTGIS, CIT_GDAL],
        "sig_lens": (
            "The Signature read: Dijkstra's ripple is the honest search - "
            "it refuses to declare any road shortest until every nearer "
            "claim has been examined. The Signature Survey Method walks "
            "the graph the same way: nearest truth first, no shortcuts "
            "past an unexamined witness, the destination sworn only when "
            "the ripple reaches it."
        ),
    },
    {
        "key": "fast_routing",
        "name": "Fast Routing: A-Star and Contraction Hierarchies",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Dijkstra is exact but slow at continental scale, so the "
            "routing world built two great accelerators. A-star (1968) "
            "keeps Dijkstra's machinery but aims it: each node's priority "
            "becomes known-cost plus a heuristic estimate of remaining "
            "cost, typically straight-line distance divided by max speed. "
            "With an admissible heuristic - one that never overestimates - "
            "A-star stays optimal while exploring far fewer nodes, because "
            "the search leans toward the destination instead of rippling "
            "everywhere. Contraction hierarchies (2008) take the opposite "
            "approach: preprocess the graph once by repeatedly removing "
            "('contracting') the least important nodes and adding shortcut "
            "edges that preserve all shortest paths, building a hierarchy "
            "from local streets to highways. A query then runs Dijkstra "
            "upward from both ends through the hierarchy, meeting in the "
            "middle - answering continental routes in milliseconds by "
            "visiting thousands of nodes instead of millions. The price is "
            "preprocessing time and the assumption that the hierarchy "
            "fits the cost function; live traffic forces either "
            "re-customization or hybrid schemes. Together they are why "
            "your phone answers 'route to Chicago' before you finish "
            "lifting your thumb."
        ),
        "how_it_works": (
            "A-star's priority for a node n is f(n) = g(n) + h(n), where "
            "g is the exact cost from the origin and h is the heuristic. "
            "The Euclidean distance divided by the maximum road speed is "
            "the classic admissible heuristic for travel time: no road can "
            "beat straight-line at top speed, so h never overestimates and "
            "optimality holds. The search pops smallest f first, and the "
            "destination is optimal when popped, exactly as in Dijkstra - "
            "but nodes pointing away from the goal get large f values and "
            "are never expanded. Contraction hierarchies preprocess "
            "differently: nodes are ordered by importance (a mix of edge "
            "difference, uniformity, and depth heuristics), then contracted "
            "in that order - when node v is removed, shortcuts are added "
            "between its neighbors wherever the shortest path went through "
            "v, preserving all-pairs shortest paths in the augmented graph. "
            "A query runs bidirectional Dijkstra restricted to edges going "
            "up the hierarchy from the source and from the target; the two "
            "searches meet at the highest-ranked node on the true shortest "
            "path. Customization variants separate the slow topology "
            "preprocessing from the fast metric customization, so new "
            "traffic weights apply in seconds rather than hours."
        ),
        "key_points": [
            "A-star aims Dijkstra with f(n) = g(n) + h(n); an admissible (never-overestimating) heuristic keeps it optimal while exploring far less.",
            "Straight-line distance over max speed is the classic admissible heuristic for travel-time routing.",
            "Contraction hierarchies preprocess once - contracting unimportant nodes into shortcuts - then answer continental queries in milliseconds.",
            "Bidirectional upward search through the hierarchy visits thousands of nodes instead of millions.",
            "Preprocessing assumes a cost function: live traffic needs customization variants that re-weight in seconds.",
        ],
        "requirements": [
            "An admissible heuristic for A-star: provably never overestimating, or optimality is lost.",
            "A node-importance ordering and shortcut set for contraction hierarchies, built from the actual graph topology.",
            "Bidirectional search meeting logic that correctly combines forward and backward distances.",
            "A metric-customization path for time-dependent costs like live traffic.",
            "Fallback to exact Dijkstra where hierarchy assumptions break (e.g., arbitrary cost functions).",
        ],
        "standards": [
            "A-star optimality follows Hart, Nilsson, and Raphael 1968: admissible heuristic, settle-on-pop.",
            "Contraction hierarchies follow Geisberger et al. 2008 with documented ordering and shortcut construction.",
            "Published route times state the graph vintage and whether live traffic was applied.",
        ],
        "citations": [CIT_ASTAR, CIT_CH, CIT_DIJKSTRA],
        "sig_lens": (
            "The Signature read: A-star is the hound that scents the "
            "destination, and contraction hierarchies are the map drawn "
            "before the journey - both honest, both sworn to the same "
            "shortest path. The Signature Survey Method lets the hound "
            "run where the ground is unknown and trusts the drawn map "
            "where the ground has been sworn a thousand times."
        ),
    },
    {
        "key": "map_matching",
        "name": "Map-Matching: Snapping GPS Tracks to Roads",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Raw GPS points jitter: a phone in a downtown canyon reports "
            "positions that wander across sidewalks, through buildings, and "
            "sometimes onto the wrong street entirely. Map-matching is the "
            "discipline of snapping that noisy track onto the actual road "
            "network - deciding which road each point was really on - and "
            "it is what turns a cloud of dots into a drivable route for "
            "navigation, tolling, and fleet analytics. The naive approach "
            "snaps each point to its nearest road, which fails at "
            "intersections, parallel streets, and overpasses where the "
            "nearest road is the wrong level. The professional method is a "
            "Hidden Markov Model (Newson and Krumm, 2009): each GPS point "
            "generates candidate positions on nearby roads (the hidden "
            "states are the true road segments), the emission probability "
            "scores how well a candidate explains the observed point given "
            "GPS noise, and the transition probability scores how "
            "plausibly a driver travels from one candidate to the next "
            "along the network. The Viterbi algorithm then finds the "
            "single most likely sequence of roads through the whole track. "
            "The result respects both the measurements and the physics of "
            "driving - no teleporting across medians, no impossible turns."
        ),
        "how_it_works": (
            "For each observed point, candidates are gathered from road "
            "segments within a search radius (scaled to the GPS noise, often "
            "tens of meters), projected to the nearest point on each "
            "segment. The emission score is typically a zero-mean Gaussian "
            "in the great-circle distance between observation and candidate "
            "- a candidate 5 meters away with 10-meter noise scores far "
            "better than one 40 meters away. The transition score compares "
            "the network distance between consecutive candidates (shortest "
            "path along roads) against the straight-line distance between "
            "the observations: if the car seemingly moved 100 meters but "
            "the road route between candidates is 2 kilometers, that "
            "transition is implausible. Viterbi processes the track left "
            "to right, keeping for each candidate the best total score of "
            "any path ending there, then backtracks from the best final "
            "candidate to recover the winning road sequence. Sparse "
            "sampling (points minutes apart) still works because the "
            "transition model reasons about the network path, not just "
            "adjacency - though tunnels and stacked overpasses remain the "
            "hard cases, resolved with heading, speed, and sometimes "
            "barometric hints."
        ),
        "key_points": [
            "Map-matching snaps noisy GPS tracks onto the road network, turning dot clouds into drivable routes.",
            "Nearest-road snapping fails at intersections, parallel streets, and overpasses - context along the whole track is required.",
            "The Hidden Markov Model treats true road segments as hidden states, GPS noise as emission probability, and network travel as transition probability.",
            "Viterbi decoding finds the single most likely road sequence, respecting both measurements and driving physics.",
            "Sparse tracks still match because transitions reason about network paths; tunnels and stacked roads are the remaining hard cases.",
        ],
        "requirements": [
            "A routable road network with segment geometry accurate to the GPS noise level or better.",
            "A GPS noise model (emission sigma) calibrated to the receiver and environment - urban canyons need wider sigmas.",
            "Candidate search radius scaled to the noise: too small drops the true road, too large drowns Viterbi in candidates.",
            "Network-distance transition scoring, not straight-line, so impossible routes score as impossible.",
            "Heading and speed inputs wherever available to disambiguate parallel and stacked roads.",
        ],
        "standards": [
            "HMM map-matching follows Newson and Krumm 2009: Gaussian emissions, network-distance transitions, Viterbi decoding.",
            "Matched outputs carry per-point confidence so downstream analytics know which snaps were certain.",
            "Evaluation reports match rate against ground-truth trajectories, not just visual plausibility.",
        ],
        "citations": [CIT_MAPMATCH, CIT_GPS, CIT_DIJKSTRA],
        "sig_lens": (
            "The Signature read: raw GPS is a nervous witness, blurting "
            "positions that jitter and lie - map-matching is the "
            "cross-examination that pins each statement to the road it "
            "was really on. The Signature Survey Method hears the whole "
            "testimony before judging any single point, because truth "
            "about a journey lives in the sequence, not the dot."
        ),
    },
    {
        "key": "gps_error_budget",
        "name": "GPS Error Budgets",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "A GPS position is never exact - it is the sum of a true "
            "position plus a stack of independent errors, and an error "
            "budget lists every contributor with its size so the total "
            "uncertainty is honest. The user-equivalent range error (UERE) "
            "bundles the ranging errors: satellite clock and ephemeris "
            "errors (the satellite's advertised position and time being "
            "slightly off), ionospheric delay (the signal slows in the "
            "charged upper atmosphere - the largest single term for "
            "single-frequency receivers, meters in size), tropospheric "
            "delay (the lower atmosphere, decimeters), multipath (signals "
            "bouncing off buildings arriving late - the urban killer), and "
            "receiver noise and resolution (decimeters). These range errors "
            "combine by root-sum-of-squares into the UERE, typically a few "
            "meters for civilian single-frequency service. Then geometry "
            "multiplies it: dilution of precision (DOP) measures how the "
            "satellite constellation's shape amplifies ranging error into "
            "position error - horizontal error is roughly HDOP times UERE, "
            "so an HDOP of 1 with 4-meter UERE means about 4 meters of "
            "horizontal uncertainty, while an HDOP of 5 in a downtown "
            "canyon means 20. Dual-frequency receivers kill most of the "
            "ionosphere term; augmentation systems (WAAS, EGNOS) broadcast "
            "corrections; RTK adds a base station and carrier-phase math "
            "to reach centimeters. The budget is what turns 'the GPS says "
            "here' into 'here, plus or minus this much, for these reasons.'"
        ),
        "how_it_works": (
            "Each UERE component is characterized as a 1-sigma (standard "
            "deviation) range error: clock/ephemeris ~2 m, ionosphere ~4 m "
            "single-frequency (near zero dual-frequency), troposphere ~0.5 "
            "m, multipath ~1 m open sky (much worse downtown), receiver "
            "noise ~0.5 m. Root-sum-of-squares gives UERE = sqrt(sum of "
            "squares) - about 4.7 m for the single-frequency civilian "
            "case. DOP comes from the satellite geometry matrix: with the "
            "line-of-sight unit vectors to each satellite forming matrix "
            "G, (G^T G)^-1's diagonal gives the variance multipliers, and "
            "HDOP = sqrt(d_east + d_north), VDOP = sqrt(d_up), PDOP = "
            "sqrt(d_east + d_north + d_up), TDOP for clock. Horizontal 1-sigma "
            "error = HDOP x UERE; the 95-percent horizontal accuracy is "
            "about 2.45 times that (Rayleigh distribution) - so HDOP 1.2 "
            "with 4.7 m UERE gives ~5.6 m 1-sigma, ~13.8 m at 95 percent. "
            "That factor-of-2.45 is why 'accuracy' numbers without a "
            "confidence level are meaningless. Survey practice therefore "
            "plans observations for low-DOP windows, uses choke-ring or "
            "multipath-resistant antennas, and logs long enough sessions "
            "that averaging beats down the random terms - while the "
            "systematic terms (like unmodeled ionosphere) are attacked with "
            "better receivers and corrections, not more time."
        ),
        "key_points": [
            "UERE bundles ranging errors: clock/ephemeris, ionosphere (largest for single-frequency), troposphere, multipath, receiver noise - combined by root-sum-of-squares.",
            "DOP multiplies ranging error into position error: horizontal error is roughly HDOP times UERE.",
            "Single-frequency civilian UERE is a few meters; dual-frequency, augmentation, and RTK attack the ionosphere and multipath terms to reach decimeters and centimeters.",
            "95-percent horizontal accuracy is about 2.45 times the 1-sigma value - confidence level is part of every honest accuracy claim.",
            "The budget turns 'the GPS says here' into 'here, plus or minus this much, for these documented reasons.'",
        ],
        "requirements": [
            "Every error component listed with its 1-sigma size and its source - no hidden terms.",
            "DOP values logged with the fix, because the same receiver has different accuracy under different skies.",
            "A stated confidence level on every accuracy claim: 1-sigma, 95 percent, or CEP.",
            "Environment-matched terms: open-sky budgets do not apply in urban canyons where multipath dominates.",
            "Correction-source documentation: standalone, SBAS, or RTK - each changes which terms survive.",
        ],
        "standards": [
            "Error budgeting follows Kaplan and Hegarty / Parkinson and Spilker: UERE components, RSS combination, DOP multiplication.",
            "Accuracy is reported at a stated confidence per NSSDA conventions.",
            "DOP is computed from the actual satellite geometry matrix, not assumed.",
        ],
        "citations": [CIT_GPS, CIT_PARKINSON, CIT_NSSDA],
        "sig_lens": (
            "The Signature read: every instrument testifies with a tremor, "
            "and the error budget is the sworn accounting of the tremor - "
            "each source named, each magnitude confessed. The Signature "
            "Survey Method never lets a position testify without its "
            "uncertainty standing beside it, because precision without a "
            "budget is boasting, not measurement."
        ),
    },
    {
        "key": "coordinate_transforms",
        "name": "Coordinate Transformations in Practice",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Data arrives in one coordinate system and the work needs "
            "another, so transformation is the daily plumbing of "
            "geospatial operations. The toolbox has three drawers. "
            "Conversions change the representation inside one datum - "
            "geographic to projected via a map projection, or geocentric "
            "XYZ to latitude-longitude - and are exact mathematics. "
            "Transformations change the datum itself - NAD83 to WGS84, "
            "WGS84 to ETRS89 - and are measured estimates with error "
            "budgets, usually a 7-parameter Helmert (three translations, "
            "three rotations, one scale) plus time evolution for plate "
            "motion. Concatenated operations chain them: a survey in NAD83 "
            "UTM becomes WGS84 geographic by unprojecting, applying the "
            "Helmert with epoch propagation, and stopping - never "
            "projecting again unless the target needs it. The classic "
            "production traps are axis order (lat-first vs lon-first "
            "silently swapping hemispheres), applying a transformation "
            "twice, using a datum shift outside its valid area, and "
            "treating a 3-parameter (translation-only) shift as good enough "
            "where rotations matter. Modern practice expresses the whole "
            "chain as a PROJ pipeline - a single auditable string of "
            "named steps - so the transformation is data, not folklore."
        ),
        "how_it_works": (
            "A Helmert transformation maps source coordinates X to target "
            "X' = T + (1 + s) * R * X, where T is the translation vector "
            "in meters, s the scale in parts per million, and R the "
            "rotation matrix built from three small angles (arcseconds). "
            "For small angles R is linearized, and a typical continental "
            "datum shift moves points by meters - for example a translation "
            "of (1.0, -1.5, 0.8) meters plus sub-arcsecond rotations. "
            "Time-dependent versions add velocities: X(t) = X(t0) + V * "
            "(t - t0), propagating the frame to the observation epoch. "
            "PROJ pipelines compose steps textually, e.g. convert UTM to "
            "geographic, apply the Helmert, change units - each step a "
            "named operation with parameters, executed in order, with "
            "inverse available by reversing the chain. Accuracy metadata "
            "rides along: PROJ records the stated accuracy of each "
            "transformation step (often 1-2 m for continental Helmerts, "
            "centimeters for local grid shifts like NADCON), so the "
            "pipeline's total error budget is the RSS of its steps. Grid-"
            "based transformations (NADCON, NTv2) replace formulas with "
            "interpolated shift tables for sub-meter local accuracy where "
            "the datum distortion is irregular."
        ),
        "key_points": [
            "Conversions change representation within one datum (exact math); transformations change the datum itself (measured estimates with error budgets).",
            "The 7-parameter Helmert - three translations, three rotations, one scale - is the standard datum-shift model, extended with velocities for plate motion.",
            "PROJ pipelines express the whole chain as auditable named steps, with inverses by reversal.",
            "Grid-shift tables (NADCON, NTv2) beat formulas where datum distortion is locally irregular.",
            "Classic traps: axis-order swaps, double-applying a shift, using a shift outside its valid area, and translation-only models where rotation matters.",
        ],
        "requirements": [
            "Source and target CRS fully specified (EPSG/WKT2) before any math runs.",
            "Helmert parameters with their epoch and stated accuracy - a shift without an accuracy is a guess.",
            "Time propagation for frames with plate velocity when epochs differ by years.",
            "Axis-order verification at both ends of the pipeline.",
            "Grid files versioned and local: transformations are only valid inside their documented area.",
        ],
        "standards": [
            "Datum transformations use published Helmert parameters with epochs, per geodetic authority publications.",
            "Pipelines follow PROJ conventions so the operation chain is portable and auditable.",
            "Transformation accuracy is stated per step and combined by RSS for the total budget.",
        ],
        "citations": [CIT_PROJ, CIT_EPSG, CIT_WGS84],
        "sig_lens": (
            "The Signature read: transformation is translation of testimony "
            "- the same witness speaking in another courtroom's language. "
            "The Signature Survey Method translates word by word, on the "
            "record, with each step's accuracy sworn aloud - because a "
            "translation that hides its losses is not translation but "
            "rumor."
        ),
    },
    {
        "key": "raster_operations",
        "name": "Raster Operations: Map Algebra and Zonal Statistics",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Where vector data draws boundaries, raster data paints "
            "surfaces - grids of cells covering continuous phenomena like "
            "elevation, temperature, rainfall, or satellite reflectance. "
            "Map algebra is the arithmetic of these grids: add, subtract, "
            "multiply, and apply functions cell by cell across perfectly "
            "aligned rasters. Its most famous product is the Normalized "
            "Difference Vegetation Index - (NIR - Red) / (NIR + Red) - which "
            "turns two satellite bands into a -1 to +1 map where healthy "
            "vegetation glows near +0.8 and bare soil hovers near zero. "
            "Focal operations look at neighborhoods: a 3-by-3 mean smooths "
            "noise, a gradient filter finds edges. Zonal operations flip "
            "the question: given zone polygons (counties, watersheds) and "
            "a value raster (rainfall), compute per-zone statistics - mean, "
            "min, max, sum - the operation behind every 'average rainfall "
            "by county' map. The discipline's iron rule is alignment: map "
            "algebra on misaligned grids (different cell sizes, offsets, "
            "or projections) silently computes garbage, so professional "
            "pipelines resample to a common grid first and document the "
            "resampling method, because nearest-neighbor and bilinear give "
            "different answers."
        ),
        "how_it_works": (
            "Local map algebra walks the grids in lockstep: for each cell "
            "position, read the values from every input raster, apply the "
            "expression, write the output cell. NDVI's formula normalizes "
            "the difference by the sum, which cancels most illumination "
            "variation - a sunlit and a shadowed patch of the same crop "
            "give nearly the same index. Focal operations center a kernel "
            "on each cell: the 3-by-3 mean replaces each cell with its "
            "neighborhood average (smoothing), while Sobel-style kernels "
            "estimate gradients (edge detection). Zonal statistics invert "
            "the loop: rasterize each zone polygon onto the value grid, "
            "then accumulate per-zone sums and counts in a single pass - "
            "mean = sum/count, with min/max tracked alongside. NoData "
            "handling is the quiet correctness issue: a NoData cell must "
            "propagate as unknown through local math (never as zero) and "
            "be excluded from zonal counts, or deserts will average in as "
            "seas of zero. Resampling to the common grid happens before "
            "any of this: categorical rasters (land cover classes) use "
            "nearest-neighbor to avoid inventing classes, continuous "
            "rasters (elevation) use bilinear or cubic for smoothness."
        ),
        "key_points": [
            "Map algebra computes cell-by-cell across aligned rasters: NDVI = (NIR - Red)/(NIR + Red) maps vegetation health from -1 to +1.",
            "Focal operations use neighborhoods: mean kernels smooth, gradient kernels find edges.",
            "Zonal statistics aggregate value rasters by zone polygons - mean rainfall per county in a single pass.",
            "NoData must propagate as unknown through math and be excluded from zonal counts - never silently treated as zero.",
            "Alignment is the iron rule: resample to a common grid first, with nearest-neighbor for categories and bilinear/cubic for continuous fields.",
        ],
        "requirements": [
            "A common grid (extent, cell size, projection, alignment) for all inputs before any algebra runs.",
            "Documented resampling per raster type: nearest-neighbor for categorical, bilinear/cubic for continuous.",
            "Explicit NoData value with propagate-as-unknown semantics in every operation.",
            "Zonal polygons in the same CRS as the value raster, validated before rasterization.",
            "Output metadata recording the expression, inputs, and resampling so the map is reproducible.",
        ],
        "standards": [
            "Map algebra follows the Tomlin cartographic-modeling framework: local, focal, zonal, and global operators.",
            "NoData semantics follow GDAL conventions: unknown propagates, and is excluded from statistics.",
            "Published raster derivatives document source grids, resampling method, and the exact expression.",
        ],
        "citations": [CIT_GDAL, CIT_OGC_SFS, CIT_ISO19115],
        "sig_lens": (
            "The Signature read: rasters are testimony given by the whole "
            "landscape at once - every cell a witness, every zone a jury "
            "summing the evidence. The Signature Survey Method aligns the "
            "witnesses before hearing them and lets the silent cells stay "
            "silent, because a grid that invents answers is perjury by "
            "arithmetic."
        ),
    },
    {
        "key": "isochrones",
        "name": "Isochrones and Service Areas",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "An isochrone is a line of equal travel time - every point "
            "reachable within 15 minutes from here - and the area inside "
            "it is the service area. It is the honest answer to 'what can "
            "I reach,' replacing the lie of the perfect circle: a "
            "15-minute circle ignores rivers, highways, and one-way "
            "mazes, while a true isochrone bulges along fast arterials "
            "and pinches at barriers. Emergency planners draw them around "
            "fire stations to prove coverage; retailers draw them around "
            "sites to count reachable customers; transit agencies draw "
            "them around stops including the walk to the stop. Computation "
            "runs Dijkstra (or its faster cousins) from the origin on the "
            "network, recording each node's travel time, then extracts the "
            "boundary where time crosses the threshold - on road networks "
            "this means interpolating along edges, because the 15-minute "
            "mark usually falls mid-segment. Multimodal isochrones chain "
            "networks: walk to transit, ride, walk again, with schedule "
            "timetables making the answer time-of-day dependent. The "
            "polygon that results is only as honest as its network, speeds, "
            "and departure time - an isochrone without those three stated "
            "is decoration."
        ),
        "how_it_works": (
            "The network isochrone starts with a shortest-path tree from "
            "the origin: Dijkstra settles nodes in order of travel time, "
            "and every node records its arrival time. All edges are then "
            "classified: fully inside (both endpoints under the limit), "
            "fully outside (both over), or cut by the threshold - for cut "
            "edges the crossing point is interpolated by the fraction "
            "(limit - t_near)/(t_far - t_near) along the segment. The "
            "crossing points plus the fully-inside geometry form the raw "
            "reachable set; buffering and dissolving turns it into clean "
            "polygons, often with holes where barriers (rivers, rail yards) "
            "punch through. Grid-based variants rasterize instead: each "
            "cell gets its shortest travel time and the isochrone is the "
            "contour at the limit - simpler with multimodal costs, "
            "coarser at boundaries. Time-dependent versions run the "
            "shortest-path computation against timetable edges (a bus that "
            "leaves at 08:14), producing different polygons for 8 AM and "
            "midnight. Quality control compares the polygon's area and "
            "shape against known barriers: an isochrone that crosses an "
            "uncrossable river indicts the network data, not the algorithm."
        ),
        "key_points": [
            "An isochrone is the equal-travel-time boundary; the service area inside is the honest answer to 'what can I reach.'",
            "True isochrones bulge along arterials and pinch at barriers - the perfect circle is the lie they replace.",
            "Computation runs shortest-path from the origin, then interpolates the threshold crossing along cut edges.",
            "Multimodal isochrones chain walk, transit timetables, and walking again - making the answer time-of-day dependent.",
            "Every isochrone must state its network, speeds, and departure time, or it is decoration.",
        ],
        "requirements": [
            "A routable network with realistic speeds per road class - isochrones on speed-limit fantasy mislead.",
            "A stated departure time and cost model: time-of-day changes transit-inclusive answers completely.",
            "Threshold interpolation along edges, not just node classification, for honest boundaries.",
            "Barrier checking: the polygon must respect rivers, rail lines, and other uncrossable features in the data.",
            "Mode documentation: driving, walking, transit, or chained multimodal - each draws a different map.",
        ],
        "standards": [
            "Network isochrones derive from shortest-path trees per Dijkstra 1959 or faster exact equivalents.",
            "Published service areas state network vintage, speed model, departure time, and mode.",
            "Multimodal results follow timetable-based routing practice with the schedule vintage stated.",
        ],
        "citations": [CIT_DIJKSTRA, CIT_CH, CIT_OGC_SFS],
        "sig_lens": (
            "The Signature read: an isochrone is the sworn reach of a "
            "place - how far its help, its customers, its engines can "
            "honestly travel in the allotted minutes. The Signature "
            "Survey Method draws the reach along real roads at real "
            "speeds, and where the polygon crosses an uncrossable river "
            "it indicts the map, never the traveler."
        ),
    },
    {
        "key": "geofencing",
        "name": "Geofencing: Enter, Dwell, and Exit",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "A geofence is a virtual boundary that watches real movement: "
            "when a tracked phone, vehicle, or asset crosses into a zone, "
            "the system fires an enter event; when it leaves, an exit "
            "event. Logistics companies fence depots to timestamp arrivals "
            "automatically; retailers fence stores to count visits; "
            "parents fence the neighborhood to know the kids got home. The "
            "engineering problem is that positions jitter and update "
            "irregularly, so a naive inside/outside test at each fix "
            "flickers - enter, exit, enter - when the target lingers near "
            "the boundary. Professional geofencing adds hysteresis: separate "
            "enter and exit thresholds (enter at the fence, exit only "
            "after leaving by a margin, or after a time delay), plus dwell "
            "detection that requires the target to remain inside for a "
            "minimum duration before the visit counts. Polygon fences need "
            "the same validity discipline as any polygon work; circular "
            "fences need their radius in honest meters with the distance "
            "model stated. And because location is sensitive, every "
            "geofencing deployment carries a privacy duty: collect the "
            "minimum positions needed, process on-device where possible, "
            "and get consent before watching anyone."
        ),
        "how_it_works": (
            "Each incoming position is tested against the fence geometry - "
            "point-in-polygon for polygonal fences, distance <= radius for "
            "circular ones - producing a raw inside/outside state. The "
            "state machine then applies hysteresis: the state flips to "
            "inside only when the raw test says inside, but flips back to "
            "outside only when the target is outside by the exit margin "
            "(or the raw outside persists for the exit delay). This kills "
            "boundary flicker: a GPS point wandering 10 meters across a "
            "fence line no longer generates a storm of events. Dwell logic "
            "adds a timer: an enter event fires immediately (or after a "
            "short confirm delay), but the visit is only confirmed after "
            "continuous inside-time exceeds the dwell threshold - drive-bys "
            "past the store never count as visits. Between fixes, "
            "interpolation decides crossings: if fix A is inside and fix B "
            "(five minutes later) is outside, the exit is timestamped by "
            "interpolating the segment-boundary intersection, with a "
            "confidence that degrades as the gap grows. High-rate, "
            "battery-hungry tracking gives crisp events; adaptive sampling "
            "(fast near fences, slow far away, driven by distance to the "
            "nearest fence) gives nearly the same events at a fraction of "
            "the power."
        ),
        "key_points": [
            "Geofencing fires enter/dwell/exit events when tracked targets cross virtual boundaries - depots, stores, neighborhoods.",
            "Raw inside/outside tests flicker at boundaries; hysteresis (separate enter/exit thresholds or delays) makes events stable.",
            "Dwell detection requires minimum continuous inside-time before a visit counts - drive-bys never become visits.",
            "Crossings between sparse fixes are interpolated along the segment, with confidence degrading as the gap grows.",
            "Adaptive sampling (fast near fences, slow far away) preserves event quality at a fraction of the battery cost.",
        ],
        "requirements": [
            "Valid fence geometry: closed honest polygons or circles with radius in stated meters and distance model.",
            "Hysteresis parameters documented: exit margin or delay, chosen against the positioning noise.",
            "Dwell thresholds matched to the use: seconds for security, minutes for visit analytics.",
            "Interpolation policy for sparse fixes, with confidence attached to interpolated crossings.",
            "Privacy design: minimum necessary collection, on-device processing where possible, consent before tracking people.",
        ],
        "standards": [
            "Inside/outside tests follow OGC simple-features predicates on valid geometry.",
            "Event streams document fence geometry version, hysteresis, and dwell parameters so counts are reproducible.",
            "Human tracking follows consent and data-minimization practice.",
        ],
        "citations": [CIT_OGC_SFS, CIT_GPS, CIT_ISO19115],
        "sig_lens": (
            "The Signature read: a geofence is a sworn perimeter - the "
            "line that testifies when the watched one comes and goes. "
            "The Signature Survey Method guards the perimeter against "
            "jitter-lies with hysteresis and against drive-by rumors "
            "with dwell, and it never watches a person without their "
            "knowing consent - for a perimeter without consent is not "
            "operations but surveillance."
        ),
    },
    {
        "key": "location_uncertainty",
        "name": "Location Uncertainty: Error Ellipses and Confidence Regions",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "A position without an uncertainty region is a claim without a "
            "margin, and the error ellipse is the standard way to draw the "
            "margin. When a GPS receiver (or any estimator) reports a "
            "position, it really holds a probability cloud described by a "
            "covariance matrix: how much the easting varies, how much the "
            "northing varies, and how the two vary together. The error "
            "ellipse is the contour of constant probability density of "
            "that cloud - its axes point along the directions of maximum "
            "and minimum uncertainty, with lengths set by the eigenvalues "
            "of the covariance and scaled to the desired confidence. A "
            "1-sigma ellipse contains the true position about 39 percent "
            "of the time in two dimensions (not 68 - that is the 1D "
            "number); the 95-percent ellipse is scaled by 2.4477 and is the "
            "honest reporting shape. The ellipse's tilt tells its own "
            "story: a long thin ellipse along the street means the "
            "position is well known across the street but poorly known "
            "along it - classic urban-canyon geometry where satellites "
            "line up overhead. Circular error probable (CEP), the radius "
            "containing 50 percent of fixes, is the military-flavored "
            "single number; the ellipse is the full truth. Operations "
            "that ignore the ellipse - snapping a jittery fix to the "
            "nearest building, drawing a fence tighter than the noise - "
            "manufacture false precision and then act on it."
        ),
        "how_it_works": (
            "The 2-by-2 covariance matrix [[s_ee, s_en], [s_en, s_nn]] is "
            "diagonalized in closed form: the eigenvalues are "
            "(s_ee + s_nn)/2 +/- sqrt(((s_ee - s_nn)/2)^2 + s_en^2), and "
            "the eigenvectors give the axis directions, with the tilt "
            "angle theta = 0.5 * atan2(2*s_en, s_ee - s_nn). The 1-sigma "
            "semi-axes are sqrt(lambda_max) and sqrt(lambda_min); scaling "
            "by k gives the k-sigma ellipse, with k = 2.4477 for 95 "
            "percent (the chi-square 2-DOF value) and k = 1 for the "
            "39.35-percent standard ellipse. A receiver reporting east "
            "variance 25 m^2, north variance 9 m^2, and zero covariance "
            "has 1-sigma axes of 5 m and 3 m, and a 95-percent ellipse of "
            "12.2 by 7.3 m - the honest footprint of that fix. When east "
            "and north errors correlate (s_en nonzero), the ellipse "
            "rotates, capturing directional knowledge the circular "
            "approximation throws away. Downstream operations consume the "
            "ellipse, not the point: map-matching weights candidates by "
            "it, geofences set hysteresis from it, and sensor fusion "
            "treats it as the measurement's vote in the Kalman update. "
            "Storing the full covariance - not just a single 'accuracy' "
            "number - is what makes all of that possible."
        ),
        "key_points": [
            "The error ellipse is the contour of the position's probability cloud: axes from the covariance eigenvalues, scaled to the confidence level.",
            "A 1-sigma 2D ellipse holds the truth only ~39 percent of the time; the 95-percent ellipse scales by 2.4477.",
            "The ellipse's tilt and elongation tell the geometry story - long thin ellipses mean satellites lined up and knowledge is directional.",
            "CEP (50-percent radius) is a single number; the ellipse is the full truth - operations should consume the ellipse.",
            "Acting on the point while ignoring the ellipse manufactures false precision: fences tighter than noise, snaps to wrong buildings.",
        ],
        "requirements": [
            "The full 2-by-2 covariance (or equivalent) stored with the position - a single accuracy number discards direction.",
            "A stated confidence scale on every reported ellipse: 1-sigma, 95 percent, or CEP - never an unlabeled shape.",
            "Closed-form eigen-decomposition for the 2D case, documented so tilt and axes are reproducible.",
            "Downstream consumers (matching, fencing, fusion) fed the ellipse, not just the center point.",
            "Correlation terms kept: zeroing the off-diagonal silently circularizes directional knowledge.",
        ],
        "standards": [
            "Uncertainty regions follow the covariance-ellipse convention with chi-square 2-DOF scaling (2.4477 at 95 percent).",
            "Accuracy claims state the confidence level per NSSDA/ASPRS practice.",
            "Covariance is exchanged alongside positions in estimation and fusion interfaces.",
        ],
        "citations": [CIT_GPS, CIT_KALMAN, CIT_NSSDA],
        "sig_lens": (
            "The Signature read: the error ellipse is the honest shadow "
            "of every measurement - the region where the truth might "
            "stand, drawn to scale. The Signature Survey Method never "
            "trims the shadow to flatter the point, for a witness who "
            "hides their uncertainty testifies falsely about their "
            "certainty."
        ),
    },
    {
        "key": "kalman_filtering",
        "name": "Kalman Filtering for Moving Positions",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "A moving target is never where its last measurement said: "
            "the measurement is noisy and the target kept moving. The "
            "Kalman filter (1960) is the optimal way to fuse a motion "
            "model with noisy measurements - it keeps a running estimate "
            "of position and velocity plus their uncertainty, predicts "
            "forward with the physics, then corrects with each new "
            "measurement, weighting prediction against measurement by "
            "their relative uncertainties. When GPS is good, the filter "
            "trusts it; when the signal drops in a tunnel, the filter "
            "coasts on the motion model, its uncertainty growing honestly "
            "until the next fix arrives. Every phone's blue dot, every "
            "drone's hover hold, every fleet tracker runs some descendant "
            "of this filter. The linear Kalman filter is provably optimal "
            "for linear systems with Gaussian noise; the extended Kalman "
            "filter linearizes mildly nonlinear ones (the industry "
            "workhorse for GPS/INS fusion); the unscented variant handles "
            "stronger nonlinearity without Jacobians. The filter's "
            "contract is that its noise models are honest - feed it "
            "understated measurement noise and it will trust bad fixes "
            "and diverge with total confidence."
        ),
        "how_it_works": (
            "Each cycle has two steps. Predict: x_pred = F * x, P_pred = "
            "F * P * F^T + Q, where F encodes the motion model (position += "
            "velocity * dt), P is the estimate covariance, and Q is the "
            "process noise - how much the true motion can surprise the "
            "model. Update: K = P_pred * H^T * (H * P_pred * H^T + R)^-1 "
            "is the Kalman gain, x = x_pred + K * (z - H * x_pred) corrects "
            "the estimate toward the measurement z, and P = (I - K * H) * "
            "P_pred shrinks the uncertainty. The gain is the whole art: "
            "large R (noisy measurement) makes K small and the filter "
            "leans on prediction; small R makes K large and the estimate "
            "jumps to the measurement. A 1D constant-velocity tracker "
            "with dt = 1 s, process noise modest, and measurement noise "
            "25 m^2 converges within a handful of fixes to track a target "
            "moving 10 m/s, its velocity estimate settling as the "
            "position history accumulates. Tuning is empirical: Q from "
            "the target's agility (a walking person vs a race car), R "
            "from the sensor's error budget, and consistency checked by "
            "the normalized innovation squared - which must match its "
            "chi-square statistics, or the models are lying."
        ),
        "key_points": [
            "The Kalman filter fuses a motion model with noisy measurements: predict with physics, correct with data, weighted by relative uncertainty.",
            "The Kalman gain is the whole art: noisy measurements get small gains (trust prediction), clean ones get large gains (trust the fix).",
            "Linear systems with Gaussian noise get the optimal linear filter; extended and unscented variants handle nonlinear reality.",
            "Through signal outages the filter coasts on the model with honestly growing uncertainty - then snaps back on reacquisition.",
            "Honest noise models are the contract: understated R makes the filter trust bad fixes and diverge confidently.",
        ],
        "requirements": [
            "A motion model matched to the target: constant-velocity for cruise, coordinated-turn for maneuvering.",
            "Process noise Q from the target's real agility; measurement noise R from the sensor's real error budget.",
            "Time-stamped measurements with correct dt in the prediction - clock errors become motion errors.",
            "Consistency monitoring via normalized innovation squared against chi-square statistics.",
            "A named variant (linear, extended, unscented) with its linearization assumptions documented.",
        ],
        "standards": [
            "Filter equations follow Kalman 1960 with the standard predict/update, gain, and covariance forms.",
            "Noise models are documented and validated, not tuned until the plot looks nice.",
            "Fusion outputs carry the estimate covariance so downstream consumers inherit the uncertainty.",
        ],
        "citations": [CIT_KALMAN, CIT_GPS, CIT_GOODCHILD],
        "sig_lens": (
            "The Signature read: the Kalman filter is the wise judge - "
            "hearing the model and the measurement both, believing each "
            "exactly as much as its record deserves. The Signature "
            "Survey Method sets the weights by honest history, never by "
            "hope, for a judge who trusts a lying witness is no judge at "
            "all."
        ),
    },
    {
        "key": "spatial_query_scale",
        "name": "Spatial Query Patterns at Scale",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "A spatial query that answers in milliseconds on ten thousand "
            "rows can take hours on ten billion - unless the data is "
            "organized for the question. Scale brings three patterns. "
            "Partitioning cuts the dataset into spatial tiles (uniform "
            "grid, quadtree, or geohash cells) so each query touches only "
            "the tiles it overlaps; the tile index is small enough to "
            "live in memory while the tiles themselves rest in cheap "
            "storage. Two-level indexing puts a coarse global index over "
            "tile extents and a fine R-tree inside each tile, so the "
            "planner prunes at both levels. And predicate pushdown moves "
            "the spatial test to the storage: columnar formats with "
            "per-block bounding boxes (GeoParquet's bbox metadata) let the "
            "reader skip entire blocks without decompressing them. The "
            "classic failure is skew - a uniform grid over a city puts "
            "Manhattan and an empty ocean in equal tiles, so adaptive "
            "partitioners (quadtree, k-d splits on data) balance by count, "
            "not by area. The second failure is the global shuffle: a "
            "spatial join across tiles without replication or a "
            "shared-nothing-aware partitioner moves the whole dataset "
            "across the network. Professionals therefore co-partition join "
            "inputs on the same grid and replicate boundary-straddling "
            "objects, making the common queries embarrassingly parallel."
        ),
        "how_it_works": (
            "A tiled range query works like this: the query rectangle is "
            "mapped to the set of overlapping tiles via the tile index "
            "(an in-memory map from tile key to storage location); each "
            "tile's local R-tree returns candidates; exact tests refine "
            "them; results merge. If the query covers 3 of 10,000 tiles, "
            "the system reads 0.03 percent of the data - that ratio is "
            "the entire performance story. GeoParquet sharpens the "
            "storage layer: each row-group stores its bbox, and the "
            "reader evaluates the query rectangle against those boxes "
            "before touching any geometry bytes, routinely skipping "
            "90-plus percent of a file. For joins, both inputs are "
            "partitioned on the same scheme (say, geohash-6 cells); "
            "polygons straddling boundaries are replicated to each "
            "touched cell; each cell joins locally with zero network "
            "traffic. Skew control splits hot cells: when a cell exceeds "
            "its row budget it subdivides (quadtree-style) or its data "
            "spills to more workers. The query planner's cost model "
            "knows all this - it estimates selectivity from tile "
            "histograms and chooses the tile set before reading a single "
            "geometry."
        ),
        "key_points": [
            "Partition into spatial tiles so each query reads only the tiles it overlaps - the read ratio is the whole performance story.",
            "Two-level indexing (coarse tile index, fine per-tile R-tree) prunes at both levels.",
            "Predicate pushdown with per-block bounding boxes (GeoParquet) skips most storage without decompressing it.",
            "Adaptive partitioners balance by row count, not area - uniform grids die of skew over cities vs oceans.",
            "Co-partition join inputs on the same grid and replicate boundary objects to keep joins embarrassingly parallel.",
        ],
        "requirements": [
            "A partitioning scheme chosen for the data distribution: adaptive (quadtree/geohash) for skewed data, uniform only for uniform data.",
            "Tile extents indexed in memory while tile contents stay in cheap storage.",
            "Per-block bounding-box metadata on columnar stores for predicate pushdown.",
            "Boundary replication policy for joins so straddling objects are never missed.",
            "Skew monitoring with split thresholds - hot tiles must subdivide before they bottleneck.",
        ],
        "standards": [
            "Cloud-native geospatial formats (GeoParquet, Cloud-Optimized GeoTIFF) carry bbox metadata per block/tile.",
            "Tiled query semantics preserve exactness: partitioning is an optimization, never an approximation.",
            "Partitioners and replication rules are documented so distributed results are reproducible.",
        ],
        "citations": [CIT_RTR, CIT_GDAL, CIT_POSTGIS],
        "sig_lens": (
            "The Signature read: scale is the census of a nation of "
            "witnesses - no single clerk can hear them all, so the "
            "testimony is divided by district and each district heard in "
            "parallel. The Signature Survey Method draws the districts "
            "by where the people actually are, and posts the boundary "
            "watchers so no witness standing on a line is ever unheard."
        ),
    },
    {
        "key": "viewshed_watershed",
        "name": "Terrain Analysis: Viewsheds and Watersheds",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Two questions dominate applied terrain analysis: what can be "
            "seen from here, and where does the water go. A viewshed is "
            "the set of terrain cells visible from an observer point - "
            "the foundation of cell-tower placement, scenic-impact "
            "studies, and watchtower siting. It is computed by casting "
            "lines of sight across the elevation grid: a target cell is "
            "visible if no intermediate cell rises above the sight line, "
            "with Earth curvature and atmospheric refraction corrections "
            "for long distances. A watershed (drainage basin) is the area "
            "draining to a common outlet, derived by routing flow downhill "
            "from cell to cell: each cell's flow direction points to its "
            "lowest neighbor (the D8 method picks among eight), cells are "
            "processed in descending elevation order accumulating "
            "upstream counts, and the pour point's upstream set is its "
            "watershed. Both analyses are brutally sensitive to DEM "
            "quality: a viewshed on a surface model sees over trees that "
            "a bare-earth model correctly blocks, and watershed "
            "delineation fails wherever the DEM has pits - spurious "
            "depressions that trap flow - so professional pipelines fill "
            "or breach depressions first and document which. Resolution "
            "rules both: a 30-meter DEM cannot see a hedgerow that blocks "
            "a real view or a ditch that redirects real water."
        ),
        "how_it_works": (
            "Line-of-sight testing walks the raster profile between "
            "observer and target: at each step the terrain height is "
            "compared against the sight-line height interpolated between "
            "observer eye height and target height. If any terrain sample "
            "exceeds the line, the target is hidden; the maximum excess "
            "angle over all steps also yields the horizon. Efficient "
            "viewsheds sweep radially, maintaining the maximum sight-line "
            "angle per direction so each cell is tested once. For "
            "watersheds, D8 assigns each cell the direction of steepest "
            "descent among its eight neighbors; flat areas and pits are "
            "resolved by filling (raising depressions to their pour "
            "point) or breaching (carving an outlet). Flow accumulation "
            "then processes cells from highest to lowest, each cell adding "
            "its accumulated count to its downstream neighbor - cells with "
            "huge accumulation are the streams, and thresholding the "
            "accumulation grid extracts the channel network. The watershed "
            "of an outlet is all cells whose flow paths reach it. Curvature "
            "correction drops the effective terrain by d^2/(2R) over "
            "distance d (about 0.08 m per km^2), and standard refraction "
            "models use an effective Earth radius of 4/3 R - small terms "
            "that decide long viewsheds."
        ),
        "key_points": [
            "A viewshed is every cell visible from the observer: no intermediate terrain may rise above the sight line.",
            "A watershed is every cell draining to an outlet, found by D8 flow directions plus upstream accumulation.",
            "Depression filling/breaching must precede watershed work - spurious pits trap flow and corrupt basins.",
            "Long viewsheds need Earth-curvature and refraction corrections; short ones live or die on DEM resolution.",
            "Bare-earth vs surface-model choice decides both analyses: trees block views and are not ground for water.",
        ],
        "requirements": [
            "A hydrologically conditioned DEM (depressions handled, method documented) before any watershed delineation.",
            "Observer and target heights stated for viewsheds - eye height is part of the question.",
            "Curvature and refraction corrections for sight lines beyond a few kilometers.",
            "Resolution matched to the features that matter: hedgerows, ditches, and walls need fine grids.",
            "Bare-earth/surface-model labeling, because the wrong surface answers a different question.",
        ],
        "standards": [
            "Flow routing follows the D8 steepest-descent convention with documented depression handling.",
            "Viewshed algorithms document sampling density, curvature, and refraction treatment.",
            "Published basins state the DEM source, resolution, conditioning method, and outlet definition.",
        ],
        "citations": [CIT_HORN, CIT_GDAL, CIT_ISO19115],
        "sig_lens": (
            "The Signature read: the viewshed is what the watchtower "
            "swears it can see, and the watershed is where the rain "
            "swears it will go - two testimonies the terrain gives "
            "about itself. The Signature Survey Method checks the "
            "ground's own words against its resolution, for the Earth "
            "never lies but a coarse grid misquotes it."
        ),
    },
    {
        "key": "constrained_routing",
        "name": "Constrained Network Routing: Turns and Transfers",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Real routing is never just 'shortest path on a graph' - the "
            "graph has rules. Turn restrictions forbid specific maneuvers "
            "(no left turn here, no U-turn there); one-way streets, "
            "vehicle-class bans (no trucks on this bridge), time windows "
            "(this lane reverses at rush hour), and hazmat exclusions all "
            "constrain which edges a given traveler may use. Multimodal "
            "routing adds transfers: walk to the station, ride the train, "
            "walk to the destination - each leg on its own network, joined "
            "at transfer nodes with waiting-time costs from real "
            "timetables. The modeling trick for turns is graph expansion: "
            "replace each intersection node with states for 'arrived via "
            "edge X,' so a forbidden turn is simply a missing edge in the "
            "expanded graph and a turn penalty is an edge cost. Time-"
            "dependent routing makes edge costs functions of departure "
            "time (that 8 AM bus exists only at 8 AM), which requires the "
            "FIFO property - departing later cannot arrive earlier - for "
            "Dijkstra-class algorithms to stay correct. Emergency routing "
            "adds soft constraints: prefer wide roads, avoid low bridges, "
            "penalize school zones. The route that ignores constraints is "
            "not a route at all - it is a suggestion the driver cannot "
            "legally follow."
        ),
        "how_it_works": (
            "Turn expansion converts each directed edge into a node in the "
            "expanded graph; an expanded edge from (u->v) to (v->w) exists "
            "only if the turn u-v-w is legal, carrying the turn's cost or "
            "penalty. Dijkstra then runs unchanged on the expanded graph, "
            "and the expanded path maps back to a legal street sequence - "
            "no U-turn at the forbidden intersection because no edge "
            "represents it. Vehicle profiles filter edges before the "
            "search: a truck profile drops edges tagged maxweight below "
            "the load or hazmat=no. For multimodal, each mode is a "
            "layer - walk layer, transit layer with timetable edges "
            "(an edge from stop A at 08:14 to stop B at 08:31 exists only "
            "then), bike layer - connected by transfer edges carrying "
            "walking time plus expected wait. Time-dependent Dijkstra "
            "evaluates edge costs at the actual arrival time, and the "
            "FIFO property guarantees the settled-on-pop optimality still "
            "holds. Contraction hierarchies extend to all of this by "
            "contracting the expanded graph and customizing per vehicle "
            "profile - which is how production routers answer truck-legal, "
            "turn-legal, multimodal queries in milliseconds."
        ),
        "key_points": [
            "Turn restrictions and penalties are modeled by expanding the graph: states become 'arrived via edge X,' forbidden turns become missing edges.",
            "Vehicle profiles (weight, height, hazmat) filter edges before search - illegal-for-you edges simply do not exist.",
            "Multimodal routing layers networks (walk, transit, bike) joined by transfer edges with timetable-driven wait costs.",
            "Time-dependent costs need the FIFO property - departing later can never arrive earlier - for Dijkstra-class correctness.",
            "A route that ignores constraints is not a route; legality is part of optimality.",
        ],
        "requirements": [
            "Turn restriction and penalty data at every constrained intersection, kept current with signage.",
            "Vehicle profile definitions (dimensions, weight, cargo class) applied as edge filters per query.",
            "Timetable data with service calendars for transit layers - a Tuesday schedule is not a Sunday schedule.",
            "FIFO verification on time-dependent cost functions before trusting Dijkstra-class results.",
            "Expanded-graph or equivalent modeling so the algorithm cannot 'discover' a forbidden maneuver.",
        ],
        "standards": [
            "Turn modeling follows expanded-graph practice with documented restriction and penalty semantics.",
            "Multimodal transfers follow timetable-based routing with stated schedule vintage.",
            "Published routes state the vehicle profile and constraint set so legality is auditable.",
        ],
        "citations": [CIT_DIJKSTRA, CIT_CH, CIT_ASTAR],
        "sig_lens": (
            "The Signature read: constraints are the laws of the road "
            "given as testimony - this turn forbidden, that bridge too "
            "weak, this train only at dawn. The Signature Survey Method "
            "binds the search to the law before it seeks the shortest, "
            "because the fastest illegal path is not a path but a "
            "violation with directions."
        ),
    },
    {
        "key": "projection_math",
        "name": "Projection Math: Forward, Inverse, and Scale Factor",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Behind every map projection sit three computations that "
            "operations must actually run: forward (angles to plane), "
            "inverse (plane back to angles), and the scale factor (how "
            "much the map stretches reality at each point). The Mercator "
            "formulas are the canonical example - forward: x = R * "
            "(lon - lon0), y = R * ln(tan(pi/4 + lat/2)); inverse: lon = "
            "x/R + lon0, lat = 2*atan(e^(y/R)) - pi/2 - and every "
            "projection has its own pair, some closed-form, some "
            "iterative. The scale factor k is the local truth-teller: for "
            "Mercator k = sec(lat) on the sphere, meaning a measured map "
            "distance divided by k gives the true ground distance - at "
            "60 degrees latitude every map meter is really half a ground "
            "meter of map exaggeration, i.e., the map draws things twice "
            "as large. Area scale is k squared; angular distortion has "
            "its own formula per projection. UTM's deliberate 0.9996 "
            "central scale factor is applied wisdom: shrink the center "
            "slightly so the zone's edges (which would otherwise exceed "
            "1.0) balance out, minimizing maximum distortion across the "
            "zone. Anyone measuring on a projected map without dividing "
            "by the scale factor is reading the map's flattery as fact."
        ),
        "how_it_works": (
            "The forward Mercator at latitude 40 degrees: y = R * "
            "ln(tan(pi/4 + 0.3491)) with R = 6,378,137 m gives y about "
            "4,865,946 m - the spherical formula, within meters of the "
            "ellipsoidal truth for illustration. The inverse recovers "
            "latitude exactly: lat = 2*atan(e^(y/R)) - pi/2 returns 40.0 "
            "degrees, and round-trip error in double precision sits near "
            "1e-9 degrees - far below any measurement. The scale factor "
            "k = sec(40 deg) = 1.3054, so a 1,305-meter segment measured "
            "on the Mercator map at that latitude is truly 1,000 ground "
            "meters; area inflation is k^2 = 1.704. Conic projections "
            "like Albers carry two standard parallels where k = 1 exactly, "
            "with distortion growing between and beyond - the parallels "
            "are chosen to bracket the mapped region. Transverse Mercator "
            "(the UTM engine) uses series expansions in longitude offset "
            "from the central meridian (Karney's and Kruger's series to "
            "high order), accurate to nanometers within the zone. Software "
            "never hand-rolls these: PROJ implements every formula with "
            "its domain limits, and the operation's job is to call "
            "forward/inverse/scale correctly and apply k wherever a map "
            "measurement becomes a ground truth."
        ),
        "key_points": [
            "Every projection needs three computations: forward (angles to plane), inverse (plane to angles), and scale factor k.",
            "Mercator: y = R*ln(tan(pi/4 + lat/2)), inverse lat = 2*atan(e^(y/R)) - pi/2, scale k = sec(lat).",
            "Map distance divided by k is ground distance; area distortion is k squared - at 60 deg latitude Mercator draws 4x area.",
            "UTM's 0.9996 central scale is deliberate: shrink the middle so the edges balance, minimizing worst distortion.",
            "Round-trip forward/inverse error in doubles is ~1e-9 degrees; hand-rolled projection code is never worth the risk.",
        ],
        "requirements": [
            "Forward, inverse, and scale-factor functions from a proven library (PROJ) - never hand-derived series.",
            "Scale-factor division applied to every distance or area measured on a projected map.",
            "Standard parallels / central meridian chosen to bracket the actual work area.",
            "Round-trip validation (forward then inverse) in acceptance tests for any custom pipeline.",
            "Ellipsoidal vs spherical formula awareness: know which the library used and its error.",
        ],
        "standards": [
            "Projection formulas follow their published definitions as implemented in PROJ.",
            "Scale factors are reported per location, not assumed constant across a map.",
            "Measurement workflows document the k-correction so map readings convert to ground truth.",
        ],
        "citations": [CIT_PROJ, CIT_EPSG, CIT_WGS84],
        "sig_lens": (
            "The Signature read: the scale factor is the map's confession "
            "- here is exactly how much I flatter the truth at this "
            "spot. The Signature Survey Method reads the confession "
            "before the measurement and divides out the flattery, "
            "because testimony taken from a bragging map convicts no "
            "one but the surveyor."
        ),
    },
    {
        "key": "trajectory_analysis",
        "name": "Trajectory Analysis: Stays, Segments, and Similarity",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A trajectory is a timestamped trail of positions - a delivery "
            "truck's day, a hurricane's path, a migrating herd - and "
            "trajectory analysis turns the raw trail into meaning. Stay-"
            "point detection finds where the mover stopped: a cluster of "
            "points within a small radius spanning a minimum duration is "
            "a stay (the warehouse, the nest), while everything between "
            "stays is a move segment. Segmentation splits the trail by "
            "behavior change - speed, heading, or transport mode shifts - "
            "so one tangled GPS log becomes a clean sequence of walk, "
            "drive, and dwell episodes. Similarity measures compare whole "
            "trajectories: dynamic time warping aligns two trails in time "
            "before measuring distance (forgiving different speeds along "
            "the same route), the Frechet distance measures the longest "
            "leash needed to walk both curves together, and longest common "
            "subsequence tolerates outlier points that would corrupt the "
            "others. Fleet analytics uses these to find common routes, "
            "detect detours, and cluster drivers by behavior; ecology uses "
            "them to find migration corridors; urban planning uses stay "
            "points to map activity hotspots. The privacy shadow over all "
            "of it is real: trajectories identify people with shocking "
            "ease, so analysis needs aggregation, consent, and purpose "
            "limitation designed in."
        ),
        "how_it_works": (
            "Stay detection scans the timestamped points: starting at point "
            "i, it extends j forward while every point stays within the "
            "distance threshold of point i; if the time span from i to j "
            "exceeds the duration threshold, the cluster's centroid is a "
            "stay point and the scan resumes after j. Typical thresholds "
            "are 100-200 meters and 10-30 minutes for urban human movement. "
            "Segmentation then cuts the trail at stay boundaries and "
            "further splits move segments where speed or heading changes "
            "abruptly - a heading change above ~45 degrees sustained over "
            "several fixes marks a turn worth splitting on. Dynamic time "
            "warping builds a cost matrix between the two point sequences "
            "and finds the cheapest alignment path through it, so a "
            "delivery van that drove the same street slowly and quickly on "
            "two days still matches. The discrete Frechet distance is the "
            "minimum over all alignments of the maximum paired distance - "
            "the shortest leash that lets a person walk one curve while "
            "their dog walks the other. Clustering (e.g., TRACLUS-style "
            "partition-and-group) then finds the corridors: subtrajectories "
            "that many movers share, which are the real routes hidden in "
            "the noise."
        ),
        "key_points": [
            "Stay points are clusters within a distance threshold spanning a duration threshold - the stops hidden in the trail.",
            "Segmentation cuts trajectories at behavior changes (speed, heading, mode) into clean episodes.",
            "Dynamic time warping aligns trails in time before measuring distance, forgiving speed differences on the same route.",
            "Frechet distance is the longest leash needed to walk both curves together - the strict shape comparison.",
            "Trajectories identify people easily: aggregation, consent, and purpose limitation are designed in, not bolted on.",
        ],
        "requirements": [
            "Timestamped positions with honest accuracy - stay detection on jittery fixes invents stops.",
            "Distance and duration thresholds calibrated to the mover: person, vehicle, and animal need different values.",
            "A stated similarity measure (DTW, Frechet, LCSS) with its outlier and speed semantics documented.",
            "Map context where available: stays snap to places, segments snap to roads, via map-matching.",
            "Privacy design: k-anonymity or aggregation for published patterns, consent for personal trails.",
        ],
        "standards": [
            "Stay-point detection follows the distance-duration threshold convention with published parameters.",
            "Similarity measures state their alignment semantics so comparisons are reproducible.",
            "Published movement patterns follow aggregation practice that prevents re-identification.",
        ],
        "citations": [CIT_MAPMATCH, CIT_GPS, CIT_TOBLER],
        "sig_lens": (
            "The Signature read: a trajectory is a life written in "
            "footsteps - where it rested, where it hurried, which roads "
            "it trusts. The Signature Survey Method reads the footsteps "
            "for the honest patterns - the stays, the corridors, the "
            "detours - and treats the writer behind them as a person, "
            "never as a dataset."
        ),
    },
    {
        "key": "uncertainty_propagation",
        "name": "Propagating Uncertainty Through Spatial Operations",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Every spatial operation inherits the uncertainty of its "
            "inputs and usually adds its own: buffer a GPS point with 5-"
            "meter accuracy by 100 meters and the boundary's true location "
            "is uncertain by those same 5 meters; intersect two uncertain "
            "polygons and the overlap's edges carry both uncertainties "
            "combined. Uncertainty propagation is the discipline of "
            "carrying the error budget through the whole pipeline so the "
            "final answer still knows how much to trust itself. Analytical "
            "propagation uses the covariance law: for linear (or "
            "linearized) operations, output covariance = J * input "
            "covariance * J^T with J the Jacobian - exact for affine "
            "transforms, approximate for the rest. Monte Carlo propagation "
            "is the general workhorse: perturb the inputs by sampling "
            "their error distributions, run the operation hundreds or "
            "thousands of times, and read the output distribution "
            "directly - it handles buffers, overlays, and network "
            "analysis that defeat closed forms. The classic blunder is "
            "the crisp-boundary fallacy: drawing a 100-meter buffer as a "
            "razor line and counting 'inside' as certain, when the honest "
            "answer is a probability field - 95 percent inside here, 50 "
            "percent at the line, 5 percent beyond. Flood maps, "
            "contamination plumes, and service areas all become "
            "probabilistic under honest propagation, and decisions made "
            "on them get risk curves instead of false certainties."
        ),
        "how_it_works": (
            "Monte Carlo propagation runs the pipeline as a loop: draw "
            "input realization k from the input error model (e.g., each "
            "GPS point perturbed by its 2D Gaussian with the recorded "
            "covariance), execute the deterministic operation (buffer, "
            "intersect, route), record the output. After N realizations "
            "(hundreds for means, thousands for tails), the output's "
            "empirical distribution is the propagated uncertainty: the "
            "mean buffer boundary, the 5th/95th percentile boundary band, "
            "the probability each raster cell falls inside. For a 100 m "
            "buffer on a point with 5 m 1-sigma radial error, the boundary "
            "band at 95 percent spans roughly 95 to 107 m - asymmetric, "
            "because radial error is one-sided - so the crisp line was "
            "always a fiction about 12 meters wide. Analytical propagation "
            "covers the linearizable cases: a Helmert-transformed point's "
            "covariance transforms exactly by J*C*J^T, so datum-shifted "
            "control networks carry honest ellipses without sampling. "
            "Variance-based sensitivity (Sobol-style decomposition on the "
            "Monte Carlo runs) then attributes the output uncertainty to "
            "inputs - revealing, often, that one sloppy input dominates "
            "the whole pipeline's error, which tells the operator exactly "
            "where better data pays off."
        ),
        "key_points": [
            "Uncertainty compounds through operations: buffers, overlays, and routes inherit and add error - the final answer must carry the budget.",
            "Monte Carlo propagation samples input error distributions, runs the operation N times, and reads the output distribution directly.",
            "Analytical propagation (J*C*J^T) covers linearizable steps like datum transforms exactly.",
            "Crisp boundaries are the classic blunder: honest buffers are probability fields, not razor lines.",
            "Sensitivity decomposition shows which input dominates the output error - telling operators where better data pays.",
        ],
        "requirements": [
            "Input error models for every input: covariance, distribution family, and stated confidence.",
            "Enough Monte Carlo realizations for the needed tail: hundreds for means, thousands for 95th percentiles.",
            "Seeded, reproducible sampling so propagated results are auditable.",
            "Probability-field outputs (per-cell inside-probability) instead of crisp lines where decisions carry risk.",
            "Analytical propagation wherever Jacobians exist, to cross-check the Monte Carlo.",
        ],
        "standards": [
            "Propagated uncertainty is reported with the method (analytical/Monte Carlo), realization count, and confidence level.",
            "Error models follow the recorded input covariances; invented distributions are labeled as assumptions.",
            "Risk-relevant outputs (flood, plume, service) present probability bands per uncertainty-propagation practice.",
        ],
        "citations": [CIT_GOODCHILD, CIT_KALMAN, CIT_NSSDA],
        "sig_lens": (
            "The Signature read: uncertainty is the honest echo of every "
            "measurement, and propagation follows the echo through every "
            "room it enters. The Signature Survey Method lets no "
            "operation launder doubt into certainty - the final map shows "
            "its shadows, because a map that hides its doubt testifies "
            "falsely about its confidence."
        ),
    },
    {
        "key": "itrf_plate_motion",
        "name": "Time-Dependent Coordinates: ITRF and Plate Motion",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "At the top of the accuracy ladder, coordinates are functions "
            "of time. The International Terrestrial Reference Frame (ITRF) "
            "- realized by the IERS from VLBI, satellite laser ranging, "
            "GNSS, and DORIS observations - defines station positions at "
            "a reference epoch plus linear velocities, with recent "
            "realizations adding seasonal terms and post-seismic "
            "deformation models. A station in California might carry "
            "position at epoch 2015.0 plus a velocity of 35 mm/year "
            "northwest: propagate eleven years and the coordinate has "
            "moved 38 centimeters - larger than most survey tolerances. "
            "This is why high-accuracy GNSS processing outputs ITRF-at-"
            "observation-epoch, and why the last step of any precise "
            "workflow is an explicit transformation to the target frame "
            "at the target epoch. Earthquakes complicate the linear story: "
            "a magnitude-7 event can offset stations by meters in "
            "seconds, so modern frames publish coseismic jumps and "
            "post-seismic decay curves alongside the velocities. "
            "Operational rule at this level: a coordinate is a triple of "
            "(frame, epoch, velocity-model), and any software that stores "
            "only lat/lon has silently frozen time."
        ),
        "how_it_works": (
            "Propagation is linear at first order: X(t) = X(t0) + V * "
            "(t - t0), with X in geocentric Cartesian meters and V in "
            "meters per year. A station at X(t0) with velocity "
            "(0.025, -0.018, 0.011) m/yr moves about 3.3 cm/yr; over a "
            "decade the displacement passes 30 cm, and the horizontal "
            "component dominates. The ITRF realization ties it together: "
            "ITRF2020, for example, publishes positions, velocities, and "
            "annual/semiannual seasonal coefficients for hundreds of core "
            "stations, plus parametric models of major earthquakes' "
            "coseismic offsets and logarithmic/exponential post-seismic "
            "relaxation. Transforming ITRF-at-epoch to a plate-fixed frame "
            "(like ETRS89 in Europe or NAD83 in North America) applies the "
            "published Helmert plus the plate-motion model in reverse - "
            "which is exactly what national mapping agencies publish as "
            "their datum modernization. Validation closes the loop: "
            "re-observing a control point years later must reproduce the "
            "propagated coordinate within the combined error budget, or "
            "the velocity model (or the monument) is indicted."
        ),
        "key_points": [
            "ITRF defines station positions at a reference epoch plus velocities (and now seasonal and post-seismic terms) from four space-geodetic techniques.",
            "Propagation X(t) = X(t0) + V*(t-t0): a decade of plate motion moves coordinates decimeters - beyond survey tolerance.",
            "High-accuracy GNSS yields ITRF-at-observation-epoch; the final step is an explicit transform to the target frame at the target epoch.",
            "Earthquakes add coseismic jumps and post-seismic decay - the linear story needs parametric event models.",
            "A coordinate at this level is (frame, epoch, velocity-model): storing bare lat/lon silently freezes time.",
        ],
        "requirements": [
            "Frame, epoch, and velocity model recorded for every high-accuracy coordinate.",
            "Propagation to a common epoch before comparing or combining coordinates from different years.",
            "Earthquake event models applied where coseismic offsets exceed the tolerance.",
            "Published Helmert + plate-motion parameters for frame-to-frame conversion, never ad-hoc shifts.",
            "Re-observation validation: propagated coordinates must reproduce within the error budget.",
        ],
        "standards": [
            "Reference frames follow IERS ITRF realizations with documented epoch and velocity models.",
            "Plate-fixed national frames document their tie and transformation to the current ITRF.",
            "Time-dependent coordinates are exchanged with epoch metadata per geodetic practice.",
        ],
        "citations": [CIT_WGS84, CIT_PROJ, CIT_EPSG],
        "sig_lens": (
            "The Signature read: at the highest accuracy the Earth itself "
            "is a moving witness, and its testimony carries a timestamp "
            "down to the millimeter. The Signature Survey Method hears "
            "the date as part of the oath - frame, epoch, and velocity "
            "sworn together - for time is the one witness no surveyor "
            "may cross-examine twice."
        ),
    },
    {
        "key": "spatial_data_quality",
        "name": "Spatial Data Quality and Fitness for Use",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Data quality is not a single score - it is the documented "
            "answer to 'can I use this for my purpose,' and the answer "
            "changes with the purpose. The standard quality elements are "
            "five: positional accuracy (how close to truth - the NSSDA "
            "95-percent test against independent higher-accuracy "
            "checkpoints), attribute accuracy (are the labels right), "
            "completeness (what is missing - omission - and what should "
            "not be there - commission), logical consistency (valid "
            "geometry, correct topology, domain-valid values), and lineage "
            "(the full history: sources, transformations, processing "
            "steps). A road dataset with 2-meter accuracy is superb for "
            "navigation and useless for autonomous-vehicle lane control; "
            "fitness for use is always purpose-relative. The NSSDA test "
            "is the quantitative anchor: compare the dataset against "
            "independent checkpoints of higher accuracy, compute RMSE in x "
            "and y, and report horizontal accuracy = 1.7308 * RMSE_r at 95 "
            "percent confidence - a dataset claiming '1-meter accuracy' "
            "must show the checkpoint statistics, not just assert it. "
            "ASPRS 2014 modernized this for digital data with RMSE-based "
            "classes and separate treatment of orthoimagery, elevation, "
            "and planimetrics. Lineage is the element most often skipped "
            "and most often needed: when two datasets disagree, the one "
            "with documented lineage wins the argument because its errors "
            "can be audited."
        ),
        "how_it_works": (
            "An NSSDA accuracy assessment selects at least 20 independent "
            "checkpoints (more for large areas), each surveyed to at least "
            "three times the expected accuracy of the dataset under test, "
            "well distributed across the area. Residuals dx, dy at each "
            "checkpoint give RMSE_x = sqrt(mean(dx^2)), RMSE_y similarly, "
            "RMSE_r = sqrt(RMSE_x^2 + RMSE_y^2), and the reported "
            "horizontal accuracy at 95 percent = 1.7308 * RMSE_r. A "
            "dataset with RMSE_r = 1.2 m reports 2.08 m at 95 percent - "
            "the number that goes on the metadata, not the RMSE. "
            "Completeness is measured by sampling: omission rate from "
            "ground-truth comparison plots, commission rate from "
            "verification of a feature sample. Logical consistency runs "
            "as automated rules: geometry validity, no duplicate IDs, "
            "attribute domains, topological must-not-overlap rules for "
            "parcels. Lineage is recorded as a process chain per ISO "
            "19115: source -> transformation (with parameters and dates) "
            "-> output, so any feature can be traced to its origins. The "
            "fitness-for-use statement then binds it together: 'tested 2.1 "
            "m at 95 percent, complete for paved public roads as of 2024, "
            "valid topology' - which lets the autonomous-vehicle team "
            "decline and the logistics team accept, both correctly."
        ),
        "key_points": [
            "Quality has five elements: positional accuracy, attribute accuracy, completeness, logical consistency, and lineage - fitness is always purpose-relative.",
            "The NSSDA test anchors accuracy: 95-percent horizontal = 1.7308 x RMSE_r against independent higher-accuracy checkpoints.",
            "Completeness tracks omission (missing) and commission (spurious); consistency runs as automated validity and topology rules.",
            "Lineage - the full source-to-output process chain - wins arguments when datasets disagree, because its errors are auditable.",
            "A fitness-for-use statement binds it all: tested accuracy, completeness scope, and vintage, so each consumer judges correctly.",
        ],
        "requirements": [
            "Independent checkpoints (3x more accurate than the data under test, n >= 20) for any claimed positional accuracy.",
            "RMSE-based reporting at 95 percent confidence - never a bare 'accuracy' number.",
            "Completeness and consistency metrics with their sampling or rule definitions.",
            "Full lineage per ISO 19115: sources, transformations with parameters and dates.",
            "A written fitness-for-use statement per intended purpose, because one dataset serves purposes differently.",
        ],
        "standards": [
            "Positional accuracy testing follows FGDC NSSDA (FGDC-STD-007.3-1998); digital data classes follow ASPRS 2014.",
            "Metadata and lineage follow ISO 19115-1:2014.",
            "Accuracy claims without checkpoint statistics are assertions, not measurements.",
        ],
        "citations": [CIT_NSSDA, CIT_ASPRS, CIT_ISO19115],
        "sig_lens": (
            "The Signature read: quality is the cross-examination of the "
            "data itself - accuracy tested, completeness counted, lineage "
            "sworn step by step. The Signature Survey Method puts every "
            "dataset on the stand before trusting it, and writes the "
            "fitness verdict where all can read it - for testimony "
            "unexamined is rumor with coordinates."
        ),
    },
    {
        "key": "realtime_pipelines",
        "name": "Real-Time Geospatial Pipelines",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Static maps answer 'what is where'; real-time pipelines answer "
            "'what is happening where, right now.' A fleet tracker ingests "
            "thousands of GPS pings per second, map-matches them to roads, "
            "detects speeding and geofence events, and serves live ETAs - "
            "all with end-to-end latency measured in seconds. The "
            "architecture is a stream processor: ingest (message queue "
            "with partitioning by vehicle ID so each vehicle's events stay "
            "ordered), enrich (map-match, attach road attributes, compute "
            "speed from successive fixes), detect (geofence state machines, "
            "speeding windows, dwell timers), and serve (live tile layers, "
            "alert webhooks, materialized current-state tables). The hard "
            "problems are all operational: out-of-order and late events "
            "(a ping delayed 30 seconds must still correct the record, not "
            "corrupt it), exactly-once-ish semantics via idempotent "
            "event IDs, backpressure when a cellular dead zone releases a "
            "flood of buffered pings, and state management for millions of "
            "concurrent geofence state machines. Watermarks bound the "
            "lateness the system tolerates; beyond the watermark, late "
            "data goes to a corrections channel rather than rewriting the "
            "live view. Testing is scenario-based: replay recorded "
            "rush-hours, tunnel outages, and GPS-jump storms through the "
            "pipeline and assert the events come out right - because the "
            "pipeline that has never seen a tunnel will fail in the first "
            "one."
        ),
        "how_it_works": (
            "Each ping carries (vehicle_id, timestamp, lat, lon, accuracy). "
            "Partitioning by vehicle_id sends each vehicle's pings to one "
            "stream worker in timestamp order. The worker keeps per-vehicle "
            "state: last matched position, current geofence states, speed "
            "window. Enrichment map-matches the ping (HMM over recent "
            "fixes), computes speed from the matched distance over dt, and "
            "flags implausible jumps (200 km/h in a city grid = GPS glitch, "
            "quarantined). Detection evaluates the geofence state machines "
            "with hysteresis, accumulates speeding durations, and starts "
            "dwell timers. Watermarks track the minimum event-time seen "
            "across partitions minus the allowed lateness (e.g., 60 s): "
            "windows close at the watermark, late pings update a "
            "corrections log. Serving has two faces: a materialized "
            "'current state' table (vehicle -> last known good position, "
            "updated idempotently by event ID) for live maps, and an "
            "append-only event log for analytics. Backpressure comes from "
            "bounded queues with load-shedding policies documented in "
            "advance - during a ping flood the pipeline degrades by "
            "sampling, never by silently dropping state updates. Replay "
            "testing feeds recorded scenarios and asserts exact expected "
            "event sequences, making the pipeline deterministic under "
            "chaos."
        ),
        "key_points": [
            "Stream architecture: ingest partitioned by entity, enrich (map-match, speed), detect (fences, speeding, dwell), serve (live state + event log).",
            "Out-of-order and late events are corrected via watermarks and a corrections channel - never by corrupting the live view.",
            "Idempotent event IDs give exactly-once-ish semantics across retries and replays.",
            "Backpressure policy is documented in advance: degrade by sampling under flood, never silently drop state.",
            "Scenario replay testing (rush hours, tunnel outages, GPS jumps) proves the pipeline before the real chaos does.",
        ],
        "requirements": [
            "Partitioning key that keeps each entity's events ordered (vehicle/device ID).",
            "Watermark and allowed-lateness policy with a corrections path for late data.",
            "Idempotent sinks keyed by event ID so replays and retries never double-count.",
            "Per-entity state management sized for the concurrent population (millions of fence state machines).",
            "Documented load-shedding behavior and replay-test scenarios covering outages and glitch storms.",
        ],
        "standards": [
            "Event-time processing with watermarks follows standard stream-processing semantics.",
            "Position enrichment uses the same map-matching and error-budget practice as batch work.",
            "Published live services document latency SLOs and degradation behavior.",
        ],
        "citations": [CIT_MAPMATCH, CIT_GPS, CIT_ISO19115],
        "sig_lens": (
            "The Signature read: a real-time pipeline is testimony given "
            "at speed - thousands of witnesses speaking at once, each "
            "heard in order, none lost, none double-counted. The "
            "Signature Survey Method keeps the courtroom orderly under "
            "the flood: every voice partitioned, every late arrival "
            "noted, the record corrected but never corrupted."
        ),
    },
    {
        "key": "operations_playbook",
        "name": "The Geospatial Operations Playbook",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "This record is the capstone: the checklist that binds all "
            "thirty-three records before it into one operational "
            "discipline. Every geospatial job - from a site survey to a "
            "continental routing service - runs the same gauntlet. One: "
            "name the coordinate system, datum, epoch, and axis order for "
            "every input, and transform everything to one common frame "
            "before any computation. Two: state the distance and area "
            "model (planar, great-circle, ellipsoidal, network) and the "
            "projection bargain for every measurement. Three: budget the "
            "errors - sensor noise, datum shifts, transformation steps - "
            "and propagate the uncertainty to the final answer, reporting "
            "it at a stated confidence. Four: validate the geometry "
            "(valid polygons, sane topology) and index it (R-tree, tiles, "
            "geohash) before the first query. Five: choose algorithms by "
            "scale - exact Dijkstra where the graph is small, hierarchies "
            "where it is continental, tiled joins where the data is "
            "massive. Six: document lineage, transformation paths, and "
            "fitness for use so the next operator - or the auditor - can "
            "reproduce everything. Seven: design for the failure modes: "
            "GPS outages, datum mismatches at project boundaries, skewed "
            "tiles, late stream events. The playbook's motto is the "
            "database's in one line: a coordinate without a system is two "
            "numbers, a distance without a model is a guess, a map "
            "without an error budget is a rumor, and an operation that "
            "cannot be reproduced did not happen."
        ),
        "how_it_works": (
            "The playbook executes as a validation pipeline: each check is "
            "a predicate over the job's inputs and plan, and the job runs "
            "only when all predicates pass. The CRS check asserts every "
            "input carries an EPSG/WKT2 definition and one common target "
            "frame is chosen. The model check asserts the distance/area "
            "model matches the data family and range. The error-budget "
            "check asserts every sensor and transformation step has a "
            "stated uncertainty and that propagation reaches the output. "
            "The geometry check runs validity and the index check confirms "
            "query structures exist for the data volume. The algorithm "
            "check matches method to scale with documented complexity. "
            "The lineage check requires source, transformation, and "
            "parameter records. The failure-mode check walks a premortem "
            "list: outage, mismatch, skew, lateness - each with its "
            "mitigation named. In software this is a runnable gate: a "
            "function per check returning pass/fail with the evidence, "
            "and the pipeline refuses to run on red. Organizations adopt "
            "it as a review template: no map ships, no API launches, no "
            "analysis publishes until the playbook is green - because "
            "every geospatial disaster in history was a playbook check "
            "someone skipped."
        ),
        "key_points": [
            "One common CRS, datum, epoch, and axis order for all inputs - transformed before any computation, never during.",
            "A stated distance/area model and projection bargain for every measurement taken.",
            "Error budgets propagated to the final answer and reported at a stated confidence.",
            "Valid geometry, proper indexes, and algorithms matched to scale - exact where small, hierarchical and tiled where massive.",
            "Full lineage plus a premortem on failure modes (outages, mismatches, skew, lateness) - the job runs only when the playbook is green.",
        ],
        "requirements": [
            "A runnable validation gate: one predicate per playbook check, with evidence, refusing to run on red.",
            "CRS, model, budget, geometry, index, algorithm, lineage, and failure-mode checks - all eight, every job.",
            "Review sign-off: no map ships, no API launches, no analysis publishes until green.",
            "Premortem documentation naming each failure mode and its mitigation.",
            "Reproducibility: inputs, parameters, and code versions recorded so the operation can be rerun exactly.",
        ],
        "standards": [
            "The playbook composes the standards of all prior records: WGS84/ITRF frames, OGC predicates, NSSDA/ASPRS accuracy, ISO 19115 lineage.",
            "Validation gates are versioned with the playbook so audits can replay any historical run.",
            "Fitness-for-use statements are the playbook's output artifact for every delivered product.",
        ],
        "citations": [CIT_WGS84, CIT_NSSDA, CIT_ISO19115, CIT_OGC_SFS],
        "sig_lens": (
            "The Signature read: the playbook is the oath of oaths - the "
            "sworn procedure that makes every lesser oath trustworthy. "
            "The Signature Survey Method runs the gauntlet before the "
            "work, not after the disaster, for the witness who checks "
            "their testimony before speaking is the one the court "
            "believes."
        ),
    },
]
