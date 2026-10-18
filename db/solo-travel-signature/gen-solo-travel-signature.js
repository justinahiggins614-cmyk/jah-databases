(function(){'use strict';
/* JAH Solo Travel Database generator — jahdb-solo-travel-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SOTRS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Solo Travel?",
  "Why Travel Alone",
  "Best Destinations for First-Time Solo Travelers",
  "Solo Travel Safety Foundations",
  "Staying Connected: Check-Ins and Contacts",
  "Meeting People on the Road",
  "Dining Alone, Confidently",
  "Solo Accommodation Choices",
  "The Solo Travel Budget",
  "Packing Solo",
  "Solo Travel Mindset"
 ],
 "Compounded": [
  "Solo Female Travel Foundations",
  "Navigating Nightlife Solo, Safely",
  "Solo Road Trips",
  "Solo Hiking Safety",
  "Group Tours for Solo Travelers",
  "Cruises for Solo Travelers",
  "Solo Travel Photography",
  "Journaling the Solo Journey",
  "Handling Loneliness on the Road",
  "Solo Travel Scams to Know",
  "Travel Insurance for Solo Travelers",
  "The Solo Sabbatical"
 ],
 "Advanced": [
  "Advanced: Solo Travel in Remote Regions",
  "Advanced: The One-Year Solo Journey",
  "Advanced: Solo Travel as a Lifestyle",
  "Advanced: Teaching Solo Travel",
  "Advanced: Solo Travel Content Creation",
  "Advanced: The Solo Travel Index",
  "Advanced: Volunteering Solo Abroad",
  "Advanced: Solo Travel in Your 60s+",
  "Advanced: The Solo Travel Memoir",
  "Advanced: Giving Back on the Road",
  "The Solo Travel Encyclopedia"
 ]
};
var DEMOKIND="node-demo";
var SAMPLEDESC="Sample records are complete solo travel record entries with real measurement math.";
function demoProgram(topic,field){
  return "'use strict';\n// "+topic+" \u2014 sample demo.\n// Field: "+field+"\nconst a = 12;\nconst b = 4;\nconst r = a / b;\nconsole.log('sample ratio = ' + r.toFixed(2));\nif (!isFinite(r)) throw new Error('bad');\nconsole.log('DEMO_OK');\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — solo travel record record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A solo travel record record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:DEMOKIND,language:'node',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-solo-travel-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('solo-travel-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
