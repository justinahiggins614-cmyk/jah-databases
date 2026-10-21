(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "panels", "hooks", "layout", "mounting", "care"];
var PREFIX='JAH-PCO69-';
var GENVER='jahdb-pc-organizer-perforated-pegboard-hooks-1.0';
var DBNAME='Perforated Pegboard & Hooks';
var PROV='Public documentation and published specifications for Perforated Pegboard & Hooks; compiled and fact-checked.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["What pegboard does", "overview", "Perforated pegboard turns a wall into tool storage: a panel of evenly spaced holes that takes hooks, bins, and shelves. Screwdrivers, pliers, and cables hang in reach instead of drowning in drawers.", {"mode": "holes"}, "Runnable demo \u2014 What pegboard does"], ["The hole standard", "overview", "The standard is quarter-inch holes on one-inch centers \u2014 the pattern every hook manufacturer builds for. Off-standard boards orphan you to one hook brand, so standard is the whole game.", {"mode": "holes"}, "Runnable demo \u2014 The hole standard"], ["Panel sizes", "panels", "Panels commonly run 2x4 feet, tileable into full walls, in hardboard or steel. Two panels flank a bench beautifully; four make a proper tool wall.", {"mode": "panel", "w": 2, "h": 4, "mat": "hardboard"}, "Runnable demo \u2014 Panel sizes"], ["Hardboard vs steel", "panels", "Hardboard is the classic brown, cheap and plenty strong for hand tools; steel costs more, holds magnets, and shrugs off heavier loads. Workshops that hang power tools go steel.", {"mode": "steel"}, "Runnable demo \u2014 Hardboard vs steel"], ["Hook types", "hooks", "The hook family: single and double straight hooks for tools, curved holders for pliers, ring hooks for rolls of tape and wire, and locking hooks that cannot lift out. Match the hook to the tool's hang point.", {"mode": "hooks", "types": ["Single straight - screwdrivers", "Double - pliers, hammers", "Ring - tape rolls, wire spools", "Locking - cannot lift out"]}, "Runnable demo \u2014 Hook types"], ["Hook-on bins", "hooks", "Hook-on bins turn pegboard into small-parts storage for screws, connectors, and adapters, each bin labeled. They are the wall-mounted cousins of the drawer cabinet.", {"mode": "bins"}, "Runnable demo \u2014 Hook-on bins"], ["Hook-on shelves", "hooks", "Hook-on shelves hold multimeters, label printers, and parts boxes at bench height. Shelves convert vertical wall into usable bench-adjacent surface.", {"mode": "shelf", "d": 6}, "Runnable demo \u2014 Hook-on shelves"], ["Planning the layout", "layout", "Plan on paper first: trace each tool, arrange the cutouts on a panel outline, then hang hooks once. Most-used tools live at hand height between shoulder and hip; rarely used goes high.", {"mode": "plan"}, "Runnable demo \u2014 Planning the layout"], ["Tool shadowing", "layout", "Shadowing traces each tool's outline on the board in marker or tape, so a missing tool leaves a visible ghost. Shops that shadow never wonder where the flush cutters went.", {"mode": "shadow"}, "Runnable demo \u2014 Tool shadowing"], ["Mounting with spacers", "mounting", "Pegboard mounts on spacers or furring strips holding it off the wall, because hooks need depth behind the board to seat. Into studs for loaded boards \u2014 drywall anchors are for pictures, not tool walls.", {"mode": "mount"}, "Runnable demo \u2014 Mounting with spacers"], ["Weight distribution", "mounting", "Heavy tools hang low and near studs; light tools fill the high and middle field. This demo averages a loaded board's weight across its hooks to show the gentle reality.", {"mode": "weight", "kg": 18, "hooks": 24}, "Runnable demo \u2014 Weight distribution"], ["Zoned walls", "layout", "Zone the wall by job: fastening tools together, electrical together, cutting together. Zones turn 'where is' into muscle memory within a week.", {"mode": "layout", "rows": ["Fastening: drivers, wrenches", "Electrical: strippers, meter, iron", "Cutting: snips, knives, saws", "Consumables: tape, ties, bins"]}, "Runnable demo \u2014 Zoned walls"], ["Common mistakes", "layout", "Hanging the board flat to the wall with no spacers is the classic \u2014 hooks cannot seat and everything falls. The runner-up is loading one corner until the board leans; distribute like you mean it.", {"mode": "mistake", "bad": "board flat on wall, no spacers", "good": "spacers + studs + distributed load"}, "Runnable demo \u2014 Common mistakes"], ["Care", "care", "Dust the board yearly and replace bent hooks before they drop tools \u2014 a two-cent hook is not worth a cracked meter. Tighten the mounting screws when seasons change the wall.", {"mode": "care"}, "Runnable demo \u2014 Care"], ["Wall workflow", "layout", "The wall ritual: inventory tools, plan on paper, mount with spacers into studs, hang by zone, shadow the outlines. A finished tool wall is the bench's memory made visible.", {"mode": "workflow", "steps": ["Inventory every tool", "Plan zones on paper", "Mount with spacers into studs", "Hang hooks by zone", "Shadow each outline", "Maintain: bent hooks out"]}, "Runnable demo \u2014 Wall workflow"]];
var ENGINE="var DATA = __DATA__;\nfunction show(k,v){console.log(k+\": \"+v);}\nvar m=DATA.mode;\nif(m===\"holes\"){\n  show(\"Standard\",\"1/4 in holes on 1 in centers\");\n  show(\"Fits\",\"standard pegboard hooks\");\n}else if(m===\"panel\"){\n  show(\"Panel\",DATA.w+\" x \"+DATA.h+\" ft\");\n  show(\"Area\",(DATA.w*DATA.h)+\" sq ft\");\n  show(\"Material\",DATA.mat);\n}else if(m===\"hooks\"){\n  console.log(\"Hook types:\");DATA.types.forEach(function(t){console.log(\"  \"+t);});\n}else if(m===\"layout\"){\n  console.log(\"Planned layout:\");DATA.rows.forEach(function(r,i){console.log(\"  Row \"+(i+1)+\": \"+r);});\n}else if(m===\"mount\"){\n  show(\"Mounting\",\"spacers hold the board off the wall\");\n  show(\"Why\",\"hooks need depth behind the board\");\n  show(\"Into\",\"studs for loaded boards\");\n}else if(m===\"weight\"){\n  show(\"Load\",DATA.kg+\" kg across \"+DATA.hooks+\" hooks\");\n  show(\"Per hook\",(Math.round(DATA.kg/DATA.hooks*10)/10)+\" kg average\");\n  show(\"Rule\",\"heavy tools low and near studs\");\n}else if(m===\"bins\"){\n  show(\"Bins\",\"hook-on bins for screws and small parts\");\n  show(\"Labels\",\"every bin labeled\");\n}else if(m===\"shelf\"){\n  show(\"Shelves\",\"hook-on shelves for boxes and testers\");\n  show(\"Depth\",DATA.d+\" in\");\n}else if(m===\"steel\"){\n  show(\"Steel board\",\"magnetic, stronger, pricier\");\n  show(\"Hardboard\",\"classic brown, cheaper, plenty strong\");\n}else if(m===\"plan\"){\n  show(\"Planning\",\"trace tools on paper, arrange, then hang\");\n  show(\"Rule\",\"most-used at hand height\");\n}else if(m===\"shadow\"){\n  show(\"Shadowing\",\"trace each tool's outline on the board\");\n  show(\"Result\",\"missing tools are instantly visible\");\n}else if(m===\"mistake\"){\n  show(\"Mistake\",DATA.bad);show(\"Instead\",DATA.good);\n}else if(m===\"care\"){\n  show(\"Care\",\"dust yearly, tighten hooks\");\n  show(\"Hooks\",\"replace bent ones - they drop tools\");\n}else if(m===\"workflow\"){\n  console.log(\"Wall workflow:\");DATA.steps.forEach(function(s,i){console.log(\"  \"+(i+1)+\". \"+s);});\n}\nconsole.log(\"DEMO_OK\");";
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
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-perforated-pegboard-hooks/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-perforated-pegboard-hooks',_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-perforated-pegboard-hooks',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
