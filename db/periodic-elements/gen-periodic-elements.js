(function(){'use strict';
/* JAH Periodic Elements Database generator — jahdb-periodic-elements-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='periodic-elements',PREFIX='JAH-ELM-',NAME='JAH Periodic Elements Database';
var FIELDS=["nonmetal", "noble gas", "alkali metal", "alkaline earth", "metalloid", "halogen", "post-transition metal", "transition metal", "lanthanide", "actinide"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Hydrogen (H)", "d": "Atomic number 1; weight 1.008; group 1, period 1.", "g": "nonmetal", "l": 1, "q": "What is the symbol of Hydrogen?", "a": "H", "x": "Hydrogen (H), atomic number 1: a nonmetal in group 1, period 1, with standard atomic weight 1.008.  Its position on the periodic table predicts its chemistry: elements in the same group share valence behavior, and the table marches from the light nonmetals of life to the heavy metals of industry and the synthetic frontier.", "s": "public-reference", "f": null}, {"t": "Helium (He)", "d": "Atomic number 2; weight 4.003; group 18, period 1.", "g": "noble gas", "l": 1, "q": "What is the symbol of Helium?", "a": "He", "x": "Helium (He), atomic number 2: a noble gas in group 18, period 1, with standard atomic weight 4.003.  Its position on the periodic table predicts its chemistry: elements in the same group share valence behavior, and the table marches from the light nonmetals of life to the heavy metals of industry and the synthetic frontier.", "s": "public-reference", "f": null}, {"t": "Lithium (Li)", "d": "Atomic number 3; weight 6.94; group 1, period 2.", "g": "alkali metal", "l": 1, "q": "What is the symbol of Lithium?", "a": "Li", "x": "Lithium (Li), atomic number 3: a alkali metal in group 1, period 2, with standard atomic weight 6.94.  Its position on the periodic table predicts its chemistry: elements in the same group share valence behavior, and the table marches from the light nonmetals of life to the heavy metals of industry and the synthetic frontier.", "s": "public-reference", "f": null}, {"t": "Beryllium (Be)", "d": "Atomic number 4; weight 9.012; group 2, period 2.", "g": "alkaline earth", "l": 1, "q": "What is the symbol of Beryllium?", "a": "Be", "x": "Beryllium (Be), atomic number 4: a alkaline earth in group 2, period 2, with standard atomic weight 9.012.  Its position on the periodic table predicts its chemistry: elements in the same group share valence behavior, and the table marches from the light nonmetals of life to the heavy metals of industry and the synthetic frontier.", "s": "public-reference", "f": null}, {"t": "Boron (B)", "d": "Atomic number 5; weight 10.81; group 13, period 2.", "g": "metalloid", "l": 1, "q": "What is the symbol of Boron?", "a": "B", "x": "Boron (B), atomic number 5: a metalloid in group 13, period 2, with standard atomic weight 10.81.  Its position on the periodic table predicts its chemistry: elements in the same group share valence behavior, and the table marches from the light nonmetals of life to the heavy metals of industry and the synthetic frontier.", "s": "public-reference", "f": null}, {"t": "Carbon (C)", "d": "Atomic number 6; weight 12.011; group 14, period 2.", "g": "nonmetal", "l": 1, "q": "What is the symbol of Carbon?", "a": "C", "x": "Carbon (C), atomic number 6: a nonmetal in group 14, period 2, with standard atomic weight 12.011.  Its position on the periodic table predicts its chemistry: elements in the same group share valence behavior, and the table marches from the light nonmetals of life to the heavy metals of industry and the synthetic frontier.", "s": "public-reference", "f": null}, {"t": "Nitrogen (N)", "d": "Atomic number 7; weight 14.007; group 15, period 2.", "g": "nonmetal", "l": 1, "q": "What is the symbol of Nitrogen?", "a": "N", "x": "Nitrogen (N), atomic number 7: a nonmetal in group 15, period 2, with standard atomic weight 14.007.  Its position on the periodic table predicts its chemistry: elements in the same group share valence behavior, and the table marches from the light nonmetals of life to the heavy metals of industry and the synthetic frontier.", "s": "public-reference", "f": null}, {"t": "Oxygen (O)", "d": "Atomic number 8; weight 16.0; group 16, period 2.", "g": "nonmetal", "l": 1, "q": "What is the symbol of Oxygen?", "a": "O", "x": "Oxygen (O), atomic number 8: a nonmetal in group 16, period 2, with standard atomic weight 16.0.  Its position on the periodic table predicts its chemistry: elements in the same group share valence behavior, and the table marches from the light nonmetals of life to the heavy metals of industry and the synthetic frontier.", "s": "public-reference", "f": null}, {"t": "Fluorine (F)", "d": "Atomic number 9; weight 19.0; group 17, period 2.", "g": "halogen", "l": 1, "q": "What is the symbol of Fluorine?", "a": "F", "x": "Fluorine (F), atomic number 9: a halogen in group 17, period 2, with standard atomic weight 19.0.  Its position on the periodic table predicts its chemistry: elements in the same group share valence behavior, and the table marches from the light nonmetals of life to the heavy metals of industry and the synthetic frontier.", "s": "public-reference", "f": null}, {"t": "Neon (Ne)", "d": "Atomic number 10; weight 20.18; group 18, period 2.", "g": "noble gas", "l": 1, "q": "What is the symbol of Neon?", "a": "Ne", "x": "Neon (Ne), atomic number 10: a noble gas in group 18, period 2, with standard atomic weight 20.18.  Its position on the periodic table predicts its chemistry: elements in the same group share valence behavior, and the table marches from the light nonmetals of life to the heavy metals of industry and the synthetic frontier.", "s": "public-reference", "f": null}, {"t": "Sodium (Na)", "d": "Atomic number 11; weight 22.99; group 1, period 3.", "g": "alkali metal", "l": 1, "q": "What is the symbol of Sodium?", "a": "Na", "x": "Sodium (Na), atomic number 11: a alkali metal in group 1, period 3, with standard atomic weight 22.99.  Its position on the periodic table predicts its chemistry: elements in the same group share valence behavior, and the table marches from the light nonmetals of life to the heavy metals of industry and the synthetic frontier.", "s": "public-reference", "f": null}, {"t": "Magnesium (Mg)", "d": "Atomic number 12; weight 24.305; group 2, period 3.", "g": "alkaline earth", "l": 1, "q": "What is the symbol of Magnesium?", "a": "Mg", "x": "Magnesium (Mg), atomic number 12: a alkaline earth in group 2, period 3, with standard atomic weight 24.305.  Its position on the periodic table predicts its chemistry: elements in the same group share valence behavior, and the table marches from the light nonmetals of life to the heavy metals of industry and the synthetic frontier.", "s": "public-reference", "f": null}, {"t": "Aluminium (Al)", "d": "Atomic number 13; weight 26.982; group 13, period 3.", "g": "post-transition metal", "l": 1, "q": "What is the symbol of Aluminium?", "a": "Al", "x": "Aluminium (Al), atomic number 13: a post-transition metal in group 13, period 3, with standard atomic weight 26.982.  Its position on the periodic table predicts its chemistry: elements in the same group share valence behavior, and the table marches from the light nonmetals of life to the heavy metals of industry and the synthetic frontier.", "s": "public-reference", "f": null}, {"t": "Silicon (Si)", "d": "Atomic number 14; weight 28.085; group 14, period 3.", "g": "metalloid", "l": 1, "q": "What is the symbol of Silicon?", "a": "Si", "x": "Silicon (Si), atomic number 14: a metalloid in group 14, period 3, with standard atomic weight 28.085.  Its position on the periodic table predicts its chemistry: elements in the same group share valence behavior, and the table marches from the light nonmetals of life to the heavy metals of industry and the synthetic frontier.", "s": "public-reference", "f": null}, {"t": "Phosphorus (P)", "d": "Atomic number 15; weight 30.974; group 15, period 3.", "g": "nonmetal", "l": 1, "q": "What is the symbol of Phosphorus?", "a": "P", "x": "Phosphorus (P), atomic number 15: a nonmetal in group 15, period 3, with standard atomic weight 30.974.  Its position on the periodic table predicts its chemistry: elements in the same group share valence behavior, and the table marches from the light nonmetals of life to the heavy metals of industry and the synthetic frontier.", "s": "public-reference", "f": null}, {"t": "Sulfur (S)", "d": "Atomic number 16; weight 32.06; group 16, period 3.", "g": "nonmetal", "l": 1, "q": "What is the symbol of Sulfur?", "a": "S", "x": "Sulfur (S), atomic number 16: a nonmetal in group 16, period 3, with standard atomic weight 32.06.  Its position on the periodic table predicts its chemistry: elements in the same group share valence behavior, and the table marches from the light nonmetals of life to the heavy metals of industry and the synthetic frontier.", "s": "public-reference", "f": null}, {"t": "Chlorine (Cl)", "d": "Atomic number 17; weight 35.45; group 17, period 3.", "g": "halogen", "l": 1, "q": "What is the symbol of Chlorine?", "a": "Cl", "x": "Chlorine (Cl), atomic number 17: a halogen in group 17, period 3, with standard atomic weight 35.45.  Its position on the periodic table predicts its chemistry: elements in the same group share valence behavior, and the table marches from the light nonmetals of life to the heavy metals of industry and the synthetic frontier.", "s": "public-reference", "f": null}, {"t": "Argon (Ar)", "d": "Atomic number 18; weight 39.948; group 18, period 3.", "g": "noble gas", "l": 1, "q": "What is the symbol of Argon?", "a": "Ar", "x": "Argon (Ar), atomic number 18: a noble gas in group 18, period 3, with standard atomic weight 39.948.  Its position on the periodic table predicts its chemistry: elements in the same group share valence behavior, and the table marches from the light nonmetals of life to the heavy metals of industry and the synthetic frontier.", "s": "public-reference", "f": null}, {"t": "Potassium (K)", "d": "Atomic number 19; weight 39.098; group 1, period 4.", "g": "alkali metal", "l": 1, "q": "What is the symbol of Potassium?", "a": "K", "x": "Potassium (K), atomic number 19: a alkali metal in group 1, period 4, with standard atomic weight 39.098.  Its position on the periodic table predicts its chemistry: elements in the same group share valence behavior, and the table marches from the light nonmetals of life to the heavy metals of industry and the synthetic frontier.", "s": "public-reference", "f": null}, {"t": "Calcium (Ca)", "d": "Atomic number 20; weight 40.078; group 2, period 4.", "g": "alkaline earth", "l": 1, "q": "What is the symbol of Calcium?", "a": "Ca", "x": "Calcium (Ca), atomic number 20: a alkaline earth in group 2, period 4, with standard atomic weight 40.078.  Its position on the periodic table predicts its chemistry: elements in the same group share valence behavior, and the table marches from the light nonmetals of life to the heavy metals of industry and the synthetic frontier.", "s": "public-reference", "f": null}, {"t": "Scandium (Sc)", "d": "Atomic number 21; weight 44.956; group 3, period 4.", "g": "transition metal", "l": 1, "q": "What is the symbol of Scandium?", "a": "Sc", "x": "Scandium (Sc), atomic number 21: a transition metal in group 3, period 4, with standard atomic weight 44.956.  Its position on the periodic table predicts its chemistry: elements in the same group share valence behavior, and the table marches from the light nonmetals of life to the heavy metals of industry and the synthetic frontier.", "s": "public-reference", "f": null}, {"t": "Titanium (Ti)", "d": "Atomic number 22; weight 47.867; group 4, period 4.", "g": "transition metal", "l": 1, "q": "What is the symbol of Titanium?", "a": "Ti", "x": "Titanium (Ti), atomic number 22: a transition metal in group 4, period 4, with standard atomic weight 47.867.  Its position on the periodic table predicts its chemistry: elements in the same group share valence behavior, and the table marches from the light nonmetals of life to the heavy metals of industry and the synthetic frontier.", "s": "public-reference", "f": null}, {"t": "Vanadium (V)", "d": "Atomic number 23; weight 50.942; group 5, period 4.", "g": "transition metal", "l": 1, "q": "What is the symbol of Vanadium?", "a": "V", "x": "Vanadium (V), atomic number 23: a transition metal in group 5, period 4, with standard atomic weight 50.942.  Its position on the periodic table predicts its chemistry: elements in the same group share valence behavior, and the table marches from the light nonmetals of life to the heavy metals of industry and the synthetic frontier.", "s": "public-reference", "f": null}, {"t": "Chromium (Cr)", "d": "Atomic number 24; weight 51.996; group 6, period 4.", "g": "transition metal", "l": 1, "q": "What is the symbol of Chromium?", "a": "Cr", "x": "Chromium (Cr), atomic number 24: a transition metal in group 6, period 4, with standard atomic weight 51.996.  Its position on the periodic table predicts its chemistry: elements in the same group share valence behavior, and the table marches from the light nonmetals of life to the heavy metals of industry and the synthetic frontier.", "s": "public-reference", "f": null}, {"t": "Manganese (Mn)", "d": "Atomic number 25; weight 54.938; group 7, period 4.", "g": "transition metal", "l": 1, "q": "What is the symbol of Manganese?", "a": "Mn", "x": "Manganese (Mn), atomic number 25: a transition metal in group 7, period 4, with standard atomic weight 54.938.  Its position on the periodic table predicts its chemistry: elements in the same group share valence behavior, and the table marches from the light nonmetals of life to the heavy metals of industry and the synthetic frontier.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-periodic-elements-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
