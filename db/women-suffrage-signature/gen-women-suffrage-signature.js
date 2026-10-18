(function(){'use strict';
/* JAH Signature Women Suffrage Database generator — jahdb-women-suffrage-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WOMSUFS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Women's Suffrage: An Overview (Signature Edition)", "Seneca Falls 1848 (Signature Edition)", "Susan B. Anthony (Signature Edition)", "Elizabeth Cady Stanton (Signature Edition)", "Sojourner Truth (Signature Edition)", "The 19th Amendment (Signature Edition)", "The Pankhursts and the WSPU (Signature Edition)", "New Zealand 1893: First in the World (Signature Edition)", "Alice Paul and the NWP (Signature Edition)", "The Hunger Strikes (Signature Edition)", "Wyoming 1869: The Equality State (Signature Edition)"], "Compounded": ["The Anti-Suffrage Opposition (Signature Edition)", "Suffrage and Race (Signature Edition)", "Ida B. Wells (Signature Edition)", "The State-by-State Campaigns (Signature Edition)", "World War I and the Vote (Signature Edition)", "The Suffrage Press (Signature Edition)", "Suffrage Tactics: Parades and Pickets (Signature Edition)", "The 1913 Washington Parade (Signature Edition)", "Suffrage and Labor (Signature Edition)", "Suffrage and Temperance (Signature Edition)", "The International Wave (Signature Edition)", "After 1920: The Unfinished Vote (Signature Edition)"], "Advanced": ["Frances Willard and the WCTU (Signature Edition)", "Lucy Stone and the AWSA (Signature Edition)", "Matilda Joslyn Gage (Signature Edition)", "The Equal Rights Amendment (1923) (Signature Edition)", "Carrie Chapman Catt (Signature Edition)", "Suffragette Tactics in Detail (Signature Edition)", "Suffrage Art and Propaganda (Signature Edition)", "The Men's Leagues (Signature Edition)", "The Ratification Battle: Tennessee (Signature Edition)", "Scandinavian Suffrage (Signature Edition)", "From Suffrage to Feminism (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — women-suffrage-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — suffrage record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A suffrage record of "'+topic+'" in '+field+'. Signature original sample are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:false,
    signature_label:'Signature original - created in the Signature system; not a public record.',
    disclaimer:'Signature original sample — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"women-suffrage-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-women-suffrage-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("women-suffrage-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
