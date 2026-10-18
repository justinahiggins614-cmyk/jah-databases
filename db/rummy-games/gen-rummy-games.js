(function(){'use strict';
/* JAH Rummy Card Games Database generator — jahdb-rummy-games-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RUMMY-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["The rummy concept: melds", "Basic Rummy: 500 Rummy rules", "Sets vs runs", "Rummy drawing and discarding", "Going out", "Scoring a hand", "Gin Rummy: rules", "Knocking", "Counting deadwood", "Basic gin strategy", "Rummy table etiquette"], "Compounded": ["Oklahoma Gin", "Canasta: rules", "Canasta melds and going out", "Hand and Foot", "Indian Rummy: 13 cards", "Kalooki", "Conquian: the ancestor", "Carioca", "Buraco", "Tile rummy games", "Continental rummy", "Defensive discarding"], "Advanced": ["Gin advanced: reading hands", "Gin odds and probabilities", "Canasta strategy: freezing the pile", "Tournament gin", "Partnership rummy tactics", "Speed rummy variants", "Scoring variants", "Teaching rummy", "The history of rummy", "Online rummy", "Building a rummy night"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# rummy-meld-demo \u2014 "+safe+"\n"
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
    name:topic+' \u2014 rummy game record',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A rummy game record of \"'+topic+'\" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"rummy-meld-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-rummy-games-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('rummy-games',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
