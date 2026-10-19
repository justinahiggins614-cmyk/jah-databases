(function(){'use strict';
/* JAH Rhyme Database generator — jahdb-rhyme-1.0.
   Property of Justin Addam Higgins (JAH).
   A full rhyming dictionary of real English words: perfect rhymes, near rhymes, rhyme families, syllable counts, and examp
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-RHY';
var FIELDS=["-abel", "-able", "-ack", "-addle", "-adow", "-ail", "-ain", "-ainbow", "-ale", "-all", "-an", "-ance", "-andle", "-angle", "-ap", "-ar", "-arble", "-art", "-ash", "-at", "-attle", "-away", "-awn", "-ay", "-eadow", "-eagle", "-eal", "-eam", "-eat", "-echo", "-eck", "-ee", "-eedle", "-eel", "-een", "-eep", "-eeple", "-eet", "-eetle", "-egal", "-elbow", "-ell", "-ellow", "-elp", "-elt", "-elve", "-em", "-en", "-ence", "-end", "-end2", "-ent", "-entle", "-eople", "-ept", "-ern", "-ero", "-ertile", "-ess", "-est", "-et", "-etal", "-ettle", "-ew", "-ext", "-ice", "-ick", "-iddle", "-ide", "-igh", "-ight", "-ignal", "-ild", "-ile", "-illow", "-ime", "-imple", "-in", "-inal", "-indow", "-ine", "-ing", "-ingle", "-ip", "-ircle", "-ire", "-ise", "-it", "-ital", "-ite", "-itle", "-ittle", "-ival", "-ive", "-ize", "-ocal", "-ock", "-oil", "-old", "-ole", "-ollow", "-ome", "-one", "-one2", "-ong", "-ood", "-ook", "-ool", "-oom", "-oon", "-oop", "-oor", "-oot", "-op", "-oral", "-orn", "-orning", "-orrow", "-orse", "-ory", "-oss", "-ost", "-ot", "-ottle", "-ouble", "-oud", "-ound", "-ouse", "-out", "-oval", "-ove", "-ower", "-own", "-oy", "-oyal", "-qual", "-quel", "-ual", "-ub", "-ubble", "-uck", "-uddle", "-ue", "-uff", "-ug", "-um", "-umble", "-ump", "-un", "-ungle", "-unk", "-ur", "-ural", "-urb", "-urge", "-url", "-urn", "-urple", "-urse", "-urtle", "-ush", "-ust", "-ut", "-y", "thunder", "river", "summer", "winter", "garden", "rocket", "castle", "bridge", "ocean", "forest"];
var NAMES=["cat", "hat", "man", "can", "day", "say", "light", "night", "time", "rhyme", "song", "long", "heart", "part", "dream", "stream", "love", "dove", "moon", "soon", "thunder", "river", "summer", "winter", "garden", "rocket", "castle", "bridge", "ocean", "forest"];
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var name=pick(NAMES,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id, name:name, title:name,
    description:'SAMPLE RECORD (generated — structural sample). A '+field+' rhyme entries generated deterministically from seed '+seed+'. Generated samples are clearly labeled and never presented as real records.',
    field:field, src:'signature-generated-sample', sample:true,
    disclaimer:'Generated sample record — not a real entry. Seeded archive records are the authoritative entries.',
    demo:{kind:'sample',program:"function sample(){return '"+name+"';}",note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||r.name.length<2)e.push('name');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.name===record.name;});
  return dups.length?{ok:false,errors:['duplicate name in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-rhyme-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('rhyme',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
