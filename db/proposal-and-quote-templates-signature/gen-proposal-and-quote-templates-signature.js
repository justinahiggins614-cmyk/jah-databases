(function(){'use strict';
/* JAH The Proposal and Quote Templates Signature Database generator — jahdb-proposal-and-quote-templates-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PAQTS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Proposal and Quote Templates (Signature): Defining Your Offer Clearly — foundations",
  "Proposal and Quote Templates (Signature): Knowing Your Customer — foundations",
  "Proposal and Quote Templates (Signature): Pricing That Holds — foundations",
  "Proposal and Quote Templates (Signature): The Interview Conversation — foundations",
  "Proposal and Quote Templates (Signature): Proposals That Win — foundations",
  "Proposal and Quote Templates (Signature): Quotes and Estimates — foundations",
  "Proposal and Quote Templates (Signature): Contracts in Plain Terms — foundations",
  "Proposal and Quote Templates (Signature): Invoicing and Getting Paid — foundations",
  "Proposal and Quote Templates (Signature): Email Marketing Basics — foundations",
  "Proposal and Quote Templates (Signature): CAN-SPAM Compliance — foundations",
  "Proposal and Quote Templates (Signature): Following Up Systematically — foundations",
  "Proposal and Quote Templates (Signature): Handling Objections — foundations"
 ],
 "compounded": [
  "Proposal and Quote Templates (Signature): Delivering Great Service — compounded",
  "Proposal and Quote Templates (Signature): Asking for Reviews and Referrals — compounded",
  "Proposal and Quote Templates (Signature): Basic Bookkeeping — compounded",
  "Proposal and Quote Templates (Signature): Cash Flow Management — compounded",
  "Proposal and Quote Templates (Signature): Hiring Your First Help — compounded",
  "Proposal and Quote Templates (Signature): Time Management for Owners — compounded",
  "Proposal and Quote Templates (Signature): Marketing on a Small Budget — compounded",
  "Proposal and Quote Templates (Signature): Handling Difficult Customers — compounded",
  "Proposal and Quote Templates (Signature): Legal Basics for Small Business — compounded",
  "Proposal and Quote Templates (Signature): Tax Basics for Small Business — compounded",
  "Proposal and Quote Templates (Signature): Advanced: Scaling Operations — compounded",
  "Proposal and Quote Templates (Signature): Advanced: Strategic Partnerships — compounded"
 ],
 "advanced": [
  "Proposal and Quote Templates (Signature): Advanced: Pricing Power — advanced",
  "Proposal and Quote Templates (Signature): Advanced: Building a Brand — advanced",
  "Proposal and Quote Templates (Signature): Advanced: Exit and Succession — advanced",
  "Proposal and Quote Templates (Signature): Advanced: Advanced Marketing Systems — advanced",
  "Proposal and Quote Templates (Signature): Advanced: Financial Mastery — advanced",
  "Proposal and Quote Templates (Signature): Advanced: Leading a Team — advanced",
  "Proposal and Quote Templates (Signature): Advanced: Innovation on Purpose — advanced",
  "Proposal and Quote Templates (Signature): Advanced: Crisis Management — advanced",
  "Proposal and Quote Templates (Signature): Advanced: Giving Back Profitably — advanced",
  "Proposal and Quote Templates (Signature): Advanced: The 10-Year Vision — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Proposal and Quote Templates Signature Database — structural study\n"
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
var gen={version:'jahdb-proposal-and-quote-templates-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('proposal-and-quote-templates-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
