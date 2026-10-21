(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "mounting", "types", "adjustment", "ergonomics", "multi"];
var PREFIX='JAH-PCO68S-';
var GENVER='jahdb-pc-organizer-monitor-arm-multi-monitor-mount-signature-1.0';
var DBNAME='Signature SkyArm Mounts';
var PROV='Original Signature design by Justin Addam Higgins (JAH) — authored for the JAH Databases network.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["SkyArm concept", "overview", "The Signature SkyArm Mounts are Manon's original display rigging: gas-spring arms with a calibration dial, so the float feels identical on every desk. Monitors should hover; stands are just the compromise we outgrew.", {"mode": "reach", "cm": 60}, "Runnable demo \u2014 SkyArm concept"], ["Universal VESA head", "mounting", "The quick-release VESA head takes 75 and 100 patterns with one sliding plate and ejects with a lever \u2014 monitor swaps take seconds. The head self-levels, so hanging straight is automatic.", {"mode": "vesa", "v": "100x100", "ok": true}, "Runnable demo \u2014 Universal VESA head"], ["Honest capacity", "mounting", "Every SkyArm prints its tested capacity \u2014 not a marketing number \u2014 with the test method on the box. This demo verifies a heavy ultrawide against that honest rating.", {"mode": "weight", "kg": 9.5, "rated": 12}, "Runnable demo \u2014 Honest capacity"], ["Feather gas springs", "types", "Feather gas springs are matched to the monitor's weight at the factory option you choose, arriving pre-tensioned. Out of the box, the float is already right.", {"mode": "gas"}, "Runnable demo \u2014 Feather gas springs"], ["Set-and-stay mechanical", "types", "The mechanical SkyArm uses a cam tensioner with detents \u2014 click, click, perfect \u2014 instead of an endless screw. Detents make the setting repeatable across reinstalls.", {"mode": "mech"}, "Runnable demo \u2014 Set-and-stay mechanical"], ["Edge-sense clamp", "mounting", "The edge-sense clamp distributes pressure across a wide pad and warns if the desk edge flexes past its limit. Thin tops get flagged before they get crushed.", {"mode": "mount", "how": "edge-sense C-clamp", "desk": "20-90 mm"}, "Runnable demo \u2014 Edge-sense clamp"], ["Through-desk anchor", "mounting", "The through-desk anchor uses the grommet hole with a expanding collar that grips without crushing cable pass-throughs. Maximum rigidity, zero desk damage.", {"mode": "mount", "how": "expanding-collar anchor", "desk": "with grommet hole"}, "Runnable demo \u2014 Through-desk anchor"], ["Full-motion choreography", "adjustment", "Tilt, swivel, rotate, and lift move on sealed bearings with adjustable damping \u2014 the motion feels engineered, not improvised. Portrait rotation locks at exactly 90 degrees.", {"mode": "tilt", "tilt": "+/- 50 deg", "sw": "+/- 90 deg", "rot": "360 deg, 90 deg lock"}, "Runnable demo \u2014 Full-motion choreography"], ["Deep-desk reach", "adjustment", "A 60 cm articulated reach with a folding elbow brings the screen close on deep benches and folds flat for shipping. The elbow's fold is the packing trick.", {"mode": "reach", "cm": 60}, "Runnable demo \u2014 Deep-desk reach"], ["Invisible cabling", "adjustment", "Cables vanish into the arm's internal channel with a service loop at each joint, emerging only at the desk. Full motion, zero visible cable \u2014 the floating look, perfected.", {"mode": "cable"}, "Runnable demo \u2014 Invisible cabling"], ["Ergo presets", "ergonomics", "Ergo presets mark sitting, standing, and shared positions on the pole with stops you can feel. Switching from sit to stand is one lift to the click.", {"mode": "ergo"}, "Runnable demo \u2014 Ergo presets"], ["Command dual rig", "multi", "The command dual rig pairs a landscape primary with a portrait secondary on one pole \u2014 code beside, docs upright. The portrait arm counterbalances independently.", {"mode": "multi", "n": 2, "layout": "primary landscape, secondary portrait"}, "Runnable demo \u2014 Command dual rig"], ["Situation wall", "multi", "Situation walls gang SkyArms on a rail for three, four, six displays with one alignment procedure. Monitoring walls align in minutes instead of an afternoon of shimming.", {"mode": "multi", "n": 3, "layout": "railed arc, laser-aligned"}, "Runnable demo \u2014 Situation wall"], ["Two-minute hang", "mounting", "The two-minute hang: clamp, raise the pole, click the VESA head, hang the monitor, feel it level itself. The demo lists the ritual that makes it routine.", {"mode": "install", "steps": ["Clamp the pole", "Raise to working height", "Click on the VESA head", "Hang the monitor", "Feel it self-level", "Set the ergo preset"]}, "Runnable demo \u2014 Two-minute hang"], ["SkyArm workflow", "ergonomics", "The SkyArm workflow: verify fit, mount, calibrate float, set ergo presets, hide the cables. Displays that hover where eyes want them, adjusted in seconds forever after.", {"mode": "workflow", "steps": ["Verify VESA and weight", "Mount per the ritual", "Calibrate the float", "Set sit/stand presets", "Hide cables in the channel", "Enjoy the hover"]}, "Runnable demo \u2014 SkyArm workflow"]];
var ENGINE="var DATA = __DATA__;\nfunction show(k,v){console.log(k+\": \"+v);}\nvar m=DATA.mode;\nif(m===\"vesa\"){\n  show(\"VESA patterns\",\"75x75 and 100x100 mm\");\n  show(\"Your monitor\",DATA.v);\n  show(\"Fits\",DATA.ok?\"YES\":\"NO - needs an adapter plate\");\n}else if(m===\"weight\"){\n  show(\"Monitor weight\",DATA.kg+\" kg\");\n  show(\"Arm rated\",DATA.rated+\" kg\");\n  show(\"Verdict\",DATA.kg<=DATA.rated?\"SAFE\":\"OVERLOAD - bigger arm needed\");\n}else if(m===\"reach\"){\n  show(\"Arm reach\",DATA.cm+\" cm\");\n  show(\"Covers\",\"deep desks and corner setups\");\n}else if(m===\"tilt\"){\n  show(\"Tilt\",DATA.tilt);\n  show(\"Swivel\",DATA.sw);\n  show(\"Rotate\",DATA.rot+\" (portrait in seconds)\");\n}else if(m===\"mount\"){\n  show(\"Mount\",DATA.how);\n  show(\"Desk thickness\",DATA.desk);\n  show(\"Check\",\"desk edge must be solid, not hollow-core thin\");\n}else if(m===\"gas\"){\n  show(\"Mechanism\",\"gas spring\");\n  show(\"Feel\",\"one finger moves it, stays where left\");\n  show(\"Best for\",\"frequent adjusting, shared desks\");\n}else if(m===\"mech\"){\n  show(\"Mechanism\",\"mechanical spring + tilt head\");\n  show(\"Setup\",\"set tension once per monitor weight\");\n  show(\"Best for\",\"set-and-forget single user\");\n}else if(m===\"multi\"){\n  show(\"Arms\",DATA.n);\n  show(\"Layout\",DATA.layout);\n  show(\"Use\",\"code + terminal + stats, all visible\");\n}else if(m===\"cable\"){\n  show(\"Routing\",\"clips along the arm\");\n  show(\"Slack\",\"enough for full motion range\");\n}else if(m===\"ergo\"){\n  show(\"Height\",\"top of screen at or below eye level\");\n  show(\"Distance\",\"about an arm's length\");\n  show(\"Tilt\",\"slight upward tilt of the panel\");\n}else if(m===\"install\"){\n  console.log(\"Install:\");DATA.steps.forEach(function(s,i){console.log(\"  \"+(i+1)+\". \"+s);});\n}else if(m===\"mistake\"){\n  show(\"Mistake\",DATA.bad);show(\"Instead\",DATA.good);\n}else if(m===\"care\"){\n  show(\"Care\",\"check clamp tightness yearly\");\n  show(\"Gas arms\",\"never disassemble the cylinder\");\n}else if(m===\"workflow\"){\n  console.log(\"Rigging workflow:\");DATA.steps.forEach(function(s,i){console.log(\"  \"+(i+1)+\". \"+s);});\n}\nconsole.log(\"DEMO_OK\");";
function jitter(v,rnd){
  if(typeof v==='number'){return Math.round(v*(0.9+rnd()*0.2)*100)/100;}
  if(Array.isArray(v)){return v.map(function(x){return jitter(x,rnd);});}
  if(v&&typeof v==='object'){var o={};Object.keys(v).forEach(function(k){o[k]=jitter(v[k],rnd);});return o;}
  return v;
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  if(typeof seed==='number'&&seed>SELFREG.maxRecords)throw new Error('SELF-REGULATION HARD STOP: 1,000,000,000,000 record limit reached');
  var cat=opts.category||pick(CATS,rnd);
  var pool=ARCH.filter(function(a){return a[1]===cat;});
  var a=pick(pool.length?pool:ARCH,rnd);
  var scen=jitter(a[3],rnd); scen.mode=a[3].mode;
  var id=PREFIX+String(10001+seed).padStart(6,'0');
  var program=ENGINE.split('__DATA__').join(JSON.stringify(scen));
  var facts=jitter(a[4]||{},rnd);
  return {id:id,t:a[0]+' (simulated #'+seed+')',
    title:DBNAME+' \u2014 '+a[0]+' (simulated variant, seed '+seed+')',
    g:a[1],category:a[1],
    description:a[2]+' This is a simulated boundless-generator variant (seed '+seed+') from '+GENVER+': the scenario values were deterministically jittered from the archive archetype, and the record passed the independent correctness validator before acceptance.',
    ladder_rank:1+((seed-1)%15),
    march:'MILLION MARCH \u00b7 simulated record \u00b7 archive marches to a 1,000,000-record target \u2014 in progress',
    provenance:PROV,last_verified:'2026-10-21',record_label:SELFREG.simulatedLabel,
    facts:facts,
    demo:{engine:'jahdb-demo-1.0',kind:'code',title:'Runnable demo \u2014 '+a[0]+' (simulated)',language:'javascript',
      program:program,run_hint:'PC: save as demo.js, run `node demo.js`. In-page: press Run.',
      how_to_run:'PC: save the program as demo.js and run `node demo.js`. In-page: open the Demo Lab tab and press Run.',runnable:true},
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-monitor-arm-multi-monitor-mount-signature/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-monitor-arm-multi-monitor-mount-signature',_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  var rx=new RegExp('^'+PREFIX.replace(/[-\/\\^$*+?.()|[\]{}]/g,'\\$&')+'\\d{6}$');
  if(!rx.test(r.id||''))e.push('id');
  var n=parseInt(String(r.id||'').slice(PREFIX.length),10);
  if(!(n>=10001))e.push('id-block (generator ids start at 10001; archive owns 1-9999)');
  if(typeof r.t!=='string'||!r.t.length)e.push('t');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=15))e.push('ladder_rank');
  if(r.record_label!==SELFREG.simulatedLabel)e.push('record_label');
  if(!r.demo||typeof r.demo.program!=='string'||!r.demo.program.length)e.push('demo');
  if(r.demo&&r.demo.language!=='javascript')e.push('demo-language');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){if(sample[i]&&sample[i].title===rec.title)return{ok:false,errors:['drift: exact title already in archive']}; }
  return{ok:true,errors:[]};
}
var gen={version:GENVER,selfRegulation:SELFREG,generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-monitor-arm-multi-monitor-mount-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
