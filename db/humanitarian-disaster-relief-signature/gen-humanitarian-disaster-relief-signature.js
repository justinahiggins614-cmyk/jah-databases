(function(){'use strict';
/* JAH The Humanitarian Disaster Relief Signature Database generator — jahdb-humanitarian-disaster-relief-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HUMRELIEF-SIG-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Disaster Declaration Process (Signature Edition)", "Emergency Operations Centers (EOC) (Signature Edition)", "Incident Command System (ICS) (Signature Edition)", "Search and Rescue Operations (Signature Edition)", "Emergency Sheltering (Signature Edition)", "Mass Feeding Operations (Signature Edition)", "Emergency First Aid Stations (Signature Edition)", "Evacuation Planning (Signature Edition)", "Emergency Alert Systems (WEA/IPAWS) (Signature Edition)", "Damage Assessment: Windshield Surveys (Signature Edition)", "Community Emergency Response Teams (CERT) (Signature Edition)", "Disaster Recovery Centers (Signature Edition)"], "Compounded": ["Humanitarian Supply Chains (Signature Edition)", "Last-Mile Logistics (Signature Edition)", "Water, Sanitation, and Hygiene (WASH) (Signature Edition)", "Emergency Medical Teams (Signature Edition)", "Field Hospitals (Signature Edition)", "Temporary Housing Programs (Signature Edition)", "Debris Management (Signature Edition)", "Volunteer Coordination (Signature Edition)", "Donations Management (Signature Edition)", "Psychological First Aid (Signature Edition)", "Animal Sheltering in Disasters (Signature Edition)", "Power Restoration Coordination (Signature Edition)"], "Advanced": ["Post-Disaster Needs Assessment (PDNA) (Signature Edition)", "The UN Cluster Coordination System (Signature Edition)", "Sphere Humanitarian Standards (Signature Edition)", "Cash and Voucher Assistance (Signature Edition)", "Early Recovery Planning (Signature Edition)", "Build Back Better (Signature Edition)", "Disaster Risk Reduction (Signature Edition)", "Contingency Stockpiles (Signature Edition)", "Civil-Military Coordination (Signature Edition)", "Accountability to Affected Populations (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Disaster Relief Study — "+safe+"\n"
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
    name:topic+' — disaster relief record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A disaster relief record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"relief-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-humanitarian-disaster-relief-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("humanitarian-disaster-relief-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
