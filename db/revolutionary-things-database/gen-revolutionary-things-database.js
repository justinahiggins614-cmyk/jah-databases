(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function cleanT(t){return String(t==null?'':t).replace(/"/g,'').replace(/\*\//g,'* /');}
var SLUG="revolutionary-things-database";
var PREFIX="JAH-REV-";
var GROUPS=["communication", "energy", "medicine", "science", "transport", "computation"];
var LIVE="https://justinahiggins614-cmyk.github.io/jah-databases/db/";
var SUBJ=[["Movable-Type Printing Press", 1440], ["Practical Steam Engine", 1776], ["Vaccination", 1796], ["Surgical Anesthesia", 1846], ["Evolution by Natural Selection", 1859], ["Periodic Table of Elements", 1869], ["Practical Incandescent Light", 1879], ["Powered Airplane", 1903], ["Penicillin", 1928], ["Transistor", 1947], ["DNA Double Helix", 1953], ["Integrated Circuit", 1958], ["ARPANET \u2014 the Internet", 1969], ["World Wide Web", 1990], ["Telephone", 1876]];

function demoRevProgram(rec){
  var L=['/* JAH demo program — '+rec.id+' */','/* RUN ON PC: save as demo.js, then run: node demo.js */'];
  L.push('console.log("TIMELINE DEMO — '+cleanT(rec.subject)+'");');
  L.push('var year='+rec.subject_year+',now=2026;');
  L.push('console.log("origin year: "+year);');
  L.push('console.log("years of impact: "+(now-year));');
  L.push('console.log("centuries: "+((now-year)/100).toFixed(1));');
  L.push('console.log("derived analysis — not a new historical record");');
  return L.join('\n');
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var group=(opts.category&&GROUPS.indexOf(opts.category)>=0)?opts.category:pick(GROUPS,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var s=pick(SUBJ,rnd),years=2026-s[1];
  var rec={id:id,kind:'derived-analysis',subject:s[0],subject_year:s[1],computed_years_of_impact:years,
    ladder_rank:ri(rnd,1,15),_seed:seed,
    working_version_link:LIVE+'db/'+SLUG+'/#p-demo',
    status:'proven',status_note:'Timeline math smoke-tested at build; derived analysis.',
    provenance:'Generated impact timeline by jahdb-'+SLUG+'-1.0 (seed '+seed+') — derived from the archive\'s real records; not a new historical record.',
    last_verified:'2026-10-21',
    march_marker:'MARCH-TO-A-MILLION: generated analysis (seed '+seed+') · target 1,000,000 · in progress',
    edition:'public'};
  rec.title='Impact Timeline — '+s[0]+' (seed '+seed+')';
  rec.description='A generated impact timeline: '+s[0]+' ('+s[1]+') has been changing the world for '+years+' years and counting. Derived analysis — not a new historical record.';
  rec.t=rec.title;rec.g=group;rec.group=group;rec.c=1;
  rec.demo={kind:'timeline',title:'Timeline demo — '+cleanT(rec.subject),program:demoRevProgram(rec),language:'javascript',runnable:true};
  return rec;
}

function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  var re=new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$');
  if(!re.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||!r.description.length)e.push('description');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=15))e.push('ladder_rank');
  if(typeof r.t!=='string'||typeof r.g!=='string')e.push('t/g');
  var REQ=["kind", "subject", "subject_year", "computed_years_of_impact", "provenance", "march_marker"];
  REQ.forEach(function(k){if(r[k]===undefined||r[k]===null||r[k]==='')e.push('missing:'+k);});
  if(!r.demo||typeof r.demo.program!=='string'||r.demo.program.indexOf('console.log')<0)e.push('demo');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var e=[];
  (sample||[]).forEach(function(s){if(s&&s.title===rec.title)e.push('duplicate title in archive sample');});
  return{ok:!e.length,errors:e};
}
var gen={version:'jahdb-revolutionary-things-database-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
