(function(){'use strict';
/* JAH The 1940s Signature Database generator — jahdb-decades-1940s-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-D1940S-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The 1940s at a Glance: World War and the Atomic Age (Signature Edition) - Foundations",
  "1940: The Fall of France (Signature Edition) - Foundations",
  "1940: The Battle of Britain (Signature Edition) - Foundations",
  "1941: Lend-Lease Arms the Allies (Signature Edition) - Foundations",
  "1941: Pearl Harbor (Signature Edition) - Foundations",
  "1942: The Battle of Midway (Signature Edition) - Foundations",
  "1943: Stalingrad \u2014 the Tide Turns in Europe (Signature Edition) - Foundations",
  "1944: D-Day \u2014 the Normandy Landings (Signature Edition) - Foundations",
  "1945: Roosevelt Dies; Truman Takes Command (Signature Edition) - Foundations",
  "1945: V-E Day \u2014 Victory in Europe (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "1945: Hiroshima \u2014 the Atomic Age Begins (Signature Edition) - Compounded",
  "1945: Nagasaki and the Surrender of Japan (Signature Edition) - Compounded",
  "1945: The United Nations Is Founded (Signature Edition) - Compounded",
  "1945: The Nuremberg Trials Begin (Signature Edition) - Compounded",
  "1946: ENIAC \u2014 the First General-Purpose Computer (Signature Edition) - Compounded",
  "1946: Churchill Declares an Iron Curtain (Signature Edition) - Compounded",
  "1947: Jackie Robinson Breaks Baseball's Color Barrier (Signature Edition) - Compounded",
  "1947: The Dead Sea Scrolls Are Discovered (Signature Edition) - Compounded",
  "1947: Yeager Breaks the Sound Barrier (Signature Edition) - Compounded",
  "1947: The Transistor Is Invented (Signature Edition) - Compounded",
  "1948: Israel Is Founded (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "1948: The Berlin Airlift Begins (Signature Edition) - Advanced",
  "1945: Auschwitz Is Liberated (Signature Edition) - Advanced",
  "1949: NATO Is Founded (Signature Edition) - Advanced",
  "1949: The People's Republic of China Is Proclaimed (Signature Edition) - Advanced",
  "1949: The Soviet Union Detonates Its First Atomic Bomb (Signature Edition) - Advanced",
  "1945: The Microwave Oven Is Invented (Signature Edition) - Advanced",
  "1944: Bretton Woods Designs the Postwar Economy (Signature Edition) - Advanced",
  "1944: The Battle of the Bulge (Signature Edition) - Advanced",
  "1945: Japan Formally Surrenders (Signature Edition) - Advanced",
  "1947: The CIA Is Founded (Signature Edition) - Advanced",
  "1948: The Marshall Plan Rebuilds Europe (Signature Edition) - Advanced",
  "1949: The 'Big Bang' Gets Its Name (Signature Edition) - Advanced",
  "1940: The First McDonald's Opens (Signature Edition) - Advanced"
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
var gen={version:'jahdb-decades-1940s-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('decades-1940s-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
