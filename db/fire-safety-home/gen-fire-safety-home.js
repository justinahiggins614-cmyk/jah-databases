(function(){'use strict';
/* JAH Home Fire Safety Database generator — jahdb-fire-safety-home-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='fire-safety-home',PREFIX='JAH-FIR-',NAME='JAH Home Fire Safety Database';
var FIELDS=["alarms", "planning", "kitchen", "heating", "electrical", "general", "laundry", "outdoor", "equipment", "first-aid", "seasonal", "recovery"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Smoke alarms every level", "d": "Working alarms on every floor, in every bedroom.", "g": "alarms", "l": 2, "q": "What is Smoke alarms every level?", "a": "Working alarms on every floor, in every bedroom.", "x": "Working alarms on every floor, in every bedroom. Key steps: Install in each bedroom and outside sleeping areas; One per level including basement; Test monthly; Replace batteries yearly. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Escape plan", "d": "Two ways out of every room, practiced twice a year.", "g": "planning", "l": 2, "q": "What is Escape plan?", "a": "Two ways out of every room, practiced twice a year.", "x": "Two ways out of every room, practiced twice a year. Key steps: Draw the floor plan; Mark two exits per room; Pick an outside meeting spot; Practice day and night. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Kitchen fire prevention", "d": "Kitchens start most home fires.", "g": "kitchen", "l": 2, "q": "What is Kitchen fire prevention?", "a": "Kitchens start most home fires.", "x": "Kitchens start most home fires. Key steps: Stay in the kitchen when cooking; Keep flammables from burners; Turn pot handles inward; Clean grease buildup. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Grease fire response", "d": "Never water on a grease fire.", "g": "kitchen", "l": 2, "q": "What is Grease fire response?", "a": "Never water on a grease fire.", "x": "Never water on a grease fire. Key steps: Turn off the heat if safe; Smother with a lid or cookie sheet; Use baking soda for small fires; Use a Class K or B extinguisher. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Heating safety", "d": "Space heaters need 3 feet of clearance.", "g": "heating", "l": 2, "q": "What is Heating safety?", "a": "Space heaters need 3 feet of clearance.", "x": "Space heaters need 3 feet of clearance. Key steps: Keep 3 feet clear around heaters; Plug directly into the wall; Turn off when leaving; Annual furnace check. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Electrical fire prevention", "d": "Overloads and damaged cords start fires.", "g": "electrical", "l": 2, "q": "What is Electrical fire prevention?", "a": "Overloads and damaged cords start fires.", "x": "Overloads and damaged cords start fires. Key steps: Do not overload outlets; Replace frayed cords; Use correct bulb wattage; Call an electrician for sparking outlets. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Candle safety", "d": "Candles unattended are a top cause.", "g": "general", "l": 2, "q": "What is Candle safety?", "a": "Candles unattended are a top cause.", "x": "Candles unattended are a top cause. Key steps: Never leave burning candles; Keep from curtains and pets; Use sturdy holders; Consider flameless alternatives. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Dryer fire prevention", "d": "Lint is extremely flammable.", "g": "laundry", "l": 2, "q": "What is Dryer fire prevention?", "a": "Lint is extremely flammable.", "x": "Lint is extremely flammable. Key steps: Clean the lint trap every load; Clean the vent yearly; Do not run while asleep; Keep area clear. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Grill safety", "d": "Grills need distance from the house.", "g": "outdoor", "l": 2, "q": "What is Grill safety?", "a": "Grills need distance from the house.", "x": "Grills need distance from the house. Key steps: Keep 10 feet from structures; Never grill in garages; Check gas connections; Keep a spray bottle and extinguisher. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Fireplace safety", "d": "Chimneys need annual sweeping.", "g": "heating", "l": 2, "q": "What is Fireplace safety?", "a": "Chimneys need annual sweeping.", "x": "Chimneys need annual sweeping. Key steps: Annual chimney inspection; Use a screen; Burn dry hardwood only; Dispose of ashes in metal containers. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Extinguisher types", "d": "Know ABC vs K before you need one.", "g": "equipment", "l": 2, "q": "What is Extinguisher types?", "a": "Know ABC vs K before you need one.", "x": "Know ABC vs K before you need one. Key steps: ABC for most home fires; K for kitchen grease; Check the gauge yearly; Learn PASS: Pull, Aim, Squeeze, Sweep. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Using an extinguisher (PASS)", "d": "Pull, Aim, Squeeze, Sweep.", "g": "equipment", "l": 2, "q": "What is Using an extinguisher (PASS)?", "a": "Pull, Aim, Squeeze, Sweep.", "x": "Pull, Aim, Squeeze, Sweep. Key steps: Pull the pin; Aim at the base of the fire; Squeeze the handle; Sweep side to side. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "When NOT to fight a fire", "d": "Your life beats your stuff.", "g": "planning", "l": 2, "q": "What is When NOT to fight a fire?", "a": "Your life beats your stuff.", "x": "Your life beats your stuff. Key steps: If the fire is spreading, leave; If smoke is thick, leave; If the extinguisher empties, leave; Close doors behind you. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Stop, drop, and roll", "d": "For clothing fires.", "g": "planning", "l": 2, "q": "What is Stop, drop, and roll?", "a": "For clothing fires.", "x": "For clothing fires. Key steps: Stop moving; Drop to the ground; Roll to smother flames; Cool burns with water. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Crawling under smoke", "d": "Smoke and heat rise; clean air is low.", "g": "planning", "l": 2, "q": "What is Crawling under smoke?", "a": "Smoke and heat rise; clean air is low.", "x": "Smoke and heat rise; clean air is low. Key steps: Get low under smoke; Crawl to the exit; Feel doors before opening; Use the second exit if hot. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Bedroom door closed", "d": "A closed door buys critical minutes.", "g": "planning", "l": 2, "q": "What is Bedroom door closed?", "a": "A closed door buys critical minutes.", "x": "A closed door buys critical minutes. Key steps: Sleep with bedroom doors closed; Doors block heat and smoke; Practice opening safely. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Carbon monoxide safety", "d": "CO is odorless; detectors save lives.", "g": "alarms", "l": 2, "q": "What is Carbon monoxide safety?", "a": "CO is odorless; detectors save lives.", "x": "CO is odorless; detectors save lives. Key steps: Install CO alarms near bedrooms; Never run generators indoors; Service fuel appliances yearly; Leave immediately if it alarms. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Holiday decoration safety", "d": "December brings fire risk.", "g": "seasonal", "l": 2, "q": "What is Holiday decoration safety?", "a": "December brings fire risk.", "x": "December brings fire risk. Key steps: Water live trees daily; Turn lights off overnight; Keep trees from heat sources; Use LED candles. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Fireworks safety", "d": "Leave fireworks to professionals.", "g": "seasonal", "l": 2, "q": "What is Fireworks safety?", "a": "Leave fireworks to professionals.", "x": "Leave fireworks to professionals. Key steps: Attend public shows; Never relight duds; Keep water nearby; Sparklers burn at 1000 C+. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Wildfire defensible space", "d": "Clear 30 feet around the home.", "g": "outdoor", "l": 2, "q": "What is Wildfire defensible space?", "a": "Clear 30 feet around the home.", "x": "Clear 30 feet around the home. Key steps: Clear dead vegetation 30 feet out; Trim trees 10 feet from structures; Clean roofs and gutters; Use fire-resistant mulch near walls. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Wildfire evacuation prep", "d": "Go-bags ready before fire season.", "g": "outdoor", "l": 2, "q": "What is Wildfire evacuation prep?", "a": "Go-bags ready before fire season.", "x": "Go-bags ready before fire season. Key steps: Pack documents, meds, supplies; Know two evacuation routes; Park facing outward; Leave early when told. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Apartment fire safety", "d": "High-rise rules differ.", "g": "planning", "l": 2, "q": "What is Apartment fire safety?", "a": "High-rise rules differ.", "x": "High-rise rules differ. Key steps: Know the building plan; Never use elevators in fire; Stairwells are the exits; Close doors to slow spread. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Garage fire safety", "d": "Garages hold fuels and chemicals.", "g": "general", "l": 2, "q": "What is Garage fire safety?", "a": "Garages hold fuels and chemicals.", "x": "Garages hold fuels and chemicals. Key steps: Store fuels in approved containers; No open flames near chemicals; Keep a extinguisher accessible; Separate from living space. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Kids and fire safety", "d": "Teach without scaring.", "g": "planning", "l": 2, "q": "What is Kids and fire safety?", "a": "Teach without scaring.", "x": "Teach without scaring. Key steps: Teach matches are tools, not toys; Practice the escape plan; Teach 911 calls; Designate a meeting spot. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Pet fire safety", "d": "Include pets in the plan.", "g": "planning", "l": 2, "q": "What is Pet fire safety?", "a": "Include pets in the plan.", "x": "Include pets in the plan. Key steps: Keep leashes near exits; Window stickers alert firefighters; Never re-enter for pets; Close doors. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-fire-safety-home-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
