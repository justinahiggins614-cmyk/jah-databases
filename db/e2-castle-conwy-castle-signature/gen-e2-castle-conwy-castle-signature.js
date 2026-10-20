(function(){'use strict';
/* The Signature JAH Conwy Castle Castle Database generator — jahdb-e2-castle-conwy-castle-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Signature-original records. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-E2CASTLECONS-";
var SLUG="e2-castle-conwy-castle-signature";
var FIELDS=["Foundations","Compounded","Advanced"];
var GROUPS={Foundations:"guide",Compounded:"details",Advanced:"resources"};
var LADDERS={Foundations:1,Compounded:2,Advanced:3};
var TOPICS={"Foundations": ["The Signature Approach to Conwy Castle", "Signature Conwy Castle Principles", "The Signature Conwy Castle Starter System", "Signature Conwy Castle Vocabulary Reimagined", "Signature Conwy Castle Tools Reimagined", "Signature Conwy Castle Safety Redesign", "The Signature Conwy Castle Learning Path"], "Compounded": ["Signature Conwy Castle Method I: First Build", "Signature Conwy Castle Method II: Working Sessions", "Signature Conwy Castle Method III: Combinations", "Signature Conwy Castle Experience Design", "Signature Conwy Castle Quality System", "Signature Conwy Castle Troubleshooting Engine", "Signature Conwy Castle Cost and Time Philosophy"], "Advanced": ["Signature Conwy Castle Method IV: Mastery", "Signature Conwy Castle Method V: Performance", "Signature Conwy Castle Teaching System", "Signature Conwy Castle Community Model", "Signature Conwy Castle Future Concepts", "The Signature Conwy Castle Master Plan"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "// Signature drill — "+safe+"\n"
    + "// Field: "+field+" — run with: node drill.js\n"
    + "var CARDS=[\n"
    + "  ["+JSON.stringify(safe)+", "+JSON.stringify("A Signature-original "+"castle"+" creation.")+"],\n"
    + "  ["+JSON.stringify(field)+", "+JSON.stringify("Tier of the Signature "+"Conwy Castle"+" method.")+"]\n"
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
    d:"Signature-original "+"castle"+": "+topic+".",
    definition:topic+" — a Signature-original "+"castle"+" creation from the Signature system.",
    description:"SAMPLE RECORD (generated — structural sample). "+topic+": a Signature-original "+"castle"+" in the "+field+" tier of the Signature "+"Conwy Castle"+" method. Generated samples are clearly labeled and never presented as archive records or public record.",
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
var gen={version:"jahdb-e2-castle-conwy-castle-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
