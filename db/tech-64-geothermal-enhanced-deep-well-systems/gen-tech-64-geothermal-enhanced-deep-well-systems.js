(function(){'use strict';
/* JAH The Geothermal Enhanced Deep-Well Systems Database generator — jahdb-tech-64-geothermal-enhanced-deep-well-systems-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET64-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["What Geothermal Enhanced Deep-Well Systems Is","Current Research State of Geothermal Enhanced Deep-Well Systems","Key Technical Specifications of Geothermal Enhanced Deep-Well Systems","Key Public Developments in Geothermal Enhanced Deep-Well Systems","Challenges and Open Problems in Geothermal Enhanced Deep-Well Systems"],"Compounded": ["Deep Drilling Rig","Reservoir Stimulation System","Fiber-Optic Monitoring","Power Plant Module","Induced Seismicity Protocol","Closed-Loop Well Design","Super-Hot Rock Program"],"Advanced": ["Reservoir Longevity Model","District Heating Network","Lithium Co-Production","Drilling Cost Program","Permitting Reform Pack","Workforce Transition","Global Resource Atlas","Community Partnership"]};
var DEMOKIND="geothermal enhanced deep-well system record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# geothermal enhanced deep-well system record planner — "+safe+"\n"
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
    name:topic+' — geothermal enhanced deep-well system record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A geothermal enhanced deep-well system record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-64-geothermal-enhanced-deep-well-systems-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-64-geothermal-enhanced-deep-well-systems',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
