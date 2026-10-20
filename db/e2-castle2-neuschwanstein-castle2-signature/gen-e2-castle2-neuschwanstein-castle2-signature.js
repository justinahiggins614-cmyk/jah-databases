(function(){'use strict';
/* The Signature JAH Neuschwanstein Castle2 Database generator — jahdb-e2-castle2-neuschwanstein-castle2-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Signature-original records. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-E2CASTLE2NES-";
var SLUG="e2-castle2-neuschwanstein-castle2-signature";
var FIELDS=["Foundations","Compounded","Advanced"];
var GROUPS={Foundations:"guide",Compounded:"details",Advanced:"resources"};
var LADDERS={Foundations:1,Compounded:2,Advanced:3};
var TOPICS={"Foundations": ["The Signature Approach to Neuschwanstein Castle2", "Signature Neuschwanstein Castle2 Principles", "The Signature Neuschwanstein Castle2 Starter System", "Signature Neuschwanstein Castle2 Vocabulary Reimagined", "Signature Neuschwanstein Castle2 Tools Reimagined", "Signature Neuschwanstein Castle2 Safety Redesign", "The Signature Neuschwanstein Castle2 Learning Path"], "Compounded": ["Signature Neuschwanstein Castle2 Method I: First Build", "Signature Neuschwanstein Castle2 Method II: Working Sessions", "Signature Neuschwanstein Castle2 Method III: Combinations", "Signature Neuschwanstein Castle2 Experience Design", "Signature Neuschwanstein Castle2 Quality System", "Signature Neuschwanstein Castle2 Troubleshooting Engine", "Signature Neuschwanstein Castle2 Cost and Time Philosophy"], "Advanced": ["Signature Neuschwanstein Castle2 Method IV: Mastery", "Signature Neuschwanstein Castle2 Method V: Performance", "Signature Neuschwanstein Castle2 Teaching System", "Signature Neuschwanstein Castle2 Community Model", "Signature Neuschwanstein Castle2 Future Concepts", "The Signature Neuschwanstein Castle2 Master Plan"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "// Signature drill — "+safe+"\n"
    + "// Field: "+field+" — run with: node drill.js\n"
    + "var CARDS=[\n"
    + "  ["+JSON.stringify(safe)+", "+JSON.stringify("A Signature-original "+"castle"+" creation.")+"],\n"
    + "  ["+JSON.stringify(field)+", "+JSON.stringify("Tier of the Signature "+"Neuschwanstein Castle2"+" method.")+"]\n"
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
    description:"SAMPLE RECORD (generated — structural sample). "+topic+": a Signature-original "+"castle"+" in the "+field+" tier of the Signature "+"Neuschwanstein Castle2"+" method. Generated samples are clearly labeled and never presented as archive records or public record.",
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
var gen={version:"jahdb-e2-castle2-neuschwanstein-castle2-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
