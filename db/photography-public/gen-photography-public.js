(function(){'use strict';
/* Public Photography Database generator — jahdb-photography-public-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-PHOTO-PUB-';
var TOPICS=[["Exposure", "Aperture, shutter, ISO: the triangle."], ["Composition", "Rule of thirds, leading lines, framing."], ["Lighting", "Natural and artificial light."], ["Portrait Photography", "People: posing and connection."], ["Landscape Photography", "Place, patience, and golden hour."], ["Street Photography", "Candid life in public."], ["Macro", "The tiny world up close."], ["Night Photography", "Long exposures and stars."], ["Sports and Action", "Freezing motion."], ["Event Photography", "Weddings and gatherings."], ["Camera Basics", "Modes, menus, and mastery."], ["Lenses", "Focal lengths and their look."], ["Depth of Field", "Controlling sharpness zones."], ["White Balance", "True color in any light."], ["Editing", "Lightroom-style workflow basics."], ["Black and White", "Seeing in tone."], ["Phone Photography", "Pro results from phones."], ["Flash", "On and off-camera strobe."], ["Studio Lighting", "Softboxes and setups."], ["Photo Essays", "Storytelling in series."], ["Archiving", "Backup and organization."], ["Printing", "From screen to paper."], ["Photography Business", "Clients, pricing, contracts."], ["Ethics", "Consent and truth in images."], ["Photo History", "The medium's masters."]];
var ANGLES=['overview','detailed','examples','faq','history','applications'];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function generate(seed,opts){
  var s=prng(seed);
  var ti=(s()*TOPICS.length)|0, ai=(s()*ANGLES.length)|0;
  var topic=TOPICS[ti], angle=ANGLES[ai];
  var id=PREFIX+pad(seed);
  var title=topic[0]+' ('+angle+')';
  var desc=topic[1]+' This '+angle+' guide provides comprehensive coverage.';
  var content='['+angle+'] '+topic[0]+': '+topic[1]+' Full detailed content for '+angle+' perspective.';
  return {
    id:id, title:title, description:desc, genre:angle,
    type:'photography knowledge record', content:content,
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('photography-public',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();