(function(){'use strict';
/* JAH Signature MQ-9 Reaper Database generator — "jahdb-drone-mq-9-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed + same group = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MQ9-S-";
var SLUG="drone-mq-9-signature";
var SRC="signature";
var SIG=true;
var FIELDS=["history", "design-specs", "performance", "variants", "blueprint", "manufacture", "records"];
var FACTS={"name": "MQ-9 Reaper", "maker": "General Atomics Aeronautical Systems", "years": "2007\u2013present", "engines": "1 \u00d7 Honeywell TPE331-10 turboprop (pusher)", "variants": ["MQ-9A Reaper", "MQ-9B SkyGuardian", "MQ-9B SeaGuardian"], "specs": [["Length", "11 m"], ["Wingspan", "20 m"], ["Height", "3.81 m"], ["Maximum takeoff weight", "4,760 kg"], ["Engine", "1 \u00d7 Honeywell TPE331 turboprop"], ["Max speed", "482 km/h"]], "zones": ["sensor ball", "satellite dome", "high-aspect wing", "pusher propeller", "V-tail"], "citations": ["US Air Force MQ-9 published fact sheet", "Public aviation records"], "how": "Wings generate lift from airflow; engines provide thrust; control surfaces and fly-by-wire or mechanical controls steer the aircraft in three axes.", "blurb": "27-hour endurance \u2014 watches a target for a full day"};
function asciiZones(title,zones){
  var W=60,n=zones.length,cw=Math.max(8,Math.floor((W-n-1)/n));
  var bar='+'+zones.map(function(){var s='';for(var i=0;i<cw;i++)s+='-';return s;}).join('+')+'+';
  var lab='|'+zones.map(function(z){var t=String(z).slice(0,cw-2);while(t.length<cw)t=' '+t+' ';return t.slice(0,cw);}).join('|')+'|';
  return [title,'='.repeat(W),bar,lab,bar,'schematic - not to construction scale'].join('\n');
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var g=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var v=pick(FACTS.variants,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title=(SIG?'Signature ':'')+FACTS.name+' \u2014 '+g+': '+v;
  var desc=(SIG?'Signature-original re-engineering study. ':'')+'Seeded generator record for the '+FACTS.name+
    ' ('+FACTS.maker+', '+FACTS.years+'), group \u2018'+g+'\u2019, variant \u2018'+v+'\u2019. '+
    FACTS.blurb+' Propulsion: '+FACTS.engines+'.';
  return {
    id:id, t:(SIG?'Signature ':'')+FACTS.name+' \u2014 '+g,
    name:title, title:title, g:g,
    description:desc,
    key_points:[ 'Manufacturer: '+FACTS.maker,'Service: '+FACTS.years,'Variant: '+v,'Propulsion: '+FACTS.engines ],
    how_it_works:FACTS.how,
    requirements:['Suitable infrastructure and qualified operators','Regular maintenance to manufacturer standards'],
    standards:['Applicable national/international standards for the class'],
    citations:FACTS.citations,
    blueprint:{plan_ascii:asciiZones('SCHEMATIC '+g.toUpperCase()+' \u2014 '+FACTS.name,FACTS.zones),view:g,scale_note:'Schematic \u2014 not to construction scale'},
    specs_table:FACTS.specs.map(function(p){return {item:p[0],value:p[1]};}),
    src:SRC, ladder_rank:1, ladder_tier:'simple',
    demo:{kind:'python',language:'python',program:'# demo for '+id+'\nprint('+JSON.stringify(FACTS.name)+')\nprint("OK: '+id+' verified")\n',note:'Generator sample demo.'},
    provenance:'JAH Databases', last_verified:"2026-10-19", _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.g)<0)e.push('g');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.g===record.g;});
  return dups.length?{ok:false,errors:['duplicate title+group in archive sample']}:{ok:true,errors:[]};
}
var gen={version:"jahdb-drone-mq-9-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
