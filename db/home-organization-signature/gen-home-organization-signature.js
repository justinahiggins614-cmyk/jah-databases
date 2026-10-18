(function(){'use strict';
/* JAH The Home Organization Signature Database generator — jahdb-home-cleaning-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HORGS-";
var FIELDS=["Organization Foundations", "Kitchen & Pantry", "Bedrooms & Closets", "Bathrooms & Laundry", "Living Areas & Home Office", "Garage, Storage & Maintenance"];
var TOPICS={
 "Organization Foundations": [
  "The Golden Rule: A Place for Everything (Signature Edition) - Organization Foundations",
  "Declutter First, Organize Second (Signature Edition) - Organization Foundations",
  "Zones: Organize by Activity, Not by Object (Signature Edition) - Organization Foundations",
  "One In, One Out: The Replacement Rule (Signature Edition) - Organization Foundations",
  "Labels: The Secret Maintenance System (Signature Edition) - Organization Foundations",
  "The Daily Reset: 15 Minutes to Order (Signature Edition) - Organization Foundations",
  "Measuring Before Buying Containers (Signature Edition) - Organization Foundations",
  "The Landing Zone: Entryway Command Center (Signature Edition) - Organization Foundations",
  "Paper Triage: The Two-Minute Rule (Signature Edition) - Organization Foundations",
  "Vertical Space: Think Up, Not Out (Signature Edition) - Organization Foundations",
  "The Donation Station (Signature Edition) - Organization Foundations",
  "Whole-House Organization Audit (Signature Edition) - Organization Foundations",
  "Small Space Organization (Signature Edition) - Organization Foundations",
  "Organizing With ADHD or Executive Dysfunction (Signature Edition) - Organization Foundations",
  "The 30-Day Organization Challenge (Signature Edition) - Organization Foundations",
  "When to Hire a Professional Organizer (Signature Edition) - Organization Foundations",
  "The Minimalist Maintenance Mode (Signature Edition) - Organization Foundations"
 ],
 "Kitchen & Pantry": [
  "Kitchen Zones in Practice (Signature Edition) - Kitchen & Pantry",
  "Pantry Organization Systems (Signature Edition) - Kitchen & Pantry",
  "Taming the Junk Drawer (Signature Edition) - Kitchen & Pantry"
 ],
 "Bedrooms & Closets": [
  "Bedroom Organization: Calm by Design (Signature Edition) - Bedrooms & Closets",
  "Closet Systems That Work (Signature Edition) - Bedrooms & Closets"
 ],
 "Bathrooms & Laundry": [
  "Bathroom Organization (Signature Edition) - Bathrooms & Laundry",
  "Laundry Room Workflow (Signature Edition) - Bathrooms & Laundry"
 ],
 "Living Areas & Home Office": [
  "Living Room: Hidden Storage Strategies (Signature Edition) - Living Areas & Home Office",
  "Home Office Organization (Signature Edition) - Living Areas & Home Office",
  "Kids' Rooms and Toy Rotation (Signature Edition) - Living Areas & Home Office",
  "Digital-Physical Handoff Systems (Signature Edition) - Living Areas & Home Office",
  "Teaching Kids Organization Systems (Signature Edition) - Living Areas & Home Office"
 ],
 "Garage, Storage & Maintenance": [
  "Garage Zones and Wall Storage (Signature Edition) - Garage, Storage & Maintenance",
  "Seasonal Storage Rotation (Signature Edition) - Garage, Storage & Maintenance",
  "Organizing for Roommates and Shared Spaces (Signature Edition) - Garage, Storage & Maintenance",
  "Estate and Legacy Organization (Signature Edition) - Garage, Storage & Maintenance",
  "Maintenance Calendars That Run Themselves (Signature Edition) - Garage, Storage & Maintenance"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# JAH Home Organization Guide Study — "+safe+"\n"
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
    name:topic+' — home organization guide record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A home organization guide record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"home-organization-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-home-organization-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('home-organization-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
