(function(){'use strict';
/* JAH HEMA Longsword Combat Signature Database generator — jahdb-combat-hema-longsword-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBHLS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is HEMA: The Historical European Martial Arts Revival (Signature Edition) (Signature Edition) - Foundations",
  "The Longsword: Anatomy of the Weapon (Signature Edition) (Signature Edition) - Foundations",
  "Safety Gear and Training Weapons (Signature Edition) (Signature Edition) - Foundations",
  "Vom Tag: The Roof Guard (Signature Edition) (Signature Edition) - Foundations",
  "Ochs: The Ox Guard (Signature Edition) (Signature Edition) - Foundations",
  "Pflug: The Plow Guard (Signature Edition) (Signature Edition) - Foundations",
  "Alber: The Fool Guard (Signature Edition) (Signature Edition) - Foundations",
  "Footwork: The Passing Step and the Gathering Step (Signature Edition) (Signature Edition) - Foundations",
  "The Oberhau: The Overhand Cut (Signature Edition) (Signature Edition) - Foundations",
  "The Unterhau: The Rising Cut (Signature Edition) (Signature Edition) - Foundations",
 ],
 "Compounded": [
  "The Zornhau: The Wrath Cut (Signature Edition) (Signature Edition) - Compounded",
  "The Zwerchau: The Thwart Cut (Signature Edition) (Signature Edition) - Compounded",
  "The Schielhau: The Squinting Cut (Signature Edition) (Signature Edition) - Compounded",
  "The Scheitelhau: The Parting Cut (Signature Edition) (Signature Edition) - Compounded",
  "The Krumphau: The Crooked Cut (Signature Edition) (Signature Edition) - Compounded",
  "Nachreisen: Travelling After (Signature Edition) (Signature Edition) - Compounded",
  "The Thrust: Setting the Point (Signature Edition) (Signature Edition) - Compounded",
  "Winden: The Eight Windings (Signature Edition) (Signature Edition) - Compounded",
  "Duplieren and Mutieren: Doubling and Mutating (Signature Edition) (Signature Edition) - Compounded",
  "Abschneiden: Slicing Off (Signature Edition) (Signature Edition) - Compounded",
  "Durchwechseln: Changing Through (Signature Edition) (Signature Edition) - Compounded",
  "Zucken: Pulling Through (Signature Edition) (Signature Edition) - Compounded",
  "Grappling at the Sword: Ringen am Schwert (Signature Edition) (Signature Edition) - Compounded",
  "Half-Sword Play: Halbschwert (Signature Edition) (Signature Edition) - Compounded",
 ],
 "Advanced": [
  "Versetzen: The Displacements (Signature Edition) (Signature Edition) - Advanced",
  "Fühlen: Feeling in the Bind (Signature Edition) (Signature Edition) - Advanced",
  "Indes: The Instant - Vor, Nach, and Indes (Signature Edition) (Signature Edition) - Advanced",
  "Free Play: The Freifechten Progression (Signature Edition) (Signature Edition) - Advanced",
  "Longsword Against Other Weapons (Signature Edition) (Signature Edition) - Advanced",
  "Reading the Fight Books: The Manual Tradition (Signature Edition) (Signature Edition) - Advanced",
  "Judging the Longsword Tournament (Signature Edition) (Signature Edition) - Advanced",
  "Teaching HEMA Longsword: The Instructor Ladder (Signature Edition) (Signature Edition) - Advanced",
  "The Grand Assault: A Complete Longsword Sequence (Signature Edition) (Signature Edition) - Advanced",
  "Preserving the Art: The Lineage of the Longsword (Signature Edition) (Signature Edition) - Advanced",
 ],
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# HEMA Longsword Study — "+safe+"\n"
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
    name:topic+' — combat technique record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A combat technique record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"hema-longsword-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-combat-hema-longsword-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('combat-hema-longsword-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
