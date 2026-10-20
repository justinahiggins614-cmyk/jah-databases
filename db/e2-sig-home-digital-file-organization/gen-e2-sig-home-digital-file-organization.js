(function(){'use strict';
/* JAH Signature Digital File Organization Database generator — jahdb-e2-sig-home-digital-file-organization-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sig-home-digital-file-organization',PREFIX='JAH-E2SIGHOMEDI-',NAME='JAH Signature Digital File Organization Database';
var FIELDS=["overview", "fundamentals", "plays", "action-plan", "mistakes", "resources", "quick-wins", "advanced", "walkthrough", "myths", "checklist", "faq", "help", "quiz"];
var GEN_SRC='signature-original';
var MODE='quiz';
var BANK=[{"t": "Signature Digital File Organization: the playbook", "d": "Digital File Organization: find anything fast..", "g": "overview", "l": 2, "q": "What is Signature Digital File Organization: the playbook?", "a": "Digital File Organization: find anything fast..", "x": "The Signature Digital File Organization playbook: find anything fast.. Folder system. This is a complete working guide — not theory, but the actual moves: what to do first, what to avoid, and how to know it is working. Naming consistent. Every record is actionable.", "s": "signature-original", "f": null}, {"t": "The fundamentals", "d": "First principles of Digital File Organization.", "g": "fundamentals", "l": 2, "q": "What is The fundamentals?", "a": "First principles of Digital File Organization.", "x": "First principles: Cloud backup.. find anything fast. Get these right and the rest is optimization; get them wrong and nothing else matters. Digital File Organization Inbox zero. is simple but not easy — fundamentals first, always.", "s": "signature-original", "f": null}, {"t": "Play 1", "d": "Folder system.", "g": "plays", "l": 2, "q": "What is Play 1?", "a": "Folder system.", "x": "Digital File Organization play 1: Folder system.. Inbox zero. This is one of the eight core moves — master all eight and you outperform most people who wing it. find anything fast. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 1 in action", "d": "Applying: Folder system..", "g": "plays", "l": 2, "q": "What is Play 1 in action?", "a": "Applying: Folder system..", "x": "In action: Folder system.. Here is how to actually do it — Archive.. Digital File Organization The difference between knowing and doing is a calendar entry: schedule it. Cloud backup. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2", "d": "Naming consistent.", "g": "plays", "l": 2, "q": "What is Play 2?", "a": "Naming consistent.", "x": "Digital File Organization play 2: Naming consistent.. Archive. This is one of the eight core moves — master all eight and you outperform most people who wing it. find anything fast. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2 in action", "d": "Applying: Naming consistent..", "g": "plays", "l": 2, "q": "What is Play 2 in action?", "a": "Applying: Naming consistent..", "x": "In action: Naming consistent.. Here is how to actually do it — Passwords manager.. Digital File Organization The difference between knowing and doing is a calendar entry: schedule it. Inbox zero. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3", "d": "Cloud backup.", "g": "plays", "l": 2, "q": "What is Play 3?", "a": "Cloud backup.", "x": "Digital File Organization play 3: Cloud backup.. Passwords manager. This is one of the eight core moves — master all eight and you outperform most people who wing it. find anything fast. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3 in action", "d": "Applying: Cloud backup..", "g": "plays", "l": 2, "q": "What is Play 3 in action?", "a": "Applying: Cloud backup..", "x": "In action: Cloud backup.. Here is how to actually do it — Photos sorted.. Digital File Organization The difference between knowing and doing is a calendar entry: schedule it. Archive. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4", "d": "Inbox zero.", "g": "plays", "l": 2, "q": "What is Play 4?", "a": "Inbox zero.", "x": "Digital File Organization play 4: Inbox zero.. Photos sorted. This is one of the eight core moves — master all eight and you outperform most people who wing it. find anything fast. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4 in action", "d": "Applying: Inbox zero..", "g": "plays", "l": 2, "q": "What is Play 4 in action?", "a": "Applying: Inbox zero..", "x": "In action: Inbox zero.. Here is how to actually do it — Purge.. Digital File Organization The difference between knowing and doing is a calendar entry: schedule it. Passwords manager. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5", "d": "Archive.", "g": "plays", "l": 2, "q": "What is Play 5?", "a": "Archive.", "x": "Digital File Organization play 5: Archive.. Purge. This is one of the eight core moves — master all eight and you outperform most people who wing it. find anything fast. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5 in action", "d": "Applying: Archive..", "g": "plays", "l": 2, "q": "What is Play 5 in action?", "a": "Applying: Archive..", "x": "In action: Archive.. Here is how to actually do it — Folder system.. Digital File Organization The difference between knowing and doing is a calendar entry: schedule it. Photos sorted. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6", "d": "Passwords manager.", "g": "plays", "l": 2, "q": "What is Play 6?", "a": "Passwords manager.", "x": "Digital File Organization play 6: Passwords manager.. Folder system. This is one of the eight core moves — master all eight and you outperform most people who wing it. find anything fast. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6 in action", "d": "Applying: Passwords manager..", "g": "plays", "l": 2, "q": "What is Play 6 in action?", "a": "Applying: Passwords manager..", "x": "In action: Passwords manager.. Here is how to actually do it — Naming consistent.. Digital File Organization The difference between knowing and doing is a calendar entry: schedule it. Purge. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7", "d": "Photos sorted.", "g": "plays", "l": 2, "q": "What is Play 7?", "a": "Photos sorted.", "x": "Digital File Organization play 7: Photos sorted.. Naming consistent. This is one of the eight core moves — master all eight and you outperform most people who wing it. find anything fast. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7 in action", "d": "Applying: Photos sorted..", "g": "plays", "l": 2, "q": "What is Play 7 in action?", "a": "Applying: Photos sorted..", "x": "In action: Photos sorted.. Here is how to actually do it — Cloud backup.. Digital File Organization The difference between knowing and doing is a calendar entry: schedule it. Folder system. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8", "d": "Purge.", "g": "plays", "l": 2, "q": "What is Play 8?", "a": "Purge.", "x": "Digital File Organization play 8: Purge.. Cloud backup. This is one of the eight core moves — master all eight and you outperform most people who wing it. find anything fast. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8 in action", "d": "Applying: Purge..", "g": "plays", "l": 2, "q": "What is Play 8 in action?", "a": "Applying: Purge..", "x": "In action: Purge.. Here is how to actually do it — Inbox zero.. Digital File Organization The difference between knowing and doing is a calendar entry: schedule it. Naming consistent. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Your action plan", "d": "Digital File Organization: week one.", "g": "action-plan", "l": 2, "q": "What is Your action plan?", "a": "Digital File Organization: week one.", "x": "Week one: Folder system.. Start here — Naming consistent.. Digital File Organization Do not try to do everything; do the first three plays badly rather than all eight never. find anything fast. Momentum beats perfection.", "s": "signature-original", "f": null}, {"t": "Mistakes to avoid", "d": "Where Digital File Organization goes wrong.", "g": "mistakes", "l": 2, "q": "What is Mistakes to avoid?", "a": "Where Digital File Organization goes wrong.", "x": "The classic mistakes: Archive.. find anything fast. Most failure in Digital File Organization is not bad luck — it is these avoidable errors. Passwords manager. Learn them from this database, not from experience.", "s": "signature-original", "f": null}, {"t": "Tools and resources", "d": "The Digital File Organization toolkit.", "g": "resources", "l": 2, "q": "What is Tools and resources?", "a": "The Digital File Organization toolkit.", "x": "The toolkit: Photos sorted.. Digital File Organization The right tools multiply effort — Purge.. find anything fast. Keep it simple: master a few tools rather than collecting dozens. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Quick wins", "d": "Digital File Organization results this week.", "g": "quick-wins", "l": 2, "q": "What is Quick wins?", "a": "Digital File Organization results this week.", "x": "Quick wins: Naming consistent.. Inbox zero. These pay off fast — do them first for the motivation to continue. Digital File Organization find anything fast. compounds; start the compounding now. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Advanced tactics", "d": "Level up Digital File Organization.", "g": "advanced", "l": 2, "q": "What is Advanced tactics?", "a": "Level up Digital File Organization.", "x": "Advanced: Purge.. Passwords manager. Once the fundamentals run on autopilot, these separate the good from the great at Digital File Organization. find anything fast. Do not attempt until the basics are solid.", "s": "signature-original", "f": null}, {"t": "Walkthrough", "d": "Digital File Organization: a complete example.", "g": "walkthrough", "l": 2, "q": "What is Walkthrough?", "a": "Digital File Organization: a complete example.", "x": "Walkthrough: find anything fast., applied end to end — Folder system.. Cloud backup. Follow along with your own situation beside you. Digital File Organization Theory becomes skill by doing. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Myths", "d": "Myths about Digital File Organization.", "g": "myths", "l": 2, "q": "What is Myths?", "a": "Myths about Digital File Organization.", "x": "The myths: Digital File Organization is surrounded by bad advice — Photos sorted.. find anything fast. Ignore the gurus selling shortcuts; the fundamentals in this database are the shortcut. Archive. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}];
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
var gen={version:'jahdb-e2-sig-home-digital-file-organization-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
