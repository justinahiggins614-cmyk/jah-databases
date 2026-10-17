#!/usr/bin/env python3
"""Entries for the Nanophotonics field databases (field #30, taxonomy order).

Verified 2026-10-17: NO database covers the nanophotonics discipline (nanoscale
light-matter interaction: plasmonics, metamaterials, photonic crystals,
near-field optics, quantum dots in cavities, single-photon sources, nanolasers,
optical nano-antennas, subwavelength waveguiding, Purcell effect, strong
coupling / cavity QED, nanophotonic biosensing, nanoscale silicon photonics,
2D-material photonics, metasurfaces).
- Manifest search (2360 databases): nearest neighbors are 'optics' (10,002
  general-optics records), 'nanotech' (10,001 general-nanotechnology records),
  'photonics-engineers' / 'photonics-technicians' (people/career records, not
  the discipline), and 'optical-imaging-inspection' (31 inspection records).
  None teaches the nanophotonics discipline.
- Whole-system title sweep over all 759 shard indexes (1,129,517 records):
  nanophotonics discipline terms hit exactly 3 records - 'Sub-Atomic Quantum
  Dot Cellular Automata Catalog (Signature Edition)' (a quantum-dot computing
  record, not nanophotonics), and 'Plasmonic Nanophotonic Waveguide States'
  (+ Signature edition, a holographic-storage data-type record with incidental
  wording). ZERO full-record discipline coverage anywhere.
- Per the task rule, bare formula cards and study-corpus items do NOT count
  as discipline coverage.

So this build creates two NEW databases, 34 ladder-ordered records each:

  nanophotonics              - The Nanophotonics Database
                               (public-harvest: real, fact-checked
                               nanophotonics - the standard references are
                               Novotny & Hecht 'Principles of Nano-Optics',
                               Maier 'Plasmonics', Prasad 'Nanophotonics',
                               Joannopoulos et al. 'Photonic Crystals')
  nanophotonics-signature    - The Nanophotonics Signature Database
                               (his original Signature interpretation; src
                               signature, titles suffixed
                               " (Signature Edition)", never presented as
                               authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Subtitle disambiguation (fields #13-29 pattern): specialty titles carry
teaching-focused subtitles rather than bare cards, e.g. "Surface Plasmons:
Light Riding the Skin of a Metal".

Numerical cores (all hand-verified 2026-10-17):
- 532 nm photon: 5.64e14 Hz, 3.74e-19 J, 2.33 eV (1240/532).
- Abbe limit at 550 nm, NA 1.4 (oil): 196 nm; Rayleigh: 240 nm.
- Drude gold (hbar*omega_p = 9.03 eV): Re(eps) = -14.0 at 532 nm (free-electron
  estimate; interband absorption shifts real gold), crosses zero at 137 nm,
  positive below it.
- Glass (n=1.5) to air: critical angle 41.8 deg, normal reflectance 4.0%,
  Brewster angle 33.7 deg.
- Step-index fiber (a=4 um, NA=0.14, 1550 nm): V=2.27 < 2.405 -> single mode;
  multimode (a=25 um, NA=0.22, 850 nm): V=40.7 -> ~826 modes.
- Au/air SPP at 633 nm (eps_Au = -11.8+1.3i): n_eff = 1.045, lambda_spp =
  606 nm, propagation length 9.6 um.
- LSPR Frohlich condition Re(eps) = -2*eps_d: with representative measured
  gold permittivities, resonance ~512 nm in water (eps_d=1.77) vs ~473 nm in
  air - the red shift behind every plasmonic sensor.
- CdSe quantum dot (Brus): R=2 nm -> 2.545 eV (487 nm); R=3 nm -> 2.070 eV
  (599 nm). Size sets the color.
- Bragg mirror: 6 pairs TiO2/SiO2 (2.4/1.46) -> 99.0% reflectance; 10 pairs
  -> 99.98%.
- Slot waveguide field enhancement (3.48/1)^2 = 12.1x field, ~147x intensity.
- 800 nm half-wave optical antenna in n_eff=2 medium: 200 nm long; captures
  from ~4x its geometric area.
- Metasurface phase gradient (period 2 um, 800 nm light): steers to 23.6 deg.
- Evanescent penetration (n=1.5, 60 deg, 500 nm): 96 nm; NSOM beats 196 nm
  diffraction with a 50 nm aperture.
- Purcell: Q=1e4, V=(lambda/n)^3 -> Fp=760; 1 ns emitter -> 1.3 ps.
- 50 um silica microsphere at 1550 nm: FSR 10.5 nm (1.32 THz), mode number
  ~147, Q=1e8 -> 82 ns photon lifetime -> 17 m effective path.
- Au SPP at 1550 nm (eps=-131.9+12.65i): L ~ 343 um.
- QD-cavity: g/2pi=20 GHz, kappa/2pi=30 GHz, gamma/2pi=1 GHz -> strong
  coupling (20 > 15.5), C=13.3, Rabi splitting 0.108 nm at 900 nm.
- g2(0) = 0.004 from coincidence counts -> true single photons.
- LSPR biosensing: S=200 nm/RIU; 0.005 RIU protein layer -> 1.0 nm shift;
  0.02 nm spectrometer -> 1e-4 RIU limit.
- SERS: 30x field -> 8.1e5 enhancement; 1 pM in 1 fL -> 0.6 molecules.
- Yablonovitch 4n^2 = 49x for Si: 2 um film at 1000 nm goes 1.27% -> 46.6%
  absorption.
- Plasmonic nanolaser threshold gain: 2*pi*n/(lambda*Q) = 1571 cm^-1 at
  Q=100, 600 nm.
- n=-1 slab: 30 deg incidence refracts to -30 deg (same side).
- Si ring R=10 um: FSR 9.1 nm; Q=155,000 at 0.01 nm linewidth.
- Graphene plasmon: lambda_p/lambda_0 = (2*alpha/pi)(E_F/hbar*omega):
  10 um light, E_F=0.5 eV -> 187 nm plasmon (53x compression).
- Slow light n_g=20 over 1 mm: 66.7 ps delay.
- SHG: 4x pump -> 16x harmonic; coherence length 25 um at Delta_n=0.01.
- SSH chain t1=1, t2=2: gap 2|t1-t2|=2, bands +-1..+-3, gap closes at t1=t2.
- HOM dip V=0.95: coincidences fall to 5% at zero delay.
- Selective thermal emitter at 1500 K: 25.9% of blackbody power in 1-2 um.
- Binary amplitude grating inverse design: gradient ascent converges to
  DC=0.5, eta_1 = 10.13%.
- PT dimer H=[[i*gamma,kappa],[kappa,-i*gamma]]: EP at gamma=kappa=1.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature interpretation of "
            "nanophotonics, clearly labeled Signature-made, never "
            "presented as authentic public record.")

C_NOVOTNY = ("Novotny, L. and Hecht, B. 'Principles of Nano-Optics'. 2nd ed. "
             "Cambridge University Press, 2012.")
C_MAIER = ("Maier, S. A. 'Plasmonics: Fundamentals and Applications'. "
           "Springer, 2007.")
C_PRASAD = ("Prasad, P. N. 'Nanophotonics'. Wiley, 2004.")
C_JOANNO = ("Joannopoulos, J. D., Johnson, S. G., Winn, J. N. and Meade, R. D. "
            "'Photonic Crystals: Molding the Flow of Light'. 2nd ed. Princeton "
            "University Press, 2008.")
C_SALEH = ("Saleh, B. E. A. and Teich, M. C. 'Fundamentals of Photonics'. 3rd "
           "ed. Wiley, 2019.")
C_BOHREN = ("Bohren, C. F. and Huffman, D. R. 'Absorption and Scattering of "
            "Light by Small Particles'. Wiley, 1983.")
C_KREIBIG = ("Kreibig, U. and Vollmer, M. 'Optical Properties of Metal "
             "Clusters'. Springer, 1995.")
C_RAETHER = ("Raether, H. 'Surface Plasmons on Smooth and Rough Surfaces and "
             "on Gratings'. Springer, 1988.")
C_BARNES = ("Barnes, W. L., Dereux, A. and Ebbesen, T. W. 'Surface plasmon "
            "subwavelength optics'. Nature 424, 824-830 (2003).")
C_EBBESEN = ("Ebbesen, T. W. et al. 'Extraordinary optical transmission "
             "through sub-wavelength hole arrays'. Nature 391, 667-669 (1998).")
C_SCHULLER = ("Schuller, J. A. et al. 'Plasmonics for extreme light "
              "concentration and manipulation'. Nature Materials 9, 193-204 "
              "(2010).")
C_GRAMOTNEV = ("Gramotnev, D. K. and Bozhevolnyi, S. I. 'Plasmonics beyond the "
               "diffraction limit'. Nature Photonics 4, 83-91 (2010).")
C_HALAS = ("Halas, N. J. et al. 'Plasmons in strongly coupled metallic "
           "nanostructures'. Chemical Reviews 111, 3913-3921 (2011).")
C_STOCKMAN = ("Stockman, M. I. 'Nanoplasmonics: past, present, and glimpse "
              "into future'. Optics Express 19, 22029-22106 (2011).")
C_KHURGIN = ("Khurgin, J. B. 'How to deal with the loss in plasmonics and "
             "metamaterials'. Nature Nanotechnology 10, 2-6 (2015).")
C_LAL = ("Lal, S., Link, S. and Nordlander, P. 'Nano-optics from sensing to "
         "waveguiding'. Nature Photonics 1, 641-648 (2007).")
C_PRODAN = ("Prodan, E. et al. 'A hybridization model for the plasmon "
            "response of complex nanostructures'. Science 302, 419-422 (2003).")
C_ANKER = ("Anker, J. N. et al. 'Biosensing with plasmonic nanosensors'. "
           "Nature Materials 7, 442-453 (2008).")
C_MAYER = ("Mayer, K. M. and Hafner, J. H. 'Localized surface plasmon "
           "resonance sensors'. Chemical Reviews 111, 3828-3857 (2011).")
C_HOMOLA = ("Homola, J. 'Surface plasmon resonance sensors for detection of "
            "chemical and biological species'. Chemical Reviews 108, 462-493 "
            "(2008).")
C_LIEDBERG = ("Liedberg, B., Nylander, C. and Lundstrom, I. 'Surface plasmon "
              "resonance for gas detection and biosensing'. Sensors and "
              "Actuators 4, 299-304 (1983).")
C_KRETSCHMANN = ("Kretschmann, E. 'Die Bestimmung optischer Konstanten von "
                 "Metallen durch Anregung von Oberflaechenplasmaschwingungen'. "
                 "Zeitschrift fuer Physik 241, 313-324 (1971).")
C_SARID = ("Sarid, G. I. 'Long-range surface-plasma waves on very thin metal "
           "films'. Physical Review Letters 47, 1927-1931 (1981).")
C_BERINI = ("Berini, P. 'Long-range surface plasmon polaritons'. Advances in "
            "Optics and Photonics 1, 484-588 (2009).")
C_DIONNE = ("Dionne, J. A. et al. 'Plasmon slot waveguides: towards "
            "chip-scale propagation with subwavelength-scale localization'. "
            "Physical Review B 73, 035407 (2006).")
C_BOZHEVOLNYI = ("Bozhevolnyi, S. I. et al. 'Channel plasmon subwavelength "
                 "waveguide components including interferometers and ring "
                 "resonators'. Nature 440, 508-511 (2006).")
C_QUINTEN = ("Quinten, M. et al. 'Electromagnetic energy transport via linear "
             "chains of silver nanoparticles'. Optics Letters 23, 1331-1333 "
             "(1998).")
C_MAIER2 = ("Maier, S. A. et al. 'Local detection of electromagnetic energy "
            "transport below the diffraction limit'. Nature Materials 2, "
            "229-232 (2003).")
C_YABLONOVITCH = ("Yablonovitch, E. 'Inhibited spontaneous emission in "
                  "solid-state physics and electronics'. Physical Review "
                  "Letters 58, 2059-2062 (1987).")
C_PURCELL = ("Purcell, E. M. 'Spontaneous emission probabilities at radio "
             "frequencies'. Physical Review 69, 681 (1946).")
C_DREXHAGE = ("Drexhage, K. H. 'Influence of a dielectric interface on "
              "fluorescence decay time'. Journal of Luminescence 12, 693-701 "
              "(1974).")
C_KLEPPNER = ("Kleppner, D. 'Inhibited spontaneous emission'. Physical Review "
              "Letters 47, 233-236 (1981).")
C_VAHALA = ("Vahala, K. J. 'Optical microcavities'. Nature 424, 839-846 "
            "(2003).")
C_KIPPENBERG = ("Kippenberg, T. J. and Vahala, K. J. 'Cavity optomechanics: "
                "back-action at the mesoscale'. Science 321, 1172-1176 "
                "(2008).")
C_ILCHENKO = ("Ilchenko, V. S. and Matsko, A. B. 'Optical resonators with "
              "whispering-gallery modes'. IEEE Journal of Selected Topics in "
              "Quantum Electronics 12, 15-32 (2006).")
C_MCCALL = ("McCall, S. L. et al. 'Whispering-gallery mode microdisk "
            "lasers'. Applied Physics Letters 60, 289-291 (1992).")
C_PAINTER = ("Painter, O. et al. 'Two-dimensional photonic band-gap defect "
             "mode laser'. Science 284, 1819-1821 (1999).")
C_AKAHANE = ("Akahane, Y. et al. 'High-Q photonic nanocavity in a "
             "two-dimensional photonic crystal'. Nature 425, 944-947 (2003).")
C_VUCKOVIC = ("Vuckovic, J. et al. 'Design of photonic crystal microcavities "
              "for cavity QED'. Physical Review E 65, 016608 (2001).")
C_NODA = ("Noda, S. et al. 'Full three-dimensional photonic bandgap crystals "
          "at near-infrared wavelengths'. Science 289, 604-606 (2000).")
C_VLASOV = ("Vlasov, Y. A. et al. 'On-chip natural assembly of silicon "
            "photonic bandgap crystals'. Nature 414, 289-293 (2001).")
C_BABA = ("Baba, T. 'Slow light in photonic crystals'. Nature Photonics 2, "
          "465-473 (2008).")
C_NOTOMI = ("Notomi, M. et al. 'Extremely large group-velocity dispersion of "
            "line-defect waveguides in photonic crystal slabs'. Physical "
            "Review Letters 87, 253902 (2001).")
C_KRAUSS = ("Krauss, T. F. 'Slow light in photonic crystal waveguides'. "
            "Journal of Physics D 40, 2666-2670 (2007).")
C_VLASOV2 = ("Vlasov, Y. A. et al. 'Active control of slow light on a chip "
             "with photonic crystal waveguides'. Nature 438, 65-69 (2005).")
C_YARIV = ("Yariv, A. et al. 'Coupled-resonator optical waveguide: a proposal "
           "and analysis'. Optics Letters 24, 711-713 (1999).")
C_SMITH = ("Smith, D. R., Pendry, J. B. and Wiltshire, M. C. K. "
           "'Metamaterials and negative refractive index'. Science 305, "
           "788-792 (2004).")
C_PENDRY = ("Pendry, J. B. 'Negative refraction makes a perfect lens'. "
            "Physical Review Letters 85, 3966-3969 (2000).")
C_ZHELUDEV = ("Zheludev, N. I. and Kivshar, Y. S. 'From metamaterials to "
              "metadevices'. Nature Materials 11, 917-924 (2012).")
C_YU = ("Yu, N. and Capasso, F. 'Flat optics with designer metasurfaces'. "
        "Nature Materials 13, 139-150 (2014).")
C_YU2 = ("Yu, N. et al. 'Light propagation with phase discontinuities: "
         "generalized laws of reflection and refraction'. Science 334, "
         "333-337 (2011).")
C_KILDISHEV = ("Kildishev, A. V., Boltasseva, A. and Shalaev, V. M. 'Planar "
               "photonics with metasurfaces'. Science 339, 1232009 (2013).")
C_KHORASANINEJAD = ("Khorasaninejad, M. et al. 'Metalenses at visible "
                    "wavelengths: diffraction-limited focusing and "
                    "subwavelength resolution imaging'. Science 352, "
                    "1190-1194 (2016).")
C_AIETA = ("Aieta, F. et al. 'Aberration-free ultrathin flat lenses and "
           "axicons at telecom wavelengths based on plasmonic metasurfaces'. "
           "Nano Letters 12, 4932-4936 (2012).")
C_STAUDT = ("Staude, I. and Schilling, J. 'Metamaterial-inspired silicon "
            "nanophotonics'. Nature Photonics 8, 387-400 (2014).")
C_KUZNETSOV = ("Kuznetsov, A. I. et al. 'Optically resonant dielectric "
               "nanostructures'. Science 354, aag2472 (2016).")
C_GARCIA = ("Garcia-Etxarri, A. et al. 'Strong magnetic response of submicron "
            "silicon particles in the infrared'. Optics Express 19, 4815-4826 "
            "(2011).")
C_NOVOTNY2 = ("Novotny, L. and van Hulst, N. 'Antennas for light'. Nature "
              "Photonics 5, 83-90 (2011).")
C_MUHLSCHLEGEL = ("Muhlschlegel, P. et al. 'Resonant optical antennas'. "
                  "Science 308, 1607-1609 (2005).")
C_BIAGIONI = ("Biagioni, P., Huang, J.-S. and Hecht, B. 'Nanoantennas for "
              "visible and infrared radiation'. Reports on Progress in Physics "
              "75, 024402 (2012).")
C_CURTO = ("Curto, A. G. et al. 'Unidirectional emission of a quantum dot "
           "coupled to a nanoantenna'. Science 329, 930-933 (2010).")
C_KINKHABWALA = ("Kinkhabwala, A. et al. 'Large single-molecule fluorescence "
                 "enhancements produced by a bowtie nanoantenna'. Nature "
                 "Photonics 3, 654-657 (2009).")
C_PAESLER = ("Paesler, M. A. and Moyer, P. J. 'Near-Field Optics: Theory, "
             "Instrumentation, and Applications'. Wiley, 1996.")
C_SYNGE = ("Synge, E. H. 'A suggested method for extending microscopic "
           "resolution into the ultramicroscopic region'. Philosophical "
           "Magazine 6, 356-362 (1928).")
C_DUNN = ("Dunn, R. C. 'Near-field scanning optical microscopy'. Chemical "
          "Reviews 99, 2891-2928 (1999).")
C_BETZIG = ("Betzig, E. et al. 'Imaging intracellular fluorescent proteins at "
            "nanometer resolution'. Science 313, 1642-1645 (2006).")
C_HELL = ("Hell, S. W. 'Far-field optical nanoscopy'. Science 316, "
          "1153-1158 (2007).")
C_ALIVISATOS = ("Alivisatos, A. P. 'Semiconductor clusters, nanocrystals, and "
                "quantum dots'. Science 271, 933-937 (1996).")
C_BRUS = ("Brus, L. E. 'Electron-electron and electron-hole interactions in "
          "small semiconductor crystallites'. Journal of Chemical Physics 80, "
          "4403-4409 (1984).")
C_EKIMOV = ("Ekimov, A. I. and Onushchenko, A. A. 'Quantum size effect in "
            "three-dimensional microscopic semiconductor crystals'. JETP "
            "Letters 34, 345-349 (1981).")
C_MICHLER = ("Michler, P. et al. 'A quantum dot single-photon turnstile "
             "device'. Science 290, 2282-2285 (2000).")
C_SANTORI = ("Santori, C. et al. 'Indistinguishable photons from a "
             "single-photon device'. Nature 419, 594-597 (2002).")
C_SENELLART = ("Senellart, P., Solomon, G. and White, A. 'High-performance "
               "semiconductor quantum-dot single-photon sources'. Nature "
               "Nanotechnology 12, 1026-1039 (2017).")
C_LODAHL = ("Lodahl, P. et al. 'Interfacing single photons and single quantum "
            "dots with photonic nanostructures'. Reviews of Modern Physics "
            "87, 347-400 (2015).")
C_GERARD = ("Gerard, J. M. et al. 'Enhanced spontaneous emission by quantum "
            "boxes in a monolithic optical microcavity'. Physical Review "
            "Letters 81, 1110-1113 (1998).")
C_SOMASCHI = ("Somaschi, N. et al. 'Near-optimal single-photon sources in the "
              "solid state'. Nature Photonics 10, 340-345 (2016).")
C_GRANGIER = ("Grangier, P., Roger, G. and Aspect, A. 'Experimental evidence "
              "for a photon anticorrelation effect on a beam splitter'. "
              "Europhysics Letters 1, 173-179 (1986).")
C_HOM = ("Hong, C. K., Ou, Z. Y. and Mandel, L. 'Measurement of subpicosecond "
         "time intervals between two photons by interference'. Physical "
         "Review Letters 59, 2044-2046 (1987).")
C_RAIMOND = ("Raimond, J. M., Brune, M. and Haroche, S. 'Manipulating quantum "
             "entanglement with atoms and photons in a cavity'. Reviews of "
             "Modern Physics 73, 565-582 (2001).")
C_KIMBLE = ("Kimble, H. J. 'The quantum internet'. Nature 453, 1023-1030 "
            "(2008).")
C_KNILL = ("Knill, E., Laflamme, R. and Milburn, G. J. 'A scheme for "
           "efficient quantum computation with linear optics'. Nature 409, "
           "46-52 (2001).")
C_KOK = ("Kok, P. et al. 'Linear optical quantum computing with photonic "
         "qubits'. Reviews of Modern Physics 79, 135-174 (2007).")
C_POLITI = ("Politi, A. et al. 'Silica-on-silicon waveguide quantum "
            "circuits'. Science 320, 646-649 (2008).")
C_WANG = ("Wang, J. et al. 'Integrated photonic quantum technologies'. "
          "Nature Photonics 14, 273-284 (2020).")
C_CAROLAN = ("Carolan, J. et al. 'Universal linear optics'. Science 349, "
             "711-716 (2015).")
C_BERGMAN = ("Bergman, D. J. and Stockman, M. I. 'Surface plasmon "
             "amplification by stimulated emission of radiation'. Physical "
             "Review Letters 90, 027402 (2003).")
C_NOGINOV = ("Noginov, M. A. et al. 'Demonstration of a spaser-based "
             "nanolaser'. Nature 460, 1110-1112 (2009).")
C_OULTON = ("Oulton, R. F. et al. 'Plasmon lasers at deep subwavelength "
            "scale'. Nature 461, 629-632 (2009).")
C_HILL = ("Hill, M. T. et al. 'Lasing in metallic-coated nanocavities'. "
          "Nature Photonics 1, 589-594 (2007).")
C_MA = ("Ma, R.-M. et al. 'Room-temperature sub-diffraction-limited plasmon "
        "laser by total internal reflection'. Nature Materials 10, 110-113 "
        "(2011).")
C_NEZHAD = ("Nezhad, M. P. et al. 'Room-temperature subwavelength "
            "metallo-dielectric lasers'. Nature Photonics 4, 395-399 (2010).")
C_DUAN = ("Duan, X. et al. 'Single-nanowire electrically driven lasers'. "
          "Nature 421, 241-245 (2003).")
C_SORE = ("Soref, R. 'The past, present, and future of silicon photonics'. "
          "IEEE Journal of Selected Topics in Quantum Electronics 12, "
          "1678-1687 (2006).")
C_JALALI = ("Jalali, B. and Fathpour, S. 'Silicon photonics'. Journal of "
            "Lightwave Technology 24, 4600-4615 (2006).")
C_REED = ("Reed, G. T. et al. 'Silicon optical modulators'. Nature Photonics "
          "4, 518-526 (2010).")
C_XU = ("Xu, Q. et al. 'Micrometre-scale silicon electro-optic modulator'. "
        "Nature 435, 325-327 (2005).")
C_THOMSON = ("Thomson, D. et al. 'Roadmap on silicon photonics'. Journal of "
             "Optics 18, 073003 (2016).")
C_RONG = ("Rong, H. et al. 'A continuous-wave Raman silicon laser'. Nature "
          "433, 725-728 (2005).")
C_MILLER = ("Miller, D. A. B. 'Device requirements for optical interconnects "
            "to silicon chips'. Proceedings of the IEEE 97, 1166-1185 (2009).")
C_LIPSON = ("Lipson, M. 'Guiding, modulating, and emitting light on silicon'. "
            "MRS Bulletin 28, 495-499 (2003).")
C_BONACCORSO = ("Bonaccorso, F. et al. 'Graphene photonics and "
                "optoelectronics'. Nature Photonics 4, 611-622 (2010).")
C_NAIR = ("Nair, R. R. et al. 'Fine structure constant defines visual "
          "transparency of graphene'. Science 320, 1308 (2008).")
C_JABLAN = ("Jablan, M., Buljan, H. and Soljacic, M. 'Plasmonics in graphene "
            "at infrared frequencies'. Physical Review B 80, 245435 (2009).")
C_FEI = ("Fei, Z. et al. 'Gate-tuning of graphene plasmons revealed by "
         "infrared nano-imaging'. Nature 487, 82-85 (2012).")
C_CHEN = ("Chen, J. et al. 'Optical nano-imaging of gate-tunable graphene "
          "plasmons'. Nature 487, 77-81 (2012).")
C_KOPPENS = ("Koppens, F. H. L., Chang, D. E. and Garcia de Abajo, F. J. "
             "'Graphene plasmonics: a platform for strong light-matter "
             "interactions'. Nano Letters 11, 3370-3377 (2011).")
C_BASOV = ("Basov, D. N., Fogler, M. M. and Garcia de Abajo, F. J. "
           "'Polaritons in van der Waals materials'. Science 354, aag1992 "
           "(2016).")
C_CALDWELL = ("Caldwell, J. D. et al. 'Sub-diffractional volume-confined "
              "polaritons in the natural hyperbolic material hexagonal boron "
              "nitride'. Nature Communications 5, 5221 (2014).")
C_WU = ("Wu, S. et al. 'Monolayer semiconductor nanocavity lasers with "
        "ultralow thresholds'. Nature 520, 69-72 (2015).")
C_LIU = ("Liu, X. et al. 'Strong light-matter coupling in two-dimensional "
         "atomic crystals'. Nature Photonics 9, 30-34 (2015).")
C_FLEISCHMANN = ("Fleischmann, M., Hendra, P. J. and McQuillan, A. J. 'Raman "
                 "spectra of pyridine adsorbed at a silver electrode'. "
                 "Chemical Physics Letters 26, 163-166 (1974).")
C_JEANMAIRE = ("Jeanmaire, D. L. and Van Duyne, R. P. 'Surface Raman "
               "spectroelectrochemistry'. Journal of Electroanalytical "
               "Chemistry 84, 1-20 (1977).")
C_MOSKOVITS = ("Moskovits, M. 'Surface-enhanced spectroscopy'. Reviews of "
               "Modern Physics 57, 783-826 (1985).")
C_STILES = ("Stiles, P. L. et al. 'Surface-enhanced Raman spectroscopy'. "
            "Annual Review of Analytical Chemistry 1, 601-626 (2008).")
C_NIE = ("Nie, S. and Emory, S. R. 'Probing single molecules and single "
         "nanoparticles by surface-enhanced Raman scattering'. Science 275, "
         "1102-1106 (1997).")
C_KNEIPP = ("Kneipp, K. et al. 'Single molecule detection using "
            "surface-enhanced Raman scattering (SERS)'. Physical Review "
            "Letters 78, 1667-1670 (1997).")
C_ATWATER = ("Atwater, H. A. and Polman, A. 'Plasmonics for improved "
             "photovoltaic devices'. Nature Materials 9, 205-213 (2010).")
C_POLMAN = ("Polman, A. and Atwater, H. A. 'Photonic design principles for "
            "ultrahigh-efficiency photovoltaics'. Nature Materials 11, "
            "174-177 (2012).")
C_ASHKIN = ("Ashkin, A. 'Acceleration and trapping of particles by radiation "
            "pressure'. Physical Review Letters 24, 156-159 (1970).")
C_GRIER = ("Grier, D. G. 'A revolution in optical manipulation'. Nature 424, "
           "810-816 (2003).")
C_NEUMAN = ("Neuman, K. C. and Block, S. M. 'Optical trapping'. Review of "
            "Scientific Instruments 75, 2787-2809 (2004).")
C_NOVOTNY3 = ("Novotny, L., Bian, R. X. and Xie, X. S. 'Theory of nanometric "
              "optical tweezers'. Physical Review Letters 79, 645-648 (1997).")
C_MARAGO = ("Marago, O. M. et al. 'Optical trapping and manipulation of "
            "nanostructures'. Nature Nanotechnology 8, 807-819 (2013).")
C_ALTuG = ("Altug, H., Oh, S.-H., Maier, S. A. and Homola, J. 'Advances and "
           "applications of nanophotonic biosensors'. Nature Nanotechnology "
           "17, 5-16 (2022).")
C_STEWART = ("Stewart, M. E. et al. 'Nanostructured plasmonic sensors'. "
             "Chemical Reviews 108, 494-521 (2008).")
C_BROLO = ("Brolo, A. G. 'Plasmonics for future biosensors'. Nature Photonics "
           "6, 709-713 (2012).")
C_SONNICHSEN = ("Sonnichsen, C. et al. 'A molecular ruler based on plasmon "
                "coupling of single gold and silver nanoparticles'. Nature "
                "Biotechnology 23, 741-745 (2005).")
C_HAU = ("Hau, L. V. et al. 'Light speed reduction to 17 metres per second in "
         "an ultracold atomic gas'. Nature 397, 594-598 (1999).")
C_FLEISCHHAUER = ("Fleischhauer, M., Imamoglu, A. and Marangos, J. P. "
                  "'Electromagnetically induced transparency: optics in "
                  "coherent media'. Reviews of Modern Physics 77, 633-673 "
                  "(2005).")
C_BOYD = ("Boyd, R. W. 'Nonlinear Optics'. 3rd ed. Academic Press, 2008.")
C_FRANKEN = ("Franken, P. A. et al. 'Generation of optical harmonics'. "
             "Physical Review Letters 7, 118-119 (1961).")
C_KAURANEN = ("Kauranen, M. and Zayats, A. V. 'Nonlinear plasmonics'. Nature "
              "Photonics 6, 737-748 (2012).")
C_LU = ("Lu, L., Joannopoulos, J. D. and Soljacic, M. 'Topological "
        "photonics'. Nature Photonics 8, 821-829 (2014).")
C_KHANIKAEv = ("Khanikaev, A. B. and Shvets, G. 'Two-dimensional topological "
               "photonics'. Nature Photonics 11, 763-773 (2017).")
C_SSH = ("Su, W. P., Schrieffer, J. R. and Heeger, A. J. 'Solitons in "
         "polyacetylene'. Physical Review Letters 42, 1698-1701 (1979).")
C_ELGANAINY = ("El-Ganainy, R. et al. 'Non-Hermitian physics and PT "
               "symmetry'. Nature Physics 14, 11-19 (2018).")
C_OZDEMIR = ("Ozdemir, S. K. et al. 'Parity-time symmetry and exceptional "
             "points in photonics'. Nature Materials 18, 783-798 (2019).")
C_BENDER = ("Bender, C. M. and Boettcher, S. 'Real spectra in non-Hermitian "
            "Hamiltonians having PT symmetry'. Physical Review Letters 80, "
            "5243-5246 (1998).")
C_MOLESKY = ("Molesky, S. et al. 'Inverse design in nanophotonics'. Nature "
             "Photonics 12, 659-670 (2018).")
C_LIN = ("Lin, S. Y. et al. 'Three-dimensional photonic-crystal emitter for "
         "thermal photovoltaic power generation'. Applied Physics Letters 83, "
         "380-382 (2003).")
C_GREFFET = ("Greffet, J.-J. et al. 'Coherent emission of light by thermal "
             "sources'. Nature 416, 61-64 (2002).")
C_FAN = ("Fan, S. 'Thermal photonics and energy applications'. Joule 1, "
         "264-272 (2017).")
C_KASPRZAK = ("Kasprzak, J. et al. 'Bose-Einstein condensation of exciton "
              "polaritons'. Nature 443, 409-414 (2006).")
C_SANVITTO = ("Sanvitto, D. and Kena-Cohen, S. 'The road towards polaritonic "
              "devices'. Nature Materials 15, 1061-1068 (2016).")
C_CARUSOTTO = ("Carusotto, I. and Ciuti, C. 'Quantum fluids of light'. "
               "Reviews of Modern Physics 85, 299-366 (2013).")
C_AMO = ("Amo, A. et al. 'Superfluidity of polaritons in semiconductor "
         "microcavities'. Nature Physics 5, 805-810 (2009).")
C_LOUDON = ("Loudon, R. 'The Quantum Theory of Light'. 3rd ed. Oxford "
            "University Press, 2000.")
C_WALLS = ("Walls, D. F. and Milburn, G. J. 'Quantum Optics'. 2nd ed. "
           "Springer, 2008.")

ENTRIES = [
{
"key": "what_is",
"name": "Nanophotonics: The Science of Light at the Nanoscale",
"group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
"description": (
"Nanophotonics is the science of light interacting with structures that are "
"sized at or below the wavelength of the light itself - roughly one to a few "
"hundred nanometres for visible light. Ordinary optics treats light as rays "
"bouncing off mirrors and bending through lenses; nanophotonics treats light "
"as waves and photons dancing with structures smaller than the wave, where "
"the ray picture breaks down completely. When metal particles, holes, wires, "
"or crystal lattices shrink to this scale, light stops behaving politely: "
"it squeezes into volumes far below the diffraction limit, it rides the "
"surface of metals as plasmons, it gets forbidden from existing at certain "
"colors inside photonic crystals, and single atoms can be made to talk to "
"single photons. The field sits at the crossing of optics, solid-state "
"physics, materials science, and quantum mechanics, and it underpins "
"plasmonic biosensors, flat metalenses, nanoscale lasers, photonic chips, "
"and quantum light sources. Across one green wavelength of 550 nanometres "
"you could line up about 5,500 atoms - nanophotonics is the engineering of "
"everything that happens in that crowded space between the atom and the "
"wave."),
"how_it_works": (
"Everything in nanophotonics starts from Maxwell's equations applied to "
"structures with features comparable to the wavelength. Because the "
"structure size and the wavelength are similar, light cannot simply stream "
"past: it diffracts, resonates, and binds to the geometry. Two material "
"responses dominate. Dielectrics (glass, silicon) slow and guide light by "
"their refractive index, trapping it in waveguides and resonators. Metals "
"(gold, silver) respond with free electrons that slosh back and forth with "
"the light field, creating surface plasmons - combined waves of electrons "
"and light pinned to the metal surface. Quantum mechanics enters when the "
"structures shrink to a few nanometres: semiconductor quantum dots confine "
"electrons so tightly that their colors become size-tunable, and single "
"emitters placed in tiny optical cavities exchange energy with single "
"photons reversibly. The engineer designs the geometry, the geometry sets "
"the allowed electromagnetic modes, and the modes decide what the light is "
"permitted to do."),
"key_points": [
"Nanophotonics studies light interacting with structures at or below the optical wavelength (1-500 nm for visible light).",
"At this scale the ray picture of optics fails; wave, near-field, and quantum effects take over.",
"Two workhorse responses: dielectric confinement (refractive index) and metallic plasmonics (free-electron sloshing).",
"Quantum dots and single emitters bring quantum mechanics in: size-tunable color and single-photon physics.",
"Applications span biosensors, flat lenses, nanolasers, photonic chips, and quantum light sources.",
"A 550 nm wavelength spans about 5,500 atoms - nanophotonics engineers that in-between world."],
"requirements": [
"Maxwell's equations in differential form (curl E, curl H).",
"The wave equation and the meaning of wavelength, frequency, and photon energy.",
"Basic quantum ideas: photons, energy levels, spontaneous emission.",
"A calculator for the scale and energy exercises in the demo."],
"standards": [
"SI units throughout: metres, hertz, joules, electron-volts for photon energy.",
"Nanometre (nm) as the working length unit of the field.",
"Photon energy conversions use E = hc/lambda with hc = 1240 eV nm."],
"citations": [C_NOVOTNY, C_MAIER, C_PRASAD],
"sig_lens": (
"Signature take: light is not a beam to be pointed - at the nanoscale it is "
"a citizen of the structure, bound by its geometry the way a river is bound "
"by its banks. The Signature builder does not fight the wavelength; he "
"builds rooms exactly its size and lets the light move in. Every device in "
"this database is a room designed for light, from the plasmon's closet to "
"the photonic crystal's forbidden city."),
},
{
"key": "light_wave",
"name": "Light as a Wave and a Particle: Wavelength, Frequency, and the Photon",
"group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
"description": (
"Light is an electromagnetic wave and a stream of photons at the same time, "
"and nanophotonics lives exactly where both descriptions matter. The wave "
"picture gives wavelength (lambda), frequency (f), and the iron law c = "
"lambda times f, with c = 299,792,458 metres per second. The particle picture "
"gives the photon energy E = h times f = hc/lambda, with h = 6.626e-34 joule "
"seconds. A handy form every nanophotonics worker memorizes is E(eV) = "
"1240/lambda(nm): a green 532 nm photon carries 2.33 eV, a red 700 nm photon "
"1.77 eV, a blue 400 nm photon 3.10 eV. These energies decide everything - "
"whether a photon can kick an electron across a semiconductor bandgap, which "
"color a quantum dot emits, and how much heat a plasmonic particle dumps. "
"Frequency sets the color your eye sees; wavelength sets the size of the "
"structures that can grab the light. The whole discipline is the art of "
"building structures measured in wavelengths and counting photons measured "
"in electron-volts."),
"how_it_works": (
"An oscillating electric field drags charges with it, and the dragged "
"charges re-radiate - that is the wave. Its wavelength in vacuum is fixed "
"by its frequency through c, and inside a material of refractive index n it "
"shrinks to lambda/n while the frequency stays put. The particle side "
"appears in every exchange of energy: atoms absorb and emit light only in "
"whole photons of energy hf, which is why a red photon can never do a blue "
"photon's job in a solar cell. Interference - waves adding crest-to-crest "
"or cancelling crest-to-trough - is the mechanism behind Bragg mirrors, "
"photonic crystals, and interferometers. Diffraction - waves bending around "
"obstacles their own size - is why subwavelength structures scatter so "
"strongly. Nanophotonics designs structures whose sizes are chosen in "
"wavelength units, so interference and diffraction become design tools "
"rather than nuisances."),
"key_points": [
"c = lambda x f always; E = hf = hc/lambda always - the two sentences the field is built on.",
"E(eV) = 1240/lambda(nm): 532 nm -> 2.33 eV, 400 nm -> 3.10 eV, 700 nm -> 1.77 eV.",
"Frequency fixes color and photon energy; wavelength fixes the structure size that can interact with it.",
"Inside a material of index n the wavelength shrinks to lambda/n; the frequency never changes.",
"Interference and diffraction become design tools when structures are sized in wavelengths."],
"requirements": [
"Arithmetic with scientific notation and unit conversion (nm, THz, eV).",
"The constants c = 2.998e8 m/s and h = 6.626e-34 J s.",
"The electron-volt: 1 eV = 1.602e-19 J."],
"standards": [
"Photon energies quoted in electron-volts; wavelengths in nanometres.",
"Frequencies in hertz with THz/GHz/PHz prefixes as appropriate."],
"citations": [C_NOVOTNY, C_SALEH, C_LOUDON],
"sig_lens": (
"Signature take: the photon is the smallest honest package in the universe - "
"it cannot be split, borrowed against, or counterfeited. The Signature "
"builder counts photons the way a banker counts gold: every electron-volt "
"accounted for, every wavelength measured against the structure. Waste a "
"photon and the books never balance."),
},
{
"key": "diffraction_limit",
"name": "The Diffraction Limit: Why Ordinary Lenses Cannot See the Nanoscale",
"group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
"description": (
"The diffraction limit is the reason nanophotonics exists. A conventional "
"lens cannot focus light to a spot smaller than about half its wavelength, "
"and cannot resolve two points closer than that - not because lenses are "
"crude, but because light is a wave. Ernst Abbe's formula gives the smallest "
"resolvable distance as d = lambda/(2 x NA), where NA is the numerical "
"aperture of the lens. For green 550 nm light and the best oil-immersion "
"objective (NA = 1.4), that is 196 nm: anything smaller blurs into a single "
"blob. Lord Rayleigh's criterion (0.61 x lambda/NA = 240 nm) says the same "
"thing with a slightly different ruler. A 50 nm transistor feature, a 20 nm "
"virus, a single molecule - all invisible to ordinary microscopes. The "
"entire field of nanophotonics is a collection of lawful evasions of this "
"limit: near-field probes that never let the light travel, plasmons that "
"squeeze light below the limit, and super-resolution tricks that switch "
"molecules on and off to beat it."),
"how_it_works": (
"A point of light imaged by a lens does not become a point - it becomes an "
"Airy disk, a bright spot ringed by faint rings, because the lens clips the "
"wave and diffraction spreads it. Two nearby points make two overlapping "
"disks, and when the disks merge, the information is gone from the far "
"field forever. The missing information is carried by evanescent waves - "
"near-field ripples that decay within a fraction of a wavelength of the "
"object and never reach the lens. Nanophotonics recovers or sidesteps them: "
"a near-field probe picks them up before they decay; a plasmonic structure "
"converts them into bound surface waves that can be guided; a fluorescent "
"molecule can be localized to a few nanometres by finding the center of its "
"blur. The limit governs propagating light only - the near field was never "
"subject to it."),
"key_points": [
"Abbe: d = lambda/(2 x NA); at 550 nm with NA 1.4 the limit is 196 nm.",
"Rayleigh: 0.61 x lambda/NA gives 240 nm under the same conditions.",
"The limit is fundamental to propagating waves, not a lens quality problem.",
"Sub-wavelength detail lives in evanescent waves that decay within ~lambda of the object.",
"Nanophotonics beats the limit with near-field probes, plasmons, and super-resolution switching."],
"requirements": [
"The Abbe and Rayleigh formulas and the meaning of numerical aperture.",
"Oil immersion (n = 1.5) as the practical NA ceiling near 1.4-1.5.",
"A calculator for the limit and ratio exercises in the demo."],
"standards": [
"Resolution quoted as a distance in nanometres at a stated wavelength and NA.",
"NA = n x sin(theta): dimensionless, at most the refractive index."],
"citations": [C_NOVOTNY, C_SALEH, C_HELL],
"sig_lens": (
"Signature take: the diffraction limit is not a wall - it is a toll booth "
"that only taxes travelers. The Signature builder does not pay the toll; "
"he walks the near field, where the light has not yet decided to leave. "
"Every subwavelength device in this database is a structure that meets the "
"light before it gets far enough away to forget the details."),
},
{
"key": "materials_response",
"name": "How Materials Answer Light: Dielectrics, Metals, and the Drude Model",
"group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
"description": (
"Every nanophotonic device is a conversation between light and matter, and "
"the material's answer is written in its permittivity - how its charges "
"move when an electric field shakes them. Dielectrics like glass and "
"silicon answer with bound electrons that stretch and spring back: the "
"permittivity stays positive, light slows by the refractive index, and "
"losses stay low. Metals like gold and silver answer with free electrons "
"that slosh as a gas: below the plasma frequency the permittivity turns "
"negative, the metal reflects, and light can bind to the surface as a "
"plasmon. The Drude model captures the free-electron answer in one line: "
"epsilon(omega) = 1 - omega_p^2/omega^2, where omega_p is the plasma "
"frequency (about 9.03 eV, or 137 nm wavelength, for gold). Above omega_p "
"the metal goes transparent; below it, negative permittivity rules. Real "
"metals add damping and interband absorption - gold's pretty colors come "
"from electrons jumping between bands, not just sloshing - but the Drude "
"picture correctly predicts the sign flip that makes plasmonics possible."),
"how_it_works": (
"Shine light on a metal and its free electrons oscillate with the field, "
"radiating a response that cancels the field inside - that cancellation is "
"reflection, and the negative permittivity is its mathematical signature. "
"The plasma frequency marks where the electrons can no longer keep up: "
"faster than omega_p, they stand still and the light passes through; slower, "
"they move with the field and the metal behaves as a mirror with a "
"negative-permittivity skin. At a metal-dielectric boundary this skin "
"supports a surface plasmon - the electrons and the light wave locked "
"together. Dielectrics have no free electrons, so their permittivity stays "
"positive and real (plus small loss); their whole contribution is the "
"refractive index n = sqrt(epsilon). Choosing the material is choosing the "
"sign of epsilon, and the sign of epsilon decides which nanophotonic "
"phenomena are even allowed."),
"key_points": [
"Permittivity epsilon(omega) is the material's complete answer to light.",
"Dielectrics: positive epsilon, low loss, light guided by refractive index.",
"Metals below the plasma frequency: negative epsilon, reflective, plasmonic.",
"Drude model: epsilon = 1 - omega_p^2/omega^2; gold's omega_p ~ 9.03 eV (137 nm).",
"Interband absorption (gold's color) rides on top of the Drude sloshing."],
"requirements": [
"Complex numbers: real part (storage) and imaginary part (loss) of epsilon.",
"Angular frequency omega = 2 x pi x f and photon energy in eV.",
"A calculator for the Drude sign-flip exercises in the demo."],
"standards": [
"Permittivity quoted as complex epsilon = epsilon' + i x epsilon''.",
"Plasma frequencies in eV (hbar x omega_p) or rad/s, stated explicitly."],
"citations": [C_MAIER, C_KREIBIG, C_NOVOTNY],
"sig_lens": (
"Signature take: the material is not the stage - it is a cast member. The "
"Signature builder auditions materials by the sign of their permittivity: "
"positive means the light passes through as a guest, negative means the "
"electrons rise to dance with it. Gold was chosen by the field the way a "
"director chooses a lead - not for being perfect, but for being brilliant "
"exactly where the light needs it."),
},
{
"key": "refractive_index",
"name": "Refractive Index: How Matter Slows, Bends, and Traps Light",
"group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
"description": (
"The refractive index n is the single number that tells you how much a "
"material slows light: light travels at c/n inside it, and its wavelength "
"shrinks to lambda/n. Air is 1.00, water 1.33, glass 1.5, silicon 3.48 at "
"telecom wavelengths. Three laws fall out of it. Snell's law (n1 x sin "
"theta1 = n2 x sin theta2) bends rays at every interface and is the whole "
"basis of lenses. Total internal reflection traps light when it tries to "
"leave a high-index material at too shallow an angle - beyond the critical "
"angle theta_c = arcsin(n2/n1), which is 41.8 degrees for glass to air, "
"nothing escapes. Fresnel's equations set the price of every interface: at "
"normal incidence a glass-air boundary reflects ((1.5-1)/(1.5+1))^2 = 4% of "
"the light. In nanophotonics the index contrast is the confinement knob: "
"silicon (3.48) surrounded by oxide (1.44) squeezes light into wires a few "
"hundred nanometres wide, because the huge contrast makes escape nearly "
"impossible."),
"how_it_works": (
"Inside a material, the light wave polarizes the atoms, and the re-radiated "
"wavelets lag behind - the sum travels slower, which is all the refractive "
"index ever meant. At an interface, the wave must keep its phase matched "
"along the boundary, and that phase-matching condition is Snell's law. When "
"light goes from high index to low index past the critical angle, no "
"transmitted wave can satisfy phase matching, so all the energy reflects - "
"but an evanescent tail still leaks a fraction of a wavelength into the low "
"index side, decaying exponentially. That tail is the handle nanophotonics "
"grips: bring a second waveguide within the tail's reach and light tunnels "
"across (directional coupling); bring a molecule and it feels the field "
"without ever entering the guide. High contrast (silicon on oxide) makes "
"the tail short and the trapping fierce; low contrast makes long gentle "
"guides."),
"key_points": [
"n = c/v: air 1.00, water 1.33, glass 1.5, silicon 3.48.",
"Snell: n1 x sin(theta1) = n2 x sin(theta2); wavelength becomes lambda/n.",
"Critical angle glass->air: 41.8 deg; beyond it, total internal reflection.",
"Normal-incidence glass reflection: 4% - every interface charges a toll.",
"Index contrast is the confinement knob: Si/SiO2 traps light in nanometre wires."],
"requirements": [
"Snell's law and the critical-angle formula.",
"Fresnel reflectance at normal incidence.",
"A calculator for the angle and toll exercises in the demo."],
"standards": [
"Refractive index dimensionless, quoted at a stated wavelength.",
"Angles measured from the surface normal, in degrees."],
"citations": [C_SALEH, C_NOVOTNY, C_PRASAD],
"sig_lens": (
"Signature take: the refractive index is a tax on speed, and the Signature "
"builder spends it where it buys confinement. Silicon's 3.48 is not a "
"number - it is a wall 3.48 times higher than air, and light that tries to "
"climb it falls back into the wire. Every nanophotonic circuit is a "
"landscape of such walls, and the light goes exactly where the walls say."),
},
{
"key": "confinement",
"name": "Confining Light: Total Internal Reflection and Waveguides",
"group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
"description": (
"A waveguide is a road for light: a high-index core wrapped in low-index "
"cladding, guiding light for centimetres or kilometres by total internal "
"reflection. The number that matters is the V-number, V = (2 x pi x a / "
"lambda) x NA, where a is the core radius and NA the numerical aperture. "
"Below V = 2.405 a round fiber carries exactly one mode - single-mode "
"operation, the cleanest possible road, used for telecom and quantum light. "
"A 4-micron-radius core with NA 0.14 at 1550 nm gives V = 2.27: single mode, "
"just barely. Make the core 25 microns with NA 0.22 at 850 nm and V = 40.7, "
"carrying about V^2/2 = 826 modes - a multimode highway, bright but messy. "
"Shrink a silicon wire to 220 by 500 nm and the single mode squeezes into a "
"spot far below the free-space wavelength: that is nanophotonic "
"confinement, the reason a whole optical circuit fits on a chip smaller "
"than a fingernail."),
"how_it_works": (
"Light trapped by total internal reflection bounces down the core, and only "
"certain bounce angles survive: the wave must reproduce itself after each "
"round trip across the core, which quantizes the allowed patterns into "
"modes. Each mode has its own propagation constant and its own field shape; "
"the fundamental mode hugs the center while higher modes wiggle. Cut the "
"core small enough (V < 2.405) and all higher modes leak away, leaving one "
"clean mode whose shape never changes - ideal for interferometers, "
"resonators, and quantum circuits. The evanescent tail outside the core is "
"the waveguide's handshake: two guides brought close exchange power "
"sinusoidally with distance (a directional coupler), and a resonator parked "
"nearby can be fed without ever touching. Bending the guide too tightly "
"spills light out of the curve - high index contrast forgives bends down to "
"a few microns radius, which is why silicon photonics can turn corners on "
"a chip."),
"key_points": [
"V-number V = (2 x pi x a/lambda) x NA decides how many modes a guide carries.",
"V < 2.405: single mode - one clean field pattern, the gold standard.",
"4 um core, NA 0.14, 1550 nm: V = 2.27 (single mode); 25 um, NA 0.22, 850 nm: V = 40.7 (~826 modes).",
"Evanescent tails enable couplers and resonator feeding without contact.",
"Tight bends need high index contrast; silicon forgives micron-scale turns."],
"requirements": [
"The V-number formula and the 2.405 single-mode cutoff.",
"Mode counting estimate V^2/2 for large-V step-index guides.",
"A calculator for the V-number exercises in the demo."],
"standards": [
"Core dimensions in microns or nanometres; wavelength stated.",
"NA dimensionless; V-number dimensionless."],
"citations": [C_SALEH, C_NOVOTNY, C_SORE],
"sig_lens": (
"Signature take: a waveguide is a promise kept over distance - the light "
"enters at one end and the mode that exits is the mode that entered, "
"kilometres later. The Signature builder lays roads, not paths: single "
"mode, low loss, corners that hold. Everything downstream - the rings, the "
"interferometers, the quantum circuits - stands on the waveguide keeping "
"its promise."),
},
{
"key": "plasmons",
"name": "Surface Plasmons: Light Riding the Skin of a Metal",
"group": "Light at the Nanoscale", "ladder_rank": 4, "ladder_tier": "compounded",
"description": (
"A surface plasmon polariton is light that has decided to travel on the "
"surface of a metal instead of through space - an electromagnetic wave "
"locked to a sloshing wave of free electrons, running along the "
"metal-dielectric boundary. Because the metal's permittivity is negative, "
"the combined wave is bound: its fields decay exponentially away from the "
"surface on both sides, squeezing the light into a skin far thinner than "
"the wavelength. Its wavevector is larger than light's in free space: "
"k_spp = k0 x sqrt(epsilon_m x epsilon_d/(epsilon_m + epsilon_d)). For gold "
"in air at 633 nm (epsilon_Au = -11.8 + 1.3i) that gives an effective index "
"of 1.045 - the plasmon wavelength is 606 nm, slightly shorter than the "
"633 nm light that made it, and it travels only about 9.6 "
"micrometres before ohmic loss eats it. That short life is the bargain of "
"plasmonics: confinement far below the diffraction limit, paid for in "
"propagation loss. Thin films do better - long-range plasmons on thin "
"gold films stretch to hundreds of microns - and the whole subfield of "
"plasmonic waveguiding is the art of spending loss wisely for "
"confinement."),
"how_it_works": (
"Solve Maxwell's equations at a metal-dielectric interface with a negative "
"permittivity on one side and out pops a bound solution: fields peaking at "
"the interface, decaying exponentially into both media, propagating along "
"the surface with a wavevector no free-space photon can match - which is "
"why you cannot excite it by just shining light at a flat film. Coupling "
"needs extra momentum: a prism in the Kretschmann geometry (light tunnels "
"through a thin film past the critical angle), a grating that adds its "
"reciprocal lattice vector, or a nanostructure that scatters with all "
"wavevectors at once. Once launched, the plasmon's energy lives partly in "
"the electron motion, and electron collisions turn it into heat - the "
"imaginary part of the permittivity sets the propagation length. The "
"confinement-loss trade is fundamental: tighter binding (more field in the "
"metal) means shorter travel. Designers pick silver for the longest run, "
"gold for chemistry that survives air, and aluminum for the ultraviolet."),
"key_points": [
"A surface plasmon polariton is a bound electron-light wave on a metal-dielectric interface.",
"k_spp = k0 x sqrt(eps_m x eps_d/(eps_m + eps_d)); Au/air at 633 nm: n_eff 1.045, 606 nm wave.",
"Fields decay exponentially from the surface: true subwavelength confinement.",
"Propagation length ~9.6 um for Au at 633 nm - confinement bought with loss.",
"Launching needs extra momentum: prism, grating, or nanostructure scattering."],
"requirements": [
"Complex permittivity and the meaning of its imaginary part (loss).",
"Wavevector, effective index, and exponential decay lengths.",
"A calculator for the SPP dispersion exercises in the demo."],
"standards": [
"Permittivities quoted at stated wavelength with real and imaginary parts.",
"Propagation length = 1/(2 x Im(k_spp)) in microns."],
"citations": [C_MAIER, C_RAETHER, C_BARNES, C_KRETSCHMANN],
"sig_lens": (
"Signature take: the plasmon is light that took off its traveling shoes "
"and moved into the metal's skin. The Signature builder respects the "
"bargain openly: so many microns of travel for so many nanometres of "
"squeeze, priced in heat. Nothing in plasmonics is free, and that honesty "
"is what makes the devices trustworthy."),
},
{
"key": "lspr",
"name": "Localized Surface Plasmon Resonance: Why Gold Nanoparticles Are Red",
"group": "Light at the Nanoscale", "ladder_rank": 4, "ladder_tier": "compounded",
"description": (
"A gold nanoparticle smaller than the wavelength does something a gold "
"mirror never does: it glows ruby red in transmission. The particle's free "
"electrons slosh back and forth as one, driven by the light field, and at "
"the localized surface plasmon resonance the sloshing hits its natural "
"frequency - the particle then scatters and absorbs enormously, with a "
"cross-section many times its geometric area. In the quasistatic limit the "
"resonance condition is beautifully simple: Re(epsilon_m) = -2 x epsilon_d, "
"the Frohlich condition. Because the right side contains the surrounding "
"medium's permittivity, the resonance color reports the local refractive "
"index - the entire basis of plasmonic biosensing. With representative "
"measured gold permittivities the condition predicts resonance near 512 nm "
"in water versus 473 nm in air: raise the index, redden the particle. "
"Shape tunes it further: rods split the resonance into transverse and "
"longitudinal modes, and stretching a gold nanorod slides its long-axis "
"resonance from green deep into the near-infrared."),
"how_it_works": (
"Treat the nanoparticle as a dipole in a uniform driving field (valid when "
"the particle is much smaller than the wavelength). Its polarizability is "
"proportional to (epsilon_m - epsilon_d)/(epsilon_m + 2 x epsilon_d), and the "
"denominator vanishes - the response explodes - exactly at the Frohlich "
"condition. The electrons move in phase, the near field around the particle "
"intensifies by factors of tens, and the far field sees a brilliant "
"scatterer. Damping (the imaginary part of epsilon) keeps the explosion "
"finite and sets the resonance width: silver is sharper than gold, gold "
"survives air and water. When two particles approach, their dipoles couple "
"and hybridize like molecular orbitals - bonding modes red-shift - which "
"is why particle dimers and aggregates change color, the plasmon ruler "
"effect. Coating the particle or binding molecules raises epsilon_d at the "
"surface and red-shifts the peak by nanometres: a spectrometer watches "
"molecules arrive in real time."),
"key_points": [
"LSPR: the whole electron cloud of a nanoparticle sloshing in resonance with light.",
"Frohlich condition Re(eps_m) = -2 x eps_d sets the resonance color.",
"~512 nm in water vs ~473 nm in air for gold spheres: index shifts the color.",
"Scattering cross-section exceeds geometric area many times over.",
"Rods split the mode; dimers hybridize; binding molecules red-shift the peak - all are sensors."],
"requirements": [
"Quasistatic (dipole) approximation: particle << wavelength.",
"The polarizability denominator and what makes it vanish.",
"A calculator for the Frohlich interpolation exercises in the demo."],
"standards": [
"Resonance wavelengths in nm at stated medium index.",
"Permittivity values representative of measured (Johnson-Christy style) data."],
"citations": [C_KREIBIG, C_BOHREN, C_MAIER, C_SONNICHSEN],
"sig_lens": (
"Signature take: a gold sphere is a bell, and light is the hammer - at the "
"resonance frequency the whole electron sea rings as one. The Signature "
"builder tunes bells, not mirrors: a nanometre of protein on the surface "
"detunes the ring by a measurable note, and the spectrometer is the ear. "
"That is sensing with no label, no battery, no moving part - just resonance."),
},
{
"key": "quantum_dots",
"name": "Quantum Dots: Artificial Atoms That Glow on Command",
"group": "Light at the Nanoscale", "ladder_rank": 4, "ladder_tier": "compounded",
"description": (
"A quantum dot is a semiconductor crystal so small - a few nanometres, a "
"few thousand atoms - that its electrons feel the walls: confine an "
"electron-hole pair in all three dimensions and its energies become "
"discrete like an atom's, but tunable by size. The Brus equation gives the "
"effective bandgap: E = E_g + (h^2/8R^2)(1/m_e + 1/m_h) - 1.8e^2/(4 x pi x "
"epsilon x epsilon_0 x R). For CdSe (E_g = 1.74 eV), a 2 nm radius dot emits "
"at 2.545 eV - 487 nm, blue-green - while a 3 nm dot emits at 2.070 eV - 599 "
"nm, orange. Same material, different color, chosen by size: that is the "
"quantum size effect, discovered in glass by Ekimov and explained by Brus. "
"Quantum dots are brighter and more photostable than dye molecules, their "
"emission lines are narrow, and one ultraviolet lamp excites every color at "
"once - which is why they light up displays, tag biology, and serve as "
"single-photon sources when isolated. They are artificial atoms with a "
"volume knob."),
"how_it_works": (
"An electron promoted to the conduction band leaves a hole in the valence "
"band; the two attract and would form a hydrogen-like exciton with the "
"semiconductor's Bohr radius (about 5.6 nm for CdSe). Squeeze the crystal "
"below that radius and the walls dominate: the particle-in-a-box kinetic "
"energy (~1/R^2) overwhelms the Coulomb attraction (~1/R), pushing the "
"levels apart as the dot shrinks. Absorb a photon above the gap and the "
"excited electron relaxes to the lowest confined level, then recombines - "
"emitting a photon of the size-set color. Surface atoms with dangling bonds "
"would trap the excitation and kill the glow, so real dots wear a shell "
"(CdSe/ZnS core-shell): the wider-gap ZnS passivates the surface and "
"confines the exciton to the core. Blink-free, shell-engineered dots now "
"hold their shine for hours under a microscope."),
"key_points": [
"3D confinement makes a semiconductor's levels discrete and size-tunable: artificial atoms.",
"Brus equation: CdSe R=2 nm -> 487 nm; R=3 nm -> 599 nm. Size is the color knob.",
"Confinement energy (~1/R^2) beats Coulomb attraction (~1/R) at small sizes.",
"Core-shell (CdSe/ZnS) passivation keeps the glow bright and steady.",
"One UV source excites all colors: displays, bio-tags, single-photon emitters."],
"requirements": [
"The Brus equation terms and the CdSe parameters (E_g, masses, epsilon).",
"Exciton Bohr radius as the confinement threshold.",
"A calculator for the size-to-color exercises in the demo."],
"standards": [
"Dot radius in nm; emission as photon energy (eV) and wavelength (nm).",
"Effective masses in units of the free electron mass."],
"citations": [C_ALIVISATOS, C_BRUS, C_EKIMOV, C_NOVOTNY],
"sig_lens": (
"Signature take: the quantum dot is proof that size is a material property. "
"The Signature builder does not shop for new elements when he wants a new "
"color - he pours the same CdSe into a smaller mold and the universe "
"repaints it. That is the deepest economy in nanophotonics: one chemistry, "
"every color, chosen by geometry alone."),
},
{
"key": "photonic_crystals",
"name": "Photonic Crystals: Semiconductors for Light",
"group": "Light at the Nanoscale", "ladder_rank": 5, "ladder_tier": "compounded",
"description": (
"A photonic crystal is a material whose refractive index repeats "
"periodically on the wavelength scale - the optical analogue of a "
"semiconductor crystal, where the periodic atomic potential gives electrons "
"bandgaps. Here the periodic index gives photons bandgaps: ranges of color "
"that cannot propagate in any direction and are perfectly reflected. The "
"simplest is the Bragg mirror: alternating quarter-wave layers of high and "
"low index (TiO2 at 2.4, SiO2 at 1.46), each lambda/(4n) thick. Six pairs "
"reflect 99.0% of the design wavelength; ten pairs reach 99.98% - a mirror "
"with no metal, no absorption, just interference. In two dimensions, "
"lattices of holes in silicon slabs guide and trap telecom light on chips; "
"in three dimensions, structures like woodpiles and inverse opals open "
"complete bandgaps that forbid light entirely. A missing hole - a defect - "
"becomes a cavity; a missing row becomes a waveguide with sharp bends. "
"Photonic crystals are how you tell light where it is not allowed to go."),
"how_it_works": (
"Each interface reflects a little; space the interfaces half a wavelength "
"apart (round trip = one full wave) and all the little reflections add in "
"phase - constructive interference builds a near-perfect mirror at the "
"Bragg wavelength lambda = 2 x n_eff x Lambda for period Lambda. Bloch's "
"theorem then organizes all possible light waves into bands, exactly as "
"for electrons, and where bands refuse to meet a gap opens. The gap's width "
"grows with index contrast: silicon/air (3.48 vs 1) opens generous gaps, "
"glass/air barely any. Break the periodicity on purpose and you create "
"defect states inside the gap - light localized to the defect, unable to "
"escape because no propagating state exists at its color. A line defect "
"guides around bends that would leak in ordinary waveguides; a point defect "
"with a carefully shifted hole reaches quality factors above a million, "
"trapping a photon for a microsecond in a volume of cubic wavelengths."),
"key_points": [
"Periodic index on the wavelength scale gives photons band structure, like electrons in crystals.",
"Bragg mirror: quarter-wave TiO2/SiO2 pairs; 6 pairs -> 99.0%, 10 pairs -> 99.98%.",
"Bandgap width grows with index contrast; Si/air is the workhorse.",
"Defects are features: missing holes make cavities (Q > 1e6), missing rows make waveguides.",
"Complete 3D gaps (woodpile, inverse opal) forbid light in all directions."],
"requirements": [
"Bragg condition lambda = 2 x n_eff x Lambda at normal incidence.",
"Quarter-wave thickness d = lambda/(4n).",
"A calculator for the mirror-stack exercises in the demo."],
"standards": [
"Periods and thicknesses in nm at stated design wavelength.",
"Reflectance as a fraction or percent; Q dimensionless."],
"citations": [C_JOANNO, C_YABLONOVITCH, C_AKAHANE, C_NODA],
"sig_lens": (
"Signature take: the photonic crystal is legislation for light - a "
"constitution written in refractive index that declares certain colors "
"illegal. The Signature builder is the legislator: he writes the period, "
"and the photons obey or reflect. And like all good law, it has deliberate "
"loopholes - the defects - where the chosen light is allowed to live."),
},
{
"key": "bandgaps",
"name": "Photonic Bandgaps: Colors That Are Forbidden to Exist",
"group": "Light at the Nanoscale", "ladder_rank": 5, "ladder_tier": "compounded",
"description": (
"Inside a photonic bandgap, light of that color simply cannot exist as a "
"propagating wave - the crystal's periodicity has organized the "
"electromagnetic modes into bands with a true gap between them, and a "
"photon in the gap has nowhere to go. Yablonovitch's 1987 proposal made "
"the consequence famous: put an excited atom inside a complete photonic "
"bandgap and spontaneous emission is inhibited, because there are no "
"optical states for the photon to be born into. The atom stays excited - "
"light's most basic process, switched off by geometry. The gap is not "
"absorption (nothing gets hot) and not reflection from a surface (there is "
"no surface) - it is a property of the infinite periodic bulk. Gaps are "
"measured as fractional bandwidths Delta_omega/omega: a 1D Bragg stack "
"reaches ~30% with high contrast, 2D silicon slabs ~20%, and full 3D "
"structures 5-15% complete gaps. Everything forbidden becomes a tool: "
"gap-guided fibers carry light in hollow cores (air!), beating material "
"limits, and gap-edge slow light crawls."),
"how_it_works": (
"Two standing waves form at the Bragg condition: one with its energy "
"peaked in the high-index material, one peaked in the low-index material. "
"Different average index means different frequencies - the degeneracy "
"splits, and between the two split frequencies no extended mode exists. "
"That is the entire origin of the gap, and it is why contrast matters: "
"bigger index difference, bigger split, wider gap. An emitter inside the "
"gap finds the local density of optical states near zero, so Fermi's "
"golden rule gives it almost nowhere to emit to - its lifetime stretches. "
"At the gap's edge the bands flatten (group velocity -> 0), which is slow "
"light for free. Introduce disorder and the gap fills with localized "
"states; introduce a deliberate defect and you get exactly one allowed "
"state - a cavity whose photon cannot leak because leakage would require "
"traveling in a forbidden color."),
"key_points": [
"A photonic bandgap is a true absence of propagating states, not absorption.",
"Origin: Bragg-split standing waves peak in different materials, splitting in frequency.",
"Spontaneous emission can be inhibited inside a complete gap (Yablonovitch 1987).",
"Fractional gaps: ~30% in 1D high-contrast stacks, 5-15% complete in 3D.",
"Hollow-core gap fibers guide light in air; gap edges give slow light."],
"requirements": [
"Bloch's theorem intuition: periodic media organize waves into bands.",
"Local density of states and Fermi's golden rule (emission needs states).",
"A calculator for the gap-fraction exercises in the demo."],
"standards": [
"Gaps quoted as fractional bandwidth Delta_omega/omega_mid or Delta_lambda/lambda.",
"Frequencies normalized to c/a where a is the lattice period."],
"citations": [C_YABLONOVITCH, C_JOANNO, C_KLEPPNER, C_VLASOV],
"sig_lens": (
"Signature take: the bandgap is the Signature builder's veto - a color "
"struck from the laws of a small universe he authored. An atom inside "
"cannot do the one thing atoms always do, because the room was built with "
"no door for its photon. To forbid light by geometry alone, with no energy "
"spent and nothing heated, is the purest power in optics."),
},
{
"key": "subwavelength_waveguides",
"name": "Subwavelength Waveguides: Light in Channels Thinner Than Itself",
"group": "Light at the Nanoscale", "ladder_rank": 5, "ladder_tier": "compounded",
"description": (
"A slot waveguide does something that sounds impossible: it carries most "
"of its light inside a low-index slot only 50 nm wide - thirty times "
"narrower than the 1550 nm wavelength - sandwiched between two silicon "
"rails. The trick is a boundary condition: the normal component of the "
"electric displacement D must be continuous across the silicon-air wall, so "
"E jumps by (n_Si/n_slot)^2 = (3.48/1)^2 = 12.1 at each wall, and the "
"intensity in the slot beats the rails by ~147 times. Light is literally "
"squeezed into the gap by electrostatics. Plasmonic waveguides go further: "
"a metal-insulator-metal slot or a nanoparticle chain binds light to charge "
"sloshing, reaching mode areas of (lambda/50)^2 and below - at the price of "
"propagation lengths measured in microns. Dielectric slots keep kilometres "
"of low loss with lambda/30 confinement; plasmonic slots trade distance for "
"extreme squeeze. Together they are the wiring of nanophotonics: roads "
"narrower than the cars."),
"how_it_works": (
"For the polarization with E across the slot, continuity of D_normal = "
"epsilon x E_normal forces the field in the low-index slot far above the "
"field in the high-index rails - the discontinuity does the squeezing, no "
"resonance required. The mode is still guided by total internal reflection "
"of the composite structure, so it propagates with dielectric losses "
"(tiny), while its peak intensity sits in the accessible slot - perfect for "
"sensing, nonlinear optics, and trapping, since analytes and atoms can be "
"placed exactly where the light is brightest. Plasmonic variants replace "
"one rail with metal: the mode becomes a gap plasmon with even tighter "
"confinement and metal loss to match. Nanoparticle chains guide by "
"near-field dipole coupling, hopping the excitation down the line below "
"the diffraction limit. The design rule is always the same: discontinuity "
"concentrates, resonance amplifies, metal spends."),
"key_points": [
"Slot waveguide: 50 nm air slot carries 1550 nm light via the D-continuity field jump.",
"Field enhancement (3.48/1)^2 = 12.1x; intensity ~147x in the slot.",
"Dielectric slots: lambda/30 confinement with low loss; analytes sit where light peaks.",
"Plasmonic slots/chains: (lambda/50)^2 modes, micron-scale propagation - squeeze for distance.",
"Rule: discontinuity concentrates, resonance amplifies, metal spends."],
"requirements": [
"Boundary conditions: continuity of D_normal and E_tangential.",
"Mode area and confinement factor definitions.",
"A calculator for the enhancement exercises in the demo."],
"standards": [
"Slot widths in nm; enhancement factors dimensionless.",
"Propagation loss in dB per micron (plasmonic) or per cm (dielectric)."],
"citations": [C_NOVOTNY, C_DIONNE, C_QUINTEN, C_MAIER2],
"sig_lens": (
"Signature take: the slot waveguide is a hallway built for a giant, used "
"by a mouse - except the mouse is the light and the hallway squeezes it "
"on purpose. The Signature builder learned that walls are lenses: two "
"silicon walls 50 nm apart focus 1550 nm light better than any glass ever "
"could, because the boundary condition does the focusing for free."),
},
{
"key": "nano_antennas",
"name": "Optical Nano-Antennas: Radio Towers Rebuilt for Light",
"group": "Resonances and Cavities", "ladder_rank": 6, "ladder_tier": "compounded",
"description": (
"A radio antenna turns guided radio waves into free-space waves and back; "
"an optical nano-antenna does the same for light, at a hundred thousand "
"times smaller scale. A half-wave dipole for 800 nm light, shortened by the "
"plasmonic effective index of ~2, is just 200 nm of gold - yet it captures "
"light from an area about four times its geometric footprint, because a "
"resonant antenna's cross-section is set by the wavelength, not the metal. "
"The recipe is scaled from radio: length ~ lambda/(2 x n_eff), feed gap at "
"the center where the field peaks, impedance matched to the load. But at "
"optical frequencies metals are no longer perfect conductors - the field "
"penetrates, electrons have inertia, and the resonance red-shifts and "
"broadens. Bowtie antennas (two triangles tip to tip) squeeze light into "
"their 10 nm gap with thousand-fold intensity boosts, brightening single "
"molecules a thousand times. Yagi-Uda designs (a driven rod plus directors) "
"beam a quantum dot's emission in one direction. The antenna is the "
"adapter between the nanoworld and the far field."),
"how_it_works": (
"Drive a metal rod at its plasmon resonance and the conduction electrons "
"oscillate as a standing wave, current maximal at the center, charge piling "
"at the ends - exactly the half-wave dipole mode, with the effective "
"wavelength shortened because the wave lives partly as electron motion. "
"The rod radiates like any dipole but with a cross-section far above its "
"physical size; reciprocity says it receives equally well, funneling "
"incident light into its feed gap. Put a quantum emitter in the gap and "
"two things happen: the antenna's concentrated vacuum field speeds up "
"emission (Purcell effect) and its radiation pattern reshapes where the "
"photons go. Gap plasmons between two arms hybridize and focus the field "
"into the tiny gap volume. Directivity comes from phasing: directors "
"slightly shorter than resonant pull the phase forward, reflectors slightly "
"longer push it back - the Yagi-Uda playbook, rewritten in gold at 200 nm "
"scale."),
"key_points": [
"Optical nano-antenna: resonant metal structure coupling guided/near-field energy to free space.",
"800 nm half-wave dipole in n_eff=2: 200 nm long; captures ~4x its geometric area.",
"Metals are imperfect at optical frequencies: field penetration red-shifts and broadens the resonance.",
"Bowtie gaps give 1000x intensity boosts and 1000x single-molecule fluorescence gains.",
"Yagi-Uda layouts beam single-emitter photons unidirectionally."],
"requirements": [
"Half-wave dipole scaling L ~ lambda/(2 x n_eff) and the plasmonic shortening idea.",
"Reciprocity: a good radiator is a good receiver.",
"A calculator for the antenna-size exercises in the demo."],
"standards": [
"Antenna dimensions in nm at stated free-space wavelength.",
"Enhancement factors as intensity ratios, dimensionless."],
"citations": [C_NOVOTNY2, C_MUHLSCHLEGEL, C_BIAGIONI, C_KINKHABWALA],
"sig_lens": (
"Signature take: the antenna is a translator, fluent in both the whisper "
"of the near field and the shout of the far field. The Signature builder "
"places his quantum dots in the antenna's feed gap the way a speaker is "
"placed at a microphone - not to change the voice, but to make sure the "
"room hears it. Every photon that leaves correctly is a message delivered."),
},
{
"key": "metasurfaces",
"name": "Metasurfaces: Flat Lenses From a Single Layer of Nanostructures",
"group": "Resonances and Cavities", "ladder_rank": 6, "ladder_tier": "compounded",
"description": (
"A metasurface replaces a curved glass lens - centimetres of polished "
"glass - with a single flat layer of nanostructures, each smaller than the "
"wavelength, each imprinting a chosen phase shift on the light passing "
"through. Arrange the phase to follow Phi(r) = -(2pi/lambda)(sqrt(r^2+f^2) "
"- f) and the flat sheet focuses like a lens of focal length f: a metalens. "
"The generalized Snell's law runs the show: n_t x sin(theta_t) - n_i x "
"sin(theta_i) = (lambda/2pi) x dPhi/dx, so a phase gradient steers light "
"without any bulk optic - a 2-micron-period gradient bends 800 nm light by "
"23.6 degrees. Each nano-post acts as a truncated waveguide whose width "
"sets its phase delay; silicon posts give full 0-to-2pi control with high "
"transmission. Metalenses now focus visible light to diffraction-limited "
"spots, correct chromatic aberration with dispersion-engineered posts, and "
"generate holograms and vortex beams from a surface thinner than a "
"bacterium. Flat optics is optics with the bulk removed."),
"how_it_works": (
"Every subwavelength scatterer re-radiates with an amplitude and phase set "
"by its geometry - its electric and magnetic dipole resonances. Huygens' "
"metasurfaces balance the two so the element transmits fully while its "
"phase sweeps 0 to 2pi as the post widens. Tile the surface with posts "
"whose widths encode the target wavefront, and the transmitted field is "
"the sampled wavefront: lens, axicon, hologram, beam-steerer, all from one "
"lithography step. Plasmonic (metal) versions came first and proved the "
"principle; all-dielectric (silicon, TiO2) versions won on efficiency, "
"reaching 80%+ focusing efficiency in the visible. The price is "
"chromaticity: one geometry gives one phase map at one wavelength, so "
"broadband designs stack resonances or use computational co-design. The "
"reward is optics that weigh nothing, cost little, and drop into phone "
"cameras and AR glasses."),
"key_points": [
"Metasurface: subwavelength resonators imprinting a designed phase map on a flat sheet.",
"Generalized Snell: phase gradient steers light; 2 um period bends 800 nm light 23.6 deg.",
"Metalens phase profile Phi(r) = -(2pi/lambda)(sqrt(r^2+f^2) - f).",
"Si/TiO2 posts: 0-2pi phase with 80%+ efficiency; plasmonic versions proved the idea.",
"One lithography step makes lenses, holograms, vortex beams - flat, light, cheap."],
"requirements": [
"The generalized law of refraction with a phase gradient.",
"Metalens phase profile and the meaning of each term.",
"A calculator for the steering and phase exercises in the demo."],
"standards": [
"Phase in radians, modulo 2pi; gradients per micron.",
"Efficiencies as fractions of incident power."],
"citations": [C_YU, C_YU2, C_KHORASANINEJAD, C_AIETA, C_KILDISHEV],
"sig_lens": (
"Signature take: the metasurface is the lens with its body removed - only "
"the decision remains, printed in silicon posts. The Signature builder "
"loved this the moment he saw it: no grinding, no polishing, no weight - "
"just a phase map, computed and etched. It is optics reduced to pure "
"information, and information is the cheapest material there is."),
},
{
"key": "near_field",
"name": "Near-Field Optics: Light That Never Leaves Home",
"group": "Resonances and Cavities", "ladder_rank": 6, "ladder_tier": "compounded",
"description": (
"The near field is the light that stays home: evanescent waves clinging "
"within a fraction of a wavelength of their source, carrying the fine "
"detail that propagating waves cannot. Synge proposed in 1928 that a tiny "
"aperture scanned close to a sample could beat the diffraction limit, and "
"the near-field scanning optical microscope (NSOM) made it real: a "
"50 nm aperture held nanometres above the surface collects the evanescent "
"detail before it decays, resolving far below Abbe's 196 nm. The "
"penetration depth sets the working distance - for glass (n=1.5) at 60 "
"degrees incidence and 500 nm light, the evanescent tail reaches only 96 "
"nm into the air. Aperture probes trade throughput for resolution (a 50 nm "
"hole passes almost nothing); apertureless tips trade background for "
"signal, scattering the near field with a sharp metal tip like a radio "
"antenna in reverse. Near-field optics is also the microscope that "
"launched plasmonics: it sees the plasmons running."),
"how_it_works": (
"Total internal reflection leaves an evanescent tail decaying as "
"exp(-z/d_p) with penetration depth d_p = lambda/(2 x pi x sqrt(n1^2 x "
"sin^2(theta) - n2^2)) - 96 nm for the glass example above. That tail "
"contains spatial frequencies beyond k0, i.e. the subwavelength detail, "
"but it carries no power away. An NSOM tip frustrates it: the subwavelength "
"aperture or sharp tip scatters the evanescent components into propagating "
"ones the detector can see, pixel by pixel as the tip scans. Resolution is "
"set by the tip size, not the wavelength - 50 nm routinely, 10 nm with "
"sharp tips. The cost is speed (scanning) and signal (tiny throughputs), "
"so the far-field super-resolution methods (STED, PALM/STORM) that switch "
"molecules on and off now dominate biology - while near-field probes "
"remain the way to map plasmonic and photonic modes themselves, watching "
"light run along waveguides and swirl in resonators."),
"key_points": [
"Near field = evanescent waves within ~lambda of the source, holding subwavelength detail.",
"Synge 1928 -> NSOM: a 50 nm aperture scanned in the near field beats Abbe's 196 nm.",
"Penetration depth: 96 nm for glass, 60 deg, 500 nm - the working distance.",
"Aperture tips trade throughput for resolution; apertureless tips scatter with a sharp probe.",
"Super-resolution (STED/PALM) now serves biology; near-field still maps photonic modes."],
"requirements": [
"Evanescent decay and the penetration-depth formula.",
"Why the near field was never subject to the diffraction limit.",
"A calculator for the decay-length exercises in the demo."],
"standards": [
"Decay lengths and resolutions in nm at stated wavelength and angle.",
"Throughputs as fractions of incident power."],
"citations": [C_PAESLER, C_SYNGE, C_DUNN, C_BETZIG],
"sig_lens": (
"Signature take: the near field is light's private diary - it writes the "
"truth about the surface and never means for it to travel. The Signature "
"builder reads diaries: he parks his tip 10 nm above the gold and watches "
"the plasmons run, because the far field only ever hears the gossip. What "
"you measure depends on how close you dare to stand."),
},
{
"key": "purcell",
"name": "The Purcell Effect: A Cavity That Hurries an Atom to Shine",
"group": "Resonances and Cavities", "ladder_rank": 6, "ladder_tier": "compounded",
"description": (
"In 1946 Purcell realized that spontaneous emission is not a property of "
"the atom alone: put the atom in a cavity and the cavity changes how fast "
"it radiates. The Purcell factor F_p = (3/4 x pi^2) x (lambda/n)^3 x (Q/V) "
"says how much faster: it grows with the cavity's quality factor Q and "
"shrinks with its mode volume V. A cavity with Q = 10,000 and a "
"diffraction-limited volume V = (lambda/n)^3 gives F_p = 760 - an emitter "
"that lived 1 nanosecond in free space now lives 1.3 picoseconds, "
"dumping its photon into the cavity mode 760 times faster. Drexhage "
"proved it in 1974 with molecules near a mirror; Gerard's group showed it "
"for quantum dots in micropillars in 1998. The reverse also works: a "
"photonic bandgap with no states at the emission color inhibits emission "
"(Kleppner, Yablonovitch). The Purcell effect is why nanolasers can be "
"fast, why single-photon sources are bright, and why cavity QED exists at "
"all - the vacuum itself is engineerable."),
"how_it_works": (
"Fermi's golden rule: the emission rate is proportional to the local "
"density of optical states times the coupling. A cavity concentrates the "
"vacuum fluctuations into its narrow resonance - the density of states at "
"the cavity frequency scales as Q/V, so an emitter tuned to the resonance "
"and placed at the field maximum radiates Q/V times faster into the mode. "
"Detune it or move it to a node and the effect vanishes: position and "
"spectrum are everything, which is why deterministic placement of quantum "
"dots in photonic-crystal cavities is a whole art. The beta-factor - the "
"fraction of emission going into the desired mode - approaches 1 in good "
"designs, meaning nearly every photon is useful. Plasmonic cavities push "
"V to (lambda/100)^3 and reach Purcell factors of thousands despite low Q, "
"trading speed for loss. The cavity does not create photons; it "
"reorganizes the vacuum so the atom cannot help but emit into the mode."),
"key_points": [
"Purcell factor F_p = (3/4pi^2)(lambda/n)^3(Q/V): cavities reshape spontaneous emission.",
"Q=1e4, V=(lambda/n)^3 -> F_p=760; 1 ns becomes 1.3 ps.",
"Emission needs optical states: cavities enhance, bandgaps inhibit.",
"Position and detuning are everything: field maximum, on resonance.",
"Plasmonic cavities: V~(lambda/100)^3 gives F_p in the thousands despite low Q."],
"requirements": [
"Fermi's golden rule in words: rate ~ density of states x coupling.",
"Q (energy stored / energy lost per cycle) and mode volume V.",
"A calculator for the Purcell-factor exercises in the demo."],
"standards": [
"V in units of (lambda/n)^3; F_p dimensionless.",
"Lifetimes in ns/ps at stated wavelength."],
"citations": [C_PURCELL, C_DREXHAGE, C_GERARD, C_VAHALA],
"sig_lens": (
"Signature take: Purcell taught that even spontaneity obeys architecture. "
"The atom wants to emit whenever it pleases - the Signature builder builds "
"a room where pleasing means emitting into his cavity, 760 times faster, "
"on his schedule. The vacuum is not empty; it is a crowd, and the cavity "
"decides which way the crowd leans."),
},
{
"key": "wgm",
"name": "Whispering-Gallery Resonators: Light Running in Circles",
"group": "Resonances and Cavities", "ladder_rank": 6, "ladder_tier": "compounded",
"description": (
"Lord Rayleigh explained the whispering gallery of St Paul's Cathedral - "
"whispers traveling along the curved wall - and light does the same in a "
"glass microsphere: trapped by total internal reflection, it circles the "
"equator millions of times. A 50-micron silica sphere at 1550 nm holds mode "
"number ~147 (m = pi x n x D/lambda), its resonances spaced by a free "
"spectral range of 10.5 nm (1.32 THz), and with Q = 1e8 a photon lives 82 "
"nanoseconds - circling an effective 17 metres inside a 50-micron bead. "
"These are the highest-Q man-made optical cavities on Earth: toroids and "
"spheres reach 1e8-1e9, microdisks lase (McCall 1992), and the narrow "
"linewidths make them exquisite sensors - a single virus binding to the "
"surface shifts the resonance measurably. Kerr combs (frequency combs from "
"microresonators), cavity optomechanics, and ultra-stable lasers all ride "
"on whispering galleries. The circle is the perfect trap: no mirrors, no "
"ends, just curvature."),
"how_it_works": (
"The mode must reproduce itself after one round trip: m x lambda = pi x n "
"x D (circumference in optical path), which quantizes the allowed "
"wavelengths into a comb spaced by the FSR = c/(pi x n x D). Confinement is "
"by continuous total internal reflection - the mode hugs the surface in "
"an evanescent-touched ring, with radiation loss dropping exponentially as "
"the sphere grows. The Q is limited by material absorption, surface "
"scattering, and coupling: silica's transparency window gives the record "
"values. Feed it with a tapered fiber touching the equator - the evanescent "
"tails overlap and power tunnels in with near-unity efficiency at critical "
"coupling. Nonlinearities love the intensity build-up (proportional to Q): "
"microwatts in give watts circulating, spawning Kerr frequency combs and "
"Raman lasers. A particle binding to the surface changes the effective path "
"by a sliver - and the resonance frequency moves by a detectable sliver."),
"key_points": [
"Whispering-gallery modes: light circling by continuous total internal reflection.",
"50 um silica sphere at 1550 nm: mode ~147, FSR 10.5 nm (1.32 THz).",
"Q=1e8 -> 82 ns photon lifetime -> 17 m effective path in a 50 um bead.",
"Tapered-fiber evanescent coupling feeds them with near-unity efficiency.",
"Record Q/V enables Kerr combs, optomechanics, single-virus sensing."],
"requirements": [
"Round-trip phase condition m x lambda = pi x n x D.",
"FSR, Q, and photon lifetime tau = Q/omega.",
"A calculator for the resonator exercises in the demo."],
"standards": [
"Diameters in microns; FSR in nm or THz; Q dimensionless.",
"Effective path length in metres."],
"citations": [C_VAHALA, C_ILCHENKO, C_MCCALL, C_KIPPENBERG],
"sig_lens": (
"Signature take: the whispering gallery is patience made of glass - a "
"photon that would cross the bead in a femtosecond instead stays 82 "
"nanoseconds, running 17 metres of laps. The Signature builder admires "
"this above all traps because it has no doors to maintain: the light "
"stays because the circle gives it no reason to leave. Endurance, not "
"force, is the confinement."),
},
{
"key": "plasmonic_waveguides",
"name": "Plasmonic Waveguides: Squeezing Light Onto Metal Rails",
"group": "Resonances and Cavities", "ladder_rank": 6, "ladder_tier": "compounded",
"description": (
"Plasmonic waveguides trade distance for squeeze: they bind light to metal "
"surfaces and carry it in modes far below the diffraction limit. The "
"family spans the single-interface SPP (tens of microns of travel), "
"long-range SPPs on thin metal films (Sarid 1981, Berini's reviews: "
"hundreds of microns by pushing the field out of the metal), metal- "
"insulator-metal slot guides (Dionne 2006: deep subwavelength slots, "
"micron-scale travel), channel plasmons in V-grooves (Bozhevolnyi 2006: "
"real waveguide components - interferometers, ring resonators - in "
"grooves), and nanoparticle chains (Quinten 1998, Maier 2003: energy "
"hopping bead to bead below the limit). At 1550 nm on gold (epsilon = "
"-131.9 + 12.65i) the single-interface SPP travels ~343 microns with an "
"effective index of just 1.004 - barely slower than light, loosely bound. "
"Squeeze harder with a 50 nm MIM slot and the mode shrinks to lambda/20 "
"while the travel shrinks to microns. The design law is fixed: "
"confinement x propagation length is roughly conserved for a given metal "
"and wavelength - pick your point on the curve."),
"how_it_works": (
"Every plasmonic guide solves the same bargain: the fraction of modal "
"energy living in the metal sets both the confinement and the loss, "
"because only metal dissipates. Thin-film long-range modes arrange the "
"field symmetrically so it mostly lives in the dielectric - low loss, weak "
"confinement. MIM slots do the opposite: the gap plasmon piles the field "
"into the nanometre insulator gap, giving extreme intensity where "
"molecules or nonlinear materials can sit. V-groove channels focus the "
"mode at the groove's bottom tip. Nanoparticle chains work differently: "
"each particle is a resonant dipole, and near-field coupling passes the "
"excitation along - the chain is a subwavelength wire made of coupled "
"resonators, with group velocity set by the coupling strength. Hybrid "
"plasmonic-photonic guides (a high-index wire near a metal film) split "
"the difference: photonic-low-loss travel with a plasmonic hot spot for "
"interaction."),
"key_points": [
"Plasmonic guides: subwavelength modes on metal, microns-to-mm travel.",
"Au at 1550 nm: single-interface SPP travels ~343 um, n_eff 1.004.",
"Long-range thin-film modes: symmetric fields dodge the metal, travel far.",
"MIM slots and V-grooves: lambda/20 modes, micron travel, huge intensity.",
"Law: confinement x propagation length ~ conserved per metal and wavelength."],
"requirements": [
"The confinement-loss trade and what sets each end.",
"Mode families: single-interface, long-range, MIM, channel, chains.",
"A calculator for the propagation-length exercises in the demo."],
"standards": [
"Propagation lengths in microns; mode widths as fractions of lambda.",
"Permittivities at stated wavelength."],
"citations": [C_SARID, C_BERINI, C_DIONNE, C_BOZHEVOLNYI, C_MAIER2],
"sig_lens": (
"Signature take: the plasmonic waveguide is a sprinter, not a marathoner "
"- it will never carry light across the chip, but nothing carries it "
"tighter. The Signature builder uses sprinters for the last hundred "
"nanometres: get the photon close with cheap photonic roads, then let the "
"plasmon do the violent, brilliant, brief work of touching the molecule. "
"Right tool, right distance, no sentimentality."),
},
{
"key": "strong_coupling",
"name": "Strong Coupling and Cavity QED: When Atom and Light Become One",
"group": "Quantum Nanophotonics", "ladder_rank": 7, "ladder_tier": "advanced",
"description": (
"Weak coupling hurries or slows emission; strong coupling does something "
"stranger: the atom and the photon lose their separate identities and form "
"a new entity, the polariton, that oscillates between matter and light. The "
"criterion is a race: the coherent exchange rate g must beat the decay "
"rates - g > (kappa + gamma)/2, where kappa is the cavity photon loss rate "
"and gamma the emitter decay rate. Take a quantum dot in a photonic-crystal "
"cavity: g/2pi = 20 GHz, kappa/2pi = 30 GHz, gamma/2pi = 1 GHz. Since 20 > "
"15.5, the system is strongly coupled, with cooperativity C = g^2/(kappa x "
"gamma) = 13.3. The smoking gun is the vacuum Rabi splitting: the cavity "
"transmission shows two peaks split by 2g (40 GHz here, 0.108 nm at 900 nm) "
"instead of one. This is cavity quantum electrodynamics - the physics "
"behind single-photon transistors, photon blockade (one photon blocks the "
"next), and quantum networks where stationary qubits (atoms, dots) talk "
"through flying qubits (photons). Nanophotonics made it practical by "
"shrinking V until g - which scales as 1/sqrt(V) - wins the race."),
"how_it_works": (
"The Jaynes-Cummings model couples a two-level emitter to one cavity mode: "
"the eigenstates are dressed states, part atom and part photon, split by "
"2g x sqrt(n+1) for n photons. With zero photons the vacuum itself splits "
"the line - vacuum Rabi splitting - because the atom perpetually emits and "
"reabsorbs a virtual photon. If g dominates, an excitation oscillates "
"between atom and cavity (Rabi oscillation) before leaking out; if loss "
"dominates, it just decays faster (Purcell regime). Reaching strong "
"coupling needs small V (photonic-crystal cavities, micropillars, plasmonic "
"gaps), high Q, and an emitter parked at the field maximum with its line "
"narrower than g. The payoff is nonlinearity at the single-photon level: "
"in photon blockade the first photon shifts the dressed states so a second "
"identical photon cannot enter - a transistor for light, switched by one "
"quantum."),
"key_points": [
"Strong coupling: g > (kappa+gamma)/2 - coherent exchange beats decay.",
"Example: 20 GHz > 15.5 GHz; cooperativity C = 13.3.",
"Vacuum Rabi splitting 2g = 40 GHz (0.108 nm at 900 nm) is the smoking gun.",
"Dressed states (polaritons) are half-atom, half-photon.",
"Enables photon blockade and single-photon transistors; needs tiny V, high Q."],
"requirements": [
"The Jaynes-Cummings picture: emitter + one cavity mode.",
"g, kappa, gamma and the strong-coupling inequality.",
"A calculator for the race and splitting exercises in the demo."],
"standards": [
"Rates as angular or cyclic frequencies, stated; 2pi factors explicit.",
"Cooperativity C dimensionless."],
"citations": [C_RAIMOND, C_VUCKOVIC, C_LODAHL, C_LOUDON],
"sig_lens": (
"Signature take: strong coupling is a marriage - after it, asking whether "
"the energy is in the atom or the photon is like asking which dancer is "
"dancing the tango. The Signature builder performs marriages: he shrinks "
"the room until the vacuum itself insists on the union, and then one "
"photon can forbid another. That is control at the level of existence, "
"not intensity."),
},
{
"key": "single_photon",
"name": "Single-Photon Sources: One Photon, Exactly, On Demand",
"group": "Quantum Nanophotonics", "ladder_rank": 7, "ladder_tier": "advanced",
"description": (
"Quantum cryptography, quantum computing, and quantum networks all need "
"the same impossible thing: exactly one photon, emitted when asked, "
"identical to the last one. A laser cannot do it (its photons come in "
"Poisson-distributed bunches); an attenuated laser fakes it badly. The "
"test is the second-order correlation g2(0): send the light to a "
"beamsplitter with a detector on each output - a true single-photon "
"source never clicks both at once. g2(0) = 0 is perfect; below 0.5 proves "
"single photons. Measured count example: side coincidence peaks average "
"1000, the zero-delay peak has 12 counts with 8 accidental - g2(0) = "
"(12-8)/1000 = 0.004, decisively single photons. Semiconductor quantum "
"dots (Michler 2000, Santori 2002) are the leading platform: excite the "
"dot, it emits one photon and must be re-excited before emitting again - "
"antibunching by construction. In micropillar cavities with Purcell "
"enhancement they now deliver 50%+ collection efficiency with 99%+ "
"indistinguishability (Senellart 2017, Somaschi 2016): on-demand, bright, "
"identical photons, the currency of photonic quantum technology."),
"how_it_works": (
"A single two-level emitter can hold only one excitation, so after "
"emitting it goes dark until re-pumped - the photon stream is "
"antibunched, with a dead time no classical source can mimic. The "
"Hanbury Brown-Twiss setup measures it: coincidences between two "
"detectors versus delay show missing counts at zero delay, the "
"antibunching dip, whose depth gives g2(0). Brightness needs the Purcell "
"effect (cavity funnels emission into one mode) and good out-coupling "
"(micropillars, photonic nanowires, circular Bragg gratings). "
"Indistinguishability needs quiet: charge noise and phonons dephase the "
"emitter, so resonant excitation and cryogenic temperatures keep each "
"photon's wavepacket identical - verified by Hong-Ou-Mandel interference, "
"where two identical photons entering a beamsplitter always exit together. "
"The remaining enemies are blinking, spectral wandering, and multi-photon "
"emission from the biexciton - each suppressed by design and filtering."),
"key_points": [
"g2(0) < 0.5 proves single photons; 0.004 measured: 12 counts vs 1000, 8 accidental.",
"Quantum dots antibunch by construction: one excitation, one photon, then dark.",
"Micropillar + Purcell: 50%+ efficiency, 99%+ indistinguishability, on demand.",
"Hong-Ou-Mandel interference verifies photons are identical.",
"Enemies: blinking, spectral wander, biexciton multi-photon emission."],
"requirements": [
"Second-order correlation g2(tau) and the Hanbury Brown-Twiss setup.",
"Antibunching vs Poisson statistics.",
"A calculator for the g2(0) exercises in the demo."],
"standards": [
"g2(0) dimensionless; count rates in counts/s.",
"Indistinguishability as HOM visibility fraction."],
"citations": [C_MICHLER, C_SANTORI, C_SENELLART, C_GRANGIER, C_SOMASCHI],
"sig_lens": (
"Signature take: the single photon is the honest coin - it cannot be "
"split, and the beamsplitter is the assayer. The Signature builder mints "
"his coins one at a time in quantum dots, because quantum money must be "
"uncounterfeitable by physics itself. g2(0) = 0.004 is not a specification; "
"it is a sworn oath, counted in coincidences."),
},
{
"key": "biosensing",
"name": "Nanophotonic Biosensing: Watching Single Molecules Arrive",
"group": "Sensing and Energy", "ladder_rank": 7, "ladder_tier": "advanced",
"description": (
"Nanophotonic biosensors watch molecules bind in real time, with no labels "
"and no waiting: the sensor is a resonant structure whose color shifts "
"when biomolecules raise the local refractive index. Two families rule. "
"Propagating SPR (Liedberg 1983, Homola's reviews): a gold film in the "
"Kretschmann geometry, sensitivity ~3000 nm per refractive-index unit "
"(RIU) - a 0.005 RIU protein layer swings the resonance 15 nm. Localized "
"LSPR (Anker 2008, Mayer & Hafner 2011): gold nanoparticles, sensitivity "
"~200 nm/RIU - the same layer shifts the peak 1.0 nm, readable on a "
"0.02 nm-resolution spectrometer for a 1e-4 RIU detection limit. The figure "
"of merit is sensitivity divided by linewidth: sharp resonances see "
"smaller shifts. Modern designs push further - plasmonic nanorod "
"metamaterials (Kabashin 2009), nanohole arrays with extraordinary "
"transmission (Ebbesen 1998) for imaging, whispering-gallery toroids that "
"feel single viruses, and photonic-crystal cavities that weigh single "
"proteins by their resonance pull. The endpoint is digital: counting "
"molecules one by one as they land."),
"how_it_works": (
"A binding event replaces water (n=1.33) with protein (n~1.45) inside the "
"mode's evanescent field; the effective index rises, and every resonance "
"condition containing n moves to longer wavelength. The shift is Delta_"
"lambda = S x Delta_n, with S the bulk sensitivity - so the game is "
"maximizing field overlap with the binding region while minimizing the "
"linewidth. SPR spreads its field ~200 nm into the solution (great for "
"bulk, wasteful for monolayers); LSPR concentrates its field within ~10-30 "
"nm of the particle (perfect for monolayers, blind to bulk). "
"Functionalization decides what binds: antibodies, aptamers, or molecular "
"imprints on the gold capture the target from serum while the reference "
"channel subtracts drift and temperature. Microfluidics delivers the "
"sample; the spectrometer or intensity readout reports kinetics - on-rate, "
"off-rate, affinity - in minutes, the numbers drug discovery pays for."),
"key_points": [
"Label-free: molecular binding raises local index, shifting a resonance.",
"SPR: ~3000 nm/RIU (15 nm for a protein layer); LSPR: ~200 nm/RIU (1.0 nm).",
"1e-4 RIU detection limit with a 0.02 nm spectrometer.",
"SPR sees 200 nm deep (bulk); LSPR sees 10-30 nm (monolayers).",
"Figure of merit = sensitivity/linewidth; endpoint is single-molecule counting."],
"requirements": [
"Resonance shift Delta_lambda = S x Delta_n.",
"Evanescent field depth vs analyte size.",
"A calculator for the shift and limit exercises in the demo."],
"standards": [
"Sensitivity in nm/RIU; detection limits in RIU or g/mL.",
"Linewidths (FWHM) in nm."],
"citations": [C_LIEDBERG, C_HOMOLA, C_ANKER, C_MAYER, C_ALTuG],
"sig_lens": (
"Signature take: the biosensor is a scale that weighs ghosts - molecules "
"too small to see, counted by the reddening of gold. The Signature builder "
"trusts no label and no dye: the molecule announces itself by changing "
"the local speed of light, and the resonance reports it honestly. To "
"watch one protein land, in real time, with nothing attached to it - that "
"is measurement with manners."),
},
{
"key": "sers",
"name": "Surface-Enhanced Raman: A Million Times Louder Fingerprints",
"group": "Sensing and Energy", "ladder_rank": 7, "ladder_tier": "advanced",
"description": (
"Raman scattering identifies molecules by their vibrational fingerprints, "
"but it is whisper-quiet - cross-sections around 1e-30 cm^2, fourteen "
"orders below fluorescence. Surface-enhanced Raman scattering (SERS), "
"discovered in 1974-77 on rough silver electrodes (Fleischmann, Jeanmaire "
"& Van Duyne, Albrecht & Creighton), turns the whisper into a shout: "
"molecules adsorbed on plasmonic nanostructures scatter millions of times "
"harder. The enhancement is electromagnetic: the hotspot field E boosts "
"both the incoming and the scattered light, so the Raman signal grows as "
"|E/E0|^4 - a 30x field gives 810,000x signal. At 100x fields the "
"enhancement passes 1e8, and single molecules become visible (Nie & Emory "
"1997, Kneipp 1997). Chemical enhancement (charge transfer between "
"molecule and metal) adds another 10-100x. Hotspots live in nanogaps - "
"dimer junctions, sharp tips, rough crevices - where coupled plasmons "
"focus light to cubic nanometres. The numbers humble: at 1 nanomolar in a "
"1-femtoliter hotspot volume there are 0.6 molecules on average - SERS "
"routinely sees fractions of a molecule's worth of signal."),
"how_it_works": (
"The molecule sits in the gap between two coupled plasmonic particles. "
"The incident laser drives the dimer plasmon; the gap field exceeds the "
"incident field by the enhancement factor; the molecule's induced Raman "
"dipole radiates at the shifted wavelength, and the same plasmon "
"resonance boosts the outgoing radiation - hence the fourth power, two "
"powers in and two out. Maximum enhancement needs the plasmon resonance "
"to straddle both the laser and the Raman-shifted wavelength (a few tens "
"of nanometres apart). Reproducibility was the field's long struggle: "
"random rough surfaces give random hotspots, so modern substrates use "
"lithographic dimers, nanostars, and shell-isolated particles (SHINERS) "
"with built-in intensity standards. Quantification uses the fingerprint "
"itself - peak ratios cancel the hotspot lottery - enabling trace "
"detection of explosives, biomarkers, and contaminants at attomolar "
"levels."),
"key_points": [
"SERS: plasmonic hotspots amplify Raman scattering by |E/E0|^4.",
"30x field -> 8.1e5 enhancement; 100x -> 1e8: single molecules visible.",
"Discovered 1974-77 on rough silver; explained by Moskovits 1985.",
"Hotspots live in nanogaps: dimers, tips, crevices - cubic-nanometre volumes.",
"1 nM in 1 fL = 0.6 molecules: SERS sees sub-molecule quantities."],
"requirements": [
"The fourth-power law and why it is two powers in, two out.",
"Hotspot geometry: coupled plasmons in nanogaps.",
"A calculator for the enhancement exercises in the demo."],
"standards": [
"Enhancement factors dimensionless; cross-sections in cm^2.",
"Concentrations in mol/L with volume context."],
"citations": [C_FLEISCHMANN, C_JEANMAIRE, C_MOSKOVITS, C_NIE, C_KNEIPP],
"sig_lens": (
"Signature take: Raman scattering is the molecule humming its name so "
"quietly no one hears - SERS builds the molecule a concert hall out of "
"two gold particles and a nanometre gap. The Signature builder loves this "
"inversion: the weakest signal in spectroscopy becomes the most sensitive, "
"not by shouting louder but by listening in a smaller room. A million "
"times louder, and the fingerprint never lies."),
},
{
"key": "solar_trapping",
"name": "Light Trapping in Solar Cells: More Sun Per Atom",
"group": "Sensing and Energy", "ladder_rank": 7, "ladder_tier": "advanced",
"description": (
"A thin solar cell is a race between absorption and material cost: silicon "
"absorbs weakly near its bandgap, so a 2-micron film at 1000 nm wavelength "
"(absorption coefficient 64/cm) drinks only 1.27% of the light in a single "
"pass - the rest escapes out the back. Light trapping folds the optical "
"path: texture the surfaces, and rays bounce at angles that trap them by "
"total internal reflection, multiplying the path length. Yablonovitch's "
"4n^2 limit sets the ergodic ceiling - for silicon (n=3.5) a 49x path "
"boost. That 2-micron film then absorbs 46.6% instead of 1.27%: a 37-fold "
"gain from geometry alone. Nanophotonics engineers the texture: plasmonic "
"nanoparticles scatter light sideways into guided modes (Atwater & Polman "
"2010), nanowire arrays act as antennas that concentrate absorption, "
"photonic-crystal backs reflect with angle-selective precision, and "
"Mie-resonant dielectric particles forward-scatter without metal loss. "
"The goal is the Shockley-Queisser limit with a tenth of the silicon: "
"cheap, thin, and optically thick."),
"how_it_works": (
"Single pass absorption is 1 - exp(-alpha x d): thin d or small alpha means "
"most photons leave. A Lambertian (randomizing) texture gives each photon "
"many passes; statistical optics shows the average path enhancement cannot "
"exceed 4n^2 for an ergodic, weakly-absorbing slab - the Yablonovitch "
"limit, derived from phase-space brightness conservation. Nanostructures "
"beat naive ray textures by coupling incident light directly into the "
"slab's guided modes: a plasmonic particle's scattered field has large "
"in-plane wavevectors that match guided modes, and a periodic back "
"reflector diffracts escaping light back at trapped angles. Nanowires go "
"further - each wire is a resonant absorber whose cross-section exceeds "
"its area, so sparse arrays drink like dense films. The accounting is "
"always absorption per atom of semiconductor: nanophotonics maximizes the "
"numerator while the denominator shrinks to foil thickness."),
"key_points": [
"2 um Si at 1000 nm: 1.27% single-pass -> 46.6% with 49x trapping (37x gain).",
"Yablonovitch limit: 4n^2 path enhancement (49x for silicon).",
"Textures trap by total internal reflection; nanostructures couple into guided modes.",
"Plasmonic scatterers, nanowire antennas, Mie particles: less metal loss, more forward scatter.",
"Goal: Shockley-Queisser efficiency with foil-thin silicon."],
"requirements": [
"Beer-Lambert absorption 1 - exp(-alpha x d).",
"The 4n^2 limit and what 'ergodic' assumes.",
"A calculator for the trapping exercises in the demo."],
"standards": [
"Absorption coefficients in /cm; thicknesses in microns.",
"Enhancement factors dimensionless."],
"citations": [C_ATWATER, C_POLMAN, C_YABLONOVITCH],
"sig_lens": (
"Signature take: the thin solar cell is a net with big holes - most fish "
"swim through. The Signature builder does not buy more net; he teaches "
"the fish to swim in circles. Forty-nine passes through the same two "
"microns of silicon: that is not a material improvement, it is a geometry "
"victory, and geometry is free after the first etch."),
},
{
"key": "nanolasers",
"name": "Nanolasers and Spasers: Lasers Smaller Than the Light They Make",
"group": "Materials and Metadevices", "ladder_rank": 8, "ladder_tier": "advanced",
"description": (
"A nanolaser breaks the oldest rule of lasers - that the cavity must be at "
"least half a wavelength long - by replacing the photon with a plasmon as "
"the oscillating particle. Bergman and Stockman's 2003 spaser proposal "
"(surface plasmon amplification by stimulated emission of radiation) and "
"Noginov's 2009 demonstration showed coherent plasmons generated in a "
"15 nm gold core wrapped in dye-doped silica: a laser whose mode volume "
"is (10 nm)^3 = 1e-24 m^3, eight thousand times below the diffraction-"
"limited (lambda/2n)^3 = 8e-21 m^3. Photonic nanolasers took the other "
"road: metallic-coated nanocavities (Hill 2007), metallo-dielectric "
"pillars (Nezhad 2010), and nanowires (Duan 2003, Oulton 2009, Ma 2011) "
"lase with mode volumes near the diffraction limit at room temperature. "
"The threshold tells the price: gain must beat loss, g_th = 2 x pi x n / "
"(lambda x Q) - at Q=100 and 600 nm that is 1571/cm of material gain, "
"enormous, which is why plasmonic lasers demand the brightest gain media "
"and why their beta-factors approach 1 (nearly every spontaneous photon "
"joins the mode: 'thresholdless' lasing). Small, fast, hungry: the "
"nanolaser trades efficiency for size and speed."),
"how_it_works": (
"Lasing needs round-trip gain >= loss. In a spaser the 'cavity' is a "
"plasmon resonance of a metal nanoparticle (Q ~ 10-100, terrible by laser "
"standards) and the gain is dye molecules or quantum dots in the "
"near field; stimulated emission of plasmons - not photons - builds the "
"coherent oscillation, which then radiates weakly as light. The Purcell "
"effect is the secret ally: the tiny V makes spontaneous emission into "
"the mode ultrafast, so the beta-factor nears unity and the laser turns "
"on without a visible threshold kink. Nanowire lasers use the wire itself "
"as both gain medium and Fabry-Perot cavity, with end-facet reflection "
"closing the loop; plasmonic nanowires (Oulton) hybridize the photonic "
"mode with plasmons to beat diffraction. Heat is the enemy - metal loss "
"becomes lattice heat - so continuous-wave room-temperature spasing "
"remains the prize; pulsed demonstrations dominate."),
"key_points": [
"Spaser (2003/2009): stimulated plasmons in a 15 nm core; V = 1e-24 m^3, 8000x below diffraction.",
"Photonic nanolasers: metallic nanocavities, metallo-dielectric pillars, nanowires - room-temp lasing.",
"Threshold gain g_th = 2pi x n/(lambda x Q): 1571/cm at Q=100, 600 nm - huge.",
"Beta -> 1: Purcell-funneled emission makes 'thresholdless' turn-on.",
"Trade: extreme size and speed for efficiency; heat is the enemy."],
"requirements": [
"Laser threshold: round-trip gain >= loss.",
"Beta-factor and what 'thresholdless' means.",
"A calculator for the threshold-gain exercises in the demo."],
"standards": [
"Mode volumes in m^3 and in (lambda/n)^3 units; gain in /cm.",
"Q dimensionless; wavelengths in nm."],
"citations": [C_BERGMAN, C_NOGINOV, C_OULTON, C_HILL, C_NEZHAD],
"sig_lens": (
"Signature take: the nanolaser is the laser with its resonator removed "
"and replaced by a storm of electrons - smaller than the light it makes, "
"which every textbook called impossible until the plasmons did it. The "
"Signature builder admires the spaser because it refuses the premise: "
"why store light in a box, when you can store it as sloshing charge? "
"The box was never the point. The oscillation was."),
},
{
"key": "negative_index",
"name": "Negative-Index Metamaterials: Bending Light Backwards",
"group": "Materials and Metadevices", "ladder_rank": 8, "ladder_tier": "advanced",
"description": (
"In 1968 Veselago asked what electrodynamics would do if a material had "
"negative permittivity AND negative permeability; in 2000-2001 Smith, "
"Schultz, Pendry and colleagues built one, and the answer was: light "
"bends backwards. With n = -sqrt(epsilon x mu), Snell's law refracts to "
"the SAME side of the normal - 30 degrees incidence from air onto n = -1 "
"emerges at -30 degrees - and the Poynting vector points opposite the "
"wavevector. Pendry's 2000 perfect-lens proposal showed a slab of n = -1 "
"not only focuses propagating waves but amplifies the evanescent near "
"field, in principle imaging with unlimited resolution. Real "
"implementations use split-ring resonators (magnetic response from "
"structured metal) paired with wire arrays (electric response): the "
"resonances, not the atoms, supply the negative parameters. At optical "
"frequencies magnetism from split rings fades, so fishnet and "
"metal-dielectric stacks take over. The field then pivoted: Zheludev's "
"metadevices, transformation optics (invisibility cloaks from coordinate "
"design), and the realization that loss is the tax on every negative-index "
"dream (Khurgin). Backwards light is real; the invoice is absorption."),
"how_it_works": (
"Natural magnetism dies above gigahertz, so metamaterials synthesize it: "
"a split-ring resonator is an LC circuit the light drives - circulating "
"currents give a magnetic dipole moment, and near its resonance the "
"effective mu swings negative. Continuous wires give a Drude-like negative "
"epsilon below their plasma frequency. Combine the unit cells on a "
"subwavelength lattice and the composite behaves as a homogeneous medium "
"with both parameters negative in the overlap band. The reversed Snell "
"law follows from phase matching with a negative index; the reversed "
"Doppler and Cherenkov effects follow from the antiparallel wavevector "
"and energy flow. The perfect lens works because the slab resonantly "
"amplifies each evanescent component en route - but the amplification is "
"a resonance phenomenon, so loss caps the resolution in practice, and "
"bandwidth stays narrow. Modern work chases low-loss routes: all-"
"dielectric Mie-resonant metamaterials (silicon spheres with overlapping "
"electric and magnetic dipole resonances) get negative effective "
"parameters with a fraction of the metal loss."),
"key_points": [
"n = -sqrt(eps x mu): both negative -> light refracts to the same side of the normal.",
"30 deg onto n=-1 emerges at -30 deg; energy flows opposite the wavevector.",
"Split rings synthesize mu<0; wire arrays give eps<0; overlap band is the medium.",
"Pendry perfect lens: evanescent amplification promises unlimited resolution; loss caps it.",
"All-dielectric Mie metamaterials now chase the effect with far less loss."],
"requirements": [
"Snell's law with a negative index and what changes sign.",
"LC-resonator picture of the split ring's magnetic response.",
"A calculator for the backwards-refraction exercises in the demo."],
"standards": [
"Effective epsilon, mu, n quoted at stated frequency; unit-cell size << lambda.",
"Figures of merit: FOM = |Re(n)/Im(n)|."],
"citations": [C_SMITH, C_PENDRY, C_ZHELUDEV, C_KHURGIN],
"sig_lens": (
"Signature take: the negative-index slab is a mirror held up to "
"electrodynamics - everything familiar, running in reverse. The Signature "
"builder keeps Veselago's question framed on his wall: 'what if the signs "
"were wrong?' Thirty years of 'impossible' became a slab that focuses "
"with no curvature. Never trust a sign convention; it might be hiding a "
"continent."),
},
{
"key": "silicon_photonics",
"name": "Nanoscale Silicon Photonics: Light on a Chip",
"group": "Materials and Metadevices", "ladder_rank": 8, "ladder_tier": "advanced",
"description": (
"Silicon photonics puts optical circuits on silicon chips using the same "
"CMOS fabs that make processors: 220-nm-thick silicon wires on oxide "
"guide 1550 nm light with 2 dB/cm loss, bend it on 5-micron radii, and "
"pack modulators, detectors, and multiplexers by the thousand. The "
"platform's workhorse is the microring resonator: a 10-micron-radius ring "
"(n_eff = 2.4, group index 4.2) has a free spectral range of 9.1 nm at "
"1550 nm, and with a 0.01 nm linewidth its Q is 155,000 - a wavelength "
"filter, modulator, and sensor in one circle. Silicon's indirect bandgap "
"forbids efficient light emission, so the field routed around it: Raman "
"lasers (Rong 2005), germanium photodetectors grown on silicon, and "
"hybrid III-V bonding for sources. Modulators exploit the plasma "
"dispersion effect (Xu 2005: micrometre-scale!) and now run at 50+ Gb/s "
"(Reed 2010). The prize is co-packaged optics: terabits of chip-to-chip "
"bandwidth at picojoules per bit (Miller 2009), with foundry PDKs "
"(Thomson 2016 roadmap) making photonic design as routine as electronic."),
"how_it_works": (
"High index contrast (3.48 vs 1.44) is the whole platform: it squeezes the "
"mode into the 220x500 nm wire, permits micron bends, and shrinks every "
"component. Rings couple evanescently to bus waveguides; on resonance, "
"light drops into the ring and either filters through or builds intensity "
"for modulation. Modulation injects or depletes carriers in a p-n junction "
"across the waveguide - the plasma dispersion effect shifts the index by "
"~1e-3, enough to swing a high-Q ring on and off resonance at tens of "
"gigahertz. Germanium, absorbing at 1550 nm, makes the detector: evanescent "
"or butt-coupled, it turns photons into photocurrent with >0.8 A/W "
"responsivity. Wavelength division multiplexing multiplies capacity: one "
"fiber, dozens of ring-defined colors. Thermal tuners (tiny heaters) trim "
"each ring to its grid wavelength, compensating fabrication variation - "
"the platform's open secret is that every ring ships with a heater."),
"key_points": [
"220 nm Si on oxide: 2 dB/cm, 5 um bends, CMOS-fab compatible.",
"10 um ring at 1550 nm: FSR 9.1 nm; 0.01 nm linewidth -> Q = 155,000.",
"Silicon can't emit (indirect gap): Raman lasers, Ge detectors, hybrid III-V sources.",
"Plasma-dispersion modulators: 50+ Gb/s from carrier injection/depletion.",
"Co-packaged optics: Tb/s at pJ/bit; foundry PDKs routinize design."],
"requirements": [
"Ring resonator FSR = lambda^2/(n_g x 2pi x R) and Q = lambda/Delta_lambda.",
"Plasma dispersion effect in words: carriers shift the index.",
"A calculator for the ring exercises in the demo."],
"standards": [
"Loss in dB/cm; radii in microns; Q dimensionless.",
"Modulator rates in Gb/s; energies in pJ/bit."],
"citations": [C_SORE, C_JALALI, C_REED, C_XU, C_RONG, C_MILLER],
"sig_lens": (
"Signature take: silicon photonics is the railroad built with the same "
"tools as the telegraph - the CMOS fab, repurposed for light. The "
"Signature builder admires pragmatism over purity: silicon cannot lase, "
"so the field bonded on lasers, grew germanium, and kept shipping. A "
"thousand rings on a chip, each with its heater, each on its wavelength - "
"that is not a physics demonstration. That is infrastructure."),
},
{
"key": "graphene",
"name": "2D-Material Photonics: Graphene's Tunable Plasmons",
"group": "Materials and Metadevices", "ladder_rank": 8, "ladder_tier": "advanced",
"description": (
"Graphene - one atomic layer of carbon - is a photonic material with a "
"volume knob: gate voltage moves its Fermi level, and its optical response "
"follows. A single layer absorbs exactly pi x alpha = 2.3% of incident "
"light (Nair 2008), a number written in the fine-structure constant, and "
"its plasmons compress infrared light spectacularly: at 10-micron "
"wavelength with E_F = 0.5 eV, the graphene plasmon wavelength is ~187 nm "
"- 53 times shorter than the free-space wave (compression factor "
"(2 x alpha/pi) x (E_F/hbar x omega)). Turn the gate from 0.2 to 0.8 eV "
"and the plasmon stretches from 75 to 300 nm: the whole infrared rewritten "
"by a volt. Nano-imaging (Fei 2012, Chen 2012) photographed these "
"plasmons directly. The family extends: hexagonal boron nitride hosts "
"ultra-low-loss phonon polaritons (Caldwell 2014), alpha-MoO3 carries them "
"in-plane anisotropically, and monolayer transition-metal dichalcogenides "
"(MoS2, WSe2) bring direct-gap excitons that lase in nanocavities (Wu "
"2015) and couple strongly to light (Liu 2015). Flatland photonics: all "
"the physics, one atom thick."),
"how_it_works": (
"Graphene's electrons are massless Dirac fermions with a conical band "
"structure; gating fills the cone to E_F, and intraband transitions give "
"a Drude-like conductivity tunable by that filling. The plasmon "
"dispersion goes as omega ~ sqrt(q x E_F): higher Fermi level, stiffer "
"plasmon, and the extreme confinement (lambda_p << lambda_0) comes from "
"the 2D sheet's weak screening. Losses are set by scattering - mobility "
"is destiny, so encapsulated high-mobility samples win. hBN's phonon "
"polaritons exploit its hyperbolic bands (permittivity of opposite signs "
"in different directions), guiding rays inside the slab with almost no "
"loss. TMDC monolayers add tightly bound excitons (hundreds of meV "
"binding): strong oscillators that reach the strong-coupling regime with "
"cavities at room temperature and emit valley-polarized light. Stack the "
"layers into van der Waals heterostructures and each atomic sheet "
"contributes its polariton - designer dispersion, assembled like Lego."),
"key_points": [
"Graphene absorbs pi x alpha = 2.3%: a universal number from the fine-structure constant.",
"Plasmon compression 53x at 10 um (E_F=0.5 eV); gate tunes 75 -> 300 nm.",
"omega ~ sqrt(q x E_F): gating rewrites the infrared by a volt.",
"hBN: hyperbolic phonon polaritons, ultra-low loss; MoO3: in-plane anisotropy.",
"TMDC monolayers: direct-gap excitons, nanolasers, room-temp strong coupling."],
"requirements": [
"Dirac cone and Fermi-level gating in words.",
"Plasmon compression factor and its ingredients.",
"A calculator for the compression exercises in the demo."],
"standards": [
"Fermi levels in eV; plasmon wavelengths in nm; compression dimensionless.",
"Mobilities in cm^2/Vs where quoted."],
"citations": [C_BONACCORSO, C_NAIR, C_JABLAN, C_FEI, C_KOPPENS, C_BASOV, C_WU],
"sig_lens": (
"Signature take: graphene is the material with a dimmer switch - one atom "
"thick, yet its plasmons answer to a gate voltage like a well-trained "
"instrument. The Signature builder finds this morally correct: the "
"photonic response should be adjustable, not ordained. Fifty-three times "
"compression, tunable with a volt - the infrared, finally, with a volume "
"knob."),
},
{
"key": "slow_light",
"name": "Slow Light: Braking a Photon",
"group": "Materials and Metadevices", "ladder_rank": 8, "ladder_tier": "advanced",
"description": (
"Light's group velocity - the speed of its pulse envelope - can be "
"dragged far below c: Hau's 1999 Bose-Einstein condensate slowed light to "
"17 metres per second, seven orders down, using electromagnetically "
"induced transparency. Nanophotonics does it on chips: photonic-crystal "
"waveguides flatten their bands near the gap edge (Notomi 2001, Krauss, "
"Baba), reaching group indices n_g = 20-100 - light crawling at c/20 - "
"and coupled-resonator waveguides (Yariv 1999) hop photons ring to ring "
"at whatever pace the coupling sets. A 1-mm photonic-crystal guide with "
"n_g = 20 delays a pulse by 66.7 picoseconds - longer than a 10 ps pulse "
"itself, real optical buffering. The price is the delay-bandwidth "
"product: slow light compresses the pulse spatially (great for enhancing "
"nonlinearity and absorption per unit length) but narrows the usable "
"bandwidth and magnifies disorder scattering - fabrication roughness "
"backscatters slow modes fiercely. Stopped light (stored as atomic "
"coherence, then released) became quantum memory. Slow light is time, "
"traded for space."),
"how_it_works": (
"Group velocity is v_g = d(omega)/d(k): where the dispersion band goes "
"flat, pulses crawl. Near a photonic band edge the band must turn around "
"(zero slope at the zone boundary), so engineering the edge engineers the "
"slowness - line-defect waveguides pull a guided band into the gap with a "
"tunable flat region. The spatial compression is automatic: a 10 ps pulse "
"at n_g = 20 occupies 150 microns instead of 3 mm, so its energy density "
"rises 20x and every intensity-dependent effect (nonlinearity, absorption, "
"emission) strengthens per unit length. EIT does it differently: a control "
"laser opens a narrow transparency window with ferocious dispersion "
"(dn/d(omega) huge), and the pulse's information is temporarily written "
"into atomic spin coherence - true storage, milliseconds long. The chip-"
"scale version accepts smaller factors for robustness: n_g ~ 20-40 with "
"engineered flat bands (Vlasov 2005 showed active control), enough for "
"compact delay lines and enhanced modulators."),
"key_points": [
"Group velocity v_g = d(omega)/dk: flat bands mean slow pulses.",
"Hau 1999: 17 m/s in a BEC; photonic-crystal guides: n_g = 20-100 on chip.",
"1 mm at n_g=20: 66.7 ps delay - buffering a 10 ps pulse.",
"Spatial compression 20x boosts nonlinearity and absorption per length.",
"Price: delay-bandwidth product, disorder backscattering; EIT gives true storage."],
"requirements": [
"Group vs phase velocity and the band-flattening idea.",
"Delay-bandwidth product as the conservation law.",
"A calculator for the delay exercises in the demo."],
"standards": [
"Group index n_g dimensionless; delays in ps/ns; lengths in mm/um."],
"citations": [C_HAU, C_FLEISCHHAUER, C_NOTOMI, C_BABA, C_YARIV, C_VLASOV2],
"sig_lens": (
"Signature take: slow light is the Signature builder's time machine in "
"reverse - he cannot speed the photon, so he shortens its road until a "
"millimetre holds 66 picoseconds. The pulse arrives later, denser, more "
"potent: time traded for space, then spent on nonlinearity. To brake "
"light with nothing but a pattern of holes is to conduct traffic with "
"architecture."),
},
{
"key": "nonlinear",
"name": "Nonlinear Nanophotonics: When Light Changes the Rules",
"group": "Frontiers", "ladder_rank": 9, "ladder_tier": "advanced",
"description": (
"Ordinary optics is linear: double the light, double the response. "
"Nonlinear optics begins when the light is intense enough to change the "
"material's own properties - the polarization gains terms in E^2, E^3, "
"and up. Second-harmonic generation (Franken 1961: 694 nm in, 347 nm out "
"of quartz) converts two photons into one of doubled energy, with "
"efficiency scaling as the pump intensity squared: 4x the pump gives 16x "
"the harmonic. The catch is phase matching: the fundamental and harmonic "
"must stay in step, or they drift out of phase after one coherence length "
"L_c = pi/Delta_k - just 25 microns for Delta_n = 0.01 at 1 micron "
"wavelength. Nanophotonics attacks both problems: resonant cavities and "
"plasmonic hotspots raise the local intensity by orders of magnitude, and "
"subwavelength structures engineer the phase - metasurfaces impart abrupt "
"phase jumps that replace bulk phase matching (Kauranen & Zayats 2012), "
"and periodic poling flips the crystal domains every coherence length. "
"The Kerr effect (n = n0 + n2 x I) makes the index itself intensity-"
"dependent: at 1 GW/cm^2 in silica fiber, one metre adds 1.22 radians of "
"nonlinear phase - the basis of all-optical switching, supercontinuum, "
"and soliton physics, now shrunk onto chips."),
"how_it_works": (
"The anharmonic electron motion at high fields radiates at new "
"frequencies: chi2 materials (no inversion symmetry - lithium niobate, "
"GaAs) generate sum and difference frequencies; chi3 materials (everything, "
"including glass) give third harmonic, Kerr shift, and four-wave mixing. "
"Nanostructures boost the interaction two ways: field concentration "
"(plasmonic gaps, Mie resonances, high-Q cavities raise I by 10^2-10^6) "
"and mode engineering (dispersion-designed waveguides keep waves in step "
"over centimetres). Quasi-phase-matching in periodically poled lithium "
"niobate flips the sign of chi2 every coherence length so the harmonic "
"keeps growing instead of oscillating. Metasurface nonlinear optics goes "
"further: each nano-antenna is a phase-controlled harmonic source, and "
"the array's phase gradient steers the generated beam independently of "
"the pump - nonlinear beam shaping from a flat sheet. The frontier is "
"single-photon nonlinearity: one photon shifting a cavity enough to block "
"the next, the optical transistor."),
"key_points": [
"Nonlinear: response grows as E^2, E^3 - new frequencies from intense light.",
"SHG scales as pump^2: 4x pump -> 16x harmonic (Franken 1961).",
"Phase matching: L_c = 25 um at Delta_n=0.01, 1 um; poling and metasurfaces fix it.",
"Kerr: n2 x I; 1 GW/cm^2 in silica -> 1.22 rad per metre of nonlinear phase.",
"Nanophotonics boosts I 10^2-10^6x and engineers phase at the nanoscale."],
"requirements": [
"chi2 vs chi3 and which materials have which.",
"Phase matching and coherence length.",
"A calculator for the scaling exercises in the demo."],
"standards": [
"Intensities in W/cm^2 or W/m^2; n2 in m^2/W; lengths in um/mm."],
"citations": [C_BOYD, C_FRANKEN, C_KAURANEN],
"sig_lens": (
"Signature take: linear optics is polite conversation; nonlinear optics "
"is the moment the room starts answering back. The Signature builder "
"drives the field until the material's own rules bend - then the light "
"writes new colors that were never sent in. Four times the pump, sixteen "
"times the harmonic: that is not amplification, it is the universe "
"negotiating."),
},
{
"key": "topological",
"name": "Topological Photonics: Light That Refuses to Scatter",
"group": "Frontiers", "ladder_rank": 9, "ladder_tier": "advanced",
"description": (
"Topological photonics gives light a kind of armor: edge states that flow "
"around defects and corners without backscattering, protected by the "
"bulk's topology rather than by careful fabrication. The prototype is the "
"Su-Schrieffer-Heeger chain - dimers with alternating couplings t1, t2. "
"Its bands are E(k) = +-sqrt(t1^2 + t2^2 + 2 x t1 x t2 x cos k): with t1 = "
"1, t2 = 2 the gap is 2|t1-t2| = 2, bands spanning +-1 to +-3, and the gap "
"closes exactly at t1 = t2 - the topological transition. Join a chain "
"with t1 < t2 to one with t1 > t2 and a mid-gap state appears at the "
"interface, pinned to zero energy, exponentially localized: it cannot be "
"removed without closing the bulk gap. Photonics copied the playbook "
"(Lu 2014, Khanikaev & Shvets 2017): coupled-resonator lattices with "
"engineered phases mimic magnetic fields for light, and helical waveguide "
"arrays showed light rounding sharp corners with no reflection. The payoff "
"is disorder-immune transport - waveguides that work despite fabrication "
"slop - and topological lasers that lase in a single protected mode."),
"how_it_works": (
"Topology classifies band structures by integers (winding numbers, Chern "
"numbers) that cannot change without closing the gap - like the number of "
"holes in a donut cannot change without tearing. The SSH chain's winding "
"counts how many times the (t1 + t2 x cos k, t2 x sin k) vector circles "
"the origin: 0 for t1 > t2 (trivial), 1 for t1 < t2 (topological). The "
"bulk-boundary correspondence guarantees an edge state wherever the "
"integer jumps - at the chain's end or at a domain wall. Photonic versions "
"replace the electron hopping with evanescent coupling between resonators "
"or waveguides, and break time-reversal symmetry with magneto-optical "
"materials or with dynamic modulation/floquet driving (since photons "
"ignore real magnetic fields). The edge mode's unidirectionality forbids "
"backscattering: a defect has no backward state to scatter into, so the "
"light flows around it. That is the armor - not perfection of the road, "
"but absence of anywhere to fall off."),
"key_points": [
"SSH chain: E(k)=+-sqrt(t1^2+t2^2+2t1t2cosk); t1=1,t2=2 -> gap 2, bands +-1..+-3.",
"Gap closes at t1=t2: the topological transition point.",
"Domain wall between the two phases hosts a protected mid-gap state.",
"Integer invariants (winding/Chern) can't change without closing the gap.",
"Photonic copies: disorder-immune transport, topological lasers, no backscattering."],
"requirements": [
"Bands, gaps, and the idea of a topological invariant in words.",
"Bulk-boundary correspondence: interface states where the invariant jumps.",
"A calculator for the SSH band exercises in the demo."],
"standards": [
"Couplings in energy units; bands as E(k); invariants dimensionless integers."],
"citations": [C_LU, C_KHANIKAEv, C_SSH],
"sig_lens": (
"Signature take: topological protection is the Signature builder's "
"favorite kind of guarantee - not 'I built it perfectly' but 'it cannot "
"break.' The edge state rounds the corner because the universe has "
"nowhere else to put it; the defect is irrelevant, the disorder is "
"irrelevant. Build the invariant, and the light defends itself."),
},
{
"key": "quantum_integrated",
"name": "Integrated Quantum Nanophotonics: Circuits of Entanglement",
"group": "Frontiers", "ladder_rank": 9, "ladder_tier": "advanced",
"description": (
"Integrated quantum nanophotonics moves quantum optics off the optical "
"table and onto chips: sources, circuits, and detectors in waveguides, "
"stable to nanometres and scalable to thousands of components. The "
"foundations were laid with silica-on-silicon waveguide quantum circuits "
"(Politi 2008), universal linear optics (Carolan 2015: any unitary on N "
"modes from meshes of beamsplitters and phase shifters), and the Knill-"
"Laflamme-Milburn scheme (2001) proving linear optics plus measurement "
"can compute. The workhorse interference is Hong-Ou-Mandel: two identical "
"photons entering a 50:50 beamsplitter always exit together, so "
"coincidences dip to near zero at zero delay - with 95% visibility the "
"coincidence rate falls to 5% of its baseline, the signature of "
"indistinguishability. On chip, a Mach-Zehnder interferometer is two "
"directional couplers and a phase shifter: transmission T = cos^2(Delta_"
"phi/2), reprogrammable at kilohertz. Wang's 2020 review charts the "
"trajectory: boson sampling, quantum walks, and variational circuits now "
"run on programmable nanophotonic processors (Harris 2017, Shen 2017) - "
"the same hardware that accelerates neural networks, because linear "
"optics is linear algebra at light speed."),
"how_it_works": (
"Qubits are encoded in photon paths (dual-rail), polarization, or time "
"bins; single-qubit gates are phase shifters and beamsplitters - both "
"trivial in waveguides - and the hard two-qubit gate is done by "
"measurement-induced nonlinearity (KLM) or by deterministic emitters "
"(quantum dots). Integration wins on stability: a centimetre-scale chip "
"holds phase to milliradians where a tabletop interferometer drifts, and "
"lithography replicates components identically. Sources improved in "
"parallel: multiplexed heralded pair sources and on-demand dots feed the "
"circuits; superconducting nanowire detectors (95%+ efficiency) count the "
"photons at the outputs. Programmable meshes (triangular or rectangular "
"arrangements of Mach-Zehnder interferometers) implement any linear "
"transformation by dialing phases - one chip, many circuits, reconfigured "
"in software. Loss remains the tax: every dB halves the multi-photon "
"rate, so ultra-low-loss platforms (silicon nitride, thin-film lithium "
"niobate) lead."),
"key_points": [
"Quantum optics on chips: sources, circuits, detectors in waveguides.",
"HOM dip at 95% visibility: coincidences fall to 5% - identical photons bunch.",
"Mach-Zehnder: T = cos^2(Dphi/2); meshes of them make any linear unitary.",
"KLM 2001: linear optics + measurement computes; Politi 2008 put it in silica.",
"Integration = phase stability + replication; loss is the tax (every dB halves rates)."],
"requirements": [
"Beamsplitter + phase shifter as the universal gate set.",
"Hong-Ou-Mandel interference in words.",
"A calculator for the dip and MZI exercises in the demo."],
"standards": [
"Visibilities as fractions; phases in radians; loss in dB."],
"citations": [C_KNILL, C_KOK, C_POLITI, C_CAROLAN, C_HOM, C_WANG],
"sig_lens": (
"Signature take: the integrated quantum chip is the optical table folded "
"into a fingernail - every mirror a waveguide, every knob a voltage. The "
"Signature builder prefers it because tables drift and chips do not: "
"phase is a promise, and lithography keeps promises. When two photons "
"bunch at the beamsplitter, 95% silent at zero delay, the chip has proven "
"it can be trusted with entanglement."),
},
{
"key": "thermal_emission",
"name": "Controlling Thermal Light: Emitting Only What You Want",
"group": "Frontiers", "ladder_rank": 9, "ladder_tier": "advanced",
"description": (
"Hot objects glow - Planck's law, the blackbody spectrum, peaked at "
"Wien's lambda_max = 2898 um K / T (500 nm for the 5800 K sun, 2.9 um for "
"a 1000 K furnace). Nanophotonics edits that glow: structure the emitter "
"on the wavelength scale and Kirchhoff's law (emissivity = absorptivity, "
"per wavelength, angle, and polarization) becomes a design tool. A "
"photonic-crystal emitter (Lin 2003) suppresses long-wavelength emission "
"and concentrates radiation where a photovoltaic cell can use it; at "
"1500 K, a selective emitter radiating only in the 1-2 um band puts 25.9% "
"of the blackbody power exactly where it counts instead of wasting it as "
"useless long-wave heat. Greffet's 2002 silicon carbide grating went "
"further: thermal emission that is spatially coherent - a hot surface "
"radiating like a laser beam, because surface phonon polaritons give the "
"thermal field a well-defined wavevector. Applications: thermophotovoltaics "
"(heat -> tailored light -> electricity), radiative cooling (surfaces that "
"dump heat to the 3 K sky through the atmospheric window), incandescent "
"sources that beat the filament, and infrared camouflage. Fire, edited."),
"how_it_works": (
"Emissivity equals absorptivity, so designing absorption designs "
"emission: a resonant absorber at the target wavelength becomes a bright, "
"narrowband thermal emitter there, and a reflector everywhere else stays "
"dark. Photonic crystals open bandgaps that forbid emission at long "
"wavelengths while defect modes emit brightly in-band - the emitter "
"glows only in useful colors. Gratings couple surface polaritons to the "
"far field at specific angles, making the emission directional and "
"coherent: the thermal near field already has the polariton's coherence, "
"the grating just lets it out. Refractory metals (tungsten) and ceramics "
"survive the 1500-2000 K operating points; 2D materials and phase-change "
"alloys add tunability. The thermodynamic limit is respected - no "
"perpetual motion, just spectral and angular concentration - but the "
"practical gains are large: thermophotovoltaic systems target 40%+ heat-"
"to-electricity by feeding the cell only above-bandgap photons."),
"key_points": [
"Wien: 2898 um K/T; sun 500 nm, 1000 K furnace 2.9 um.",
"Kirchhoff: emissivity = absorptivity - design absorption, get emission.",
"1500 K selective emitter: 25.9% of blackbody power in the 1-2 um band.",
"Greffet 2002: grating-coupled polaritons make thermal emission laser-like.",
"Uses: thermophotovoltaics, radiative cooling, IR camouflage, bright filaments."],
"requirements": [
"Planck's law shape and Wien's displacement law.",
"Kirchhoff's law per wavelength/angle/polarization.",
"A calculator for the band-fraction exercises in the demo."],
"standards": [
"Temperatures in K; bands in um; emissivities dimensionless 0-1."],
"citations": [C_LIN, C_GREFFET, C_FAN],
"sig_lens": (
"Signature take: thermal light is the most democratic light - everything "
"hot glows, most of it wasted. The Signature builder is not democratic "
"about photons: he builds the emitter a photonic crystal corset so it "
"glows only where the cell can eat. Twenty-six percent in the useful "
"band instead of single digits - fire, taxed at the source, spending only "
"on what matters."),
},
{
"key": "inverse_design",
"name": "Inverse Design: Teaching Computers to Sculpt Light",
"group": "Frontiers", "ladder_rank": 10, "ladder_tier": "advanced",
"description": (
"Forward design picks a shape and computes what it does; inverse design "
"states what the light must do and lets the computer find the shape. The "
"engine is gradient-based optimization: simulate (Maxwell solver), compute "
"how the figure of merit changes with each design pixel (adjoint method "
"gives all gradients in one extra simulation), and climb. A textbook "
"microcosm: a binary amplitude grating's first-order efficiency is eta_1 = "
"(sin(pi x DC)/pi)^2 for duty cycle DC - start gradient ascent at DC = 0.2 "
"and finite-difference steps converge to DC = 0.5 with eta_1 = 10.13%, the "
"analytic optimum. Real inverse design (Molesky 2018 review) optimizes "
"thousands of pixels: wavelength demultiplexers that look like frozen "
"static but split colors perfectly, metasurface lenses co-designed with "
"the image sensor, and photonic-crystal cavities with Q in the millions "
"found by algorithms, not intuition. Topology optimization removes the "
"human's shape library entirely - every pixel of permittivity is free - "
"and discovers structures no one would draw: bends, splitters, and mode "
"converters smaller than anything hand-designed. The designer writes the "
"goal; Maxwell writes the shape."),
"how_it_works": (
"Discretize the design region into pixels, each holding a permittivity "
"value between the material bounds. One forward simulation gives the "
"fields and the figure of merit (transmission into a mode, focusing "
"efficiency, Q). The adjoint trick: run one more simulation with sources "
"derived from the merit's derivative, and the overlap of the two field "
"sets gives the gradient with respect to every pixel at once - thousands "
"of derivatives for the price of two simulations. Project onto "
"fabricable shapes (minimum feature size, binarization) and iterate: "
"gradient ascent/descent climbs to a local optimum, and good "
"parameterizations plus multi-start avoid bad ones. The results are "
"alien-looking but fabricable: a 1x2 splitter the size of a wavelength, "
"a three-channel demultiplexer in a few square microns. Machine learning "
"now accelerates it further - neural surrogates replace the solver in "
"the loop - but the adjoint gradient remains the workhorse. The human "
"contribution moved up one level: choosing the merit function is the "
"design."),
"key_points": [
"Inverse design: specify the light's goal, optimize the shape to meet it.",
"Adjoint method: all pixel gradients from one extra simulation.",
"Grating microcosm: gradient ascent from DC=0.2 converges to 0.5, eta_1=10.13%.",
"Topology optimization frees every permittivity pixel; discovers alien, fabricable shapes.",
"Designer writes the merit function; Maxwell writes the geometry."],
"requirements": [
"Gradient ascent/descent and finite differences in words.",
"The adjoint idea: two simulations, all gradients.",
"A calculator for the grating-optimization exercises in the demo."],
"standards": [
"Efficiencies as fractions; duty cycles 0-1; feature sizes in nm."],
"citations": [C_MOLESKY, C_NOVOTNY],
"sig_lens": (
"Signature take: inverse design is the Signature builder hiring Maxwell "
"as his draftsman - he states what the light must do, and the equations "
"draw the shape. The results look like nothing a human would sketch, "
"which is exactly the point: human intuition is a small room, and the "
"optimizer searches the whole building. Specify the destination honestly; "
"let the physics choose the road."),
},
{
"key": "non_hermitian",
"name": "Non-Hermitian Nanophotonics: Gain, Loss, and Exceptional Points",
"group": "Frontiers", "ladder_rank": 10, "ladder_tier": "advanced",
"description": (
"Textbook quantum mechanics demands Hermitian matrices (real energies, "
"conserved probability); nanophotonics cheerfully violates it, because "
"photonic structures have gain and loss. The 2x2 parity-time (PT) symmetric "
"dimer H = [[i x gamma, kappa],[kappa, -i x gamma]] - gain on one site, "
"equal loss on the other, coupled by kappa - has eigenvalues "
"+-sqrt(kappa^2 - gamma^2). With kappa = 1: at gamma = 0.5 the eigenvalues "
"are +-0.866, real (PT-unbroken: the modes share gain and loss equally); "
"at gamma = 1 they coalesce to 0 - the exceptional point, where not just "
"the eigenvalues but the eigenvectors merge; at gamma = 1.5 they become "
"+-1.118i, one mode growing, one decaying (PT-broken). Bender and "
"Boettcher's 1998 discovery (real spectra from PT-symmetric non-Hermitian "
"Hamiltonians) became an experimental photonics program (El-Ganainy 2018, "
"Ozdemir 2019): exceptional points give sensors whose frequency splitting "
"grows as the square root of the perturbation (beating linear sensors for "
"tiny signals), single-mode lasers (the broken phase selects one mode), "
"and unidirectional invisibility. Nanophotonics supplies the platform: "
"coupled microrings, plasmonic dimers, and metasurfaces with patterned "
"gain and loss, engineered to sit exactly at the coalescence."),
"how_it_works": (
"PT symmetry means the structure looks the same after mirroring space and "
"reversing time (gain <-> loss): the Hamiltonian commutes with the joint "
"operation even though it is not Hermitian. Below the exceptional point "
"the eigenmodes respect the symmetry and the spectrum stays real - loss "
"and gain balance inside each mode. At the EP the two eigenvectors become "
"parallel (a defective matrix, a Jordan block): the system loses a "
"dimension, and perturbations split the eigenvalues as sqrt(epsilon) "
"rather than epsilon - the enhanced-sensing trick. Above the EP the modes "
"localize: one lives mostly on the gain site and grows, one on the loss "
"site and decays. Experiments implement it with coupled waveguides or "
"rings where one has optical pumping (gain) and the other has metal "
"(loss)), tuning the coupling to hit the EP. The square-root response "
"cuts both ways - it amplifies signal and noise alike - so the metrology "
"debate continues; the mode-selection and chiral-transport applications "
"are already devices."),
"key_points": [
"Non-Hermitian: gain and loss make photonic Hamiltonians non-Hermitian.",
"PT dimer eigenvalues +-sqrt(k^2-g^2): real at g=0.5, coalesce at g=1 (EP), +-1.118i at g=1.5.",
"Exceptional point: eigenvalues AND eigenvectors merge - a defective matrix.",
"EP sensors: splitting ~ sqrt(perturbation), beating linear scaling for tiny signals.",
"Platforms: coupled rings/waveguides with patterned gain and loss."],
"requirements": [
"Eigenvalues of a 2x2 matrix and what coalescence means.",
"PT symmetry: mirror space, reverse time, swap gain and loss.",
"A calculator for the EP exercises in the demo."],
"standards": [
"Gain/loss rates and couplings in the same frequency units; EP dimensionless ratio."],
"citations": [C_BENDER, C_ELGANAINY, C_OZDEMIR],
"sig_lens": (
"Signature take: the exceptional point is where two become one - not "
"merely equal, but the same, the matrix itself losing a dimension. The "
"Signature builder tunes his dimer to that knife's edge deliberately: "
"gain on the left, loss on the right, coupled just so, until the system "
"forgets it was ever two. At the coalescence, the smallest touch splits "
"the world as a square root - sensitivity bought with symmetry, priced "
"in fragility."),
},
]
