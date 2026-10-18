(function(){'use strict';
/* JAH The Interactive Mystery Story Database generator — jahdb-db-interactive-mystery-story-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MIMS-";
var FIELDS=["City Cases","Country Cases","Locked Rooms"];
var TOPICS={
 "City Cases": [
  "Your First Case \u2014 City Cases",
  "Your First Case \u2014 Deep Dive \u2014 City Cases",
  "Choose Your Suspect \u2014 City Cases",
  "Choose Your Suspect \u2014 Deep Dive \u2014 City Cases",
  "The Chase Branch \u2014 City Cases",
  "The Chase Branch \u2014 Deep Dive \u2014 City Cases",
  "The Interrogation \u2014 City Cases",
  "The Interrogation \u2014 Deep Dive \u2014 City Cases",
  "The Evidence Locker \u2014 City Cases",
  "The Evidence Locker \u2014 Deep Dive \u2014 City Cases",
  "The Docks at Midnight \u2014 City Cases",
  "The Docks at Midnight \u2014 Deep Dive \u2014 City Cases",
  "The Master Branch \u2014 City Cases",
  "The Master Branch \u2014 Deep Dive \u2014 City Cases"
 ],
 "Country Cases": [
  "The Unreliable Ally \u2014 Country Cases",
  "The Unreliable Ally \u2014 Deep Dive \u2014 Country Cases",
  "The Storm Branch \u2014 Country Cases",
  "The Storm Branch \u2014 Deep Dive \u2014 Country Cases",
  "The Disguise Choice \u2014 Country Cases",
  "The Disguise Choice \u2014 Deep Dive \u2014 Country Cases",
  "The Letter or the Life \u2014 Country Cases",
  "The Letter or the Life \u2014 Deep Dive \u2014 Country Cases",
  "The Village Fete \u2014 Country Cases",
  "The Village Fete \u2014 Deep Dive \u2014 Country Cases"
 ],
 "Locked Rooms": [
  "The Maze of Alibis \u2014 Locked Rooms",
  "The Maze of Alibis \u2014 Deep Dive \u2014 Locked Rooms",
  "The Key Choice \u2014 Locked Rooms",
  "The Key Choice \u2014 Deep Dive \u2014 Locked Rooms",
  "The Mirror Suspect \u2014 Locked Rooms",
  "The Mirror Suspect \u2014 Deep Dive \u2014 Locked Rooms",
  "The Final Choice \u2014 Locked Rooms",
  "The Final Choice \u2014 Deep Dive \u2014 Locked Rooms",
  "The Manor's Second Floor \u2014 Locked Rooms",
  "The Manor's Second Floor \u2014 Deep Dive \u2014 Locked Rooms"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Interactive Mystery Study — "+safe+"\n"
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
    name:topic+' — interactive mystery record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A interactive mystery record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-db-interactive-mystery-story-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-interactive-mystery-story',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
