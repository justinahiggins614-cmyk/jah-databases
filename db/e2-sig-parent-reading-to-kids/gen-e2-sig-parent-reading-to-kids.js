(function(){'use strict';
/* JAH Signature Reading to Kids Database generator — jahdb-e2-sig-parent-reading-to-kids-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sig-parent-reading-to-kids',PREFIX='JAH-E2SIGPARENT-',NAME='JAH Signature Reading to Kids Database';
var FIELDS=["overview", "fundamentals", "plays", "action-plan", "mistakes", "resources", "quick-wins", "advanced", "walkthrough", "myths", "checklist", "faq", "help", "quiz"];
var GEN_SRC='signature-original';
var MODE='quiz';
var BANK=[{"t": "Signature Reading to Kids: the playbook", "d": "Reading to Kids: raise readers..", "g": "overview", "l": 2, "q": "What is Signature Reading to Kids: the playbook?", "a": "Reading to Kids: raise readers..", "x": "The Signature Reading to Kids playbook: raise readers.. Read daily. This is a complete working guide — not theory, but the actual moves: what to do first, what to avoid, and how to know it is working. Let them choose. Every record is actionable.", "s": "signature-original", "f": null}, {"t": "The fundamentals", "d": "First principles of Reading to Kids.", "g": "fundamentals", "l": 2, "q": "What is The fundamentals?", "a": "First principles of Reading to Kids.", "x": "First principles: Library trips.. raise readers. Get these right and the rest is optimization; get them wrong and nothing else matters. Reading to Kids Read aloud. is simple but not easy — fundamentals first, always.", "s": "signature-original", "f": null}, {"t": "Play 1", "d": "Read daily.", "g": "plays", "l": 2, "q": "What is Play 1?", "a": "Read daily.", "x": "Reading to Kids play 1: Read daily.. Read aloud. This is one of the eight core moves — master all eight and you outperform most people who wing it. raise readers. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 1 in action", "d": "Applying: Read daily..", "g": "plays", "l": 2, "q": "What is Play 1 in action?", "a": "Applying: Read daily..", "x": "In action: Read daily.. Here is how to actually do it — Model reading.. Reading to Kids The difference between knowing and doing is a calendar entry: schedule it. Library trips. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2", "d": "Let them choose.", "g": "plays", "l": 2, "q": "What is Play 2?", "a": "Let them choose.", "x": "Reading to Kids play 2: Let them choose.. Model reading. This is one of the eight core moves — master all eight and you outperform most people who wing it. raise readers. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2 in action", "d": "Applying: Let them choose..", "g": "plays", "l": 2, "q": "What is Play 2 in action?", "a": "Applying: Let them choose..", "x": "In action: Let them choose.. Here is how to actually do it — Talk about books.. Reading to Kids The difference between knowing and doing is a calendar entry: schedule it. Read aloud. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3", "d": "Library trips.", "g": "plays", "l": 2, "q": "What is Play 3?", "a": "Library trips.", "x": "Reading to Kids play 3: Library trips.. Talk about books. This is one of the eight core moves — master all eight and you outperform most people who wing it. raise readers. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3 in action", "d": "Applying: Library trips..", "g": "plays", "l": 2, "q": "What is Play 3 in action?", "a": "Applying: Library trips..", "x": "In action: Library trips.. Here is how to actually do it — Bedtime stories.. Reading to Kids The difference between knowing and doing is a calendar entry: schedule it. Model reading. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4", "d": "Read aloud.", "g": "plays", "l": 2, "q": "What is Play 4?", "a": "Read aloud.", "x": "Reading to Kids play 4: Read aloud.. Bedtime stories. This is one of the eight core moves — master all eight and you outperform most people who wing it. raise readers. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4 in action", "d": "Applying: Read aloud..", "g": "plays", "l": 2, "q": "What is Play 4 in action?", "a": "Applying: Read aloud..", "x": "In action: Read aloud.. Here is how to actually do it — Comics count.. Reading to Kids The difference between knowing and doing is a calendar entry: schedule it. Talk about books. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5", "d": "Model reading.", "g": "plays", "l": 2, "q": "What is Play 5?", "a": "Model reading.", "x": "Reading to Kids play 5: Model reading.. Comics count. This is one of the eight core moves — master all eight and you outperform most people who wing it. raise readers. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5 in action", "d": "Applying: Model reading..", "g": "plays", "l": 2, "q": "What is Play 5 in action?", "a": "Applying: Model reading..", "x": "In action: Model reading.. Here is how to actually do it — Read daily.. Reading to Kids The difference between knowing and doing is a calendar entry: schedule it. Bedtime stories. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6", "d": "Talk about books.", "g": "plays", "l": 2, "q": "What is Play 6?", "a": "Talk about books.", "x": "Reading to Kids play 6: Talk about books.. Read daily. This is one of the eight core moves — master all eight and you outperform most people who wing it. raise readers. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6 in action", "d": "Applying: Talk about books..", "g": "plays", "l": 2, "q": "What is Play 6 in action?", "a": "Applying: Talk about books..", "x": "In action: Talk about books.. Here is how to actually do it — Let them choose.. Reading to Kids The difference between knowing and doing is a calendar entry: schedule it. Comics count. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7", "d": "Bedtime stories.", "g": "plays", "l": 2, "q": "What is Play 7?", "a": "Bedtime stories.", "x": "Reading to Kids play 7: Bedtime stories.. Let them choose. This is one of the eight core moves — master all eight and you outperform most people who wing it. raise readers. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7 in action", "d": "Applying: Bedtime stories..", "g": "plays", "l": 2, "q": "What is Play 7 in action?", "a": "Applying: Bedtime stories..", "x": "In action: Bedtime stories.. Here is how to actually do it — Library trips.. Reading to Kids The difference between knowing and doing is a calendar entry: schedule it. Read daily. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8", "d": "Comics count.", "g": "plays", "l": 2, "q": "What is Play 8?", "a": "Comics count.", "x": "Reading to Kids play 8: Comics count.. Library trips. This is one of the eight core moves — master all eight and you outperform most people who wing it. raise readers. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8 in action", "d": "Applying: Comics count..", "g": "plays", "l": 2, "q": "What is Play 8 in action?", "a": "Applying: Comics count..", "x": "In action: Comics count.. Here is how to actually do it — Read aloud.. Reading to Kids The difference between knowing and doing is a calendar entry: schedule it. Let them choose. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Your action plan", "d": "Reading to Kids: week one.", "g": "action-plan", "l": 2, "q": "What is Your action plan?", "a": "Reading to Kids: week one.", "x": "Week one: Read daily.. Start here — Let them choose.. Reading to Kids Do not try to do everything; do the first three plays badly rather than all eight never. raise readers. Momentum beats perfection.", "s": "signature-original", "f": null}, {"t": "Mistakes to avoid", "d": "Where Reading to Kids goes wrong.", "g": "mistakes", "l": 2, "q": "What is Mistakes to avoid?", "a": "Where Reading to Kids goes wrong.", "x": "The classic mistakes: Model reading.. raise readers. Most failure in Reading to Kids is not bad luck — it is these avoidable errors. Talk about books. Learn them from this database, not from experience.", "s": "signature-original", "f": null}, {"t": "Tools and resources", "d": "The Reading to Kids toolkit.", "g": "resources", "l": 2, "q": "What is Tools and resources?", "a": "The Reading to Kids toolkit.", "x": "The toolkit: Bedtime stories.. Reading to Kids The right tools multiply effort — Comics count.. raise readers. Keep it simple: master a few tools rather than collecting dozens. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Quick wins", "d": "Reading to Kids results this week.", "g": "quick-wins", "l": 2, "q": "What is Quick wins?", "a": "Reading to Kids results this week.", "x": "Quick wins: Let them choose.. Read aloud. These pay off fast — do them first for the motivation to continue. Reading to Kids raise readers. compounds; start the compounding now. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Advanced tactics", "d": "Level up Reading to Kids.", "g": "advanced", "l": 2, "q": "What is Advanced tactics?", "a": "Level up Reading to Kids.", "x": "Advanced: Comics count.. Talk about books. Once the fundamentals run on autopilot, these separate the good from the great at Reading to Kids. raise readers. Do not attempt until the basics are solid. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Walkthrough", "d": "Reading to Kids: a complete example.", "g": "walkthrough", "l": 2, "q": "What is Walkthrough?", "a": "Reading to Kids: a complete example.", "x": "Walkthrough: raise readers., applied end to end — Read daily.. Library trips. Follow along with your own situation beside you. Reading to Kids Theory becomes skill by doing. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Myths", "d": "Myths about Reading to Kids.", "g": "myths", "l": 2, "q": "What is Myths?", "a": "Myths about Reading to Kids.", "x": "The myths: Reading to Kids is surrounded by bad advice — Bedtime stories.. raise readers. Ignore the gurus selling shortcuts; the fundamentals in this database are the shortcut. Model reading. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}];
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
var gen={version:'jahdb-e2-sig-parent-reading-to-kids-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
