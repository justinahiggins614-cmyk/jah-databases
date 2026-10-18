(function(){'use strict';
/* JAH Signature Abolition of Slavery Database generator — jahdb-abolition-slavery-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ABOLSLS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Slavery and Abolition: An Overview (Signature Edition)", "The Transatlantic Slave Trade (Signature Edition)", "The Middle Passage (Signature Edition)", "Plantation Slavery (Signature Edition)", "The Quakers and Early Abolition (Signature Edition)", "Olaudah Equiano (Signature Edition)", "William Wilberforce (Signature Edition)", "Thomas Clarkson (Signature Edition)", "The Haitian Revolution (Signature Edition)", "Toussaint Louverture (Signature Edition)", "Frederick Douglass (Signature Edition)"], "Compounded": ["The Underground Railroad (Signature Edition)", "Harriet Tubman (Signature Edition)", "John Brown (Signature Edition)", "The 13th Amendment (Signature Edition)", "Britain Abolishes Slavery (1833) (Signature Edition)", "The Amistad Case (1839-41) (Signature Edition)", "Uncle Tom's Cabin (1852) (Signature Edition)", "The Liberator and Abolitionist Press (Signature Edition)", "Nat Turner's Rebellion (1831) (Signature Edition)", "The West Africa Squadron (Signature Edition)", "Brazil: The Last Abolition (1888) (Signature Edition)", "The Economics of Abolition (Signature Edition)"], "Advanced": ["Slavery in the Ancient World (Signature Edition)", "Slavery in the Islamic World (Signature Edition)", "The Internal African Trades (Signature Edition)", "The Slave Trade Act 1807 (Signature Edition)", "Sierra Leone: The Resettlement (Signature Edition)", "Lincoln and Emancipation (Signature Edition)", "The Emancipation Proclamation (Signature Edition)", "Reconstruction and Its Betrayal (Signature Edition)", "Modern Slavery (Signature Edition)", "Reparations: The Unfinished Debate (Signature Edition)", "Convict Leasing: Slavery by Another Name (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — abolition-slavery-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — abolition record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A abolition record of "'+topic+'" in '+field+'. Signature original sample are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:false,
    signature_label:'Signature original - created in the Signature system; not a public record.',
    disclaimer:'Signature original sample — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"abolition-slavery-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-abolition-slavery-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("abolition-slavery-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
