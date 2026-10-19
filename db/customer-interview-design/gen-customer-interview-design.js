(function(){'use strict';
/* JAH The Customer Interview Design Database generator — jahdb-customer-interview-design-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CID-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Customer Interview Design: Defining Your Offer Clearly — foundations",
  "Customer Interview Design: Knowing Your Customer — foundations",
  "Customer Interview Design: Pricing That Holds — foundations",
  "Customer Interview Design: The Interview Conversation — foundations",
  "Customer Interview Design: Proposals That Win — foundations",
  "Customer Interview Design: Quotes and Estimates — foundations",
  "Customer Interview Design: Contracts in Plain Terms — foundations",
  "Customer Interview Design: Invoicing and Getting Paid — foundations",
  "Customer Interview Design: Email Marketing Basics — foundations",
  "Customer Interview Design: CAN-SPAM Compliance — foundations",
  "Customer Interview Design: Following Up Systematically — foundations",
  "Customer Interview Design: Handling Objections — foundations"
 ],
 "compounded": [
  "Customer Interview Design: Delivering Great Service — compounded",
  "Customer Interview Design: Asking for Reviews and Referrals — compounded",
  "Customer Interview Design: Basic Bookkeeping — compounded",
  "Customer Interview Design: Cash Flow Management — compounded",
  "Customer Interview Design: Hiring Your First Help — compounded",
  "Customer Interview Design: Time Management for Owners — compounded",
  "Customer Interview Design: Marketing on a Small Budget — compounded",
  "Customer Interview Design: Handling Difficult Customers — compounded",
  "Customer Interview Design: Legal Basics for Small Business — compounded",
  "Customer Interview Design: Tax Basics for Small Business — compounded",
  "Customer Interview Design: Advanced: Scaling Operations — compounded",
  "Customer Interview Design: Advanced: Strategic Partnerships — compounded"
 ],
 "advanced": [
  "Customer Interview Design: Advanced: Pricing Power — advanced",
  "Customer Interview Design: Advanced: Building a Brand — advanced",
  "Customer Interview Design: Advanced: Exit and Succession — advanced",
  "Customer Interview Design: Advanced: Advanced Marketing Systems — advanced",
  "Customer Interview Design: Advanced: Financial Mastery — advanced",
  "Customer Interview Design: Advanced: Leading a Team — advanced",
  "Customer Interview Design: Advanced: Innovation on Purpose — advanced",
  "Customer Interview Design: Advanced: Crisis Management — advanced",
  "Customer Interview Design: Advanced: Giving Back Profitably — advanced",
  "Customer Interview Design: Advanced: The 10-Year Vision — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Customer Interview Design Database — structural study\n"
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
var gen={version:'jahdb-customer-interview-design-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('customer-interview-design',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
