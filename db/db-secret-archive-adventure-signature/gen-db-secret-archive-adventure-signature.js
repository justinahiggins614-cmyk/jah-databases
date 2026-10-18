(function(){'use strict';
/* JAH The Secret Archive Adventure Signature Database generator — jahdb-db-secret-archive-adventure-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MSAAS-";
var FIELDS=["The Boxes","The Letters","The Maps"];
var TOPICS={
 "The Boxes": [
  "Box One: The Captain's Letters (Signature Edition) \u2014 The Boxes",
  "The Signature Method for Box One: The Captain's Letters \u2014 The Boxes",
  "The Photograph Album (Signature Edition) \u2014 The Boxes",
  "The Signature Method for The Photograph Album \u2014 The Boxes",
  "The Menu Collection (Signature Edition) \u2014 The Boxes",
  "The Signature Method for The Menu Collection \u2014 The Boxes",
  "The Ticket Stubs (Signature Edition) \u2014 The Boxes",
  "The Signature Method for The Ticket Stubs \u2014 The Boxes",
  "The Inventory (Signature Edition) \u2014 The Boxes",
  "The Signature Method for The Inventory \u2014 The Boxes",
  "The Seed Catalog (Signature Edition) \u2014 The Boxes",
  "The Signature Method for The Seed Catalog \u2014 The Boxes",
  "The Master Finding Aid (Signature Edition) \u2014 The Boxes",
  "The Signature Method for The Master Finding Aid \u2014 The Boxes"
 ],
 "The Letters": [
  "The Double Ledger (Signature Edition) \u2014 The Letters",
  "The Signature Method for The Double Ledger \u2014 The Letters",
  "The Gardener's Diary (Signature Edition) \u2014 The Letters",
  "The Signature Method for The Gardener's Diary \u2014 The Letters",
  "The Telegram File (Signature Edition) \u2014 The Letters",
  "The Signature Method for The Telegram File \u2014 The Letters",
  "The Recipe Cards (Signature Edition) \u2014 The Letters",
  "The Signature Method for The Recipe Cards \u2014 The Letters",
  "The Postcard Wall (Signature Edition) \u2014 The Letters",
  "The Signature Method for The Postcard Wall \u2014 The Letters"
 ],
 "The Maps": [
  "The Map With No North (Signature Edition) \u2014 The Maps",
  "The Signature Method for The Map With No North \u2014 The Maps",
  "The Blueprint Room (Signature Edition) \u2014 The Maps",
  "The Signature Method for The Blueprint Room \u2014 The Maps",
  "The Star Chart (Signature Edition) \u2014 The Maps",
  "The Signature Method for The Star Chart \u2014 The Maps",
  "The Passport Stamps (Signature Edition) \u2014 The Maps",
  "The Signature Method for The Passport Stamps \u2014 The Maps",
  "The Annotated Atlas (Signature Edition) \u2014 The Maps",
  "The Signature Method for The Annotated Atlas \u2014 The Maps"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Secret Archive Study — "+safe+"\n"
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
    name:topic+' — secret archive record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A secret archive record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-db-secret-archive-adventure-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-secret-archive-adventure-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
