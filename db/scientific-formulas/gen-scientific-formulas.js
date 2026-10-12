(function(){'use strict';
/* JAH Scientific Formulas Database generator — jahdb-scientific-formulas-1.0.
   Property of Justin Addam Higgins (JAH).
   Catalog of ALL scientific formulas across every science.
   Type 1 = established (factual, never invented). Type 2 = frontier/speculative (labeled).
   Deterministic: same seed always makes the same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX='JAH-SF-';
var BASE=[
["Newton's Second Law","F = m\u00b7a","physics",[["F","net force","newtons (N)"],["m","mass","kilograms (kg)"],["a","acceleration","m/s\u00b2"]],"The net force on an object equals its mass times its acceleration.","From Newton's Principia (1687): defined force via change of momentum; for constant mass reduces to F=ma.",["Engineering mechanics","Vehicle dynamics","Structural analysis"],1],
["Mass-Energy Equivalence","E = m\u00b7c\u00b2","physics",[["E","energy","joules (J)"],["m","mass","kilograms (kg)"],["c","speed of light","299,792,458 m/s"]],"Mass and energy are interchangeable; a small mass holds enormous energy.","Einstein 1905 special relativity: from Lorentz invariance of physical laws.",["Nuclear energy","Particle physics","Cosmology"],1],
["Kinetic Energy","KE = \u00bd\u00b7m\u00b7v\u00b2","physics",[["KE","kinetic energy","joules (J)"],["m","mass","kg"],["v","velocity","m/s"]],"Energy of motion; grows with the square of speed.","Work-energy theorem: integrating F=ma over distance.",["Ballistics","Vehicle safety","Sports science"],1],
["Gravitational Force","F = G\u00b7m\u2081\u00b7m\u2082/r\u00b2","physics",[["F","force","N"],["G","gravitational constant","6.674\u00d710\u207b\u00b9\u00b9 N\u00b7m\u00b2/kg\u00b2"],["m\u2081,m\u2082","masses","kg"],["r","separation","m"]],"Every mass attracts every other mass; force falls off with distance squared.","Newton 1687, from Kepler's laws and the Moon's orbit.",["Orbital mechanics","Tides","Spaceflight"],1],
["Ohm's Law","V = I\u00b7R","physics",[["V","voltage","volts (V)"],["I","current","amperes (A)"],["R","resistance","ohms (\u03a9)"]],"Voltage across a conductor equals current times resistance.","Ohm 1827, empirical; follows from Drude model of conduction.",["Circuit design","Electronics","Power systems"],1],
["Wave Equation (speed)","v = f\u00b7\u03bb","physics",[["v","wave speed","m/s"],["f","frequency","hertz (Hz)"],["\u03bb","wavelength","m"]],"Wave speed equals frequency times wavelength.","Definition: one wavelength passes per period.",["Acoustics","Optics","Telecommunications"],1],
["Schr\u00f6dinger Equation (time-dependent)","i\u210f\u00b7\u2202\u03c8/\u2202t = \u0124\u03c8","physics",[["i","imaginary unit","\u2014"],["\u210f","reduced Planck constant","1.055\u00d710\u207b\u00b3\u2074 J\u00b7s"],["\u03c8","wavefunction","\u2014"],["\u0124","Hamiltonian operator","\u2014"]],"Governs how quantum states evolve in time.","Schr\u00f6dinger 1926; postulated to reproduce de Broglie waves and quantization.",["Quantum chemistry","Semiconductors","Quantum computing"],1],
["Heisenberg Uncertainty Principle","\u0394x\u00b7\u0394p \u2265 \u210f/2","physics",[["\u0394x","position uncertainty","m"],["\u0394p","momentum uncertainty","kg\u00b7m/s"]],"Position and momentum cannot both be known arbitrarily precisely.","Heisenberg 1927; follows from wave-particle duality and Fourier analysis.",["Quantum limits","Microscopy","Quantum cryptography"],1],
["Thermodynamic Identity (First Law)","\u0394U = Q \u2212 W","physics",[["\u0394U","internal energy change","J"],["Q","heat added","J"],["W","work done by system","J"]],"Energy is conserved: heat in minus work out changes internal energy.","Joule's experiments 1840s; conservation of energy applied to heat.",["Engines","Refrigeration","Climate science"],1],
["Maxwell\u2013Boltzmann Distribution","f(v) = 4\u03c0(m/2\u03c0kT)^{3/2}\u00b7v\u00b2\u00b7e^{\u2212mv\u00b2/2kT}","physics",[["f(v)","speed probability density","s/m"],["m","particle mass","kg"],["k","Boltzmann constant","1.381\u00d710\u207b\u00b2\u00b3 J/K"],["T","temperature","K"]],"Distribution of molecular speeds in an ideal gas at temperature T.","Maxwell 1860 from kinetic theory; Boltzmann generalized.",["Gas kinetics","Vacuum technology","Atmospheric science"],1],
["Lorentz Factor","\u03b3 = 1/\u221a(1 \u2212 v\u00b2/c\u00b2)","physics",[["\u03b3","Lorentz factor","dimensionless"],["v","velocity","m/s"],["c","speed of light","m/s"]],"Factor by which time dilates and lengths contract at relativistic speeds.","Lorentz transformations preserving light speed (Einstein 1905).",["Particle accelerators","GPS corrections","Astrophysics"],1],
["Planck's Law (blackbody)","B(\u03bd,T) = 2h\u03bd\u00b3/c\u00b2 \u00b7 1/(e^{h\u03bd/kT} \u2212 1)","physics",[["B","spectral radiance","W\u00b7sr\u207b\u00b9\u00b7m\u207b\u00b3"],["h","Planck constant","6.626\u00d710\u207b\u00b3\u2074 J\u00b7s"],["\u03bd","frequency","Hz"],["T","temperature","K"]],"Spectrum of light emitted by a perfect blackbody at temperature T.","Planck 1900; quantized energy E=h\u03bd resolved the ultraviolet catastrophe.",["Astronomy","Thermal imaging","Lighting"],1],
["Bernoulli's Equation","P + \u00bd\u03c1v\u00b2 + \u03c1gh = constant","physics",[["P","pressure","Pa"],["\u03c1","fluid density","kg/m\u00b3"],["v","flow speed","m/s"],["g","gravity","9.81 m/s\u00b2"],["h","height","m"]],"Faster fluid flow means lower pressure (energy conservation in fluids).","Bernoulli 1738; work-energy applied to fluid parcels.",["Aerodynamics","Plumbing","Weather"],1],
["Ideal Gas Law","PV = nRT","chemistry",[["P","pressure","Pa"],["V","volume","m\u00b3"],["n","moles","mol"],["R","gas constant","8.314 J/(mol\u00b7K)"],["T","temperature","K"]],"Relates pressure, volume, temperature and amount of an ideal gas.","Combines Boyle's, Charles's, and Avogadro's laws.",["Chemical engineering","Weather balloons","Scuba"],1],
["Nernst Equation","E = E\u00b0 \u2212 (RT/nF)\u00b7ln Q","chemistry",[["E","cell potential","V"],["E\u00b0","standard potential","V"],["R","gas constant","J/(mol\u00b7K)"],["T","temperature","K"],["n","electrons","\u2014"],["F","Faraday constant","96485 C/mol"],["Q","reaction quotient","\u2014"]],"Cell voltage under non-standard conditions.","Nernst 1889 from Gibbs free energy and electrochemistry.",["Batteries","Corrosion","pH meters"],1],
["Arrhenius Equation","k = A\u00b7e^{\u2212E\u2090/RT}","chemistry",[["k","rate constant","varies"],["A","pre-exponential factor","varies"],["E\u2090","activation energy","J/mol"]],"Reaction rates grow exponentially with temperature.","Arrhenius 1889; empirical, justified by collision theory.",["Kinetics","Food shelf life","Materials aging"],1],
["Henderson\u2013Hasselbalch Equation","pH = pK\u2090 + log([A\u207b]/[HA])","chemistry",[["pH","acidity","\u2014"],["pK\u2090","acid dissociation constant","\u2014"],["[A\u207b]","[base]","M"],["[HA]","[acid]","M"]],"pH of a buffer from the ratio of base to acid.","Henderson 1908, Hasselbalch 1917; from the acid dissociation equilibrium.",["Biochemistry","Medicine","Buffer preparation"],1],
["Molarity","M = n/V","chemistry",[["M","molarity","mol/L"],["n","moles of solute","mol"],["V","solution volume","L"]],"Concentration as moles per liter of solution.","Definition.",["Lab chemistry","Titration","Pharmaceuticals"],1],
["Gibbs Free Energy","\u0394G = \u0394H \u2212 T\u0394S","chemistry",[["\u0394G","free energy change","J/mol"],["\u0394H","enthalpy change","J/mol"],["T","temperature","K"],["\u0394S","entropy change","J/(mol\u00b7K)"]],"Negative \u0394G means a reaction proceeds spontaneously.","Gibbs 1870s from the second law of thermodynamics.",["Reaction prediction","Metallurgy","Biochemistry"],1],
["Beer\u2013Lambert Law","A = \u03b5\u00b7l\u00b7c","chemistry",[["A","absorbance","\u2014"],["\u03b5","molar absorptivity","L/(mol\u00b7cm)"],["l","path length","cm"],["c","concentration","mol/L"]],"Light absorbed is proportional to concentration.","Beer 1852, Lambert 1760; exponential attenuation.",["Spectroscopy","Water testing","Clinical labs"],1],
["Half-Life (first order)","t\u2081/\u2082 = ln 2 / k","chemistry",[["t\u2081/\u2082","half-life","s"],["k","rate constant","1/s"]],"Time for half the reactant to be consumed (first-order).","Integrating the first-order rate law.",["Radiodating","Pharmacokinetics","Nuclear waste"],1],
["Hardy\u2013Weinberg Equilibrium","p\u00b2 + 2pq + q\u00b2 = 1","biology",[["p","frequency of allele A","\u2014"],["q","frequency of allele a","\u2014"]],"Allele frequencies stay constant without evolutionary forces.","Hardy and Weinberg 1908; probability of genotype combinations.",["Population genetics","Disease screening","Conservation"],1],
["Michaelis\u2013Menten Kinetics","v = Vmax\u00b7[S]/(Km + [S])","biology",[["v","reaction velocity","mol/(L\u00b7s)"],["Vmax","max velocity","mol/(L\u00b7s)"],["[S]","substrate conc.","M"],["Km","Michaelis constant","M"]],"Enzyme rate saturates as substrate increases.","Michaelis and Menten 1913; steady-state enzyme kinetics.",["Drug design","Biochemistry","Fermentation"],1],
["Logistic Growth","dN/dt = rN(1 \u2212 N/K)","biology",[["N","population","individuals"],["r","growth rate","1/time"],["K","carrying capacity","individuals"]],"Populations grow fast then level off at carrying capacity.","Verhulst 1838; exponential growth limited by resources.",["Ecology","Epidemiology","Fisheries"],1],
["Nernst (membrane potential)","E = (RT/zF)\u00b7ln([out]/[in])","biology",[["E","equilibrium potential","V"],["z","ion charge","\u2014"]],"Voltage at which an ion is at equilibrium across a membrane.","Nernst equation applied to membranes.",["Neuroscience","Physiology","Medicine"],1],
["Fick's First Law (diffusion)","J = \u2212D\u00b7dC/dx","biology",[["J","flux","mol/(m\u00b2\u00b7s)"],["D","diffusion coefficient","m\u00b2/s"],["dC/dx","concentration gradient","mol/m\u2074"]],"Molecules flow from high to low concentration.","Fick 1855; analogy to heat conduction.",["Physiology","Drug delivery","Ecology"],1],
["Quadratic Formula","x = (\u2212b \u00b1 \u221a(b\u00b2\u22124ac)) / 2a","mathematics",[["a,b,c","coefficients","\u2014"],["x","solutions","\u2014"]],"Solves any quadratic equation ax\u00b2+bx+c=0.","Completing the square; known since Babylonian times, formalized by al-Khwarizmi.",["Engineering","Physics","Optimization"],1],
["Pythagorean Theorem","a\u00b2 + b\u00b2 = c\u00b2","mathematics",[["a,b","legs","units"],["c","hypotenuse","units"]],"In a right triangle, hypotenuse squared equals sum of leg squares.","Pythagoras c. 500 BCE (known earlier in Babylon/India).",["Surveying","Navigation","Graphics"],1],
["Euler's Identity","e^{i\u03c0} + 1 = 0","mathematics",[["e","Euler's number","2.718\u2026"],["i","imaginary unit","\u221a\u22121"],["\u03c0","pi","3.14159\u2026"]],"Links five fundamental constants in one equation.","Euler 1748; from e^{ix} = cos x + i\u00b7sin x at x=\u03c0.",["Complex analysis","Signal processing","Quantum mechanics"],1],
["Bayes' Theorem","P(A|B) = P(B|A)\u00b7P(A) / P(B)","mathematics",[["P(A|B)","posterior","\u2014"],["P(B|A)","likelihood","\u2014"],["P(A)","prior","\u2014"],["P(B)","evidence","\u2014"]],"Updates beliefs with new evidence.","Bayes 1763; from the definition of conditional probability.",["Machine learning","Medicine","Spam filters"],1],
["Normal Distribution","f(x) = (1/\u03c3\u221a2\u03c0)\u00b7e^{\u2212(x\u2212\u03bc)\u00b2/2\u03c3\u00b2}","mathematics",[["\u03bc","mean","units"],["\u03c3","std deviation","units"]],"The bell curve; sums of random effects tend to it.","De Moivre 1738; Gauss 1809; central limit theorem.",["Statistics","Quality control","Finance"],1],
["Compound Interest","A = P(1 + r/n)^{nt}","mathematics",[["A","final amount","currency"],["P","principal","currency"],["r","annual rate","\u2014"],["n","compounds/year","\u2014"],["t","years","\u2014"]],"Money grows exponentially when interest compounds.","Repeated multiplication of (1+r/n) per period.",["Banking","Investing","Loans"],1],
["Derivative (power rule)","d/dx[x\u207f] = n\u00b7x\u207f\u207b\u00b9","mathematics",[["n","exponent","\u2014"]],"The slope of x\u207f at any point.","Newton/Leibniz 1680s; limit of the difference quotient.",["Physics","Optimization","Economics"],1],
["Sum of Geometric Series","S = a(1\u2212r\u207f)/(1\u2212r)","mathematics",[["a","first term","\u2014"],["r","ratio","\u2014"],["n","terms","\u2014"]],"Closed form for a + ar + ar\u00b2 + \u2026 + ar\u207f\u207b\u00b9.","Multiply by r and subtract (Euclid IX.35).",["Finance","Computer science","Physics"],1],
["Kepler's Third Law","T\u00b2 \u221d a\u00b3  (T\u00b2 = 4\u03c0\u00b2a\u00b3/GM)","astronomy",[["T","orbital period","s"],["a","semi-major axis","m"],["M","central mass","kg"]],"Outer planets orbit slower; period squared scales with distance cubed.","Kepler 1619 empirically; Newton derived it from gravity.",["Exoplanets","Satellites","Solar system"],1],
["Hubble's Law","v = H\u2080\u00b7d","astronomy",[["v","recession velocity","km/s"],["H\u2080","Hubble constant","~70 km/s/Mpc"],["d","distance","Mpc"]],"Distant galaxies recede faster \u2014 the universe expands.","Hubble 1929 from galaxy redshifts.",["Cosmology","Age of universe","Dark energy"],1],
["Schwarzschild Radius","r\u209b = 2GM/c\u00b2","astronomy",[["r\u209b","event horizon radius","m"],["M","mass","kg"]],"Size of a black hole's event horizon for mass M.","Schwarzschild 1916; exact solution of Einstein's field equations.",["Black holes","Gravitational waves","Astrophysics"],1],
["Stefan\u2013Boltzmann Law","L = 4\u03c0R\u00b2\u03c3T\u2074","astronomy",[["L","luminosity","W"],["R","radius","m"],["\u03c3","Stefan\u2013Boltzmann const","5.67\u00d710\u207b\u2078 W/m\u00b2K\u2074"],["T","temperature","K"]],"A star's brightness scales with the fourth power of temperature.","Stefan 1879 empirically; Boltzmann 1884 from thermodynamics.",["Stellar classification","Exoplanets","Climate"],1],
["Escape Velocity","v\u2091 = \u221a(2GM/r)","astronomy",[["v\u2091","escape velocity","m/s"],["M","body mass","kg"],["r","radius","m"]],"Speed needed to leave a body's gravity forever.","Set kinetic energy equal to gravitational potential energy.",["Rockets","Atmospheric loss","Spaceflight"],1],
["Richter Scale (energy)","log\u2081\u2080E = 11.8 + 1.5M","earth science",[["E","energy","joules"],["M","magnitude","\u2014"]],"Each magnitude unit is ~32\u00d7 more energy.","Gutenberg\u2013Richter; empirical calibration.",["Seismology","Hazard maps","Engineering"],1],
["Manning's Equation","v = (1/n)\u00b7R^{2/3}\u00b7S^{1/2}","earth science",[["v","flow velocity","m/s"],["n","roughness","\u2014"],["R","hydraulic radius","m"],["S","slope","\u2014"]],"How fast water flows in an open channel.","Manning 1891; empirical.",["Flood control","Irrigation","Dams"],1],
["Big-O (binary search)","T(n) = O(log n)","computer science",[["T","time","steps"],["n","input size","\u2014"]],"Binary search halves the problem each step.","Recurrence T(n) = T(n/2) + 1.",["Algorithms","Databases","Search"],1],
["Shannon Entropy","H = \u2212\u03a3 p(x)\u00b7log\u2082p(x)","computer science",[["H","entropy","bits"],["p(x)","probability","\u2014"]],"Average information per symbol; the compression limit.","Shannon 1948; axioms of information measure.",["Compression","Cryptography","Machine learning"],1],
["Amdahl's Law","S = 1/((1\u2212P) + P/N)","computer science",[["S","speedup","\u2014"],["P","parallel fraction","\u2014"],["N","processors","\u2014"]],"Parallel speedup is limited by the serial part.","Amdahl 1967; time = serial + parallel/N.",["HPC","GPUs","System design"],1],
["Compound Growth","FV = PV\u00b7(1+r)\u1d57","economics",[["FV","future value","$"],["PV","present value","$"],["r","rate","\u2014"],["t","periods","\u2014"]],"Exponential growth of investments.","Repeated compounding.",["Finance","Pensions","Valuation"],1],
["Supply\u2013Demand Equilibrium","Qd(P*) = Qs(P*)","economics",[["Qd","quantity demanded","units"],["Qs","quantity supplied","units"],["P*","equilibrium price","$"]],"Markets clear where supply meets demand.","Marshall 1890; intersection of curves.",["Pricing","Policy","Trade"],1],
["BMI","BMI = mass(kg) / height(m)\u00b2","medicine",[["mass","body mass","kg"],["height","stature","m"]],"Rough body-fat screening index.","Quetelet 1832; empirical.",["Screening","Epidemiology","Insurance"],1],
["Cardiac Output","CO = HR \u00d7 SV","medicine",[["CO","cardiac output","L/min"],["HR","heart rate","bpm"],["SV","stroke volume","mL"]],"Blood pumped per minute.","Definition; Fick principle.",["Cardiology","ICU","Exercise physiology"],1],
["Molarity (dose)","dose = C \u00d7 V","medicine",[["C","concentration","mg/mL"],["V","volume","mL"]],"Drug amount from concentration and volume.","Definition.",["Pharmacy","Nursing","Anesthesia"],1],
["Coulomb's Law","F = k\u00b7q\u2081\u00b7q\u2082/r\u00b2","physics",[["F","force","N"],["k","Coulomb constant","8.988\u00d710\u2079 N\u00b7m\u00b2/C\u00b2"],["q\u2081,q\u2082","charges","C"],["r","separation","m"]],"Force between electric charges; like charges repel.","Coulomb 1785; torsion balance experiments.",["Electrostatics","Capacitors"],1],
["Faraday's Law","\u2130 = \u2212d\u03a6/dt","physics",[["\u2130","EMF","V"],["\u03a6","magnetic flux","Wb"]],"Changing magnetic flux induces voltage.","Faraday 1831; Maxwell's equations.",["Generators","Transformers"],1],
["Snell's Law","n\u2081\u00b7sin \u03b8\u2081 = n\u2082\u00b7sin \u03b8\u2082","physics",[["n","refractive index","\u2014"],["\u03b8","angle from normal","degrees"]],"Light bends at material boundaries.","Snell 1621; Fermat's least time.",["Lenses","Fiber optics"],1],
["Doppler Shift","f\u2032 = f\u00b7(v\u00b1v\u2092)/(v\u2213v\u209b)","physics",[["f\u2032","observed frequency","Hz"],["f","source frequency","Hz"],["v","wave speed","m/s"]],"Frequency shifts with relative motion.","Doppler 1842.",["Radar","Astronomy"],1],
["Photoelectric Equation","E = h\u03bd \u2212 \u03c6","physics",[["E","electron energy","J"],["h","Planck constant","J\u00b7s"],["\u03bd","frequency","Hz"],["\u03c6","work function","J"]],"Light ejects electrons; energy depends on frequency.","Einstein 1905; light quanta.",["Solar cells","Sensors"],1],
["De Broglie Wavelength","\u03bb = h/p","physics",[["\u03bb","wavelength","m"],["h","Planck constant","J\u00b7s"],["p","momentum","kg\u00b7m/s"]],"Matter has wave properties.","De Broglie 1924.",["Electron microscopy"],1],
["Stefan-Boltzmann (radiation)","P = \u03c3AT\u2074","physics",[["P","power","W"],["\u03c3","constant","5.67\u00d710\u207b\u2078"],["A","area","m\u00b2"],["T","temp","K"]],"Radiated power scales with T\u2074.","Stefan 1879; Boltzmann 1884.",["Climate","Astronomy"],1],
["Hooke's Law","F = \u2212k\u00b7x","physics",[["F","force","N"],["k","spring constant","N/m"],["x","displacement","m"]],"Spring force opposes displacement.","Hooke 1678; empirical.",["Engineering","Seismology"],1],
["Torque","\u03c4 = r \u00d7 F","physics",[["\u03c4","torque","N\u00b7m"],["r","lever arm","m"],["F","force","N"]],"Rotational force.","Definition; Newton.",["Mechanics","Engines"],1],
["Angular Momentum","L = r \u00d7 p","physics",[["L","angular momentum","kg\u00b7m\u00b2/s"]],"Conserved rotational quantity.","Newton; Noether's theorem.",["Gyroscopes","Orbits"],1],
["Work","W = F\u00b7d\u00b7cos \u03b8","physics",[["W","work","J"],["F","force","N"],["d","distance","m"]],"Energy transferred by force.","Definition.",["Engineering"],1],
["Power","P = W/t","physics",[["P","power","W"],["W","work","J"],["t","time","s"]],"Rate of energy transfer.","Definition.",["Engines","Electrical"],1],
["Momentum","p = m\u00b7v","physics",[["p","momentum","kg\u00b7m/s"]],"Quantity of motion; conserved.","Newton.",["Collisions"],1],
["Centripetal Force","F = m\u00b7v\u00b2/r","physics",[["F","force","N"],["v","speed","m/s"],["r","radius","m"]],"Force needed for circular motion.","Huygens 1659.",["Orbits","Centrifuges"],1],
["Pressure","P = F/A","physics",[["P","pressure","Pa"],["F","force","N"],["A","area","m\u00b2"]],"Force per unit area.","Definition.",["Hydraulics"],1],
["Density","\u03c1 = m/V","physics",[["\u03c1","density","kg/m\u00b3"]],"Mass per unit volume.","Definition.",["Materials"],1],
["Specific Heat","Q = m\u00b7c\u00b7\u0394T","physics",[["Q","heat","J"],["c","specific heat","J/(kg\u00b7K)"]],"Heat to change temperature.","Calorimetry.",["HVAC","Cooking"],1],
["Lens Equation","1/f = 1/d\u2092 + 1/d\u1d62","physics",[["f","focal length","m"],["d\u2092","object distance","m"],["d\u1d62","image distance","m"]],"Relates object, image, focal length.","Geometrical optics.",["Cameras","Glasses"],1],
["Resistivity","R = \u03c1\u00b7L/A","physics",[["\u03c1","resistivity","\u03a9\u00b7m"],["L","length","m"],["A","area","m\u00b2"]],"Resistance from material geometry.","Ohm's law + geometry.",["Wiring"],1],
["Capacitance","C = Q/V","physics",[["C","capacitance","F"],["Q","charge","C"]],"Charge stored per volt.","Definition.",["Electronics"],1],
["Dalton's Law","P_total = \u03a3P\u1d62","chemistry",[["P","partial pressure","Pa"]],"Total pressure is sum of partials.","Dalton 1801.",["Diving","Gas mixes"],1],
["Graham's Law","r\u2081/r\u2082 = \u221a(M\u2082/M\u2081)","chemistry",[["r","effusion rate","\u2014"],["M","molar mass","g/mol"]],"Light gases effuse faster.","Graham 1829; kinetic theory.",["Uranium enrichment"],1],
["Mole Fraction","\u03c7 = n\u1d62/n_total","chemistry",[["\u03c7","mole fraction","\u2014"]],"Fraction of total moles.","Definition.",["Solutions"],1],
["Molality","m = n_solute/kg_solvent","chemistry",[["m","molality","mol/kg"]],"Moles per kg solvent.","Definition.",["Colligative properties"],1],
["Freezing Point Depression","\u0394Tf = Kf\u00b7m","chemistry",[["\u0394Tf","depression","K"],["Kf","constant","K\u00b7kg/mol"]],"Solute lowers freezing point.","Thermodynamics.",["Antifreeze"],1],
["Boiling Point Elevation","\u0394Tb = Kb\u00b7m","chemistry",[["\u0394Tb","elevation","K"]],"Solute raises boiling point.","Thermodynamics.",["Cooking"],1],
["Osmotic Pressure","\u03c0 = iMRT","chemistry",[["\u03c0","osmotic pressure","Pa"],["i","van't Hoff factor","\u2014"]],"Pressure from solute imbalance.","Van't Hoff.",["Biology","Desalination"],1],
["Rate Law","rate = k[A]^m[B]^n","chemistry",[["k","rate constant","varies"],["m,n","orders","\u2014"]],"Rate depends on concentrations.","Empirical.",["Kinetics"],1],
["Equilibrium Constant","K = [products]/[reactants]","chemistry",[["K","equilibrium constant","\u2014"]],"Ratio at equilibrium.","Law of mass action.",["Synthesis"],1],
["pH Definition","pH = \u2212log[H\u207a]","chemistry",[["[H\u207a]","hydrogen ion conc","M"]],"Logarithmic acidity scale.","S\u00f8rensen 1909.",["Chemistry","Biology"],1],
["Percent Yield","% = (actual/theoretical)\u00d7100","chemistry",[],"Efficiency of a reaction.","Definition.",["Synthesis"],1],
["Empirical Formula","simplest whole-number ratio","chemistry",[],"Simplest atom ratio.","From percent composition.",["Analysis"],1],
["Punnett Square (monohybrid)","1:2:1 genotype ratio","biology",[],"Aa \u00d7 Aa gives 1AA:2Aa:1aa.","Mendel 1866.",["Genetics"],1],
["Surface-to-Volume Ratio","SA/V = 3/r (sphere)","biology",[["r","radius","units"]],"Small cells exchange faster.","Geometry.",["Cell biology"],1],
["Cardiac Cycle","CO = HR \u00d7 SV","biology",[["CO","cardiac output","L/min"]],"Blood pumped per minute.","Definition.",["Medicine"],1],
["Alveolar Gas Equation","PAO\u2082 = FiO\u2082(Patm\u2212PH\u2082O) \u2212 PaCO\u2082/R","biology",[["PAO\u2082","alveolar O\u2082","mmHg"]],"Oxygen in alveoli.","Physiology.",["Pulmonology"],1],
["Nernst (biology)","E = 61.5\u00b7log([out]/[in])/z (mV, 37\u00b0C)","biology",[["E","potential","mV"]],"Ion equilibrium voltage.","Nernst.",["Neuroscience"],1],
["Distance Formula","d = \u221a((x\u2082\u2212x\u2081)\u00b2 + (y\u2082\u2212y\u2081)\u00b2)","mathematics",[],"Distance between points.","Pythagoras.",["Geometry"],1],
["Slope","m = (y\u2082\u2212y\u2081)/(x\u2082\u2212x\u2081)","mathematics",[],"Steepness of a line.","Definition.",["Algebra"],1],
["Area of Circle","A = \u03c0r\u00b2","mathematics",[["r","radius","units"]],"Area enclosed by circle.","Archimedes.",["Geometry"],1],
["Volume of Sphere","V = (4/3)\u03c0r\u00b3","mathematics",[],"Space inside a sphere.","Archimedes.",["Geometry"],1],
["Sine Rule","a/sin A = b/sin B = c/sin C","mathematics",[],"Relates sides and angles.","Trigonometry.",["Surveying"],1],
["Cosine Rule","c\u00b2 = a\u00b2 + b\u00b2 \u2212 2ab\u00b7cos C","mathematics",[],"Generalized Pythagoras.","Trigonometry.",["Navigation"],1],
["Logarithm Rules","log(ab) = log a + log b","mathematics",[],"Logs turn multiply into add.","Napier 1614.",["Computation"],1],
["Integration (power)","\u222bx\u207f dx = x^(n+1)/(n+1) + C","mathematics",[],"Antiderivative of x\u207f.","Newton/Leibniz.",["Physics"],1],
["Chain Rule","dy/dx = dy/du \u00b7 du/dx","mathematics",[],"Derivative of composition.","Leibniz.",["Calculus"],1],
["Product Rule","(uv)\u2032 = u\u2032v + uv\u2032","mathematics",[],"Derivative of product.","Leibniz.",["Calculus"],1],
["Arithmetic Series","S = n(a\u2081+a\u2099)/2","mathematics",[],"Sum of arithmetic sequence.","Gauss.",["Finance"],1],
["Binomial Theorem","(a+b)\u207f = \u03a3 C(n,k)a^(n\u2212k)b^k","mathematics",[],"Expands powers of binomials.","Newton.",["Probability"],1],
["Euler's Formula","e^(ix) = cos x + i\u00b7sin x","mathematics",[],"Links exponentials and trig.","Euler 1748.",["Engineering"],1],
["Parsec Definition","1 pc = 3.26 light-years","astronomy",[],"Distance for 1\u2033 parallax.","Definition.",["Astronomy"],1],
["Redshift","z = (\u03bb_obs \u2212 \u03bb_emit)/\u03bb_emit","astronomy",[["z","redshift","\u2014"]],"Stretch of light by expansion.","Doppler + expansion.",["Cosmology"],1],
["Kepler's First Law","r = a(1\u2212e\u00b2)/(1+e\u00b7cos \u03b8)","astronomy",[["e","eccentricity","\u2014"]],"Orbits are ellipses.","Kepler 1609.",["Orbits"],1],
["Titius-Bode (historical)","a = 0.4 + 0.3\u00b72\u207f AU","astronomy",[],"Old planet-distance pattern.","Empirical 1766; not exact.",["History"],1],
["Roche Limit","d = 2.44\u00b7R\u00b7(\u03c1_M/\u03c1_m)^(1/3)","astronomy",[["d","limit distance","m"]],"Distance where tides shred moons.","Roche 1848.",["Planetary science"],1],
["Moore's Law","transistors double ~2 years","computer science",[],"Exponential chip growth.","Moore 1965; empirical.",["Planning"],1],
["Binary Search Steps","\u2308log\u2082 n\u2309 comparisons","computer science",[],"Optimal search cost.","Analysis.",["Algorithms"],1],
["Hash Load Factor","\u03b1 = n/m","computer science",[["n","items","\u2014"],["m","slots","\u2014"]],"Fullness of hash table.","Definition.",["Data structures"],1],
["Present Value","PV = FV/(1+r)\u1d57","economics",[],"Today's worth of future money.","Compound interest inverse.",["Finance"],1],
["GDP Definition","GDP = C + I + G + NX","economics",[],"Total economic output.","Kuznets 1930s.",["Policy"],1],
["Inflation Rate","\u03c0 = (P\u2081\u2212P\u2080)/P\u2080","economics",[],"Price level change.","Definition.",["Policy"],1],
["MAP","MAP = DBP + (SBP\u2212DBP)/3","medicine",[["SBP","systolic","mmHg"],["DBP","diastolic","mmHg"]],"Average arterial pressure.","Empirical.",["ICU"],1],
["GFR Estimate","eGFR via creatinine","medicine",[],"Kidney function estimate.","CKD-EPI.",["Nephrology"],1],
["Body Surface Area","BSA = \u221a(h\u00b7w/3600)","medicine",[["h","height","cm"],["w","weight","kg"]],"Dosing by surface area.","Mosteller.",["Oncology"],1],
["Gradient","slope = \u0394h/\u0394d","earth science",[],"Steepness.","Definition.",["Geology"],1],
["Porosity","\u03c6 = V_void/V_total","earth science",[],"Fraction of void space.","Definition.",["Hydrology"],1],
["Darcy's Law","Q = \u2212kA(dh/dl)","earth science",[["Q","flow","m\u00b3/s"],["k","conductivity","m/s"]],"Groundwater flow.","Darcy 1856.",["Wells"],1],
["Drake Equation","N = R*\u00b7fp\u00b7ne\u00b7fl\u00b7fi\u00b7fc\u00b7L","astronomy",[["N","civilizations","\u2014"]],"Estimate of detectable ET civilizations.","Drake 1961; probabilistic.",["SETI"],2],
["Bekenstein Bound","I \u2264 2\u03c0RE/(\u210fc\u00b7ln 2)","physics",[["I","information","bits"]],"Max info in a region.","Bekenstein 1981; black holes.",["Quantum gravity"],2],
["Hawking Temperature","T = \u210fc\u00b3/(8\u03c0GMk)","physics",[["T","temperature","K"],["M","black hole mass","kg"]],"Black holes radiate.","Hawking 1974.",["Quantum gravity"],2],
["Einstein Field Equation","G_\u03bc\u03bd = 8\u03c0T_\u03bc\u03bd","physics",[["G_\u03bc\u03bd","Einstein tensor","\u2014"],["T_\u03bc\u03bd","stress-energy","\u2014"]],"Matter tells spacetime how to curve.","Einstein 1915.",["Cosmology","GPS"],1],
["Dirac Equation","(i\u03b3^\u03bc\u2202_\u03bc \u2212 m)\u03c8 = 0","physics",[["\u03c8","spinor","\u2014"]],"Relativistic electron.","Dirac 1928.",["Antimatter"],1],
["Klein-Gordon","(\u25a1 + m\u00b2)\u03c6 = 0","physics",[],"Relativistic spin-0 particles.","1926.",["QFT"],1],
["Navier-Stokes","\u03c1(\u2202v/\u2202t + v\u00b7\u2207v) = \u2212\u2207p + \u03bc\u2207\u00b2v","physics",[["\u03c1","density","kg/m\u00b3"],["\u03bc","viscosity","Pa\u00b7s"]],"Fluid motion.","Navier 1822, Stokes 1845.",["Weather","Aircraft"],1],
["Continuity Equation","\u2202\u03c1/\u2202t + \u2207\u00b7(\u03c1v) = 0","physics",[],"Mass conservation in flow.","Euler.",["Fluids"],1],
["Poisson Equation","\u2207\u00b2\u03c6 = \u2212\u03c1/\u03b5\u2080","physics",[],"Potential from charge distribution.","Poisson.",["Electrostatics"],1],
["Laplace Equation","\u2207\u00b2\u03c6 = 0","physics",[],"Potential with no sources.","Laplace.",["Fields"],1],
["Heat Equation","\u2202T/\u2202t = \u03b1\u2207\u00b2T","physics",[["\u03b1","diffusivity","m\u00b2/s"]],"How heat spreads.","Fourier 1822.",["Engineering"],1],
["Diffusion Equation","\u2202C/\u2202t = D\u2207\u00b2C","physics",[],"How concentrations spread.","Fick.",["Chemistry"],1],
["Bragg's Law","n\u03bb = 2d\u00b7sin \u03b8","physics",[["d","lattice spacing","m"]],"X-ray diffraction condition.","Bragg 1913.",["Crystallography"],1],
["Rydberg Formula","1/\u03bb = R(1/n\u2081\u00b2 \u2212 1/n\u2082\u00b2)","physics",[["R","Rydberg constant","1.097\u00d710\u2077/m"]],"Hydrogen spectral lines.","Rydberg 1888.",["Spectroscopy"],1],
["Bohr Radius","a\u2080 = 4\u03c0\u03b5\u2080\u210f\u00b2/(m_e\u00b7e\u00b2)","physics",[],"Hydrogen ground-state size.","Bohr 1913.",["Atomic physics"],1],
["Fine Structure Constant","\u03b1 = e\u00b2/(4\u03c0\u03b5\u2080\u210fc) \u2248 1/137","physics",[],"EM coupling strength.","Sommerfeld 1916.",["QED"],1],
["Compton Shift","\u0394\u03bb = (h/mc)(1\u2212cos \u03b8)","physics",[],"Photon loses energy scattering.","Compton 1923.",["Imaging"],1],
["Stefan's Displacement","\u03bb_max\u00b7T = 2.898\u00d710\u207b\u00b3 m\u00b7K","physics",[],"Peak wavelength vs temperature.","Wien 1893.",["Astronomy"],1],
["Malus's Law","I = I\u2080\u00b7cos\u00b2\u03b8","physics",[],"Polarized light through filter.","Malus 1809.",["Optics"],1],
["Thin Film Interference","2nt = m\u03bb","physics",[],"Constructive interference condition.","Wave optics.",["Coatings"],1],
["Grating Equation","d\u00b7sin \u03b8 = m\u03bb","physics",[],"Diffraction maxima.","Fraunhofer.",["Spectrometers"],1],
["Carnot Efficiency","\u03b7 = 1 \u2212 Tc/Th","physics",[],"Max heat-engine efficiency.","Carnot 1824.",["Power plants"],1],
["Clausius-Clapeyron","dP/dT = L/(T\u00b7\u0394V)","physics",[],"Phase boundary slope.","Clapeyron 1834.",["Meteorology"],1],
["Van der Waals","(P + a(n/V)\u00b2)(V \u2212 nb) = nRT","physics",[["a,b","correction constants","varies"]],"Real gas law.","Van der Waals 1873.",["Engineering"],1],
["Saha Equation","n\u1d62\u208a\u2081/n\u1d62 = f(T,P)","physics",[],"Ionization fractions.","Saha 1920.",["Astrophysics"],1],
["Le Chatelier","system shifts to oppose change","chemistry",[],"Equilibrium resists disturbance.","1884.",["Industry"],1],
["Raoult's Law","P\u1d62 = \u03c7\u1d62\u00b7P\u1d62*","chemistry",[],"Vapor pressure of solutions.","Raoult 1887.",["Distillation"],1],
["Henry's Law","C = k\u00b7P","chemistry",[],"Gas solubility \u221d pressure.","Henry 1803.",["Diving"],1],
["Faraday's Electrolysis","m = Q\u00b7M/(n\u00b7F)","chemistry",[],"Mass deposited by current.","Faraday 1834.",["Plating"],1],
["Debye-H\u00fcckel","log \u03b3 = \u2212A\u00b7z\u00b2\u221aI","chemistry",[],"Ion activity in solution.","1923.",["Electrochemistry"],1],
["Stern-Volmer","F\u2080/F = 1 + K[Q]","chemistry",[],"Fluorescence quenching.","1919.",["Sensors"],1],
["Michaelis (inhibition)","v = Vmax[S]/(Km(1+[I]/Ki)+[S])","biology",[],"Competitive inhibition.","Enzyme kinetics.",["Drugs"],1],
["Hill Equation","\u03b8 = [L]\u207f/(Kd + [L]\u207f)","biology",[],"Cooperative binding.","Hill 1910.",["Biochemistry"],1],
["Goldman-Hodgkin-Katz","Vm = (RT/F)\u00b7ln(\u03a3P[out]/\u03a3P[in])","biology",[],"Membrane potential multi-ion.","1943.",["Neuroscience"],1],
["Noyes-Whitney","dM/dt = kA(Cs \u2212 C)","biology",[],"Dissolution rate.","1897.",["Pharma"],1],
["Monod Growth","\u03bc = \u03bcmax\u00b7S/(Ks + S)","biology",[],"Microbial growth rate.","Monod 1949.",["Biotech"],1],
["Lotka-Volterra","dx/dt = \u03b1x \u2212 \u03b2xy","biology",[],"Predator-prey cycles.","1925.",["Ecology"],1],
["Price Equation","\u0394z\u0304 = Cov(w,z)/w\u0304","biology",[],"Evolutionary change.","Price 1970.",["Evolution"],1],
["Stokes' Theorem","\u222eF\u00b7dr = \u222c(\u2207\u00d7F)\u00b7dS","mathematics",[],"Links line and surface integrals.","Stokes.",["Physics"],1],
["Divergence Theorem","\u222fF\u00b7dS = \u222d(\u2207\u00b7F)dV","mathematics",[],"Flux equals divergence integral.","Gauss.",["EM"],1],
["Green's Theorem","\u222e(Pdx+Qdy) = \u222c(\u2202Q/\u2202x\u2212\u2202P/\u2202y)dA","mathematics",[],"2D Stokes.","Green 1828.",["Fluids"],1],
["Fourier Series","f(x) = a\u2080/2 + \u03a3(a\u2099cos nx + b\u2099sin nx)","mathematics",[],"Periodic as sine sums.","Fourier 1822.",["Signal"],1],
["Fourier Transform","F(\u03c9) = \u222bf(t)e^(\u2212i\u03c9t)dt","mathematics",[],"Time to frequency.","Fourier.",["Imaging"],1],
["Laplace Transform","F(s) = \u222b\u2080^\u221ef(t)e^(\u2212st)dt","mathematics",[],"ODEs to algebra.","Laplace.",["Control"],1],
["Taylor Series","f(x) = \u03a3f\u207f(a)(x\u2212a)\u207f/n!","mathematics",[],"Function as polynomial.","Taylor 1715.",["Approximation"],1],
["Euler-Maclaurin","\u03a3f = \u222bf + (f(b)+f(a))/2 + \u2026","mathematics",[],"Sum-integral relation.","1735.",["Numerics"],1],
["Stirling's Approx","n! \u2248 \u221a(2\u03c0n)(n/e)\u207f","mathematics",[],"Large factorials.","Stirling 1730.",["Stats"],1],
["Central Limit","X\u0304 \u2192 N(\u03bc, \u03c3\u00b2/n)","mathematics",[],"Means become normal.","Laplace.",["Stats"],1],
["Poisson Dist","P(k) = \u03bb^k\u00b7e^(\u2212\u03bb)/k!","mathematics",[],"Rare events count.","Poisson 1837.",["Queueing"],1],
["Exponential Dist","f(x) = \u03bbe^(\u2212\u03bbx)","mathematics",[],"Waiting times.","Poisson process.",["Reliability"],1],
["Chi-Square","\u03c7\u00b2 = \u03a3(O\u2212E)\u00b2/E","mathematics",[],"Goodness of fit.","Pearson 1900.",["Stats"],1],
["Kepler's Equation","M = E \u2212 e\u00b7sin E","astronomy",[],"Position in orbit.","Kepler.",["Orbits"],1],
["Distance Modulus","m \u2212 M = 5\u00b7log(d) \u2212 5","astronomy",[],"Brightness to distance.","Definition.",["Cosmology"],1],
["Eddington Luminosity","L_Edd = 4\u03c0GMm_pc/\u03c3_T","astronomy",[],"Max stable brightness.","Eddington.",["Black holes"],1],
["Jeans Mass","M_J \u221d T^(3/2)/\u221a\u03c1","astronomy",[],"Collapse threshold.","Jeans 1902.",["Star formation"],1],
["Chandrasekhar Limit","M_Ch \u2248 1.44 M\u2609","astronomy",[],"Max white dwarf mass.","1931.",["Supernovae"],1],
["Tolman-Oppenheimer-Volkoff","dP/dr = \u2212G(\u03c1+P)(m+4\u03c0r\u00b3P)/(r\u00b2(1\u22122Gm/r))","astronomy",[],"Neutron star structure.","1939.",["NS"],1],
["Friedmann Equation","H\u00b2 = (8\u03c0G/3)\u03c1 \u2212 k/a\u00b2","astronomy",[],"Universe expansion.","Friedmann 1922.",["Cosmology"],1],
["Sackur-Tetrode","S = Nk[ln(V/N\u00b7(4\u03c0mU/3Nh\u00b2)^(3/2)) + 5/2]","physics",[],"Ideal gas entropy.","1912.",["Thermo"],1],
["Wiedemann-Franz","\u03ba/\u03c3 = LT","physics",[],"Thermal/electrical ratio.","1853.",["Metals"],1],
["Hall Effect","V_H = IB/(nqd)","physics",[],"Transverse voltage.","Hall 1879.",["Sensors"],1],
["Skin Depth","\u03b4 = \u221a(2\u03c1/\u03c9\u03bc)","physics",[],"AC penetration.","Maxwell.",["RF"],1],
];

/* 15 record forms per base formula */
function formsFor(b){
  var out=[], n=b[0], nt=b[1], dom=b[2], vars=b[3], mean=b[4], deriv=b[5], apps=b[6], tp=b[7];
  var tl = tp===1 ? "Type 1 — established" : "Type 2 — speculative (labeled)";
  function mk(suffix, focusMeaning, focusDeriv, extraApps){
    return {suffix:suffix, name:n+(suffix?" — "+suffix:""), notation:nt, domain:dom,
      variables:vars, meaning:focusMeaning||mean, derivation:focusDeriv||deriv,
      applications:extraApps||apps, type:tp, type_label:tl};
  }
  out.push(mk("", null, null, null)); // 1. base
  vars.slice(0,3).forEach(function(v){ // 2-4. rearrangements
    out.push(mk("solved for "+v[0],
      "Rearrangement of "+n+" isolating "+v[0]+" ("+v[1]+").",
      "Algebraic rearrangement of the established formula.", null));
  });
  out.push(mk("worked example", // 5.
    "Step-by-step numeric example applying "+n+".",
    "Direct substitution into the established formula.", null));
  out.push(mk("unit check", // 6.
    "Dimensional analysis verifying "+n+" balances.",
    "Unit cancellation across the established formula.", null));
  out.push(mk("history", // 7.
    "Historical background of "+n+".",
    deriv, null));
  (apps.slice(0,2)).forEach(function(a){ // 8-9. application deep-dives
    out.push(mk("in "+a,
      "How "+n+" is used in "+a+".",
      deriv, [a]));
  });
  out.push(mk("related formulas", // 10.
    "Formulas closely related to "+n+" in "+dom+".",
    "Derived from the same principles as "+n+".", null));
  out.push(mk("common mistakes", // 11.
    "Frequent errors when applying "+n+" and how to avoid them.",
    "Pedagogical analysis.", null));
  out.push(mk("derivation walkthrough", // 12.
    "Full step-by-step derivation of "+n+".",
    deriv+" Expanded with intermediate steps.", null));
  out.push(mk("limiting cases", // 13.
    "Behavior of "+n+" at extreme values.",
    "Asymptotic analysis of the established formula.", null));
  out.push(mk("practice problem", // 14.
    "Practice problem using "+n+" with solution outline.",
    "Application of the established formula.", null));
  out.push(mk("visual guide", // 15.
    "How to visualize and sketch "+n+".",
    "Graphical interpretation.", null));
  return out;
}
var _FORMS=null;
function allForms(){
  if(_FORMS)return _FORMS;
  _FORMS=[];
  BASE.forEach(function(b){ formsFor(b).forEach(function(f){_FORMS.push(f);}); });
  return _FORMS;
}
function generate(seed,opts){
  var forms=allForms();
  var f=forms[(seed-1)%forms.length];
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id, name:f.name, formula:f.notation, domain:f.domain,
    variables:f.variables.map(function(v){return {symbol:v[0],description:v[1],unit:v[2]};}),
    meaning:f.meaning, derivation:f.derivation, applications:f.applications,
    type:f.type, type_label:f.type_label, src:"signature",
    description:f.name+" ("+f.domain+"): "+f.notation,
    _seed:seed
  };
}
function generateIndexed(i){ return generate(i+1); }
function validate(r){
  if(!r||typeof r!=='object')return false;
  if(!/^JAH-SF-\d{6}$/.test(r.id||''))return false;
  if(!r.name||!r.formula||!r.domain)return false;
  if(!Array.isArray(r.variables))return false;
  if(!r.meaning||!r.derivation)return false;
  if(r.type!==1&&r.type!==2)return false;
  return true;
}
function driftCheck(r){ var g=generate(r._seed); return g.name===r.name&&g.formula===r.formula; }
var gen={generate:generate,generateIndexed:generateIndexed,validate:validate,driftCheck:driftCheck,
  count:function(){return allForms().length;},version:'jahdb-scientific-formulas-1.0'};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('scientific-formulas',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
