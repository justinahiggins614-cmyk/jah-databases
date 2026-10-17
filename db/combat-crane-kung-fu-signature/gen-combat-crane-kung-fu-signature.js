(function(){'use strict';
/* JAH Crane Kung Fu Combat Signature Database generator — jahdb-combat-crane-kung-fu-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBCRNS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": ["Waking the Crane (Signature Opening Salute)",
 "The Hollow Beak (Signature Beak Hand Build)",
 "Wingspan (Signature Wing Arm Build)",
 "Root of One Leg (Signature Single-Leg Root)",
 "The Nest (Signature Resting Guard)",
 "The Four-Count Crane Breath (Signature Breathing)",
 "Three-Point Steps (Signature Triangle Walking)",
 "Silent Evasion (Signature Side Step)",
 "Turn of the Wing (Signature Pivot)",
 "Morning Stone Beak (Signature Beak Conditioning)",
 "The Forty Pecks (Signature Solo Drill)",
 "Mirror Wing (Signature Cover Drill)"],
 "Compounded": ["Strike of the Dawn (Signature Single Peck)",
 "Twin Beaks (Signature Double Peck)",
 "Open Wing (Signature Wing Slap)",
 "The Snap Hook (Signature Hook and Pull)",
 "Rising Crane Elbow (Signature Elbow)",
 "Thunder Knee (Signature Knee)",
 "Low Tide Sweep (Signature Sweep)",
 "The Leaping Crane (Signature Flying Strike)",
 "High Wind (Signature High Wing Block)",
 "Deep Water (Signature Low Wing Block)",
 "Catch and Answer (Signature Parry Counter)",
 "Breaking the Grip (Signature Grab Escape)"],
 "Advanced": ["The First Signature Crane Form (Twelve Moves)",
 "The Second Signature Crane Form (Eighteen Moves)",
 "Crane Walks the Garden (Signature Walking Form)",
 "Night Crane (Signature Shadow Set)",
 "The One Hundred Pecks (Signature Endurance)",
 "Signature Pressure-Point Map (Beak Points)",
 "Iron Wing (Signature Arm Conditioning)",
 "Crane and Shadow (Signature Two-Person Set)",
 "The Crane Combat Code (Signature Principles)",
 "Seal of the Crane (Signature Final Integration)"]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Crane Kung Fu Study -- "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record -- structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — combat technique record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A combat technique record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"crane-kung-fu-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-combat-crane-kung-fu-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('combat-crane-kung-fu-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
