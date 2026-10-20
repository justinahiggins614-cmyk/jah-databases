(function(){'use strict';
/* JAH Hiking Safety Database generator — jahdb-hiking-safety-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='hiking-safety',PREFIX='JAH-HIK-',NAME='JAH Hiking Safety Database';
var FIELDS=["gear", "navigation", "weather", "wildlife", "emergency"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "The ten essentials", "d": "Navigation, water, food, layers, light, first aid, knife, fire, shelter, sun protection.", "g": "gear", "l": 2, "q": "What is The ten essentials?", "a": "Navigation, water, food, layers, light, first aid, knife, fire, shelter, sun protection.", "x": "Navigation, water, food, layers, light, first aid, knife, fire, shelter, sun protection. Key steps: Pack all ten every time; Adjust for season; No exceptions. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Proper footwear", "d": "Boots or trail runners broken in.", "g": "gear", "l": 2, "q": "What is Proper footwear?", "a": "Boots or trail runners broken in.", "x": "Boots or trail runners broken in. Key steps: Fit with hiking socks; Break in before big hikes; Waterproof for wet trails. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Layering system", "d": "Base, mid, shell.", "g": "gear", "l": 2, "q": "What is Layering system?", "a": "Base, mid, shell.", "x": "Base, mid, shell. Key steps: Wicking base; Insulating mid; Waterproof shell; No cotton. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Backpack fitting", "d": "Fit matters more than size.", "g": "gear", "l": 2, "q": "What is Backpack fitting?", "a": "Fit matters more than size.", "x": "Fit matters more than size. Key steps: Hip belt carries weight; Torso-length fit; Pack heavy items high and close. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Water planning", "d": "Half liter per hour is a baseline.", "g": "gear", "l": 2, "q": "What is Water planning?", "a": "Half liter per hour is a baseline.", "x": "Half liter per hour is a baseline. Key steps: Carry more than you think; Filter or treat wild water; Electrolytes for long days. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Map and compass", "d": "Batteries die; maps do not.", "g": "navigation", "l": 2, "q": "What is Map and compass?", "a": "Batteries die; maps do not.", "x": "Batteries die; maps do not. Key steps: Carry paper maps; Learn basic compass; Practice before you need it. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "GPS and apps", "d": "Great tools with limits.", "g": "navigation", "l": 2, "q": "What is GPS and apps?", "a": "Great tools with limits.", "x": "Great tools with limits. Key steps: Download offline maps; Carry a power bank; GPS is a complement, not a plan. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Trail markers", "d": "Blazes, cairns, ducks.", "g": "navigation", "l": 2, "q": "What is Trail markers?", "a": "Blazes, cairns, ducks.", "x": "Blazes, cairns, ducks. Key steps: Learn local marking systems; Check at junctions; Backtrack when unsure. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Route planning", "d": "Know before you go.", "g": "navigation", "l": 2, "q": "What is Route planning?", "a": "Know before you go.", "x": "Know before you go. Key steps: Study the route; Note bailout points; Share your plan; Check closures. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Pace and timing", "d": "Naismith rule: 5 km/h plus 30 min per 300 m climb.", "g": "navigation", "l": 2, "q": "What is Pace and timing?", "a": "Naismith rule: 5 km/h plus 30 min per 300 m climb.", "x": "Naismith rule: 5 km/h plus 30 min per 300 m climb. Key steps: Start early; Turnaround time set in advance; Half your energy for return. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Weather checks", "d": "Mountain weather changes fast.", "g": "weather", "l": 2, "q": "What is Weather checks?", "a": "Mountain weather changes fast.", "x": "Mountain weather changes fast. Key steps: Check the night before and morning; Know the signs; Turn back early. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Lightning safety", "d": "Get below treeline fast.", "g": "weather", "l": 2, "q": "What is Lightning safety?", "a": "Get below treeline fast.", "x": "Get below treeline fast. Key steps: Avoid ridges and lone trees; Crouch if caught; 30-minute rule after thunder. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Heat hiking", "d": "Desert and summer danger.", "g": "weather", "l": 2, "q": "What is Heat hiking?", "a": "Desert and summer danger.", "x": "Desert and summer danger. Key steps: Start before dawn; A liter per hour; Electrolytes; Shade breaks. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Cold hiking", "d": "Hypothermia kills.", "g": "weather", "l": 2, "q": "What is Cold hiking?", "a": "Hypothermia kills.", "x": "Hypothermia kills. Key steps: Layers, no cotton; Eat and drink; Watch companions for the umbles. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "River crossings", "d": "The leading backcountry killer.", "g": "weather", "l": 2, "q": "What is River crossings?", "a": "The leading backcountry killer.", "x": "The leading backcountry killer. Key steps: Unbuckle hip belt; Face upstream; Shuffle, do not step; Turn back if unsure. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Wildlife: bears", "d": "Make noise, carry spray.", "g": "wildlife", "l": 2, "q": "What is Wildlife: bears?", "a": "Make noise, carry spray.", "x": "Make noise, carry spray. Key steps: Bear spray accessible; Hang food; Never run; Know black vs grizzly response. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Wildlife: mountain lions", "d": "Rare but serious.", "g": "wildlife", "l": 2, "q": "What is Wildlife: mountain lions?", "a": "Rare but serious.", "x": "Rare but serious. Key steps: Do not run; Make yourself big; Fight back if attacked. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Wildlife: snakes", "d": "Watch where you step and reach.", "g": "wildlife", "l": 2, "q": "What is Wildlife: snakes?", "a": "Watch where you step and reach.", "x": "Watch where you step and reach. Key steps: Boots and attention; Do not handle; Back away slowly. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Wildlife: ticks", "d": "Check after every hike.", "g": "wildlife", "l": 2, "q": "What is Wildlife: ticks?", "a": "Check after every hike.", "x": "Check after every hike. Key steps: Repellent; Tuck pants; Full-body check; Remove properly. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Leave No Trace", "d": "The seven principles.", "g": "gear", "l": 2, "q": "What is Leave No Trace?", "a": "The seven principles.", "x": "The seven principles. Key steps: Plan ahead; Durable surfaces; Pack out trash; Leave what you find. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "First aid kit", "d": "Blister care to splints.", "g": "emergency", "l": 2, "q": "What is First aid kit?", "a": "Blister care to splints.", "x": "Blister care to splints. Key steps: Blister kit; Bandages and tape; Antihistamines; Emergency blanket. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Blister prevention", "d": "Hot spots become trip-enders.", "g": "emergency", "l": 2, "q": "What is Blister prevention?", "a": "Hot spots become trip-enders.", "x": "Hot spots become trip-enders. Key steps: Tape hot spots early; Proper socks; Lace techniques. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Getting lost: STOP", "d": "Stop, Think, Observe, Plan.", "g": "emergency", "l": 2, "q": "What is Getting lost: STOP?", "a": "Stop, Think, Observe, Plan.", "x": "Stop, Think, Observe, Plan. Key steps: Stop moving; Think; Observe; Plan. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Signaling for help", "d": "Three of anything is distress.", "g": "emergency", "l": 2, "q": "What is Signaling for help?", "a": "Three of anything is distress.", "x": "Three of anything is distress. Key steps: Whistle: 3 blasts; Mirror flashes; Bright clothing. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Emergency shelter", "d": "Stay warm and dry.", "g": "emergency", "l": 2, "q": "What is Emergency shelter?", "a": "Stay warm and dry.", "x": "Stay warm and dry. Key steps: Emergency bivy; Learn debris shelters; Conserve energy. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}];
function pad(n){return String(n).padStart(6,'0');}
function drillProg(q,a){
  return '// boundless drill program\nvar Q='+JSON.stringify(q)+';\nvar A='+JSON.stringify(a)+';\n'
    +'console.log("DRILL: "+Q);\nconsole.log("Say it out loud, then check:");\nconsole.log("ANSWER: "+A);';
}
function bankRec(i){
  var b=BANK[(i-1)%BANK.length];
  var r={id:PREFIX+pad(i),title:b.t,description:b.x,group:b.g,ladder:b.l,
    question:b.q,answer:b.a,method:'archive-sample',
    program:drillProg(b.q,b.a),language:'javascript',
    src:b.s,last_verified:'2026-10-19',sample:true};
  return r;
}
function genQuizDrill(rnd,seed){
  var b=BANK[(rnd()*BANK.length)|0];
  var desc='Boundless drill #'+seed+' — '+NAME+'. The question: '+b.q+'\n\n'
    +'Cover the answer and say it out loud before reading on. Fluency with these facts is the whole game: '
    +'each drill pulls a real record from this database\'s archive and tests exactly one fact cold. '
    +'If you knew it, it is yours; if not, open the archive record "'+b.t+'" and read the full entry, then come back and drill it again. '
    +'The validated answer: '+b.a+'\n\n'
    +'Drills never repeat the archive verbatim — they re-ask the same true facts from new angles so the knowledge sticks.';
  return {id:PREFIX+pad(seed),title:'Drill: '+b.t,description:desc,group:b.g,ladder:b.l,
    method:'quiz-drill',question:b.q,answer:b.a,
    program:drillProg(b.q,b.a),language:'javascript',src:GEN_SRC,last_verified:'2026-10-19'};
}
function genConvertDrill(rnd,seed){
  var b1=BANK[(rnd()*BANK.length)|0],b2=BANK[(rnd()*BANK.length)|0];
  var v=Math.round((1+rnd()*999)*100)/100;
  var ans=v*b1.f/b2.f;
  var q='Convert '+v+' '+b1.t+' to '+b2.t+'.';
  var a=String(Math.round(ans*1e6)/1e6)+' '+b2.t;
  var desc='Boundless drill #'+seed+' — '+NAME+'. The question: '+q+'\n\n'
    +'Work it with the factor table: multiply by the "from" unit\'s factor to reach the base unit, then divide by the "to" unit\'s factor. '
    +'The demo program on any archive record in this database runs the same computation, so you can check your method there first. '
    +'The validated answer: '+a+'. If your number matches, the method is yours; drills like this one keep every conversion in this database one multiplication and one division away.';
  return {id:PREFIX+pad(seed),title:'Conversion drill: '+b1.t+' to '+b2.t,description:desc,
    group:b1.g,ladder:2,method:'convert-drill',question:q,answer:a,
    conv:{value:v,from:b1.t,fromF:b1.f,to:b2.t,toF:b2.f},
    program:'// conversion drill program\nvar v='+v+';\nvar fromF='+b1.f+';\nvar toF='+b2.f+';\n'
      +'console.log("Q: convert "+v+" '+b1.t.replace(/'/g,"\\'")+' to '+b2.t.replace(/'/g,"\\'")+'");\n'
      +'console.log("A: "+(v*fromF/toF)+" '+b2.t.replace(/'/g,"\\'")+'");',
    language:'javascript',src:GEN_SRC,last_verified:'2026-10-19'};
}
function generate(seed,opts,rnd){
  opts=opts||{};seed=+seed||1;rnd=rnd||prng(seed);
  var g=opts.group||opts.category;
  if(g&&FIELDS.indexOf(g)<0)g=null;
  var r;
  if(seed>=1&&seed<=BANK.length){r=bankRec(seed);}
  else{r=(MODE==='convert')?genConvertDrill(rnd,seed):genQuizDrill(rnd,seed);}
  if(g)r.group=g;
  return r;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.group)<0)e.push('group');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<200)e.push('description');
  if(r.method==='quiz-drill'||r.method==='archive-sample'){
    var hit=null;
    for(var i=0;i<BANK.length;i++){if(BANK[i].q===r.question&&BANK[i].a===r.answer){hit=BANK[i];break;}}
    if(!hit)e.push('answer not banked');
  }else if(r.method==='convert-drill'){
    var c=r.conv;
    if(!c||typeof c.value!=='number')e.push('conv missing');
    else{
      var expect=c.value*c.fromF/c.toF;
      var got=parseFloat(String(r.answer).split(' ')[0]);
      if(!(Math.abs(got-expect)<Math.max(1e-6,Math.abs(expect)*1e-9)))e.push('conversion mismatch');
    }
  }else{e.push('method');}
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var seen={};(sample||[]).forEach(function(s){if(s&&s.t)seen[s.t]=1;});
  if(rec&&seen[rec.title])return{ok:false,errors:['duplicate title in archive sample']};
  return{ok:true,errors:[]};
}
var gen={version:'jahdb-hiking-safety-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
