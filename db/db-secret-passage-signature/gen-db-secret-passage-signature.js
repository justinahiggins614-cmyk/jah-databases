(function(){'use strict';
/* JAH The Secret Passage Signature Database generator — jahdb-db-secret-passage-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MSPDS-";
var FIELDS=["Houses","Public Buildings","Underground"];
var TOPICS={
 "Houses": [
  "The Bookcase Door (Signature Edition) \u2014 Houses",
  "The Signature Method for The Bookcase Door \u2014 Houses",
  "The Fireplace Passage (Signature Edition) \u2014 Houses",
  "The Signature Method for The Fireplace Passage \u2014 Houses",
  "The Staircase Within (Signature Edition) \u2014 Houses",
  "The Signature Method for The Staircase Within \u2014 Houses",
  "The Lighthouse Cellar (Signature Edition) \u2014 Houses",
  "The Signature Method for The Lighthouse Cellar \u2014 Houses",
  "The Cottage Loft (Signature Edition) \u2014 Houses",
  "The Signature Method for The Cottage Loft \u2014 Houses",
  "The Garden Grotto (Signature Edition) \u2014 Houses",
  "The Signature Method for The Garden Grotto \u2014 Houses",
  "The Architect's Notebook (Signature Edition) \u2014 Houses",
  "The Signature Method for The Architect's Notebook \u2014 Houses"
 ],
 "Public Buildings": [
  "The Pulpit Passage (Signature Edition) \u2014 Public Buildings",
  "The Signature Method for The Pulpit Passage \u2014 Public Buildings",
  "The Vault's Second Door (Signature Edition) \u2014 Public Buildings",
  "The Signature Method for The Vault's Second Door \u2014 Public Buildings",
  "The Theater's Ghost Box (Signature Edition) \u2014 Public Buildings",
  "The Signature Method for The Theater's Ghost Box \u2014 Public Buildings",
  "The Observatory Floor (Signature Edition) \u2014 Public Buildings",
  "The Signature Method for The Observatory Floor \u2014 Public Buildings",
  "The Hotel's Service Spine (Signature Edition) \u2014 Public Buildings",
  "The Signature Method for The Hotel's Service Spine \u2014 Public Buildings",
  "The Town Hall Vault (Signature Edition) \u2014 Public Buildings",
  "The Signature Method for The Town Hall Vault \u2014 Public Buildings",
  "The Station's Lost Platform (Signature Edition) \u2014 Public Buildings",
  "The Signature Method for The Station's Lost Platform \u2014 Public Buildings"
 ],
 "Underground": [
  "The Well Stair (Signature Edition) \u2014 Underground",
  "The Signature Method for The Well Stair \u2014 Underground",
  "The Tunnel Network (Signature Edition) \u2014 Underground",
  "The Signature Method for The Tunnel Network \u2014 Underground",
  "The Mill's Wheel Pit (Signature Edition) \u2014 Underground",
  "The Signature Method for The Mill's Wheel Pit \u2014 Underground"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Secret Passage Study — "+safe+"\n"
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
    name:topic+' — secret passage record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A secret passage record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-secret-passage-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-secret-passage-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
