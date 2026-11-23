// Seeded boundless generator for the The Signature Classical Mechanics Database ("signature" edition).
// Deterministic: the same seed always emits the same record.
// Usage: node gen-college-classical-mechanics-signature.js [seed]  (prints one JSON record)
// or: node gen-college-classical-mechanics-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "college-classical-mechanics-signature";
const RECORD_KIND = "classical mechanics record";
const ID_PREFIX = "JAH-CCLMECHS-";
const AI_NAME = "JAH Classical Mechanics Librarian (Signature)";
const EDITION = "signature";
const SRC = "signature-generated";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI — not stored files.";

const TOPICS = [
  {
    "title": "Signature Design: The Motion Tracker",
    "subject": "a Signature motion tracker design",
    "description": "The Motion Tracker is a Signature-made design for teaching kinematics: a tracker where a learner films a moving object, and the tool plots its position, velocity, and acceleration against time, with the graphs linked so a slope on one is a value on the next. Velocity is the slope of the position graph. The position, velocity, and acceleration graphs are shown together. The slope of the position graph is the velocity; the slope of the velocity graph is the acceleration. The area under the velocity graph is the distance travelled.",
    "inputs": "FIGURES = {'max_height': 22.4, 'time_to_top': 2.04, 'total_time': 4.18, 'acceleration': -9.8, 'graphs': 3, 'initial_speed': 20, 'net_change': -2, 'design_version': 1}\nLABEL = 'a-signature-motion-tracker-design'\n",
    "expected": "count: 8\nlabel: a-signature-motion-tracker-design\nmax: 22.4\nmean: 5.1025\nmin: -9.8\ntotal: 40.82\nResult: count=8|label=a-signature-motion-tracker-design|max=22.4|mean=5.1025|min=-9.8|total=40.82\nRun 1 SHA-256: cc470f64eba532c0f0195f3565b15fbc8255d26ab89676e8e3047fdc2c675f24\nRun 2 SHA-256: cc470f64eba532c0f0195f3565b15fbc8255d26ab89676e8e3047fdc2c675f24\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Force Table",
    "subject": "a Signature force table design",
    "description": "The Force Table is a Signature-made design for teaching Newton's laws: a table where a learner places forces as arrows on a body, and the tool shows the net force, the acceleration, and the motion that follows. The net force divided by the mass is the acceleration. Forces are drawn as arrows, and the net force is shown. The acceleration follows from F = m a, and the motion is animated. The third-law pair is shown: every push has its equal opposite.",
    "inputs": "FIGURES = {'mass_kg': 2, 'force_N': 10, 'acceleration': 5, 'speed_after': 15, 'distance_m': 22.5, 'normal_force_N': 19.6, 'laws': 3, 'design_version': 1}\nLABEL = 'a-signature-force-table-design'\n",
    "expected": "count: 8\nlabel: a-signature-force-table-design\nmax: 22.5\nmean: 9.7625\nmin: 1\ntotal: 78.1\nResult: count=8|label=a-signature-force-table-design|max=22.5|mean=9.7625|min=1|total=78.1\nRun 1 SHA-256: 7a30c381181f34ce652176c3db587a0f2f6dd0042b6b635061ae45db499eff3e\nRun 2 SHA-256: 7a30c381181f34ce652176c3db587a0f2f6dd0042b6b635061ae45db499eff3e\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Energy Accountant",
    "subject": "a Signature energy accountant design",
    "description": "The Energy Accountant is a Signature-made design for teaching work and energy: an accountant where a learner tracks energy as it moves between kinetic, potential, and heat, with the books always balancing. Energy is never created or destroyed, only moved. Each form of energy is a column, and the total is shown balancing. Work done on the system adds a column; friction moves energy to heat. The power is shown as the rate of energy flow.",
    "inputs": "FIGURES = {'mass_kg': 2, 'height_m': 10, 'energy_J': 196, 'speed_ms': 14, 'power_W': 98, 'columns': 3, 'total_constant': 196, 'design_version': 1}\nLABEL = 'a-signature-energy-accountant-design'\n",
    "expected": "count: 8\nlabel: a-signature-energy-accountant-design\nmax: 196\nmean: 65.0\nmin: 1\ntotal: 520\nResult: count=8|label=a-signature-energy-accountant-design|max=196|mean=65.0|min=1|total=520\nRun 1 SHA-256: 3317922eb339ce7b8cee2c2bc4beafe1fb4a88f6203068cb8e2a66d3e72f7281\nRun 2 SHA-256: 3317922eb339ce7b8cee2c2bc4beafe1fb4a88f6203068cb8e2a66d3e72f7281\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Collision Lab",
    "subject": "a Signature collision laboratory design",
    "description": "The Collision Lab is a Signature-made design for teaching momentum: a laboratory where a learner collides carts, and the tool shows the momentum before and after, the kinetic energy, and what is lost. Momentum is conserved; kinetic energy is conserved only in elastic collisions. The momentum of each cart is shown before and after. The total momentum is shown conserved in every collision. The kinetic energy is shown, and the loss in an inelastic collision is named.",
    "inputs": "FIGURES = {'mass_A': 2, 'speed_A': 3, 'mass_B': 3, 'total_momentum': 6, 'combined_speed': 1.2, 'energy_before': 9, 'energy_after': 3.6, 'energy_lost': 5.4}\nLABEL = 'a-signature-collision-laboratory-design'\n",
    "expected": "count: 8\nlabel: a-signature-collision-laboratory-design\nmax: 9\nmean: 4.15\nmin: 1.2\ntotal: 33.2\nResult: count=8|label=a-signature-collision-laboratory-design|max=9|mean=4.15|min=1.2|total=33.2\nRun 1 SHA-256: 5df8357b4b3be0634732a5c34a1644c0455e79d50c9c1de7be4ef197667f880b\nRun 2 SHA-256: 5df8357b4b3be0634732a5c34a1644c0455e79d50c9c1de7be4ef197667f880b\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Spinning Wheel Bench",
    "subject": "a Signature spinning wheel bench design",
    "description": "The Spinning Wheel Bench is a Signature-made design for teaching rotation: a bench where a learner applies a torque to a wheel, and the tool shows the angular acceleration, the spin rate, and the angular momentum. Torque is force times lever arm. The torque is set, and the angular acceleration follows from tau = I alpha. The spin rate and the angle are shown growing with time. Pulling mass inward is shown doubling the spin rate by conservation of angular momentum.",
    "inputs": "FIGURES = {'moment_of_inertia': 0.5, 'torque_Nm': 2, 'angular_acceleration': 4, 'angular_velocity': 12, 'rpm': 115, 'time_s': 3, 'spin_factor': 2, 'design_version': 1}\nLABEL = 'a-signature-spinning-wheel-bench-design'\n",
    "expected": "count: 8\nlabel: a-signature-spinning-wheel-bench-design\nmax: 115\nmean: 17.4375\nmin: 0.5\ntotal: 139.5\nResult: count=8|label=a-signature-spinning-wheel-bench-design|max=115|mean=17.4375|min=0.5|total=139.5\nRun 1 SHA-256: 8c52d0ab927c5e41a66541c0cca4a5497e1313d263218295c63fa766a0c2ce7c\nRun 2 SHA-256: 8c52d0ab927c5e41a66541c0cca4a5497e1313d263218295c63fa766a0c2ce7c\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Orbit Plotter",
    "subject": "a Signature orbit plotter design",
    "description": "The Orbit Plotter is a Signature-made design for teaching gravitation: a plotter where a learner sets a planet's distance, and the tool draws its orbit, gives its period from Kepler's third law, and shows the speed. The period squared is proportional to the distance cubed. The orbit is drawn as an ellipse with the Sun at a focus. The period follows from Kepler's third law. The speed at each point is shown, fastest at perigee.",
    "inputs": "FIGURES = {'mars_au': 1.524, 'mars_period_years': 1.88, 'leo_speed_kms': 7.7, 'leo_period_min': 92, 'leo_altitude_km': 400, 'orbits_drawn': 2, 'laws': 3, 'design_version': 1}\nLABEL = 'a-signature-orbit-plotter-design'\n",
    "expected": "count: 8\nlabel: a-signature-orbit-plotter-design\nmax: 400\nmean: 63.638\nmin: 1\ntotal: 509.104\nResult: count=8|label=a-signature-orbit-plotter-design|max=400|mean=63.638|min=1|total=509.104\nRun 1 SHA-256: 0ccfe5a5405539c83a10e726abc654f764ab0b06fc35d028e3bfb403b7fbec01\nRun 2 SHA-256: 0ccfe5a5405539c83a10e726abc654f764ab0b06fc35d028e3bfb403b7fbec01\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Oscillator Tuner",
    "subject": "a Signature oscillator tuner design",
    "description": "The Oscillator Tuner is a Signature-made design for teaching oscillations: a tuner where a learner sets the mass and the spring stiffness, and the tool shows the frequency, the period, and the motion, with resonance when the drive matches. The frequency depends on stiffness and mass, not amplitude. The mass and stiffness are set on sliders, and the frequency updates. The motion is drawn as a sine wave with the set frequency. Driving at the natural frequency is shown growing the amplitude.",
    "inputs": "FIGURES = {'mass_kg': 0.5, 'stiffness': 20, 'omega': 6.32, 'frequency_Hz': 1.01, 'period_s': 0.99, 'pendulum_period': 2.01, 'resonance_Hz': 1.01, 'design_version': 1}\nLABEL = 'a-signature-oscillator-tuner-design'\n",
    "expected": "count: 8\nlabel: a-signature-oscillator-tuner-design\nmax: 20\nmean: 4.105\nmin: 0.5\ntotal: 32.84\nResult: count=8|label=a-signature-oscillator-tuner-design|max=20|mean=4.105|min=0.5|total=32.84\nRun 1 SHA-256: 12de010f95a86602e9e6c04fe4be96ec97e70611417bffd17cc963d809855015\nRun 2 SHA-256: 12de010f95a86602e9e6c04fe4be96ec97e70611417bffd17cc963d809855015\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Wave Tank",
    "subject": "a Signature wave tank design",
    "description": "The Wave Tank is a Signature-made design for teaching waves: a tank where a learner sends waves, watches them travel, reflect, and interfere, and sees standing waves form. Wave speed is frequency times wavelength. Waves are sent with a chosen frequency, and their wavelength is shown. Reflection and interference are drawn. Standing waves are shown with nodes and antinodes marked.",
    "inputs": "FIGURES = {'sound_speed': 343, 'frequency_Hz': 440, 'wavelength_m': 0.78, 'string_length': 1, 'wave_speed': 200, 'fundamental_Hz': 100, 'harmonics': 4, 'nodes_per_wavelength': 2}\nLABEL = 'a-signature-wave-tank-design'\n",
    "expected": "count: 8\nlabel: a-signature-wave-tank-design\nmax: 440\nmean: 136.3475\nmin: 0.78\ntotal: 1090.78\nResult: count=8|label=a-signature-wave-tank-design|max=440|mean=136.3475|min=0.78|total=1090.78\nRun 1 SHA-256: 2f17448cc855da16a6a764857242e4738935074972869a8f7d436be59e79b981\nRun 2 SHA-256: 2f17448cc855da16a6a764857242e4738935074972869a8f7d436be59e79b981\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Lagrangian Workbench",
    "subject": "a Signature Lagrangian workbench design",
    "description": "The Lagrangian Workbench is a Signature-made design for teaching Lagrangian mechanics: a workbench where a learner writes the kinetic and potential energies, and the tool forms the Lagrangian and derives the equations of motion. The Lagrangian is kinetic minus potential energy. The kinetic and potential energies are entered, and L = T - V is formed. The Euler-Lagrange equation is applied step by step. The result is checked against Newton's laws on the same problem.",
    "inputs": "FIGURES = {'length_m': 1, 'mass_kg': 1, 'g_acceleration': 9.8, 'period_s': 2.01, 'equations': 1, 'checks': 1, 'coordinates': 1, 'design_version': 1}\nLABEL = 'a-signature-lagrangian-workbench-design'\n",
    "expected": "count: 8\nlabel: a-signature-lagrangian-workbench-design\nmax: 9.8\nmean: 2.2263\nmin: 1\ntotal: 17.81\nResult: count=8|label=a-signature-lagrangian-workbench-design|max=9.8|mean=2.2263|min=1|total=17.81\nRun 1 SHA-256: dab41b5114d032a8fb2614f53266bffdeb2bed7875279913968e7716c3bf4d8d\nRun 2 SHA-256: dab41b5114d032a8fb2614f53266bffdeb2bed7875279913968e7716c3bf4d8d\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Phase Space Viewer",
    "subject": "a Signature phase space viewer design",
    "description": "The Phase Space Viewer is a Signature-made design for teaching Hamiltonian mechanics: a viewer where a learner watches a point move through phase space (position against momentum), with the energy contours drawn and the area conserved. The Hamiltonian is the total energy. The phase space is drawn with the energy contours. The point moves along a contour, with the area conserved. Hamilton's equations are shown as the flow field.",
    "inputs": "FIGURES = {'mass_kg': 1, 'stiffness': 1, 'energy': 2, 'phase_radius': 2, 'phase_area': 12.566, 'equations': 2, 'dimensions': 2, 'design_version': 1}\nLABEL = 'a-signature-phase-space-viewer-design'\n",
    "expected": "count: 8\nlabel: a-signature-phase-space-viewer-design\nmax: 12.566\nmean: 2.9458\nmin: 1\ntotal: 23.566\nResult: count=8|label=a-signature-phase-space-viewer-design|max=12.566|mean=2.9458|min=1|total=23.566\nRun 1 SHA-256: 650d55242f6c4af873d96194cb5d3cd360ec0e1c38378316f3dd3ff861d3c8a0\nRun 2 SHA-256: 650d55242f6c4af873d96194cb5d3cd360ec0e1c38378316f3dd3ff861d3c8a0\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Tumbling Book Demo",
    "subject": "a Signature tumbling book demonstration design",
    "description": "The Tumbling Book Demo is a Signature-made design for teaching rigid-body rotation: a demonstration where a learner tosses a book spinning about each of its three principal axes, and watches the middle-axis spin flip while the other two stay steady. Rotation about the middle axis is unstable. The book is tossed about each principal axis in turn. The middle-axis toss is shown flipping; the other two are steady. Euler's equations are shown explaining the flip.",
    "inputs": "FIGURES = {'moments': 3, 'principal_axes': 3, 'unstable_axis': 2, 'stable_axes': 2, 'flips': 1, 'steady': 2, 'moment_1': 1, 'moment_3': 3}\nLABEL = 'a-signature-tumbling-book-demonstration-design'\n",
    "expected": "count: 8\nlabel: a-signature-tumbling-book-demonstration-design\nmax: 3\nmean: 2.125\nmin: 1\ntotal: 17\nResult: count=8|label=a-signature-tumbling-book-demonstration-design|max=3|mean=2.125|min=1|total=17\nRun 1 SHA-256: 3eaedcf7cd9d7bd5eca4d99d88a5da999df32723080632723b128c7d52375ee0\nRun 2 SHA-256: 3eaedcf7cd9d7bd5eca4d99d88a5da999df32723080632723b128c7d52375ee0\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Transfer Orbit Planner",
    "subject": "a Signature transfer orbit planner design",
    "description": "The Transfer Orbit Planner is a Signature-made design for teaching orbital transfers: a planner where a learner picks two orbits, and the tool draws the Hohmann ellipse between them, gives the two burns, and the transfer time. The Hohmann transfer is the lowest-energy route between two circular orbits. The two orbits are drawn, and the transfer ellipse touches both. The two burns are computed from the vis-viva equation. The transfer time is half the ellipse period.",
    "inputs": "FIGURES = {'radius_1_km': 7000, 'radius_2_km': 14000, 'semi_major_km': 10500, 'speed_1_kms': 7.5, 'perigee_speed_kms': 8.7, 'apogee_speed_kms': 4.4, 'circular_speed_2_kms': 5.3, 'transfer_hours': 1.5, 'design_version': 1}\nLABEL = 'a-signature-transfer-orbit-planner-design'\n",
    "expected": "count: 9\nlabel: a-signature-transfer-orbit-planner-design\nmax: 14000\nmean: 3503.1556\nmin: 1\ntotal: 31528.4\nResult: count=9|label=a-signature-transfer-orbit-planner-design|max=14000|mean=3503.1556|min=1|total=31528.4\nRun 1 SHA-256: 2a7c5e91a6101db3e5d89e0f4b5cc342fd7714d1e64315fc09b403ace62ea305\nRun 2 SHA-256: 2a7c5e91a6101db3e5d89e0f4b5cc342fd7714d1e64315fc09b403ace62ea305\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Rotating Frame Simulator",
    "subject": "a Signature rotating frame simulator design",
    "description": "The Rotating Frame Simulator is a Signature-made design for teaching fictitious forces: a simulator where a learner stands on a rotating platform, throws a ball, and watches it curve in the rotating frame while going straight in the inertial frame. The Coriolis force bends moving bodies sideways. The ball is shown in both frames at once: straight in the inertial frame, curved in the rotating frame. The centrifugal and Coriolis forces are shown as arrows. Foucault's pendulum is shown precessing at the learner's latitude.",
    "inputs": "FIGURES = {'omega': 7.27e-05, 'centrifugal_acc': 0.034, 'gravity_fraction': 0.0035, 'latitude_deg': 40, 'precession_rate': 4.67e-05, 'precession_hours': 37, 'frames': 2, 'design_version': 1}\nLABEL = 'a-signature-rotating-frame-simulator-design'\n",
    "expected": "count: 8\nlabel: a-signature-rotating-frame-simulator-design\nmax: 40\nmean: 10.0047\nmin: 4.67e-05\ntotal: 80.0376\nResult: count=8|label=a-signature-rotating-frame-simulator-design|max=40|mean=10.0047|min=4.67e-05|total=80.0376\nRun 1 SHA-256: ba69cf9eff9efa61d41ca6d6c9c6051df4e3c19bd4e2365ee2cbacda0f32693d\nRun 2 SHA-256: ba69cf9eff9efa61d41ca6d6c9c6051df4e3c19bd4e2365ee2cbacda0f32693d\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Pipe Flow Bench",
    "subject": "a Signature pipe flow bench design",
    "description": "The Pipe Flow Bench is a Signature-made design for teaching fluid mechanics: a bench where a learner narrows a pipe, and the tool shows the speed rising by continuity and the pressure falling by Bernoulli. Continuity says the volume flow is constant; Bernoulli says the pressure falls as the speed rises. The pipe diameter is set, and the speed follows from continuity. The pressure follows from Bernoulli's equation. A ship's displacement is shown balancing its weight by Archimedes' principle.",
    "inputs": "FIGURES = {'pipe_diameter_1': 10, 'pipe_diameter_2': 5, 'speed_1': 1, 'speed_2': 4, 'pressure_drop_Pa': 7500, 'ship_displacement_t': 10000, 'buoyant_force_MN': 98, 'design_version': 1}\nLABEL = 'a-signature-pipe-flow-bench-design'\n",
    "expected": "count: 8\nlabel: a-signature-pipe-flow-bench-design\nmax: 10000\nmean: 2202.375\nmin: 1\ntotal: 17619\nResult: count=8|label=a-signature-pipe-flow-bench-design|max=10000|mean=2202.375|min=1|total=17619\nRun 1 SHA-256: dacaaafed83ff1516ea045cec3babc394f8fe818a559a8145979d7a612af63a3\nRun 2 SHA-256: dacaaafed83ff1516ea045cec3babc394f8fe818a559a8145979d7a612af63a3\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Beam Bender",
    "subject": "a Signature beam bender design",
    "description": "The Beam Bender is a Signature-made design for teaching elasticity: a bender where a learner loads a beam, and the tool shows the stress, the strain, and the deflection, with the deflection growing with the cube of the length. Stress is force per area; strain is fractional deformation. The load is set, and the stress is shown. The strain follows from Young's modulus. The deflection is shown, growing with the cube of the span.",
    "inputs": "FIGURES = {'rod_length_m': 2, 'cross_section_cm2': 1, 'force_N': 20000, 'stress_MPa': 200, 'youngs_GPa': 200, 'strain': 0.001, 'stretch_mm': 2, 'deflection_factor': 8}\nLABEL = 'a-signature-beam-bender-design'\n",
    "expected": "count: 8\nlabel: a-signature-beam-bender-design\nmax: 20000\nmean: 2551.6251\nmin: 0.001\ntotal: 20413.001\nResult: count=8|label=a-signature-beam-bender-design|max=20000|mean=2551.6251|min=0.001|total=20413.001\nRun 1 SHA-256: 9abc2d97bd6642a56cfc80fb71951c7b4772a9dfe76beb757e130ee7b75985e4\nRun 2 SHA-256: 9abc2d97bd6642a56cfc80fb71951c7b4772a9dfe76beb757e130ee7b75985e4\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Chaos Butterfly",
    "subject": "a Signature chaos butterfly design",
    "description": "The Chaos Butterfly is a Signature-made design for teaching chaos: a butterfly where a learner starts a double pendulum twice with nearly the same angle, and watches the two motions separate exponentially. Chaos is deterministic but unpredictable in practice. Two pendulums are started with angles differing by 0.001 radians. The separation is shown growing exponentially. The Lyapunov exponent is shown, and the predictability horizon is computed.",
    "inputs": "FIGURES = {'angle_difference': 0.001, 'lyapunov': 0.5, 'separation_10s': 0.148, 'separation_20s': 22, 'lorenz_lambda': 0.9, 'weather_horizon_days': 14, 'pendulums': 2, 'design_version': 1}\nLABEL = 'a-signature-chaos-butterfly-design'\n",
    "expected": "count: 8\nlabel: a-signature-chaos-butterfly-design\nmax: 22\nmean: 5.0686\nmin: 0.001\ntotal: 40.549\nResult: count=8|label=a-signature-chaos-butterfly-design|max=22|mean=5.0686|min=0.001|total=40.549\nRun 1 SHA-256: 4d25e7a644643e664d61cafcf90235110cbb5feaefc6ce9610ee791cdec62f90\nRun 2 SHA-256: 4d25e7a644643e664d61cafcf90235110cbb5feaefc6ce9610ee791cdec62f90\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Light Clock",
    "subject": "a Signature light clock design",
    "description": "The Light Clock is a Signature-made design for teaching special relativity: a clock where a learner watches a light pulse bounce between two mirrors, and sees the pulse take a longer path when the clock moves, so the moving clock ticks slower. Time dilation follows from the constancy of the speed of light. The light pulse is shown bouncing between the mirrors. The moving clock's path is longer, so it ticks slower by gamma. The length contraction is shown alongside.",
    "inputs": "FIGURES = {'speed_fraction': 0.6, 'gamma': 1.25, 'ship_time_s': 10, 'earth_time_s': 12.5, 'ship_length_m': 100, 'observed_length_m': 80, 'kinetic_fraction': 0.25, 'newtonian_fraction': 0.18}\nLABEL = 'a-signature-light-clock-design'\n",
    "expected": "count: 8\nlabel: a-signature-light-clock-design\nmax: 100\nmean: 25.5975\nmin: 0.18\ntotal: 204.78\nResult: count=8|label=a-signature-light-clock-design|max=100|mean=25.5975|min=0.18|total=204.78\nRun 1 SHA-256: f938503f57fb0f2f3beea3708eeb88f79a1b2de7e7b04b7cc7c3980950e1fd06\nRun 2 SHA-256: f938503f57fb0f2f3beea3708eeb88f79a1b2de7e7b04b7cc7c3980950e1fd06\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Lagrange Point Finder",
    "subject": "a Signature Lagrange point finder design",
    "description": "The Lagrange Point Finder is a Signature-made design for teaching the three-body problem: a finder where a learner places two large masses, and the tool finds the five Lagrange points where a small body can orbit with them. The L4 and L5 points form equilateral triangles. The two masses are placed, and the five points are drawn. L1, L2, L3 lie on the line; L4 and L5 form equilateral triangles. The James Webb Space Telescope is shown at L2.",
    "inputs": "FIGURES = {'l1_distance_km': 1500000, 'l2_distance_km': 1500000, 'lagrange_points': 5, 'trojan_groups': 2, 'bodies': 3, 'special_solutions': 2, 'jwst_location': 2, 'design_version': 1}\nLABEL = 'a-signature-lagrange-point-finder-design'\n",
    "expected": "count: 8\nlabel: a-signature-lagrange-point-finder-design\nmax: 1500000\nmean: 375001.875\nmin: 1\ntotal: 3000015\nResult: count=8|label=a-signature-lagrange-point-finder-design|max=1500000|mean=375001.875|min=1|total=3000015\nRun 1 SHA-256: e9ae1d9bb8b2f633f6c0605b0cd89cd60c5a6f3b6f7b3510f14fb41c09465112\nRun 2 SHA-256: e9ae1d9bb8b2f633f6c0605b0cd89cd60c5a6f3b6f7b3510f14fb41c09465112\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Suspension Tuner",
    "subject": "a Signature suspension tuner design",
    "description": "The Suspension Tuner is a Signature-made design for teaching damped oscillations: a tuner where a learner sets the mass, spring, and damping of a suspension, and the tool shows the decay, the critical damping, and the response to a bump. Critical damping returns to equilibrium fastest without oscillating. The mass, stiffness, and damping are set on sliders. The decay is shown, with the half-life computed. Critical damping is marked, and the response to a bump is animated.",
    "inputs": "FIGURES = {'mass_kg': 1, 'stiffness': 100, 'omega': 10, 'period_s': 0.63, 'damping_b': 2, 'decay_rate': 1, 'half_life_s': 0.69, 'critical_damping': 20}\nLABEL = 'a-signature-suspension-tuner-design'\n",
    "expected": "count: 8\nlabel: a-signature-suspension-tuner-design\nmax: 100\nmean: 16.915\nmin: 0.63\ntotal: 135.32\nResult: count=8|label=a-signature-suspension-tuner-design|max=100|mean=16.915|min=0.63|total=135.32\nRun 1 SHA-256: f6f5069beeb090fc54b797142c17418c07d345643332819d38e9889f81b88c53\nRun 2 SHA-256: f6f5069beeb090fc54b797142c17418c07d345643332819d38e9889f81b88c53\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Pendulum Amplitude Meter",
    "subject": "a Signature pendulum amplitude meter design",
    "description": "The Pendulum Amplitude Meter is a Signature-made design for teaching the nonlinear pendulum: a meter where a learner releases a pendulum from a chosen angle, and the tool shows the period growing with the amplitude, against the small-angle value. The exact period is an elliptic integral. The release angle is set, and the period is shown. The small-angle period is shown as the reference. The correction factor is shown growing with the angle.",
    "inputs": "FIGURES = {'length_m': 1, 'small_period_s': 2.007, 'amplitude_60_deg': 60, 'factor_60': 1.0685, 'period_60_s': 2.144, 'factor_170': 2.44, 'period_170_s': 4.9, 'design_version': 1}\nLABEL = 'a-signature-pendulum-amplitude-meter-design'\n",
    "expected": "count: 8\nlabel: a-signature-pendulum-amplitude-meter-design\nmax: 60\nmean: 9.3199\nmin: 1\ntotal: 74.5595\nResult: count=8|label=a-signature-pendulum-amplitude-meter-design|max=60|mean=9.3199|min=1|total=74.5595\nRun 1 SHA-256: ffdb2bab4fae72ee804ecb633f7a847d8265e89d786eb4aa76e3b149fa99f302\nRun 2 SHA-256: ffdb2bab4fae72ee804ecb633f7a847d8265e89d786eb4aa76e3b149fa99f302\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Symmetry Board",
    "subject": "a Signature symmetry board design",
    "description": "The Symmetry Board is a Signature-made design for teaching Noether's theorem: a board where a learner switches symmetries on and off, and the tool shows which quantities are conserved. Every continuous symmetry gives a conserved quantity. Time, space, and rotation symmetries are switches. Switching a symmetry on shows its conserved quantity. A central force is shown with its angular momentum conserved.",
    "inputs": "FIGURES = {'symmetries': 3, 'conserved_quantities': 3, 'components': 3, 'theorem_year': 1918, 'kepler_law': 2, 'energy_conserved': 1, 'momentum_conserved': 1, 'angular_conserved': 1}\nLABEL = 'a-signature-symmetry-board-design'\n",
    "expected": "count: 8\nlabel: a-signature-symmetry-board-design\nmax: 1918\nmean: 241.5\nmin: 1\ntotal: 1932\nResult: count=8|label=a-signature-symmetry-board-design|max=1918|mean=241.5|min=1|total=1932\nRun 1 SHA-256: 5610f51bd86b0686540c70a5f123a8ebcbeb15cca0a8e4db30b81664bde6b12a\nRun 2 SHA-256: 5610f51bd86b0686540c70a5f123a8ebcbeb15cca0a8e4db30b81664bde6b12a\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Least Action Path Finder",
    "subject": "a Signature least action path finder design",
    "description": "The Least Action Path Finder is a Signature-made design for teaching the principle of least action: a finder where a learner draws candidate paths, and the tool computes the action of each, showing the true path as the one with stationary action. The action is the integral of the Lagrangian over time. Candidate paths are drawn, and the action of each is computed. The true path is marked as the stationary one. The brachistochrone (fastest slide) is shown as a cycloid.",
    "inputs": "FIGURES = {'brachistochrone_year': 1696, 'least_time_year': 1662, 'lagrange_year': 1788, 'paths_compared': 3, 'principles': 2, 'equations': 1, 'cycloid': 1, 'design_version': 1}\nLABEL = 'a-signature-least-action-path-finder-design'\n",
    "expected": "count: 8\nlabel: a-signature-least-action-path-finder-design\nmax: 1788\nmean: 644.25\nmin: 1\ntotal: 5154\nResult: count=8|label=a-signature-least-action-path-finder-design|max=1788|mean=644.25|min=1|total=5154\nRun 1 SHA-256: c267c375ed3eea6c97a05ff73c887a5ec8150e54020ec6c53f736261c737ea2b\nRun 2 SHA-256: c267c375ed3eea6c97a05ff73c887a5ec8150e54020ec6c53f736261c737ea2b\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Normal Mode Harp",
    "subject": "a Signature normal mode harp design",
    "description": "The Normal Mode Harp is a Signature-made design for teaching coupled oscillators: a harp where a learner plucks coupled masses, and the tool shows the motion as a sum of normal modes, with the beating pattern as energy swaps between the masses. Any motion is a sum of the modes. The masses are plucked, and the motion is shown. The two normal modes are shown separately, with their frequencies. The beating pattern is shown as the motion swaps between the masses.",
    "inputs": "FIGURES = {'masses': 2, 'springs': 3, 'omega_1': 3.16, 'omega_2': 5.48, 'k_stiffness': 10, 'mass_kg': 1, 'beat_period_s': 2.71, 'modes': 2}\nLABEL = 'a-signature-normal-mode-harp-design'\n",
    "expected": "count: 8\nlabel: a-signature-normal-mode-harp-design\nmax: 10\nmean: 3.6688\nmin: 1\ntotal: 29.35\nResult: count=8|label=a-signature-normal-mode-harp-design|max=10|mean=3.6688|min=1|total=29.35\nRun 1 SHA-256: c1fb3f44b89c84486fcd4d76359019b40a5c92b3d1ae9a65a775d2571b1d4742\nRun 2 SHA-256: c1fb3f44b89c84486fcd4d76359019b40a5c92b3d1ae9a65a775d2571b1d4742\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Mechanics Capstone Console",
    "subject": "a Signature mechanics capstone console design",
    "description": "The Mechanics Capstone Console is a Signature-made design for teaching end-to-end mechanics: a console where a learner plans a Mars mission by choosing the tools, computing the numbers, and checking each step, with the plan, the checks, and the assembly scored. A capstone problem uses several tools at once. The console plans the tools: escape speed, transfer, landing. Each part is computed and checked separately. The assembly is scored as a whole argument, with the answer stated with its checks.",
    "inputs": "FIGURES = {'escape_speed_kms': 11.2, 'transfer_days': 259, 'semi_major_axis_au': 1.262, 'transfer_period_years': 1.42, 'arrival_vinf_kms': 2.6, 'entry_speed_kms': 5.7, 'parts': 3, 'design_version': 1}\nLABEL = 'a-signature-mechanics-capstone-console-design'\n",
    "expected": "count: 8\nlabel: a-signature-mechanics-capstone-console-design\nmax: 259\nmean: 35.6478\nmin: 1\ntotal: 285.182\nResult: count=8|label=a-signature-mechanics-capstone-console-design|max=259|mean=35.6478|min=1|total=285.182\nRun 1 SHA-256: 1865ab9899718e8bbaa5576efacafbc941ba39de1fe11930c24fadb85a41713a\nRun 2 SHA-256: 1865ab9899718e8bbaa5576efacafbc941ba39de1fe11930c24fadb85a41713a\nDeterministic: MATCH\n"
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Mechanics",
    "url": "https://en.wikipedia.org/wiki/Mechanics",
    "establishes": "The reference for a Signature motion tracker design in this record."
  },
  {
    "name": "Wikipedia - Classical mechanics",
    "url": "https://en.wikipedia.org/wiki/Classical_mechanics",
    "establishes": "The reference for a Signature motion tracker design in this record."
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
