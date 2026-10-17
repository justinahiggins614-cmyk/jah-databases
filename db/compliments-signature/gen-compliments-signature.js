(function(){'use strict';
/* JAH The Compliments Signature Database generator — jahdb-compliments-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CMPLS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Thank You, and I Mean It (Signature Edition) - Foundations",
  "Noticing Small Efforts (Signature Edition) - Foundations",
  "You Are a Kind Person (Signature Edition) - Foundations",
  "Greeting People by Name (Signature Edition) - Foundations",
  "Praising Punctuality (Signature Edition) - Foundations",
  "Praising a Good Question (Signature Edition) - Foundations",
  "Acknowledging Hard Work in Progress (Signature Edition) - Foundations",
  "Complimenting Calm Under Pressure (Signature Edition) - Foundations",
  "Thanking Someone Publicly (Signature Edition) - Foundations",
  "Noticing Consistency (Signature Edition) - Foundations",
  "Praising Good Listening (Signature Edition) - Foundations",
  "Thanking Someone for Their Time (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Praising Craftsmanship (Signature Edition) - Compounded",
  "Complimenting a Well-Run Meeting (Signature Edition) - Compounded",
  "Acknowledging Everyday Courage (Signature Edition) - Compounded",
  "Praising Clear Writing (Signature Edition) - Compounded",
  "Complimenting Patience (Signature Edition) - Compounded",
  "Tasteful Appearance Compliments (Signature Edition) - Compounded",
  "Praising a Good Mentor (Signature Edition) - Compounded",
  "Complimenting Integrity (Signature Edition) - Compounded",
  "Recognizing Behind-the-Scenes Work (Signature Edition) - Compounded",
  "Praising Problem Solving (Signature Edition) - Compounded",
  "Complimenting Humor That Lifts a Room (Signature Edition) - Compounded",
  "Praising a Comeback From a Mistake (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Complimenting a Person's Whole Character (Signature Edition) - Advanced",
  "The Lifetime Achievement Tribute (Signature Edition) - Advanced",
  "Praising Moral Courage (Signature Edition) - Advanced",
  "Honoring a Life's Work (Signature Edition) - Advanced",
  "The Living Tribute: Say It While They Can Hear It (Signature Edition) - Advanced",
  "Recognizing a Mentor's Legacy (Signature Edition) - Advanced",
  "Complimenting Grace in Hard Times (Signature Edition) - Advanced",
  "Recognizing the Unsung Hero (Signature Edition) - Advanced",
  "Praising Forgiveness (Signature Edition) - Advanced",
  "The Compliment That Changes a Life (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Compliment Study — "+safe+"\n"
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
    name:topic+' — compliment record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A compliment record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"compliment-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-compliments-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('compliments-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
