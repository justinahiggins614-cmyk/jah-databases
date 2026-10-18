(function(){'use strict';
/* JAH The Community Challenge Database Database generator — jahdb-db-community-challenge-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-COMCHA-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Challenge: The Porch Light Welcome",
  "Challenge: The Litter Sweep",
  "Challenge: The Food Drive Sprint",
  "Challenge: The Senior Check-In",
  "Challenge: The Little Library",
  "Challenge: The Sidewalk Chalk Day",
  "Challenge: The Lost Pet Network",
  "Challenge: The Garden Share",
  "Challenge: The Storm Prep Buddy",
  "Challenge: The Book Swap",
  "Challenge: The Welcome Basket"
 ],
 "Compounded": [
  "Challenge: The Block Party",
  "Challenge: The Community Garden",
  "Challenge: The Tutoring Circle",
  "Challenge: The Tool Library",
  "Challenge: The Mural Project",
  "Challenge: The Night Watch",
  "Challenge: The Repair Cafe",
  "Challenge: The History Walk",
  "Challenge: The Playground Build",
  "Challenge: The Language Table",
  "Challenge: The Seed Bank",
  "Challenge: The Choir Flash"
 ],
 "Advanced": [
  "Challenge: The Vacant Lot Transformation",
  "Challenge: The Mutual Aid Network",
  "Challenge: The Youth Council",
  "Challenge: The Emergency Plan",
  "Challenge: The Co-op Store",
  "Challenge: The Scholarship Fund",
  "Challenge: The Oral History Project",
  "Challenge: The Green Corridor",
  "Challenge: The Time Bank",
  "Challenge: The Festival",
  "Challenge: The Legacy Project"
 ]
};
var DEMOKIND="mission-proof";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Community Challenge Study — "+safe+"\n"
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
    name:topic+' — community challenge record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A community challenge record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:DEMOKIND,language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-community-challenge-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-community-challenge',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
