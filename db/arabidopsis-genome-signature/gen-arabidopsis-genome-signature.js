(function(){'use strict';
/* JAH The Thale Cress Reference Genome (TAIR10) Database (Signature Edition) generator - JAH-AGS-1.0. Property of Justin Addam Higgins.
   Deterministic: same seed, same record. Hard stop: 10^15 records or complete-with-reason. */
var QUADRILLION=1e15;
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AGS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var LADDER=["simple","most competitive","mix-and-match","unmade","top-notch","future grade","god mode"];
var TOPICS={
 "Foundations":["Chromosome 1","Chromosome 2","Chromosome 3","Chromosome 4","Chromosome 5"],
 "Compounded":["Gene ABI1","Gene AG","Gene BRI1","Gene CLV1","Gene CO","Gene FLC","Gene FT","Gene PHYB"],
 "Advanced":["From Genome to Phenome","Mix-and-Match: Designed Pathways","The Deterministic Scale Ladder","Trait Drought tolerance","Trait Flowering time","Trait Leaf shape","Trait Phototropism","Unmade Genomes and Universal Abilities"]
};
function demoFor(field,topic){
 var safe=topic.replace(/\\/g,'\\\\').replace(/"/g,"'");
 return "// Generated sample demo - structural sample only\n"
 +"console.log(\u0022sample: "+safe+"\u0022);\n"
 +"console.log(\u0022tier: "+field+"\u0022);\n"
 +"console.log(\u0022ladder: chromosome>gene>protein>pathway>trait\u0022);\n";
}
function generate(seed,opts){
 opts=opts||{};var rnd=prng(seed);
 if(seed>QUADRILLION)return {id:PREFIX+"STOP",title:"Generator stop: quadrillion cap",sample:true,src:"generated",
  description:"Hard stop reached at 10^15 records.",disclaimer:"Stop record, not an archive record.",demo:{program:"console.log('stop');"}};
 var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
 var pool=TOPICS[field]||["General Study"];
 var topic=pick(pool,rnd);
 var id=PREFIX+String(seed).padStart(6,"0");
 return {id:id,name:topic+" - genome record",title:topic,sample:true,src:"generated",field:field,
  ladder:LADDER[(seed%LADDER.length)],
  description:"SAMPLE RECORD (generated - structural sample). '"+topic+"' in "+field+". Generated samples are clearly labeled and never presented as archive records.",
  disclaimer:"Generated sample record - not an archive record. Seeded archive records are authoritative.",
  demo:{kind:"genome-demo",language:"javascript",program:demoFor(field,topic),note:"Structural sample demo."},
  _seed:seed};
}
function validate(r){var e=[];
 if(!r||typeof r!=="object")return {ok:false,errors:["not an object"]};
 if(!new RegExp("^"+PREFIX.replace(/-/g,"\\-")+"(\\d{6}|STOP)$").test(r.id||""))e.push("id");
 if(!r.src)e.push("src");
 if(!r.demo||!r.demo.program)e.push("demo");
 return {ok:!e.length,errors:e};}
function driftCheck(record,sample){var d=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
 return d.length?{ok:false,errors:["duplicate topic+field"]}:{ok:true,errors:[]};}
var GEN={version:"JAH-AGS-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,cap:QUADRILLION,ladder:LADDER};
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator)JAHDB.registerGenerator("arabidopsis-genome-signature",GEN);
if(typeof module!=="undefined"&&module.exports)module.exports=GEN;
if(typeof window!=="undefined")window.GEN=GEN;
})();
