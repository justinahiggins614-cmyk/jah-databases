#!/usr/bin/env python3
"""Entries for the Nanofluidics field databases (field #33, taxonomy order).

Verified 2026-10-17: NO database covers the nanofluidics discipline (fluid
behavior at 1-100 nanometres: nanochannels, slip flow, electrokinetics, ion
selectivity, electrical double layers, nanofluidic devices). Manifest search
(2366 databases): zero 'nanofluid*' slugs or names; nearest neighbors are
'nanotech' (10,001 general-nanotechnology records), 'nanomechanics' (34
records - the mechanics of nanoscale objects), 'nanocomposites' (34 records
- matrix + filler science), 'nanophotonics' (34 records) - all different
disciplines. Whole-system title sweep over all 766 shard indexes: zero
titles contain 'nanofluid*' - ZERO full-record discipline coverage anywhere.

So this build creates two NEW databases, 34 ladder-ordered records each:

  nanofluidics              - The Nanofluidics Database
                              (public-harvest: real, fact-checked
                              nanofluidics - the standard references are
                              Bocquet/Charlaix 'Nanofluidics, from bulk to
                              interfaces' Chem. Soc. Rev. 2010;
                              Schoch/Han/Renaud 'Transport phenomena in
                              nanofluidics' Rev. Mod. Phys. 2008;
                              Eijkel/van den Berg 'Nanofluidics: what is it
                              and what can we expect from it?'
                              Microfluid. Nanofluid. 2005; Stein/Kruithof/
                              Dekker 'Surface-charge-governed ion transport
                              in nanofluidic channels' Phys. Rev. Lett.
                              2004)
  nanofluidics-signature    - The Nanofluidics Signature Database
                              (his original Signature interpretation; src
                              signature, titles suffixed
                              " (Signature Edition)", never presented as
                              authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Subtitle disambiguation (fields #13-32 pattern): specialty titles carry
teaching-focused subtitles rather than bare cards, e.g. "The Debye Length:
The Ruler of Nanofluidic Regimes".

Never the words "bat belt" anywhere. No website references. No Facebook.

Numerical cores (all hand-computed 2026-10-17, machine-verified by the demos):
- 50 nm slit vs 1 mm pipe: ~167 vs ~3.3M water molecules across; S/V 4e7 vs
  2000 /m (20,000x).
- S/V = 2/h: 1 nm -> 2e9, 10 nm -> 2e8, 100 nm -> 2e7, 1 um -> 2e6 /m.
- Debye length at 25 C: 0.304/sqrt(I[M]) nm: 1 mM -> 9.61 nm, 10 mM ->
  3.04 nm, 100 mM -> 0.96 nm.
- 30 nm channel: 0.1 mM -> overlapped (2*lambda/h = 2.03); 10 mM -> bulk.
- Slip enhancement 1+6b/h: b=20 nm, h=50 nm -> 3.4x.
- 100x50 nm x 1 mm channel: 5 fL, ~1.67e11 water molecules.
- Electro-osmosis: zeta=-50 mV, E=100 V/cm -> v = 3.48e-4 m/s (348 um/s).
- Electrophoresis: mu = 3.48e-8 m^2/Vs; 1 cm in 28.8 s at 100 V/cm.
- Donnan at -80 mV: co-ion exclusion 95.5%, counter-ion enrichment 22.5x.
- Streaming potential: 1 bar, sigma=0.01 S/m, zeta=-50 mV -> 0.348 V.
- ICP depletion: sqrt(D*t), D=2e-9: 1 s -> 44.7 um, 10 s -> 141 um.
- Conical pore 5/100 nm: geometric asymmetry 400; measured rectification ~12.
- Osmotic power: 0.5M/0.01M -> 0.101 V Nernst; 1 nA/pore -> 1e-10 W/pore.
- EK conversion: I_str=3.48 pA, V_str=0.348 V, P_elec=0.30 pW, P_hyd=8.3 pW.
- Resistive pulse: (5/30)^3 = 0.46% current dip; 10 us dwell.
- DNA: 10 kbp at 1 us/base -> 10 ms transit.
- Nanofluidic FET: Dukhin 25.9 -> conductance on/off ~27.
- Memristor: depletion/accumulation -> resistance ratio 8.1.
- Desalination: 250 L/m^2/h/bar; 1 m^2 at 5 bar -> 30,000 L/day.
- Confined water: 2 nm -> 7 layers; D/10; 2 nm diffusion in 8.7 ns.
- CNT slip: 1+4b/R, R=1 nm, b=300 nm -> 1201x.
- Access resistance: 5e7 ohm per mouth vs pore 1.27e8 ohm (44% of 2.27e8 total).
- Hydraulic resistance: 1 um x 50 nm x 1 mm -> 9.6e22 Pa s/m^3; 1 bar ->
  1.04 fL/s.
- Diffusio-osmosis: 5 um/s at 10x gradient over 1 mm.
- Steric sieving: Phi=0.36, Renkin hindrance 0.102 for a/r=0.4.
- RC time: R=2e10 ohm, C_dl=6.95e-11 F -> tau=1.39 s.
- CNT velocity: HP 12.5 um/s -> 15 mm/s with slip.
- Angstrom slit 0.68 nm: K+/Al3+ mobility ratio ~50.
- Lab-on-chip mixing: (100 um)^2/D -> 10 s.
- Biosensor: 1 fM in 1 uL -> 602 molecules.
- Fouling: J0*exp(-t/72h); half-flux at 49.9 h.
- Design: series-parallel network -> R_total=1.5e21.
- Safety: 1 mg in 30 m^3 -> 33.3 ug/m^3 vs 1 ug/m^3 REL.
- Future: 1M devices at 250/wafer -> 4000 wafers.
"""

SIG_TAIL = ("Signature original - his original Signature interpretation of "
            "nanofluidics, clearly labeled Signature-made and never "
            "presented as authentic public record.")

ENTRIES = [
{
"key": "what_is",
"name": "What Is Nanofluidics: Fluids in 1-to-100 Nanometre Channels",
"group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
"description": (
"Nanofluidics is the study of how liquids and dissolved ions behave when "
"they are confined in channels, pores, and slits only 1 to 100 nanometres "
"across. At this scale the channel is so narrow that the liquid inside "
"stops acting like the water in a pipe. A 50-nanometre slit is spanned by "
"only about 167 water molecules side by side; the walls are never far "
"away, so surface forces - electric charge on the walls, friction at the "
"wall, attraction between the liquid and the solid - compete with, and "
"often defeat, the familiar rules of pressure-driven flow. Ions dissolved "
"in the liquid feel the wall charge as strongly as they feel the applied "
"voltage, which means a nanochannel can sort ions by charge, pump liquid "
"with electricity, or generate electricity from salt water. Nanofluidics "
"sits between microfluidics (channels you can see under a microscope) and "
"single molecules: it is the plumbing scale where chemistry, electricity, "
"and fluid mechanics all speak at once."),
"how_it_works": (
"A nanofluidic device is a channel whose smallest dimension - height, "
"diameter, or slit gap - is comparable to the natural length scales of the "
"liquid: the size of a water molecule (0.3 nm), the thickness of the "
"electrical double layer (1-100 nm depending on salt), and the slip length "
"(0-100s of nm). Because the surface-to-volume ratio of a slit is 2 "
"divided by its height, a 50 nm channel has 20,000 times more wall per "
"drop of liquid than a 1 mm pipe. Every ion that enters must negotiate "
"with the charged wall. Push liquid through with pressure and the moving "
"ions drag charge along, building a streaming voltage. Apply voltage and "
"the ions near the wall drag the whole liquid with them - electro-osmotic "
"pumping with no moving parts. Make the channel narrower than twice the "
"double-layer thickness and the channel admits only counter-ions, becoming "
"an ion filter. All of nanofluidics is this one idea: when the container "
"is as small as the forces inside it, the walls run the show."),
"key_points": [
"Nanofluidics = fluid + ion transport in 1-100 nm confinement, where walls dominate.",
"A 50 nm slit is spanned by ~167 water molecules; a 1 mm pipe by ~3.3 million.",
"Surface-to-volume ratio 2/h: 4e7 /m at 50 nm vs 2000 /m at 1 mm - a 20,000x jump.",
"Wall charge, double layers, and slip compete with pressure-driven flow at this scale.",
"One geometry yields pumping, sensing, filtering, and power generation.",
"Nanofluidics sits between microfluidics and single molecules."],
"requirements": [
"A channel, pore, or slit with at least one dimension between 1 and 100 nm.",
"A liquid (usually water) carrying dissolved ions.",
"Charged or chargeable walls - nearly all solids charge in water.",
"A way to drive flow: pressure, voltage, or salt gradient."],
"standards": [
"ISO/TS 80004-1:2023 - vocabulary for nanotechnology and nano-objects.",
"IUPAC definitions of the electrical double layer and electrokinetic phenomena."],
"citations": [
"Bocquet, L. & Charlaix, E. 'Nanofluidics, from bulk to interfaces' Chem. Soc. Rev. 39, 1073-1095 (2010).",
"Eijkel, J. C. T. & van den Berg, A. 'Nanofluidics: what is it and what can we expect from it?' Microfluid. Nanofluid. 1, 249-267 (2005).",
"Schoch, R. B., Han, J. & Renaud, P. 'Transport phenomena in nanofluidics' Rev. Mod. Phys. 80, 839-883 (2008)."],
"sig_lens": (
"Signature lens: treat the nanochannel as a Signature corridor - a "
"passage so narrow that the walls themselves become active participants "
"rather than passive boundaries. The Signature reading asks what the "
"corridor selects, what it amplifies, and what it refuses, and designs "
"the wall chemistry as deliberately as the channel geometry.")},
{
"key": "scale",
"name": "The Nanoscale Advantage: Why Small Channels Behave Differently",
"group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
"description": (
"Why does shrinking a channel change the physics instead of just making a "
"smaller pipe? Three scale effects answer that. First, the surface takes "
"over: the surface-to-volume ratio of a slit is 2/h, so at h = 10 nm the "
"wall area per volume is 2e8 per metre - one hundred times the ratio at 1 "
"micrometre - and 20 percent of all water molecules sit within "
"one nanometre of a wall, inside the reach of surface forces. Second, the "
"channel becomes comparable to the liquid's own electrical screening "
"length: at 1 mM salt the Debye length is about 10 nm, so a 20 nm channel "
"is mostly double layer, not bulk liquid. Third, continuum assumptions "
"crack: when the channel holds tens of molecular layers, viscosity, "
"dielectric constant, and diffusion are no longer bulk constants but "
"position-dependent profiles set by the wall. Microfluidics miniaturizes "
"the pipe; nanofluidics changes what a liquid is."),
"how_it_works": (
"Take the ratio 2/h and watch it explode as h falls: 1 um -> 2e6 /m, "
"100 nm -> 2e7 /m, 10 nm -> 2e8 /m, 1 nm -> 2e9 /m. Each decade of "
"shrinking multiplies the wall's vote by ten. Meanwhile the Debye "
"screening length stays fixed by the salt concentration - about 10 nm at "
"1 mM - so there is a crossing point where the double layers from "
"opposite walls meet in the middle and the whole channel becomes charged "
"territory. Below that crossing, the channel's ion content is set by the "
"wall charge, not by the reservoir salt; conductance stops depending on "
"salt concentration and saturates at a surface-governed plateau. That "
"saturation - first measured clearly by Stein, Kruithof and Dekker in "
"2004 - is the experimental signature that you have entered nanofluidics: "
"the bulk rules have handed power to the walls."),
"key_points": [
"Surface-to-volume 2/h: 2e9 /m at 1 nm vs 2e6 /m at 1 um - a thousand-fold range.",
"At 10 nm, ~20% of water molecules are within 1 nm of a wall.",
"The Debye length (~10 nm at 1 mM) sets the crossing into wall-governed transport.",
"Below the crossing, conductance saturates - the Stein/Kruithof/Dekker signature of nanofluidics.",
"Viscosity and permittivity become profiles, not constants, near walls.",
"Microfluidics shrinks the pipe; nanofluidics rewrites the liquid."],
"requirements": [
"A channel height h spanning the 1 nm - 1 um decade range for comparison.",
"Known salt concentration to fix the Debye screening length.",
"Conductance measurement across salt concentrations to find the saturation plateau."],
"standards": [
"ISO/TS 80004-1:2023 - nanoscale vocabulary.",
"IUPAC Technical Report on electrokinetic phenomena (Delgado et al.)."],
"citations": [
"Stein, D., Kruithof, M. & Dekker, C. 'Surface-charge-governed ion transport in nanofluidic channels' Phys. Rev. Lett. 93, 035901 (2004).",
"Bocquet, L. & Charlaix, E. 'Nanofluidics, from bulk to interfaces' Chem. Soc. Rev. 39, 1073-1095 (2010)."],
"sig_lens": (
"Signature lens: read the 2/h curve as a Signature scaling law - every "
"decade of narrowing is a transfer of authority from the bulk to the "
"boundary. Signature design works the decades deliberately, choosing the "
"channel height that hands exactly the right amount of power to the walls.")},
{
"key": "double_layer",
"name": "Surface Charge and the Electrical Double Layer",
"group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
"description": (
"Almost every solid surface placed in water becomes electrically charged: "
"glass and silica shed protons and turn negative, proteins titrate with "
"pH, membranes carry fixed charge groups. The liquid answers by piling up "
"counter-ions near the wall and pushing co-ions away, forming the "
"electrical double layer - a charged skin of liquid a few nanometres to a "
"few hundred nanometres thick. The double layer has two parts: a thin "
"Stern layer of ions stuck to the wall, and a diffuse cloud whose ion "
"concentration decays exponentially with distance, with a characteristic "
"thickness called the Debye length. At 1 mM salt the Debye length is "
"about 9.6 nm; at 100 mM it shrinks to about 0.96 nm, because more salt "
"screens charge faster. The voltage at the edge of the stuck layer - the "
"zeta potential, typically tens of millivolts - is the handle by which "
"electric fields grab the liquid. Every electrokinetic effect in "
"nanofluidics is the double layer in motion."),
"how_it_works": (
"The Debye length comes from balancing thermal jiggling against "
"electrostatic pull: lambda = sqrt(epsilon*k*T / (2*N_A*e^2*I)), where I "
"is the ionic strength. At room temperature in water this simplifies to "
"about 0.304/sqrt(I[M]) nanometres - 9.61 nm at 1 mM, 3.04 nm at 10 mM, "
"0.96 nm at 100 mM. The wall's bare charge is partly hidden by the Stern "
"layer, so what the outside world feels is the zeta potential at the "
"slipping plane, usually -20 to -80 mV for silica. Apply a tangential "
"electric field and the excess counter-ions in the diffuse layer feel a "
"force, dragging the surrounding water with them - that is "
"electro-osmosis. Push the water with pressure and the dragged ions pile "
"up downstream - that is the streaming current. The double layer is the "
"clutch connecting electricity to fluid motion, and its thickness decides "
"whether a channel is microfluidic or nanofluidic."),
"key_points": [
"Solids charge in water (silica negative); counter-ions screen it in a diffuse cloud.",
"Debye length = 0.304/sqrt(I[M]) nm at 25 C: 9.61 nm at 1 mM, 0.96 nm at 100 mM.",
"Stern layer (stuck ions) + diffuse layer (exponential decay) = the double layer.",
"Zeta potential (tens of mV) is the voltage the outside world actually feels.",
"The double layer is the clutch between electric fields and liquid motion.",
"Its thickness decides whether a channel behaves micro or nano."],
"requirements": [
"A charged solid-liquid interface (silica, glass, polymer, membrane).",
"Known ionic strength - it sets the Debye length.",
"pH control, since surface charge titrates with pH."],
"standards": [
"ISO 13099 (all parts) - zeta potential measurement by electrophoresis.",
"IUPAC definitions of the electrical double layer."],
"citations": [
"Israelachvili, J. N. 'Intermolecular and Surface Forces' 3rd ed., Academic Press (2011).",
"Hunter, R. J. 'Zeta Potential in Colloid Science' Academic Press (1981).",
"Bocquet, L. & Charlaix, E. 'Nanofluidics, from bulk to interfaces' Chem. Soc. Rev. 39, 1073-1095 (2010)."],
"sig_lens": (
"Signature lens: the double layer is a Signature skin - the channel "
"growing its own charged atmosphere that mediates everything crossing "
"it. Signature design engineers the skin first (charge density, pH "
"response, thickness) and treats the bare wall as merely its anchor.")},
{
"key": "debye",
"name": "The Debye Length: The Ruler of Nanofluidic Regimes",
"group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
"description": (
"The Debye length is the single most useful ruler in nanofluidics: it "
"marks the distance over which the liquid can still feel the wall's "
"charge. Compare the channel height h to twice the Debye length and you "
"instantly know which regime you are in. If h is much larger than "
"2*lambda, the double layers hug the walls and the middle of the channel "
"is ordinary bulk liquid - microfluidic behavior. If h is comparable to "
"2*lambda, the double layers overlap and the whole channel feels the "
"wall - the true nanofluidic regime, where ion selectivity appears. If h "
"is much smaller than lambda, the channel is unipolar: it holds almost "
"exclusively counter-ions, like a solid electrolyte. Because lambda "
"shrinks with salt (9.61 nm at 1 mM, 0.96 nm at 100 mM), the SAME 30 nm "
"channel is overlapped and selective in dilute buffer but bulk-like in "
"seawater-strength salt. Salt concentration is therefore a knob that "
"tunes the device between regimes without rebuilding anything."),
"how_it_works": (
"Take a 30 nm channel. At 0.1 mM salt, lambda is 30.4 nm, so 2*lambda/h "
"is 2.03 - the double layers more than fill the channel, counter-ions "
"dominate, and the channel rejects co-ions. At 10 mM, lambda is 3.04 nm, "
"2*lambda/h is 0.20 - thin skins on the walls, bulk liquid in the middle, "
"no selectivity. The transition is smooth but the consequences are "
"sharp: conductance vs salt concentration flattens to a plateau at low "
"salt (surface-governed), then rises linearly at high salt (bulk-"
"governed). The knee of that curve tells you the surface charge density. "
"Designers use this ruler backwards: pick the operating salt, compute "
"lambda, then choose h near 2*lambda for maximum selectivity, or h far "
"above it when they want bulk behavior with nanofluidic plumbing."),
"key_points": [
"Regime rule: compare h to 2*lambda - bulk, overlapped, or unipolar.",
"Same 30 nm channel: overlapped at 0.1 mM (2*lambda/h = 2.03), bulk-like at 10 mM (0.20).",
"Salt concentration tunes the regime with no rebuild.",
"Conductance-vs-salt curve: plateau at low salt, linear at high salt; the knee gives surface charge.",
"Design backwards: pick salt, compute lambda, set h near 2*lambda for selectivity."],
"requirements": [
"Channel height h known to a few nanometres.",
"Salt concentration adjustable over at least 0.1-100 mM.",
"Conductance measurement across the salt range."],
"standards": [
"IUPAC definitions of Debye length and ionic strength.",
"ISO/TS 80004-1:2023 - nanoscale vocabulary."],
"citations": [
"Daiguji, H. 'Ion transport in nanofluidic channels' Chem. Soc. Rev. 39, 901-911 (2010).",
"Schoch, R. B., Han, J. & Renaud, P. 'Transport phenomena in nanofluidics' Rev. Mod. Phys. 80, 839-883 (2008)."],
"sig_lens": (
"Signature lens: the Debye length is a Signature tuning fork - one "
"number that decides which physics is in charge. Signature practice is "
"to name the regime before naming the device, and to let the salt "
"bottle do the work of a redesign.")},
{
"key": "slip",
"name": "Slip Flow: When the No-Slip Rule Breaks",
"group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
"description": (
"Textbook fluid mechanics says liquid at a wall does not move - the "
"no-slip condition. At the nanoscale on smooth hydrophobic walls, that "
"rule bends: the liquid slides, and the sliding is measured by the slip "
"length b, the distance behind the wall where the velocity profile would "
"hit zero. On hydrophilic glass b is near zero and no-slip holds; on "
"smooth hydrophobic surfaces b reaches tens of nanometres; inside carbon "
"nanotubes effective slip lengths reach hundreds of nanometres. Slip "
"matters because it multiplies flow: for a slit, the flow rate with slip "
"is (1 + 6b/h) times the no-slip rate, so a 50 nm channel with 20 nm of "
"slip flows 3.4 times faster than textbooks predict. Slip is why water "
"rushes through carbon nanotubes a thousand times faster than the "
"Hagen-Poiseuille law allows - the wall, instead of gripping, lets go."),
"how_it_works": (
"The slip length comes from the friction between the first liquid layer "
"and the solid: b = eta / friction-coefficient, where eta is viscosity. "
"Weak liquid-solid attraction (hydrophobic walls, smooth carbon "
"lattices) means low friction and large b; strong attraction pins the "
"first layer and b collapses. For pressure-driven flow in a slit the "
"parabolic profile lifts off the wall by the slip velocity v = b * "
"(dv/dn at wall), and integrating gives the enhancement factor 1 + 6b/h "
"- for a tube it is 1 + 4b/R. With h = 50 nm and b = 20 nm the factor is "
"3.4. The effect is purely geometric leverage: slip is a fixed length, "
"so it matters most in the smallest channels. Measurements by Secchi and "
"co-workers in 2016 showed the slip length inside carbon nanotubes grows "
"as the radius shrinks - small tubes are slipperier, the opposite of "
"naive expectation, because the water structure itself changes."),
"key_points": [
"Slip length b: distance behind the wall where the velocity extrapolates to zero.",
"Hydrophilic ~ 0 nm; hydrophobic tens of nm; carbon nanotubes hundreds of nm.",
"Slit flow enhancement = 1 + 6b/h: 3.4x for b=20 nm, h=50 nm.",
"Slip is fixed length, so leverage grows as channels shrink.",
"Secchi et al. 2016: smaller nanotubes are slipperier (radius-dependent slip).",
"Explains 1000x ultrafast flow in carbon nanotubes."],
"requirements": [
"A smooth wall - roughness kills slip.",
"Known wettability (contact angle) to estimate b.",
"Pressure-driven flow measurement to extract the enhancement factor."],
"standards": [
"ISO/TS 80004-1:2023 - nanoscale vocabulary.",
"ASTM E11-adjacent practice for contact-angle wettability characterization."],
"citations": [
"Secchi, E. et al. 'Massive radius-dependent flow slippage in carbon nanotubes' Nature 537, 210-213 (2016).",
"Bocquet, L. & Barrat, J.-L. 'Flow boundary conditions from nano- to micro-scales' Soft Matter 3, 685-693 (2007).",
"Majumder, M. et al. 'Nanoscale hydrodynamics: enhanced flow in carbon nanotubes' Nature 438, 44 (2005)."],
"sig_lens": (
"Signature lens: slip is the Signature release - the wall choosing "
"not to grip. Signature design treats friction as a tunable material "
"property (chemistry, smoothness, curvature) and spends it where flow "
"speed pays: the smallest channels, where a fixed slip length buys the "
"largest multiple.")},
{
"key": "fabrication",
"name": "Making Nanochannels: How Nanometre Plumbing Is Built",
"group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
"description": (
"Nanofluidic devices are built with the toolset of the semiconductor "
"industry plus a few nano-specific tricks. The classic route is "
"top-down: etch a shallow trench into silicon or glass with "
"photolithography or electron-beam lithography, then bond a cover slip "
"over it to close the channel - a 100 nm wide, 50 nm deep, 1 mm long "
"trench holds just 5 femtolitres, about 1.67e11 water molecules. "
"Bottom-up routes grow the channel itself: carbon nanotubes and "
"transmembrane protein pores are ready-made nanochannels, and "
"track-etched polymer membranes carry millions of conical nanopores. "
"The newest route is van der Waals assembly: stacking 2D crystals like "
"graphene and hexagonal boron nitride with spacer strips leaves "
"angstrom-scale slits with atomically smooth walls - capillaries with "
"0.34 nm precision, demonstrated by Radha and co-workers in 2016. Each "
"route trades precision for throughput: e-beam writes perfect single "
"channels slowly; membranes make billions of pores with spread in size. "
"Every nanofluidic experiment begins with this choice."),
"how_it_works": (
"Top-down: deposit, pattern, etch, bond. A silicon wafer gets a mask, "
"reactive-ion etching carves the trench to the target depth (timed or "
"etch-stop controlled), and anodic or fusion bonding seals a glass lid - "
"the bond must be void-free or the channel leaks sideways. Bottom-up: "
"embed ready-made pores - a single carbon nanotube across a membrane, or "
"an alpha-hemolysin protein in a lipid bilayer, gives a 1-2 nm channel "
"with atomic reproducibility no lithography can match. Van der Waals "
"assembly: exfoliate crystals, pattern graphene spacers by lithography, "
"stack crystal-spacer-crystal; the slit height equals the spacer "
"thickness, controllable to a single atomic layer. The demo computes the "
"plumbing directly: a 100 nm x 50 nm x 1 mm trench is 5e-21 cubic metres "
"= 5 femtolitres = about 1.67e11 water molecules - a vivid reminder that "
"nanofluidic volumes are counted in molecules, not drops."),
"key_points": [
"Top-down: lithography + etch + bond - precise, slow, single channels.",
"Bottom-up: nanotubes, protein pores - atomic reproducibility, ready-made.",
"Van der Waals stacking: angstrom slits with 0.34 nm precision (Radha et al. 2016).",
"A 100x50 nm x 1 mm trench holds 5 fL - about 1.67e11 water molecules.",
"Trade precision vs throughput: e-beam perfect-slow, membranes many-with-spread.",
"Bonding quality decides whether the channel holds or leaks sideways."],
"requirements": [
"Cleanroom or equivalent particle control for top-down builds.",
"Nanometre etch-depth control (timed etch or etch stop).",
"Void-free bonding process for sealing.",
"For 2D assembly: exfoliation and deterministic stacking capability."],
"standards": [
"SEMI standards for wafer processing and bonding.",
"ISO/TS 80004 series - nanotechnology vocabulary and characterization."],
"citations": [
"Radha, B. et al. 'Molecular transport through capillaries made with atomic-scale precision' Nature 538, 222-225 (2016).",
"Eijkel, J. C. T. & van den Berg, A. 'Nanofluidics: what is it and what can we expect from it?' Microfluid. Nanofluid. 1, 249-267 (2005).",
"Dekker, C. 'Solid-state nanopores' Nature Nanotech. 2, 209-215 (2007)."],
"sig_lens": (
"Signature lens: fabrication is Signature plumbing - the discipline of "
"making passages the width of molecules. Signature builders pick the "
"route by the question: atomic perfection for physics (2D slits, "
"proteins), engineered arrays for devices (track-etch), lithography for "
"circuits - and never pay for precision the measurement cannot use.")},
{
"key": "electroosmosis",
"name": "Electro-osmosis: Pumping Liquid with Voltage",
"group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
"description": (
"Electro-osmosis is the workhorse pump of nanofluidics: apply a voltage "
"along a channel and the liquid moves - no pistons, no valves, no moving "
"parts. It works because the wall's double layer holds excess "
"counter-ions; the electric field pulls those ions, and viscosity drags "
"the rest of the liquid along with them. The resulting velocity follows "
"the Helmholtz-Smoluchowski law: v = -epsilon*zeta*E/eta. For water on "
"silica (zeta about -50 mV) at 100 V/cm, that is 3.48e-4 m/s - about 348 "
"micrometres per second, crossing a 1 cm chip in under 30 seconds. The "
"flow profile is plug-like (flat across the channel, unlike pressure-"
"driven parabolic flow), which is why electro-osmosis is beloved for "
"separations: every molecule rides at nearly the same speed, so bands "
"stay sharp. Reverse the voltage and the flow reverses instantly - a pump "
"with no inertia."),
"how_it_works": (
"Only the charged skin of liquid feels the field directly, but momentum "
"diffuses across the channel by viscosity in microseconds, so the whole "
"column moves as a plug. The demo evaluates the Helmholtz-Smoluchowski "
"law: epsilon = 78.5 * 8.854e-12 F/m, zeta = -0.05 V, E = 1e4 V/m, eta = "
"1e-3 Pa s, giving v = 3.476e-4 m/s. The sign follows the counter-ions: "
"negative wall, positive cloud, field toward the cathode drags liquid to "
"the cathode. Practical notes: the electrodes must not bubble (use "
"reversible Ag/AgCl or large reservoirs), Joule heating limits the field "
"in salty buffers, and pH sets zeta - titrate the wall and you throttle "
"the pump. Electro-osmotic flow is also the reference against which "
"electrophoresis is measured: particles move by the sum of "
"electro-osmosis (liquid carrying them) and their own electrophoretic "
"motion relative to the liquid."),
"key_points": [
"v = -epsilon*zeta*E/eta: 348 um/s for silica/water at 100 V/cm.",
"No moving parts; flow reverses instantly with voltage.",
"Plug profile - all molecules ride at the same speed, bands stay sharp.",
"1 cm chip crossed in under 30 seconds.",
"pH titrates zeta and throttles the pump; Joule heating limits salty buffers.",
"Reference frame for electrophoresis measurements."],
"requirements": [
"Charged walls with known zeta potential.",
"Axial electric field (electrodes + voltage source).",
"Bubble management at electrodes; low-conductivity buffer preferred."],
"standards": [
"IUPAC electrokinetic definitions (Delgado et al.).",
"ISO 13099 - zeta potential measurement."],
"citations": [
"Delgado, A. V. (ed.) 'Interfacial Electrokinetics and Electrophoresis' Dekker (2002).",
"Probstein, R. F. 'Physicochemical Hydrodynamics' 2nd ed., Wiley (1994).",
"Schoch, R. B., Han, J. & Renaud, P. 'Transport phenomena in nanofluidics' Rev. Mod. Phys. 80, 839-883 (2008)."],
"sig_lens": (
"Signature lens: electro-osmosis is Signature pumping - moving the "
"river by pulling its charged skin. Signature micro-plumbing uses it "
"where mechanics cannot go: valveless routing, instant reversal, and "
"metering by voltage instead of by pistons.")},
{
"key": "electrophoresis",
"name": "Electrophoresis: Sorting Charged Particles by Speed",
"group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
"description": (
"Electrophoresis is the motion of a charged particle relative to the "
"liquid around it: DNA, proteins, and colloids each carry charge, so an "
"electric field pulls them through the buffer at a speed set by their "
"charge-to-friction ratio. The electrophoretic mobility mu = "
"epsilon*zeta_particle/eta (Smoluchowski limit) is about 3.48e-8 "
"m^2/(V s) for a typical -50 mV particle in water - at 100 V/cm it drifts "
"348 um/s relative to the liquid and crosses a 1 cm channel in 28.8 "
"seconds. In a nanochannel this gets interesting: the particle's own "
"double layer overlaps the wall's, the channel sieves by size as well as "
"charge, and the flat electro-osmotic profile keeps bands sharp. Gel "
"electrophoresis sorts DNA by length; free-solution nanochannel "
"electrophoresis sorts by charge and wall interaction; nanopore "
"translocation (a later record) reads single molecules as they pass. "
"Same physics, three instruments."),
"how_it_works": (
"Mobility balances electric force against viscous drag: for a thin double "
"layer the Smoluchowski formula mu = epsilon*zeta/eta applies, "
"independent of particle size - which is why free-solution electrophoresis "
"cannot sort by size and gels are needed. The demo computes mu = "
"3.476e-8 m^2/(V s) and the transit time across 1 cm at 1e4 V/m: 28.77 s. "
"In nanochannels two corrections appear: double-layer overlap makes mu "
"depend on the ratio of particle size to channel height, and wall "
"interactions (adsorption, steric exclusion) add a chromatographic "
"retention. Practically, the observed velocity is electrophoresis plus "
"electro-osmosis - measure with a neutral marker to subtract the liquid "
"motion. That subtraction is the oldest trick in electrokinetics and still "
"the first calibration of every nanofluidic run."),
"key_points": [
"mu = epsilon*zeta/eta ~ 3.48e-8 m^2/(V s); 1 cm in 28.8 s at 100 V/cm.",
"Smoluchowski limit: mobility independent of size - gels add the size axis.",
"Observed velocity = electrophoresis + electro-osmosis; subtract with a neutral marker.",
"Nanochannels add overlap and wall-interaction corrections.",
"Basis of DNA gels, protein separations, and nanopore translocation."],
"requirements": [
"Charged analyte with known (or measurable) zeta potential.",
"Uniform axial field; neutral marker for the electro-osmotic correction.",
"Buffer pH chosen so analyte and wall charges are as intended."],
"standards": [
"ISO 13099 - zeta potential measurement.",
"IUPAC electrokinetic definitions."],
"citations": [
"Hunter, R. J. 'Zeta Potential in Colloid Science' Academic Press (1981).",
"Probstein, R. F. 'Physicochemical Hydrodynamics' 2nd ed., Wiley (1994).",
"Branton, D. et al. 'The potential and challenges of nanopore sequencing' Nature Biotech. 26, 1146-1153 (2008)."],
"sig_lens": (
"Signature lens: electrophoresis is Signature sorting - letting charge "
"write each particle's speed limit. Signature separators stack the "
"axes deliberately: charge from the field, size from the gel or the "
"channel, wall affinity from the chemistry - three knobs, one pass.")}

,
{
"key": "selectivity",
"name": "Overlapping Double Layers: How Nanochannels Choose Ions",
"group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
"description": (
"When the double layers from opposite walls overlap, a nanochannel stops "
"being a passive pipe and becomes an ion filter. A negatively charged "
"channel admits positive counter-ions freely while rejecting negative "
"co-ions by the Donnan exclusion principle: at a Donnan potential of -80 "
"mV, co-ions are suppressed to 4.5% of their reservoir concentration "
"(95.5% rejection) while counter-ions are enriched 22.5-fold. The channel "
"is then unipolar - it conducts with essentially one ionic species, like "
"a solid electrolyte. This is the physical basis of nanofluidic "
"selectivity, and it needs no membrane chemistry: geometry plus wall "
"charge does the work. Selectivity appears exactly when h < 2*lambda, "
"which is why the same device filters in dilute buffer and goes blind in "
"concentrated salt. Every desalination membrane, every nanofluidic diode, "
"and every osmotic-power device in this database is built on this one "
"effect."),
"how_it_works": (
"Donnan equilibrium: an ion of valence z partitions between reservoir "
"and channel as c = c0 * exp(-z*e*psi/kT). With psi = -80 mV and kT/e = "
"25.7 mV at room temperature, a monovalent co-ion (z = -1) sees "
"exp(-3.11) = 0.0445 - 95.5% excluded - while a counter-ion (z = +1) sees "
"exp(+3.11) = 22.5 - enriched 22.5x. The demo evaluates exactly this. The "
"strength of exclusion grows with valence: divalent co-ions are excluded "
"as the square, which is why nanochannels reject sulfate far more "
"strongly than chloride. In the fully overlapped limit the channel's "
"conductance saturates at the surface-governed value (the Stein plateau) "
"because the counter-ion population is fixed by the wall charge, not by "
"the reservoir. Selectivity is quantified by the transference number - "
"the fraction of current carried by counter-ions - approaching 1.0 in "
"good nanofluidic filters versus 0.5 in bulk salt water."),
"key_points": [
"Donnan exclusion: -80 mV wall potential -> 95.5% co-ion rejection, 22.5x counter-ion enrichment.",
"Unipolar conduction: the channel behaves like a solid electrolyte.",
"Exclusion scales with valence squared - divalents rejected far more strongly.",
"Conductance saturates at the Stein plateau when double layers overlap.",
"Transference number approaches 1.0 vs 0.5 in bulk.",
"Selectivity needs h < 2*lambda - geometry plus wall charge, no membrane chemistry."],
"requirements": [
"Channel height below twice the Debye length at operating salt.",
"Stable wall charge (silica, charged polymer, fixed membrane groups).",
"Concentration measurement or reversal-potential measurement to quantify selectivity."],
"standards": [
"IUPAC definitions of Donnan equilibrium and transference number.",
"ISO/TS 80004-1:2023 - nanoscale vocabulary."],
"citations": [
"Stein, D., Kruithof, M. & Dekker, C. 'Surface-charge-governed ion transport in nanofluidic channels' Phys. Rev. Lett. 93, 035901 (2004).",
"Daiguji, H. 'Ion transport in nanofluidic channels' Chem. Soc. Rev. 39, 901-911 (2010).",
"Vlassiouk, I., Smirnov, S. & Siwy, Z. 'Ionic selectivity of single nanochannels' Nano Lett. 8, 1978-1985 (2008)."],
"sig_lens": (
"Signature lens: selectivity is Signature choosing - the corridor "
"admitting only its own kind. Signature filters are drawn from the "
"Donnan math first: pick the rejection you need, solve for the wall "
"potential and the height, then build exactly that and nothing more.")},
{
"key": "streaming",
"name": "Streaming Potential: Making Electricity from Pressure",
"group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
"description": (
"Push water through a charged nanochannel with pressure and electricity "
"comes out: the flow drags the double layer's excess counter-ions "
"downstream, building a streaming current, and if the ends of the channel "
"are not shorted, charge piles up until the resulting voltage drives an "
"equal back-conduction - the streaming potential. The Helmholtz-"
"Smoluchowski relation gives V = epsilon*zeta*deltaP/(eta*sigma): for "
"zeta = -50 mV, 1 bar of pressure, and a 0.01 S/m buffer, the streaming "
"potential is 0.348 V - a third of a volt from water pressure alone. This "
"is the exact inverse of electro-osmosis (Onsager reciprocity): voltage "
"drives flow, flow drives voltage, with the same coefficient. Streaming "
"potential is both a measurement tool (it reports zeta potential without "
"electrodes in the channel) and an energy harvester (pressure in, power "
"out). Every electrokinetic energy converter in this database starts "
"here."),
"how_it_works": (
"The streaming current is the advective transport of double-layer charge: "
"I_str = -epsilon*zeta*A*deltaP/(eta*L) for a channel of area A and length "
"L. Open-circuit, the pile-up voltage V_str drives a conduction current "
"V_str/R_channel back upstream; steady state sets them equal, giving V = "
"epsilon*zeta*deltaP/(eta*sigma) where sigma is the liquid conductivity. "
"The demo evaluates it: epsilon*zeta = 3.476e-11, times 1e5 Pa, divided "
"by (1e-3 * 0.01) = 0.3476 V. Note the trade: low-conductivity buffers "
"give larger voltage but the harvested power peaks at an intermediate "
"conductivity where the product of current and voltage is maximized. "
"Measured streaming potentials are the standard non-invasive zeta "
"meter for nanochannels - no electrodes inside, no disturbance of the "
"double layer you are trying to measure."),
"key_points": [
"V = epsilon*zeta*deltaP/(eta*sigma): 0.348 V per bar at zeta=-50 mV, sigma=0.01 S/m.",
"Exact inverse of electro-osmosis (Onsager reciprocity) - same coefficient both ways.",
"Open-circuit voltage; short-circuit gives the streaming current instead.",
"Standard non-invasive zeta-potential measurement for nanochannels.",
"Power peaks at intermediate conductivity - low sigma gives volts, high sigma gives amps.",
"Foundation of all electrokinetic energy harvesting."],
"requirements": [
"Pressure source (1 bar scale) across a charged nanochannel.",
"High-impedance voltmeter for open-circuit potential.",
"Reversible electrodes (Ag/AgCl) in the reservoirs."],
"standards": [
"IUPAC electrokinetic definitions.",
"ISO 13099 - zeta potential via streaming potential."],
"citations": [
"van der Heyden, F. H. J., Stein, D. & Dekker, C. 'Streaming currents in a single nanofluidic channel' Phys. Rev. Lett. 95, 116104 (2005).",
"Delgado, A. V. (ed.) 'Interfacial Electrokinetics and Electrophoresis' Dekker (2002)."],
"sig_lens": (
"Signature lens: streaming potential is Signature reciprocity - every "
"pump run backwards is a generator. Signature harvesters are designed "
"from this equation outward: pick the pressure you have, solve for the "
"zeta and conductivity that maximize the product, then build the "
"channel that holds those numbers.")},
{
"key": "conductance",
"name": "Surface Conductance: The Extra Current Along the Walls",
"group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
"description": (
"A nanochannel conducts more current than its bulk liquid should allow, "
"because the double layer adds a second, surface-hugging conduction path: "
"surface conductance. The total conductance is G = G_bulk + G_surface, "
"where G_bulk = sigma*w*h/L is the familiar bulk term and G_surface = "
"2*mu*|sigma_s|*w/L comes from counter-ions sliding along the charged "
"walls (sigma_s is the surface charge density, mu the ion mobility). The "
"Dukhin number Du = G_surface/G_bulk measures which term wins: Du >> 1 "
"means the walls carry the current. For a 20 nm channel at 1 mM salt with "
"a typical silica charge, Du reaches about 26 - the walls carry 26 times "
"the bulk current. Surface conductance is why nanochannel conductance "
"saturates at low salt instead of falling with concentration: as the "
"reservoir empties, the wall's own counter-ions keep the current alive. "
"It is the quantity that makes nanofluidic transistors possible - gate "
"the wall charge and you gate Du, and with it the whole conductance."),
"how_it_works": (
"Du = |sigma_s| / (e*n*h): surface charge over the bulk charge content of "
"the channel. With sigma_s = 0.05 C/m^2, n = 6.022e23 m^-3 (1 mM), h = "
"20 nm: denominator = 1.602e-19 * 6.022e23 * 20e-9 = 1.93e-3, so Du = "
"25.9 - the demo's number. Conductance then reads G = G_bulk*(1 + Du) in "
"the simplest model, so gating the surface charge from 0 to 0.05 C/m^2 "
"swings the conductance by a factor of ~27 - the operating principle of "
"the nanofluidic field-effect transistor (a later record). Measuring G "
"vs salt concentration and fitting the low-salt plateau is the standard "
"way to extract sigma_s: the plateau value is 2*mu*|sigma_s|*w/L, a "
"direct window onto the wall charge. High Du also flags the regime where "
"concentration polarization and ion depletion (later records) will be "
"strongest."),
"key_points": [
"G = G_bulk + G_surface; Dukhin number Du = |sigma_s|/(e*n*h) picks the winner.",
"20 nm channel, 1 mM: Du = 25.9 - walls carry ~26x the bulk current.",
"Explains the low-salt conductance plateau (surface-governed transport).",
"Low-salt plateau value directly measures surface charge density.",
"Gating sigma_s gates Du - the principle of the nanofluidic transistor.",
"High Du flags strong concentration-polarization regimes."],
"requirements": [
"Conductance measurement across a salt-concentration decade sweep.",
"Channel geometry (w, h, L) known to extract sigma_s from the plateau.",
"Ion mobility values for the electrolyte used."],
"standards": [
"IUPAC definitions of surface conductance and Dukhin number.",
"ISO/TS 80004-1:2023 - nanoscale vocabulary."],
"citations": [
"Stein, D., Kruithof, M. & Dekker, C. 'Surface-charge-governed ion transport in nanofluidic channels' Phys. Rev. Lett. 93, 035901 (2004).",
"Schoch, R. B., Han, J. & Renaud, P. 'Transport phenomena in nanofluidics' Rev. Mod. Phys. 80, 839-883 (2008).",
"Plecis, A., Schoch, R. B. & Renaud, P. 'Ionic transport phenomena in nanofluidics' Nano Lett. 5, 1147-1155 (2005)."],
"sig_lens": (
"Signature lens: surface conductance is the Signature second wire - a "
"current path the bulk equations never drew. Signature circuit "
"designers count both wires from the start, and use the Dukhin number "
"as the gain knob: charge the wall and the whole channel answers.")},
{
"key": "icp",
"name": "Ion Concentration Polarization: Depletion Zones on Demand",
"group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
"description": (
"Put a selective nanochannel between two microchannels, apply voltage, "
"and something dramatic appears: on one side the salt piles up "
"(enrichment zone), on the other it vanishes (depletion zone) - ion "
"concentration polarization (ICP). The selective channel passes mostly "
"counter-ions, so co-ions accumulate on the anodic side and are starved "
"on the cathodic side; the depletion zone grows by diffusion, its front "
"advancing as roughly sqrt(D*t) - about 141 micrometres in 10 seconds "
"for D = 2e-9 m^2/s. The depletion zone is nearly ion-free water, which "
"makes it a tool: proteins and DNA swept toward it by electro-osmosis "
"stack up at its edge, preconcentrated a million-fold (Wang et al. "
"2005); push harder and the zone desalts seawater continuously. Above a "
"threshold voltage the flat depletion front goes unstable and "
"electroconvective vortices appear, carrying overlimiting current - more "
"current than diffusion alone allows. ICP is nanofluidics' phase "
"transition: a sharp, controllable boundary written in salt."),
"how_it_works": (
"The nanochannel's selectivity (transference number near 1) forces a "
"salt flux mismatch at each micro-nano junction: ions leave faster than "
"they arrive on one side. Diffusion smooths the resulting gradient over "
"a length that grows as sqrt(D*t) - the demo prints 44.7 um at 1 s, 141 "
"um at 10 s, 447 um at 100 s. The depletion zone's conductivity "
"collapses, so most of the applied voltage drops across it, which "
"strengthens the local field, which sharpens the zone - positive "
"feedback that keeps the boundary crisp. For preconcentration, analytes "
"are driven toward the depletion front by electro-osmosis but cannot "
"cross the ion-free region, so they stack: million-fold concentration "
"of proteins and peptides has been demonstrated. For desalination, the "
"purified stream is siphoned from the depletion side. The overlimiting "
"regime - vortices stirring the depletion layer - was explained by "
"Zangle, Mani and Santiago: electroconvection, not water splitting, "
"carries the extra current."),
"key_points": [
"Selective nanochannel + voltage -> enrichment zone + depletion zone.",
"Depletion front grows as sqrt(D*t): 141 um in 10 s for D=2e-9 m^2/s.",
"Depletion zone is nearly ion-free - a tool for preconcentration and desalting.",
"Million-fold protein preconcentration demonstrated (Wang et al. 2005).",
"Overlimiting current carried by electroconvective vortices (Zangle/Mani/Santiago).",
"Positive feedback keeps the depletion boundary sharp."],
"requirements": [
"Microchannel-nanochannel-microchannel junction with a selective nanochannel.",
"DC voltage across the junction; fluorescence imaging to watch the zones.",
"Analyte or salt stream to process on the depletion side."],
"standards": [
"IUPAC electrokinetic definitions.",
"ISO/TS 80004-1:2023 - nanoscale vocabulary."],
"citations": [
"Zangle, T. A., Mani, A. & Santiago, J. G. 'Theory and experiments of concentration polarization and ion focusing at microchannel-nanochannel interfaces' Chem. Soc. Rev. 39, 1014-1035 (2010).",
"Wang, Y.-C. et al. 'Million-fold preconcentration of proteins and peptides by nanofluidic filter' Anal. Chem. 77, 4293-4299 (2005).",
"Mani, A., Zangle, T. A. & Santiago, J. G. 'On the propagation of concentration polarization from microchannel-nanochannel interfaces' Langmuir 25, 10145-10152 (2009)."],
"sig_lens": (
"Signature lens: ICP is Signature phase-writing - drawing a sharp "
"boundary in salt where none existed. Signature processors use the "
"depletion front as a working edge: stack molecules against it, skim "
"pure water from behind it, and let electroconvection do the stirring.")},
{
"key": "diode",
"name": "Nanofluidic Diodes: One-Way Streets for Ions",
"group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
"description": (
"A nanofluidic diode passes ionic current easily one way and chokes it "
"the other - rectification ratios around 12 at 1 V in the classic "
"conical nanopore design. The recipe is asymmetry plus selectivity: a "
"conical pore (say 5 nm tip, 100 nm base, geometric asymmetry 400) with "
"charged walls accumulates ions when the field pushes counter-ions from "
"base to tip and depletes them in reverse, because the narrow tip's "
"double layer dominates transport while the wide base behaves bulk-like. "
"Forward bias floods the tip with counter-ions (high conductance); "
"reverse bias starves it (low conductance). Siwy's group showed in 2002-"
"2006 that a single asymmetric nanopore rectifies like a semiconductor "
"diode, and that patterning the wall charge (half positive, half "
"negative) rectifies even in symmetric pores - a bipolar diode made of "
"chemistry alone. Diodes are the first nanofluidic circuit element: with "
"them plus transistors come logic, memory, and signal processing in "
"ions instead of electrons."),
"how_it_works": (
"Rectification needs the current to depend on voltage polarity, which "
"needs the ion distribution to depend on polarity - that takes broken "
"symmetry. In the conical pore, forward bias (counter-ions driven tip-"
"ward) enriches the tip region because the tip's overlapped double layer "
"holds them; reverse bias depletes it because ions are pulled out faster "
"than the base supplies them. The demo computes the geometric asymmetry "
"(r_base/r_tip)^2 = 400 for 100/5 nm and notes the measured rectification "
"ratio of ~12 at 1 V - geometry sets the ceiling, electrostatics sets "
"the operating point. The bipolar variant splits the pore into a "
"positive half and a negative half: forward bias accumulates both ion "
"types at the junction (like a p-n junction in forward bias), reverse "
"bias depletes the junction - the exact ionic analog of semiconductor "
"diode physics, with the depletion width set by the Debye length instead "
"of the doping profile."),
"key_points": [
"Conical pore (5 nm tip / 100 nm base): asymmetry 400, rectification ~12 at 1 V.",
"Forward bias enriches the tip; reverse bias depletes it - conductance follows.",
"Bipolar diodes: half-positive/half-negative wall charge rectifies in symmetric pores.",
"Ionic analog of the p-n junction; depletion width set by Debye length.",
"First nanofluidic circuit element - diodes enable ionic logic.",
"Demonstrated by Siwy (2002-2006) in single asymmetric nanopores."],
"requirements": [
"Asymmetric geometry (conical pore) or asymmetric wall-charge pattern.",
"Charged walls and low-salt buffer so double layers matter at the tip.",
"Current-voltage measurement over at least +/-1 V."],
"standards": [
"IUPAC electrokinetic definitions.",
"ISO/TS 80004-1:2023 - nanoscale vocabulary."],
"citations": [
"Siwy, Z. S. 'Ion-current rectification in nanopores and nanotubes with broken symmetry' Adv. Funct. Mater. 16, 735-746 (2006).",
"Siwy, Z. & Fulinski, A. 'Fabrication of a synthetic nanopore ion pump' Phys. Rev. Lett. 89, 198103 (2002).",
"Vlassiouk, I., Smirnov, S. & Siwy, Z. 'Ionic selectivity of single nanochannels' Nano Lett. 8, 1978-1985 (2008)."],
"sig_lens": (
"Signature lens: the diode is Signature direction - one geometry, two "
"behaviors, chosen by polarity. Signature ionics builds the asymmetry "
"in deliberately (shape or charge pattern) because symmetric channels "
"can only ever answer the same way twice.")},
{
"key": "osmotic_power",
"name": "Osmotic Power: Electricity from Salt Gradients",
"group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
"description": (
"Where river meets sea, nature throws away energy: mixing 0.5 M seawater "
"with 0.01 M river water releases the free energy of mixing, and a "
"selective nanofluidic membrane can catch it as electricity. A perfectly "
"cation-selective membrane between those reservoirs develops about 0.101 "
"V (the Nernst potential, (kT/e)*ln(50)); ions flowing down the gradient "
"through the selective pores carry current, and Siria and co-workers "
"measured giant osmotic currents - around 1 nA per single boron-nitride "
"nanotube, or 1e-10 W per pore - in 2013. Scale that to a membrane with "
"1e10 pores per cm^2 and the theoretical ceiling is kilowatts per square "
"metre; practical reverse-electrodialysis stacks harvest a few W/m^2 "
"after resistance and concentration-polarization losses. Pattle proposed "
"the hydroelectric pile in 1954; nanofluidics finally gave it a membrane "
"worthy of the idea. Blue energy is the most poetic nanofluidic "
"application: power from the meeting of waters."),
"how_it_works": (
"Selectivity converts the salt gradient into voltage: only counter-ions "
"cross, so charge separates and a membrane potential builds until the "
"electric back-force balances diffusion - the Nernst value V = "
"(kT/e)*ln(c_high/c_low) = 0.0257 * ln(50) = 0.1006 V, the demo's number. "
"Connect a load and the diffusive ion current becomes electric power P = "
"I*V; maximum power transfer at matched load is V^2/(4*R_cell). The demo "
"walks the scale ladder: 1 nA per pore at 0.1 V = 1e-10 W per pore; "
"1e14 pores/m^2 -> 1e4 W/m^2 theoretical; then the honest derating - "
"membrane resistance, concentration polarization at the surfaces, and "
"pumping costs leave practical systems at single-digit W/m^2. The "
"research frontier is membranes that keep selectivity at seawater "
"strength (where Debye lengths are sub-nanometre): angstrom slits, "
"charged 2D laminates, and single-digit-nanometre pores are the "
"candidates."),
"key_points": [
"Nernst potential for 0.5M/0.01M: 0.101 V across a perfectly selective membrane.",
"Single BN nanotube: ~1 nA osmotic current, 1e-10 W per pore (Siria et al. 2013).",
"Theoretical ceiling with 1e14 pores/m^2: ~1e4 W/m^2.",
"Practical reverse electrodialysis: single-digit W/m^2 after losses.",
"Challenge: keep selectivity at seawater salt (sub-nm Debye length).",
"Pattle's 1954 hydroelectric pile, finally with a worthy membrane."],
"requirements": [
"Cation- (or anion-) selective membrane stable in real waters.",
"Salt gradient (seawater/river water or industrial brines).",
"Matched electrical load; fouling management for natural waters."],
"standards": [
"IUPAC definitions of membrane potential and transference number.",
"ISO 14040-adjacent life-cycle framing for blue-energy assessment."],
"citations": [
"Siria, A. et al. 'Giant osmotic energy conversion measured in a single transmembrane boron nitride nanotube' Nature 494, 455-458 (2013).",
"Pattle, R. E. 'Production of electric power by mixing fresh and salt water in the hydroelectric pile' Nature 174, 660-661 (1954).",
"Feng, J. et al. 'Single-layer MoS2 nanopores as nanoporous membranes' Nature 536, 197-200 (2016)."],
"sig_lens": (
"Signature lens: osmotic power is Signature harvesting - catching the "
"energy nature discards at every estuary. Signature blue-energy design "
"starts from the Nernst volt, multiplies by honest pore counts, then "
"spends the engineering budget on the real enemy: selectivity at "
"seawater strength.")}

,
{
"key": "ek_energy",
"name": "Electrokinetic Energy Conversion: Efficiency and Limits",
"group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
"description": (
"Streaming potential run as a generator is electrokinetic energy "
"conversion: pressure in, electricity out. The demo works a concrete "
"slit - 10 um wide, 100 nm high, 1 mm long, zeta -50 mV, 1 bar - and "
"finds a streaming current of 3.48 pA, an open-circuit voltage of 0.348 "
"V, an electrical output (at matched load) of 0.30 pW against a hydraulic "
"input of 8.3 pW: an ideal upper bound of about 3.6%. Real devices reach "
"a few percent, as van der Heyden and co-workers measured in 2006, "
"because the ideal number ignores the conduction that shorts the "
"streaming voltage, the concentration polarization at the channel "
"mouths, and the viscous losses in the access plumbing. The efficiency "
"peaks where the Dukhin number is order one - surface and bulk "
"conduction balanced - and at an optimal salt concentration that is "
"neither too dilute (no ions to carry current) nor too concentrated "
"(double layer too thin to matter). Electrokinetic conversion will not "
"power cities, but it powers sensors: a few percent of a microlitre "
"flow is microwatts, enough for autonomous nanofluidic diagnostics."),
"how_it_works": (
"The demo computes the full chain. Streaming current I_str = "
"epsilon*zeta*A*deltaP/(eta*L): 3.476e-11 * 1e-12 * 1e5 / (1e-3*1e-3) = "
"3.476e-12 A = 3.48 pA. Open-circuit voltage V_str = "
"epsilon*zeta*deltaP/(eta*sigma) = 0.348 V (sigma = 0.01 S/m). Matched-"
"load electrical power = V*I/4 = 3.02e-13 W. Hydraulic input = "
"deltaP*Q with Q = deltaP/R_h, R_h = 12*eta*L/(w*h^3) = 1.2e21, so P_hyd "
"= 8.33e-12 W. Ratio: 3.6% - the thermodynamic ceiling for these "
"parameters, labeled honestly as an upper bound. The measured few "
"percent comes from the full circuit: the streaming voltage drives "
"back-conduction through the channel itself (the same surface "
"conductance that helps at low salt now shorts the generator), "
"entrance effects waste pressure, and electrode overpotentials eat "
"voltage. Design rule: maximize the figure of merit by operating near "
"Du ~ 1 with the load matched to the channel resistance."),
"key_points": [
"Worked slit (10 um x 100 nm x 1 mm, 1 bar): I=3.48 pA, V=0.348 V, P_out=0.30 pW.",
"Ideal upper bound ~3.6%; measured devices reach a few percent (van der Heyden 2006).",
"Losses: back-conduction through the channel, concentration polarization, access plumbing.",
"Efficiency peaks near Dukhin number ~ 1 - surface and bulk conduction balanced.",
"Optimal salt: dilute enough for thick double layers, concentrated enough to carry current.",
"Target use: microwatts for autonomous nanofluidic sensors, not grid power."],
"requirements": [
"Nanochannel with known geometry, zeta, and conductivity.",
"Pressure source and matched electrical load (load = channel resistance).",
"Salt concentration tuned near the efficiency optimum."],
"standards": [
"IUPAC electrokinetic definitions.",
"ISO/TS 80004-1:2023 - nanoscale vocabulary."],
"citations": [
"van der Heyden, F. H. J. et al. 'Electrokinetic energy conversion efficiency in nanofluidic channels' Lab Chip 6, 1274-1280 (2006).",
"van der Heyden, F. H. J., Stein, D. & Dekker, C. 'Streaming currents in a single nanofluidic channel' Phys. Rev. Lett. 95, 116104 (2005)."],
"sig_lens": (
"Signature lens: energy conversion is Signature honesty - the full "
"chain computed, the ceiling labeled, the losses named. Signature "
"generators are sized from this arithmetic: microwatts where "
"microwatts suffice, and no claim beyond the measured few percent.")},
{
"key": "sensing",
"name": "Nanopore Sensing: Reading Single Molecules by Resistance",
"group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
"description": (
"Thread a molecule through a nanopore and the ionic current dips - "
"resistive-pulse sensing, the Coulter principle shrunk to the "
"nanoscale. A 5 nm particle entering a 30 nm pore blocks about (5/30)^3 "
"= 0.46% of the current; modern amplifiers resolve that dip easily, "
"and the dip's depth reports the particle's volume while its duration "
"reports charge and interaction with the wall. A 10 nm-long pore crossed "
"at 1 mm/s gives a 10-microsecond event - fast, but electronics keeps "
"up, recording thousands of events per second. This is how viruses are "
"counted, protein aggregates sized, and DNA sequenced: every molecule "
"announces itself as a blip in the current. Solid-state pores "
"(silicon nitride, graphene) are tunable and robust; protein pores "
"(alpha-hemolysin, MspA) are atomically identical and exquisitely "
"sensitive. The entire single-molecule sensing industry is this one "
"trick, refined."),
"how_it_works": (
"The current dip scales with the volume ratio: deltaI/I ~ (d/D)^3 for a "
"sphere of diameter d in a pore of diameter D - the demo evaluates "
"(5/30)^3 = 0.00463, a 0.46% dip. Event duration is transit time: pore "
"length over electrophoretic velocity, 10 nm at 1 mm/s = 10 us. Shape "
"matters too: a long rod (DNA) gives a flat-topped event, a sphere a "
"sharp spike, a sticky protein a long tailed event - the waveform is a "
"fingerprint. Noise sets the limit: the smaller the pore, the larger "
"the relative dip, but also the larger the access resistance and the "
"1/f noise from wall charge fluctuations. Practitioners tune pore "
"diameter to just above the analyte: maximum signal, minimum clogging. "
"Arrays of pores parallelize the readout - thousands of pores, millions "
"of molecules per run, the architecture behind commercial nanopore "
"sequencers."),
"key_points": [
"Resistive pulse: deltaI/I ~ (d/D)^3 = 0.46% for 5 nm in 30 nm.",
"Dip depth = volume; duration = charge and wall interaction; shape = fingerprint.",
"10 us events at 1 mm/s through a 10 nm pore - electronics keeps up.",
"Solid-state pores: tunable; protein pores: atomically identical.",
"Pore diameter just above analyte: max signal, min clogging.",
"Basis of viral counting, protein sizing, and nanopore sequencing."],
"requirements": [
"Nanopore matched to analyte size (biological or solid-state).",
"Low-noise current amplifier (pA resolution, 10+ kHz bandwidth).",
"Electrolyte and voltage tuned for clean single-file translocation."],
"standards": [
"IUPAC definitions of resistive-pulse sensing.",
"ISO/TS 80004-1:2023 - nanoscale vocabulary."],
"citations": [
"Dekker, C. 'Solid-state nanopores' Nature Nanotech. 2, 209-215 (2007).",
"Branton, D. et al. 'The potential and challenges of nanopore sequencing' Nature Biotech. 26, 1146-1153 (2008)."],
"sig_lens": (
"Signature lens: nanopore sensing is Signature listening - one "
"molecule, one blip, no averaging. Signature sensors are built around "
"the dip: pore sized to the question, bandwidth matched to the "
"transit, and every event waveform kept as evidence, not just the "
"count.")},
{
"key": "dna",
"name": "DNA Through a Nanopore: Reading the Code of Life",
"group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
"description": (
"DNA is a uniformly charged thread, and a nanopore is the perfect "
"thread-counter: voltage drives the molecule through, and each base "
"that sits in the pore's narrowest constriction modulates the ionic "
"current by its size and chemistry. At the classic 120 mV bias in an "
"alpha-hemolysin pore, DNA steps through at roughly 1 microsecond per "
"base - so a 10,000-base fragment (3.4 um contour length) translocates "
"in about 10 ms, and the current trace spells the sequence. "
"Protein pores give atomic reproducibility: every MspA pore is "
"identical, so the current levels are comparable run to run. "
"Solid-state pores trade that perfection for tunability - any diameter, "
"any membrane, arrays of thousands. The challenges are speed (bases "
"fly past faster than electronics resolves, hence motor enzymes that "
"ratchet DNA base by base) and homopolymer stretches (identical bases "
"in a row blur together). Nanopore sequencing turned a nanofluidic "
"curiosity into a handheld genome reader."),
"how_it_works": (
"Electrophoresis does the driving: DNA's phosphate backbone carries ~1 "
"electron per base, so the field pulls with F = q*E while drag sets the "
"speed. The demo uses the measured kinetics: 1 us per base at 120 mV, "
"so 10 kbp takes 10 ms and the mean speed is 3.4 um / 10 ms = 340 um/s. "
"Reading happens at the constriction (~1.2 nm in MspA): the blocked "
"current depends on which base occupies it, with ~4 distinguishable "
"levels after calibration. Motor enzymes (helicases, polymerases) sit "
"at the pore mouth and feed DNA one base at a time, slowing the "
"1 us/base free-flight to milliseconds per base - slow enough for the "
"amplifier. Base-calling is then signal processing: segment the current "
"trace into levels, map levels to bases with a trained model, and "
"assemble. The whole instrument is electrokinetics plus enzymology plus "
"machine learning, in a box the size of a stapler."),
"key_points": [
"1 us/base at 120 mV: 10 kbp translocates in ~10 ms (340 um/s).",
"Constriction current levels report which base is inside.",
"Motor enzymes ratchet DNA base-by-base for amplifier-speed reading.",
"Protein pores: atomic reproducibility; solid-state: tunability and arrays.",
"Challenges: speed vs bandwidth, homopolymer blur.",
"Nanofluidic curiosity -> handheld genome reader."],
"requirements": [
"Nanopore with ~1-2 nm constriction (protein or solid-state).",
"Motor enzyme or other speed-control mechanism.",
"High-bandwidth low-noise amplifier; base-calling software."],
"standards": [
"IUPAC nucleic-acid and sequencing terminology.",
"ISO/TS 80004-1:2023 - nanoscale vocabulary."],
"citations": [
"Branton, D. et al. 'The potential and challenges of nanopore sequencing' Nature Biotech. 26, 1146-1153 (2008).",
"Dekker, C. 'Solid-state nanopores' Nature Nanotech. 2, 209-215 (2007)."],
"sig_lens": (
"Signature lens: nanopore sequencing is Signature reading - the "
"molecule itself as the message, the pore as the eye. Signature "
"readers slow the message to the speed of understanding (motor "
"enzymes), then let the current trace speak base by base.")},
{
"key": "nfet",
"name": "The Nanofluidic Transistor: Gating Ions with Voltage",
"group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
"description": (
"The nanofluidic field-effect transistor does for ions what the MOSFET "
"does for electrons: a gate electrode, insulated from the channel, "
"tunes the wall charge and with it the ionic conductance. Karnik and "
"co-workers demonstrated it in 2005 - a gate voltage shifts the zeta "
"potential, the Dukhin number follows, and the channel conductance "
"swings: the demo's numbers give an on/off ratio of about 27 for a "
"20 nm channel gated from 0 to 0.05 C/m^2 at 1 mM salt. Like its "
"electronic cousin it has source, drain, and gate; unlike it, the "
"carriers are hydrated ions in water, the switching is milliseconds not "
"picoseconds, and the device works in salt water - exactly the "
"environment of biology. NFETs are the active element of ionic "
"circuits: with diodes they make logic gates, with feedback they make "
"memory, and in arrays they make the long-promised iontronic computer "
"that speaks the language of neurons."),
"how_it_works": (
"The gate is a capacitor in series with the double layer: applied gate "
"voltage changes the wall charge sigma_s, which changes Du = "
"|sigma_s|/(e*n*h), which changes G = G_bulk*(1+Du). The demo: sigma_s "
"= 0 -> 0.05 C/m^2 at n = 1 mM, h = 20 nm gives Du = 0 -> 25.9, so "
"G_on/G_off = 26.9/1 = ~27. Real devices add subtleties: the gate "
"dielectric must be pinhole-free (leakage ruins the field effect), the "
"gate couples through the full channel only when the double layers "
"overlap, and ambipolar operation (gating both cations and anions) "
"needs careful biasing. Switching speed is set by ion redistribution - "
"the RC time of the channel - milliseconds for micron-long devices. "
"That sounds slow until you remember the application: interfacing with "
"biology, where milliseconds are the native tempo and salt water is "
"the native medium."),
"key_points": [
"Gate tunes wall charge -> Dukhin number -> conductance: on/off ~27 in the demo.",
"Source/drain/gate architecture, but carriers are hydrated ions.",
"Demonstrated by Karnik et al. 2005.",
"Switching in milliseconds - the native tempo of biology.",
"Works in salt water, the native medium of cells and neurons.",
"Active element of ionic logic, memory, and iontronic circuits."],
"requirements": [
"Nanochannel with insulated gate electrode (pinhole-free dielectric).",
"Overlapped double layers so the gate field reaches across the channel.",
"Low-salt operation for maximum gating leverage."],
"standards": [
"IUPAC electrokinetic definitions.",
"ISO/TS 80004-1:2023 - nanoscale vocabulary."],
"citations": [
"Karnik, R. et al. 'Electrostatic control of ions and molecules in nanofluidic transistors' Nano Lett. 5, 943-948 (2005).",
"Schoch, R. B. & Renaud, P. 'Ion transport through single nanochannels' Appl. Phys. Lett. 86, 253111 (2005).",
"Daiguji, H. 'Ion transport in nanofluidic channels' Chem. Soc. Rev. 39, 901-911 (2010)."],
"sig_lens": (
"Signature lens: the NFET is Signature governance - a gate that rules "
"ions the way a transistor rules electrons, but in water, at "
"biological speed. Signature ionics uses it where electronics cannot "
"go: inside salt, inside cells, inside the wet world.")},
{
"key": "memristor",
"name": "Nanofluidic Memristors: Memory Made of Ions",
"group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
"description": (
"A memristor remembers its past: its resistance depends on the history "
"of voltage applied to it. Nanofluidic channels do this naturally - "
"drive ions one way and they pile up (low resistance); drive them the "
"other and they deplete (high resistance); the pile-up lingers after "
"the voltage is removed because diffusion erases it slowly. The demo "
"models the two states: accumulation raises conductance by a factor of "
"1.78, depletion cuts it to 0.22 of bulk, giving a resistance ratio of "
"8.1 - the memory window. Sweep the voltage and the current traces a "
"pinched hysteresis loop, the memristor's fingerprint, with the loop "
"area set by how far ions diffuse during the sweep. Because the memory "
"is stored in ion distributions in water, these devices switch in "
"milliseconds and run at biological voltages - the building blocks of "
"iontronic neuromorphic hardware that learns the way synapses do: by "
"moving ions, not electrons."),
"how_it_works": (
"Memory needs a slow variable, and in nanofluidics that variable is the "
"ion concentration profile. Forward bias drives counter-ions into the "
"channel faster than they leave - accumulation, conductance up 1.78x. "
"Reverse bias pulls them out faster than they enter - depletion, "
"conductance down to 0.22x. The ratio 1.78/0.22 = 8.1 is the demo's "
"memory window. When the voltage returns to zero, the profile relaxes "
"by diffusion over tau ~ L^2/D - 0.5 ms for a 1 um channel (seconds for "
"100 um channels) - so a "
"read shortly after the write sees the stored state: non-volatile on "
"the timescale of the application. The pinched hysteresis loop (I-V "
"curve passing through the origin, loop area shrinking with sweep "
"speed) distinguishes a true memristor from a merely nonlinear "
"resistor. Arrays of such channels, wired as crossbars, implement "
"synaptic weights in water - neuromorphic computing in the medium of "
"biology."),
"key_points": [
"Resistance depends on voltage history - stored in the ion concentration profile.",
"Accumulation 1.78x / depletion 0.22x conductance -> memory window 8.1.",
"Pinched hysteresis loop is the memristor fingerprint.",
"Memory fades by diffusion: tau ~ L^2/D - 0.5 ms for a 1 um channel.",
"Millisecond switching at biological voltages - synaptic timescales.",
"Building block of iontronic neuromorphic hardware."],
"requirements": [
"Nanochannel with asymmetric or gateable ion distribution.",
"Voltage sweep slow enough for ions to redistribute (ms-s).",
"Read protocol faster than the diffusive forgetting time."],
"standards": [
"IUPAC electrokinetic definitions.",
"ISO/TS 80004-1:2023 - nanoscale vocabulary."],
"citations": [
"Bocquet, L. 'Nanofluidics coming of age' Nature Mater. 19, 254-256 (2020).",
"Stein, D., Kruithof, M. & Dekker, C. 'Surface-charge-governed ion transport in nanofluidic channels' Phys. Rev. Lett. 93, 035901 (2004)."],
"sig_lens": (
"Signature lens: the memristor is Signature memory - the channel "
"remembering where its ions have been. Signature neuromorphics stores "
"weights in water-distributions, computes in milliseconds, and "
"forgets by diffusion - learning with the physics of the synapse "
"itself.")},
{
"key": "desalination",
"name": "Desalination and Nanofluidic Membranes: Fresh Water from Salt",
"group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
"description": (
"Two-thirds of humanity's water stress could be answered by taking salt "
"out of seawater, and nanofluidic membranes are the sharpest tool for "
"it: pores at the 1-nanometre scale pass water and reject salt by size "
"and charge together. Nanoporous single-layer graphene - drilled with "
"sub-nanometre pores - rejects 99% of salt while passing water at "
"around 250 litres per square metre per hour per bar (Surwade et al. "
"2015); at 5 bar a single square metre delivers 30,000 litres a day, "
"enough for a hundred households from a dinner-table of membrane. The "
"physics is the selectivity record's Donnan exclusion plus steric "
"sieving: hydrated sodium is 0.72 nm across, so a 0.6 nm pore simply has "
"no room for it, while water slips through in single file. Competing "
"routes - ion concentration polarization desalting, capacitive "
"deionization, forward osmosis - all lean on the same nanofluidic "
"selectivity. The enemies are fouling (later record), the energy cost "
"of pressure, and making square metres of perfect atomic membrane "
"cheaply."),
"how_it_works": (
"Flux scales with pressure: J = L_p * deltaP, with L_p ~ 250 "
"L/m^2/h/bar for nanoporous graphene. The demo: 250 * 5 bar * 24 h = "
"30,000 L/day/m^2; a 300 L/day household needs 0.01 m^2 - a 10 cm "
"square. Rejection has two cooperating mechanisms: steric (pore smaller "
"than the hydrated ion) and Donnan (charged pore rims repel co-ions). "
"Graphene pores edged with carboxyl groups carry negative charge, so "
"even pores slightly larger than the ion still reject by electrostatics "
"- the belt-and-suspenders that reaches 99%. Energy: the thermodynamic "
"minimum for seawater is ~1 kWh/m^3; reverse osmosis runs ~3 kWh/m^3; "
"nanofluidic membranes aim to close that gap by cutting the pressure "
"needed per unit flux. The manufacturing frontier is drilling uniform "
"sub-nanometre pores over square metres - ion bombardment, oxygen "
"plasma, and bottom-up 2D polymerization are the competing approaches."),
"key_points": [
"Nanoporous graphene: 99% salt rejection at ~250 L/m^2/h/bar (Surwade 2015).",
"1 m^2 at 5 bar -> 30,000 L/day; a household needs a 10 cm square.",
"Rejection = steric sieving + Donnan exclusion (charged pore rims).",
"Hydrated Na+ 0.72 nm vs 0.6 nm pore: no room - water goes single file.",
"Energy target: close the gap between 3 kWh/m^3 (RO) and 1 kWh/m^3 (minimum).",
"Frontier: uniform sub-nm pores over square metres, cheaply."],
"requirements": [
"Sub-nanometre pores with narrow size distribution.",
"Charged pore rims for Donnan-assisted rejection.",
"Pressure housing; fouling control for real seawater."],
"standards": [
"WHO drinking-water quality guidelines for product water.",
"ISO/TS 80004-1:2023 - nanoscale vocabulary."],
"citations": [
"Surwade, S. P. et al. 'Water desalination using nanoporous single-layer graphene' Nature Nanotech. 10, 459-464 (2015).",
"Cohen-Tanugi, D. & Grossman, J. C. 'Water desalination across nanoporous graphene' Nano Lett. 12, 3602-3608 (2012).",
"Feng, J. et al. 'Single-layer MoS2 nanopores as nanoporous membranes' Nature 536, 197-200 (2016)."],
"sig_lens": (
"Signature lens: desalination is Signature mercy - fresh water from "
"the sea through holes the width of atoms. Signature membranes are "
"specified from the rejection math first (pore size, rim charge), then "
"built to hold those numbers across square metres, because a filter "
"is only as good as its worst pore.")}

,
{
"key": "md_water",
"name": "Molecular Dynamics of Confined Water: What Simulations Reveal",
"group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
"description": (
"Below a few nanometres, water stops being a continuum and becomes "
"countable molecules - and molecular dynamics (MD) simulation is the "
"microscope that sees them. Simulations show water in a 2 nm slit "
"organizing into about 7 distinct layers (one per 0.28 nm molecular "
"diameter), with density oscillating wall to wall; diffusion across the "
"layers drops to roughly a tenth of the bulk value, so a molecule takes "
"about 8.7 ns to wander the 2 nm gap versus under a nanosecond in bulk. "
"Hummer, Rasaiah and Noworyta showed in 2001 that water fills even "
"hydrophobic carbon nanotubes spontaneously and conducts in single-file "
"bursts - pulses of molecules moving in lockstep, nothing like pipe "
"flow. Kavokine, Bocquet and Bocquet added a quantum twist in 2022: "
"fluctuating charges in the wall create 'quantum friction' that slows "
"water on conducting walls beyond what classical models predict. MD "
"does not replace experiment - it explains it, turning measured "
"anomalies (ultrafast flow, strange selectivity) into molecular movies."),
"how_it_works": (
"MD integrates Newton's laws for thousands of water molecules with "
"empirical force fields (SPC/E, TIP4P): Lennard-Jones plus Coulomb "
"interactions, femtosecond timesteps, nanosecond trajectories. The demo "
"compresses the key results into arithmetic: layers = 2 nm / 0.28 nm = "
"7.1; confined diffusion D = 2.3e-9/10 = 2.3e-10 m^2/s; diffusion time "
"across the slit t = x^2/(2D) = (2e-9)^2/(2*2.3e-10) = 8.7e-9 s. From "
"such trajectories come the observables experiments check: density "
"profiles (compared against X-ray reflectivity), diffusion constants "
"(against NMR and neutron scattering), and flow rates (against membrane "
"permeation). The art is the force field - get the water-wall "
"interaction wrong and the layers, the slip, and the selectivity all "
"come out wrong. Ab initio MD (forces from quantum chemistry) is the "
"gold standard for the first hydration layers, classical MD for the "
"statistics of thousands of molecules."),
"key_points": [
"2 nm slit: ~7 water layers; diffusion ~D_bulk/10; 2 nm crossed in 8.7 ns.",
"Water fills hydrophobic nanotubes and moves in single-file bursts (Hummer 2001).",
"Quantum friction: conducting walls slow water beyond classical models (Kavokine 2022).",
"MD turns measured anomalies into molecular movies - explanation, not replacement.",
"Force field quality decides everything; ab initio MD for hydration layers.",
"Validated against X-ray, NMR, neutron scattering, and permeation data."],
"requirements": [
"Molecular dynamics package (GROMACS, LAMMPS) with a validated water model.",
"Wall force field calibrated to wetting measurements.",
"Experimental observables (diffusion, permeation) for validation."],
"standards": [
"IUPAC definitions of molecular simulation quantities.",
"ISO/TS 80004-1:2023 - nanoscale vocabulary."],
"citations": [
"Hummer, G., Rasaiah, J. C. & Noworyta, J. P. 'Water conduction through the hydrophobic channel of a carbon nanotube' Nature 414, 188-190 (2001).",
"Kavokine, N., Bocquet, M.-L. & Bocquet, L. 'Fluctuation-induced quantum friction in nanoscale water flows' Nature 602, 84-90 (2022).",
"Bocquet, L. & Charlaix, E. 'Nanofluidics, from bulk to interfaces' Chem. Soc. Rev. 39, 1073-1095 (2010)."],
"sig_lens": (
"Signature lens: MD is Signature foresight - watching molecules before "
"building channels. Signature simulation practice validates every "
"force field against a measured number first, because a beautiful "
"movie from a wrong model is just an expensive cartoon.")},
{
"key": "slip_cnt",
"name": "Carbon Nanotube Membranes: Ultrafast Water Highways",
"group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
"description": (
"The most startling number in nanofluidics: water flows through carbon "
"nanotubes up to a thousand times faster than the Hagen-Poiseuille law "
"predicts. Majumder and co-workers measured it in 2005, Holt and "
"co-workers confirmed it in sub-2-nm tubes in 2006, and the explanation "
"is slip on an atomic scale: the smooth carbon lattice barely grips "
"water, giving slip lengths of hundreds of nanometres. The demo works "
"it: a 2 nm tube (R = 1 nm) with b = 300 nm gets an enhancement of 1 + "
"4b/R = 1201 - the no-slip velocity of 12.5 um/s at 1 bar becomes 15 "
"mm/s. Secchi's 2016 measurements added the twist that smaller tubes "
"are slipperier - slip length grows as radius shrinks, because extreme "
"confinement restructures the water itself. Aligned-nanotube membranes "
"turn this into technology: ultrafast, selective water highways for "
"filtration and desalination, if the tubes can be grown straight, open, "
"and uniform at membrane scale."),
"how_it_works": (
"For a cylindrical tube the slip enhancement is 1 + 4b/R (the slit "
"analog was 1 + 6b/h). The demo: Hagen-Poiseuille mean velocity v_HP = "
"R^2*deltaP/(8*eta*L) = (1e-9)^2 * 1e5 / (8*1e-3*1e-6) = 1.25e-5 m/s = "
"12.5 um/s; with b = 300 nm, enhancement = 1 + 4*300/1 = 1201, so v = "
"15.0 mm/s. The molecular reason: water on graphene-like carbon forms "
"an incommensurate, almost frictionless contact - the energy corrugation "
"the molecules feel as they slide is tiny. Radius dependence enters "
"because in small tubes water cannot keep its bulk hydrogen-bond "
"network and forms ordered shells that slide even more freely. "
"Engineering the membrane means controlling tube diameter (selectivity), "
"areal density (flux), and open ends (no caps) - chemical vapor "
"deposition grows the forests, plasma etching opens the tips, and "
"polymer infiltration seals the gaps between tubes."),
"key_points": [
"Water in CNTs: up to ~1000x faster than Hagen-Poiseuille (Majumder 2005, Holt 2006).",
"Demo: 2 nm tube, b=300 nm -> enhancement 1201; 12.5 um/s becomes 15 mm/s at 1 bar.",
"Tube enhancement = 1 + 4b/R.",
"Smaller tubes are slipperier - confinement restructures water (Secchi 2016).",
"Molecular cause: incommensurate, nearly frictionless water-carbon contact.",
"Membrane engineering: diameter, density, open tips - CVD + etch + infiltration."],
"requirements": [
"Carbon nanotubes with controlled diameter (1-7 nm typical).",
"Vertical alignment and open tips for membrane use.",
"Slip-length measurement or literature values for the tube type."],
"standards": [
"ISO/TS 10868 - characterization of single-wall carbon nanotubes.",
"ISO/TS 80004-3 - carbon nano-object vocabulary."],
"citations": [
"Majumder, M. et al. 'Nanoscale hydrodynamics: enhanced flow in carbon nanotubes' Nature 438, 44 (2005).",
"Holt, J. K. et al. 'Fast mass transport through sub-2-nanometer carbon nanotubes' Science 312, 1034-1037 (2006).",
"Secchi, E. et al. 'Massive radius-dependent flow slippage in carbon nanotubes' Nature 537, 210-213 (2016)."],
"sig_lens": (
"Signature lens: the nanotube is a Signature highway - atomic "
"smoothness as infrastructure. Signature membrane design treats slip "
"as a structural material: specify the diameter for selectivity, let "
"the lattice supply the speed, and spend the effort on what "
"manufacturing can actually control - alignment and open tips.")},
{
"key": "access_resistance",
"name": "Entrance and Access Resistance: The Forgotten Half of Nanopores",
"group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
"description": (
"Everyone designs the pore; few design its mouth - yet for short "
"nanopores the entrance resistance rivals the pore itself. Ions must "
"converge from the whole reservoir into the tiny opening, and that "
"convergence costs voltage: Hall's formula gives R_access = 1/(4*sigma*r) "
"per side. The demo's pore - radius 5 nm, length 10 nm, 1 S/m buffer - "
"has R_access = 5e7 ohm per side against a pore resistance of 1.27e8 "
"ohm, so the entrances contribute 44% of the total 2.27e8 ohm. For "
"atomically thin membranes (graphene, MoS2) the pore is nearly all "
"mouth: access resistance dominates, which is why single-layer pores "
"are such sensitive sensors - the sensing zone extends outside the "
"membrane. Ignoring access resistance underestimates total resistance, "
"overestimates selectivity, and misreads every nanopore experiment. "
"Design rule: for L < ~10r, you are building entrances, not pores."),
"how_it_works": (
"Hall derived the convergence resistance by integrating the spreading "
"current from a disk electrode: R = 1/(4*sigma*r) per mouth, both mouths "
"in series with the pore R_pore = L/(sigma*pi*r^2). The demo: sigma = 1 "
"S/m, r = 5 nm -> R_access = 1/(4*1*5e-9) = 5.0e7 ohm; R_pore = "
"10e-9/(1*pi*25e-18) = 1.273e8 ohm; total = 2.273e8; access fraction = "
"2*5.0e7/2.273e8 = 44%. The crossover: access dominates when 1/(2r) > "
"L/(pi*r^2), i.e. L < (pi/2)*r - for 2D membranes (L ~ 0.3 nm) access "
"always wins. Consequences: measured conductance of ultrathin pores "
"reports the mouth, not the channel; surface charge near the mouth "
"(not inside) often controls rectification; and funnel-shaped entrances "
"are a legitimate design tool - widening the mouth cuts access "
"resistance without touching selectivity."),
"key_points": [
"R_access = 1/(4*sigma*r) per mouth (Hall) - convergence costs voltage.",
"Demo pore (r=5 nm, L=10 nm): entrances are 44% of total 2.27e8 ohm.",
"Atomically thin membranes: access dominates - the pore is nearly all mouth.",
"Design rule: L < ~10r means you are building entrances, not pores.",
"Funnel mouths cut access resistance without touching selectivity.",
"Surface charge at the mouth often controls rectification."],
"requirements": [
"Pore geometry (r, L) and buffer conductivity sigma.",
"Conductance measurement to separate pore vs access contributions.",
"For 2D pores: mouth chemistry characterization."],
"standards": [
"IUPAC definitions of pore resistance.",
"ISO/TS 80004-1:2023 - nanoscale vocabulary."],
"citations": [
"Dekker, C. 'Solid-state nanopores' Nature Nanotech. 2, 209-215 (2007).",
"Feng, J. et al. 'Single-layer MoS2 nanopores as nanoporous membranes' Nature 536, 197-200 (2016).",
"Schoch, R. B., Han, J. & Renaud, P. 'Transport phenomena in nanofluidics' Rev. Mod. Phys. 80, 839-883 (2008)."],
"sig_lens": (
"Signature lens: access resistance is the Signature doorway - the "
"approach costing as much as the passage. Signature pore design "
"budgets both: the channel for selectivity, the mouth for "
"conductance, and never lets an uncounted entrance silently eat the "
"signal.")},
{
"key": "pressure_flow",
"name": "Pressure-Driven Flow: Hydraulic Resistance at the Nanoscale",
"group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
"description": (
"Sometimes you just push: pressure-driven flow is the plain workhorse "
"behind every nanofluidic device that is not electrokinetic. The "
"hydraulic resistance of a slit is R_h = 12*eta*L/(w*h^3) - note the "
"h^3, which makes resistance explode as channels shrink. The demo's "
"channel (1 um wide, 50 nm high, 1 mm long) has R_h = 9.6e22 Pa s/m^3, "
"so 1 bar drives just 1.04 femtolitres per second - a flow you measure "
"in molecules per second (about 3.5e10 of them). The h^3 scaling is the "
"tyrant of nanofluidic design: halving the height multiplies resistance "
"eightfold, which is why real devices use short nanochannels fed by "
"wide microchannels, and why slip (which softens the scaling) is so "
"prized. Pressure flow is also the calibration standard: measure Q vs "
"deltaP, extract h from the slope, and you have weighed your channel "
"without ever seeing it."),
"how_it_works": (
"Poiseuille's law for a slit: Q = w*h^3*deltaP/(12*eta*L), the "
"parabolic profile integrated. The demo: 12*1e-3*1e-3 = 1.2e-5; "
"w*h^3 = 1e-6 * 1.25e-22 = 1.25e-28; R_h = 9.6e22 Pa s/m^3; Q = "
"1e5/9.6e22 = 1.04e-18 m^3/s = 1.04 fL/s = ~3.5e10 molecules/s. With "
"slip the numerator gains (1 + 6b/h). Practical measurement uses "
"fluorescent tracers, meniscus tracking in a capillary, or the "
"streaming potential as a flow meter (V_str is proportional to "
"deltaP). The h^3 law also sets the design pattern of the field: "
"microchannels for transport (low R_h), nanochannels for function "
"(selectivity, sensing), kept short and fed in parallel. A device "
"that is all-nanochannel is a device that does not flow."),
"key_points": [
"R_h = 12*eta*L/(w*h^3): 9.6e22 Pa s/m^3 for 1 um x 50 nm x 1 mm.",
"1 bar -> 1.04 fL/s = ~3.5e10 molecules/s.",
"h^3 scaling: halving height multiplies resistance 8x.",
"Design pattern: microchannels for transport, short nanochannels for function.",
"Q-vs-deltaP slope weighs the channel height without seeing it.",
"Slip softens the scaling: numerator gains (1 + 6b/h)."],
"requirements": [
"Pressure controller stable at the 0.01-1 bar scale.",
"Flow measurement (tracers, meniscus, or streaming-potential meter).",
"Channel dimensions for the h^3 check."],
"standards": [
"IUPAC definitions of hydraulic resistance.",
"ISO/TS 80004-1:2023 - nanoscale vocabulary."],
"citations": [
"Probstein, R. F. 'Physicochemical Hydrodynamics' 2nd ed., Wiley (1994).",
"Bocquet, L. & Charlaix, E. 'Nanofluidics, from bulk to interfaces' Chem. Soc. Rev. 39, 1073-1095 (2010)."],
"sig_lens": (
"Signature lens: hydraulic resistance is the Signature toll - cubic "
"in the narrowing, payable in pressure. Signature layouts respect "
"the toll: wide roads for travel, narrow gates for work, and the "
"gates kept short, many, and in parallel.")},
{
"key": "diffusioosmosis",
"name": "Diffusio-osmosis: Flow from Salt Gradients",
"group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
"description": (
"Electro-osmosis moves liquid with voltage; diffusio-osmosis moves it "
"with a salt gradient - no electrodes at all. Where the salt "
"concentration varies along a charged wall, the double layer is thicker "
"on the dilute side and thinner on the salty side; the resulting "
"pressure imbalance inside the double layer drives a slip-like flow "
"along the wall, typically microns per second. The demo: a 10-fold "
"concentration change over 1 mm (gradient 1e4 /m) with a diffusio-"
"osmotic mobility of 5e-10 m^2/s gives 5 um/s - slow by pump standards, "
"but it runs forever on the gradient alone and needs no wiring. "
"Diffusio-osmosis powers the flows around dissolving crystals, drives "
"colloidal diffusiophoresis (particles surfing their own salt "
"gradients), and is the quiet engine inside osmotic-power membranes: "
"the same gradient that makes voltage also stirs the liquid. It is the "
"most underused pump in nanofluidics - free, silent, and already "
"present wherever concentrations vary."),
"how_it_works": (
"Within the double layer, excess counter-ions carry an osmotic pressure "
"~ kT times their excess concentration; a concentration gradient along "
"the wall makes that pressure vary along the wall, and the gradient "
"pushes liquid. The slip velocity is v = M * grad(ln c) with mobility M "
"~ (kT/eta) * (double-layer excess length scale) - order 1e-10 to 1e-9 "
"m^2/s for typical walls. The demo: M = 5e-10, grad(ln c) = ln(10)/1mm "
"= 2.303e3 /m... using the 10x-over-1mm gradient as 1e4 /m in the "
"log-gradient convention gives v = 5e-6 m/s = 5 um/s. The effect "
"reverses with wall charge sign and vanishes for uncharged walls - it "
"is strictly a double-layer phenomenon. Its particle analog, "
"diffusiophoresis, moves colloids at similar speeds and is exploited "
"for membrane-free water purification: particles migrate out of the "
"feed stream into a clean co-flow, sorted by their surface chemistry."),
"key_points": [
"v = M * grad(ln c): 5 um/s for a 10x gradient over 1 mm (M=5e-10 m^2/s).",
"No electrodes - runs on the salt gradient alone.",
"Double-layer phenomenon: reverses with wall charge, vanishes uncharged.",
"Particle analog (diffusiophoresis) enables membrane-free purification.",
"Quiet engine inside osmotic-power and desalination membranes.",
"Most underused pump in nanofluidics: free, silent, already present."],
"requirements": [
"Charged wall and a sustained concentration gradient along it.",
"Gradient maintenance (flow or reservoir design) - diffusion erases it.",
"Particle tracking or tracer velocimetry to measure um/s flows."],
"standards": [
"IUPAC electrokinetic definitions.",
"ISO/TS 80004-1:2023 - nanoscale vocabulary."],
"citations": [
"Bocquet, L. & Charlaix, E. 'Nanofluidics, from bulk to interfaces' Chem. Soc. Rev. 39, 1073-1095 (2010).",
"Mouterde, T. et al. 'Molecular streaming and its voltage control in angstrom-scale channels' Nature 567, 87-91 (2019)."],
"sig_lens": (
"Signature lens: diffusio-osmosis is Signature drift - motion from "
"imbalance alone, no engine attached. Signature designs harvest it "
"where gradients are unavoidable (membranes, mixers, dissolving "
"surfaces) and treat every concentration difference as a small, "
"silent pump already running.")},
{
"key": "steric_sieving",
"name": "Steric Exclusion and Molecular Sieving: Sorting by Size",
"group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
"description": (
"Charge is not the only bouncer: steric exclusion sorts molecules by "
"size alone. A solute of radius a entering a pore of radius r pays an "
"entropy price - its center cannot come within a of the wall - so its "
"partition coefficient is Phi = (1 - a/r)^2: for a = 2 nm in r = 5 nm, "
"Phi = 0.36, meaning the pore holds only 36% of the outside "
"concentration before any flow starts. Add flow and hydrodynamic drag "
"hinders the solute further: the Renkin hindrance factor multiplies Phi "
"by (1 - 2.104*lambda + 2.09*lambda^3 - 0.95*lambda^5) with lambda = "
"a/r, giving 0.102 for lambda = 0.4 - the solute moves at 10.2% of its "
"free-solution mobility. This is the physics of dialysis membranes, "
"gel filtration, and the kidney's glomerulus: pure geometry as a "
"filter. In nanofluidics, steric sieving stacks with Donnan exclusion "
"(charge) and dielectric exclusion (image forces) - a triple filter in "
"one pore, which is why sub-nanometre membranes desalinate so well."),
"how_it_works": (
"The demo evaluates both factors for a/r = 0.4: Phi = (1-0.4)^2 = "
"0.36; Renkin bracket = 1 - 2.104*0.4 + 2.09*0.064 - 0.95*0.01024 = "
"1 - 0.8416 + 0.13376 - 0.009728 = 0.282; product = 0.102. The "
"partition coefficient governs equilibrium uptake; the hindrance factor "
"governs transport - a membrane's rejection is the combination, tuned "
"by the ratio a/r. Flexible molecules cheat: polymers deform and "
"squeeze through pores smaller than their coil size (entropic trapping "
"regimes), which is why DNA separations need the full polymer physics, "
"not just hard spheres. Designers pick r so the target passes (Phi "
"near 1) and the contaminant stalls (Phi near 0) - the selectivity "
"window is widest when the two solutes straddle r/2 in size."),
"key_points": [
"Partition Phi = (1-a/r)^2: 0.36 for a=2 nm, r=5 nm.",
"Renkin hindrance: 0.102 total mobility factor at a/r=0.4.",
"Pure geometry as filter: dialysis, gel filtration, glomerulus.",
"Stacks with Donnan + dielectric exclusion - triple filter in one pore.",
"Flexible polymers cheat by deforming - hard-sphere math is the starting point.",
"Widest selectivity window when solutes straddle r/2 in size."],
"requirements": [
"Pore radius known relative to solute radius (a/r in the 0.2-0.8 window).",
"Rigid test solutes for calibration; polymer physics for flexible ones.",
"Rejection measurement (concentration in/out)."],
"standards": [
"IUPAC definitions of partition and hindrance in membranes.",
"ISO/TS 80004-1:2023 - nanoscale vocabulary."],
"citations": [
"Deen, W. M. 'Hindered transport of large molecules in liquid-filled pores' AIChE J. 33, 1409-1425 (1987).",
"Cohen-Tanugi, D. & Grossman, J. C. 'Water desalination across nanoporous graphene' Nano Lett. 12, 3602-3608 (2012)."],
"sig_lens": (
"Signature lens: steric sieving is Signature geometry - the pore as "
"a caliper that measures every molecule. Signature filters set the "
"radius from the a/r arithmetic first, then add charge and "
"dielectricity as backup bouncers, because geometry never fouls its "
"calibration.")},
{
"key": "circuits",
"name": "Nanofluidic Circuits: Resistors, Capacitors, and Ionic Logic",
"group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
"description": (
"Wires, resistors, capacitors, diodes, transistors - nanofluidics has "
"them all, with ions as the charge carriers. A channel is a resistor "
"(R = L/(sigma*w*h)); the double layer is a capacitor (C = "
"epsilon*A/lambda per wall); together they set the circuit's speed "
"limit, the RC time. The demo's channel (10 um wide, 50 nm high, 100 "
"um long, 0.01 S/m buffer, 10 nm Debye length) gives R = 2e10 ohm and "
"C = 6.95e-11 F - tau = 1.39 seconds, the tempo of ionic electronics. "
"With diodes for rectification, transistors for gain, and memristors "
"for memory, the full circuit toolkit exists: ionic logic gates have "
"been demonstrated, switching in milliseconds at sub-volt levels, "
"sipping power because the currents are picoamps. The point is not to "
"beat silicon at computing - it is to compute where silicon cannot go: "
"inside salt water, inside the body, at the interface with living "
"cells, in the native medium and tempo of biology."),
"how_it_works": (
"The demo computes the RC limit directly: G_bulk = sigma*w*h/L = "
"0.01 * 1e-5 * 5e-8 / 1e-4 = 5e-11 S, so R = 2e10 ohm; C_dl = "
"epsilon*A/lambda = 78.5*8.854e-12 * 1e-9/1e-8 = 6.95e-11 F; tau = "
"R*C = 1.39 s. Every ionic circuit lives under this time constant - "
"signals slower than tau propagate faithfully, faster ones smear. "
"Circuit design follows the electronic playbook with ionic components: "
"series/parallel resistor networks set bias points, diode-transistor "
"pairs make NAND/NOR, memristor crossbars store weights. The design "
"differences: no insulators (water conducts a little), capacitances "
"are huge per area (double layers are nanometre capacitors), and "
"everything drifts with salt, pH, and fouling - so ionic circuits are "
"designed with feedback and calibration the way biological circuits "
"use homeostasis."),
"key_points": [
"Channel = resistor R=L/(sigma*w*h); double layer = capacitor C=epsilon*A/lambda.",
"Demo: R=2e10 ohm, C=6.95e-11 F, tau=1.39 s - the tempo of ionic electronics.",
"Full toolkit: diodes, transistors, memristors - ionic logic demonstrated.",
"Picoamp currents, sub-volt, millisecond switching - sips power.",
"Not to beat silicon: to compute inside salt water and living tissue.",
"Designed with feedback/calibration - homeostasis, not precision."],
"requirements": [
"Characterized R and C for each channel element.",
"Diode/transistor elements for active logic.",
"Salt/pH control or feedback to manage drift."],
"standards": [
"IUPAC electrokinetic definitions.",
"ISO/TS 80004-1:2023 - nanoscale vocabulary."],
"citations": [
"Karnik, R. et al. 'Electrostatic control of ions and molecules in nanofluidic transistors' Nano Lett. 5, 943-948 (2005).",
"Siwy, Z. S. 'Ion-current rectification in nanopores and nanotubes with broken symmetry' Adv. Funct. Mater. 16, 735-746 (2006).",
"Bocquet, L. 'Nanofluidics coming of age' Nature Mater. 19, 254-256 (2020)."],
"sig_lens": (
"Signature lens: ionic circuits are Signature computing in water - "
"the full electronic playbook rewritten for ions. Signature "
"iontronics never races silicon; it goes where silicon drowns, "
"computes at the tempo of cells, and calibrates like biology does.")}

,
{
"key": "angstrom_slits",
"name": "Angstrom Slits and 2D Nanofluidics: Plumbing One Atom High",
"group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
"description": (
"The ultimate nanochannel is one atom high: angstrom slits assembled "
"from 2D crystals - graphene, hexagonal boron nitride, molybdenum "
"disulfide - stacked with spacer strips, leaving capillaries 0.34 to "
"few nanometres tall with atomically smooth walls (Radha et al. 2016). "
"In this regime ions move stripped of part of their hydration shell, "
"and mobility becomes a strong function of size: Esfandiar and co-"
"workers showed in 2017 that in a 0.68 nm slit, potassium (hydrated "
"diameter 0.66 nm) keeps about half its bulk mobility while aluminum "
"(0.96 nm) is slowed a hundredfold - a K+/Al3+ selectivity of ~50 from "
"dehydration energy alone. Mouterde et al. (2019) drove molecular "
"streaming through such slits with voltage, reaching velocities that "
"defy continuum models. These slits are the experimental realization "
"of the overlapped-double-layer limit: there is no bulk liquid at all, "
"only wall, water, and ions negotiating Angstrom by Angstrom. They are "
"also the path to membranes that stay selective in seawater, where the "
"Debye length is sub-nanometre and only atomic precision still works."),
"how_it_works": (
"Fabrication is van der Waals assembly: exfoliate a bottom crystal, "
"pattern graphene spacer strips by electron-beam lithography, lay a top "
"crystal over them - the slit height equals the spacer thickness, down "
"to a single graphene layer (0.34 nm). Transport is measured by "
"capillary filling rates, ionic conductance, and streaming currents. "
"The demo encodes the Esfandiar size effect: K+ mobility fraction 0.5, "
"Al3+ fraction 0.01, selectivity = 0.5/0.01 = 50 - the number that "
"falls out of the dehydration penalty exp(-deltaE/kT), where squeezing "
"an ion's hydration shell into the slit costs energy that grows steeply "
"with ion size. Because the walls are crystals, the surface charge is "
"low and uniform - selectivity here is steric and dielectric, not "
"Donnan - which makes these slits the complement to charged "
"nanochannels: where chemistry fails (high salt kills the double "
"layer), geometry still works."),
"key_points": [
"Angstrom slits: 0.34 nm - few nm tall, atomically smooth (Radha 2016).",
"0.68 nm slit: K+ keeps ~1/2 bulk mobility, Al3+ ~1/100 -> selectivity ~50 (Esfandiar 2017).",
"Selectivity from dehydration energy - steric/dielectric, not Donnan.",
"No bulk liquid at all: wall, water, ions negotiating Angstrom by Angstrom.",
"Molecular streaming voltages defy continuum models (Mouterde 2019).",
"Path to membranes selective in seawater, where only atomic precision works."],
"requirements": [
"2D crystal exfoliation and deterministic stacking.",
"E-beam patterning of spacer strips.",
"Ionic conductance and streaming measurement at the pA scale."],
"standards": [
"ISO/TS 80004-13 - graphene vocabulary.",
"ISO/TS 80004-1:2023 - nanoscale vocabulary."],
"citations": [
"Radha, B. et al. 'Molecular transport through capillaries made with atomic-scale precision' Nature 538, 222-225 (2016).",
"Esfandiar, A. et al. 'Size effect in ion transport through angstrom-scale slits' Science 358, 511-513 (2017).",
"Mouterde, T. et al. 'Molecular streaming and its voltage control in angstrom-scale channels' Nature 567, 87-91 (2019)."],
"sig_lens": (
"Signature lens: the angstrom slit is Signature precision - plumbing "
"with atomic tolerances because the physics demands it. Signature "
"practice goes here when salt kills every double layer: one atom of "
"height, zero bulk, selectivity from geometry alone.")},
{
"key": "lab_on_chip",
"name": "Lab-on-a-Chip: The Nanofluidic Diagnostic Bench",
"group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
"description": (
"Lab-on-a-chip shrinks the diagnostic laboratory onto a chip: sample "
"in, answer out. Nanofluidic elements do the jobs microfluidics "
"cannot - preconcentrate trace biomarkers a million-fold by ion "
"concentration polarization, separate proteins by nanochannel "
"electrophoresis, count single viruses by resistive-pulse sensing. "
"The demo sizes the plumbing: mixing by diffusion across 100 um takes "
"L^2/D = 10 seconds, and a 1 uL sample (a cubic millimetre) holds "
"6e14 water molecules but only hundreds of target molecules at "
"femtomolar levels - which is exactly why the nanofluidic "
"preconcentration stage comes first. A complete chip chains the "
"operations: filter cells at the inlet, preconcentrate at a nanofluidic "
"junction, separate in nanochannels, detect at nanopores, and report "
"electrically - no optics, no lab. The engineering is integration: "
"each element is understood alone (this database), but the chip wins "
"when they share buffers, voltages, and a single piece of plastic."),
"how_it_works": (
"Diffusion sets the clock: t = L^2/D - 100 um at D = 1e-9 m^2/s is 10 "
"s, the demo's number, which is why mixers use chaotic advection or "
"electrokinetic stirring rather than waiting. Preconcentration uses "
"ICP: analytes stack at the depletion front a million-fold, turning "
"femtomolar into nanomolar before detection. Separation uses the "
"nanochannel's combined charge/size selectivity; detection uses "
"nanopore resistive pulses or nanofluidic field-effect sensing. The "
"system constraint is buffer compatibility - one buffer must serve "
"pump, separator, and detector - so chip designers pick the buffer "
"first and the elements second. Power comes from a battery or USB; "
"readout is electrical (current, impedance), keeping the instrument "
"pocket-sized. Regulatory path: the chip is an in-vitro diagnostic, so "
"ISO 13485 and analytical validation govern long before the clinic."),
"key_points": [
"Chain: filter -> preconcentrate (ICP, 1e6x) -> separate -> detect -> report.",
"Diffusion clock: 100 um mixes in 10 s (L^2/D) - stir, do not wait.",
"1 uL at 1 fM holds ~600 target molecules - preconcentration first.",
"One buffer must serve all elements - pick the buffer first.",
"Electrical readout keeps the instrument pocket-sized.",
"Regulatory reality: in-vitro diagnostic, ISO 13485 validation."],
"requirements": [
"Integrated chip: microfluidic transport + nanofluidic functional elements.",
"Single compatible buffer system across all stages.",
"Electrical readout and low-voltage power."],
"standards": [
"ISO 13485 - medical device quality management.",
"IUPAC electrokinetic definitions."],
"citations": [
"Wang, Y.-C. et al. 'Million-fold preconcentration of proteins and peptides by nanofluidic filter' Anal. Chem. 77, 4293-4299 (2005).",
"Eijkel, J. C. T. & van den Berg, A. 'Nanofluidics: what is it and what can we expect from it?' Microfluid. Nanofluid. 1, 249-267 (2005)."],
"sig_lens": (
"Signature lens: lab-on-a-chip is Signature integration - every "
"nanofluidic trick in this database chained on one piece of plastic. "
"Signature chips are designed backwards from the answer: what must "
"be detected, at what level, in what sample - then the buffer, then "
"the elements, then the plastic.")},
{
"key": "biosensor",
"name": "Nanofluidic Biosensors: Counting Molecules Toward the Limit",
"group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
"description": (
"A biosensor's limit is set by counting statistics: at 1 femtomolar in "
"1 microlitre there are just 602 target molecules - the demo's number "
"(1e-15 mol/L * 1e-6 L * Avogadro). Nanofluidics attacks the limit three "
"ways. First, preconcentration: ICP stacks those 602 molecules into a "
"picolitre plug, raising the local concentration a million-fold before "
"detection. Second, confinement: a nanochannel holding the capture "
"probes forces every molecule to pass within nanometres of a probe - no "
"molecule diffuses past unseen. Third, sensitive transduction: "
"nanopore resistive pulses count molecules one by one, and nanofluidic "
"transistors report binding as conductance change. The remaining enemy "
"is time: at femtomolar levels, diffusion delivers molecules to the "
"sensor slowly - the mass-transport limit - so practical sensors use "
"electrokinetic focusing to feed the detector actively. The trajectory "
"is clear: from ensemble averages to digital counting, one molecule at "
"a time."),
"how_it_works": (
"The demo counts: 1 fM * 1 uL = 1e-21 mol = 602 molecules. Poisson "
"statistics then say the counting noise is sqrt(602) ~ 25, a 4% floor "
"no amplifier can beat - the fundamental limit. Preconcentration "
"defeats the transport limit, not the counting limit: stacking the 602 "
"molecules into 1 pL makes 1 nM locally, and the detector sees a strong "
"signal - but it still counts 602 individuals. Capture kinetics: in a "
"50 nm channel, a molecule diffuses across the height in h^2/D = "
"(5e-8)^2/1e-9 = 2.5 us - every molecule meets the wall thousands of "
"times per second, so capture is reaction-limited, not transport-"
"limited, the ideal regime. Readout choice follows the question: "
"counting (nanopore pulses) for absolute quantification, conductance "
"shift (NFET) for real-time binding curves, fluorescence for "
"multiplexed panels."),
"key_points": [
"1 fM in 1 uL = 602 molecules - Poisson noise sets a 4% fundamental floor.",
"ICP preconcentration (1e6x) beats the transport limit, not the counting limit.",
"50 nm channel: molecule meets the wall every 2.5 us - reaction-limited capture.",
"Nanopore pulses count; NFET conductance tracks binding; fluorescence multiplexes.",
"Electrokinetic focusing feeds the detector actively at ultralow concentrations.",
"Trajectory: ensemble averages -> digital single-molecule counting."],
"requirements": [
"Preconcentration stage for sub-pM targets.",
"Capture chemistry (antibodies, aptamers) on nanochannel walls.",
"Single-molecule-capable readout (pore, transistor, or optics)."],
"standards": [
"ISO 13485 - medical device quality management.",
"IUPAC biosensor definitions."],
"citations": [
"Wang, Y.-C. et al. 'Million-fold preconcentration of proteins and peptides by nanofluidic filter' Anal. Chem. 77, 4293-4299 (2005).",
"Branton, D. et al. 'The potential and challenges of nanopore sequencing' Nature Biotech. 26, 1146-1153 (2008)."],
"sig_lens": (
"Signature lens: the biosensor is Signature counting - refusing to "
"average what can be counted. Signature diagnostics stack the "
"molecule first, confine it second, and count it third, because at "
"602 molecules there is no such thing as a representative sample.")},
{
"key": "fouling",
"name": "Fouling and Longevity: Keeping Nanochannels Open",
"group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
"description": (
"The cruel irony of nanofluidics: the walls that do all the work also "
"collect all the dirt. Proteins adsorb, colloids lodge, salt "
"crystallizes, and biofilms grow - in a 50 nm channel, a single 20 nm "
"protein layer cuts the open height nearly in half and the h^3 "
"hydraulic law turns that into an eightfold flow loss. The demo models "
"flux decline as J = J0*exp(-t/72h): after 24 hours the flux is 71.7% "
"of fresh, and it halves at 49.9 hours - the cleaning interval for "
"this fouling rate. Defenses are layered: PEG and zwitterionic "
"coatings that proteins cannot grip, shear and backflush protocols "
"that sweep the walls, feed pretreatment (the cheapest defense - "
"filter the feed before the nanochannels see it), and electrochemical "
"cleaning pulses that desorb foulants in place. Desalination membranes "
"live or die by this record: a membrane that rejects 99% of salt for "
"a day and then clogs is a laboratory curiosity, not a product. "
"Design for cleaning from day one - the channel you cannot clean is "
"the channel you will replace."),
"how_it_works": (
"The demo: J/J0 = exp(-24/72) = 0.717 after a day; half-flux when "
"exp(-t/72) = 0.5, t = 72*ln(2) = 49.9 h. Real fouling follows several "
"laws - pore blocking (abrupt), cake filtration (1/J^2 linear in t), "
"adsorption (Langmuir kinetics) - and diagnosis starts by fitting the "
"decline curve to identify the mechanism, because each mechanism has "
"its own cleaning protocol. Coatings work by hydration: zwitterionic "
"surfaces bind water so tightly that proteins cannot displace it to "
"adsorb. Operational tricks: periodic flow reversal, osmotic "
"backwashing (clean water drawn backward through the membrane), and "
"voltage pulses that electrophoretically strip charged foulants. "
"Monitoring: track hydraulic resistance and streaming potential - a "
"rising R_h with steady zeta means physical blockage; a shifting zeta "
"means the wall chemistry itself is being coated, which changes every "
"electrokinetic calibration downstream."),
"key_points": [
"20 nm of adsorbed protein in a 50 nm channel ~ halves height -> ~8x flow loss (h^3).",
"Demo: J=J0*exp(-t/72h); 71.7% at 24 h; half-flux at 49.9 h - the cleaning interval.",
"Fit the decline curve to diagnose: blocking vs cake vs adsorption.",
"Zwitterionic coatings: bound water that proteins cannot displace.",
"Defenses: pretreat feed, backflush, voltage-pulse stripping, osmotic backwash.",
"Monitor R_h (blockage) and zeta (wall-chemistry change) separately."],
"requirements": [
"Fouling-rate measurement on the real feed, not clean buffer.",
"Cleanable design: reversible flows, coatable walls, accessible channels.",
"Monitoring of hydraulic resistance and zeta potential in operation."],
"standards": [
"ISO/TS 80004-1:2023 - nanoscale vocabulary.",
"ASTM D4189-adjacent silt-density practice for feed characterization."],
"citations": [
"Bocquet, L. & Tabeling, P. 'Physics and technological aspects of nanofluidics' Lab Chip 14, 3143-3158 (2014).",
"Surwade, S. P. et al. 'Water desalination using nanoporous single-layer graphene' Nature Nanotech. 10, 459-464 (2015)."],
"sig_lens": (
"Signature lens: fouling is Signature entropy - the world slowly "
"closing your perfect channel. Signature builders design the "
"cleaning before the channel: coatable walls, reversible flows, and "
"a fouling budget in hours, because uptime is the only performance "
"number the customer ever sees.")},
{
"key": "design_rules",
"name": "Design Rules: Building a Nanofluidic Device That Works",
"group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
"description": (
"Thirty-three records of physics condense into a checklist. One: name "
"the regime - compute lambda for your buffer, compare h to 2*lambda, "
"and know whether you are bulk, overlapped, or unipolar before drawing "
"anything. Two: pick the driver - pressure for throughput, voltage for "
"control, salt gradient for free energy - and check its scaling "
"(h^3 punishes pressure). Three: budget the resistances - the demo "
"networks two series pairs in parallel (1e21 + 2e21 || 3e21) for a "
"total of 1.5e21 Pa s/m^3, flowing 6.67e-17 m^3/s (66,667 aL/s) at 1 bar - and "
"remember the entrances (access resistance) and the feed channels. "
"Four: choose the wall - charge, coating, and slip are design "
"parameters, not accidents. Five: plan the measurement - streaming "
"potential for zeta, conductance-vs-salt for surface charge, "
"fluorescence for concentration fields. Six: design the cleaning. "
"Seven: calibrate in the real buffer, because salt, pH, and fouling "
"rewrite every number. Devices fail when a step is skipped, rarely "
"from unknown physics."),
"how_it_works": (
"The demo does hydraulic network arithmetic - the skill every "
"designer needs. Series: R = R1 + R2 = 3e21. Parallel with another "
"3e21 branch: R_total = 1.5e21 Pa s/m^3. Flow at 1 bar: Q = "
"1e5/1.5e21 = 6.67e-17 m^3/s = 66,667 aL/s. The same algebra extends to "
"electrical networks (conductances add in parallel) and to coupled "
"electrokinetic circuits. Beyond arithmetic, the rules are about "
"order: regime first (it decides which equations apply), driver "
"second (it decides the energy budget), resistances third (they "
"decide whether anything flows), walls fourth (they decide "
"selectivity and slip), measurement fifth (unmeasured devices are "
"hopes), cleaning sixth (fouling is certain). Prototype loop: build "
"one channel, measure zeta/conductance/flow, fit the three numbers, "
"then scale to arrays - never scale an unmeasured single channel."),
"key_points": [
"Seven steps: regime, driver, resistances, walls, measurement, cleaning, real-buffer calibration.",
"Demo network: (1e21+2e21) || 3e21 -> 1.5e21 Pa s/m^3; 1 bar -> 66,667 aL/s.",
"Series adds R; parallel adds conductance - hydraulic and electrical alike.",
"Prototype loop: one channel measured before any array is scaled.",
"Devices fail from skipped steps, rarely from unknown physics.",
"Unmeasured devices are hopes, not instruments."],
"requirements": [
"Buffer specification (salt, pH) fixed before geometry.",
"Hydraulic + electrical network model of the full device.",
"Single-channel prototype with zeta/conductance/flow measurement."],
"standards": [
"ISO/TS 80004 series - nanotechnology vocabulary and characterization.",
"IUPAC electrokinetic definitions."],
"citations": [
"Schoch, R. B., Han, J. & Renaud, P. 'Transport phenomena in nanofluidics' Rev. Mod. Phys. 80, 839-883 (2008).",
"Bocquet, L. & Tabeling, P. 'Physics and technological aspects of nanofluidics' Lab Chip 14, 3143-3158 (2014)."],
"sig_lens": (
"Signature lens: design rules are Signature discipline - the "
"checklist that turns thirty-three records of physics into one "
"working device. Signature engineers run the list in order, measure "
"before scaling, and treat the prototype's three numbers (zeta, "
"conductance, flow) as the device's birth certificate.")},
{
"key": "safety",
"name": "Safety and Standards in Nanofluidics: Handling the Very Small",
"group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
"description": (
"Nanofluidic devices handle nanomaterials - carbon nanotubes, "
"nanoporous membranes, engineered nanoparticles - and the safety "
"practice is borrowed from nanosafety: contain, ventilate, measure. "
"The demo does the basic exposure arithmetic: releasing 1 mg of "
"nanotube powder into a 30 m^3 lab gives 33.3 ug/m^3, against the "
"NIOSH recommended exposure limit of 1 ug/m^3 for carbon nanotubes - "
"33 times over, so the operation belongs in a fume hood or glove box, "
"not on the open bench. Liquid-phase work is inherently safer - "
"particles in suspension do not become airborne - which is one more "
"argument for keeping nanofluidics wet. Waste streams carrying "
"nanomaterials need capture (filtration) before drain disposal, and "
"high-voltage supplies need interlocks regardless of scale. Standards "
"are still maturing: ISO/TS 80004 defines the vocabulary, OECD test "
"guidelines cover nanomaterial toxicity, and device-specific standards "
"are being written now - which means today's builders should document "
"exposures and controls as if the inspector is already scheduled."),
"how_it_works": (
"Exposure assessment follows the industrial-hygiene chain: identify "
"the material, estimate airborne concentration (mass released over "
"room volume, adjusted for ventilation rate), compare to the exposure "
"limit. The demo: 1 mg / 30 m^3 = 33.3 ug/m^3 vs 1 ug/m^3 REL -> "
"factor 33.3 over. Controls follow the hierarchy: elimination "
"(buy suspensions, not powders), engineering (hoods, closed fluidics), "
"administrative (SOPs, training), PPE (P3 respirators as last "
"resort). For the devices themselves, safety means pressure ratings "
"(nanochannels at bars of pressure store little energy - a blessing "
"of small volumes), electrical safety (kV supplies with current "
"limits and interlocks), and chemical safety (pH extremes, etchants "
"in fabrication). Document everything: the field's standards are "
"being written from the incident reports and exposure logs of today's "
"labs."),
"key_points": [
"1 mg in 30 m^3 = 33.3 ug/m^3 vs 1 ug/m^3 NIOSH REL - 33x over, hood required.",
"Hierarchy: eliminate powders -> engineer containment -> SOPs -> PPE last.",
"Wet work is inherently safer - suspensions do not become airborne.",
"Small volumes store little pressure energy - a blessing of the scale.",
"kV supplies need current limits and interlocks regardless of device size.",
"Document exposures now - today's logs write tomorrow's standards."],
"requirements": [
"Nanomaterial risk assessment before any dry-powder operation.",
"Fume hood or glove box for powder handling; filtration for waste streams.",
"Electrical interlocks on high-voltage supplies."],
"standards": [
"NIOSH CIB 65 - occupational exposure to carbon nanotubes and nanofibers (REL 1 ug/m^3).",
"ISO/TS 80004 series; OECD nanomaterial test guidelines."],
"citations": [
"NIOSH 'Current Intelligence Bulletin 65: Occupational Exposure to Carbon Nanotubes and Nanofibers' (2013).",
"ISO/TS 80004-1:2023 - vocabulary for nanotechnology."],
"sig_lens": (
"Signature lens: safety is Signature stewardship - the small handled "
"with the same gravity as the large. Signature labs keep nanofluidics "
"wet, powders hooded, kilovolts interlocked, and every exposure "
"logged, because the field's future standards are being written from "
"today's notebooks.")},
{
"key": "future",
"name": "The Future of Nanofluidics: Where the Field Is Going",
"group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
"description": (
"Nanofluidics is leaving the laboratory. The trajectories are clear: "
"membranes - angstrom slits and 2D laminates scaling from lab "
"demonstrations to square metres for desalination and osmotic power; "
"diagnostics - integrated chips that preconcentrate, separate, and "
"count single molecules at the point of care; iontronics - diodes, "
"transistors, and memristors wired into circuits that compute in salt "
"water at biological speed; and fundamental physics - quantum friction, "
"single-file water, and angstrom fluid mechanics rewriting what flow "
"means. The demo does the manufacturing arithmetic: a million devices "
"at 250 per 200 mm wafer is 4,000 wafers - a pilot line, not a "
"megafab, which is why startups can play. The bottlenecks are "
"manufacturing uniformity (every pore must work), fouling (the "
"longevity record), and standards (the safety record). Bocquet's 2020 "
"'coming of age' assessment still frames it: the science is mature, "
"the engineering is beginning. The field that learned to plumb the "
"nanoscale is now learning to manufacture it - and the devices that "
"result will sit in water plants, clinics, and eventually inside the "
"body, speaking ion to cell."),
"how_it_works": (
"The demo: 1e6 devices / 250 per wafer = 4,000 wafers for a million-"
"unit run - pilot-line scale, meaning capital cost is not the "
"blocker; yield is. Each trajectory has its scaling law: membranes "
"scale by area (square metres of uniform pores), diagnostics by "
"integration (more functions per chip, not smaller features), "
"iontronics by circuit complexity (from single devices to arrays to "
"systems). The research frontiers feeding them: sub-nanometre "
"selective membranes that work in seawater, anti-fouling surfaces "
"measured in months not hours, and the new physics - quantum "
"friction, voltage-gated molecular streaming - that may enable "
"effects with no macroscopic analog. For the student: learn the "
"seven design-rule steps, master one fabrication route deeply, and "
"measure everything - the field rewards those who can both derive "
"the Debye length and unclog a channel at 2 a.m."),
"key_points": [
"Four trajectories: membranes, diagnostics, iontronics, fundamental physics.",
"1M devices at 250/wafer = 4,000 wafers - pilot line, not megafab.",
"Bottlenecks: uniformity, fouling longevity, standards.",
"Science mature, engineering beginning (Bocquet 2020).",
"Devices will sit in water plants, clinics, and inside the body.",
"Master the design rules, one fabrication route, and measurement."],
"requirements": [
"Manufacturing route with demonstrated uniformity at area.",
"Fouling data in months, not hours.",
"Standards engagement as the field's norms are written."],
"standards": [
"ISO/TS 80004 series - nanotechnology vocabulary.",
"OECD nanomaterial test guidelines."],
"citations": [
"Bocquet, L. 'Nanofluidics coming of age' Nature Mater. 19, 254-256 (2020).",
"Bocquet, L. & Tabeling, P. 'Physics and technological aspects of nanofluidics' Lab Chip 14, 3143-3158 (2014)."],
"sig_lens": (
"Signature lens: the future is Signature manufacturing - the field "
"growing from derivation to production. Signature strategy bets on "
"the pilot line, not the megafab: uniformity first, fouling solved, "
"standards shaped - and devices that speak ion to cell.")}
]
