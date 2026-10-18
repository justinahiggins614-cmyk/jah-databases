(function(){'use strict';
/* JAH The Fact-Checking Academy generator — jahdb-db-fact-checking-academy-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FCA-";
var FIELDS=["Claims","Verification","Field Work"];
var TOPICS={
 "Claims": [
  "What Makes a Claim Checkable - Claims",
  "The Anatomy of Viral Misinformation - Claims",
  "Headlines vs Reality - Claims",
  "Quotes: Real or Fabricated? - Claims",
  "Statistics in the Wild - Claims",
  "Photos Can Lie - Claims",
  "Videos: Harder to Fake, Still Faked - Claims",
  "The 'They' Trick - Claims",
  "Miracle Cures and Red Flags - Claims",
  "Conspiracy Patterns - Claims",
  "Satire vs Fake News - Claims",
  "Your Brain Wants to Believe - Claims"
 ],
 "Verification": [
  "Lateral Reading - Verification",
  "Triangulation: Three Independent Sources - Verification",
  "Reading the Original Study - Verification",
  "Checking Dates and Timelines - Verification",
  "Reverse Image Search - Verification",
  "Verifying People and Accounts - Verification",
  "Following the Money - Verification",
  "Primary Sources Win - Verification",
  "The SIFT Method - Verification",
  "Prebunking: Inoculation Theory - Verification",
  "Using Fact-Check Databases - Verification"
 ],
 "Field Work": [
  "Running a Fact-Check - Field Work",
  "Writing the Verdict - Field Work",
  "Debunking Without Backfire - Field Work",
  "Talking to Believers - Field Work",
  "Building a Verification Toolkit - Field Work",
  "Crowdsourced Verification - Field Work",
  "Teaching Others to Verify - Field Work",
  "The Fact-Checker's Oath - Field Work",
  "Your First Investigation - Field Work",
  "Staying Current: The Misinformation Beat - Field Work",
  "Live Fact-Checking Events - Field Work"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Fact Checking Study — "+safe+"\n"
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
    name:topic+' — fact-checking lesson record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A fact-checking lesson record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"fact-checking-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-fact-checking-academy-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-fact-checking-academy',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
