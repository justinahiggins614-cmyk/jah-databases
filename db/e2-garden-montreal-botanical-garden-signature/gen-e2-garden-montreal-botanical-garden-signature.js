(function(){'use strict';
/* The Signature JAH Montreal Botanical Garden Botanical Garden Database generator — jahdb-e2-garden-montreal-botanical-garden-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Signature-original records. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-E2GARDENMONS-";
var SLUG="e2-garden-montreal-botanical-garden-signature";
var FIELDS=["Foundations","Compounded","Advanced"];
var GROUPS={Foundations:"guide",Compounded:"details",Advanced:"resources"};
var LADDERS={Foundations:1,Compounded:2,Advanced:3};
var TOPICS={"Foundations": ["The Signature Approach to Montreal Botanical Garden Botanical Garden", "Signature Montreal Botanical Garden Botanical Garden Principles", "The Signature Montreal Botanical Garden Botanical Garden Starter System", "Signature Montreal Botanical Garden Botanical Garden Vocabulary Reimagined", "Signature Montreal Botanical Garden Botanical Garden Tools Reimagined", "Signature Montreal Botanical Garden Botanical Garden Safety Redesign", "The Signature Montreal Botanical Garden Botanical Garden Learning Path"], "Compounded": ["Signature Montreal Botanical Garden Botanical Garden Method I: First Build", "Signature Montreal Botanical Garden Botanical Garden Method II: Working Sessions", "Signature Montreal Botanical Garden Botanical Garden Method III: Combinations", "Signature Montreal Botanical Garden Botanical Garden Experience Design", "Signature Montreal Botanical Garden Botanical Garden Quality System", "Signature Montreal Botanical Garden Botanical Garden Troubleshooting Engine", "Signature Montreal Botanical Garden Botanical Garden Cost and Time Philosophy"], "Advanced": ["Signature Montreal Botanical Garden Botanical Garden Method IV: Mastery", "Signature Montreal Botanical Garden Botanical Garden Method V: Performance", "Signature Montreal Botanical Garden Botanical Garden Teaching System", "Signature Montreal Botanical Garden Botanical Garden Community Model", "Signature Montreal Botanical Garden Botanical Garden Future Concepts", "The Signature Montreal Botanical Garden Botanical Garden Master Plan"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "// Signature drill — "+safe+"\n"
    + "// Field: "+field+" — run with: node drill.js\n"
    + "var CARDS=[\n"
    + "  ["+JSON.stringify(safe)+", "+JSON.stringify("A Signature-original "+"botanical garden"+" creation.")+"],\n"
    + "  ["+JSON.stringify(field)+", "+JSON.stringify("Tier of the Signature "+"Montreal Botanical Garden Botanical Garden"+" method.")+"]\n"
    + "];\n"
    + "function drill(n){var o=[];n=Math.min(n,CARDS.length);for(var i=0;i<n;i++){var c=CARDS[(Math.random()*CARDS.length)|0];o.push('Q'+(i+1)+': '+c[0]+'\nA'+(i+1)+': '+c[1]);}return o.join('\n\n');}\n"
    + "console.log(drill(2));\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    title:topic,
    t:topic,
    name:topic,
    g:GROUPS[field]||"guide",
    c:0,
    l:LADDERS[field]||1,
    d:"Signature-original "+"botanical garden"+": "+topic+".",
    definition:topic+" — a Signature-original "+"botanical garden"+" creation from the Signature system.",
    description:"SAMPLE RECORD (generated — structural sample). "+topic+": a Signature-original "+"botanical garden"+" in the "+field+" tier of the Signature "+"Montreal Botanical Garden Botanical Garden"+" method. Generated samples are clearly labeled and never presented as archive records or public record.",
    field:field,
    facts:{topic:topic,field:field,origin:"created in the Signature system"},
    program:demoProgram(topic,field),
    language:"javascript",
    src:"signature",
    source:"signature",
    last_verified:"2026-10-19",
    sample:true,
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.program)e.push('program');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:"jahdb-e2-garden-montreal-botanical-garden-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
