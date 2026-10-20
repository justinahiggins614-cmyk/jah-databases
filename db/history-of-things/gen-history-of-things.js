(function(){'use strict';
/* JAH The History of Things Database generator — jahdb-history-of-things-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HIST-";
var FIELDS=["Communication", "Everyday Objects", "Home & Energy", "Home & Kitchen", "Play & Games", "Tools & Transport"];
var TOPICS={"Tools & Transport": ["The Wheel", "The Airplane", "The Automobile", "The Bicycle", "The Compass", "The Shipping Container", "The Elevator"], "Everyday Objects": ["Paper", "The Zipper", "The Paperclip", "The Ballpoint Pen", "The Pencil", "Velcro", "The Clock", "Coins and Money", "The Barcode"], "Communication": ["The Printing Press", "The Telephone", "Television", "The Computer", "The Internet", "The Camera", "The Phonograph", "Radio"], "Home & Energy": ["The Light Bulb", "Air Conditioning"], "Home & Kitchen": ["The Microwave Oven", "The Refrigerator", "The Flush Toilet"], "Play & Games": ["The LEGO Brick"]};
var DEMOKIND="timeline printer";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# "+safe+" — "+field+" sample\n"
   + "record = {'topic': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "print('SAMPLE TOPIC: ' + record['topic'])\n"
   + "print('FIELD: ' + record['field'])\n"
   + "print('This is a labeled structural sample, not an archive record.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — history of things record',
    title:topic+' — The History of Things Database',
    description:'SAMPLE RECORD (generated — structural sample). A history of things record sample of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-history-of-things-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('history-of-things',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
