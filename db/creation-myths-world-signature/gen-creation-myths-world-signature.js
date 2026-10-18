(function(){'use strict';
/* JAH The World Creation Myths Signature Database generator — jahdb-creation-myths-world-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CRMY-S-";
var FIELDS=["Cosmic Beginnings", "Earth & Humankind", "Order from Chaos"];
var TOPICS={
 "Cosmic Beginnings": [
  "The Cosmic Egg — Worldwide (Signature Edition) \u2014 Cosmic Beginnings",
  "The Signature Method for The Earth-Diver — Worldwide \u2014 Cosmic Beginnings",
  "The Primeval Waters — Worldwide (Signature Edition) \u2014 Cosmic Beginnings",
  "The Signature Method for The Creator's Word — Worldwide \u2014 Cosmic Beginnings",
  "The World Parents — Worldwide (Signature Edition) \u2014 Cosmic Beginnings",
  "The Dreaming — Aboriginal (Signature Edition) \u2014 Cosmic Beginnings",
  "The Signature Method for Popol Vuh — The Maya Book \u2014 Cosmic Beginnings",
  "Genesis — The Hebrew Account (Signature Edition) \u2014 Cosmic Beginnings",
  "The Signature Method for Theogony — Hesiod's Account \u2014 Cosmic Beginnings",
  "Enuma Elish — Babylon's Account (Signature Edition) \u2014 Cosmic Beginnings",
  "The Eddas — The Norse Account (Signature Edition) \u2014 Cosmic Beginnings",
  "The Signature Method for The Rainbow Serpent — Aboriginal \u2014 Cosmic Beginnings",
  "Rangi and Papa — The Maori Parents (Signature Edition) \u2014 Cosmic Beginnings"
 ],
 "Earth & Humankind": [
  "The Signature Method for The First Humans — Worldwide \u2014 Earth & Humankind",
  "The Theft of Fire — The Gift (Signature Edition) \u2014 Earth & Humankind",
  "The Signature Method for The Fall — Paradise Lost \u2014 Earth & Humankind",
  "The Flood — The Deluge (Signature Edition) \u2014 Earth & Humankind",
  "The Signature Method for The Tower — Pride's Monument \u2014 Earth & Humankind",
  "The Signature Method for Kojiki — Japan's Account \u2014 Earth & Humankind",
  "The Signature Method for Ask and Embla — The Norse Pair \u2014 Earth & Humankind",
  "The Maize People — Maya (Signature Edition) \u2014 Earth & Humankind",
  "The Signature Method for The Clay People — Yoruba \u2014 Earth & Humankind",
  "Pandora's Jar — The Greek Release (Signature Edition) \u2014 Earth & Humankind",
  "The Signature Method for The First Fire — The Hearth \u2014 Earth & Humankind"
 ],
 "Order from Chaos": [
  "The Separation — Sky from Earth (Signature Edition) \u2014 Order from Chaos",
  "The Signature Method for The Slaying — Chaos Dragon \u2014 Order from Chaos",
  "The Ordering — Laws and Calendars (Signature Edition) \u2014 Order from Chaos",
  "The Signature Method for The World Tree — Axis \u2014 Order from Chaos",
  "The Signature Method for The Golden Age — The Lost Prime \u2014 Order from Chaos",
  "The World Mountain — Axis (Signature Edition) \u2014 Order from Chaos",
  "Comparative Patterns — The Scholar's Map (Signature Edition) \u2014 Order from Chaos",
  "The Signature Method for The Endings — Eschatology \u2014 Order from Chaos",
  "Why Beginnings Matter (Signature Edition) \u2014 Order from Chaos",
  "The Signature Method for The Five Suns — Aztec Ages \u2014 Order from Chaos"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# World Creation Myths Signature — "+safe+"\n"
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
    name:topic+' — mythology record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A mythology record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-creation-myths-world-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('creation-myths-world-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
