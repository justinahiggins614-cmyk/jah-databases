(function(){'use strict';
/* JAH The Signature Super Center Site Plans Database generator — jahdb-super-center-signature-site-plans-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SCSP-";
var FIELDS=["circulation", "grounds", "utilities", "resilience"];
var TOPICS={"circulation": ["The Main Entry Plaza Site Plan \u2014 circulation", "The Traffic Circulation and Parking Plan \u2014 circulation", "The Transit Hub and Bus Loop Plan \u2014 circulation", "The Pedestrian Greenway Site Plan \u2014 circulation", "The Bicycle Network and Bike Hub Plan \u2014 circulation", "The Service Vehicle and Loading Court Plan \u2014 circulation", "The Emergency Vehicle Access Plan \u2014 circulation", "The Delivery Drone Pad Plan \u2014 circulation"], "grounds": ["The Market Square Site Plan \u2014 grounds", "The Amphitheater Lawn Plan \u2014 grounds", "The Community Garden Plots Plan \u2014 grounds", "The Orchard Ring Planting Plan \u2014 grounds", "The Playground and Family Park Plan \u2014 grounds", "The Sports Fields Layout Plan \u2014 grounds", "The Senior Walking Loop Plan \u2014 grounds", "The Dog Park and Pet Zone Plan \u2014 grounds", "The Festival Street Section Plan \u2014 grounds"], "utilities": ["The Water Main and Cistern Plan \u2014 utilities", "The Electrical Service Corridor Plan \u2014 utilities", "The Stormwater Garden Plan \u2014 utilities", "The Solar Canopy Field Plan \u2014 utilities", "The Compost and Waste Center Plan \u2014 utilities", "The Snow Storage and Melt Plan \u2014 utilities", "The Utility Easement Map \u2014 utilities"], "resilience": ["The Emergency Staging Area Plan \u2014 resilience", "The Flood and Drainage Mitigation Plan \u2014 resilience", "The Shade and Heat Relief Plan \u2014 resilience", "The Night Lighting and Safety Plan \u2014 resilience", "The Perimeter Security Plan \u2014 resilience", "The Wildlife Buffer and Wetland Plan \u2014 resilience", "The Noise Buffer Landscape Plan \u2014 resilience", "The Public Art Placement Plan \u2014 resilience", "The Gateway Monument Signage Plan \u2014 resilience", "The Future Expansion Reserve Plan \u2014 resilience"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# JAH The Signature Super Center Site Plans Database \u2014 structural study\n"
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
    description:'SAMPLE RECORD (generated \u2014 structural sample). A structural site plan record study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"super-center-signature-site-plans-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-super-center-signature-site-plans-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('super-center-signature-site-plans',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
