(function(){'use strict';
/* JAH Personal Resource Finder Database generator — jahdb-personal-resource-finder-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PERSRFS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Defining the Need (Signature Edition)", "Calling 211 (Signature Edition)", "The Public Library (Signature Edition)", "Community Centers (Signature Edition)", "Faith Community Resources (Signature Edition)", "Mutual Aid Networks (Signature Edition)", "Free Clinics and Health Fairs (Signature Edition)", "Food Resources (Signature Edition)", "Housing Assistance (Signature Edition)", "Utility Assistance (Signature Edition)", "Transportation Resources (Signature Edition)"], "Compounded": ["Job Search Resources (Signature Edition)", "Legal Aid Clinics (Signature Edition)", "Childcare Resources (Signature Edition)", "Senior Services (Signature Edition)", "Disability Resources (Signature Edition)", "Mental Health Resources (Signature Edition)", "Substance Use Resources (Signature Edition)", "Veteran Resources (Signature Edition)", "Immigrant and Refugee Services (Signature Edition)", "Language and Literacy Programs (Signature Edition)", "Tax Preparation Help (Signature Edition)", "Financial Counseling (Signature Edition)"], "Advanced": ["Small Business Resources (Signature Edition)", "Tool Libraries (Signature Edition)", "Clothing Resources (Signature Edition)", "Technology Access (Signature Edition)", "Recreation Access (Signature Edition)", "Volunteer Matching (Signature Edition)", "Neighborhood Associations (Signature Edition)", "Religious and Cultural Organizations (Signature Edition)", "Emergency Preparedness Resources (Signature Edition)", "Building Your Personal Directory (Signature Edition)", "The Annual Resource Audit (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — resource guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — resource guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A resource guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"personal-resource-finder-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-personal-resource-finder-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("personal-resource-finder-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
