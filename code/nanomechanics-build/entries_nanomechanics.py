#!/usr/bin/env python3
"""Entries for the Nanomechanics field databases (field #31, taxonomy order).

Verified 2026-10-17: NO database covers the nanomechanics discipline (the
mechanical behavior of materials and structures at the nanoscale: size
effects, surface-dominated mechanics, nanoindentation, AFM force
spectroscopy, nanowire/nanotube/graphene mechanics, Hall-Petch and its
breakdown, nanotribology, nanoscale contact and adhesion, NEMS resonators,
nanoscale fracture and fatigue, molecular-dynamics mechanics, in-situ TEM
testing, thermoelastic damping, electromechanical coupling, quantum limits
of nanomechanical motion).
- Manifest search (2362 databases): zero slugs or names matching
  nanomechan*. Nearest neighbors are 'nanotech' (10,001 general-
  nanotechnology records), 'nanophotonics' (field #30: nanoscale
  light-matter interaction, not mechanics), 'nanosystems-engineers' and
  'nanotechnology-engineering-technologists-and-technicians' (people/career
  records, not the discipline), 'submicroscopic-phenomena-databases'
  (general submicroscopic phenomena), 'materials-science'-family databases
  (bulk materials records), and 'mechanical-engineering'-family databases
  (macroscale mechanical engineering). None teaches nanomechanics.
- Whole-system title sweep over all 762 shard indexes (1,134,585 records):
  nanomechanics discipline terms (nanomechanic*, nanoindentation,
  hall-petch, nanobeam, nanowire mechanics, NEMS, nanotribology,
  van der Waals mechanics, contact mechanics, in-situ TEM mechanics)
  hit exactly 2 records - 'Tribological Properties of Natural and Synthetic
  Lubricants' and its Signature edition in submicroscopic-phenomena-
  databases: general tribology records, not nanomechanics. ZERO
  full-record discipline coverage anywhere.

So this build creates two NEW databases, 34 ladder-ordered records each:

  nanomechanics              - The Nanomechanics Database
                               (public-harvest: real, fact-checked
                               nanomechanics - the standard references are
                               Bhushan 'Nanotribology and Nanomechanics',
                               Cleland 'Foundations of Nanomechanics',
                               Gerberich & Michler 'Micro and
                               Nanomechanical Testing', Oliver & Pharr's
                               indentation method, Johnson-Kendall-Roberts
                               and Derjaguin-Muller-Toporov contact theory)
  nanomechanics-signature    - The Nanomechanics Signature Database
                               (his original Signature interpretation; src
                               signature, titles suffixed
                               " (Signature Edition)", never presented as
                               authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Subtitle disambiguation (fields #13-30 pattern): specialty titles carry
teaching-focused subtitles rather than bare cards, e.g. "Nanoindentation:
Reading Hardness from a Force Curve".

Numerical cores (all hand-verified 2026-10-17):
- Surface-to-volume of a cube = 6/L: 1 cm -> 600 /m; 10 nm -> 6e8 /m.
- Steel nanowire d=100 nm, L=10 um, F=1 uN: sigma=127.3 MPa, elongation 6.37 nm.
- Laplace pressure 2*gamma/R: gold nanoparticle R=10 nm -> 300 MPa.
- vdW sphere-plate F=AR/6D^2: 10 nm silica tip at 0.5 nm -> 433 pN;
  capillary 4*pi*R*gamma -> 9.05 nN (~21x larger).
- Si cantilever 10x1x0.1 um: k=0.0422 N/m, f=1.38 MHz, 1 nN -> 23.7 nm.
- Nanoindentation: P=500 uN, S=150 uN/nm, hc=97.5 nm -> H=2.15 GPa, Er=266 GPa.
- Oliver-Pharr: S=200 uN/nm, hc=80 nm -> Er=432.9 GPa -> E=633 GPa (nu=0.3).
- WLC DNA (Lp=50 nm): x/L=0.9 -> 2.11 pN; x/L=0.99 -> 205.6 pN.
- Au nanowire d=100 nm: breaks at 11.78 uN / 1.5 GPa, 12.5x bulk strength.
- Hall-Petch Cu: 10 um -> 69.3 MPa; 100 nm -> 468 MPa; 10 nm -> 1425 MPa,
  then inverse softening below ~15 nm.
- SWCNT d=1.4 nm: axial k=1.50 N/m per um; cantilever f=7.54 MHz at L=1 um;
  breaks at ~150 nN (100 GPa).
- Graphene indentation: E_2D=340 N/m -> E_3D=1.01 TPa.
- Friction loop: F_f=59 nN at 100 nN load -> mu=0.59; PT slip F_max=0.40 nN.
- Hertz Si tip R=50 nm, P=100 nN: a=3.48 nm, p=2.63 GPa;
  JKR pull-off 23.6 nN, DMT 31.4 nN.
- Tabor parameter: R=10 nm -> 0.049 (DMT); R=100 um -> 1.06 (JKR).
- NEMS Si beam 5x0.5x0.1 um, f0=10 MHz: R=2.17e22 Hz/kg; 100 kDa -> 3.60 Hz.
- CNT doubly-clamped L=200 nm: f=1.20 GHz.
- Basquin Au nanowire: 1e6 cycles -> 469 MPa; 1e9 cycles -> 235 MPa.
- Griffith glass: a=10 nm -> 2.11 GPa; a=1 um -> 211 MPa; flaw tolerance 0.91 nm.
- LJ argon: k=0.815 N/m per bond, E~2.13 GPa, vibration 0.558 THz;
  velocity-Verlet energy drift < 1e-4.
- In-situ TEM: 38 nm over 2 um in 60 s -> strain rate 3.17e-4 /s.
- Dislocation starvation: 200 nm Au pillar holds ~0.031 dislocations;
  Frenkel shear strength 4.30 GPa.
- NiTi nanowire: 6% recoverable strain, hysteresis 1.2e7 J/m^3 per cycle.
- Octet nanolattice at 1% density: E=600 MPa at 80 kg/m^3.
- Kelvin-Voigt: tau=0.5 ms, De=0.5 at 1 ms process time.
- Euler nanopillar d=100 nm L=1 um: P_cr=7.81 uN (994 MPa);
  film wrinkling lambda=7.12 um.
- TED Si 100 nm beam: tau=11.0 ps, peak 14.4 GHz, Q_TED=9519.
- ZnO nanowire: axial press 1 uN -> Q=1.24e-17 C (12.4 fA at 1 kHz);
  flexoelectric P=3e-4 C/m^2 in bending.
- Squeeze film: Q=1e4 at 1 mTorr -> 0.0131 at 1 atm; water immersion drops
  f by 2.09x.
- Quantum: m=1e-15 kg, f=1 MHz -> x_zp=91.6 fm; ground state below 48 uK.
- Design: 10 MHz Si cantilever -> L=5.25 um; pull-in 43.2 V at 500 nm gap.
- Cell indentation: 1 kPa cell, 5 um probe, 500 nm deep -> 1.41 nN.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature interpretation of "
            "nanomechanics, clearly labeled Signature-made, never "
            "presented as authentic public record.")

C_BHUSHAN_HB = ("Bhushan, B. (ed.) 'Springer Handbook of Nanotechnology'. "
                "4th ed. Springer, 2017.")
C_BHUSHAN_NM = ("Bhushan, B. 'Nanotribology and Nanomechanics: An "
                "Introduction'. 4th ed. Springer, 2017.")
C_CLELAND = ("Cleland, A. N. 'Foundations of Nanomechanics: From Solid-State "
             "Theory to Device Applications'. Springer, 2003.")
C_GERBERICH = ("Gerberich, W. W. and Michler, J. (eds.) 'Micro and "
               "Nanomechanical Testing of Materials and Devices'. Springer, "
               "2008.")
C_OLIVER92 = ("Oliver, W. C. and Pharr, G. M. 'An improved technique for "
              "determining hardness and elastic modulus using load and "
              "displacement sensing indentation experiments'. Journal of "
              "Materials Research 7, 1564-1583 (1992).")
C_OLIVER04 = ("Oliver, W. C. and Pharr, G. M. 'Measurement of hardness and "
              "elastic modulus by instrumented indentation: Advances in "
              "understanding and refinements to methodology'. Journal of "
              "Materials Research 19, 3-20 (2004).")
C_HERTZ = ("Hertz, H. 'Ueber die Beruehrung fester elastischer Koerper'. "
           "Journal fuer die reine und angewandte Mathematik 92, 156-171 "
           "(1882).")
C_JKR = ("Johnson, K. L., Kendall, K. and Roberts, A. D. 'Surface energy "
         "and the contact of elastic solids'. Proceedings of the Royal "
         "Society A 324, 301-313 (1971).")
C_DMT = ("Derjaguin, B. V., Muller, V. M. and Toporov, Y. P. 'Effect of "
         "contact deformations on the adhesion of particles'. Journal of "
         "Colloid and Interface Science 53, 314-326 (1975).")
C_TABOR = ("Tabor, D. 'Surface forces and surface interactions'. Journal of "
           "Colloid and Interface Science 58, 2-13 (1977).")
C_MAUGIS = ("Maugis, D. 'Adhesion of spheres: the JKR-DMT transition using "
            "a Dugdale model'. Journal of Colloid and Interface Science 150, "
            "243-269 (1992).")
C_HAMAKER = ("Hamaker, H. C. 'The London-van der Waals attraction between "
             "spherical particles'. Physica 4, 1058-1072 (1937).")
C_LIFSHITZ = ("Lifshitz, E. M. 'The theory of molecular attractive forces "
              "between solids'. Soviet Physics JETP 2, 73-83 (1956).")
C_ISRAEL = ("Israelachvili, J. N. 'Intermolecular and Surface Forces'. 3rd "
            "ed. Academic Press, 2011.")
C_GRIFFITH = ("Griffith, A. A. 'The phenomena of rupture and flow in "
              "solids'. Philosophical Transactions of the Royal Society A "
              "221, 163-198 (1921).")
C_HALL = ("Hall, E. O. 'The deformation and ageing of mild steel: III "
          "discussion of results'. Proceedings of the Physical Society B 64, "
          "747-753 (1951).")
C_PETCH = ("Petch, N. J. 'The cleavage strength of polycrystals'. Journal "
           "of the Iron and Steel Institute 174, 25-28 (1953).")
C_MEYERS = ("Meyers, M. A., Mishra, A. and Benson, D. J. 'Mechanical "
            "properties of nanocrystalline materials'. Progress in Materials "
            "Science 51, 427-556 (2006).")
C_SCHIOTZ = ("Schiotz, J., Di Tolla, F. D. and Jacobsen, K. W. 'Softening "
             "of nanocrystalline metals at very small grain sizes'. Nature "
             "391, 561-563 (1998).")
C_GAO = ("Gao, H., Ji, B., Jager, I. L., Arzt, E. and Fratzl, P. 'Materials "
         "become insensitive to flaws at nanoscale: Lessons from nature'. "
         "Proceedings of the National Academy of Sciences 100, 5597-5600 "
         "(2003).")
C_PUGNO = ("Pugno, N. M. and Ruoff, R. S. 'Quantized fracture mechanics'. "
           "Philosophical Magazine 84, 2829-2845 (2004).")
C_UCHIC = ("Uchic, M. D., Dimiduk, D. M., Florando, J. N. and Nix, W. D. "
           "'Sample dimensions influence strength and crystal plasticity'. "
           "Science 305, 986-989 (2004).")
C_GREER = ("Greer, J. R. and Nix, W. D. 'Nanoscale gold pillars strengthened "
           "through dislocation starvation'. Physical Review B 73, 245410 "
           "(2006).")
C_VOLKERT = ("Volkert, C. A. and Lilleodden, E. T. 'Size effects in the "
             "deformation of sub-micron Au columns'. Philosophical Magazine "
             "86, 5567-5579 (2006).")
C_SHAN = ("Shan, Z. W., Mishra, R. K., Syed Asif, S. A., Warren, O. L. and "
          "Minor, A. M. 'Mechanical annealing and source-limited deformation "
          "in submicrometre-diameter Ni crystals'. Nature Materials 7, "
          "115-119 (2008).")
C_ARZT = ("Arzt, E. 'Size effects in materials due to microstructural and "
          "dimensional constraints: a comparative review'. Acta Materialia "
          "46, 5611-5626 (1998).")
C_TREACY = ("Treacy, M. M. J., Ebbesen, T. W. and Gibson, J. M. "
            "'Exceptionally high Young's modulus observed for individual "
            "carbon nanotubes'. Nature 381, 678-680 (1996).")
C_KRISHNAN = ("Krishnan, A., Dujardin, E., Ebbesen, T. W., Yianilos, P. N. "
              "and Treacy, M. M. J. 'Young's modulus of single-walled "
              "nanotubes'. Physical Review B 58, 14013-14019 (1998).")
C_PONCHARAL = ("Poncharal, P., Wang, Z. L., Ugarte, D. and de Heer, W. A. "
               "'Electrostatic deflections and electromechanical resonances "
               "of carbon nanotubes'. Science 283, 1513-1516 (1999).")
C_FALVO = ("Falvo, M. R., Clary, G. J., Taylor, R. M., Chi, V., Brooks, "
           "F. P., Washburn, S. and Superfine, R. 'Bending and buckling of "
           "carbon nanotubes under large strain'. Nature 389, 582-584 "
           "(1997).")
C_YU = ("Yu, M.-F., Files, B. S., Arepati, S. and Ruoff, R. S. 'Tensile "
        "loading of ropes of single wall carbon nanotubes and their "
        "mechanical properties'. Physical Review Letters 84, 5552-5555 "
        "(2000).")
C_WONG = ("Wong, E. W., Sheehan, P. E. and Lieber, C. M. 'Nanobeam "
          "mechanics: Elasticity, strength, and toughness of nanorods and "
          "nanotubes'. Science 277, 1971-1975 (1997).")
C_LEE08 = ("Lee, C., Wei, X., Kysar, J. W. and Hone, J. 'Measurement of the "
           "elastic properties and intrinsic strength of monolayer "
           "graphene'. Science 321, 385-388 (2008).")
C_BUNCH = ("Bunch, J. S., van der Zande, A. M., Verbridge, S. S., Frank, "
           "I. W., Tanenbaum, D. M., Parpia, J. M., Craighead, H. G. and "
           "McEuen, P. L. 'Electromechanical resonators from graphene "
           "sheets'. Science 315, 490-493 (2007).")
C_SAZONOVA = ("Sazonova, V., Yaish, Y., Ustunel, H., Roundy, D., Arias, T. "
              "A. and McEuen, P. L. 'A tunable carbon nanotube "
              "electromechanical oscillator'. Nature 428, 284-287 (2004).")
C_HUANG = ("Huang, X. M. H., Zorman, C. A., Mehregany, M. and Roukes, M. L. "
           "'Nanodevice motion at microwave frequencies'. Nature 421, "
           "496-496 (2003).")
C_CRAIGHEAD = ("Craighead, H. G. 'Nanoelectromechanical systems'. Science "
               "290, 1532-1535 (2000).")
C_EKROU = ("Ekinci, K. L. and Roukes, M. L. 'Nanoelectromechanical "
           "systems'. Review of Scientific Instruments 76, 061101 (2005).")
C_EKMASS = ("Ekinci, K. L., Yang, Y. T. and Roukes, M. L. 'Ultimate limits "
            "to inertial mass sensing based upon nanoelectromechanical "
            "systems'. Journal of Applied Physics 95, 2682-2689 (2004).")
C_NAIK = ("Naik, A. K., Hanay, M. S., Hiebert, W. K., Feng, X. L. and "
          "Roukes, M. L. 'Towards single-molecule nanomechanical mass "
          "spectrometry'. Nature Nanotechnology 4, 445-450 (2009).")
C_CHASTE = ("Chaste, J., Eichler, A., Moser, J., Ceballos, G., Rurali, R. "
            "and Bachtold, A. 'A nanomechanical mass sensor with yoctogram "
            "resolution'. Nature Nanotechnology 7, 301-304 (2012).")
C_LAHAYE = ("LaHaye, M. D., Buu, O., Camarota, B. and Schwab, K. C. "
            "'Approaching the quantum limit of a nanomechanical resonator'. "
            "Science 304, 74-77 (2004).")
C_OCONNELL = ("O'Connell, A. D. et al. 'Quantum ground state and "
              "single-phonon control of a mechanical resonator'. Nature 464, "
              "697-703 (2010).")
C_TEUFEL = ("Teufel, J. D. et al. 'Sideband cooling of micromechanical "
            "motion to the quantum ground state'. Nature 475, 359-363 "
            "(2011).")
C_ASPELMEYER = ("Aspelmeyer, M., Kippenberg, T. J. and Marquardt, F. "
                "'Cavity optomechanics'. Reviews of Modern Physics 86, "
                "1391-1452 (2014).")
C_SCHMID = ("Schmid, S., Villanueva, L. G. and Roukes, M. L. 'Fundamentals "
            "of Nanomechanical Resonators'. Springer, 2016.")
C_LIFROU = ("Lifshitz, R. and Roukes, M. L. 'Thermoelastic damping in "
            "micro- and nanomechanical systems'. Physical Review B 61, "
            "5600-5609 (2000).")
C_ZENER = ("Zener, C. 'Elasticity and Anelasticity of Metals'. University "
           "of Chicago Press, 1948.")
C_SADER = ("Sader, J. E. 'Frequency response of cantilever beams immersed "
           "in viscous fluids with applications to the atomic force "
           "microscope'. Journal of Applied Physics 83, 1723-1734 (1998).")
C_PERSSON = ("Persson, B. N. J. 'Sliding Friction: Physical Principles and "
             "Applications'. 2nd ed. Springer, 2000.")
C_MATE = ("Mate, C. M., McClelland, G. M., Erlandsson, R. and Chiang, S. "
          "'Atomic-scale friction of a tungsten tip on a graphite surface'. "
          "Physical Review Letters 59, 1942-1945 (1987).")
C_GNECCO = ("Gnecco, E., Bennewitz, R., Gyalog, T. and Meyer, E. 'Friction "
            "experiments on the nanometre scale'. Journal of Physics: "
            "Condensed Matter 13, R619-R642 (2001).")
C_CARPI = ("Carpick, R. W., Ogletree, D. F. and Salmeron, M. 'A general "
           "equation for fitting contact area and friction vs load "
           "measurements'. Journal of Colloid and Interface Science 211, "
           "395-400 (1999).")
C_MO = ("Mo, Y., Turner, K. T. and Szlufarska, I. 'Friction laws at the "
        "nanoscale'. Nature 458, 1116-1119 (2009).")
C_SZLUF = ("Szlufarska, I., Chandross, M. and Carpick, R. W. 'Recent "
           "advances in single-asperity nanotribology'. Journal of Physics "
           "D: Applied Physics 41, 123001 (2008).")
C_BUTT = ("Butt, H.-J., Cappella, B. and Kappl, M. 'Force measurements with "
          "the atomic force microscope: Technique, interpretation and "
          "applications'. Surface Science Reports 59, 1-152 (2005).")
C_CAPPELLA = ("Cappella, B. and Dietler, G. 'Force-distance curves by "
              "atomic force microscopy'. Surface Science Reports 34, 1-104 "
              "(1999).")
C_HUTTER = ("Hutter, J. L. and Bechhoefer, J. 'Calibration of atomic-force "
            "microscope tips'. Review of Scientific Instruments 64, 1868- "
            "1873 (1993).")
C_BUSTAMANTE = ("Bustamante, C., Smith, S. B., Liphardt, J. and Smith, D. "
                "'Single-molecule studies of DNA mechanics'. Current "
                "Opinion in Structural Biology 10, 279-285 (2000).")
C_MARKO = ("Marko, J. F. and Siggia, E. D. 'Stretching DNA'. "
           "Macromolecules 28, 8759-8770 (1995).")
C_RADMACHER = ("Radmacher, M. 'Measuring the elastic properties of "
               "biological samples with the AFM'. IEEE Engineering in "
               "Medicine and Biology Magazine 16, 47-57 (1997).")
C_WANG = ("Wang, Z. L. and Song, J. 'Piezoelectric nanogenerators based on "
          "zinc oxide nanowire arrays'. Science 312, 242-246 (2006).")
C_MAJDOUB = ("Majdoub, M. S., Sharma, P. and Cagin, T. 'Enhanced "
             "size-dependent piezoelectricity and elasticity in "
             "nanostructures due to the flexoelectric effect'. Physical "
             "Review B 77, 125424 (2008).")
C_GIBSON = ("Gibson, L. J. and Ashby, M. F. 'Cellular Solids: Structure and "
            "Properties'. 2nd ed. Cambridge University Press, 1997.")
C_SCHAEDLER = ("Schaedler, T. A. et al. 'Ultralight metallic microlattices'. "
               "Science 334, 962-965 (2011).")
C_ZHENG = ("Zheng, X. et al. 'Ultralight, ultrastiff mechanical "
           "metamaterials'. Science 344, 1373-1377 (2014).")
C_MEZA = ("Meza, L. R., Das, S. and Greer, J. R. 'Strong, lightweight, and "
          "recoverable three-dimensional ceramic nanolattices'. Science 345, "
          "1322-1326 (2014).")
C_LANDAU = ("Landau, L. D. and Lifshitz, E. M. 'Theory of Elasticity'. 3rd "
            "ed. Pergamon, 1986.")
C_TIMOSHENKO = ("Timoshenko, S. P. and Goodier, J. N. 'Theory of "
                "Elasticity'. 3rd ed. McGraw-Hill, 1970.")
C_FRENKEL = ("Frenkel, J. 'Zur Theorie der Elastizitaetsgrenze und der "
             "Festigkeit kristallinischer Koerper'. Zeitschrift fuer Physik "
             "37, 572-609 (1926).")
C_NIX = ("Nix, W. D. 'Mechanical properties of thin films'. Metallurgical "
         "Transactions A 20, 2217-2245 (1989).")
C_GREENWOOD = ("Greenwood, J. A. and Williamson, J. B. P. 'Contact of "
               "nominally flat surfaces'. Proceedings of the Royal Society A "
               "295, 300-319 (1966).")
C_FERRY = ("Ferry, J. D. 'Viscoelastic Properties of Polymers'. 3rd ed. "
           "Wiley, 1980.")
C_WARD = ("Ward, I. M. and Sweeney, J. 'Mechanical Properties of Solid "
          "Polymers'. 3rd ed. Wiley, 2013.")
C_CLELAND_NOISE = ("Cleland, A. N. and Roukes, M. L. 'Noise processes in "
                   "nanomechanical resonators'. Journal of Applied Physics "
                   "92, 2758-2769 (2002).")
C_KNOBEL = ("Knobel, R. G. and Cleland, A. N. 'Nanometre-scale displacement "
            "sensing using a single electron transistor'. Nature 424, "
            "291-293 (2003).")

ENTRIES = [
{
"key": "what_is",
"name": "Nanomechanics: The Science of Forces at the Nanoscale",
"group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
"description": (
"Nanomechanics is the study of how materials and structures deform, break, "
"vibrate, stick, and wear when their size shrinks to the nanometre scale - "
"roughly one to a few hundred nanometres. At human scale, a steel beam "
"bends the way the textbooks say, friction follows simple rules, and "
"surfaces are a footnote. Shrink that beam to 100 nanometres wide and the "
"footnote becomes the headline: surfaces carry a large share of the atoms, "
"defects that weaken bulk materials may be absent entirely, forces like "
"van der Waals attraction and capillarity that we ignore at the macroscale "
"can dominate, and familiar laws of friction, fracture, and plasticity "
"change their form. Nanomechanics asks the practical questions - how hard "
"is this coating, how much will this nanowire stretch before it snaps, how "
"sensitively can this vibrating beam weigh a molecule, will these two "
"surfaces stick together - and answers them with experiments (nanoindenters, "
"atomic force microscopes, in-situ electron microscopy) and theory "
"(continuum elasticity pushed to its limits, atomistic simulation). It is "
"the mechanical foundation beneath nanoelectromechanical systems, "
"nanocomposites, protective coatings, and nanomanufacturing."),
"how_it_works": (
"Everything in nanomechanics starts with the same move: take a macroscopic "
"mechanical idea - stress, strain, bending, contact, friction, fracture - "
"and ask what changes when the object is only thousands of atoms across. "
"Three changes dominate. First, the surface-to-volume ratio explodes: a "
"10-nanometre cube has a million times the surface per volume of a "
"1-centimetre cube, so surface energy, surface stress, and surface forces "
"stop being corrections and become drivers. Second, the defect population "
"collapses: a nanowire may contain zero dislocations, so it deforms near "
"the theoretical strength instead of the defect-controlled strength of "
"bulk. Third, the measuring tools must become part of the physics: a "
"nanoindenter tip, an AFM cantilever, and an electron beam all exert forces "
"comparable to the forces being measured. The worker's toolkit therefore "
"pairs scaled-down continuum theory (beams, plates, Hertz contact) with "
"atomistic methods (molecular dynamics) and exquisite instruments, and "
"checks every result against the question: is this a material property, or "
"a size effect?"),
"key_points": [
"Nanomechanics studies deformation, fracture, vibration, adhesion, and wear at the 1-500 nm scale.",
"Surface-to-volume ratio grows as 1/size: a 10 nm cube has a million times the surface share of a 1 cm cube.",
"Small volumes can be defect-free, so nanostructures often approach theoretical strength.",
"Surface forces (van der Waals, capillary, electrostatic) dominate where gravity and inertia vanish.",
"Instruments are part of the experiment: indenters, AFM tips, and electron beams all apply real forces.",
"The central question of every result: material property, or size effect?"],
"requirements": [
"A working sense of stress (force per area) and strain (relative deformation).",
"Orders of magnitude in SI units: nano = 1e-9, pico = 1e-12.",
"Comfort with ratios and scaling arguments (the demo is arithmetic, not calculus).",
"A calculator for the scale exercises."],
"standards": [
"SI units throughout: metres, newtons, pascals.",
"Nanometre (nm) as the working length unit; micronewton (uN) and nanonewton (nN) for forces.",
"1 Pa = 1 N/m^2; 1 GPa = 1e9 Pa."],
"citations": [C_BHUSHAN_NM, C_CLELAND, C_GERBERICH],
"sig_lens": (
"Signature take: strength is not a property of the material - it is a "
"property of the size. Shrink anything far enough and the flaws run out "
"of room to exist; what is left is the honest strength of the bonds "
"themselves. The Signature builder treats the nanoscale as the place "
"where materials finally tell the truth, and every device in this "
"database is built to listen at exactly that scale."),
},
{
"key": "scale_effects",
"name": "Smaller Is Different: Size Effects in Mechanical Behavior",
"group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
"description": (
"'Smaller is stronger' is the most famous sentence in nanomechanics, and it "
"is true often enough to design around. Gold pillars a few hundred "
"nanometres wide yield at stresses ten times the bulk value; silicon "
"nanowires bend further before breaking than any silicon beam; nanoporous "
"gold is far stronger than its density suggests. The causes are several "
"and they stack: fewer and smaller flaws (a crack cannot be bigger than "
"the object), dislocation starvation (dislocations escape to the free "
"surface faster than they multiply), strain gradients that harden small "
"bent volumes, and surfaces that carry load directly through surface "
"stress. But 'smaller is different' cuts both ways - adhesion and friction "
"grow in relative importance, melting points drop, diffusion accelerates, "
"and some materials soften at the smallest grain sizes (the inverse "
"Hall-Petch effect). The competent nanomechanics worker never quotes a "
"bulk property for a nanoscale object without asking which way the size "
"effect points, and by roughly how much."),
"how_it_works": (
"Size effects are quantified by scaling laws - how a property changes when "
"all dimensions shrink by a factor lambda. Surface-to-volume ratio scales "
"as 1/L, so anything surface-driven (surface stress, adhesion, surface "
"diffusion) grows as objects shrink. Strength often scales as a power law "
"of diameter, sigma ~ d^-n with n around 0.5-1 for metallic pillars. "
"Beam stiffness scales as t^3 for a plate of thickness t, while mass "
"scales as t, so resonant frequency scales as t/L^2 - the reason smaller "
"resonators ring at higher frequencies. Thermal equilibration time scales "
"as L^2 (diffusion), so a 100 nm object thermalizes roughly a hundred "
"million times faster than a 1 cm one. The demo walks the size ladder "
"from metres to nanometres computing surface-to-volume ratio and the "
"fraction of atoms on the surface, showing the crossover where 'surface "
"material' outnumbers 'bulk material' - near a few nanometres, where "
"roughly every atom is a surface atom."),
"key_points": [
"'Smaller is stronger' holds for many nanostructures: flaws shrink with the object and dislocations starve.",
"Surface-to-volume ratio scales as 1/L; surface effects dominate below ~100 nm.",
"Strength of metallic nanopillars follows roughly sigma ~ d^-0.6.",
"Resonant frequency scales as thickness/length^2: smaller rings higher.",
"Thermal times scale as L^2: nanoscale objects thermalize almost instantly.",
"Counter-effects exist: inverse Hall-Petch softening, melting-point depression, faster diffusion."],
"requirements": [
"Power-law and ratio reasoning (the entry before this one).",
"The idea of a dislocation as a line defect (one paragraph is enough).",
"A calculator."],
"standards": [
"Scaling laws written as quantity ~ L^n with the exponent stated.",
"Surface-to-volume ratio in 1/m.",
"Atom diameter ~0.25-0.3 nm for order-of-magnitude atom counts."],
"citations": [C_ARZT, C_NIX, C_BHUSHAN_NM],
"sig_lens": (
"Signature take: the bulk world is the diluted world - properties "
"averaged over trillions of defects. The nanoscale is the concentrated "
"world, where one missing row of atoms changes everything. Signature "
"engineering works in the concentrated world on purpose, because that "
"is where a small change buys a large effect."),
},
{
"key": "stress_strain",
"name": "Stress, Strain, and Modulus at the Nanoscale: The Universal Language",
"group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
"description": (
"Stress (force divided by area) and strain (deformation divided by length) "
"are the nouns and verbs of all mechanics, and they survive the trip to "
"the nanoscale intact - what changes is the size of the numbers. A "
"micronewton pulling on a 100-nanometre wire produces over a hundred "
"megapascals, because the area is only about eight quadrillionths of a "
"square metre. The elastic modulus E = stress/strain is, remarkably, "
"almost size-independent down to a few nanometres: steel is 200 GPa "
"whether the beam is a bridge or a nanowire, since stiffness comes from "
"bond stretching and bonds do not know the size of the object. Strength, "
"by contrast, is wildly size-dependent, because strength is controlled "
"by flaws and flaws are size-limited. This entry fixes the vocabulary "
"(engineering vs true stress, elastic vs plastic strain, yield, ultimate "
"strength, toughness as the area under the curve) and the unit instincts "
"(a nanonewton on a square nanometre is a gigapascal) that every later "
"entry assumes without apology."),
"how_it_works": (
"Take a nanowire of diameter d and length L, pull with force F, and measure "
"elongation delta. Engineering stress sigma = F/A with A = pi*d^2/4; "
"engineering strain epsilon = delta/L; modulus E = sigma/epsilon in the "
"linear region. At the nanoscale the same definitions hold, but the "
"measurement chain is delicate: forces come from calibrated cantilevers "
"or load cells with nanonewton resolution, displacements from capacitive "
"sensors or electron-microscope images with nanometre resolution, and the "
"cross-section from electron microscopy - a 10% error in diameter is a 21% "
"error in stress. True stress and true strain (referred to the instantaneous "
"area and length) matter once deformation exceeds a few percent, which "
"nanowires routinely survive. The demo pulls a 100 nm steel wire with one "
"micronewton, computing stress, strain, and elongation, and shows the "
"mnemonic every worker carries: 1 nN per nm^2 = 1 GPa."),
"key_points": [
"Stress = F/A, strain = delta/L, modulus E = stress/strain: unchanged at the nanoscale.",
"Modulus is nearly size-independent (bond property); strength is strongly size-dependent (flaw property).",
"1 nN on 1 nm^2 = 1 GPa: the unit instinct for nanoscale forces.",
"Diameter errors square into stress errors: measure the cross-section carefully.",
"True stress/strain (instantaneous geometry) beat engineering values past a few percent strain.",
"Toughness is the area under the stress-strain curve, not the peak."],
"requirements": [
"Arithmetic with powers of ten.",
"The circle area formula A = pi*d^2/4.",
"Nothing else - this entry is the foundation."],
"standards": [
"Stress and modulus in Pa (GPa, MPa); force in N (nN, uN); length in m (nm, um).",
"Engineering stress/strain as the default; true values flagged explicitly.",
"Elastic modulus quoted with the material and crystal direction where it matters."],
"citations": [C_LANDAU, C_TIMOSHENKO, C_GERBERICH],
"sig_lens": (
"Signature take: stress and strain are the honest bookkeeping of "
"mechanics - every force accounted for, every stretch measured. At "
"the nanoscale the books are kept in nanonewtons and the auditor is "
"unforgiving: a sloppy diameter measurement is a lie about strength. "
"Signature work measures twice and reports the true numbers."),
},
{
"key": "continuum_breakdown",
"name": "Where Continuum Mechanics Breaks Down: The Ten-Nanometre Boundary",
"group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
"description": (
"Continuum mechanics treats matter as smooth and infinitely divisible, "
"and it works astonishingly well down to about ten nanometres - roughly "
"forty atoms across. Below that, the grain of the material shows: a "
"5-nanometre wire is twenty atoms wide, a dislocation core is a few atoms "
"wide, and 'the surface' is a substantial fraction of the whole object. "
"The breakdown is gradual, not a cliff. First the surface needs its own "
"elastic constants (surface stress and surface elasticity); then "
"nonlocal effects appear, where the stress at a point depends on the "
"strain in its neighborhood; finally, for objects of a few nanometres, "
"only atomistic simulation is trustworthy. The practical rule: continuum "
"elasticity with surface corrections handles 10-100 nm; atomistics owns "
"the territory below ~5 nm; between them, use both and demand agreement. "
"This entry maps the boundary so the worker knows which tool is legal "
"where - because applying bulk continuum formulas to a 2-nanometre "
"particle is not an approximation, it is a category error."),
"how_it_works": (
"The test for continuum validity is the ratio of the feature size to the "
"material's internal lengths: the atomic spacing (~0.25 nm), the "
"dislocation core width (~1 nm), and the range of surface influence "
"(~1-2 nm). When the object spans dozens of these lengths, averaging "
"over atoms is legitimate and elasticity works. The demo counts atoms "
"across features from 100 nm down to 1 nm and computes the fraction of "
"atoms within one atomic layer of the surface, showing the crossover: at "
"100 nm the surface is a 1% correction, at 10 nm it is ~10%, at 2 nm the "
"object is essentially all surface. Nonlocal elasticity (Eringen's "
"theory) and surface-elasticity models (Gurtin-Murdoch) extend the "
"continuum a little further by giving the theory a built-in length "
"scale, but they are bridges, not new territory - the far side belongs "
"to molecular dynamics."),
"key_points": [
"Continuum elasticity is reliable down to ~10 nm (~40 atoms across).",
"Below ~5 nm, atomistic simulation is the trustworthy tool.",
"Surface elasticity (Gurtin-Murdoch) and nonlocal theory extend the continuum partway.",
"The validity test: feature size vs atomic spacing, dislocation core, surface-influence range.",
"At 2 nm, an object is essentially all surface: continuum 'bulk' concepts lose meaning.",
"Using bulk formulas on few-nanometre objects is a category error, not an approximation."],
"requirements": [
"The stress/strain entry before this one.",
"Acceptance that matter is made of atoms (the demo counts them).",
"A calculator."],
"standards": [
"Internal length scales quoted in nm alongside any continuum result near the boundary.",
"Atomistic results flagged with the potential/model used.",
"Continuum-plus-surface-correction results labeled as such."],
"citations": [C_CLELAND, C_LANDAU, C_BHUSHAN_HB],
"sig_lens": (
"Signature take: every theory has a jurisdiction, and wisdom is knowing "
"where yours ends. The Signature worker uses continuum theory the way "
"a surveyor uses a map - excellent within its borders, fiction beyond "
"them. Below ten nanometres, the map is the atoms themselves."),
},
{
"key": "surface_energy",
"name": "Surface Energy and Surface Stress: Why Small Surfaces Rule",
"group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
"description": (
"Creating a surface costs energy - atoms at the surface have fewer "
"neighbors and unsatisfied bonds - and that cost, the surface energy "
"gamma (joules per square metre), becomes a dominant force at the "
"nanoscale. It drives sintering (powders fuse to reduce surface area), "
"Ostwald ripening (small particles dissolve, large ones grow), the "
"Laplace pressure inside small droplets and particles (delta-p = "
"2*gamma/R), and capillary forces that can crush or assemble "
"nanostructures. Surface stress - the work to stretch a surface "
"elastically, distinct from the work to create it - can even compress "
"the lattice of a nanoparticle measurably. For a 10-nanometre gold "
"particle, the Laplace pressure reaches about 300 MPa, comparable to "
"the yield strength of bulk metals: the particle squeezes itself. "
"Typical values: water 0.072 J/m^2, most metals 1-2 J/m^2, ceramics "
"higher. Every nanomechanics calculation that ignores surfaces is "
"missing a load comparable to the applied loads."),
"how_it_works": (
"Surface energy enters mechanics through the Laplace pressure: a curved "
"surface with energy gamma pulls inward with pressure 2*gamma/R for a "
"sphere (gamma/R for a cylinder, by the Young-Laplace equation). For a "
"water droplet of R = 100 nm this is 1.44 MPa; for a gold nanoparticle "
"of R = 10 nm with gamma = 1.5 J/m^2 it is 300 MPa - a self-imposed "
"hydrostatic compression that shifts lattice parameters and melting "
"points. Surface stress f (force per length) acts like a membrane "
"tension on solids and can bend thin cantilevers: Stoney's formula "
"relates the curvature of a coated cantilever to the surface stress, "
"the basis of many chemical sensors. The demo computes Laplace "
"pressures for droplets and particles across sizes, showing the 1/R "
"explosion that makes surface energy the ruling force below ~100 nm."),
"key_points": [
"Surface energy gamma: the cost of unsatisfied bonds, J/m^2.",
"Laplace pressure 2*gamma/R: 300 MPa inside a 10 nm gold particle.",
"Drives sintering, Ostwald ripening, capillary assembly and collapse.",
"Surface stress (stretching a surface) differs from surface energy (creating it).",
"Stoney's formula: surface stress bends cantilevers - the basis of surface-stress sensors.",
"Below ~100 nm, surface loads rival or exceed applied loads."],
"requirements": [
"Pressure as force per area.",
"The sphere surface/volume formulas.",
"A calculator."],
"standards": [
"Surface energy in J/m^2 (= N/m).",
"Laplace pressure in Pa.",
"Surface stress distinguished from surface energy in every statement."],
"citations": [C_ISRAEL, C_BHUSHAN_NM, C_NIX],
"sig_lens": (
"Signature take: a surface is a wound that never heals, and it pulls "
"on everything around it trying to close. The Signature builder does "
"not fight this pull - he budgets for it like a load, because at the "
"nanoscale it IS a load, hundreds of megapascals strong, arriving "
"free with every surface ever made."),
},
{
"key": "surface_forces",
"name": "Van der Waals, Capillary, and Electrostatic Forces at the Nanoscale",
"group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
"description": (
"Three forces rule the nanoscale, and gravity is not among them. Van der "
"Waals forces - the correlated flicker of electron clouds, formalized by "
"Hamaker (1937) and Lifshitz (1956) - attract all matter at short range "
"with a strength set by the Hamaker constant A (~1e-19 J for most solids). "
"Capillary forces from condensed water bridges can exceed van der Waals "
"by an order of magnitude in humid air and are the main cause of stiction "
"in microdevices. Electrostatic forces from trapped charges or applied "
"voltages are the long-range actors, reaching across gaps where the "
"others have faded. Together they decide whether an AFM tip snaps into "
"contact, whether a nanoparticle sticks to a surface, whether two "
"cantilevers weld themselves together, and how friction really works at "
"a single asperity. The worker's numbers: a 10 nm tip 0.5 nm from a "
"surface feels ~400 pN of van der Waals pull; a water meniscus around "
"the same tip pulls with ~9 nN - twenty times more."),
"how_it_works": (
"Van der Waals force between a sphere of radius R and a flat plate at gap "
"D is F = A*R/(6*D^2): linear in radius, inverse-square in gap, which is "
"why it is negligible at 100 nm separation and overwhelming at 0.5 nm. "
"The Hamaker constant comes from the materials' dielectric spectra via "
"Lifshitz theory; combining rules estimate A_12 ~ sqrt(A_11 * A_22). "
"Capillary force for a sphere on a plate in humidity is F ~ 4*pi*R*gamma "
"(for zero contact angle), independent of humidity over a wide range - "
"the bridge is always there once it forms. Electrostatic force between "
"charged surfaces follows Coulomb's law with the local geometry; even "
"'uncharged' insulators carry patch charges that matter at nanometre "
"gaps. The demo computes the van der Waals and capillary forces for a "
"10 nm tip and shows the crossover: capillarity wins wherever water can "
"condense, which is why dry nitrogen is a nanomechanics laboratory's "
"best friend."),
"key_points": [
"Van der Waals: F = A*R/(6*D^2) sphere-plate; ~400 pN for a 10 nm tip at 0.5 nm.",
"Capillary: F ~ 4*pi*R*gamma; ~9 nN for the same tip - 20x the van der Waals pull.",
"Electrostatic: the long-range actor; patch charges matter at nanometre gaps.",
"Hamaker constants ~1e-19 J; Lifshitz theory derives them from dielectric spectra.",
"Humidity control is force control: dry the air, kill the meniscus.",
"These three forces ARE adhesion, stiction, and single-asperity friction."],
"requirements": [
"Force in newtons; comfort with pN (1e-12 N) and nN (1e-9 N).",
"Inverse-square intuition.",
"A calculator."],
"standards": [
"Forces in N with pN/nN submultiples; energies in J.",
"Hamaker constants in J; surface tension in N/m.",
"Humidity stated whenever capillary forces are discussed."],
"citations": [C_HAMAKER, C_LIFSHITZ, C_ISRAEL, C_BUTT],
"sig_lens": (
"Signature take: at the nanoscale, nothing is ever truly 'not touching'. "
"Every surface reaches out with invisible hands - electron flicker, "
"water bridges, stray charge - and the hands are strong enough to weld "
"machines shut. Signature design treats empty space as a crowded room "
"and gives every gap a bodyguard of dryness or distance."),
},
{
"key": "elastic_beams",
"name": "Bending a Nanobeam: Euler-Bernoulli Shrunk a Million Times",
"group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
"description": (
"The cantilever - a beam clamped at one end - is the workhorse of "
"nanomechanics: it is the AFM probe, the NEMS resonator, the "
"surface-stress sensor, the mass balance. Its mechanics come straight "
"from Euler-Bernoulli beam theory, which survives miniaturization "
"beautifully: stiffness k = 3*E*I/L^3, resonant frequency f = "
"(1/2*pi)*sqrt(k/m_eff), static deflection delta = F/k. For a silicon "
"cantilever 10 um long, 1 um wide, 100 nm thick: k ~ 0.04 N/m (soft as "
"a whisper), f ~ 1.38 MHz, and a single nanonewton bends the tip by "
"~24 nm. Shrink all dimensions by 10 and the stiffness drops 1000x "
"while the frequency rises 10x - the scaling every resonator designer "
"rides. Doubly-clamped beams (bridges) are stiffer by ~16x and ring "
"higher; their tension can be tuned electrically, which is how "
"nanotube radios tune stations. This entry is the reference for every "
"beam calculation later in the database."),
"how_it_works": (
"Euler-Bernoulli assumes plane cross-sections stay plane: bending moment "
"M = E*I*kappa, with I the area moment of inertia (w*t^3/12 for a "
"rectangular beam) and kappa the curvature. Integrating along the beam "
"with the clamped-free boundary conditions gives the famous results: "
"tip deflection delta = F*L^3/(3*E*I), stiffness k = 3*E*I/L^3, and the "
"first resonance f_1 = (1.875^2/2*pi)*(t/L^2)*sqrt(E/(12*rho)). The "
"effective mass for dynamics is 0.24 times the beam mass for a "
"cantilever (0.396 for a doubly-clamped beam). Residual stress and "
"surface stress add corrections at the nanoscale but rarely exceed "
"10-20%. The demo builds the reference silicon cantilever, computing "
"stiffness, frequency, effective mass, and static deflection, and "
"verifies the scaling: halve the length, stiffness goes up 8x."),
"key_points": [
"Cantilever: k = 3EI/L^3, f = (1/2pi)*sqrt(k/m_eff), delta = F/k.",
"Reference: 10x1x0.1 um Si beam -> k = 0.042 N/m, f = 1.38 MHz.",
"Doubly-clamped beams are ~16x stiffer; tension tunes their frequency.",
"m_eff = 0.24*m (cantilever), 0.396*m (bridge).",
"Scaling: k ~ t^3*w/L^3, f ~ t/L^2 - shrink for speed, thicken for stiffness.",
"Surface and residual stress correct the ideal values by ~10-20%."],
"requirements": [
"The stress/strain entry.",
"Area moment of inertia I = w*t^3/12 (given, not derived).",
"A calculator."],
"standards": [
"Beam dimensions L x w x t in m; stiffness in N/m; frequency in Hz.",
"Mode shapes identified by number (first flexural, etc.).",
"Boundary conditions stated (cantilever vs bridge)."],
"citations": [C_CLELAND, C_LANDAU, C_SCHMID],
"sig_lens": (
"Signature take: the cantilever is the finger of nanomechanics - it "
"feels what eyes cannot see. Every AFM image, every mass measurement, "
"every surface-stress reading is a cantilever bending and telling the "
"truth about it. Signature instruments are built around this one "
"honest beam, because a beam cannot lie about a force."),
},
{
"key": "nanoindentation",
"name": "Nanoindentation: Reading Hardness from a Force Curve",
"group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
"description": (
"Nanoindentation is the hardness test shrunk to the nanoscale: a diamond "
"tip (usually a three-sided Berkovich pyramid) is pressed into the "
"material while force and displacement are recorded continuously, "
"producing a load-displacement curve. From that one curve come hardness "
"H = P_max/A (resistance to permanent deformation) and elastic modulus "
"via the Oliver-Pharr analysis of the unloading slope. A modern "
"instrument resolves forces below a micronewton and depths below a "
"nanometre, probing thin films, coatings, individual phases, and "
"single nanostructures. The classic signatures: loading curves that "
"rise smoothly for homogeneous material and show pop-ins (sudden "
"displacement bursts) when dislocations nucleate or cracks start; "
"unloading curves whose initial slope is pure elastic recovery. "
"Example numbers: 500 uN into fused silica to 100 nm depth gives H ~ "
"2.1 GPa; the same test on sapphire gives H ~ 30 GPa. Every coating "
"laboratory and thin-film group owns one of these machines."),
"how_it_works": (
"The experiment: load P ramps up to P_max while depth h is recorded, "
"then unloads. The contact depth h_c = h_max - epsilon*P_max/S, where S "
"= dP/dh is the initial unloading stiffness and epsilon = 0.75 for a "
"Berkovich tip. The projected contact area comes from the tip's area "
"function, A = 24.5*h_c^2 for an ideal Berkovich (real tips are "
"calibrated against fused silica). Hardness H = P_max/A. The reduced "
"modulus E_r = (sqrt(pi)/(2*beta))*S/sqrt(A) with beta = 1.034, and the "
"sample modulus follows from 1/E_r = (1-nu^2)/E + (1-nu_i^2)/E_i with "
"diamond indenter constants. Pile-up (soft materials) and sink-in "
"(hard materials) bias the area and must be corrected. The demo "
"reduces a synthetic 500 uN curve to H = 2.15 GPa and E_r = 266 GPa, "
"the full Oliver-Pharr pipeline in miniature."),
"key_points": [
"One load-displacement curve yields hardness H = P_max/A and modulus via Oliver-Pharr.",
"h_c = h_max - 0.75*P_max/S; A = 24.5*h_c^2 for ideal Berkovich.",
"Unloading slope S is pure elastic recovery: S -> reduced modulus.",
"Pop-ins mark dislocation nucleation or cracking events.",
"Pile-up/sink-in correct the contact area; tip area function calibrated on fused silica.",
"Depth resolution < 1 nm, force resolution < 1 uN: films, phases, and nanostructures."],
"requirements": [
"Stress/strain vocabulary.",
"Derivatives as slopes (S = dP/dh).",
"A calculator."],
"standards": [
"Hardness in GPa; modulus in GPa; depths in nm; loads in uN/mN.",
"Tip geometry and area function stated; beta = 1.034 for Berkovich.",
"Poisson's ratio assumed value stated explicitly."],
"citations": [C_OLIVER92, C_OLIVER04, C_GERBERICH],
"sig_lens": (
"Signature take: the indenter asks the material one rude question - "
"how much force does it take to leave a permanent mark? - and the "
"material answers in the shape of its unloading curve. Signature "
"testing trusts the unloading, because loading is full of excuses "
"and unloading is pure elasticity telling the truth."),
},
{
"key": "oliver_pharr",
"name": "The Oliver-Pharr Method: Unloading Curves to Modulus",
"group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
"description": (
"Oliver and Pharr's 1992 method (refined in 2004) is the standard "
"algorithm that turned nanoindentation from a hardness tester into a "
"modulus meter. Its insight: the very start of unloading is purely "
"elastic - the plastic zone sits frozen while the elastic field "
"relaxes - so the initial unloading stiffness S = dP/dh encodes the "
"elastic modulus through Sneddon's elastic contact solution, "
"independent of the plastic mayhem underneath. The recipe: fit the "
"top of the unloading curve to P = alpha*(h - h_f)^m, differentiate "
"for S, compute contact depth and area, then E_r = "
"(sqrt(pi)/2*beta)*S/sqrt(A). The method assumes sink-in contact "
"(no pile-up), time-independent behavior (no creep during the hold), "
"and a calibrated area function. Worked example: S = 200 uN/nm, h_c "
"= 80 nm into a stiff ceramic gives E_r = 433 GPa, converting to E "
"= 633 GPa with nu = 0.3. When the assumptions break - soft metals "
"that pile up, polymers that creep - the method warns you through "
"its own diagnostics (m far from 1.5, h_f/h_max ratios)."),
"how_it_works": (
"Step by step: (1) From the unloading data, fit P = alpha*(h-h_f)^m "
"over the top 50-80% of the unloading curve; m ~ 1.2-1.6 for Berkovich. "
"(2) S = alpha*m*(h_max - h_f)^(m-1). (3) h_c = h_max - "
"epsilon*P_max/S, epsilon = 0.75. (4) A = area function(h_c), ideal "
"24.5*h_c^2. (5) E_r = sqrt(pi)*S/(2*beta*sqrt(A)), beta = 1.034. "
"(6) 1/E_r = (1-nu^2)/E + (1-nu_i^2)/E_i; with diamond E_i = 1141 GPa, "
"nu_i = 0.07. The demo runs this pipeline on the worked example, "
"landing on E_r = 432.9 GPa and E = 633 GPa, and shows the "
"sensitivity: a 5% error in S is a 5% error in E_r, but a 5% error in "
"h_c is a 10% error in area and modulus - depth calibration is king."),
"key_points": [
"Initial unloading is purely elastic: S = dP/dh gives modulus via Sneddon's solution.",
"Pipeline: fit P = alpha*(h-h_f)^m -> S -> h_c -> A -> E_r -> E.",
"epsilon = 0.75, beta = 1.034 for Berkovich; diamond E_i = 1141 GPa.",
"Assumes sink-in, no creep, calibrated area function.",
"Diagnostics: m far from ~1.5 or odd h_f/h_max flags bad assumptions.",
"Depth errors hurt twice (area ~ h_c^2): calibrate depth first."],
"requirements": [
"The nanoindentation entry.",
"Power-law fitting concept (fit quality judged by eye here).",
"A calculator."],
"standards": [
"Unloading fit range reported (e.g. top 60% of unload).",
"m, alpha, h_f reported with the fit.",
"Assumed nu stated; indenter constants stated."],
"citations": [C_OLIVER92, C_OLIVER04],
"sig_lens": (
"Signature take: Oliver and Pharr found the one honest moment in a "
"violent experiment - the first instant of retreat, when the "
"material relaxes elastically and forgets the plastic damage below. "
"Signature analysis looks for exactly such moments: the clean "
"signal hiding inside the messy event."),
},
{
"key": "afm_mechanics",
"name": "AFM Force Spectroscopy: Pulling Single Molecules Apart",
"group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
"description": (
"An atomic force microscope is a cantilever with a sharp tip, and in "
"force-spectroscopy mode it becomes the most delicate tensile tester "
"ever built: it stretches single molecules and measures the force, "
"pico-newton by pico-newton. The cantilever obeys Hooke's law F = k*x "
"with k ~ 0.01-1 N/m (calibrated by the thermal-noise method of Hutter "
"and Bechhoefer, 1993); the tip deflection x is read by a laser with "
"sub-angstrom resolution. Pull a DNA molecule and the force-extension "
"curve follows the worm-like-chain model, rising gently then "
"diverging as the chain straightens - 2 pN at 90% extension, 200 pN "
"at 99% for a 1000 nm strand. Pull the muscle protein titin and each "
"domain unfolds with a sawtooth pop at ~200 pN. Push into a cell and "
"the Hertz contact fit gives its stiffness (~1 kPa for a soft cell). "
"AFM force spectroscopy turned mechanics into a single-molecule "
"science and remains the standard tool for biomolecular mechanics."),
"how_it_works": (
"The cantilever base is driven toward and away from the sample while "
"deflection is recorded: approach, contact, indentation or molecule "
"stretching, retraction with adhesion pull-off. Force = k * deflection, "
"with k from the thermal calibration (equipartition: k = k_B*T/<x^2>). "
"For polymer stretching, the worm-like-chain interpolation F = "
"(k_B*T/L_p)*[1/(4(1-x/L)^2) - 1/4 + x/L] (Marko and Siggia, 1995) fits "
"the curve with persistence length L_p and contour length L as the "
"prizes - DNA gives L_p ~ 50 nm. For indentation of soft samples the "
"Hertz or Sneddon contact models convert force-depth into modulus. "
"The demo computes the WLC force at 90% and 99% extension for DNA "
"(2.11 pN and 205.6 pN), showing the entropic spring stiffening over "
"two orders of magnitude in the last 9% of stretch."),
"key_points": [
"AFM cantilever: F = k*x, k ~ 0.01-1 N/m, thermal-noise calibrated.",
"Worm-like-chain: F = (kT/Lp)[1/4(1-x/L)^2 - 1/4 + x/L]; DNA Lp ~ 50 nm.",
"DNA: 2 pN at 90% extension, ~200 pN at 99%: entropic stiffening.",
"Titin domains unfold at ~200 pN each: the sawtooth fingerprint.",
"Cell indentation + Hertz fit -> cell modulus (~0.1-10 kPa).",
"Force resolution ~10 pN, displacement resolution ~0.1 nm."],
"requirements": [
"Hooke's law.",
"The elastic-beams entry (the cantilever is the instrument).",
"A calculator."],
"standards": [
"Cantilever k reported with calibration method (thermal noise).",
"Loading rate stated: biomolecular rupture forces are rate-dependent.",
"Buffer/temperature stated for biological measurements."],
"citations": [C_BUTT, C_CAPPELLA, C_HUTTER, C_MARKO, C_BUSTAMANTE],
"sig_lens": (
"Signature take: the AFM does not grab the molecule - it invites it "
"to stretch and listens to its resistance, pico-newton by pico-newton. "
"That is the Signature way of measuring: never break the thing to "
"learn its strength if you can persuade it to confess instead."),
},
{
"key": "nanowires",
"name": "Nanowires in Tension: Stronger Than Steel, Tested One at a Time",
"group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
"description": (
"A nanowire pulled in tension is the purest strength experiment in "
"mechanics: a single crystal, often defect-free, loaded uniformly until "
"it breaks. The results rewrote expectations. Gold nanowires 100 nm in "
"diameter break near 1.5 GPa - more than ten times bulk gold. Silicon "
"nanowires reach several GPa. Zinc oxide, silicon carbide, and metallic "
"glass nanowires all show strengths far above their bulk forms and "
"elastic strains of several percent that bulk samples could never "
"survive. The testing is heroic: wires are grown or etched, picked up "
"with nanomanipulators inside electron microscopes, glued or clamped "
"across a tensile stage, and pulled while the load cell (often an AFM "
"cantilever) and the elongation (from micrographs) are recorded. The "
"lesson, confirmed wire after wire: remove the flaws and the material "
"approaches its ideal strength, the stress at which the lattice itself "
"becomes unstable - roughly E/10. Nanowire tension is the experimental "
"proof of 'smaller is stronger.'"),
"how_it_works": (
"Uniaxial tension: sigma = F/A, epsilon = delta/L, uniform by Saint-"
"Venant's principle away from the grips. The ideal (defect-free) "
"tensile strength is ~E/10 from Frenkel's lattice-shear argument "
"adapted to tension. Real nanowires fall between bulk strength and "
"ideal strength depending on diameter: at 100 nm, surface dislocation "
"nucleation controls yielding; below ~20 nm, even nucleation is hard "
"and strengths crowd the ideal limit. Worked example: a gold wire d = "
"100 nm (A = 7.85e-15 m^2), L = 2 um, breaking at sigma = 1.5 GPa, "
"gives F_break = 11.8 uN, breaking strain epsilon = 1.9%, elongation "
"38 nm - all easily resolved by modern stages. The demo computes "
"these and the ratio to bulk gold (~120 MPa): 12.5x, the size effect "
"as a single number."),
"key_points": [
"Nanowire tension: the purest strength test - single crystal, uniform load.",
"Au 100 nm wire: breaks at 1.5 GPa / 11.8 uN, 12.5x bulk strength.",
"Ideal strength ~ E/10: the lattice-instability ceiling.",
"Strength rises as diameter falls: fewer flaws, harder dislocation nucleation.",
"Elastic strains of several percent: impossible in bulk, routine in nanowires.",
"Grips and alignment are the experiment: Saint-Venant needs uniform loading."],
"requirements": [
"The stress/strain entry.",
"Circle area from diameter.",
"A calculator."],
"standards": [
"Diameter, length, and crystal orientation reported with every strength.",
"Loading rate and temperature stated.",
"Strength quoted as engineering stress at fracture unless noted."],
"citations": [C_WONG, C_UCHIC, C_FRENKEL, C_GERBERICH],
"sig_lens": (
"Signature take: pull a wire with no flaws and it shows you what the "
"material was always capable of - ten times the textbook strength. "
"The textbook was describing the flaws, not the material. Signature "
"engineering builds at the scale where the flaws run out, and takes "
"the real number."),
},
{
"key": "hall_petch",
"name": "Hall-Petch and Its Breakdown: Grain Size vs Strength",
"group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
"description": (
"The Hall-Petch relation, sigma_y = sigma_0 + k/sqrt(d) (Hall, 1951; "
"Petch, 1953), is the oldest size effect in metallurgy: shrink the "
"grain size d and the metal gets stronger, because grain boundaries "
"block dislocation motion and dislocations pile up against them. It "
"works beautifully from millimetres down to about 100 nanometres - "
"copper climbs from ~70 MPa at 10 um grains to ~470 MPa at 100 nm. "
"Then, around 10-20 nm, the law breaks: metals get SOFTER as grains "
"shrink further. This inverse Hall-Petch effect (Schiotz et al., "
"1998, in simulation; confirmed experimentally) happens because the "
"grains become too small to hold a dislocation pile-up at all - "
"deformation switches to grain-boundary sliding and rotation, and "
"boundaries, now a large volume fraction, are the weak phase. The "
"peak strength sits near 10-15 nm for many metals: the strongest "
"copper ever made has ~15 nm grains. Nanomechanics lives on both "
"sides of this peak, and quoting Hall-Petch below 20 nm without the "
"breakdown is simply wrong."),
"how_it_works": (
"Classic regime: dislocations emitted from a source pile up at a "
"grain boundary; the stress concentration scales as sqrt(d), so "
"yielding needs sigma ~ 1/sqrt(d). Fit copper with sigma_0 = 25 MPa "
"and k = 0.14 MPa*m^1/2: d = 10 um -> 69 MPa; d = 1 um -> 165 MPa; "
"d = 100 nm -> 468 MPa. Breakdown regime: below a critical size d_c "
"~ 10-20 nm, the pile-up holds fewer than one dislocation, so the "
"mechanism dies; grain-boundary-mediated flow takes over with an "
"effective viscosity, and strength falls as d shrinks. The demo "
"computes the Hall-Petch curve for copper, marks the peak near 15 "
"nm, and shows the turnover - the most important shape in "
"nanocrystalline metallurgy, and the reason 'nanocrystalline' is an "
"optimum, not a limit."),
"key_points": [
"Hall-Petch: sigma_y = sigma_0 + k/sqrt(d); grain boundaries block dislocations.",
"Copper: 69 MPa at 10 um -> 468 MPa at 100 nm.",
"Breakdown below ~10-20 nm: grains too small for pile-ups; boundaries slide instead.",
"Inverse Hall-Petch: strength FALLS as grains shrink past the peak.",
"Peak strength near 10-15 nm for many metals: nanocrystalline is an optimum.",
"Mechanism map matters more than the formula: know which regime you are in."],
"requirements": [
"Square roots.",
"The dislocation idea from the scale-effects entry.",
"A calculator."],
"standards": [
"sigma_0 and k quoted with units (MPa, MPa*m^1/2) and the fitted range.",
"Grain size as mean linear intercept, method stated.",
"Breakdown flagged whenever d < 50 nm is discussed."],
"citations": [C_HALL, C_PETCH, C_SCHIOTZ, C_MEYERS],
"sig_lens": (
"Signature take: every strengthening trick has a scale where it "
"inverts - push grain refinement past ~15 nm and the boundaries you "
"were using as walls become the corridors of failure. Signature "
"design finds the peak and builds there, instead of worshipping "
"'smaller' past the point where smaller turns traitor."),
},
{
"key": "nanotubes",
"name": "Carbon Nanotube Mechanics: The One-Terapascal Spring",
"group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
"description": (
"The carbon nanotube is nanomechanics' flagship structure: a rolled "
"graphene sheet, 1-2 nm in diameter, with axial modulus ~1 TPa "
"(five times steel), tensile strength up to ~100 GPa (fifty times "
"steel), and the ability to bend and buckle reversibly at enormous "
"strains. Treacy, Ebbesen and Gibson (1996) first measured the "
"modulus from thermal vibration amplitudes in a TEM; Krishnan et al. "
"(1998) refined it to ~1.25 TPa; Poncharal et al. (1999) drove "
"nanotubes into electromechanical resonance; Falvo et al. (1997) "
"bent them with an AFM tip and watched them buckle and recover; Yu "
"et al. (2000) pulled ropes to breaking. A 1.4 nm single-wall tube, "
"1 um long: axial stiffness 1.5 N/m, cantilever resonance 7.5 MHz, "
"breaking force ~150 nN. Nanotubes are also the ultimate test of "
"continuum shell theory at the atomic limit - and the theory, with "
"wall thickness 0.34 nm, passes. Every claim about 'strongest "
"material' is measured against this tube."),
"how_it_works": (
"Model the tube as a thin cylindrical shell: cross-section A = pi*d*t "
"(t = 0.34 nm), bending inertia I = pi*r^3*t. Axial stiffness k = "
"E*A/L; with E = 1 TPa, d = 1.4 nm, L = 1 um: k = 1.50 N/m - a soft "
"spring made of the stiffest material known, because it is so thin. "
"Cantilever resonance f = (1.875^2/2*pi)*(1/L^2)*sqrt(E*I/(rho*A)) "
"gives 3.72 MHz. Tensile breaking force = sigma_max * A with sigma_max "
"~ 100 GPa gives ~150 nN. Thermal vibration method: the mean-square "
"tip amplitude <u^2> = k_B*T*L^3/(3*E*I) lets the modulus be read from "
"a blurry TEM image - equipartition as a measuring instrument. The "
"demo computes the spring constant, resonance, and breaking force, "
"and shows the paradox resolved: 1 TPa material, 1.5 N/m spring - "
"geometry is destiny."),
"key_points": [
"SWCNT: E ~ 1 TPa, strength to ~100 GPa, reversible buckling.",
"d=1.4 nm, L=1 um: axial k = 1.5 N/m, cantilever f = 3.7 MHz, F_break ~ 150 nN.",
"Thin-shell model (t = 0.34 nm) works down to single atoms: continuum's finest hour.",
"Thermal-vibration TEM: modulus read from blur via equipartition.",
"Bending/buckling is reversible: the tube kinks but does not break (Falvo 1997).",
"The benchmark every 'strongest material' claim is measured against."],
"requirements": [
"The elastic-beams entry.",
"Cylinder shell formulas (given).",
"A calculator."],
"standards": [
"Tube diameter, wall count, and length stated with every modulus.",
"Measurement method stated (tension, resonance, thermal vibration, AFM bending).",
"E in TPa; breaking stress distinguished from yield."],
"citations": [C_TREACY, C_KRISHNAN, C_PONCHARAL, C_FALVO, C_YU],
"sig_lens": (
"Signature take: the nanotube is proof that perfection is a "
"mechanical strategy - a flawless lattice of carbon, one nanometre "
"wide, out-pulls steel fifty to one. Signature building chases "
"this lesson everywhere: remove the defects and the bonds will "
"carry absurd loads without complaint."),
},
{
"key": "graphene",
"name": "Graphene Mechanics: One Atom Thick, Strongest Material Known",
"group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
"description": (
"Graphene - a single atomic layer of carbon - forced mechanics to "
"invent two-dimensional elasticity: its stiffness is quoted as a "
"2D modulus E_2D = 340 N/m (Lee et al., Science 2008), which "
"converts to ~1 TPa in 3D units using the 0.335 nm layer spacing, "
"and its intrinsic breaking strength is 42 N/m (~130 GPa), the "
"highest ever measured. Lee's experiment is a classic: graphene "
"suspended over micron-scale holes, pressed with a diamond AFM tip, "
"the force-deflection curve fitted to membrane theory F = "
"(pi*sigma_0)*delta + (E_2D*q^3/a^2)*delta^3. The cubic term - "
"pure stretching, no bending possible in one atom - gives the "
"modulus directly. Graphene also made resonators (Bunch et al., "
"2007: MHz frequencies from an atom-thick drum) and showed that "
"defects degrade strength far faster than stiffness. It is the "
"ultimate membrane: nothing thinner can exist, nothing stiffer per "
"weight has been found."),
"how_it_works": (
"A suspended circular membrane under a central point load obeys F = "
"(pi*sigma_0)*delta + (E_2D*q^3/a^2)*delta^3, where sigma_0 is the "
"pretension, a the hole radius, and q ~ 1.02 a geometric factor. At "
"small deflection the linear pretension term dominates; at large "
"deflection the cubic stretching term takes over - fitting both "
"extracts sigma_0 and E_2D independently. With a = 500 nm and a "
"measured cubic coefficient C = 1.44e15 N/m^3, E_2D = C*a^2/q^3 = "
"340 N/m, and dividing by 0.335 nm gives E = 1.01 TPa. Breaking "
"occurs at ~2.9 uN load for these membranes, i.e. 42 N/m of line "
"force. The demo performs the fit inversion and the 2D-to-3D "
"conversion, showing why 2D units are the honest ones for a "
"one-atom material."),
"key_points": [
"Graphene: E_2D = 340 N/m (~1.01 TPa), breaking strength 42 N/m (~130 GPa).",
"Membrane indentation: F = (pi*sigma_0)*delta + (E_2D*q^3/a^2)*delta^3.",
"Cubic term = pure stretching: one atom cannot bend, only stretch.",
"2D units (N/m) are the honest units for atom-thick materials.",
"Defects hurt strength far more than stiffness.",
"Atom-thick drums resonate at MHz: Bunch et al. 2007."],
"requirements": [
"Cubic equations (fitting concept only).",
"The nanotubes entry for contrast.",
"A calculator."],
"standards": [
"2D modulus/strength in N/m; 3D conversions state the thickness assumed.",
"Hole radius and pretension reported with every indentation modulus.",
"Layer count verified (Raman or contrast) for 'graphene' claims."],
"citations": [C_LEE08, C_BUNCH],
"sig_lens": (
"Signature take: graphene is the end of the road for thinness - "
"you cannot make a material thinner than one atom, and at that "
"limit the strength per weight is the best the universe offers. "
"Signature design treats graphene as the existence proof: the "
"ceiling is real, it has been measured, now build toward it."),
},
{
"key": "nanotribology",
"name": "Nanotribology: Friction, Wear, and Stick-Slip at Atomic Scale",
"group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
"description": (
"Nanotribology studies friction, wear, and lubrication one asperity "
"at a time - a single AFM tip sliding on a crystal, where friction "
"is not a coefficient but a movie of atomic stick and slip. Mate et "
"al. (1987) saw the first atomic stick-slip: the tip sticks in a "
"lattice hollow, the cantilever winds up, then slips one atomic "
"spacing with a snap. The Prandtl-Tomlinson model captures it: a "
"tip dragged by a spring over a periodic potential slips when the "
"spring force exceeds the potential's max slope. Key results: "
"friction is often proportional to true contact area, not load "
"(breaking Amontons' law at the single asperity); friction can "
"vanish in incommensurate contacts (structural superlubricity, "
"friction coefficients ~0.001); and Mo, Turner and Szlufarska (2009) "
"showed friction laws change character with tip size and load. "
"Measured the honest way - a friction loop (trace minus retrace "
"divided by two): 59 nN of friction at 100 nN load gives mu = 0.59 "
"for a sharp tip on a hard surface, while graphite on graphite can "
"be a thousand times slipperier."),
"how_it_works": (
"The friction force microscope drags the tip laterally and records "
"the torsional twist of the cantilever: forward trace vs backward "
"retrace form a loop whose half-width is the friction force, "
"canceling topography artifacts. Stick-slip analysis: with lateral "
"stiffness k_lat and lattice spacing a, the maximum static friction "
"before a slip is ~2*pi*U_0/a for barrier U_0; for U_0 = 0.1 eV and "
"a = 0.25 nm, F_max = 0.40 nN per slip event, and hundreds of such "
"events per second make the macroscopic friction. Load dependence "
"follows the contact area (Hertz/JKR/DMT from the contact entry), "
"so F_f ~ L^(2/3) for a single elastic asperity, not F_f ~ L. The "
"demo reduces a friction loop (forward 60 nN, reverse -58 nN at "
"100 nN load) to mu = 0.59 and computes the Prandtl-Tomlinson slip "
"force, connecting the atomic snap to the measured friction."),
"key_points": [
"Single-asperity friction: stick-slip over atomic corrugation, seen since Mate 1987.",
"Friction loop: F_f = (trace - retrace)/2; example mu = 0.59.",
"Prandtl-Tomlinson: slip when spring force beats the potential slope; F_max ~ 0.4 nN.",
"F_f scales with contact AREA (~L^2/3), not load: Amontons breaks at one asperity.",
"Structural superlubricity: incommensurate contacts reach mu ~ 0.001.",
"Humidity, tip size, and load change the friction law itself (Mo et al. 2009)."],
"requirements": [
"The surface-forces and contact-mechanics entries.",
"Springs in series/parallel intuition.",
"A calculator."],
"standards": [
"Tip radius, material, and humidity stated with every friction value.",
"Scan speed and direction stated (friction is rate- and direction-sensitive).",
"mu distinguished from single-asperity shear strength."],
"citations": [C_MATE, C_GNECCO, C_MO, C_SZLUF, C_PERSSON],
"sig_lens": (
"Signature take: friction is not a property - it is a negotiation "
"between two surfaces, conducted one atomic snap at a time. Change "
"the lattice alignment and the same two materials go from grinding "
"to gliding. Signature machines are designed at the negotiation "
"table, choosing alignments and environments where the surfaces "
"agree to slip."),
},
{
"key": "contact_mechanics",
"name": "Contact Mechanics at the Nanoscale: Hertz, JKR, DMT",
"group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
"description": (
"Every touch at the nanoscale is a contact-mechanics problem: a tip "
"pressing a surface, a particle resting on a substrate, two "
"asperities colliding. Three theories divide the territory. Hertz "
"(1882): no adhesion, contact radius a = (3*P*R/4*E*)^(1/3), for "
"large stiff contacts at high load. JKR (Johnson-Kendall-Roberts, "
"1971): adhesion inside the contact, pull-off force (3/2)*pi*w*R, "
"for soft large contacts at low load. DMT (Derjaguin-Muller-Toporov, "
"1975): adhesion outside the contact, pull-off 2*pi*w*R, for stiff "
"small contacts. Tabor's parameter mu_T = (R*w^2/(E*^2*z_0^3))^(1/3) "
"chooses: mu_T > ~5 is JKR, mu_T < ~0.1 is DMT, between is Maugis' "
"transition (1992). Worked example: a silicon tip R = 50 nm at P = "
"100 nN gives Hertz radius 3.48 nm and mean pressure 2.63 GPa - "
"already near yield - with JKR pull-off 23.6 nN vs DMT 31.4 nN. "
"Carpick, Ogletree and Salmeron (1999) gave the general fitting "
"equation used to extract contact area from friction-vs-load data. "
"No AFM force curve is interpretable without this entry."),
"how_it_works": (
"Hertz: elastic sphere on flat, pressure distribution p = p_0*"
"sqrt(1-(r/a)^2), a^3 = 3*P*R/(4*E*), 1/E* = (1-nu_1^2)/E_1 + "
"(1-nu_2^2)/E_2. JKR adds surface energy w inside the contact: "
"a^3 = (3*R/4*E*)*(P + 3*pi*w*R + sqrt(6*pi*w*R*P + (3*pi*w*R)^2)), "
"finite contact area even at zero load, pull-off (3/2)*pi*w*R. DMT "
"keeps the Hertz shape and adds adhesion as an extra load: a^3 = "
"3*R*(P + 2*pi*w*R)/(4*E*), pull-off 2*pi*w*R. Tabor's mu_T weighs "
"the elastic deformation at pull-off against the range of surface "
"forces z_0 (~0.3 nm). The demo computes the Hertz contact for the "
"silicon tip (a = 3.43 nm, p_mean = 2.70 GPa), both pull-off forces, "
"and mu_T for R = 10 nm (0.049: DMT) and R = 100 um (1.06: "
"transition/JKR) - the map from tip size to theory."),
"key_points": [
"Hertz (no adhesion): a^3 = 3PR/4E*; Si tip 50 nm at 100 nN -> a = 3.43 nm, 2.70 GPa.",
"JKR (soft/large): pull-off (3/2)*pi*w*R; finite area at zero load.",
"DMT (stiff/small): pull-off 2*pi*w*R; Hertz shape plus adhesion load.",
"Tabor mu_T picks the theory: <0.1 DMT, >5 JKR, between Maugis.",
"Maugis-Dugdale (1992) bridges the transition; Carpick's equation fits real data.",
"Mean pressures reach GPa at nanonewton loads: contacts yield routinely."],
"requirements": [
"Cube roots.",
"The surface-forces entry (w, the work of adhesion).",
"A calculator."],
"standards": [
"Contact theory named (Hertz/JKR/DMT/Maugis) with every contact result.",
"R, E*, w, and z_0 stated; pull-off quoted as force.",
"Adhesion measured in the same environment as the contact (humidity!)."],
"citations": [C_HERTZ, C_JKR, C_DMT, C_TABOR, C_MAUGIS, C_CARPI],
"sig_lens": (
"Signature take: every touch is a negotiation between elasticity "
"pushing back and adhesion pulling in, and the Tabor parameter is "
"the referee that picks the rulebook. Signature contact design "
"chooses the tip size knowing which theory will judge it - because "
"arguing JKR numbers in DMT territory is arguing with the wrong "
"referee."),
},
{
"key": "adhesion",
"name": "Adhesion and Stiction: When Surfaces Won't Let Go",
"group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
"description": (
"Adhesion is the price of surface energy: separate two surfaces and "
"you pay 2*gamma per unit area (the work of adhesion w); bring them "
"together and they pay you, often more than you want. At the "
"nanoscale the bill dominates: an AFM tip snaps into contact from "
"nanometres away, nanoparticles stick where they land, and entire "
"microdevices die of stiction - suspended parts pulled down by "
"capillary or van der Waals forces during drying, never to move "
"again. The pull-off forces are the JKR/DMT values from the contact "
"entry (tens of nanonewtons for a 50 nm tip), but real surfaces are "
"rough: Greenwood and Williamson (1966) showed the real contact is "
"an archipelago of asperities, and adhesion scales with the "
"statistics of the highest ones. Defenses, in order of effectiveness: "
"dry the environment (kill capillarity), roughen deliberately "
"(reduce real contact area), coat with low-energy monolayers, and "
"design stiffness to beat the adhesion (the elastocapillary number). "
"Gecko setae are the existence proof that controlled adhesion at "
"the nanoscale is a feature, not just a failure."),
"how_it_works": (
"Work of adhesion w = gamma_1 + gamma_2 - gamma_12 (~0.05-0.1 J/m^2 "
"for van der Waals solids in air, up to ~1 J/m^2 for clean metals). "
"Pull-off for a sphere: JKR (3/2)*pi*w*R, DMT 2*pi*w*R - linear in "
"radius, which is why a 1 um particle sticks with micronewtons while "
"a 10 nm particle sticks with nanonewtons, but both stick relative "
"to their weight (adhesion beats gravity below ~100 um). Roughness "
"enters through the Greenwood-Williamson plasticity/adhesion indices: "
"if the elastic energy to flatten asperities exceeds w times the "
"area, contact is partial and adhesion drops. Stiction criterion for "
"a cantilever: restoring force k*gap vs adhesion force over the "
"contact zone - design k*gap >> F_adh with margin. The demo computes "
"pull-off vs particle radius from 10 nm to 100 um and the "
"adhesion-to-weight ratio, showing the crossover where sticking "
"beats falling - around tens of microns, the reason dust never falls "
"off clean surfaces."),
"key_points": [
"Work of adhesion w: the energy bill for separating surfaces, ~0.05-1 J/m^2.",
"Pull-off ~ pi*w*R: 10 nm particle sticks with nN, 1 um with uN.",
"Adhesion beats gravity below ~100 um: dust sticks, it does not fall.",
"Roughness (Greenwood-Williamson): real contact is an asperity archipelago.",
"Stiction kills MEMS: capillary/vdW collapse during drying; design stiffness to win.",
"Defenses: dry, roughen, coat, stiffen - in that order of leverage."],
"requirements": [
"The contact-mechanics and surface-forces entries.",
"Ratios (adhesion vs weight).",
"A calculator."],
"standards": [
"w quoted with environment (vacuum/air/humidity).",
"Roughness (rms, correlation length) stated with real-surface adhesion.",
"Stiction safety margin stated as force ratio."],
"citations": [C_JKR, C_DMT, C_GREENWOOD, C_ISRAEL, C_BHUSHAN_NM],
"sig_lens": (
"Signature take: adhesion is surface energy collecting its debt, "
"and at the nanoscale the debt collectors are stronger than the "
"machines. Signature design pays the debt on its own terms - dry "
"air, rough landscapes, stiff beams - or it does not build moving "
"parts at that scale at all."),
},
{
"key": "nems",
"name": "NEMS Resonators: Weighing Single Molecules with Vibrating Beams",
"group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
"description": (
"A nanoelectromechanical systems (NEMS) resonator is a vibrating beam "
"or membrane shrunk until its resonance climbs into the MHz-GHz range "
"and its mass falls to femtograms - at which point landing a single "
"molecule shifts the frequency measurably. The mass responsivity is "
"R = |df/dm| = f_0/(2*m_eff): a silicon beam 5 um x 500 nm x 100 nm "
"at f_0 = 10 MHz has R ~ 2.2e22 Hz/kg, so a 100 kDa protein "
"(1.66e-22 kg) shifts it by 3.6 Hz - detectable with 1 Hz frequency "
"noise, giving mass resolution ~28 kDa. Ekinci, Yang and Roukes "
"(2004) set the theoretical limits; Naik et al. (2009) demonstrated "
"single-molecule mass spectrometry; Chaste et al. (2012) reached "
"yoctogram (1e-24 g) resolution with a carbon nanotube resonator. "
"Beyond weighing: NEMS are clocks, filters, force sensors "
"(attonewton resolution), and the mechanical arms of quantum "
"experiments. Frequency stability - thermomechanical noise, "
"adsorption-desorption noise, temperature drift - is the entire "
"game, and the entire game is played in this entry's equations."),
"how_it_works": (
"Responsivity derivation: f = (1/2*pi)*sqrt(k/m_eff); a small added "
"mass dm at the antinode gives df = -f_0*dm/(2*m_eff), so R = "
"f_0/(2*m_eff). Maximize R by maximizing f_0 and minimizing m_eff: "
"short, thin, light beams of stiff material - the scaling that also "
"raises frequency. Mass resolution delta_m = (frequency noise)/R; "
"frequency noise comes from thermomechanical fluctuations "
"(Cleland and Roukes, 2002) and readout noise. Position matters: "
"mass at the node shifts nothing, at the antinode shifts most - "
"multimode readout (Naik 2009) solves for mass AND position. The "
"demo builds the reference 10 MHz beam, computes R = 2.17e22 Hz/kg, "
"the 3.60 Hz shift of a 100 kDa protein, and the 4.6e-23 kg mass "
"floor at 1 Hz noise - the complete weighing calculation."),
"key_points": [
"Mass responsivity R = f_0/(2*m_eff): frequency per unit mass.",
"Reference: 5x0.5x0.1 um Si beam at 10 MHz -> R = 2.17e22 Hz/kg.",
"100 kDa protein -> 3.6 Hz shift; 1 Hz noise -> 4.6e-23 kg resolution.",
"Single-molecule mass spec demonstrated (Naik 2009); yoctogram record (Chaste 2012).",
"Position matters: multimode readout finds mass AND landing site.",
"Frequency stability is the game: thermomechanical, adsorption, and thermal drift noise."],
"requirements": [
"The elastic-beams entry.",
"Derivatives as sensitivities.",
"A calculator."],
"standards": [
"f_0, m_eff, and R stated with every mass-sensing claim.",
"Frequency noise (Allan deviation) and averaging time stated.",
"Mass AND position for single-particle claims (multimode)."],
"citations": [C_EKMASS, C_NAIK, C_CHASTE, C_EKROU, C_CRAIGHEAD, C_CLELAND_NOISE],
"sig_lens": (
"Signature take: a NEMS beam is a scale that weighs ghosts - "
"molecules too small to see, registered as a few hertz of missing "
"frequency. Signature measurement trusts the shift, not the "
"eyeball: when the beam sings flat by 3.6 Hz, a hundred-kilodalton "
"ghost has landed, and the books balance."),
},
{
"key": "nanotube_resonance",
"name": "Nanotube and Nanowire Resonators: Gigahertz Mechanics",
"group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
"description": (
"Drive a carbon nanotube or nanowire into resonance and it becomes a "
"tuning fork for the gigahertz age: a doubly-clamped single-wall tube "
"200 nm long rings at 1.2 GHz, a silicon carbide beam reached 1 GHz "
"back in 2003 (Huang et al.), and Sazonova et al. (2004) built a "
"tunable nanotube oscillator - a radio with a one-nanometre antenna "
"element. The frequency formula for a doubly-clamped beam, f = "
"(beta^2/2*pi*L^2)*sqrt(E*I/(rho*A)) with beta = 4.73, shows the "
"levers: stiffness up, mass down, length down hard (1/L^2). "
"Electrostatic tuning pulls the frequency with a gate voltage via "
"tension - Sazonova's device tuned over MHz - and the resonance "
"detects mass, force, and charge with the sensitivities of the NEMS "
"entry. The quality factor Q = f/delta_f measures the ring-down: "
"nanotube resonators reach Q ~ 1e5 at low temperature, limited by "
"surface defects, clamping loss, and thermoelastic damping. These "
"devices are the bridge between the NEMS mass sensors and the "
"quantum-limited motion of the final entries."),
"how_it_works": (
"Doubly-clamped (bridge) boundary conditions quantize the bending "
"wavelengths: the first mode has beta*L = 4.730. With the thin-shell "
"tube values from the nanotube entry (E*I = 3.66e-25 N*m^2, rho*A = "
"2.02e-15 kg/m for d = 1.4 nm), L = 200 nm gives f = "
"(22.37/(2*pi*(2e-7)^2))*sqrt(3.66e-25/2.02e-15) = 1.20 GHz. "
"Detection: the vibrating tube modulates a capacitance or a field-"
"emission current; drive is electrostatic or magnetomotive. "
"Tension tuning: gate voltage pulls the tube, adding tension T, and "
"f rises as sqrt(1 + T*L^2/(pi^2*E*I)) - the guitar-string effect. "
"Q is measured from the ring-down or the linewidth; at room "
"temperature air damping and surface losses dominate, in vacuum at "
"cryogenic temperatures Q climbs past 1e5. The demo computes the "
"1.20 GHz resonance and the tension-tuning curve, showing how a few "
"volts on a gate play the nanotube like a string."),
"key_points": [
"Doubly-clamped tube 200 nm long: f = 1.20 GHz (beta = 4.73).",
"f = (beta^2/2*pi*L^2)*sqrt(EI/rho*A): short, stiff, light rings high.",
"Gate-voltage tension tuning: the nanotube as a tunable radio (Sazonova 2004).",
"SiC beam at 1 GHz (Huang 2003): the microwave milestone.",
"Q to 1e5 at low T: limited by surfaces, clamping, thermoelastic loss.",
"Readout via capacitance or field-emission modulation."],
"requirements": [
"The nanotubes and NEMS entries.",
"Square roots of ratios.",
"A calculator."],
"standards": [
"Boundary conditions (cantilever vs bridge) and mode number stated.",
"Q quoted with temperature, pressure, and drive level.",
"Tuning range quoted as df/dV at the operating point."],
"citations": [C_SAZONOVA, C_HUANG, C_PONCHARAL, C_SCHMID],
"sig_lens": (
"Signature take: a nanotube ringing at a gigahertz is a bell the "
"eye cannot see, tuned by a voltage like a guitar string. "
"Signature devices play these invisible bells on purpose - because "
"at a gigahertz, the bell hears molecules land, feels charges "
"pass, and counts time better than quartz ever could."),
},
{
"key": "fatigue_nano",
"name": "Fatigue of Nanostructures: A Billion Cycles of Tiny Bending",
"group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
"description": (
"Fatigue - failure under repeated loading far below the static "
"strength - does not spare the nanoscale; it just changes its "
"face. NEMS resonators vibrate billions of times per day, AFM tips "
"tap millions of times per image, and nanomechanical switches must "
"survive 1e9-1e12 cycles. The good news: defect-scarce nanostructures "
"resist crack nucleation far better than bulk - there are no "
"inclusions to start cracks from. The bad news: when a crack does "
"start in a 100 nm beam, it crosses the whole part in a few hundred "
"cycles, and surface damage (oxidation, wear, adsorption) accumulates "
"relentlessly because the surface IS the part. The S-N (stress vs "
"cycles) description survives: Basquin's law sigma_a = sigma_f'*"
"(2N)^b, with b ~ -0.1 for metals. Worked example for a gold "
"nanowire (sigma_f' = 2 GPa): 1e6 cycles at 469 MPa, 1e9 cycles at "
"235 MPa, and 300 MPa fails at ~8.7e7 cycles. Testing methods: "
"resonant fatigue (drive the beam at resonance and watch the "
"frequency drop as damage accumulates), AFM tapping fatigue, and "
"in-situ TEM cycling that films the crack atom by atom."),
"how_it_works": (
"Basquin's law is a power law on log-log axes: log(sigma_a) = "
"log(sigma_f') + b*log(2N). Fit b and sigma_f' from tests at "
"several stress amplitudes; extrapolate to the design life. For "
"the gold nanowire: at N = 1e6, 2N = 2e6, (2e6)^-0.1 = 0.234, "
"sigma_a = 469 MPa; at N = 1e9, sigma_a = 235 MPa. Inverting: at "
"sigma_a = 300 MPa, 2N = (300/2000)^(1/-0.1) = 1.73e8, N = 8.65e7 "
"cycles - about one day at 1 kHz, about 20 minutes at 70 MHz, "
"which is why resonator designers live in the very-high-cycle "
"regime. Damage mechanisms at the nanoscale: surface oxide "
"cracking, dislocation accumulation at the surface, and "
"adsorbate-assisted cracking. The demo builds the S-N curve, "
"inverts it for life at a given stress, and converts cycles to "
"wall-clock time at resonator frequencies - the number that "
"decides whether a NEMS switch lives a year or an afternoon."),
"key_points": [
"Basquin: sigma_a = sigma_f'*(2N)^b, b ~ -0.1 for metals.",
"Au nanowire: 469 MPa at 1e6 cycles, 235 MPa at 1e9 cycles.",
"300 MPa -> 8.65e7 cycles: minutes at MHz, a day at kHz.",
"Nanostructures resist nucleation (no inclusions) but cracks cross fast.",
"Surface damage dominates: oxidation, wear, adsorbates - the surface IS the part.",
"Test by resonant fatigue, AFM tapping, or in-situ TEM cycling."],
"requirements": [
"Logarithms and power laws.",
"The nanowires entry (strength baseline).",
"A calculator."],
"standards": [
"S-N data quoted with R ratio (min/max stress), frequency, environment.",
"b and sigma_f' fitted, not assumed, with the fitted range stated.",
"Runouts (survivors) distinguished from failures on the plot."],
"citations": [C_GERBERICH, C_BHUSHAN_NM, C_CLELAND],
"sig_lens": (
"Signature take: static strength is a boast; fatigue life is a "
" biography - it records every cycle the part ever lived. At the "
"nanoscale the biography is written fast, a billion cycles before "
"lunch, and the surface writes most of it. Signature parts are "
"designed for the biography, not the boast."),
},
{
"key": "fracture_nano",
"name": "Fracture at the Nanoscale: Flaws, Toughness, and Ideal Strength",
"group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
"description": (
"Griffith (1921) taught that brittle fracture starts at flaws: "
"fracture stress sigma_f = sqrt(2*E*gamma/(pi*a)) for a crack of "
"half-length a. At the nanoscale this formula becomes a promise - "
"shrink the flaw and the strength explodes. Glass with a 1 um flaw "
"breaks at 211 MPa; with a 10 nm flaw, at 2.11 GPa; with a 1 nm "
"flaw, at 6.7 GPa, within reach of the theoretical strength E/10. "
"Gao et al. (2003) proved the punchline: below a critical flaw size "
"a_c = 2*E*gamma/(pi*sigma_th^2) (~0.9 nm for glass), the material "
"becomes FLAW-INSENSITIVE - cracks do not concentrate stress "
"anymore, and the part reaches theoretical strength no matter "
"what. This is why nanoscale ceramics, thin films, and "
"nanocomposites can be both strong and reliable: their flaws are "
"below the sensitivity limit. Pugno and Ruoff's quantized fracture "
"mechanics (2004) rewrote Griffith for cracks that advance one "
"atomic spacing at a time. Toughness - resistance to crack growth, "
"K_Ic - remains the design property for larger parts, but at the "
"nanoscale the game is flaw control, not toughness."),
"how_it_works": (
"Griffith energy balance: a crack grows when the released elastic "
"energy exceeds the surface energy of the new faces, giving sigma_f "
"= sqrt(2*E*gamma/(pi*a)) in plane stress. Plug in glass (E = 70 "
"GPa, gamma = 1 J/m^2): a = 1 um -> 211 MPa; a = 10 nm -> 2.11 "
"GPa; a = 1 nm -> 6.68 GPa. The theoretical strength sigma_th ~ "
"E/10 = 7 GPa caps the curve. Set sigma_f = sigma_th and solve for "
"a: a_c = 2*E*gamma/(pi*sigma_th^2) = 0.91 nm - flaws smaller than "
"this cannot weaken the material, the Gao flaw-tolerance result "
"that explains teeth, nacre, and bone at their smallest scales. "
"The demo computes the Griffith curve across six decades of flaw "
"size, marks the flaw-tolerance threshold, and shows the ceiling - "
"the complete nanoscale fracture map in one plot's worth of "
"numbers."),
"key_points": [
"Griffith: sigma_f = sqrt(2*E*gamma/(pi*a)); smaller flaw, higher strength.",
"Glass: 211 MPa (1 um flaw) -> 2.11 GPa (10 nm) -> 6.68 GPa (1 nm).",
"Flaw tolerance below a_c ~ 0.9 nm: cracks stop mattering (Gao 2003).",
"Theoretical strength E/10 is the ceiling the curve approaches.",
"Quantized fracture mechanics: cracks advance one atomic spacing at a time.",
"At the nanoscale, design for flaw control; toughness rules larger parts."],
"requirements": [
"Square roots.",
"The stress/strain entry.",
"A calculator."],
"standards": [
"gamma identified as surface energy vs fracture energy (they differ).",
"Plane stress vs plane strain stated for K_Ic conversions.",
"Flaw size defined (half-length a) with the geometry."],
"citations": [C_GRIFFITH, C_GAO, C_PUGNO, C_FRENKEL],
"sig_lens": (
"Signature take: Griffith's formula is usually read as a curse - "
"flaws make everything weak. Read it backwards at the nanoscale "
"and it is a blessing: make the flaws small enough and they "
"retire, leaving the theoretical strength standing alone. "
"Signature materials are built below the flaw-sensitivity limit, "
"where perfection is not required because flaws have been "
"fired."),
},
{
"key": "md_mechanics",
"name": "Molecular Dynamics for Mechanics: Atoms as Springs",
"group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
"description": (
"Molecular dynamics (MD) is the computational microscope of "
"nanomechanics: atoms as point masses, interatomic potentials as "
"springs, Newton's laws integrated femtosecond by femtosecond. "
"From a Lennard-Jones pair potential U = 4*epsilon*((sigma/r)^12 - "
"(sigma/r)^6) comes the bond stiffness k = d^2U/dr^2 at the "
"minimum - 0.815 N/m per bond for argon - and from the stiffness "
"comes an estimated modulus (~2.1 GPa for solid argon, near the "
"measured 2-3 GPa): elasticity derived from atoms, no fitting. "
"Real potentials (EAM for metals, Tersoff/REBO for carbon, "
"Stillinger-Weber for silicon) capture bond breaking, letting MD "
"simulate nanoindentation, nanowire tension, crack tips, and "
"dislocation nucleation atom by atom. The method's honesty is its "
"limit: a million atoms for a nanosecond costs real computer "
"time, strain rates are 1e6-1e9 /s (far above experiment), and the "
"potential IS the physics - a bad potential is a fantasy. Used "
"right, MD is the only tool that watches a dislocation nucleate; "
"used wrong, it is a very expensive cartoon."),
"how_it_works": (
"Velocity Verlet integration: x(t+dt) = x(t) + v*dt + a*dt^2/2, "
"v(t+dt) = v(t) + (a(t)+a(t+dt))*dt/2 - symplectic, stable, and "
"energy-conserving to the order of the timestep. The demo does "
"two things honestly. First, analytic: from the Lennard-Jones "
"potential, k = 57.1*epsilon/sigma^2 = 0.815 N/m for argon, bond "
"vibration frequency 0.558 THz, modulus estimate k/r_0 = 2.13 "
"GPa. Second, numeric: a velocity-Verlet oscillator integrated "
"for 2000 steps of 1 fs, verifying total-energy drift below 1e-4 "
"relative - the conservation check every real MD run must pass. "
"The numbers connect: the same curvature that sets the "
"vibration frequency sets the elastic modulus, which is why "
"measuring one predicts the other."),
"key_points": [
"MD: atoms + potentials + Newton's laws, femtosecond steps.",
"Lennard-Jones argon: k = 0.815 N/m/bond -> E ~ 2.13 GPa from atoms alone.",
"Velocity Verlet: symplectic, energy drift < 1e-4 is the honesty check.",
"Real potentials: EAM (metals), Tersoff/REBO (carbon), Stillinger-Weber (Si).",
"Limits: 1e6 atoms-ns costs; strain rates 1e6-1e9 /s; the potential IS the physics.",
"The only tool that films dislocation nucleation atom by atom."],
"requirements": [
"Newton's second law.",
"Derivatives as slopes/curvatures.",
"A Python interpreter for the demo (stdlib only)."],
"standards": [
"Potential named and cited with every MD result.",
"System size, timestep, and strain rate stated.",
"Energy conservation reported; equilibration described."],
"citations": [C_BHUSHAN_HB, C_CLELAND, C_GERBERICH],
"sig_lens": (
"Signature take: molecular dynamics is the honest witness - it "
"does not assume the dislocation nucleates, it watches it happen "
"or not. But a witness can be coached: the potential tells the "
"atoms how to behave, so Signature simulation interrogates the "
"potential first and trusts the movie second."),
},
{
"key": "insitu_tem",
"name": "In-Situ TEM Nanomechanical Testing: Watching Deformation Live",
"group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
"description": (
"In-situ transmission electron microscopy marries a nanomechanical "
"tester to an electron microscope: pull, push, indent, or bend a "
"nanostructure while filming its atoms. Dislocations are seen "
"nucleating at surfaces and escaping; cracks are watched choosing "
"their path; phase transformations are caught mid-act; nanowires "
"are filmed necking down to a single atomic chain before breaking. "
"The instruments are MEMS-based tensile stages, nanoindenters, and "
"STM tips fitted into the microscope column, with load cells "
"reading nanonewtons while the camera reads picometres. Shan et "
"al. (2008) filmed 'mechanical annealing' - a nickel crystal "
"purging its dislocations under load until it was pristine. "
"Worked numbers: a 2 um wire elongating 38 nm over a 60 s video "
"strains at 3.17e-4 /s while the load cell reports 11.8 uN (1.5 "
"GPa on 100 nm diameter) - stress, strain, and microstructure in "
"one synchronized record. The cost: the electron beam heats, "
"charges, and can damage the sample - the observer effect, priced "
"in picoamps."),
"how_it_works": (
"Synchronization is the method: the mechanical data (load vs time, "
"displacement vs time) and the video frames share a clock, so each "
"stress-strain point has a microstructure photograph. Strain rate "
"epsilon_dot = (delta_L/L)/delta_t from frame measurements; stress "
"from the load cell over the imaged cross-section. Dislocation "
"density is counted frame by frame; crack length vs time gives "
"da/dt directly. Beam effects are controlled by dose series: repeat "
"at several beam currents and extrapolate to zero, or blank the "
"beam between frames. The demo reduces a synthetic 5-frame tensile "
"test - loads and elongations read 'from the video' - to stress, "
"strain, strain rate (3.17e-4 /s), and modulus, the complete "
"in-situ data reduction in miniature."),
"key_points": [
"Tester + TEM: stress-strain curves with atomic movies attached.",
"Filmed: dislocation nucleation/escape, crack paths, phase changes, atomic-chain necks.",
"Mechanical annealing (Shan 2008): loading purges dislocations on camera.",
"Strain rate from frames: 38 nm / 2 um / 60 s = 3.17e-4 /s.",
"Electron beam is a participant: heating, charging, damage - control by dose series.",
"Load cell (nN) + camera (pm) on one clock: the synchronized record."],
"requirements": [
"The nanowires and nanoindentation entries.",
"Rates as quantity per time.",
"A calculator."],
"standards": [
"Beam current/voltage and dose stated with every in-situ result.",
"Frame rate and load-cell bandwidth stated.",
"Beam-off control or dose series for beam-sensitive claims."],
"citations": [C_SHAN, C_GERBERICH, C_UCHIC],
"sig_lens": (
"Signature take: most testing interrogates the corpse - the broken "
"halves, the post-mortem micrograph. In-situ TEM interrogates the "
"living: the dislocation caught in the act, the crack choosing its "
"road. Signature failure analysis prefers witnesses to autopsies."),
},
{
"key": "plasticity",
"name": "Dislocation Starvation and Source Truncation: Plasticity Without Dislocations",
"group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
"description": (
"Bulk metals deform because dislocations - line defects - glide and "
"multiply; nanostructures deform differently because they run out of "
"dislocations. A 200 nm gold pillar with a typical dislocation density "
"of 1e12 /m^2 contains on average 0.031 dislocations - effectively "
"none. Under load, the few mobile dislocations escape to the free "
"surface faster than new ones nucleate ('dislocation starvation', "
"Greer and Nix, 2006), and the truncated sources that remain need "
"near-theoretical stresses to operate ('source truncation'). The "
"result: pillars yield at 1-4 GPa instead of 100 MPa, deform in "
"jerky avalanches (strain bursts) as single sources fire, and "
"sometimes 'mechanically anneal' to pristine crystal (Shan et al., "
"2008). Uchic et al. (2004) launched the field by compressing "
"micron-scale pillars and finding strength rising as size fell; "
"Volkert and Lilleodden (2006) mapped it in gold. Frenkel's 1926 "
"estimate of ideal shear strength, tau = G/2*pi (4.30 GPa for gold), "
"is the ceiling the smallest pillars approach. Plasticity without "
"dislocations is nucleation-controlled, stochastic, and strong - "
"the opposite of the smooth bulk flow engineers were taught."),
"how_it_works": (
"Count the dislocations: N = rho * A_cross. For a pillar d = 200 nm, "
"A = 3.14e-14 m^2, rho = 1e12 /m^2: N = 0.031 - starvation "
"is arithmetic, not poetry. Image forces pull dislocations to the "
"surface over nanometre distances, so mobile defects drain in "
"picoseconds. Yield then requires nucleating fresh dislocations at "
"the surface, needing stresses near Frenkel's tau_th = G/(2*pi) = "
"27 GPa/(2*pi) = 4.30 GPa shear (~7-8 GPa tensile). Single-arm "
"sources (one end pinned, one at the surface) give the observed "
"size scaling: smaller pillar, shorter arm, higher stress. Strain "
"bursts: when a source fires, it runs to the surface and stops - "
"deformation proceeds as discrete avalanches, visible as pop-ins "
"on the stress-strain curve. The demo does the dislocation census, "
"computes the Frenkel ceiling, and shows the starvation criterion "
"N << 1 that separates bulk-like from source-limited plasticity."),
"key_points": [
"200 nm Au pillar holds ~0.031 dislocations: starvation is arithmetic.",
"Dislocations escape to the surface faster than they multiply.",
"Yield needs surface nucleation at near-Frenkel stresses (4.30 GPa shear for Au).",
"Deformation is jerky: strain bursts as single sources fire and exhaust.",
"Mechanical annealing: loading can purge a crystal pristine (Shan 2008).",
"N << 1 dislocations marks the switch to nucleation-controlled plasticity."],
"requirements": [
"The nanowires and scale-effects entries.",
"Volumes of cylinders.",
"A calculator."],
"standards": [
"Dislocation density (initial) stated or bounded with every pillar strength.",
"Pillar aspect ratio and taper stated (FIB damage noted).",
"Strain bursts reported as pop-in statistics, not smoothed away."],
"citations": [C_GREER, C_UCHIC, C_VOLKERT, C_SHAN, C_FRENKEL],
"sig_lens": (
"Signature take: bulk plasticity is a crowd phenomenon - millions "
"of dislocations jostling. Nanoscale plasticity is an individual "
"sport - one dislocation, one surface, one nucleation event at a "
"time, at gigapascal stakes. Signature metals are trained like "
"athletes, not managed like crowds: fewer defects, higher "
"performance, every rep counted."),
},
{
"key": "superelasticity",
"name": "Shape Memory and Superelasticity at the Nanoscale",
"group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
"description": (
"Some materials cheat Hooke's law honestly: nickel-titanium (Nitinol) "
"nanowires can be stretched 6% and spring back completely - ten times "
"the elastic limit of steel - by a reversible martensitic phase "
"transformation rather than bond stretching. Pull, and the crystal "
"switches from austenite to martensite along a stress plateau (~500 "
"MPa); release, and it switches back, recovering the full strain. "
"The hysteresis loop between loading and unloading plateaus "
"dissipates energy: with a 200 MPa loop width over 6% strain, each "
"cycle soaks up 1.2e7 J/m^3 - superb damping in a wire 100 nm wide. "
"At the nanoscale the transformation is cleaner than in bulk: fewer "
"defects to pin the interfaces, plateaus flatter, fatigue lives "
"longer. Applications: nanoscale actuators (the wire contracts on "
"heating), superelastic surgical tools and stents at larger scales, "
"and vibration dampers where the hysteresis is the product. The "
"demo computes the recoverable elongation (120 nm on a 2 um wire), "
"the per-cycle dissipated energy, and the work output - the three "
"numbers that size a nanoactuator."),
"how_it_works": (
"Stress-induced martensite: above the austenite-finish temperature, "
"applied stress drives the diffusionless transformation at a "
"plateau stress sigma_p; the transformation strain epsilon_tr (~6% "
"for NiTi) accumulates at nearly constant stress. Unload and the "
"reverse transformation runs at a lower plateau; the loop area ~ "
"delta_sigma * epsilon_tr is the dissipated energy density. For "
"sigma_p = 500 MPa, loop width 200 MPa, epsilon_tr = 0.06: W = "
"1.2e7 J/m^3 per cycle; a d = 100 nm, L = 2 um wire (V = 1.57e-20 "
"m^3) dissipates 1.9e-13 J per cycle and strokes 120 nm. "
"Temperature dependence follows Clausius-Clapeyron: d(sigma_p)/dT "
"~ 5-7 MPa/K for NiTi, so the actuator force is temperature-"
"tunable. Size effects: below ~50 nm, the transformation can be "
"suppressed by surface energy - even shape memory has a size "
"limit. The demo sizes the actuator: stroke, force (sigma_p * A = "
"3.9 uN), and energy per cycle."),
"key_points": [
"NiTi nanowires: 6% recoverable strain via martensitic transformation, not bond stretch.",
"Plateau ~500 MPa loading, lower on unload: the hysteresis IS the damping product.",
"1.2e7 J/m^3 per cycle dissipated: superb nanoscale damping.",
"2 um wire strokes 120 nm at 3.9 uN force: the nanoactuator spec.",
"Clausius-Clapeyron: plateau stress rises ~6 MPa/K - temperature-tunable force.",
"Below ~50 nm surfaces can suppress the transformation: even this has a size limit."],
"requirements": [
"The stress/strain entry.",
"Areas of loops as energy.",
"A calculator."],
"standards": [
"Alloy composition and test temperature stated (transformation is temperature-sharp).",
"Cycle number stated: plateaus evolve with training.",
"Strain rate stated: the transformation has kinetics."],
"citations": [C_BHUSHAN_HB, C_GERBERICH],
"sig_lens": (
"Signature take: most materials remember their shape the way a "
"spring does - by never leaving it. Shape-memory alloys remember "
"the way a story does: they live a whole other crystal structure "
"under stress and return home when released. Signature actuators "
"use the story, not the spring - six percent stroke where steel "
"gives half a percent."),
},
{
"key": "nanolattices",
"name": "Nanotrusses and Mechanical Metamaterials: Strength Without Weight",
"group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
"description": (
"Architected materials - lattices of nanoscale trusses - decouple "
"stiffness and strength from density, reaching combinations no bulk "
"material offers. The Gibson-Ashby scaling laws rule the design: "
"E/E_s = C*(rho/rho_s)^n, with n = 1 for stretch-dominated lattices "
"(octet truss) and n = 2 for bend-dominated foams. An octet "
"nanolattice at 1% relative density (C ~ 0.3) keeps 0.3% of the "
"solid's modulus: 600 MPa from a 200 GPa parent at just 80 kg/m^3 "
"- lighter than balsa, stiffer than many polymers. Schaedler et "
"al. (2011) built ultralight metallic microlattices; Zheng et al. "
"(2014) showed stretch-dominated architectures are ultrastiff; "
"Meza, Das and Greer (2014) made ceramic nanolattices that are "
"strong, lightweight, AND recoverable after 50% compression - "
"ceramics that bounce. The nanoscale struts bring the size effect "
"as a bonus: each strut is a dislocation-starved pillar, so the "
"lattice inherits 'smaller is stronger' strut by strut. Design "
"variables: unit cell (octet, Kelvin, gyroid), relative density, "
"strut slenderness, parent material."),
"how_it_works": (
"Pick relative density rho_bar = rho/rho_s and architecture. "
"Stretch-dominated (octet): E = 0.3*E_s*rho_bar, sigma_y = "
"0.3*sigma_s*rho_bar. Bend-dominated (foam): E = E_s*rho_bar^2, "
"sigma_y = 0.3*sigma_s*rho_bar^1.5. For rho_bar = 0.01, E_s = 200 "
"GPa, sigma_s = 1 GPa, rho_s = 8000 kg/m^3: octet gives E = 600 "
"MPa, sigma = 3 MPa, rho = 80 kg/m^3; foam gives E = 20 MPa, "
"sigma = 0.3 MPa - the architecture premium is 30x in stiffness. "
"Specific stiffness E/rho = 7.5e6 m^2/s^2, approaching aluminum's "
"range at 3% of the weight. Strut buckling check: Euler load per "
"strut must exceed the lattice stress times the tributary area - "
"the demo includes it, closing the design loop. Hollow-tube "
"struts (Meza's ceramics) push the buckling limit up by raising "
"I per unit mass."),
"key_points": [
"Gibson-Ashby: E/E_s = C*(rho/rho_s)^n; n=1 stretch-dominated, n=2 foams.",
"Octet at 1% density: 600 MPa at 80 kg/m^3 - 30x stiffer than a foam at equal weight.",
"Ceramic nanolattices recover from 50% compression: ceramics that bounce (Meza 2014).",
"Struts inherit 'smaller is stronger': the lattice gets the size effect free.",
"Design loop: density -> modulus/strength -> Euler buckling check per strut.",
"Hollow struts raise buckling resistance per mass."],
"requirements": [
"The buckling and plasticity entries (strut-level checks).",
"Power laws.",
"A calculator."],
"standards": [
"Unit cell, relative density, and parent properties stated.",
"Stretch- vs bend-dominated classification stated.",
"Buckling check reported, not assumed."],
"citations": [C_GIBSON, C_SCHAEDLER, C_ZHENG, C_MEZA],
"sig_lens": (
"Signature take: bulk materials force a bargain - stiffness OR "
"lightness. Architected nanolattices refuse the bargain by "
"spending material only where the load paths run, the way a "
"bridge spends steel only in its trusses. Signature structures "
"are mostly empty space, engineered - because empty space is "
"free and stiffness placed wisely is priceless."),
},
{
"key": "viscoelastic",
"name": "Viscoelasticity at the Nanoscale: Polymers, Creep, and Time",
"group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
"description": (
"Not everything springs back instantly: polymers, biomaterials, and "
"soft nanostructures are viscoelastic - part elastic solid, part "
"viscous liquid - with a memory of how fast they were deformed. "
"The Kelvin-Voigt model (spring and dashpot in parallel) captures "
"creep: under constant stress sigma_0, strain approaches sigma_0/E "
"with time constant tau = eta/E. For a polymer nanofiber with E = 2 "
"GPa and eta = 1e6 Pa*s, tau = 0.5 ms: load it for microseconds "
"and it is glassy-stiff; load it for seconds and it flows. The "
"Deborah number De = tau/t_process decides: De >> 1 is solid-like, "
"De << 1 is liquid-like, De ~ 1 is the full viscoelastic drama - "
"and at the nanoscale, process times (resonator periods, AFM taps) "
"routinely land near material times. Consequences: polymer NEMS "
"resonators have low Q (the dashpot eats the ring), nanoimprint "
"lithography is a viscoelastic flow process, and AFM indentation "
"of cells must fit viscoelastic, not elastic, models or the "
"'modulus' is meaningless. Ferry (1980) remains the bible; the "
"time-temperature superposition that shifts polymer data across "
"decades works at the nanoscale too."),
"how_it_works": (
"Kelvin-Voigt creep: epsilon(t) = (sigma_0/E)*(1 - exp(-t/tau)), "
"tau = eta/E. With sigma_0 = 100 MPa, E = 2 GPa, tau = 0.5 ms: "
"epsilon(infinity) = 0.05; at t = tau, epsilon = 0.0316 (63%); at "
"t = 5*tau, 99.3% - the 'five time constants' rule. Stress "
"relaxation (Maxwell model, spring and dashpot in series): "
"sigma(t) = sigma_0*exp(-t/tau). Dynamic: storage modulus E' and "
"loss modulus E'' with tan(delta) = E''/E' measuring damping per "
"cycle. Deborah number: a 1 ms AFM dwell on the 0.5 ms fiber gives "
"De = 0.5 - squarely viscoelastic, so a Hertz fit would lie. The "
"demo computes the creep curve, the Deborah number for two process "
"times (1 us: De = 500, glassy; 1 s: De = 0.0005, flowing), and the "
"per-cycle energy loss - the numbers that decide whether a polymer "
"beam rings or thuds."),
"key_points": [
"Kelvin-Voigt: epsilon(t) = (sigma_0/E)(1 - e^-t/tau); tau = eta/E = 0.5 ms example.",
"Deborah De = tau/t_process: >>1 solid, <<1 liquid, ~1 full drama.",
"Nanoscale process times routinely match material times: viscoelasticity is unavoidable.",
"Polymer resonators have low Q: the dashpot eats the ring.",
"AFM cell indentation must use viscoelastic models; elastic fits lie.",
"Time-temperature superposition works at the nanoscale too."],
"requirements": [
"Exponentials (e^-x).",
"The stress/strain entry.",
"A calculator."],
"standards": [
"Model named (Kelvin-Voigt/Maxwell/standard linear solid) with every fit.",
"Temperature and humidity stated: both shift tau enormously.",
"Loading history stated: viscoelastic response is path-dependent."],
"citations": [C_FERRY, C_WARD, C_BHUSHAN_NM],
"sig_lens": (
"Signature take: elastic materials answer immediately; viscoelastic "
"materials answer eventually, and charge interest for the delay. "
"At the nanoscale the delay and the experiment run on the same "
"clock, so Signature polymer design always asks the time "
"question first: how long is the load on, and what does the "
"material remember?"),
},
{
"key": "buckling",
"name": "Buckling, Wrinkling, and Instability of Nanostructures",
"group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
"description": (
"Slender structures fail sideways: a column under compression "
"buckles when the Euler load P_cr = pi^2*E*I/(K*L)^2 is reached, "
"long before the material yields. At the nanoscale this is a "
"daily event - nanopillars buckle in compression tests, nanotubes "
"kink under AFM tips (and recover), thin films wrinkle on soft "
"substrates with a wavelength set by the modulus ratio. Worked "
"example: a gold nanopillar d = 100 nm, L = 1 um (K = 0.7, "
"fixed-pinned) buckles at P_cr = 7.81 uN, i.e. 994 MPa - below "
"gold's nanoscale yield, so the pillar buckles before it yields, "
"exactly as the demo shows. Wrinkling: a stiff film (E_f) on a "
"soft substrate (E_s) wrinkles with wavelength lambda = "
"2*pi*h*(E_f/3*E_s)^(1/3) - a 50 nm film on a 2 MPa substrate "
"wrinkles at 7.12 um, a built-in metrology ruler for film modulus. "
"Wrinkles are also technology: stretchable electronics ride "
"pre-wrinkled films, and wrinkled graphene tunes its electronics "
"with strain. Instability is not failure here - it is a design "
"tool with a formula."),
"how_it_works": (
"Euler buckling: the bent shape's extra bending energy vs the "
"load's lost potential energy; instability when P exceeds "
"pi^2*E*I/(K*L)^2. For the gold pillar: I = pi*d^4/64 = "
"4.91e-30 m^4, E*I = 3.88e-19 N*m^2, (K*L)^2 = 4.9e-13 m^2, "
"P_cr = 7.81e-6 N; stress 994 MPa < nanoscale yield (~1.5 GPa "
"for Au at this size) so buckling wins - the test measures a "
"structure, not a material, and the worker must know which. "
"Film wrinkling minimizes bending energy of the film plus "
"stretching energy of the substrate, giving lambda = "
"2*pi*h*(E_f/(3*E_s))^(1/3): h = 50 nm, E_f = 70 GPa, E_s = 2 "
"MPa -> (1.167e4)^(1/3) = 22.66, lambda = 7.12 um. Invert it: "
"measure lambda, read off E_f - wrinkle metrology. The demo "
"computes both and the buckling-vs-yield race for the pillar."),
"key_points": [
"Euler: P_cr = pi^2*EI/(KL)^2; Au nanopillar 100 nm x 1 um buckles at 7.81 uN (994 MPa).",
"Buckling can precede yielding: the test may measure the structure, not the material.",
"Wrinkling: lambda = 2*pi*h*(E_f/3E_s)^1/3; 50 nm film -> 7.12 um wrinkles.",
"Wrinkle wavelength is a modulus ruler: measure lambda, read E_f.",
"Nanotubes kink reversibly under bending (Falvo 1997): buckling without breaking.",
"Instability as design: stretchable electronics ride pre-wrinkled films."],
"requirements": [
"The elastic-beams entry (I, E).",
"Fourth powers (d^4).",
"A calculator."],
"standards": [
"End conditions (K) stated with every buckling load.",
"Buckling-vs-yield race checked and the winner named.",
"Wrinkle regime (small-strain sinusoidal) verified before metrology use."],
"citations": [C_LANDAU, C_TIMOSHENKO, C_FALVO],
"sig_lens": (
"Signature take: buckling is the structure voting against the "
"load - it would rather bend sideways than compress. The "
"Signature builder counts this vote before testing, because a "
"pillar that buckles at 994 MPa has told you nothing about the "
"material's 1.5 GPa yield except that you asked the wrong "
"question."),
},
{
"key": "thermal_effects",
"name": "Thermoelastic Damping and Heat at the Nanoscale: The Hot Small World",
"group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
"description": (
"Bend a beam and one side warms while the other cools; heat flows "
"across, entropy is generated, and the vibration damps - this is "
"thermoelastic damping (TED), Zener (1948), and at the nanoscale "
"it is often the dominant loss. Lifshitz and Roukes (2000) worked "
"it out for micro- and nanomechanical systems: the thermal time "
"constant tau_th ~ h^2*rho*C_p/(pi^2*kappa) for a beam of "
"thickness h. For a 100 nm silicon beam, tau_th = 11.0 ps and "
"damping peaks at 14.4 GHz with Q_TED ~ 9500 - design your "
"resonator near that frequency and TED caps your Q no matter how "
"perfect the surfaces. Heat otherwise behaves strangely at small "
"scales: thermal equilibration goes as L^2 (a 100 nm object "
"thermalizes in picoseconds), conductivity drops below the phonon "
"mean free path (boundary scattering), and laser heating in "
"experiments can dwarf the signal - a milliwatt focused to a "
"micron is 1e9 W/m^2. Thermal management is mechanical design at "
"the nanoscale: expansion bends bilayers, gradients drive "
"thermophoresis, and every loss budget starts with TED."),
"how_it_works": (
"Zener's standard anelastic solid: Q^-1 = Delta * (omega*tau)/"
"(1 + (omega*tau)^2), peaking at omega*tau = 1 with Q^-1_max = "
"Delta/2. The relaxation strength Delta = E*alpha^2*T/(rho*C_p): "
"for Si (E = 169 GPa, alpha = 2.6e-6 /K, T = 300 K, rho = 2330 "
"kg/m^3, C_p = 700 J/kg*K), Delta = 2.10e-4, so max Q^-1 = "
"1.05e-4 and the TED-limited Q is 9524. The thermal time across "
"thickness h: tau = h^2*rho*C_p/(pi^2*kappa) = 11.0 ps for h = "
"100 nm (kappa = 150 W/m*K), peaking at f = 1/(2*pi*tau) = 14.4 "
"GHz. Design rule: operate far from omega*tau = 1, or accept the "
"cap. The demo computes tau, the peak frequency, and Q_TED, plus "
"the thermalization time scaling (L^2) from 1 cm to 100 nm - "
"eleven orders of magnitude in one ratio."),
"key_points": [
"TED: bending makes heat flow; heat flow damps vibration (Zener 1948).",
"100 nm Si beam: tau = 11.0 ps, damping peaks at 14.4 GHz, Q_TED = 9524.",
"Relaxation strength Delta = E*alpha^2*T/(rho*C_p): materials choose their own cap.",
"Design rule: stay far from omega*tau = 1 or accept the TED ceiling.",
"Thermal time ~ L^2: 100 nm thermalizes ~1e11 x faster than 1 cm.",
"Laser heating in experiments can exceed the signal: budget the photons."],
"requirements": [
"The NEMS entry (Q factor).",
"Exponentials.",
"A calculator."],
"standards": [
"Q reported with the loss inventory: TED, clamping, surface, gas.",
"Temperature stated: TED is T-dependent through Delta and tau.",
"Beam theory regime checked (h vs phonon mean free path)."],
"citations": [C_ZENER, C_LIFROU, C_SCHMID],
"sig_lens": (
"Signature take: every vibration pays a heat tax - bend the beam "
"and the universe takes its cut in entropy, no exceptions, no "
"appeals. The Signature designer prices the tax before building: "
"Zener's formula is the tax table, and 9,524 is the best Q a "
"100 nm silicon beam can ever buy at its worst frequency."),
},
{
"key": "electromechanical",
"name": "Electromechanical Coupling: Piezoelectric Nanowires and Flexoelectricity",
"group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
"description": (
"Deform a piezoelectric crystal and it makes electricity; apply a "
"voltage and it deforms - and at the nanoscale this two-way street "
"gets wider. Wang and Song (2006) bent zinc oxide nanowires with an "
"AFM tip and harvested the piezoelectric charge: nanogenerators "
"that power sensors from vibration. Worked numbers: a ZnO wire d = "
"100 nm, L = 10 um pressed axially with 1 uN (127 MPa) generates "
"Q = d_33*sigma*A = 1.24e-17 C per press - 12.4 fA at 1 kHz of "
"tapping, small but real and rectifiable. Then comes flexoelectricity: "
"a STRAIN GRADIENT polarizes even non-piezoelectric materials, with "
"P = mu * (strain gradient). Gradients scale as 1/L, so flexoelectric "
"effects grow as devices shrink - bending a 1 um cantilever with a "
"100 nm tip deflection makes gradients of 3e5 /m and polarization "
"3e-4 C/m^2 with mu = 1 nC/m, rivaling piezoelectrics at the "
"nanoscale. Majdoub, Sharma and Cagin (2008) showed flexoelectricity "
"measurably enhances apparent piezoelectricity in nanostructures. "
"The lesson: at the nanoscale, every bent insulator is a little bit "
"piezoelectric whether its crystal class allows it or not."),
"how_it_works": (
"Piezoelectric charge: Q = d_33 * F for axial loading (d_33 = 12.4 "
"pC/N for ZnO). F = 1 uN on A = 7.85e-15 m^2 gives sigma = 127 "
"MPa, Q = 12.4e-12 * 1e-6 = 1.24e-17 C; cyclic at frequency f "
"gives current I = Q*f = 12.4 fA at 1 kHz. Real devices lose much "
"to screening by free carriers - the measured output is lower, "
"and the demo notes it. Flexoelectricity: for a cantilever with "
"tip deflection delta, curvature kappa = 3*delta/L^2; strain "
"gradient ~ kappa = 3e5 /m for delta = 100 nm, L = 1 um; P = "
"mu*kappa = 1e-9 * 3e5 = 3e-4 C/m^2. Shrink L to 100 nm at the "
"same delta and the gradient - and P - grow 100x, while the "
"piezoelectric term stays flat: the crossover where flexoelectricity "
"wins is the nanoscale. The demo computes both and their ratio vs "
"size - the chart that decides which effect to design around."),
"key_points": [
"ZnO nanowire: 1 uN axial press -> 1.24e-17 C; 12.4 fA at 1 kHz (Wang & Song 2006).",
"Piezoelectricity is two-way: sensing and actuation in one material.",
"Flexoelectricity: strain GRADIENT polarizes any insulator; scales as 1/L.",
"Bent 1 um cantilever: gradient 3e5 /m -> P = 3e-4 C/m^2.",
"Shrink 10x, flexoelectricity grows 10x, piezo stays flat: the crossover is nanoscale.",
"Free-carrier screening eats real device output: design the contacts too."],
"requirements": [
"Charge, current, capacitance basics.",
"The elastic-beams entry (curvature).",
"A calculator."],
"standards": [
"d_33 (or e_ij) quoted with crystal orientation and units.",
"Screening and contact effects discussed with every nanogenerator claim.",
"Flexoelectric mu quoted with the gradient geometry."],
"citations": [C_WANG, C_MAJDOUB, C_BHUSHAN_HB],
"sig_lens": (
"Signature take: squeeze a crystal and it answers in volts - the "
"most honest transduction in physics, no amplifier philosophy "
"required. And bend anything sharply enough and even the "
"non-piezoelectrics join in, because a gradient is a gradient. "
"Signature harvesters bend the small things sharply and collect "
"the volts that fall out."),
},
{
"key": "fluid_structure",
"name": "Nanomechanics in Fluids: Damping, Squeeze Films, and the Quality Factor",
"group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
"description": (
"Take a nanomechanical resonator out of vacuum and the fluid "
"attacks on two fronts: viscous drag steals energy (killing Q) "
"and the fluid's mass rides along (dropping the frequency). In "
"air at 1 atm, a NEMS beam with Q = 10,000 in vacuum can fall to "
"Q ~ 0.01 - the resonance drowns entirely. In the molecular "
"regime Q scales inversely with pressure (Q = 1e4 at 1 mTorr -> "
"1330 at 1 Pa -> 0.013 at 1 atm), which is why NEMS mass sensors "
"live in vacuum chambers. Squeeze-film damping - gas trapped in "
"the gap under a moving plate - adds a stiffness and a damping "
"that depend on the squeeze number; it is the dominant loss for "
"MEMS mirrors and switches. Immersed in water, a cantilever's "
"frequency halves (added mass ~3.4x the beam mass for a 1 um "
"wide beam) and Q collapses to single digits - yet AFM works in "
"liquid anyway, because force sensitivity survives where frequency "
"precision dies. Sader (1998) gave the hydrodynamic function that "
"predicts it all from the Reynolds number. Rule: vacuum for "
"frequency, fluid for force, and never confuse the two."),
"how_it_works": (
"Molecular-regime damping: each gas molecule collision steals "
"momentum ~ m_mol * v_beam; Q proportional to (beam mass * "
"frequency)/(pressure * area) so Q(p) = Q_0 * (p_0/p). With Q_0 "
"= 1e4 at p_0 = 1 mTorr (0.133 Pa): at 1 Pa, Q = 1330; at 1 atm "
"(101325 Pa), Q = 0.0131 - no resonance, just a floppy paddle. "
"Added mass in liquid: for a wide beam, m_added/L = pi*rho_f*"
"w^2/4; w = 1 um in water gives 7.85e-10 kg/m vs beam 2.33e-10 "
"kg/m, ratio 3.37, so f_water = f_vac/sqrt(1 + 3.37) = f_vac/"
"2.09. Sader's hydrodynamic function Gamma(Re) gives the full "
"frequency and Q from the Reynolds number Re = rho_f*omega*w^2/"
"(4*eta). The demo computes the Q-vs-pressure ladder, the "
"water-immersion frequency drop, and the pressure where Q = 100 "
" - the practical vacuum spec for a resonator product."),
"key_points": [
"Q ~ 1/p in the molecular regime: 1e4 at 1 mTorr -> 0.013 at 1 atm.",
"Air at 1 atm drowns NEMS resonance: vacuum is not optional for frequency work.",
"Water immersion: added mass 3.4x -> frequency halves (2.09x drop).",
"Squeeze-film damping dominates gapped MEMS: stiffness + damping from trapped gas.",
"Sader (1998): hydrodynamic function predicts f and Q from Reynolds number.",
"Vacuum for frequency, fluid for force: AFM in liquid trades Q for force sensitivity."],
"requirements": [
"The NEMS entry (Q factor).",
"Proportions (Q ~ 1/p).",
"A calculator."],
"standards": [
"Pressure stated with every Q: 'Q = 1e4' is meaningless without it.",
"Gas species stated (damping scales with molecular mass).",
"Immersion results state fluid density and viscosity."],
"citations": [C_SADER, C_EKROU, C_BUTT],
"sig_lens": (
"Signature take: a resonator in air is a bell rung underwater - "
"the fluid steals the ring and wears the frequency like a "
"coat. Signature frequency work is done in vacuum, where the "
"beam answers only to its own stiffness and mass; fluid work "
"is done knowing the coat is on, and measuring the arm inside "
"it anyway."),
},
{
"key": "quantum_limits",
"name": "Quantum Limits of Nanomechanical Motion: Toward the Ground State",
"group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
"description": (
"Cool a mechanical resonator far enough and its thermal jitter "
"surrenders to quantum zero-point motion: x_zp = sqrt(hbar/(2*m*"
"omega)). For a 1 MHz resonator with m = 1e-15 kg, x_zp = 91.6 fm "
"- less than a proton's diameter, yet measurable. The ground "
"state condition hbar*omega > k_B*T demands T < 48 uK for that "
"1 MHz device - dilution-fridge territory - which is why the "
"field moved to GHz resonators: O'Connell et al. (Nature 2010) "
"cooled a 6 GHz piezoelectric resonator to its ground state and "
"controlled single phonons, and Teufel et al. (Nature 2011) "
"sideband-cooled a 10 MHz drum to the ground state with "
"microwaves. LaHaye et al. (2004) approached the quantum limit of "
"displacement detection with a single-electron transistor. At "
"10 mK the 1 MHz resonator still holds ~208 thermal phonons; "
"each factor of cooling halves the noise floor. Cavity "
"optomechanics (Aspelmeyer, Kippenberg and Marquardt, 2014) now "
"uses light to cool, squeeze, and entangle mechanical motion. "
"This is nanomechanics at its limit: a visible object (well, "
"nearly) obeying quantum rules, weighed phonon by phonon."),
"how_it_works": (
"Zero-point motion from the harmonic oscillator ground state: "
"<x^2> = hbar/(2*m*omega). With m = 1e-15 kg, f = 1 MHz (omega "
"= 6.283e6 rad/s): x_zp = sqrt(1.055e-34/(2*1e-15*6.283e6)) = "
"9.16e-14 m = 91.6 fm. Thermal occupation n_th = k_B*T/(hbar*"
"omega): at T = 10 mK, n = 1.381e-23*0.01/6.628e-28 = 208.4 "
"phonons; ground state (n < 1) needs T < hbar*omega/k_B = 48 uK. "
"Sideband cooling: drive a coupled microwave/optical cavity red-"
"detuned by omega_m; anti-Stokes scattering carries phonons out "
"as photons - the refrigerator with no moving parts. "
"Displacement detection at the standard quantum limit balances "
"shot noise against backaction (LaHaye 2004 approached it). The "
"demo computes x_zp, the ground-state temperature, and n_th at "
"10 mK, 1 K, and 300 K (6.25e6 phonons at room temperature) - the "
"ladder from the everyday to the quantum."),
"key_points": [
"x_zp = sqrt(hbar/2*m*omega): 91.6 fm for 1 MHz, 1e-15 kg.",
"Ground state needs hbar*omega > k_B*T: 48 uK for 1 MHz - hence GHz devices.",
"6 GHz resonator cooled to ground state, single phonons controlled (O'Connell 2010).",
"Sideband cooling: red-detuned cavity carries phonons out as photons (Teufel 2011).",
"10 mK still leaves 208 phonons in a 1 MHz mode; 300 K leaves 6.25e6.",
"Quantum-limited detection balances shot noise vs backaction (LaHaye 2004)."],
"requirements": [
"Planck's constant and Boltzmann's constant (values given in demo).",
"The NEMS entry.",
"A calculator handling 1e-34."],
"standards": [
"Phonon occupation n_th stated with every 'quantum' claim.",
"Cooling method and base temperature stated.",
"Detection noise quoted relative to the standard quantum limit."],
"citations": [C_LAHAYE, C_OCONNELL, C_TEUFEL, C_ASPELMEYER],
"sig_lens": (
"Signature take: cool the beam until heat surrenders and what "
"remains is the trembling the universe cannot take away - "
"ninety femtometres of irreducible motion, the ground state. "
"Signature measurement goes there on purpose: past every "
"thermal lie, down to the floor where the only thing moving "
"the beam is quantum mechanics itself."),
},
{
"key": "design_rules",
"name": "Design Rules for Nanomechanical Devices: From Concept to Chip",
"group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
"description": (
"This entry is the checklist that turns the previous 33 into a "
"device. Designing a nanomechanical resonator, sensor, or switch "
"means satisfying every constraint at once: (1) Frequency: f = "
"0.56*(t/L^2)*sqrt(E/(12*rho)) for a cantilever - pick L for the "
"target f. (2) Stiffness vs force: k = 3*E*I/L^3 must exceed "
"adhesion and shock loads with margin. (3) Pull-in: electrostatic "
"actuation collapses past V_pi = sqrt(8*k*g_0^3/(27*eps_0*A)) - "
"stay below 70% of it. (4) Damping budget: TED (Zener), gas "
"(pressure spec), clamping, surface - sum the Q^-1. (5) "
"Nonlinearity: keep vibration amplitude below ~t/10 or the "
"Duffing term detunes you. (6) Fabrication: aspect ratios etchable, "
"release holes for sacrificial layers, anchor design against "
"clamping loss. (7) Packaging: vacuum level for the Q target, "
"getter for lifetime, temperature coefficient of f. Worked "
"design: a 10 MHz silicon cantilever, w = 1 um, t = 200 nm needs "
"L = 5.25 um; with a 500 nm gap the pull-in is 43.2 V, so drive "
"below ~30 V; TED at 10 MHz is far from the 14.4 GHz peak, so "
"gas and clamping set the Q. Follow the list and the first "
"fabrication run has a chance; skip it and the cleanroom teaches "
"the entries one expensive lesson at a time."),
"how_it_works": (
"The design flow, computed end to end. Target f_0 = 10 MHz, Si "
"(E = 169 GPa, rho = 2330 kg/m^3), t = 200 nm: f = 1375.8*t/L^2 "
"(cantilever, first mode) gives L = sqrt(1375.8*2e-7/1e7) = 5.25 "
"um. Stiffness k = 3*E*I/L^3 with I = w*t^3/12 = 6.67e-28 m^4: "
"k = 2.34 N/m. Pull-in with gap g_0 = 500 nm, area A = w*L = "
"5.25e-12 m^2: V_pi = sqrt(8*2.34*(5e-7)^3/(27*8.854e-12*"
"5.25e-12)) = 43.2 V. Checks: adhesion (JKR pull-off for the "
"contact area) << k*g_0; TED peak at 14.4 GHz >> 10 MHz so TED "
"Q >> 1e6, negligible; amplitude limit t/10 = 20 nm. The demo "
"runs this flow and prints the spec sheet - dimensions, "
"frequency, stiffness, pull-in, damping budget, limits - the "
"document every nanomechanical design review starts from."),
"key_points": [
"Seven checks: frequency, stiffness margin, pull-in, damping budget, nonlinearity, fabrication, packaging.",
"10 MHz Si cantilever (1 um x 200 nm): L = 5.25 um, k = 2.34 N/m.",
"Pull-in 43.2 V at 500 nm gap: drive below ~70% (30 V).",
"Damping budget sums Q^-1: TED + gas + clamping + surface.",
"Amplitude below t/10 keeps the Duffing nonlinearity quiet.",
"The spec sheet is the design: dimensions, f, k, V_pi, Q budget, limits."],
"requirements": [
"All entries before this one (it spends them).",
"Square roots.",
"A calculator and a willingness to iterate."],
"standards": [
"Every design states the full constraint list with margins.",
"Worst-case corners (temperature, pressure, adhesion) analyzed.",
"First-silicon expectations set: one unknown per run."],
"citations": [C_SCHMID, C_CRAIGHEAD, C_EKROU],
"sig_lens": (
"Signature take: a device is a promise made to physics, and "
"physics collects - on frequency, on pull-in, on damping, on "
"stiction, all at once. The Signature designer writes the "
"whole promise down before etching anything, because the "
"cleanroom charges tuition for every constraint discovered "
"late."),
},
{
"key": "bio_mechanics",
"name": "Nanobiomechanics: Cells, Proteins, and DNA as Mechanical Structures",
"group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
"description": (
"Biology is soft mechanics at the nanoscale: a cell is a "
"viscoelastic bag with modulus ~0.1-10 kPa (a million times softer "
"than steel), DNA is a semiflexible polymer with persistence length "
"50 nm, proteins unfold at ~200 pN, and molecular motors pull with "
"~5 pN per stroke. Nanobiomechanics measures it all with the tools "
"of this database: AFM indentation of cells (Hertz fit on the "
"approach curve - a 5 um colloidal probe indenting 500 nm into a "
"1 kPa cell reads 1.41 nN), optical tweezers stretching DNA "
"(the worm-like chain of the AFM entry, now with torque), and "
"magnetic tweezers twisting it. Findings that matter: cancer cells "
"are softer than healthy ones (a diagnostic signal), red blood "
"cells must deform through 3 um capillaries (spectrin network "
"mechanics), and the stiffness of the extracellular matrix directs "
"stem-cell fate (mechanotransduction). The numbers are small - "
"piconewtons, kilopascals - but the lever arms are biology itself: "
"mechanics is a signaling language cells speak fluently, and "
"nanobiomechanics is learning to read it."),
"how_it_works": (
"Cell indentation: Hertz sphere-on-flat, F = (4/3)*E**sqrt(R)*"
"delta^(3/2) with E** = E/(1-nu^2), nu ~ 0.5 for cells. With E = "
"1 kPa, R = 5 um, delta = 500 nm: E** = 1333 Pa, F = (4/3)*1333*"
"sqrt(5e-6)*(5e-7)^1.5 = 1.41 nN - the working equation of every "
"cell-mechanics lab (Radmacher, 1997). Corrections: finite "
"thickness (the rigid dish underneath stiffens the reading), "
"viscoelasticity (the modulus is rate-dependent - see the "
"viscoelastic entry), adhesion on retraction. DNA: worm-like "
"chain (Marko and Siggia, 1995; Bustamante et al., 2000) gives "
"persistence length from the force-extension fit; twist adds "
"the twistable-WLC for supercoiling. Protein unfolding: sawtooth "
"force spectra, each peak a domain, ~200 pN for titin. The demo "
"computes the cell-indentation force and the thickness correction "
"rule of thumb (keep delta < 10% of cell height), closing the "
"database where mechanics meets life."),
"key_points": [
"Cells: 0.1-10 kPa - a million times softer than steel; cancer cells softer still.",
"AFM cell poke: F = (4/3)E*sqrt(R)*delta^3/2; 1 kPa cell, 500 nm deep -> 1.41 nN.",
"DNA: persistence length 50 nm from worm-like-chain fits; twistable for supercoiling.",
"Proteins unfold at ~200 pN per domain: the sawtooth fingerprint.",
"Matrix stiffness directs stem-cell fate: mechanics as a signaling language.",
"Caveats: finite thickness, viscoelasticity, adhesion - correct all three."],
"requirements": [
"The AFM and viscoelastic entries.",
"Fractional powers (x^3/2).",
"A calculator."],
"standards": [
"Indenter geometry, rate, and medium stated with every cell modulus.",
"Thickness correction applied when delta > 10% of cell height.",
"Viscoelastic fit preferred over elastic for cells; rate stated always."],
"citations": [C_RADMACHER, C_MARKO, C_BUSTAMANTE, C_BUTT],
"sig_lens": (
"Signature take: the cell is the softest machine that matters - "
"kilopascals where steel is gigapascals - and it feels its way "
"through the world mechanically, stiffening, softening, "
"signaling. Signature bio-design speaks this soft language: "
"piconewtons delivered precisely, because the cell is listening "
"with its whole cytoskeleton."),
},
]
