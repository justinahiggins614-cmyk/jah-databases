(function(){'use strict';
/* Signature Optical Illusions Database generator — jahdb-optical-illusions-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled) */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-OPTIC-';
var TOPICS=[["Impossible Objects", "Penrose triangles and staircases."], ["Motion Illusions", "Static images that seem to move."], ["Color Illusions", "Shades that fool the eye."], ["Afterimages", "Stare, look away, see ghosts."], ["Ambiguous Images", "Duck-rabbit and vase-faces."], ["Size Illusions", "Same-size shapes that look different."], ["Hidden Images", "Find the concealed picture."], ["Stereograms", "Magic-eye 3D pictures."], ["Anamorphic Art", "Stretched art that resolves."], ["Trompe-l'oeil", "Fool-the-eye paintings."], ["Moir\u00e9 Magic", "Overlapping-pattern shimmer."], ["Blind Spot Demo", "Find your own blind spot."], ["Peripheral Drift", "Rotating-snakes style motion."], ["Lilac Chaser", "The vanishing-dots illusion."], ["Grid Illusions", "Hermann and Ebbinghaus grids."], ["Caf\u00e9 Wall", "Wavy-lines tile trick."], ["M\u00fcller-Lyer Arrows", "Arrow-length deception."], ["Ponzo Illusion", "Railroad-track size trick."], ["Necker Cube", "The flipping wireframe."], ["Spinning Dancer", "Which way is she turning."], ["Hybrid Images", "Near-far double pictures."], ["Chalk 3D Street Art", "Sidewalk depth illusions."], ["Shadow Illusions", "Light-and-dark trickery."], ["Typography Illusions", "Words that hide images."], ["DIY Illusion Crafts", "Make your own eye tricks."]];
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
    type:'optical illusions creation', content:content,
    demo:null, src:'signature', _seed:seed
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('optical-illusions',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();