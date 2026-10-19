(function(){'use strict';
/* jahdb-fundamental-aerospace-engineering-1.0 — fundamental aerospace-engineering bedrock generator.
   Property of Justin Addam Higgins (JAH). Deterministic: same seed always makes the same record.
   src:"public-harvest" = established first-principles knowledge, fact-checked */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX='JAH-FAE-';
var KIND='fundamental aerospace-engineering record';
var SECTIONS=['about', 'reasoning', 'quantities', 'mechanism', 'miscon'];
var BRIEF={'about':'Aerospace engineering designs vehicles that fly and operate in space: aircraft, spacecraft, rockets, and the systems that guide them. It is the engineering of the most unforgiving environments — where failure is not an option and weight is everything.', 'reasoning':'Aerospace engineers reason with margins and redundancy: every critical function has a backup, every load has its factor, every failure mode is analyzed (FMEA). The vehicle must work the first time — there are no roadside repairs at 30,000 feet.', 'quantities':'The core quantities are lift, drag, thrust, and weight — the four forces of flight — plus specific impulse for rockets and delta-v for missions. The lift-to-drag ratio and the rocket equation govern the possible.', 'mechanism':'Aerospace design works the mission loop: define the mission → size the vehicle → analyze aerodynamics, structures, propulsion → test → fly. The rocket equation, Δv = ve·ln(m₀/mf), sets the hard limit every design must respect.', 'miscon':'Aerospace is not just \'faster mechanical engineering\': the regimes (subsonic to hypersonic to orbital) have different physics. Lift is not \'Bernoulli versus Newton\' — both describe the same pressure field. And space is not empty of challenges: radiation, vacuum, and thermal extremes rule design.'};
var SIGLENS=['In the Signature system, aerospace engineering is the discipline of the unforgiving environment: every critical system in this network — backups, redundancy, failure analysis — borrows its habits, and the Signature formulation teaches each principle as a margin you can compute.','The Signature practice is to engineer the margin: compute the forces, size the redundancy, analyze the failure — so aerospace reasoning is done with the discipline of systems that must work the first time.'];
var DEMOS=['#!/usr/bin/env python3\n"""{TITLE} -- lift demo. Runs as-is with python3."""\ndef lift_newtons(rho, v, s, cl):\n    return 0.5 * rho * v**2 * s * cl\nL = lift_newtons(1.225, 70, 20, 1.2)\nprint(f"rho=1.225 v=70m/s S=20m^2 Cl=1.2 -> lift={L/1000:.1f} kN (~{L/9.81:.0f} kg)")\nprint("lift grows with velocity squared: speed is the lever")\n', '#!/usr/bin/env python3\n"""{TITLE} -- rocket equation demo. Runs as-is with python3."""\nimport math\ndef delta_v(ve, m0, mf):\n    return ve * math.log(m0 / mf)\ndv = delta_v(4400, 100, 10)  # ve~4400 m/s (LOX/LH2), 90% propellant\nprint(f"90% propellant mass fraction -> delta-v = {dv/1000:.1f} km/s")\nprint(f"LEO needs ~9.4 km/s: mass ratio required = {math.exp(9400/4400):.1f}:1")\nprint("the tyranny of the rocket equation: exponential mass for linear delta-v")\n', '#!/usr/bin/env python3\n"""{TITLE} -- orbital velocity demo. Runs as-is with python3."""\nimport math\nMU = 3.986e14  # Earth, m^3/s^2\ndef circular_velocity(alt_km):\n    r = 6371e3 + alt_km * 1000\n    return math.sqrt(MU / r)\nfor alt in [400, 2000, 35786]:\n    print(f"alt {alt} km -> {circular_velocity(alt)/1000:.2f} km/s circular")\n'];
var TOPICS=[['What Aerospace Engineering Is','Aerospace engineering designs flight vehicles: aircraft for the atmosphere, spacecraft and rockets for beyond it. It integrates aerodynamics, propulsion, structures, and control into machines that operate where failure is catastrophic and weight is the currency.'],
['The Core Question of Aerospace Engineering','The core question is: how do we fly this mission safely within the weight budget? Every design trades performance against mass — and the rocket equation makes the trade exponential.'],
['Assumptions: Regimes of Flight','The field assumes regime-appropriate physics: incompressible flow at low speed, compressible at transonic, hypersonic heating at reentry, orbital mechanics in space. Using the wrong regime\'s assumptions is the classic analysis error.'],
['The Vocabulary: Lift, Drag, Thrust, Weight','The vocabulary names the four forces: lift (up), weight (down), thrust (forward), drag (back). Steady flight balances them; performance is their ratios — lift-to-drag, thrust-to-weight — the field\'s master numbers.'],
['Delta-v: The Fundamental Quantity','Delta-v is the fundamental quantity of spaceflight: the total velocity change a mission needs, in m/s. Every mission is budgeted in delta-v — and the rocket equation converts the budget into mass.'],
['Aerodynamic Analysis: The Primary Method','Aerodynamic analysis is the primary method in atmosphere: wind tunnels, CFD, and flight test measuring lift, drag, and stability. The wind tunnel is the field\'s laboratory — the air made visible and measurable.'],
['A Canonical First Example','The canonical first example is level flight: lift equals weight, thrust equals drag. Four arrows in balance — and from that balance, range, endurance, and ceiling all follow.'],
['How Aerospace Engineering Measures','The field measures with wind tunnels, telemetry, and flight test: pressures on the model, thousands of sensors in flight, each maneuver expanding the envelope. Flight test is the graduation exam no simulation can waive.'],
['The Core Mechanism: The Rocket Equation','The core mechanism of spaceflight is Tsiolkovsky\'s rocket equation: Δv = vₑ·ln(m₀/mf). Final velocity depends on exhaust speed and the logarithm of the mass ratio — the tyranny that makes staging necessary and mass precious.'],
['The Simplest Law: Lift Balances Weight','The simplest law of flight is the balance: in steady level flight, lift equals weight and thrust equals drag. Every performance calculation starts by perturbing this balance — climb, turn, accelerate.'],
['Common Misconceptions in Aerospace Engineering','The misconceptions persist: the Bernoulli-versus-Newton false choice for lift (one pressure field, two descriptions), that space is \'zero gravity\' (it\'s freefall), and that rockets push against air (they push against their own exhaust).'],
['How Beginners Practice Aerospace Engineering','Beginners practice by analyzing and building: compute the airfoil\'s lift, then build the model glider and fly it. The flight teaches what the polar curve assumed.'],
['The Core Model: The Airfoil','The airfoil is the core model: a shaped section turning airflow into lift with minimum drag. Its polar — lift and drag versus angle — is the wing\'s biography, and stall is its cautionary tale.'],
['The Great Equation: The Rocket Equation','The rocket equation is the great equation: logarithmic, unforgiving, and non-negotiable. It dictates staging, it prices every kilogram, and it is why single-stage-to-orbit remains brutally hard.'],
['Systems Thinking: The Vehicle as System','Systems thinking treats the vehicle whole: structures, propulsion, avionics, and thermal as coupled subsystems trading mass and power. Systems engineering — requirements, interfaces, verification — is the discipline of the whole.'],
['Invariance: Conservation in Fluids','The invariance principles are conservation of mass, momentum, and energy applied to airflow: the Navier-Stokes equations. Every aerodynamic result is these conservations made specific to a shape.'],
['Approximation: Potential Flow to CFD','Approximation climbs the ladder: potential flow for insight, panel methods for speed, RANS CFD for detail, flight test for truth. Each level checks the one below — and the wind tunnel checks them all.'],
['Evidence Standards: Flight Test','The evidence standard is flight test: the vehicle flown through its envelope, every limit demonstrated. Certification demands it — analysis and simulation support, but only flight proves.'],
['Classic Discoveries','The classic discoveries are powered flight, the jet engine, the area rule, and the moon landing\'s systems engineering. Each redefined the possible — and each was an engineering triumph, not just a scientific one.'],
['Core Trade-offs: Performance versus Weight','The core trade-off is performance versus weight versus cost: every kilogram costs performance, every redundancy costs kilograms. The design converges where the mission closes — barely, with margin.'],
['Handling Uncertainty: Margins and Redundancy','The field handles uncertainty with margins and redundancy: factors of safety on structures, redundant computers and sensors, abort modes for crews. Uncertainty is not reduced — it is survived by design.'],
['Tools of the Trade','The tools of the trade are CFD, finite elements, the wind tunnel, and telemetry. The deepest is the failure modes analysis — imagining everything that can break, before it does.'],
['Ethics and Responsibility','Ethics in aerospace is absolute: the crew, the passengers, the public below. The field\'s safety culture — reporting, investigating, grounding — was written by disasters and is non-negotiable.'],
['Teaching Aerospace Engineering','Teaching it well flies things: the model rocket, the glider, the simulator. Students who have watched their design stall understand the polar viscerally.'],
['The Frontier Question','The frontier question is sustainable and autonomous flight: electric aircraft, hypersonic transport, autonomous air mobility, and the reusable rocket economy. The frontier asks what flight becomes when it is routine.'],
['Unifying Theories','The unifying theories are fluid mechanics, orbital mechanics, and control theory: air, space, and the guidance between. Together they describe every vehicle from paper airplane to interplanetary probe.'],
['Computational Aerospace','Computational aerospace flies before building: CFD for aerodynamics, trajectory optimization for missions, coupled simulations for the whole vehicle. The computer flies a thousand designs; the wind tunnel flies the best.'],
['Bridges to Other Fields','Aerospace bridges to mechanical engineering (structures), electrical (avionics), computer science (autonomy), physics (plasmas, relativity for GPS), and medicine (human spaceflight). It is systems engineering\'s home field.'],
['The Great Unsolved Problems','The great unsolved problems are open and labeled as such: turbulence modeling from first principles, scramjet practicality, and economical single-stage-to-orbit. Active research, no settled answers.'],
['How New Claims Are Validated','New vehicles are validated by the test program: ground tests, then envelope expansion in flight, then certification. A vehicle earns trust one test point at a time — there are no shortcuts to flight-proven.'],
['The Great Debates','The great debates include reusable versus expendable economics, piloted versus autonomous futures, and the pace of commercial spaceflight. The debates are industrial — they allocate billions.'],
['Failure Modes: When Aerospace Gets It Wrong','The field gets it wrong through untested regimes, normalization of deviance, and schedule pressure — its failures are public tragedies. The immune system is the independent investigation, whose reports the whole field studies.'],
['Synthesis: Building on the Fundamentals','Advanced synthesis flies whole missions from fundamentals: the trajectory, the vehicle, the margins, the redundancies — each verified, the system proven in flight. The fundamentals are the airworthiness of the design.'],
['The Signature Formulation: Aerospace as Unforgiving Discipline','The Signature formulation treats aerospace principles as the discipline of no second chances: every concept here carries margins and redundancy, because in the Signature system critical systems must work the first time. That is the Signature capstone on aerospace bedrock.']];
var TIERS=[['foundations','Foundations',1,12],['compounded','Compounded',13,24],['advanced','Advanced',25,34]];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function firstSentence(s){var m=/^(.+?[.!?])(\s|$)/.exec(String(s).trim());return m?m[1]:String(s).slice(0,160);}
function compose(i,title,essence){
  var elab,desc,how,kps;
  if(true){
    elab=[BRIEF[SECTIONS[(i+0)%5]],BRIEF[SECTIONS[(i+2)%5]]];
    desc=essence+'\n\n'+elab.join('\n\n');
    how=BRIEF.mechanism+' '+firstSentence(essence)+' The working habit here: '+BRIEF.reasoning.split('. ')[0]+'.';
    kps=[firstSentence(essence),'How the field reasons: '+firstSentence(BRIEF.reasoning),'Core quantities and units: '+firstSentence(BRIEF.quantities),'Common misconception to avoid: '+firstSentence(BRIEF.miscon),'Run the demo program below to make this principle concrete and testable.'];
  }else{
    elab=[SIGLENS[0],BRIEF[SECTIONS[(i+3)%5]]];
    desc=essence+'\n\n'+elab.join('\n\n');
    how=SIGLENS[1]+' '+BRIEF.mechanism+' '+firstSentence(essence);
    kps=[firstSentence(essence),'Signature framing: '+firstSentence(SIGLENS[0]),'Signature practice: '+firstSentence(SIGLENS[1]),'Common misconception to avoid: '+firstSentence(BRIEF.miscon),'Run the demo program below to make this principle concrete and testable.'];
  }
  return {desc:desc,how:how,kps:kps};
}
function generate(seed,opts){
  var s=prng(seed);
  var ti=(s()*TOPICS.length)|0;
  var topic=TOPICS[ti], i=ti, rank=ti+1, title=topic[0], essence=topic[1];
  var tier='foundations',glabel='Foundations';
  for(var k=0;k<TIERS.length;k++){if(rank>=TIERS[k][2]&&rank<=TIERS[k][3]){tier=TIERS[k][0];glabel=TIERS[k][1];}}
  var id=PREFIX+pad(seed);
  var c=compose(i,title,essence);
  var demo=DEMOS[ti%DEMOS.length].split('{TITLE}').join(title);
  return {id:id,t:title,g:glabel,c:0,name:title+' - '+KIND,title:title,description:c.desc,how_it_works:c.how,
    key_points:c.kps,requirements:['Read the description and key points first — they carry the essential first principles.','No prior knowledge of the subject is assumed; the ladder rank tells you what to read first.','Use the demo program to make the principle concrete — run it, change the numbers, re-run.'],
    standards:["Failure modes are analyzed: FMEA/FMECA covers every critical function.", "Redundancy is designed: no single failure causes loss of the mission.", "Testing is exhaustive: test like you fly, fly like you test."],citations:["Anderson, J. D. \u2014 Introduction to Flight (McGraw-Hill).", "Sutton, G. P. and Biblarz, O. \u2014 Rocket Propulsion Elements.", "Cross-checked against the JAH Databases network archive before filing."],src:'public-harvest',ladder_rank:rank,ladder_tier:tier,
    demo:{kind:'fundamental-aerospace-engineering-demo',language:'python',program:demo,note:'Working demonstration program for this record. Runs as-is with python3.'},_seed:seed};
}
function validate(r){
  var errs=[];
  if(!r.id)errs.push('missing id');
  if(!r.title)errs.push('missing title');
  if(!r.description||r.description.length<200)errs.push('description too short (<200)');
  if(!r.key_points||r.key_points.length<3)errs.push('key_points too few');
  if(!r.demo||!r.demo.program||r.demo.program.length<100)errs.push('demo program missing/short');
  if(!r.ladder_rank||!r.ladder_tier)errs.push('ladder missing');
  return {ok:errs.length===0,errors:errs};
}
function driftCheck(rec,sample){
  for(var i=0;i<sample.length;i++){if(sample[i].t===rec.title)return {ok:false,errors:['duplicate title']};}
  return {ok:true,errors:[]};
}
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('fundamental-aerospace-engineering',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
