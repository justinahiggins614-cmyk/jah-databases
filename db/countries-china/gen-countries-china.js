(function(){'use strict';
/* JAH The China Database generator — jahdb-countries-china-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Samples are clearly labeled structural
   samples and are never archive records. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CTRYCN-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["China \u2014 Geography and Landscape", "China \u2014 Climate Zones", "China \u2014 Provinces and Regions", "China \u2014 Major Rivers \u2014 Yangtze and Yellow", "China \u2014 Mountains and Plateaus", "China \u2014 Population and Demographics", "China \u2014 The Constitution and State Structure", "China \u2014 The Communist Party System", "China \u2014 The State Council and Premiership", "China \u2014 National People\u2019s Congress", "China \u2014 The Legal System", "China \u2014 Major Cities \u2014 Beijing"], "Compounded": ["China \u2014 Economy Overview", "China \u2014 Manufacturing \u2014 World Factory", "China \u2014 Technology Sector", "China \u2014 Agriculture", "China \u2014 Energy Production", "China \u2014 Transportation \u2014 High-Speed Rail", "China \u2014 Major Cities \u2014 Shanghai", "China \u2014 Greater Bay Area \u2014 Guangzhou-Shenzhen", "China \u2014 Education System", "China \u2014 Healthcare System", "China \u2014 Belt and Road Initiative"], "Advanced": ["China \u2014 Ancient Dynasties \u2014 Xia to Han", "China \u2014 Tang and Song Golden Ages", "China \u2014 Ming and Qing Dynasties", "China \u2014 The Century of Humiliation", "China \u2014 Founding of the PRC", "China \u2014 Reform and Opening Up", "China \u2014 Culture \u2014 Language and Writing", "China \u2014 Culture \u2014 Cuisine", "China \u2014 Culture \u2014 Philosophy and Thought", "China \u2014 Space Program", "China \u2014 Foreign Policy"]};
var DEMOKIND="country reference math";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Country demo: reference math with rounded public statistics. Educational illustration.\n# Topic: \""+safe+"\" | Field: "+field+"\n"
   + "record = {'topic': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "print('Sample record — structural sample, not an archive entry.')\n"
   + "print(record['topic'] + ' [' + record['field'] + ']')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic,
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A China country record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:"public-harvest",
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
var gen={version:"jahdb-countries-china-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('countries-china',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
