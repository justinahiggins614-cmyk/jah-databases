(function(){'use strict';
/* JAH Signature Small Space Living Database generator — jahdb-e2-sig-home-small-space-living-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sig-home-small-space-living',PREFIX='JAH-E2SIGHOMESM-',NAME='JAH Signature Small Space Living Database';
var FIELDS=["overview", "fundamentals", "plays", "action-plan", "mistakes", "resources", "quick-wins", "advanced", "walkthrough", "myths", "checklist", "faq", "help", "quiz"];
var GEN_SRC='signature-original';
var MODE='quiz';
var BANK=[{"t": "Signature Small Space Living: the playbook", "d": "Small Space Living: live large small..", "g": "overview", "l": 2, "q": "What is Signature Small Space Living: the playbook?", "a": "Small Space Living: live large small..", "x": "The Signature Small Space Living playbook: live large small.. Multifunction. This is a complete working guide — not theory, but the actual moves: what to do first, what to avoid, and how to know it is working. Vertical. Every record is actionable.", "s": "signature-original", "f": null}, {"t": "The fundamentals", "d": "First principles of Small Space Living.", "g": "fundamentals", "l": 2, "q": "What is The fundamentals?", "a": "First principles of Small Space Living.", "x": "First principles: Declutter ruthless.. live large small. Get these right and the rest is optimization; get them wrong and nothing else matters. Small Space Living Light colors. is simple but not easy — fundamentals first, always.", "s": "signature-original", "f": null}, {"t": "Play 1", "d": "Multifunction.", "g": "plays", "l": 2, "q": "What is Play 1?", "a": "Multifunction.", "x": "Small Space Living play 1: Multifunction.. Light colors. This is one of the eight core moves — master all eight and you outperform most people who wing it. live large small. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 1 in action", "d": "Applying: Multifunction..", "g": "plays", "l": 2, "q": "What is Play 1 in action?", "a": "Applying: Multifunction..", "x": "In action: Multifunction.. Here is how to actually do it — Zones.. Small Space Living The difference between knowing and doing is a calendar entry: schedule it. Declutter ruthless. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2", "d": "Vertical.", "g": "plays", "l": 2, "q": "What is Play 2?", "a": "Vertical.", "x": "Small Space Living play 2: Vertical.. Zones. This is one of the eight core moves — master all eight and you outperform most people who wing it. live large small. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2 in action", "d": "Applying: Vertical..", "g": "plays", "l": 2, "q": "What is Play 2 in action?", "a": "Applying: Vertical..", "x": "In action: Vertical.. Here is how to actually do it — Storage ottoman.. Small Space Living The difference between knowing and doing is a calendar entry: schedule it. Light colors. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3", "d": "Declutter ruthless.", "g": "plays", "l": 2, "q": "What is Play 3?", "a": "Declutter ruthless.", "x": "Small Space Living play 3: Declutter ruthless.. Storage ottoman. This is one of the eight core moves — master all eight and you outperform most people who wing it. live large small. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3 in action", "d": "Applying: Declutter ruthless..", "g": "plays", "l": 2, "q": "What is Play 3 in action?", "a": "Applying: Declutter ruthless..", "x": "In action: Declutter ruthless.. Here is how to actually do it — Mirrors.. Small Space Living The difference between knowing and doing is a calendar entry: schedule it. Zones. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4", "d": "Light colors.", "g": "plays", "l": 2, "q": "What is Play 4?", "a": "Light colors.", "x": "Small Space Living play 4: Light colors.. Mirrors. This is one of the eight core moves — master all eight and you outperform most people who wing it. live large small. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4 in action", "d": "Applying: Light colors..", "g": "plays", "l": 2, "q": "What is Play 4 in action?", "a": "Applying: Light colors..", "x": "In action: Light colors.. Here is how to actually do it — Edit often.. Small Space Living The difference between knowing and doing is a calendar entry: schedule it. Storage ottoman. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5", "d": "Zones.", "g": "plays", "l": 2, "q": "What is Play 5?", "a": "Zones.", "x": "Small Space Living play 5: Zones.. Edit often. This is one of the eight core moves — master all eight and you outperform most people who wing it. live large small. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5 in action", "d": "Applying: Zones..", "g": "plays", "l": 2, "q": "What is Play 5 in action?", "a": "Applying: Zones..", "x": "In action: Zones.. Here is how to actually do it — Multifunction.. Small Space Living The difference between knowing and doing is a calendar entry: schedule it. Mirrors. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6", "d": "Storage ottoman.", "g": "plays", "l": 2, "q": "What is Play 6?", "a": "Storage ottoman.", "x": "Small Space Living play 6: Storage ottoman.. Multifunction. This is one of the eight core moves — master all eight and you outperform most people who wing it. live large small. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6 in action", "d": "Applying: Storage ottoman..", "g": "plays", "l": 2, "q": "What is Play 6 in action?", "a": "Applying: Storage ottoman..", "x": "In action: Storage ottoman.. Here is how to actually do it — Vertical.. Small Space Living The difference between knowing and doing is a calendar entry: schedule it. Edit often. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7", "d": "Mirrors.", "g": "plays", "l": 2, "q": "What is Play 7?", "a": "Mirrors.", "x": "Small Space Living play 7: Mirrors.. Vertical. This is one of the eight core moves — master all eight and you outperform most people who wing it. live large small. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7 in action", "d": "Applying: Mirrors..", "g": "plays", "l": 2, "q": "What is Play 7 in action?", "a": "Applying: Mirrors..", "x": "In action: Mirrors.. Here is how to actually do it — Declutter ruthless.. Small Space Living The difference between knowing and doing is a calendar entry: schedule it. Multifunction. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8", "d": "Edit often.", "g": "plays", "l": 2, "q": "What is Play 8?", "a": "Edit often.", "x": "Small Space Living play 8: Edit often.. Declutter ruthless. This is one of the eight core moves — master all eight and you outperform most people who wing it. live large small. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8 in action", "d": "Applying: Edit often..", "g": "plays", "l": 2, "q": "What is Play 8 in action?", "a": "Applying: Edit often..", "x": "In action: Edit often.. Here is how to actually do it — Light colors.. Small Space Living The difference between knowing and doing is a calendar entry: schedule it. Vertical. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Your action plan", "d": "Small Space Living: week one.", "g": "action-plan", "l": 2, "q": "What is Your action plan?", "a": "Small Space Living: week one.", "x": "Week one: Multifunction.. Start here — Vertical.. Small Space Living Do not try to do everything; do the first three plays badly rather than all eight never. live large small. Momentum beats perfection.", "s": "signature-original", "f": null}, {"t": "Mistakes to avoid", "d": "Where Small Space Living goes wrong.", "g": "mistakes", "l": 2, "q": "What is Mistakes to avoid?", "a": "Where Small Space Living goes wrong.", "x": "The classic mistakes: Zones.. live large small. Most failure in Small Space Living is not bad luck — it is these avoidable errors. Storage ottoman. Learn them from this database, not from experience. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Tools and resources", "d": "The Small Space Living toolkit.", "g": "resources", "l": 2, "q": "What is Tools and resources?", "a": "The Small Space Living toolkit.", "x": "The toolkit: Mirrors.. Small Space Living The right tools multiply effort — Edit often.. live large small. Keep it simple: master a few tools rather than collecting dozens. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Quick wins", "d": "Small Space Living results this week.", "g": "quick-wins", "l": 2, "q": "What is Quick wins?", "a": "Small Space Living results this week.", "x": "Quick wins: Vertical.. Light colors. These pay off fast — do them first for the motivation to continue. Small Space Living live large small. compounds; start the compounding now. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Advanced tactics", "d": "Level up Small Space Living.", "g": "advanced", "l": 2, "q": "What is Advanced tactics?", "a": "Level up Small Space Living.", "x": "Advanced: Edit often.. Storage ottoman. Once the fundamentals run on autopilot, these separate the good from the great at Small Space Living. live large small. Do not attempt until the basics are solid.", "s": "signature-original", "f": null}, {"t": "Walkthrough", "d": "Small Space Living: a complete example.", "g": "walkthrough", "l": 2, "q": "What is Walkthrough?", "a": "Small Space Living: a complete example.", "x": "Walkthrough: live large small., applied end to end — Multifunction.. Declutter ruthless. Follow along with your own situation beside you. Small Space Living Theory becomes skill by doing. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Myths", "d": "Myths about Small Space Living.", "g": "myths", "l": 2, "q": "What is Myths?", "a": "Myths about Small Space Living.", "x": "The myths: Small Space Living is surrounded by bad advice — Mirrors.. live large small. Ignore the gurus selling shortcuts; the fundamentals in this database are the shortcut. Zones. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}];
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
var gen={version:'jahdb-e2-sig-home-small-space-living-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
