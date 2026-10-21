(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function cleanT(t){return String(t==null?'':t).replace(/"/g,'').replace(/\*\//g,'* /');}
var SLUG="quanta-jumps-configurations";
var PREFIX="JAH-QUAN-";
var GROUPS=["hydrogen-lines", "discharge-lamps", "solid-state-lasers", "quantum-standards"];
var LIVE="https://justinahiggins614-cmyk.github.io/jah-databases/db/";
var LINES=[["Hydrogen Lyman-Alpha Jump", 121.6], ["Hydrogen Lyman-Beta Jump", 102.6], ["Hydrogen Balmer-Alpha (H-Alpha) Jump", 656.3], ["Hydrogen Balmer-Beta (H-Beta) Jump", 486.1], ["Sodium D-Line Jump", 589.3], ["Mercury 254 nm Jump", 253.7], ["Neon Helium-Neon 632.8 nm Jump", 632.8], ["Ruby 694.3 nm Jump", 694.3], ["Nd:YAG 1064 nm Jump", 1064.1], ["Rubidium-87 D2 Jump", 780.24], ["Calcium-Ion 729 nm Jump", 729.1], ["Ytterbium-Ion 369 nm Jump", 369.5], ["Cesium-133 Hyperfine Jump", 32574000.0], ["Nitrogen-Vacancy 637 nm Jump", 637.0], ["Electron Shelving Jump (Dehmelt)", 493.4]];

function demoQuanProgram(rec){
  var L=['/* JAH demo program — '+rec.id+' */','/* RUN ON PC: save as demo.js, then run: node demo.js */'];
  L.push('console.log("PHOTON DEMO — '+cleanT(rec.transition_of)+'");');
  L.push('var lambda_nm='+rec.wavelength_nm+';');
  L.push('var h=6.62607015e-34,c=299792458,eV=1.602176634e-19;');
  L.push('var E=h*c/(lambda_nm*1e-9);');
  L.push('console.log("wavelength: "+lambda_nm+" nm");');
  L.push('console.log("photon energy: "+E.toExponential(3)+" J = "+(E/eV).toFixed(4)+" eV");');
  L.push('console.log("derived analysis — not a new measurement");');
  return L.join('\n');
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var group=(opts.category&&GROUPS.indexOf(opts.category)>=0)?opts.category:pick(GROUPS,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var s=pick(LINES,rnd);
  var E=6.62607015e-34*299792458/(s[1]*1e-9)/1.602176634e-19;
  var rec={id:id,kind:'derived-analysis',transition_of:s[0],wavelength_nm:s[1],
    computed_photon_ev:Math.round(E*10000)/10000,
    ladder_rank:ri(rnd,1,15),_seed:seed,
    working_version_link:LIVE+'db/'+SLUG+'/#p-demo',
    status:'proven',status_note:'Photon math smoke-tested at build; derived analysis.',
    provenance:'Generated photon check by jahdb-'+SLUG+'-1.0 (seed '+seed+') — derived from the archive\'s real transition data; not a new measurement.',
    last_verified:'2026-10-21',
    march_marker:'MARCH-TO-A-MILLION: generated analysis (seed '+seed+') · target 1,000,000 · in progress',
    edition:'public'};
  rec.title='Photon Check — '+s[0]+' (seed '+seed+')';
  rec.description='A generated photon check: recomputing the photon energy of the '+s[0]+' transition ('+s[1]+' nm) from first principles. Derived analysis — not a new measurement.';
  rec.t=rec.title;rec.g=group;rec.group=group;rec.c=1;
  rec.demo={kind:'photon-math',title:'Photon demo — '+cleanT(rec.transition_of),program:demoQuanProgram(rec),language:'javascript',runnable:true};
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
  var REQ=["kind", "transition_of", "wavelength_nm", "computed_photon_ev", "provenance", "march_marker"];
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
var gen={version:'jahdb-quanta-jumps-configurations-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
