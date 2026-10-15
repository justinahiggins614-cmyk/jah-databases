(function(){'use strict';
/* Flags Database generator — jahdb-flags-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-FLAG-';
var TOPICS=[["Stars and Stripes", "The flag of the United States, with thirteen stripes and fifty stars."], ["The Union Jack", "The flag of the United Kingdom combining the crosses of its nations."], ["The French Tricolor", "The blue, white, and red vertical stripes of France."], ["The Maple Leaf", "The red-and-white flag of Canada with its central maple leaf."], ["The Rising Sun", "The white flag with a red disc of Japan."], ["Flag Colors", "How red, white, blue, green, and other colors carry meaning on flags."], ["Stripes on Flags", "What horizontal and vertical stripes commonly represent."], ["Stars on Flags", "How stars stand for states, ideals, or history."], ["Crosses on Flags", "The Nordic crosses and other cross designs on national flags."], ["Flag Etiquette", "The respectful customs for displaying and handling flags."], ["Raising and Lowering", "The ceremonies of hoisting a flag at dawn and lowering it at dusk."], ["Half-Mast", "Flying a flag lowered to honor the dead."], ["The UN Flag", "The light-blue flag with the world map emblem of the United Nations."], ["The Olympic Flag", "The five interlocking rings representing the world's continents."], ["Maritime Signal Flags", "The alphabet flags ships use to communicate at sea."], ["Semaphore Flags", "Hand-held flags spelling letters by position."], ["Vexillology", "The study of flags and their history."], ["The Oldest Flags", "National flags with centuries of continuous use."], ["Flag Design", "The principles of simple, memorable flag design."], ["Provincial Flags", "The flags of states, provinces, and regions."], ["City Flags", "Municipal flags and their symbols."], ["Military Flags", "Regimental colors and battle flags."], ["Pirate Flags", "The Jolly Roger and other historic pirate banners."], ["Peace Flags", "Banners and symbols of peace movements."], ["Flags of Revolution", "The banners raised in revolutions around the world."], ["Retired Flags", "Old national flags preserved in museums."], ["Flag Day", "Holidays honoring national flags."], ["Folding a Flag", "The ceremonial triangle fold of the American flag."]];
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
    type:'flags record', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('flags',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();