(function(){'use strict';
/* JAH HEMA Longsword Combat Database generator — jahdb-combat-hema-longsword-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBHL-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is HEMA: The Historical European Martial Arts Revival - Foundations",
  "The Longsword: Anatomy of the Weapon - Foundations",
  "Safety Gear and Training Weapons - Foundations",
  "Vom Tag: The Roof Guard - Foundations",
  "Ochs: The Ox Guard - Foundations",
  "Pflug: The Plow Guard - Foundations",
  "Alber: The Fool Guard - Foundations",
  "Footwork: The Passing Step and the Gathering Step - Foundations",
  "The Oberhau: The Overhand Cut - Foundations",
  "The Unterhau: The Rising Cut - Foundations",
 ],
 "Compounded": [
  "The Zornhau: The Wrath Cut - Compounded",
  "The Zwerchau: The Thwart Cut - Compounded",
  "The Schielhau: The Squinting Cut - Compounded",
  "The Scheitelhau: The Parting Cut - Compounded",
  "The Krumphau: The Crooked Cut - Compounded",
  "Nachreisen: Travelling After - Compounded",
  "The Thrust: Setting the Point - Compounded",
  "Winden: The Eight Windings - Compounded",
  "Duplieren and Mutieren: Doubling and Mutating - Compounded",
  "Abschneiden: Slicing Off - Compounded",
  "Durchwechseln: Changing Through - Compounded",
  "Zucken: Pulling Through - Compounded",
  "Grappling at the Sword: Ringen am Schwert - Compounded",
  "Half-Sword Play: Halbschwert - Compounded",
 ],
 "Advanced": [
  "Versetzen: The Displacements - Advanced",
  "Fühlen: Feeling in the Bind - Advanced",
  "Indes: The Instant - Vor, Nach, and Indes - Advanced",
  "Free Play: The Freifechten Progression - Advanced",
  "Longsword Against Other Weapons - Advanced",
  "Reading the Fight Books: The Manual Tradition - Advanced",
  "Judging the Longsword Tournament - Advanced",
  "Teaching HEMA Longsword: The Instructor Ladder - Advanced",
  "The Grand Assault: A Complete Longsword Sequence - Advanced",
  "Preserving the Art: The Lineage of the Longsword - Advanced",
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
    demo:{kind:"hema-longsword-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-combat-hema-longsword-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('combat-hema-longsword',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
