(function(){'use strict';
/* JAH The Most Expensive vs. Most Affordable Database generator — jahdb-db-most-expensive-vs-most-affordable-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MEVMA-";
var FIELDS=["Cost Foundations","Luxury vs Thrift","Value Verdicts"];
var TOPICS={
 "Cost Foundations": [
  "Yacht vs Kayak: Watercraft Cost - Cost Foundations",
  "Caviar vs Beans: Protein Cost - Cost Foundations",
  "Mansion vs Tiny House: Home Cost - Cost Foundations",
  "First Class vs Economy: Flight Cost - Cost Foundations",
  "Designer Bag vs Tote: Carry Cost - Cost Foundations",
  "Truffle vs Mushroom: Fungi Cost - Cost Foundations",
  "Champagne vs Sparkling Water: Bubbles - Cost Foundations",
  "Sports Car vs Bicycle: Commute Cost - Cost Foundations",
  "Hotel Suite vs Hostel: Sleep Cost - Cost Foundations",
  "Watch vs Phone Time: Time Cost - Cost Foundations",
  "Suit vs Jeans: Clothing Cost - Cost Foundations",
  "Private Jet vs Bus: Travel Cost - Cost Foundations"
 ],
 "Luxury vs Thrift": [
  "Wagyu vs Ground Beef: Meat Cost - Luxury vs Thrift",
  "Penthouse vs Studio: City Living - Luxury vs Thrift",
  "Grand Piano vs Keyboard: Music Cost - Luxury vs Thrift",
  "Safari vs Backyard Camping: Adventure Cost - Luxury vs Thrift",
  "Diamond vs Cubic Zirconia: Sparkle Cost - Luxury vs Thrift",
  "Espresso Machine vs French Press: Coffee Cost - Luxury vs Thrift",
  "Tesla vs Used Corolla: Car Value - Luxury vs Thrift",
  "Spa Day vs Hot Bath: Relaxation Cost - Luxury vs Thrift",
  "Art Original vs Print: Wall Cost - Luxury vs Thrift",
  "Golf Club vs Park: Green Cost - Luxury vs Thrift"
 ],
 "Value Verdicts": [
  "Wedding vs Courthouse: Celebration Cost - Value Verdicts",
  "College vs Library: Education Cost - Value Verdicts",
  "Gym vs Bodyweight: Fitness Cost - Value Verdicts",
  "Therapist vs Journal: Mind Cost - Value Verdicts",
  "New Phone vs Old Phone: Tech Cost - Value Verdicts",
  "Organic vs Conventional: Food Cost - Value Verdicts",
  "House Cleaner vs DIY: Time Cost - Value Verdicts",
  "Lawyer vs Legal Aid: Justice Cost - Value Verdicts",
  "Concert vs Street Music: Music Cost - Value Verdicts",
  "Fine Dining vs Food Truck: Meal Cost - Value Verdicts",
  "Business Class vs Premium Economy: Middle Path - Value Verdicts",
  "New Car vs Certified Used: Smart Money - Value Verdicts"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Expensive Vs Affordable Study — "+safe+"\n"
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
    name:topic+' — cost comparison record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A cost comparison record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"expensive-vs-affordable-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-most-expensive-vs-most-affordable-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-most-expensive-vs-most-affordable',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
