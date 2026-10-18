(function(){'use strict';
/* JAH Train Travel Japan Database generator — jahdb-train-travel-japan-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TTJPS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Trains in Japan: An Overview",
  "The Shinkansen, Explained",
  "The Japan Rail Pass, Explained",
  "Buying Tickets in Japan",
  "Reserved vs Non-Reserved Seats",
  "The Tokyo Rail Network",
  "IC Cards: Suica and Pasmo",
  "Luggage on Japanese Trains",
  "Train Etiquette in Japan",
  "Station Bento (Ekiben)",
  "Planning Around Train Schedules"
 ],
 "Compounded": [
  "The Tokaido Shinkansen: Tokyo to Osaka",
  "The Tohoku Shinkansen: Into the North",
  "The Hokuriku Shinkansen: To Kanazawa",
  "The Kyushu Shinkansen: South to Kagoshima",
  "The Hokkaido Shinkansen",
  "Sleeper Trains in Japan",
  "Scenic Railways: The Sagano Romantic Train",
  "The Hakone Romancecar and Mountain Railways",
  "Private Railways: Kintetsu and Hankyu",
  "Day Trips by Train from Tokyo",
  "Day Trips by Train from Osaka and Kyoto",
  "The Seishun 18 Ticket"
 ],
 "Advanced": [
  "Rail Pass Alternatives",
  "Advanced: The Complete Rail Circuit of Japan",
  "Advanced: The Seven Stars in Kyushu",
  "Advanced: Twilight Express Mizukaze",
  "Advanced: Station Architecture",
  "Advanced: The Rail Fan’s Japan",
  "Advanced: Teaching Japan Rail Travel",
  "Advanced: The Japan Rail Journal",
  "Advanced: Accessibility on Japanese Trains",
  "Advanced: The Japan Rail Year",
  "The Train Travel Japan Encyclopedia"
 ]
};
var DEMOKIND="node-demo";
var SAMPLEDESC="Sample records are complete japan rail travel record entries with real measurement math.";
function demoProgram(topic,field){
  return "'use strict';\n// "+topic+" \u2014 sample demo.\n// Field: "+field+"\nconst a = 12;\nconst b = 4;\nconst r = a / b;\nconsole.log('sample ratio = ' + r.toFixed(2));\nif (!isFinite(r)) throw new Error('bad');\nconsole.log('DEMO_OK');\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — japan rail travel record record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A japan rail travel record record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:DEMOKIND,language:'node',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-train-travel-japan-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('train-travel-japan-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
