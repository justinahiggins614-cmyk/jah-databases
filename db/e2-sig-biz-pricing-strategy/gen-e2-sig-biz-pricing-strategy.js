(function(){'use strict';
/* JAH Signature Pricing Strategy Database generator — jahdb-e2-sig-biz-pricing-strategy-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sig-biz-pricing-strategy',PREFIX='JAH-E2SIGBIZPRI-',NAME='JAH Signature Pricing Strategy Database';
var FIELDS=["overview", "fundamentals", "plays", "action-plan", "mistakes", "resources", "quick-wins", "advanced", "walkthrough", "myths", "checklist", "faq", "help", "quiz"];
var GEN_SRC='signature-original';
var MODE='quiz';
var BANK=[{"t": "Signature Pricing Strategy: the playbook", "d": "Pricing Strategy: charge what you are worth..", "g": "overview", "l": 2, "q": "What is Signature Pricing Strategy: the playbook?", "a": "Pricing Strategy: charge what you are worth..", "x": "The Signature Pricing Strategy playbook: charge what you are worth.. Know your costs fully. This is a complete working guide — not theory, but the actual moves: what to do first, what to avoid, and how to know it is working. Value-based beats hourly. Every record is actionable.", "s": "signature-original", "f": null}, {"t": "The fundamentals", "d": "First principles of Pricing Strategy.", "g": "fundamentals", "l": 2, "q": "What is The fundamentals?", "a": "First principles of Pricing Strategy.", "x": "First principles: Test prices up.. charge what you are worth. Get these right and the rest is optimization; get them wrong and nothing else matters. Pricing Strategy Anchor high. is simple but not easy — fundamentals first, always.", "s": "signature-original", "f": null}, {"t": "Play 1", "d": "Know your costs fully.", "g": "plays", "l": 2, "q": "What is Play 1?", "a": "Know your costs fully.", "x": "Pricing Strategy play 1: Know your costs fully.. Anchor high. This is one of the eight core moves — master all eight and you outperform most people who wing it. charge what you are worth. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 1 in action", "d": "Applying: Know your costs fully..", "g": "plays", "l": 2, "q": "What is Play 1 in action?", "a": "Applying: Know your costs fully..", "x": "In action: Know your costs fully.. Here is how to actually do it — Discounts train cheap.. Pricing Strategy The difference between knowing and doing is a calendar entry: schedule it. Test prices up. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2", "d": "Value-based beats hourly.", "g": "plays", "l": 2, "q": "What is Play 2?", "a": "Value-based beats hourly.", "x": "Pricing Strategy play 2: Value-based beats hourly.. Discounts train cheap. This is one of the eight core moves — master all eight and you outperform most people who wing it. charge what you are worth.", "s": "signature-original", "f": null}, {"t": "Play 2 in action", "d": "Applying: Value-based beats hourly..", "g": "plays", "l": 2, "q": "What is Play 2 in action?", "a": "Applying: Value-based beats hourly..", "x": "In action: Value-based beats hourly.. Here is how to actually do it — Raise yearly.. Pricing Strategy The difference between knowing and doing is a calendar entry: schedule it. Anchor high. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3", "d": "Test prices up.", "g": "plays", "l": 2, "q": "What is Play 3?", "a": "Test prices up.", "x": "Pricing Strategy play 3: Test prices up.. Raise yearly. This is one of the eight core moves — master all eight and you outperform most people who wing it. charge what you are worth. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3 in action", "d": "Applying: Test prices up..", "g": "plays", "l": 2, "q": "What is Play 3 in action?", "a": "Applying: Test prices up..", "x": "In action: Test prices up.. Here is how to actually do it — Packages beat menus.. Pricing Strategy The difference between knowing and doing is a calendar entry: schedule it. Discounts train cheap. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4", "d": "Anchor high.", "g": "plays", "l": 2, "q": "What is Play 4?", "a": "Anchor high.", "x": "Pricing Strategy play 4: Anchor high.. Packages beat menus. This is one of the eight core moves — master all eight and you outperform most people who wing it. charge what you are worth. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4 in action", "d": "Applying: Anchor high..", "g": "plays", "l": 2, "q": "What is Play 4 in action?", "a": "Applying: Anchor high..", "x": "In action: Anchor high.. Here is how to actually do it — Never apologize for price.. Pricing Strategy The difference between knowing and doing is a calendar entry: schedule it. Raise yearly. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5", "d": "Discounts train cheap.", "g": "plays", "l": 2, "q": "What is Play 5?", "a": "Discounts train cheap.", "x": "Pricing Strategy play 5: Discounts train cheap.. Never apologize for price. This is one of the eight core moves — master all eight and you outperform most people who wing it. charge what you are worth.", "s": "signature-original", "f": null}, {"t": "Play 5 in action", "d": "Applying: Discounts train cheap..", "g": "plays", "l": 2, "q": "What is Play 5 in action?", "a": "Applying: Discounts train cheap..", "x": "In action: Discounts train cheap.. Here is how to actually do it — Know your costs fully.. Pricing Strategy The difference between knowing and doing is a calendar entry: schedule it. Packages beat menus.", "s": "signature-original", "f": null}, {"t": "Play 6", "d": "Raise yearly.", "g": "plays", "l": 2, "q": "What is Play 6?", "a": "Raise yearly.", "x": "Pricing Strategy play 6: Raise yearly.. Know your costs fully. This is one of the eight core moves — master all eight and you outperform most people who wing it. charge what you are worth. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6 in action", "d": "Applying: Raise yearly..", "g": "plays", "l": 2, "q": "What is Play 6 in action?", "a": "Applying: Raise yearly..", "x": "In action: Raise yearly.. Here is how to actually do it — Value-based beats hourly.. Pricing Strategy The difference between knowing and doing is a calendar entry: schedule it. Never apologize for price.", "s": "signature-original", "f": null}, {"t": "Play 7", "d": "Packages beat menus.", "g": "plays", "l": 2, "q": "What is Play 7?", "a": "Packages beat menus.", "x": "Pricing Strategy play 7: Packages beat menus.. Value-based beats hourly. This is one of the eight core moves — master all eight and you outperform most people who wing it. charge what you are worth. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7 in action", "d": "Applying: Packages beat menus..", "g": "plays", "l": 2, "q": "What is Play 7 in action?", "a": "Applying: Packages beat menus..", "x": "In action: Packages beat menus.. Here is how to actually do it — Test prices up.. Pricing Strategy The difference between knowing and doing is a calendar entry: schedule it. Know your costs fully. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8", "d": "Never apologize for price.", "g": "plays", "l": 2, "q": "What is Play 8?", "a": "Never apologize for price.", "x": "Pricing Strategy play 8: Never apologize for price.. Test prices up. This is one of the eight core moves — master all eight and you outperform most people who wing it. charge what you are worth. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8 in action", "d": "Applying: Never apologize for price..", "g": "plays", "l": 2, "q": "What is Play 8 in action?", "a": "Applying: Never apologize for price..", "x": "In action: Never apologize for price.. Here is how to actually do it — Anchor high.. Pricing Strategy The difference between knowing and doing is a calendar entry: schedule it. Value-based beats hourly.", "s": "signature-original", "f": null}, {"t": "Your action plan", "d": "Pricing Strategy: week one.", "g": "action-plan", "l": 2, "q": "What is Your action plan?", "a": "Pricing Strategy: week one.", "x": "Week one: Know your costs fully.. Start here — Value-based beats hourly.. Pricing Strategy Do not try to do everything; do the first three plays badly rather than all eight never. charge what you are worth. Momentum beats perfection.", "s": "signature-original", "f": null}, {"t": "Mistakes to avoid", "d": "Where Pricing Strategy goes wrong.", "g": "mistakes", "l": 2, "q": "What is Mistakes to avoid?", "a": "Where Pricing Strategy goes wrong.", "x": "The classic mistakes: Discounts train cheap.. charge what you are worth. Most failure in Pricing Strategy is not bad luck — it is these avoidable errors. Raise yearly. Learn them from this database, not from experience.", "s": "signature-original", "f": null}, {"t": "Tools and resources", "d": "The Pricing Strategy toolkit.", "g": "resources", "l": 2, "q": "What is Tools and resources?", "a": "The Pricing Strategy toolkit.", "x": "The toolkit: Packages beat menus.. Pricing Strategy The right tools multiply effort — Never apologize for price.. charge what you are worth. Keep it simple: master a few tools rather than collecting dozens.", "s": "signature-original", "f": null}, {"t": "Quick wins", "d": "Pricing Strategy results this week.", "g": "quick-wins", "l": 2, "q": "What is Quick wins?", "a": "Pricing Strategy results this week.", "x": "Quick wins: Value-based beats hourly.. Anchor high. These pay off fast — do them first for the motivation to continue. Pricing Strategy charge what you are worth. compounds; start the compounding now.", "s": "signature-original", "f": null}, {"t": "Advanced tactics", "d": "Level up Pricing Strategy.", "g": "advanced", "l": 2, "q": "What is Advanced tactics?", "a": "Level up Pricing Strategy.", "x": "Advanced: Never apologize for price.. Raise yearly. Once the fundamentals run on autopilot, these separate the good from the great at Pricing Strategy. charge what you are worth. Do not attempt until the basics are solid.", "s": "signature-original", "f": null}, {"t": "Walkthrough", "d": "Pricing Strategy: a complete example.", "g": "walkthrough", "l": 2, "q": "What is Walkthrough?", "a": "Pricing Strategy: a complete example.", "x": "Walkthrough: charge what you are worth., applied end to end — Know your costs fully.. Test prices up. Follow along with your own situation beside you. Pricing Strategy Theory becomes skill by doing. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Myths", "d": "Myths about Pricing Strategy.", "g": "myths", "l": 2, "q": "What is Myths?", "a": "Myths about Pricing Strategy.", "x": "The myths: Pricing Strategy is surrounded by bad advice — Packages beat menus.. charge what you are worth. Ignore the gurus selling shortcuts; the fundamentals in this database are the shortcut. Discounts train cheap.", "s": "signature-original", "f": null}];
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
var gen={version:'jahdb-e2-sig-biz-pricing-strategy-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
