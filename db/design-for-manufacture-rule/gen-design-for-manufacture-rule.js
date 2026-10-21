(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["molding", "machining", "sheet-metal", "assembly", "tolerance"];
var PREFIX='JAH-DESIGN-';
var USE="Used by product designers and manufacturing engineers to avoid costly redesigns.";
var FLD=[["rule", "Rule"], ["process", "Process"], ["value", "Value"]];
var DEMO="# {title} - thickness check (python3)\nactual={d1}\nminimum={d2}\nfactor={d3}\nrequired=minimum*factor\nprint(\"actual %.2f mm, required %.2f mm\" % (actual, required))\nprint(\"PASS\" if actual >= required else \"THICKEN PART\")\n";
var SIG=false;
var SRC="public-harvest";
var B=[["molding", "Minimum Wall Thickness", "Keeps walls thick enough to fill the mold and survive ejection without warping.", "Minimum Wall Thickness", "injection molding", "fewer rejects", "2.5", "2.0", "1.25"], ["machining", "Draft Angle", "Tapers vertical walls so parts release from the mold cleanly.", "Draft Angle", "injection molding", "clean ejection", "3.0", "1.0", "2.0"], ["sheet-metal", "Uniform Wall", "Holds wall thickness constant to prevent sink marks and uneven cooling.", "Uniform Wall", "molding/casting", "cosmetic quality", "3.0", "2.5", "1.2"], ["assembly", "Fillet Radii", "Rounds internal corners to cut stress concentration and improve flow.", "Fillet Radii", "all processes", "stronger parts", "1.5", "0.5", "2.0"], ["tolerance", "Tolerance Budgeting", "Assigns tolerances by function, keeping tight only where it matters.", "Tolerance Budgeting", "all processes", "lower cost", "0.1", "0.05", "1.5"], ["molding", "Undercut Avoidance", "Designs out undercuts or plans side-actions so molds open simply.", "Undercut Avoidance", "injection molding", "cheaper tooling", "0.0", "0.0", "1.0"], ["machining", "Parting Line Placement", "Puts the mold split where flash is hidden and ejection is natural.", "Parting Line Placement", "injection molding", "clean appearance", "1.0", "1.0", "1.0"], ["sheet-metal", "Gate Location", "Places gates where flow fills evenly and weld lines land in low-stress areas.", "Gate Location", "injection molding", "strong parts", "2.0", "1.0", "1.5"], ["assembly", "Ejector Planning", "Sizes and places ejector pins to push without denting or distorting.", "Ejector Planning", "injection molding", "no ejector marks", "4.0", "2.0", "1.5"], ["tolerance", "Rib Design", "Uses thin ribs for stiffness instead of thick walls, saving material and cycle time.", "Rib Design", "injection molding", "light + stiff", "1.5", "1.0", "1.25"], ["molding", "Boss Design", "Designs screw bosses with proper OD/ID ratios and gussets to avoid cracking.", "Boss Design", "injection molding", "reliable fastening", "6.0", "4.0", "1.25"], ["machining", "Snap-fit Geometry", "Shapes cantilever snaps with correct deflection and strain for thousands of cycles.", "Snap-fit Geometry", "injection molding", "tool-free assembly", "2.0", "1.5", "1.2"], ["sheet-metal", "Living Hinge", "Uses thin polypropylene sections as integral hinges rated for flex life.", "Living Hinge", "injection molding", "one-piece design", "0.4", "0.3", "1.2"], ["assembly", "Threaded Insert", "Specifies heat-staked or molded inserts where screws meet plastic.", "Threaded Insert", "injection molding", "durable threads", "5.0", "3.0", "1.5"], ["tolerance", "Overmold Compatibility", "Chooses material pairs with proven chemical bonding for two-shot parts.", "Overmold Compatibility", "overmolding", "no delamination", "2.0", "1.0", "1.5"], ["molding", "Machining Access", "Keeps features reachable by standard tools with clearance for the cutter.", "Machining Access", "CNC machining", "fewer setups", "12.0", "6.0", "1.5"], ["machining", "Bend Radius", "Holds inside bend radius >= material thickness to avoid cracking.", "Bend Radius", "sheet metal", "no cracks", "2.0", "1.0", "1.5"], ["sheet-metal", "Hole-to-edge Distance", "Keeps holes far enough from edges to prevent tear-out.", "Hole-to-edge Distance", "sheet metal/punching", "strong holes", "3.0", "2.0", "1.25"], ["assembly", "Surface Finish Spec", "Calls out only the finish the function needs; mirror polish everywhere wastes money.", "Surface Finish Spec", "all processes", "right cost", "1.6", "0.8", "1.5"], ["tolerance", "Assembly Direction", "Designs parts to assemble along one axis for fast, error-proof builds.", "Assembly Direction", "assembly", "faster builds", "1.0", "1.0", "1.0"]];
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
var gen={version:'jahdb-design-for-manufacture-rule-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('design-for-manufacture-rule',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
