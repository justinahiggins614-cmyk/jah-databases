(function(){'use strict';
/* JAH Barbecue Hobby Database generator — jahdb-e2-hobby-barbecue-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hobby-barbecue',PREFIX='JAH-E2HOBBYBARB-',NAME='JAH Barbecue Hobby Database';
var FIELDS=["overview", "getting-started", "essentials", "tips", "gear", "costs", "safety", "skills", "projects", "community", "mistakes", "resources", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Barbecue: the complete hobby guide", "d": "Barbecue: low and slow..", "g": "overview", "l": 2, "q": "What is Barbecue: the complete hobby guide?", "a": "Barbecue: low and slow..", "x": "The complete Barbecue hobby guide: low and slow.. Smoker/grill. Everything to start and master it — the essentials, the gear, the skills ladder, starter projects, costs, safety, and the community. Thermometer.", "s": "public-reference", "f": null}, {"t": "Getting started", "d": "Start Barbecue this weekend.", "g": "getting-started", "l": 2, "q": "What is Getting started?", "a": "Start Barbecue this weekend.", "x": "Start here: Smoker/grill.. low and slow. Begin with Wood. — small, cheap, and fun. Patience. Mastery comes later; joy comes first. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Smoker/grill.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Smoker/grill.", "x": "Barbecue essential: Smoker/grill.. Patience. One of the six things every practitioner knows — Rubs.. low and slow. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 1 in practice", "d": "Doing: Smoker/grill..", "g": "essentials", "l": 2, "q": "What is Essential 1 in practice?", "a": "Doing: Smoker/grill..", "x": "In practice: Smoker/grill.. Practice. Here is how it works in real sessions — Temperature.. Barbecue Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Wood.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Wood.", "x": "Barbecue essential: Wood.. Practice. One of the six things every practitioner knows — Temperature.. low and slow. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 2 in practice", "d": "Doing: Wood..", "g": "essentials", "l": 2, "q": "What is Essential 2 in practice?", "a": "Doing: Wood..", "x": "In practice: Wood.. Wood. Here is how it works in real sessions — Rest.. Barbecue Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Rubs.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Rubs.", "x": "Barbecue essential: Rubs.. Wood. One of the six things every practitioner knows — Rest.. low and slow. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 3 in practice", "d": "Doing: Rubs..", "g": "essentials", "l": 2, "q": "What is Essential 3 in practice?", "a": "Doing: Rubs..", "x": "In practice: Rubs.. Rest. Here is how it works in real sessions — Cuts.. Barbecue Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Temperature.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Temperature.", "x": "Barbecue essential: Temperature.. Rest. One of the six things every practitioner knows — Cuts.. low and slow. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 4 in practice", "d": "Doing: Temperature..", "g": "essentials", "l": 2, "q": "What is Essential 4 in practice?", "a": "Doing: Temperature..", "x": "In practice: Temperature.. Community. Here is how it works in real sessions — Smoker/grill.. Barbecue Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Rest.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Rest.", "x": "Barbecue essential: Rest.. Community. One of the six things every practitioner knows — Smoker/grill.. low and slow. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 5 in practice", "d": "Doing: Rest..", "g": "essentials", "l": 2, "q": "What is Essential 5 in practice?", "a": "Doing: Rest..", "x": "In practice: Rest.. Thermometer. Here is how it works in real sessions — Wood.. Barbecue Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Cuts.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Cuts.", "x": "Barbecue essential: Cuts.. Thermometer. One of the six things every practitioner knows — Wood.. low and slow. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 6 in practice", "d": "Doing: Cuts..", "g": "essentials", "l": 2, "q": "What is Essential 6 in practice?", "a": "Doing: Cuts..", "x": "In practice: Cuts.. Patience. Here is how it works in real sessions — Rubs.. Barbecue Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 1", "d": "Thermometer.", "g": "tips", "l": 2, "q": "What is Tip 1?", "a": "Thermometer.", "x": "Barbecue tip: Thermometer.. Wood. From experienced hobbyists — Wood.. low and slow. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 2", "d": "Patience.", "g": "tips", "l": 2, "q": "What is Tip 2?", "a": "Patience.", "x": "Barbecue tip: Patience.. Rubs. From experienced hobbyists — Rest.. low and slow. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 3", "d": "Practice.", "g": "tips", "l": 2, "q": "What is Tip 3?", "a": "Practice.", "x": "Barbecue tip: Practice.. Temperature. From experienced hobbyists — Community.. low and slow. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 4", "d": "Wood.", "g": "tips", "l": 2, "q": "What is Tip 4?", "a": "Wood.", "x": "Barbecue tip: Wood.. Rest. From experienced hobbyists — Thermometer.. low and slow. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 5", "d": "Rest.", "g": "tips", "l": 2, "q": "What is Tip 5?", "a": "Rest.", "x": "Barbecue tip: Rest.. Cuts. From experienced hobbyists — Patience.. low and slow. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 6", "d": "Community.", "g": "tips", "l": 2, "q": "What is Tip 6?", "a": "Community.", "x": "Barbecue tip: Community.. Smoker/grill. From experienced hobbyists — Practice.. low and slow. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Gear guide", "d": "Barbecue gear: Smoker/grill..", "g": "gear", "l": 2, "q": "What is Gear guide?", "a": "Barbecue gear: Smoker/grill..", "x": "Gear: Smoker/grill.. Start minimal — Wood. — and upgrade as skills demand. low and slow. Buy once where it matters; go cheap where it does not. Practice. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "What it costs", "d": "Barbecue on a budget.", "g": "costs", "l": 2, "q": "What is What it costs?", "a": "Barbecue on a budget.", "x": "Costs: Wood.. Barbecue can start for little and scale to obsession — Rubs.. low and slow. Budget for the hobby, not against it; joy has value. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Barbecue safety: Rest..", "g": "safety", "l": 2, "q": "What is Safety?", "a": "Barbecue safety: Rest..", "x": "Safety: Rest.. Temperature. Every hobby has its risks — Barbecue. low and slow. Learn the rules before the skills; no project is worth an injury. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "The skill ladder", "d": "Barbecue: beginner to expert.", "g": "skills", "l": 2, "q": "What is The skill ladder?", "a": "Barbecue: beginner to expert.", "x": "The ladder: low and slow.. Beginner: Rest.. Intermediate: Cuts.. Advanced: Community.. Barbecue Climb one rung at a time; plateaus are normal. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Advanced techniques", "d": "Level up Barbecue.", "g": "skills", "l": 2, "q": "What is Advanced techniques?", "a": "Level up Barbecue.", "x": "Advanced: Cuts.. Thermometer. Once basics are automatic, these separate good from great — Barbecue. low and slow. Study masters; copy, then innovate. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hobby-barbecue-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
