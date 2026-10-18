(function(){'use strict';
/* JAH Unhinged Idea Generator - jahdb-gen-unhinged-idea-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL client-side generator: combinatorial unhinged ideas. Same seed, same idea.
   public edition. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX="JAH-HUIG-";
var FIELDS=["Gadgets", "Home", "Daily Life"];
var THINGS={"Gadgets": ["a toaster", "an alarm clock", "a doorbell", "a lamp"], "Home": ["a houseplant", "a pillow", "a fridge", "an umbrella"], "Daily Life": ["a backpack", "a toothbrush", "a spatula", "a pair of socks"]};
var UPGRADES=["that gives motivational speeches", "with built-in karaoke", "that files your taxes", "that judges your life choices (lovingly)", "with a tiny weather system inside", "that live-streams its opinions", "with emotional support features", "that predicts the stock market (badly)", "with a built-in lie detector", "that writes poetry about you", "with turbo mode", "that has unionized and demands weekends"];
var BENEFITS=["increases productivity by 400% (unverified)", "reduces existential dread", "impresses houseguests", "counts as a personality trait", "solves boredom permanently", "makes Mondays 12% better", "is a guaranteed conversation starter", "ships with 50% more chaos"];
var WARNINGS=["Side effects include spontaneous jazz.", "Do not operate while emotional.", "May develop opinions.", "Not responsible for enlightenment.", "Keep away from philosophers.", "May cause sudden expertise.", "Do not feed after midnight.", "Consult your cat before use."];
var SOURCE='public';
function pick(r,arr){return arr[(r()*arr.length)|0];}
function assemble(seed,field){
  var r=prng(seed>>>0||1);
  var f=(field&&THINGS[field])?field:pick(r,FIELDS);
  var th=pick(r,THINGS[f]), up=pick(r,UPGRADES), be=pick(r,BENEFITS), wa=pick(r,WARNINGS);
  return {field:f,thing:th,upgrade:up,benefit:be,warning:wa,
          idea:'What if '+th+' '+up+'? It '+be+'. Warning: '+wa};
}
function demoProgram(a){
  function q(s){return s.replace(/"/g,"'");}
  return '# Unhinged Idea Generator - live idea\nprint("FIELD:   '+q(a.field)+'")\nprint("THING:   '+q(a.thing)+'")\nprint("UPGRADE: '+q(a.upgrade)+'")\nprint("BENEFIT: '+q(a.benefit)+'")\nprint("WARNING: '+q(a.warning)+'")\nprint()\nprint("IDEA: '+q(a.idea)+'")\nprint("OK: unhinged idea assembled from 4 banks")\n';
}
function generate(seed,opts,rnd){
  opts=opts||{};
  var a=assemble(seed>>>0||1,opts.field||null);
  var id=PREFIX+String(seed>>>0||1).padStart(6,'0');
  var title='Fresh Idea: '+a.thing.charAt(0).toUpperCase()+a.thing.slice(1)+' '+a.upgrade+(SOURCE==='signature'?' (Signature Edition)':'');
  return {
    id:id,
    name:title+' — '+a.field,
    title:title,
    description:'GENERATED IDEA (live generator output - clearly labeled fiction). "'+a.idea+'"',
    field:a.field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Live generator output - fictional concept, not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:demoProgram(a),note:'Live idea demo program.'},
    _seed:seed>>>0||1, parts:a
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  if(!r.parts||!r.parts.idea)e.push('parts');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-gen-unhinged-idea-generator-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,assemble:assemble};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gen-unhinged-idea-generator',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
