(function(){'use strict';
/* JAH The Mars Economy Signature Database generator — jahdb-db-mars-economy-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CMED1S-";
var FIELDS=["Resources","Industries","Independence"];
var TOPICS={
 "Resources": [
  "Mars Propellant Production (Signature Edition) \u2014 Resources",
  "The Signature Method for Mars Propellant Production \u2014 Resources",
  "Mars Water Mining (Signature Edition) \u2014 Resources",
  "The Signature Method for Mars Water Mining \u2014 Resources",
  "Mars Construction Materials (Signature Edition) \u2014 Resources",
  "The Signature Method for Mars Construction Materials \u2014 Resources",
  "The Mars Economist's Method (Signature Edition) \u2014 Resources",
  "The Signature Method for The Mars Economist's Method \u2014 Resources"
 ],
 "Industries": [
  "Mars Greenhouse Districts (Signature Edition) \u2014 Industries",
  "The Signature Method for Mars Greenhouse Districts \u2014 Industries",
  "Mars Manufacturing (Signature Edition) \u2014 Industries",
  "The Signature Method for Mars Manufacturing \u2014 Industries",
  "Mars Energy Systems (Signature Edition) \u2014 Industries",
  "The Signature Method for Mars Energy Systems \u2014 Industries",
  "Mars Science Economy (Signature Edition) \u2014 Industries",
  "The Signature Method for Mars Science Economy \u2014 Industries",
  "Mars Tourism (Signature Edition) \u2014 Industries",
  "The Signature Method for Mars Tourism \u2014 Industries",
  "Mars Logistics Corps (Signature Edition) \u2014 Industries",
  "The Signature Method for Mars Logistics Corps \u2014 Industries"
 ],
 "Independence": [
  "Earth-Mars Trade (Signature Edition) \u2014 Independence",
  "The Signature Method for Earth-Mars Trade \u2014 Independence",
  "Mars Currency (Signature Edition) \u2014 Independence",
  "The Signature Method for Mars Currency \u2014 Independence",
  "Mars Governance (Signature Edition) \u2014 Independence",
  "The Signature Method for Mars Governance \u2014 Independence",
  "The Independence Threshold (Signature Edition) \u2014 Independence",
  "The Signature Method for The Independence Threshold \u2014 Independence",
  "Mars Culture Economy (Signature Edition) \u2014 Independence",
  "The Signature Method for Mars Culture Economy \u2014 Independence",
  "Mars Art and Media (Signature Edition) \u2014 Independence",
  "The Signature Method for Mars Art and Media \u2014 Independence",
  "Mars Education System (Signature Edition) \u2014 Independence",
  "The Signature Method for Mars Education System \u2014 Independence"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Mars Economy Study — "+safe+"\n"
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
    name:topic+' — mars economy record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A mars economy record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-db-mars-economy-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-mars-economy-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
