(function(){'use strict';
/* JAH The 2000s Signature Database generator — jahdb-decades-2000s-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-D2000S-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The 2000s at a Glance: 9/11 and the Networked Age (Signature Edition) - Foundations",
  "2000: Bush v. Gore Decides the Presidency (Signature Edition) - Foundations",
  "2001: September 11 (Signature Edition) - Foundations",
  "2001: The Afghanistan War Begins (Signature Edition) - Foundations",
  "2001: The iPod \u2014 a Thousand Songs in Your Pocket (Signature Edition) - Foundations",
  "2001: Wikipedia Launches (Signature Edition) - Foundations",
  "2003: The Iraq War Begins (Signature Edition) - Foundations",
  "2003: The Human Genome Is Completed (Signature Edition) - Foundations",
  "2004: Facebook Launches (Signature Edition) - Foundations",
  "2004: The Indian Ocean Tsunami (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "2001: Enron Collapses (Signature Edition) - Compounded",
  "2004: The Mars Rovers Land (Signature Edition) - Compounded",
  "2004: Gmail Launches \u2014 1 GB Free (Signature Edition) - Compounded",
  "2005: YouTube Is Founded (Signature Edition) - Compounded",
  "2005: Hurricane Katrina (Signature Edition) - Compounded",
  "2006: Twitter Launches (Signature Edition) - Compounded",
  "2006: The Nintendo Wii (Signature Edition) - Compounded",
  "2007: The iPhone (Signature Edition) - Compounded",
  "2008: The Beijing Olympics (Signature Edition) - Compounded",
  "2008: Lehman Falls \u2014 the Financial Crisis (Signature Edition) - Compounded",
  "2008: Obama Is Elected (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "2002: Euro Notes Enter Circulation (Signature Edition) - Advanced",
  "2005: Google Maps Launches (Signature Edition) - Advanced",
  "2007: The Amazon Kindle (Signature Edition) - Advanced",
  "2008: The Large Hadron Collider's First Beam (Signature Edition) - Advanced",
  "2008: Android Launches (Signature Edition) - Advanced",
  "2009: Bitcoin's Genesis Block (Signature Edition) - Advanced",
  "2009: The H1N1 Pandemic (Signature Edition) - Advanced",
  "2005: 'Me at the Zoo' \u2014 the First YouTube Video (Signature Edition) - Advanced",
  "2006: Pluto Is Demoted (Signature Edition) - Advanced",
  "2003: The Columbia Disaster (Signature Edition) - Advanced",
  "2007: Netflix Starts Streaming (Signature Edition) - Advanced",
  "2002: SpaceX Is Founded (Signature Edition) - Advanced",
  "2009: Sully Lands on the Hudson (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# 2000S — "+safe+"\n"
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
    name:topic+' — 2000s history record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A 2000s history record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"decades-2000s-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-decades-2000s-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('decades-2000s-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
