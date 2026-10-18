(function(){'use strict';
/* JAH The Deduction Detective Database Database generator — jahdb-db-deduction-detective-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DEDDET-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Case: The missing cookies: someone raided the jar between lu...",
  "Case: The wilted plant: who forgot to water it...",
  "Case: The broken vase: three kids, one confession each...",
  "Case: The empty bird feeder: seeds vanish nightly...",
  "Case: The muddy footprints: who tracked mud inside...",
  "Case: The missing library book: last seen Tuesday...",
  "Case: The cold cup of cocoa: who left it...",
  "Case: The flat tire: nail or mischief...",
  "Case: The silent phone: who turned off the ringer...",
  "Case: The eaten homework: the dog is accused...",
  "Case: The mysterious gift: no card attached..."
 ],
 "Compounded": [
  "Case: The locked room: the window was locked from inside...",
  "Case: The poisoned punch: three drank, one fell ill...",
  "Case: The alibi: 'I was home alone watching the finale.'...",
  "Case: The forged note: 'Please excuse Sam - signed, Mom.'...",
  "Case: The missing money: the cash box is light by $20...",
  "Case: The swapped suitcases: two identical bags, one owner...",
  "Case: The midnight snacker: the fridge raids continue...",
  "Case: The broken window: ball or break-in...",
  "Case: The late library book: who kept it 40 days...",
  "Case: The anonymous compliment: who left the kind note...",
  "Case: The great cookie swap: whose recipe won the contest...",
  "Case: The phantom text: 'meet me at 8' - from whom..."
 ],
 "Advanced": [
  "Case: The chess cheat: who moved the knight illegally...",
  "Case: The art forgery: real or fake...",
  "Case: The two alibis: both claim the theater...",
  "Case: The coded diary: who wrote the margin notes...",
  "Case: The missing will: three heirs, one drawer...",
  "Case: The perfect attendance: who forged the sign-in sheet...",
  "Case: The secret recipe: who leaked it...",
  "Case: The time capsule: whose item is oldest...",
  "Case: The double booking: two parties, one hall...",
  "Case: The final exam: who had the answers early...",
  "Case: The garden gnome heist: three suspects, one wheelbarro..."
 ]
};
var DEMOKIND="deduction-proof";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Deduction Study — "+safe+"\n"
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
    name:topic+' — deduction mystery record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A deduction mystery record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'public-harvest',
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
var gen={version:'jahdb-db-deduction-detective-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-deduction-detective',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
