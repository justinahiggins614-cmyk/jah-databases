(function(){'use strict';
/* JAH The Reusable Interplanetary Spacecraft (Starship Class) Database generator — jahdb-tech-154-reusable-interplanetary-spacecraft-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET154-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["What Reusable Interplanetary Spacecraft (Starship Class) Is","Current Research State of Reusable Interplanetary Spacecraft (Starship Class)","Key Technical Specifications of Reusable Interplanetary Spacecraft (Starship Class)","Key Public Developments in Reusable Interplanetary Spacecraft (Starship Class)","Challenges and Open Problems in Reusable Interplanetary Spacecraft (Starship Class)"],"Compounded": ["Super Heavy Booster","Starship Upper Stage","Raptor Engine","Orbital Refueling","Heat Shield","Life Support","Lunar Variant"],"Advanced": ["Mars Architecture","Launch Cadence","Point-to-Point","Satellite Deployment","Manufacturing","Regulatory Path","Deep-Space Variant","Crew Training"]};
var DEMOKIND="reusable interplanetary spacecraft record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# reusable interplanetary spacecraft record planner — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — reusable interplanetary spacecraft record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A reusable interplanetary spacecraft record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:DEMOKIND,language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-tech-154-reusable-interplanetary-spacecraft-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-154-reusable-interplanetary-spacecraft',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
