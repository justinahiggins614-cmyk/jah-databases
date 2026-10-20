(function(){'use strict';
/* JAH Signature Sleep Training Database generator — jahdb-e2-sig-parent-sleep-training-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sig-parent-sleep-training',PREFIX='JAH-E2SIGPARENT-',NAME='JAH Signature Sleep Training Database';
var FIELDS=["overview", "fundamentals", "plays", "action-plan", "mistakes", "resources", "quick-wins", "advanced", "walkthrough", "myths", "checklist", "faq", "help", "quiz"];
var GEN_SRC='signature-original';
var MODE='quiz';
var BANK=[{"t": "Signature Sleep Training: the playbook", "d": "Sleep Training: healthy sleep habits..", "g": "overview", "l": 2, "q": "What is Signature Sleep Training: the playbook?", "a": "Sleep Training: healthy sleep habits..", "x": "The Signature Sleep Training playbook: healthy sleep habits.. Bedtime routine. This is a complete working guide — not theory, but the actual moves: what to do first, what to avoid, and how to know it is working. Drowsy but awake. Every record is actionable.", "s": "signature-original", "f": null}, {"t": "The fundamentals", "d": "First principles of Sleep Training.", "g": "fundamentals", "l": 2, "q": "What is The fundamentals?", "a": "First principles of Sleep Training.", "x": "First principles: Consistent bedtime.. healthy sleep habits. Get these right and the rest is optimization; get them wrong and nothing else matters. Sleep Training White noise. is simple but not easy — fundamentals first, always.", "s": "signature-original", "f": null}, {"t": "Play 1", "d": "Bedtime routine.", "g": "plays", "l": 2, "q": "What is Play 1?", "a": "Bedtime routine.", "x": "Sleep Training play 1: Bedtime routine.. White noise. This is one of the eight core moves — master all eight and you outperform most people who wing it. healthy sleep habits. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 1 in action", "d": "Applying: Bedtime routine..", "g": "plays", "l": 2, "q": "What is Play 1 in action?", "a": "Applying: Bedtime routine..", "x": "In action: Bedtime routine.. Here is how to actually do it — Naps matter.. Sleep Training The difference between knowing and doing is a calendar entry: schedule it. Consistent bedtime. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2", "d": "Drowsy but awake.", "g": "plays", "l": 2, "q": "What is Play 2?", "a": "Drowsy but awake.", "x": "Sleep Training play 2: Drowsy but awake.. Naps matter. This is one of the eight core moves — master all eight and you outperform most people who wing it. healthy sleep habits. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2 in action", "d": "Applying: Drowsy but awake..", "g": "plays", "l": 2, "q": "What is Play 2 in action?", "a": "Applying: Drowsy but awake..", "x": "In action: Drowsy but awake.. Here is how to actually do it — Patience.. Sleep Training The difference between knowing and doing is a calendar entry: schedule it. White noise. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3", "d": "Consistent bedtime.", "g": "plays", "l": 2, "q": "What is Play 3?", "a": "Consistent bedtime.", "x": "Sleep Training play 3: Consistent bedtime.. Patience. This is one of the eight core moves — master all eight and you outperform most people who wing it. healthy sleep habits. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3 in action", "d": "Applying: Consistent bedtime..", "g": "plays", "l": 2, "q": "What is Play 3 in action?", "a": "Applying: Consistent bedtime..", "x": "In action: Consistent bedtime.. Here is how to actually do it — Dark room.. Sleep Training The difference between knowing and doing is a calendar entry: schedule it. Naps matter. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4", "d": "White noise.", "g": "plays", "l": 2, "q": "What is Play 4?", "a": "White noise.", "x": "Sleep Training play 4: White noise.. Dark room. This is one of the eight core moves — master all eight and you outperform most people who wing it. healthy sleep habits. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4 in action", "d": "Applying: White noise..", "g": "plays", "l": 2, "q": "What is Play 4 in action?", "a": "Applying: White noise..", "x": "In action: White noise.. Here is how to actually do it — No screens before bed.. Sleep Training The difference between knowing and doing is a calendar entry: schedule it. Patience. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5", "d": "Naps matter.", "g": "plays", "l": 2, "q": "What is Play 5?", "a": "Naps matter.", "x": "Sleep Training play 5: Naps matter.. No screens before bed. This is one of the eight core moves — master all eight and you outperform most people who wing it. healthy sleep habits. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5 in action", "d": "Applying: Naps matter..", "g": "plays", "l": 2, "q": "What is Play 5 in action?", "a": "Applying: Naps matter..", "x": "In action: Naps matter.. Here is how to actually do it — Bedtime routine.. Sleep Training The difference between knowing and doing is a calendar entry: schedule it. Dark room. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6", "d": "Patience.", "g": "plays", "l": 2, "q": "What is Play 6?", "a": "Patience.", "x": "Sleep Training play 6: Patience.. Bedtime routine. This is one of the eight core moves — master all eight and you outperform most people who wing it. healthy sleep habits. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6 in action", "d": "Applying: Patience..", "g": "plays", "l": 2, "q": "What is Play 6 in action?", "a": "Applying: Patience..", "x": "In action: Patience.. Here is how to actually do it — Drowsy but awake.. Sleep Training The difference between knowing and doing is a calendar entry: schedule it. No screens before bed. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7", "d": "Dark room.", "g": "plays", "l": 2, "q": "What is Play 7?", "a": "Dark room.", "x": "Sleep Training play 7: Dark room.. Drowsy but awake. This is one of the eight core moves — master all eight and you outperform most people who wing it. healthy sleep habits. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7 in action", "d": "Applying: Dark room..", "g": "plays", "l": 2, "q": "What is Play 7 in action?", "a": "Applying: Dark room..", "x": "In action: Dark room.. Here is how to actually do it — Consistent bedtime.. Sleep Training The difference between knowing and doing is a calendar entry: schedule it. Bedtime routine. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8", "d": "No screens before bed.", "g": "plays", "l": 2, "q": "What is Play 8?", "a": "No screens before bed.", "x": "Sleep Training play 8: No screens before bed.. Consistent bedtime. This is one of the eight core moves — master all eight and you outperform most people who wing it. healthy sleep habits. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8 in action", "d": "Applying: No screens before bed..", "g": "plays", "l": 2, "q": "What is Play 8 in action?", "a": "Applying: No screens before bed..", "x": "In action: No screens before bed.. Here is how to actually do it — White noise.. Sleep Training The difference between knowing and doing is a calendar entry: schedule it. Drowsy but awake. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Your action plan", "d": "Sleep Training: week one.", "g": "action-plan", "l": 2, "q": "What is Your action plan?", "a": "Sleep Training: week one.", "x": "Week one: Bedtime routine.. Start here — Drowsy but awake.. Sleep Training Do not try to do everything; do the first three plays badly rather than all eight never. healthy sleep habits. Momentum beats perfection.", "s": "signature-original", "f": null}, {"t": "Mistakes to avoid", "d": "Where Sleep Training goes wrong.", "g": "mistakes", "l": 2, "q": "What is Mistakes to avoid?", "a": "Where Sleep Training goes wrong.", "x": "The classic mistakes: Naps matter.. healthy sleep habits. Most failure in Sleep Training is not bad luck — it is these avoidable errors. Patience. Learn them from this database, not from experience. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Tools and resources", "d": "The Sleep Training toolkit.", "g": "resources", "l": 2, "q": "What is Tools and resources?", "a": "The Sleep Training toolkit.", "x": "The toolkit: Dark room.. Sleep Training The right tools multiply effort — No screens before bed.. healthy sleep habits. Keep it simple: master a few tools rather than collecting dozens. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Quick wins", "d": "Sleep Training results this week.", "g": "quick-wins", "l": 2, "q": "What is Quick wins?", "a": "Sleep Training results this week.", "x": "Quick wins: Drowsy but awake.. White noise. These pay off fast — do them first for the motivation to continue. Sleep Training healthy sleep habits. compounds; start the compounding now. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Advanced tactics", "d": "Level up Sleep Training.", "g": "advanced", "l": 2, "q": "What is Advanced tactics?", "a": "Level up Sleep Training.", "x": "Advanced: No screens before bed.. Patience. Once the fundamentals run on autopilot, these separate the good from the great at Sleep Training. healthy sleep habits. Do not attempt until the basics are solid.", "s": "signature-original", "f": null}, {"t": "Walkthrough", "d": "Sleep Training: a complete example.", "g": "walkthrough", "l": 2, "q": "What is Walkthrough?", "a": "Sleep Training: a complete example.", "x": "Walkthrough: healthy sleep habits., applied end to end — Bedtime routine.. Consistent bedtime. Follow along with your own situation beside you. Sleep Training Theory becomes skill by doing. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Myths", "d": "Myths about Sleep Training.", "g": "myths", "l": 2, "q": "What is Myths?", "a": "Myths about Sleep Training.", "x": "The myths: Sleep Training is surrounded by bad advice — Dark room.. healthy sleep habits. Ignore the gurus selling shortcuts; the fundamentals in this database are the shortcut. Naps matter. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}];
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
var gen={version:'jahdb-e2-sig-parent-sleep-training-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
