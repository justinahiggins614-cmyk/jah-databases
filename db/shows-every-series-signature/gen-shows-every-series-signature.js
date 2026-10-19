(function(){'use strict';
/* JAH The Shows Signature Database generator — jahdb-shows-every-series-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TVS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Captain Video and His Video Rangers \u2014 Signature Season Curation (Signature Edition) \u2014 foundations",
  "The Cisco Kid \u2014 Signature Season Curation (Signature Edition) \u2014 foundations",
  "The Gene Autry Show \u2014 Signature Season Curation (Signature Edition) \u2014 foundations",
  "You Bet Your Life \u2014 Signature Season Curation (Signature Edition) \u2014 foundations",
  "Tom Corbett, Space Cadet \u2014 Signature Season Curation (Signature Edition) \u2014 foundations",
  "Dragnet \u2014 Signature Season Curation (Signature Edition) \u2014 foundations",
  "The Adventures of Kit Carson \u2014 Signature Season Curation (Signature Edition) \u2014 foundations",
  "The Roy Rogers Show \u2014 Signature Season Curation (Signature Edition) \u2014 foundations",
  "Hopalong Cassidy \u2014 Signature Season Curation (Signature Edition) \u2014 foundations",
  "Sherlock Holmes \u2014 Signature Season Curation (Signature Edition) \u2014 foundations",
  "Annie Oakley \u2014 Signature Season Curation (Signature Edition) \u2014 foundations",
  "Flash Gordon \u2014 Signature Season Curation (Signature Edition) \u2014 foundations"
 ],
 "compounded": [
  "I Love Lucy \u2014 Signature Season Curation (Signature Edition) \u2014 compounded",
  "The Twilight Zone \u2014 Signature Season Curation (Signature Edition) \u2014 compounded",
  "The Andy Griffith Show \u2014 Signature Season Curation (Signature Edition) \u2014 compounded",
  "Star Trek: The Original Series \u2014 Signature Season Curation (Signature Edition) \u2014 compounded",
  "Mister Rogers' Neighborhood \u2014 Signature Season Curation (Signature Edition) \u2014 compounded",
  "Sesame Street \u2014 Signature Season Curation (Signature Edition) \u2014 compounded",
  "The Mary Tyler Moore Show \u2014 Signature Season Curation (Signature Edition) \u2014 compounded",
  "All in the Family \u2014 Signature Season Curation (Signature Edition) \u2014 compounded",
  "M*A*S*H \u2014 Signature Season Curation (Signature Edition) \u2014 compounded",
  "Cheers \u2014 Signature Season Curation (Signature Edition) \u2014 compounded",
  "The Simpsons \u2014 Signature Season Curation (Signature Edition) \u2014 compounded",
  "Seinfeld \u2014 Signature Season Curation (Signature Edition) \u2014 compounded"
 ],
 "advanced": [
  "The X-Files \u2014 Signature Season Curation (Signature Edition) \u2014 advanced",
  "Friends \u2014 Signature Season Curation (Signature Edition) \u2014 advanced",
  "The Sopranos \u2014 Signature Season Curation (Signature Edition) \u2014 advanced",
  "The Wire \u2014 Signature Season Curation (Signature Edition) \u2014 advanced",
  "The Office \u2014 Signature Season Curation (Signature Edition) \u2014 advanced",
  "Planet Earth \u2014 Signature Season Curation (Signature Edition) \u2014 advanced",
  "Breaking Bad \u2014 Signature Season Curation (Signature Edition) \u2014 advanced",
  "Game of Thrones \u2014 Signature Season Curation (Signature Edition) \u2014 advanced",
  "Cosmos: A Spacetime Odyssey \u2014 Signature Season Curation (Signature Edition) \u2014 advanced",
  "Stranger Things \u2014 Signature Season Curation (Signature Edition) \u2014 advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Signature Series Study — "+safe+"\n"
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
    name:topic+' — Signature series record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A Signature series record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"signature-series-record",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-shows-every-series-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('shows-every-series-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
