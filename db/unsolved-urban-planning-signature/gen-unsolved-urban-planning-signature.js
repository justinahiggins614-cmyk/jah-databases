(function(){'use strict';
/* JAH The Unsolved Urban Planning Signature Database generator — jahdb-unsolved-urban-planning-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-USUPS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Why Cities Exist (Signature Edition) - Theory",
  "The Optimal City Size (Signature Edition) - Theory",
  "Zoning: Help or Harm (Signature Edition) - Policy",
  "The Housing Shortage: Why (Signature Edition) - Housing",
  "Rent Control: Does It Work (Signature Edition) - Housing",
  "Gentrification: Inevitable (Signature Edition) - Housing",
  "The Suburb Problem (Signature Edition) - Form",
  "Sprawl: Can It Be Stopped (Signature Edition) - Form",
  "The 15-Minute City Debate (Signature Edition) - Form",
  "Streets: Who Are They For (Signature Edition) - Mobility",
  "Parking: How Much (Signature Edition) - Mobility"
 ],
 "Compounded": [
  "Transit: Why America Fails (Signature Edition) - Mobility",
  "Congestion Pricing: Does It Work (Signature Edition) - Mobility",
  "The Bike Lane Wars (Signature Edition) - Mobility",
  "High-Speed Rail: Why Not America (Signature Edition) - Mobility",
  "The Downtown Problem (Signature Edition) - Form",
  "Mixed Use: Does It Work (Signature Edition) - Form",
  "Density: How Much Is Enough (Signature Edition) - Form",
  "The Greenbelt Question (Signature Edition) - Policy",
  "Eminent Domain: Just (Signature Edition) - Policy",
  "Tax Increment Financing: Fair (Signature Edition) - Policy",
  "Participatory Planning: Real (Signature Edition) - Policy",
  "The NIMBY Problem (Signature Edition) - Housing"
 ],
 "Advanced": [
  "The YIMBY Answer (Signature Edition) - Housing",
  "Social Housing: The Models (Signature Edition) - Housing",
  "Homelessness: What Ends It (Signature Edition) - Housing",
  "Climate Migration and Cities (Signature Edition) - Theory",
  "The Smart City Problem (Signature Edition) - Theory",
  "Surveillance Urbanism (Signature Edition) - Theory",
  "The Post-Pandemic City (Signature Edition) - Theory",
  "Shrinking Cities: The Response (Signature Edition) - Theory",
  "The Global South City (Signature Edition) - Theory",
  "Planning and Justice (Signature Edition) - Policy",
  "A Unified Theory of Cities (Signature Edition) - Theory"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Unsolved Urban Planning Study — "+safe+"\n"
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
    name:topic+' — unsolved problem record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A unsolved problem record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"unsolved-urban-planning-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-unsolved-urban-planning-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('unsolved-urban-planning-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
