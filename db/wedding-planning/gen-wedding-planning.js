(function(){'use strict';
/* JAH The Wedding Planning Database generator — jahdb-wedding-planning-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WEDP-";
var FIELDS=["Budgets & Timelines","Venues","Vendors","Ceremony","Reception","Attire & Details"];
var TOPICS={
 "Budgets & Timelines": [
  "Setting the Wedding Budget - Budgets & Timelines",
  "The 12-Month Planning Timeline - Budgets & Timelines",
  "The Guest List: Building and Trimming - Budgets & Timelines",
  "Wedding Budget Savers That Don't Look Cheap - Budgets & Timelines",
  "Hiring a Wedding Planner (or Not) - Budgets & Timelines",
  "Wedding Insurance and Contracts - Budgets & Timelines"
 ],
 "Venues": [
  "Choosing the Wedding Venue - Venues",
  "Outdoor Weddings and Weather Plans - Venues",
  "Venue Logistics: Power, Parking, and Access - Venues",
  "Ceremony and Reception in One Place (or Not) - Venues",
  "Negotiating With Venues - Venues"
 ],
 "Vendors": [
  "Photographers and Videographers - Vendors",
  "Caterers and the Wedding Menu - Vendors",
  "Florists: Flowers That Matter - Vendors",
  "Music: Bands, DJs, and Ceremony Musicians - Vendors",
  "The Wedding Cake and Desserts - Vendors",
  "Officiants: Finding the Right Voice - Vendors"
 ],
 "Ceremony": [
  "Designing the Ceremony - Ceremony",
  "Writing Your Own Vows - Ceremony",
  "Ceremony Rituals and Traditions - Ceremony",
  "The Wedding Party: Roles and Responsibilities - Ceremony",
  "Rehearsal and Rehearsal Dinner - Ceremony"
 ],
 "Reception": [
  "The Reception Timeline - Reception",
  "Seating Charts That Work - Reception",
  "Toasts and Speeches - Reception",
  "First Dance and Parent Dances - Reception",
  "Keeping Guests Happy All Night - Reception",
  "The Send-Off and After-Party - Reception"
 ],
 "Attire & Details": [
  "Wedding Attire: Dresses, Suits, and Timing - Attire & Details",
  "Rings: Choosing and Caring - Attire & Details",
  "Invitations and Stationery - Attire & Details",
  "Wedding Day Emergency Kit - Attire & Details",
  "Honeymoon Planning - Attire & Details",
  "Thank-You Notes Done Right - Attire & Details"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Wedding Planning Study — "+safe+"\n"
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
    name:topic+' — wedding planning guide record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A wedding planning guide record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"wedding-planning-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-wedding-planning-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('wedding-planning',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
