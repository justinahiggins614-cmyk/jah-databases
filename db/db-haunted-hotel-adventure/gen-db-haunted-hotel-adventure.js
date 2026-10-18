(function(){'use strict';
/* JAH The Haunted Hotel Adventure Database generator — jahdb-db-haunted-hotel-adventure-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MHHA-";
var FIELDS=["The Lobby","The Upper Floors","The Basement"];
var TOPICS={
 "The Lobby": [
  "Check-In at Midnight \u2014 The Lobby",
  "Check-In at Midnight \u2014 Deep Dive \u2014 The Lobby",
  "The Elevator That Stops at 13 \u2014 The Lobby",
  "The Elevator That Stops at 13 \u2014 Deep Dive \u2014 The Lobby",
  "The Empty Dining Room \u2014 The Lobby",
  "The Empty Dining Room \u2014 Deep Dive \u2014 The Lobby",
  "Checkout at Dawn \u2014 The Lobby",
  "Checkout at Dawn \u2014 Deep Dive \u2014 The Lobby",
  "The Night Clerk's Ledger \u2014 The Lobby",
  "The Night Clerk's Ledger \u2014 Deep Dive \u2014 The Lobby"
 ],
 "The Upper Floors": [
  "The Stairwell That Counts \u2014 The Upper Floors",
  "The Stairwell That Counts \u2014 Deep Dive \u2014 The Upper Floors",
  "Room 204's Guestbook \u2014 The Upper Floors",
  "Room 204's Guestbook \u2014 Deep Dive \u2014 The Upper Floors",
  "The Chandelier's Shadow \u2014 The Upper Floors",
  "The Chandelier's Shadow \u2014 Deep Dive \u2014 The Upper Floors",
  "The Roof Garden \u2014 The Upper Floors",
  "The Roof Garden \u2014 Deep Dive \u2014 The Upper Floors",
  "The Library That Lends \u2014 The Upper Floors",
  "The Library That Lends \u2014 Deep Dive \u2014 The Upper Floors",
  "The Penthouse That Isn't \u2014 The Upper Floors",
  "The Penthouse That Isn't \u2014 Deep Dive \u2014 The Upper Floors",
  "The Ballroom's Last Waltz \u2014 The Upper Floors",
  "The Ballroom's Last Waltz \u2014 Deep Dive \u2014 The Upper Floors"
 ],
 "The Basement": [
  "The Pool at 4 A.M. \u2014 The Basement",
  "The Pool at 4 A.M. \u2014 Deep Dive \u2014 The Basement",
  "The Boiler Room Bargain \u2014 The Basement",
  "The Boiler Room Bargain \u2014 Deep Dive \u2014 The Basement",
  "The Door With No Room \u2014 The Basement",
  "The Door With No Room \u2014 Deep Dive \u2014 The Basement",
  "The Kitchen's Night Shift \u2014 The Basement",
  "The Kitchen's Night Shift \u2014 Deep Dive \u2014 The Basement",
  "The Laundry's Lost Socks \u2014 The Basement",
  "The Laundry's Lost Socks \u2014 Deep Dive \u2014 The Basement"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Haunted Hotel Study — "+safe+"\n"
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
    name:topic+' — haunted hotel adventure record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A haunted hotel adventure record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-db-haunted-hotel-adventure-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-haunted-hotel-adventure',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
