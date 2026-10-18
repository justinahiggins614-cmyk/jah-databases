(function(){'use strict';
/* JAH Passport and Visa Guide Database generator — jahdb-passport-visa-guide-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PSVSS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is a Passport?",
  "Getting Your First Passport",
  "Passport Renewal, Explained",
  "Passport Photos: The Rules",
  "What Is a Visa?",
  "Visa-Free Travel, Explained",
  "The Six-Month Passport Validity Rule",
  "Blank Pages and Entry Requirements",
  "Traveling with Children: Passport Rules",
  "Lost or Stolen Passports Abroad",
  "Passport Cards vs Passport Books"
 ],
 "Compounded": [
  "ETIAS: Europe’s Travel Authorization",
  "The US ESTA, Explained",
  "E-Visas and Visa on Arrival",
  "The Schengen 90/180 Rule",
  "Work Visas vs Tourist Visas",
  "Dual Citizenship and Travel",
  "Passport Processing Times and Expediting",
  "Visas for Long Stays",
  "Travel to Countries with Entry Restrictions",
  "The Global Entry Program",
  "TSA PreCheck and Trusted Traveler Programs",
  "Keeping Copies of Travel Documents"
 ],
 "Advanced": [
  "Advanced: Second Passports",
  "Advanced: The Passport Power Index",
  "Advanced: Citizenship by Investment",
  "Advanced: Traveling on a Refugee Travel Document",
  "Advanced: Visa Runs and Border Runs",
  "Advanced: The Document Security System",
  "Advanced: Teaching Document Prep",
  "Advanced: Emergency Travel Documents",
  "Advanced: The 10-Year Document Plan",
  "Advanced: Diplomatic and Official Passports",
  "The Passport and Visa Encyclopedia"
 ]
};
var DEMOKIND="node-demo";
var SAMPLEDESC="Sample records are complete passport and visa record entries with real measurement math.";
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
    name:topic+' — passport and visa record record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A passport and visa record record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-passport-visa-guide-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('passport-visa-guide-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
