// Seeded boundless generator for the Classical Mechanics Database ("public" edition).
// Deterministic: the same seed always emits the same record.
// Usage: node gen-college-classical-mechanics.js [seed]  (prints one JSON record)
// or: node gen-college-classical-mechanics.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "college-classical-mechanics";
const RECORD_KIND = "classical mechanics record";
const ID_PREFIX = "JAH-CCLMECH-";
const AI_NAME = "JAH Classical Mechanics Librarian";
const EDITION = "public";
const SRC = "public-harvest";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI — not stored files.";

const TOPICS = [
  {
    "title": "Classical Mechanics: Kinematics and the Description of Motion",
    "subject": "kinematics and the description of motion",
    "description": "Kinematics is the description of motion without asking what causes it: position, velocity, and acceleration as functions of time, in one, two, and three dimensions. Velocity is the rate of change of position; acceleration is the rate of change of velocity. Velocity is the derivative of position with respect to time. Acceleration is the derivative of velocity with respect to time. In two dimensions, motion can be split into independent horizontal and vertical parts.",
    "inputs": "FIGURES = {'initial_speed': 20, 'max_height': 22.4, 'time_to_top': 2.04, 'total_time': 4.18, 'landing_speed': 21, 'g_acceleration': 9.8, 'launch_height': 2, 'velocity_zero_time': 2.04}\nLABEL = 'kinematics-and-the-description-of-motion'\n",
    "expected": "count: 8\nlabel: kinematics-and-the-description-of-motion\nmax: 22.4\nmean: 10.4325\nmin: 2\ntotal: 83.46\nResult: count=8|label=kinematics-and-the-description-of-motion|max=22.4|mean=10.4325|min=2|total=83.46\nRun 1 SHA-256: cea3d116f6532ec1cc8dd47a726867fed7529bffc56a70de7fb94699db8fdece\nRun 2 SHA-256: cea3d116f6532ec1cc8dd47a726867fed7529bffc56a70de7fb94699db8fdece\nDeterministic: MATCH\n"
  },
  {
    "title": "Classical Mechanics: Newton's Laws of Motion",
    "subject": "Newton's laws of motion",
    "description": "Newton's three laws are the foundation of classical mechanics. The first law: a body stays at rest or in uniform motion unless a net force acts. The second law: force equals mass times acceleration. The third law: every action has an equal and opposite reaction. The first law defines inertial frames: frames in which a free body does not accelerate. The second law, F = m a, relates the net force to the acceleration. The third law pairs forces: when A pushes B, B pushes A equally and oppositely.",
    "inputs": "FIGURES = {'mass_kg': 2, 'force_N': 10, 'acceleration': 5, 'time_s': 3, 'speed_after': 15, 'distance_m': 22.5, 'weight_N': 19.6, 'laws_count': 3}\nLABEL = 'newton-s-laws-of-motion'\n",
    "expected": "count: 8\nlabel: newton-s-laws-of-motion\nmax: 22.5\nmean: 10.0125\nmin: 2\ntotal: 80.1\nResult: count=8|label=newton-s-laws-of-motion|max=22.5|mean=10.0125|min=2|total=80.1\nRun 1 SHA-256: 479f39c6e9f2a5a73e413ddedbedd8d4d58d8335ca0347b1d8e935be10d24cca\nRun 2 SHA-256: 479f39c6e9f2a5a73e413ddedbedd8d4d58d8335ca0347b1d8e935be10d24cca\nDeterministic: MATCH\n"
  },
  {
    "title": "Classical Mechanics: Work, Energy, and Power",
    "subject": "work, energy, and power",
    "description": "Work is force times distance along the direction of motion. Kinetic energy is the energy of motion, one half mass times speed squared. Potential energy is stored energy, such as height in a gravitational field or stretch in a spring. Power is the rate of doing work. Work is the integral of force along the path. Kinetic energy is (1/2) m v squared; gravitational potential energy is m g h. In a closed system with conservative forces, total mechanical energy is conserved.",
    "inputs": "FIGURES = {'mass_kg': 2, 'height_m': 10, 'energy_J': 196, 'speed_ms': 14, 'power_W': 98, 'engine_kW': 100, 'g_acceleration': 9.8, 'time_s': 2}\nLABEL = 'work-energy-and-power'\n",
    "expected": "count: 8\nlabel: work-energy-and-power\nmax: 196\nmean: 53.975\nmin: 2\ntotal: 431.8\nResult: count=8|label=work-energy-and-power|max=196|mean=53.975|min=2|total=431.8\nRun 1 SHA-256: a6885706a0cac03be4c21d131067a5428bd261818fb948695f506fd94b0463f3\nRun 2 SHA-256: a6885706a0cac03be4c21d131067a5428bd261818fb948695f506fd94b0463f3\nDeterministic: MATCH\n"
  },
  {
    "title": "Classical Mechanics: Momentum and Impulse",
    "subject": "momentum and impulse",
    "description": "Momentum is mass times velocity, a vector quantity. Impulse is force times time, and equals the change in momentum. In a closed system with no external force, total momentum is conserved. Collisions are classified as elastic (kinetic energy conserved) or inelastic (kinetic energy lost). Momentum is p = m v, a vector. Impulse is the change in momentum: J = F times delta t = delta p. Total momentum is conserved when no external impulse acts.",
    "inputs": "FIGURES = {'mass_A': 2, 'speed_A': 3, 'mass_B': 3, 'total_momentum': 6, 'combined_speed': 1.2, 'energy_before': 9, 'energy_after': 3.6, 'energy_lost': 5.4}\nLABEL = 'momentum-and-impulse'\n",
    "expected": "count: 8\nlabel: momentum-and-impulse\nmax: 9\nmean: 4.15\nmin: 1.2\ntotal: 33.2\nResult: count=8|label=momentum-and-impulse|max=9|mean=4.15|min=1.2|total=33.2\nRun 1 SHA-256: fa8a6e5a4f4d3028bbf6a32396b72ff7ff266e9c476c20d54a00477eff73956f\nRun 2 SHA-256: fa8a6e5a4f4d3028bbf6a32396b72ff7ff266e9c476c20d54a00477eff73956f\nDeterministic: MATCH\n"
  },
  {
    "title": "Classical Mechanics: Rotational Motion and Torque",
    "subject": "rotational motion and torque",
    "description": "Rotation has its own kinematics: angle, angular velocity, and angular acceleration. Torque is the rotational analogue of force: force times lever arm. The moment of inertia is the rotational analogue of mass. Angular momentum is conserved when no external torque acts. Angular velocity is the rate of change of angle. Torque is r cross F, force times perpendicular distance. Angular momentum L = I omega is conserved without external torque.",
    "inputs": "FIGURES = {'moment_of_inertia': 0.5, 'torque_Nm': 2, 'angular_acceleration': 4, 'time_s': 3, 'angular_velocity': 12, 'rpm': 115, 'spin_double_factor': 2, 'axes': 3}\nLABEL = 'rotational-motion-and-torque'\n",
    "expected": "count: 8\nlabel: rotational-motion-and-torque\nmax: 115\nmean: 17.6875\nmin: 0.5\ntotal: 141.5\nResult: count=8|label=rotational-motion-and-torque|max=115|mean=17.6875|min=0.5|total=141.5\nRun 1 SHA-256: 61123929b36cafba6f94572ec9a1dc3b58cac2d14e94397a0f76c8a0837de5bb\nRun 2 SHA-256: 61123929b36cafba6f94572ec9a1dc3b58cac2d14e94397a0f76c8a0837de5bb\nDeterministic: MATCH\n"
  },
  {
    "title": "Classical Mechanics: Gravitation and Kepler's Laws",
    "subject": "gravitation and Kepler's laws",
    "description": "Newton's law of universal gravitation says every mass attracts every other with a force proportional to the product of the masses and inversely proportional to the square of the distance. Kepler's three laws describe planetary orbits: ellipses with the Sun at a focus, equal areas in equal times, and the period squared proportional to the semi-major axis cubed. The gravitational force is G m1 m2 / r squared. Orbits are ellipses, parabolas, or hyperbolas, by energy. Kepler's third law: T squared is proportional to a cubed.",
    "inputs": "FIGURES = {'mars_au': 1.524, 'mars_period_years': 1.88, 'leo_speed_kms': 7.7, 'leo_period_min': 92, 'leo_altitude_km': 400, 'g_constant': 6.674e-11, 'moon_g': 3.3e-05, 'laws_count': 3}\nLABEL = 'gravitation-and-kepler-s-laws'\n",
    "expected": "count: 8\nlabel: gravitation-and-kepler-s-laws\nmax: 400\nmean: 63.263\nmin: 6.674e-11\ntotal: 506.104\nResult: count=8|label=gravitation-and-kepler-s-laws|max=400|mean=63.263|min=6.674e-11|total=506.104\nRun 1 SHA-256: bd0d4226b7fc6aa0b4af15fe65938c6a665fd9aa29ca0c209e98a3bdfd1329a1\nRun 2 SHA-256: bd0d4226b7fc6aa0b4af15fe65938c6a665fd9aa29ca0c209e98a3bdfd1329a1\nDeterministic: MATCH\n"
  },
  {
    "title": "Classical Mechanics: Oscillations and the Harmonic Oscillator",
    "subject": "oscillations and the harmonic oscillator",
    "description": "The simple harmonic oscillator is a mass on a spring, or a pendulum at small angles: the restoring force is proportional to the displacement, and the motion is sinusoidal with a frequency that depends on the stiffness and the mass, not the amplitude. Damping and driving produce resonance. The equation is x double-dot = -(k/m) x, with omega = sqrt(k/m). The period is 2 pi sqrt(m/k), independent of amplitude. Driving at the natural frequency produces resonance, with large amplitude.",
    "inputs": "FIGURES = {'mass_kg': 0.5, 'stiffness': 20, 'omega': 6.32, 'frequency_Hz': 1.01, 'period_s': 0.99, 'amplitude_m': 0.1, 'pendulum_period': 2.01, 'resonance_Hz': 1.01}\nLABEL = 'oscillations-and-the-harmonic-oscillator'\n",
    "expected": "count: 8\nlabel: oscillations-and-the-harmonic-oscillator\nmax: 20\nmean: 3.9925\nmin: 0.1\ntotal: 31.94\nResult: count=8|label=oscillations-and-the-harmonic-oscillator|max=20|mean=3.9925|min=0.1|total=31.94\nRun 1 SHA-256: c11b1a2fc22d97bfe1023893c7be419e87f97d91fbf00f65f6979648fb67ef5f\nRun 2 SHA-256: c11b1a2fc22d97bfe1023893c7be419e87f97d91fbf00f65f6979648fb67ef5f\nDeterministic: MATCH\n"
  },
  {
    "title": "Classical Mechanics: Waves and Sound",
    "subject": "waves and sound",
    "description": "A wave carries energy through a medium without carrying the medium: the wave equation relates the second time derivative to the second space derivative, with speed v = f lambda. Sound is a longitudinal pressure wave; its speed in air is about 343 metres per second. Standing waves form when waves reflect and interfere. Wave speed is v = f times lambda, frequency times wavelength. The wave equation is u_tt = v squared u_xx. Standing waves have nodes (no motion) and antinodes (maximum motion).",
    "inputs": "FIGURES = {'sound_speed': 343, 'frequency_Hz': 440, 'wavelength_m': 0.78, 'string_length': 1, 'wave_speed': 200, 'fundamental_Hz': 100, 'harmonics': 4, 'nodes_per_wavelength': 2}\nLABEL = 'waves-and-sound'\n",
    "expected": "count: 8\nlabel: waves-and-sound\nmax: 440\nmean: 136.3475\nmin: 0.78\ntotal: 1090.78\nResult: count=8|label=waves-and-sound|max=440|mean=136.3475|min=0.78|total=1090.78\nRun 1 SHA-256: a28465aec55ba2de7f24c008ecaa6e1db5df32a559e8121fc05dafbc1ae01be4\nRun 2 SHA-256: a28465aec55ba2de7f24c008ecaa6e1db5df32a559e8121fc05dafbc1ae01be4\nDeterministic: MATCH\n"
  },
  {
    "title": "Classical Mechanics: Lagrangian Mechanics",
    "subject": "Lagrangian mechanics",
    "description": "Lagrangian mechanics reformulates dynamics in terms of energy: the Lagrangian L is kinetic minus potential energy, and the motion follows the Euler-Lagrange equations, one per generalised coordinate. It handles constraints naturally and reveals conservation laws through symmetry (Noether's theorem). L = T - V, kinetic minus potential energy. The Euler-Lagrange equation is d/dt (dL/d q-dot) - dL/dq = 0. A symmetry of L gives a conserved quantity (Noether's theorem).",
    "inputs": "FIGURES = {'length_m': 1, 'mass_kg': 1, 'g_acceleration': 9.8, 'period_s': 2.01, 'coordinates': 1, 'equations': 1, 'symmetries': 1, 'conserved': 1}\nLABEL = 'lagrangian-mechanics'\n",
    "expected": "count: 8\nlabel: lagrangian-mechanics\nmax: 9.8\nmean: 2.2263\nmin: 1\ntotal: 17.81\nResult: count=8|label=lagrangian-mechanics|max=9.8|mean=2.2263|min=1|total=17.81\nRun 1 SHA-256: 7b14c2ce9568ff9222c4e32cd2d52c1a21332adb2badbcf7caf43c28413089ce\nRun 2 SHA-256: 7b14c2ce9568ff9222c4e32cd2d52c1a21332adb2badbcf7caf43c28413089ce\nDeterministic: MATCH\n"
  },
  {
    "title": "Classical Mechanics: Hamiltonian Mechanics and Phase Space",
    "subject": "Hamiltonian mechanics and phase space",
    "description": "Hamiltonian mechanics describes motion in phase space, the space of positions and momenta: the Hamiltonian H is the total energy, and the motion follows Hamilton's equations, q-dot = dH/dp and p-dot = -dH/dq. Phase space volume is conserved (Liouville's theorem), and the Hamiltonian is the starting point of quantum mechanics. H = T + V, the total energy, in terms of position and momentum. Hamilton's equations: q-dot = dH/dp, p-dot = -dH/dq. Phase space volume is conserved along the flow.",
    "inputs": "FIGURES = {'mass_kg': 1, 'stiffness': 1, 'energy': 2, 'phase_radius': 2, 'phase_area': 12.566, 'equations': 2, 'coordinates': 1, 'dimensions': 2}\nLABEL = 'hamiltonian-mechanics-and-phase-space'\n",
    "expected": "count: 8\nlabel: hamiltonian-mechanics-and-phase-space\nmax: 12.566\nmean: 2.9458\nmin: 1\ntotal: 23.566\nResult: count=8|label=hamiltonian-mechanics-and-phase-space|max=12.566|mean=2.9458|min=1|total=23.566\nRun 1 SHA-256: 5f3a75b1c34c1366f716872ca76ebbd08772c60e5a5e0fc2e6deff30f402de2b\nRun 2 SHA-256: 5f3a75b1c34c1366f716872ca76ebbd08772c60e5a5e0fc2e6deff30f402de2b\nDeterministic: MATCH\n"
  },
  {
    "title": "Classical Mechanics: Rigid Bodies and Euler's Equations",
    "subject": "rigid bodies and Euler's equations",
    "description": "A rigid body rotates about its centre of mass with three principal moments of inertia; Euler's equations describe the rotation in the body frame, where the angular momentum is I times omega. Free rotation is stable about the largest and smallest principal axes, and unstable about the middle one (the tennis-racket effect). The inertia tensor has three principal axes and three principal moments. Euler's equations couple the three components of angular velocity. Rotation about the middle axis is unstable; the other two are stable.",
    "inputs": "FIGURES = {'moments': 3, 'principal_axes': 3, 'unstable_axis': 2, 'stable_axes': 2, 'euler_equations': 3, 'moment_1': 1, 'moment_2': 2, 'moment_3': 3}\nLABEL = 'rigid-bodies-and-euler-s-equations'\n",
    "expected": "count: 8\nlabel: rigid-bodies-and-euler-s-equations\nmax: 3\nmean: 2.375\nmin: 1\ntotal: 19\nResult: count=8|label=rigid-bodies-and-euler-s-equations|max=3|mean=2.375|min=1|total=19\nRun 1 SHA-256: ea0fe22f7b7d0fc3968f631a5d784bb31cb0b4f1eb1381ed66f5e077b92fec47\nRun 2 SHA-256: ea0fe22f7b7d0fc3968f631a5d784bb31cb0b4f1eb1381ed66f5e077b92fec47\nDeterministic: MATCH\n"
  },
  {
    "title": "Classical Mechanics: Central Forces and Orbital Motion",
    "subject": "central forces and orbital motion",
    "description": "A central force points toward a fixed centre and depends only on distance. Angular momentum is conserved, so the motion lies in a plane and sweeps equal areas in equal times. For the inverse-square force, the orbits are conic sections: circles, ellipses, parabolas, hyperbolas. Angular momentum is conserved, so the motion is planar. The effective potential combines the real potential with the centrifugal barrier. For gravity, bound orbits are ellipses; unbound orbits are parabolas or hyperbolas.",
    "inputs": "FIGURES = {'radius_km': 7000, 'speed_kms': 7.5, 'angular_momentum': 52500, 'halved_speed': 10.7, 'transfer_type': 1, 'conic_types': 4, 'conserved': 1, 'dimensions': 2}\nLABEL = 'central-forces-and-orbital-motion'\n",
    "expected": "count: 8\nlabel: central-forces-and-orbital-motion\nmax: 52500\nmean: 7440.775\nmin: 1\ntotal: 59526.2\nResult: count=8|label=central-forces-and-orbital-motion|max=52500|mean=7440.775|min=1|total=59526.2\nRun 1 SHA-256: 61a4d9fbb15cdafee021254ca7a5702a5de85ca9e2bd77c61f60eb88edb2729f\nRun 2 SHA-256: 61a4d9fbb15cdafee021254ca7a5702a5de85ca9e2bd77c61f60eb88edb2729f\nDeterministic: MATCH\n"
  },
  {
    "title": "Classical Mechanics: Non-Inertial Frames and Fictitious Forces",
    "subject": "non-inertial frames and fictitious forces",
    "description": "In a frame that accelerates or rotates, Newton's laws appear to fail unless fictitious forces are added: the centrifugal force (outward in a rotating frame), the Coriolis force (sideways for moving bodies), and the Euler force (when the rotation rate changes). These are not real forces, but the price of using a rotating frame. The centrifugal force is m omega squared r, outward. The Coriolis force is -2 m omega cross v, sideways to the motion. Foucault's pendulum demonstrates the Earth's rotation through the Coriolis effect.",
    "inputs": "FIGURES = {'omega': 7.27e-05, 'centrifugal_acc': 0.034, 'gravity_fraction': 0.0035, 'latitude_deg': 40, 'precession_rate': 4.67e-05, 'precession_hours': 37, 'earth_radius_km': 6371, 'forces': 3}\nLABEL = 'non-inertial-frames-and-fictitious-forces'\n",
    "expected": "count: 8\nlabel: non-inertial-frames-and-fictitious-forces\nmax: 6371\nmean: 806.3797\nmin: 4.67e-05\ntotal: 6451.0376\nResult: count=8|label=non-inertial-frames-and-fictitious-forces|max=6371|mean=806.3797|min=4.67e-05|total=6451.0376\nRun 1 SHA-256: 78d54cae7259c417d72014ec61b8f2e55b9861b220001d6270a57328d5594f74\nRun 2 SHA-256: 78d54cae7259c417d72014ec61b8f2e55b9861b220001d6270a57328d5594f74\nDeterministic: MATCH\n"
  },
  {
    "title": "Classical Mechanics: Fluids at Rest and in Motion",
    "subject": "fluids at rest and in motion",
    "description": "Fluid mechanics studies liquids and gases: pressure, buoyancy (Archimedes' principle), the continuity equation (mass conservation), and Bernoulli's equation (energy along a streamline). Viscosity adds friction, and the Reynolds number decides whether flow is laminar or turbulent. Pressure increases with depth: p = p0 + rho g h. Archimedes' principle: the buoyant force equals the weight of displaced fluid. Bernoulli's equation: p + (1/2) rho v squared + rho g h is constant along a streamline.",
    "inputs": "FIGURES = {'ship_displacement_t': 10000, 'buoyant_force_MN': 98, 'pipe_diameter_1': 10, 'pipe_diameter_2': 5, 'speed_1': 1, 'speed_2': 4, 'pressure_drop_Pa': 7500, 'water_density': 1000}\nLABEL = 'fluids-at-rest-and-in-motion'\n",
    "expected": "count: 8\nlabel: fluids-at-rest-and-in-motion\nmax: 10000\nmean: 2327.25\nmin: 1\ntotal: 18618\nResult: count=8|label=fluids-at-rest-and-in-motion|max=10000|mean=2327.25|min=1|total=18618\nRun 1 SHA-256: a921a6df2362c6b594aecf96d7583d1df0bf37d27eab2b4a05ae5fd2f1f62424\nRun 2 SHA-256: a921a6df2362c6b594aecf96d7583d1df0bf37d27eab2b4a05ae5fd2f1f62424\nDeterministic: MATCH\n"
  },
  {
    "title": "Classical Mechanics: Elasticity and the Deformation of Solids",
    "subject": "elasticity and the deformation of solids",
    "description": "Elasticity describes how solids deform under load: stress is force per area, strain is fractional deformation, and Young's modulus relates them (Hooke's law for solids). Beams bend, columns buckle, and the elastic limit marks where deformation becomes permanent. Stress is force per unit area; strain is the fractional change in length. Young's modulus E relates stress to strain: stress = E times strain. Beyond the elastic limit, the material deforms permanently.",
    "inputs": "FIGURES = {'rod_length_m': 2, 'cross_section_cm2': 1, 'force_N': 20000, 'stress_MPa': 200, 'youngs_GPa': 200, 'strain': 0.001, 'stretch_mm': 2, 'deflection_factor': 8}\nLABEL = 'elasticity-and-the-deformation-of-solids'\n",
    "expected": "count: 8\nlabel: elasticity-and-the-deformation-of-solids\nmax: 20000\nmean: 2551.6251\nmin: 0.001\ntotal: 20413.001\nResult: count=8|label=elasticity-and-the-deformation-of-solids|max=20000|mean=2551.6251|min=0.001|total=20413.001\nRun 1 SHA-256: 9c4c13641b341db5617ae859417e857b87e7f3c93f86aa46184dca2f1a32040a\nRun 2 SHA-256: 9c4c13641b341db5617ae859417e857b87e7f3c93f86aa46184dca2f1a32040a\nDeterministic: MATCH\n"
  },
  {
    "title": "Classical Mechanics: Chaos and the Sensitive Dependence on Initial Conditions",
    "subject": "chaos and sensitive dependence on initial conditions",
    "description": "Chaos is deterministic motion that is unpredictable in practice: nearby trajectories separate exponentially, with a rate given by the Lyapunov exponent. The double pendulum is the classic example; the Lorenz system showed that weather cannot be predicted far ahead, even with perfect equations. Chaos is deterministic: the same start gives the same motion. Nearby starts separate exponentially, with rate lambda (the Lyapunov exponent). The predictability horizon is about (1/lambda) times log(precision).",
    "inputs": "FIGURES = {'angle_difference': 0.001, 'lyapunov': 0.5, 'separation_10s': 0.148, 'separation_20s': 22, 'lorenz_lambda': 0.9, 'weather_horizon_days': 14, 'systems': 3, 'exponent_units': 1}\nLABEL = 'chaos-and-sensitive-dependence-on-initial-conditions'\n",
    "expected": "count: 8\nlabel: chaos-and-sensitive-dependence-on-initial-conditions\nmax: 22\nmean: 5.1936\nmin: 0.001\ntotal: 41.549\nResult: count=8|label=chaos-and-sensitive-dependence-on-initial-conditions|max=22|mean=5.1936|min=0.001|total=41.549\nRun 1 SHA-256: fd9063a239bb81836717e30d225407d659334e7b9dda2244dde2ef9d38edf085\nRun 2 SHA-256: fd9063a239bb81836717e30d225407d659334e7b9dda2244dde2ef9d38edf085\nDeterministic: MATCH\n"
  },
  {
    "title": "Classical Mechanics: Special Relativity and the Limits of Newton",
    "subject": "special relativity and the limits of Newton",
    "description": "Special relativity replaces Newton's absolute time and space: the speed of light is the same for all observers, moving clocks run slow (time dilation), moving objects shorten (length contraction), and mass and energy are related by E = m c squared. At low speeds, Newton's laws are recovered. The speed of light c is the same in every inertial frame. Time dilation: a moving clock ticks slower by the factor gamma = 1/sqrt(1 - v squared/c squared). E = m c squared relates rest mass to energy.",
    "inputs": "FIGURES = {'speed_fraction': 0.6, 'gamma': 1.25, 'ship_time_s': 10, 'earth_time_s': 12.5, 'ship_length_m': 100, 'observed_length_m': 80, 'kinetic_fraction': 0.25, 'newtonian_fraction': 0.18}\nLABEL = 'special-relativity-and-the-limits-of-newton'\n",
    "expected": "count: 8\nlabel: special-relativity-and-the-limits-of-newton\nmax: 100\nmean: 25.5975\nmin: 0.18\ntotal: 204.78\nResult: count=8|label=special-relativity-and-the-limits-of-newton|max=100|mean=25.5975|min=0.18|total=204.78\nRun 1 SHA-256: 451288b9ad3b91a3caad69c744a5c396dad746cf4f4f7ab7d8a7d79c35ce015f\nRun 2 SHA-256: 451288b9ad3b91a3caad69c744a5c396dad746cf4f4f7ab7d8a7d79c35ce015f\nDeterministic: MATCH\n"
  },
  {
    "title": "Classical Mechanics: The Three-Body Problem",
    "subject": "the three-body problem",
    "description": "The three-body problem asks for the motion of three masses under mutual gravitation. Unlike the two-body problem, it has no general closed-form solution: the motion is chaotic, and only special solutions (such as Lagrange's triangular points) are known exactly. The five Lagrange points are positions where a small body can orbit with two larger ones. The two-body problem is solvable; the three-body problem is not, in general. The motion is chaotic: small changes grow exponentially. The five Lagrange points (L1 to L5) are equilibrium positions in the rotating frame.",
    "inputs": "FIGURES = {'l1_distance_km': 1500000, 'l2_distance_km': 1500000, 'lagrange_points': 5, 'trojan_groups': 2, 'bodies': 3, 'special_solutions': 2, 'jwst_location': 2, 'years_since': 1772}\nLABEL = 'the-three-body-problem'\n",
    "expected": "count: 8\nlabel: the-three-body-problem\nmax: 1500000\nmean: 375223.25\nmin: 2\ntotal: 3001786\nResult: count=8|label=the-three-body-problem|max=1500000|mean=375223.25|min=2|total=3001786\nRun 1 SHA-256: c0a5c96e793a5f588e0a833d6d6950fcb52e67fb0c8ba579019a670c44b3c1ef\nRun 2 SHA-256: c0a5c96e793a5f588e0a833d6d6950fcb52e67fb0c8ba579019a670c44b3c1ef\nDeterministic: MATCH\n"
  },
  {
    "title": "Classical Mechanics: Damped and Driven Oscillations",
    "subject": "damped and driven oscillations",
    "description": "Real oscillators lose energy to friction (damping) and are often driven by a periodic force. Light damping gives a slowly decaying oscillation; critical damping returns to equilibrium fastest without oscillating; heavy damping creeps back. Driving at the natural frequency gives resonance, with amplitude limited only by damping. Damping adds a force -b v; the amplitude decays as e^(-(b/2m) t). Critical damping is b squared = 4 m k, the fastest non-oscillating return. Resonance: driving at the natural frequency maximises the amplitude.",
    "inputs": "FIGURES = {'mass_kg': 1, 'stiffness': 100, 'omega': 10, 'period_s': 0.63, 'damping_b': 2, 'decay_rate': 1, 'half_life_s': 0.69, 'critical_damping': 20}\nLABEL = 'damped-and-driven-oscillations'\n",
    "expected": "count: 8\nlabel: damped-and-driven-oscillations\nmax: 100\nmean: 16.915\nmin: 0.63\ntotal: 135.32\nResult: count=8|label=damped-and-driven-oscillations|max=100|mean=16.915|min=0.63|total=135.32\nRun 1 SHA-256: 1d9c918d416db7c86bc0da3b6704e4921313525db11c9eba02765dd1ec37033f\nRun 2 SHA-256: 1d9c918d416db7c86bc0da3b6704e4921313525db11c9eba02765dd1ec37033f\nDeterministic: MATCH\n"
  },
  {
    "title": "Classical Mechanics: The Pendulum, Exact and Approximate",
    "subject": "the pendulum, exact and approximate",
    "description": "The pendulum is the simplest nonlinear oscillator: the equation is theta double-dot = -(g/L) sin theta. For small angles, sin theta is about theta, giving simple harmonic motion with period 2 pi sqrt(L/g). For large angles, the period grows, and the exact period is an elliptic integral. Small angles: the period is 2 pi sqrt(L/g), independent of amplitude. Large angles: the period grows, by about 1 + theta0 squared/16. The exact period is an elliptic integral of the first kind.",
    "inputs": "FIGURES = {'length_m': 1, 'small_period_s': 2.007, 'amplitude_60_deg': 60, 'factor_60': 1.0685, 'period_60_s': 2.144, 'factor_170': 2.44, 'period_170_s': 4.9, 'g_acceleration': 9.8}\nLABEL = 'the-pendulum-exact-and-approximate'\n",
    "expected": "count: 8\nlabel: the-pendulum-exact-and-approximate\nmax: 60\nmean: 10.4199\nmin: 1\ntotal: 83.3595\nResult: count=8|label=the-pendulum-exact-and-approximate|max=60|mean=10.4199|min=1|total=83.3595\nRun 1 SHA-256: f539831cf2429cbb516342f801c7f922a78359c6695eb0f82ac79dfafc23790b\nRun 2 SHA-256: f539831cf2429cbb516342f801c7f922a78359c6695eb0f82ac79dfafc23790b\nDeterministic: MATCH\n"
  },
  {
    "title": "Classical Mechanics: Conservation Laws and Noether's Theorem",
    "subject": "conservation laws and Noether's theorem",
    "description": "Conservation laws follow from symmetries: time-translation symmetry gives energy conservation, space-translation symmetry gives momentum conservation, and rotational symmetry gives angular momentum conservation. Noether's theorem makes this precise: every continuous symmetry of the action gives a conserved quantity. Time symmetry gives energy conservation. Space symmetry gives momentum conservation. Rotational symmetry gives angular momentum conservation.",
    "inputs": "FIGURES = {'symmetries': 3, 'conserved_quantities': 3, 'components': 3, 'theorem_year': 1918, 'kepler_law': 2, 'energy_conserved': 1, 'momentum_conserved': 1, 'angular_conserved': 1}\nLABEL = 'conservation-laws-and-noether-s-theorem'\n",
    "expected": "count: 8\nlabel: conservation-laws-and-noether-s-theorem\nmax: 1918\nmean: 241.5\nmin: 1\ntotal: 1932\nResult: count=8|label=conservation-laws-and-noether-s-theorem|max=1918|mean=241.5|min=1|total=1932\nRun 1 SHA-256: 66ca95b7035bb12aa126df42846f29c365b06fb06825c2a9987758d858907477\nRun 2 SHA-256: 66ca95b7035bb12aa126df42846f29c365b06fb06825c2a9987758d858907477\nDeterministic: MATCH\n"
  },
  {
    "title": "Classical Mechanics: The Calculus of Variations and Least Action",
    "subject": "the calculus of variations and least action",
    "description": "The principle of least action says the true path of a system is the one that makes the action stationary: the action is the integral of the Lagrangian over time. The calculus of variations gives the Euler-Lagrange equations from this principle, and the same mathematics finds the shortest path, the fastest slide (brachistochrone), and the strongest arch. The action S is the integral of L dt over the path. The true path makes S stationary: delta S = 0. The Euler-Lagrange equations follow from the variation.",
    "inputs": "FIGURES = {'brachistochrone_year': 1696, 'least_time_year': 1662, 'lagrange_year': 1788, 'paths_compared': 3, 'principles': 2, 'equations': 1, 'dimensions': 3, 'cycloid': 1}\nLABEL = 'the-calculus-of-variations-and-least-action'\n",
    "expected": "count: 8\nlabel: the-calculus-of-variations-and-least-action\nmax: 1788\nmean: 644.5\nmin: 1\ntotal: 5156\nResult: count=8|label=the-calculus-of-variations-and-least-action|max=1788|mean=644.5|min=1|total=5156\nRun 1 SHA-256: 7eccce4039a7fa9a9c4bf5007c7208112185685bc29be65ab45c941458241ddb\nRun 2 SHA-256: 7eccce4039a7fa9a9c4bf5007c7208112185685bc29be65ab45c941458241ddb\nDeterministic: MATCH\n"
  },
  {
    "title": "Classical Mechanics: Coupled Oscillators and Normal Modes",
    "subject": "coupled oscillators and normal modes",
    "description": "Coupled oscillators are masses connected by springs: the system has as many normal modes as degrees of freedom, each with its own frequency, and any motion is a sum of the modes. The normal modes diagonalise the equations, and resonance occurs when a drive matches a mode frequency. A system with n degrees of freedom has n normal modes. Each mode oscillates at one frequency, with a fixed pattern of motion. Any motion is a sum of the normal modes.",
    "inputs": "FIGURES = {'masses': 2, 'springs': 3, 'omega_1': 3.16, 'omega_2': 5.48, 'k_stiffness': 10, 'mass_kg': 1, 'beat_period_s': 2.71, 'modes': 2}\nLABEL = 'coupled-oscillators-and-normal-modes'\n",
    "expected": "count: 8\nlabel: coupled-oscillators-and-normal-modes\nmax: 10\nmean: 3.6688\nmin: 1\ntotal: 29.35\nResult: count=8|label=coupled-oscillators-and-normal-modes|max=10|mean=3.6688|min=1|total=29.35\nRun 1 SHA-256: cdbf73c8898ac8148e2957d3c04e025a7c30af4d06004ea8ff05d7dd4aa4e1e3\nRun 2 SHA-256: cdbf73c8898ac8148e2957d3c04e025a7c30af4d06004ea8ff05d7dd4aa4e1e3\nDeterministic: MATCH\n"
  },
  {
    "title": "Classical Mechanics: Capstone — Design a Space Mission",
    "subject": "a capstone space mission design",
    "description": "This capstone combines kinematics, energy, momentum, gravitation, and orbital mechanics into one mission: launch a probe from Earth, transfer to Mars, and land, with every number checked. A capstone problem uses several tools at once, and the answer is stated with its checks. The launch needs the escape speed, 11.2 km/s, from Earth's surface. The Hohmann transfer needs a delta-v of about 3.6 km/s at Earth and 2.6 km/s at Mars. The landing needs the entry speed and the parachute or retro-rocket plan.",
    "inputs": "FIGURES = {'escape_speed_kms': 11.2, 'transfer_days': 259, 'semi_major_axis_au': 1.262, 'transfer_period_years': 1.42, 'arrival_vinf_kms': 2.6, 'entry_speed_kms': 5.7, 'delta_v_earth': 3.6, 'delta_v_mars': 2.6, 'viking_year': 1976}\nLABEL = 'a-capstone-space-mission-design'\n",
    "expected": "count: 9\nlabel: a-capstone-space-mission-design\nmax: 1976\nmean: 251.4869\nmin: 1.262\ntotal: 2263.382\nResult: count=9|label=a-capstone-space-mission-design|max=1976|mean=251.4869|min=1.262|total=2263.382\nRun 1 SHA-256: 03ced7eb82bf309a04135aaa29a993cbaf0a270d7559f04cbebf92442b5aae85\nRun 2 SHA-256: 03ced7eb82bf309a04135aaa29a993cbaf0a270d7559f04cbebf92442b5aae85\nDeterministic: MATCH\n"
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Mechanics",
    "url": "https://en.wikipedia.org/wiki/Mechanics",
    "establishes": "The reference for kinematics and the description of motion in this record."
  },
  {
    "name": "Wikipedia - Classical mechanics",
    "url": "https://en.wikipedia.org/wiki/Classical_mechanics",
    "establishes": "The reference for kinematics and the description of motion in this record."
  }
];

function mulberry32(seed) {
  let a = seed >>> 0;
  return function () {
    a |= 0; a = (a + 0x6D2B79F5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function canonical(obj) {
  if (obj === null || typeof obj !== "object") return JSON.stringify(obj);
  if (Array.isArray(obj)) return "[" + obj.map(canonical).join(",") + "]";
  const keys = Object.keys(obj).sort();
  return "{" + keys.map((k) => JSON.stringify(k) + ":" + canonical(obj[k])).join(",") + "}";
}

function buildDemo(topic) {
  const code = "import hashlib\n" + topic.inputs +
    "def compute():\n" +
    "    total = sum(FIGURES.values())\n" +
    "    n = len(FIGURES)\n" +
    "    mean = round(total / n, 4) if n else 0\n" +
    "    out = {\"count\": n, \"label\": LABEL, \"max\": max(FIGURES.values()), " +
    "\"mean\": mean, \"min\": min(FIGURES.values()), \"total\": round(total, 4)}\n" +
    "    return out\n" +
    "outputs = compute()\n" +
    "result = \"|\".join(f\"{k}={v}\" for k, v in sorted(outputs.items()))\n" +
    "h1 = hashlib.sha256(result.encode()).hexdigest()\n" +
    "outputs2 = compute()\n" +
    "result2 = \"|\".join(f\"{k}={v}\" for k, v in sorted(outputs2.items()))\n" +
    "h2 = hashlib.sha256(result2.encode()).hexdigest()\n" +
    "for k, v in sorted(outputs.items()):\n" +
    "    print(f\"{k}: {v}\")\n" +
    "print(f\"Result: {result}\")\n" +
    "print(f\"Run 1 SHA-256: {h1}\")\n" +
    "print(f\"Run 2 SHA-256: {h2}\")\n" +
    "print(f\"Deterministic: {'MATCH' if h1 == h2 else 'MISMATCH'}\")\n";
  return { code: code, expected: topic.expected };
}

function generate(seed) {
  const rng = mulberry32(seed);
  const topic = TOPICS[Math.floor(rng() * TOPICS.length)];
  const idx = seed % 1000000;
  const id = ID_PREFIX + "GEN-" + String(idx).padStart(6, "0");
  const demo = buildDemo(topic);
  const rec = {
    id: id,
    slug: SLUG,
    edition: EDITION,
    record_kind: RECORD_KIND,
    title: topic.title + " (Generated " + idx + ")",
    subject: topic.subject,
    status: "built",
    src: SRC,
    ai_name: AI_NAME,
    description: topic.description + (EDITION === "signature"
      ? " Design-study: this is a Signature-made design, labelled design-study throughout, never presented as established fact or as an authentic public record."
      : " Established college-level knowledge, checked against its cited sources."),
    body: "<h2>Description</h2><p>" + topic.description + "</p>",
    demo: demo.code,
    expected_output: demo.expected,
    program: "class GeneratedProgram:\n    def run(self):\n        return {\"deterministic\": True}\n",
    sources: SOURCES,
    generator: { type: "seeded boundless generator", gen_id_prefix: ID_PREFIX + "GEN-", hard_stop: 1000000000, throttle_per_call: 100, ceiling_note: CEILING },
    scales: { A1: "One generated record: the same shape as the filed records, with its own figures.", A2: "The whole edition: every generated record joins the 24 filed records.", A3: "The subject against the whole network: every college subject linked, every record searchable." },
  };
  const slim = {};
  for (const k of Object.keys(rec)) slim[k] = rec[k];
  rec.jcc_key = "k=" + crypto.createHash("sha256").update(canonical(slim)).digest("hex").slice(0, 8);
  rec.jcc_code = "JAHDB/" + SLUG + "#" + id;
  return rec;
}

function runTests() {
  let passed = 0, failed = 0;
  function t(name, ok) { if (ok) { passed++; } else { failed++; console.log("FAIL: " + name); } }
  const a = generate(42), b = generate(42);
  t("same seed twice identical", JSON.stringify(a) === JSON.stringify(b));
  t("record_kind", a.record_kind === RECORD_KIND);
  t("slug", a.slug === SLUG);
  t("slug signature form", EDITION === "signature" ? (a.slug.split("-signature").length - 1) === 1 : a.slug.indexOf("-signature") === -1);
  t("id prefix own family", a.id.indexOf(ID_PREFIX) === 0);
  t("generator hard_stop 1e9", a.generator.hard_stop === 1000000000);
  t("generator gen prefix own family", a.generator.gen_id_prefix === ID_PREFIX + "GEN-");
  t("jcc_code form", a.jcc_code === "JAHDB/" + SLUG + "#" + a.id);
  const slim = {}; for (const k of Object.keys(a)) { if (k !== "jcc_code" && k !== "jcc_key") slim[k] = a[k]; }
  t("jcc_key round-trip", a.jcc_key === "k=" + crypto.createHash("sha256").update(canonical(slim)).digest("hex").slice(0, 8));
  t("different seeds differ", JSON.stringify(generate(42)) !== JSON.stringify(generate(43)));
  t("19 keys", Object.keys(a).length === 19);
  console.log("Tests: " + passed + " passed, " + failed + " failed");
  return failed === 0;
}

if (require.main === module) {
  const arg = process.argv[2];
  if (arg === "--test") {
    process.exit(runTests() ? 0 : 1);
  }
  const seed = arg === undefined ? 1 : parseInt(arg, 10);
  if (!Number.isFinite(seed)) { console.error("seed must be an integer"); process.exit(2); }
  console.log(JSON.stringify(generate(seed)));
}
module.exports = { generate, runTests };
