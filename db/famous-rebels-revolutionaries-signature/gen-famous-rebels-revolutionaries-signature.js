(function(){'use strict';
/* JAH Signature Famous Rebels and Revolutionaries Database generator — jahdb-famous-rebels-revolutionaries-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-REBELS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Rebels and Revolutionaries: An Overview (Signature Edition)", "Spartacus (Signature Edition)", "Boudica (Signature Edition)", "Vercingetorix (Signature Edition)", "The Gracchi (Signature Edition)", "William Wallace (Signature Edition)", "Jan Hus (Signature Edition)", "Martin Luther (Reformer) (Signature Edition)", "Guy Fawkes (Signature Edition)", "Oliver Cromwell (Signature Edition)", "The American Revolutionaries (Signature Edition)"], "Compounded": ["Robespierre and the Terror (Signature Edition)", "Toussaint Louverture (Revolutionary) (Signature Edition)", "Simon Bolivar (Liberator) (Signature Edition)", "Giuseppe Garibaldi (Signature Edition)", "John Brown (Militant) (Signature Edition)", "The 1848 Revolutions (Signature Edition)", "The Paris Commune (1871) (Signature Edition)", "Emiliano Zapata (Signature Edition)", "Vladimir Lenin (Signature Edition)", "Rosa Luxemburg (Signature Edition)", "The Russian Revolution (1917) (Signature Edition)", "Mao Zedong (Revolutionary) (Signature Edition)"], "Advanced": ["Che Guevara (Signature Edition)", "Fidel Castro (Signature Edition)", "Ho Chi Minh (Revolutionary) (Signature Edition)", "The Cuban Revolution (Signature Edition)", "The Iranian Revolution (1979) (Signature Edition)", "1989: The Velvet Revolutions (Signature Edition)", "The Arab Spring (2011) (Signature Edition)", "The Color Revolutions (Signature Edition)", "Nonviolent Revolution (Signature Edition)", "The Counter-Revolution (Signature Edition)", "The Revolutionary's Ledger (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — famous-rebels-revolutionaries-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — revolutionary record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A revolutionary record of "'+topic+'" in '+field+'. Signature original sample are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:false,
    signature_label:'Signature original - created in the Signature system; not a public record.',
    disclaimer:'Signature original sample — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"famous-rebels-revolutionaries-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-famous-rebels-revolutionaries-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("famous-rebels-revolutionaries-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
