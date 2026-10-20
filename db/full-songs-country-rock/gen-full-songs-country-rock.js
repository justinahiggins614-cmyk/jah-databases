(function(){'use strict';
/* JAH The Full Songs: Country Rock Database generator - full-songs-country-rock-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CROU-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS=["Foundations: Country Rock - The Complete Guide", "Country Rock Etude No. 1: Eagles vi\u2013IV\u2013I\u2013V", "Hotel California - Country Rock Song Study", "Country Rock Etude No. 2: Desert ii\u2013V\u2013I", "Take It Easy - Country Rock Song Study", "Country Rock Etude No. 3: Eagles vi\u2013IV\u2013I\u2013V", "Desperado - Country Rock Song Study", "Country Rock Etude No. 4: Desert ii\u2013V\u2013I", "Sin City - Country Rock Song Study", "Country Rock Etude No. 5: Eagles vi\u2013IV\u2013I\u2013V", "Peaceful Easy Feeling - Country Rock Song Study", "Country Rock Etude No. 6: Desert ii\u2013V\u2013I", "Teach Your Children - Country Rock Song Study", "Country Rock Etude No. 7: Eagles vi\u2013IV\u2013I\u2013V", "Hotel California - Country Rock Song Study", "Country Rock Etude No. 8: Desert ii\u2013V\u2013I", "Take It Easy - Country Rock Song Study", "Country Rock Etude No. 9: Eagles vi\u2013IV\u2013I\u2013V", "Desperado - Country Rock Song Study", "Country Rock Etude No. 10: Desert ii\u2013V\u2013I"];
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
var gen={version:'full-songs-country-rock-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('full-songs-country-rock',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
