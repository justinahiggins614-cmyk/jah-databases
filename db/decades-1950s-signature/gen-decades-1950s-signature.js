(function(){'use strict';
/* JAH The 1950s Signature Database generator — jahdb-decades-1950s-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-D1950S-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The 1950s at a Glance: Boom, Bomb, and the Cold War (Signature Edition) - Foundations",
  "1950: The Korean War Begins (Signature Edition) - Foundations",
  "1953: The Double Helix \u2014 DNA's Structure Revealed (Signature Edition) - Foundations",
  "1953: Stalin Dies (Signature Edition) - Foundations",
  "1954: Brown v. Board of Education (Signature Edition) - Foundations",
  "1955: The Polio Vaccine Is Declared Safe (Signature Edition) - Foundations",
  "1955: The Montgomery Bus Boycott Begins (Signature Edition) - Foundations",
  "1955: Disneyland Opens (Signature Edition) - Foundations",
  "1956: The Interstate Highway System Is Authorized (Signature Edition) - Foundations",
  "1957: Sputnik Shocks the World (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "1950: McCarthy Launches the Red Scare (Signature Edition) - Compounded",
  "1952: The First Hydrogen Bomb (Signature Edition) - Compounded",
  "1953: Everest Is Conquered (Signature Edition) - Compounded",
  "1953: The Korean War Ends in Armistice (Signature Edition) - Compounded",
  "1954: The First Nuclear Power Plant (Signature Edition) - Compounded",
  "1955: The Warsaw Pact Is Signed (Signature Edition) - Compounded",
  "1956: The Suez Crisis (Signature Edition) - Compounded",
  "1956: The Hungarian Revolution (Signature Edition) - Compounded",
  "1957: FORTRAN \u2014 the First Programming Language (Signature Edition) - Compounded",
  "1958: NASA Is Founded (Signature Edition) - Compounded",
  "1958: The Modern LEGO Brick (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "1959: Castro Takes Cuba (Signature Edition) - Advanced",
  "1959: Barbie Debuts (Signature Edition) - Advanced",
  "1958: The Integrated Circuit (Signature Edition) - Advanced",
  "1950: The First Credit Card (Signature Edition) - Advanced",
  "1952: The First Holiday Inn (Signature Edition) - Advanced",
  "1954: The First Successful Organ Transplant (Signature Edition) - Advanced",
  "1955: Ray Kroc Opens His First McDonald's Franchise (Signature Edition) - Advanced",
  "1956: Elvis Shakes Up Ed Sullivan (Signature Edition) - Advanced",
  "1957: The Asian Flu Pandemic (Signature Edition) - Advanced",
  "1959: Luna 2 Reaches the Moon (Signature Edition) - Advanced",
  "1953: Color Television Is Approved (Signature Edition) - Advanced",
  "1951: The First Electricity from Nuclear Power (Signature Edition) - Advanced",
  "1959: The Kitchen Debate (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# 1950S — "+safe+"\n"
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
    name:topic+' — 1950s history record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A 1950s history record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"decades-1950s-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-decades-1950s-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('decades-1950s-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
