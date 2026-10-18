(function(){'use strict';
/* JAH The Rhythm Pattern Database generator — jahdb-rhythm-pattern-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RHPTS-";
var FIELDS=["Rhythm Foundations", "World Grooves", "Rhythm Mastery"];
var TOPICS={
 "Rhythm Foundations": [
  "Son Clave 3-2",
  "Bossa Nova",
  "Four-on-the-Floor",
  "Boom-Bap",
  "Half-Time Feel",
  "Dembow",
  "Shuffle Blues",
  "Two-Step Garage",
  "Waltz Time",
  "Samba Surdo",
  "Reggae One Drop",
  "Swing Ride"
 ],
 "World Grooves": [
  "Afrobeat Engine",
  "Highlife Guitar",
  "Soukous Flow",
  "Mbalax Sabar",
  "Gqom Broken",
  "Amapiano Log Drum",
  "Cumbia Sonidera",
  "Soca Road",
  "Calypso Groove",
  "Bhangra Dhol",
  "Taiko Matsuri",
  "Gnawa Krakebs",
  "Second Line"
 ],
 "Rhythm Mastery": [
  "Drum'n'Bass Sprint",
  "Jungle Chop",
  "Amen Breakbeat",
  "Footwork Rush",
  "Dubstep Half-Drop",
  "Metal Double-Kick",
  "Punk D-Beat",
  "Balkan Brass Blast",
  "Your Rhythm Signature"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# rhythm — "+safe+"\n"
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
    name:topic+' — rhythm pattern record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A rhythm pattern record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"rhythm-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-rhythm-pattern-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('rhythm-pattern-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
