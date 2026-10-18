(function(){'use strict';
/* JAH The 2010s Signature Database generator — jahdb-decades-2010s-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-D2010S-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The 2010s at a Glance: The Smartphone Decade (Signature Edition) - Foundations",
  "2010: The iPad (Signature Edition) - Foundations",
  "2010: Instagram Launches (Signature Edition) - Foundations",
  "2010: The Arab Spring Begins (Signature Edition) - Foundations",
  "2011: Bin Laden Is Killed (Signature Edition) - Foundations",
  "2011: Occupy Wall Street (Signature Edition) - Foundations",
  "2012: The Higgs Boson (Signature Edition) - Foundations",
  "2012: Curiosity Lands on Mars (Signature Edition) - Foundations",
  "2013: The Boston Marathon Bombing (Signature Edition) - Foundations",
  "2015: Same-Sex Marriage Becomes Law (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "2010: The Bitcoin Pizza (Signature Edition) - Compounded",
  "2011: Fukushima (Signature Edition) - Compounded",
  "2012: Sandy Hook (Signature Edition) - Compounded",
  "2013: Snowden's Revelations (Signature Edition) - Compounded",
  "2014: The Ebola Outbreak (Signature Edition) - Compounded",
  "2015: The Paris Attacks (Signature Edition) - Compounded",
  "2015: SpaceX Lands the Falcon 9 (Signature Edition) - Compounded",
  "2015: New Horizons Reaches Pluto (Signature Edition) - Compounded",
  "2016: Brexit (Signature Edition) - Compounded",
  "2016: Trump Is Elected (Signature Edition) - Compounded",
  "2017: #MeToo (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "2018: The CRISPR Babies Scandal (Signature Edition) - Advanced",
  "2018: GDPR Takes Effect (Signature Edition) - Advanced",
  "2018: Parkland (Signature Edition) - Advanced",
  "2019: The First Image of a Black Hole (Signature Edition) - Advanced",
  "2019: Notre-Dame Burns (Signature Edition) - Advanced",
  "2019: Hong Kong's Protests (Signature Edition) - Advanced",
  "2012: The London Olympics (Signature Edition) - Advanced",
  "2014: The Ice Bucket Challenge (Signature Edition) - Advanced",
  "2016: AlphaGo Beats Lee Sedol (Signature Edition) - Advanced",
  "2017: The Great American Eclipse (Signature Edition) - Advanced",
  "2018: The Thai Cave Rescue (Signature Edition) - Advanced",
  "2019: Avengers: Endgame (Signature Edition) - Advanced",
  "2019: COVID-19 Emerges in Wuhan (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# 2010S — "+safe+"\n"
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
    name:topic+' — 2010s history record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A 2010s history record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"decades-2010s-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-decades-2010s-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('decades-2010s-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
