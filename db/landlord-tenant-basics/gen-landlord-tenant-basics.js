(function(){'use strict';
/* JAH The Landlord Tenant Basics Database generator — jahdb-home-cleaning-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LDTB-";
var FIELDS=["Lease Foundations", "Tenant Rights", "Landlord Duties", "Money Matters", "Repairs & Maintenance", "Moving Out & Disputes"];
var TOPICS={
 "Lease Foundations": [
  "How Leases Work: The Basics - Lease Foundations",
  "Security Deposits Explained - Lease Foundations",
  "Rent: Payment Rules and Records - Lease Foundations",
  "Roommates and Joint Leases - Lease Foundations",
  "Lease Negotiation Before Signing - Lease Foundations",
  "The Model Renter: Building Rental History - Lease Foundations"
 ],
 "Tenant Rights": [
  "Your Right to Habitable Housing - Tenant Rights",
  "Privacy: Notice Before Entry - Tenant Rights",
  "Discrimination Protections for Renters - Tenant Rights",
  "Renters and Home Businesses - Tenant Rights",
  "Accessibility and Reasonable Accommodations - Tenant Rights",
  "Retaliation Protections - Tenant Rights",
  "Domestic Violence Protections for Tenants - Tenant Rights",
  "Military Tenant Protections (SCRA) - Tenant Rights",
  "Tenant Unions and Collective Action - Tenant Rights"
 ],
 "Landlord Duties": [
  "Landlord's Repair Responsibilities - Landlord Duties",
  "What Tenants Must Maintain - Landlord Duties"
 ],
 "Money Matters": [
  "Utilities: Who Pays for What - Money Matters",
  "Renter's Insurance: Why You Need It - Money Matters",
  "Rent Increases: Rules and Responses - Money Matters",
  "Rent Control and Stabilization - Money Matters",
  "Co-Signers and Guarantors - Money Matters",
  "Insurance Claims as a Renter - Money Matters"
 ],
 "Repairs & Maintenance": [
  "Maintenance Requests That Get Results - Repairs & Maintenance",
  "Mold, Pests, and Habitability Hazards - Repairs & Maintenance"
 ],
 "Moving Out & Disputes": [
  "Breaking a Lease Legally - Moving Out & Disputes",
  "Eviction: Process and Your Rights - Moving Out & Disputes",
  "Lease Renewals: Negotiate or Move - Moving Out & Disputes",
  "Subletting and Assigning Your Lease - Moving Out & Disputes",
  "Security Deposit Deductions and Disputes - Moving Out & Disputes",
  "Lease Termination Notices - Moving Out & Disputes",
  "Small Claims Court for Renters - Moving Out & Disputes",
  "Constructive Eviction Claims - Moving Out & Disputes",
  "When to Consult a Tenant Attorney - Moving Out & Disputes"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# JAH Landlord Tenant Guide Study — "+safe+"\n"
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
    name:topic+' — landlord tenant guide record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A landlord tenant guide record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"landlord-tenant-basics-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-landlord-tenant-basics-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('landlord-tenant-basics',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
