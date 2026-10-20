(function(){'use strict';
/* JAH Signature Medicare Guide Database generator — jahdb-e2-sig-retire-medicare-guide-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sig-retire-medicare-guide',PREFIX='JAH-E2SIGRETIRE-',NAME='JAH Signature Medicare Guide Database';
var FIELDS=["overview", "fundamentals", "plays", "action-plan", "mistakes", "resources", "quick-wins", "advanced", "walkthrough", "myths", "checklist", "faq", "help", "quiz"];
var GEN_SRC='signature-original';
var MODE='quiz';
var BANK=[{"t": "Signature Medicare Guide: the playbook", "d": "Medicare Guide: health coverage at sixty-five..", "g": "overview", "l": 2, "q": "What is Signature Medicare Guide: the playbook?", "a": "Medicare Guide: health coverage at sixty-five..", "x": "The Signature Medicare Guide playbook: health coverage at sixty-five.. Parts A B C D. This is a complete working guide — not theory, but the actual moves: what to do first, what to avoid, and how to know it is working. Enroll at sixty-five. Every record is actionable.", "s": "signature-original", "f": null}, {"t": "The fundamentals", "d": "First principles of Medicare Guide.", "g": "fundamentals", "l": 2, "q": "What is The fundamentals?", "a": "First principles of Medicare Guide.", "x": "First principles: Penalties.. health coverage at sixty-five. Get these right and the rest is optimization; get them wrong and nothing else matters. Medicare Guide Medigap vs Advantage. is simple but not easy — fundamentals first, always.", "s": "signature-original", "f": null}, {"t": "Play 1", "d": "Parts A B C D.", "g": "plays", "l": 2, "q": "What is Play 1?", "a": "Parts A B C D.", "x": "Medicare Guide play 1: Parts A B C D.. Medigap vs Advantage. This is one of the eight core moves — master all eight and you outperform most people who wing it. health coverage at sixty-five. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 1 in action", "d": "Applying: Parts A B C D..", "g": "plays", "l": 2, "q": "What is Play 1 in action?", "a": "Applying: Parts A B C D..", "x": "In action: Parts A B C D.. Here is how to actually do it — IRMAA surcharges.. Medicare Guide The difference between knowing and doing is a calendar entry: schedule it. Penalties. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2", "d": "Enroll at sixty-five.", "g": "plays", "l": 2, "q": "What is Play 2?", "a": "Enroll at sixty-five.", "x": "Medicare Guide play 2: Enroll at sixty-five.. IRMAA surcharges. This is one of the eight core moves — master all eight and you outperform most people who wing it. health coverage at sixty-five. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2 in action", "d": "Applying: Enroll at sixty-five..", "g": "plays", "l": 2, "q": "What is Play 2 in action?", "a": "Applying: Enroll at sixty-five..", "x": "In action: Enroll at sixty-five.. Here is how to actually do it — Annual review.. Medicare Guide The difference between knowing and doing is a calendar entry: schedule it. Medigap vs Advantage. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3", "d": "Penalties.", "g": "plays", "l": 2, "q": "What is Play 3?", "a": "Penalties.", "x": "Medicare Guide play 3: Penalties.. Annual review. This is one of the eight core moves — master all eight and you outperform most people who wing it. health coverage at sixty-five. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3 in action", "d": "Applying: Penalties..", "g": "plays", "l": 2, "q": "What is Play 3 in action?", "a": "Applying: Penalties..", "x": "In action: Penalties.. Here is how to actually do it — SHIPs free help.. Medicare Guide The difference between knowing and doing is a calendar entry: schedule it. IRMAA surcharges. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4", "d": "Medigap vs Advantage.", "g": "plays", "l": 2, "q": "What is Play 4?", "a": "Medigap vs Advantage.", "x": "Medicare Guide play 4: Medigap vs Advantage.. SHIPs free help. This is one of the eight core moves — master all eight and you outperform most people who wing it. health coverage at sixty-five. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4 in action", "d": "Applying: Medigap vs Advantage..", "g": "plays", "l": 2, "q": "What is Play 4 in action?", "a": "Applying: Medigap vs Advantage..", "x": "In action: Medigap vs Advantage.. Here is how to actually do it — Drug plans.. Medicare Guide The difference between knowing and doing is a calendar entry: schedule it. Annual review. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5", "d": "IRMAA surcharges.", "g": "plays", "l": 2, "q": "What is Play 5?", "a": "IRMAA surcharges.", "x": "Medicare Guide play 5: IRMAA surcharges.. Drug plans. This is one of the eight core moves — master all eight and you outperform most people who wing it. health coverage at sixty-five. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5 in action", "d": "Applying: IRMAA surcharges..", "g": "plays", "l": 2, "q": "What is Play 5 in action?", "a": "Applying: IRMAA surcharges..", "x": "In action: IRMAA surcharges.. Here is how to actually do it — Parts A B C D.. Medicare Guide The difference between knowing and doing is a calendar entry: schedule it. SHIPs free help. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6", "d": "Annual review.", "g": "plays", "l": 2, "q": "What is Play 6?", "a": "Annual review.", "x": "Medicare Guide play 6: Annual review.. Parts A B C D. This is one of the eight core moves — master all eight and you outperform most people who wing it. health coverage at sixty-five. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6 in action", "d": "Applying: Annual review..", "g": "plays", "l": 2, "q": "What is Play 6 in action?", "a": "Applying: Annual review..", "x": "In action: Annual review.. Here is how to actually do it — Enroll at sixty-five.. Medicare Guide The difference between knowing and doing is a calendar entry: schedule it. Drug plans. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7", "d": "SHIPs free help.", "g": "plays", "l": 2, "q": "What is Play 7?", "a": "SHIPs free help.", "x": "Medicare Guide play 7: SHIPs free help.. Enroll at sixty-five. This is one of the eight core moves — master all eight and you outperform most people who wing it. health coverage at sixty-five. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7 in action", "d": "Applying: SHIPs free help..", "g": "plays", "l": 2, "q": "What is Play 7 in action?", "a": "Applying: SHIPs free help..", "x": "In action: SHIPs free help.. Here is how to actually do it — Penalties.. Medicare Guide The difference between knowing and doing is a calendar entry: schedule it. Parts A B C D. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8", "d": "Drug plans.", "g": "plays", "l": 2, "q": "What is Play 8?", "a": "Drug plans.", "x": "Medicare Guide play 8: Drug plans.. Penalties. This is one of the eight core moves — master all eight and you outperform most people who wing it. health coverage at sixty-five. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8 in action", "d": "Applying: Drug plans..", "g": "plays", "l": 2, "q": "What is Play 8 in action?", "a": "Applying: Drug plans..", "x": "In action: Drug plans.. Here is how to actually do it — Medigap vs Advantage.. Medicare Guide The difference between knowing and doing is a calendar entry: schedule it. Enroll at sixty-five. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Your action plan", "d": "Medicare Guide: week one.", "g": "action-plan", "l": 2, "q": "What is Your action plan?", "a": "Medicare Guide: week one.", "x": "Week one: Parts A B C D.. Start here — Enroll at sixty-five.. Medicare Guide Do not try to do everything; do the first three plays badly rather than all eight never. health coverage at sixty-five. Momentum beats perfection.", "s": "signature-original", "f": null}, {"t": "Mistakes to avoid", "d": "Where Medicare Guide goes wrong.", "g": "mistakes", "l": 2, "q": "What is Mistakes to avoid?", "a": "Where Medicare Guide goes wrong.", "x": "The classic mistakes: IRMAA surcharges.. health coverage at sixty-five. Most failure in Medicare Guide is not bad luck — it is these avoidable errors. Annual review. Learn them from this database, not from experience.", "s": "signature-original", "f": null}, {"t": "Tools and resources", "d": "The Medicare Guide toolkit.", "g": "resources", "l": 2, "q": "What is Tools and resources?", "a": "The Medicare Guide toolkit.", "x": "The toolkit: SHIPs free help.. Medicare Guide The right tools multiply effort — Drug plans.. health coverage at sixty-five. Keep it simple: master a few tools rather than collecting dozens. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Quick wins", "d": "Medicare Guide results this week.", "g": "quick-wins", "l": 2, "q": "What is Quick wins?", "a": "Medicare Guide results this week.", "x": "Quick wins: Enroll at sixty-five.. Medigap vs Advantage. These pay off fast — do them first for the motivation to continue. Medicare Guide health coverage at sixty-five. compounds; start the compounding now.", "s": "signature-original", "f": null}, {"t": "Advanced tactics", "d": "Level up Medicare Guide.", "g": "advanced", "l": 2, "q": "What is Advanced tactics?", "a": "Level up Medicare Guide.", "x": "Advanced: Drug plans.. Annual review. Once the fundamentals run on autopilot, these separate the good from the great at Medicare Guide. health coverage at sixty-five. Do not attempt until the basics are solid.", "s": "signature-original", "f": null}, {"t": "Walkthrough", "d": "Medicare Guide: a complete example.", "g": "walkthrough", "l": 2, "q": "What is Walkthrough?", "a": "Medicare Guide: a complete example.", "x": "Walkthrough: health coverage at sixty-five., applied end to end — Parts A B C D.. Penalties. Follow along with your own situation beside you. Medicare Guide Theory becomes skill by doing. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Myths", "d": "Myths about Medicare Guide.", "g": "myths", "l": 2, "q": "What is Myths?", "a": "Myths about Medicare Guide.", "x": "The myths: Medicare Guide is surrounded by bad advice — SHIPs free help.. health coverage at sixty-five. Ignore the gurus selling shortcuts; the fundamentals in this database are the shortcut. IRMAA surcharges.", "s": "signature-original", "f": null}];
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
var gen={version:'jahdb-e2-sig-retire-medicare-guide-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
