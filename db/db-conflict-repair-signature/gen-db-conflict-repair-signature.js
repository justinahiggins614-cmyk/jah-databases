(function(){'use strict';
/* JAH The Conflict Repair Database Signature Database generator — jahdb-db-conflict-repair-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CONREPS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Repair: You forgot your friend's birthday...",
  "Repair: You snapped at someone when tired...",
  "Repair: You broke a borrowed item...",
  "Repair: You shared something told in confidence...",
  "Repair: You stood someone up...",
  "Repair: You took credit for a group idea...",
  "Repair: You gossiped about a friend...",
  "Repair: You lost a borrowed book...",
  "Repair: You laughed at someone's mistake...",
  "Repair: You forgot to reply for weeks...",
  "Repair: You double-booked a friend..."
 ],
 "Compounded": [
  "Repair: You lied about something small...",
  "Repair: A harsh argument with a sibling...",
  "Repair: You missed their big moment...",
  "Repair: Money lent, resentment grown...",
  "Repair: You criticized them publicly...",
  "Repair: A broken promise to a child...",
  "Repair: Workplace credit dispute...",
  "Repair: You chose sides in their divorce...",
  "Repair: A friendship faded from neglect...",
  "Repair: You broke a diet pact together...",
  "Repair: Holiday hosting blowup...",
  "Repair: You read their journal..."
 ],
 "Advanced": [
  "Repair: Betrayal of trust in a partnership...",
  "Repair: Estranged parent and child...",
  "Repair: Business partnership collapse...",
  "Repair: A lie that grew for years...",
  "Repair: Addiction's damage to family...",
  "Repair: Sibling inheritance fight...",
  "Repair: Public shaming online...",
  "Repair: A friendship ended over politics...",
  "Repair: Parental favoritism wounds...",
  "Repair: Workplace bullying aftermath...",
  "Repair: A broken engagement..."
 ]
};
var DEMOKIND="repair-proof";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Conflict Repair Study — "+safe+"\n"
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
    name:topic+' — repair guide record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A repair guide record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-db-conflict-repair-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-conflict-repair-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
