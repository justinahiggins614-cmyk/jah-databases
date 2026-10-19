(function(){'use strict';
/* JAH Signature World War II Database generator — "jahdb-history-world-war-ii-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HWWS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["World War II: An Overview (Signature Edition)", "The Road to War: Versailles to 1939 (Signature Edition)", "Hitler and the Nazi State (Signature Edition)", "Blitzkrieg (Signature Edition)", "The Battle of Britain (1940) (Signature Edition)", "Barbarossa and the Eastern Front (Signature Edition)", "Pearl Harbor (Signature Edition)", "D-Day (1944) (Signature Edition)", "The Pacific War (Signature Edition)", "The Holocaust (Signature Edition)", "The Home Fronts (Signature Edition)", "1945: The End and the Aftermath (Signature Edition)"], "Compounded": ["Churchill (Signature Edition)", "Roosevelt (Signature Edition)", "Stalin (Signature Edition)", "Stalingrad (Signature Edition)", "The Generals (Signature Edition)", "The Battle of the Atlantic (Signature Edition)", "The Strategic Bombing Campaign (Signature Edition)", "The Manhattan Project (Signature Edition)", "The Resistance (Signature Edition)", "The Codebreakers: Bletchley Park (Signature Edition)", "Leningrad: The 872-Day Siege (Signature Edition)", "The Endgames: Bulge, Iwo Jima, Berlin (Signature Edition)"], "Advanced": ["Nuremberg: Justice After War (Signature Edition)", "The War's Technology (Signature Edition)", "Women at War (Signature Edition)", "Deception: Fortitude and Double Cross (Signature Edition)", "Asia After the War (Signature Edition)", "The Memory of the War (Signature Edition)", "The Economics of Peace (Signature Edition)", "1942: The Hinge Year (Signature Edition)", "What If: The Counterfactuals (Signature Edition)", "The Legacy: The Institutions (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — history-world-war-ii-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
   + "TOPIC = \""+safe+"\"\n"
   + "FIELD = \""+field+"\"\n"
   + "def summarize():\n"
   + "    return TOPIC + ' [' + FIELD + ']'\n"
   + "print(summarize())\n"
   + "print('Signature sample — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — Signature-original history record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature-original history record study. Signature original samples are clearly labeled and never presented as archive records.",
    field:field,
    src:"signature-sample",
    sample:true,
    disclaimer:"Generated Signature sample \u2014 not an archive record. Seeded archive records are the authoritative entries.",
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
var gen={version:"jahdb-history-world-war-ii-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("history-world-war-ii-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
