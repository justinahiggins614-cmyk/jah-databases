(function(){'use strict';
/* JAH The Signature Super Center Community Database generator — jahdb-community-super-center-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SCC-";
var FIELDS=["districts", "daily-life", "services", "design"];
var TOPICS={"districts": ["The Market District \u2014 districts", "The Clinic Quarter \u2014 districts", "The School Campus District \u2014 districts", "The Maker Row District \u2014 districts", "The Library Commons \u2014 districts", "The Food Hall Neighborhood \u2014 districts", "The Transit Village \u2014 districts", "The Senior Village \u2014 districts", "The Family Blocks \u2014 districts"], "daily-life": ["The Morning Market Ritual \u2014 daily-life", "The School Run and Safe Routes \u2014 daily-life", "The Lunch Break Commons \u2014 daily-life", "The After-School Workshop Hours \u2014 daily-life", "The Evening Stroll Culture \u2014 daily-life", "The Weekend Festival Rhythm \u2014 daily-life", "The Night Market Season \u2014 daily-life", "The Community Kitchen Nights \u2014 daily-life", "The Volunteer Saturday Tradition \u2014 daily-life"], "services": ["The Health and Wellness Network \u2014 services", "The Childcare Cooperative Network \u2014 services", "The Repair and Reuse District \u2014 services", "The Apprenticeship Row \u2014 services", "The Business Incubator Row \u2014 services", "The Civic Plaza and Town Hall \u2014 services", "The Faith and Gathering Row \u2014 services"], "design": ["The Block and Lot Pattern \u2014 design", "The Street and Sidewalk Standard \u2014 design", "The Housing Mix and Types \u2014 design", "The Courtyard and Pocket Park Pattern \u2014 design", "The Storefront and Signage Code \u2014 design", "The Tree Canopy Plan \u2014 design", "The Front Porch and Fence Pattern \u2014 design", "The Alley and Service Lane Pattern \u2014 design", "The District Gateway Markers \u2014 design"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# JAH The Signature Super Center Community Database \u2014 structural study\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record \u2014 structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' \u2014 structural study record',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A structural community record study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"community-super-center-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-community-super-center-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('community-super-center-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
