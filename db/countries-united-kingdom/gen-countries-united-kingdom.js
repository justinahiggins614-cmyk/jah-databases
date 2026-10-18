(function(){'use strict';
/* JAH The United Kingdom Database generator — jahdb-countries-united-kingdom-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Samples are clearly labeled structural
   samples and are never archive records. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CTRYUK-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["United Kingdom \u2014 Geography and Landscape", "United Kingdom \u2014 Climate Zones", "United Kingdom \u2014 Regions and Administrative Divisions", "United Kingdom \u2014 Major Rivers and Lakes", "United Kingdom \u2014 Mountain Ranges", "United Kingdom \u2014 National Parks and Protected Areas", "United Kingdom \u2014 Population and Demographics", "United Kingdom \u2014 Languages", "United Kingdom \u2014 Religion and Belief", "United Kingdom \u2014 Flag and National Symbols", "United Kingdom \u2014 The Capital City", "United Kingdom \u2014 Major Cities"], "Compounded": ["United Kingdom \u2014 Government and Constitution", "United Kingdom \u2014 The Legislature", "United Kingdom \u2014 Political Parties and Elections", "United Kingdom \u2014 Economy Overview", "United Kingdom \u2014 Agriculture", "United Kingdom \u2014 Manufacturing and Industry", "United Kingdom \u2014 Technology and Services", "United Kingdom \u2014 Energy Production", "United Kingdom \u2014 Transportation Networks", "United Kingdom \u2014 Education System", "United Kingdom \u2014 Healthcare System"], "Advanced": ["United Kingdom \u2014 Ancient History", "United Kingdom \u2014 Medieval History", "United Kingdom \u2014 Early Modern Era", "United Kingdom \u2014 The 20th Century", "United Kingdom \u2014 The Modern Era", "United Kingdom \u2014 Culture \u2014 Cuisine", "United Kingdom \u2014 Culture \u2014 Music and Arts", "United Kingdom \u2014 Culture \u2014 Literature and Film", "United Kingdom \u2014 Culture \u2014 Sports", "United Kingdom \u2014 Science and Innovation", "United Kingdom \u2014 Foreign Policy and Alliances"]};
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
    description:'SAMPLE RECORD (generated — structural sample). A United Kingdom country record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:"jahdb-countries-united-kingdom-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('countries-united-kingdom',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
