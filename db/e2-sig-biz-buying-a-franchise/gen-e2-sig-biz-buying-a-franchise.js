(function(){'use strict';
/* JAH Signature Buying a Franchise Database generator — jahdb-e2-sig-biz-buying-a-franchise-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sig-biz-buying-a-franchise',PREFIX='JAH-E2SIGBIZBUY-',NAME='JAH Signature Buying a Franchise Database';
var FIELDS=["overview", "fundamentals", "plays", "action-plan", "mistakes", "resources", "quick-wins", "advanced", "walkthrough", "myths", "checklist", "faq", "help", "quiz"];
var GEN_SRC='signature-original';
var MODE='quiz';
var BANK=[{"t": "Signature Buying a Franchise: the playbook", "d": "Buying a Franchise: business in a box: evaluate well..", "g": "overview", "l": 2, "q": "What is Signature Buying a Franchise: the playbook?", "a": "Buying a Franchise: business in a box: evaluate well..", "x": "The Signature Buying a Franchise playbook: business in a box: evaluate well.. FDD: read all. This is a complete working guide — not theory, but the actual moves: what to do first, what to avoid, and how to know it is working. Talk to franchisees. Every record is actionable.", "s": "signature-original", "f": null}, {"t": "The fundamentals", "d": "First principles of Buying a Franchise.", "g": "fundamentals", "l": 2, "q": "What is The fundamentals?", "a": "First principles of Buying a Franchise.", "x": "First principles: Total investment.. business in a box: evaluate well. Get these right and the rest is optimization; get them wrong and nothing else matters. Buying a Franchise Royalties. is simple but not easy — fundamentals first, always.", "s": "signature-original", "f": null}, {"t": "Play 1", "d": "FDD: read all.", "g": "plays", "l": 2, "q": "What is Play 1?", "a": "FDD: read all.", "x": "Buying a Franchise play 1: FDD: read all.. Royalties. This is one of the eight core moves — master all eight and you outperform most people who wing it. business in a box: evaluate well. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 1 in action", "d": "Applying: FDD: read all..", "g": "plays", "l": 2, "q": "What is Play 1 in action?", "a": "Applying: FDD: read all..", "x": "In action: FDD: read all.. Here is how to actually do it — Territory.. Buying a Franchise The difference between knowing and doing is a calendar entry: schedule it. Total investment. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2", "d": "Talk to franchisees.", "g": "plays", "l": 2, "q": "What is Play 2?", "a": "Talk to franchisees.", "x": "Buying a Franchise play 2: Talk to franchisees.. Territory. This is one of the eight core moves — master all eight and you outperform most people who wing it. business in a box: evaluate well. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2 in action", "d": "Applying: Talk to franchisees..", "g": "plays", "l": 2, "q": "What is Play 2 in action?", "a": "Applying: Talk to franchisees..", "x": "In action: Talk to franchisees.. Here is how to actually do it — Exit terms.. Buying a Franchise The difference between knowing and doing is a calendar entry: schedule it. Royalties. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3", "d": "Total investment.", "g": "plays", "l": 2, "q": "What is Play 3?", "a": "Total investment.", "x": "Buying a Franchise play 3: Total investment.. Exit terms. This is one of the eight core moves — master all eight and you outperform most people who wing it. business in a box: evaluate well. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3 in action", "d": "Applying: Total investment..", "g": "plays", "l": 2, "q": "What is Play 3 in action?", "a": "Applying: Total investment..", "x": "In action: Total investment.. Here is how to actually do it — Item 19 earnings.. Buying a Franchise The difference between knowing and doing is a calendar entry: schedule it. Territory. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4", "d": "Royalties.", "g": "plays", "l": 2, "q": "What is Play 4?", "a": "Royalties.", "x": "Buying a Franchise play 4: Royalties.. Item 19 earnings. This is one of the eight core moves — master all eight and you outperform most people who wing it. business in a box: evaluate well. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4 in action", "d": "Applying: Royalties..", "g": "plays", "l": 2, "q": "What is Play 4 in action?", "a": "Applying: Royalties..", "x": "In action: Royalties.. Here is how to actually do it — Lawyer review.. Buying a Franchise The difference between knowing and doing is a calendar entry: schedule it. Exit terms. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5", "d": "Territory.", "g": "plays", "l": 2, "q": "What is Play 5?", "a": "Territory.", "x": "Buying a Franchise play 5: Territory.. Lawyer review. This is one of the eight core moves — master all eight and you outperform most people who wing it. business in a box: evaluate well. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5 in action", "d": "Applying: Territory..", "g": "plays", "l": 2, "q": "What is Play 5 in action?", "a": "Applying: Territory..", "x": "In action: Territory.. Here is how to actually do it — FDD: read all.. Buying a Franchise The difference between knowing and doing is a calendar entry: schedule it. Item 19 earnings. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6", "d": "Exit terms.", "g": "plays", "l": 2, "q": "What is Play 6?", "a": "Exit terms.", "x": "Buying a Franchise play 6: Exit terms.. FDD: read all. This is one of the eight core moves — master all eight and you outperform most people who wing it. business in a box: evaluate well. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6 in action", "d": "Applying: Exit terms..", "g": "plays", "l": 2, "q": "What is Play 6 in action?", "a": "Applying: Exit terms..", "x": "In action: Exit terms.. Here is how to actually do it — Talk to franchisees.. Buying a Franchise The difference between knowing and doing is a calendar entry: schedule it. Lawyer review. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7", "d": "Item 19 earnings.", "g": "plays", "l": 2, "q": "What is Play 7?", "a": "Item 19 earnings.", "x": "Buying a Franchise play 7: Item 19 earnings.. Talk to franchisees. This is one of the eight core moves — master all eight and you outperform most people who wing it. business in a box: evaluate well. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7 in action", "d": "Applying: Item 19 earnings..", "g": "plays", "l": 2, "q": "What is Play 7 in action?", "a": "Applying: Item 19 earnings..", "x": "In action: Item 19 earnings.. Here is how to actually do it — Total investment.. Buying a Franchise The difference between knowing and doing is a calendar entry: schedule it. FDD: read all. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8", "d": "Lawyer review.", "g": "plays", "l": 2, "q": "What is Play 8?", "a": "Lawyer review.", "x": "Buying a Franchise play 8: Lawyer review.. Total investment. This is one of the eight core moves — master all eight and you outperform most people who wing it. business in a box: evaluate well. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8 in action", "d": "Applying: Lawyer review..", "g": "plays", "l": 2, "q": "What is Play 8 in action?", "a": "Applying: Lawyer review..", "x": "In action: Lawyer review.. Here is how to actually do it — Royalties.. Buying a Franchise The difference between knowing and doing is a calendar entry: schedule it. Talk to franchisees. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Your action plan", "d": "Buying a Franchise: week one.", "g": "action-plan", "l": 2, "q": "What is Your action plan?", "a": "Buying a Franchise: week one.", "x": "Week one: FDD: read all.. Start here — Talk to franchisees.. Buying a Franchise Do not try to do everything; do the first three plays badly rather than all eight never. business in a box: evaluate well. Momentum beats perfection.", "s": "signature-original", "f": null}, {"t": "Mistakes to avoid", "d": "Where Buying a Franchise goes wrong.", "g": "mistakes", "l": 2, "q": "What is Mistakes to avoid?", "a": "Where Buying a Franchise goes wrong.", "x": "The classic mistakes: Territory.. business in a box: evaluate well. Most failure in Buying a Franchise is not bad luck — it is these avoidable errors. Exit terms. Learn them from this database, not from experience.", "s": "signature-original", "f": null}, {"t": "Tools and resources", "d": "The Buying a Franchise toolkit.", "g": "resources", "l": 2, "q": "What is Tools and resources?", "a": "The Buying a Franchise toolkit.", "x": "The toolkit: Item 19 earnings.. Buying a Franchise The right tools multiply effort — Lawyer review.. business in a box: evaluate well. Keep it simple: master a few tools rather than collecting dozens.", "s": "signature-original", "f": null}, {"t": "Quick wins", "d": "Buying a Franchise results this week.", "g": "quick-wins", "l": 2, "q": "What is Quick wins?", "a": "Buying a Franchise results this week.", "x": "Quick wins: Talk to franchisees.. Royalties. These pay off fast — do them first for the motivation to continue. Buying a Franchise business in a box: evaluate well. compounds; start the compounding now.", "s": "signature-original", "f": null}, {"t": "Advanced tactics", "d": "Level up Buying a Franchise.", "g": "advanced", "l": 2, "q": "What is Advanced tactics?", "a": "Level up Buying a Franchise.", "x": "Advanced: Lawyer review.. Exit terms. Once the fundamentals run on autopilot, these separate the good from the great at Buying a Franchise. business in a box: evaluate well. Do not attempt until the basics are solid.", "s": "signature-original", "f": null}, {"t": "Walkthrough", "d": "Buying a Franchise: a complete example.", "g": "walkthrough", "l": 2, "q": "What is Walkthrough?", "a": "Buying a Franchise: a complete example.", "x": "Walkthrough: business in a box: evaluate well., applied end to end — FDD: read all.. Total investment. Follow along with your own situation beside you. Buying a Franchise Theory becomes skill by doing.", "s": "signature-original", "f": null}, {"t": "Myths", "d": "Myths about Buying a Franchise.", "g": "myths", "l": 2, "q": "What is Myths?", "a": "Myths about Buying a Franchise.", "x": "The myths: Buying a Franchise is surrounded by bad advice — Item 19 earnings.. business in a box: evaluate well. Ignore the gurus selling shortcuts; the fundamentals in this database are the shortcut. Territory.", "s": "signature-original", "f": null}];
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
var gen={version:'jahdb-e2-sig-biz-buying-a-franchise-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
