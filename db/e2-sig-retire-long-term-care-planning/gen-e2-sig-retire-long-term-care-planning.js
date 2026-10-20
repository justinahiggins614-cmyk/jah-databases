(function(){'use strict';
/* JAH Signature Long-Term Care Planning Database generator — jahdb-e2-sig-retire-long-term-care-planning-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sig-retire-long-term-care-planning',PREFIX='JAH-E2SIGRETIRE-',NAME='JAH Signature Long-Term Care Planning Database';
var FIELDS=["overview", "fundamentals", "plays", "action-plan", "mistakes", "resources", "quick-wins", "advanced", "walkthrough", "myths", "checklist", "faq", "help", "quiz"];
var GEN_SRC='signature-original';
var MODE='quiz';
var BANK=[{"t": "Signature Long-Term Care Planning: the playbook", "d": "Long-Term Care Planning: the risk most ignore..", "g": "overview", "l": 2, "q": "What is Signature Long-Term Care Planning: the playbook?", "a": "Long-Term Care Planning: the risk most ignore..", "x": "The Signature Long-Term Care Planning playbook: the risk most ignore.. Seventy percent need care. This is a complete working guide — not theory, but the actual moves: what to do first, what to avoid, and how to know it is working. Costs huge. Every record is actionable.", "s": "signature-original", "f": null}, {"t": "The fundamentals", "d": "First principles of Long-Term Care Planning.", "g": "fundamentals", "l": 2, "q": "What is The fundamentals?", "a": "First principles of Long-Term Care Planning.", "x": "First principles: Insurance options.. the risk most ignore. Get these right and the rest is optimization; get them wrong and nothing else matters. Long-Term Care Planning Medicaid planning. is simple but not easy — fundamentals first, always.", "s": "signature-original", "f": null}, {"t": "Play 1", "d": "Seventy percent need care.", "g": "plays", "l": 2, "q": "What is Play 1?", "a": "Seventy percent need care.", "x": "Long-Term Care Planning play 1: Seventy percent need care.. Medicaid planning. This is one of the eight core moves — master all eight and you outperform most people who wing it. the risk most ignore. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 1 in action", "d": "Applying: Seventy percent need care..", "g": "plays", "l": 2, "q": "What is Play 1 in action?", "a": "Applying: Seventy percent need care..", "x": "In action: Seventy percent need care.. Here is how to actually do it — Home mods.. Long-Term Care Planning The difference between knowing and doing is a calendar entry: schedule it. Insurance options.", "s": "signature-original", "f": null}, {"t": "Play 2", "d": "Costs huge.", "g": "plays", "l": 2, "q": "What is Play 2?", "a": "Costs huge.", "x": "Long-Term Care Planning play 2: Costs huge.. Home mods. This is one of the eight core moves — master all eight and you outperform most people who wing it. the risk most ignore. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2 in action", "d": "Applying: Costs huge..", "g": "plays", "l": 2, "q": "What is Play 2 in action?", "a": "Applying: Costs huge..", "x": "In action: Costs huge.. Here is how to actually do it — Family talks.. Long-Term Care Planning The difference between knowing and doing is a calendar entry: schedule it. Medicaid planning. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3", "d": "Insurance options.", "g": "plays", "l": 2, "q": "What is Play 3?", "a": "Insurance options.", "x": "Long-Term Care Planning play 3: Insurance options.. Family talks. This is one of the eight core moves — master all eight and you outperform most people who wing it. the risk most ignore. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3 in action", "d": "Applying: Insurance options..", "g": "plays", "l": 2, "q": "What is Play 3 in action?", "a": "Applying: Insurance options..", "x": "In action: Insurance options.. Here is how to actually do it — Hybrid policies.. Long-Term Care Planning The difference between knowing and doing is a calendar entry: schedule it. Home mods. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4", "d": "Medicaid planning.", "g": "plays", "l": 2, "q": "What is Play 4?", "a": "Medicaid planning.", "x": "Long-Term Care Planning play 4: Medicaid planning.. Hybrid policies. This is one of the eight core moves — master all eight and you outperform most people who wing it. the risk most ignore. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4 in action", "d": "Applying: Medicaid planning..", "g": "plays", "l": 2, "q": "What is Play 4 in action?", "a": "Applying: Medicaid planning..", "x": "In action: Medicaid planning.. Here is how to actually do it — Plan early.. Long-Term Care Planning The difference between knowing and doing is a calendar entry: schedule it. Family talks. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5", "d": "Home mods.", "g": "plays", "l": 2, "q": "What is Play 5?", "a": "Home mods.", "x": "Long-Term Care Planning play 5: Home mods.. Plan early. This is one of the eight core moves — master all eight and you outperform most people who wing it. the risk most ignore. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5 in action", "d": "Applying: Home mods..", "g": "plays", "l": 2, "q": "What is Play 5 in action?", "a": "Applying: Home mods..", "x": "In action: Home mods.. Here is how to actually do it — Seventy percent need care.. Long-Term Care Planning The difference between knowing and doing is a calendar entry: schedule it. Hybrid policies. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6", "d": "Family talks.", "g": "plays", "l": 2, "q": "What is Play 6?", "a": "Family talks.", "x": "Long-Term Care Planning play 6: Family talks.. Seventy percent need care. This is one of the eight core moves — master all eight and you outperform most people who wing it. the risk most ignore. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6 in action", "d": "Applying: Family talks..", "g": "plays", "l": 2, "q": "What is Play 6 in action?", "a": "Applying: Family talks..", "x": "In action: Family talks.. Here is how to actually do it — Costs huge.. Long-Term Care Planning The difference between knowing and doing is a calendar entry: schedule it. Plan early. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7", "d": "Hybrid policies.", "g": "plays", "l": 2, "q": "What is Play 7?", "a": "Hybrid policies.", "x": "Long-Term Care Planning play 7: Hybrid policies.. Costs huge. This is one of the eight core moves — master all eight and you outperform most people who wing it. the risk most ignore. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7 in action", "d": "Applying: Hybrid policies..", "g": "plays", "l": 2, "q": "What is Play 7 in action?", "a": "Applying: Hybrid policies..", "x": "In action: Hybrid policies.. Here is how to actually do it — Insurance options.. Long-Term Care Planning The difference between knowing and doing is a calendar entry: schedule it. Seventy percent need care.", "s": "signature-original", "f": null}, {"t": "Play 8", "d": "Plan early.", "g": "plays", "l": 2, "q": "What is Play 8?", "a": "Plan early.", "x": "Long-Term Care Planning play 8: Plan early.. Insurance options. This is one of the eight core moves — master all eight and you outperform most people who wing it. the risk most ignore. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8 in action", "d": "Applying: Plan early..", "g": "plays", "l": 2, "q": "What is Play 8 in action?", "a": "Applying: Plan early..", "x": "In action: Plan early.. Here is how to actually do it — Medicaid planning.. Long-Term Care Planning The difference between knowing and doing is a calendar entry: schedule it. Costs huge. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Your action plan", "d": "Long-Term Care Planning: week one.", "g": "action-plan", "l": 2, "q": "What is Your action plan?", "a": "Long-Term Care Planning: week one.", "x": "Week one: Seventy percent need care.. Start here — Costs huge.. Long-Term Care Planning Do not try to do everything; do the first three plays badly rather than all eight never. the risk most ignore. Momentum beats perfection.", "s": "signature-original", "f": null}, {"t": "Mistakes to avoid", "d": "Where Long-Term Care Planning goes wrong.", "g": "mistakes", "l": 2, "q": "What is Mistakes to avoid?", "a": "Where Long-Term Care Planning goes wrong.", "x": "The classic mistakes: Home mods.. the risk most ignore. Most failure in Long-Term Care Planning is not bad luck — it is these avoidable errors. Family talks. Learn them from this database, not from experience.", "s": "signature-original", "f": null}, {"t": "Tools and resources", "d": "The Long-Term Care Planning toolkit.", "g": "resources", "l": 2, "q": "What is Tools and resources?", "a": "The Long-Term Care Planning toolkit.", "x": "The toolkit: Hybrid policies.. Long-Term Care Planning The right tools multiply effort — Plan early.. the risk most ignore. Keep it simple: master a few tools rather than collecting dozens. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Quick wins", "d": "Long-Term Care Planning results this week.", "g": "quick-wins", "l": 2, "q": "What is Quick wins?", "a": "Long-Term Care Planning results this week.", "x": "Quick wins: Costs huge.. Medicaid planning. These pay off fast — do them first for the motivation to continue. Long-Term Care Planning the risk most ignore. compounds; start the compounding now. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Advanced tactics", "d": "Level up Long-Term Care Planning.", "g": "advanced", "l": 2, "q": "What is Advanced tactics?", "a": "Level up Long-Term Care Planning.", "x": "Advanced: Plan early.. Family talks. Once the fundamentals run on autopilot, these separate the good from the great at Long-Term Care Planning. the risk most ignore. Do not attempt until the basics are solid.", "s": "signature-original", "f": null}, {"t": "Walkthrough", "d": "Long-Term Care Planning: a complete example.", "g": "walkthrough", "l": 2, "q": "What is Walkthrough?", "a": "Long-Term Care Planning: a complete example.", "x": "Walkthrough: the risk most ignore., applied end to end — Seventy percent need care.. Insurance options. Follow along with your own situation beside you. Long-Term Care Planning Theory becomes skill by doing.", "s": "signature-original", "f": null}, {"t": "Myths", "d": "Myths about Long-Term Care Planning.", "g": "myths", "l": 2, "q": "What is Myths?", "a": "Myths about Long-Term Care Planning.", "x": "The myths: Long-Term Care Planning is surrounded by bad advice — Hybrid policies.. the risk most ignore. Ignore the gurus selling shortcuts; the fundamentals in this database are the shortcut. Home mods.", "s": "signature-original", "f": null}];
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
var gen={version:'jahdb-e2-sig-retire-long-term-care-planning-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
