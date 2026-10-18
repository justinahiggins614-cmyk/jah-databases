(function(){'use strict';
/* JAH The Brazil Database generator — jahdb-countries-brazil-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Samples are clearly labeled structural
   samples and are never archive records. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CTRYBR-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Brazil \u2014 Geography and Landscape", "Brazil \u2014 Climate Zones", "Brazil \u2014 Regions and Administrative Divisions", "Brazil \u2014 Major Rivers and Lakes", "Brazil \u2014 Mountain Ranges", "Brazil \u2014 National Parks and Protected Areas", "Brazil \u2014 Population and Demographics", "Brazil \u2014 Languages", "Brazil \u2014 Religion and Belief", "Brazil \u2014 Flag and National Symbols", "Brazil \u2014 The Capital City", "Brazil \u2014 Major Cities"], "Compounded": ["Brazil \u2014 Government and Constitution", "Brazil \u2014 The Legislature", "Brazil \u2014 Political Parties and Elections", "Brazil \u2014 Economy Overview", "Brazil \u2014 Agriculture", "Brazil \u2014 Manufacturing and Industry", "Brazil \u2014 Technology and Services", "Brazil \u2014 Energy Production", "Brazil \u2014 Transportation Networks", "Brazil \u2014 Education System", "Brazil \u2014 Healthcare System"], "Advanced": ["Brazil \u2014 Ancient History", "Brazil \u2014 Medieval History", "Brazil \u2014 Early Modern Era", "Brazil \u2014 The 20th Century", "Brazil \u2014 The Modern Era", "Brazil \u2014 Culture \u2014 Cuisine", "Brazil \u2014 Culture \u2014 Music and Arts", "Brazil \u2014 Culture \u2014 Literature and Film", "Brazil \u2014 Culture \u2014 Sports", "Brazil \u2014 Science and Innovation", "Brazil \u2014 Foreign Policy and Alliances"]};
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
    description:'SAMPLE RECORD (generated — structural sample). A Brazil country record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:"jahdb-countries-brazil-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('countries-brazil',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
