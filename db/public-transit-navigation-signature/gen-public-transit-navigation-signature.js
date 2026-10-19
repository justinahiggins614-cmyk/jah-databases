(function(){'use strict';
/* JAH Public Transit Navigation Database generator — jahdb-public-transit-navigation-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PUBLTNS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Reading Transit Maps (Signature Edition)", "Trip Planning Apps (Signature Edition)", "Fare Systems (Signature Edition)", "Bus Riding (Signature Edition)", "Subway and Rail (Signature Edition)", "Transfers (Signature Edition)", "Schedules (Signature Edition)", "Service Disruptions (Signature Edition)", "Rush Hour (Signature Edition)", "Night Service (Signature Edition)", "Accessibility (Signature Edition)"], "Compounded": ["Safety (Signature Edition)", "Etiquette (Signature Edition)", "Bikes on Transit (Signature Edition)", "Transit and Errands (Signature Edition)", "New City Transit (Signature Edition)", "Teaching Transit (Signature Edition)", "The Annual Transit Review (Signature Edition)", "Fare Evasion (Signature Edition)", "Transit Apps Compared (Signature Edition)", "Rush Hour Alternatives (Signature Edition)", "Transit Delays (Signature Edition)", "Lost and Found (Signature Edition)"], "Advanced": ["Transit Police (Signature Edition)", "Senior Discounts (Signature Edition)", "Student Passes (Signature Edition)", "Employer Benefits (Signature Edition)", "Transit-Oriented Living (Signature Edition)", "Intercity Buses (Signature Edition)", "Amtrak Basics (Signature Edition)", "Paratransit (Signature Edition)", "Transit Advocacy (Signature Edition)", "The Car-Free Budget (Signature Edition)", "Multimodal Trips (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — transit guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — transit guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A transit guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"public-transit-navigation-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-public-transit-navigation-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("public-transit-navigation-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
