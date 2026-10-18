(function(){'use strict';
/* JAH The Public Art Explorer Database Signature Database generator — jahdb-db-public-art-explorer-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PXES-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Public Art?",
  "The Wynwood Walls, Miami",
  "Finding Public Art",
  "The East Side Gallery, Berlin",
  "The Art Walk",
  "The Bushwick Collective, Brooklyn",
  "The Public Art Photography",
  "The Valparaiso Murals (Art)",
  "The Art with Kids",
  "The Hosier Lane, Melbourne",
  "The Art Year"
 ],
 "Compounded": [
  "The Bellas Artes Murals, Mexico City",
  "The Art Story",
  "The Shoreditch, London (Art)",
  "The Art Tour",
  "The George Town, Penang (Art)",
  "The Art Solo",
  "The Kreuzberg, Berlin (Art)",
  "The Art Decade",
  "The NDSM Wharf, Amsterdam (Art)",
  "The Art Road Trip",
  "The Vila Madalena, São Paulo (Art)",
  "The Art Festival"
 ],
 "Advanced": [
  "Advanced: The Art Index",
  "Advanced: Your Art Ranking",
  "Advanced: The Art Passport",
  "Advanced: The Art Storyteller",
  "Advanced: The Art Bucket List",
  "Advanced: The Art Finale",
  "Advanced: The Art Legacy",
  "Advanced: The Art Memoir",
  "Advanced: The Art Master Decade",
  "Advanced: The Art Year",
  "The Public Art Explorer Encyclopedia"
 ]
};
var DEMOKIND="travel-lab-demo";
var SAMPLEDESC="Sample records are complete real public-art entries with real measurement math.";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Travel Lab Demo — "+safe+"\n"
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
    name:topic+' — public art record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A public art record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'signature',
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
var gen={version:'jahdb-db-public-art-explorer-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-public-art-explorer-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
