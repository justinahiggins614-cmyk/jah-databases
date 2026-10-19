(function(){'use strict';
/* JAH Small Business Marketing Playbook Database generator — jahdb-small-business-marketing-playbook-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SMALBMPS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Positioning Basics (Signature Edition)", "Google Business Profile (Signature Edition)", "Review Strategy (Signature Edition)", "Local SEO (Signature Edition)", "Your Website (Signature Edition)", "Social Media Strategy (Signature Edition)", "Content Marketing (Signature Edition)", "Email Marketing (Signature Edition)", "Referral Programs (Signature Edition)", "Word of Mouth (Signature Edition)", "Networking (Signature Edition)"], "Compounded": ["Community Involvement (Signature Edition)", "Paid Advertising (Signature Edition)", "Direct Mail (Signature Edition)", "Signage (Signature Edition)", "Promotions and Offers (Signature Edition)", "Loyalty Programs (Signature Edition)", "Customer Service as Marketing (Signature Edition)", "Photography and Visuals (Signature Edition)", "Video Marketing (Signature Edition)", "Partnerships (Signature Edition)", "Event Marketing (Signature Edition)", "Public Relations (Signature Edition)"], "Advanced": ["Measuring Marketing (Signature Edition)", "Marketing Budget (Signature Edition)", "Branding Basics (Signature Edition)", "Seasonal Marketing (Signature Edition)", "Crisis Communication (Signature Edition)", "Competitor Awareness (Signature Edition)", "Online Directories (Signature Edition)", "Teaching Marketing (Signature Edition)", "The Annual Marketing Review (Signature Edition)", "Hiring Marketing Help (Signature Edition)", "Marketing on Zero Budget (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — marketing guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — marketing guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A marketing guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"small-business-marketing-playbook-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-small-business-marketing-playbook-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("small-business-marketing-playbook-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
