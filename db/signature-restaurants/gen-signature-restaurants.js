(function(){'use strict';
/* JAH Signature Restaurants Database generator — jahdb-signature-restaurants-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-SREST-';
var FIELDS=["signature-concept", "signature-fastfood"];
var TOPICS={
 "signature-concept":["Prime Coordinate Kitchen","The Boundless Buffet","Archive & Ember","Junction Table","The A-.A+ Diner","Mosaic Kitchen","The Chapter House","Quantum Cantina","The Drip Room","Neon Night Market","The Seed Vault","Filing Room Eats","The Generator","Deep Search Deli","The Merger","Paradox Pizza","The Spec Kitchen","Almanac Table","The Phone Book","Genome Grill","The Observatory","Thesaurus Table","The Library","Museum Café","The Dispensary","Surgery Suite","The Compounding Bar","The Poets' Table","The Coin Counter","The Timekeeper"],
 "signature-fastfood":["The Filing Feast","JAH Burger Joint","Trickle Taco","The 39 Stalls","Ember Express","The Daily Drip","Swap Shop Eats","The Red Button","Chapter Bites","The Exhaustive","Polarity Pizza","The Grid","Smoke Signals","The Tasting Tap","The Verse Café","The Vault Deli","The Observatory Express","The Word Wok","The Exhibit Express","The Chronology","The Junction","The Spec Shack","The Almanac","The Directory","The Helix","The Orrery","The Drip Drive-Thru","The Mosaic","The Night Market Express","The Compound"]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/"/g,"'");
  return "# Restaurant Lab — "+safe+"\n"
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
    name:topic+' — restaurant concept study',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A restaurant concept study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'recipe-scaler',language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-signature-restaurants-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('signature-restaurants',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
