(function(){'use strict';
/* JAH The Home Organization Database generator — jahdb-home-cleaning-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HORG-";
var FIELDS=["Organization Foundations", "Kitchen & Pantry", "Bedrooms & Closets", "Bathrooms & Laundry", "Living Areas & Home Office", "Garage, Storage & Maintenance"];
var TOPICS={
 "Organization Foundations": [
  "The Golden Rule: A Place for Everything - Organization Foundations",
  "Declutter First, Organize Second - Organization Foundations",
  "Zones: Organize by Activity, Not by Object - Organization Foundations",
  "One In, One Out: The Replacement Rule - Organization Foundations",
  "Labels: The Secret Maintenance System - Organization Foundations",
  "The Daily Reset: 15 Minutes to Order - Organization Foundations",
  "Measuring Before Buying Containers - Organization Foundations",
  "The Landing Zone: Entryway Command Center - Organization Foundations",
  "Paper Triage: The Two-Minute Rule - Organization Foundations",
  "Vertical Space: Think Up, Not Out - Organization Foundations",
  "The Donation Station - Organization Foundations",
  "Whole-House Organization Audit - Organization Foundations",
  "Small Space Organization - Organization Foundations",
  "Organizing With ADHD or Executive Dysfunction - Organization Foundations",
  "The 30-Day Organization Challenge - Organization Foundations",
  "When to Hire a Professional Organizer - Organization Foundations",
  "The Minimalist Maintenance Mode - Organization Foundations"
 ],
 "Kitchen & Pantry": [
  "Kitchen Zones in Practice - Kitchen & Pantry",
  "Pantry Organization Systems - Kitchen & Pantry",
  "Taming the Junk Drawer - Kitchen & Pantry"
 ],
 "Bedrooms & Closets": [
  "Bedroom Organization: Calm by Design - Bedrooms & Closets",
  "Closet Systems That Work - Bedrooms & Closets"
 ],
 "Bathrooms & Laundry": [
  "Bathroom Organization - Bathrooms & Laundry",
  "Laundry Room Workflow - Bathrooms & Laundry"
 ],
 "Living Areas & Home Office": [
  "Living Room: Hidden Storage Strategies - Living Areas & Home Office",
  "Home Office Organization - Living Areas & Home Office",
  "Kids' Rooms and Toy Rotation - Living Areas & Home Office",
  "Digital-Physical Handoff Systems - Living Areas & Home Office",
  "Teaching Kids Organization Systems - Living Areas & Home Office"
 ],
 "Garage, Storage & Maintenance": [
  "Garage Zones and Wall Storage - Garage, Storage & Maintenance",
  "Seasonal Storage Rotation - Garage, Storage & Maintenance",
  "Organizing for Roommates and Shared Spaces - Garage, Storage & Maintenance",
  "Estate and Legacy Organization - Garage, Storage & Maintenance",
  "Maintenance Calendars That Run Themselves - Garage, Storage & Maintenance"
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
var gen={version:'jahdb-home-organization-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('home-organization',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
