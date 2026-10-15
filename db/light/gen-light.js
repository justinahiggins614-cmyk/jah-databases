(function(){'use strict';
/* Light Database generator — jahdb-light-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-LIGHT-';
var TOPICS=[["The Speed of Light", "About 300,000 kilometers per second, the fastest speed known."], ["Reflection", "Light bouncing off surfaces, as in mirrors."], ["Refraction", "Light bending as it passes between materials, as in lenses."], ["Prisms and Rainbows", "How glass and raindrops split light into colors."], ["The Spectrum", "The range of colors from red to violet in visible light."], ["Wavelength", "The distance between light waves, determining color."], ["Photons", "The particles of light."], ["Shadows", "The dark shapes cast when objects block light."], ["Lenses", "Curved glass that focuses or spreads light."], ["Mirrors", "Smooth surfaces reflecting clear images."], ["Cameras", "Devices capturing light to make photographs."], ["Vision", "How eyes and brains turn light into sight."], ["Lasers", "Concentrated beams of single-color light."], ["Fiber Optics", "Glass fibers carrying light signals for communications."], ["Primary Colors", "The basic colors that mix to make others."], ["Transparency", "How materials let light pass through."], ["Solar Energy", "Power captured from sunlight."], ["Photosynthesis", "How plants use light to make food."], ["The Light-Year", "The distance light travels in a year, used for cosmic scales."], ["Ultraviolet Light", "Invisible light beyond violet, causing sunburn."], ["Infrared Light", "Invisible heat radiation beyond red."], ["Polarized Light", "Light waves vibrating in one direction, cut by special lenses."], ["Eclipses", "When the Moon or Earth blocks sunlight."], ["The Aurora", "The shimmering northern and southern lights."], ["Bioluminescence", "Living things making their own light."], ["Candlelight", "The warm glow of burning wax."], ["Neon Signs", "Glowing tubes of electrified gas."], ["Light Pollution", "Excess artificial light hiding the night sky."]];
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
    type:'light record', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('light',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();