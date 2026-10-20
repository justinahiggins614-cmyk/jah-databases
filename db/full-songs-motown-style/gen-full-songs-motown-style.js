(function(){'use strict';
/* JAH The Full Songs: Motown Style Database generator - full-songs-motown-style-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MSOT-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS=["Foundations: Motown Style - The Complete Guide", "Motown Style Etude No. 1: Dancing I\u2013IV\u2013V", "My Girl - Motown Style Song Study", "Motown Style Etude No. 2: Groove I\u2013VII\u2013IV", "I Heard It Through the Grapevine - Motown Style Song Study", "Motown Style Etude No. 3: Dancing I\u2013IV\u2013V", "Superstition - Motown Style Song Study", "Motown Style Etude No. 4: Groove I\u2013VII\u2013IV", "Respect - Motown Style Song Study", "Motown Style Etude No. 5: Dancing I\u2013IV\u2013V", "Ain't No Mountain High Enough - Motown Style Song Study", "Motown Style Etude No. 6: Groove I\u2013VII\u2013IV", "Dancing in the Street - Motown Style Song Study", "Motown Style Etude No. 7: Dancing I\u2013IV\u2013V", "My Girl - Motown Style Song Study", "Motown Style Etude No. 8: Groove I\u2013VII\u2013IV", "I Heard It Through the Grapevine - Motown Style Song Study", "Motown Style Etude No. 9: Dancing I\u2013IV\u2013V", "Superstition - Motown Style Song Study", "Motown Style Etude No. 10: Groove I\u2013VII\u2013IV"];
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
var gen={version:'full-songs-motown-style-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('full-songs-motown-style',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
