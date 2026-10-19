(function(){'use strict';
/* JAH Creative Commons License Reference Database generator — jahdb-creative-commons-license-reference-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CREACLRS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Four Elements (Signature Edition)", "CC BY (Signature Edition)", "CC BY-SA (Signature Edition)", "CC BY-NC (Signature Edition)", "CC BY-ND (Signature Edition)", "The NC Combinations (Signature Edition)", "CC0 Public Domain (Signature Edition)", "Choosing a License (Signature Edition)", "Attribution (Signature Edition)", "Remixing (Signature Edition)", "Finding CC Works (Signature Edition)"], "Compounded": ["Teaching CC (Signature Edition)", "The License Review (Signature Edition)", "License Compatibility Chart (Signature Edition)", "Commercial Use Defined (Signature Edition)", "Moral Rights (Signature Edition)", "CC and Fair Use (Signature Edition)", "Institutional Policies (Signature Edition)", "CC for Educators (Signature Edition)", "CC for Scientists (Signature Edition)", "CC for Musicians (Signature Edition)", "CC for Photographers (Signature Edition)", "CC for Writers (Signature Edition)"], "Advanced": ["Enforcing CC Licenses (Signature Edition)", "CC License Versions (Signature Edition)", "Public Domain Marks (Signature Edition)", "CC Plus (Signature Edition)", "Orphan Works (Signature Edition)", "CC in AI Training (Signature Edition)", "International CC (Signature Edition)", "The Commons Community (Signature Edition)", "License Migration (Signature Edition)", "The Sharing Audit (Signature Edition)", "Future of Open (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — license reference demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — license reference',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A license reference of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"creative-commons-license-reference-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-creative-commons-license-reference-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("creative-commons-license-reference-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
