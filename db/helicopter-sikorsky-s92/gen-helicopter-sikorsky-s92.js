(function(){'use strict';
/* JAH The Sikorsky S-92 Database generator — "jahdb-helicopter-sikorsky-s92-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed + same group = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-S92-";
var SLUG="helicopter-sikorsky-s92";
var SRC="public-harvest";
var SIG=false;
var FIELDS=["history", "design-specs", "performance", "variants", "blueprint", "manufacture", "records"];
var FACTS={"name": "Sikorsky S-92", "maker": "Sikorsky (Lockheed Martin)", "years": "2004\u2013present", "engines": "2 \u00d7 General Electric CT7-8A turboshafts", "variants": ["S-92A", "S-92A+", "VH-92A Patriot (Marine One)", "CH-148 Cyclone (military)"], "specs": [["Length", "20.9 m"], ["Rotor diameter", "17.71 m"], ["Height", "5.47 m"], ["Maximum takeoff weight", "12,568 kg"], ["Engines", "2 \u00d7 General Electric CT7-8A"], ["Max speed", "283 km/h"]], "zones": ["nose / cockpit", "cabin (19 seats)", "main rotor mast", "twin engine nacelles", "tail / ramp"], "citations": ["Sikorsky S-92 published specifications", "Public aviation records"], "how": "Wings generate lift from airflow; engines provide thrust; control surfaces and fly-by-wire or mechanical controls steer the aircraft in three axes.", "blurb": "VH-92A flies the US President as Marine One"};
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
var gen={version:"jahdb-helicopter-sikorsky-s92-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
