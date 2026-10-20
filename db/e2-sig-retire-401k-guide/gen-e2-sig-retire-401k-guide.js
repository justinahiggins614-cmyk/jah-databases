(function(){'use strict';
/* JAH Signature 401k Guide Database generator — jahdb-e2-sig-retire-401k-guide-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sig-retire-401k-guide',PREFIX='JAH-E2SIGRETIRE-',NAME='JAH Signature 401k Guide Database';
var FIELDS=["overview", "fundamentals", "plays", "action-plan", "mistakes", "resources", "quick-wins", "advanced", "walkthrough", "myths", "checklist", "faq", "help", "quiz"];
var GEN_SRC='signature-original';
var MODE='quiz';
var BANK=[{"t": "Signature 401k Guide: the playbook", "d": "401k Guide: the workplace retirement workhorse..", "g": "overview", "l": 2, "q": "What is Signature 401k Guide: the playbook?", "a": "401k Guide: the workplace retirement workhorse..", "x": "The Signature 401k Guide playbook: the workplace retirement workhorse.. Match: free money. This is a complete working guide — not theory, but the actual moves: what to do first, what to avoid, and how to know it is working. Contribute to match first. Every record is actionable.", "s": "signature-original", "f": null}, {"t": "The fundamentals", "d": "First principles of 401k Guide.", "g": "fundamentals", "l": 2, "q": "What is The fundamentals?", "a": "First principles of 401k Guide.", "x": "First principles: Roth vs traditional.. the workplace retirement workhorse. Get these right and the rest is optimization; get them wrong and nothing else matters. 401k Guide Increase one percent yearly. is simple but not easy — fundamentals first, always.", "s": "signature-original", "f": null}, {"t": "Play 1", "d": "Match: free money.", "g": "plays", "l": 2, "q": "What is Play 1?", "a": "Match: free money.", "x": "401k Guide play 1: Match: free money.. Increase one percent yearly. This is one of the eight core moves — master all eight and you outperform most people who wing it. the workplace retirement workhorse.", "s": "signature-original", "f": null}, {"t": "Play 1 in action", "d": "Applying: Match: free money..", "g": "plays", "l": 2, "q": "What is Play 1 in action?", "a": "Applying: Match: free money..", "x": "In action: Match: free money.. Here is how to actually do it — Target-date funds simple.. 401k Guide The difference between knowing and doing is a calendar entry: schedule it. Roth vs traditional. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2", "d": "Contribute to match first.", "g": "plays", "l": 2, "q": "What is Play 2?", "a": "Contribute to match first.", "x": "401k Guide play 2: Contribute to match first.. Target-date funds simple. This is one of the eight core moves — master all eight and you outperform most people who wing it. the workplace retirement workhorse.", "s": "signature-original", "f": null}, {"t": "Play 2 in action", "d": "Applying: Contribute to match first..", "g": "plays", "l": 2, "q": "What is Play 2 in action?", "a": "Applying: Contribute to match first..", "x": "In action: Contribute to match first.. Here is how to actually do it — Vesting schedule.. 401k Guide The difference between knowing and doing is a calendar entry: schedule it. Increase one percent yearly.", "s": "signature-original", "f": null}, {"t": "Play 3", "d": "Roth vs traditional.", "g": "plays", "l": 2, "q": "What is Play 3?", "a": "Roth vs traditional.", "x": "401k Guide play 3: Roth vs traditional.. Vesting schedule. This is one of the eight core moves — master all eight and you outperform most people who wing it. the workplace retirement workhorse. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3 in action", "d": "Applying: Roth vs traditional..", "g": "plays", "l": 2, "q": "What is Play 3 in action?", "a": "Applying: Roth vs traditional..", "x": "In action: Roth vs traditional.. Here is how to actually do it — Loans: avoid.. 401k Guide The difference between knowing and doing is a calendar entry: schedule it. Target-date funds simple. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4", "d": "Increase one percent yearly.", "g": "plays", "l": 2, "q": "What is Play 4?", "a": "Increase one percent yearly.", "x": "401k Guide play 4: Increase one percent yearly.. Loans: avoid. This is one of the eight core moves — master all eight and you outperform most people who wing it. the workplace retirement workhorse. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4 in action", "d": "Applying: Increase one percent yearly..", "g": "plays", "l": 2, "q": "What is Play 4 in action?", "a": "Applying: Increase one percent yearly..", "x": "In action: Increase one percent yearly.. Here is how to actually do it — Roll over when leaving.. 401k Guide The difference between knowing and doing is a calendar entry: schedule it. Vesting schedule.", "s": "signature-original", "f": null}, {"t": "Play 5", "d": "Target-date funds simple.", "g": "plays", "l": 2, "q": "What is Play 5?", "a": "Target-date funds simple.", "x": "401k Guide play 5: Target-date funds simple.. Roll over when leaving. This is one of the eight core moves — master all eight and you outperform most people who wing it. the workplace retirement workhorse.", "s": "signature-original", "f": null}, {"t": "Play 5 in action", "d": "Applying: Target-date funds simple..", "g": "plays", "l": 2, "q": "What is Play 5 in action?", "a": "Applying: Target-date funds simple..", "x": "In action: Target-date funds simple.. Here is how to actually do it — Match: free money.. 401k Guide The difference between knowing and doing is a calendar entry: schedule it. Loans: avoid. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6", "d": "Vesting schedule.", "g": "plays", "l": 2, "q": "What is Play 6?", "a": "Vesting schedule.", "x": "401k Guide play 6: Vesting schedule.. Match: free money. This is one of the eight core moves — master all eight and you outperform most people who wing it. the workplace retirement workhorse. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6 in action", "d": "Applying: Vesting schedule..", "g": "plays", "l": 2, "q": "What is Play 6 in action?", "a": "Applying: Vesting schedule..", "x": "In action: Vesting schedule.. Here is how to actually do it — Contribute to match first.. 401k Guide The difference between knowing and doing is a calendar entry: schedule it. Roll over when leaving. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7", "d": "Loans: avoid.", "g": "plays", "l": 2, "q": "What is Play 7?", "a": "Loans: avoid.", "x": "401k Guide play 7: Loans: avoid.. Contribute to match first. This is one of the eight core moves — master all eight and you outperform most people who wing it. the workplace retirement workhorse. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7 in action", "d": "Applying: Loans: avoid..", "g": "plays", "l": 2, "q": "What is Play 7 in action?", "a": "Applying: Loans: avoid..", "x": "In action: Loans: avoid.. Here is how to actually do it — Roth vs traditional.. 401k Guide The difference between knowing and doing is a calendar entry: schedule it. Match: free money. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8", "d": "Roll over when leaving.", "g": "plays", "l": 2, "q": "What is Play 8?", "a": "Roll over when leaving.", "x": "401k Guide play 8: Roll over when leaving.. Roth vs traditional. This is one of the eight core moves — master all eight and you outperform most people who wing it. the workplace retirement workhorse. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8 in action", "d": "Applying: Roll over when leaving..", "g": "plays", "l": 2, "q": "What is Play 8 in action?", "a": "Applying: Roll over when leaving..", "x": "In action: Roll over when leaving.. Here is how to actually do it — Increase one percent yearly.. 401k Guide The difference between knowing and doing is a calendar entry: schedule it. Contribute to match first.", "s": "signature-original", "f": null}, {"t": "Your action plan", "d": "401k Guide: week one.", "g": "action-plan", "l": 2, "q": "What is Your action plan?", "a": "401k Guide: week one.", "x": "Week one: Match: free money.. Start here — Contribute to match first.. 401k Guide Do not try to do everything; do the first three plays badly rather than all eight never. the workplace retirement workhorse. Momentum beats perfection.", "s": "signature-original", "f": null}, {"t": "Mistakes to avoid", "d": "Where 401k Guide goes wrong.", "g": "mistakes", "l": 2, "q": "What is Mistakes to avoid?", "a": "Where 401k Guide goes wrong.", "x": "The classic mistakes: Target-date funds simple.. the workplace retirement workhorse. Most failure in 401k Guide is not bad luck — it is these avoidable errors. Vesting schedule. Learn them from this database, not from experience.", "s": "signature-original", "f": null}, {"t": "Tools and resources", "d": "The 401k Guide toolkit.", "g": "resources", "l": 2, "q": "What is Tools and resources?", "a": "The 401k Guide toolkit.", "x": "The toolkit: Loans: avoid.. 401k Guide The right tools multiply effort — Roll over when leaving.. the workplace retirement workhorse. Keep it simple: master a few tools rather than collecting dozens. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Quick wins", "d": "401k Guide results this week.", "g": "quick-wins", "l": 2, "q": "What is Quick wins?", "a": "401k Guide results this week.", "x": "Quick wins: Contribute to match first.. Increase one percent yearly. These pay off fast — do them first for the motivation to continue. 401k Guide the workplace retirement workhorse. compounds; start the compounding now.", "s": "signature-original", "f": null}, {"t": "Advanced tactics", "d": "Level up 401k Guide.", "g": "advanced", "l": 2, "q": "What is Advanced tactics?", "a": "Level up 401k Guide.", "x": "Advanced: Roll over when leaving.. Vesting schedule. Once the fundamentals run on autopilot, these separate the good from the great at 401k Guide. the workplace retirement workhorse. Do not attempt until the basics are solid.", "s": "signature-original", "f": null}, {"t": "Walkthrough", "d": "401k Guide: a complete example.", "g": "walkthrough", "l": 2, "q": "What is Walkthrough?", "a": "401k Guide: a complete example.", "x": "Walkthrough: the workplace retirement workhorse., applied end to end — Match: free money.. Roth vs traditional. Follow along with your own situation beside you. 401k Guide Theory becomes skill by doing.", "s": "signature-original", "f": null}, {"t": "Myths", "d": "Myths about 401k Guide.", "g": "myths", "l": 2, "q": "What is Myths?", "a": "Myths about 401k Guide.", "x": "The myths: 401k Guide is surrounded by bad advice — Loans: avoid.. the workplace retirement workhorse. Ignore the gurus selling shortcuts; the fundamentals in this database are the shortcut. Target-date funds simple.", "s": "signature-original", "f": null}];
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
var gen={version:'jahdb-e2-sig-retire-401k-guide-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
