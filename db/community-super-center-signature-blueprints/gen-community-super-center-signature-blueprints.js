(function(){'use strict';
/* JAH The Signature Super Center Community Blueprints Database generator — jahdb-community-super-center-signature-blueprints-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SCCB-";
var FIELDS=["street-grid", "buildings", "public-space", "infrastructure"];
var TOPICS={"street-grid": ["The District Grid and Block Template \u2014 street-grid", "The Main Street Cross-Section \u2014 street-grid", "The Residential Street Cross-Section \u2014 street-grid", "The Alley and Service Lane Plan \u2014 street-grid", "The Roundabout and Intersection Plan \u2014 street-grid", "The Transit Stop Blueprint \u2014 street-grid", "The Bike Lane Network Plan \u2014 street-grid", "The Pedestrian Crossing Plan \u2014 street-grid", "The Parking Court Layout \u2014 street-grid"], "buildings": ["The Cottage Housing Prototype \u2014 buildings", "The Townhouse Row Prototype \u2014 buildings", "The Apartment Building Prototype \u2014 buildings", "The Co-Living House Prototype \u2014 buildings", "The Mixed-Use Corner Building Plan \u2014 buildings", "The Market Hall Building Plan \u2014 buildings", "The Clinic Building Plan \u2014 buildings", "The School Building Site Plan \u2014 buildings", "The Library Building Plan \u2014 buildings"], "public-space": ["The Corner Plaza Blueprint \u2014 public-space", "The Pocket Park Plan \u2014 public-space", "The Community Garden Grid \u2014 public-space", "The Playground Blueprint \u2014 public-space", "The Sports Field Layout \u2014 public-space", "The Amphitheater Plan \u2014 public-space", "The Festival Street Section \u2014 public-space", "The Greenway Section Blueprint \u2014 public-space"], "infrastructure": ["The Stormwater Management Plan \u2014 infrastructure", "The Utility Corridor Map \u2014 infrastructure", "The Street Lighting Plan \u2014 infrastructure", "The Tree Planting Plan \u2014 infrastructure", "The Fire Access and Hydrant Plan \u2014 infrastructure", "The Water Distribution Plan \u2014 infrastructure", "The Energy Microgrid Plan \u2014 infrastructure", "The Phased Build-Out Plan \u2014 infrastructure"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# JAH The Signature Super Center Community Blueprints Database \u2014 structural study\n"
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
    description:'SAMPLE RECORD (generated \u2014 structural sample). A structural community blueprint record study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"community-super-center-signature-blueprints-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-community-super-center-signature-blueprints-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('community-super-center-signature-blueprints',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
