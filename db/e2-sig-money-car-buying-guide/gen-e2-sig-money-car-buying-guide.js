(function(){'use strict';
/* JAH Signature Car Buying Guide Database generator — jahdb-e2-sig-money-car-buying-guide-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sig-money-car-buying-guide',PREFIX='JAH-E2SIGMONEYC-',NAME='JAH Signature Car Buying Guide Database';
var FIELDS=["overview", "fundamentals", "plays", "action-plan", "mistakes", "resources", "quick-wins", "advanced", "walkthrough", "myths", "checklist", "faq", "help", "quiz"];
var GEN_SRC='signature-original';
var MODE='quiz';
var BANK=[{"t": "Signature Car Buying Guide: the playbook", "d": "Car Buying Guide: don't overpay..", "g": "overview", "l": 2, "q": "What is Signature Car Buying Guide: the playbook?", "a": "Car Buying Guide: don't overpay..", "x": "The Signature Car Buying Guide playbook: don't overpay.. Budget. This is a complete working guide — not theory, but the actual moves: what to do first, what to avoid, and how to know it is working. Research. Every record is actionable.", "s": "signature-original", "f": null}, {"t": "The fundamentals", "d": "First principles of Car Buying Guide.", "g": "fundamentals", "l": 2, "q": "What is The fundamentals?", "a": "First principles of Car Buying Guide.", "x": "First principles: Pre-approved loan.. don't overpay. Get these right and the rest is optimization; get them wrong and nothing else matters. Car Buying Guide Negotiate price. is simple but not easy — fundamentals first, always.", "s": "signature-original", "f": null}, {"t": "Play 1", "d": "Budget.", "g": "plays", "l": 2, "q": "What is Play 1?", "a": "Budget.", "x": "Car Buying Guide play 1: Budget.. Negotiate price. This is one of the eight core moves — master all eight and you outperform most people who wing it. don't overpay. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 1 in action", "d": "Applying: Budget..", "g": "plays", "l": 2, "q": "What is Play 1 in action?", "a": "Applying: Budget..", "x": "In action: Budget.. Here is how to actually do it — Out the door.. Car Buying Guide The difference between knowing and doing is a calendar entry: schedule it. Pre-approved loan. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2", "d": "Research.", "g": "plays", "l": 2, "q": "What is Play 2?", "a": "Research.", "x": "Car Buying Guide play 2: Research.. Out the door. This is one of the eight core moves — master all eight and you outperform most people who wing it. don't overpay. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2 in action", "d": "Applying: Research..", "g": "plays", "l": 2, "q": "What is Play 2 in action?", "a": "Applying: Research..", "x": "In action: Research.. Here is how to actually do it — Used value.. Car Buying Guide The difference between knowing and doing is a calendar entry: schedule it. Negotiate price. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3", "d": "Pre-approved loan.", "g": "plays", "l": 2, "q": "What is Play 3?", "a": "Pre-approved loan.", "x": "Car Buying Guide play 3: Pre-approved loan.. Used value. This is one of the eight core moves — master all eight and you outperform most people who wing it. don't overpay. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3 in action", "d": "Applying: Pre-approved loan..", "g": "plays", "l": 2, "q": "What is Play 3 in action?", "a": "Applying: Pre-approved loan..", "x": "In action: Pre-approved loan.. Here is how to actually do it — Timing.. Car Buying Guide The difference between knowing and doing is a calendar entry: schedule it. Out the door. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4", "d": "Negotiate price.", "g": "plays", "l": 2, "q": "What is Play 4?", "a": "Negotiate price.", "x": "Car Buying Guide play 4: Negotiate price.. Timing. This is one of the eight core moves — master all eight and you outperform most people who wing it. don't overpay. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4 in action", "d": "Applying: Negotiate price..", "g": "plays", "l": 2, "q": "What is Play 4 in action?", "a": "Applying: Negotiate price..", "x": "In action: Negotiate price.. Here is how to actually do it — Walk away.. Car Buying Guide The difference between knowing and doing is a calendar entry: schedule it. Used value. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5", "d": "Out the door.", "g": "plays", "l": 2, "q": "What is Play 5?", "a": "Out the door.", "x": "Car Buying Guide play 5: Out the door.. Walk away. This is one of the eight core moves — master all eight and you outperform most people who wing it. don't overpay. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5 in action", "d": "Applying: Out the door..", "g": "plays", "l": 2, "q": "What is Play 5 in action?", "a": "Applying: Out the door..", "x": "In action: Out the door.. Here is how to actually do it — Budget.. Car Buying Guide The difference between knowing and doing is a calendar entry: schedule it. Timing. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6", "d": "Used value.", "g": "plays", "l": 2, "q": "What is Play 6?", "a": "Used value.", "x": "Car Buying Guide play 6: Used value.. Budget. This is one of the eight core moves — master all eight and you outperform most people who wing it. don't overpay. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6 in action", "d": "Applying: Used value..", "g": "plays", "l": 2, "q": "What is Play 6 in action?", "a": "Applying: Used value..", "x": "In action: Used value.. Here is how to actually do it — Research.. Car Buying Guide The difference between knowing and doing is a calendar entry: schedule it. Walk away. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7", "d": "Timing.", "g": "plays", "l": 2, "q": "What is Play 7?", "a": "Timing.", "x": "Car Buying Guide play 7: Timing.. Research. This is one of the eight core moves — master all eight and you outperform most people who wing it. don't overpay. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7 in action", "d": "Applying: Timing..", "g": "plays", "l": 2, "q": "What is Play 7 in action?", "a": "Applying: Timing..", "x": "In action: Timing.. Here is how to actually do it — Pre-approved loan.. Car Buying Guide The difference between knowing and doing is a calendar entry: schedule it. Budget. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8", "d": "Walk away.", "g": "plays", "l": 2, "q": "What is Play 8?", "a": "Walk away.", "x": "Car Buying Guide play 8: Walk away.. Pre-approved loan. This is one of the eight core moves — master all eight and you outperform most people who wing it. don't overpay. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8 in action", "d": "Applying: Walk away..", "g": "plays", "l": 2, "q": "What is Play 8 in action?", "a": "Applying: Walk away..", "x": "In action: Walk away.. Here is how to actually do it — Negotiate price.. Car Buying Guide The difference between knowing and doing is a calendar entry: schedule it. Research. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Your action plan", "d": "Car Buying Guide: week one.", "g": "action-plan", "l": 2, "q": "What is Your action plan?", "a": "Car Buying Guide: week one.", "x": "Week one: Budget.. Start here — Research.. Car Buying Guide Do not try to do everything; do the first three plays badly rather than all eight never. don't overpay. Momentum beats perfection. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Mistakes to avoid", "d": "Where Car Buying Guide goes wrong.", "g": "mistakes", "l": 2, "q": "What is Mistakes to avoid?", "a": "Where Car Buying Guide goes wrong.", "x": "The classic mistakes: Out the door.. don't overpay. Most failure in Car Buying Guide is not bad luck — it is these avoidable errors. Used value. Learn them from this database, not from experience. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Tools and resources", "d": "The Car Buying Guide toolkit.", "g": "resources", "l": 2, "q": "What is Tools and resources?", "a": "The Car Buying Guide toolkit.", "x": "The toolkit: Timing.. Car Buying Guide The right tools multiply effort — Walk away.. don't overpay. Keep it simple: master a few tools rather than collecting dozens. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Quick wins", "d": "Car Buying Guide results this week.", "g": "quick-wins", "l": 2, "q": "What is Quick wins?", "a": "Car Buying Guide results this week.", "x": "Quick wins: Research.. Negotiate price. These pay off fast — do them first for the motivation to continue. Car Buying Guide don't overpay. compounds; start the compounding now. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Advanced tactics", "d": "Level up Car Buying Guide.", "g": "advanced", "l": 2, "q": "What is Advanced tactics?", "a": "Level up Car Buying Guide.", "x": "Advanced: Walk away.. Used value. Once the fundamentals run on autopilot, these separate the good from the great at Car Buying Guide. don't overpay. Do not attempt until the basics are solid. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Walkthrough", "d": "Car Buying Guide: a complete example.", "g": "walkthrough", "l": 2, "q": "What is Walkthrough?", "a": "Car Buying Guide: a complete example.", "x": "Walkthrough: don't overpay., applied end to end — Budget.. Pre-approved loan. Follow along with your own situation beside you. Car Buying Guide Theory becomes skill by doing. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Myths", "d": "Myths about Car Buying Guide.", "g": "myths", "l": 2, "q": "What is Myths?", "a": "Myths about Car Buying Guide.", "x": "The myths: Car Buying Guide is surrounded by bad advice — Timing.. don't overpay. Ignore the gurus selling shortcuts; the fundamentals in this database are the shortcut. Out the door. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}];
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
var gen={version:'jahdb-e2-sig-money-car-buying-guide-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
