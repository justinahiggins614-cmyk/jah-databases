#!/usr/bin/env python3
"""Entries for The Force and Motion Basics Database (fundamentals order #9).

Roster-verified 2026-10-17: slugs force-motion-basics /
force-motion-basics-signature free in the manifest (2,386 databases);
ID prefixes JAH-FMOB- / JAH-FMOBS- verified free in the manifest
id_prefix values and in all 809 shard index files (zero hits); all 68
titles (34 public + 34 " (Signature Edition)") passed through
code/dedupe_gate.py against the whole system with zero refusals.

Two NEW databases, 34 ladder-ordered records each:

  force-motion-basics            - The Force and Motion Basics Database
                                   (public-harvest: real, fact-checked
                                   first-principles physics - push and pull,
                                   gravity, friction, speed and direction,
                                   and the simple machines: lever, wheel and
                                   axle, pulley, inclined plane, wedge, and
                                   screw; standard references Halliday
                                   Resnick Walker Fundamentals of Physics
                                   12th ed 2022; Serway and Jewett Physics
                                   for Scientists and Engineers 10th ed 2019;
                                   Young and Freedman University Physics
                                   15th ed 2020; Hewitt Conceptual Physics
                                   13th ed 2021; the SI Brochure 9th ed;
                                   ISO 80000-3 and ISO 80000-4; and the
                                   other landmarks cited per record)
  force-motion-basics-signature  - The Force and Motion Basics Signature
                                   Database
                                   (his original Signature Motion Method:
                                   every push a promise, every pull an
                                   agreement, gravity the Signature anchor,
                                   friction the Signature grip, and the
                                   simple machines the Signature leverage;
                                   src signature, titles suffixed
                                   " (Signature Edition)", never presented
                                   as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_force_motion_basics.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

Never the words "bat belt" anywhere. No website references. No Facebook.
No religious talk. Nothing on neutralizing or defeating military or
defense-grade systems.
"""

SIG_TAIL = ("Signature original - his original Signature Motion Method: "
            "every push a promise, every pull an agreement, gravity the "
            "Signature anchor, friction the Signature grip, and the simple "
            "machines the Signature leverage. Clearly labeled "
            "Signature-made, never presented as authentic public record.")

CIT_HALLIDAY = ("Halliday D, Resnick R, Walker J. Fundamentals of Physics. "
                "12th ed. Wiley; 2022.")
CIT_SERWAY = ("Serway RA, Jewett JW. Physics for Scientists and Engineers. "
              "10th ed. Cengage; 2019.")
CIT_YOUNG = ("Young HD, Freedman RA. University Physics with Modern Physics. "
             "15th ed. Pearson; 2020.")
CIT_HEWITT = ("Hewitt PG. Conceptual Physics. 13th ed. Pearson; 2021.")
CIT_KNIGHT = ("Knight RD. Physics for Scientists and Engineers: A Strategic "
              "Approach. 5th ed. Pearson; 2022.")
CIT_CUTNELL = ("Cutnell JD, Johnson KW. Physics. 12th ed. Wiley; 2021.")
CIT_GIANCOLI = ("Giancoli DC. Physics: Principles with Applications. 8th ed. "
                "Pearson; 2020.")
CIT_FEYNMAN = ("Feynman RP, Leighton RB, Sands M. The Feynman Lectures on "
               "Physics. Vol. I. California Institute of Technology; 1963.")
CIT_BIPM = ("Bureau International des Poids et Mesures. The International "
            "System of Units (SI). 9th ed.; 2019.")
CIT_NIST811 = ("Thompson A, Taylor BN. NIST Special Publication 811: Guide "
               "for the Use of the International System of Units; 2008.")
CIT_ISO3 = ("ISO 80000-3:2019. Quantities and units - Part 3: Space and time.")
CIT_ISO4 = ("ISO 80000-4:2019. Quantities and units - Part 4: Mechanics.")
CIT_TIPLER = ("Tipler PA, Mosca G. Physics for Scientists and Engineers. "
              "6th ed. Freeman; 2008.")

ENTRIES = [
    {
        "key": "what_is_force",
        "name": "What Is a Force",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "A force is a push or a pull acting on an object, and it is the "
            "reason anything ever starts moving, stops moving, speeds up, "
            "slows down, or changes direction. Forces are measured in "
            "newtons and always have two qualities: a size (how strong the "
            "push or pull is) and a direction (which way it points). "
            "Everything you have ever seen move - a rolling ball, a falling "
            "apple, a car turning a corner, a rocket climbing - moved "
            "because forces acted on it, and everything sitting still is "
            "either feeling no force or feeling forces that cancel each "
            "other out. Forces come in two great families. Contact forces "
            "need touch: the push of a hand, the pull of a rope, the grip "
            "of friction, the springiness of a compressed spring. Field "
            "forces act across empty space: gravity pulls every mass toward "
            "every other mass, magnets pull and push without touching, and "
            "static electricity can lift hair off a scalp from a distance. "
            "A force never acts alone on a motion story: objects respond to "
            "the combination of all forces on them at once, and learning to "
            "track every force is the first skill of physics."
        ),
        "how_it_works": (
            "A force changes motion by accelerating mass: the same push "
            "moves a light object easily and a heavy object sluggishly, "
            "which is why force, mass, and acceleration are bound together "
            "in every calculation this database makes. To work with a "
            "force you name its size in newtons, draw it as an arrow "
            "pointing the way it acts, and add it together with every other "
            "arrow on the object. If the arrows cancel, motion does not "
            "change; if they do not cancel, the leftover arrow - the net "
            "force - decides exactly how the motion changes. Contact forces "
            "switch on only while surfaces touch: let go of the rope and "
            "the tension vanishes instantly. Field forces never switch off: "
            "gravity pulls on a thrown ball through its whole flight, which "
            "is why the ball arcs and falls. Because force has direction, "
            "two equal forces pulling opposite ways erase each other, while "
            "two equal forces pulling the same way double up - direction is "
            "half the physics."
        ),
        "key_points": [
            "A force is a push or a pull with both a size in newtons and a direction; size alone is never the whole story.",
            "Contact forces require touch (push, pull, friction, tension, spring force) while field forces act at a distance (gravity, magnetism, static electricity).",
            "Objects respond to the combination of all forces at once, never to one force in isolation.",
            "Equal opposing forces cancel; the leftover net force is what actually changes motion.",
            "Forces are the reason for every change in motion: starting, stopping, speeding, slowing, and turning.",
        ],
        "requirements": [
            "State every force with a size in newtons and a direction - an arrow drawn to scale is the honest statement.",
            "Classify each force as contact or field so none of the field forces get forgotten while counting.",
            "List ALL forces on the object before concluding anything about its motion.",
            "Keep mass separate from force: mass resists the change, force causes it.",
            "Check units at every step: newtons for force, kilograms for mass, meters per second squared for acceleration.",
        ],
        "standards": [
            "Force is stated in newtons (N), the SI unit: one newton accelerates one kilogram at one meter per second squared (SI Brochure, 9th ed.).",
            "Quantities and units for mechanics follow ISO 80000-4:2019 conventions for symbols and definitions.",
            "Instructional framing follows Hewitt, Conceptual Physics, 13th ed., and Halliday, Resnick and Walker, Fundamentals of Physics, 12th ed.",
        ],
        "citations": [CIT_HEWITT, CIT_HALLIDAY, CIT_BIPM],
        "sig_lens": (
            "The Signature read: a force is a promise with direction - the "
            "push promises motion one way, the pull promises it the other, "
            "and the Signature keeps every promise it makes. Where public "
            "physics files forces as arrows, the Signature Motion Method "
            "files them as agreements between the mover and the moved, "
            "signed in newtons."
        ),
    },
    {
        "key": "push_pull",
        "name": "Push and Pull: The Two Faces of Force",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Push and pull are the two faces of every force: a push drives "
            "an object away from the source of the force, and a pull draws "
            "it toward the source. The distinction matters because the "
            "source tells you which way the force points - you cannot draw "
            "the arrow correctly until you know whether the agent is "
            "shoving the object away or dragging it closer. A hand shoving "
            "a box across the floor is a push; a rope dragging a sled is a "
            "pull; a magnet can do either depending on which pole faces the "
            "object. In a tug-of-war both teams pull the same rope in "
            "opposite directions, and the rope - and the flag at its center "
            "- moves toward the stronger pull, which is the same rule that "
            "governs every contest of forces: add them as arrows, and the "
            "sum decides the winner. Pushes and pulls also pair up: when "
            "you push on a wall, the wall pushes back on you with an equal "
            "force, which is the first hint of the action-reaction pairing "
            "that Newton made into his third law."
        ),
        "how_it_works": (
            "To analyze any push or pull, locate the agent (the hand, the "
            "rope, the engine) and the object, then draw the force arrow on "
            "the object pointing away from a pushing agent and toward a "
            "pulling agent. When two agents contest one object - two teams "
            "on a rope, a horse pulling a cart while friction holds back - "
            "place the arrows tail-to-tail and add them: arrows in the same "
            "direction add, arrows in opposite directions subtract, and the "
            "sign of the result names the winning direction. The rope in a "
            "tug-of-war carries tension equal to the smaller pull when one "
            "side is winning, because the rope can only transmit what the "
            "weaker side can hold. Muscles, engines, springs, stretched "
            "rubber bands, and compressed air all produce pushes and pulls "
            "the same way: stored effort released along one line, with the "
            "line itself - the rope, the rod, the contact - defining the "
            "direction."
        ),
        "key_points": [
            "A push points away from its source; a pull points toward its source - the agent locates the arrow.",
            "Opposing pushes and pulls subtract; the sign of the net force names the winning direction.",
            "A rope transmits tension along its own line, limited by what the weaker side can hold.",
            "Every push or pull implies an equal opposite push or pull back on the agent - the seed of action and reaction.",
            "Engines, muscles, springs, and stretched bands are all push/pull machines: stored effort released along a line.",
        ],
        "requirements": [
            "Identify the agent and the object for every push and pull before drawing any arrow.",
            "Draw the arrow on the object, not the agent - forces belong to the thing being acted on.",
            "Resolve contests by signed addition along the line of action; the net sign decides the motion.",
            "Name the transmission path (rope, rod, contact surface) because the path sets the direction.",
            "Never leave the reaction force off the books: it acts on the agent, equal and opposite.",
        ],
        "standards": [
            "Tension is treated as a single magnitude acting along the rope or cable, pulling away from each attached body (Serway and Jewett, 10th ed.).",
            "Contact push/pull forces follow the normal-force and tension conventions of Halliday, Resnick and Walker, 12th ed.",
            "Direction is stated with an explicit coordinate or compass reference, per ISO 80000-3:2019.",
        ],
        "citations": [CIT_SERWAY, CIT_HALLIDAY, CIT_ISO3],
        "sig_lens": (
            "The Signature read: the push is the Signature promise sent "
            "outward and the pull is the promise called home - two faces of "
            "one agreement between mover and moved. In the Signature Motion "
            "Method no push is ever lonely: every shove signs its return "
            "receipt on the shover, which is why the Method counts "
            "reactions as carefully as actions."
        ),
    },
    {
        "key": "position_distance",
        "name": "Position, Distance, and Displacement",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Position tells where an object is, distance tells how far it "
            "traveled, and displacement tells how far it ended up from "
            "where it started - and distance and displacement are not the "
            "same thing. Position is measured from a chosen origin: a "
            "runner at the 40-meter mark of a track has position 40 meters, "
            "and the origin is the agreement everyone shares before "
            "measuring starts. Distance is the total path length - every "
            "step counts, including backtracking - so a runner who sprints "
            "40 meters out and 30 meters back has covered 70 meters of "
            "distance. Displacement is the straight-line change from start "
            "to finish, with direction attached: the same runner ends 10 "
            "meters from the start in the outward direction, so the "
            "displacement is 10 meters outward. Distance is always "
            "positive and grows with every step; displacement can be zero "
            "(a round trip), positive, or negative depending on the chosen "
            "direction, and it is displacement - not distance - that pairs "
            "with velocity later."
        ),
        "how_it_works": (
            "Pick an origin and a positive direction, then every location "
            "becomes a signed number: positions to one side are positive, "
            "to the other side negative. Distance accumulates as the sum of "
            "the absolute values of each leg of the trip - no leg ever "
            "cancels another, because distance has no direction to cancel "
            "with. Displacement is simply final position minus initial "
            "position, one subtraction that erases all the back-and-forth: "
            "only the endpoints matter. On a track, a runner going from the "
            "0 mark to the 40 mark and back to the 10 mark covers 40 plus "
            "30 equals 70 meters of distance, but the displacement is 10 "
            "minus 0 equals 10 meters. In two dimensions the same idea uses "
            "arrows: displacement is the straight arrow from start to "
            "finish, and its length comes from the Pythagorean theorem "
            "while distance remains the sum of every leg."
        ),
        "key_points": [
            "Position is a location measured from an agreed origin; distance is total path length; displacement is the straight change from start to finish.",
            "Distance never cancels and never goes negative; displacement can be zero or negative because direction counts.",
            "A round trip always has zero displacement no matter how large the distance.",
            "Displacement is final position minus initial position - only the endpoints matter.",
            "Displacement, not distance, is the quantity that pairs with velocity and acceleration.",
        ],
        "requirements": [
            "Fix an origin and a positive direction before recording any position.",
            "Accumulate distance as the sum of absolute leg lengths - never let legs cancel.",
            "Compute displacement as final minus initial, keeping the sign.",
            "State displacement with its direction; state distance as a plain positive number.",
            "In two dimensions, use the straight start-to-finish arrow for displacement and the Pythagorean theorem for its length.",
        ],
        "standards": [
            "Length and position quantities follow ISO 80000-3:2019; the meter is the SI base unit (SI Brochure, 9th ed.).",
            "Displacement is defined as the vector difference of position vectors, per Young and Freedman, 15th ed.",
            "Sign conventions are stated explicitly with the coordinate choice, per Knight, 5th ed.",
        ],
        "citations": [CIT_ISO3, CIT_YOUNG, CIT_KNIGHT],
        "sig_lens": (
            "The Signature read: position is where the Signature stands, "
            "distance is every step the Signature took to get there, and "
            "displacement is the honest answer to how far it really moved. "
            "The Method honors the honest answer - the straight line from "
            "start to finish - because backtracking is effort, not "
            "progress."
        ),
    },
    {
        "key": "speed",
        "name": "Speed: Measuring How Fast",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Speed is distance divided by time: how much ground gets covered "
            "per second, per hour, per whatever clock you are using. A car "
            "covering 150 meters in 25 seconds moves at 6 meters per "
            "second, and that single number answers the only question speed "
            "asks - how fast - without caring which way the car pointed. "
            "Speed is a scalar, which means it has size but no direction: "
            "60 kilometers per hour tells you the pace, not the road. "
            "Average speed over a whole trip is total distance over total "
            "time, and it can hide a multitude of sins - a driver who "
            "speeds then crawls can still average the limit. Instantaneous "
            "speed is what the speedometer shows right now, the average "
            "over a vanishingly short moment. Common units are meters per "
            "second in science, kilometers per hour on roads, and miles per "
            "hour in some countries, and converting between them is just "
            "multiplying by the right chain of unit fractions."
        ),
        "how_it_works": (
            "Measure a distance and the time it took, then divide: speed "
            "equals distance over time. For unit conversion, multiply by "
            "fractions equal to one - 1000 meters per kilometer, 3600 "
            "seconds per hour - so that unwanted units cancel and only the "
            "wanted ones survive. Meters per second become kilometers per "
            "hour by multiplying by 3.6, because each meter per second is "
            "3.6 kilometers per hour. Average speed uses the whole trip: a "
            "100-kilometer drive taking 2 hours averages 50 kilometers per "
            "hour even if the car stopped for lunch halfway. Instantaneous "
            "speed is the limit of that division as the time interval "
            "shrinks toward zero - the speedometer reading, the radar gun "
            "number. Because speed ignores direction, a car circling a "
            "track at steady speed has constant speed while its velocity - "
            "which includes direction - keeps changing."
        ),
        "key_points": [
            "Speed is distance over time: a scalar with size but no direction.",
            "Average speed is total distance over total time and can hide varying pace; instantaneous speed is the now-reading.",
            "Convert units with multiply-by-one fractions: meters per second times 3.6 gives kilometers per hour.",
            "Constant speed does not mean constant velocity - direction can change while speed holds steady.",
            "Every speed statement needs its unit; a bare number is not a measurement.",
        ],
        "requirements": [
            "Divide a measured distance by its measured time; never estimate one of them.",
            "Distinguish average speed (whole trip) from instantaneous speed (this moment).",
            "Carry units through the division and convert with explicit multiply-by-one chains.",
            "State the unit with every speed value: m/s, km/h, or mph.",
            "Remember that speed alone cannot describe motion fully - direction is a separate record.",
        ],
        "standards": [
            "Speed is the magnitude of the velocity vector, with SI unit meter per second (SI Brochure, 9th ed.).",
            "Unit conversions follow the NIST SP 811 guidance on exact conversion factors.",
            "Average versus instantaneous speed follows the limit definition in Halliday, Resnick and Walker, 12th ed.",
        ],
        "citations": [CIT_BIPM, CIT_NIST811, CIT_HALLIDAY],
        "sig_lens": (
            "The Signature read: speed is the Signature pace - how fast "
            "the promise travels, measured honestly against the clock. The "
            "Method distrusts the average that hides the speeding and the "
            "crawling alike, and trusts the speedometer of the moment, "
            "because a promise kept late is a promise bent."
        ),
    },
    {
        "key": "direction",
        "name": "Direction: Giving Motion an Address",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Direction is the address of motion: it tells which way the "
            "movement points, and without it a speed is a rumor rather than "
            "a report. Humans give direction many ways - compass points "
            "(north, southeast), clock faces, left and right, up and down, "
            "plus and minus along a line, or angles measured from a "
            "reference. In physics the cleanest address is the coordinate "
            "system: pick an x-axis and a y-axis, and any direction becomes "
            "an arrow with components, or a single angle measured from the "
            "axis. A displacement of 30 meters east and 40 meters north is "
            "a 50-meter arrow pointing at about 53 degrees north of east - "
            "the 3-4-5 triangle hiding inside every map. Direction is what "
            "turns distance into displacement and speed into velocity, and "
            "it is the reason forces, velocities, and accelerations must be "
            "added as arrows rather than as plain numbers."
        ),
        "how_it_works": (
            "Fix a reference - east as the x-axis, north as the y-axis, or "
            "any agreed pair - then describe each motion as components "
            "along those axes or as a length plus an angle. Components add "
            "simply: total east-west motion is the sum of all east-west "
            "parts, and total north-south motion is the sum of all "
            "north-south parts. The length of the resulting arrow comes "
            "from the Pythagorean theorem, and its angle from the inverse "
            "tangent of north over east (with care for which quadrant the "
            "arrow lands in). A 30-east, 40-north displacement has length "
            "the square root of 900 plus 1600, which is 50 meters, at an "
            "angle whose tangent is 40 over 30 - about 53.1 degrees north "
            "of east. Compass bearings, map grids, and the plus/minus of a "
            "number line are all the same idea wearing different clothes: "
            "an agreed reference plus a measured turn from it."
        ),
        "key_points": [
            "Direction is the address of motion; speed plus direction is the full report.",
            "Any direction can be stated as components on agreed axes or as a length plus an angle.",
            "Components along each axis add independently - east-west parts never mix with north-south parts.",
            "Arrow length comes from the Pythagorean theorem; angle comes from the inverse tangent with quadrant care.",
            "Compass points, bearings, clock faces, and signed number lines are all direction-address systems.",
        ],
        "requirements": [
            "Declare the reference axes or compass convention before stating any direction.",
            "Break every arrow into components before adding; never add lengths at different angles directly.",
            "Use the Pythagorean theorem for the resultant length and inverse tangent for its angle.",
            "Check the quadrant: inverse tangent alone cannot tell northeast from southwest.",
            "Keep direction attached to every vector quantity - force, displacement, velocity, acceleration.",
        ],
        "standards": [
            "Plane-angle measurement follows ISO 80000-3:2019; bearings are stated with their reference convention.",
            "Vector component conventions follow Young and Freedman, 15th ed.",
            "Coordinate-system declarations precede vector statements, per Knight, 5th ed.",
        ],
        "citations": [CIT_ISO3, CIT_YOUNG, CIT_KNIGHT],
        "sig_lens": (
            "The Signature read: direction is the Signature address - the "
            "promise is not kept until it arrives at the right door. The "
            "Method writes every address twice, once in components and "
            "once in angle, because a promise with only a distance is a "
            "letter with no street."
        ),
    },
    {
        "key": "velocity",
        "name": "Velocity: Speed with Direction",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Velocity is speed with direction attached: 6 meters per second "
            "east is a velocity, while 6 meters per second alone is only a "
            "speed. Because direction counts, velocity is a vector - an "
            "arrow with length and heading - and changing the heading "
            "changes the velocity even if the speed never wavers. A car "
            "rounding a curve at a steady 20 meters per second has constant "
            "speed but changing velocity, because its arrow keeps swinging "
            "around to follow the road. Average velocity is displacement "
            "over time, not distance over time: the round-trip runner whose "
            "displacement is zero has zero average velocity no matter how "
            "fast the legs moved. Instantaneous velocity is the velocity at "
            "one instant - the speedometer reading plus the compass "
            "heading. Velocity is the quantity that Newton laws actually "
            "govern: forces change velocity, and everything interesting in "
            "motion is a story about velocity changing."
        ),
        "how_it_works": (
            "Compute average velocity as displacement divided by time, "
            "keeping the direction of the displacement: 10 meters east in "
            "5 seconds is 2 meters per second east. In components, track "
            "each axis separately - the x-velocity is the east-west rate, "
            "the y-velocity the north-south rate - and the full velocity "
            "arrow is rebuilt from the pair. A change in velocity is found "
            "by subtracting arrows: final velocity minus initial velocity, "
            "done component by component. If a car goes from 2 meters per "
            "second east to 2 meters per second east plus 3 meters per "
            "second north, the change is 3 meters per second north - the "
            "eastward part cancels because it never changed. Divide that "
            "change by the time it took and you have the average "
            "acceleration, which is why velocity is the bridge between the "
            "kinematics of motion and the dynamics of forces."
        ),
        "key_points": [
            "Velocity is the vector partner of speed: same size, plus a direction that matters.",
            "Changing direction changes velocity even at constant speed - the curve is the proof.",
            "Average velocity is displacement over time; a zero-displacement trip has zero average velocity.",
            "Velocity changes are found by subtracting arrows component by component.",
            "Forces act on velocity, not on speed: Newton laws are written in velocity.",
        ],
        "requirements": [
            "Always attach direction to a velocity value; a bare number is a speed, not a velocity.",
            "Use displacement, not distance, when computing average velocity.",
            "Subtract velocities as vectors: final minus initial, component by component.",
            "Distinguish the instantaneous velocity (now) from the average (over the interval).",
            "Read turning as a velocity change even when the speedometer holds steady.",
        ],
        "standards": [
            "Velocity is defined as the time derivative of the position vector, per ISO 80000-3:2019.",
            "Vector subtraction conventions follow Halliday, Resnick and Walker, 12th ed.",
            "Component-wise treatment follows Serway and Jewett, 10th ed.",
        ],
        "citations": [CIT_ISO3, CIT_HALLIDAY, CIT_SERWAY],
        "sig_lens": (
            "The Signature read: velocity is the Signature in motion - "
            "pace with purpose, speed that knows where it is going. The "
            "Method measures the turning car as carefully as the speeding "
            "one, because a promise that arrives at the wrong door at "
            "exactly the right speed is still a broken promise."
        ),
    },
    {
        "key": "acceleration",
        "name": "Acceleration: Changing Velocity",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Acceleration is the rate at which velocity changes: speeding "
            "up, slowing down, or turning all count, because velocity "
            "includes direction. A car going from 5 to 20 meters per second "
            "in 3 seconds accelerates at 5 meters per second squared - "
            "each second, the velocity grows by 5 meters per second. "
            "Slowing down is acceleration too, pointing opposite the "
            "motion: brakes apply a backward acceleration that shrinks the "
            "forward velocity. Turning at constant speed is acceleration "
            "as well, since the velocity arrow swings - passengers feel it "
            "as the sideways push in a curve. The unit, meters per second "
            "squared, reads literally: meters per second of velocity gained "
            "(or lost) per second of time. Acceleration is the quantity "
            "that forces produce directly: push harder and the acceleration "
            "grows in exact proportion, which is the heart of Newton "
            "second law."
        ),
        "how_it_works": (
            "Average acceleration is the change in velocity divided by the "
            "time it took: final velocity minus initial velocity, over "
            "elapsed time, done as vector subtraction when direction "
            "changes. With constant acceleration, the motion equations give "
            "everything: velocity grows linearly (final equals initial plus "
            "acceleration times time) while distance grows with the square "
            "of time (distance equals initial velocity times time plus one "
            "half acceleration times time squared). A car accelerating "
            "from 5 meters per second at 5 meters per second squared for 3 "
            "seconds reaches 20 meters per second and covers 5 times 3 plus "
            "half of 5 times 9 - 15 plus 22.5, or 37.5 meters. For a turn "
            "at constant speed, the acceleration points toward the center "
            "of the curve with size speed squared over radius - the "
            "centripetal acceleration that the road friction or the "
            "banking must supply."
        ),
        "key_points": [
            "Acceleration is any change in velocity: faster, slower, or turning - all three count.",
            "Average acceleration is velocity change over time; the unit reads as velocity gained per second.",
            "Constant acceleration gives linear velocity growth and quadratic distance growth.",
            "Turning at steady speed is centripetal acceleration toward the curve center, size v squared over r.",
            "Forces produce acceleration directly - acceleration is the bridge from forces to motion.",
        ],
        "requirements": [
            "Compute acceleration from the velocity change, not the speed change alone - include direction.",
            "Use vector subtraction for the velocity change when the heading turns.",
            "Apply the constant-acceleration equations only when acceleration truly stays constant.",
            "Keep the unit honest: meters per second squared, never meters per second.",
            "Point centripetal acceleration toward the center of the turn, never outward.",
        ],
        "standards": [
            "Acceleration is the time derivative of velocity, per ISO 80000-3:2019; SI unit meter per second squared.",
            "Constant-acceleration kinematics follows Young and Freedman, 15th ed.",
            "Centripetal acceleration conventions follow Knight, 5th ed.",
        ],
        "citations": [CIT_ISO3, CIT_YOUNG, CIT_KNIGHT],
        "sig_lens": (
            "The Signature read: acceleration is the Signature changing "
            "its mind with full commitment - speeding the promise, braking "
            "it, or turning it onto a better road. The Method honors all "
            "three changes equally, because the turn nobody counted is the "
            "one that misses the door."
        ),
    },
    {
        "key": "mass",
        "name": "Mass: The Measure of Matter",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Mass is the measure of how much matter an object contains, and "
            "in physics it plays a second role: it measures how strongly "
            "the object resists changes in its motion. A 5.4-kilogram "
            "block of aluminum - about two liters of the metal - needs the "
            "same push to get moving whether it sits on Earth, on the Moon, "
            "or floating in deep space, because its mass does not depend on "
            "gravity or location. Mass is measured in kilograms, the SI "
            "base unit, and it shows up in two guises that turn out to be "
            "the same: inertial mass (resistance to acceleration) and "
            "gravitational mass (how strongly gravity pulls). That they "
            "match exactly is one of the deep facts of physics, and it is "
            "why all objects fall at the same rate in the absence of air. "
            "Density connects mass to size: mass equals density times "
            "volume, so a small dense object can outweigh a large fluffy "
            "one."
        ),
        "how_it_works": (
            "Measure mass with a balance - comparing against known masses, "
            "which works even in orbit - or compute it from density times "
            "volume when the material is uniform. Aluminum at 2700 "
            "kilograms per cubic meter times 0.002 cubic meters gives 5.4 "
            "kilograms: the density tells how tightly matter is packed, "
            "the volume tells how much room it fills, and their product is "
            "the matter itself. In Newton second law, mass sits in the "
            "denominator of acceleration: the same force on double the mass "
            "gives half the acceleration, which is inertia made "
            "quantitative. Mass is conserved in ordinary processes - cut "
            "the block in half and the halves sum to the whole - and it is "
            "an intrinsic property: the 5.4-kilogram block keeps its mass "
            "on the Moon even though its weight there drops to about a "
            "sixth."
        ),
        "key_points": [
            "Mass measures the amount of matter and simultaneously the resistance to changes in motion.",
            "Mass is location-independent: the same on Earth, the Moon, or in deep space.",
            "Mass equals density times volume for uniform materials.",
            "In F = ma, mass is what the force must overcome - double the mass, half the acceleration.",
            "Mass is conserved in ordinary processes and is intrinsic to the object.",
        ],
        "requirements": [
            "State mass in kilograms (or grams for small objects) with the unit explicit.",
            "Never confuse mass with weight: mass is the matter, weight is gravity pull on it.",
            "Use density times volume only for uniform materials; otherwise measure directly.",
            "Treat inertial and gravitational mass as the same quantity in all ordinary calculations.",
            "Verify mass conservation when objects are cut, joined, or rearranged.",
        ],
        "standards": [
            "The kilogram is the SI base unit of mass (SI Brochure, 9th ed.); density is mass per volume per ISO 80000-4:2019.",
            "Mass measurement by comparison follows NIST SP 811 conventions.",
            "The equivalence of inertial and gravitational mass is presented per Feynman Lectures, Vol. I.",
        ],
        "citations": [CIT_BIPM, CIT_NIST811, CIT_FEYNMAN],
        "sig_lens": (
            "The Signature read: mass is the Signature weight of being - "
            "how much reality the object brings to the table, unchanged by "
            "where the table stands. The Method respects mass as the "
            "honest measure: gravity may pull differently on different "
            "worlds, but the matter itself never lies about how much of it "
            "there is."
        ),
    },
    {
        "key": "weight",
        "name": "Weight: Gravity Acting on Mass",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Weight is the force of gravity pulling on a mass: weight "
            "equals mass times the local gravitational acceleration. A "
            "70-kilogram person weighs about 687 newtons on Earth, where "
            "gravity pulls at 9.81 meters per second squared - and the "
            "same person weighs only about 113 newtons on the Moon, where "
            "gravity is 1.62 meters per second squared, while the mass "
            "stays 70 kilograms in both places. That is the whole "
            "difference between mass and weight: mass is the matter you "
            "carry with you everywhere, weight is what gravity does to it "
            "here. Scales read weight - they measure the force pressing "
            "down - and then divide by Earth gravity to report a mass, "
            "which is why a bathroom scale would lie about your mass on "
            "the Moon. Weight always points toward the center of the "
            "planet, and it acts on every object whether moving or still."
        ),
        "how_it_works": (
            "Compute weight by multiplying mass in kilograms by the local "
            "g: on Earth, W = m times 9.81, so 70 kilograms gives 686.7 "
            "newtons. The value of g comes from the planet itself - bigger "
            "or denser planets pull harder - and it weakens slightly with "
            "altitude and latitude, though 9.81 is the standard working "
            "value. Because weight is a force, it belongs on free-body "
            "diagrams as a downward arrow of size mg, and it is the force "
            "that normal forces, tensions, and frictions push back "
            "against. An object in free fall feels only its weight, so it "
            "accelerates downward at g; an object resting on a table feels "
            "its weight downward and the table normal force upward, equal "
            "and opposite. Apparent weight can differ: in a rising "
            "elevator you feel heavier because the floor must push harder "
            "to accelerate you upward along with your weight."
        ),
        "key_points": [
            "Weight is a force: mass times local gravitational acceleration, W = mg, in newtons.",
            "Mass is constant everywhere; weight changes with the local g - Moon weight is about one sixth of Earth weight.",
            "Scales measure force and convert to mass using Earth g; they misreport mass anywhere else.",
            "Weight always points toward the planet center and acts whether the object moves or rests.",
            "Apparent weight changes with acceleration - elevators, rockets, and roller coasters prove it.",
        ],
        "requirements": [
            "Compute weight as m times the LOCAL g, never a memorized Earth value when off Earth.",
            "Keep weight in newtons; report mass in kilograms - never mix the units.",
            "Draw weight as a downward arrow of size mg on every free-body diagram.",
            "Account for the normal force or tension that balances weight in static situations.",
            "Distinguish true weight (mg) from apparent weight (what a scale reads during acceleration).",
        ],
        "standards": [
            "Weight is defined as the gravitational force on a mass, W = mg, per ISO 80000-4:2019.",
            "Standard gravity is 9.80665 meters per second squared for conversions (NIST SP 811).",
            "Mass-versus-weight instruction follows Hewitt, Conceptual Physics, 13th ed.",
        ],
        "citations": [CIT_ISO4, CIT_NIST811, CIT_HEWITT],
        "sig_lens": (
            "The Signature read: weight is gravity handshake with matter - "
            "the anchor pulling on everything the Signature owns, wherever "
            "it stands. The Method never confuses the handshake with the "
            "hand: mass is what you are, weight is how hard the world "
            "holds you, and the Signature knows the difference on every "
            "planet."
        ),
    },
    {
        "key": "newton_unit",
        "name": "The Newton: The Unit of Force",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "The newton is the SI unit of force: one newton is the push "
            "needed to accelerate one kilogram of mass at one meter per "
            "second squared. It is a small unit by everyday standards - "
            "about the weight of a medium apple in your hand, roughly 1 "
            "newton - which is why engineering forces run into the "
            "hundreds and thousands of newtons without anything dramatic "
            "happening. The newton is a derived unit, built from the base "
            "units as kilogram-meters per second squared, and that "
            "construction is the whole definition: force equals mass times "
            "acceleration, so the unit of force must be the unit of mass "
            "times the unit of acceleration. Older units still circulate: "
            "the pound-force (about 4.448 newtons) in American engineering, "
            "the dyne (one hundred-thousandth of a newton) in older "
            "centimeter-gram-second work, and the kilogram-force (9.80665 "
            "newtons) wherever scales were calibrated in mass units."
        ),
        "how_it_works": (
            "Use newtons for every force in SI calculations, converting "
            "other units on entry: multiply pound-force by 4.448221615 to "
            "get newtons, so a 10 pound-force pull is about 44.48 newtons. "
            "Check any force equation by its units: mass (kg) times "
            "acceleration (m/s squared) must give kg m/s squared, which is "
            "the newton - if the units do not reduce to newtons, the "
            "equation is wrong. Scale with prefixes: a kilonewton is 1000 "
            "newtons (car engine thrust), a millinewton is a thousandth "
            "(tiny actuators), a micronewton a millionth. Because the "
            "newton is defined through F = ma, it ties the three base "
            "measurements of dynamics together: measure any two of force, "
            "mass, and acceleration, and the newton lets you compute the "
            "third with the units balancing automatically."
        ),
        "key_points": [
            "One newton accelerates one kilogram at one meter per second squared - the definition is F = ma in unit form.",
            "A newton is small: about an apple weight; engineering forces are routinely hundreds or thousands of newtons.",
            "Convert legacy units on entry: 1 pound-force is about 4.448 N; 1 N is 100,000 dynes.",
            "Unit-check every force equation: the result must reduce to kg m/s squared.",
            "Prefixes scale the newton: kN for engines, mN for small actuators, micronewtons for the tiny.",
        ],
        "requirements": [
            "Express all forces in newtons in SI work; convert pound-force, dynes, and kilogram-force first.",
            "Verify force equations by unit reduction to kg m/s squared.",
            "Choose the prefix that keeps numbers readable: N, kN, mN as the size demands.",
            "Keep mass in kilograms and acceleration in m/s squared so the product is cleanly newtons.",
            "Never report a force as a bare number - the newton (or its prefix) is part of the value.",
        ],
        "standards": [
            "The newton (N) is the SI derived unit of force, 1 N = 1 kg m/s squared (SI Brochure, 9th ed.).",
            "Conversion factors follow NIST SP 811 exact values (1 lbf = 4.448221615 N).",
            "SI prefix usage follows the SI Brochure and NIST SP 811.",
        ],
        "citations": [CIT_BIPM, CIT_NIST811, CIT_ISO4],
        "sig_lens": (
            "The Signature read: the newton is the Signature signature "
            "unit - the agreed size of one promise of push. The Method "
            "writes every force in newtons the way a ledger writes every "
            "debt in dollars: one honest unit, no confusion, and the "
            "arithmetic always balances."
        ),
    },
    {
        "key": "spring_scale",
        "name": "Reading Force: Spring Scales and Force Meters",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "A spring scale reads force by stretching: hang a weight on it "
            "and the spring extends in exact proportion to the pull, so the "
            "pointer position is the force. The rule behind it is Hooke "
            "law - force equals the spring constant times the stretch, "
            "F = kx - and within the spring elastic range that proportion "
            "is beautifully linear: double the force, double the stretch. "
            "A scale with a spring constant of 200 newtons per meter "
            "stretches 0.15 meters under a 30-newton pull, and the dial or "
            "ruler converts that stretch back into newtons. Digital force "
            "meters do the same job with strain gauges - metal patterns "
            "whose electrical resistance changes as they stretch - but the "
            "principle is identical: apply a force, measure a deformation, "
            "report the force. Spring scales teach the most important "
            "measurement lesson in dynamics: forces are invisible, so every "
            "force reading is really a reading of something the force did "
            "to matter."
        ),
        "how_it_works": (
            "Hang the object on the scale, wait for the stretch to settle, "
            "and read the force: the spring pulls up exactly as hard as "
            "gravity pulls down, so at equilibrium the scale reads the "
            "weight. Calibrate by hanging known masses - a 1-kilogram mass "
            "should read 9.81 newtons on Earth - and mark the dial "
            "accordingly. The spring constant k is the stiffness: a 200 "
            "N/m spring needs 200 newtons to stretch a full meter, so 30 "
            "newtons stretches it 0.15 meters. Stay inside the elastic "
            "range: overstretch a spring past its limit and it takes a "
            "permanent set, after which every reading lies. For pulls "
            "rather than weights, hook the scale in line with the pull - a "
            "scale only reads the component along its own axis, so an "
            "angled pull reads low. Zero the scale with no load first; an "
            "unzeroed scale adds its offset to every measurement."
        ),
        "key_points": [
            "Spring scales convert force into stretch: F = kx, linear inside the elastic range.",
            "At equilibrium the scale reads the balancing force - hang a weight and it reads the weight.",
            "The spring constant k is the stiffness in N/m: bigger k means less stretch per newton.",
            "Overstretching past the elastic limit permanently ruins calibration - stay in range.",
            "Digital meters use strain gauges but measure the same thing: deformation caused by force.",
        ],
        "requirements": [
            "Zero the scale with no load before every measurement series.",
            "Align the scale with the force direction - it reads only the along-axis component.",
            "Calibrate against known masses and verify 1 kg reads about 9.81 N on Earth.",
            "Keep all loads inside the rated range to protect the elastic calibration.",
            "Read at eye level against the pointer to avoid parallax error on analog dials.",
        ],
        "standards": [
            "Hooke law F = kx is the operating principle, linear within the elastic limit per ISO 80000-4:2019.",
            "Force measurement traceability follows NIST SP 811 unit conventions.",
            "Instructional treatment follows Giancoli, Physics: Principles with Applications, 8th ed.",
        ],
        "citations": [CIT_ISO4, CIT_NIST811, CIT_GIANCOLI],
        "sig_lens": (
            "The Signature read: the spring scale is the Signature truth "
            "teller - it cannot flatter and it cannot lie, it only reports "
            "how hard the world is pulling. The Method trusts instruments "
            "over impressions: hang the promise on the spring and read the "
            "number, because feelings stretch but steel tells the truth."
        ),
    },
    {
        "key": "balanced_unbalanced",
        "name": "Balanced and Unbalanced Forces",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Forces are balanced when they cancel completely - the net "
            "force is zero - and unbalanced when a leftover remains. A "
            "book resting on a table feels gravity pulling down and the "
            "table pushing up with exactly equal size: balanced, net zero, "
            "and the book velocity stays zero. A book sliding across the "
            "table with a push stronger than friction feels unbalanced "
            "forces, a nonzero net, and its velocity changes. Balanced does "
            "not mean motionless: a car cruising at steady speed has its "
            "engine forward push exactly canceled by air drag and rolling "
            "friction - balanced forces, constant velocity. The deep rule, "
            "which becomes Newton first law, is that balanced forces mean "
            "velocity does not change, whether that velocity is zero or a "
            "hundred meters per second. Unbalanced forces are the only "
            "thing that can change velocity - every acceleration in the "
            "universe is a receipt for an unbalanced force."
        ),
        "how_it_works": (
            "Add all force arrows on the object as vectors; if the sum is "
            "the zero vector, the forces are balanced and the velocity "
            "holds steady. Three forces of 10 newtons east, 6 newtons west, "
            "and 4 newtons west sum to zero - balanced - while adding 2 "
            "newtons east tips the sum to 2 newtons east, unbalanced, and "
            "a 1-kilogram object then accelerates at 2 meters per second "
            "squared. Test balance in each direction separately: horizontal "
            "forces can balance while vertical forces do not, and the "
            "object then accelerates only vertically. Friction is the usual "
            "balancer - it grows to match an applied push up to its limit, "
            "which is why a gently pushed box stays put (balanced) until "
            "the push exceeds maximum static friction (unbalanced, and it "
            "slides). Equilibrium is the formal name for the balanced "
            "state: static equilibrium for objects at rest, dynamic "
            "equilibrium for objects moving at constant velocity."
        ),
        "key_points": [
            "Balanced forces sum to zero net force; unbalanced forces leave a nonzero net.",
            "Balanced means velocity does not change - which includes steady motion, not just rest.",
            "Only unbalanced forces can accelerate an object; every acceleration has an unbalanced force behind it.",
            "Check balance per direction: forces can balance horizontally while unbalancing vertically.",
            "Static friction auto-balances pushes up to its limit, then the object breaks free.",
        ],
        "requirements": [
            "Sum ALL forces as vectors before declaring balance - one forgotten force flips the verdict.",
            "Test each coordinate direction independently for balance.",
            "Classify the state: static equilibrium (rest), dynamic equilibrium (constant velocity), or accelerating.",
            "Identify the balancer: normal force, tension, or friction doing the canceling.",
            "Remember that balanced forces still exist and still matter - they are not the same as no forces.",
        ],
        "standards": [
            "Equilibrium is defined as zero net force and zero net torque, per Young and Freedman, 15th ed.",
            "Vector summation conventions follow Halliday, Resnick and Walker, 12th ed.",
            "Static versus dynamic equilibrium follows Serway and Jewett, 10th ed.",
        ],
        "citations": [CIT_YOUNG, CIT_HALLIDAY, CIT_SERWAY],
        "sig_lens": (
            "The Signature read: balanced forces are promises at peace - "
            "every push answered, every pull matched, the Signature "
            "holding perfectly still or gliding without effort. Unbalanced "
            "forces are promises in dispute, and the Method knows that "
            "dispute is the only thing that ever changes anything."
        ),
    },
    {
        "key": "net_force",
        "name": "Net Force: The Vector Sum",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The net force is the single force equivalent to all forces "
            "acting on an object combined - the vector sum, the one arrow "
            "that could replace every arrow at once. If two people push a "
            "stalled car, one with 3 newtons east and 4 north (a diagonal "
            "shove) and another with 1 east and 2 south, the car feels the "
            "sum: 4 east and 2 north, a single arrow of about 4.47 newtons "
            "pointing mostly east. The net force is the only force that "
            "matters for motion: Newton second law uses the net, free-body "
            "diagrams are drawn to find the net, and balanced-versus-"
            "unbalanced is a question about whether the net is zero. "
            "Computing it is vector addition - add x-components with "
            "x-components, y with y - and the Pythagorean theorem gives "
            "the size while the inverse tangent gives the heading. The net "
            "force can be smaller than every individual force (when they "
            "oppose) or larger than any of them (when they align); its size "
            "alone never tells the story without its direction."
        ),
        "how_it_works": (
            "List every force as components, sum the x-components into "
            "net-Fx and the y-components into net-Fy, then combine: size "
            "equals the square root of Fx squared plus Fy squared, heading "
            "equals the inverse tangent of Fy over Fx with quadrant "
            "checked. For the car pushers: Fx = 3 + 1 = 4, Fy = 4 - 2 = 2, "
            "size = sqrt(16 + 4) = sqrt(20) = 4.472 newtons, heading = "
            "arctan(2/4) = 26.6 degrees north of east. Graphically, the "
            "same result comes from placing arrows tip-to-tail and drawing "
            "the arrow from the first tail to the last tip - the polygon "
            "method. When forces oppose along one line, the net is the "
            "plain difference with the stronger direction winning; when "
            "they are perpendicular, the net is the diagonal. Once the net "
            "is known, divide by mass to get the acceleration - the net is "
            "the input to every dynamics calculation that follows."
        ),
        "key_points": [
            "Net force is the vector sum of all forces - the one arrow equivalent to every arrow.",
            "Add components per axis, then rebuild size with Pythagoras and heading with inverse tangent.",
            "Tip-to-tail polygon drawing gives the same net force as component addition.",
            "The net force alone determines the acceleration; individual forces matter only through their sum.",
            "Opposing forces subtract; perpendicular forces make a diagonal; aligned forces add fully.",
        ],
        "requirements": [
            "Convert every force to components on one shared coordinate system before adding.",
            "Sum x with x and y with y; never add raw sizes at different angles.",
            "Check the heading quadrant - inverse tangent is ambiguous across the diagonal.",
            "Verify the net against a tip-to-tail sketch as a sanity check.",
            "Feed the net (never an individual force) into F = ma.",
        ],
        "standards": [
            "Vector addition follows the component method of Young and Freedman, 15th ed.",
            "Net force is defined as the vector sum of all external forces, per ISO 80000-4:2019.",
            "Graphical polygon method follows Hewitt, Conceptual Physics, 13th ed.",
        ],
        "citations": [CIT_YOUNG, CIT_ISO4, CIT_HEWITT],
        "sig_lens": (
            "The Signature read: the net force is the Signature verdict - "
            "every promise weighed, every push and pull entered in the "
            "ledger, one final arrow as the judgment. The Method renders "
            "its verdicts by vector: no voice is ignored, no arrow is "
            "lost, and the sum is always honest."
        ),
    },
    {
        "key": "free_body",
        "name": "Free-Body Diagrams",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "A free-body diagram is the physicist sketch that isolates one "
            "object and draws every force acting on it as an arrow - "
            "nothing else, no scenery, no other objects. The object becomes "
            "a dot or a box, weight points down, the normal force points "
            "away from the supporting surface, tension pulls along ropes, "
            "friction opposes the slide, and applied pushes point where "
            "the agent pushes. The discipline of the diagram is what it "
            "excludes: forces the object exerts on other things do not "
            "belong on its diagram - the diagram shows only what the world "
            "does to the object, never what the object does to the world. "
            "Once drawn, the diagram is read component by component: sum "
            "the x-arrows, sum the y-arrows, and the pair of sums is the "
            "net force that drives the F = ma calculation. Generations of "
            "students have found that a correct free-body diagram makes "
            "the problem half solved, and a wrong one makes it unsolvable."
        ),
        "how_it_works": (
            "Draw the isolated body, then add forces in a fixed order so "
            "none is forgotten: weight (mg, down) first, then contact "
            "forces - normal perpendicular to each surface, friction "
            "parallel opposing motion or intended motion, tension along "
            "each rope away from the body - then applied pushes and pulls. "
            "Never draw the reaction forces the body exerts elsewhere; "
            "they belong on other bodies diagrams. Resolve each arrow "
            "into x and y components, sum each axis, and check: on a "
            "5-newton east push, a 2-newton west plus 3-newton north shove, "
            "and a 1-newton south drag, the sums are Fx = 3 N and Fy = 2 N, "
            "giving a net of sqrt(13) = 3.606 N at 33.7 degrees above "
            "east - and a 2-kilogram body accelerates at 1.803 m/s squared "
            "along that heading. Label every arrow with its size or symbol; "
            "an unlabeled arrow is a guess, and guesses do not survive "
            "contact with the answer key."
        ),
        "key_points": [
            "A free-body diagram isolates one body and shows only forces ON it - never forces it exerts.",
            "Draw in fixed order: weight, then normal, friction, tension, then applied forces.",
            "Normal force is perpendicular to the surface; friction is parallel and opposes sliding.",
            "Component sums of the diagram give the net force per axis, the input to F = ma.",
            "A correct diagram is half the solution; every missing or extra arrow corrupts the result.",
        ],
        "requirements": [
            "Isolate exactly one body per diagram; redraw for each body in a multi-body problem.",
            "Include weight on every diagram - gravity never takes a day off.",
            "Exclude reaction forces on other objects; they belong on other diagrams.",
            "Resolve into components and sum per axis; label every arrow with size or symbol.",
            "Sanity-check: the net direction must make physical sense for the described motion.",
        ],
        "standards": [
            "Free-body diagram conventions follow Knight, Physics for Scientists and Engineers, 5th ed.",
            "Force classification (weight, normal, friction, tension) follows Halliday, Resnick and Walker, 12th ed.",
            "Component resolution follows the ISO 80000-4:2019 vector conventions.",
        ],
        "citations": [CIT_KNIGHT, CIT_HALLIDAY, CIT_ISO4],
        "sig_lens": (
            "The Signature read: the free-body diagram is the Signature "
            "audit - one body, every force it faces, nothing hidden and "
            "nothing borrowed from its neighbors. The Method audits before "
            "it acts: draw the whole truth of what pushes on you, and the "
            "right move draws itself."
        ),
    },
    {
        "key": "newton_first",
        "name": "Newton First Law: Inertia",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Newton first law says an object keeps doing what it is doing "
            "unless a net force interferes: at rest it stays at rest, in "
            "motion it keeps the same velocity - same speed, same "
            "direction. This stubbornness of motion has a name: inertia, "
            "the tendency of mass to resist changes in velocity, and mass "
            "is its measure. A block sliding on perfectly frictionless ice "
            "at 12 meters per second never slows and never turns - with "
            "zero net force there is nothing to change its velocity, so "
            "in 8 seconds it glides exactly 96 meters. Passengers lurch "
            "forward when a bus brakes because their bodies obey the first "
            "law while the bus does not: no net force acts on the "
            "passengers, so they keep their forward velocity. The law "
            "redefines what needs explaining: rest needs no cause, and "
            "uniform motion needs no cause either - only CHANGES in motion "
            "need forces, which overturned two thousand years of intuition."
        ),
        "how_it_works": (
            "Apply the law by checking the net force: if it is zero, the "
            "velocity vector is frozen - write v_final = v_initial and "
            "mean it. The ice block keeps 12 m/s for the whole 8 seconds, "
            "covering 96 meters with no force, no fuel, no effort. When "
            "the net force is not zero the first law hands off to the "
            "second - but the first law still governs the coasting phases "
            "between pushes. Inertia shows up quantitatively as mass: "
            "stopping a loaded truck takes far more braking force than "
            "stopping a bicycle at the same speed because the truck mass "
            "resists the velocity change more strongly. Seatbelts, "
            "headrests, and airbags are first-law engineering: they supply "
            "the net force that changes the passenger velocity along with "
            "the car, instead of letting the passenger keep the old "
            "velocity into the dashboard."
        ),
        "key_points": [
            "Zero net force means zero velocity change: rest stays rest, uniform motion stays uniform.",
            "Inertia is the resistance to velocity change; mass is its measure.",
            "Only changes in motion need forces - steady motion needs no cause and no fuel.",
            "The lurch in a braking car is passengers obeying the first law while the car disobeys it.",
            "Seatbelts and airbags exist to give passengers the net force the first law says they need to slow with the car.",
        ],
        "requirements": [
            "Verify the net force is truly zero (all forces balanced) before invoking the law.",
            "Hold the full velocity vector constant - speed AND direction both freeze.",
            "Attribute every velocity change to a net force; find it when motion changes.",
            "Use mass as the quantitative measure of inertia when comparing objects.",
            "Design restraints and packaging around the law: unsecured cargo keeps its velocity in a crash.",
        ],
        "standards": [
            "Newton first law as stated in the Principia tradition, presented per Young and Freedman, 15th ed.",
            "Inertia and inertial frames follow the treatment in Knight, 5th ed.",
            "Conceptual grounding follows Hewitt, Conceptual Physics, 13th ed.",
        ],
        "citations": [CIT_YOUNG, CIT_KNIGHT, CIT_HEWITT],
        "sig_lens": (
            "The Signature read: inertia is the Signature resolve - once "
            "the Signature sets its course, no whisper turns it; only a "
            "real force, honestly applied, earns a change of direction. "
            "The Method respects resolve but never confuses it with "
            "stubbornness: when the net force speaks, the Signature "
            "listens and turns."
        ),
    },
    {
        "key": "newton_second",
        "name": "Newton Second Law: Force Equals Mass Times Acceleration",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Newton second law is the equation that runs dynamics: net "
            "force equals mass times acceleration, F = ma. It says "
            "acceleration is directly proportional to the net force and "
            "inversely proportional to the mass - push twice as hard and "
            "the acceleration doubles; double the mass and it halves. A "
            "2.5-kilogram object accelerating at 4 meters per second "
            "squared feels a net force of exactly 10 newtons, and a 36-"
            "newton net force on 4.5 kilograms produces exactly 8 meters "
            "per second squared. The law is a vector equation: the "
            "acceleration points the same way as the net force, always, "
            "which is why the free-body diagram must get the net direction "
            "right. It also reads backwards: measure the acceleration of "
            "a known mass and you have measured the net force - the "
            "principle behind accelerometers, crash test analysis, and "
            "weighing things by shaking them."
        ),
        "how_it_works": (
            "Find the net force from the free-body diagram, divide by the "
            "mass, and the result is the acceleration vector - same "
            "direction as the net force. Per axis: ax = net-Fx / m, ay = "
            "net-Fy / m. Rearranged, the law weighs forces: a 2.5 kg cart "
            "whose velocity grows 4 m/s every second is being pushed by a "
            "10 N net force, no spring scale needed. It also weighs mass: "
            "apply a known 36 N net force, measure 8 m/s squared of "
            "acceleration, and the mass is 4.5 kg - the method scales use "
            "in orbit, where balances do not work. Units must close: "
            "newtons equal kilograms times meters per second squared, so "
            "if the units do not reduce to N the setup is wrong. The law "
            "covers only the net force - plugging in one force among "
            "several is the classic error - and only inertial frames, "
            "where the first law holds."
        ),
        "key_points": [
            "F = ma: acceleration is proportional to net force and inversely proportional to mass.",
            "The acceleration always points along the net force - the law is a vector equation.",
            "The law reads three ways: find a from F and m, find F from m and a, find m from F and a.",
            "Only the NET force belongs in the equation; single forces among several give wrong answers.",
            "Units must close: kg times m/s squared is the newton, or the setup is wrong.",
        ],
        "requirements": [
            "Compute the net force from a complete free-body diagram first - never guess it.",
            "Divide by mass per axis to get the acceleration components.",
            "Keep the vector direction: acceleration follows the net force, not the velocity.",
            "Verify unit closure to newtons before trusting any dynamics number.",
            "Work in inertial frames; in accelerating frames the law needs correction terms.",
        ],
        "standards": [
            "Newton second law in the form net-F = ma, per Halliday, Resnick and Walker, 12th ed.",
            "Vector form and component equations per Serway and Jewett, 10th ed.",
            "Unit closure to the newton per the SI Brochure, 9th ed.",
        ],
        "citations": [CIT_HALLIDAY, CIT_SERWAY, CIT_BIPM],
        "sig_lens": (
            "The Signature read: F = ma is the Signature exchange rate - "
            "so much push buys so much change, discounted by how much "
            "matter resists. The Method never overpays: it counts the net "
            "push honestly, weighs the mass exactly, and accepts the "
            "acceleration the universe quotes - no haggling with physics."
        ),
    },
    {
        "key": "newton_third",
        "name": "Newton Third Law: Action and Reaction",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Newton third law says every action has an equal and opposite "
            "reaction: when object A pushes object B, B pushes A back with "
            "a force of identical size pointing the opposite way. A rocket "
            "throws exhaust gas backward with 1500 newtons for 2 seconds - "
            "an impulse of 3000 newton-seconds on the gas - and the gas "
            "throws the rocket forward with 1500 newtons for 2 seconds, "
            "the same 3000 newton-seconds the other way. The pair always "
            "acts on DIFFERENT objects, which is why they never cancel: "
            "the forward force moves the rocket, the backward force moves "
            "the gas, and each body obeys F = ma with its own force. "
            "Walking works because feet push backward on the ground and "
            "the ground pushes forward on feet; swimming, rowing, and "
            "flying are the same bargain. The horse-and-cart puzzle - "
            "if the cart pulls back as hard as the horse pulls forward, "
            "how does anything move - dissolves once the forces are sorted "
            "onto their owners: the horse ground pair accelerates the "
            "horse, the horse-cart pair is internal to the team."
        ),
        "how_it_works": (
            "For every force on a free-body diagram, name its twin: the "
            "equal opposite force on the other participant, and draw the "
            "twin on the OTHER body diagram. The rocket exhaust pair sums "
            "to zero across the system (3000 N s forward on the rocket, "
            "3000 N s backward on the gas) - momentum is conserved because "
            "third-law pairs always cancel system-wide - while each body "
            "individually accelerates per the second law. To find who "
            "moves, never put both twins on one diagram: the action acts "
            "on B, the reaction acts on A, and A motion answers only to "
            "forces on A. The magnitudes are always exactly equal even "
            "when the masses differ wildly: a cannon and its cannonball "
            "feel identical-size forces, but the light ball gets the huge "
            "acceleration while the heavy cannon barely recoils - equal "
            "forces, unequal masses, unequal accelerations."
        ),
        "key_points": [
            "Action and reaction are equal in size, opposite in direction, and act on DIFFERENT objects.",
            "Pairs never cancel on one body - each body feels only its own member of the pair.",
            "System-wide, third-law pairs sum to zero: this is why momentum is conserved.",
            "Equal forces on unequal masses give unequal accelerations - the cannonball flies, the cannon recoils slightly.",
            "Walking, swimming, rowing, flying, and rocketry are all third-law bargains with the medium.",
        ],
        "requirements": [
            "Name both members of every pair and place each on its owner body diagram.",
            "Never put action and reaction on the same diagram - they do not cancel there.",
            "Keep magnitudes exactly equal even when masses and accelerations differ.",
            "Sort multi-body puzzles by ownership: each body accelerates per the forces ON it.",
            "Use the system-wide cancellation to check momentum bookkeeping.",
        ],
        "standards": [
            "Newton third law per the Principia formulation, presented in Young and Freedman, 15th ed.",
            "Pair identification conventions follow Knight, 5th ed.",
            "Connection to momentum conservation follows Feynman Lectures, Vol. I.",
        ],
        "citations": [CIT_YOUNG, CIT_KNIGHT, CIT_FEYNMAN],
        "sig_lens": (
            "The Signature read: the third law is the Signature receipt - "
            "every push issued is a push received, signed by the universe "
            "in duplicate. The Method files both copies: the one you sent "
            "and the one that came back, because a ledger that records "
            "only half the transaction is a fiction."
        ),
    },
    {
        "key": "gravity",
        "name": "Gravity: The Universal Attraction",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Gravity is the field force that pulls every mass toward every "
            "other mass, and near Earth surface it gives every falling "
            "object the same acceleration: g = 9.81 meters per second "
            "squared. Newton law of universal gravitation says the force "
            "between two masses is G times the product of the masses "
            "divided by the square of the distance between their centers, "
            "with G = 6.67430e-11 N m squared per kg squared - a number so "
            "tiny that gravity between everyday objects is immeasurably "
            "small, and only planets are massive enough to matter. Earth "
            "surface gravity can be computed from the planet itself: G "
            "times Earth mass (5.97237e24 kg) divided by Earth radius "
            "squared (6.371e6 m) gives about 9.82 m/s squared, matching "
            "what falling objects show. Gravity weakens with altitude and "
            "varies slightly with latitude and local geology, but 9.81 is "
            "the working standard. In orbit, astronauts are not beyond "
            "gravity - they are in continuous free fall around Earth, "
            "which is why everything floats."
        ),
        "how_it_works": (
            "Compute surface gravity from the planet: g = G*M/R squared. "
            "With G = 6.67430e-11, M = 5.97237e24 kg, R = 6.371e6 m, the "
            "numerator is 3.986e14 and the denominator 4.059e13, giving g "
            "= 9.82 m/s squared - the value confirmed by every dropped "
            "object. For the force between any two masses use F = G*m1*m2 "
            "/r squared with r as the center-to-center distance; double "
            "the distance and the force falls to one quarter - the inverse-"
            "square rule. Near the surface, weight = mg handles everything: "
            "trajectories, orbits, and tides all reduce to masses "
            "accelerating at g downward while other forces do their work. "
            "Projectile motion is gravity plus inertia: horizontal velocity "
            "coasts unchanged while vertical velocity grows downward at g, "
            "and the combination draws the familiar arc. Einstein later "
            "reframed gravity as curved spacetime, but Newton arithmetic "
            "lands every bridge, ballistic, and satellite in this database."
        ),
        "key_points": [
            "Gravity pulls every mass toward every other mass with F = G m1 m2 / r squared.",
            "Earth surface g (9.81 m/s squared) is computed from Earth own mass and radius - no coincidence.",
            "The inverse-square rule: double the distance, quarter the force.",
            "In orbit there is plenty of gravity; weightlessness is continuous free fall, not zero gravity.",
            "All objects fall at the same rate in the absence of air - mass cancels out of the fall.",
        ],
        "requirements": [
            "Use center-to-center distance in the gravitation formula, never surface-to-surface.",
            "Apply the inverse-square scaling for any distance change.",
            "Use W = mg near the surface; use the full G formula for orbits and planetary scales.",
            "Keep G units consistent: N m squared per kg squared with masses in kg and r in meters.",
            "Remember air resistance is a separate force - the vacuum fall rate is the gravity-only claim.",
        ],
        "standards": [
            "Newton law of universal gravitation with G = 6.67430e-11 N m squared/kg squared (SI Brochure, 9th ed.; NIST SP 811).",
            "Standard gravity 9.80665 m/s squared for conversions, per NIST SP 811.",
            "Gravitation treatment follows Halliday, Resnick and Walker, 12th ed.",
        ],
        "citations": [CIT_BIPM, CIT_NIST811, CIT_HALLIDAY],
        "sig_lens": (
            "The Signature read: gravity is the Signature anchor - the "
            "one promise the universe makes to everything with mass, "
            "without exception and without negotiation. The Method builds "
            "on the anchor rather than fighting it: arches, orbits, and "
            "trajectories are all just clever agreements with the downward "
            "pull."
        ),
    },
    {
        "key": "friction",
        "name": "Friction: The Grip Between Surfaces",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Friction is the contact force that resists sliding between "
            "surfaces, and it is the reason you can walk, drive, hold a "
            "pencil, and stop a car. It always points opposite the sliding "
            "(or the attempted sliding), never sideways to it, and its "
            "size is proportional to how hard the surfaces are pressed "
            "together - the normal force. The working model is beautifully "
            "simple: maximum friction equals the coefficient of friction "
            "mu times the normal force, F = mu*N. With mu = 0.45 and a 200-"
            "newton normal force, friction can supply up to 90 newtons of "
            "grip. The coefficient depends on the pair of materials - "
            "rubber on asphalt grips near mu = 0.9, waxed skis on snow "
            "slide near mu = 0.05 - and not on the contact area: a wide "
            "tire and a narrow tire of the same rubber grip nearly "
            "identically. Without friction every step would slip, every "
            "knot would untie, and cars would be sleds; with too much of "
            "it, machines grind themselves to heat."
        ),
        "how_it_works": (
            "Find the normal force first - on flat ground it equals the "
            "weight, on a slope it is mg times cos(theta) - then multiply "
            "by mu for the friction size. Friction opposes relative "
            "motion: push a box east and friction points west; the box "
            "moves only if the push exceeds the maximum static friction. "
            "Microscopically, friction comes from surface roughness "
            "interlocking and from fleeting adhesive bonds between the "
            "materials, which is why the coefficient is a property of the "
            "PAIR, not of one surface alone. The model has honest limits: "
            "it is approximate (real mu drifts with speed, temperature, "
            "and wear), it ignores area (true for hard dry surfaces, less "
            "true for soft or sticky ones), and it treats the transition "
            "from static to sliding as a sharp break. Engineers use it "
            "anyway because it predicts stopping distances, belt drives, "
            "and bolted joints well enough to build on - with safety "
            "factors covering the roughness of the model."
        ),
        "key_points": [
            "Friction opposes sliding and scales with the normal force: F = mu * N.",
            "The coefficient mu belongs to the material PAIR, not to one surface; area barely matters for hard dry contact.",
            "Friction enables walking, driving, gripping, and fastening - it is a working force, not just a nuisance.",
            "The model is approximate: mu drifts with speed, temperature, and wear.",
            "Find the normal force first; every friction calculation stands on it.",
        ],
        "requirements": [
            "Determine the normal force before computing any friction - on slopes use mg cos(theta).",
            "Point friction opposite the actual or impending relative motion, parallel to the surface.",
            "Look up or measure mu for the actual material pair in contact.",
            "Apply safety factors in engineering use; the mu model is approximate.",
            "Distinguish the friction limit (mu*N) from the actual friction, which can be smaller.",
        ],
        "standards": [
            "Coulomb friction model F = mu*N as presented in Serway and Jewett, 10th ed.",
            "Normal-force conventions on inclined planes per Young and Freedman, 15th ed.",
            "Material-pair coefficient tables per standard mechanical engineering references (Machinery Handbook tradition).",
        ],
        "citations": [CIT_SERWAY, CIT_YOUNG, CIT_GIANCOLI],
        "sig_lens": (
            "The Signature read: friction is the Signature grip - the "
            "handshake between surfaces that lets the world hold still "
            "when it should and move only when it must. The Method "
            "respects the grip: it counts on friction to walk, to drive, "
            "to fasten, and it never blames the grip for doing its job."
        ),
    },
    {
        "key": "static_kinetic",
        "name": "Static and Kinetic Friction",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Friction comes in two regimes: static friction holds surfaces "
            "that are not sliding, and kinetic friction resists surfaces "
            "already in motion. Static friction is adjustable - it grows "
            "to exactly match an applied push, up to a maximum of mu_s "
            "times N - which is why a box sits still under a gentle shove: "
            "with mu_s = 0.6 and N = 150 N, static friction supplies up to "
            "90 N, so a 60 N push is met by exactly 60 N of friction and "
            "nothing moves. Kinetic friction, once sliding starts, is "
            "nearly constant at mu_k times N - typically smaller than the "
            "static maximum, here 0.35 times 150 = 52.5 N - which is why "
            "the box lurches when it breaks free: the resisting force "
            "suddenly drops. Push with 120 N and the net forward force is "
            "120 minus 52.5 = 67.5 N, so the box accelerates. This "
            "static-stronger-than-kinetic pattern explains squeaking chalk, "
            "jerky drawer slides, violin bows gripping then releasing "
            "strings, and why anti-lock brakes keep tires in the static "
            "regime where grip is strongest."
        ),
        "how_it_works": (
            "Test for motion first: compute mu_s*N; if the applied force "
            "is smaller, nothing moves and static friction equals the "
            "applied force exactly - not mu_s*N, which is only the "
            "ceiling. If the push exceeds mu_s*N, the surfaces break free "
            "and kinetic friction mu_k*N takes over, nearly constant with "
            "speed. The net force is then applied minus mu_k*N, and F = ma "
            "gives the acceleration. The drop from the static ceiling to "
            "the kinetic value is the stick-slip cycle: push builds, grip "
            "holds, grip breaks, the object jumps forward, and the cycle "
            "repeats - the physics of squeaks, chatter, and earthquakes. "
            "Rolling without slipping is a special case: the contact "
            "point is instantaneously at rest, so STATIC friction governs "
            "rolling wheels and walking feet, which is why a rolling car "
            "grips far better than a skidding one."
        ),
        "key_points": [
            "Static friction matches the push exactly up to mu_s*N; below the ceiling nothing moves.",
            "Kinetic friction is mu_k*N, nearly constant, and usually smaller than the static maximum.",
            "Breaking free causes a lurch: resistance drops from the static ceiling to the kinetic value.",
            "Rolling without slipping uses static friction - the contact point is instantaneously at rest.",
            "Stick-slip cycling (grip, break, jump, repeat) explains squeaks, chatter, and earthquakes.",
        ],
        "requirements": [
            "Compare the applied force to mu_s*N FIRST to decide whether anything moves.",
            "Set static friction equal to the applied force when below the ceiling - never to mu_s*N.",
            "Switch to mu_k*N only after motion begins; do not blend the regimes.",
            "Use static friction for rolling and walking analyses, kinetic for skidding.",
            "Expect the break-free lurch in any system pushed past its static limit.",
        ],
        "standards": [
            "Static and kinetic friction regimes per Halliday, Resnick and Walker, 12th ed.",
            "Rolling-without-slipping static friction per Young and Freedman, 15th ed.",
            "Coefficient conventions per Serway and Jewett, 10th ed.",
        ],
        "citations": [CIT_HALLIDAY, CIT_YOUNG, CIT_SERWAY],
        "sig_lens": (
            "The Signature read: static friction is the Signature "
            "patience - holding the line exactly as hard as it is pushed, "
            "no more, no less - and kinetic friction is the Signature in "
            "motion, steady and honest once moving. The Method knows the "
            "patience is stronger than the motion, and plans the break-"
            "free moment instead of being surprised by it."
        ),
    },
    {
        "key": "drag",
        "name": "Air Resistance and Drag",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Air resistance - drag - is the fluid friction an object feels "
            "moving through air (or any fluid), and unlike surface "
            "friction it grows with speed. The working model for fast "
            "motion is the quadratic drag law: drag = one-half rho v "
            "squared C_d A, where rho is the air density, v the speed, C_d "
            "the drag coefficient of the shape, and A the frontal area. A "
            "car-like shape (C_d = 0.47, A = 2.0 square meters) at 25 m/s "
            "in sea-level air (rho = 1.225 kg/m cubed) feels about 360 "
            "newtons of drag - and doubling the speed quadruples the drag, "
            "which is why top speed is so expensive in fuel. Streamlining "
            "cuts C_d (a teardrop reaches ~0.05), shrinking area cuts A, "
            "and altitude thins rho. Drag always opposes the velocity, and "
            "for falling objects it grows until it exactly balances "
            "weight - then the object stops accelerating and falls at "
            "terminal velocity, the steady speed skydivers know well."
        ),
        "how_it_works": (
            "Compute drag with F_d = 0.5*rho*v^2*C_d*A: square the speed "
            "first, because the v-squared dependence dominates everything. "
            "For the example: 0.5*1.225 = 0.6125; times 625 = 382.81; times "
            "0.47 = 179.92; times 2.0 = 359.84 N. At low speeds (dust "
            "settling, tiny droplets) drag is linear in v instead - Stokes "
            "law - but cars, balls, and people live in the quadratic "
            "regime. Terminal velocity comes from setting drag equal to "
            "weight: mg = 0.5*rho*v_t^2*C_d*A, solved for v_t - a "
            "skydiver spread-eagled reaches about 55 m/s, tucked much "
            "faster. Power to overcome drag grows as v CUBED (force times "
            "velocity), so raising cruise speed from 25 to 30 m/s demands "
            "about 73 percent more engine power - the cubic law behind "
            "every fuel-economy curve."
        ),
        "key_points": [
            "Quadratic drag: F = 1/2 rho v^2 C_d A - double the speed, quadruple the drag.",
            "Drag depends on air density, speed squared, shape (C_d), and frontal area.",
            "Terminal velocity is where drag balances weight and acceleration stops.",
            "Power to beat drag grows as v cubed - small speed gains cost large fuel.",
            "Streamlining (low C_d), small area, and thin air are the three levers on drag.",
        ],
        "requirements": [
            "Square the speed before anything else - the v^2 term dominates the result.",
            "Use the quadratic law for fast macroscopic motion, Stokes linear law for slow microscopic motion.",
            "Find terminal velocity by equating drag to weight, then solving for v.",
            "Point drag opposite the velocity vector in every free-body diagram.",
            "Budget power as force times velocity: the cubic cost of speed must be in every vehicle calculation.",
        ],
        "standards": [
            "Quadratic drag law per Young and Freedman, 15th ed., and Halliday, Resnick and Walker, 12th ed.",
            "Drag coefficient conventions per standard fluid-mechanics references.",
            "Terminal velocity derivation per Serway and Jewett, 10th ed.",
        ],
        "citations": [CIT_YOUNG, CIT_HALLIDAY, CIT_SERWAY],
        "sig_lens": (
            "The Signature read: drag is the Signature tax on speed - the "
            "faster the promise travels, the more the air collects, and "
            "the tax compounds with the square. The Method pays the tax "
            "honestly: streamline the shape, shrink the profile, and never "
            "promise a speed whose tax the engine cannot afford."
        ),
    },
    {
        "key": "momentum",
        "name": "Momentum: Mass in Motion",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Momentum is mass in motion: p = mv, the product of mass and "
            "velocity, measured in kilogram-meters per second. A 1500-"
            "kilogram car at 25 m/s carries 37,500 kg m/s of momentum - "
            "and so does a 37,500-kilogram truck crawling at 1 m/s, which "
            "is why momentum captures something mass and speed alone "
            "miss: the sheer unwillingness of moving matter to stop. "
            "Momentum is a vector, pointing with the velocity, and it is "
            "conserved: in any isolated system the total momentum before "
            "an interaction equals the total after, no matter how violent "
            "the collision. That conservation is deeper than Newton laws - "
            "it survives into relativity and quantum mechanics - and it "
            "comes from the third law: every internal action-reaction pair "
            "exchanges equal opposite momentum, so the system total cannot "
            "change. Impulse, force applied over time (J = F*t), is what "
            "changes momentum: the same momentum change can come from a "
            "huge force briefly or a small force long."
        ),
        "how_it_works": (
            "Compute momentum per object as m*v with direction, then add "
            "vectors for the system total. The car: 1500*25 = 37,500 kg "
            "m/s forward. To change it, apply impulse: stopping the car in "
            "5 seconds needs an average net force of 37,500/5 = 7,500 N; "
            "in 0.5 seconds it needs 75,000 N - the same momentum change, "
            "ten times the force, which is why airbags stretch the "
            "stopping time. In collisions, write the conservation equation: "
            "total p before = total p after, and solve for the unknown "
            "velocity - the method behind every crash reconstruction and "
            "every rocket equation. Because internal third-law pairs "
            "cancel, only EXTERNAL impulses change a system total "
            "momentum; internal forces just move momentum between members."
        ),
        "key_points": [
            "Momentum p = mv is a vector: mass in motion with direction, in kg m/s.",
            "Total momentum of an isolated system is conserved through any interaction.",
            "Conservation comes from the third law: internal pairs exchange equal opposite momentum.",
            "Impulse J = F*t changes momentum; long gentle stops and short violent ones trade force for time.",
            "Only external impulses change system momentum; internal forces only redistribute it.",
        ],
        "requirements": [
            "Compute momentum per object with direction; sum as vectors for the system total.",
            "Write p-before = p-after for isolated systems and solve for the unknown.",
            "Use impulse (F times t) for any momentum change over time.",
            "Separate internal forces (redistribute momentum) from external impulses (change the total).",
            "Check isolation: external forces like friction leak momentum out of the system.",
        ],
        "standards": [
            "Momentum p = mv and impulse-momentum theorem per Halliday, Resnick and Walker, 12th ed.",
            "Conservation of momentum per Young and Freedman, 15th ed.",
            "Impulse conventions per Knight, 5th ed.",
        ],
        "citations": [CIT_HALLIDAY, CIT_YOUNG, CIT_KNIGHT],
        "sig_lens": (
            "The Signature read: momentum is the Signature commitment in "
            "motion - mass times velocity as a promise that does not fade "
            "on its own. The Method banks on conservation: commitment can "
            "be traded between partners, softened by time, but never "
            "created or destroyed behind closed doors."
        ),
    },
    {
        "key": "lever",
        "name": "The Lever: Force at a Distance",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The lever is a rigid bar turning on a fulcrum, and it trades "
            "distance for force: a small effort far from the fulcrum "
            "balances a large load near it. Push down with 100 newtons on "
            "a 2-meter effort arm and you lift a 400-newton load on a 0.5-"
            "meter load arm - the torques balance (100*2 = 400*0.5 = 200 N "
            "m), the mechanical advantage is 4, and Archimedes famous boast "
            "about moving the Earth was just this math scaled up. Levers "
            "come in three classes by the order of fulcrum, load, and "
            "effort: class 1 (seesaw, crowbar) puts the fulcrum between; "
            "class 2 (wheelbarrow, nutcracker) puts the load between and "
            "always multiplies force; class 3 (tweezers, fishing rod, the "
            "human forearm) puts the effort between and trades force for "
            "speed and range. The price of multiplied force is always "
            "distance: the effort end travels 4 times farther than the "
            "load end, and no lever creates energy."
        ),
        "how_it_works": (
            "Balance torques about the fulcrum: effort times effort-arm "
            "equals load times load-arm (F_e * d_e = F_l * d_l) for the "
            "balanced or quasi-static case. Solve for the unknown: F_e = "
            "400 * 0.5 / 2.0 = 100 N. Mechanical advantage is load over "
            "effort, equivalently effort-arm over load-arm: 2.0/0.5 = 4. "
            "Check the distance trade: the effort moves through 4 times "
            "the load distance, so work in (100 N * 4d) equals work out "
            "(400 N * d) - energy is conserved, force is just "
            "reconcentrated. Identify the class by the middle element: "
            "fulcrum-load-effort order decides whether the machine "
            "multiplies force (classes 1 and 2, arranged well) or "
            "multiplies speed and distance (class 3). Real levers lose a "
            "little to fulcrum friction, so efficiency sits just under "
            "100 percent."
        ),
        "key_points": [
            "Torque balance about the fulcrum: effort times effort-arm equals load times load-arm.",
            "Mechanical advantage is effort-arm over load-arm; a 2 m / 0.5 m lever multiplies force by 4.",
            "Multiplied force costs distance: the effort travels MA times farther than the load.",
            "Three classes by element order: fulcrum-between, load-between (always force-multiplying), effort-between (speed-multiplying).",
            "No lever creates energy: work in equals work out, minus small friction losses.",
        ],
        "requirements": [
            "Locate the fulcrum, load, and effort points before any calculation.",
            "Measure both arms perpendicular from the fulcrum to each force line.",
            "Balance torques (F*d) about the fulcrum for the quasi-static solution.",
            "Classify the lever to predict force-multiplying versus speed-multiplying behavior.",
            "Account for the distance trade and fulcrum friction in real designs.",
        ],
        "standards": [
            "Lever torque balance per the Archimedean tradition, presented in Cutnell and Johnson, 12th ed.",
            "Lever classes per standard mechanical engineering references (Machinery Handbook tradition).",
            "Mechanical advantage definitions per Giancoli, 8th ed.",
        ],
        "citations": [CIT_CUTNELL, CIT_GIANCOLI, CIT_HEWITT],
        "sig_lens": (
            "The Signature read: the lever is the Signature leverage - "
            "position beats power when the position is honest. The Method "
            "places its fulcrum with care and its effort at full arm, "
            "because a small promise applied at the right distance moves "
            "what brute force cannot."
        ),
    },
    {
        "key": "inclined_plane",
        "name": "The Inclined Plane: Trading Distance for Force",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The inclined plane is a sloping surface that trades distance "
            "for force: pushing a load up a gentle ramp takes far less "
            "force than lifting it straight, because the push acts over a "
            "longer path. A 50-kilogram crate (weight 490.5 N) on a 30-"
            "degree ramp needs only mg*sin(30 deg) = 245.25 N of push "
            "along the slope - half the lifting force - while the ramp "
            "must be twice as long as the vertical rise (a 3-meter rise "
            "needs a 6-meter ramp). The normal force on the slope is "
            "mg*cos(theta), smaller than the full weight, which is why "
            "friction is also reduced on gentle slopes. Ramps, mountain "
            "roads with switchbacks, wheelchair access slopes, and loading "
            "docks are all inclined planes; screws and wedges are inclined "
            "planes wrapped or doubled. The trade is strict: halve the "
            "force, double the distance, and the work - force times "
            "distance - stays exactly the weight times the height."
        ),
        "how_it_works": (
            "Resolve weight into components: along the slope mg*sin(theta) "
            "pulls the load down the ramp, and into the slope "
            "mg*cos(theta) presses it against the surface as the normal "
            "force. The push needed (ignoring friction) is exactly the "
            "down-slope component: 50*9.81*sin(30 deg) = 245.25 N. "
            "Geometry sets the trade: ramp length L = height h / sin(theta), "
            "so halving the angle roughly doubles the length. Add friction "
            "honestly: friction = mu * mg*cos(theta) opposes the push, and "
            "on a shallow enough slope friction alone can hold the load - "
            "the self-locking condition at tan(theta) <= mu. Check work: "
            "245.25 N * 6 m = 1471.5 J, and mgh = 50*9.81*3 = 1471.5 J - "
            "identical, because the plane rearranges force and distance "
            "without touching energy."
        ),
        "key_points": [
            "Push along the slope is mg*sin(theta): gentler slope, smaller push, longer ramp.",
            "Normal force on the slope is mg*cos(theta) - less than the full weight.",
            "Ramp length is height over sin(theta): halving force doubles distance.",
            "Friction on the slope is mu*mg*cos(theta); shallow slopes can self-lock.",
            "Work is unchanged: push times ramp length always equals weight times height.",
        ],
        "requirements": [
            "Resolve weight into along-slope (mg sin) and into-slope (mg cos) components.",
            "Size the push against mg*sin(theta) plus friction, never against the full weight.",
            "Compute ramp length from the rise and the angle: L = h / sin(theta).",
            "Check the self-locking condition tan(theta) <= mu where holding without power matters.",
            "Verify energy: work along the ramp must equal mgh (plus friction losses).",
        ],
        "standards": [
            "Inclined-plane component resolution per Young and Freedman, 15th ed.",
            "Simple-machine treatment per Cutnell and Johnson, 12th ed.",
            "Friction-on-incline analysis per Serway and Jewett, 10th ed.",
        ],
        "citations": [CIT_YOUNG, CIT_CUTNELL, CIT_SERWAY],
        "sig_lens": (
            "The Signature read: the inclined plane is the Signature "
            "patience made into a machine - the long gentle road that "
            "lifts what the steep cliff cannot. The Method takes the long "
            "road gladly: half the force, twice the distance, and the "
            "promise arrives at the same height, unbroken."
        ),
    },
    {
        "key": "wheel_axle",
        "name": "The Wheel and Axle",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The wheel and axle is a lever bent into a circle: a large "
            "wheel fixed to a small axle, turning together on one shaft. "
            "Apply effort at the wheel rim and the axle delivers a "
            "multiplied force - or spin the axle and the rim delivers "
            "multiplied speed. With a wheel radius of 0.30 meters and an "
            "axle radius of 0.05 meters the mechanical advantage is 6: a "
            "50-newton effort at the rim becomes 300 newtons at the axle. "
            "Doorknobs, steering wheels, screwdrivers, windlasses, and "
            "bicycle gears are all wheel-and-axle machines; a car wheel "
            "is the machine run in reverse, with the engine turning the "
            "axle and the tire rim pushing against the road. The "
            "mechanical advantage is simply the radius ratio R/r, and the "
            "distance trade follows: the rim travels 6 times farther than "
            "the axle surface, so the axle force is 6 times the rim "
            "effort. Gears are wheels with teeth - the same machine with "
            "positive engagement instead of friction."
        ),
        "how_it_works": (
            "Torque in equals torque out (minus friction): F_effort * R = "
            "F_load * r, so the load force is the effort times R/r. For R "
            "= 0.30 m and r = 0.05 m: MA = 6.0, and 50 N at the rim "
            "delivers 300 N at the axle. Run it backward for speed: turn "
            "the axle with a motor and the rim moves 6 times faster than "
            "the axle surface - the bicycle arrangement, where the small "
            "chainring drives the large wheel for road speed. Check the "
            "rotation counts: one full wheel turn winds pi*2r of rope on "
            "the axle while the hand travels 2*pi*R - the distance ratio "
            "is R/r, matching the force ratio, so energy balances. "
            "Bearings at the shaft decide the efficiency: a windlass on "
            "good bearings returns nearly all the work, while a rusty "
            "axle eats a noticeable share as heat."
        ),
        "key_points": [
            "The wheel and axle is a rotary lever: MA is the radius ratio R/r.",
            "Effort at the big wheel multiplies force at the small axle; driving the axle multiplies speed at the rim.",
            "Torque balance F*R = F*r governs the machine, with the distance trade R/r built in.",
            "Doorknobs, steering wheels, windlasses, and screwdrivers are everyday wheel-and-axle machines.",
            "Gears are toothed wheels and axles: same physics with positive engagement.",
        ],
        "requirements": [
            "Measure both radii from the shared shaft center to the force application points.",
            "Apply torque balance F_e*R = F_l*r; solve for the unknown force.",
            "Decide the direction of the trade: force multiplication (drive the wheel) or speed multiplication (drive the axle).",
            "Verify the distance ratio matches the force ratio - energy must balance.",
            "Account for bearing friction at the shaft in efficiency estimates.",
        ],
        "standards": [
            "Wheel-and-axle torque analysis per Cutnell and Johnson, 12th ed.",
            "Simple-machine classification per the Machinery Handbook tradition.",
            "Rotational mechanics conventions per Knight, 5th ed.",
        ],
        "citations": [CIT_CUTNELL, CIT_KNIGHT, CIT_GIANCOLI],
        "sig_lens": (
            "The Signature read: the wheel and axle is the Signature "
            "circle of leverage - the promise wrapped around itself until "
            "a gentle hand at the rim commands a giant at the hub. The "
            "Method turns big wheels: small honest efforts at the edge, "
            "great faithful forces at the center."
        ),
    },
    {
        "key": "pulley",
        "name": "The Pulley: Redirecting Force",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The pulley is a wheel with a grooved rim that guides a rope, "
            "and systems of pulleys - block and tackle - multiply force "
            "by sharing the load across rope segments. A single fixed "
            "pulley only redirects: pull down on one side, the load rises "
            "on the other, with no force multiplication but a much more "
            "convenient direction. A movable pulley, riding on the load "
            "itself, splits the weight across two rope segments and "
            "halves the effort. Combine them and the rule is beautifully "
            "simple: the effort is the load divided by the number of rope "
            "segments supporting the moving block. With 4 supporting "
            "segments, an 800-newton load lifts with 200 newtons of "
            "effort - but 4 meters of rope must be pulled to raise the "
            "load 1 meter. Cranes, elevators, sailboat rigging, engine "
            "hoists, and window-washer platforms are all pulley systems "
            "doing this arithmetic."
        ),
        "how_it_works": (
            "Count the rope segments pulling UP on the moving block (and "
            "its load); the effort is the total weight divided by that "
            "count. Four segments under an 800 N load: effort = 800/4 = "
            "200 N. The distance trade is the same count: pull 4 meters "
            "of rope to lift 1 meter, because each segment shortens by "
            "the lift distance and the free end must supply the sum. "
            "Verify with work: 200 N * 4 m = 800 J in, 800 N * 1 m = 800 "
            "J out - energy balances exactly. Fixed pulleys change "
            "direction only (MA = 1); movable pulleys give MA = 2 each; "
            "gun tackle, luff tackle, and double tackle are standard "
            "arrangements with MAs of 3, 4, and more. Real blocks lose a "
            "few percent per sheave to bearing and rope-bending friction, "
            "so riggers derate the theoretical MA - a 4-part tackle "
            "delivers closer to 3.6 in practice."
        ),
        "key_points": [
            "Effort is load divided by the number of rope segments supporting the moving block.",
            "A fixed pulley redirects only (MA 1); a movable pulley halves the effort (MA 2).",
            "Rope pulled equals segments times lift distance: 4 m of pull lifts 1 m on 4 parts.",
            "Work balances: effort times pull distance equals load times lift.",
            "Each sheave costs a few percent to friction - derate theoretical MA in real rigging.",
        ],
        "requirements": [
            "Count supporting segments on the MOVING block only; fixed-anchor segments do not multiply.",
            "Divide the total suspended weight (load plus moving block) by the segment count.",
            "Multiply the lift distance by the segment count to get the required pull length.",
            "Verify work in equals work out as an energy sanity check.",
            "Apply a friction derate per sheave for real-world rigging plans.",
        ],
        "standards": [
            "Pulley mechanical advantage by supporting-segment count, per Giancoli, 8th ed.",
            "Block-and-tackle arrangements per standard rigging references (Machinery Handbook tradition).",
            "Work-energy verification per Halliday, Resnick and Walker, 12th ed.",
        ],
        "citations": [CIT_GIANCOLI, CIT_HALLIDAY, CIT_CUTNELL],
        "sig_lens": (
            "The Signature read: the pulley is the Signature teamwork - "
            "one rope, many hands, the heavy promise shared until it "
            "feels light. The Method counts its segments honestly: every "
            "strand that shoulders the load earns its share of the pull, "
            "and no strand is asked to carry alone."
        ),
    },
    {
        "key": "wedge_screw",
        "name": "The Wedge and the Screw: Inclined Planes in Disguise",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The wedge and the screw are inclined planes in disguise: the "
            "wedge is two inclined planes back to back, driven forward to "
            "split things apart sideways, and the screw is an inclined "
            "plane wrapped around a cylinder, turning rotation into "
            "forward drive. A wedge 0.20 meters long and 0.04 meters "
            "thick at the back multiplies force by 5 - drive it with 200 "
            "newtons and the sides feel 1000 newtons of splitting force, "
            "which is why axes, chisels, nails, and doorstops all work. "
            "The screw mechanical advantage is the circumference the "
            "handle sweeps divided by the thread pitch: a 0.15-meter "
            "handle turning a 2-millimeter pitch gives MA = 2*pi*0.15 / "
            "0.002 = 471 - one newton at the handle becomes 471 newtons "
            "of clamping force, the reason bolts hold the world together. "
            "Both machines trade enormous distance for enormous force: "
            "the screw handle travels nearly half a kilometer of circle "
            "to advance one thread."
        ),
        "how_it_works": (
            "For the wedge, MA is length over thickness: 0.20/0.04 = 5, "
            "with the splitting force normal to each face. Drive the thin "
            "edge forward and the faces push outward with MA times the "
            "driving force - minus friction, which is considerable on "
            "wedge faces and also what keeps nails from backing out. For "
            "the screw, one full turn advances the thread by exactly one "
            "pitch, while the hand travels the handle circumference: MA = "
            "2*pi*r_handle / pitch. With r = 0.15 m and pitch 0.002 m, MA "
            "= 471.24 - a 20 N hand force becomes about 9425 N of "
            "clamping force. Check the distance: 471 turns of the handle "
            "circle per unit advance - the force multiplier and the "
            "distance divisor are the same number, so work balances. "
            "Thread friction makes screws self-locking (they do not spin "
            "back under load), which is a feature for fasteners and a "
            "cost in efficiency."
        ),
        "key_points": [
            "The wedge is a doubled inclined plane: MA is length over back thickness (here 5).",
            "The screw is a wrapped inclined plane: MA is handle circumference over thread pitch (here ~471).",
            "Both trade huge distances for huge forces - the screw handle sweeps hundreds of turns per advance.",
            "Wedge faces deliver splitting force normal to each face; friction on the faces is significant.",
            "Thread friction makes screws self-locking: they hold without spinning back under load.",
        ],
        "requirements": [
            "Compute wedge MA as length over maximum thickness; resolve the output normal to the faces.",
            "Compute screw MA as 2*pi*handle-radius over pitch with consistent length units.",
            "Verify the distance trade: handle travel per advance equals MA times the advance.",
            "Account for face/thread friction - it dominates wedge efficiency and gives screws their locking.",
            "Respect pitch units: millimeters of pitch against meters of handle radius need conversion first.",
        ],
        "standards": [
            "Wedge and screw as inclined-plane derivatives per Cutnell and Johnson, 12th ed.",
            "Screw mechanical advantage per the Machinery Handbook thread mechanics tradition.",
            "Simple-machine taxonomy per Hewitt, Conceptual Physics, 13th ed.",
        ],
        "citations": [CIT_CUTNELL, CIT_HEWITT, CIT_GIANCOLI],
        "sig_lens": (
            "The Signature read: the wedge is the Signature focus - the "
            "long gentle plane folded double until its patience becomes "
            "splitting power - and the screw is the Signature promise "
            "that holds: turn by turn, thread by thread, until 471 to 1 "
            "says the joint will never part. The Method fastens what it "
            "builds and splits only what must be split."
        ),
    },
    {
        "key": "mech_advantage",
        "name": "Mechanical Advantage: The Machine Multiplier",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Mechanical advantage is the number that rates every machine: "
            "output force divided by input force, the factor by which the "
            "machine multiplies your effort. A machine that turns 150 "
            "newtons of input into 600 newtons of output has MA = 4 - "
            "the same 4 you get from a 2-meter/0.5-meter lever or a 4-part "
            "pulley tackle. The ideal mechanical advantage (IMA) comes "
            "from geometry alone - arm ratios, rope counts, radii - while "
            "the actual mechanical advantage (AMA) is measured with "
            "friction included, and AMA never exceeds IMA. Efficiency "
            "ties them together: efficiency = work out / work in = AMA / "
            "IMA, so a machine delivering 240 J from 300 J input runs at "
            "80 percent. No machine beats MA = effort-distance over load-"
            "distance in the ideal case, and no real machine reaches its "
            "ideal - the gap is friction, and the gap is always honest."
        ),
        "how_it_works": (
            "Compute IMA from the machine geometry: for levers, effort-"
            "arm over load-arm; for pulleys, the supporting segment "
            "count; for the wheel and axle, R over r; for the screw, "
            "handle circumference over pitch. Measure AMA as output force "
            "over input force in real operation: 600/150 = 4.0 here. "
            "Efficiency is the work ratio: with 2 m of input travel at "
            "150 N (300 J in) producing 0.4 m of output travel at 600 N "
            "(240 J out), efficiency = 240/300 = 80%. Note the identity: "
            "AMA/IMA = 4.0/5.0 = 0.80 - the same 80 percent, since IMA = "
            "2/0.4 = 5 from the distances. Design rule: pick IMA about "
            "25 percent above the needed AMA to leave room for friction, "
            "wear, and imperfect loading - machines rated exactly at "
            "their need have no margin for reality."
        ),
        "key_points": [
            "MA is output force over input force - the machine force multiplier.",
            "IMA comes from geometry; AMA is measured with friction; AMA never exceeds IMA.",
            "Efficiency = work out / work in = AMA / IMA.",
            "Ideal MA also equals input distance over output distance - the distance trade, quantified.",
            "Design with margin: IMA roughly 25 percent above the required AMA covers friction and wear.",
        ],
        "requirements": [
            "Derive IMA from geometry (arms, segments, radii, pitch) before measuring anything.",
            "Measure AMA as real output force over real input force under load.",
            "Compute efficiency from the work ratio with measured distances, not assumed ones.",
            "Check AMA/IMA agreement as a consistency test on the measurements.",
            "Size IMA with margin above the needed AMA; never design exactly at the requirement.",
        ],
        "standards": [
            "Mechanical advantage and efficiency definitions per Giancoli, 8th ed.",
            "IMA/AMA distinction per Cutnell and Johnson, 12th ed.",
            "Work-based efficiency per Halliday, Resnick and Walker, 12th ed.",
        ],
        "citations": [CIT_GIANCOLI, CIT_CUTNELL, CIT_HALLIDAY],
        "sig_lens": (
            "The Signature read: mechanical advantage is the Signature "
            "measure of leverage - how much the world multiplies an honest "
            "effort, and how much friction takes its cut. The Method "
            "designs with margin, measures what is real, and never "
            "promises the ideal while delivering the actual."
        ),
    },
    {
        "key": "work",
        "name": "Work: Force Through Distance",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Work is force applied through a distance: W = F*d*cos(theta), "
            "where theta is the angle between the force and the "
            "displacement. Push with 200 newtons over 15 meters in the "
            "direction of motion and you do 3000 joules of work; push at "
            "60 degrees to the motion with 100 newtons over 10 meters and "
            "only the along-motion component counts, giving 100*10*0.5 = "
            "500 joules. The joule - one newton-meter - is the SI unit, "
            "and it is also the unit of energy, because work is energy "
            "transferred by a force. Forces perpendicular to motion do no "
            "work: the normal force on a rolling cart, gravity on a "
            "satellite in circular orbit, the tension on a whirling ball - "
            "all zero work, all motion unchanged in energy. Negative work "
            "is real too: friction opposing motion does negative work, "
            "draining energy as heat. The work-energy theorem ties it "
            "together: the net work on an object equals its change in "
            "kinetic energy."
        ),
        "how_it_works": (
            "Resolve the force along the displacement, multiply by the "
            "distance: W = F_parallel * d. Straight push: 200*15 = 3000 "
            "J. Angled push: 100*cos(60 deg)*10 = 50*10 = 500 J. For "
            "varying forces, work is the area under the force-versus-"
            "distance curve - the spring integral giving (1/2)kx squared "
            "is the classic case. Add the work of every force for the net "
            "work, then apply the work-energy theorem: net work = change "
            "in (1/2)mv squared. That is how stopping distances are "
            "computed: friction force times stopping distance equals the "
            "initial kinetic energy, so doubling speed quadruples the "
            "stopping distance. Sign discipline matters: work done BY the "
            "object or against the motion is negative; work done ON it "
            "along its motion is positive."
        ),
        "key_points": [
            "Work is force through distance along the motion: W = F*d*cos(theta), in joules.",
            "Only the force component parallel to displacement does work; perpendicular forces do zero work.",
            "The joule is the newton-meter - and the energy unit, because work is transferred energy.",
            "Net work equals change in kinetic energy: the work-energy theorem.",
            "Negative work (friction, braking) removes energy; positive work adds it.",
        ],
        "requirements": [
            "Resolve each force along the displacement before multiplying - angle matters.",
            "Use the net work (sum over all forces) in the work-energy theorem.",
            "Keep work in joules; verify force in newtons and distance in meters.",
            "Assign signs honestly: with-the-motion positive, against it negative, perpendicular zero.",
            "For varying forces, integrate or use the area under the F-d curve.",
        ],
        "standards": [
            "Work definition W = F dot d per ISO 80000-4:2019.",
            "Work-energy theorem per Young and Freedman, 15th ed.",
            "Joule as the SI unit of work and energy (SI Brochure, 9th ed.).",
        ],
        "citations": [CIT_ISO4, CIT_YOUNG, CIT_BIPM],
        "sig_lens": (
            "The Signature read: work is the Signature ledger of effort - "
            "force times distance, receipted in joules, with every angle "
            "accounted and every perpendicular free-rider struck from the "
            "books. The Method pays for work done and only for work done: "
            "no credit for pushing sideways, no debit forgotten against "
            "the motion."
        ),
    },
    {
        "key": "energy",
        "name": "Energy: The Capacity to Do Work",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Energy is the capacity to do work, and it comes in forms that "
            "convert into each other while the total stays constant. "
            "Kinetic energy - the energy of motion - is (1/2)mv squared: "
            "a 2-kilogram object at 10 m/s carries exactly 100 joules. "
            "Gravitational potential energy - the energy of position - is "
            "mgh: the same 2 kilograms held 5 meters up stores 2*9.81*5 = "
            "98.1 joules, ready to become motion on release. Drop it and "
            "the books balance: 98.1 J of potential becomes kinetic (minus "
            "a whisper of air drag), totaling 198.1 J in the system at the "
            "start. Elastic potential ((1/2)kx squared), chemical energy "
            "in fuels and batteries, thermal energy in hot matter, and "
            "mass itself (E = mc squared) complete the family. "
            "Conservation of energy is the deepest accounting rule in "
            "physics: energy is never created or destroyed, only "
            "transformed - and every machine, from levers to power plants, "
            "is an energy transformer with the books balanced."
        ),
        "how_it_works": (
            "Track each form with its formula: KE = 0.5*m*v^2, "
            "gravitational PE = m*g*h (h measured from an agreed zero), "
            "spring PE = 0.5*k*x^2. For the 2 kg example: KE = 0.5*2*100 "
            "= 100 J; PE = 2*9.81*5 = 98.1 J; system total 198.1 J. "
            "Write the conservation equation: total before = total after, "
            "including thermal energy when friction acts - the missing "
            "mechanical energy is never missing, it heated something. "
            "Solve for the unknown: drop the mass from 5 m and impact "
            "speed comes from 0.5*m*v^2 = m*g*h, giving v = sqrt(2*9.81*5) "
            "= 9.90 m/s - mass cancels, so all objects hit at the same "
            "speed in vacuum. Efficiency is useful energy out over total "
            "energy in; the rest is heat, noise, and the honest cost of "
            "transformation."
        ),
        "key_points": [
            "Energy is the capacity to do work; the joule is its unit.",
            "Kinetic (1/2 mv^2) and potential (mgh, 1/2 kx^2) convert into each other with the total conserved.",
            "Conservation of energy: never created or destroyed, only transformed - friction turns it to heat.",
            "Free-fall speed from height h is sqrt(2gh), independent of mass.",
            "Every machine is an energy transformer; efficiency is useful energy out over total in.",
        ],
        "requirements": [
            "List every energy form present before writing the conservation equation.",
            "Fix the zero of potential energy explicitly - only differences matter.",
            "Include thermal energy when friction or drag acts; the books must balance.",
            "Use conservation to solve for unknowns (speeds, heights, compressions) directly.",
            "Report efficiency as useful output over total input, with the losses named.",
        ],
        "standards": [
            "Energy forms and conservation per Halliday, Resnick and Walker, 12th ed.",
            "Potential energy conventions per Young and Freedman, 15th ed.",
            "Joule as SI energy unit (SI Brochure, 9th ed.).",
        ],
        "citations": [CIT_HALLIDAY, CIT_YOUNG, CIT_BIPM],
        "sig_lens": (
            "The Signature read: energy is the Signature treasury - "
            "counted in joules, never printed and never burned, only "
            "moved from vault to vault. The Method audits the treasury "
            "continuously: motion, height, spring, and heat all entered, "
            "the total unchanging, because a treasury that leaks is not "
            "a treasury."
        ),
    },
    {
        "key": "power",
        "name": "Power: Work Over Time",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Power is the rate of doing work: P = W/t, energy per unit "
            "time, measured in watts. Doing 3000 joules of work in 10 "
            "seconds is 300 watts - about what a strong cyclist sustains - "
            "while doing the same work in 1 second would take 3000 watts. "
            "The same work at different speeds is the difference between "
            "a crane and a rocket: both may lift the same load to the "
            "same height, but the faster one needs the bigger power "
            "plant. Power also equals force times velocity (P = F*v) for "
            "steady motion: pushing with 200 N at 1.5 m/s is 300 W, the "
            "same 300 W as the work-over-time figure - two faces of one "
            "quantity. A watt is one joule per second; a kilowatt is 1000 "
            "W; a horsepower is 746 W, so 300 W is about 0.40 hp. "
            "Electricity bills charge for energy (kilowatt-hours), not "
            "power - power is how fast you spend it, energy is how much "
            "you spent."
        ),
        "how_it_works": (
            "Divide work by time for average power: 3000 J / 10 s = 300 "
            "W. For steady pushing, multiply force by velocity: 200 N * "
            "1.5 m/s = 300 W - identical, as it must be, since W = F*d "
            "and d/t = v. Convert to horsepower by dividing by 745.7: "
            "300/745.7 = 0.4023 hp. Size motors and engines by the "
            "maximum sustained power the task demands: lifting 490.5 N "
            "(50 kg) at 2 m/s needs 981 W before losses - a 1 kW motor "
            "with margin, not a 500 W one. For accelerating loads, peak "
            "power exceeds the average: compute P = F*v at the highest "
            "force-velocity product in the cycle. Remember drag power "
            "grows as v cubed, so vehicle power requirements explode "
            "with speed - the power number, not the force number, sizes "
            "the engine."
        ),
        "key_points": [
            "Power is work over time: P = W/t, in watts (joules per second).",
            "For steady motion, P = F*v - force times velocity is the same power.",
            "Same work faster needs more power: the crane-versus-rocket distinction.",
            "1 horsepower = 745.7 W; 300 W is about 0.40 hp.",
            "Bills charge energy (kWh); power is the rate of spending it.",
        ],
        "requirements": [
            "Compute average power as work over elapsed time; use F*v for steady-motion power.",
            "Size power sources by the PEAK force-velocity product in the duty cycle, with margin.",
            "Convert watts to horsepower (divide by 745.7) when speaking engine ratings.",
            "Distinguish power (rate) from energy (total) in every specification and bill.",
            "Include the v-cubed drag power in any vehicle power budget.",
        ],
        "standards": [
            "Power P = dW/dt, watt as SI unit (SI Brochure, 9th ed.).",
            "P = F dot v for mechanical power per ISO 80000-4:2019.",
            "Horsepower conversion 1 hp = 745.7 W per NIST SP 811.",
        ],
        "citations": [CIT_BIPM, CIT_ISO4, CIT_NIST811],
        "sig_lens": (
            "The Signature read: power is the Signature pace of spending - "
            "how fast the treasury pays out its joules. The Method spends "
            "at the pace the task demands, sizes the engine for the peak "
            "rather than the average, and never confuses the rate of "
            "spending with the fortune spent."
        ),
    },
    {
        "key": "torque",
        "name": "Torque and Rotational Equilibrium",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Torque is the rotational equivalent of force: the twist that "
            "changes spinning motion, tau = r*F*sin(theta), where r is the "
            "lever arm from the pivot and theta the angle between the arm "
            "and the force. Push with 80 N at the end of a 0.5-meter "
            "wrench, perpendicular to it, and the torque is 40 N m - the "
            "unit newton-meter, same letters as the joule but a different "
            "quantity, twist rather than energy. Maximum torque comes at "
            "90 degrees; push straight along the wrench (theta = 0) and "
            "the torque is zero no matter how hard you shove. Rotational "
            "equilibrium - the seesaw balanced, the bridge unmoving - "
            "needs zero net torque: clockwise twists must exactly cancel "
            "counterclockwise twists. Put +40 N m counterclockwise on one "
            "side and -40 N m clockwise on the other and the net is zero: "
            "no angular acceleration, the system holds its attitude. "
            "Torque is why doorknobs sit far from hinges, why lug nuts "
            "need long wrenches, and why tightrope walkers carry long "
            "poles."
        ),
        "how_it_works": (
            "Compute each torque as r*F*sin(theta) with a sign convention "
            "- counterclockwise positive is standard - then sum: net "
            "zero means rotational equilibrium. The wrench: 0.5*80*"
            "sin(90 deg) = 40 N m. Balance it with an equal opposite "
            "twist: -40 N m from a second force, and the shaft feels no "
            "net twist. For extended bodies in full equilibrium, demand "
            "both zero net force AND zero net torque - a bridge needs "
            "both, and checking only forces misses tipping failures. "
            "Torque also drives rotation via the rotational second law, "
            "net-tau = I*alpha, where I is the moment of inertia (the "
            "rotational mass) and alpha the angular acceleration. "
            "Stability follows from torque too: a tall load tips when its "
            "weight line falls outside its base, because gravity then "
            "applies a toppling torque instead of a restoring one."
        ),
        "key_points": [
            "Torque tau = r*F*sin(theta): twist from a force, in newton-meters, max at 90 degrees.",
            "Rotational equilibrium needs zero net torque: clockwise and counterclockwise twists cancel.",
            "Full static equilibrium needs zero net force AND zero net torque - check both.",
            "The rotational second law is net-tau = I*alpha, with moment of inertia as rotational mass.",
            "Tipping happens when the weight line leaves the base: gravity torque changes from restoring to toppling.",
        ],
        "requirements": [
            "Measure r from the pivot to the force application point, perpendicular distance for angled forces.",
            "Apply sin(theta) for the angle between arm and force - zero along the arm.",
            "Sum torques with a consistent sign convention; demand zero for equilibrium.",
            "Verify full equilibrium with both force and torque balances on every structure.",
            "Check tip-over by tracking the weight line against the support base.",
        ],
        "standards": [
            "Torque definition per ISO 80000-4:2019; newton-meter as the torque unit.",
            "Equilibrium conditions (net F = 0, net tau = 0) per Young and Freedman, 15th ed.",
            "Rotational dynamics per Knight, 5th ed.",
        ],
        "citations": [CIT_ISO4, CIT_YOUNG, CIT_KNIGHT],
        "sig_lens": (
            "The Signature read: torque is the Signature twist - the "
            "promise applied at a distance from the pivot, turning the "
            "world instead of shoving it. The Method balances its twists "
            "the way it balances its books: clockwise against counter, "
            "until the net is zero and the structure stands."
        ),
    },
    {
        "key": "projectile",
        "name": "Projectile Motion: Two Motions at Once",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Projectile motion is two independent motions sharing one "
            "clock: horizontal velocity coasts unchanged (no horizontal "
            "forces, ignoring air) while vertical velocity grows downward "
            "at g. Launch at 20 m/s at 45 degrees and the horizontal part "
            "stays 14.14 m/s the whole flight while the vertical part "
            "starts at +14.14 m/s, slows to zero at the peak, and falls "
            "back - the combination draws the perfect parabola. The range "
            "is v0 squared times sin(2*theta) over g: 400/9.81 = 40.77 "
            "meters here, the maximum possible at 45 degrees. Peak height "
            "is (v0*sin(theta)) squared over 2g = 10.19 m, and flight time "
            "is 2*v0*sin(theta)/g = 2.883 s. Galileo insight was the "
            "independence: the horizontal motion never knows the vertical "
            "is falling, which is why a bullet fired level and a bullet "
            "dropped from the same height hit the ground together "
            "(in vacuum). Sports, artillery, and water fountains all run "
            "this arithmetic."
        ),
        "how_it_works": (
            "Split the launch velocity: vx = v0*cos(theta), vy = "
            "v0*sin(theta) - here 14.1421 m/s each. The x-position grows "
            "linearly (x = vx*t); the y-position follows y = vy*t - "
            "0.5*g*t^2. Range comes from the flight time: t = "
            "2*vy/g = 2.8829 s, so R = vx*t = 40.7747 m - matching "
            "v0^2*sin(90 deg)/g = 400/9.81. Peak height: vy^2/(2g) = "
            "200/19.62 = 10.1937 m. For targets at a given range, two "
            "launch angles work (a low flat arc and a high lob) except "
            "at maximum range where they merge at 45 degrees. Add air "
            "drag for real projectiles: it shortens range, lowers the "
            "optimal angle below 45 degrees, and makes the descent "
            "steeper than the ascent - the vacuum parabola is the ideal "
            "the real arc approximates."
        ),
        "key_points": [
            "Horizontal motion coasts at constant vx; vertical motion accelerates downward at g - independent, sharing one clock.",
            "Range is v0^2*sin(2 theta)/g, maximum at 45 degrees in vacuum.",
            "Peak height is (v0*sin theta)^2/(2g); flight time is 2*v0*sin theta/g.",
            "Fired-level and dropped-from-rest objects hit the ground together - Galileo independence.",
            "Air drag shortens range, drops the optimal angle below 45 deg, and steepens the descent.",
        ],
        "requirements": [
            "Resolve the launch velocity into vx and vy before any further step.",
            "Treat x as uniform motion and y as constant-acceleration motion - never mix the rules.",
            "Compute flight time from the vertical motion, then range from vx times that time.",
            "Verify 45 degrees as the vacuum optimum; adjust downward when drag is significant.",
            "State the vacuum assumption; real trajectories need the drag correction.",
        ],
        "standards": [
            "Projectile kinematics per Halliday, Resnick and Walker, 12th ed.",
            "Independence of perpendicular motions per Galileo tradition, in Young and Freedman, 15th ed.",
            "Range/height/time formulas per Serway and Jewett, 10th ed.",
        ],
        "citations": [CIT_HALLIDAY, CIT_YOUNG, CIT_SERWAY],
        "sig_lens": (
            "The Signature read: the projectile is the Signature promise "
            "in flight - coasting on its word horizontally while gravity "
            "collects vertically, two honest motions keeping one clock. "
            "The Method launches at the true angle, accounts for the air, "
            "and lands its promises where it aimed."
        ),
    },
    {
        "key": "collisions",
        "name": "Conservation of Momentum in Collisions",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "In collisions, total momentum is always conserved while "
            "kinetic energy may or may not be - and that split defines "
            "the collision types. Elastic collisions keep kinetic energy "
            "(billiard balls, nearly); inelastic collisions lose some to "
            "heat, sound, and deformation (most real crashes); perfectly "
            "inelastic collisions stick together and lose the maximum "
            "(a 2-kg lump at 3 m/s hitting a stationary 3-kg lump leaves "
            "both moving at 1.2 m/s). The momentum books always balance: "
            "before, 2*3 + 3*0 = 6 kg m/s; after, 5*1.2 = 6 kg m/s - "
            "conserved exactly. The energy books show the cost: 9 J of "
            "kinetic energy before, 3.6 J after, 5.4 J converted to heat "
            "and deformation. Crash engineers exploit this: crumple zones "
            "are designed to be inelastic, converting kinetic energy into "
            "deformation work over a long distance so the forces on "
            "passengers stay survivable - while momentum conservation "
            "sets the final velocity of the wreckage no matter how the "
            "crushing goes."
        ),
        "how_it_works": (
            "Write momentum conservation first: m1*v1 + m2*v2 = "
            "m1*v1p + m2*v2p (primes for after), as vectors in 2D. For "
            "the perfectly inelastic stick-together case the afters share "
            "one velocity: v = (2*3 + 3*0)/5 = 1.2 m/s. Then audit "
            "energy: KE_before = 0.5*2*9 = 9 J; KE_after = 0.5*5*1.44 = "
            "3.6 J; loss = 5.4 J to heat and deformation. For elastic "
            "collisions add the second equation - kinetic energy "
            "conserved - and solve the pair for both final velocities. "
            "In 2D (billiard balls scattering), conserve each momentum "
            "component separately. The center of mass moves at constant "
            "velocity through every collision regardless of type - a "
            "powerful check: compute it before and after, and it must "
            "match."
        ),
        "key_points": [
            "Total momentum is conserved in every collision; kinetic energy is conserved only in elastic ones.",
            "Perfectly inelastic (stick together) loses the maximum kinetic energy to heat and deformation.",
            "Crumple zones are engineered inelasticity: convert KE to deformation work over distance.",
            "Elastic collisions need both conservation equations to solve for the final velocities.",
            "The center of mass moves at constant velocity through any collision - the universal check.",
        ],
        "requirements": [
            "Write momentum conservation before anything else in every collision problem.",
            "Classify the collision (elastic, inelastic, perfectly inelastic) to know whether KE is conserved.",
            "Conserve each momentum component separately in two-dimensional collisions.",
            "Audit the kinetic energy before and after; name where the lost energy went.",
            "Check the center-of-mass velocity as an independent verification.",
        ],
        "standards": [
            "Collision classification and conservation laws per Young and Freedman, 15th ed.",
            "Perfectly inelastic analysis per Halliday, Resnick and Walker, 12th ed.",
            "Center-of-mass motion per Knight, 5th ed.",
        ],
        "citations": [CIT_YOUNG, CIT_HALLIDAY, CIT_KNIGHT],
        "sig_lens": (
            "The Signature read: the collision is the Signature "
            "settlement - momentum conserved to the last unit, energy "
            "converted at honest rates, the wreckage moving exactly as "
            "the books require. The Method settles every account: what "
            "goes in as motion comes out as motion or heat, and nothing "
            "vanishes."
        ),
    },
]
