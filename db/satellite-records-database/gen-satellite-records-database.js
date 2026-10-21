(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function cleanT(t){return String(t==null?'':t).replace(/"/g,'').replace(/\*\//g,'* /');}
var SLUG="satellite-records-database";
var PREFIX="JAH-SATL-";
var GROUPS=["early-space-age", "communications", "earth-science", "deep-space", "modern-era"];
var LIVE="https://justinahiggins614-cmyk.github.io/jah-databases/db/";
var SATS=[["Sputnik 1", "1957-001B", "1957-10-04", 577, 0, "LEO", 0], ["Sputnik 2", "1957-002A", "1957-11-03", 900, 0, "LEO", 0], ["Explorer 1", "1958-001A", "1958-02-01", 1000, 0, "LEO", 0], ["Vanguard 1", "1958-002B", "1958-03-17", 2300, 0, "LEO", 0], ["Echo 1", "1960-009A", "1960-08-12", 1600, 0, "LEO", 0], ["Telstar 1", "1962-029A", "1962-07-10", 3300, 0, "MEO", 0], ["Syncom 3", "1964-047A", "1964-08-19", 35786, 0, "GEO", 0], ["Landsat 1 (ERTS-1)", "1972-058A", "1972-07-23", 907, 0, "SSO (LEO)", 0], ["Voyager 1", "1977-084A", "1977-09-05", 0, 1, "Heliocentric escape", 24900000000], ["Hubble Space Telescope", "1990-037B", "1990-04-24", 540, 0, "LEO", 0], ["International Space Station", "1998-067A", "1998-11-20", 420, 0, "LEO", 0], ["Iridium 33", "1997-051C", "1997-09-14", 776, 0, "LEO", 0], ["Envisat", "2002-009A", "2002-03-01", 790, 0, "SSO (LEO)", 0], ["Kepler Space Telescope", "2009-011A", "2009-03-07", 0, 1, "Heliocentric (Earth-trailing)", 26000000], ["GOES-16", "2016-071A", "2016-11-19", 35786, 0, "GEO", 0]];

function demoSatProgram(rec){
  var L=['/* JAH demo program — '+rec.id+' */','/* RUN ON PC: save as demo.js, then run: node demo.js */'];
  L.push('console.log("ORBIT DEMO — '+cleanT(rec.analysis_of)+' ('+rec.cospar_id+')");');
  if(rec.alt_km!==undefined&&rec.alt_km!==null){
    L.push('var mu=398600.4418,alt='+rec.alt_km+',a=6371+alt;');
    L.push('var T=2*Math.PI*Math.sqrt(Math.pow(a,3)/mu);');
    L.push('console.log("mean altitude: "+alt+" km");');
    L.push('console.log("orbital period: "+(T/60).toFixed(2)+" minutes ("+(T/3600).toFixed(2)+" hours)");');
  }else{
    L.push('var dist='+rec.distance_km+',c=299792.458,lt=dist/c;');
    L.push('console.log("distance from Earth: ~"+(dist/1e9).toFixed(2)+" billion km");');
    L.push('console.log("one-way light time: "+(lt/3600).toFixed(2)+" hours");');
  }
  L.push('console.log("derived analysis — not a new satellite record");');
  return L.join('\n');
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var group=(opts.category&&GROUPS.indexOf(opts.category)>=0)?opts.category:pick(GROUPS,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var s=pick(SATS,rnd);
  var rec={id:id,kind:'derived-analysis',analysis_of:s[0],cospar_id:s[1],launch_date:s[2],orbit_type:s[5],
    ladder_rank:ri(rnd,1,15),_seed:seed,
    working_version_link:LIVE+'db/'+SLUG+'/#p-demo',
    status:'proven',status_note:'Orbit math smoke-tested at build; derived analysis.',
    provenance:'Generated orbit analysis by jahdb-'+SLUG+'-1.0 (seed '+seed+') — derived from the archive\'s real satellite records; not a new satellite.',
    last_verified:'2026-10-21',
    march_marker:'MARCH-TO-A-MILLION: generated analysis (seed '+seed+') · target 1,000,000 · in progress',
    edition:'public'};
  if(s[4]===0){
    var a=6371+s[3],T=2*Math.PI*Math.sqrt(Math.pow(a,3)/398600.4418);
    rec.alt_km=s[3];rec.computed_period_min=Math.round(T/60*100)/100;
    rec.title='Orbit Analysis — '+s[0]+' (seed '+seed+')';
    rec.description='A generated orbit analysis: recomputing the orbital period of '+s[0]+' ('+s[1]+', launched '+s[2]+') from its mean altitude with Kepler\'s third law. Derived analysis — not a new satellite record.';
  }else{
    var lt=s[6]/299792.458;
    rec.distance_km=s[6];rec.computed_light_hours=Math.round(lt/3600*100)/100;
    rec.title='Distance Analysis — '+s[0]+' (seed '+seed+')';
    rec.description='A generated distance analysis: one-way light time to '+s[0]+' ('+s[1]+') from its approximate distance. Derived analysis — not a new satellite record.';
  }
  rec.t=rec.title;rec.g=group;rec.group=group;rec.c=1;
  rec.demo={kind:'orbit-math',title:'Orbit math demo — '+cleanT(rec.title),program:demoSatProgram(rec),language:'javascript',runnable:true};
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
  var REQ=["kind", "analysis_of", "cospar_id", "orbit_type", "provenance", "march_marker"];
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
var gen={version:'jahdb-satellite-records-database-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
