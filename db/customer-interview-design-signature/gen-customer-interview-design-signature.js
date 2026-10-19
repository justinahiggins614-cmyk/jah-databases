(function(){'use strict';
/* JAH The Customer Interview Design Signature Database generator — jahdb-customer-interview-design-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CIDS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Customer Interview Design (Signature): Defining Your Offer Clearly — foundations",
  "Customer Interview Design (Signature): Knowing Your Customer — foundations",
  "Customer Interview Design (Signature): Pricing That Holds — foundations",
  "Customer Interview Design (Signature): The Interview Conversation — foundations",
  "Customer Interview Design (Signature): Proposals That Win — foundations",
  "Customer Interview Design (Signature): Quotes and Estimates — foundations",
  "Customer Interview Design (Signature): Contracts in Plain Terms — foundations",
  "Customer Interview Design (Signature): Invoicing and Getting Paid — foundations",
  "Customer Interview Design (Signature): Email Marketing Basics — foundations",
  "Customer Interview Design (Signature): CAN-SPAM Compliance — foundations",
  "Customer Interview Design (Signature): Following Up Systematically — foundations",
  "Customer Interview Design (Signature): Handling Objections — foundations"
 ],
 "compounded": [
  "Customer Interview Design (Signature): Delivering Great Service — compounded",
  "Customer Interview Design (Signature): Asking for Reviews and Referrals — compounded",
  "Customer Interview Design (Signature): Basic Bookkeeping — compounded",
  "Customer Interview Design (Signature): Cash Flow Management — compounded",
  "Customer Interview Design (Signature): Hiring Your First Help — compounded",
  "Customer Interview Design (Signature): Time Management for Owners — compounded",
  "Customer Interview Design (Signature): Marketing on a Small Budget — compounded",
  "Customer Interview Design (Signature): Handling Difficult Customers — compounded",
  "Customer Interview Design (Signature): Legal Basics for Small Business — compounded",
  "Customer Interview Design (Signature): Tax Basics for Small Business — compounded",
  "Customer Interview Design (Signature): Advanced: Scaling Operations — compounded",
  "Customer Interview Design (Signature): Advanced: Strategic Partnerships — compounded"
 ],
 "advanced": [
  "Customer Interview Design (Signature): Advanced: Pricing Power — advanced",
  "Customer Interview Design (Signature): Advanced: Building a Brand — advanced",
  "Customer Interview Design (Signature): Advanced: Exit and Succession — advanced",
  "Customer Interview Design (Signature): Advanced: Advanced Marketing Systems — advanced",
  "Customer Interview Design (Signature): Advanced: Financial Mastery — advanced",
  "Customer Interview Design (Signature): Advanced: Leading a Team — advanced",
  "Customer Interview Design (Signature): Advanced: Innovation on Purpose — advanced",
  "Customer Interview Design (Signature): Advanced: Crisis Management — advanced",
  "Customer Interview Design (Signature): Advanced: Giving Back Profitably — advanced",
  "Customer Interview Design (Signature): Advanced: The 10-Year Vision — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Customer Interview Design Signature Database — structural study\n"
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
    name:topic+' — signature-original record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A signature-original record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
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
var gen={version:'jahdb-customer-interview-design-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('customer-interview-design-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
