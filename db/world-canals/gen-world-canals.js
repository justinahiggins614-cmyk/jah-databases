(function(){'use strict';
/* JAH World Canals Database generator — jahdb-world-canals-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WCWO-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Canals Are",
  "The Panama Canal: Locks and Transit",
  "The Suez Canal",
  "The Grand Canal of China",
  "The Erie Canal",
  "The Kiel Canal",
  "The Corinth Canal",
  "How Locks Work",
  "The Manchester Ship Canal",
  "Canal Boats",
  "The Bridgewater Canal"
 ],
 "Compounded": [
  "The Welland Canal",
  "The Saint Lawrence Seaway",
  "The Volga-Don Canal",
  "The White Sea-Baltic Canal",
  "The Danube-Black Sea Canal",
  "The Mittellandkanal",
  "The Rhine-Main-Danube Canal",
  "The Canal du Midi",
  "The Caledonian Canal",
  "The Kennet and Avon Canal",
  "The Rideau Canal",
  "The Shubenacadie Canal"
 ],
 "Advanced": [
  "Canal Engineering",
  "Lock Design",
  "The Panama Expansion",
  "The Suez Ever Given Lesson",
  "Canal Economics",
  "Canal Ecology",
  "Restoring Historic Canals",
  "Ship Lifts",
  "The Future of Canals",
  "Proposed New Canals",
  "Canal Heritage"
 ]
};
var DEMOKIND="canal analyzer";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Canal transit calculator — "+safe+"\n"
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
    name:topic+' — canal record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A canal record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-world-canals-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('world-canals',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
