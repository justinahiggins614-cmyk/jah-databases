(function(){'use strict';
/* JAH The 1960s Database generator — jahdb-decades-1960s-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-D1960-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The 1960s at a Glance: The Decade That Broke the Mold - Foundations",
  "1960: The First Televised Presidential Debate - Foundations",
  "1961: The Bay of Pigs - Foundations",
  "1961: Gagarin \u2014 the First Human in Space - Foundations",
  "1961: The Berlin Wall Goes Up - Foundations",
  "1962: The Cuban Missile Crisis - Foundations",
  "1963: The March on Washington - Foundations",
  "1963: Kennedy Is Assassinated - Foundations",
  "1964: The Civil Rights Act - Foundations",
  "1965: The Voting Rights Act - Foundations"
 ],
 "Compounded": [
  "1960: The Birth Control Pill Is Approved - Compounded",
  "1960: The Laser Fires for the First Time - Compounded",
  "1961: Shepard \u2014 the First American in Space - Compounded",
  "1962: Telstar \u2014 Television from Space - Compounded",
  "1963: Tereshkova \u2014 the First Woman in Space - Compounded",
  "1964: The Beatles Conquer America - Compounded",
  "1965: The First Spacewalk - Compounded",
  "1965: Watts Burns - Compounded",
  "1966: Star Trek Premieres - Compounded",
  "1967: The First Super Bowl - Compounded",
  "1967: The First Heart Transplant - Compounded"
 ],
 "Advanced": [
  "1968: The Tet Offensive - Advanced",
  "1968: Martin Luther King Jr. Is Assassinated - Advanced",
  "1968: Robert Kennedy Is Assassinated - Advanced",
  "1968: Apollo 8 \u2014 Earthrise - Advanced",
  "1969: Apollo 11 Lands on the Moon - Advanced",
  "1969: Woodstock - Advanced",
  "1969: Stonewall \u2014 the Birth of Gay Liberation - Advanced",
  "1969: ARPANET \u2014 the Internet's First Message - Advanced",
  "1969: Sesame Street Premieres - Advanced",
  "1962: The First Walmart Opens - Advanced",
  "1967: The First ATM - Advanced",
  "1964: The Gulf of Tonkin Resolution - Advanced",
  "1963: The Feminine Mystique Ignites Feminism - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# 1960S — "+safe+"\n"
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
    name:topic+' — 1960s history record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A 1960s history record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"decades-1960s-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-decades-1960s-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('decades-1960s',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
