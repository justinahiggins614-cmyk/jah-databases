(function(){'use strict';
/* JAH Signature Famous Generals Database generator — jahdb-famous-generals-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FGENS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Great Generals: An Overview (Signature Edition)", "Hannibal Barca (Signature Edition)", "Scipio Africanus (Signature Edition)", "Gaius Marius (Signature Edition)", "Belisarius (Signature Edition)", "Saladin (Signature Edition)", "Subutai (Signature Edition)", "Joan of Arc (Commander) (Signature Edition)", "Hernan Cortes (Commander) (Signature Edition)", "Gustavus Adolphus (Signature Edition)", "Frederick the Great (Signature Edition)"], "Compounded": ["Napoleon as General (Signature Edition)", "Wellington (Signature Edition)", "Ulysses S. Grant (Signature Edition)", "Robert E. Lee (Signature Edition)", "William Tecumseh Sherman (Signature Edition)", "Helmuth von Moltke the Elder (Signature Edition)", "Erwin Rommel (Signature Edition)", "Georgy Zhukov (Signature Edition)", "Bernard Montgomery (Signature Edition)", "Douglas MacArthur (Signature Edition)", "Dwight D. Eisenhower (Signature Edition)", "George Patton (Signature Edition)"], "Advanced": ["Vo Nguyen Giap (Signature Edition)", "Moshe Dayan (Signature Edition)", "Ariel Sharon (Signature Edition)", "Norman Schwarzkopf (Signature Edition)", "Colin Powell (Signature Edition)", "The General Staff System (Signature Edition)", "Logistics: The Sinews of War (Signature Edition)", "Intelligence in Warfare (Signature Edition)", "The Citizen-Soldier Tradition (Signature Edition)", "Women Generals (Signature Edition)", "The General's Library (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — famous-generals-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — general record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A general record of "'+topic+'" in '+field+'. Signature original sample are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:false,
    signature_label:'Signature original - created in the Signature system; not a public record.',
    disclaimer:'Signature original sample — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"famous-generals-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-famous-generals-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("famous-generals-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
