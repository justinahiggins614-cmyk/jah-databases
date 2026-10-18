(function(){'use strict';
/* JAH Signature Famous Leaders Database generator — jahdb-famous-leaders-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FLEADS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Great Leaders: An Overview (Signature Edition)", "Hammurabi of Babylon (Signature Edition)", "Alexander the Great (Signature Edition)", "Julius Caesar (Signature Edition)", "Augustus: The First Emperor (Signature Edition)", "Ashoka the Great (Signature Edition)", "Qin Shi Huang (Signature Edition)", "Cleopatra VII (Signature Edition)", "Charlemagne (Signature Edition)", "Genghis Khan (Signature Edition)", "Joan of Arc (Signature Edition)"], "Compounded": ["Suleiman the Magnificent (Signature Edition)", "Elizabeth I of England (Signature Edition)", "Peter the Great (Signature Edition)", "Catherine the Great (Signature Edition)", "George Washington (Signature Edition)", "Napoleon Bonaparte (Signature Edition)", "Simon Bolivar (Signature Edition)", "Abraham Lincoln (Signature Edition)", "Otto von Bismarck (Signature Edition)", "Winston Churchill (Signature Edition)", "Franklin D. Roosevelt (Signature Edition)", "Mahatma Gandhi (Signature Edition)"], "Advanced": ["Nelson Mandela (Signature Edition)", "Martin Luther King Jr. (Signature Edition)", "Eleanor Roosevelt (Signature Edition)", "Mustafa Kemal Ataturk (Signature Edition)", "Jawaharlal Nehru (Signature Edition)", "Sun Yat-sen (Signature Edition)", "Golda Meir (Signature Edition)", "Kwame Nkrumah (Signature Edition)", "Ho Chi Minh (Signature Edition)", "Haile Selassie (Signature Edition)", "The Leader's Craft (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — famous-leaders-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — leader record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A leader record of "'+topic+'" in '+field+'. Signature original sample are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:false,
    signature_label:'Signature original - created in the Signature system; not a public record.',
    disclaimer:'Signature original sample — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"famous-leaders-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-famous-leaders-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("famous-leaders-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
