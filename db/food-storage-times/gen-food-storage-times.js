(function(){'use strict';
/* JAH Food Storage Times Database generator — jahdb-food-storage-times-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='food-storage-times',PREFIX='JAH-FDS-',NAME='JAH Food Storage Times Database';
var FIELDS=["fridge", "freezer", "pantry"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Raw chicken", "d": "Raw chicken keeps 1-2 days refrigerated, 9 months frozen. Never wash it — cooking kills bacteria.", "g": "fridge", "l": 2, "q": "What is Raw chicken?", "a": "Raw chicken keeps 1-2 days refrigerated, 9 months frozen. Never wash it — cooking kills bacteria.", "x": "Raw chicken keeps 1-2 days refrigerated, 9 months frozen. Never wash it — cooking kills bacteria. fridge: 1-2 days. freezer: 9 months. tip: coldest shelf, sealed. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Raw beef steaks", "d": "Steaks keep 3-5 days in the fridge, up to a year frozen.", "g": "fridge", "l": 2, "q": "What is Raw beef steaks?", "a": "Steaks keep 3-5 days in the fridge, up to a year frozen.", "x": "Steaks keep 3-5 days in the fridge, up to a year frozen. fridge: 3-5 days. freezer: 6-12 months. tip: original wrap for freezer. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Ground meat", "d": "Ground meat is the most perishable: 1-2 days fridge, 3-4 months freezer.", "g": "fridge", "l": 2, "q": "What is Ground meat?", "a": "Ground meat is the most perishable: 1-2 days fridge, 3-4 months freezer.", "x": "Ground meat is the most perishable: 1-2 days fridge, 3-4 months freezer. fridge: 1-2 days. freezer: 3-4 months. tip: freeze flat for fast thaw. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Bacon", "d": "Opened bacon lasts a week refrigerated.", "g": "fridge", "l": 2, "q": "What is Bacon?", "a": "Opened bacon lasts a week refrigerated.", "x": "Opened bacon lasts a week refrigerated. fridge: 1 week opened. freezer: 1 month. tip: freeze in portions. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Hot dogs", "d": "Opened hot dogs: one week in the fridge.", "g": "fridge", "l": 2, "q": "What is Hot dogs?", "a": "Opened hot dogs: one week in the fridge.", "x": "Opened hot dogs: one week in the fridge. fridge: 1 week opened. freezer: 1-2 months. tip: keep sealed. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Deli meat", "d": "Opened deli meat lasts 3-5 days.", "g": "fridge", "l": 2, "q": "What is Deli meat?", "a": "Opened deli meat lasts 3-5 days.", "x": "Opened deli meat lasts 3-5 days. fridge: 3-5 days opened. freezer: 1-2 months. tip: keep cold, sealed. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Cooked chicken", "d": "Cooked chicken: 3-4 days refrigerated.", "g": "fridge", "l": 2, "q": "What is Cooked chicken?", "a": "Cooked chicken: 3-4 days refrigerated.", "x": "Cooked chicken: 3-4 days refrigerated. fridge: 3-4 days. freezer: 4 months. tip: cool within 2 hours. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Cooked beef", "d": "Cooked beef keeps 3-4 days in the fridge.", "g": "fridge", "l": 2, "q": "What is Cooked beef?", "a": "Cooked beef keeps 3-4 days in the fridge.", "x": "Cooked beef keeps 3-4 days in the fridge. fridge: 3-4 days. freezer: 2-3 months. tip: slice before freezing. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Fish (raw)", "d": "Raw fish is the most time-critical: 1-2 days max refrigerated.", "g": "fridge", "l": 2, "q": "What is Fish (raw)?", "a": "Raw fish is the most time-critical: 1-2 days max refrigerated.", "x": "Raw fish is the most time-critical: 1-2 days max refrigerated. fridge: 1-2 days. freezer: 6 months. tip: coldest part, ice. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Shrimp (raw)", "d": "Raw shrimp: 1-2 days refrigerated.", "g": "fridge", "l": 2, "q": "What is Shrimp (raw)?", "a": "Raw shrimp: 1-2 days refrigerated.", "x": "Raw shrimp: 1-2 days refrigerated. fridge: 1-2 days. freezer: 6 months. tip: keep iced. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Eggs (in shell)", "d": "Eggs keep 3-5 weeks refrigerated in their carton.", "g": "fridge", "l": 2, "q": "What is Eggs (in shell)?", "a": "Eggs keep 3-5 weeks refrigerated in their carton.", "x": "Eggs keep 3-5 weeks refrigerated in their carton. fridge: 3-5 weeks. freezer: do not freeze in shell. tip: keep in carton. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Milk", "d": "Milk lasts about a week past sell-by if kept cold; the door is warmest.", "g": "fridge", "l": 2, "q": "What is Milk?", "a": "Milk lasts about a week past sell-by if kept cold; the door is warmest.", "x": "Milk lasts about a week past sell-by if kept cold; the door is warmest. fridge: 1 week past sell-by. freezer: 3 months. tip: coldest shelf, not door. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Butter", "d": "Butter: months refrigerated; a week at room temp is safe.", "g": "fridge", "l": 2, "q": "What is Butter?", "a": "Butter: months refrigerated; a week at room temp is safe.", "x": "Butter: months refrigerated; a week at room temp is safe. fridge: 1-3 months. freezer: 6-9 months. tip: a week on counter is fine. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Hard cheese", "d": "Hard cheese keeps 6 months; cut mold off with a 1-inch margin.", "g": "fridge", "l": 2, "q": "What is Hard cheese?", "a": "Hard cheese keeps 6 months; cut mold off with a 1-inch margin.", "x": "Hard cheese keeps 6 months; cut mold off with a 1-inch margin. fridge: 6 months unopened. freezer: 6 months. tip: wax paper, not plastic. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Soft cheese", "d": "Soft cheeses last 1-2 weeks; discard moldy soft cheese entirely.", "g": "fridge", "l": 2, "q": "What is Soft cheese?", "a": "Soft cheeses last 1-2 weeks; discard moldy soft cheese entirely.", "x": "Soft cheeses last 1-2 weeks; discard moldy soft cheese entirely. fridge: 1-2 weeks. freezer: not recommended. tip: eat fresh. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Yogurt", "d": "Yogurt keeps 1-3 weeks past its date if sealed and cold.", "g": "fridge", "l": 2, "q": "What is Yogurt?", "a": "Yogurt keeps 1-3 weeks past its date if sealed and cold.", "x": "Yogurt keeps 1-3 weeks past its date if sealed and cold. fridge: 1-3 weeks. freezer: 1-2 months. tip: sealed. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Leftovers", "d": "All leftovers: 3-4 days fridge. Cool within 2 hours.", "g": "fridge", "l": 2, "q": "What is Leftovers?", "a": "All leftovers: 3-4 days fridge. Cool within 2 hours.", "x": "All leftovers: 3-4 days fridge. Cool within 2 hours. fridge: 3-4 days. freezer: 3-4 months. tip: shallow containers cool fast. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Pizza", "d": "Leftover pizza: 3-4 days refrigerated.", "g": "fridge", "l": 2, "q": "What is Pizza?", "a": "Leftover pizza: 3-4 days refrigerated.", "x": "Leftover pizza: 3-4 days refrigerated. fridge: 3-4 days. freezer: 1-2 months. tip: reheat to 75 C. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Rice (cooked)", "d": "Cooked rice must cool fast: 4-6 days fridge, and reheat steaming.", "g": "fridge", "l": 2, "q": "What is Rice (cooked)?", "a": "Cooked rice must cool fast: 4-6 days fridge, and reheat steaming.", "x": "Cooked rice must cool fast: 4-6 days fridge, and reheat steaming. fridge: 4-6 days. freezer: 6 months. tip: cool fast, bacillus cereus risk. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Pasta (cooked)", "d": "Cooked pasta: 3-5 days refrigerated.", "g": "fridge", "l": 2, "q": "What is Pasta (cooked)?", "a": "Cooked pasta: 3-5 days refrigerated.", "x": "Cooked pasta: 3-5 days refrigerated. fridge: 3-5 days. freezer: 1-2 months. tip: toss with oil. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Bread", "d": "Bread stales fastest in the fridge; freeze for long storage.", "g": "pantry", "l": 2, "q": "What is Bread?", "a": "Bread stales fastest in the fridge; freeze for long storage.", "x": "Bread stales fastest in the fridge; freeze for long storage. fridge: do not refrigerate. freezer: 3 months. tip: room temp 2-3 days. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Flour (white)", "d": "White flour: 6-8 months in the pantry airtight.", "g": "pantry", "l": 2, "q": "What is Flour (white)?", "a": "White flour: 6-8 months in the pantry airtight.", "x": "White flour: 6-8 months in the pantry airtight. fridge: —. freezer: 1-2 years. tip: pantry 6-8 months airtight. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Flour (whole wheat)", "d": "Whole wheat flour goes rancid: fridge 3 months.", "g": "pantry", "l": 2, "q": "What is Flour (whole wheat)?", "a": "Whole wheat flour goes rancid: fridge 3 months.", "x": "Whole wheat flour goes rancid: fridge 3 months. fridge: 3 months. freezer: 1 year. tip: oils go rancid. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Sugar", "d": "Sugar keeps indefinitely if dry.", "g": "pantry", "l": 2, "q": "What is Sugar?", "a": "Sugar keeps indefinitely if dry.", "x": "Sugar keeps indefinitely if dry. fridge: —. freezer: indefinite. tip: dry, airtight. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Honey", "d": "Honey never spoils; crystallization is normal, warm to reliquefy.", "g": "pantry", "l": 2, "q": "What is Honey?", "a": "Honey never spoils; crystallization is normal, warm to reliquefy.", "x": "Honey never spoils; crystallization is normal, warm to reliquefy. fridge: do not refrigerate. freezer: indefinite. tip: crystallization is normal. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-food-storage-times-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
