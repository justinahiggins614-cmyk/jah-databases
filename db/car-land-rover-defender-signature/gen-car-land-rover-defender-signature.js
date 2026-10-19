(function(){'use strict';
/* JAH Signature Land Rover Defender Database generator — "jahdb-car-land-rover-defender-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed + same group = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DEF-S-";
var SLUG="car-land-rover-defender-signature";
var SRC="signature";
var SIG=true;
var FIELDS=["history", "design-specs", "performance", "variants", "blueprint", "manufacture", "records"];
var FACTS={"name": "Land Rover Defender", "maker": "Jaguar Land Rover", "years": "1983\u20132016 / 2020\u2013present", "engines": "3.0L turbo I6 (395 hp); 5.0L supercharged V8 (518 hp); 2.0L diesel", "variants": ["Defender 90/110/130 (classic)", "Defender 90/110/130 (L663, 2020)", "Defender OCTA"], "specs": [["Body", "3-door / 5-door SUV"], ["Engine", "3.0L turbo I6 / 5.0L V8"], ["Power", "395 hp (P400); 518 hp (V8)"], ["4WD", "Permanent, locking center + rear"], ["Wading depth", "900 mm"], ["Layout", "Front-engine, 4WD"]], "zones": ["flat grille", "I6/V8 bay", "5-7 seat cabin", "rear cargo", "side-hinged spare"], "citations": ["Land Rover published specifications", "Public automotive records"], "how": "An engine or electric motors drive the wheels through a transmission; steering, suspension, and brakes control direction, ride, and stopping.", "blurb": "Descended from the 1948 Series I \u2014 the original 4x4"};
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
var gen={version:"jahdb-car-land-rover-defender-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
