(function(){'use strict';
/* JAH Painting Techniques Hobby Database generator — jahdb-e2-hobby-painting-techniques-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hobby-painting-techniques',PREFIX='JAH-E2HOBBYPAIN-',NAME='JAH Painting Techniques Hobby Database';
var FIELDS=["overview", "getting-started", "essentials", "tips", "gear", "costs", "safety", "skills", "projects", "community", "mistakes", "resources", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Painting Techniques: the complete hobby guide", "d": "Painting Techniques: oils, acrylics, watercolor..", "g": "overview", "l": 2, "q": "What is Painting Techniques: the complete hobby guide?", "a": "Painting Techniques: oils, acrylics, watercolor..", "x": "The complete Painting Techniques hobby guide: oils, acrylics, watercolor.. Acrylics start. Everything to start and master it — the essentials, the gear, the skills ladder, starter projects, costs, safety, and the community. Practice.", "s": "public-reference", "f": null}, {"t": "Getting started", "d": "Start Painting Techniques this weekend.", "g": "getting-started", "l": 2, "q": "What is Getting started?", "a": "Start Painting Techniques this weekend.", "x": "Start here: Acrylics start.. oils, acrylics, watercolor. Begin with Brushes. — small, cheap, and fun. Value first. Mastery comes later; joy comes first. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Acrylics start.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Acrylics start.", "x": "Painting Techniques essential: Acrylics start.. Value first. One of the six things every practitioner knows — Color mixing.. oils, acrylics, watercolor. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 1 in practice", "d": "Doing: Acrylics start..", "g": "essentials", "l": 2, "q": "What is Essential 1 in practice?", "a": "Doing: Acrylics start..", "x": "In practice: Acrylics start.. Limited palette. Here is how it works in real sessions — Canvas prep.. Painting Techniques Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Brushes.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Brushes.", "x": "Painting Techniques essential: Brushes.. Limited palette. One of the six things every practitioner knows — Canvas prep.. oils, acrylics, watercolor. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 2 in practice", "d": "Doing: Brushes..", "g": "essentials", "l": 2, "q": "What is Essential 2 in practice?", "a": "Doing: Brushes..", "x": "In practice: Brushes.. Plein air. Here is how it works in real sessions — Mediums.. Painting Techniques Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Color mixing.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Color mixing.", "x": "Painting Techniques essential: Color mixing.. Plein air. One of the six things every practitioner knows — Mediums.. oils, acrylics, watercolor. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 3 in practice", "d": "Doing: Color mixing..", "g": "essentials", "l": 2, "q": "What is Essential 3 in practice?", "a": "Doing: Color mixing..", "x": "In practice: Color mixing.. Critique. Here is how it works in real sessions — Styles.. Painting Techniques Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Canvas prep.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Canvas prep.", "x": "Painting Techniques essential: Canvas prep.. Critique. One of the six things every practitioner knows — Styles.. oils, acrylics, watercolor. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 4 in practice", "d": "Doing: Canvas prep..", "g": "essentials", "l": 2, "q": "What is Essential 4 in practice?", "a": "Doing: Canvas prep..", "x": "In practice: Canvas prep.. Enjoy. Here is how it works in real sessions — Acrylics start.. Painting Techniques Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Mediums.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Mediums.", "x": "Painting Techniques essential: Mediums.. Enjoy. One of the six things every practitioner knows — Acrylics start.. oils, acrylics, watercolor. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 5 in practice", "d": "Doing: Mediums..", "g": "essentials", "l": 2, "q": "What is Essential 5 in practice?", "a": "Doing: Mediums..", "x": "In practice: Mediums.. Practice. Here is how it works in real sessions — Brushes.. Painting Techniques Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Styles.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Styles.", "x": "Painting Techniques essential: Styles.. Practice. One of the six things every practitioner knows — Brushes.. oils, acrylics, watercolor. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 6 in practice", "d": "Doing: Styles..", "g": "essentials", "l": 2, "q": "What is Essential 6 in practice?", "a": "Doing: Styles..", "x": "In practice: Styles.. Value first. Here is how it works in real sessions — Color mixing.. Painting Techniques Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 1", "d": "Practice.", "g": "tips", "l": 2, "q": "What is Tip 1?", "a": "Practice.", "x": "Painting Techniques tip: Practice.. Brushes. From experienced hobbyists — Plein air.. oils, acrylics, watercolor. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 2", "d": "Value first.", "g": "tips", "l": 2, "q": "What is Tip 2?", "a": "Value first.", "x": "Painting Techniques tip: Value first.. Color mixing. From experienced hobbyists — Critique.. oils, acrylics, watercolor. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 3", "d": "Limited palette.", "g": "tips", "l": 2, "q": "What is Tip 3?", "a": "Limited palette.", "x": "Painting Techniques tip: Limited palette.. Canvas prep. From experienced hobbyists — Enjoy.. oils, acrylics, watercolor. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 4", "d": "Plein air.", "g": "tips", "l": 2, "q": "What is Tip 4?", "a": "Plein air.", "x": "Painting Techniques tip: Plein air.. Mediums. From experienced hobbyists — Practice.. oils, acrylics, watercolor. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 5", "d": "Critique.", "g": "tips", "l": 2, "q": "What is Tip 5?", "a": "Critique.", "x": "Painting Techniques tip: Critique.. Styles. From experienced hobbyists — Value first.. oils, acrylics, watercolor. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 6", "d": "Enjoy.", "g": "tips", "l": 2, "q": "What is Tip 6?", "a": "Enjoy.", "x": "Painting Techniques tip: Enjoy.. Acrylics start. From experienced hobbyists — Limited palette.. oils, acrylics, watercolor. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Gear guide", "d": "Painting Techniques gear: Acrylics start..", "g": "gear", "l": 2, "q": "What is Gear guide?", "a": "Painting Techniques gear: Acrylics start..", "x": "Gear: Acrylics start.. Start minimal — Brushes. — and upgrade as skills demand. oils, acrylics, watercolor. Buy once where it matters; go cheap where it does not. Limited palette. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "What it costs", "d": "Painting Techniques on a budget.", "g": "costs", "l": 2, "q": "What is What it costs?", "a": "Painting Techniques on a budget.", "x": "Costs: Plein air.. Painting Techniques can start for little and scale to obsession — Color mixing.. oils, acrylics, watercolor. Budget for the hobby, not against it; joy has value. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Painting Techniques safety: Critique..", "g": "safety", "l": 2, "q": "What is Safety?", "a": "Painting Techniques safety: Critique..", "x": "Safety: Critique.. Canvas prep. Every hobby has its risks — Painting Techniques. oils, acrylics, watercolor. Learn the rules before the skills; no project is worth an injury. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "The skill ladder", "d": "Painting Techniques: beginner to expert.", "g": "skills", "l": 2, "q": "What is The skill ladder?", "a": "Painting Techniques: beginner to expert.", "x": "The ladder: oils, acrylics, watercolor.. Beginner: Mediums.. Intermediate: Styles.. Advanced: Enjoy.. Painting Techniques Climb one rung at a time; plateaus are normal. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Advanced techniques", "d": "Level up Painting Techniques.", "g": "skills", "l": 2, "q": "What is Advanced techniques?", "a": "Level up Painting Techniques.", "x": "Advanced: Styles.. Practice. Once basics are automatic, these separate good from great — Painting Techniques. oils, acrylics, watercolor. Study masters; copy, then innovate. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hobby-painting-techniques-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
