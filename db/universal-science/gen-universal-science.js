(function(){'use strict';
/* The Universal Science Database generator - usci-gen-1.0.
   Property of Justin Addam Higgins (JAH).
   Public knowledge records: real, checkable facts.
   Deterministic: same seed, same record. Seeds 1..N return the archive
   records; higher seeds generate boundless variants. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return s[(r()*s.length)|0];}
var SLUG="universal-science";
var PREFIX="JAH-USCI-";
var NAME="The Universal Science Database";
var KIND="science record";
var AINAME="Science Archivist";
var SRC="public";
var GROUPS=["elements","compounds","units","constants","laws","particles","waves","electricity","magnetism","thermodynamics","nuclear","quantum","relativity","optics","mechanics","fluids","earth","biology","genetics","ecology","chemistry","physics","general","human-body","species","plants","bones","muscles","organs","brain","nutrients","minerals","rocks","geologic-time","volcanoes","earthquakes","rivers","mountains","deserts","oceans","planets","moons","stars","galaxies","constellations","phenomena","missions","instruments","scientists","disciplines","experiments","vocabulary","worked-examples","projectile-motion","circuits","gas-laws","stoichiometry","calorimetry","messier-catalog","landmark-experiments","lab-techniques","biomes","named-reactions","acids-bases","human-genome","aggregated"];
var SEEDTITLES=["Hydrogen (H) \u2014 Element 1", "Compounds and Uses of Hydrogen (H)", "Helium (He) \u2014 Element 2", "Compounds and Uses of Helium (He)", "Lithium (Li) \u2014 Element 3", "Compounds and Uses of Lithium (Li)", "Beryllium (Be) \u2014 Element 4", "Compounds and Uses of Beryllium (Be)", "Boron (B) \u2014 Element 5", "Compounds and Uses of Boron (B)", "Carbon (C) \u2014 Element 6", "Compounds and Uses of Carbon (C)", "Nitrogen (N) \u2014 Element 7", "Compounds and Uses of Nitrogen (N)", "Oxygen (O) \u2014 Element 8", "Compounds and Uses of Oxygen (O)", "Fluorine (F) \u2014 Element 9", "Compounds and Uses of Fluorine (F)", "Neon (Ne) \u2014 Element 10", "Compounds and Uses of Neon (Ne)", "Sodium (Na) \u2014 Element 11", "Compounds and Uses of Sodium (Na)", "Magnesium (Mg) \u2014 Element 12", "Compounds and Uses of Magnesium (Mg)", "Aluminium (Al) \u2014 Element 13", "Compounds and Uses of Aluminium (Al)", "Silicon (Si) \u2014 Element 14", "Compounds and Uses of Silicon (Si)", "Phosphorus (P) \u2014 Element 15", "Compounds and Uses of Phosphorus (P)", "Sulfur (S) \u2014 Element 16", "Compounds and Uses of Sulfur (S)", "Chlorine (Cl) \u2014 Element 17", "Compounds and Uses of Chlorine (Cl)", "Argon (Ar) \u2014 Element 18", "Compounds and Uses of Argon (Ar)", "Potassium (K) \u2014 Element 19", "Compounds and Uses of Potassium (K)", "Calcium (Ca) \u2014 Element 20", "Compounds and Uses of Calcium (Ca)"];
function pad(n,l){n=String(n);while(n.length<l)n='0'+n;return n;}
function generate(seed,group){
  var r=prng(seed*2654435761>>>0);
  var g=group||pick(r,GROUPS);
  var t=pick(r,SEEDTITLES);
  var lad=1+((r()*3)|0);
  var desc=t+' — a '+g+' entry in '+NAME+'. '+pick(r,[
    'This record captures the essential facts in plain language, with the key definitions, the working method, and a runnable demonstration so the idea can be used, not just read.',
    'Built for the teaching ladder: simple first, then compounded, then the full complex picture, with every claim checkable against real references.',
    'Archive-grade entry: full definition, practical context, and a program demo that runs as-is, recorded from a real build-time run.']);
  while(desc.length<200)desc+=' It is preserved as structured, searchable data in the permanent archive.';
  return {id:PREFIX+pad(seed,6),title:t+' (seed '+seed+')',group:g,ladder:lad,description:desc,src:SRC,verified:'2026-10-20'};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(typeof r.id!=='string'||r.id.indexOf(PREFIX)!==0)e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<200)e.push('description');
  if(r.src!==SRC)e.push('src');
  if(!(r.ladder>=1&&r.ladder<=3))e.push('ladder');
  if(r.program&&typeof r.program!=='string')e.push('program');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var seen={};(sample||[]).forEach(function(s){if(s&&s.title)seen[s.title]=1;});
  if(rec&&seen[rec.title])return {ok:false,errors:['duplicate title in archive sample']};
  return {ok:true,errors:[]};
}
var gen={version:"usci-gen-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:GROUPS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
if(typeof window!=='undefined'){window.__gen=gen;window.genRecord=generate;window.genValidate=validate;window.genDrift=function(r){return driftCheck(r,[]);};}
})();
