(function(){'use strict';
/* JAH The Fact-Checking Academy generator — jahdb-db-fact-checking-academy-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FCAS-";
var FIELDS=["Claims","Verification","Field Work"];
var TOPICS={
 "Claims": [
  "What Makes a Claim Checkable (Signature Edition) - Claims",
  "The Anatomy of Viral Misinformation (Signature Edition) - Claims",
  "Headlines vs Reality (Signature Edition) - Claims",
  "Quotes: Real or Fabricated? (Signature Edition) - Claims",
  "Statistics in the Wild (Signature Edition) - Claims",
  "Photos Can Lie (Signature Edition) - Claims",
  "Videos: Harder to Fake, Still Faked (Signature Edition) - Claims",
  "The 'They' Trick (Signature Edition) - Claims",
  "Miracle Cures and Red Flags (Signature Edition) - Claims",
  "Conspiracy Patterns (Signature Edition) - Claims",
  "Satire vs Fake News (Signature Edition) - Claims",
  "Your Brain Wants to Believe (Signature Edition) - Claims"
 ],
 "Verification": [
  "Lateral Reading (Signature Edition) - Verification",
  "Triangulation: Three Independent Sources (Signature Edition) - Verification",
  "Reading the Original Study (Signature Edition) - Verification",
  "Checking Dates and Timelines (Signature Edition) - Verification",
  "Reverse Image Search (Signature Edition) - Verification",
  "Verifying People and Accounts (Signature Edition) - Verification",
  "Following the Money (Signature Edition) - Verification",
  "Primary Sources Win (Signature Edition) - Verification",
  "The SIFT Method (Signature Edition) - Verification",
  "Prebunking: Inoculation Theory (Signature Edition) - Verification",
  "Using Fact-Check Databases (Signature Edition) - Verification"
 ],
 "Field Work": [
  "Running a Fact-Check (Signature Edition) - Field Work",
  "Writing the Verdict (Signature Edition) - Field Work",
  "Debunking Without Backfire (Signature Edition) - Field Work",
  "Talking to Believers (Signature Edition) - Field Work",
  "Building a Verification Toolkit (Signature Edition) - Field Work",
  "Crowdsourced Verification (Signature Edition) - Field Work",
  "Teaching Others to Verify (Signature Edition) - Field Work",
  "The Fact-Checker's Oath (Signature Edition) - Field Work",
  "Your First Investigation (Signature Edition) - Field Work",
  "Staying Current: The Misinformation Beat (Signature Edition) - Field Work",
  "Live Fact-Checking Events (Signature Edition) - Field Work"
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
var gen={version:'jahdb-db-fact-checking-academy-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-fact-checking-academy-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
