(function(){'use strict';
/* JAH The Egypt Database generator — jahdb-countries-egypt-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Samples are clearly labeled structural
   samples and are never archive records. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CTRYEG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Egypt \u2014 Geography and Landscape", "Egypt \u2014 Climate Zones", "Egypt \u2014 Regions and Administrative Divisions", "Egypt \u2014 Major Rivers and Lakes", "Egypt \u2014 Mountain Ranges", "Egypt \u2014 National Parks and Protected Areas", "Egypt \u2014 Population and Demographics", "Egypt \u2014 Languages", "Egypt \u2014 Religion and Belief", "Egypt \u2014 Flag and National Symbols", "Egypt \u2014 The Capital City", "Egypt \u2014 Major Cities"], "Compounded": ["Egypt \u2014 Government and Constitution", "Egypt \u2014 The Legislature", "Egypt \u2014 Political Parties and Elections", "Egypt \u2014 Economy Overview", "Egypt \u2014 Agriculture", "Egypt \u2014 Manufacturing and Industry", "Egypt \u2014 Technology and Services", "Egypt \u2014 Energy Production", "Egypt \u2014 Transportation Networks", "Egypt \u2014 Education System", "Egypt \u2014 Healthcare System"], "Advanced": ["Egypt \u2014 Ancient History", "Egypt \u2014 Medieval History", "Egypt \u2014 Early Modern Era", "Egypt \u2014 The 20th Century", "Egypt \u2014 The Modern Era", "Egypt \u2014 Culture \u2014 Cuisine", "Egypt \u2014 Culture \u2014 Music and Arts", "Egypt \u2014 Culture \u2014 Literature and Film", "Egypt \u2014 Culture \u2014 Sports", "Egypt \u2014 Science and Innovation", "Egypt \u2014 Foreign Policy and Alliances"]};
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
    description:'SAMPLE RECORD (generated — structural sample). A Egypt country record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:"jahdb-countries-egypt-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('countries-egypt',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
