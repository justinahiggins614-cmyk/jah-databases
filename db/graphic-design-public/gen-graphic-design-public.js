(function(){'use strict';
/* Public Graphic Design Database generator — jahdb-graphic-design-public-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-GRAD-PUB-';
var TOPICS=[["Typography", "Type anatomy, pairing, and hierarchy."], ["Color Theory", "Hue, harmony, and psychological effects."], ["Layout", "Grids, alignment, and visual flow."], ["Composition", "Balance, contrast, and focal points."], ["Logo Design", "Marks that identify and endure."], ["Branding", "Systems beyond the logo."], ["Print Design", "Brochures, posters, and prepress."], ["Web Design", "Designing for screens and interaction."], ["UI Design", "Interfaces users understand."], ["Packaging", "Structure, shelf impact, and unboxing."], ["Illustration", "Drawing for design contexts."], ["Photography for Design", "Shooting images that design around."], ["Design History", "Bauhaus to Swiss to digital."], ["Design Software", "Vector, raster, and layout tools."], ["Portfolios", "Presenting work to get hired."], ["Client Work", "Briefs, revisions, and professionalism."], ["Accessibility", "Design everyone can use."], ["Motion Graphics", "Design in time."], ["Infographics", "Data made visual and honest."], ["Social Media Design", "Formats, templates, and brand voice."], ["Design Critique", "Giving and receiving feedback."], ["Copyright for Designers", "Ownership and fair use basics."], ["Freelancing", "Running a design practice."], ["Design Trends", "Reading trends without chasing them."], ["Design Ethics", "Honest persuasion in visual work."]];
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
    type:'graphic design knowledge record', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('graphic-design-public',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();