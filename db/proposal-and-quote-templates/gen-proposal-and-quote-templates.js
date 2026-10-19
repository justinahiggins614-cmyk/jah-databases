(function(){'use strict';
/* JAH The Proposal and Quote Templates Database generator — jahdb-proposal-and-quote-templates-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PAQT-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Proposal and Quote Templates: Defining Your Offer Clearly — foundations",
  "Proposal and Quote Templates: Knowing Your Customer — foundations",
  "Proposal and Quote Templates: Pricing That Holds — foundations",
  "Proposal and Quote Templates: The Interview Conversation — foundations",
  "Proposal and Quote Templates: Proposals That Win — foundations",
  "Proposal and Quote Templates: Quotes and Estimates — foundations",
  "Proposal and Quote Templates: Contracts in Plain Terms — foundations",
  "Proposal and Quote Templates: Invoicing and Getting Paid — foundations",
  "Proposal and Quote Templates: Email Marketing Basics — foundations",
  "Proposal and Quote Templates: CAN-SPAM Compliance — foundations",
  "Proposal and Quote Templates: Following Up Systematically — foundations",
  "Proposal and Quote Templates: Handling Objections — foundations"
 ],
 "compounded": [
  "Proposal and Quote Templates: Delivering Great Service — compounded",
  "Proposal and Quote Templates: Asking for Reviews and Referrals — compounded",
  "Proposal and Quote Templates: Basic Bookkeeping — compounded",
  "Proposal and Quote Templates: Cash Flow Management — compounded",
  "Proposal and Quote Templates: Hiring Your First Help — compounded",
  "Proposal and Quote Templates: Time Management for Owners — compounded",
  "Proposal and Quote Templates: Marketing on a Small Budget — compounded",
  "Proposal and Quote Templates: Handling Difficult Customers — compounded",
  "Proposal and Quote Templates: Legal Basics for Small Business — compounded",
  "Proposal and Quote Templates: Tax Basics for Small Business — compounded",
  "Proposal and Quote Templates: Advanced: Scaling Operations — compounded",
  "Proposal and Quote Templates: Advanced: Strategic Partnerships — compounded"
 ],
 "advanced": [
  "Proposal and Quote Templates: Advanced: Pricing Power — advanced",
  "Proposal and Quote Templates: Advanced: Building a Brand — advanced",
  "Proposal and Quote Templates: Advanced: Exit and Succession — advanced",
  "Proposal and Quote Templates: Advanced: Advanced Marketing Systems — advanced",
  "Proposal and Quote Templates: Advanced: Financial Mastery — advanced",
  "Proposal and Quote Templates: Advanced: Leading a Team — advanced",
  "Proposal and Quote Templates: Advanced: Innovation on Purpose — advanced",
  "Proposal and Quote Templates: Advanced: Crisis Management — advanced",
  "Proposal and Quote Templates: Advanced: Giving Back Profitably — advanced",
  "Proposal and Quote Templates: Advanced: The 10-Year Vision — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Proposal and Quote Templates Database — structural study\n"
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
var gen={version:'jahdb-proposal-and-quote-templates-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('proposal-and-quote-templates',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
