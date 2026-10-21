(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["mechanical", "thermal", "chemical", "regulatory", "supply"];
var PREFIX='JAH-ENGINE-';
var USE="Used by design and procurement engineers when the specified material is unavailable or too costly.";
var FLD=[["rule", "Rule"], ["matches", "Matches"], ["risk", "Risk"]];
var DEMO="# {title} - property match score (python3)\nratios=[{d1}, {d2}, {d3}]\nworst=min(ratios)\nprint(\"property ratios:\", ratios, \"worst=%.2f\" % worst)\nprint(\"SUBSTITUTE OK\" if worst >= 0.9 else \"REJECT SUBSTITUTE\")\n";
var SIG=false;
var SRC="public-harvest";
var B=[["mechanical", "Equivalent Grade Swap", "Replaces with a standardized equivalent grade (e.g. 304 -> 304L) from material specs.", "Equivalent Grade Swap", "grade tables", "low", "1.0", "0.98", "1.02"], ["thermal", "Property-envelope Match", "Requires the substitute's properties to enclose the original's across the operating range.", "Property-envelope Match", "datasheets", "medium", "0.95", "1.05", "0.97"], ["chemical", "Tensile Strength Parity", "Matches ultimate and yield strength so structural margins are preserved.", "Tensile Strength Parity", "test reports", "medium", "1.03", "0.99", "1.0"], ["regulatory", "Corrosion Equivalence", "Matches corrosion resistance in the actual service environment, not just salt spray.", "Corrosion Equivalence", "exposure data", "high", "0.92", "1.0", "0.95"], ["supply", "Temperature Rating Match", "Keeps continuous and peak temperature ratings at or above the original.", "Temperature Rating Match", "ratings", "medium", "1.0", "1.1", "0.96"], ["mechanical", "Fatigue Life Equivalence", "Matches S-N behavior so cyclic life predictions stay valid.", "Fatigue Life Equivalence", "fatigue data", "high", "0.94", "0.97", "1.02"], ["thermal", "Density Trade-off", "Accepts a density change only if mass budgets and dynamics still close.", "Density Trade-off", "mass budget", "low", "1.08", "0.99", "1.0"], ["chemical", "Cost-driven Substitution", "Substitutes a cheaper material only after re-validating every affected requirement.", "Cost-driven Substitution", "cost analysis", "medium", "0.96", "1.0", "0.93"], ["regulatory", "Availability-driven Swap", "Uses an in-stock alternate during shortages with documented temporary approval.", "Availability-driven Swap", "stock", "medium", "0.95", "0.98", "1.01"], ["supply", "Regulatory-approved Alternate", "Limits substitutes to those already qualified by the applicable standard.", "Regulatory-approved Alternate", "approvals", "low", "1.0", "1.0", "1.0"], ["mechanical", "Form-fit-function Match", "For COTS parts, requires identical form, fit, and function with test proof.", "Form-fit-function Match", "test", "low", "1.0", "0.99", "1.0"], ["thermal", "Surface Treatment Parity", "Matches coatings and finishes so wear and corrosion behavior carry over.", "Surface Treatment Parity", "process specs", "medium", "0.97", "1.0", "0.94"], ["chemical", "Weldability Match", "Confirms the substitute welds with qualified procedures without cracking.", "Weldability Match", "weld tests", "high", "0.93", "0.96", "0.99"], ["regulatory", "Recyclability Upgrade", "Prefers substitutes with better end-of-life recyclability when properties allow.", "Recyclability Upgrade", "LCA", "low", "1.02", "1.0", "0.98"], ["supply", "Biocompatibility Match", "For medical parts, requires equal or better biocompatibility certification.", "Biocompatibility Match", "ISO 10993", "high", "1.0", "1.0", "1.0"], ["mechanical", "Flammability Rating", "Matches UL94 or equivalent flammability rating for the application.", "Flammability Rating", "UL ratings", "medium", "1.0", "1.0", "0.97"], ["thermal", "UV Resistance Parity", "Matches weathering resistance for outdoor service.", "UV Resistance Parity", "UV test", "medium", "0.95", "0.98", "1.0"], ["chemical", "Chemical Compatibility", "Verifies resistance to every chemical the part will contact.", "Chemical Compatibility", "compatibility chart", "high", "0.96", "0.94", "0.99"], ["regulatory", "Creep Resistance", "Matches long-term deformation under sustained load at temperature.", "Creep Resistance", "creep data", "high", "0.92", "0.95", "0.97"], ["supply", "Hardness Match", "Keeps surface hardness within the range the wear design assumed.", "Hardness Match", "hardness tests", "low", "1.01", "0.99", "1.0"]];
function buildTitle(b){ return SIG?('Signature '+b[1]):b[1]; }
function buildDesc(b){
  var d=b[2]+' Recorded facts \u2014 '+FLD[0][1]+': '+b[3]+'; '+FLD[1][1]+': '+b[4]+'; '+FLD[2][1]+': '+b[5]+'. '+USE;
  if(SIG) d='Signature-original: '+d+' Built as a Signature-authored original for the JAH network; clearly labeled Signature and never presented as a public record.';
  return d;
}
function buildDemo(b){
  return DEMO.split('{title}').join(b[1]).split('{d1}').join(b[6]).split('{d2}').join(b[7]).split('{d3}').join(b[8]);
}
function generate(seed,opts){
  opts=opts||{}; var rnd=prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title=buildTitle(b);
  var fields={}; fields[FLD[0][0]]=b[3]; fields[FLD[1][0]]=b[4]; fields[FLD[2][0]]=b[5];
  if(SIG) fields['signature_label']='Signature-authored original';
  return {id:id,title:title,description:buildDesc(b),category:cat,fields:fields,
    ladder_rank:1+(seed%3),
    demo:'# '+title+' \u2014 runnable demo (python3)\n'+buildDemo(b),
    provenance:'JAH Databases \u00b7 lane N3 build',last_verified:'2026-10-21',src:SRC,_seed:seed};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){
    if(sample[i]&&sample[i].title===rec.title&&sample[i].category===rec.category)
      return {ok:false,errors:['duplicate of archive record '+sample[i].id]};
  }
  return {ok:true,errors:[]};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var idre=new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$');
  if(!idre.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('print(')<0)e.push('demo');
  if(['public-harvest','signature-generated-completion'].indexOf(r.src)<0)e.push('src');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-engineering-material-substitution-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('engineering-material-substitution',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
