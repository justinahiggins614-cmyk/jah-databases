(function(){'use strict';
/* JAH The Thrift Store Treasure Database generator — jahdb-db-thrift-store-treasure-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TSTT-";
var FIELDS=["Thrift Foundations", "Treasure Hunting", "Thrift Mastery"];
var TOPICS={"Thrift Foundations": ["Why Thrift", "Know Your Stores", "The Thrift Kit", "Fabric First", "The Quality Scan", "Sizing Across Eras", "Stain Triage", "The Smell Test", "Price Intelligence", "Fitting Room Strategy", "The Wash-First Rule"], "Treasure Hunting": ["The Wool Hunt", "Leather Finds", "Silk Scores", "Denim Gold", "Designer Spotting", "The Suit Hunt", "Vintage Tees", "Cashmere Dreams", "The Linen Look", "Costume and Vintage Formal", "Kids Thrift Wins", "Flipping Finds"], "Thrift Mastery": ["The Revival Workshop", "Tailoring Thrift Finds", "The Estate Sale Edge", "Online Thrifting", "The Collection Build", "Sustainable Thrifting", "Teaching Thrifting", "The Thrift Community", "Upcycling Mastery", "The Lifetime Thrift Wardrobe", "Giving Back the Finds"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# minibot — "+safe+"\n"
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
    name:topic+' — thrift treasure record',
    title:topic,
    description:"SAMPLE RECORD (generated — structural sample). A thrift treasure record of \""+topic+"\" in "+field+". Generated samples are clearly labeled and never presented as archive records.",
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"topic-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-db-thrift-store-treasure-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("db-thrift-store-treasure",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
