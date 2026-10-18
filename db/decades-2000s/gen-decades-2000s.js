(function(){'use strict';
/* JAH The 2000s Database generator — jahdb-decades-2000s-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-D2000-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The 2000s at a Glance: 9/11 and the Networked Age - Foundations",
  "2000: Bush v. Gore Decides the Presidency - Foundations",
  "2001: September 11 - Foundations",
  "2001: The Afghanistan War Begins - Foundations",
  "2001: The iPod \u2014 a Thousand Songs in Your Pocket - Foundations",
  "2001: Wikipedia Launches - Foundations",
  "2003: The Iraq War Begins - Foundations",
  "2003: The Human Genome Is Completed - Foundations",
  "2004: Facebook Launches - Foundations",
  "2004: The Indian Ocean Tsunami - Foundations"
 ],
 "Compounded": [
  "2001: Enron Collapses - Compounded",
  "2004: The Mars Rovers Land - Compounded",
  "2004: Gmail Launches \u2014 1 GB Free - Compounded",
  "2005: YouTube Is Founded - Compounded",
  "2005: Hurricane Katrina - Compounded",
  "2006: Twitter Launches - Compounded",
  "2006: The Nintendo Wii - Compounded",
  "2007: Apple Unveils the iPhone - Compounded",
  "2008: The Beijing Olympics - Compounded",
  "2008: Lehman Falls \u2014 the Financial Crisis - Compounded",
  "2008: Obama Is Elected - Compounded"
 ],
 "Advanced": [
  "2002: Euro Notes Enter Circulation - Advanced",
  "2005: Google Maps Launches - Advanced",
  "2007: The Amazon Kindle - Advanced",
  "2008: The Large Hadron Collider's First Beam - Advanced",
  "2008: Android Launches - Advanced",
  "2009: Bitcoin's Genesis Block - Advanced",
  "2009: The H1N1 Pandemic - Advanced",
  "2005: 'Me at the Zoo' \u2014 the First YouTube Video - Advanced",
  "2006: Pluto Is Demoted - Advanced",
  "2003: The Columbia Disaster - Advanced",
  "2007: Netflix Starts Streaming - Advanced",
  "2002: SpaceX Is Founded - Advanced",
  "2009: Sully Lands on the Hudson - Advanced"
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
var gen={version:'jahdb-decades-2000s-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('decades-2000s',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
