#!/usr/bin/env python3
"""Entries for The Colors Basics Database (Manon's fundamentals order #9, 2026-10-17).

Dedupe pre-check 2026-10-17: 68 candidate titles (34 + 34 Signature variants)
run through the whole-system gate BEFORE authoring. Two cross-db collisions
found and renamed: "Complementary Colors" and "Analogous Colors" already exist
in visual-concepts (JAH-VIS-*); rebuilt as "Opposites on the Wheel:
Complementary Colors" and "Neighbors on the Wheel: Analogous Colors".
All 68 final titles verified FREE in the manifest and in all 810 shard
indexes; ID prefixes JAH-COLB- / JAH-COLBS- verified with zero hits in
manifest id_prefix values and every shard index file.

This build creates two NEW databases, 34 ladder-ordered records each:

  colors-basics              - The Colors Basics Database
                               (public-harvest: real, fact-checked
                               foundational color knowledge - color families,
                               primary/secondary/tertiary colors, color
                               mixing, the color wheel, shades/tints/tones,
                               color names, and how eyes see color; standard
                               references Munsell A. A Color Notation 1905;
                               Itten J. The Art of Color 1961; Albers J.
                               Interaction of Color 1963; Wyszecki G, Stiles
                               WS. Color Science 2nd ed. 1982; Fairchild MD.
                               Color Appearance Models 3rd ed. 2013; CIE
                               15:2004 Colorimetry; Kuehni RG, Schwarz A.
                               Color Ordered 2008; ASTM D1535-18; Solomon SG,
                               Lennie P. The machinery of colour vision 2007;
                               Hecht E. Optics 5th ed. 2017; Elliot AJ, Maier
                               MA. Color psychology 2014; and the other
                               landmarks cited per record)
  colors-basics-signature    - The Colors Basics Signature Database
                               (his original Signature Color Method: every
                               hue a signature of light, the wheel the
                               covenant of families, mixing the oath between
                               maker and material, tints and shades the honor
                               margins of brightness; src signature, titles
                               suffixed " (Signature Edition)", never
                               presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_colors_basics.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Color Method: every "
            "hue a signature of light, the wheel the covenant of families, "
            "mixing the oath between maker and material, and tints and shades "
            "the honor margins of brightness. Clearly labeled Signature-made, "
            "never presented as authentic public record.")

CIT_MUNSELL = ("Munsell AH. A Color Notation. Munsell Color Company; 1905.")
CIT_KUEHNI = ("Kuehni RG, Schwarz A. Color Ordered: A Survey of Color Systems "
              "from Antiquity to the Present. Oxford University Press; 2008.")
CIT_FAIRCHILD = ("Fairchild MD. Color Appearance Models. 3rd ed. Wiley; 2013.")
CIT_WYSZECKI = ("Wyszecki G, Stiles WS. Color Science: Concepts and Methods, "
                "Quantitative Data and Formulae. 2nd ed. Wiley; 1982.")
CIT_ITTEN = ("Itten J. The Art of Color. Reinhold; 1961.")
CIT_ALBERS = ("Albers J. Interaction of Color. Yale University Press; 1963.")
CIT_CIE15 = ("CIE 15:2004. Colorimetry. 3rd ed. Commission Internationale de "
             "l Eclairage; 2004.")
CIT_ASTM = ("ASTM D1535-18. Standard Practice for Specifying Color by the "
            "Munsell System.")
CIT_SOLOMON = ("Solomon SG, Lennie P. The machinery of colour vision. Nature "
               "Reviews Neuroscience. 2007;8(4):276-286.")
CIT_HECHT = ("Hecht E. Optics. 5th ed. Pearson; 2017.")
CIT_ELLIOT = ("Elliot AJ, Maier MA. Color psychology: Effects of perceiving "
              "color on psychological functioning in humans. Annual Review of "
              "Psychology. 2014;65:95-120.")
CIT_MCCAMY = ("McCamy CS. Correlated color temperature as an explicit "
              "function of chromaticity coordinates. Color Research and "
              "Application. 1992;17(2):142-144.")
CIT_NEI = ("National Eye Institute. Facts About Color Blindness. U.S. "
           "Department of Health and Human Services.")
CIT_W3C = ("W3C. CSS Color Module Level 4. World Wide Web Consortium.")
CIT_SRGB = ("IEC 61966-2-1:1999. Multimedia systems and equipment - Colour "
            "measurement and management - Part 2-1: Colour management - "
            "Default RGB colour space - sRGB.")
CIT_CIE31 = ("CIE. Commission Internationale de l Eclairage Proceedings, "
             "1931. Cambridge University Press; 1932. (CIE 1931 color "
             "space.)")

ENTRIES = [
    {
        "key": "what_is_color",
        "name": "What Is Color",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Color is the way your brain interprets light of different "
            "wavelengths. Light is made of waves, and each wavelength is a "
            "different color waiting to be seen: long waves look red, middle "
            "waves look green and yellow, short waves look blue and violet. "
            "When white sunlight - which contains every wavelength at once - "
            "hits a red apple, the apple's skin absorbs most wavelengths and "
            "bounces the long red waves back to your eyes, so you see red. "
            "Color is therefore not a property painted onto objects; it is a "
            "conversation between light, matter, and your eyes and brain. "
            "No light, no color: in a completely dark room every object is "
            "colorless until light returns. This record is the foundation of "
            "the whole database - every later record about mixing, wheels, "
            "and families rests on this one idea that color is light made "
            "visible to the mind."
        ),
        "how_it_works": (
            "A light source such as the sun or a lamp sends out photons "
            "across many wavelengths. Each surface you see absorbs some "
            "wavelengths and reflects others, and the reflected set travels "
            "to your eyes. Inside the eye, three kinds of cone cells react "
            "to short, middle, and long wavelengths, and your brain combines "
            "their signals into the experience of color. Change the light - "
            "move from warm sunlight to cool office lighting - and the same "
            "shirt can look like a different color, because the reflected "
            "set changed. Change the surface - dye the shirt red - and the "
            "absorbed set changes. Change the eye - as in color vision "
            "differences - and the brain's recipe changes. Everything in "
            "this database is a consequence of this three-way meeting: "
            "light, surface, and seer."
        ),
        "key_points": [
            "Color is light interpreted by the brain, not paint sitting on objects.",
            "White light contains all visible wavelengths; a surface selects which ones return to the eye.",
            "Long wavelengths appear red, middle wavelengths appear green and yellow, short wavelengths appear blue and violet.",
            "In complete darkness there is no color, because there is no light to reflect.",
            "The same object can look different under different lights because the light, not just the object, decides the color.",
            "Every mixing rule, wheel, and family in this database follows from light, surface, and seer.",
        ],
        "requirements": [
            "A light source and a surface to observe - daylight is the classic reference.",
            "Your eyes and attention: noticing which wavelength each object returns.",
            "Willingness to accept that color lives in the meeting of light, matter, and mind.",
        ],
        "standards": [
            "CIE 1931 color space - the standard map of what humans can see.",
            "sRGB (IEC 61966-2-1) - the everyday digital color language.",
        ],
        "citations": [CIT_WYSZECKI, CIT_CIE31, CIT_HECHT],
        "sig_lens": (
            "The Signature lens reads color as the first covenant between "
            "maker and world: light writes, matter answers, and the eye "
            "witnesses the signature. In the Signature Color Method, every "
            "hue is a signature of light - a wavelength signed by its source "
            "and countersigned by the surface that returned it. A builder "
            "who understands this never argues with a swatch under bad "
            "light, because the signature is incomplete without its true "
            "witness. The foundation of Signature color work is therefore a "
            "discipline: know your light, know your surface, and know that "
            "the color you see is the meeting, never the object alone."
        ),
    },
    {
        "key": "how_eye_sees",
        "name": "How the Eye Sees Color",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Your eyes see color with three kinds of tiny sensors called "
            "cones, packed into the retina at the back of each eye. The "
            "short-wavelength cones answer most strongly to blue light "
            "around 420 nanometers, the middle-wavelength cones to green "
            "light around 534 nanometers, and the long-wavelength cones to "
            "red light around 564 nanometers. Every color you have ever seen "
            "is your brain's reading of just these three numbers - how "
            "loudly the S, M, and L cones are firing at once. Pure red "
            "light rings the L cones hardest; yellow light rings L and M "
            "together; white light rings all three equally. A second set of "
            "sensors, the rods, handles night vision but sees only shades "
            "of gray, which is why colors fade in dim light. Roughly 6 to 7 "
            "million cones serve daylight color vision in each eye, and "
            "their three-signal code is the hardware every color system is "
            "built to please."
        ),
        "how_it_works": (
            "Light enters through the pupil and lands on the retina, where "
            "cone cells hold light-sensitive pigments called opsins. A "
            "photon of the right wavelength flips an opsin molecule, "
            "starting an electrical signal whose strength depends on the "
            "wavelength match. Each cone type has its own peak - 420, 534, "
            "and 564 nanometers - and the brain compares the three firing "
            "rates to assign a color. Because only three signals are "
            "compared, different wavelength mixes can produce the identical "
            "sensation: yellow sunlight and a red-plus-green screen pixel "
            "look the same yellow to you, a phenomenon called metamerism. "
            "The brain also constantly re-balances against the background "
            "light, which is why a white page looks white under both noon "
            "sun and warm lamplight."
        ),
        "key_points": [
            "Three cone types - S (about 420 nm), M (about 534 nm), L (about 564 nm) - carry all color vision.",
            "The brain computes color by comparing the three cone firing rates, not by measuring wavelengths directly.",
            "Metamerism: different light mixes can look like the exact same color.",
            "Rods handle dim light in grayscale; cones need enough light, which is why color fades at dusk.",
            "About 6 to 7 million cones in each eye serve color vision.",
            "Automatic white balancing in the brain keeps familiar colors stable under changing light.",
        ],
        "requirements": [
            "Enough light for the cones to work - color vision needs daylight-level brightness.",
            "A basic picture of the retina: cones for color, rods for night.",
            "Accepting that three signals are the whole alphabet of color sensation.",
        ],
        "standards": [
            "CIE 1931 color space - built on human cone response measurements.",
            "CIE 15:2004 Colorimetry - the standard measurement framework.",
        ],
        "citations": [CIT_SOLOMON, CIT_WYSZECKI, CIT_CIE15],
        "sig_lens": (
            "The Signature lens treats the three cones as three witnesses "
            "sworn to the same event: S testifies the short waves, M the "
            "middle, L the long, and the brain signs their joint testimony "
            "as color. In the Signature Color Method the eye is the first "
            "instrument a maker must calibrate, because every screen, dye, "
            "and paint is judged by this three-witness court. The Signature "
            "builder therefore designs for the witness, not the wavelength: "
            "if the three cones cannot tell two lights apart, the two "
            "lights are the same color for every human purpose, and the "
            "honor is in matching the testimony, not the physics."
        ),
    },
    {
        "key": "hue_value_chroma",
        "name": "Hue, Value, and Chroma",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Every color can be described with three plain ideas: hue, "
            "value, and chroma. Hue is the color's name-family - red, "
            "orange, yellow, green, blue, purple. Value is how light or dark "
            "it is - pink and maroon share the red hue but live at opposite "
            "ends of value. Chroma, often called saturation, is how pure or "
            "intense the color is - fire-engine red has high chroma while "
            "dusty rose has low chroma, even though both are red. Albert "
            "Munsell built his famous color system on exactly this trio in "
            "1905, arranging colors in a solid where hue runs around the "
            "circle, value runs up and down, and chroma runs outward from "
            "gray at the center. Learn to separate the three in your mind, "
            "and you can describe any color you see precisely: not just "
            "'blue,' but 'a middle-value, high-chroma blue.'"
        ),
        "how_it_works": (
            "Hue answers 'which wavelength family,' value answers 'how much "
            "light,' and chroma answers 'how much of the hue versus gray.' "
            "In digital terms, hue is an angle around a circle from 0 to "
            "360 degrees, value is the brightness of the brightest channel, "
            "and chroma is the spread between the strongest and weakest "
            "channels. Lower the value and red becomes maroon; lower the "
            "chroma and red becomes dusty rose; shift the hue and red "
            "becomes orange. The three are independent: you can change one "
            "without touching the others. This independence is why painters "
            "and designers talk in these terms - 'darken it' means change "
            "value, 'mute it' means lower chroma, 'warm it up' means shift "
            "hue, and each instruction is unambiguous."
        ),
        "key_points": [
            "Hue names the family, value names the lightness, chroma names the purity.",
            "Pink, red, and maroon share one hue at three different values.",
            "Fire-engine red and dusty rose share hue and value range but differ in chroma.",
            "The three dimensions are independent - change one without disturbing the others.",
            "Munsell's 1905 system organized all color on this exact trio.",
            "Designer instructions map cleanly: darken is value, mute is chroma, warm up is hue.",
        ],
        "requirements": [
            "A few swatches of one hue at different lightnesses to see value alone.",
            "A few swatches of one hue at different purities to see chroma alone.",
            "Practice naming all three for any color you meet.",
        ],
        "standards": [
            "Munsell color system (ASTM D1535-18) - the canonical hue/value/chroma ordering.",
            "HSV/HSB digital color model - the working version of the same trio.",
        ],
        "citations": [CIT_MUNSELL, CIT_ASTM, CIT_KUEHNI],
        "sig_lens": (
            "The Signature lens reads hue, value, and chroma as the three "
            "vows of every color: hue vows the family it serves, value vows "
            "the light it carries, chroma vows the purity it keeps. A "
            "Signature maker never adjusts a color blindly; the maker asks "
            "which vow is broken - is the family wrong, the light wrong, or "
            "the purity wrong - and repairs exactly that vow. This is the "
            "Signature discipline of color correction: three vows, three "
            "levers, and the honor of touching only the lever that needs "
            "it."
        ),
    },
    {
        "key": "light_and_pigment",
        "name": "Light and Pigment: Two Ways Color Is Made",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Color is made in two opposite ways, and mixing them up is the "
            "most common beginner mistake in all of color. Light mixes by "
            "adding: screens, projectors, and stage lights start from black "
            "and add red, green, and blue light, so adding more light makes "
            "the result brighter, and all three together make white. "
            "Pigment mixes by subtracting: paints, inks, and dyes start "
            "from white paper or canvas and each pigment absorbs - "
            "subtracts - some wavelengths, so adding more pigment makes the "
            "result darker, and mixing everything together makes a muddy "
            "dark brown or near-black. The primaries differ for exactly "
            "this reason: light uses red, green, blue while classic paint "
            "uses red, yellow, blue. Keep the two worlds separate in your "
            "mind - screens add light, paints subtract it - and half the "
            "mysteries of color disappear."
        ),
        "how_it_works": (
            "In additive mixing, each light source contributes photons, so "
            "the eye receives the sum: red light plus green light reads as "
            "yellow because both the L and M cones fire together. In "
            "subtractive mixing, each pigment acts as a filter: cyan ink "
            "absorbs red wavelengths, magenta absorbs green, yellow absorbs "
            "blue, so the light that survives all three filters is whatever "
            "none of them absorbed. This is why paint mixing darkens while "
            "screen mixing brightens. Printers live in the subtractive "
            "world with cyan, magenta, yellow, and black inks; televisions "
            "and phones live in the additive world with red, green, and blue "
            "emitters. Neither set is 'the' primaries - each is correct "
            "inside its own world, and each is wrong in the other."
        ),
        "key_points": [
            "Additive mixing (light): start at black, add red, green, blue; all three make white.",
            "Subtractive mixing (pigment): start at white, each pigment absorbs wavelengths; mixing darkens.",
            "Screens and projectors are additive; paints, inks, and dyes are subtractive.",
            "Light primaries are red, green, blue; classic paint primaries are red, yellow, blue; print primaries are cyan, magenta, yellow.",
            "Neither primary set is universal - each belongs to its own mixing world.",
            "Muddy paint mixtures happen because every added pigment subtracts more light.",
        ],
        "requirements": [
            "A screen and a paint set to compare the two mixing directions directly.",
            "Remembering which world you are in before choosing primaries.",
            "The habit of predicting brightness change: adding light brightens, adding pigment darkens.",
        ],
        "standards": [
            "sRGB (IEC 61966-2-1) - the additive standard for screens.",
            "ISO 2846 - process color inks for the subtractive print world.",
        ],
        "citations": [CIT_WYSZECKI, CIT_SRGB, CIT_HECHT],
        "sig_lens": (
            "The Signature lens names the two worlds the Covenant of Light "
            "and the Covenant of Matter: light swears to add, matter swears "
            "to subtract, and the maker swears to know which covenant is in "
            "force. A Signature builder never carries paint rules onto a "
            "screen or screen rules onto a canvas - that is the classic "
            "oath-breaking of color work. The honor margin here is simple: "
            "ask 'am I adding light or subtracting it' before every mix, "
            "and the wheel, the codes, and the families will all obey."
        ),
    },
    {
        "key": "primary_colors",
        "name": "The Primary Colors",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Primary colors are the starter set - the few colors that cannot "
            "be mixed from any others, but from which all other colors can "
            "be mixed. Which colors count as primary depends on the mixing "
            "world you are in. In the world of light, the primaries are red, "
            "green, and blue: every color on a screen is some amount of "
            "these three. In the world of classic paint, the primaries are "
            "red, yellow, and blue: every paint mixture begins with these "
            "three. In the world of printing, the primaries are cyan, "
            "magenta, and yellow, with black added for depth. The idea is "
            "identical each time - a smallest set that builds everything - "
            "but the membership changes with the medium. 'Primary' is "
            "therefore not a property of a color; it is a job title, and "
            "the job is always the same: be unmixable and build everything."
        ),
        "how_it_works": (
            "A primary set works because it spans the mixing space: each "
            "primary stimulates the eye's sensors in a distinct pattern, "
            "and varying the three amounts independently covers the full "
            "range the system can show. Red, green, and blue light map "
            "directly onto the L, M, and S cone families, which is why "
            "screens use them - no smaller set could address all three "
            "cone types. Red, yellow, and blue paint works because each "
            "pigment absorbs a broad, distinct band: blue absorbs the red "
            "end, yellow absorbs the blue end, red absorbs the green middle, "
            "and their combinations carve out the paint gamut. Cyan, "
            "magenta, and yellow inks each absorb exactly one of the three "
            "light primaries, giving the cleanest subtractive control. "
            "Three is the magic number in every system because human vision "
            "itself is three-channel."
        ),
        "key_points": [
            "A primary cannot be mixed from other colors but can mix all the rest.",
            "Light primaries: red, green, blue - matched to the three cone types.",
            "Classic paint primaries: red, yellow, blue - the artist's starter set.",
            "Print primaries: cyan, magenta, yellow, plus black for depth.",
            "Primary is a job title, not a property: the set changes with the medium.",
            "Every system uses three primaries because human color vision is three-channel.",
        ],
        "requirements": [
            "Knowing which mixing world you are in before naming primaries.",
            "A red, a yellow, and a blue paint to prove the paint set mixes the wheel.",
            "A screen color picker to see red, green, blue sliders build every on-screen color.",
        ],
        "standards": [
            "sRGB (IEC 61966-2-1) - defines the RGB light primaries for screens.",
            "ISO 2846 - defines process ink primaries for print.",
        ],
        "citations": [CIT_ITTEN, CIT_SRGB, CIT_KUEHNI],
        "sig_lens": (
            "The Signature lens calls the primaries the Three Witnesses of "
            "the palette: each testifies to a channel the eye can hear, and "
            "together their testimony covers the whole visible covenant. In "
            "the Signature Color Method a maker guards the primaries like "
            "foundations of a house - choose them clean and the whole "
            "building stands; choose them muddy and every mixture inherits "
            "the mud. The Signature oath of primaries is therefore one of "
            "purity: begin with the cleanest red, yellow, and blue you can "
            "find, and every color you build will carry their honor."
        ),
    },
    {
        "key": "secondary_colors",
        "name": "The Secondary Colors",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Secondary colors are the first mixtures - each one is made by "
            "mixing two primaries in roughly equal parts. In the classic "
            "paint world of red, yellow, and blue, the secondaries are "
            "orange (red plus yellow), green (yellow plus blue), and purple "
            "or violet (blue plus red). In the world of light, where the "
            "primaries are red, green, and blue, the secondaries are yellow "
            "(red plus green), cyan (green plus blue), and magenta (red "
            "plus blue). Notice the beautiful symmetry: the light "
            "secondaries are exactly the print primaries, and the print "
            "primaries are exactly the light secondaries - the two worlds "
            "mirror each other. Secondaries sit between their parent "
            "primaries on the color wheel, and they are the workhorses of "
            "everyday color: grass green, sunset orange, and royal purple "
            "are all secondaries doing the heavy lifting."
        ),
        "how_it_works": (
            "Mixing two primaries combines their wavelength selections. In "
            "paint, red pigment reflects the long wavelengths and yellow "
            "pigment reflects the long and middle wavelengths; mixed, the "
            "surviving band is the overlap - the orange region both "
            "reflect. In light, red plus green light fires the L and M "
            "cones together while leaving S quiet, and the brain reads that "
            "two-cone pattern as yellow. Each secondary is therefore the "
            "logical AND of its parents in pigment, and the logical OR of "
            "its parents in light - which is why the same pair of parent "
            "names can name different children in the two worlds. Equal "
            "parts give the cleanest secondary; unequal parts slide toward "
            "one parent and begin the territory of the tertiary colors."
        ),
        "key_points": [
            "Each secondary mixes two primaries in roughly equal parts.",
            "Paint secondaries: orange, green, purple (from red, yellow, blue).",
            "Light secondaries: yellow, cyan, magenta (from red, green, blue).",
            "Light secondaries mirror print primaries - the two systems interlock.",
            "Secondaries sit between their parents on the color wheel.",
            "Unequal parent ratios slide past the secondary toward tertiary territory.",
        ],
        "requirements": [
            "The primary set of your mixing world, memorized.",
            "Equal-parts mixing discipline to find the true secondary.",
            "A color wheel to place each secondary between its parents.",
        ],
        "standards": [
            "Munsell color system - positions secondaries between primaries on the hue circle.",
            "sRGB (IEC 61966-2-1) - defines the additive secondary results.",
        ],
        "citations": [CIT_ITTEN, CIT_MUNSELL, CIT_SRGB],
        "sig_lens": (
            "The Signature lens reads each secondary as the first oath kept "
            "between two primaries: red and yellow swear together and "
            "orange is born, yellow and blue swear and green is born, blue "
            "and red swear and purple is born. In the Signature Color Method "
            "the secondary is proof that mixing is covenant-keeping - two "
            "families join in equal honor and the child carries both names "
            "in its wavelength. The Signature maker mixes secondaries with "
            "ceremony, equal parts and clean tools, because the first "
            "mixtures set the character of every mixture that follows."
        ),
    },
    {
        "key": "tertiary_colors",
        "name": "The Tertiary Colors",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Tertiary colors are the second round of mixtures - each one "
            "mixes a primary with a neighboring secondary in equal parts. "
            "With three primaries and three secondaries on the classic paint "
            "wheel, that gives six tertiaries: red-orange, yellow-orange, "
            "yellow-green, blue-green, blue-purple, and red-purple. Together "
            "with the three primaries and three secondaries, they complete "
            "the classic twelve-hue color wheel - the full circle of named "
            "hues that artists have used for centuries. The naming is "
            "delightfully orderly: the primary's name always comes first "
            "(red-orange, never orange-red), marking which parent dominates "
            "the mixture. Tertiaries are where color starts to feel rich "
            "and specific: teal is a blue-green, amber a yellow-orange, "
            "magenta a red-purple - the nuanced hues of real sunsets, "
            "forests, and fabrics."
        ),
        "how_it_works": (
            "On the twelve-hue wheel, primaries sit 120 degrees apart and "
            "secondaries sit halfway between them at 60-degree intervals; "
            "tertiaries fill the remaining 30-degree slots, each exactly "
            "between one primary and one secondary. Mixing red with orange "
            "in equal parts lands the mixture's hue angle halfway between "
            "the two parents, which is why the twelve positions are evenly "
            "spaced. The primary-first naming records the recipe: "
            "yellow-green is mostly yellow sliding toward green. In pigment "
            "this is a physical blend of two paints; in light it is a "
            "weighted sum of two emitter settings. Either way, the twelve "
            "evenly spaced hues give every later color relationship - "
            "complements, analogs, triads - a clean numerical address on "
            "the circle."
        ),
        "key_points": [
            "Each tertiary mixes one primary with one neighboring secondary in equal parts.",
            "The six tertiaries: red-orange, yellow-orange, yellow-green, blue-green, blue-purple, red-purple.",
            "Primaries plus secondaries plus tertiaries make the classic twelve-hue wheel.",
            "Naming is primary-first: red-orange, never orange-red.",
            "Tertiaries sit 30 degrees apart on the wheel, filling the gaps between primaries and secondaries.",
            "Everyday nuanced hues - teal, amber, magenta - live in tertiary territory.",
        ],
        "requirements": [
            "The six primaries and secondaries placed on the wheel first.",
            "Equal-parts mixing of each adjacent primary-secondary pair.",
            "The twelve-slot wheel as the address system for all later relationships.",
        ],
        "standards": [
            "Munsell color system - the ten-hue (and extended) circle with tertiary positions.",
            "Johannes Itten's twelve-hue wheel - the classic artist's arrangement.",
        ],
        "citations": [CIT_ITTEN, CIT_MUNSELL, CIT_KUEHNI],
        "sig_lens": (
            "The Signature lens sees the tertiaries as the wheel's coming "
            "of age: the first mixtures have grown up and now marry back "
            "into the founding families, and the covenant circle is "
            "complete at twelve. In the Signature Color Method the twelve "
            "hues are the twelve seats of the color council - no hue rules "
            "alone, every harmony is a coalition of seats, and the maker "
            "who knows all twelve addresses can summon any alliance. The "
            "Signature oath of the tertiary is specificity: name the exact "
            "seat - blue-green, not 'greenish blue' - and the color will "
            "answer to its true name."
        ),
    },
    {
        "key": "warm_cool",
        "name": "Warm and Cool Colors",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Colors divide into two great temperaments: warm and cool. "
            "Warm colors are the reds, oranges, and yellows - the colors of "
            "fire, sunlight, and autumn leaves. Cool colors are the greens, "
            "blues, and purples - the colors of water, shade, and winter "
            "sky. The association is physical, not arbitrary: fire and the "
            "sun genuinely radiate at the long-wavelength end that looks "
            "warm, while water and sky scatter the short wavelengths that "
            "look cool. Warm colors advance toward the viewer and feel "
            "energetic, cozy, or urgent; cool colors recede and feel calm, "
            "spacious, or distant. Painters use this deliberately - warm "
            "foregrounds against cool backgrounds create instant depth. "
            "Every hue leans one way: even a 'warm blue' or 'cool red' is "
            "meaningful, because it names which side of its family the "
            "particular shade favors."
        ),
        "how_it_works": (
            "On the twelve-hue wheel the warm half runs from red through "
            "orange and yellow to yellow-green, and the cool half runs from "
            "green through blue and purple back to red-purple - six hues "
            "each, split down the middle. The warm-cool feeling comes from "
            "deep wiring: long-wavelength light dominates firelight and "
            "low sun, so the brain tags reds and oranges with heat and "
            "nearness, while short-wavelength light dominates sky and "
            "water, tagged with coolness and distance. Warm colors also "
            "focus very slightly behind the retina compared with cool "
            "colors, a real optical effect that makes warm shapes feel "
            "closer. Within a single family the lean is relative: an "
            "orange-leaning red is the warm red, a blue-leaning red is the "
            "cool red, and artists exploit these micro-leans constantly."
        ),
        "key_points": [
            "Warm: reds, oranges, yellows - fire, sun, autumn. Cool: greens, blues, purples - water, sky, shade.",
            "The split is physical: warm light is long-wavelength, cool light is short-wavelength.",
            "Warm colors advance and energize; cool colors recede and calm.",
            "The twelve-hue wheel splits into six warm and six cool hues.",
            "Every family has warm and cool members - warm blue, cool red - naming the lean inside the family.",
            "Warm foregrounds against cool backgrounds are the classic recipe for depth.",
        ],
        "requirements": [
            "The twelve-hue wheel to see the warm half and cool half.",
            "Memory of fire, sun, water, and sky as the physical anchors.",
            "Practice sorting any swatch set into warm and cool piles.",
        ],
        "standards": [
            "Johannes Itten's warm-cool contrast - the classic teaching of temperature in painting.",
            "Munsell hue circle - the address system for naming warm and cool leans.",
        ],
        "citations": [CIT_ITTEN, CIT_MUNSELL, CIT_ELLIOT],
        "sig_lens": (
            "The Signature lens reads warm and cool as the two moods of the "
            "covenant: warm colors are the hearth-mood, gathering the viewer "
            "close, and cool colors are the horizon-mood, sending the viewer "
            "outward. In the Signature Color Method the maker chooses mood "
            "before hue - first swear whether the work gathers or releases, "
            "then pick the family that keeps the oath. A Signature "
            "composition never drifts between moods by accident; the warm "
            "half and the cool half are two choirs, and the maker conducts "
            "which one sings."
        ),
    },
    {
        "key": "tints_shades_tones",
        "name": "Tints, Shades, and Tones",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "From any single hue you can build a whole family of related "
            "colors with three simple moves. A tint is the hue mixed with "
            "white: red plus white makes pink, blue plus white makes sky "
            "blue. A shade is the hue mixed with black: red plus black "
            "makes maroon, blue plus black makes navy. A tone is the hue "
            "mixed with gray: red plus gray makes dusty rose, blue plus "
            "gray makes slate. Tints feel light, airy, and gentle; shades "
            "feel deep, rich, and serious; tones feel muted, natural, and "
            "sophisticated. Together with the pure hue, these three moves "
            "generate the monochromatic color scheme - an entire design "
            "built from one hue's extended family, guaranteed harmonious "
            "because every member shares the same parent."
        ),
        "how_it_works": (
            "Mixing with white raises the value while lowering the chroma: "
            "the hue stays but the color gets lighter and softer, because "
            "white adds all wavelengths equally. Mixing with black lowers "
            "the value while also lowering chroma: the color gets darker "
            "and heavier. Mixing with gray lowers chroma while holding "
            "value roughly steady: the color gets dustier without much "
            "change in lightness. In digital terms, a 50 percent tint of a "
            "color averages each channel with 255, a 50 percent shade "
            "averages each channel with 0, and a 50 percent tone averages "
            "each channel with 128. Because tints, shades, and tones of one "
            "hue all share the same hue angle, they can never clash - the "
            "shared parent is the guarantee."
        ),
        "key_points": [
            "Tint: hue plus white - lighter and softer, like pink from red.",
            "Shade: hue plus black - darker and heavier, like maroon from red.",
            "Tone: hue plus gray - dustier and more muted, like dusty rose from red.",
            "Tints raise value, shades lower value, tones lower chroma at steady value.",
            "One hue plus its tints, shades, and tones is the monochromatic scheme - always harmonious.",
            "The shared hue angle is the guarantee: family members cannot clash.",
        ],
        "requirements": [
            "One pure hue, plus white, black, and gray to mix with.",
            "Equal-parts mixing to find the true middle tint, shade, and tone.",
            "The habit of naming which move made each swatch.",
        ],
        "standards": [
            "Munsell value and chroma scales - the measured version of tints, shades, and tones.",
            "CSS Color Module - tint/shade language in digital design tools.",
        ],
        "citations": [CIT_MUNSELL, CIT_ITTEN, CIT_W3C],
        "sig_lens": (
            "The Signature lens calls tints, shades, and tones the honor "
            "margins of brightness: the tint is the hue's promise kept in "
            "daylight, the shade is the hue's promise kept in shadow, and "
            "the tone is the hue's promise kept in weather. In the "
            "Signature Color Method a maker never deploys a lone hue - the "
            "oath is to bring its whole family, tint to shade, so the work "
            "holds together in any light. The monochromatic scheme is the "
            "Signature's simplest covenant: one parent, many children, and "
            "not one quarrel among them."
        ),
    },
    {
        "key": "neutral_colors",
        "name": "Neutral Colors",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Neutral colors are the quiet diplomats of the palette: black, "
            "white, gray, brown, beige, tan, ivory, and their cousins. They "
            "carry little or no hue of their own, which makes them the "
            "perfect companions - they go with everything because they "
            "compete with nothing. Neutrals do the structural work of "
            "design: white opens space, black adds gravity and outlines, "
            "gray calms busy compositions, and earthy browns and beiges "
            "ground a scheme in nature. Almost every great painting, room, "
            "and outfit is mostly neutrals with a few chromatic accents on "
            "top - the neutrals are the stage, the bright colors are the "
            "actors. Learning neutrals first is wise: master the quiet "
            "colors and the loud ones become easy to place."
        ),
        "how_it_works": (
            "True neutrals reflect all wavelengths roughly equally - white "
            "reflects nearly all, black absorbs nearly all, gray reflects a "
            "fraction - so the three cone types fire in near-equal "
            "proportions and the brain reports 'no hue.' Earthy neutrals "
            "like brown, beige, and tan carry a whisper of hue (usually "
            "orange-yellow at low chroma) but behave as neutrals because "
            "the chroma is too low to demand attention. Because neutrals "
            "add no hue of their own, they never clash: any hue placed "
            "beside gray or beige keeps its own character while the neutral "
            "absorbs the visual noise around it. Designers exploit this "
            "constantly - a gray sofa accepts any cushion color, a white "
            "wall accepts any art."
        ),
        "key_points": [
            "Neutrals: black, white, gray, brown, beige, tan, ivory - little or no hue.",
            "They go with everything because they compete with nothing.",
            "White opens space, black adds gravity, gray calms, earth tones ground.",
            "Most great designs are mostly neutrals with a few chromatic accents.",
            "True neutrals reflect all wavelengths equally; earthy neutrals carry only a whisper of hue.",
            "Master the quiet colors first and the loud ones become easy to place.",
        ],
        "requirements": [
            "A neutral swatch set: several grays, a warm beige, a cool gray, black, white.",
            "One bright accent color to test against each neutral.",
            "Noticing which neutrals lean warm and which lean cool.",
        ],
        "standards": [
            "Munsell neutral value scale - the measured gray ladder from black to white.",
            "CIE 1931 achromatic locus - the scientific address of 'no hue.'",
        ],
        "citations": [CIT_MUNSELL, CIT_ALBERS, CIT_CIE15],
        "sig_lens": (
            "The Signature lens honors neutrals as the keepers of the "
            "covenant: they ask for nothing, witness everything, and let "
            "every hue speak without interruption. In the Signature Color "
            "Method the neutral is the oath of restraint - the maker "
            "swears to give bright colors a quiet stage rather than a "
            "shouting match. A Signature work is built neutral-first: lay "
            "the quiet foundation of gray, beige, black, and white, then "
            "place each chromatic accent like a jewel in a plain setting, "
            "where it can shine without competition."
        ),
    },
    {
        "key": "color_wheel",
        "name": "The Color Wheel",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The color wheel is the map of all color relationships: the "
            "hues arranged in a circle so that neighbors blend and "
            "opposites contrast. The classic artist's wheel holds twelve "
            "hues in order - red, red-orange, orange, yellow-orange, "
            "yellow, yellow-green, green, blue-green, blue, blue-purple, "
            "purple, red-purple, and back to red - each sitting exactly 30 "
            "degrees from its neighbors. Once the wheel is drawn, every "
            "harmony becomes geometry: opposites across the circle are "
            "complements, neighbors are analogs, and triangles mark the "
            "triads. Sir Isaac Newton built the first color circle in "
            "1704 after splitting sunlight with a prism, and artists "
            "from Moses Harris to Johannes Itten refined it into the "
            "twelve-hue tool every painter knows. Learn the wheel's "
            "addresses and you can navigate any color decision the way a "
            "sailor navigates by compass."
        ),
        "how_it_works": (
            "The wheel works because hue is genuinely circular: the "
            "spectrum's ends - deep red and violet - meet in the brain "
            "through purple, closing the loop. Placing hues by their "
            "spectral order around the circle puts the most similar hues "
            "side by side, so distance on the wheel measures visual "
            "difference. With twelve evenly spaced hues, complementary "
            "pairs sit exactly 180 degrees apart, analogous groups span "
            "60 to 90 degrees, and triadic sets sit 120 degrees apart - "
            "the geometry does the color theory for you. Painters keep a "
            "physical wheel on the easel; digital tools compute the same "
            "angles from hue numbers. The wheel does not dictate taste, "
            "it organizes options: every scheme in this database is a "
            "shape drawn on this circle."
        ),
        "key_points": [
            "The classic wheel holds twelve hues in spectral order, 30 degrees apart.",
            "Neighbors blend, opposites contrast - distance on the wheel measures visual difference.",
            "Hue is circular because the brain closes the spectrum's ends through purple.",
            "Complements sit 180 degrees apart, triads 120 degrees apart, analogs within 60 to 90 degrees.",
            "Newton drew the first color circle in 1704; Itten refined the twelve-hue artist's wheel.",
            "Every harmony scheme is a shape drawn on this circle.",
        ],
        "requirements": [
            "The twelve hues memorized in order around the circle.",
            "A printed or digital wheel for looking up relationships.",
            "Thinking in angles: 30 degrees a step, 180 the opposite shore.",
        ],
        "standards": [
            "Johannes Itten's twelve-hue wheel - the standard artist's arrangement.",
            "Munsell hue circle - the measured version of the same idea.",
        ],
        "citations": [CIT_ITTEN, CIT_MUNSELL, CIT_KUEHNI],
        "sig_lens": (
            "The Signature lens calls the wheel the Covenant Circle: twelve "
            "seats, twelve witnesses, and every harmony a sworn alliance of "
            "seats. In the Signature Color Method the wheel is not a "
            "decoration but the council chamber where color decisions are "
            "made - the maker walks the circle, hears each hue's testimony, "
            "and signs only the alliances the geometry blesses. The "
            "Signature oath of the wheel is orientation: never choose a "
            "color relationship by feeling alone when the circle will show "
            "you its true address."
        ),
    },
    {
        "key": "subtractive_mixing",
        "name": "Mixing Paint: Subtractive Color Mixing",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Subtractive mixing is what happens in the paint tube, the ink "
            "cartridge, and the dye bath. Each pigment is a filter: it "
            "absorbs certain wavelengths and reflects the rest, and when "
            "you mix two pigments the result reflects only the wavelengths "
            "that survive both filters. Red paint plus yellow paint makes "
            "orange because both reflect the long wavelengths while each "
            "absorbs the parts the other lets through. Every added pigment "
            "subtracts more light, which is why paint mixtures get darker "
            "and why mixing too many paints makes mud: each new pigment "
            "eats more of the spectrum until almost nothing is reflected. "
            "The practical rule is economy - mix with as few pigments as "
            "possible, keep them clean, and let white paint do the "
            "lightening, because white is the only pigment that adds "
            "reflection instead of subtracting it."
        ),
        "how_it_works": (
            "Think of each pigment as a set of surviving wavelengths. Red "
            "pigment's set is the long-wave region, yellow's set is the "
            "long and middle region; mixed, the surviving set is the "
            "intersection - the orange region both sets share. Mathematically "
            "this is close to multiplying the two reflectance curves "
            "wavelength by wavelength: wherever either pigment absorbs "
            "strongly, the mixture goes dark. Cyan, magenta, and yellow "
            "inks are engineered so each absorbs exactly one third of the "
            "spectrum, giving the cleanest possible subtractive control - "
            "which is why printers use them instead of red, yellow, blue. "
            "Traditional red-yellow-blue paint mixing is a coarser version "
            "of the same intersection logic, and its slightly muddy "
            "secondaries are the price of using historical pigments."
        ),
        "key_points": [
            "Each pigment is a filter; a mixture reflects only wavelengths surviving all filters.",
            "Mixing is intersection of reflectance sets - the overlap of what both pigments return.",
            "Every added pigment subtracts light, so mixtures darken and too many pigments make mud.",
            "Economy rule: mix with the fewest pigments possible and keep them clean.",
            "Cyan, magenta, yellow inks are engineered for the cleanest subtractive mixing.",
            "White is the only pigment that adds reflection; it does the lightening.",
        ],
        "requirements": [
            "Real paints or inks to mix - the darkening is only believed when seen.",
            "Clean brushes and palette: contaminated pigments muddy every mixture.",
            "The intersection habit: predict each mixture as the overlap of its parents.",
        ],
        "standards": [
            "ISO 2846 - process ink color and transparency for subtractive print mixing.",
            "Kubelka-Munk theory - the standard model of paint mixture reflectance.",
        ],
        "citations": [CIT_ITTEN, CIT_WYSZECKI, CIT_ALBERS],
        "sig_lens": (
            "The Signature lens reads subtractive mixing as the Covenant of "
            "Matter: every pigment swears what it will return and what it "
            "will keep, and the mixture honors only the wavelengths both "
            "swear to return. In the Signature Color Method the maker "
            "treats each pigment as a sworn witness - clean, few, and "
            "honest - because a contaminated witness corrupts every "
            "testimony it joins. The Signature oath of the palette is "
            "economy: the fewest pigments, the cleanest tools, and the mud "
            "never invited."
        ),
    },
    {
        "key": "additive_mixing",
        "name": "Mixing Light: Additive Color Mixing",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Additive mixing is what happens on every screen you own. Each "
            "pixel holds tiny red, green, and blue emitters, and the eye "
            "receives the sum of their light: red plus green reads as "
            "yellow, green plus blue reads as cyan, red plus blue reads as "
            "magenta, and all three at full strength read as white. Adding "
            "light always brightens - the opposite of paint - because each "
            "new source contributes more photons. This is why stage "
            "lighting designers and screen engineers think in RGB: the "
            "whole visible gamut of a display is addressed by three "
            "numbers, one per emitter. The famous demonstration is the "
            "overlapping flashlight beams: red, green, and blue circles "
            "projected on a white wall produce yellow, cyan, magenta, and "
            "a white center where all three overlap."
        ),
        "how_it_works": (
            "Each emitter stimulates the cone types in a distinct pattern: "
            "red light fires mainly the L cones, green mainly the M cones, "
            "blue mainly the S cones. The brain adds the patterns: red plus "
            "green fires L and M together while S stays quiet, which is "
            "exactly the cone pattern of spectral yellow - so the mixture "
            "looks yellow even though no yellow wavelength is present. "
            "Varying the three emitter strengths independently addresses "
            "every three-cone pattern the eye can distinguish, which is "
            "why three primaries suffice and why digital color is stored "
            "as three numbers. The sum is clipped at the display's maximum "
            "brightness: once all emitters are at full, adding more "
            "intended light changes nothing - the pixel is already white."
        ),
        "key_points": [
            "Screens mix by adding: red plus green is yellow, green plus blue is cyan, red plus blue is magenta.",
            "All three emitters at full make white; all off is black.",
            "Adding light always brightens - the reverse of paint mixing.",
            "The brain reads red-plus-green as yellow because the cone pattern matches spectral yellow.",
            "Every on-screen color is three numbers: the red, green, and blue emitter strengths.",
            "Brightness clips at maximum: a pixel cannot exceed white.",
        ],
        "requirements": [
            "A screen with an RGB color picker to add the channels yourself.",
            "The flashlight-overlap image in mind: three beams, seven regions.",
            "Remembering that light adds while pigment subtracts.",
        ],
        "standards": [
            "sRGB (IEC 61966-2-1) - the additive mixing standard for screens.",
            "Rec. ITU-R BT.709 - the HDTV additive primaries.",
        ],
        "citations": [CIT_SRGB, CIT_WYSZECKI, CIT_HECHT],
        "sig_lens": (
            "The Signature lens reads additive mixing as the Covenant of "
            "Light: every emitter swears its photons into the sum, and the "
            "eye signs the total as color. In the Signature Color Method "
            "the screen is an instrument of testimony - three witnesses "
            "speaking at once, their volumes set by three numbers. The "
            "Signature maker addresses the emitters with intention: each "
            "channel a deliberate voice, never a slider dragged blindly, "
            "because on a screen every number is a vow of light."
        ),
    },
    {
        "key": "complementary",
        "name": "Opposites on the Wheel: Complementary Colors",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Complementary colors are the pairs sitting directly across "
            "from each other on the color wheel: red and green, blue and "
            "orange, yellow and purple, and every 180-degree pair between. "
            "They are called complements because each completes the "
            "spectrum the other lacks - together a complementary pair "
            "contains all three primaries, which is why mixing them in "
            "paint neutralizes toward gray or brown. Placed side by side, "
            "complements create the strongest possible contrast: each "
            "makes the other look more vivid, a phenomenon painters call "
            "simultaneous contrast. Van Gogh's blazing sunflowers against "
            "blue backgrounds and countless sports uniforms exploit "
            "exactly this. The rule of use is proportion - a little of one "
            "complement against a field of the other sings, while equal "
            "amounts shout and can vibrate uncomfortably at full strength."
        ),
        "how_it_works": (
            "A complementary pair spans the full cone response: red "
            "stimulates L strongly, green stimulates M strongly, so the "
            "pair together exercises the whole opponent system the brain "
            "uses to compute color. Stare at red for thirty seconds and "
            "then look at white, and you see a green afterimage - the "
            "fatigued L channel leaves the M channel dominant, and the "
            "brain reads the imbalance as the complement. This opponent "
            "wiring is why complements intensify each other: each hue "
            "pushes the visual system away from itself, which is toward "
            "its opposite. In pigment, mixing complements subtracts almost "
            "everything - red absorbs the middle, green absorbs the ends - "
            "so the mixture collapses toward neutral gray or brown."
        ),
        "key_points": [
            "Complements sit 180 degrees apart: red-green, blue-orange, yellow-purple.",
            "Each pair completes the spectrum; mixed in paint they neutralize to gray or brown.",
            "Side by side they create maximum contrast through simultaneous contrast.",
            "Afterimages prove the wiring: stare at a hue, see its complement on white.",
            "Use in unequal proportion - a little complement against a field of its opposite.",
            "Equal full-strength complements can vibrate; mute one for comfort.",
        ],
        "requirements": [
            "The twelve-hue wheel to find each hue's 180-degree opposite.",
            "An afterimage test: thirty seconds on a hue, then white paper.",
            "Proportion discipline: complements are seasoning, rarely the whole meal.",
        ],
        "standards": [
            "Opponent color theory (Hering) - the physiological basis of complementarity.",
            "Munsell hue circle - complements as opposite addresses.",
        ],
        "citations": [CIT_ITTEN, CIT_ALBERS, CIT_SOLOMON],
        "sig_lens": (
            "The Signature lens reads complements as the sworn opposites of "
            "the council: two seats across the chamber, each completing "
            "what the other lacks, each testifying against the other's "
            "excess. In the Signature Color Method the complement is the "
            "honor-check on every hue - place a color beside its opposite "
            "and both must stand taller, or the choice was unworthy. The "
            "Signature maker deploys complements like a debater deploys a "
            "worthy opponent: with respect, in measured proportion, and "
            "never to annihilate, only to sharpen."
        ),
    },
    {
        "key": "analogous",
        "name": "Neighbors on the Wheel: Analogous Colors",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Analogous colors are the neighbors on the color wheel: three "
            "or four hues sitting side by side, like red, red-orange, and "
            "orange, or blue, blue-green, and green. Because neighbors "
            "share wavelengths, analogous schemes feel naturally "
            "harmonious - there is nothing to clash when every member of "
            "the family resembles the others. Nature paints almost "
            "entirely in analogous schemes: autumn forests run red through "
            "orange to yellow, oceans run blue through blue-green to "
            "green. The design recipe is simple: pick a hero hue, take one "
            "or two neighbors on each side, and let one dominate while "
            "the others support. Analogous schemes are serene and "
            "cohesive, and their one danger is monotony - a dash of the "
            "hero's complement as an accent cures it instantly."
        ),
        "how_it_works": (
            "Neighboring hues stimulate overlapping cone patterns: "
            "red-orange fires the L cones almost like red does, with a "
            "touch more M, so the brain processes the family as variations "
            "on one theme rather than competing signals. The typical "
            "analogous span is 60 to 90 degrees of the wheel - wide enough "
            "for variety, narrow enough that no complement sneaks in to "
            "create tension. In pigment, neighboring paints mix cleanly "
            "because their reflectance sets overlap heavily; unlike "
            "complements, they never neutralize each other. The standard "
            "construction is dominance plus support: roughly 60 percent "
            "hero hue, 30 percent first neighbor, 10 percent second "
            "neighbor, with the accent complement optional at a whisper."
        ),
        "key_points": [
            "Analogous schemes use three or four neighboring hues on the wheel.",
            "Neighbors share wavelengths, so the scheme is inherently harmonious.",
            "Nature's default: autumn forests and oceans are analogous compositions.",
            "Recipe: hero hue dominates, neighbors support at roughly 60-30-10.",
            "The danger is monotony; a whisper of the hero's complement cures it.",
            "Neighboring paints mix cleanly because their reflectance sets overlap.",
        ],
        "requirements": [
            "The wheel, to collect each hero's immediate neighbors.",
            "The 60-30-10 proportion habit for dominance and support.",
            "One complement accent on standby against monotony.",
        ],
        "standards": [
            "Johannes Itten's harmony theory - analogous as the serene scheme.",
            "Munsell hue circle - neighbor addresses within 60 to 90 degrees.",
        ],
        "citations": [CIT_ITTEN, CIT_MUNSELL, CIT_ALBERS],
        "sig_lens": (
            "The Signature lens reads analogous colors as the family "
            "alliance: neighboring seats of the council swearing together, "
            "their testimonies overlapping into one harmonious voice. In "
            "the Signature Color Method the analogous scheme is the "
            "covenant of kinship - choose the hero, gather its kin, and let "
            "one lead while the others witness. The Signature maker guards "
            "against the alliance growing sleepy: a single whisper of the "
            "complement, the loyal opposition, keeps the family honest."
        ),
    },
    {
        "key": "triadic",
        "name": "Triadic Color Schemes",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "A triadic scheme takes three hues spaced evenly around the "
            "wheel, 120 degrees apart, forming a perfect triangle. The "
            "classic triad is the three primaries themselves - red, yellow, "
            "blue - the scheme of children's toys, flags, and bold modern "
            "art. Rotate the triangle and you get subtler triads: "
            "orange, green, purple (the secondaries), or red-orange, "
            "yellow-green, blue-purple. Triads are vibrant and balanced at "
            "once: the hues are far enough apart for real contrast, yet "
            "the even spacing keeps them in equilibrium. The working rule "
            "is the same as for complements - let one hue dominate and "
            "keep the other two as support - because three equal "
            "full-strength hues compete for attention. Triads suit work "
            "that must feel energetic and complete: playgrounds, posters, "
            "and festival designs."
        ),
        "how_it_works": (
            "Even 120-degree spacing means each triad member stimulates a "
            "different balance of the three cone types, so the trio "
            "exercises the whole visual system symmetrically - no channel "
            "is left out, which reads as completeness. On the twelve-hue "
            "wheel there are exactly four distinct triads (starting at "
            "each of the first four hues; the rest repeat), each an "
            "equilateral triangle: 0-120-240, 30-150-270, 60-180-300, "
            "90-210-330. In pigment, triad members mix toward neutrals in "
            "pairs but the trio together spans the primaries, so a skilled "
            "painter can mix nearly the full gamut from one triad - the "
            "famous 'triad palette' of watercolorists. Dominance ordering "
            "(60-30-10 across the three) prevents the democratic shouting "
            "of equal shares."
        ),
        "key_points": [
            "Triads are three hues 120 degrees apart - an equilateral triangle on the wheel.",
            "The classic triad is red, yellow, blue; the secondary triad is orange, green, purple.",
            "Exactly four distinct triads exist on the twelve-hue wheel.",
            "Even spacing exercises all three cone channels symmetrically - vibrant yet balanced.",
            "One triad of paints can mix nearly the full gamut: the watercolorist's triad palette.",
            "Let one hue dominate at 60-30-10; three equal hues compete.",
        ],
        "requirements": [
            "The wheel and a triangle: pick a starting hue, step 120 degrees twice.",
            "The four triads memorized or marked on your wheel.",
            "Dominance discipline: one leader, two supporters.",
        ],
        "standards": [
            "Johannes Itten's contrast and harmony theory - the triadic construction.",
            "Munsell hue circle - the 120-degree address math.",
        ],
        "citations": [CIT_ITTEN, CIT_MUNSELL, CIT_ALBERS],
        "sig_lens": (
            "The Signature lens reads the triad as the council in full "
            "session: three seats at equal remove, no two allied against "
            "the third, the whole circle represented. In the Signature "
            "Color Method the triadic scheme is the covenant of "
            "completeness - the maker who deploys a triad swears to leave "
            "no region of color unrepresented. The Signature discipline is "
            "hierarchy within equality: the triangle is geometrically "
            "perfect, but the composition still crowns one hue, because "
            "even a perfect council needs a chair."
        ),
    },
    {
        "key": "color_temperature",
        "name": "Color Temperature",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Color temperature measures the color of white light itself, in "
            "degrees Kelvin, and the naming is gloriously backwards: low "
            "numbers are warm and high numbers are cool. A candle flame "
            "glows near 1800 K with deep orange warmth; household bulbs "
            "shine near 2700 K with cozy warm white; noon daylight measures "
            "about 5500 to 6500 K with neutral-to-cool white; overcast sky "
            "light can exceed 7000 K with a distinctly cool cast. The scale "
            "comes from heating a theoretical black body: as it gets "
            "hotter it glows red, then orange, then white, then bluish - "
            "so 'temperature' names the heat of the ideal radiator that "
            "would glow that color. Photographers, filmmakers, and "
            "interior designers live by this scale: matching the light "
            "temperature to the mood is half the craft."
        ),
        "how_it_works": (
            "Heat a perfect radiator and the peak of its emitted spectrum "
            "slides from infrared toward the visible as temperature rises, "
            "following Wien's displacement law: peak wavelength in "
            "nanometers equals about 2,898,000 divided by the Kelvin "
            "temperature. At 2700 K the peak sits near 1073 nm (deep in the "
            "infrared, with only the red tail visible - hence warm orange); "
            "at 6500 K the peak sits near 446 nm (blue light - hence cool "
            "white). Real sources approximate this ideal: tungsten "
            "filaments at 2700 K, daylight near 6500 K. Cameras and eyes "
            "both white-balance against the assumed temperature, which is "
            "why a photo taken under warm bulbs looks orange until white "
            "balance corrects it. The backwards naming trips everyone "
            "once: remember that the number names the radiator's heat, "
            "not the feeling - hot radiators glow blue-white."
        ),
        "key_points": [
            "Color temperature names the color of white light, in Kelvin.",
            "Low numbers are warm (candle 1800 K, household bulb 2700 K); high numbers are cool (daylight 6500 K).",
            "The scale follows a heated black body: red to orange to white to blue-white as it heats.",
            "Wien's law: peak wavelength (nm) is about 2,898,000 divided by Kelvin.",
            "At 2700 K the peak is near 1073 nm; at 6500 K near 446 nm.",
            "The naming feels backwards because the number is the radiator's heat, not the mood.",
        ],
        "requirements": [
            "The Kelvin landmarks memorized: 1800 candle, 2700 warm bulb, 6500 daylight.",
            "Wien's law for converting between temperature and peak wavelength.",
            "White-balance awareness: cameras and eyes both correct for the assumed temperature.",
        ],
        "standards": [
            "CIE standard illuminants (A at 2856 K, D65 at 6500 K) - the reference whites.",
            "McCamy's correlated color temperature formula - computing temperature from chromaticity.",
        ],
        "citations": [CIT_MCCAMY, CIT_HECHT, CIT_CIE15],
        "sig_lens": (
            "The Signature lens reads color temperature as the signature of "
            "the light source itself: every lamp and sun signs its work "
            "with a Kelvin number, and the maker reads the signature "
            "before judging any color under it. In the Signature Color "
            "Method no hue is ever evaluated without naming its light's "
            "temperature - to judge a swatch under unknown light is to read "
            "a testimony without knowing the witness. The Signature oath "
            "of temperature is calibration: know your 2700 from your 6500, "
            "white-balance deliberately, and let the light sign honestly."
        ),
    },
    {
        "key": "saturation",
        "name": "Saturation: How Intense a Color Is",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Saturation is how intense, pure, or vivid a color is - how "
            "much of the hue and how little gray. A stop sign's red is "
            "highly saturated; a dusty rose is the same hue at low "
            "saturation; gray itself is zero saturation. Turn the "
            "saturation slider down in any photo app and the image drains "
            "toward black and white; turn it up and colors shout. "
            "Saturation is the drama control of color: high saturation "
            "demands attention and signals energy, artificiality, or "
            "urgency, while low saturation whispers and signals nature, "
            "age, calm, or sophistication. Skilled colorists rarely max "
            "out saturation everywhere - they saturate the hero and mute "
            "the surroundings, so the eye knows where to look."
        ),
        "how_it_works": (
            "Saturation measures the spread between a color's strongest "
            "and weakest channels relative to its strength: a pure hue "
            "has one channel far above the others, while gray has all "
            "channels nearly equal. In HSV terms, saturation equals the "
            "channel spread divided by the maximum channel - (255, 128, 0) "
            "scores about 1.0 spread over 255, a strongly saturated "
            "orange. Lowering saturation pulls the channels toward their "
            "average, which is literally adding gray. The eye reads high "
            "saturation as 'more signal' - the cone contrast is large - "
            "which is why saturated colors pop against muted backgrounds "
            "and why oversaturation looks garish: every color shouting at "
            "once leaves no hierarchy. Muted, low-saturation palettes "
            "dominate nature because natural surfaces mix many wavelengths."
        ),
        "key_points": [
            "Saturation is the purity of a color: hue versus gray.",
            "High saturation shouts; low saturation whispers; zero is gray.",
            "Digitally, saturation is the channel spread divided by the strongest channel.",
            "Lowering saturation is literally adding gray to the color.",
            "Saturate the hero and mute the surroundings to direct the eye.",
            "Nature runs low-saturation; high saturation signals the artificial or the urgent.",
        ],
        "requirements": [
            "A saturation slider to drain and flood a photo while watching.",
            "One hue at three saturations to feel the drama control.",
            "Restraint: saturation is seasoning, and the whole dish cannot be seasoning.",
        ],
        "standards": [
            "HSV/HSB color model - saturation as a computed channel.",
            "Munsell chroma scale - the measured version of saturation.",
        ],
        "citations": [CIT_MUNSELL, CIT_FAIRCHILD, CIT_ALBERS],
        "sig_lens": (
            "The Signature lens reads saturation as the volume of the "
            "hue's testimony: high saturation is a witness speaking "
            "clearly, low saturation a witness speaking through fog. In "
            "the Signature Color Method the maker conducts saturation "
            "like a choir - one voice carries the melody at full volume "
            "while the rest hum in support. The Signature oath of "
            "intensity is hierarchy: never let two colors shout at once, "
            "and let the quiet grays do the listening."
        ),
    },
    {
        "key": "brightness_lightness",
        "name": "Brightness and Lightness",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Brightness and lightness both answer 'how much light,' but "
            "from different points of view. Brightness is absolute - how "
            "much light is coming from the color, like a lamp's wattage. "
            "Lightness is relative - how light the color looks compared "
            "to its surroundings, like judging a gray square against "
            "white versus black. The classic demonstration is the "
            "checker-shadow illusion: two identical gray squares look "
            "dramatically different because one sits in 'shadow' and the "
            "brain judges lightness against context. Designers care "
            "because readability lives here: dark text on a light "
            "background works through lightness contrast, not hue. And "
            "yellow is inherently lighter than blue at equal brightness - "
            "the eye's green-tuned M cones make middle wavelengths look "
            "brighter - which is why pure yellow text on white vanishes "
            "while blue holds."
        ),
        "how_it_works": (
            "Brightness follows the physical light level; lightness "
            "follows the brain's context-corrected estimate of "
            "reflectance. The standard digital measure of perceived "
            "lightness contribution is relative luminance: 0.2126 times "
            "red plus 0.7152 times green plus 0.0722 times blue (after "
            "linearizing the channels), which weights green heavily "
            "because the M cones dominate brightness sensation. This is "
            "why (255, 128, 0) orange computes a luminance near 0.367 - "
            "respectable brightness driven mostly by its green channel - "
            "while pure blue (0, 0, 255) manages only about 0.072. "
            "Contrast ratios for readability are computed from these "
            "luminances: white against black scores 21 to 1, the maximum. "
            "The brain's lightness constancy then discounts the "
            "illumination, judging surfaces by estimated reflectance, "
            "which is what makes the checker-shadow illusion possible."
        ),
        "key_points": [
            "Brightness is absolute light output; lightness is relative to surroundings.",
            "The checker-shadow illusion proves the brain judges lightness by context.",
            "Relative luminance weights green at 0.7152, red at 0.2126, blue at 0.0722.",
            "Yellow is inherently lighter than blue at equal settings because of M-cone tuning.",
            "Readability runs on lightness contrast; white on black scores 21 to 1.",
            "Lightness constancy lets the brain discount illumination and judge the surface.",
        ],
        "requirements": [
            "The checker-shadow illusion, seen once and never forgotten.",
            "The luminance weights memorized: green dominates brightness.",
            "Testing text contrast by lightness, never by hue alone.",
        ],
        "standards": [
            "WCAG contrast formulas - relative luminance for readable text.",
            "CIE lightness L* - the perceptual lightness scale.",
        ],
        "citations": [CIT_WYSZECKI, CIT_FAIRCHILD, CIT_W3C],
        "sig_lens": (
            "The Signature lens reads brightness as the lamp's oath and "
            "lightness as the witness's judgment: the lamp swears how "
            "much light it gives, but the eye judges against the "
            "surroundings and signs its own verdict. In the Signature "
            "Color Method the maker designs for the verdict, not the "
            "lamp - a gray is never 'middle' until its neighbors are "
            "named. The Signature discipline of lightness is context: "
            "place every value deliberately, because no brightness is "
            "ever seen alone."
        ),
    },
    {
        "key": "red_family",
        "name": "The Red Family",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Red is the color of blood, fire, ripe fruit, and alarm - the "
            "hue the human eye notices first and the brain treats as "
            "urgent. Its family spans from the palest pink through "
            "scarlet, crimson, and vermilion to the deep maroons and "
            "burgundies, with rust and brick carrying it toward earth. "
            "Physically, reds are the long-wavelength end of vision, "
            "around 620 to 750 nanometers, stimulating the L cones most "
            "strongly. Culturally, red is the most charged hue on the "
            "wheel: stop signs, warning labels, and sale tags borrow its "
            "urgency, while roses, hearts, and ceremonial dress borrow its "
            "passion. In design, red advances - it jumps forward from "
            "any background - so a little red goes a long way, and large "
            "fields of pure red can feel aggressive. The family rule is "
            "simple: the red channel dominates every member."
        ),
        "how_it_works": (
            "Every red-family color carries its strength in the red "
            "channel: pure red is (255, 0, 0), crimson (220, 20, 60) keeps "
            "red far above blue and green, scarlet (255, 36, 0) adds a "
            "touch of green for heat, maroon (128, 0, 0) is red darkened "
            "toward black, and brick (178, 34, 34) is red dusted toward "
            "gray. Pink is simply red tinted with white, which is why "
            "pink reads as gentle red rather than a separate hue. The "
            "urgency response is partly wired: long-wavelength light "
            "dominates firelight and blood, so the brain tags red with "
            "alertness before culture adds a single meaning. Because red "
            "focuses slightly behind the retina, red shapes also feel "
            "closer than identical blue shapes - the advancing effect "
            "designers exploit."
        ),
        "key_points": [
            "Red is the long-wavelength end of vision, roughly 620 to 750 nanometers, firing the L cones hardest.",
            "The family runs pink to scarlet to crimson to maroon and burgundy, with rust and brick toward earth.",
            "Red is the most psychologically charged hue: urgency, passion, warning, celebration.",
            "In design red advances - a little goes a long way and large fields can feel aggressive.",
            "Every member carries its strength in the red channel, above green and blue.",
            "Pink is red tinted with white; maroon is red shaded with black.",
        ],
        "requirements": [
            "A red-family swatch ladder from pink to maroon.",
            "Respect for red's volume: use it as the accent, rarely the field.",
            "Noticing which reds lean warm (scarlet) and which lean cool (crimson).",
        ],
        "standards": [
            "sRGB red primary (IEC 61966-2-1) - the digital reference red.",
            "Munsell 5R - the measured address of true red.",
        ],
        "citations": [CIT_WYSZECKI, CIT_ELLIOT, CIT_MUNSELL],
        "sig_lens": (
            "The Signature lens reads red as the first alarm of the "
            "covenant: the hue that testifies loudest and is therefore "
            "spent most sparingly. In the Signature Color Method red is "
            "the seal pressed only on what matters - the signature, the "
            "warning, the heart of the work - because a seal on "
            "everything seals nothing. The Signature oath of red is "
            "proportion: let it advance, let it speak, but never let it "
            "shout the whole composition down."
        ),
    },
    {
        "key": "blue_family",
        "name": "The Blue Family",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Blue is the color of sky and deep water, distance and calm - "
            "the most universally liked hue in study after study across "
            "cultures. Its family runs from the palest ice and powder "
            "blues through sky, azure, and cobalt to the profound navies "
            "and midnight blues, with teal and steel carrying it toward "
            "green and gray. Physically, blues are the short-wavelength "
            "middle of vision, around 450 to 495 nanometers, and blue is "
            "the hue most tied to the S cones. Blue recedes: it falls "
            "back from the viewer, which is why distant mountains look "
            "blue and why blue rooms feel larger. In design, blue is the "
            "great trustworthy neutral-chromatic: banks, uniforms, and "
            "technology brands lean on its calm authority. The family "
            "rule: the blue channel leads every member."
        ),
        "how_it_works": (
            "Blue-family colors carry their strength in the blue channel: "
            "pure blue (0, 0, 255), navy (0, 0, 128) darkened toward "
            "black, sky blue (135, 206, 235) lifted with white and a "
            "breath of green, teal (0, 128, 128) balanced between blue "
            "and green, cobalt (0, 71, 171) deepened with authority. The "
            "receding effect is optical: short wavelengths focus slightly "
            "in front of the retina, so the brain places blue shapes "
            "farther away than identical red shapes. Atmospheric "
            "perspective is the same physics outdoors - air scatters "
            "short wavelengths toward the eye, veiling distance in blue. "
            "Blue's popularity may be evolutionary: clear sky and clean "
            "water are survival goods, and the brain tags their color "
            "with approval."
        ),
        "key_points": [
            "Blue spans roughly 450 to 495 nanometers, the S-cone territory between violet and green.",
            "The family runs ice and powder through sky, azure, cobalt, to navy and midnight.",
            "Blue is the most universally liked hue across cultures.",
            "Blue recedes optically, making rooms feel larger and distance look bluer.",
            "Banks, uniforms, and tech brands borrow blue's calm authority.",
            "Every member leads with the blue channel.",
        ],
        "requirements": [
            "A blue-family swatch ladder from ice to midnight.",
            "Using blue's recession deliberately for depth and spaciousness.",
            "Pairing blue with warm accents - its complement orange - for balance.",
        ],
        "standards": [
            "sRGB blue primary (IEC 61966-2-1) - the digital reference blue.",
            "Munsell 5B - the measured address of true blue.",
        ],
        "citations": [CIT_WYSZECKI, CIT_ELLIOT, CIT_MUNSELL],
        "sig_lens": (
            "The Signature lens reads blue as the horizon-mood of the "
            "covenant: the hue that testifies of distance, depth, and "
            "trust kept over time. In the Signature Color Method blue is "
            "the steady witness - the color of the sky that has never "
            "broken an appointment. The Signature maker deploys blue "
            "where the work must be believed: the foundation, the uniform, "
            "the promise. The Signature oath of blue is steadiness: calm, "
            "receding, and utterly reliable."
        ),
    },
    {
        "key": "green_family",
        "name": "The Green Family",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Green is the color of leaves, growth, and the living world - "
            "the hue the human eye sees most efficiently, tuned by "
            "evolution to the forest canopy. Its family stretches from "
            "pale mint and sage through lime, emerald, and kelly to deep "
            "forest and hunter greens, with olive carrying it toward "
            "earth. Physically, greens sit in the middle wavelengths, "
            "around 495 to 570 nanometers, squarely on the M cones' peak "
            "at 534 nanometers - which is why green looks brighter than "
            "any other hue at equal energy and why night-vision displays "
            "glow green. Culturally, green means go, growth, nature, and "
            "money; it calms like blue but with the warmth of life in it. "
            "In design, green is the great balancer - restful to the eye "
            "because the visual system is literally built for it."
        ),
        "how_it_works": (
            "Green-family colors lead with the green channel: pure green "
            "(0, 128, 0), lime (0, 255, 0) at full strength, forest "
            "(34, 139, 34) deepened toward black, mint (189, 252, 201) "
            "lifted with white, olive (128, 128, 0) balanced between green "
            "and red for earthiness. The M cones peak at 534 nanometers, "
            "right in green territory, so the eye extracts more brightness "
            "signal from green light than from any other hue - the reason "
            "relative luminance weights green at 0.7152. Chlorophyll "
            "reflects green because it absorbs red and blue for "
            "photosynthesis and discards the middle; the planet's green "
            "is literally the wavelength plants throw away. This "
            "evolutionary tuning makes green the least fatiguing hue for "
            "long viewing."
        ),
        "key_points": [
            "Green spans roughly 495 to 570 nanometers, centered on the M-cone peak at 534 nm.",
            "The family runs mint and sage through lime, emerald, kelly, to forest and hunter greens.",
            "The eye sees green most efficiently; luminance weights it at 0.7152.",
            "Green means go, growth, nature, and money across cultures.",
            "Leaves are green because chlorophyll discards the middle wavelengths.",
            "Green is the least fatiguing hue - the eye is built for it.",
        ],
        "requirements": [
            "A green-family swatch ladder from mint to forest.",
            "Remembering green's brightness advantage when balancing palettes.",
            "Olive and sage for natural, muted greens that never shout.",
        ],
        "standards": [
            "sRGB green primary (IEC 61966-2-1) - the digital reference green.",
            "Munsell 5G - the measured address of true green.",
        ],
        "citations": [CIT_WYSZECKI, CIT_SOLOMON, CIT_MUNSELL],
        "sig_lens": (
            "The Signature lens reads green as the living witness of the "
            "covenant: the hue the eye was built to hear, testifying of "
            "growth and of light the planet itself set aside. In the "
            "Signature Color Method green is the restful center - the "
            "color of the workbench where the maker returns to recover. "
            "The Signature oath of green is balance: neither advancing "
            "like red nor receding like blue, but holding the middle "
            "ground where the eye is at peace."
        ),
    },
    {
        "key": "yellow_family",
        "name": "The Yellow Family",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Yellow is the color of sunlight, ripeness, and caution - the "
            "brightest hue on the wheel and the hardest to ignore. Its "
            "family runs from pale cream and lemon through canary, gold, "
            "and amber to deep mustard and ochre. Physically, yellow fires "
            "the L and M cones together, around 570 to 590 nanometers, "
            "which is why it looks so luminous: two cone channels at "
            "once. Yellow is the great attention-getter - taxis, school "
            "buses, warning signs, and highlighters all exploit its "
            "visibility - but it is also the most fatiguing hue in large "
            "doses, and pure yellow text on white is nearly unreadable "
            "because its lightness leaves no contrast. In design, yellow "
            "is sunshine in small doses and a headache in large ones; "
            "gold and amber are its sophisticated, deepened members."
        ),
        "how_it_works": (
            "Yellow-family colors carry high red and high green together: "
            "pure yellow (255, 255, 0), gold (255, 215, 0) deepened "
            "slightly, amber (255, 191, 0) warming toward orange, lemon "
            "(255, 247, 0) lifted toward white, mustard (255, 219, 88) "
            "muted toward earth. The L-plus-M firing pattern is the "
            "strongest combined cone signal any single hue produces, "
            "which is the physical root of yellow's luminosity and its "
            "attention-grabbing power. But high lightness is also "
            "yellow's weakness: against white it offers almost no "
            "luminance contrast, so yellow text needs a dark outline or "
            "background to be read. Muted members like ochre and mustard "
            "keep the warmth while taming the shout."
        ),
        "key_points": [
            "Yellow spans roughly 570 to 590 nanometers, firing L and M cones together.",
            "The family runs cream and lemon through canary, gold, amber, to mustard and ochre.",
            "Yellow is the brightest, most attention-grabbing hue - and the most fatiguing in large doses.",
            "Pure yellow on white is nearly unreadable for lack of lightness contrast.",
            "Taxis, buses, and warning signs exploit yellow's visibility.",
            "Every member carries high red and high green together, with blue trailing.",
        ],
        "requirements": [
            "A yellow-family swatch ladder from cream to ochre.",
            "The contrast test: never set pure yellow type on white.",
            "Small doses for energy; gold and amber for sophistication.",
        ],
        "standards": [
            "Munsell 5Y - the measured address of true yellow.",
            "ISO 3864 safety colors - yellow for warning signage.",
        ],
        "citations": [CIT_WYSZECKI, CIT_ELLIOT, CIT_MUNSELL],
        "sig_lens": (
            "The Signature lens reads yellow as the herald of the "
            "covenant: the hue that announces, warns, and celebrates, "
            "never meant to carry the whole message alone. In the "
            "Signature Color Method yellow is the trumpet - sounded "
            "briefly for attention, then yielded to steadier voices. The "
            "Signature oath of yellow is measure: let it herald the "
            "important, never wallpaper the room, and its brightness will "
            "always be a gift instead of a glare."
        ),
    },
    {
        "key": "purple_family",
        "name": "The Purple Family",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Purple is the color of royalty, mystery, and imagination - "
            "the hue with no single wavelength, made by the brain from "
            "the spectrum's two ends at once. Its family runs from pale "
            "lavender and lilac through violet, orchid, and magenta to "
            "deep indigo, plum, and royal purple. Historically, purple "
            "dye came from thousands of sea snails per garment, so only "
            "emperors wore it - the royal association is literally dyed "
            "in. Because purple stimulates both the S cones (blue end) "
            "and the L cones (red end) while skipping the middle, it "
            "feels simultaneously calm and passionate, which is why it "
            "reads as magical, spiritual, or creative. In design, purple "
            "is the wildcard: luxurious in deep shades, playful in light "
            "ones, and always a little otherworldly."
        ),
        "how_it_works": (
            "Purple-family colors lead with blue while keeping red strong: "
            "purple (128, 0, 128) balanced, violet (238, 130, 238) lifted "
            "and reddened, indigo (75, 0, 130) deepened toward blue, "
            "lavender (230, 230, 250) tinted toward white, plum "
            "(221, 160, 221) muted toward gray. No single wavelength looks "
            "purple - the spectrum runs red to violet without passing "
            "through it - so purple exists only as a brain construction "
            "when S and L cones fire together. This 'extra-spectral' "
            "status is unique among the named hues and may explain "
            "purple's aura of mystery: it is the one color the rainbow "
            "never shows. Tyrian purple's ancient cost came from the "
            "Mediterranean murex snail, thousands per robe."
        ),
        "key_points": [
            "Purple has no single wavelength - the brain builds it from the spectrum's two ends.",
            "The family runs lavender and lilac through violet, orchid, magenta, to indigo, plum, royal purple.",
            "Royal associations come from Tyrian purple dye: thousands of sea snails per garment.",
            "Purple feels calm and passionate at once, reading as magical or creative.",
            "It is extra-spectral: the rainbow never shows purple.",
            "Every member leads with blue while keeping red strong.",
        ],
        "requirements": [
            "A purple-family swatch ladder from lavender to royal purple.",
            "Remembering purple's dual nature when choosing its mood.",
            "Deep purples for luxury, light purples for playfulness.",
        ],
        "standards": [
            "Munsell 5P - the measured address of true purple.",
            "CIE 1931 chromaticity diagram - showing purple on the line of purples, off the spectrum.",
        ],
        "citations": [CIT_WYSZECKI, CIT_KUEHNI, CIT_MUNSELL],
        "sig_lens": (
            "The Signature lens reads purple as the covenant's mystery: "
            "the hue the rainbow never shows, sworn into being by the "
            "brain alone. In the Signature Color Method purple is the "
            "seal of imagination - the color of what is real but not "
            "found, like the idea before the build. The Signature maker "
            "spends purple on the visionary parts of the work: the dream, "
            "the invention, the reach beyond the spectrum."
        ),
    },
    {
        "key": "orange_family",
        "name": "The Orange Family",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Orange is the color of sunsets, harvest, and enthusiasm - the "
            "warmest-feeling hue on the wheel, blending red's energy with "
            "yellow's cheer. Its family runs from pale peach and apricot "
            "through tangerine and vivid orange to deep rust and burnt "
            "orange. Physically, orange sits near 590 to 620 nanometers, "
            "between yellow and red, firing L strongly and M moderately. "
            "Orange is the great friendly hue: less aggressive than red, "
            "less glaring than yellow, it invites rather than commands - "
            "which is why it suits food, play, and hospitality. In design, "
            "orange is the approachable accent, the call to action that "
            "doesn't shout, the autumn that everyone loves. The family "
            "rule: red leads, green follows closely, blue trails far "
            "behind."
        ),
        "how_it_works": (
            "Orange-family colors stack red above green above blue: pure "
            "orange (255, 165, 0), tangerine (242, 133, 0) deepened "
            "slightly, coral (255, 127, 80) softened with extra red-blue "
            "balance, peach (255, 229, 180) tinted toward white, rust "
            "(183, 65, 14) shaded toward brown. The red-greater-than-green-"
            "greater-than-blue ordering is the signature of the family - "
            "any color with that channel order reads as some kind of "
            "orange. Orange feels warmest because it concentrates energy "
            "in the long wavelengths the brain associates with firelight "
            "and low sun. Safety orange works because it is the hue most "
            "distant from natural backgrounds: nothing in nature is "
            "safety-cone orange, so it cannot be missed."
        ),
        "key_points": [
            "Orange sits near 590 to 620 nanometers, blending red's energy with yellow's cheer.",
            "The family runs peach and apricot through tangerine and vivid orange to rust and burnt orange.",
            "The channel order red greater than green greater than blue defines every member.",
            "Orange is the friendliest warm hue: inviting rather than commanding.",
            "Safety orange works because no natural background matches it.",
            "In design, orange is the approachable accent and the gentle call to action.",
        ],
        "requirements": [
            "An orange-family swatch ladder from peach to rust.",
            "The channel-order test: R greater than G greater than B means orange territory.",
            "Using orange where red would shout and yellow would glare.",
        ],
        "standards": [
            "Munsell 5YR region - the measured address of orange hues.",
            "ANSI Z535 safety orange - the standardized high-visibility orange.",
        ],
        "citations": [CIT_WYSZECKI, CIT_MUNSELL, CIT_ELLIOT],
        "sig_lens": (
            "The Signature lens reads orange as the hearth-fire of the "
            "covenant: red's passion tempered by yellow's cheer into the "
            "warmest welcome on the wheel. In the Signature Color Method "
            "orange is the handshake hue - the color of the open door, the "
            "shared table, the invitation. The Signature maker spends "
            "orange where the work must befriend its user: the button that "
            "invites the click, the room that invites the guest."
        ),
    },
    {
        "key": "brown",
        "name": "Brown: The Dark Orange",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Brown is the great surprise of color theory: there is no "
            "brown wavelength. Brown is simply dark orange - orange with "
            "its lightness turned down - and the brain refuses to call it "
            "orange once it gets dark enough. The family includes "
            "chocolate, coffee, tan, beige, khaki, sienna, and umber, the "
            "colors of earth, wood, leather, and bread crust. Brown is "
            "the color of the natural and the honest: it grounds designs, "
            "suggests reliability and warmth without flash, and pairs "
            "beautifully with nearly every hue. The famous demonstration "
            "is the isolated swatch: cut a brown square out of a photo "
            "and view it alone against black, and it suddenly looks "
            "orange - brown exists only in context, darker than its "
            "surroundings. No context, no brown."
        ),
        "how_it_works": (
            "Take orange (255, 165, 0) and scale it toward black: at 40 "
            "percent you get (102, 66, 0), which every viewer names "
            "brown. The channel order is unchanged - red still greater "
            "than green greater than blue - but the low overall lightness "
            "plus a brighter surround makes the brain categorize it as a "
            "new color. This is why brown is called a 'relative' color: "
            "unlike red or blue, it cannot be identified from the light "
            "alone; it needs the context of brighter surroundings. Mix "
            "complements in paint and you get brown for the same reason - "
            "the mixture is dark with a warm residual. Tans and beiges "
            "are browns lifted with white; chocolates are browns deepened "
            "toward black."
        ),
        "key_points": [
            "There is no brown wavelength: brown is dark orange, a relative color needing context.",
            "The family includes chocolate, coffee, tan, beige, khaki, sienna, umber.",
            "Viewed alone against black, a brown swatch looks orange - context creates brown.",
            "Brown signals earth, honesty, reliability, and warmth without flash.",
            "Mixing complements in paint yields brown: dark with a warm residual.",
            "Tans and beiges are lifted browns; chocolates are deepened browns.",
        ],
        "requirements": [
            "The isolated-swatch test: brown alone against black reads as orange.",
            "Orange scaled toward black to manufacture any brown.",
            "Using brown as the grounding neutral in warm schemes.",
        ],
        "standards": [
            "Munsell earth hues - the measured addresses of browns as dark oranges.",
            "Kubelka-Munk mixing theory - predicting brown from complement mixtures.",
        ],
        "citations": [CIT_WYSZECKI, CIT_FAIRCHILD, CIT_ALBERS],
        "sig_lens": (
            "The Signature lens reads brown as the covenant's humility: "
            "orange grown honest, brightness surrendered for groundedness. "
            "In the Signature Color Method brown is the oath of the "
            "earth - the maker swears the work will stand on something "
            "real: wood, leather, soil, bread. The Signature builder uses "
            "brown where flash would be a lie, and remembers its secret: "
            "that humility is just glory, darkened by context, waiting "
            "for the right light to be recognized."
        ),
    },
    {
        "key": "gray",
        "name": "Gray: Between Black and White",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Gray is the color of stone, smoke, and overcast skies - the "
            "perfect middle child of the neutrals, carrying no hue and "
            "no opinion. A true gray reflects all wavelengths equally, "
            "just less of them than white and more than black; the "
            "familiar ladder runs from near-black charcoal through "
            "middle gray to near-white silver. Gray is the designer's "
            "great moderator: it calms busy compositions, lets bright "
            "colors shine by contrast, and carries text with quiet "
            "authority. But gray is never truly neutral in practice - "
            "every gray leans warm or cool, and the lean matters: warm "
            "grays (a whisper of yellow-red) feel cozy, cool grays (a "
            "whisper of blue) feel crisp and modern. The Munsell system "
            "built its famous value scale on grays alone, ten steps from "
            "black to white, because gray is the purest measure of "
            "lightness."
        ),
        "how_it_works": (
            "A true gray has equal channels - (128, 128, 128) is the "
            "digital middle gray - so the three cone types fire in "
            "near-equal proportion and the brain reports no hue. Mix "
            "black and white paint in equal parts and the reflectance "
            "curve stays flat across the spectrum, which is the "
            "physical definition of gray. The warm-cool lean comes from "
            "tiny imbalances: (130, 128, 125) reads warm, (125, 128, 132) "
            "reads cool, though both are 'gray' by the numbers. Gray's "
            "moderating power is simultaneous contrast in reverse: beside "
            "a saturated hue, gray looks slightly tinted with the hue's "
            "complement, which makes the hue itself look purer. This is "
            "why galleries hang colorful art on gray walls."
        ),
        "key_points": [
            "True gray reflects all wavelengths equally; equal digital channels make gray.",
            "The ladder runs charcoal through middle gray to silver.",
            "Every practical gray leans warm or cool; the lean sets the mood.",
            "Gray moderates compositions and makes bright colors look purer by contrast.",
            "Galleries use gray walls because gray never competes with art.",
            "The Munsell value scale is ten grays from black to white.",
        ],
        "requirements": [
            "A gray ladder from charcoal to silver for lightness reference.",
            "Checking every gray's lean: warm whisper or cool whisper.",
            "Using gray as the stage, never the star.",
        ],
        "standards": [
            "Munsell neutral value scale - the ten-step gray ladder.",
            "CIE 1931 achromatic locus - the scientific address of gray.",
        ],
        "citations": [CIT_MUNSELL, CIT_ALBERS, CIT_CIE15],
        "sig_lens": (
            "The Signature lens reads gray as the covenant's judge: the "
            "color that testifies to nothing but the truth of lightness, "
            "and before whom every hue's case is heard fairly. In the "
            "Signature Color Method gray is the oath of impartiality - "
            "the maker swears to judge each color against a neutral "
            "witness, never against a tinted rival. The Signature "
            "discipline is to keep a gray card at hand and consult the "
            "judge before signing any color decision."
        ),
    },
    {
        "key": "black_white",
        "name": "Black and White",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Black and white are the two poles of color: the absence and "
            "the fullness of light. White reflects nearly all visible "
            "wavelengths - paper white returns about 80 to 90 percent - "
            "while black absorbs nearly all, with the blackest materials "
            "returning under 5 percent. Together they define the entire "
            "value scale: every lightness judgment is really a judgment "
            "of distance from these two poles. White means clarity, "
            "cleanliness, openness, and new beginnings across most "
            "cultures; black means gravity, elegance, mystery, and "
            "finality. In design their contrast is the strongest tool "
            "available: black text on white is the most readable "
            "combination possible, scoring the maximum 21-to-1 contrast "
            "ratio. Photography began in their duet, and every color "
            "image still carries their grayscale skeleton underneath."
        ),
        "how_it_works": (
            "White fires all three cone types near equally and near "
            "maximum; black leaves them near silent. Relative luminance "
            "runs from 1.0 for reference white to 0.0 for ideal black, "
            "and the contrast ratio formula - (lighter plus 0.05) divided "
            "by (darker plus 0.05) - gives white-on-black the maximum "
            "score of 21 to 1. In pigment, white is the reflector (titanium "
            "dioxide in modern paints) and black is the absorber (carbon "
            "black); in light, white is all emitters at full and black is "
            "all emitters off. The brain treats white as the reference "
            "illuminant and judges every other color against it, which is "
            "why white balance matters so much in photography. No hue can "
            "match their contrast: black and white are the ultimate "
            "figure-ground pair."
        ),
        "key_points": [
            "White reflects nearly all wavelengths; black absorbs nearly all.",
            "They are the two poles defining the entire value scale.",
            "Black on white scores the maximum 21-to-1 contrast ratio - the most readable pairing.",
            "White signals clarity and openness; black signals gravity and elegance.",
            "In paint: titanium white reflects, carbon black absorbs. In light: all emitters on or off.",
            "Every color image carries a grayscale skeleton of black-to-white underneath.",
        ],
        "requirements": [
            "The contrast habit: check readability against the 21-to-1 maximum.",
            "White as the reference illuminant for judging all other colors.",
            "Using the poles deliberately: white to open, black to anchor.",
        ],
        "standards": [
            "WCAG contrast ratio - the 21-to-1 maximum defined.",
            "CIE standard illuminants - the reference whites.",
        ],
        "citations": [CIT_WYSZECKI, CIT_W3C, CIT_CIE15],
        "sig_lens": (
            "The Signature lens reads black and white as the covenant's "
            "two eternal witnesses: the fullness and the absence, the "
            "yes and the no, between which every color testifies. In the "
            "Signature Color Method no composition is signed until it "
            "has been read in black and white - strip the hues away, and "
            "the value structure must still stand. The Signature oath of "
            "the poles is structure: if the grays hold, the colors may "
            "play; if the grays collapse, no hue can save the work."
        ),
    },
    {
        "key": "harmonies",
        "name": "Color Harmonies and Schemes",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "A color harmony is a deliberate team of hues chosen to work "
            "together - the playbook this whole database has been "
            "building toward. The classic schemes are six: monochromatic "
            "(one hue with its tints, shades, and tones), analogous "
            "(neighbors on the wheel), complementary (opposites), "
            "split-complementary (one hue plus the two neighbors of its "
            "opposite), triadic (three hues 120 degrees apart), and "
            "tetradic or square (two complementary pairs, a rectangle on "
            "the wheel). Each scheme is a contract with a different "
            "personality: monochromatic is serene, analogous is natural, "
            "complementary is bold, split-complementary is bold but safer, "
            "triadic is vibrant and balanced, tetradic is rich and "
            "complex. Professionals choose the scheme before choosing the "
            "colors - the scheme is the strategy, the hues are the "
            "tactics. And every scheme obeys the iron law of proportion: "
            "one hue dominates, the rest support, or the team argues "
            "instead of harmonizing."
        ),
        "how_it_works": (
            "Each scheme is a geometric shape on the twelve-hue wheel, "
            "and the geometry predicts the visual effect. Monochromatic "
            "uses one address - zero hue contrast, pure value and chroma "
            "play. Analogous spans 60 to 90 degrees - low contrast, high "
            "unity. Complementary spans 180 degrees - maximum contrast. "
            "Split-complementary takes a hue plus the pair flanking its "
            "opposite (for red: blue-green and yellow-green) - strong "
            "contrast with less tension than the direct opposite. Triadic "
            "is the 120-degree triangle; tetradic pairs two opposites "
            "(for example red-green plus blue-orange), four hues in a "
            "rectangle. The tetradic scheme is the hardest: with four "
            "hues, one must clearly dominate or the composition "
            "fragments. Across all six, the 60-30-10 proportion rule (or "
            "60-25-15 for four hues) keeps the hierarchy the eye needs."
        ),
        "key_points": [
            "Six classic schemes: monochromatic, analogous, complementary, split-complementary, triadic, tetradic.",
            "Each scheme is a shape on the wheel; the geometry predicts the effect.",
            "Split-complementary gives bold contrast with less tension than direct complements.",
            "Tetradic is richest and hardest - four hues demand a clear dominant.",
            "Choose the scheme (strategy) before the hues (tactics).",
            "The iron law: one hue dominates at 60-30-10, or the team argues.",
        ],
        "requirements": [
            "The wheel with all six shapes drawable on it.",
            "The scheme personalities memorized: serene, natural, bold, safer-bold, vibrant, rich.",
            "Proportion discipline on every scheme, especially tetradic.",
        ],
        "standards": [
            "Johannes Itten's seven color contrasts - the theoretical basis of harmony.",
            "Josef Albers' interaction studies - harmony as perceived relationship.",
        ],
        "citations": [CIT_ITTEN, CIT_ALBERS, CIT_KUEHNI],
        "sig_lens": (
            "The Signature lens reads the six harmonies as the six "
            "covenants of composition: six ways the council of hues may "
            "lawfully assemble, each with its sworn character. In the "
            "Signature Color Method the maker signs the scheme before a "
            "single hue is chosen - strategy before tactics, covenant "
            "before color. The Signature oath of harmony is allegiance: "
            "once the scheme is sworn, every hue serves it, one leads, "
            "and none freelances."
        ),
    },
    {
        "key": "hex_rgb",
        "name": "Reading Color Codes: Hex and RGB",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Every color on a screen has a code, and the two great code "
            "languages are RGB and hex. RGB names a color as three "
            "numbers - the red, green, and blue emitter strengths, each "
            "from 0 to 255 - so pure red is rgb(255, 0, 0) and middle gray "
            "is rgb(128, 128, 128). Hex is the same three numbers written "
            "in hexadecimal: pure red is #FF0000, middle gray is #808080, "
            "because FF is 255 and 80 is 128 in base sixteen. Being able "
            "to read these codes is a genuine superpower: you can look "
            "at #FF8000 and know instantly it is a vivid orange (full "
            "red, half green, no blue), or glance at rgb(135, 206, 235) "
            "and recognize sky blue. Designers, developers, and printers "
            "trade in these codes daily, and this record teaches you to "
            "read them like words."
        ),
        "how_it_works": (
            "Each RGB channel holds 8 bits, giving 256 levels per channel "
            "and 256 cubed - 16,777,216 - possible colors. Hexadecimal "
            "writes each channel as two base-16 digits (0-9 then A-F), so "
            "#FF8000 decodes as red FF (15 times 16 plus 15 = 255), green "
            "80 (8 times 16 plus 0 = 128), blue 00 (0) - the vivid orange "
            "(255, 128, 0). Shorthand hex compresses doubles: #F80 means "
            "#FF8800. Reading fluency comes from landmarks: #000000 is "
            "black, #FFFFFF is white, equal pairs like #808080 are gray, "
            "one channel at FF with others at 00 is a pure primary, two "
            "at FF is a secondary. The first pair is always red, the "
            "second green, the third blue - order never changes."
        ),
        "key_points": [
            "RGB names a color as three emitter strengths, each 0 to 255.",
            "Hex writes the same three numbers in base sixteen: #FF0000 is rgb(255, 0, 0).",
            "Eight bits per channel gives 16,777,216 possible colors.",
            "#FF8000 decodes to (255, 128, 0): full red, half green, no blue - vivid orange.",
            "Landmarks: #000000 black, #FFFFFF white, equal pairs gray, one FF a primary, two FF a secondary.",
            "Channel order is always red, green, blue - first pair, second pair, third pair.",
        ],
        "requirements": [
            "The hex digits 0-9, A-F and the 16-times-plus math for decoding.",
            "The landmark codes memorized: black, white, grays, primaries, secondaries.",
            "A color picker to check your readings against the swatch.",
        ],
        "standards": [
            "W3C CSS Color Module - the hex and rgb() notation standard.",
            "sRGB (IEC 61966-2-1) - what the numbers mean on a standard display.",
        ],
        "citations": [CIT_W3C, CIT_SRGB, CIT_WYSZECKI],
        "sig_lens": (
            "The Signature lens reads hex and RGB as the true names of "
            "screen colors: every on-screen hue answers to its code, and "
            "the maker who knows the code commands the hue precisely. In "
            "the Signature Color Method a color is not chosen until it is "
            "named - #FF8000, not 'orangey' - because the true name is "
            "the oath that guarantees the same color on every screen that "
            "keeps the standard. The Signature discipline is literacy: "
            "read the code, see the color, and never confuse the two."
        ),
    },
    {
        "key": "cmyk",
        "name": "CMYK: Color for Print",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "CMYK is the color language of printing: Cyan, Magenta, "
            "Yellow, and Key (black). Where screens add light with RGB, "
            "printers subtract it with inks - cyan ink absorbs red light, "
            "magenta absorbs green, yellow absorbs blue, and the "
            "combination of all three should absorb everything, making "
            "black. In practice the three-ink black is a muddy dark "
            "brown and wastes expensive ink, so printers add a dedicated "
            "black plate - the K - for depth, crisp text, and economy. "
            "Every magazine photo, cereal box, and poster you have ever "
            "held was built from these four inks, laid down as tiny "
            "halftone dots your eye blends from a distance. The crucial "
            "lesson for designers: the print gamut is smaller than the "
            "screen gamut, so vivid screen colors - especially bright "
            "greens and oranges - often print duller than they look."
        ),
        "how_it_works": (
            "Converting RGB to CMYK starts from the strongest channel: "
            "black (K) equals 1 minus the maximum channel, then each ink "
            "is (1 minus its light primary minus K) divided by (1 minus "
            "K). For vivid orange rgb(255, 128, 0): K is 0, cyan is 0, "
            "magenta is about 0.498, yellow is 1.0 - the printer lays no "
            "cyan, half magenta, full yellow, no black. On paper the inks "
            "are printed as overlapping halftone dot screens at different "
            "angles (typically 15, 45, 75, 90 degrees) so the dots form "
            "rosettes instead of moire patterns. Because inks are "
            "imperfect absorbers, the CMYK gamut cannot reach the most "
            "saturated RGB colors - professional workflows soft-proof on "
            "calibrated screens to preview the dulling before printing."
        ),
        "key_points": [
            "CMYK is cyan, magenta, yellow, plus black (Key) - the subtractive print language.",
            "Cyan absorbs red, magenta absorbs green, yellow absorbs blue.",
            "The K plate exists because three-ink black is muddy and wasteful.",
            "Printers lay halftone dots at angled screens; the eye blends them from a distance.",
            "The print gamut is smaller than the screen gamut - vivid screen colors print duller.",
            "Orange rgb(255, 128, 0) converts to roughly C0 M50 Y100 K0.",
        ],
        "requirements": [
            "The RGB-to-CMYK conversion: K from the max channel, then each ink.",
            "A loupe or macro photo to see halftone rosettes on printed matter.",
            "Soft-proofing before print: never trust the screen for final color.",
        ],
        "standards": [
            "ISO 2846 - process ink colors for CMYK printing.",
            "ISO 12647 - process control for halftone color separations.",
        ],
        "citations": [CIT_WYSZECKI, CIT_SRGB, CIT_HECHT],
        "sig_lens": (
            "The Signature lens reads CMYK as the covenant translated for "
            "paper: the screen's oath of light re-sworn in the language "
            "of ink, with black standing witness to keep the translation "
            "honest. In the Signature Color Method the maker never sends "
            "RGB vows to a CMYK court without translation - soft-proof the "
            "gamut, honor the K plate, and let the paper sign what the "
            "screen promised. The Signature oath of print is fidelity: "
            "what the eye was promised, the press must deliver."
        ),
    },
    {
        "key": "color_vision",
        "name": "Color Vision Differences",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Not everyone sees the same colors. About 1 in 12 men and 1 "
            "in 200 women have some form of color vision difference - "
            "often called color blindness - most commonly confusing reds "
            "and greens because one cone type's pigment is shifted or "
            "missing. The main types are protanopia and deuteranopia "
            "(red-green confusion, the most common), tritanopia "
            "(blue-yellow confusion, very rare), and achromatopsia (total "
            "color blindness, extremely rare). People with these "
            "differences still see a rich world - red-green confusion "
            "does not mean seeing in black and white - but certain pairs "
            "become indistinguishable: red and green traffic-light hues, "
            "for example, are told apart by position and brightness, not "
            "hue. For designers this is a duty, not a footnote: never "
            "encode meaning in red-versus-green alone; always add a "
            "second channel like shape, label, or brightness."
        ),
        "how_it_works": (
            "Color vision differences come from the cone pigments: in "
            "deuteranomaly (the most common), the M-cone pigment's peak "
            "shifts toward the L peak, so middle and long wavelengths "
            "produce similar M and L signals and red-green distinctions "
            "collapse. A simplified simulation remaps the red channel: "
            "for pure red (255, 0, 0), a protanopia approximation gives "
            "roughly (145, 142, 0) - the red collapses toward a dim "
            "yellow-green, nearly identical to how green would map. "
            "Designers test with simulators that apply these matrix "
            "transforms to whole images. The accessibility rule is "
            "redundant encoding: charts use color plus pattern or label, "
            "status uses color plus icon or text, and palettes like "
            "blue-orange replace red-green because blue-yellow confusion "
            "is far rarer."
        ),
        "key_points": [
            "About 1 in 12 men and 1 in 200 women have a color vision difference.",
            "Red-green confusion (protanopia, deuteranopia) is by far the most common type.",
            "The cause is shifted or missing cone pigments, collapsing red-green distinctions.",
            "It is not black-and-white vision; most affected people see rich color with specific confusions.",
            "Simulations remap channels with matrices - pure red maps near (145, 142, 0) in protanopia.",
            "Design duty: never encode meaning in red-versus-green alone; add shape, label, or brightness.",
        ],
        "requirements": [
            "A color vision simulator to see your own designs through other eyes.",
            "The prevalence numbers: 1 in 12 men keeps the duty concrete.",
            "Redundant encoding on every meaningful color distinction.",
        ],
        "standards": [
            "WCAG 2.1 success criterion 1.4.1 - color must not be the sole means of conveying information.",
            "Ishihara test plates - the standard screening for red-green differences.",
        ],
        "citations": [CIT_NEI, CIT_SOLOMON, CIT_W3C],
        "sig_lens": (
            "The Signature lens reads color vision differences as a "
            "reminder that every covenant is signed before many "
            "witnesses, and no two witnesses see exactly alike. In the "
            "Signature Color Method the maker swears the work will speak "
            "to all three-witness courts - the standard and the shifted "
            "alike. The Signature oath of inclusion is redundancy: color "
            "plus shape, color plus label, color plus brightness, so that "
            "no witness is ever left out of the testimony."
        ),
    },
    {
        "key": "color_emotion",
        "name": "Color and Emotion",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Colors carry feelings, and the associations are remarkably "
            "consistent: red energizes and excites, blue calms and builds "
            "trust, yellow cheers, green restores, orange befriends, "
            "purple intrigues, black dignifies, white purifies. Some of "
            "this is wired - red raises alertness because it meant blood "
            "and fire long before it meant sale tags - and some is learned: "
            "white means purity in some cultures and mourning in others, "
            "so the learned half varies around the world. Psychologists "
            "study these effects carefully: red can improve performance "
            "on detail tasks but impair creative thinking; blue does the "
            "reverse. For the maker, the lesson is instrumental, not "
            "mystical: choose colors for the feeling the work must "
            "produce, test the choice on real viewers, and remember that "
            "context - a red heart versus a red warning - always "
            "outvotes the swatch."
        ),
        "how_it_works": (
            "Emotional effects flow through two channels: arousal (how "
            "activated the viewer feels) and valence (how pleasant it "
            "feels). Long-wavelength, high-saturation colors raise arousal "
            "- the mechanism behind red's urgency - while short-"
            "wavelength, low-saturation colors lower it, behind blue's "
            "calm. Learned associations then steer valence: cultural "
            "training pairs black with formality, green with nature, gold "
            "with value. The effects are real but modest and "
            "context-dependent - a red 'buy' button may convert better "
            "while a red exam folder may raise anxiety. Careful "
            "researchers therefore test in context rather than trusting "
            "swatch superstition, and the honest summary is that color "
            "nudges feeling while content, composition, and culture decide "
            "it."
        ),
        "key_points": [
            "Consistent associations: red energizes, blue calms, yellow cheers, green restores.",
            "Some effects are wired (red alertness); some are learned and vary by culture.",
            "Red can aid detail work but impair creativity; blue reverses the pattern.",
            "Effects flow through arousal and valence, and are modest and context-dependent.",
            "Context outvotes the swatch: a red heart and a red warning feel nothing alike.",
            "Choose colors for the feeling the work must produce, then test on real viewers.",
        ],
        "requirements": [
            "The association map as a starting hypothesis, never a law.",
            "Cultural awareness: learned meanings like white's vary worldwide.",
            "Testing in context with real viewers before committing.",
        ],
        "standards": [
            "Elliot and Maier's color-in-context theory - the research framework.",
            "WCAG and design research - emotion claims tested against usability evidence.",
        ],
        "citations": [CIT_ELLIOT, CIT_ALBERS, CIT_ITTEN],
        "sig_lens": (
            "The Signature lens reads color emotion as the covenant's "
            "unspoken clause: every hue signs a feeling alongside its "
            "wavelength, and the maker is responsible for both "
            "signatures. In the Signature Color Method the feeling is "
            "chosen first - what must the viewer feel? - and the hue is "
            "the instrument hired to produce it. The Signature oath of "
            "emotion is honesty: never borrow red's urgency for trivia, "
            "never spend blue's trust on the untrustworthy, and test the "
            "feeling the way you test the color."
        ),
    },
    {
        "key": "spectrum",
        "name": "The Spectrum and Beyond: Infrared and Ultraviolet",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The rainbow is only a slice. Visible light runs from about "
            "380 nanometers (violet) to about 750 nanometers (red) - a "
            "band just 370 nanometers wide, a sliver of the vast "
            "electromagnetic spectrum. Beyond the red end stretches "
            "infrared: longer waves we feel as heat, used by remote "
            "controls, night-vision cameras, and astronomers peering "
            "through cosmic dust. Beyond the violet end stretches "
            "ultraviolet: shorter waves that tan skin, make certain "
            "minerals fluoresce, and let bees navigate by patterns on "
            "flowers that are invisible to us. Many animals see these "
            "hidden bands - bees read ultraviolet, pit vipers sense "
            "infrared - so human color vision is just one species' "
            "slice. This record closes the database by placing color in "
            "its true context: a narrow, beautiful window onto an "
            "enormous spectrum."
        ),
        "how_it_works": (
            "Wavelength and frequency are locked by the speed of light: "
            "frequency equals 299,792,458 meters per second divided by "
            "wavelength. Red light at 700 nanometers oscillates about "
            "4.28 times 10 to the 14th times per second; violet at 400 "
            "nanometers about 7.49 times 10 to the 14th. Just past red, "
            "750-nanometer light drops to about 4.00 times 10 to the 14th "
            "hertz - the infrared frontier, where photons carry too "
            "little energy per quantum to trigger the cone pigments, so "
            "we feel them as warmth instead of seeing them. Just past "
            "violet, 380-nanometer light rises to about 7.89 times 10 to "
            "the 14th hertz - the ultraviolet frontier, where photons "
            "carry enough energy to drive chemistry: tanning, fluorescence, "
            "and sunburn. The eye's window is set by the chemistry of "
            "the opsin pigments and the transparency of the eye's lens, "
            "which blocks most ultraviolet before it can reach the "
            "retina."
        ),
        "key_points": [
            "Visible light is 380 to 750 nanometers - a 370-nanometer slice of the whole spectrum.",
            "Infrared lies beyond red: felt as heat, used by remotes, night vision, and astronomy.",
            "Ultraviolet lies beyond violet: tans skin, fluoresces minerals, guides bees.",
            "Frequency equals the speed of light divided by wavelength.",
            "Red at 700 nm is about 4.28 times 10^14 Hz; violet at 400 nm about 7.49 times 10^14 Hz.",
            "Bees see ultraviolet and pit vipers sense infrared - human vision is one species' slice.",
        ],
        "requirements": [
            "Wien's and wave math: frequency from wavelength via the speed of light.",
            "The frontier numbers: 750 nm infrared, 380 nm ultraviolet.",
            "Humility: the rainbow is a narrow window, not the whole of light.",
        ],
        "standards": [
            "CIE 1931 color space - defining the visible window's edges.",
            "ISO 21348 - the standard classification of ultraviolet and infrared bands.",
        ],
        "citations": [CIT_HECHT, CIT_WYSZECKI, CIT_CIE15],
        "sig_lens": (
            "The Signature lens reads the spectrum's edges as the "
            "covenant's horizon: the visible hues are the sworn "
            "territory, and beyond them lie the unsworn lands of heat and "
            "of chemistry. In the Signature Color Method the maker works "
            "inside the window with gratitude - 370 nanometers of "
            "testimony, millions of colors, a whole art - and remembers "
            "that the bees and the vipers keep their own covenants in "
            "bands we will never sign. The Signature closing oath is "
            "wonder: the narrow window is enough."
        ),
    },
]
