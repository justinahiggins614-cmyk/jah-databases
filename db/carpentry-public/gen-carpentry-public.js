(function(){'use strict';
/* Public Carpentry Database generator — jahdb-carpentry-public-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-CARP-PUB-';
var TOPICS=[["Framing", "Walls, floors, and roofs: structural carpentry."], ["Rough Carpentry", "The structural shell of buildings."], ["Finish Carpentry", "Trim, molding, and fine interior work."], ["Roofing", "Framing roofs and installing coverings."], ["Stairs", "Layout, stringers, and code-compliant stairs."], ["Decks", "Design, footings, and deck construction."], ["Siding", "Exterior cladding materials and installation."], ["Drywall", "Hanging, taping, and finishing."], ["Flooring", "Hardwood, laminate, and tile substrates."], ["Doors", "Hanging, planing, and hardware."], ["Windows", "Installation, flashing, and trim."], ["Cabinetry", "Building and installing cabinets."], ["Concrete Forms", "Formwork for foundations and slabs."], ["Reading Plans", "Blueprints and construction drawings."], ["Measuring and Layout", "The 3-4-5 rule and accurate layout."], ["Fasteners", "Nails, screws, and anchors: choosing right."], ["Power Tools", "Circular saw, nail gun, and miter saw."], ["Ladders and Scaffolds", "Working safely at height."], ["Building Codes", "The rules that keep structures safe."], ["Estimating", "Materials takeoffs and job costing."], ["Remodeling", "Working in existing structures."], ["Insulation", "Types and proper installation."], ["Trim and Molding", "Baseboards, crowns, and casings."], ["Repair", "Fixing rot, squeaks, and damage."], ["Tool Maintenance", "Keeping carpentry tools working."]];
var ANGLES=['overview','detailed','examples','faq','history','applications'];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function generate(seed,opts){
  var s=prng(seed);
  var ti=(s()*TOPICS.length)|0, ai=(s()*ANGLES.length)|0;
  var topic=TOPICS[ti], angle=ANGLES[ai];
  var id=PREFIX+pad(seed);
  var title=topic[0]+' ('+angle+')';
  var desc=topic[1];
  var content=topic[0]+' \u2014 '+topic[1];
  return {
    id:id, title:title, description:desc, genre:angle,
    type:'carpentry knowledge record', content:content, content_completeness:'stub',
    stub_note:'Topic stub: the topic title and its one-line brief are real; the full guide article is not yet written. This record does not present shell text as a complete guide.',
    demo:null, src:'public', _seed:seed
  };
}
function validate(r){
  var errs=[];
  if(!r.id)errs.push('missing id');
  if(!r.title)errs.push('missing title');
  if(!r.content||r.content.length<50)errs.push('content too short');
  return {ok:errs.length===0, errors:errs};
}
function driftCheck(rec,sample){
  // Simple: check for exact title duplicates in sample
  for(var i=0;i<sample.length;i++){if(sample[i].t===rec.title)return {ok:false,errors:['duplicate title']};}
  return {ok:true,errors:[]};
}
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('carpentry-public',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();