(function(){'use strict';
/* JAH Community Arts Resource Finder Database generator — jahdb-community-arts-resource-finder-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-COMMARFS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Arts Councils (Signature Edition)", "Arts Grants (Signature Edition)", "Community Venues (Signature Edition)", "Art Classes (Signature Edition)", "Public Art (Signature Edition)", "Local Artists (Signature Edition)", "Youth Arts (Signature Edition)", "Arts Volunteering (Signature Edition)", "Teaching Arts Discovery (Signature Edition)", "The Annual Arts Review (Signature Edition)", "Finding Funding (Signature Edition)"], "Compounded": ["Artist Residencies (Signature Edition)", "Art in Public Spaces (Signature Edition)", "Community Theaters (Signature Edition)", "Community Music (Signature Edition)", "Dance Communities (Signature Edition)", "Literary Communities (Signature Edition)", "Film Communities (Signature Edition)", "Craft Communities (Signature Edition)", "Cultural Festivals (Signature Edition)", "Arts Education (Signature Edition)", "Art Therapy (Signature Edition)", "Digital Arts (Signature Edition)"], "Advanced": ["Photography Clubs (Signature Edition)", "Art Markets (Signature Edition)", "Public Libraries (Signature Edition)", "Faith and Arts (Signature Edition)", "Senior Arts (Signature Edition)", "Disability Arts (Signature Edition)", "Rural Arts (Signature Edition)", "Arts Journalism (Signature Edition)", "Preserving Traditions (Signature Edition)", "Starting Arts Groups (Signature Edition)", "The Creative Life (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — arts directory demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — arts directory',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A arts directory of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"community-arts-resource-finder-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-community-arts-resource-finder-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("community-arts-resource-finder-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
