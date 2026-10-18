(function(){'use strict';
/* JAH The Social Etiquette Explorer Database Signature Database generator — jahdb-db-social-etiquette-explorer-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SOCETIEXPS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Etiquette: Meeting someone new",
  "Etiquette: At the dinner table",
  "Etiquette: On the phone",
  "Etiquette: In line",
  "Etiquette: Saying thank you",
  "Etiquette: Apologizing",
  "Etiquette: Giving gifts",
  "Etiquette: At work",
  "Etiquette: With elders",
  "Etiquette: With children",
  "Etiquette: In public"
 ],
 "Compounded": [
  "Etiquette: Difficult dinners",
  "Etiquette: Weddings",
  "Etiquette: Funerals",
  "Etiquette: Job interviews",
  "Etiquette: First dates",
  "Etiquette: Houseguests",
  "Etiquette: Hosting",
  "Etiquette: Tipping",
  "Etiquette: Online",
  "Etiquette: Disagreements",
  "Etiquette: Compliments",
  "Etiquette: Criticism"
 ],
 "Advanced": [
  "Etiquette: State dinners",
  "Etiquette: Cultural differences",
  "Etiquette: Power dynamics",
  "Etiquette: Public speaking",
  "Etiquette: Media interviews",
  "Etiquette: Negotiations",
  "Etiquette: Ceremonies",
  "Etiquette: Condolences",
  "Etiquette: Celebrations",
  "Etiquette: Farewells",
  "Etiquette: Reunions"
 ]
};
var DEMOKIND="grace-proof";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Etiquette Study — "+safe+"\n"
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
    name:topic+' — etiquette guide record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A etiquette guide record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-db-social-etiquette-explorer-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-social-etiquette-explorer-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
