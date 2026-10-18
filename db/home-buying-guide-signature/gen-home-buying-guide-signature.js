(function(){'use strict';
/* JAH The Home Buying Guide Signature Database generator — jahdb-home-cleaning-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HBYGS-";
var FIELDS=["Buying Foundations", "Money & Mortgages", "House Hunting", "Offers & Negotiation", "Inspections & Closing", "After the Purchase"];
var TOPICS={
 "Buying Foundations": [
  "Are You Ready to Buy? The Honest Checklist (Signature Edition) - Buying Foundations",
  "How Much House Can You Actually Afford (Signature Edition) - Buying Foundations",
  "Credit Scores and Home Buying (Signature Edition) - Buying Foundations",
  "Buying With Partners, Family, or Investors (Signature Edition) - Buying Foundations",
  "From Renter to Owner: The Mindset Shift (Signature Edition) - Buying Foundations"
 ],
 "Money & Mortgages": [
  "Down Payments: How Much and Where From (Signature Edition) - Money & Mortgages",
  "Mortgage Types Explained Simply (Signature Edition) - Money & Mortgages",
  "Pre-Approval vs Pre-Qualification (Signature Edition) - Money & Mortgages",
  "Closing Costs: The Forgotten 2-5% (Signature Edition) - Money & Mortgages",
  "First-Time Buyer Programs (Signature Edition) - Money & Mortgages",
  "Building Equity Faster (Signature Edition) - Money & Mortgages"
 ],
 "House Hunting": [
  "Choosing a Buyer's Agent (Signature Edition) - House Hunting",
  "Defining Your Must-Haves vs Nice-to-Haves (Signature Edition) - House Hunting",
  "Touring Homes Like a Detective (Signature Edition) - House Hunting",
  "New Construction vs Existing Homes (Signature Edition) - House Hunting",
  "HOAs: Costs, Rules, and Red Flags (Signature Edition) - House Hunting",
  "Condos and Townhomes: Special Considerations (Signature Edition) - House Hunting",
  "For Sale By Owner and Auctions (Signature Edition) - House Hunting",
  "Relocation Buying: Long-Distance Purchases (Signature Edition) - House Hunting"
 ],
 "Offers & Negotiation": [
  "Making a Competitive Offer (Signature Edition) - Offers & Negotiation",
  "Negotiation Tactics That Work (Signature Edition) - Offers & Negotiation",
  "Surviving Bidding Wars Without Overpaying (Signature Edition) - Offers & Negotiation"
 ],
 "Inspections & Closing": [
  "The Home Inspection: What Matters (Signature Edition) - Inspections & Closing",
  "Appraisals and Lender Requirements (Signature Edition) - Inspections & Closing",
  "Title Search and Title Insurance (Signature Edition) - Inspections & Closing",
  "The Closing Process Step by Step (Signature Edition) - Inspections & Closing",
  "Negotiating Repairs After Inspection (Signature Edition) - Inspections & Closing",
  "Low Appraisal: Options and Strategies (Signature Edition) - Inspections & Closing"
 ],
 "After the Purchase": [
  "Understanding Property Taxes (Signature Edition) - After the Purchase",
  "Investment Property Basics for Beginners (Signature Edition) - After the Purchase",
  "Refinancing: When and How (Signature Edition) - After the Purchase",
  "Home Warranties: Worth It? (Signature Edition) - After the Purchase",
  "Selling Your First Home Someday (Signature Edition) - After the Purchase",
  "The First Year Homeowner Playbook (Signature Edition) - After the Purchase"
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
var gen={version:'jahdb-home-buying-guide-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('home-buying-guide-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
