(function(){'use strict';
/* JAH The Factory Blueprint Database generator — jahdb-blueprint-factories-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BFP-";
var FIELDS=["Food / Beverage","Heavy Industry","Light Industry"];
var TOPICS={
 "Food / Beverage": [
  "Food Processing Plant - Compact Architectural Blueprint - Food / Beverage",
  "Brewery - Compact Architectural Blueprint - Food / Beverage",
  "Food Processing Plant - Standard Architectural Blueprint - Food / Beverage",
  "Brewery - Standard Architectural Blueprint - Food / Beverage",
  "Food Processing Plant - Grand Architectural Blueprint - Food / Beverage",
  "Brewery - Grand Architectural Blueprint - Food / Beverage"
 ],
 "Heavy Industry": [
  "Assembly Plant - Compact Architectural Blueprint - Heavy Industry",
  "Steel Fabrication Shop - Compact Architectural Blueprint - Heavy Industry",
  "Paper Mill - Compact Architectural Blueprint - Heavy Industry",
  "Auto Assembly Plant - Compact Architectural Blueprint - Heavy Industry",
  "Chemical Processing Plant - Compact Architectural Blueprint - Heavy Industry",
  "Assembly Plant - Standard Architectural Blueprint - Heavy Industry",
  "Steel Fabrication Shop - Standard Architectural Blueprint - Heavy Industry",
  "Paper Mill - Standard Architectural Blueprint - Heavy Industry",
  "Auto Assembly Plant - Standard Architectural Blueprint - Heavy Industry",
  "Chemical Processing Plant - Standard Architectural Blueprint - Heavy Industry",
  "Assembly Plant - Grand Architectural Blueprint - Heavy Industry",
  "Steel Fabrication Shop - Grand Architectural Blueprint - Heavy Industry",
  "Paper Mill - Grand Architectural Blueprint - Heavy Industry",
  "Auto Assembly Plant - Grand Architectural Blueprint - Heavy Industry",
  "Chemical Processing Plant - Grand Architectural Blueprint - Heavy Industry"
 ],
 "Light Industry": [
  "Textile Mill - Compact Architectural Blueprint - Light Industry",
  "Electronics Assembly Plant - Compact Architectural Blueprint - Light Industry",
  "Furniture Factory - Compact Architectural Blueprint - Light Industry",
  "Print Shop Factory - Compact Architectural Blueprint - Light Industry",
  "Packaging Plant - Compact Architectural Blueprint - Light Industry",
  "Textile Mill - Standard Architectural Blueprint - Light Industry",
  "Electronics Assembly Plant - Standard Architectural Blueprint - Light Industry",
  "Furniture Factory - Standard Architectural Blueprint - Light Industry",
  "Print Shop Factory - Standard Architectural Blueprint - Light Industry",
  "Packaging Plant - Standard Architectural Blueprint - Light Industry",
  "Textile Mill - Grand Architectural Blueprint - Light Industry",
  "Electronics Assembly Plant - Grand Architectural Blueprint - Light Industry",
  "Furniture Factory - Grand Architectural Blueprint - Light Industry"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Factories Blueprint Study — "+safe+"\n"
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
    name:topic+' — factory blueprint record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A factory blueprint record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"blueprint-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-blueprint-factories-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('blueprint-factories',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
