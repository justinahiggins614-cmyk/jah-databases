(function(){'use strict';
/* JAH The Then vs. Now Visual Signature Database generator — jahdb-db-then-vs-now-visual-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TVNVS-";
var FIELDS=["Daily Life Then & Now","Work Then & Now","World Then & Now"];
var TOPICS={
 "Daily Life Then & Now": [
  "Kitchen 1950 vs Now (Signature Edition) - Daily Life Then & Now",
  "Living Room 1970 vs Now (Signature Edition) - Daily Life Then & Now",
  "Bedroom 1990 vs Now (Signature Edition) - Daily Life Then & Now",
  "Bathroom 1960 vs Now (Signature Edition) - Daily Life Then & Now",
  "Laundry 1950 vs Now (Signature Edition) - Daily Life Then & Now",
  "Grocery 1980 vs Now (Signature Edition) - Daily Life Then & Now",
  "Phone Call 1990 vs Now (Signature Edition) - Daily Life Then & Now",
  "Music Listening 1985 vs Now (Signature Edition) - Daily Life Then & Now",
  "Movie Night 1995 vs Now (Signature Edition) - Daily Life Then & Now",
  "News 1970 vs Now (Signature Edition) - Daily Life Then & Now",
  "Dating 1990 vs Now (Signature Edition) - Daily Life Then & Now",
  "Travel Planning 2000 vs Now (Signature Edition) - Daily Life Then & Now"
 ],
 "Work Then & Now": [
  "Office 1985 vs Now (Signature Edition) - Work Then & Now",
  "Factory 1950 vs Now (Signature Edition) - Work Then & Now",
  "Farm 1940 vs Now (Signature Edition) - Work Then & Now",
  "Classroom 1970 vs Now (Signature Edition) - Work Then & Now",
  "Hospital 1960 vs Now (Signature Edition) - Work Then & Now",
  "Store 1990 vs Now (Signature Edition) - Work Then & Now",
  "Bank 1980 vs Now (Signature Edition) - Work Then & Now",
  "Post Office 1970 vs Now (Signature Edition) - Work Then & Now",
  "Library 1985 vs Now (Signature Edition) - Work Then & Now",
  "Newsroom 1975 vs Now (Signature Edition) - Work Then & Now"
 ],
 "World Then & Now": [
  "City Street 1950 vs Now (Signature Edition) - World Then & Now",
  "Skyline 1980 vs Now (Signature Edition) - World Then & Now",
  "Highway 1960 vs Now (Signature Edition) - World Then & Now",
  "Airport 1970 vs Now (Signature Edition) - World Then & Now",
  "Beach 1960 vs Now (Signature Edition) - World Then & Now",
  "Park 1975 vs Now (Signature Edition) - World Then & Now",
  "Main Street 1955 vs Now (Signature Edition) - World Then & Now",
  "Farmers Market 1980 vs Now (Signature Edition) - World Then & Now",
  "Drive-In 1960 vs Now (Signature Edition) - World Then & Now",
  "Camping 1970 vs Now (Signature Edition) - World Then & Now",
  "Playground 1980 vs Now (Signature Edition) - World Then & Now",
  "Arcade 1985 vs Now (Signature Edition) - World Then & Now"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Then Vs Now Study — "+safe+"\n"
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
    name:topic+' — then-vs-now comparison record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A then-vs-now comparison record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"then-vs-now-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-then-vs-now-visual-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-then-vs-now-visual-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
