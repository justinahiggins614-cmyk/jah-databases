(function(){'use strict';
/* JAH Professional Networking Database generator — jahdb-professional-networking-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PROFNS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Networking Mindset (Signature Edition)", "Your One-Line Introduction (Signature Edition)", "Informational Interviews (Signature Edition)", "LinkedIn Fundamentals (Signature Edition)", "The Follow-Up System (Signature Edition)", "Giving Value First (Signature Edition)", "Networking for Introverts (Signature Edition)", "Industry Events (Signature Edition)", "Online Communities (Signature Edition)", "Alumni Networks (Signature Edition)", "Mentor Relationships (Signature Edition)"], "Compounded": ["Peer Networks (Signature Edition)", "Networking During Job Search (Signature Edition)", "The Thank-You Habit (Signature Edition)", "Staying in Touch (Signature Edition)", "Networking Across Industries (Signature Edition)", "Personal Branding Basics (Signature Edition)", "Elevator Pitches (Signature Edition)", "Conference Strategy (Signature Edition)", "Coffee Chat Mastery (Signature Edition)", "Referral Mechanics (Signature Edition)", "Networking While Employed (Signature Edition)", "Rebuilding After a Gap (Signature Edition)"], "Advanced": ["Cultural Networking Differences (Signature Edition)", "Measuring Network Health (Signature Edition)", "Giving Back (Signature Edition)", "Digital Presence Audit (Signature Edition)", "The Annual Networking Plan (Signature Edition)", "Networking Burnout (Signature Edition)", "Long-Distance Networking (Signature Edition)", "The Lifetime Network (Signature Edition)", "Volunteering as Networking (Signature Edition)", "Content-Based Networking (Signature Edition)", "The Networking CRM (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — networking guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — networking guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A networking guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"professional-networking-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-professional-networking-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("professional-networking-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
