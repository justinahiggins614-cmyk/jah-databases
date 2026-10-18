(function(){'use strict';
/* JAH The Speed Thinking Database Signature Database generator — jahdb-db-speed-thinking-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SPETHIS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Sprint: Name 5 animals in 10 seconds...",
  "Sprint: What is 7 + 8...",
  "Sprint: Name 3 red things in 5 seconds...",
  "Sprint: What is 9 x 6...",
  "Sprint: Spell 'rhythm' in 5 seconds...",
  "Sprint: What is half of 50...",
  "Sprint: Name 4 fruits in 8 seconds...",
  "Sprint: What is 100 - 37...",
  "Sprint: How many days in a week...",
  "Sprint: What is 12 x 12...",
  "Sprint: Name 3 things that are cold in 5 seconds..."
 ],
 "Compounded": [
  "Sprint: What is 15% of 200...",
  "Sprint: Name 5 countries in 10 seconds...",
  "Sprint: What is 7 cubed...",
  "Sprint: How many seconds in 5 minutes...",
  "Sprint: Name the 7 dwarfs in 15 seconds...",
  "Sprint: What is 25 x 16...",
  "Sprint: Spell 'necessary' in 5 seconds...",
  "Sprint: What is the square root of 169...",
  "Sprint: Name 6 planets in 10 seconds...",
  "Sprint: What is 1+2+...+10...",
  "Sprint: How many minutes in a day...",
  "Sprint: What is 11 x 11..."
 ],
 "Advanced": [
  "Sprint: What is 99 x 99...",
  "Sprint: Name 10 US states in 15 seconds...",
  "Sprint: What is 2^10...",
  "Sprint: How many handshakes among 12 people...",
  "Sprint: What is 15 squared...",
  "Sprint: Name the 5 Great Lakes in 10 seconds...",
  "Sprint: What is 37 x 3...",
  "Sprint: How many degrees in a triangle's angles...",
  "Sprint: What is 8! (factorial)...",
  "Sprint: Name 8 Shakespeare plays in 15 seconds...",
  "Sprint: What is the 10th prime..."
 ]
};
var DEMOKIND="sprint-proof";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Speed Drill — "+safe+"\n"
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
    name:topic+' — speed drill record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A speed drill record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-db-speed-thinking-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-speed-thinking-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
