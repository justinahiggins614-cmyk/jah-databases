(function(){'use strict';
/* JAH The Technological Civilization Transition Future Technology Database generator — jahdb-futuretech-100-the-technological-civilization-transition-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT100-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "1769: Steam Power - Foundations",
  "1800s: the Steam Age - Foundations",
  "1879: Electric Light - Foundations",
  "1900s: Mass Production - Foundations",
  "1945: the Atomic Age - Foundations",
  "1957: Sputnik - Foundations",
  "1969: the Moon - Foundations",
  "1971: the Microprocessor - Foundations",
  "1980s: the PC - Foundations",
  "1991: the Web - Foundations",
  "2007: the Smartphone - Foundations"
 ],
 "Compounded": [
  "2010s: the Cloud - Compounded",
  "2022: the AI Age - Compounded",
  "2025: AI Transforms - Compounded",
  "The Transition Begins - Compounded",
  "Kardashev I - Compounded",
  "The Planetary Civilization - Compounded",
  "The Post-Scarcity Transition - Compounded",
  "The Merged Humanity - Compounded",
  "The Interplanetary Civilization - Compounded",
  "Kardashev II - Compounded",
  "The Stellar Civilization - Compounded",
  "The Post-Biological - Compounded"
 ],
 "Advanced": [
  "The Galactic Civilization - Advanced",
  "Kardashev III - Advanced",
  "The Universal Civilization - Advanced",
  "The Omega Transition - Advanced",
  "The Transcendent Humanity - Advanced",
  "The Eternal Civilization - Advanced",
  "The Cosmic Mind - Advanced",
  "The Type IV Question - Advanced",
  "The Completed Transition - Advanced",
  "The New Beginning - Advanced",
  "Everyday Transcendence - Working Version - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Future Technology Study — "+safe+"\n"
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
  var id=PREFIX+String(seed).padStart(4,'0');
  return {
    id:id,
    name:topic+' — civilization transition record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A civilization transition record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-100-the-technological-civilization-transition-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{4}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-futuretech-100-the-technological-civilization-transition-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-100-the-technological-civilization-transition',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
