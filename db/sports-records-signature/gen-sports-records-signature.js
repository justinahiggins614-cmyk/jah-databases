(function(){'use strict';
/* JAH Sports Records Signature Database generator — jahdb-sports-records-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SPORTRECS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["What Counts as a World Record (Signature Edition)", "Ratification Bodies (World Athletics and Others) (Signature Edition)", "The 100m Sprint Record Line (Signature Edition)", "Marathon Record Progression (Signature Edition)", "The Long Jump (Beamon 1968) (Signature Edition)", "Swimming World Records and Tech Suits (Signature Edition)", "Weightlifting Records and Weight Classes (Signature Edition)", "Cycling Hour Record (Signature Edition)", "Speed Skating Records (Signature Edition)", "Official vs Claimed Records (Signature Edition)", "Why Records Keep Falling (Signature Edition)"], "Compounded": ["Bolt's 9.58 (Berlin 2009) (Signature Edition)", "The Sub-2 Marathon (INEOS 1:59) (Signature Edition)", "Phelps's Medal Haul (Signature Edition)", "The Home Run Records (Signature Edition)", "Wilt's 100-Point Game (Signature Edition)", "Gretzky's Points Records (Signature Edition)", "Bradman's 99.94 Average (Signature Edition)", "Pele's Goal Tally (Signature Edition)", "Ripken's 2,632 Streak (Signature Edition)", "DiMaggio's 56-Game Streak (Signature Edition)", "Secretariat's Belmont (31 Lengths) (Signature Edition)", "Photo-Finish Verification Technology (Signature Edition)"], "Advanced": ["Record Progression Analytics (Signature Edition)", "Equipment Technology Effects (Signature Edition)", "Altitude and Fast Tracks (Signature Edition)", "Models of Human Limits (Signature Edition)", "Women's Records Progression (Signature Edition)", "Masters and Age-Group Records (Signature Edition)", "Para-Sport Records (Signature Edition)", "Stripped Records Policy (Signature Edition)", "The Most Unbreakable Records Debate (Signature Edition)", "The Sub-2-Hour Marathon Science (Signature Edition)", "Data Integrity in Record Keeping (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# record-progression-demo \u2014 "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record \u2014 structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' \u2014 sports record entry',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A sports record entry of \"'+topic+'\" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"record-progression-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-sports-records-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('sports-records-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
