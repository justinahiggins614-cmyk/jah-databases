#!/usr/bin/env python3
"""Entries for the Science Quiz databases (Manon's 2026-10-17 16:15 order:
"Test then quiz databases with answers at bottom").

Two NEW databases, 34 ladder-ordered records each:

  quiz-science            - The Science Quiz Database
                            (public-harvest: real, fact-checked science
                            quizzes - physics, chemistry, biology, earth
                            science, astronomy; every record one complete
                            10-question quiz with the answer key AT THE
                            BOTTOM of the record, per his explicit
                            requirement)
  quiz-science-signature  - The Science Quiz Signature Database
                            (his original Signature Quiz Method: every quiz
                            a proving ground of knowledge, the question a
                            challenge of the mind, the answer key at the
                            bottom the sealed judgment, mastery the
                            covenant stamp; src signature, titles suffixed
                            " (Signature Edition)", never presented as
                            authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-QZSC- (public) and JAH-QZSCS- (signature), verified free
in the manifest id_prefix values and in every shard index (zero hits) on
2026-10-17. Slug "quiz-science" is free - no quiz databases exist yet.

Every question and answer is hand-authored, fact-checked real science.
Numerical cores: the demos are quiz runners with answer reveal and a
simulated graded attempt (see demos_quiz_science.py). Every demo prints its
real computed values, asserts tight bounds (never float exact-equality),
and ends with the OK marker; the build machine-executes all 68 demos and
cross-checks every answer against the demo output before writing.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Quiz Method: every "
            "quiz a proving ground of knowledge, the question a challenge of "
            "the mind, the answer key at the bottom the sealed judgment, and "
            "mastery the covenant stamp. Clearly labeled Signature-made, "
            "never presented as authentic public record.")

# ---------------------------------------------------------------- standards

STD_PHYS = [
    "Next Generation Science Standards (NGSS), Physical Science core ideas: "
    "forces and interactions, energy, waves and their applications.",
    "Common Core Mathematics Practice MP.2: reason abstractly and "
    "quantitatively (measurement, ratios, formula use).",
]
STD_CHEM = [
    "Next Generation Science Standards (NGSS), Physical Science core ideas: "
    "matter and its interactions, structure and properties of matter.",
    "Common Core Mathematics Practice MP.4: model with mathematics "
    "(balanced equations, mole calculations).",
]
STD_BIO = [
    "Next Generation Science Standards (NGSS), Life Science core ideas: "
    "from molecules to organisms, ecosystems, heredity, biological "
    "evolution.",
    "Common Core ELA RST: read and interpret scientific text and data.",
]
STD_EARTH = [
    "Next Generation Science Standards (NGSS), Earth and Space Science core "
    "ideas: Earth systems, Earth and human activity, weather and climate.",
    "Common Core Mathematics Practice MP.2: reason abstractly and "
    "quantitatively (cycles, scales, rates).",
]
STD_ASTRO = [
    "Next Generation Science Standards (NGSS), Earth and Space Science core "
    "ideas: the universe and its stars, Earth and the solar system.",
    "Common Core ELA RST: read and interpret scientific text, scales, and "
    "models of the cosmos.",
]

# ---------------------------------------------------------------- citations

CIT_PHYS = [
    "OpenStax. College Physics 2e. Rice University; 2022.",
    "National Research Council. A Framework for K-12 Science Education. "
    "National Academies Press; 2012.",
]
CIT_CHEM = [
    "OpenStax. Chemistry 2e. Rice University; 2019.",
    "National Research Council. A Framework for K-12 Science Education. "
    "National Academies Press; 2012.",
]
CIT_BIO = [
    "OpenStax. Concepts of Biology. Rice University; 2013.",
    "National Research Council. A Framework for K-12 Science Education. "
    "National Academies Press; 2012.",
]
CIT_EARTH = [
    "Tarbuck EJ, Lutgens FK, Tasa D. Earth Science. 15th ed. Pearson; 2018.",
    "National Research Council. A Framework for K-12 Science Education. "
    "National Academies Press; 2012.",
]
CIT_ASTRO = [
    "OpenStax. Astronomy 2e. Rice University; 2022.",
    "National Research Council. A Framework for K-12 Science Education. "
    "National Academies Press; 2012.",
]

# ---------------------------------------------------------------- shared

REQUIREMENTS = [
    "A pencil and paper, or run the demonstration program below to take the quiz.",
    "Answer all 10 questions before looking at the answer key at the bottom.",
    "Score 7 or more correct to pass this quiz; re-take until every answer is known.",
]

DESC_TAIL = (" This quiz has 10 questions; write your answers first, then "
             "check them against the answer key at the bottom of this record.")

# ---------------------------------------------------------------- entries

ENTRIES = [
    # ---------------- FOUNDATIONS ----------------
    {
        "key": "motion-basics",
        "name": "What Is Motion? A First Physics Quiz",
        "group": "Physics",
        "ladder_rank": 1, "ladder_tier": "foundations",
        "description": ("The very first physics quiz: motion, speed, and "
                        "distance in everyday words. Tests whether a reader "
                        "can spot motion, name how fast things go, and "
                        "measure distance. Rank 1 on the teaching ladder."
                        + DESC_TAIL),
        "questions": [
            ("Which way does an object move when you push it?",
             "It moves in the direction of the push."),
            ("What word describes how fast something is moving?",
             "Speed."),
            ("What tool measures how long something is?",
             "A ruler (or meter stick, or tape measure)."),
            ("Which moves faster: a walking person or a running person?",
             "The running person."),
            ("When a car stops moving, its speed becomes what?",
             "Zero."),
            ("What makes a rolling ball slow down on the ground?",
             "Friction (and air resistance)."),
            ("Which of these is a unit for measuring distance: mile, gallon, or pound?",
             "Mile."),
            ("What word means a change of position over time?",
             "Motion."),
            ("If you walk 10 steps forward, your position has done what?",
             "It has changed (you have moved)."),
            ("What do you call the place where a race begins?",
             "The start line (the starting point)."),
        ],
        "key_points": [
            "Motion is a change of position over time.",
            "Speed tells how fast something moves; distance tells how far it travels.",
            "Pushes move objects in the direction of the push; friction slows motion down.",
        ],
        "requirements": list(REQUIREMENTS),
        "standards": list(STD_PHYS),
        "citations": list(CIT_PHYS),
    },
    {
        "key": "matter-around-us",
        "name": "Matter All Around Us",
        "group": "Chemistry",
        "ladder_rank": 1, "ladder_tier": "foundations",
        "description": ("The very first chemistry quiz: the three common "
                        "states of matter and how they behave. Tests the "
                        "idea that everything that takes up space is matter, "
                        "with ice, water, and steam as the examples. Rank 1 "
                        "on the teaching ladder." + DESC_TAIL),
        "questions": [
            ("Name the three common states of matter.",
             "Solid, liquid, and gas."),
            ("Which state of matter keeps its own shape?",
             "Solid."),
            ("Which state takes the shape of its container?",
             "Liquid and gas."),
            ("What is ice, in terms of states of matter?",
             "Water in the solid state."),
            ("What happens when ice melts?",
             "It becomes liquid water."),
            ("What is steam?",
             "Water in the gas state."),
            ("What do we call the change from liquid to gas?",
             "Evaporation (boiling when strongly heated)."),
            ("Which takes up more space: the water in a cup or the steam made from it?",
             "The steam."),
            ("Is air matter? Why?",
             "Yes, because air takes up space and has mass."),
            ("What word means anything that takes up space and has mass?",
             "Matter."),
        ],
        "key_points": [
            "Matter is anything with mass that takes up space.",
            "Solids hold their shape; liquids and gases take their container's shape.",
            "Melting and evaporation change state without changing the substance.",
        ],
        "requirements": list(REQUIREMENTS),
        "standards": list(STD_CHEM),
        "citations": list(CIT_CHEM),
    },
    {
        "key": "living-things-needs",
        "name": "Living Things and Their Needs",
        "group": "Biology",
        "ladder_rank": 1, "ladder_tier": "foundations",
        "description": ("The very first biology quiz: what makes something "
                        "alive and what living things need to survive. Tests "
                        "the difference between living and non-living things "
                        "with plain everyday examples. Rank 1 on the teaching "
                        "ladder." + DESC_TAIL),
        "questions": [
            ("Name three things living things need to survive.",
             "Water, food (nutrients), and air (oxygen)."),
            ("Which gas do most animals breathe in?",
             "Oxygen."),
            ("Which living things make their own food?",
             "Plants."),
            ("What do we call an animal that eats plants?",
             "A herbivore."),
            ("What do we call an animal that eats other animals?",
             "A carnivore."),
            ("What do living things do when they make more of their own kind?",
             "They reproduce."),
            ("Which of these is alive: a rock, a seed, or a glass?",
             "A seed."),
            ("What do plants take in from the air for photosynthesis?",
             "Carbon dioxide."),
            ("What do living things sense and respond to in their surroundings?",
             "Stimuli."),
            ("What is the young form of a frog called?",
             "A tadpole."),
        ],
        "key_points": [
            "Living things need water, food, and air; they grow, respond, and reproduce.",
            "Plants make their own food; animals get food by eating.",
            "A seed is alive; a rock and a glass are not.",
        ],
        "requirements": list(REQUIREMENTS),
        "standards": list(STD_BIO),
        "citations": list(CIT_BIO),
    },
    {
        "key": "day-night-seasons",
        "name": "Day, Night, and the Seasons",
        "group": "Earth Science",
        "ladder_rank": 1, "ladder_tier": "foundations",
        "description": ("The very first earth science quiz: why we have day "
                        "and night, and why the seasons change. Tests the "
                        "basic rhythm of Earth's rotation and orbit. Rank 1 "
                        "on the teaching ladder." + DESC_TAIL),
        "questions": [
            ("What causes day and night?",
             "Earth's rotation: one full spin takes about 24 hours."),
            ("How long does Earth take to orbit the Sun?",
             "About 365 days (one year)."),
            ("What causes the seasons?",
             "The tilt of Earth's axis as it orbits the Sun."),
            ("Which season is warmest in the Northern Hemisphere?",
             "Summer."),
            ("Where does the Sun appear to rise?",
             "In the east."),
            ("How many months are in one year?",
             "Twelve."),
            ("What shape is Earth's orbit around the Sun?",
             "Nearly circular (an ellipse)."),
            ("When the Northern Hemisphere has summer, what season does the Southern Hemisphere have?",
             "Winter."),
            ("How long is one full day?",
             "24 hours."),
            ("What is the name of the imaginary line Earth spins around?",
             "Earth's axis."),
        ],
        "key_points": [
            "Day and night come from Earth's rotation; years come from its orbit.",
            "Seasons come from Earth's tilt, not from distance to the Sun.",
            "The Sun appears to rise in the east and set in the west.",
        ],
        "requirements": list(REQUIREMENTS),
        "standards": list(STD_EARTH),
        "citations": list(CIT_EARTH),
    },
    {
        "key": "pushes-pulls-magnets",
        "name": "Pushes, Pulls, and Magnets",
        "group": "Physics",
        "ladder_rank": 2, "ladder_tier": "foundations",
        "description": ("A foundations physics quiz on forces: pushes and "
                        "pulls, gravity, friction, and magnets. Tests "
                        "naming forces in everyday situations and the rules "
                        "of magnetic poles. Rank 2 on the teaching ladder."
                        + DESC_TAIL),
        "questions": [
            ("What is a force?",
             "A push or a pull."),
            ("Which force pulls objects toward Earth?",
             "Gravity."),
            ("What are the two poles of a magnet called?",
             "The north pole and the south pole."),
            ("Which poles of two magnets push each other apart?",
             "Like poles (north-north or south-south)."),
            ("Which poles of two magnets attract each other?",
             "Opposite poles (north-south)."),
            ("What common material do magnets attract most strongly?",
             "Iron."),
            ("What do we call the force that opposes sliding?",
             "Friction."),
            ("Which is smoother to slide on: ice or sandpaper?",
             "Ice."),
            ("What happens to a ball you roll across grass?",
             "Friction slows it down until it stops."),
            ("Is the force you use to open a door a push or a pull?",
             "Either a pull or a push, depending on which way the door swings."),
        ],
        "key_points": [
            "Forces are pushes and pulls; gravity and friction act everywhere.",
            "Like magnetic poles repel; opposite poles attract.",
            "Friction opposes sliding and eventually stops rolling and sliding objects.",
        ],
        "requirements": list(REQUIREMENTS),
        "standards": list(STD_PHYS),
        "citations": list(CIT_PHYS),
    },
    {
        "key": "air-and-mixtures",
        "name": "The Air We Breathe and Mixtures",
        "group": "Chemistry",
        "ladder_rank": 2, "ladder_tier": "foundations",
        "description": ("A foundations chemistry quiz on mixtures and the "
                        "air: what mixtures are, what air is made of, and "
                        "how to separate mixtures. Tests solutions versus "
                        "mixtures with visible parts. Rank 2 on the teaching "
                        "ladder." + DESC_TAIL),
        "questions": [
            ("What is a mixture?",
             "Two or more substances physically combined that can be separated."),
            ("Is air a mixture or a pure substance?",
             "A mixture."),
            ("Which gas makes up most of Earth's air?",
             "Nitrogen (about 78 percent)."),
            ("About how much of the air is oxygen?",
             "About 21 percent."),
            ("What do we call a mixture you cannot see the parts of, like salt water?",
             "A solution."),
            ("What do we call a mixture you can see the parts of, like a fruit salad?",
             "A heterogeneous mixture."),
            ("How could you separate sand from water?",
             "By filtering (or decanting) the water away from the sand."),
            ("How could you separate salt dissolved in water?",
             "By evaporating the water, leaving the salt behind."),
            ("In salt water, which substance is the solvent?",
             "Water."),
            ("In salt water, which substance is the solute?",
             "Salt."),
        ],
        "key_points": [
            "Air is a mixture, mostly nitrogen and oxygen.",
            "Solutions are uniform mixtures; heterogeneous mixtures show their parts.",
            "Mixtures can be separated by filtering, decanting, or evaporation.",
        ],
        "requirements": list(REQUIREMENTS),
        "standards": list(STD_CHEM),
        "citations": list(CIT_CHEM),
    },
    {
        "key": "plants-and-growth",
        "name": "Plants and How They Grow",
        "group": "Biology",
        "ladder_rank": 2, "ladder_tier": "foundations",
        "description": ("A foundations biology quiz on plants: their parts "
                        "and what each part does, plus what plants need to "
                        "grow. Tests roots, stems, leaves, and the inputs "
                        "and outputs of photosynthesis. Rank 2 on the "
                        "teaching ladder." + DESC_TAIL),
        "questions": [
            ("What are the three main parts of a plant?",
             "Roots, stem, and leaves."),
            ("Which part of the plant takes in water?",
             "The roots."),
            ("Which part holds the plant upright?",
             "The stem."),
            ("Where does a plant make its food?",
             "In the leaves."),
            ("What energy source powers photosynthesis?",
             "Sunlight."),
            ("What gas do plants take in from the air?",
             "Carbon dioxide."),
            ("What gas do plants release?",
             "Oxygen."),
            ("What green pigment captures sunlight?",
             "Chlorophyll."),
            ("What do seeds need to sprout?",
             "Water, warmth, and air (oxygen)."),
            ("What do we call the plant's first food store inside a seed?",
             "The endosperm (or cotyledon food store)."),
        ],
        "key_points": [
            "Roots take in water, stems support, leaves make food.",
            "Photosynthesis uses sunlight, carbon dioxide, and water to make food.",
            "Oxygen released by plants is what animals breathe.",
        ],
        "requirements": list(REQUIREMENTS),
        "standards": list(STD_BIO),
        "citations": list(CIT_BIO),
    },
    {
        "key": "sun-and-planets",
        "name": "Our Sun and the Planets",
        "group": "Astronomy",
        "ladder_rank": 2, "ladder_tier": "foundations",
        "description": ("A foundations astronomy quiz on the solar system: "
                        "the Sun, the eight planets, and their order. Tests "
                        "planet names, positions, and the force that holds "
                        "it all together. Rank 2 on the teaching ladder."
                        + DESC_TAIL),
        "questions": [
            ("What is the Sun?",
             "A star: a huge ball of hot, glowing gas."),
            ("How many planets orbit the Sun?",
             "Eight."),
            ("Which planet is closest to the Sun?",
             "Mercury."),
            ("Which planet is farthest from the Sun?",
             "Neptune."),
            ("Which planet is known as the Red Planet?",
             "Mars."),
            ("Which planet has the most visible rings?",
             "Saturn."),
            ("Which is the largest planet?",
             "Jupiter."),
            ("Which planet do we live on?",
             "Earth."),
            ("Which planet is often called Earth's twin because of its similar size?",
             "Venus."),
            ("What holds the planets in their orbits around the Sun?",
             "The Sun's gravity."),
        ],
        "key_points": [
            "The Sun is a star; eight planets orbit it.",
            "Planet order from the Sun: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune.",
            "Gravity holds the solar system together.",
        ],
        "requirements": list(REQUIREMENTS),
        "standards": list(STD_ASTRO),
        "citations": list(CIT_ASTRO),
    },
    {
        "key": "simple-machines",
        "name": "Simple Machines",
        "group": "Physics",
        "ladder_rank": 3, "ladder_tier": "foundations",
        "description": ("A foundations physics quiz on the six simple "
                        "machines and what they do. Tests naming each "
                        "machine, spotting them in everyday objects, and "
                        "understanding how they make work easier. Rank 3 on "
                        "the teaching ladder." + DESC_TAIL),
        "questions": [
            ("Name the six simple machines.",
             "Lever, wheel and axle, pulley, inclined plane, wedge, and screw."),
            ("Which simple machine is a seesaw?",
             "A lever."),
            ("Which simple machine is a ramp?",
             "An inclined plane."),
            ("Which simple machine lifts a flag up a pole?",
             "A pulley."),
            ("What does a simple machine do?",
             "It makes work easier by changing the size or direction of a force."),
            ("Which simple machine is a doorknob?",
             "A wheel and axle."),
            ("Which simple machine is a nail?",
             "A wedge."),
            ("Which simple machine is a jar lid?",
             "A screw."),
            ("Does a simple machine reduce the total amount of work?",
             "No: it spreads the work over a longer distance or changes its direction."),
            ("What is the fixed point that a lever pivots on?",
             "The fulcrum."),
        ],
        "key_points": [
            "The six simple machines: lever, wheel and axle, pulley, inclined plane, wedge, screw.",
            "Machines trade force for distance; they never reduce total work.",
            "Simple machines are the building blocks of all complex machines.",
        ],
        "requirements": list(REQUIREMENTS),
        "standards": list(STD_PHYS),
        "citations": list(CIT_PHYS),
    },
    {
        "key": "acids-and-bases",
        "name": "Acids and Bases Around the Home",
        "group": "Chemistry",
        "ladder_rank": 3, "ladder_tier": "foundations",
        "description": ("A foundations chemistry quiz on acids and bases "
                        "using everyday examples. Tests the pH scale, "
                        "neutralization, and recognizing acids and bases in "
                        "the home. Rank 3 on the teaching ladder."
                        + DESC_TAIL),
        "questions": [
            ("What do acids taste like?",
             "Sour."),
            ("Name a common acid found in citrus fruits.",
             "Citric acid."),
            ("What do bases feel like?",
             "Slippery (soapy)."),
            ("What scale measures acidity?",
             "The pH scale."),
            ("What pH value is neutral?",
             "7."),
            ("Are acids above or below 7 on the pH scale?",
             "Below 7."),
            ("What happens when an acid and a base mix?",
             "They neutralize each other, forming salt and water."),
            ("Which is more acidic: lemon juice or pure water?",
             "Lemon juice."),
            ("What gas in carbonated drinks makes them slightly acidic?",
             "Carbon dioxide."),
            ("Name one common base used in cleaning.",
             "Ammonia (or baking soda, sodium bicarbonate)."),
        ],
        "key_points": [
            "The pH scale runs 0-14: below 7 is acidic, 7 is neutral, above 7 is basic.",
            "Acids taste sour; bases feel slippery.",
            "Acid plus base neutralize each other into salt and water.",
        ],
        "requirements": list(REQUIREMENTS),
        "standards": list(STD_CHEM),
        "citations": list(CIT_CHEM),
    },
    {
        "key": "bones-and-muscles",
        "name": "The Human Body: Bones and Muscles",
        "group": "Biology",
        "ladder_rank": 3, "ladder_tier": "foundations",
        "description": ("A foundations biology quiz on the human "
                        "musculoskeletal system: bones, joints, muscles, and "
                        "how they work together. Tests the 206-bone skeleton, "
                        "tendons, and ligaments. Rank 3 on the teaching "
                        "ladder." + DESC_TAIL),
        "questions": [
            ("What is the human body's framework called?",
             "The skeleton."),
            ("How many bones does an adult human have?",
             "206."),
            ("Which bone protects the brain?",
             "The skull."),
            ("Which bones protect the heart and lungs?",
             "The ribs."),
            ("What connects muscles to bones?",
             "Tendons."),
            ("What connects bones to other bones at joints?",
             "Ligaments."),
            ("Which is the longest bone in the human body?",
             "The femur (thigh bone)."),
            ("Do muscles push or pull to move bones?",
             "Pull: muscles contract to pull bones."),
            ("What tough tissue cushions the joints?",
             "Cartilage."),
            ("What do we call the place where two bones meet?",
             "A joint."),
        ],
        "key_points": [
            "The adult skeleton has 206 bones that protect organs and give structure.",
            "Tendons join muscle to bone; ligaments join bone to bone.",
            "Muscles pull bones by contracting; joints and cartilage let them move smoothly.",
        ],
        "requirements": list(REQUIREMENTS),
        "standards": list(STD_BIO),
        "citations": list(CIT_BIO),
    },
    {
        "key": "rocks-and-rock-cycle",
        "name": "Rocks and the Rock Cycle",
        "group": "Earth Science",
        "ladder_rank": 3, "ladder_tier": "foundations",
        "description": ("A foundations earth science quiz on the three rock "
                        "types and how each forms. Tests igneous, "
                        "sedimentary, and metamorphic rocks plus magma, "
                        "lava, and the rock cycle. Rank 3 on the teaching "
                        "ladder." + DESC_TAIL),
        "questions": [
            ("Name the three main rock types.",
             "Igneous, sedimentary, and metamorphic."),
            ("Which rock type forms from cooled magma or lava?",
             "Igneous."),
            ("Which rock type forms from pressed layers of sediment?",
             "Sedimentary."),
            ("Which rock type forms when heat and pressure change existing rock?",
             "Metamorphic."),
            ("What is molten rock beneath Earth's surface called?",
             "Magma."),
            ("What is molten rock on Earth's surface called?",
             "Lava."),
            ("Which sedimentary rock forms from compressed sand?",
             "Sandstone."),
            ("Which metamorphic rock forms from limestone?",
             "Marble."),
            ("What do we call the continuous process that forms and changes rocks?",
             "The rock cycle."),
            ("What is the hardest natural mineral?",
             "Diamond."),
        ],
        "key_points": [
            "Igneous rocks cool from magma; sedimentary rocks press from sediment; metamorphic rocks transform under heat and pressure.",
            "Magma is underground; lava is on the surface.",
            "The rock cycle continuously forms, breaks, and re-forms rock.",
        ],
        "requirements": list(REQUIREMENTS),
        "standards": list(STD_EARTH),
        "citations": list(CIT_EARTH),
    },
    {
        "key": "light-shadows-color",
        "name": "Light, Shadows, and Color",
        "group": "Physics",
        "ladder_rank": 4, "ladder_tier": "foundations",
        "description": ("A foundations physics quiz on light: how it "
                        "travels, shadows, reflection, refraction, and "
                        "color. Tests the speed of light, prisms, and why "
                        "objects look the colors they do. Rank 4 on the "
                        "teaching ladder." + DESC_TAIL),
        "questions": [
            ("What is the main source of light on Earth?",
             "The Sun."),
            ("How does light travel?",
             "In straight lines (light rays)."),
            ("What do we call the dark area behind an object that blocks light?",
             "A shadow."),
            ("What happens when light passes through a prism?",
             "It separates into the colors of the rainbow."),
            ("Name the colors of the rainbow in order.",
             "Red, orange, yellow, green, blue, indigo, violet."),
            ("What color objects reflect all colors of light?",
             "White."),
            ("What color objects absorb all colors of light?",
             "Black."),
            ("What do we call light bouncing off a surface?",
             "Reflection."),
            ("What do we call light bending as it passes through water or glass?",
             "Refraction."),
            ("About how fast does light travel?",
             "About 300,000 kilometers per second (about 186,000 miles per second)."),
        ],
        "key_points": [
            "Light travels in straight lines at about 300,000 km/s.",
            "Reflection bounces light; refraction bends it.",
            "An object's color is the light it reflects.",
        ],
        "requirements": list(REQUIREMENTS),
        "standards": list(STD_PHYS),
        "citations": list(CIT_PHYS),
    },
    {
        "key": "periodic-table-reading",
        "name": "The Periodic Table: Reading the Chart",
        "group": "Chemistry",
        "ladder_rank": 4, "ladder_tier": "foundations",
        "description": ("A foundations chemistry quiz on reading the "
                        "periodic table: atomic number, symbols, groups, "
                        "and periods. Tests finding elements and naming "
                        "their symbols. Rank 4 on the teaching ladder."
                        + DESC_TAIL),
        "questions": [
            ("What does each square on the periodic table represent?",
             "A chemical element."),
            ("What does the atomic number tell you?",
             "The number of protons in the atom."),
            ("Which element has atomic number 1?",
             "Hydrogen."),
            ("What is the symbol for oxygen?",
             "O."),
            ("What is the symbol for gold?",
             "Au."),
            ("What is the symbol for iron?",
             "Fe."),
            ("What are the vertical columns of the table called?",
             "Groups (or families)."),
            ("What are the horizontal rows of the table called?",
             "Periods."),
            ("Which element is the lightest?",
             "Hydrogen."),
            ("Who is credited with creating the first periodic table?",
             "Dmitri Mendeleev, in 1869."),
        ],
        "key_points": [
            "Atomic number equals the number of protons and identifies the element.",
            "Groups are vertical columns; periods are horizontal rows.",
            "Mendeleev organized the first periodic table in 1869.",
        ],
        "requirements": list(REQUIREMENTS),
        "standards": list(STD_CHEM),
        "citations": list(CIT_CHEM),
    },
    {
        "key": "ecosystems-food-chains",
        "name": "Ecosystems and Food Chains",
        "group": "Biology",
        "ladder_rank": 4, "ladder_tier": "foundations",
        "description": ("A foundations biology quiz on ecosystems: "
                        "producers, consumers, decomposers, food chains, and "
                        "food webs. Tests how energy flows through living "
                        "communities. Rank 4 on the teaching ladder."
                        + DESC_TAIL),
        "questions": [
            ("What is an ecosystem?",
             "A community of living things interacting with their environment."),
            ("What do producers do?",
             "They make their own food (plants are producers)."),
            ("What are consumers?",
             "Organisms that eat other organisms."),
            ("What is a decomposer?",
             "An organism that breaks down dead matter (fungi, bacteria)."),
            ("What is the first link in most food chains?",
             "A producer (a plant)."),
            ("What do we call an animal that eats both plants and animals?",
             "An omnivore."),
            ("What is a habitat?",
             "The natural home of an organism."),
            ("Which holds more energy: the producer or the top consumer?",
             "The producer."),
            ("What do we call many food chains linked together?",
             "A food web."),
            ("What happens if a top predator is removed from an ecosystem?",
             "Prey populations can grow unchecked, unbalancing the ecosystem."),
        ],
        "key_points": [
            "Producers make food; consumers eat; decomposers recycle.",
            "Energy flows from producers up the food chain.",
            "Removing a species can unbalance the whole ecosystem.",
        ],
        "requirements": list(REQUIREMENTS),
        "standards": list(STD_BIO),
        "citations": list(CIT_BIO),
    },
    {
        "key": "weather-and-water-cycle",
        "name": "Weather and the Water Cycle",
        "group": "Earth Science",
        "ladder_rank": 4, "ladder_tier": "foundations",
        "description": ("A foundations earth science quiz on weather and "
                        "the water cycle: evaporation, condensation, "
                        "precipitation, and the instruments that measure "
                        "weather. Rank 4 on the teaching ladder."
                        + DESC_TAIL),
        "questions": [
            ("What is the water cycle?",
             "The continuous movement of water between Earth's surface and the atmosphere."),
            ("What do we call water falling from clouds?",
             "Precipitation."),
            ("Name three forms of precipitation.",
             "Rain, snow, and hail (or sleet)."),
            ("What process turns liquid water into vapor?",
             "Evaporation."),
            ("What process turns water vapor back into liquid?",
             "Condensation."),
            ("What are clouds made of?",
             "Tiny water droplets or ice crystals."),
            ("What instrument measures temperature?",
             "A thermometer."),
            ("What instrument measures air pressure?",
             "A barometer."),
            ("What is wind?",
             "Moving air."),
            ("In which layer of the atmosphere does weather happen?",
             "The troposphere."),
        ],
        "key_points": [
            "The water cycle: evaporation, condensation, precipitation, repeat.",
            "Clouds are tiny water droplets or ice crystals.",
            "Thermometers measure temperature; barometers measure air pressure.",
        ],
        "requirements": list(REQUIREMENTS),
        "standards": list(STD_EARTH),
        "citations": list(CIT_EARTH),
    },
    # ---------------- COMPOUNDED ----------------
    {
        "key": "newtons-first-law",
        "name": "Forces, Friction, and Newton's First Law",
        "group": "Physics",
        "ladder_rank": 5, "ladder_tier": "compounded",
        "description": ("A compounded physics quiz on Newton's first law: "
                        "inertia, mass versus weight, balanced and "
                        "unbalanced forces. Tests why objects keep moving "
                        "or stay still until a force acts. Rank 5 on the "
                        "teaching ladder." + DESC_TAIL),
        "questions": [
            ("State Newton's first law of motion.",
             "An object at rest stays at rest, and an object in motion stays in motion, unless acted on by an unbalanced force."),
            ("What is inertia?",
             "The tendency of an object to resist changes in its motion."),
            ("What is the unit of force?",
             "The newton (N)."),
            ("Which has more inertia: a bowling ball or a tennis ball?",
             "The bowling ball (more mass means more inertia)."),
            ("What is mass?",
             "The amount of matter in an object."),
            ("What is weight?",
             "The force of gravity acting on an object's mass."),
            ("Would your mass change on the Moon?",
             "No."),
            ("Would your weight change on the Moon?",
             "Yes: it would be about one-sixth of your Earth weight."),
            ("What are balanced forces?",
             "Forces that cancel out, producing no change in motion."),
            ("What happens when unbalanced forces act on an object?",
             "The object's motion changes (it accelerates)."),
        ],
        "key_points": [
            "Newton's first law: motion continues unchanged unless an unbalanced force acts.",
            "Mass is constant; weight depends on gravity.",
            "Balanced forces cancel; unbalanced forces change motion.",
        ],
        "requirements": list(REQUIREMENTS),
        "standards": list(STD_PHYS),
        "citations": list(CIT_PHYS),
    },
    {
        "key": "chemical-reactions",
        "name": "Chemical Reactions: What Changes",
        "group": "Chemistry",
        "ladder_rank": 5, "ladder_tier": "compounded",
        "description": ("A compounded chemistry quiz on chemical reactions: "
                        "reactants, products, evidence of change, and the "
                        "conservation of mass. Tests telling chemical from "
                        "physical change. Rank 5 on the teaching ladder."
                        + DESC_TAIL),
        "questions": [
            ("What is a chemical reaction?",
             "A process where substances change into new substances."),
            ("What are the starting substances in a reaction called?",
             "Reactants."),
            ("What are the substances formed in a reaction called?",
             "Products."),
            ("Name three signs that a chemical reaction has occurred.",
             "Any three of: color change, gas bubbles, heat or light released, a solid (precipitate) forming."),
            ("What is a precipitate?",
             "A solid that forms in a liquid during a reaction."),
            ("What is the law of conservation of mass?",
             "Mass is neither created nor destroyed in a chemical reaction."),
            ("In a balanced equation, what is true about the atom counts?",
             "The number of each kind of atom is the same on both sides."),
            ("What is rust?",
             "Iron oxide, formed when iron reacts with oxygen and water."),
            ("Is burning wood a chemical or a physical change?",
             "Chemical."),
            ("Is melting ice a chemical or a physical change?",
             "Physical."),
        ],
        "key_points": [
            "Reactions turn reactants into products; atoms are rearranged, never created or destroyed.",
            "Color change, gas, heat, light, or precipitate signal a reaction.",
            "Burning is chemical; melting is physical.",
        ],
        "requirements": list(REQUIREMENTS),
        "standards": list(STD_CHEM),
        "citations": list(CIT_CHEM),
    },
    {
        "key": "cells-building-blocks",
        "name": "Cells: The Building Blocks of Life",
        "group": "Biology",
        "ladder_rank": 5, "ladder_tier": "compounded",
        "description": ("A compounded biology quiz on cells: organelles, "
                        "plant versus animal cells, and cell theory. Tests "
                        "the parts of the cell and what each does. Rank 5 "
                        "on the teaching ladder." + DESC_TAIL),
        "questions": [
            ("What is a cell?",
             "The basic unit of life."),
            ("Who first observed cells?",
             "Robert Hooke, in 1665, looking at cork."),
            ("What is the control center of the cell?",
             "The nucleus."),
            ("Which organelle makes energy for the cell?",
             "The mitochondria."),
            ("What is the jelly-like substance filling the cell?",
             "Cytoplasm."),
            ("What surrounds and protects the cell?",
             "The cell membrane."),
            ("Which structure do plant cells have that animal cells lack?",
             "A cell wall (and chloroplasts)."),
            ("What is the function of chloroplasts?",
             "Photosynthesis."),
            ("Are bacteria single-celled or multi-celled?",
             "Single-celled."),
            ("State the three parts of the cell theory.",
             "All living things are made of cells; cells are the basic unit of life; all cells come from existing cells."),
        ],
        "key_points": [
            "The cell is the basic unit of life; all living things are made of cells.",
            "The nucleus controls, mitochondria power, chloroplasts photosynthesize.",
            "Plant cells have walls and chloroplasts; animal cells do not.",
        ],
        "requirements": list(REQUIREMENTS),
        "standards": list(STD_BIO),
        "citations": list(CIT_BIO),
    },
    {
        "key": "moon-phases",
        "name": "The Moon and Its Phases",
        "group": "Astronomy",
        "ladder_rank": 5, "ladder_tier": "compounded",
        "description": ("A compounded astronomy quiz on the Moon: phases, "
                        "the lunar cycle, craters, and why the Moon shines. "
                        "Tests waxing and waning and the Moon's surface. "
                        "Rank 5 on the teaching ladder." + DESC_TAIL),
        "questions": [
            ("What causes the phases of the Moon?",
             "The changing angles of sunlight reflecting off the Moon as it orbits Earth."),
            ("How long is one lunar cycle?",
             "About 29.5 days."),
            ("What is a full moon?",
             "The phase when the Moon's entire lit face is visible from Earth."),
            ("What is a new moon?",
             "The phase when the Moon's lit side faces away from Earth."),
            ("What is a waxing moon?",
             "A moon growing toward full."),
            ("What is a waning moon?",
             "A moon shrinking toward new."),
            ("Does the Moon make its own light?",
             "No: it reflects sunlight."),
            ("What are the dark patches on the Moon called?",
             "Maria (singular: mare)."),
            ("What causes craters on the Moon?",
             "Impacts from asteroids and meteoroids."),
            ("Why does the Moon not have weather?",
             "It has almost no atmosphere."),
        ],
        "key_points": [
            "Moon phases come from viewing angles, not from Earth's shadow.",
            "The lunar cycle is about 29.5 days: waxing to full, waning to new.",
            "The Moon reflects sunlight; its craters come from impacts.",
        ],
        "requirements": list(REQUIREMENTS),
        "standards": list(STD_ASTRO),
        "citations": list(CIT_ASTRO),
    },
    {
        "key": "kinetic-potential-energy",
        "name": "Energy: Kinetic and Potential",
        "group": "Physics",
        "ladder_rank": 6, "ladder_tier": "compounded",
        "description": ("A compounded physics quiz on energy: kinetic and "
                        "potential energy, the joule, and the conservation "
                        "of energy. Tests tracing energy changes in swings, "
                        "springs, and bulbs. Rank 6 on the teaching ladder."
                        + DESC_TAIL),
        "questions": [
            ("What is energy?",
             "The ability to do work."),
            ("What is kinetic energy?",
             "Energy of motion."),
            ("What is potential energy?",
             "Stored energy (energy of position)."),
            ("What is gravitational potential energy?",
             "Energy stored in an object because of its height above the ground."),
            ("What is the unit of energy?",
             "The joule (J)."),
            ("State the law of conservation of energy.",
             "Energy cannot be created or destroyed, only transformed from one form to another."),
            ("What kind of energy does a stretched rubber band have?",
             "Elastic potential energy."),
            ("At the top of a swing's arc, which energy is greatest?",
             "Potential energy."),
            ("At the bottom of a swing's arc, which energy is greatest?",
             "Kinetic energy."),
            ("What device converts electrical energy into light?",
             "A light bulb (lamp)."),
        ],
        "key_points": [
            "Energy is the ability to do work; the joule is its unit.",
            "Kinetic energy moves; potential energy waits (height, stretch, position).",
            "Energy transforms but is never created or destroyed.",
        ],
        "requirements": list(REQUIREMENTS),
        "standards": list(STD_PHYS),
        "citations": list(CIT_PHYS),
    },
    {
        "key": "atoms-protons-neutrons-electrons",
        "name": "Atoms: Protons, Neutrons, Electrons",
        "group": "Chemistry",
        "ladder_rank": 6, "ladder_tier": "compounded",
        "description": ("A compounded chemistry quiz on atomic structure: "
                        "the three subatomic particles, the nucleus, and "
                        "what defines an element. Tests charges, locations, "
                        "and isotopes. Rank 6 on the teaching ladder."
                        + DESC_TAIL),
        "questions": [
            ("What are the three main subatomic particles?",
             "Protons, neutrons, and electrons."),
            ("Which particle has a positive charge?",
             "The proton."),
            ("Which particle has a negative charge?",
             "The electron."),
            ("Which particle has no charge?",
             "The neutron."),
            ("Where are protons and neutrons found?",
             "In the nucleus."),
            ("Where do electrons move?",
             "In shells (orbitals) around the nucleus."),
            ("What is an atom's mass number?",
             "Protons plus neutrons."),
            ("What are isotopes?",
             "Atoms of the same element with different numbers of neutrons."),
            ("What is the charge of a neutral atom?",
             "Zero: it has equal numbers of protons and electrons."),
            ("Which particle determines the element's identity?",
             "The proton (its count is the atomic number)."),
        ],
        "key_points": [
            "Protons are positive, neutrons neutral, electrons negative.",
            "The nucleus holds protons and neutrons; electrons orbit in shells.",
            "Atomic number (proton count) identifies the element.",
        ],
        "requirements": list(REQUIREMENTS),
        "standards": list(STD_CHEM),
        "citations": list(CIT_CHEM),
    },
    {
        "key": "photosynthesis-respiration",
        "name": "Photosynthesis and Respiration",
        "group": "Biology",
        "ladder_rank": 6, "ladder_tier": "compounded",
        "description": ("A compounded biology quiz on the two great energy "
                        "processes of life: photosynthesis and cellular "
                        "respiration. Tests the word equations, where each "
                        "happens, and how they mirror each other. Rank 6 on "
                        "the teaching ladder." + DESC_TAIL),
        "questions": [
            ("Write the word equation for photosynthesis.",
             "Carbon dioxide + water -> glucose + oxygen (using light energy)."),
            ("Write the word equation for cellular respiration.",
             "Glucose + oxygen -> carbon dioxide + water + energy."),
            ("Where does photosynthesis occur in the cell?",
             "In the chloroplasts."),
            ("Where does cellular respiration mainly occur?",
             "In the mitochondria."),
            ("What pigment captures light for photosynthesis?",
             "Chlorophyll."),
            ("Which process releases usable energy for the cell?",
             "Cellular respiration."),
            ("Which organisms perform photosynthesis?",
             "Plants, algae, and some bacteria."),
            ("Which organisms perform cellular respiration?",
             "Nearly all living organisms, plants and animals alike."),
            ("What enters the leaf through the stomata?",
             "Carbon dioxide."),
            ("Why are plants called producers?",
             "They produce food (glucose) that feeds the ecosystem."),
        ],
        "key_points": [
            "Photosynthesis stores light energy as glucose; respiration releases it.",
            "Chloroplasts photosynthesize; mitochondria respire.",
            "The two processes mirror each other in inputs and outputs.",
        ],
        "requirements": list(REQUIREMENTS),
        "standards": list(STD_BIO),
        "citations": list(CIT_BIO),
    },
    {
        "key": "electricity-circuits",
        "name": "Electricity: Circuits and Current",
        "group": "Physics",
        "ladder_rank": 7, "ladder_tier": "compounded",
        "description": ("A compounded physics quiz on electricity: current, "
                        "voltage, resistance, Ohm's law, and series versus "
                        "parallel circuits. Tests the units and the rules "
                        "that govern circuits. Rank 7 on the teaching "
                        "ladder." + DESC_TAIL),
        "questions": [
            ("What is electric current?",
             "The flow of electric charge."),
            ("What is the unit of current?",
             "The ampere (amp)."),
            ("What is voltage?",
             "The electric potential difference: the push that drives current."),
            ("What is the unit of voltage?",
             "The volt."),
            ("What is resistance?",
             "Opposition to the flow of current."),
            ("What is the unit of resistance?",
             "The ohm."),
            ("State Ohm's law.",
             "V = I x R: voltage equals current times resistance."),
            ("What is a series circuit?",
             "A circuit with one single path for the current."),
            ("What is a parallel circuit?",
             "A circuit with multiple paths for the current."),
            ("What happens in a series circuit if one bulb burns out?",
             "The circuit breaks and all the bulbs go out."),
        ],
        "key_points": [
            "Current (amps), voltage (volts), resistance (ohms): Ohm's law ties them together.",
            "Series circuits have one path; parallel circuits have many.",
            "Higher voltage or lower resistance means more current.",
        ],
        "requirements": list(REQUIREMENTS),
        "standards": list(STD_PHYS),
        "citations": list(CIT_PHYS),
    },
    {
        "key": "ionic-covalent-bonding",
        "name": "Bonding: Ionic and Covalent",
        "group": "Chemistry",
        "ladder_rank": 7, "ladder_tier": "compounded",
        "description": ("A compounded chemistry quiz on chemical bonds: "
                        "ionic versus covalent, molecules, compounds, and "
                        "valence electrons. Tests what holds atoms together "
                        "and why noble gases sit out. Rank 7 on the teaching "
                        "ladder." + DESC_TAIL),
        "questions": [
            ("What is a chemical bond?",
             "A force holding atoms together in a molecule or compound."),
            ("What is an ionic bond?",
             "A bond formed by the transfer of electrons, usually between a metal and a nonmetal."),
            ("What is a covalent bond?",
             "A bond formed by the sharing of electrons."),
            ("Which bond holds table salt (NaCl) together?",
             "Ionic."),
            ("Which bond holds water (H2O) together?",
             "Covalent."),
            ("What is a molecule?",
             "Two or more atoms bonded together."),
            ("What is a compound?",
             "A substance made of two or more different elements bonded together."),
            ("What are valence electrons?",
             "Electrons in the outermost shell, the ones involved in bonding."),
            ("How many valence electrons do noble gases typically have?",
             "Eight (a full outer shell; helium has two)."),
            ("Why do noble gases rarely form bonds?",
             "Their outer electron shells are already full."),
        ],
        "key_points": [
            "Ionic bonds transfer electrons; covalent bonds share them.",
            "Valence electrons control how atoms bond.",
            "Noble gases rarely bond because their outer shells are full.",
        ],
        "requirements": list(REQUIREMENTS),
        "standards": list(STD_CHEM),
        "citations": list(CIT_CHEM),
    },
    {
        "key": "plate-tectonics-earthquakes",
        "name": "Plate Tectonics and Earthquakes",
        "group": "Earth Science",
        "ladder_rank": 7, "ladder_tier": "compounded",
        "description": ("A compounded earth science quiz on plate tectonics: "
                        "plate boundaries, faults, earthquakes, and the "
                        "Ring of Fire. Tests what moves the crust and how "
                        "quakes are measured. Rank 7 on the teaching ladder."
                        + DESC_TAIL),
        "questions": [
            ("What is the theory of plate tectonics?",
             "Earth's crust is broken into plates that move over the mantle."),
            ("What are the three main plate boundaries?",
             "Divergent, convergent, and transform."),
            ("At which boundary do plates move apart?",
             "Divergent."),
            ("At which boundary do plates collide?",
             "Convergent."),
            ("What causes earthquakes?",
             "The sudden release of energy when rocks break along a fault."),
            ("What is the point underground where an earthquake starts?",
             "The focus (hypocenter)."),
            ("What is the point on the surface directly above the focus?",
             "The epicenter."),
            ("What instrument measures earthquake waves?",
             "A seismograph (seismometer)."),
            ("What scale measures earthquake magnitude?",
             "The moment magnitude scale (the Richter scale was its predecessor)."),
            ("What is the Ring of Fire?",
             "The zone of volcanoes and earthquakes ringing the Pacific Ocean."),
        ],
        "key_points": [
            "Plates move at divergent, convergent, and transform boundaries.",
            "Quakes start at the focus; the epicenter is the surface point above it.",
            "Seismographs record quakes; magnitude scales measure their size.",
        ],
        "requirements": list(REQUIREMENTS),
        "standards": list(STD_EARTH),
        "citations": list(CIT_EARTH),
    },
    # ---------------- ADVANCED ----------------
    {
        "key": "waves-sound-light",
        "name": "Waves: Sound and Light",
        "group": "Physics",
        "ladder_rank": 8, "ladder_tier": "advanced",
        "description": ("An advanced physics quiz on waves: wavelength, "
                        "frequency, amplitude, and the electromagnetic "
                        "spectrum. Tests wave math relationships and why "
                        "sound needs a medium. Rank 8 on the teaching "
                        "ladder." + DESC_TAIL),
        "questions": [
            ("What is a wave?",
             "A disturbance that transfers energy through a medium or through space."),
            ("What is wavelength?",
             "The distance between two consecutive wave crests."),
            ("What is frequency?",
             "The number of waves passing a point per second."),
            ("What is the unit of frequency?",
             "The hertz (Hz)."),
            ("What is the relationship between frequency and wavelength?",
             "They are inversely related: higher frequency means shorter wavelength."),
            ("What is amplitude?",
             "The maximum displacement from rest; it sets loudness and brightness."),
            ("Do sound waves need a medium to travel?",
             "Yes: sound cannot travel through a vacuum."),
            ("About what is the speed of sound in air?",
             "About 343 meters per second."),
            ("What is the electromagnetic spectrum?",
             "The range of all electromagnetic waves: radio, microwave, infrared, visible, ultraviolet, X-ray, gamma."),
            ("Which carries more energy: a gamma ray or a radio wave?",
             "A gamma ray (higher frequency means higher energy)."),
        ],
        "key_points": [
            "Waves carry energy: wavelength, frequency, and amplitude describe them.",
            "Frequency and wavelength are inversely related.",
            "Sound needs a medium; light does not.",
        ],
        "requirements": list(REQUIREMENTS),
        "standards": list(STD_PHYS),
        "citations": list(CIT_PHYS),
    },
    {
        "key": "dna-genes-heredity",
        "name": "DNA, Genes, and Heredity",
        "group": "Biology",
        "ladder_rank": 8, "ladder_tier": "advanced",
        "description": ("An advanced biology quiz on DNA: the double helix, "
                        "base pairing, genes, chromosomes, and heredity. "
                        "Tests the molecular basis of inheritance. Rank 8 "
                        "on the teaching ladder." + DESC_TAIL),
        "questions": [
            ("What does DNA stand for?",
             "Deoxyribonucleic acid."),
            ("What shape is the DNA molecule?",
             "A double helix."),
            ("What are the four bases of DNA?",
             "Adenine, thymine, cytosine, and guanine."),
            ("Which base pairs with adenine?",
             "Thymine."),
            ("Which base pairs with cytosine?",
             "Guanine."),
            ("What is a gene?",
             "A segment of DNA that codes for a protein (a trait)."),
            ("Where is DNA found in the cell?",
             "In the nucleus, packed into chromosomes."),
            ("How many chromosomes do humans have?",
             "46 (23 pairs)."),
            ("Who are credited with discovering the structure of DNA?",
             "James Watson and Francis Crick (1953), building on Rosalind Franklin's data."),
            ("What is heredity?",
             "The passing of traits from parents to offspring."),
        ],
        "key_points": [
            "DNA is a double helix; A pairs with T, C pairs with G.",
            "Genes are DNA segments; humans have 46 chromosomes.",
            "Heredity passes traits from parents to offspring.",
        ],
        "requirements": list(REQUIREMENTS),
        "standards": list(STD_BIO),
        "citations": list(CIT_BIO),
    },
    {
        "key": "stars-birth-life-death",
        "name": "Stars: How Stars Are Born, Live, and Die",
        "group": "Astronomy",
        "ladder_rank": 8, "ladder_tier": "advanced",
        "description": ("An advanced astronomy quiz on stars: what powers "
                        "them, how they are born, stellar colors, and how "
                        "they die. Tests fusion, nebulae, and stellar "
                        "remnants. Rank 8 on the teaching ladder."
                        + DESC_TAIL),
        "questions": [
            ("What are stars mostly made of?",
             "Hydrogen and helium gas."),
            ("What process powers stars?",
             "Nuclear fusion."),
            ("What is nuclear fusion?",
             "Light atomic nuclei combining into heavier nuclei, releasing energy."),
            ("What is a nebula?",
             "A cloud of gas and dust where stars are born."),
            ("What color are the hottest stars?",
             "Blue (or blue-white)."),
            ("What color are the coolest stars?",
             "Red."),
            ("What kind of star is our Sun?",
             "A main-sequence (G-type) star."),
            ("What is a white dwarf?",
             "The hot remnant core of a dead Sun-like star."),
            ("What is a black hole?",
             "A region where gravity is so strong that nothing, not even light, can escape."),
            ("What is a supernova?",
             "The explosive death of a massive star."),
        ],
        "key_points": [
            "Stars fuse hydrogen into helium, releasing light and heat.",
            "Star color tracks temperature: blue is hot, red is cool.",
            "Stars die as white dwarfs, neutron stars, or black holes.",
        ],
        "requirements": list(REQUIREMENTS),
        "standards": list(STD_ASTRO),
        "citations": list(CIT_ASTRO),
    },
    {
        "key": "gravity-orbits-kepler",
        "name": "Gravity, Orbits, and Kepler's Laws",
        "group": "Physics",
        "ladder_rank": 9, "ladder_tier": "advanced",
        "description": ("An advanced physics quiz on gravity and orbits: "
                        "universal gravitation, Kepler's three laws, and "
                        "why astronauts float. Tests the rules that govern "
                        "planets, moons, and satellites. Rank 9 on the "
                        "teaching ladder." + DESC_TAIL),
        "questions": [
            ("State Newton's law of universal gravitation in words.",
             "Every mass attracts every other mass; the force grows with the masses and shrinks with the square of the distance."),
            ("What is the acceleration due to gravity on Earth?",
             "About 9.8 meters per second squared."),
            ("What is an orbit?",
             "The curved path of one object around another, held by gravity."),
            ("What shape are planetary orbits?",
             "Ellipses (Kepler's first law)."),
            ("What does Kepler's second law say?",
             "A planet sweeps out equal areas in equal times: it moves faster near the Sun."),
            ("What does Kepler's third law relate?",
             "Orbital period and distance: farther planets take longer to orbit."),
            ("Why do astronauts float in orbit?",
             "They are in free fall around Earth (microgravity)."),
            ("What is escape velocity?",
             "The speed needed to break free of a body's gravity."),
            ("Which planet has the strongest surface gravity?",
             "Jupiter."),
            ("What keeps the Moon orbiting Earth?",
             "Earth's gravity, balancing the Moon's forward motion."),
        ],
        "key_points": [
            "Gravity grows with mass and shrinks with the square of distance.",
            "Kepler's laws: elliptical orbits, equal areas, period-distance relation.",
            "Orbit is continuous free fall around a body.",
        ],
        "requirements": list(REQUIREMENTS),
        "standards": list(STD_PHYS),
        "citations": list(CIT_PHYS),
    },
    {
        "key": "stoichiometry-counting-atoms",
        "name": "Stoichiometry: Counting Atoms",
        "group": "Chemistry",
        "ladder_rank": 9, "ladder_tier": "advanced",
        "description": ("An advanced chemistry quiz on stoichiometry: the "
                        "mole, Avogadro's number, molar mass, limiting "
                        "reactants, and percent yield. Tests real "
                        "mole-quantity calculations. Rank 9 on the teaching "
                        "ladder." + DESC_TAIL),
        "questions": [
            ("What is a mole?",
             "The amount of substance containing Avogadro's number of particles."),
            ("What is Avogadro's number?",
             "About 6.022 x 10^23."),
            ("What is molar mass?",
             "The mass of one mole of a substance, in grams per mole."),
            ("What is the molar mass of water (H2O)?",
             "About 18 grams per mole."),
            ("How many moles are in 36 grams of water?",
             "2 moles."),
            ("What is a limiting reactant?",
             "The reactant that runs out first, limiting how much product forms."),
            ("What is percent yield?",
             "(Actual yield divided by theoretical yield) times 100 percent."),
            ("In 2H2 + O2 -> 2H2O, how many moles of water form from 2 moles of O2?",
             "4 moles."),
            ("What is conserved in every balanced equation?",
             "Atoms (mass)."),
            ("What does STP stand for?",
             "Standard temperature and pressure."),
        ],
        "key_points": [
            "The mole (6.022 x 10^23 particles) lets chemists count atoms by weighing.",
            "Molar mass converts grams to moles and back.",
            "The limiting reactant caps the yield; percent yield compares actual to theory.",
        ],
        "requirements": list(REQUIREMENTS),
        "standards": list(STD_CHEM),
        "citations": list(CIT_CHEM),
    },
    {
        "key": "climate-systems-greenhouse",
        "name": "Climate Systems and the Greenhouse Effect",
        "group": "Earth Science",
        "ladder_rank": 9, "ladder_tier": "advanced",
        "description": ("An advanced earth science quiz on climate: the "
                        "greenhouse effect, greenhouse gases, weather "
                        "versus climate, albedo, and the carbon cycle. Tests "
                        "the machinery of Earth's climate system. Rank 9 on "
                        "the teaching ladder." + DESC_TAIL),
        "questions": [
            ("What is the greenhouse effect?",
             "Gases in the atmosphere trap heat radiated from Earth's surface, warming the planet."),
            ("Name three greenhouse gases.",
             "Carbon dioxide, methane, and water vapor."),
            ("What is the difference between weather and climate?",
             "Weather is short-term conditions; climate is the long-term pattern."),
            ("What is the main driver of Earth's climate system?",
             "Energy from the Sun."),
            ("What is an El Nino event?",
             "Warming of Pacific Ocean surface waters that shifts global weather patterns."),
            ("What is the cryosphere?",
             "The frozen parts of Earth: ice caps, glaciers, and permafrost."),
            ("What does a rising sea level indicate?",
             "Warming: thermal expansion of water plus melting ice."),
            ("What is albedo?",
             "The fraction of sunlight a surface reflects."),
            ("Which surface has higher albedo: fresh snow or dark ocean?",
             "Fresh snow."),
            ("What is the carbon cycle?",
             "The movement of carbon between the atmosphere, oceans, land, and living things."),
        ],
        "key_points": [
            "Greenhouse gases trap heat; the Sun drives the whole system.",
            "Weather is short-term; climate is the long-term pattern.",
            "Albedo, the cryosphere, and the carbon cycle are key climate gears.",
        ],
        "requirements": list(REQUIREMENTS),
        "standards": list(STD_EARTH),
        "citations": list(CIT_EARTH),
    },
    {
        "key": "relativity-time-space",
        "name": "Relativity: Time and Space Basics",
        "group": "Physics",
        "ladder_rank": 10, "ladder_tier": "advanced",
        "description": ("An advanced physics quiz on Einstein's relativity: "
                        "the constant speed of light, time dilation, "
                        "mass-energy equivalence, and curved spacetime. "
                        "Tests the big ideas that replaced Newton's "
                        "absolute time. Rank 10 on the teaching ladder."
                        + DESC_TAIL),
        "questions": [
            ("Who developed the theory of relativity?",
             "Albert Einstein."),
            ("In what year was special relativity published?",
             "1905."),
            ("What does special relativity say about the speed of light?",
             "It is constant for all observers."),
            ("What is time dilation?",
             "Moving clocks run slower as seen by a stationary observer."),
            ("What is E = mc^2?",
             "Mass-energy equivalence: energy equals mass times the speed of light squared."),
            ("What is length contraction?",
             "Moving objects appear shorter in the direction of motion."),
            ("What is spacetime?",
             "The four-dimensional union of space and time."),
            ("What does general relativity describe gravity as?",
             "The curvature of spacetime by mass and energy."),
            ("What confirmed general relativity in 1919?",
             "Starlight bending around the Sun during a solar eclipse."),
            ("Can anything travel faster than light in a vacuum?",
             "No: the speed of light is the cosmic speed limit."),
        ],
        "key_points": [
            "The speed of light is constant for all observers.",
            "E = mc^2: mass and energy are equivalent.",
            "Gravity is the curvature of spacetime.",
        ],
        "requirements": list(REQUIREMENTS),
        "standards": list(STD_PHYS),
        "citations": list(CIT_PHYS),
    },
    {
        "key": "cosmology-big-bang",
        "name": "Cosmology: The Big Bang and Beyond",
        "group": "Astronomy",
        "ladder_rank": 10, "ladder_tier": "advanced",
        "description": ("An advanced astronomy quiz on cosmology: the Big "
                        "Bang, the age of the universe, dark matter and "
                        "dark energy, and Hubble's law. Tests the evidence "
                        "for an expanding universe. Rank 10 on the teaching "
                        "ladder." + DESC_TAIL),
        "questions": [
            ("What is the Big Bang theory?",
             "The universe began in a hot, dense state and has been expanding ever since."),
            ("About how old is the universe?",
             "About 13.8 billion years."),
            ("What evidence supports the Big Bang?",
             "The cosmic microwave background and the expansion of galaxies (Hubble's law)."),
            ("What is the cosmic microwave background?",
             "The faint afterglow radiation left over from the Big Bang."),
            ("What is dark matter?",
             "Invisible matter detected by its gravity, making up about 27 percent of the universe."),
            ("What is dark energy?",
             "The unknown force accelerating the universe's expansion."),
            ("What is a galaxy?",
             "A huge system of stars, gas, and dust bound together by gravity."),
            ("What galaxy do we live in?",
             "The Milky Way."),
            ("What is Hubble's law?",
             "Distant galaxies recede faster the farther away they are."),
            ("What is the observable universe?",
             "The region of the universe we can see, limited by the speed of light and the age of the cosmos."),
        ],
        "key_points": [
            "The universe is about 13.8 billion years old and still expanding.",
            "The cosmic microwave background is the Big Bang's afterglow.",
            "Dark matter and dark energy dominate the cosmic budget.",
        ],
        "requirements": list(REQUIREMENTS),
        "standards": list(STD_ASTRO),
        "citations": list(CIT_ASTRO),
    },
]

