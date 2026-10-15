(function(){'use strict';
/* Signature RPG Games Database generator — jahdb-rpg-games-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled) */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-RPG-';
var TOPICS=[["Dungeons & Dragons", "1974's revolution; the editions."], ["The d20 System", "The mechanic; the OGL."], ["Call of Cthulhu", "The horror; the sanity."], ["Pathfinder", "The fork; the 2e."], ["The OSR Movement", "The old school; the revival."], ["Powered by the Apocalypse", "The moves; the design."], ["Blades in the Dark", "The heist; the clocks."], ["The Indie Scene", "The itch.io; the innovation."], ["JRPGs", "Final Fantasy; the tradition."], ["Western RPGs", "Baldur's Gate; the choice."], ["The Souls Formula", "The difficulty; the lore."], ["CRPG Revival", "Divinity to Baldur's 3; the renaissance."], ["Character Creation", "The builds; the fantasy."], ["The GM's Art", "The prep; the improv."], ["Worldbuilding", "The settings; the craft."], ["The Actual Play Boom", "Critical Role; the effect."], ["Solo RPGs", "The journaling; the oracles."], ["The Safety Tools", "The X-card; the consent."], ["LARP", "The live; the community."], ["The Dice", "The math; the superstition."], ["Digital Tabletops", "Roll20; the VTT."], ["The OGL Crisis", "2023's fight; the ORC."], ["Inclusivity", "The representation; the progress."], ["The Business", "The Hasbro; the market."], ["The 2025 Scene", "The state; the hits."], ["Designing Your RPG", "The hack; the advice."], ["The Future", "The AI GM; the prediction."], ["Why We Roleplay", "The psychology; the joy."]];
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
    type:'rpg games exploration', content:content, content_completeness:'stub',
    stub_note:'Topic stub: the topic title and its one-line brief are real; the full guide article is not yet written. This record does not present shell text as a complete guide.',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('rpg-games',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();