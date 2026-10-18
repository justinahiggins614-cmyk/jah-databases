(function(){'use strict';
/* JAH The Landlord Tenant Basics Signature Database generator — jahdb-home-cleaning-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LDTBS-";
var FIELDS=["Lease Foundations", "Tenant Rights", "Landlord Duties", "Money Matters", "Repairs & Maintenance", "Moving Out & Disputes"];
var TOPICS={
 "Lease Foundations": [
  "How Leases Work: The Basics (Signature Edition) - Lease Foundations",
  "Security Deposits Explained (Signature Edition) - Lease Foundations",
  "Rent: Payment Rules and Records (Signature Edition) - Lease Foundations",
  "Roommates and Joint Leases (Signature Edition) - Lease Foundations",
  "Lease Negotiation Before Signing (Signature Edition) - Lease Foundations",
  "The Model Renter: Building Rental History (Signature Edition) - Lease Foundations"
 ],
 "Tenant Rights": [
  "Your Right to Habitable Housing (Signature Edition) - Tenant Rights",
  "Privacy: Notice Before Entry (Signature Edition) - Tenant Rights",
  "Discrimination Protections for Renters (Signature Edition) - Tenant Rights",
  "Renters and Home Businesses (Signature Edition) - Tenant Rights",
  "Accessibility and Reasonable Accommodations (Signature Edition) - Tenant Rights",
  "Retaliation Protections (Signature Edition) - Tenant Rights",
  "Domestic Violence Protections for Tenants (Signature Edition) - Tenant Rights",
  "Military Tenant Protections (SCRA) (Signature Edition) - Tenant Rights",
  "Tenant Unions and Collective Action (Signature Edition) - Tenant Rights"
 ],
 "Landlord Duties": [
  "Landlord's Repair Responsibilities (Signature Edition) - Landlord Duties",
  "What Tenants Must Maintain (Signature Edition) - Landlord Duties"
 ],
 "Money Matters": [
  "Utilities: Who Pays for What (Signature Edition) - Money Matters",
  "Renter's Insurance: Why You Need It (Signature Edition) - Money Matters",
  "Rent Increases: Rules and Responses (Signature Edition) - Money Matters",
  "Rent Control and Stabilization (Signature Edition) - Money Matters",
  "Co-Signers and Guarantors (Signature Edition) - Money Matters",
  "Insurance Claims as a Renter (Signature Edition) - Money Matters"
 ],
 "Repairs & Maintenance": [
  "Maintenance Requests That Get Results (Signature Edition) - Repairs & Maintenance",
  "Mold, Pests, and Habitability Hazards (Signature Edition) - Repairs & Maintenance"
 ],
 "Moving Out & Disputes": [
  "Breaking a Lease Legally (Signature Edition) - Moving Out & Disputes",
  "Eviction: Process and Your Rights (Signature Edition) - Moving Out & Disputes",
  "Lease Renewals: Negotiate or Move (Signature Edition) - Moving Out & Disputes",
  "Subletting and Assigning Your Lease (Signature Edition) - Moving Out & Disputes",
  "Security Deposit Deductions and Disputes (Signature Edition) - Moving Out & Disputes",
  "Lease Termination Notices (Signature Edition) - Moving Out & Disputes",
  "Small Claims Court for Renters (Signature Edition) - Moving Out & Disputes",
  "Constructive Eviction Claims (Signature Edition) - Moving Out & Disputes",
  "When to Consult a Tenant Attorney (Signature Edition) - Moving Out & Disputes"
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
var gen={version:'jahdb-landlord-tenant-basics-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('landlord-tenant-basics-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
