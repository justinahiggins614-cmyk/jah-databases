(function(){'use strict';
/* JAH The Home Buying Guide Database generator — jahdb-home-cleaning-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HBYG-";
var FIELDS=["Buying Foundations", "Money & Mortgages", "House Hunting", "Offers & Negotiation", "Inspections & Closing", "After the Purchase"];
var TOPICS={
 "Buying Foundations": [
  "Are You Ready to Buy? The Honest Checklist - Buying Foundations",
  "How Much House Can You Actually Afford - Buying Foundations",
  "Credit Scores and Home Buying - Buying Foundations",
  "Buying With Partners, Family, or Investors - Buying Foundations",
  "From Renter to Owner: The Mindset Shift - Buying Foundations"
 ],
 "Money & Mortgages": [
  "Down Payments: How Much and Where From - Money & Mortgages",
  "Mortgage Types Explained Simply - Money & Mortgages",
  "Pre-Approval vs Pre-Qualification - Money & Mortgages",
  "Closing Costs: The Forgotten 2-5% - Money & Mortgages",
  "First-Time Buyer Programs - Money & Mortgages",
  "Building Equity Faster - Money & Mortgages"
 ],
 "House Hunting": [
  "Choosing a Buyer's Agent - House Hunting",
  "Defining Your Must-Haves vs Nice-to-Haves - House Hunting",
  "Touring Homes Like a Detective - House Hunting",
  "New Construction vs Existing Homes - House Hunting",
  "HOAs: Costs, Rules, and Red Flags - House Hunting",
  "Condos and Townhomes: Special Considerations - House Hunting",
  "For Sale By Owner and Auctions - House Hunting",
  "Relocation Buying: Long-Distance Purchases - House Hunting"
 ],
 "Offers & Negotiation": [
  "Making a Competitive Offer - Offers & Negotiation",
  "Negotiation Tactics That Work - Offers & Negotiation",
  "Surviving Bidding Wars Without Overpaying - Offers & Negotiation"
 ],
 "Inspections & Closing": [
  "The Home Inspection: What Matters - Inspections & Closing",
  "Appraisals and Lender Requirements - Inspections & Closing",
  "Title Search and Title Insurance - Inspections & Closing",
  "The Closing Process Step by Step - Inspections & Closing",
  "Negotiating Repairs After Inspection - Inspections & Closing",
  "Low Appraisal: Options and Strategies - Inspections & Closing"
 ],
 "After the Purchase": [
  "Understanding Property Taxes - After the Purchase",
  "Investment Property Basics for Beginners - After the Purchase",
  "Refinancing: When and How - After the Purchase",
  "Home Warranties: Worth It? - After the Purchase",
  "Selling Your First Home Someday - After the Purchase",
  "The First Year Homeowner Playbook - After the Purchase"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# JAH Home Buying Guide Study — "+safe+"\n"
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
    name:topic+' — home buying guide record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A home buying guide record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"home-buying-guide-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-home-buying-guide-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('home-buying-guide',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
