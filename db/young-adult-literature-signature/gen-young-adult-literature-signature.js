(function(){'use strict';
/* JAH The Music Genres Database generator — jahdb-young-adult-literature-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-YALS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is YA Literature (Signature edition)",
  "The Outsiders (Signature edition)",
  "The Giver (Signature edition)",
  "Harry Potter and YA (Signature edition)",
  "The Hunger Games (Signature edition)",
  "The Fault in Our Stars (Signature edition)",
  "Wonder (Signature edition)",
  "The Hate U Give (Signature edition)",
  "Percy Jackson and the Olympians (Signature edition)",
  "Divergent (Signature edition)",
  "The Perks of Being a Wallflower (Signature edition)"
 ],
 "Compounded": [
  "Dystopian YA Wave (Signature edition)",
  "YA Fantasy Boom (Signature edition)",
  "Contemporary YA Realism (Signature edition)",
  "Verse Novels for Teens (Signature edition)",
  "Graphic Novels for YA (Signature edition)",
  "The John Green Effect (Signature edition)",
  "YA BookTok (Signature edition)",
  "Diverse YA (Signature edition)",
  "Coming-of-Age Structure (Signature edition)",
  "The Love Triangle (Signature edition)",
  "Series vs Standalone (Signature edition)",
  "School Stories (Signature edition)"
 ],
 "Advanced": [
  "YA Criticism and Kidult Readers (Signature edition)",
  "Censorship and YA (Signature edition)",
  "The We Need Diverse Books Movement (Signature edition)",
  "YA Awards (Printz) (Signature edition)",
  "Mental Health in YA (Signature edition)",
  "Romance in YA (Signature edition)",
  "Dark YA (Signature edition)",
  "The Business of YA (Signature edition)",
  "Fan Communities (Signature edition)",
  "Adaptations (Signature edition)",
  "Own Voices (Signature edition)"
 ]
};
var DEMOKIND="age-band matching";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Age-band matcher — "+safe+"\n"
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
    name:topic+' — music genre record',
    title:topic,
    description:'SIGNATURE SAMPLE (generated — structural sample). A music genre record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:DEMOKIND,language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-young-adult-literature-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('young-adult-literature-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
