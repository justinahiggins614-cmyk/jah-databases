(function(){'use strict';
/* JAH The Full Songs: Bluegrass Database generator - full-songs-bluegrass-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BLUE-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS=["Foundations: Bluegrass - The Complete Guide", "In the Pines (Where Did You Sleep Last Night) - Complete Public-Domain Song", "Blue Moon of Kentucky - Bluegrass Song Study", "Bluegrass Etude No. 1: Waltz I\u2013IV\u2013V", "Foggy Mountain Breakdown - Bluegrass Song Study", "Bluegrass Etude No. 2: G-run turnaround", "Man of Constant Sorrow - Bluegrass Song Study", "Bluegrass Etude No. 3: Waltz I\u2013IV\u2013V", "Rocky Top - Bluegrass Song Study", "Bluegrass Etude No. 4: G-run turnaround", "Dueling Banjos - Bluegrass Song Study", "Bluegrass Etude No. 5: Waltz I\u2013IV\u2013V", "I'll Fly Away - Bluegrass Song Study", "Bluegrass Etude No. 6: G-run turnaround", "Blue Moon of Kentucky - Bluegrass Song Study", "Bluegrass Etude No. 7: Waltz I\u2013IV\u2013V", "Foggy Mountain Breakdown - Bluegrass Song Study", "Bluegrass Etude No. 8: G-run turnaround", "Man of Constant Sorrow - Bluegrass Song Study", "Bluegrass Etude No. 9: Waltz I\u2013IV\u2013V"];
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
var gen={version:'full-songs-bluegrass-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('full-songs-bluegrass',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
