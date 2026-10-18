(function(){'use strict';
/* JAH Signature Women in History Database generator — jahdb-women-in-history-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WOMHISTS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Women in History: An Overview (Signature Edition)", "Hatshepsut: The Female Pharaoh (Signature Edition)", "Sappho of Lesbos (Signature Edition)", "Artemisia of Halicarnassus (Signature Edition)", "Hypatia of Alexandria (Signature Edition)", "Theodora: Empress of Byzantium (Signature Edition)", "Eleanor of Aquitaine (Signature Edition)", "Hildegard of Bingen (Signature Edition)", "Joan of Arc (Woman) (Signature Edition)", "Isabella of Castile (Signature Edition)", "Catherine de Medici (Signature Edition)"], "Compounded": ["Mary Wollstonecraft (Signature Edition)", "Jane Austen (Signature Edition)", "Florence Nightingale (Signature Edition)", "Clara Barton (Signature Edition)", "Harriet Beecher Stowe (Signature Edition)", "Marie Curie (Signature Edition)", "Rosa Parks (Signature Edition)", "The Women Scientists (Signature Edition)", "The Women Writers (Signature Edition)", "Coco Chanel (Signature Edition)", "Amelia Earhart (Signature Edition)", "The Suffragists (Women) (Signature Edition)"], "Advanced": ["Indira Gandhi (Signature Edition)", "Margaret Thatcher (Signature Edition)", "Benazir Bhutto (Signature Edition)", "Angela Merkel (Signature Edition)", "Malala Yousafzai (Signature Edition)", "The Women Rulers (Signature Edition)", "The Women Warriors (Signature Edition)", "The Women Artists (Signature Edition)", "Marie Curie (Scientist) (Signature Edition)", "The Next Chapter (Signature Edition)", "Wangari Maathai (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — women-in-history-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — woman in history record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A woman in history record of "'+topic+'" in '+field+'. Signature original sample are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:false,
    signature_label:'Signature original - created in the Signature system; not a public record.',
    disclaimer:'Signature original sample — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"women-in-history-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-women-in-history-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("women-in-history-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
