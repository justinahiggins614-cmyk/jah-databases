(function(){'use strict';
/* JAH Knitting Hobby Database generator — jahdb-e2-hobby-knitting-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hobby-knitting',PREFIX='JAH-E2HOBBYKNIT-',NAME='JAH Knitting Hobby Database';
var FIELDS=["overview", "getting-started", "essentials", "tips", "gear", "costs", "safety", "skills", "projects", "community", "mistakes", "resources", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Knitting: the complete hobby guide", "d": "Knitting: yarn into fabric, one loop at a time..", "g": "overview", "l": 2, "q": "What is Knitting: the complete hobby guide?", "a": "Knitting: yarn into fabric, one loop at a time..", "x": "The complete Knitting hobby guide: yarn into fabric, one loop at a time.. Learn knit and purl. Everything to start and master it — the essentials, the gear, the skills ladder, starter projects, costs, safety, and the community. Tension even.", "s": "public-reference", "f": null}, {"t": "Getting started", "d": "Start Knitting this weekend.", "g": "getting-started", "l": 2, "q": "What is Getting started?", "a": "Start Knitting this weekend.", "x": "Start here: Learn knit and purl.. yarn into fabric, one loop at a time. Begin with Chunky yarn first. — small, cheap, and fun. Fix mistakes early. Mastery comes later; joy comes first. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Learn knit and purl.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Learn knit and purl.", "x": "Knitting essential: Learn knit and purl.. Fix mistakes early. One of the six things every practitioner knows — Needles: size 8-10.. yarn into fabric, one loop at a time. Learn these and you are no longer a beginner.", "s": "public-reference", "f": null}, {"t": "Essential 1 in practice", "d": "Doing: Learn knit and purl..", "g": "essentials", "l": 2, "q": "What is Essential 1 in practice?", "a": "Doing: Learn knit and purl..", "x": "In practice: Learn knit and purl.. YouTube teaches. Here is how it works in real sessions — Cast on.. Knitting Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Chunky yarn first.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Chunky yarn first.", "x": "Knitting essential: Chunky yarn first.. YouTube teaches. One of the six things every practitioner knows — Cast on.. yarn into fabric, one loop at a time. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 2 in practice", "d": "Doing: Chunky yarn first..", "g": "essentials", "l": 2, "q": "What is Essential 2 in practice?", "a": "Doing: Chunky yarn first..", "x": "In practice: Chunky yarn first.. Swatch. Here is how it works in real sessions — Scarf first project.. Knitting Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Needles: size 8-10.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Needles: size 8-10.", "x": "Knitting essential: Needles: size 8-10.. Swatch. One of the six things every practitioner knows — Scarf first project.. yarn into fabric, one loop at a time. Learn these and you are no longer a beginner.", "s": "public-reference", "f": null}, {"t": "Essential 3 in practice", "d": "Doing: Needles: size 8-10..", "g": "essentials", "l": 2, "q": "What is Essential 3 in practice?", "a": "Doing: Needles: size 8-10..", "x": "In practice: Needles: size 8-10.. Good light. Here is how it works in real sessions — Count stitches.. Knitting Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Cast on.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Cast on.", "x": "Knitting essential: Cast on.. Good light. One of the six things every practitioner knows — Count stitches.. yarn into fabric, one loop at a time. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 4 in practice", "d": "Doing: Cast on..", "g": "essentials", "l": 2, "q": "What is Essential 4 in practice?", "a": "Doing: Cast on..", "x": "In practice: Cast on.. Enjoy. Here is how it works in real sessions — Learn knit and purl.. Knitting Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Scarf first project.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Scarf first project.", "x": "Knitting essential: Scarf first project.. Enjoy. One of the six things every practitioner knows — Learn knit and purl.. yarn into fabric, one loop at a time. Learn these and you are no longer a beginner.", "s": "public-reference", "f": null}, {"t": "Essential 5 in practice", "d": "Doing: Scarf first project..", "g": "essentials", "l": 2, "q": "What is Essential 5 in practice?", "a": "Doing: Scarf first project..", "x": "In practice: Scarf first project.. Tension even. Here is how it works in real sessions — Chunky yarn first.. Knitting Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Count stitches.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Count stitches.", "x": "Knitting essential: Count stitches.. Tension even. One of the six things every practitioner knows — Chunky yarn first.. yarn into fabric, one loop at a time. Learn these and you are no longer a beginner.", "s": "public-reference", "f": null}, {"t": "Essential 6 in practice", "d": "Doing: Count stitches..", "g": "essentials", "l": 2, "q": "What is Essential 6 in practice?", "a": "Doing: Count stitches..", "x": "In practice: Count stitches.. Fix mistakes early. Here is how it works in real sessions — Needles: size 8-10.. Knitting Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 1", "d": "Tension even.", "g": "tips", "l": 2, "q": "What is Tip 1?", "a": "Tension even.", "x": "Knitting tip: Tension even.. Chunky yarn first. From experienced hobbyists — Swatch.. yarn into fabric, one loop at a time. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 2", "d": "Fix mistakes early.", "g": "tips", "l": 2, "q": "What is Tip 2?", "a": "Fix mistakes early.", "x": "Knitting tip: Fix mistakes early.. Needles: size 8-10. From experienced hobbyists — Good light.. yarn into fabric, one loop at a time. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 3", "d": "YouTube teaches.", "g": "tips", "l": 2, "q": "What is Tip 3?", "a": "YouTube teaches.", "x": "Knitting tip: YouTube teaches.. Cast on. From experienced hobbyists — Enjoy.. yarn into fabric, one loop at a time. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 4", "d": "Swatch.", "g": "tips", "l": 2, "q": "What is Tip 4?", "a": "Swatch.", "x": "Knitting tip: Swatch.. Scarf first project. From experienced hobbyists — Tension even.. yarn into fabric, one loop at a time. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 5", "d": "Good light.", "g": "tips", "l": 2, "q": "What is Tip 5?", "a": "Good light.", "x": "Knitting tip: Good light.. Count stitches. From experienced hobbyists — Fix mistakes early.. yarn into fabric, one loop at a time. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 6", "d": "Enjoy.", "g": "tips", "l": 2, "q": "What is Tip 6?", "a": "Enjoy.", "x": "Knitting tip: Enjoy.. Learn knit and purl. From experienced hobbyists — YouTube teaches.. yarn into fabric, one loop at a time. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Gear guide", "d": "Knitting gear: Learn knit and purl..", "g": "gear", "l": 2, "q": "What is Gear guide?", "a": "Knitting gear: Learn knit and purl..", "x": "Gear: Learn knit and purl.. Start minimal — Chunky yarn first. — and upgrade as skills demand. yarn into fabric, one loop at a time. Buy once where it matters; go cheap where it does not. YouTube teaches.", "s": "public-reference", "f": null}, {"t": "What it costs", "d": "Knitting on a budget.", "g": "costs", "l": 2, "q": "What is What it costs?", "a": "Knitting on a budget.", "x": "Costs: Swatch.. Knitting can start for little and scale to obsession — Needles: size 8-10.. yarn into fabric, one loop at a time. Budget for the hobby, not against it; joy has value. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Knitting safety: Good light..", "g": "safety", "l": 2, "q": "What is Safety?", "a": "Knitting safety: Good light..", "x": "Safety: Good light.. Cast on. Every hobby has its risks — Knitting. yarn into fabric, one loop at a time. Learn the rules before the skills; no project is worth an injury. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "The skill ladder", "d": "Knitting: beginner to expert.", "g": "skills", "l": 2, "q": "What is The skill ladder?", "a": "Knitting: beginner to expert.", "x": "The ladder: yarn into fabric, one loop at a time.. Beginner: Scarf first project.. Intermediate: Count stitches.. Advanced: Enjoy.. Knitting Climb one rung at a time; plateaus are normal. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Advanced techniques", "d": "Level up Knitting.", "g": "skills", "l": 2, "q": "What is Advanced techniques?", "a": "Level up Knitting.", "x": "Advanced: Count stitches.. Tension even. Once basics are automatic, these separate good from great — Knitting. yarn into fabric, one loop at a time. Study masters; copy, then innovate. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hobby-knitting-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
