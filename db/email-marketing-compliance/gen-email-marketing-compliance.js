(function(){'use strict';
/* JAH The Email Marketing Compliance Database generator — jahdb-email-marketing-compliance-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EMC-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Email Marketing Compliance: Defining Your Offer Clearly — foundations",
  "Email Marketing Compliance: Knowing Your Customer — foundations",
  "Email Marketing Compliance: Pricing That Holds — foundations",
  "Email Marketing Compliance: The Interview Conversation — foundations",
  "Email Marketing Compliance: Proposals That Win — foundations",
  "Email Marketing Compliance: Quotes and Estimates — foundations",
  "Email Marketing Compliance: Contracts in Plain Terms — foundations",
  "Email Marketing Compliance: Invoicing and Getting Paid — foundations",
  "Email Marketing Compliance: Email Marketing Basics — foundations",
  "Email Marketing Compliance: CAN-SPAM Compliance — foundations",
  "Email Marketing Compliance: Following Up Systematically — foundations",
  "Email Marketing Compliance: Handling Objections — foundations"
 ],
 "compounded": [
  "Email Marketing Compliance: Delivering Great Service — compounded",
  "Email Marketing Compliance: Asking for Reviews and Referrals — compounded",
  "Email Marketing Compliance: Basic Bookkeeping — compounded",
  "Email Marketing Compliance: Cash Flow Management — compounded",
  "Email Marketing Compliance: Hiring Your First Help — compounded",
  "Email Marketing Compliance: Time Management for Owners — compounded",
  "Email Marketing Compliance: Marketing on a Small Budget — compounded",
  "Email Marketing Compliance: Handling Difficult Customers — compounded",
  "Email Marketing Compliance: Legal Basics for Small Business — compounded",
  "Email Marketing Compliance: Tax Basics for Small Business — compounded",
  "Email Marketing Compliance: Advanced: Scaling Operations — compounded",
  "Email Marketing Compliance: Advanced: Strategic Partnerships — compounded"
 ],
 "advanced": [
  "Email Marketing Compliance: Advanced: Pricing Power — advanced",
  "Email Marketing Compliance: Advanced: Building a Brand — advanced",
  "Email Marketing Compliance: Advanced: Exit and Succession — advanced",
  "Email Marketing Compliance: Advanced: Advanced Marketing Systems — advanced",
  "Email Marketing Compliance: Advanced: Financial Mastery — advanced",
  "Email Marketing Compliance: Advanced: Leading a Team — advanced",
  "Email Marketing Compliance: Advanced: Innovation on Purpose — advanced",
  "Email Marketing Compliance: Advanced: Crisis Management — advanced",
  "Email Marketing Compliance: Advanced: Giving Back Profitably — advanced",
  "Email Marketing Compliance: Advanced: The 10-Year Vision — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Email Marketing Compliance Database — structural study\n"
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
    name:topic+' — practical guidance record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A practical guidance record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-email-marketing-compliance-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('email-marketing-compliance',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
