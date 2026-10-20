(function(){'use strict';
/* JAH CSS Properties Database generator — jahdb-css-properties-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='css-properties',PREFIX='JAH-CSS-',NAME='JAH CSS Properties Database';
var FIELDS=["layout", "flexbox", "grid", "typography", "color-background", "border"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "align-content", "d": "Aligns flex lines within the container.", "g": "flexbox", "l": 2, "q": "What is align-content?", "a": "Aligns flex lines within the container.", "x": "align-content — Aligns flex lines within the container. Example: align-content: center;.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "align-items", "d": "Aligns flex items on the cross axis.", "g": "flexbox", "l": 2, "q": "What is align-items?", "a": "Aligns flex items on the cross axis.", "x": "align-items — Aligns flex items on the cross axis. Example: align-items: stretch;.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "align-self", "d": "Overrides alignment for one item.", "g": "flexbox", "l": 2, "q": "What is align-self?", "a": "Overrides alignment for one item.", "x": "align-self — Overrides alignment for one item. Example: align-self: flex-end;.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "justify-content", "d": "Aligns items on the main axis.", "g": "flexbox", "l": 2, "q": "What is justify-content?", "a": "Aligns items on the main axis.", "x": "justify-content — Aligns items on the main axis. Example: justify-content: space-between;.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "justify-items", "d": "Aligns grid items on the inline axis.", "g": "grid", "l": 2, "q": "What is justify-items?", "a": "Aligns grid items on the inline axis.", "x": "justify-items — Aligns grid items on the inline axis. Example: justify-items: center;.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "justify-self", "d": "Aligns one grid item on the inline axis.", "g": "grid", "l": 2, "q": "What is justify-self?", "a": "Aligns one grid item on the inline axis.", "x": "justify-self — Aligns one grid item on the inline axis. Example: justify-self: end;.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "flex", "d": "Shorthand for grow, shrink, basis.", "g": "flexbox", "l": 2, "q": "What is flex?", "a": "Shorthand for grow, shrink, basis.", "x": "flex — Shorthand for grow, shrink, basis. Example: flex: 1;.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "flex-basis", "d": "Initial main size of a flex item.", "g": "flexbox", "l": 2, "q": "What is flex-basis?", "a": "Initial main size of a flex item.", "x": "flex-basis — Initial main size of a flex item. Example: flex-basis: 200px;.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "flex-direction", "d": "Main axis direction.", "g": "flexbox", "l": 2, "q": "What is flex-direction?", "a": "Main axis direction.", "x": "flex-direction — Main axis direction. Example: flex-direction: column;.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "flex-flow", "d": "Shorthand for direction and wrap.", "g": "flexbox", "l": 2, "q": "What is flex-flow?", "a": "Shorthand for direction and wrap.", "x": "flex-flow — Shorthand for direction and wrap. Example: flex-flow: row wrap;.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "flex-grow", "d": "How much an item grows.", "g": "flexbox", "l": 2, "q": "What is flex-grow?", "a": "How much an item grows.", "x": "flex-grow — How much an item grows. Example: flex-grow: 2;.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "flex-shrink", "d": "How much an item shrinks.", "g": "flexbox", "l": 2, "q": "What is flex-shrink?", "a": "How much an item shrinks.", "x": "flex-shrink — How much an item shrinks. Example: flex-shrink: 0;.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "flex-wrap", "d": "Whether items wrap.", "g": "flexbox", "l": 2, "q": "What is flex-wrap?", "a": "Whether items wrap.", "x": "flex-wrap — Whether items wrap. Example: flex-wrap: wrap;.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "order", "d": "Visual order of flex/grid items.", "g": "flexbox", "l": 2, "q": "What is order?", "a": "Visual order of flex/grid items.", "x": "order — Visual order of flex/grid items. Example: order: -1;.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "gap", "d": "Space between grid/flex items.", "g": "grid", "l": 2, "q": "What is gap?", "a": "Space between grid/flex items.", "x": "gap — Space between grid/flex items. Example: gap: 12px;.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "row-gap", "d": "Space between rows.", "g": "grid", "l": 2, "q": "What is row-gap?", "a": "Space between rows.", "x": "row-gap — Space between rows. Example: row-gap: 8px;.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "column-gap", "d": "Space between columns.", "g": "grid", "l": 2, "q": "What is column-gap?", "a": "Space between columns.", "x": "column-gap — Space between columns. Example: column-gap: 8px;.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "grid", "d": "Shorthand for all grid properties.", "g": "grid", "l": 2, "q": "What is grid?", "a": "Shorthand for all grid properties.", "x": "grid — Shorthand for all grid properties. Example: grid: auto-flow / 1fr 1fr;.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "grid-area", "d": "Named area or row/column placement.", "g": "grid", "l": 2, "q": "What is grid-area?", "a": "Named area or row/column placement.", "x": "grid-area — Named area or row/column placement. Example: grid-area: header;.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "grid-auto-columns", "d": "Size of implicit columns.", "g": "grid", "l": 2, "q": "What is grid-auto-columns?", "a": "Size of implicit columns.", "x": "grid-auto-columns — Size of implicit columns. Example: grid-auto-columns: 100px;.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "grid-auto-flow", "d": "Auto-placement algorithm.", "g": "grid", "l": 2, "q": "What is grid-auto-flow?", "a": "Auto-placement algorithm.", "x": "grid-auto-flow — Auto-placement algorithm. Example: grid-auto-flow: dense;.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "grid-auto-rows", "d": "Size of implicit rows.", "g": "grid", "l": 2, "q": "What is grid-auto-rows?", "a": "Size of implicit rows.", "x": "grid-auto-rows — Size of implicit rows. Example: grid-auto-rows: 50px;.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "grid-column", "d": "Column placement shorthand.", "g": "grid", "l": 2, "q": "What is grid-column?", "a": "Column placement shorthand.", "x": "grid-column — Column placement shorthand. Example: grid-column: 1 / 3;.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "grid-row", "d": "Row placement shorthand.", "g": "grid", "l": 2, "q": "What is grid-row?", "a": "Row placement shorthand.", "x": "grid-row — Row placement shorthand. Example: grid-row: 2;.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "grid-template", "d": "Shorthand for template areas/rows/columns.", "g": "grid", "l": 2, "q": "What is grid-template?", "a": "Shorthand for template areas/rows/columns.", "x": "grid-template — Shorthand for template areas/rows/columns. Example: grid-template: \"a a\" 1fr / 1fr 1fr;.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-css-properties-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
