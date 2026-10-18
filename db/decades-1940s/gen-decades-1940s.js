(function(){'use strict';
/* JAH The 1940s Database generator — jahdb-decades-1940s-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-D1940-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The 1940s at a Glance: World War and the Atomic Age - Foundations",
  "1940: The Fall of France - Foundations",
  "1940: The Battle of Britain - Foundations",
  "1941: Lend-Lease Arms the Allies - Foundations",
  "1941: Pearl Harbor - Foundations",
  "1942: The Battle of Midway - Foundations",
  "1943: Stalingrad \u2014 the Tide Turns in Europe - Foundations",
  "1944: D-Day \u2014 the Normandy Landings - Foundations",
  "1945: Roosevelt Dies; Truman Takes Command - Foundations",
  "1945: V-E Day \u2014 Victory in Europe - Foundations"
 ],
 "Compounded": [
  "1945: Hiroshima \u2014 the Atomic Age Begins - Compounded",
  "1945: Nagasaki and the Surrender of Japan - Compounded",
  "1945: The United Nations Is Founded - Compounded",
  "1945: The Nuremberg Trials Begin - Compounded",
  "1946: ENIAC \u2014 the First General-Purpose Computer - Compounded",
  "1946: Churchill Declares an Iron Curtain - Compounded",
  "1947: Jackie Robinson Breaks Baseball's Color Barrier - Compounded",
  "1947: The Dead Sea Scrolls Are Discovered - Compounded",
  "1947: Chuck Yeager Shatters the Sound Barrier - Compounded",
  "1947: The Transistor Is Invented - Compounded",
  "1948: Israel Is Founded - Compounded"
 ],
 "Advanced": [
  "1948: The Berlin Airlift Begins - Advanced",
  "1945: Auschwitz Is Liberated - Advanced",
  "1949: NATO Is Founded - Advanced",
  "1949: The People's Republic of China Is Proclaimed - Advanced",
  "1949: The Soviet Union Detonates Its First Atomic Bomb - Advanced",
  "1945: The Microwave Oven Is Invented - Advanced",
  "1944: Bretton Woods Designs the Postwar Economy - Advanced",
  "1944: The Battle of the Bulge - Advanced",
  "1945: Japan Formally Surrenders - Advanced",
  "1947: The CIA Is Founded - Advanced",
  "1948: The Marshall Plan Rebuilds Europe - Advanced",
  "1949: The 'Big Bang' Gets Its Name - Advanced",
  "1940: The First McDonald's Opens - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# 1940S — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
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
    name:topic+' — 1940s history record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A 1940s history record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"decades-1940s-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-decades-1940s-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('decades-1940s',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
