(function(){'use strict';
/* JAH Signature Aztec Database generator — jahdb-aztec-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AZTECS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Aztec: An Overview (Signature Edition)", "Tenochtitlan: The Lake City (Signature Edition)", "The Triple Alliance (Signature Edition)", "Moctezuma II (Signature Edition)", "Chinampa Agriculture (Signature Edition)", "The Aztec Calendar and the Sun Stone (Signature Edition)", "Human Sacrifice: The Facts (Signature Edition)", "Nahuatl: The Language (Signature Edition)", "The Fall of Tenochtitlan (1521) (Signature Edition)", "Hernan Cortes and the Conquest (Signature Edition)", "The Founding Myth: Eagle and Cactus (Signature Edition)"], "Compounded": ["Aztec Social Classes (Signature Edition)", "The Pochteca: Merchant-Spies (Signature Edition)", "Aztec Education: Calmecac and Telpochcalli (Signature Edition)", "Aztec Medicine (Signature Edition)", "The Tribute System (Signature Edition)", "Texcoco and Nezahualcoyotl (Signature Edition)", "The Flowery Wars (Signature Edition)", "Aztec Markets: Tlatelolco (Signature Edition)", "Eagle and Jaguar Warriors (Signature Edition)", "Aztec Women (Signature Edition)", "The Templo Mayor (Signature Edition)", "Aztec Law and Justice (Signature Edition)"], "Advanced": ["The Florentine Codex (Signature Edition)", "The Codex Mendoza (Signature Edition)", "Aztec Cosmology: The Five Suns (Signature Edition)", "The Ball Game: Tlachtli (Signature Edition)", "Aztec Philosophy: The Tlamatinime (Signature Edition)", "Tlaxcala: The Conquest's True Army (Signature Edition)", "Malinche: Dona Marina (Signature Edition)", "Cuauhtemoc: The Last Emperor (Signature Edition)", "The Noche Triste (Signature Edition)", "Nahua Continuity After the Conquest (Signature Edition)", "The Aztec Legacy in Mexico (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — aztec-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
   + "TOPIC = \""+safe+"\"\n"
   + "FIELD = \""+field+"\"\n"
   + "def summarize():\n"
   + "    return TOPIC + ' [' + FIELD + ']'\n"
   + "print(summarize())\n"
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
    name:topic+' — aztec record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A aztec record of "'+topic+'" in '+field+'. Signature original sample are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:false,
    signature_label:'Signature original - created in the Signature system; not a public record.',
    disclaimer:'Signature original sample — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"aztec-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-aztec-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("aztec-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
