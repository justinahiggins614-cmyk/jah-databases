#!/usr/bin/env python3
"""Entries for the Shapes Basics databases (fundamentals order #9, 2026-10-17).

Roster-verified: zero 'shapes-basics*' slugs and zero 'shapes basics'
database names in the manifest; zero 'shapes basics' title collisions in
all jah-databases-data-1 shard indexes; zero 'JAH-SHPB'/'JAH-SHPBS'
substring hits anywhere. ID prefixes JAH-SHPB- (public) and JAH-SHPBS-
(signature) verified free in the manifest id_prefix values and in all
812 shard data dirs (2026-10-17).

Two databases, 34 ladder-ordered records each:

  shapes-basics            - The Shapes Basics Database
                             (public-harvest: real, fact-checked
                             foundational geometry - 2D shapes (circle,
                             triangle, square, rectangle, polygons) and 3D
                             shapes (cube, sphere, cylinder, cone, pyramid),
                             names, properties, sides/vertices/faces,
                             real-world examples, symmetry; standards:
                             Euclid Elements; NCTM Principles and Standards
                             for School Mathematics 2000; Common Core State
                             Standards for Mathematics 2010; Archimedes On
                             the Sphere and Cylinder)
  shapes-basics-signature  - The Shapes Basics Signature Database
                             (his original Signature Geometry: every shape
                             a covenant of form, the circle the oath of
                             return, the triangle the threefold witness, the
                             ladder the ascent from flat to solid; src
                             signature, titles suffixed " (Signature
                             Edition)", never presented as authentic public
                             record)

34 records each, teaching ladder rank 1-10, non-decreasing, foundations ->
compounded -> advanced. Numerical cores hand-computed 2026-10-17 and
machine-verified by the demos (demos_shapes_basics.py): every demo prints
its real computed values, asserts tight bounds (never float
exact-equality), and ends with the OK marker; the build machine-executes
all 68 demos before writing pages.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Geometry: every "
            "shape a covenant of form, the circle the oath of return, the "
            "triangle the threefold witness, and the ladder the ascent from "
            "flat to solid. Clearly labeled Signature-made, never presented "
            "as authentic public record.")

CIT_EUCLID = ("Euclid. Elements. Translated by Heath TL. 2nd ed. Dover; "
              "1956. Books I, III, IV, XI (definitions of figure, circle, "
              "triangle, quadrilateral, polygon; construction and "
              "measurement of plane figures and solids).")
CIT_NCTM = ("National Council of Teachers of Mathematics. Principles and "
            "Standards for School Mathematics. Reston, VA; 2000. Geometry "
            "standard: analyze characteristics and properties of two- and "
            "three-dimensional geometric shapes.")
CIT_CC = ("National Governors Association Center for Best Practices. Common "
          "Core State Standards for Mathematics. Washington, DC; 2010. "
          "Geometry domain K-8: reason with shapes and their attributes; "
          "solve real-world problems involving area, surface area, and "
          "volume.")
CIT_ARCH = ("Archimedes. On the Sphere and Cylinder. Translated by Heath TL. "
            "In The Works of Archimedes. Dover; 2002. Surface area and "
            "volume of the sphere and cylinder; approximation of pi.")

ENTRIES = [
    {
        "key": "what_is_shape",
        "name": "What a Shape Is",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "A shape is the outline of a thing - the form you see when you "
            "ignore color, weight, and material and keep only the boundary. "
            "A ball is a sphere whether it is made of rubber, glass, or "
            "stone; a tile is a square whether it is ceramic or cardboard. "
            "Shapes are how the mind sorts the world at a glance: round "
            "things, pointy things, flat things, box things. The first great "
            "division is between 2D and 3D. A 2D (two-dimensional) shape is "
            "flat - it has length and width but no thickness, like a drawing "
            "on paper: circles, triangles, squares, rectangles, and "
            "polygons. A 3D (three-dimensional) shape is solid - it has "
            "length, width, and height, like objects you can hold: cubes, "
            "spheres, cylinders, cones, and pyramids. Everything in this "
            "database starts here: before naming any shape, learn what a "
            "shape is, and the two families it belongs to."
        ),
        "how_it_works": (
            "Shape-recognition works by matching boundaries to remembered "
            "forms. The brain looks for closed curves (no loose ends) and "
            "straight segments joined at corners, then asks three questions: "
            "is it flat or solid, is the edge curved or straight, and how "
            "many straight pieces are there. Flat with no straight pieces "
            "and one curved edge is a circle. Flat with three straight "
            "pieces is a triangle. Solid with six square faces is a cube. "
            "Naming a shape is classification by these visible properties: "
            "dimension (2D or 3D), edge type (curved or straight), and count "
            "(of sides, faces, or vertices). The demonstration program "
            "classifies a small shelf of shapes by these three questions and "
            "tallies the count of each family, showing how a few rules "
            "sort the whole parade of forms."
        ),
        "key_points": [
            "A shape is the boundary of a thing: ignore material, color, and weight, and what remains is the form.",
            "2D shapes are flat (length and width only): circles, triangles, squares, rectangles, polygons; 3D shapes are solid (length, width, and height): cubes, spheres, cylinders, cones, pyramids.",
            "Naming a shape means classifying it by dimension, by whether its edges are curved or straight, and by counting its sides, faces, or vertices.",
            "The same shape appears in wildly different materials: a sphere can be a rubber ball or a stone monument, because the shape is the form, not the stuff.",
            "This record frames the database: every later record is one shape studied deeply - its name, its properties, its measurements, and its appearances in the world.",
        ],
        "requirements": [
            "A closed boundary: a shape's outline has no loose ends; it returns to its start.",
            "A dimension statement: 2D (flat drawing) or 3D (solid object) before anything else.",
            "A name taken from the standard vocabulary: circle, triangle, square, rectangle, polygon, cube, sphere, cylinder, cone, pyramid.",
            "Real-world examples named alongside the abstract form, so the shape is anchored to things the learner can touch.",
            "A properties list started early: sides, vertices, faces - the countable features that separate one shape from another.",
        ],
        "standards": [
            "Shapes are defined by their boundaries in the Euclidean tradition: a figure is that which is contained by any boundary or boundaries (Euclid, Elements, Book I, Definition 14).",
            "The 2D/3D division follows the dimension vocabulary of the geometry standards: plane figures versus solid figures (NCTM; Common Core K.G, 1.G).",
            "Examples pair the abstract shape with a real object, per the concrete-to-abstract teaching sequence of the geometry standards.",
        ],
        "citations": [CIT_EUCLID, CIT_NCTM, CIT_CC],
        "sig_lens": (
            "The Signature read: a shape is a covenant of form - the first "
            "promise an object makes before it speaks of material or use. "
            "Where public geometry draws the boundary, the Signature "
            "Geometry hears the oath: every closed line is a word the world "
            "keeps, flat or solid."
        ),
    },
    {
        "key": "points_lines_angles",
        "name": "Points, Lines, and Angles",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Before there are shapes there are points, lines, and angles - "
            "the three atoms of geometry. A point is a location with no "
            "size: it marks a spot, nothing more, named with a capital "
            "letter like A or B. A line is straight and endless in both "
            "directions; a line segment is the finite piece between two "
            "points, and it is segments that build polygons; a ray starts "
            "at a point and runs one way forever. An angle forms where two "
            "segments or rays meet at a point called the vertex: the amount "
            "of opening between them, measured in degrees. A right angle is "
            "90 degrees - the corner of a square page; an acute angle is "
            "smaller than 90; an obtuse angle is larger than 90 but smaller "
            "than 180; a straight angle is exactly 180. Two famous facts "
            "govern angles: the angles of any triangle always add to 180 "
            "degrees, and angles that combine into a right angle are called "
            "complementary while those combining into 180 are called "
            "supplementary. Every polygon in this database is built from "
            "segments, and every corner is an angle - learn these three "
            "atoms and the rest of geometry is carpentry."
        ),
        "how_it_works": (
            "Angles are measured by how much one ray must rotate to lie on "
            "the other: a full turn is 360 degrees, so a quarter turn is a "
            "right angle of 90. When a triangle is drawn and its three "
            "angles measured - say 60, 70, and 50 - the sum is always 180, "
            "no matter how the triangle is stretched: this is the triangle "
            "angle-sum theorem, the first great theorem of the database. "
            "Complementary pairs add to 90 (a 30-degree angle needs a "
            "60-degree partner); supplementary pairs add to 180 (110 needs "
            "70). The demonstration program verifies the triangle angle sum "
            "for several triangles, computes complementary and supplementary "
            "partners, and classifies sample angles as acute, right, or "
            "obtuse, proving the atom-set behaves exactly as described."
        ),
        "key_points": [
            "Points mark locations, line segments connect points, and angles measure the opening where two segments meet at a vertex.",
            "Angles come in four named sizes: acute (under 90 degrees), right (exactly 90), obtuse (between 90 and 180), and straight (exactly 180).",
            "The angles of any triangle sum to 180 degrees - the first theorem to memorize; it never fails.",
            "Complementary angles sum to 90 degrees; supplementary angles sum to 180 degrees.",
            "Polygons are built from line segments and their corners are angles: points, lines, and angles are the atoms everything else is made from.",
        ],
        "requirements": [
            "Points named with capital letters so locations can be referenced precisely in reasoning.",
            "A clear distinction between line (endless), segment (two endpoints), and ray (one endpoint, one direction).",
            "Angle measurement in degrees, with the four named sizes (acute, right, obtuse, straight) identified by range.",
            "The triangle angle-sum theorem stated as an unconditional fact: three angles of any triangle total 180 degrees.",
            "Complementary and supplementary defined as pair relationships, not as single-angle properties.",
        ],
        "standards": [
            "Point, line, and angle are the undefined and first-defined terms of the Euclidean system (Euclid, Elements, Book I, Definitions 1-8).",
            "Angle measurement in degrees and the classification of angles follow the Common Core geometry progression (4.MD, 7.G).",
            "The triangle angle-sum is proved as Proposition 32 of Euclid Book I.",
        ],
        "citations": [CIT_EUCLID, CIT_CC],
        "sig_lens": (
            "The Signature read: the point is the seed, the line the "
            "intention, the angle the measure of the turn. Where public "
            "geometry defines atoms, the Signature Geometry names the "
            "covenant: no shape is ever larger than the honesty of its "
            "corners."
        ),
    },
    {
        "key": "sides_vertices_corners",
        "name": "Counting Sides, Vertices, and Corners",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Every straight-edged shape can be described by counting: how "
            "many sides does it have, how many vertices, how many corners. "
            "A side is one straight segment of the boundary. A vertex is a "
            "point where two sides meet - vertices is the plural; one "
            "vertex, many vertices. In everyday speech people say corner, "
            "and for 2D shapes corner and vertex mean the same meeting "
            "point; in 3D work, vertex is the formal word and the shape has "
            "edges (where two faces meet) and faces (the flat surfaces) as "
            "well. The beautiful rule for polygons: a polygon always has "
            "the same number of sides and vertices - a triangle has 3 and "
            "3, a square 4 and 4, a pentagon 5 and 5, a hexagon 6 and 6, "
            "because each side is joined to the next at exactly one vertex. "
            "Counting is the first measurement a learner does: trace the "
            "shape with a finger, count the straight pieces, count the "
            "points where the finger turns, and the shape starts to tell "
            "you its name. This record also sets the 3D vocabulary - faces, "
            "edges, vertices - that the solid-shape records will use "
            "throughout the database."
        ),
        "how_it_works": (
            "Counting works because a polygon is a closed chain of "
            "segments: side 1 ends at a vertex, side 2 begins there, and "
            "after the last side the chain closes, so vertices and sides "
            "match one-for-one. To count, walk the boundary: each straight "
            "run is one side, each turning point is one vertex. For 3D "
            "shapes the walk becomes a survey: count the flat faces (a cube "
            "has 6), the edges where faces meet (a cube has 12), and the "
            "vertices where edges meet (a cube has 8). The demonstration "
            "program counts sides and vertices for polygons from triangle "
            "through octagon, verifies the equality holds for every one, "
            "and tallies the faces, edges, and vertices of the cube, the "
            "rectangular prism, and the square pyramid."
        ),
        "key_points": [
            "A side is one straight segment of a shape's boundary; a vertex is a point where two sides meet; corner is the everyday word for the same point.",
            "Every polygon has equal numbers of sides and vertices: the boundary is a closed chain, so each side brings exactly one vertex.",
            "In 3D the vocabulary grows: faces are the flat surfaces, edges are where two faces meet, vertices are where edges meet.",
            "Counting is the first measurement: trace, count the straight runs, count the turning points, and the shape names itself.",
            "Triangle 3/3, square 4/4, pentagon 5/5, hexagon 6/6 - the pattern is the rule, not a coincidence.",
        ],
        "requirements": [
            "The terms side, vertex/vertices, face, and edge defined before they are used, with corner acknowledged as the everyday synonym.",
            "The sides-equals-vertices rule stated for all polygons and demonstrated on at least triangles through octagons.",
            "The 3D vocabulary (faces, edges, vertices) introduced here so solid-shape records can use it without redefinition.",
            "Counting taught as a physical procedure: trace the boundary, count straight runs, count turning points.",
            "Plural forms given correctly: vertices, never vertexes in formal work.",
        ],
        "standards": [
            "The side/vertex/face/edge vocabulary follows Euclid's definitions of figure, side, and solid (Elements, Books I and XI).",
            "Distinguishing defining attributes (sides, vertices) from non-defining ones (color, size) is the Common Core K-2 geometry standard (K.G, 1.G, 2.G).",
            "Composing and decomposing shapes by counting parts matches the 1st-grade geometry progression.",
        ],
        "citations": [CIT_EUCLID, CIT_NCTM, CIT_CC],
        "sig_lens": (
            "The Signature read: counting is the first covenant-keeping - "
            "the finger walks the boundary and the shape confesses its "
            "number. Where public geometry counts features, the Signature "
            "Geometry counts witnesses: every vertex testifies that a side "
            "was there."
        ),
    },
    {
        "key": "circle_intro",
        "name": "The Circle",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The circle is the roundest shape: every point on its edge is "
            "exactly the same distance from the center. That single rule "
            "creates it. The vocabulary of the circle: the center is the "
            "middle point; the radius is the distance from the center to "
            "any point on the edge; the diameter is the distance straight "
            "across through the center, exactly twice the radius; the "
            "circumference is the distance around the edge; the interior is "
            "everything inside. A circle has no sides, no vertices, no "
            "corners - its edge is one smooth continuous curve, which is "
            "why it rolls perfectly. Circles are everywhere: wheels, coins, "
            "clocks, plates, the sun and moon in the sky, the pupil of an "
            "eye. Because it has no corners to catch, the circle is the "
            "shape of motion and flow - and the foundation of wheels, "
            "gears, and every rotating machine in the world."
        ),
        "how_it_works": (
            "A circle is constructed by fixing a center point and a radius "
            "length, then collecting every point at exactly that distance: "
            "a compass does this mechanically, one leg pinned at the "
            "center, the pencil leg sweeping the edge. Doubling the radius "
            "doubles the diameter (diameter equals 2 times radius), and the "
            "circumference is about 3.14159 times the diameter - that ratio "
            "is the number pi, studied in its own advanced record. The "
            "demonstration program takes a radius of 5, computes the "
            "diameter (10), the circumference (about 31.4159), and the area "
            "(about 78.5398), and verifies the diameter-doubling rule and "
            "the pi ratio within tight bounds."
        ),
        "key_points": [
            "A circle is the set of all points at one fixed distance (the radius) from a center point.",
            "The diameter is twice the radius; the circumference is the distance around; the area is pi times the radius squared.",
            "A circle has no sides, vertices, or corners - its single smooth edge is why it rolls without catching.",
            "Real examples: wheels, coins, clocks, plates, buttons, the sun and moon, pupils.",
            "The circle underlies all rotation: wheels, gears, pulleys, and bearings all begin as circles.",
        ],
        "requirements": [
            "The defining rule stated: every edge point equidistant from the center.",
            "The five vocabulary words defined: center, radius, diameter, circumference, interior.",
            "The diameter-radius doubling rule stated and demonstrated numerically.",
            "The absence of sides/vertices/corners stated explicitly, with the rolling consequence explained.",
            "At least five real-world examples named from everyday life.",
        ],
        "standards": [
            "The circle is defined as a plane figure contained by one line such that all straight lines falling upon it from a point within are equal (Euclid, Elements, Book I, Definition 15).",
            "Radius/diameter vocabulary and the 2-to-1 relationship are the Common Core 7th-grade circle standard (7.G).",
            "Circle construction with a compass is the classical straightedge-and-compass method of Book I.",
        ],
        "citations": [CIT_EUCLID, CIT_CC],
        "sig_lens": (
            "The Signature read: the circle is the oath of return - the "
            "only shape that ends where it begins without a single corner. "
            "Where public geometry measures the radius, the Signature "
            "Geometry honors the promise: every point keeps the same "
            "distance, no exceptions, no favorites."
        ),
    },
    {
        "key": "triangle_intro",
        "name": "The Triangle",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The triangle is the simplest polygon: three sides, three "
            "vertices, three angles - and no polygon can have fewer. It is "
            "also the strongest shape in engineering: push a square and it "
            "folds into a diamond, but push a triangle and it holds, because "
            "three fixed side-lengths determine exactly one shape. "
            "Triangles sort by their sides: an equilateral triangle has all "
            "three sides equal (and all three angles 60 degrees); an "
            "isosceles triangle has two equal sides (and the angles opposite "
            "them equal); a scalene triangle has all sides different. They "
            "also sort by their angles: an acute triangle has all angles "
            "under 90 degrees; a right triangle has one 90-degree angle "
            "(the side opposite it is the hypotenuse, the longest side); an "
            "obtuse triangle has one angle over 90. The area of a triangle "
            "is half the base times the height. Triangles appear in "
            "bridge trusses, roof frames, bicycle frames, sail shapes, "
            "yield signs, and pizza slices - anywhere strength or a "
            "three-cornered marker is wanted."
        ),
        "how_it_works": (
            "Three segments form a triangle exactly when the longest is "
            "shorter than the other two put together - otherwise the ends "
            "cannot meet. Once built, the triangle is rigid: unlike a "
            "four-sided frame, it cannot change its angles without changing "
            "a side length, which is why trusses are triangulated. Area "
            "comes from the rectangle: a triangle is half of the rectangle "
            "with the same base and height, so area equals one-half times "
            "base times height. The demonstration program classifies sample "
            "triangles by sides and angles, checks the 3-4-5 right triangle "
            "(perimeter 12, area 6, angles summing to 180), and computes the "
            "area of a triangle with base 10 and height 6 (30)."
        ),
        "key_points": [
            "A triangle is the simplest polygon: 3 sides, 3 vertices, 3 angles summing to 180 degrees.",
            "By sides: equilateral (all equal), isosceles (two equal), scalene (all different); by angles: acute, right (one 90-degree angle), obtuse.",
            "The right triangle's longest side is the hypotenuse, opposite the right angle.",
            "Triangles are rigid - three fixed side lengths make exactly one shape, which is why bridges and roofs are triangulated.",
            "Area is one-half times base times height; the 3-4-5 triangle has area 6 and perimeter 12.",
        ],
        "requirements": [
            "The triangle introduced as the simplest polygon with the 3/3/3 counts stated.",
            "Both classification systems given: by sides (equilateral, isosceles, scalene) and by angles (acute, right, obtuse).",
            "The hypotenuse defined as the side opposite the right angle and the longest side.",
            "Rigidity explained as the engineering reason triangles appear in structures.",
            "The area formula (one-half base times height) stated with a worked numerical example.",
        ],
        "standards": [
            "The triangle is the first rectilineal figure of Euclid Book I (Definitions 19-20; Propositions 1-26).",
            "Side and angle classification of triangles is the Common Core 4th/5th-grade geometry standard (4.G, 5.G).",
            "The triangle angle-sum and the right-triangle relationships are proved in Elements I.32 and I.47.",
        ],
        "citations": [CIT_EUCLID, CIT_CC],
        "sig_lens": (
            "The Signature read: the triangle is the threefold witness - "
            "the smallest company that can swear a shape into being. Where "
            "public geometry proves rigidity, the Signature Geometry names "
            "the oath: three sides, three witnesses, no wavering, which is "
            "why bridges trust it."
        ),
    },
    {
        "key": "square_intro",
        "name": "The Square",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The square is the most regular four-sided shape: all four "
            "sides equal, all four angles right angles (90 degrees each). "
            "It is the shape of tiles, chessboards, window panes, sticky "
            "notes, and dice faces. Because every side matches and every "
            "corner is square, the square is the unit of measurement for "
            "area itself - area is counted in square units (square inches, "
            "square meters) precisely because the square is the fairest "
            "tile: it covers a surface with no gaps and no overlaps when "
            "repeated. The perimeter of a square is four times its side "
            "length; the area is the side length times itself (side "
            "squared); the diagonal - the line from one corner to the "
            "opposite - is the side length times the square root of 2 "
            "(about 1.4142), and it cuts the square into two equal right "
            "triangles. A square is also a special rectangle, a special "
            "rhombus, and a regular quadrilateral: it sits at the center "
            "of the quadrilateral family, which the later record explores."
        ),
        "how_it_works": (
            "A square is constructed by drawing a segment, erecting "
            "perpendiculars at both ends of equal length, and joining the "
            "tops - the right angles guarantee the top is parallel to the "
            "bottom and equal in length. Its measurements all derive from "
            "the single side length s: perimeter 4s, area s-squared, "
            "diagonal s times the square root of 2 (by the Pythagorean "
            "theorem applied to the half-square triangle). The "
            "demonstration program takes side 7, computes the perimeter "
            "(28), the area (49), and the diagonal (about 9.8995), and "
            "verifies the diagonal's square equals twice the side's square "
            "(98) within tight bounds."
        ),
        "key_points": [
            "A square has four equal sides and four right angles - the most regular quadrilateral.",
            "Perimeter is 4 times the side; area is the side squared; the diagonal is the side times the square root of 2.",
            "The square is the unit of area: area is counted in square units because the square tiles perfectly with no gaps.",
            "A square is a special rectangle, a special rhombus, and a regular quadrilateral all at once.",
            "Real examples: floor tiles, chessboard squares, window panes, sticky notes, dice faces.",
        ],
        "requirements": [
            "The square defined by both conditions: four equal sides AND four right angles.",
            "Perimeter, area, and diagonal formulas stated with the side length as the single input.",
            "The square named as the unit of area measurement, with the tiling reason given.",
            "The square's place in the quadrilateral family previewed (special rectangle, special rhombus, regular quadrilateral).",
            "At least four real-world examples named.",
        ],
        "standards": [
            "The square is defined in Euclid Book I (Definition 22) as a quadrilateral both equilateral and right-angled.",
            "Classifying squares by side and angle attributes is the Common Core 3rd-5th grade standard (3.G, 4.G, 5.G).",
            "The diagonal relationship is the Pythagorean theorem, Elements I.47.",
        ],
        "citations": [CIT_EUCLID, CIT_CC],
        "sig_lens": (
            "The Signature read: the square is the honest measure - the "
            "shape that keeps all four sides equal and all four corners "
            "true. Where public geometry counts area in square units, the "
            "Signature Geometry says why: fairness tiles the world, and "
            "the square is fairness drawn."
        ),
    },
    {
        "key": "rectangle_intro",
        "name": "The Rectangle",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "A rectangle is a four-sided shape with four right angles; its "
            "opposite sides are equal, but unlike the square the adjacent "
            "sides may differ - one pair can be long, the other short. It "
            "is the shape of doors, books, phone screens, paper sheets, "
            "television screens, and playing fields. The perimeter is twice "
            "the length plus twice the width; the area is length times "
            "width - the most-used area formula in everyday life, from "
            "carpet to paint to farmland. The diagonal is found with the "
            "Pythagorean theorem: the square root of length-squared plus "
            "width-squared. Every square is a rectangle (it has four right "
            "angles), but not every rectangle is a square - the square is "
            "the special rectangle whose sides are all equal. The rectangle "
            "is the workhorse of measurement: floor plans, fields, and "
            "screens are all rectangles first."
        ),
        "how_it_works": (
            "A rectangle is built from a length and a width joined at right "
            "angles: opposite sides run parallel and equal because each "
            "corner is 90 degrees. Its measurements derive from the two "
            "numbers: perimeter 2 times (length plus width), area length "
            "times width, diagonal the square root of (length-squared plus "
            "width-squared). The area formula is the counting of unit "
            "squares: an 8-by-5 rectangle holds exactly 40 one-by-one "
            "squares in 8 columns and 5 rows. The demonstration program "
            "takes length 8 and width 5, computes the perimeter (26), the "
            "area (40), and the diagonal (about 9.4340), and verifies the "
            "diagonal squared equals 89 within tight bounds."
        ),
        "key_points": [
            "A rectangle has four right angles with opposite sides equal; adjacent sides may differ in length.",
            "Perimeter is 2 times (length plus width); area is length times width; the diagonal is the square root of (length-squared plus width-squared).",
            "Every square is a rectangle, but not every rectangle is a square - the square is the equal-sided special case.",
            "The rectangle is the workhorse of real measurement: rooms, fields, screens, and paper are all measured as rectangles.",
            "Real examples: doors, books, phone screens, paper sheets, playing fields.",
        ],
        "requirements": [
            "The rectangle defined by four right angles, with the opposite-sides-equal property stated.",
            "The square-as-special-rectangle relationship stated in both directions.",
            "Perimeter, area, and diagonal formulas given with a worked numerical example.",
            "The area formula justified as counting unit squares in rows and columns.",
            "At least four real-world examples named.",
        ],
        "standards": [
            "The rectangle (oblong) is defined in Euclid Book I, Definition 22, as right-angled but not equilateral.",
            "Rectangle area as length times width and its use in real measurement is the Common Core 3rd-4th grade standard (3.MD, 4.MD).",
            "The diagonal is an application of the Pythagorean theorem, Elements I.47.",
        ],
        "citations": [CIT_EUCLID, CIT_CC],
        "sig_lens": (
            "The Signature read: the rectangle is the covenant of the "
            "frame - four right angles kept, opposite sides faithful, the "
            "long and the short each honored. Where public geometry "
            "measures rooms and fields, the Signature Geometry names the "
            "promise: a true corner never leans."
        ),
    },
    {
        "key": "other_quadrilaterals",
        "name": "Other Quadrilaterals: Parallelogram, Rhombus, Trapezoid, Kite",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Quadrilateral means four-sided, and the family is bigger than "
            "squares and rectangles. A parallelogram has both pairs of "
            "opposite sides parallel (and equal); push a rectangle sideways "
            "and you get one - its angles are no longer right, but opposite "
            "angles match. A rhombus is a parallelogram with all four sides "
            "equal - a pushed-over square, like a baseball diamond. A "
            "trapezoid has exactly one pair of parallel sides (the "
            "American definition used here), like a tabletop wider at the "
            "base or a megaphone's silhouette. A kite has two pairs of "
            "adjacent equal sides - the toy kite shape, with one diagonal "
            "cutting the other at a right angle. All quadrilaterals share "
            "one law: their four interior angles always sum to 360 degrees, "
            "because every quadrilateral can be split into two triangles. "
            "Real examples: parallelograms in folding gates and "
            "escalator steps, rhombuses in playing-card diamonds, "
            "trapezoids in handbags and bridge supports, kites in - of "
            "course - kites."
        ),
        "how_it_works": (
            "Each quadrilateral is defined by which parallelisms and "
            "equalities it keeps: the square keeps them all, the "
            "parallelogram keeps parallel opposite sides, the rhombus adds "
            "equal sides, the trapezoid keeps a single parallel pair, the "
            "kite keeps adjacent equal pairs. The 360-degree angle sum is "
            "proved by drawing one diagonal: it splits the quadrilateral "
            "into two triangles, each contributing 180 degrees. Area of a "
            "parallelogram is base times vertical height (a slanted copy of "
            "the rectangle's rule). The demonstration program verifies the "
            "360-degree sum on sample angle sets for each of the four "
            "shapes, and computes a parallelogram area from base 9 and "
            "height 4 (36)."
        ),
        "key_points": [
            "Quadrilateral means four-sided: the family includes squares, rectangles, parallelograms, rhombuses, trapezoids, and kites.",
            "A parallelogram has both opposite pairs parallel; a rhombus is an equal-sided parallelogram; a trapezoid has exactly one parallel pair; a kite has two adjacent equal pairs.",
            "Every quadrilateral's interior angles sum to 360 degrees, because one diagonal splits it into two 180-degree triangles.",
            "A parallelogram's area is base times vertical height - the rectangle's rule, sheared sideways.",
            "The square sits at the center of the family: it satisfies every other quadrilateral's definition at once.",
        ],
        "requirements": [
            "Each of the four shapes defined by its parallel/equal-side conditions, using the one-parallel-pair trapezoid definition.",
            "The 360-degree interior angle sum stated and proved via the diagonal-into-two-triangles argument.",
            "The square's membership in every sub-family stated (special rectangle, special rhombus, special parallelogram).",
            "The parallelogram area rule (base times vertical height) given with a numerical example.",
            "Real-world examples named for each shape.",
        ],
        "standards": [
            "Parallelogram, rhombus, and trapezoid definitions follow Euclid Book I, Definitions 22-23, with the modern inclusive/exclusive trapezoid convention stated.",
            "Classifying quadrilaterals by parallel and perpendicular sides and angle size is the Common Core 4th-grade standard (4.G).",
            "The 360-degree angle sum follows from Elements I.32 applied to the two triangles of the diagonal.",
        ],
        "citations": [CIT_EUCLID, CIT_CC],
        "sig_lens": (
            "The Signature read: the quadrilateral family is the covenant "
            "tested four ways - pushed, sheared, narrowed, and kited - and "
            "still every member keeps the 360-degree oath. Where public "
            "geometry classifies, the Signature Geometry witnesses: loyalty "
            "survives the slant."
        ),
    },
    {
        "key": "measuring_length",
        "name": "Measuring Length: Units and the Ruler",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "A shape's sides are not just counted - they are measured, and "
            "measurement needs units. The metric system measures length in "
            "millimeters, centimeters, meters, and kilometers: 10 "
            "millimeters make a centimeter, 100 centimeters make a meter, "
            "1000 meters make a kilometer. The customary system used in "
            "the United States measures in inches, feet, yards, and miles: "
            "12 inches make a foot, 3 feet make a yard, 1760 yards make a "
            "mile. To measure a segment, lay a ruler's zero mark at one "
            "endpoint and read the number at the other; for curves like a "
            "circle's circumference, a flexible tape follows the edge. "
            "Estimation comes first and checking second: guess, then "
            "measure, then compare. Area uses square units (square "
            "centimeters, square inches) and volume uses cubic units, "
            "because length times length is a square and length times "
            "length times length is a cube. Every measurement in this "
            "database - every perimeter, area, and volume - rests on this "
            "record's foundation."
        ),
        "how_it_works": (
            "Measurement converts a physical extent into a number by "
            "comparison with a unit: the ruler is a row of units laid "
            "against the object. Conversion multiplies or divides by the "
            "unit ratio: 2.5 meters times 100 centimeters per meter is 250 "
            "centimeters; 36 inches divided by 12 inches per foot is 3 feet. "
            "When two lengths multiply (length times width), the units "
            "multiply too - centimeters times centimeters become square "
            "centimeters - which is why area and volume carry their "
            "squared and cubed units honestly. The demonstration program "
            "converts 2.5 meters to centimeters (250), 36 inches to feet "
            "(3), and computes the area of a 3-by-4-meter rectangle (12 "
            "square meters), verifying each within tight bounds."
        ),
        "key_points": [
            "Length is measured by comparing against a unit: metric (mm, cm, m, km) or customary (in, ft, yd, mi).",
            "Unit ratios are exact: 100 cm per m, 12 in per ft, 3 ft per yd; conversion is multiplication or division by the ratio.",
            "Area carries square units and volume carries cubic units, because the units multiply exactly like the numbers.",
            "Measure with a ruler zeroed at the endpoint; use a flexible tape for curves; estimate first, then check.",
            "Every perimeter, area, and volume in this database is a length measurement at heart.",
        ],
        "requirements": [
            "Both unit systems given with their exact conversion ratios.",
            "The ruler procedure described: zero at one endpoint, read at the other; flexible tape for curves.",
            "Square and cubic units explained as the honest product of length units.",
            "The estimate-then-measure habit taught as the checking discipline.",
            "Numerical conversion examples worked: metric and customary.",
        ],
        "standards": [
            "Measuring lengths with standard units and converting within systems is the Common Core 2nd-5th grade measurement standard (2.MD, 4.MD, 5.MD).",
            "Square and cubic units as products of length units follow the dimensional analysis of the measurement standards.",
            "Estimation before measurement is the NCTM measurement standard practice.",
        ],
        "citations": [CIT_NCTM, CIT_CC],
        "sig_lens": (
            "The Signature read: the ruler is the covenant made visible - "
            "a row of kept promises laid against the unknown. Where public "
            "measurement compares and converts, the Signature Geometry "
            "insists the unit itself is an oath: a centimeter that lied "
            "would unmake every bridge."
        ),
    },
    {
        "key": "shapes_around_us",
        "name": "Shapes in the World Around Us",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Shapes are not confined to textbooks - the world is built from "
            "them. Look around any room: circles in clocks and cups, "
            "rectangles in doors and screens, squares in tiles and "
            "windows, triangles in roof peaks and shelf brackets. Step "
            "outside: spheres in balls and oranges, cylinders in cans and "
            "tree trunks, cones in traffic cones and ice-cream cones, "
            "pyramids in ancient monuments and modern rooftops, cubes in "
            "boxes and building blocks. Nature builds with shapes too: "
            "honeycomb hexagons, snowflake sixfold symmetry, the spherical "
            "sun and moon, cylindrical bamboo. Engineers choose shapes for "
            "their properties - triangles for strength in bridges, "
            "cylinders for rolling in wheels, spheres for even pressure in "
            "tanks - so recognizing shapes is the first step toward "
            "understanding why things are built the way they are. This "
            "record closes the foundations tier: the learner can now name "
            "shapes, count their features, measure their sides, and spot "
            "them in the wild."
        ),
        "how_it_works": (
            "Shape-spotting works by running the classification questions "
            "from the first record on real objects: is it flat or solid, "
            "curved or straight-edged, how many sides or faces. A soup can "
            "answers solid, curved side, two circular ends - a cylinder. A "
            "door answers flat, straight edges, four sides with right "
            "angles - a rectangle. The same questions work on buildings, "
            "tools, food, and nature, which is why geometry transfers from "
            "paper to the world without change. The demonstration program "
            "takes a shelf of 20 everyday objects, classifies each into "
            "its shape family, and tallies the families - showing the "
            "10 foundational shapes accounting for the whole shelf of 20, with "
            "shares computed and verified."
        ),
        "key_points": [
            "Everyday objects are shapes in disguise: cans are cylinders, doors are rectangles, balls are spheres, boxes are cubes.",
            "Nature builds with shapes: honeycomb hexagons, snowflake symmetry, spherical celestial bodies, cylindrical plant stems.",
            "Engineers choose shapes for properties: triangles for strength, cylinders for rolling, spheres for even pressure.",
            "The same classification questions work on paper drawings and real objects - geometry transfers to the world unchanged.",
            "Spotting shapes in the wild is the payoff of the foundations tier: name, count, measure, recognize.",
        ],
        "requirements": [
            "At least three real examples given for each of the ten core shapes (circle, triangle, square, rectangle, polygons, cube, sphere, cylinder, cone, pyramid).",
            "Nature examples included alongside manufactured ones.",
            "The engineering reason for at least three shape choices stated (strength, rolling, pressure).",
            "The classification questions from the first record reused on real objects.",
            "The foundations tier explicitly closed: name, count, measure, recognize.",
        ],
        "standards": [
            "Identifying shapes in the environment is the Common Core kindergarten-through-grade-2 geometry standard (K.G, 1.G, 2.G).",
            "Describing the real world with geometric shapes and measures is the Common Core modeling practice (4.MD, 7.G).",
            "The NCTM geometry standard calls for analyzing characteristics of shapes in both mathematical and real-world contexts.",
        ],
        "citations": [CIT_NCTM, CIT_CC],
        "sig_lens": (
            "The Signature read: the world is the signature written "
            "large - cans, doors, honeycombs, and moons all keeping the "
            "same covenants of form. Where public geometry finds examples, "
            "the Signature Geometry finds testimony: the shapes out there "
            "are the shapes in here, sworn twice."
        ),
    },
    {
        "key": "pentagon_hexagon",
        "name": "Polygons: The Pentagon and the Hexagon",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Beyond quadrilaterals the polygons march on, and the next two "
            "are the most famous. A pentagon has 5 sides and 5 vertices; a "
            "hexagon has 6 and 6. The regular pentagon - all sides equal, "
            "all angles equal - is the shape of the home plate in baseball "
            "and the headquarters building that bears its name. The "
            "regular hexagon is nature's favorite tile: honeycomb cells are "
            "hexagons because six-sided cells share walls with no wasted "
            "space, and snowflakes grow with sixfold symmetry. The interior "
            "angles of any pentagon sum to 540 degrees (3 times 180), and "
            "of any hexagon to 720 degrees (4 times 180) - each new side "
            "adds one more triangle's worth, 180 degrees. In a regular "
            "pentagon each interior angle is 108 degrees; in a regular "
            "hexagon each is 120 degrees. The hexagon has a lovely secret: "
            "a regular hexagon is exactly six equilateral triangles around "
            "a center point, which is why its side length equals its "
            "radius."
        ),
        "how_it_works": (
            "The interior-angle sum for any n-sided polygon is (n minus 2) "
            "times 180 degrees: pick one vertex and draw diagonals to all "
            "non-adjacent vertices, which carves the polygon into exactly "
            "n minus 2 triangles. For the pentagon that is 3 triangles "
            "(540 degrees); for the hexagon, 4 (720 degrees). In a regular "
            "polygon all interior angles are equal, so each is the sum "
            "divided by n: 540 divided by 5 is 108, 720 divided by 6 is "
            "120. The demonstration program computes the angle sums and "
            "per-angle values for the pentagon and hexagon, verifies the "
            "hexagon's six-triangle decomposition (6 times 60-degree "
            "center angles equals 360), and confirms each result within "
            "tight bounds."
        ),
        "key_points": [
            "A pentagon has 5 sides/vertices; a hexagon has 6; both follow the sides-equals-vertices polygon rule.",
            "The interior-angle sum of an n-gon is (n-2) times 180 degrees: 540 for the pentagon, 720 for the hexagon.",
            "Regular pentagon: each interior angle 108 degrees; regular hexagon: each 120 degrees.",
            "A regular hexagon is six equilateral triangles around a center - its side equals its radius.",
            "Real examples: pentagon in home plate and the Pentagon building; hexagon in honeycomb and snowflakes.",
        ],
        "requirements": [
            "Both shapes defined by side/vertex counts with the regular forms distinguished.",
            "The (n-2) times 180 interior-angle-sum rule stated, derived via the triangle-carving argument, and applied to both.",
            "Per-angle values for the regular forms computed (108 and 120 degrees).",
            "The hexagon's six-equilateral-triangle structure stated with the side-equals-radius consequence.",
            "Real-world examples named for each shape, including the honeycomb reason.",
        ],
        "standards": [
            "The pentagon and hexagon are constructed in Euclid Book IV (Propositions 11-12) as figures inscribed in circles.",
            "The interior-angle-sum rule is the polygon generalization of Elements I.32.",
            "Drawing polygons with given attributes is the Common Core 5th-grade standard (5.G).",
        ],
        "citations": [CIT_EUCLID, CIT_CC],
        "sig_lens": (
            "The Signature read: the pentagon is the covenant of five - "
            "the home plate where the game is decided - and the hexagon is "
            "the covenant the bees keep, six walls sharing everything. "
            "Where public geometry counts to five and six, the Signature "
            "Geometry hears the larger oath: nature wastes nothing."
        ),
    },
    {
        "key": "more_polygons",
        "name": "Polygons: Heptagon through Decagon and the n-gon",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The polygon family continues: a heptagon has 7 sides, an "
            "octagon 8, a nonagon 9, a decagon 10 - and the pattern never "
            "stops, because an n-gon is simply a polygon with n sides, for "
            "any n of 3 or more. The octagon is the most familiar of this "
            "group: the stop sign is a regular octagon, chosen because its "
            "distinctive shape reads at a glance even when the words are "
            "obscured. The same interior-angle rule governs them all: "
            "(n minus 2) times 180 degrees, so the heptagon's angles sum to "
            "900, the octagon's to 1080, the nonagon's to 1260, and the "
            "decagon's to 1440. The exterior angle - the turn you make when "
            "walking around the polygon - is even simpler: for a regular "
            "n-gon it is 360 divided by n, and the n exterior angles always "
            "sum to exactly 360 degrees, one full turn. As n grows, the "
            "regular polygon looks more and more like a circle - the "
            "hundred-gon is nearly indistinguishable from one, which "
            "foreshadows the circle records' limit ideas."
        ),
        "how_it_works": (
            "Walking around any polygon and turning at each vertex, the "
            "walker makes exactly one full rotation by the time the walk "
            "closes - that is why the exterior angles always sum to 360 "
            "degrees, for every polygon, regular or not. For a regular "
            "n-gon the turn is the same at each vertex, so each exterior "
            "angle is 360 divided by n: the octagon's is 45 degrees, the "
            "decagon's 36. The interior angle is the supplement: 180 minus "
            "the exterior, so the regular octagon's interior angle is 135 "
            "degrees. The demonstration program computes interior sums and "
            "per-angle values for n = 7 through 10, verifies each exterior "
            "angle times n equals 360, and checks the octagon's interior "
            "angle at 135 degrees, all within tight bounds."
        ),
        "key_points": [
            "Heptagon 7, octagon 8, nonagon 9, decagon 10 sides; the n-gon generalizes the family to any n of 3 or more.",
            "Interior-angle sum is (n-2) times 180: 900, 1080, 1260, 1440 degrees for n = 7, 8, 9, 10.",
            "Exterior angles of any polygon sum to 360 degrees - one full turn of the walk; for a regular n-gon each is 360/n.",
            "The stop sign is a regular octagon: distinctive shape chosen to read at a glance.",
            "As n grows the regular n-gon approaches the circle - the many-sided bridge to roundness.",
        ],
        "requirements": [
            "Each polygon from heptagon to decagon defined by its side count.",
            "The n-gon introduced as the general form for any n of 3 or more.",
            "Interior sums computed for n = 7 through 10 via the (n-2) times 180 rule.",
            "The exterior-angle 360-degree sum stated with the walking-turn justification, and per-angle values for the regular forms.",
            "The polygon-approaches-circle observation stated as foreshadowing.",
        ],
        "standards": [
            "The general n-gon interior-angle-sum is the polygon extension of Euclid I.32.",
            "The exterior-angle sum of 360 degrees is proved in the Euclidean tradition via the parallel postulate.",
            "Classifying and drawing polygons with specified attributes is the Common Core 5th-grade standard (5.G).",
        ],
        "citations": [CIT_EUCLID, CIT_CC],
        "sig_lens": (
            "The Signature read: the n-gon is the covenant without "
            "ceiling - three sides or three thousand, the same oath binds "
            "them. Where public geometry marches the numbers upward, the "
            "Signature Geometry watches the polygon lean toward the circle "
            "and calls it aspiration."
        ),
    },
    {
        "key": "regular_irregular",
        "name": "Regular and Irregular Polygons",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Not all polygons with the same number of sides are alike: a "
            "square and a lopsided four-sided figure are both "
            "quadrilaterals, but only one is regular. A regular polygon has "
            "all sides equal AND all angles equal - both conditions, "
            "always. The equilateral triangle, the square, the regular "
            "pentagon, the regular hexagon, and the regular octagon are the "
            "famous regulars. An irregular polygon breaks one or both "
            "conditions: a rectangle is irregular (angles equal, sides not "
            "all equal), a rhombus is irregular (sides equal, angles not "
            "all equal) - only the square, keeping both, is the regular "
            "quadrilateral. Regular polygons are special because their "
            "symmetry is perfect: every regular n-gon has exactly n lines "
            "of mirror symmetry and n-fold rotational symmetry, and each "
            "one fits perfectly inside a circle (all vertices on one "
            "circle) and around a circle (all sides tangent to one "
            "circle). The regular polygons are the aristocrats of the "
            "flat world - and exactly three of them (triangle, square, "
            "hexagon) tile a floor with no gaps, a fact tilers have used "
            "for millennia."
        ),
        "how_it_works": (
            "Regularity is tested with two checks: measure all side lengths "
            "- are they equal; measure all interior angles - are they "
            "equal. Pass both and the polygon is regular. Because all "
            "vertices of a regular polygon lie at equal angular spacing "
            "around the center, the polygon inherits the circle's symmetry: "
            "reflect across any line through the center and a vertex (or an "
            "edge midpoint) and it maps onto itself, giving n mirror lines "
            "for the n-gon; rotate by 360 divided by n and it coincides, "
            "giving n-fold rotation. The demonstration program tests "
            "sample polygons for regularity (square passes, rectangle fails "
            "the side check, rhombus fails the angle check), verifies the "
            "regular hexagon's interior angle at 120 degrees, and confirms "
            "the symmetry counts for the regular pentagon (5 and 5)."
        ),
        "key_points": [
            "Regular means all sides equal AND all angles equal - both conditions are required.",
            "The square is the only regular quadrilateral; rectangles and rhombuses are irregular (each fails one condition).",
            "Every regular n-gon has n lines of mirror symmetry and n-fold rotational symmetry.",
            "Regular polygons fit perfectly in a circle (vertices on it) and around a circle (sides tangent to it).",
            "Only the equilateral triangle, square, and regular hexagon tile the plane with no gaps.",
        ],
        "requirements": [
            "Regularity defined by the double condition, with the rectangle/rhombus counterexamples given.",
            "The square identified as the unique regular quadrilateral.",
            "Symmetry counts stated for the general regular n-gon (n mirror lines, n-fold rotation).",
            "The inscribed/circumscribed circle properties stated.",
            "The three regular tilings named (triangle, square, hexagon).",
        ],
        "standards": [
            "Regular figures are defined in Euclid Book I, Definition 22, and constructed in Book IV.",
            "Distinguishing regular from irregular polygons by side and angle attributes is the Common Core 3rd-4th grade standard (3.G, 4.G).",
            "Line symmetry in two-dimensional figures is the Common Core 4th-grade standard (4.G).",
        ],
        "citations": [CIT_EUCLID, CIT_CC],
        "sig_lens": (
            "The Signature read: the regular polygon is the covenant kept "
            "twice - equal sides and equal angles, no exceptions. Where "
            "public geometry tests two conditions, the Signature Geometry "
            "names the double oath: the regulars are the shapes that "
            "refuse to play favorites."
        ),
    },
    {
        "key": "perimeter",
        "name": "Perimeter: The Distance Around",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The perimeter is the total distance around a shape - the "
            "length of the walk that starts at one point, follows the "
            "boundary all the way around, and returns to the start. For "
            "polygons it is simply the sum of the side lengths: add every "
            "side and you have walked the whole edge. For regular polygons "
            "the sum shortens to multiplication: a regular n-gon with side "
            "s has perimeter n times s. For circles the perimeter has its "
            "own name, circumference, and its own formula, pi times the "
            "diameter. Perimeter answers practical questions: how much "
            "fence for the yard, how much trim for the room, how much "
            "ribbon for the box. It is measured in length units - meters, "
            "feet, inches - never square units, because it is a distance, "
            "not a covering. Two shapes can share a perimeter while having "
            "wildly different areas: a long thin 1-by-9 rectangle and a "
            "5-by-5 square both have perimeter 20, but their areas are 9 "
            "and 25 - a warning that perimeter and area are independent "
            "measures."
        ),
        "how_it_works": (
            "Perimeter is additive: walk each side, accumulate the "
            "distances, and the total is the boundary length regardless of "
            "the shape's complexity - even an L-shaped polygon surrenders "
            "to addition. For a rectangle the opposite sides pair up, so "
            "the sum collapses to 2 times (length plus width); for a "
            "regular polygon all sides are equal, so it collapses to n "
            "times s. The demonstration program computes the perimeter of "
            "an L-shaped hexagon (sides 6, 4, 2, 2, 4, 2 - total 20), a "
            "rectangle 8 by 5 (26), a regular pentagon of side 7 (35), and "
            "verifies the 1-by-9 rectangle and 5-by-5 square share "
            "perimeter 20 while their areas differ (9 versus 25)."
        ),
        "key_points": [
            "Perimeter is the distance around a shape: the sum of all side lengths for polygons.",
            "Shortcuts: rectangle 2 times (length plus width); regular n-gon n times side; circle pi times diameter (circumference).",
            "Perimeter is measured in length units (meters, feet), never square units.",
            "Perimeter answers fencing, trim, and edging questions - the boundary, not the covering.",
            "Equal perimeter does not mean equal area: a 1-by-9 rectangle and a 5-by-5 square both have perimeter 20, with areas 9 and 25.",
        ],
        "requirements": [
            "Perimeter defined as the boundary-walk distance, additive over sides.",
            "The three shortcut formulas given: rectangle, regular polygon, circle (named circumference).",
            "Length units required, with the square-units confusion explicitly warned against.",
            "A practical application named (fencing, trim, ribbon).",
            "The equal-perimeter-different-area example worked numerically.",
        ],
        "standards": [
            "Finding perimeter by adding side lengths and using the rectangle formula is the Common Core 3rd-4th grade standard (3.MD, 4.MD).",
            "Solving real-world problems involving perimeter is the Common Core modeling standard (4.MD).",
            "The circumference as pi times diameter is the 7th-grade circle standard (7.G).",
        ],
        "citations": [CIT_CC, CIT_NCTM],
        "sig_lens": (
            "The Signature read: the perimeter is the walk of the "
            "covenant - the full patrol of the boundary, no shortcut, no "
            "skipped side. Where public geometry adds the sides, the "
            "Signature Geometry honors the walk: the shape is only as "
            "honest as its whole edge."
        ),
    },
    {
        "key": "area_rect_square",
        "name": "Area of Rectangles and Squares",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Area measures covering: how many unit squares it takes to tile "
            "a shape with no gaps and no overlaps. The rectangle is where "
            "area begins, because its area is found by counting: a "
            "rectangle 8 units long and 5 units wide holds exactly 8 "
            "columns of 5 unit squares - 40 in all - so the area is length "
            "times width. The square is the special case: side times side, "
            "side squared, which is why the second power is called "
            "squaring. Area is counted in square units: square centimeters, "
            "square inches, square meters - the unit itself is a tiny "
            "square, the fairest tile. This one formula powers enormous "
            "parts of life: carpet and paint are sold by the square foot, "
            "farmland by the acre (43,560 square feet), countries by the "
            "square kilometer. And the rectangle's area is the seed of all "
            "other area formulas: the triangle is half a rectangle, the "
            "parallelogram is a sheared rectangle, and the circle's area "
            "can be understood by rearranging it into a near-rectangle."
        ),
        "how_it_works": (
            "The counting argument is the proof: lay a grid of unit "
            "squares over the rectangle; each row holds exactly length "
            "squares and there are width rows, so the total is the product. "
            "For whole-number sides this is exact; for fractional sides "
            "the same product holds by the same covering logic applied to "
            "fractional unit squares. The demonstration program tiles a "
            "12-by-9 rectangle by counting (108 unit squares), computes a "
            "square of side 11 (121), verifies that doubling one side of "
            "a rectangle doubles its area (6-by-4 is 24, 12-by-4 is 48), "
            "and confirms all values within tight bounds."
        ),
        "key_points": [
            "Area counts the unit squares needed to tile a shape with no gaps and no overlaps.",
            "Rectangle area is length times width; square area is side squared - the origin of the word squaring.",
            "Area is measured in square units: square centimeters, square inches, square meters, acres.",
            "Doubling one side of a rectangle doubles its area; doubling both quadruples it.",
            "The rectangle's area is the seed formula: triangle, parallelogram, and circle areas all derive from it.",
        ],
        "requirements": [
            "Area defined as unit-square covering with the no-gaps-no-overlaps condition.",
            "The rectangle formula justified by the row-and-column counting argument.",
            "Square units explained, with at least three named (square centimeter, square inch, acre).",
            "The doubling behaviors stated and demonstrated numerically.",
            "The seed-formula claim stated, naming triangle, parallelogram, and circle as descendants.",
        ],
        "standards": [
            "Tiling with unit squares and the length-times-width formula is the Common Core 3rd-4th grade standard (3.MD, 4.MD).",
            "Applying area to real-world problems (carpet, paint, land) is the Common Core modeling standard.",
            "The acre as 43,560 square feet is the standard customary land unit.",
        ],
        "citations": [CIT_CC, CIT_NCTM],
        "sig_lens": (
            "The Signature read: the rectangle's area is the covenant of "
            "the harvest - rows and columns counted honestly, nothing "
            "hidden, nothing double-counted. Where public geometry "
            "multiplies length by width, the Signature Geometry sees the "
            "field: every square unit accounted for, like grain in the "
            "storehouse."
        ),
    },
    {
        "key": "area_triangle",
        "name": "Area of Triangles",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "A triangle's area is half the area of the rectangle with the "
            "same base and height: area equals one-half times base times "
            "height. The reason is visible - draw the rectangle around the "
            "triangle using its base and its vertical height, and the "
            "triangle occupies exactly half, because the rectangle's "
            "diagonal (or the triangle's own altitude construction) splits "
            "it into two equal parts. The height must be the perpendicular "
            "height: the shortest distance from the base line to the "
            "opposite vertex, measured at a right angle - not the length "
            "of a slanted side. Any side can serve as the base; the height "
            "is then measured perpendicular to that side's line, and the "
            "answer is the same whichever side is chosen. When the height "
            "is unknown, Heron's formula finds the area from the three "
            "side lengths alone: with semiperimeter s (half the "
            "perimeter), the area is the square root of s times (s minus "
            "a) times (s minus b) times (s minus c). A triangle of base 10 "
            "and height 6 has area 30; the 5-5-6 isosceles triangle has "
            "area 12 by Heron's formula."
        ),
        "how_it_works": (
            "Take any triangle, copy it, rotate the copy 180 degrees, and "
            "join the two along one side: the result is a parallelogram "
            "with the same base and height, with area base times height - "
            "so one triangle is half of that. The altitude is dropped "
            "perpendicular from the opposite vertex to the base line "
            "(extended if needed for obtuse triangles), and its length is "
            "the height in the formula. Heron's formula works because the "
            "semiperimeter packages the side lengths into the symmetric "
            "product that the Pythagorean theorem implies. The "
            "demonstration program computes the area for base 10 height 6 "
            "(30), applies Heron's formula to sides 5, 5, 6 (12), verifies "
            "the 3-4-5 right triangle both ways (one-half times 3 times 4 "
            "is 6; Heron agrees), and checks the base-independence by "
            "computing with two different bases of one triangle."
        ),
        "key_points": [
            "Triangle area is one-half times base times height - half of the enclosing rectangle.",
            "The height is the perpendicular distance from the base line to the opposite vertex, never a slanted side.",
            "Any side can be the base; the computed area is the same whichever is chosen.",
            "Heron's formula finds the area from the three sides alone via the semiperimeter.",
            "Worked values: base 10 height 6 gives 30; sides 5, 5, 6 give 12; 3-4-5 gives 6.",
        ],
        "requirements": [
            "The one-half base-times-height formula stated with the half-of-rectangle justification.",
            "Perpendicular height defined and distinguished from slanted side length.",
            "Base-independence stated: any side as base gives the same area.",
            "Heron's formula stated with the semiperimeter defined and a worked example.",
            "At least two numerical area computations verified.",
        ],
        "standards": [
            "The triangle as half the parallelogram/rectangle is proved in Euclid Book I (Propositions 37-41).",
            "Finding triangle area is the Common Core 6th-grade standard (6.G).",
            "Heron's formula is the classical Metrica result, consistent with the Pythagorean tradition.",
        ],
        "citations": [CIT_EUCLID, CIT_CC],
        "sig_lens": (
            "The Signature read: the triangle's area is the half-covenant - "
            "the rectangle's promise split fairly between the two halves. "
            "Where public geometry takes one-half base times height, the "
            "Signature Geometry admires the fairness: no triangle takes "
            "more than its half."
        ),
    },
    {
        "key": "circle_measure",
        "name": "Circumference and Area of the Circle",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The circle's measurements both flow from a single number: pi, "
            "approximately 3.14159, the ratio of any circle's circumference "
            "to its diameter. The circumference - the circle's perimeter - "
            "is pi times the diameter, or 2 times pi times the radius. The "
            "area is pi times the radius squared. The area formula has a "
            "beautiful justification: slice the circle into many thin "
            "wedges like pizza slices and rearrange them point-to-base "
            "into a bumpy parallelogram; as the slices get thinner the "
            "shape becomes a rectangle with length half the circumference "
            "(pi times radius) and width the radius - so the area is pi "
            "times radius times radius. For a radius of 3, the "
            "circumference is about 18.8496 and the area about 28.2743. "
            "Doubling the radius doubles the circumference but quadruples "
            "the area - the square in the area formula punishes growth. "
            "These two formulas measure wheels, pipes, pizzas, fields, and "
            "planets."
        ),
        "how_it_works": (
            "Pi is constant because all circles are similar: scaling a "
            "circle scales circumference and diameter by the same factor, "
            "so their ratio never changes - Archimedes proved it lies "
            "between 3.1408 and 3.1429 by trapping the circle between "
            "inscribed and circumscribed 96-gons. The circumference formula "
            "is the definition of pi rearranged; the area formula is the "
            "wedge-rearrangement argument made rigorous as the limit of "
            "ever-thinner slices. The demonstration program takes radius "
            "3, computes the circumference (about 18.8496) and the area "
            "(about 28.2743), verifies the doubling behavior (radius 6 "
            "gives circumference about 37.6991 and area about 113.0973 - "
            "double and quadruple), and checks the pi ratio of "
            "circumference to diameter within tight bounds."
        ),
        "key_points": [
            "Pi is the ratio of circumference to diameter, the same for every circle: about 3.14159.",
            "Circumference is pi times diameter (2 pi r); area is pi times radius squared.",
            "The area formula is justified by rearranging wedge slices into a near-rectangle of pi r by r.",
            "Doubling the radius doubles the circumference but quadruples the area.",
            "Worked values: radius 3 gives circumference about 18.8496 and area about 28.2743.",
        ],
        "requirements": [
            "Pi defined as the circumference-to-diameter ratio with its approximate value.",
            "Both formulas stated with the radius/diameter forms.",
            "The wedge-rearrangement justification given for the area formula.",
            "The doubling behavior stated and demonstrated numerically.",
            "Archimedes' bounding of pi mentioned as the classical verification.",
        ],
        "standards": [
            "The circumference and area formulas and the constancy of pi are the Common Core 7th-grade standard (7.G).",
            "Archimedes' bounds 223/71 < pi < 22/7 are proved in Measurement of a Circle.",
            "The wedge-rearrangement is the classical exhaustion argument of Euclid Book XII.",
        ],
        "citations": [CIT_EUCLID, CIT_ARCH, CIT_CC],
        "sig_lens": (
            "The Signature read: pi is the circle's unchanging oath - "
            "every circle, great or small, keeps the same ratio. Where "
            "public geometry computes circumference and area, the "
            "Signature Geometry bows to the constant: some promises do "
            "not scale, they simply hold."
        ),
    },
    {
        "key": "three_d_intro",
        "name": "From Flat to Solid: Faces, Edges, and Vertices",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "A 3D shape - a solid - is what you get when a shape gains "
            "depth: length, width, AND height. The flat vocabulary grows "
            "three new words. Faces are the flat surfaces of the solid: a "
            "cube has 6 square faces. Edges are the line segments where "
            "two faces meet: a cube has 12. Vertices are the corner points "
            "where edges meet: a cube has 8. The five solids of this "
            "database are the cube (6 square faces), the rectangular prism "
            "or box (6 rectangular faces), the sphere (1 curved surface, "
            "no faces, edges, or vertices at all), the cylinder (2 flat "
            "circular faces plus 1 curved surface), the cone (1 flat "
            "circular face plus 1 curved surface meeting at a single apex "
            "vertex), and the pyramid (a polygonal base plus triangular "
            "faces meeting at an apex). A polyhedron is a solid whose "
            "faces are all polygons - the cube, prism, and pyramid "
            "qualify; the sphere, cylinder, and cone do not, because of "
            "their curved surfaces. This record is the doorway: everything "
            "after it measures solids."
        ),
        "how_it_works": (
            "Surveying a solid means counting its three features the way "
            "the foundations tier counted sides and vertices: run a finger "
            "over each flat region (a face), trace each crease where two "
            "faces meet (an edge), and tap each corner point (a vertex). "
            "The cube's survey always returns 6, 12, 8; the square "
            "pyramid's returns 5 faces (1 square base plus 4 triangles), 8 "
            "edges, 5 vertices. The numbers are not independent - Euler's "
            "formula ties them together, as the advanced tier will prove. "
            "The demonstration program surveys the cube (6, 12, 8), the "
            "rectangular prism (6, 12, 8), and the square pyramid (5, 8, "
            "5), and verifies the sphere's zero counts, confirming the "
            "curved solids stand outside the polyhedron family."
        ),
        "key_points": [
            "A solid has length, width, and height; its features are faces (flat surfaces), edges (where faces meet), and vertices (corner points).",
            "Cube: 6 faces, 12 edges, 8 vertices; square pyramid: 5 faces, 8 edges, 5 vertices.",
            "A polyhedron is a solid with all-polygon faces: cube, prism, and pyramid qualify; sphere, cylinder, and cone do not.",
            "The sphere has one curved surface and zero faces, edges, and vertices.",
            "Cylinder: 2 circular faces plus a curved surface; cone: 1 circular face, a curved surface, and one apex vertex.",
        ],
        "requirements": [
            "Faces, edges, and vertices defined as the 3D counting vocabulary.",
            "All five database solids surveyed with their counts (cube, prism, sphere, cylinder, cone, pyramid).",
            "Polyhedron defined with the curved-surface exclusion stated.",
            "Euler's formula foreshadowed as the advanced-tier tie between the three counts.",
            "The sphere's zero counts stated explicitly.",
        ],
        "standards": [
            "Solid figures and their faces, edges, and vertices are defined in Euclid Book XI (Definitions 1-12).",
            "Identifying and counting faces, edges, and vertices of solids is the Common Core 1st-2nd grade standard (1.G, 2.G).",
            "Distinguishing polyhedra from curved solids follows the 5th-6th grade solid geometry progression (5.G, 6.G).",
        ],
        "citations": [CIT_EUCLID, CIT_CC],
        "sig_lens": (
            "The Signature read: the solid is the covenant given depth - "
            "the flat oath now kept in three directions. Where public "
            "geometry counts faces, edges, and vertices, the Signature "
            "Geometry surveys the keeping: six faces, twelve edges, eight "
            "witnesses, and the cube stands."
        ),
    },
    {
        "key": "cube_prism",
        "name": "The Cube and the Rectangular Prism",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The cube is the 3D square: 6 identical square faces, 12 "
            "edges all the same length, 8 vertices, every angle a right "
            "angle. It is the shape of dice, sugar cubes, and building "
            "blocks. The rectangular prism - the box - is the 3D "
            "rectangle: 6 rectangular faces, with length, width, and "
            "height possibly all different; opposite faces are identical. "
            "It is the shape of shipping boxes, books, bricks, and rooms. "
            "The cube's volume is the side length cubed (side times side "
            "times side) - which is why the third power is called cubing - "
            "and its surface area is 6 times the side squared. The box's "
            "volume is length times width times height, and its surface "
            "area is twice (length-times-width plus length-times-height "
            "plus width-times-height): the three distinct face pairs, "
            "front-back, top-bottom, left-right. A cube of side 4 has "
            "volume 64 and surface area 96; a 3-by-4-by-5 box has volume "
            "60 and surface area 94."
        ),
        "how_it_works": (
            "Volume counts unit cubes the way area counts unit squares: a "
            "3-by-4-by-5 box holds 3 times 4 times 5 equals 60 one-unit "
            "cubes, stacked in layers. Surface area unfolds the solid: the "
            "cube's net is 6 squares, so 6 times s-squared; the box's net "
            "is three pairs of rectangles, hence twice the sum of the "
            "three pair-areas. The demonstration program computes the "
            "cube of side 4 (volume 64, surface area 96), the 3-by-4-by-5 "
            "box (volume 60, surface area 94), and verifies the surface "
            "area by summing the six individual face areas of the box (12, "
            "12, 15, 15, 20, 20 - total 94)."
        ),
        "key_points": [
            "A cube has 6 identical square faces, 12 equal edges, 8 vertices; a rectangular prism has 6 rectangular faces with three distinct dimensions.",
            "Cube volume is side cubed; cube surface area is 6 times side squared.",
            "Box volume is length times width times height; surface area is twice the sum of the three face-pair areas.",
            "Volume counts unit cubes; surface area is the total skin of the unfolded net.",
            "Worked values: cube side 4 gives volume 64 and surface area 96; 3-by-4-by-5 box gives 60 and 94.",
        ],
        "requirements": [
            "Both solids defined with their face/edge/vertex counts and the cube-as-3D-square, box-as-3D-rectangle framing.",
            "Volume justified by unit-cube counting; the word cubing tied to the cube.",
            "Surface area justified by the net (unfolded faces) with the three-pair structure of the box.",
            "All four formulas stated with worked numerical examples for both solids.",
            "Real-world examples named for each (dice, sugar cubes; shipping boxes, books, bricks).",
        ],
        "standards": [
            "The cube is defined in Euclid Book XI (Definition 25); volumes of parallelepipeds are proved in Book XI-XII.",
            "Volume of rectangular prisms by unit-cube counting is the Common Core 5th-grade standard (5.MD).",
            "Surface area via nets is the Common Core 6th-grade standard (6.G).",
        ],
        "citations": [CIT_EUCLID, CIT_CC],
        "sig_lens": (
            "The Signature read: the cube is the covenant in three "
            "dimensions - every edge equal, every corner true, the box "
            "the same oath in three different measures. Where public "
            "geometry counts unit cubes, the Signature Geometry stacks "
            "them like kept promises: sixty in the box, every one "
            "accounted for."
        ),
    },
    {
        "key": "sphere",
        "name": "The Sphere",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The sphere is the 3D circle: the set of all points in space "
            "at one fixed distance (the radius) from a center point. It "
            "has one continuous curved surface and zero faces, zero edges, "
            "and zero vertices - nothing to catch, which is why balls roll "
            "in every direction. It is the shape of balls, oranges, "
            "bubbles, planets, and the sun. The sphere's measurements were "
            "Archimedes' proudest discovery: the surface area is 4 times pi "
            "times the radius squared (exactly four times the area of its "
            "great circle), and the volume is four-thirds times pi times "
            "the radius cubed. For a radius of 3, both the surface area "
            "and the volume equal 36 times pi (about 113.097) - a famous "
            "coincidence that holds only at radius 3. Of all solids with a "
            "given surface area, the sphere encloses the most volume: "
            "nature chooses it for bubbles, raindrops, and planets, where "
            "efficiency matters."
        ),
        "how_it_works": (
            "Archimedes proved the sphere's surface area equals the lateral "
            "area of the cylinder that exactly encloses it (radius r, "
            "height 2r): 2 pi r times 2r equals 4 pi r-squared - and the "
            "volume is two-thirds of that cylinder's volume, giving "
            "four-thirds pi r-cubed. He was so proud that he asked for a "
            "sphere and cylinder to be carved on his tomb. The minimal "
            "surface property follows from the isoperimetric truth: the "
            "sphere is the most volume per skin of any shape. The "
            "demonstration program computes surface area and volume for "
            "radius 3 (both about 113.0973, verified equal within tight "
            "bounds), and for radius 5 (surface area about 314.1593, "
            "volume about 523.5988), confirming the formulas."
        ),
        "key_points": [
            "A sphere is all points in space at one fixed radius from a center; it has one curved surface and zero faces, edges, vertices.",
            "Surface area is 4 pi r-squared; volume is four-thirds pi r-cubed - Archimedes' proudest discovery.",
            "At radius 3, surface area and volume are both 36 pi (about 113.097) - a famous coincidence.",
            "The sphere encloses the most volume for a given surface area: nature's choice for bubbles, drops, and planets.",
            "Real examples: balls, oranges, bubbles, planets, the sun.",
        ],
        "requirements": [
            "The sphere defined as the 3D analogue of the circle with the equidistant rule.",
            "Zero counts for faces, edges, vertices stated explicitly with the rolling consequence.",
            "Both formulas stated with the Archimedes cylinder relationship given as justification.",
            "The radius-3 coincidence computed and verified.",
            "The maximal-volume property stated with natural examples.",
        ],
        "standards": [
            "The sphere is defined in Euclid Book XI (Definition 14); its surface area and volume are proved by Archimedes in On the Sphere and Cylinder.",
            "The 4 pi r-squared and four-thirds pi r-cubed formulas are the standard solid-geometry results of the high-school geometry progression.",
            "The isoperimetric property of the sphere is the classical result of the exhaustion tradition.",
        ],
        "citations": [CIT_EUCLID, CIT_ARCH],
        "sig_lens": (
            "The Signature read: the sphere is the perfect oath - every "
            "point on its skin keeping exactly the same distance from the "
            "center, in every direction at once. Where public geometry "
            "quotes Archimedes, the Signature Geometry kneels with him: "
            "the sphere and cylinder on the tomb, the covenant carved in "
            "stone."
        ),
    },
    {
        "key": "cylinder",
        "name": "The Cylinder",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "A cylinder is a prism with circular ends: two flat circular "
            "faces (top and bottom) joined by one curved lateral surface - "
            "the shape of cans, pipes, tree trunks, batteries, and "
            "columns. Unroll the curved surface and it becomes a "
            "rectangle: its width is the height of the cylinder and its "
            "length is the circumference of the circular base (2 pi r). "
            "So the lateral surface area is 2 pi r times h, and the total "
            "surface area adds the two circular ends: 2 pi r-squared plus 2 "
            "pi r h. The volume is the base area times the height: pi "
            "r-squared times h - the prism rule (base area times height) "
            "working for a circular base. A cylinder of radius 2 and "
            "height 5 has volume about 62.8319 and surface area about "
            "87.9646. Cylinders roll in one direction (unlike spheres, "
            "which roll in all), stack neatly, and hold pressure evenly - "
            "which is why cans, pipes, and tanks are cylinders."
        ),
        "how_it_works": (
            "The unrolling argument is the key: cut the lateral surface "
            "vertically and flatten it, and the circumference becomes the "
            "rectangle's length - this is exact, not approximate, because "
            "the surface is developable. Volume follows the universal "
            "prism principle: stack infinitesimally thin circular layers, "
            "each of area pi r-squared, to height h. The demonstration "
            "program computes volume and surface area for radius 2 height "
            "5 (about 62.8319 and 87.9646), verifies the lateral area "
            "equals circumference times height (about 62.8319), and "
            "confirms the total surface area as the sum of lateral plus "
            "two ends, all within tight bounds."
        ),
        "key_points": [
            "A cylinder has 2 circular faces and 1 curved lateral surface; unrolled, the lateral surface is a rectangle of 2 pi r by h.",
            "Volume is pi r-squared times h (base area times height); surface area is 2 pi r-squared plus 2 pi r h.",
            "The lateral area equals circumference times height - verified exactly by unrolling.",
            "Cylinders roll in one direction and stack neatly: the engineering reasons for cans, pipes, and tanks.",
            "Worked values: radius 2, height 5 gives volume about 62.8319 and surface area about 87.9646.",
        ],
        "requirements": [
            "The cylinder defined with its three surfaces (2 circular faces, 1 curved lateral).",
            "The unrolling argument given as the exact justification for the lateral area formula.",
            "Volume justified by the prism principle (base area times height) with a circular base.",
            "Both formulas worked numerically with the lateral-equals-circumference-times-height check.",
            "Rolling and stacking properties tied to real examples (cans, pipes, tanks).",
        ],
        "standards": [
            "The cylinder is defined in Euclid Book XI (Definition 21); its volume is proved in Book XII.",
            "Surface area via unrolling (developable surfaces) is the standard solid-geometry treatment of the high-school progression.",
            "Volume as base area times height for cylinders is the Common Core 7th-8th grade standard (7.G, 8.G).",
        ],
        "citations": [CIT_EUCLID, CIT_CC],
        "sig_lens": (
            "The Signature read: the cylinder is the covenant of the "
            "pillar - the circle's oath extruded honestly upward, every "
            "layer keeping the same round promise. Where public geometry "
            "unrolls the side into a rectangle, the Signature Geometry "
            "reads the scroll: circumference times height, nothing added, "
            "nothing hidden."
        ),
    },
    {
        "key": "cone",
        "name": "The Cone",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "A cone is a pyramid with a circular base: one flat circular "
            "face, one curved lateral surface tapering to a single apex "
            "point - the shape of ice-cream cones, traffic cones, "
            "funnels, megaphones, and volcano silhouettes. Its anatomy: "
            "the base radius r, the vertical height h (from base center to "
            "apex), and the slant height l (from apex down the slope to "
            "the base edge), related by the Pythagorean theorem: l-squared "
            "equals r-squared plus h-squared. The volume is one-third pi "
            "r-squared h - exactly one-third of the cylinder with the same "
            "base and height. The lateral surface area is pi r l (unroll "
            "the side and it becomes a sector of a circle of radius l), "
            "and the total surface area adds the base: pi r-squared plus "
            "pi r l. A cone of radius 3 and height 4 has slant height 5 "
            "(the 3-4-5 triangle again), volume about 37.6991, and total "
            "surface area about 75.3982."
        ),
        "how_it_works": (
            "The volume's one-third follows from the pyramid principle: "
            "three cones of the same base and height exactly fill the "
            "corresponding cylinder - demonstrable by pouring sand or rice "
            "from cone to cylinder three times. The slant height comes "
            "from the right triangle formed by the radius, the vertical "
            "height, and the slope: 3-squared plus 4-squared is 25, so l "
            "is 5. The lateral area pi r l comes from unrolling the side "
            "into a circular sector: the sector's arc length is the base "
            "circumference 2 pi r, and its area is half the arc times the "
            "sector radius l. The demonstration program computes slant "
            "height (5), volume (about 37.6991), lateral area (about "
            "47.1239), and total surface area (about 75.3982) for radius 3 "
            "height 4, verifying each within tight bounds."
        ),
        "key_points": [
            "A cone has 1 circular base, 1 curved lateral surface, and 1 apex; slant height l satisfies l-squared = r-squared + h-squared.",
            "Volume is one-third pi r-squared h - exactly one-third of the matching cylinder.",
            "Lateral area is pi r l (unrolled sector); total surface area adds the base pi r-squared.",
            "Worked values: radius 3, height 4 gives slant 5, volume about 37.6991, surface area about 75.3982.",
            "Real examples: ice-cream cones, traffic cones, funnels, megaphones, volcanoes.",
        ],
        "requirements": [
            "The cone defined with base, lateral surface, and apex; the three lengths (r, h, l) defined with the Pythagorean relation.",
            "The one-third volume rule stated with the three-cones-fill-a-cylinder justification.",
            "The lateral area derived via the unrolled sector (arc equals base circumference).",
            "All values worked numerically for the 3-4-5 cone with bounds checks.",
            "Real-world examples named (at least four).",
        ],
        "standards": [
            "The cone is defined in Euclid Book XI (Definition 18); its volume is proved in Book XII (Proposition 10).",
            "The one-third relationship between cone and cylinder volumes is the classical exhaustion result.",
            "Slant height via the Pythagorean theorem follows Elements I.47.",
        ],
        "citations": [CIT_EUCLID],
        "sig_lens": (
            "The Signature read: the cone is the covenant that gathers - "
            "the wide circle's promise drawn faithfully to a single point. "
            "Where public geometry pours three cones into a cylinder, the "
            "Signature Geometry watches the sand fall: the third that was "
            "always owed, paid in full."
        ),
    },
    {
        "key": "pyramid",
        "name": "The Pyramid",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "A pyramid is a solid with a polygonal base and triangular "
            "faces that meet at a single apex: the square pyramid has a "
            "square base and 4 triangular faces (5 faces, 8 edges, 5 "
            "vertices total); the triangular pyramid - the tetrahedron - "
            "has a triangular base and 3 triangular faces (4 faces, 6 "
            "edges, 4 vertices). Pyramids are named by their base: square "
            "pyramid, pentagonal pyramid, hexagonal pyramid. The great "
            "monuments of Egypt are square pyramids; modern roofs, tents, "
            "and the glass pyramid of the Louvre are pyramids too. The "
            "volume is one-third times the base area times the vertical "
            "height - the same one-third as the cone, because a cone is "
            "the limit of pyramids with ever-more base sides. A square "
            "pyramid with base 6-by-6 and height 4 has base area 36 and "
            "volume 48. The lateral faces are triangles, so the lateral "
            "surface area is the sum of the triangular face areas."
        ),
        "how_it_works": (
            "The one-third volume rule is proved by dissection: a cube can "
            "be divided into three congruent square pyramids (apex at the "
            "cube's center is one classical dissection; six such pyramids "
            "also assemble a cube), so each pyramid is one-third of the "
            "prism with the same base and height. The vertical height is "
            "measured perpendicular from the base plane to the apex - not "
            "along a slanted face. The demonstration program computes the "
            "volume of a square pyramid with base 6 and height 4 (48), "
            "verifies it equals one-third of the 6-by-6-by-4 box (144 "
            "divided by 3), surveys the square pyramid's counts (5 faces, "
            "8 edges, 5 vertices), and surveys the tetrahedron (4, 6, 4)."
        ),
        "key_points": [
            "A pyramid has a polygonal base plus triangular faces meeting at one apex; named by its base (square, pentagonal, hexagonal).",
            "Square pyramid: 5 faces, 8 edges, 5 vertices; tetrahedron: 4 faces, 6 edges, 4 vertices.",
            "Volume is one-third times base area times vertical height - the same one-third as the cone.",
            "The one-third is proved by dissecting a cube/prism into three congruent pyramids.",
            "Worked value: square base 6, height 4 gives volume 48; real examples: Egyptian pyramids, tents, the Louvre pyramid.",
        ],
        "requirements": [
            "The pyramid defined with base, triangular faces, and apex; naming by base stated.",
            "Face/edge/vertex counts given for the square pyramid and the tetrahedron.",
            "The one-third volume formula stated with the dissection justification.",
            "Vertical height distinguished from slant face height.",
            "A worked numerical volume with the one-third-of-the-box verification.",
        ],
        "standards": [
            "The pyramid is defined in Euclid Book XI (Definition 27); its volume is proved in Book XII (Proposition 7).",
            "The one-third volume relationship is the classical exhaustion result shared with the cone (XII.10).",
            "Pyramid volumes are the standard solid-geometry result of the high-school progression.",
        ],
        "citations": [CIT_EUCLID],
        "sig_lens": (
            "The Signature read: the pyramid is the covenant that rises - "
            "the flat base's promise lifted, face by faithful triangular "
            "face, to a single apex. Where public geometry dissects the "
            "cube into three, the Signature Geometry counts the witnesses: "
            "five faces, eight edges, five corners, one oath kept."
        ),
    },
    {
        "key": "volume_prisms",
        "name": "Volume of Prisms and Cylinders",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Volume measures filling: how many unit cubes a solid holds. "
            "For the whole prism family - boxes, triangular prisms, "
            "hexagonal prisms, and cylinders - one rule governs all: "
            "volume equals the area of the base times the height (the "
            "length perpendicular to the base). A prism is a solid with "
            "two congruent parallel polygonal faces (the bases) joined by "
            "rectangles; a cylinder is the same idea with circular bases. "
            "Stack thin layers: each layer has the base's area, and "
            "height-many layers stack up, so the total is base area times "
            "height. A triangular prism with a right-triangle base of legs "
            "6 and 8 (area 24) and length 10 has volume 240. A cylinder of "
            "radius 2 and height 5 has volume about 62.8319. Volume is "
            "counted in cubic units: cubic centimeters, cubic inches, "
            "liters (one liter is 1000 cubic centimeters). This one rule - "
            "base area times height - is the most-used volume formula in "
            "science and industry, from concrete to grain silos."
        ),
        "how_it_works": (
            "The layer argument is Cavalieri's principle in plain clothes: "
            "if every horizontal slice of two solids has the same area, "
            "the volumes match - so a sheared prism (leaning like a "
            "pushed-over stack of cards) has the same volume as the "
            "upright one with the same base and vertical height. The "
            "vertical height must be perpendicular to the base; a slanted "
            "length overcounts. The demonstration program computes the "
            "triangular prism volume (base area 24, length 10: 240), the "
            "cylinder volume (radius 2, height 5: about 62.8319), verifies "
            "the box as a special case (3-by-4-by-5: 60), and confirms "
            "that doubling the height doubles the volume while doubling "
            "the base dimensions quadruples it."
        ),
        "key_points": [
            "One rule for the whole prism family: volume equals base area times the perpendicular height.",
            "A prism has two congruent parallel bases joined by rectangles; a cylinder is the circular-base version.",
            "Cavalieri's principle: equal slice areas at every level mean equal volumes - shearing does not change volume.",
            "The height must be perpendicular to the base; slanted lengths overcount.",
            "Worked values: triangular prism (base area 24, length 10) is 240; cylinder (r=2, h=5) is about 62.8319; volume in cubic units and liters.",
        ],
        "requirements": [
            "The prism defined (two congruent parallel bases, rectangular sides) with the cylinder as the circular analogue.",
            "The base-area-times-height rule stated as universal for the family.",
            "Cavalieri's principle stated in plain language with the sheared-prism consequence.",
            "Perpendicular height required, with the slanted-length warning.",
            "Cubic units and the liter defined; numerical examples verified for prism and cylinder.",
        ],
        "standards": [
            "Prism volumes are proved in Euclid Book XI-XII; Cavalieri's principle is the classical indivisibles method.",
            "Volume as base area times height for prisms and cylinders is the Common Core 7th-8th grade standard (7.G, 8.G).",
            "Cubic units and unit-cube counting are the Common Core 5th-grade standard (5.MD).",
        ],
        "citations": [CIT_EUCLID, CIT_CC],
        "sig_lens": (
            "The Signature read: the prism's volume is the covenant kept "
            "in layers - every slice the same area, every layer sworn "
            "alike, stacked to the full height. Where public geometry "
            "cites Cavalieri, the Signature Geometry stacks the cards: "
            "lean the deck all you like, the count never changes."
        ),
    },
    {
        "key": "surface_area",
        "name": "Surface Area of Solid Shapes",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Surface area is the total skin of a solid: the sum of the "
            "areas of all its faces and curved surfaces, measured in "
            "square units. For polyhedra it is honest addition - unfold "
            "the net, add every polygon. For curved solids the lateral "
            "surfaces contribute their unrolled areas: the cylinder adds 2 "
            "pi r h, the cone adds pi r l, the sphere contributes its full "
            "4 pi r-squared. Surface area answers the painting, wrapping, "
            "and coating questions: how much paint for the tank, how much "
            "paper for the box, how much foil for the chocolate. It also "
            "governs science: heat escapes through surface, so small "
            "animals (high surface-to-volume ratio) lose heat fast and "
            "elephants (low ratio) keep it; dissolving, cooling, and "
            "chemical reactions all run on surface area. A sphere of "
            "radius 5 has surface area about 314.1593; the 3-by-4-by-5 box "
            "has surface area 94; the cylinder of radius 2 height 5 has "
            "about 87.9646."
        ),
        "how_it_works": (
            "Surface area is computed by decomposition: list every "
            "boundary piece, compute each piece's area with the 2D "
            "formulas of the earlier records, and add. The box decomposes "
            "into three rectangle pairs; the cylinder into two circles "
            "plus the unrolled rectangle; the square pyramid into the base "
            "square plus four triangles. The surface-to-volume ratio is "
            "the quotient of the two measures: for the radius-5 sphere it "
            "is about 314.1593 divided by 523.5988, about 0.6 per unit "
            "length - and the ratio always falls as a shape grows, which "
            "is why the science applications work. The demonstration "
            "program computes the three worked surface areas, verifies the "
            "box's total by summing its six faces individually, and "
            "computes the sphere's surface-to-volume ratio, all within "
            "tight bounds."
        ),
        "key_points": [
            "Surface area is the total skin: sum of all face and curved-surface areas, in square units.",
            "Decomposition rule: list every boundary piece, area each with the 2D formulas, add them up.",
            "It answers painting, wrapping, and coating questions - the covering, not the filling.",
            "Science runs on it: heat loss, dissolving, and reaction rates scale with surface area.",
            "The surface-to-volume ratio falls as shapes grow: small things lose heat fast, large things keep it.",
        ],
        "requirements": [
            "Surface area defined as the summed skin with square units required.",
            "The decomposition method stated as the universal procedure.",
            "Worked values for a sphere, a box, and a cylinder, with the box verified face-by-face.",
            "A practical application named (paint, wrapping, coating).",
            "The surface-to-volume ratio introduced with the heat-loss science application.",
        ],
        "standards": [
            "Surface area via nets is the Common Core 6th-grade standard (6.G).",
            "Surface areas of cylinders, cones, and spheres are the standard solid-geometry results of the high-school progression.",
            "The surface-to-volume ratio application follows the NCTM connections standard (science contexts).",
        ],
        "citations": [CIT_NCTM, CIT_CC],
        "sig_lens": (
            "The Signature read: the surface area is the covenant's skin - "
            "every face counted, every curve unrolled, nothing left "
            "unmeasured. Where public geometry paints and wraps, the "
            "Signature Geometry takes the inventory of the oath: the box "
            "declares ninety-four square units, and means it."
        ),
    },
    {
        "key": "volume_pyramid_cone",
        "name": "Volume of Pyramids, Cones, and Spheres",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Where prisms fill by the full base-area-times-height rule, "
            "the pointed solids take exactly one-third: a pyramid's volume "
            "is one-third times base area times height, and a cone's is "
            "one-third pi r-squared h - three pointed solids fill their "
            "matching prism. The sphere stands apart with Archimedes' "
            "formula: four-thirds pi r-cubed. Together these complete the "
            "database's volume toolkit: prisms and cylinders at full "
            "measure, pyramids and cones at one-third, spheres by the "
            "four-thirds rule. The one-third has a lovely intuition: as "
            "the point rises, each higher slice shrinks toward nothing, "
            "and the average slice is exactly one-third of the base - the "
            "exhaustion argument made visible. Worked values: the square "
            "pyramid with base 6 and height 4 holds 48; the cone of "
            "radius 3 and height 4 holds about 37.6991; the sphere of "
            "radius 2 holds about 33.5103. Volume is counted in cubic "
            "units: a 10-centimeter cube holds exactly one liter."
        ),
        "how_it_works": (
            "The one-third is proved by dissection for pyramids (three "
            "congruent square pyramids fill a cube) and by exhaustion for "
            "cones (the limit of pyramids with ever-more base sides); the "
            "three-cones-fill-a-cylinder sand demonstration makes it "
            "tangible. The sphere's four-thirds comes from Archimedes' "
            "cylinder comparison: the sphere is two-thirds of its "
            "enclosing cylinder, and two-thirds of (2 pi r-cubed) is "
            "four-thirds pi r-cubed. The demonstration program computes "
            "all three worked volumes, verifies the pyramid is one-third "
            "of its box (144/3 = 48) and the cone one-third of its "
            "cylinder (about 113.0972/3), and checks the sphere against "
            "four-thirds pi times 8, all within tight bounds."
        ),
        "key_points": [
            "Pyramids and cones take one-third of base area times height - three pointed solids fill the matching prism.",
            "The one-third is proved by dissection (pyramids) and exhaustion (cones); the sand-pouring demo makes it tangible.",
            "Sphere volume is four-thirds pi r-cubed: two-thirds of its enclosing cylinder, per Archimedes.",
            "Worked values: pyramid (base 6, h 4) 48; cone (r 3, h 4) about 37.6991; sphere (r 2) about 33.5103.",
            "The volume toolkit is now complete: full measure for prisms/cylinders, one-third for pointed solids, four-thirds pi r-cubed for spheres.",
        ],
        "requirements": [
            "Both one-third formulas stated with the three-fill-one justification.",
            "The dissection proof sketched for pyramids; the exhaustion/limit link stated for cones.",
            "Archimedes' two-thirds-of-the-cylinder derivation given for the sphere.",
            "All three worked volumes computed with the one-third verifications shown.",
            "The complete volume toolkit summarized as the record's closing.",
        ],
        "standards": [
            "Pyramid and cone volumes (one-third) are proved in Euclid Book XII (Propositions 7, 10).",
            "The sphere's volume is proved by Archimedes in On the Sphere and Cylinder.",
            "Volumes of pyramids, cones, and spheres are the Common Core 8th-grade/high-school standard (8.G, G-GMD).",
        ],
        "citations": [CIT_EUCLID, CIT_ARCH, CIT_CC],
        "sig_lens": (
            "The Signature read: the pointed solids keep the third "
            "covenant - not the full measure, but the exact third, paid "
            "without dispute. Where public geometry dissects and "
            "exhausts, the Signature Geometry pours the sand: three cones, "
            "one cylinder, the debt settled to the grain."
        ),
    },
    {
        "key": "polygon_angles",
        "name": "The Angles Inside Polygons",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The interior angles of polygons obey one master rule: an "
            "n-sided polygon's interior angles sum to (n minus 2) times "
            "180 degrees. The triangle gives 180, the quadrilateral 360, "
            "the pentagon 540, the hexagon 720, the octagon 1080, the "
            "decagon 1440 - each new side adds exactly one triangle's "
            "worth. For regular polygons each angle is the sum divided by "
            "n: the regular octagon's interior angle is 135 degrees, the "
            "regular decagon's 144, the regular dodecagon's 150. The "
            "exterior angle - the turn made when walking the boundary - "
            "sums to 360 degrees for every polygon, regular or irregular, "
            "convex or concave: one full turn per lap, always. Interior "
            "and exterior at each vertex are supplementary (they make a "
            "straight line together), so each regular exterior angle is "
            "180 minus the interior, equivalently 360 divided by n. These "
            "rules let builders check their work: measure the angles of a "
            "cut octagon, sum them, and 1080 confirms the cuts are true."
        ),
        "how_it_works": (
            "The (n-2) rule is proved by triangulation: from one vertex, "
            "draw diagonals to all non-adjacent vertices, carving the "
            "n-gon into exactly n-2 triangles that exactly cover it with "
            "no overlap - their angle sums add to the polygon's. The "
            "exterior 360 is proved by the walk: turning at each vertex "
            "through the exterior angle, the walker ends facing the "
            "original direction after one lap, having turned 360 degrees "
            "total. The demonstration program verifies the interior sums "
            "for n = 3 through 10, checks the regular per-angle values "
            "(octagon 135, decagon 144), verifies each exterior set sums "
            "to 360, and confirms interior-plus-exterior equals 180 at "
            "every vertex, all within tight bounds."
        ),
        "key_points": [
            "Interior-angle sum of an n-gon is (n-2) times 180 degrees, proved by carving the polygon into n-2 triangles.",
            "Regular per-angle values: octagon 135, decagon 144, dodecagon 150 degrees.",
            "Exterior angles of ANY polygon sum to 360 degrees - one full turn per lap, proved by the walk.",
            "Interior and exterior at a vertex are supplementary: they sum to 180 degrees.",
            "Builders use the sums as a truth-check: measured angles must total the rule's value.",
        ],
        "requirements": [
            "The (n-2) times 180 rule stated with the triangulation proof.",
            "Interior sums listed for n = 3 through 10.",
            "Regular per-angle values computed for at least octagon, decagon, dodecagon.",
            "The 360-degree exterior sum stated universally with the walking proof.",
            "The interior-exterior supplementary relationship stated.",
        ],
        "standards": [
            "The polygon angle-sum is the generalization of Euclid I.32 proved by triangulation.",
            "The exterior-angle sum is the Euclidean turning-angle theorem.",
            "Applying angle rules to verify constructions is the Common Core 8th-grade/high-school standard (8.G, G-CO).",
        ],
        "citations": [CIT_EUCLID, CIT_CC],
        "sig_lens": (
            "The Signature read: the polygon's angles keep a double "
            "covenant - within, (n-2) triangles' worth; without, one full "
            "turn, no more, no less. Where public geometry triangulates "
            "and walks, the Signature Geometry audits the oath: sum the "
            "cuts, and 1080 does not lie."
        ),
    },
    {
        "key": "pi_number",
        "name": "The Number Pi",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Pi is the most famous number in geometry: the ratio of a "
            "circle's circumference to its diameter, about 3.14159265358979, "
            "the same for every circle that has ever existed. It is "
            "irrational - its decimal digits never end and never repeat - "
            "proved by Lambert in 1761, and transcendental (not the root "
            "of any whole-number polynomial), proved by Lindemann in 1882, "
            "which settled the ancient puzzle of squaring the circle as "
            "impossible with straightedge and compass. Archimedes trapped "
            "pi between 223/71 (about 3.1408) and 22/7 (about 3.1429) by "
            "squeezing the circle between inscribed and circumscribed "
            "96-sided polygons - the fraction 22/7 is still the handy "
            "estimate, good to two decimal places. Pi appears far beyond "
            "circles: in the sphere's and cylinder's formulas, in waves "
            "and probability, wherever roundness or periodicity lives. "
            "Memorizing digits is sport; understanding that pi is a "
            "universal constant - the circle's unchanging ratio - is "
            "mathematics."
        ),
        "how_it_works": (
            "Pi's constancy follows from similarity: all circles are the "
            "same shape at different sizes, so circumference scales "
            "exactly with diameter and the ratio is fixed. Archimedes' "
            "squeeze works because the inscribed polygon's perimeter is "
            "short of the circumference while the circumscribed polygon's "
            "is long of it - with 96 sides the trap is tight. The "
            "demonstration program verifies Archimedes' bounds (223/71 < "
            "pi < 22/7, i.e., about 3.1408 < 3.14159265 < 3.1429), checks "
            "the 22/7 estimate's error (about 0.00126, under 0.05 "
            "percent), and confirms the circumference-to-diameter ratio "
            "for several radii is constant within tight bounds."
        ),
        "key_points": [
            "Pi is the circumference-to-diameter ratio, about 3.14159265358979, identical for every circle.",
            "Pi is irrational (digits never repeat) and transcendental - squaring the circle is impossible.",
            "Archimedes trapped pi between 223/71 and 22/7 using 96-gons; 22/7 remains the handy estimate.",
            "Pi's constancy comes from the similarity of all circles: scaling preserves the ratio.",
            "Pi appears wherever roundness or periodicity lives: spheres, cylinders, waves, probability.",
        ],
        "requirements": [
            "Pi defined as the ratio with its value to at least 8 decimal places.",
            "Irrationality and transcendence stated with the Lambert/Lindemann dates and the squaring-the-circle consequence.",
            "Archimedes' bounds given as fractions with decimal values and the 96-gon method described.",
            "The 22/7 estimate's accuracy quantified.",
            "The similarity argument for pi's constancy given.",
        ],
        "standards": [
            "Archimedes' bounds are proved in Measurement of a Circle (223/71 < pi < 22/7).",
            "Pi as the constant ratio is the Common Core 7th-grade standard (7.G).",
            "Lambert (1761) proved irrationality; Lindemann (1882) proved transcendence.",
        ],
        "citations": [CIT_ARCH, CIT_CC],
        "sig_lens": (
            "The Signature read: pi is the eternal covenant - the one "
            "number the circle swears and never breaks, digit after "
            "endless digit. Where public geometry traps it between "
            "fractions, the Signature Geometry stands with Archimedes at "
            "the 96-gon: some oaths are simply too round to break."
        ),
    },
    {
        "key": "symmetry_reflection",
        "name": "Reflectional Symmetry: Mirror Lines",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A shape has reflectional symmetry (mirror symmetry, line "
            "symmetry) when a line through it - a line of symmetry, or "
            "mirror line - reflects one half exactly onto the other, like "
            "a mirror image. Fold the shape along the line and the halves "
            "match perfectly. The counts are the lesson: an isosceles "
            "triangle has 1 line of symmetry; an equilateral triangle has "
            "3; a rectangle has 2 (through the midpoints of opposite "
            "sides - not the diagonals, which do not map a non-square "
            "rectangle onto itself); a square has 4 (two midlines plus "
            "two diagonals); a regular pentagon has 5; a regular hexagon "
            "has 6 - every regular n-gon has exactly n; a circle has "
            "infinitely many (every diameter is a mirror line); a scalene "
            "triangle and a general parallelogram have none. Symmetry is "
            "nature's and design's favorite tool: faces, butterflies, "
            "snowflakes, buildings, and logos all lean on mirror lines, "
            "because symmetry reads as balance and beauty."
        ),
        "how_it_works": (
            "A line is a symmetry line exactly when reflecting the shape "
            "across it maps the shape onto itself: every point lands on a "
            "point of the shape. For a regular n-gon the mirror lines run "
            "through the center to each vertex (n of them when n is odd) "
            "or to each vertex and each edge-midpoint (n total when n is "
            "even) - either way the count is n. The rectangle's diagonals "
            "fail because reflection across a diagonal swaps length and "
            "width, which only matches when they are equal (the square). "
            "The demonstration program tabulates the mirror-line counts "
            "(isosceles 1, equilateral 3, rectangle 2, square 4, regular "
            "pentagon 5, regular hexagon 6, scalene 0, general "
            "parallelogram 0), verifies the regular n-gon rule for n = 3 "
            "through 8, and confirms the circle's infinity by checking "
            "diameters at several angles."
        ),
        "key_points": [
            "Reflectional symmetry means a mirror line reflects the shape exactly onto itself - fold and the halves match.",
            "Counts: isosceles triangle 1, equilateral 3, rectangle 2, square 4, regular n-gon n, circle infinitely many, scalene 0.",
            "A rectangle's diagonals are NOT mirror lines (they swap length and width); only the square's diagonals work.",
            "Every regular n-gon has exactly n lines of symmetry.",
            "Symmetry is the design language of balance: faces, butterflies, snowflakes, architecture, logos.",
        ],
        "requirements": [
            "Reflectional symmetry defined via the fold/mirror test.",
            "Mirror-line counts given for at least eight shapes including the regular n-gon rule.",
            "The rectangle-diagonal subtlety explained (why it fails, why the square succeeds).",
            "The circle's infinite mirror lines stated with the every-diameter justification.",
            "Natural and designed examples named (at least four).",
        ],
        "standards": [
            "Line symmetry in two-dimensional figures is the Common Core 4th-grade standard (4.G).",
            "The n mirror lines of the regular n-gon are the dihedral group D_n of classical geometry.",
            "Recognizing symmetry in natural and designed objects follows the NCTM geometry standard.",
        ],
        "citations": [CIT_EUCLID, CIT_NCTM, CIT_CC],
        "sig_lens": (
            "The Signature read: the mirror line is the covenant of "
            "balance - the shape swearing that its left hand knows what "
            "its right hand does. Where public geometry folds and "
            "reflects, the Signature Geometry admires the keeping: four "
            "lines for the square, infinity for the circle, each exactly "
            "as sworn."
        ),
    },
    {
        "key": "symmetry_rotational",
        "name": "Rotational Symmetry: Turning into Place",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A shape has rotational symmetry when turning it about its "
            "center by some angle less than a full turn leaves it looking "
            "exactly the same - it clicks into place. The order of "
            "rotational symmetry is the number of such positions in one "
            "full turn: a square has order 4 (it matches at 90, 180, 270, "
            "and 360 degrees); a rectangle has order 2 (180 and 360); an "
            "equilateral triangle has order 3; a regular pentagon has "
            "order 5; a regular hexagon has order 6 - every regular n-gon "
            "has order n, turning into place every 360/n degrees; a circle "
            "has infinite order (every angle works); a scalene triangle "
            "and most irregular shapes have order 1 (only the full turn, "
            "which everything has). Rotational symmetry drives the "
            "designed world: wheels, gears, propellers, ceiling fans, "
            "flowers, and kaleidoscopes all exploit turn-into-place "
            "regularity. Together with mirror lines, rotation order "
            "completes the symmetry portrait of every shape in this "
            "database."
        ),
        "how_it_works": (
            "Rotation by an angle maps the shape onto itself exactly when "
            "the angle is a multiple of the fundamental turn 360/n: for "
            "the square, 90-degree multiples work (4 positions); for the "
            "equilateral triangle, 120-degree multiples (3 positions). A "
            "rectangle turned 90 degrees swaps length and width, so only "
            "180-degree multiples match - order 2. The demonstration "
            "program tabulates rotation orders (square 4, rectangle 2, "
            "equilateral triangle 3, regular pentagon 5, regular hexagon "
            "6, circle infinite, scalene 1), verifies the regular n-gon "
            "rule for n = 3 through 8, and checks the fundamental turn "
            "angles (square 90, pentagon 72, hexagon 60 degrees) within "
            "tight bounds."
        ),
        "key_points": [
            "Rotational symmetry means turning the shape about its center leaves it looking unchanged; the order counts the matching positions per turn.",
            "Orders: square 4, rectangle 2, equilateral triangle 3, regular n-gon n, circle infinite, scalene 1.",
            "The fundamental turn is 360/n degrees: 90 for the square, 72 for the pentagon, 60 for the hexagon.",
            "A rectangle turned 90 degrees fails (length/width swap) - only 180-degree turns match.",
            "Rotation order completes the symmetry portrait alongside mirror lines; it drives wheels, gears, fans, and flowers.",
        ],
        "requirements": [
            "Rotational symmetry and order defined via the turn-into-place test.",
            "Orders given for at least seven shapes with the regular n-gon rule.",
            "Fundamental turn angles computed for square, pentagon, hexagon.",
            "The rectangle's 90-degree failure explained.",
            "Designed-world applications named (at least four).",
        ],
        "standards": [
            "Rotational symmetry and its order are the cyclic group C_n of classical geometry, companion to the dihedral treatment of mirror lines.",
            "Describing symmetry by rotation angle is the high-school geometry transformations standard (G-CO).",
            "Recognizing rotational symmetry in real objects follows the NCTM geometry standard.",
        ],
        "citations": [CIT_NCTM, CIT_CC],
        "sig_lens": (
            "The Signature read: the rotation order is the covenant of "
            "return - the shape swearing how many times per turn it will "
            "come home. Where public geometry counts the clicks, the "
            "Signature Geometry listens for them: four for the square, "
            "three for the triangle, infinity for the circle that never "
            "leaves."
        ),
    },
    {
        "key": "nets",
        "name": "Nets: Unfolding Solid Shapes",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A net is a solid unfolded: the 2D pattern of faces that folds "
            "up - with no overlaps and no gaps - into the 3D shape. The "
            "cube's net is 6 squares joined edge to edge (the familiar "
            "cross shape is one of 11 distinct cube nets). The rectangular "
            "prism's net is 6 rectangles in three pairs. The square "
            "pyramid's net is a square with a triangle on each side. The "
            "cylinder's net is two circles plus a rectangle (the unrolled "
            "lateral surface, 2 pi r by h). The cone's net is a circle plus "
            "a circular sector (the unrolled side). Nets are how the world "
            "manufactures solids: cardboard boxes are cut as nets and "
            "folded, sheet-metal tanks are developed from nets, gift wrap "
            "is net-thinking, and sewing patterns are nets for the human "
            "body. Surface area is simply the area of the net - which is "
            "why the surface-area record's decomposition method works. A "
            "net must use exactly the solid's faces: 6 squares for the "
            "cube, and every valid cube net folds without overlap."
        ),
        "how_it_works": (
            "A valid net is a connected arrangement of the solid's faces "
            "joined along full edges such that folding along the joints "
            "closes the solid with each face landing exactly once. The "
            "cross net folds into a cube: the center square becomes the "
            "bottom, the four arms become the sides, the sixth square the "
            "top. Counting distinct cube nets (11) is a classic "
            "combinatorial result. The demonstration program verifies the "
            "face counts of each net (cube 6 squares, box 6 rectangles, "
            "square pyramid 1 square plus 4 triangles, cylinder 2 circles "
            "plus 1 rectangle, cone 1 circle plus 1 sector), checks the "
            "cube net's total area against the surface-area formula (side "
            "4: 96), and confirms the cylinder net's rectangle dimensions "
            "(2 pi r by h) within tight bounds."
        ),
        "key_points": [
            "A net is the solid's faces laid flat, joined edge to edge, folding up with no overlaps or gaps.",
            "The cube has 11 distinct nets; the cross of 6 squares is the famous one.",
            "Cylinder net: 2 circles plus a 2 pi r by h rectangle; cone net: a circle plus a circular sector.",
            "Nets are manufacturing: boxes, sheet metal, gift wrap, and sewing patterns are all net-thinking.",
            "Surface area is the area of the net - the decomposition method made visible.",
        ],
        "requirements": [
            "Nets defined as unfolded face patterns with the no-overlap-no-gap folding condition.",
            "The net described for each of the five database solids (cube, box, pyramid, cylinder, cone).",
            "The 11 distinct cube nets stated as the classical count.",
            "Manufacturing applications named (at least three).",
            "The net-area-equals-surface-area identity stated and verified numerically for the cube.",
        ],
        "standards": [
            "Representing three-dimensional figures with nets is the Common Core 6th-grade standard (6.G).",
            "The 11 cube nets are the classical combinatorial enumeration.",
            "Using nets to find surface area is the standard solid-geometry method of the high-school progression.",
        ],
        "citations": [CIT_CC, CIT_NCTM],
        "sig_lens": (
            "The Signature read: the net is the covenant laid open - the "
            "solid confessing all its faces flat before it stands. Where "
            "public geometry folds the cross into a cube, the Signature "
            "Geometry reads the pattern: six squares, eleven ways, one "
            "oath kept standing."
        ),
    },
    {
        "key": "euler",
        "name": "Euler's Formula: Faces Plus Vertices Minus Edges",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "In 1758 Leonhard Euler discovered the most beautiful "
            "equation in solid geometry: for every convex polyhedron, "
            "faces plus vertices minus edges always equals 2. The cube: 6 "
            "plus 8 minus 12 is 2. The square pyramid: 5 plus 5 minus 8 is "
            "2. The tetrahedron: 4 plus 4 minus 6 is 2. The "
            "rectangular prism: 6 plus 8 minus 12 is 2. No matter how "
            "many faces the polyhedron grows, the count balances to 2 - "
            "it is a topological invariant, a property of the shape's "
            "deep structure rather than its measurements. The formula is a "
            "powerful error-check: count a solid's features, and if "
            "F + V - E is not 2, the count is wrong or the solid is not a "
            "convex polyhedron. It fails for curved solids (the sphere has "
            "no faces to count) and for solids with holes (a donut-shaped "
            "torus gives 0), which is exactly the point: the formula "
            "detects the shape's true nature. Euler called it, and "
            "mathematicians still call it, one of the finest theorems "
            "ever proved."
        ),
        "how_it_works": (
            "The proof removes faces one by one: start with the "
            "polyhedron, delete one face (F drops by 1, the count becomes "
            "1), then repeatedly collapse boundary edges - each collapse "
            "removes one edge and one vertex together, keeping F + V - E "
            "unchanged - until a single triangle remains (3 faces "
            "counting the outside, 3 vertices, 3 edges: 3 + 3 - 3 = 3... "
            "the careful version tracks the running total to 1, and "
            "restoring the deleted face brings it to 2). Intuition "
            "suffices here: the invariant survives every legal "
            "simplification. The demonstration program verifies the "
            "formula on the cube (6 + 8 - 12 = 2), the square pyramid "
            "(5 + 5 - 8 = 2), the tetrahedron (4 + 4 - 6 = 2), a "
            "pentagonal prism (7 + 10 - 15 = 2), and a hexagonal pyramid "
            "(7 + 7 - 12 = 2), all exact integer arithmetic."
        ),
        "key_points": [
            "Euler's formula: for every convex polyhedron, F + V - E = 2, discovered 1758.",
            "Verified: cube 6+8-12, square pyramid 5+5-8, tetrahedron 4+4-6, pentagonal prism 7+10-15 - all equal 2.",
            "It is a topological invariant: a property of deep structure, not of measurements.",
            "Use it as an error-check: if the count is not 2, the survey is wrong or the solid is not a convex polyhedron.",
            "It fails informatively: curved solids have no faces to count; a torus (donut) gives 0 - the formula detects true nature.",
        ],
        "requirements": [
            "The formula stated exactly (F + V - E = 2) with Euler's name and the 1758 date.",
            "Verified on at least five polyhedra with their counts shown.",
            "Topological invariant explained in plain language.",
            "The error-checking use stated explicitly.",
            "The informative failures named (curved solids, torus).",
        ],
        "standards": [
            "Euler's polyhedron formula (1758) is the foundational result of topology as applied to convex polyhedra.",
            "Verifying F + V - E = 2 by counting is the standard solid-geometry exercise of the high-school progression.",
            "The invariant's independence from measurement follows the NCTM connections standard.",
        ],
        "citations": [CIT_EUCLID, CIT_NCTM],
        "sig_lens": (
            "The Signature read: Euler's formula is the covenant of "
            "balance - faces plus witnesses minus edges, always two, for "
            "every honest solid. Where public geometry proves the "
            "invariant, the Signature Geometry keeps the ledger: six plus "
            "eight minus twelve, and the books balance at two."
        ),
    },
    {
        "key": "congruence_similarity",
        "name": "Congruence and Similarity: Same Shape, Same or Scaled Size",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Two shapes are congruent when they are exactly the same shape "
            "and size - one can be laid perfectly on top of the other "
            "(flipping allowed). All corresponding sides and angles match. "
            "Two shapes are similar when they are the same shape but "
            "possibly different sizes - one is a scaled copy of the other, "
            "like a photograph and its enlargement. Similar shapes have "
            "equal corresponding angles, and their corresponding sides are "
            "in the same ratio: the scale factor. All circles are similar "
            "to each other; all squares are similar to each other; but "
            "rectangles need not be (a 2-by-4 and a 3-by-5 are different "
            "shapes in the similarity sense). Scaling has sharp "
            "consequences: lengths scale by the factor k, areas by k-squared, "
            "volumes by k-cubed. Double a cube's side (k=2) and its surface "
            "area quadruples while its volume octuples - the square-cube "
            "law, which is why ants are strong for their size and why "
            "overheating limits how large machines can grow."
        ),
        "how_it_works": (
            "Similarity is tested by ratios: divide each side of one shape "
            "by the corresponding side of the other - equal ratios (and "
            "equal angles) mean similar. The power laws follow from the "
            "formulas: area contains two length factors (k times k), "
            "volume three (k times k times k). So a scale factor of 3 "
            "multiplies lengths by 3, areas by 9, volumes by 27. The "
            "demonstration program verifies similarity of two rectangles "
            "(4-by-6 and 6-by-9: ratios both 1.5) and non-similarity of "
            "4-by-6 and 5-by-9, then checks the power laws on a scaled "
            "cube (side 2 to side 6: lengths x3, surface area 24 to 216 "
            "i.e. x9, volume 8 to 216 i.e. x27), all within tight bounds."
        ),
        "key_points": [
            "Congruent means same shape AND same size (superimposable); similar means same shape, possibly scaled.",
            "Similar shapes have equal corresponding angles and proportional corresponding sides (one scale factor).",
            "All circles are similar; all squares are similar; rectangles need not be.",
            "Scaling laws: lengths by k, areas by k-squared, volumes by k-cubed - the square-cube law.",
            "The square-cube law explains nature and engineering: ant strength, machine overheating limits.",
        ],
        "requirements": [
            "Congruence and similarity each defined precisely, with the superimposable test for congruence.",
            "The scale-factor ratio test stated for similarity.",
            "The always-similar families named (circles, squares, equilateral triangles) with the rectangle counterexample.",
            "The k, k-squared, k-cubed laws stated and demonstrated numerically on a scaled cube.",
            "A real consequence named (ant strength or machine heat).",
        ],
        "standards": [
            "Congruence via rigid motions and similarity via dilations are the Common Core 8th-grade/high-school standards (8.G, G-CO, G-SRT).",
            "The square-cube scaling laws follow the dimensional analysis of the measurement standards.",
            "All circles' similarity is the basis of pi's constancy (7.G).",
        ],
        "citations": [CIT_CC, CIT_NCTM],
        "sig_lens": (
            "The Signature read: similarity is the covenant honored at "
            "every size - the small square and the great square swearing "
            "the same oath, only louder. Where public geometry scales by "
            "k, k-squared, k-cubed, the Signature Geometry measures the "
            "keeping: the shape never breaks its word, it only speaks it "
            "bigger."
        ),
    },
    {
        "key": "transformations",
        "name": "Transformations: Slides, Flips, and Turns",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A transformation moves a shape: a translation (slide) shifts "
            "every point by the same distance in the same direction; a "
            "reflection (flip) mirrors the shape across a line; a rotation "
            "(turn) spins it about a point by an angle. Slides, flips, and "
            "turns are the rigid motions - they never change the shape's "
            "size or its angles, so the image is always congruent to the "
            "original. Coordinates make them arithmetic: translating the "
            "point (3, 4) by (2, -1) gives (5, 3); reflecting (3, 4) over "
            "the x-axis gives (3, -4); rotating (3, 4) ninety degrees "
            "counterclockwise about the origin gives (-4, 3). A fourth "
            "transformation, the dilation, scales the shape from a center "
            "point by a factor - this one changes size, producing similar "
            "(not congruent) images, and it is the engine of similarity. "
            "Transformations are the grammar of design and animation: "
            "every moved sprite, every folded pattern, every tiled floor "
            "is a sentence written in slides, flips, turns, and scales."
        ),
        "how_it_works": (
            "Each rigid motion is a coordinate rule applied to every "
            "vertex: translation adds the shift vector; x-axis reflection "
            "negates y; 90-degree counterclockwise rotation maps (x, y) "
            "to (-y, x). Because the rules preserve all distances between "
            "points, the transformed polygon is congruent to the original "
            "automatically - congruence is defined by the existence of "
            "such a motion. Dilation multiplies every coordinate (relative "
            "to the center) by the scale factor, preserving angles while "
            "scaling lengths. The demonstration program applies all four "
            "transformations to the point (3, 4) - translation to (5, 3), "
            "x-axis reflection to (3, -4), 90-degree rotation to (-4, 3), "
            "dilation by 2 to (6, 8) - and verifies a translated triangle "
            "keeps its side lengths (congruence) within tight bounds."
        ),
        "key_points": [
            "Translation slides, reflection flips across a line, rotation turns about a point - the three rigid motions.",
            "Rigid motions preserve size and angles: the image is always congruent to the original.",
            "Coordinate rules: translate (3,4) by (2,-1) to (5,3); reflect over x-axis to (3,-4); rotate 90 deg CCW to (-4,3).",
            "Dilation scales from a center by a factor: it changes size, producing similar images - the engine of similarity.",
            "Transformations are the grammar of design and animation: sprites, patterns, tilings are written in these moves.",
        ],
        "requirements": [
            "All four transformations defined (translation, reflection, rotation, dilation) with the rigid/non-rigid split.",
            "Congruence tied to rigid motions: the image of a rigid motion is congruent by definition.",
            "Coordinate rules given and worked for the point (3, 4) in all four cases.",
            "Dilation identified as the similarity engine.",
            "Design/animation applications named.",
        ],
        "standards": [
            "Rigid motions and their coordinate rules are the Common Core 8th-grade standard (8.G).",
            "Congruence defined via rigid motions and similarity via dilations are the high-school standards (G-CO, G-SRT).",
            "Describing transformations with coordinates is the standard analytic-geometry practice.",
        ],
        "citations": [CIT_CC, CIT_NCTM],
        "sig_lens": (
            "The Signature read: the transformations are the covenant in "
            "motion - the shape may slide, flip, and turn, but the rigid "
            "oath never bends: distances kept, angles kept, the word "
            "unchanged. Where public geometry moves the points, the "
            "Signature Geometry watches the keeping: (3, 4) becomes (5, "
            "3), and not a length is lost."
        ),
    },
]

assert len(ENTRIES) == 34, "expected 34 entries, got %d" % len(ENTRIES)
assert len({e["key"] for e in ENTRIES}) == 34, "duplicate entry keys"
ranks = [e["ladder_rank"] for e in ENTRIES]
assert ranks == sorted(ranks), "entries not in ladder order"
assert all(1 <= r <= 10 for r in ranks), "ladder_rank out of range"
assert all(e["ladder_tier"] in ("foundations", "compounded", "advanced") for e in ENTRIES)
