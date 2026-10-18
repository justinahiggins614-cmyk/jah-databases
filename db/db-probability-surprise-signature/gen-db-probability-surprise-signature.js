(function(){'use strict';
/* JAH The Probability Surprise Database Signature Database generator — jahdb-db-probability-surprise-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PROSURS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Probability: coin flip heads",
  "Probability: two heads in a row",
  "Probability: die shows 6",
  "Probability: die shows even",
  "Probability: two dice sum to 7",
  "Probability: drawing an ace",
  "Probability: heads then tails",
  "Probability: at least one head in two flips",
  "Probability: die sum of two dice is 2",
  "Probability: red card",
  "Probability: three heads in a row"
 ],
 "Compounded": [
  "Probability: birthday match in 23",
  "Probability: Monty Hall switch",
  "Probability: birthday match in 70",
  "Probability: two dice doubles",
  "Probability: flush draw?",
  "Probability: boy or girl paradox intro",
  "Probability: dice sum 7 vs 8",
  "Probability: coin streak of 5",
  "Probability: same birthday as YOU",
  "Probability: three dice all different",
  "Probability: at least one six in 4 rolls",
  "Probability: matching socks"
 ],
 "Advanced": [
  "Probability: birthday match in 50",
  "Probability: Monty Hall 100 doors",
  "Probability: dice game - 4 rolls vs 24",
  "Probability: gambler's streak fallacy",
  "Probability: three children, two boys?",
  "Probability: poker pair?",
  "Probability: lottery vs lightning",
  "Probability: false positive paradox",
  "Probability: birthday trio?",
  "Probability: dice expected value",
  "Probability: secretary problem"
 ]
};
var DEMOKIND="probability-proof";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Probability Surprise Study — "+safe+"\n"
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
    name:topic+' — probability puzzle record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A probability puzzle record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-db-probability-surprise-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-probability-surprise-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
