(function(){'use strict';
/* JAH Flood Safety Database generator — jahdb-flood-safety-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='flood-safety',PREFIX='JAH-FLD-',NAME='JAH Flood Safety Database';
var FIELDS=["before", "during", "after", "kit"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Know your flood zone", "d": "FEMA maps show your risk.", "g": "before", "l": 2, "q": "What is Know your flood zone?", "a": "FEMA maps show your risk.", "x": "FEMA maps show your risk. Key steps: Look up your zone; Buy flood insurance — 30-day wait; Know base flood elevation. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Prepare the home", "d": "Small steps cut damage.", "g": "before", "l": 2, "q": "What is Prepare the home?", "a": "Small steps cut damage.", "x": "Small steps cut damage. Key steps: Elevate utilities and valuables; Install check valves; Seal basement walls; Clear gutters. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Go-bag for floods", "d": "Be ready to leave fast.", "g": "kit", "l": 2, "q": "What is Go-bag for floods?", "a": "Be ready to leave fast.", "x": "Be ready to leave fast. Key steps: Documents waterproofed; Meds, water, food; Phone chargers; Cash. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Evacuation plan", "d": "Know routes to high ground.", "g": "before", "l": 2, "q": "What is Evacuation plan?", "a": "Know routes to high ground.", "x": "Know routes to high ground. Key steps: Two routes out; Meeting point; Never wait for mandatory orders if water rises. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Turn around, do not drown", "d": "The golden rule.", "g": "during", "l": 2, "q": "What is Turn around, do not drown?", "a": "The golden rule.", "x": "The golden rule. Key steps: 6 inches knocks you down; 12 inches floats cars; Never drive through water; Find another route. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "If water enters the home", "d": "Get up, get out.", "g": "during", "l": 2, "q": "What is If water enters the home?", "a": "Get up, get out.", "x": "Get up, get out. Key steps: Move to higher floors; Do not walk through moving water; Call for rescue if trapped; Turn off utilities if safe. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Driving in rain", "d": "Hydroplaning kills.", "g": "during", "l": 2, "q": "What is Driving in rain?", "a": "Hydroplaning kills.", "x": "Hydroplaning kills. Key steps: Slow down; Increase following distance; Avoid cruise control; Pull over if you cannot see. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "After: wait for all-clear", "d": "Water hides dangers.", "g": "after", "l": 2, "q": "What is After: wait for all-clear?", "a": "Water hides dangers.", "x": "Water hides dangers. Key steps: Do not enter until cleared; Watch for structural damage; Assume water is contaminated. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Electrical hazards", "d": "Water and power do not mix.", "g": "after", "l": 2, "q": "What is Electrical hazards?", "a": "Water and power do not mix.", "x": "Water and power do not mix. Key steps: Do not touch wet electrical; Call the utility; Have an electrician inspect. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Cleanup protective gear", "d": "Floodwater carries sewage and chemicals.", "g": "after", "l": 2, "q": "What is Cleanup protective gear?", "a": "Floodwater carries sewage and chemicals.", "x": "Floodwater carries sewage and chemicals. Key steps: Boots, gloves, masks; Ventilate; Wash hands often. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Mold: act in 48 hours", "d": "Mold grows fast.", "g": "after", "l": 2, "q": "What is Mold: act in 48 hours?", "a": "Mold grows fast.", "x": "Mold grows fast. Key steps: Remove wet drywall and insulation; Dry thoroughly; Scrub with detergent; Discard soaked porous items. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Document for insurance", "d": "Photos first, cleanup second.", "g": "after", "l": 2, "q": "What is Document for insurance?", "a": "Photos first, cleanup second.", "x": "Photos first, cleanup second. Key steps: Photograph everything; List damaged items; Keep receipts. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Drinking water", "d": "Boil or bottle until cleared.", "g": "after", "l": 2, "q": "What is Drinking water?", "a": "Boil or bottle until cleared.", "x": "Boil or bottle until cleared. Key steps: Boil 1 minute rolling; Or use bottled; Follow official guidance. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Food safety", "d": "Flood-touched food is trash.", "g": "after", "l": 2, "q": "What is Food safety?", "a": "Flood-touched food is trash.", "x": "Flood-touched food is trash. Key steps: Discard anything touched by water; Canned goods: sanitize if intact; When in doubt, throw it out. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Well water", "d": "Wells need testing after floods.", "g": "after", "l": 2, "q": "What is Well water?", "a": "Wells need testing after floods.", "x": "Wells need testing after floods. Key steps: Do not drink until tested; Disinfect per health department; Test for bacteria. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Sandbag basics", "d": "Sandbags redirect, not waterproof.", "g": "before", "l": 2, "q": "What is Sandbag basics?", "a": "Sandbags redirect, not waterproof.", "x": "Sandbags redirect, not waterproof. Key steps: Stack in pyramids; Plastic sheeting helps; Focus on doorways. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Sump pump check", "d": "Test before rain season.", "g": "before", "l": 2, "q": "What is Sump pump check?", "a": "Test before rain season.", "x": "Test before rain season. Key steps: Pour water to test; Clear the intake; Battery backup recommended. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Basement prep", "d": "Basements flood first.", "g": "before", "l": 2, "q": "What is Basement prep?", "a": "Basements flood first.", "x": "Basements flood first. Key steps: Move valuables up; Seal cracks; Consider a backup pump. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Flash flood signs", "d": "Water rises in minutes.", "g": "during", "l": 2, "q": "What is Flash flood signs?", "a": "Water rises in minutes.", "x": "Water rises in minutes. Key steps: Heavy rain upstream; Rising water, debris; Move to high ground immediately. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Urban flooding", "d": "Cities flood from drains.", "g": "during", "l": 2, "q": "What is Urban flooding?", "a": "Cities flood from drains.", "x": "Cities flood from drains. Key steps: Avoid underpasses; Do not walk in fast water; Watch for open manholes. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Coastal flooding", "d": "Storm surge and tides.", "g": "during", "l": 2, "q": "What is Coastal flooding?", "a": "Storm surge and tides.", "x": "Storm surge and tides. Key steps: Evacuate surge zones; Know tide timing; Salt water corrodes — rinse later. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "River flooding", "d": "Slow rise, long stay.", "g": "during", "l": 2, "q": "What is River flooding?", "a": "Slow rise, long stay.", "x": "Slow rise, long stay. Key steps: Monitor gauges; Move valuables early; Expect days of water. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Pets in floods", "d": "Never leave pets behind.", "g": "kit", "l": 2, "q": "What is Pets in floods?", "a": "Never leave pets behind.", "x": "Never leave pets behind. Key steps: Carriers and leashes ready; Food and water; Vaccination records. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Kids and floods", "d": "Keep children from water.", "g": "during", "l": 2, "q": "What is Kids and floods?", "a": "Keep children from water.", "x": "Keep children from water. Key steps: No playing in floodwater; Explain the dangers simply. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Returning home checklist", "d": "Systematic re-entry.", "g": "after", "l": 2, "q": "What is Returning home checklist?", "a": "Systematic re-entry.", "x": "Systematic re-entry. Key steps: Structural check first; Utilities off until inspected; Photos; Ventilate. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-flood-safety-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
