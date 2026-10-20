(function(){'use strict';
/* JAH The Full Books: Ghost Ships Database generator - full-books-ghost-ships-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GSHO2-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS=["Foundations: Ghost Ships - The Complete Guide", "Carmilla (1872) - Complete Book Record", "The Turn of the Screw (1898) - Complete Book Record", "The Monkey's Paw (1902) - Complete Book Record", "The Dunwich Horror: Context (1929) - Complete Book Record", "Dagon (1919) - Complete Book Record", "The Fall of the House of Usher (1839) - Complete Book Record", "The Strange Case of Dr Jekyll and Mr Hyde (1886) - Complete Book Record", "Dracula (1897) - Complete Book Record", "Frankenstein (1818) - Complete Book Record", "The Tell-Tale Heart (1843) - Complete Book Record", "The Call of Cthulhu (1928) - Complete Book Record", "The Great God Pan (1894) - Complete Book Record", "Suggestion Over Spectacle - Ghost Ships Craft Study", "The Unreliable Haunting - Ghost Ships Craft Study", "Cosmic Indifference - Ghost Ships Craft Study", "The Documented Unreal - Ghost Ships Craft Study", "Horror's Women See Clearly - Ghost Ships Craft Study", "Horror's Moral Engine - Ghost Ships Craft Study", "The Ghost Ships Reading Pathway"];
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
var gen={version:'full-books-ghost-ships-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('full-books-ghost-ships',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
