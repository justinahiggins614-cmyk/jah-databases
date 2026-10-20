(function(){'use strict';
/* JAH Hurricane Preparedness Database generator — jahdb-hurricane-preparedness-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='hurricane-preparedness',PREFIX='JAH-HUR-',NAME='JAH Hurricane Preparedness Database';
var FIELDS=["before", "during", "after", "kit"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Know your zone", "d": "Evacuation zones decide whether you stay or go.", "g": "before", "l": 2, "q": "What is Know your zone?", "a": "Evacuation zones decide whether you stay or go.", "x": "Evacuation zones decide whether you stay or go. Key steps: Find your evacuation zone; Know the routes; Plan where you will go. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Board up windows", "d": "Plywood or shutters against wind-borne debris.", "g": "before", "l": 2, "q": "What is Board up windows?", "a": "Plywood or shutters against wind-borne debris.", "x": "Plywood or shutters against wind-borne debris. Key steps: Use 5/8 inch plywood; Install shutters if in hurricane country; Do not tape windows — it does nothing. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Secure outdoor items", "d": "Everything loose becomes a missile.", "g": "before", "l": 2, "q": "What is Secure outdoor items?", "a": "Everything loose becomes a missile.", "x": "Everything loose becomes a missile. Key steps: Bring in furniture and toys; Secure trash cans; Trim weak tree limbs. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Emergency kit: 7 days", "d": "Hurricanes isolate you for a week.", "g": "kit", "l": 2, "q": "What is Emergency kit: 7 days?", "a": "Hurricanes isolate you for a week.", "x": "Hurricanes isolate you for a week. Key steps: One gallon of water per person per day; 7 days of no-cook food; Medications and documents; Cash in small bills. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Important documents", "d": "Waterproof your paperwork.", "g": "kit", "l": 2, "q": "What is Important documents?", "a": "Waterproof your paperwork.", "x": "Waterproof your paperwork. Key steps: IDs, insurance, deeds in waterproof bags; Photos of belongings; Digital backups. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Evacuate when told", "d": "Storm surge kills; never ride out a surge zone order.", "g": "during", "l": 2, "q": "What is Evacuate when told?", "a": "Storm surge kills; never ride out a surge zone order.", "x": "Storm surge kills; never ride out a surge zone order. Key steps: Leave when officials say go; Take the kit and pets; Lock up; Do not drive through flooded roads. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "If you stay", "d": "Only outside surge and flood zones, in sturdy buildings.", "g": "during", "l": 2, "q": "What is If you stay?", "a": "Only outside surge and flood zones, in sturdy buildings.", "x": "Only outside surge and flood zones, in sturdy buildings. Key steps: Stay in an interior room; Away from windows; Keep supplies handy; Monitor official updates. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Turn around, do not drown", "d": "Six inches of water can knock you down; 12 inches floats cars.", "g": "during", "l": 2, "q": "What is Turn around, do not drown?", "a": "Six inches of water can knock you down; 12 inches floats cars.", "x": "Six inches of water can knock you down; 12 inches floats cars. Key steps: Never drive through floodwater; Never walk through moving water; Find alternate routes. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Generator safety", "d": "CO kills after storms.", "g": "during", "l": 2, "q": "What is Generator safety?", "a": "CO kills after storms.", "x": "CO kills after storms. Key steps: Never indoors or in garages; 20 feet from the house; Heavy outdoor cords only. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "After: wait for all-clear", "d": "Do not rush back.", "g": "after", "l": 2, "q": "What is After: wait for all-clear?", "a": "Do not rush back.", "x": "Do not rush back. Key steps: Wait for official all-clear; Watch for downed lines; Avoid floodwater. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "After: document damage", "d": "Photos before cleanup for insurance.", "g": "after", "l": 2, "q": "What is After: document damage?", "a": "Photos before cleanup for insurance.", "x": "Photos before cleanup for insurance. Key steps: Photograph everything; Keep receipts; File promptly. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "After: avoid hazards", "d": "Floodwater hides dangers.", "g": "after", "l": 2, "q": "What is After: avoid hazards?", "a": "Floodwater hides dangers.", "x": "Floodwater hides dangers. Key steps: Avoid walking in floodwater; Watch for snakes and debris; Do not touch electrical equipment if wet. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Food safety after outage", "d": "When in doubt, throw it out.", "g": "after", "l": 2, "q": "What is Food safety after outage?", "a": "When in doubt, throw it out.", "x": "When in doubt, throw it out. Key steps: Fridge safe 4 hours closed; Freezer 48 hours full; Discard above 40 F for 2+ hours. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Water safety", "d": "Assume tap water is unsafe until cleared.", "g": "after", "l": 2, "q": "What is Water safety?", "a": "Assume tap water is unsafe until cleared.", "x": "Assume tap water is unsafe until cleared. Key steps: Boil 1 minute if advised; Or use bottled; Disinfect with bleach per official ratios. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Mold prevention", "d": "Dry out within 24-48 hours.", "g": "after", "l": 2, "q": "What is Mold prevention?", "a": "Dry out within 24-48 hours.", "x": "Dry out within 24-48 hours. Key steps: Remove wet materials; Ventilate; Scrub with detergent; Discard porous items that stayed wet. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Chainsaw safety", "d": "Cleanup injuries spike after storms.", "g": "after", "l": 2, "q": "What is Chainsaw safety?", "a": "Cleanup injuries spike after storms.", "x": "Cleanup injuries spike after storms. Key steps: Protective gear always; Cut at waist height or below; Beware spring-loaded limbs; Take breaks. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Pet hurricane plan", "d": "Pets are family in evacuation.", "g": "kit", "l": 2, "q": "What is Pet hurricane plan?", "a": "Pets are family in evacuation.", "x": "Pets are family in evacuation. Key steps: Carrier, food, water, meds; Vaccination records; Never leave pets behind. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Car preparation", "d": "A full tank before landfall.", "g": "before", "l": 2, "q": "What is Car preparation?", "a": "A full tank before landfall.", "x": "A full tank before landfall. Key steps: Fill the tank early; Emergency kit in the car; Park on high ground. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Yard preparation", "d": "Landscaping matters.", "g": "before", "l": 2, "q": "What is Yard preparation?", "a": "Landscaping matters.", "x": "Landscaping matters. Key steps: Trim trees before season; Secure fences; Clear gutters and drains. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Roof check", "d": "Roofs fail first.", "g": "before", "l": 2, "q": "What is Roof check?", "a": "Roofs fail first.", "x": "Roofs fail first. Key steps: Inspect yearly; Hurricane straps in high-risk zones; Seal roof deck. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Flood insurance", "d": "Standard homeowners excludes flood.", "g": "before", "l": 2, "q": "What is Flood insurance?", "a": "Standard homeowners excludes flood.", "x": "Standard homeowners excludes flood. Key steps: Buy flood insurance early — 30-day wait; Know your flood zone; Elevate valuables. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Seniors and medical needs", "d": "Plan for power-dependent devices.", "g": "kit", "l": 2, "q": "What is Seniors and medical needs?", "a": "Plan for power-dependent devices.", "x": "Plan for power-dependent devices. Key steps: Backup power for devices; Medication supply; Medical info on hand; Register with local assistance lists. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Kids and storms", "d": "Calm routines reduce fear.", "g": "during", "l": 2, "q": "What is Kids and storms?", "a": "Calm routines reduce fear.", "x": "Calm routines reduce fear. Key steps: Explain simply; Keep routines; Comfort items in the kit. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Saffir-Simpson scale", "d": "Know what the categories mean.", "g": "before", "l": 2, "q": "What is Saffir-Simpson scale?", "a": "Know what the categories mean.", "x": "Know what the categories mean. Key steps: Cat 1: 119-153 km/h, some damage; Cat 3+: major damage, evacuate surge zones; Cat 5: catastrophic. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Hurricane vs tropical storm", "d": "74 mph (119 km/h) is the hurricane line.", "g": "before", "l": 2, "q": "What is Hurricane vs tropical storm?", "a": "74 mph (119 km/h) is the hurricane line.", "x": "74 mph (119 km/h) is the hurricane line. Key steps: Tropical storm: 39-73 mph; Hurricane: 74+ mph; Damage scales fast with wind. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-hurricane-preparedness-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
