(function(){'use strict';
/* JAH The Germany Database generator — jahdb-countries-germany-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Samples are clearly labeled structural
   samples and are never archive records. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CTRYDE-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Germany \u2014 Geography and Landscape", "Germany \u2014 Climate Zones", "Germany \u2014 Regions and Administrative Divisions", "Germany \u2014 Major Rivers and Lakes", "Germany \u2014 Mountain Ranges", "Germany \u2014 National Parks and Protected Areas", "Germany \u2014 Population and Demographics", "Germany \u2014 Languages", "Germany \u2014 Religion and Belief", "Germany \u2014 Flag and National Symbols", "Germany \u2014 The Capital City", "Germany \u2014 Major Cities"], "Compounded": ["Germany \u2014 Government and Constitution", "Germany \u2014 The Legislature", "Germany \u2014 Political Parties and Elections", "Germany \u2014 Economy Overview", "Germany \u2014 Agriculture", "Germany \u2014 Manufacturing and Industry", "Germany \u2014 Technology and Services", "Germany \u2014 Energy Production", "Germany \u2014 Transportation Networks", "Germany \u2014 Education System", "Germany \u2014 Healthcare System"], "Advanced": ["Germany \u2014 Ancient History", "Germany \u2014 Medieval History", "Germany \u2014 Early Modern Era", "Germany \u2014 The 20th Century", "Germany \u2014 The Modern Era", "Germany \u2014 Culture \u2014 Cuisine", "Germany \u2014 Culture \u2014 Music and Arts", "Germany \u2014 Culture \u2014 Literature and Film", "Germany \u2014 Culture \u2014 Sports", "Germany \u2014 Science and Innovation", "Germany \u2014 Foreign Policy and Alliances"]};
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
    description:'SAMPLE RECORD (generated — structural sample). A Germany country record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:"jahdb-countries-germany-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('countries-germany',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
