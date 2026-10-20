(function(){'use strict';
/* JAH The Full Books: Gunslinger Tales Database generator - full-books-gunslinger-tales-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GTUN-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS=["Foundations: Gunslinger Tales - The Complete Guide", "The Virginian (1902) - Complete Book Record", "Riders of the Purple Sage (1912) - Complete Book Record", "The Log of a Cowboy (1903) - Complete Book Record", "The Lone Star Ranger (1915) - Complete Book Record", "The Luck of Roaring Camp (1868) - Complete Book Record", "The Outcasts of Poker Flat (1869) - Complete Book Record", "Oh! Susanna (context) (1848) - Complete Book Record", "A Texas Cowboy (1885) - Complete Book Record", "The Border Legion (1916) - Complete Book Record", "To the Last Man (1921) - Complete Book Record", "The Vanishing American (1925) - Complete Book Record", "Desert Gold (1913) - Complete Book Record", "The Code - Gunslinger Tales Craft Study", "Landscape as Character - Gunslinger Tales Craft Study", "The Showdown Structure - Gunslinger Tales Craft Study", "The Vanishing World - Gunslinger Tales Craft Study", "Authenticity's Value - Gunslinger Tales Craft Study", "The Outsider Hero - Gunslinger Tales Craft Study", "The Gunslinger Tales Reading Pathway"];
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# "+safe+"\n# Field: "+field+"\nrecord={'title': \""+safe+"\", 'field': \""+field+"\"}\nprint('Record: '+record['title']+' ['+record['field']+']')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var topic=pick(TOPICS,rnd);
  return {id:PREFIX+String(seed).padStart(6,'0'),title:topic,field:field,src:'public-harvest',
    summary:'Generated record for '+topic+'.',demo:{language:'python',program:demoProgram(topic,field)},_seed:seed};
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
var gen={version:'full-books-gunslinger-tales-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('full-books-gunslinger-tales',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
