(function(){'use strict';
/* JAH The Missing Object Mystery Signature Database generator — jahdb-db-missing-object-mystery-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MMOMS-";
var FIELDS=["Household Cases","Office Cases","Travel Cases"];
var TOPICS={
 "Household Cases": [
  "The Brass Key (Signature Edition) \u2014 Household Cases",
  "The Signature Method for The Brass Key \u2014 Household Cases",
  "The Wedding Ring (Signature Edition) \u2014 Household Cases",
  "The Signature Method for The Wedding Ring \u2014 Household Cases",
  "The Recipe Box (Signature Edition) \u2014 Household Cases",
  "The Signature Method for The Recipe Box \u2014 Household Cases",
  "The Telescope Lens (Signature Edition) \u2014 Household Cases",
  "The Signature Method for The Telescope Lens \u2014 Household Cases",
  "The Pocket Watch (Inheritance) (Signature Edition) \u2014 Household Cases",
  "The Signature Method for The Pocket Watch (Inheritance) \u2014 Household Cases",
  "The Service Medal (Signature Edition) \u2014 Household Cases",
  "The Signature Method for The Service Medal \u2014 Household Cases",
  "The Violin Bow (Signature Edition) \u2014 Household Cases",
  "The Signature Method for The Violin Bow \u2014 Household Cases"
 ],
 "Office Cases": [
  "The Unsent Letter (Signature Edition) \u2014 Office Cases",
  "The Signature Method for The Unsent Letter \u2014 Office Cases",
  "The Shop Ledger (Signature Edition) \u2014 Office Cases",
  "The Signature Method for The Shop Ledger \u2014 Office Cases",
  "The Rare Stamp (Signature Edition) \u2014 Office Cases",
  "The Signature Method for The Rare Stamp \u2014 Office Cases",
  "The Manuscript Pages (Signature Edition) \u2014 Office Cases",
  "The Signature Method for The Manuscript Pages \u2014 Office Cases",
  "The Signed Contract (Signature Edition) \u2014 Office Cases",
  "The Signature Method for The Signed Contract \u2014 Office Cases"
 ],
 "Travel Cases": [
  "The Camera at the Station (Signature Edition) \u2014 Travel Cases",
  "The Signature Method for The Camera at the Station \u2014 Travel Cases",
  "The Passport (Signature Edition) \u2014 Travel Cases",
  "The Signature Method for The Passport \u2014 Travel Cases",
  "The Red Umbrella (Signature Edition) \u2014 Travel Cases",
  "The Signature Method for The Red Umbrella \u2014 Travel Cases",
  "The Single Glove (Signature Edition) \u2014 Travel Cases",
  "The Signature Method for The Single Glove \u2014 Travel Cases",
  "The Silver Locket (Signature Edition) \u2014 Travel Cases",
  "The Signature Method for The Silver Locket \u2014 Travel Cases"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Missing Object Study — "+safe+"\n"
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
    name:topic+' — missing object mystery record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A missing object mystery record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-db-missing-object-mystery-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-missing-object-mystery-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
