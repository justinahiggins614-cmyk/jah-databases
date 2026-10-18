(function(){'use strict';
/* JAH The Sports and Recreation Signature Database generator — jahdb-sports-recreation-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SPRCS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Great Game — The Signature View (Signature Edition) - Foundations",
  "The Engine Within — Signature Physiology (Signature Edition) - Foundations",
  "The Honest Motion — Signature Biomechanics (Signature Edition) - Foundations",
  "The Daily Practice — Signature Training (Signature Edition) - Foundations",
  "The Honest Fuel — Signature Nutrition (Signature Edition) - Foundations",
  "The Code of Contests — Signature Team Rules (Signature Edition) - Foundations",
  "The Solo Trial — Signature Individual Rules (Signature Edition) - Foundations",
  "The Impartial Eye — Signature Officiating (Signature Edition) - Foundations",
  "The Teacher's Art — Signature Coaching (Signature Edition) - Foundations",
  "The Young Players — Signature Youth Sport (Signature Edition) - Foundations",
  "The Tools of Play — Signature Equipment (Signature Edition) - Foundations",
  "The Counting — Signature Sports Math (Signature Edition) - Foundations",
 ],
 "Compounded": [
  "The Nested Seasons — Signature Periodization (Signature Edition) - Compounded",
  "The Strong Foundation — Signature Strength (Signature Edition) - Compounded",
  "The Healers — Signature Sports Medicine (Signature Edition) - Compounded",
  "The True Measure — Signature Performance Stats (Signature Edition) - Compounded",
  "The Crafted Gear — Signature Equipment Engineering (Signature Edition) - Compounded",
  "The Stage — Signature Venue Design (Signature Edition) - Compounded",
  "The Living Carpet — Signature Turf (Signature Edition) - Compounded",
  "The Unseen Machine — Signature Event Operations (Signature Edition) - Compounded",
  "The Welcomed Crowd — Signature Ticketing (Signature Edition) - Compounded",
  "The Far Eye — Signature Broadcasting (Signature Edition) - Compounded",
  "The Common Ground — Signature Parks and Trails (Signature Edition) - Compounded",
 ],
 "Advanced": [
  "The Deep Numbers — Signature Advanced Analytics (Signature Edition) - Advanced",
  "The Clean Contest — Signature Anti-Doping (Signature Edition) - Advanced",
  "The Honest Ledger — Signature Sports Business (Signature Edition) - Advanced",
  "The True Pairing — Signature Sponsorship (Signature Edition) - Advanced",
  "The Open Arena — Signature Adaptive Sport (Signature Edition) - Advanced",
  "The Trained Mind — Signature Sports Psychology (Signature Edition) - Advanced",
  "The Tended House — Signature Facility Maintenance (Signature Edition) - Advanced",
  "The Great Gathering — Signature Mega-Events (Signature Edition) - Advanced",
  "The Law of Games — Signature Sports Law (Signature Edition) - Advanced",
  "The Coming Games — Signature Future Tech (Signature Edition) - Advanced",
  "The Steward's Review — Signature Mastery (Signature Edition) - Advanced",
 ],
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n"
   + "# "+safe+" -- structural sample demo. Property of Justin Addam Higgins (JAH).\n"
   + "# Win-percentage structural sample calculator (sports industry)\n"
   + "w, l = 58.0, 24.0\n"
   + "pct = w/(w+l)\n"
   + "print('sample wins:', w, 'losses:', l)\n"
   + "print('sample win pct:', round(pct,3))\n"
   + "assert 0 <= pct <= 1\n"
   + "print('OK: structural sample demo ran')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — sports industry record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A sports industry record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"sports-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-sports-recreation-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('sports-recreation-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
