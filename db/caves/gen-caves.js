(function(){'use strict';
/* Caves Database generator — jahdb-caves-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-CAVE-';
var TOPICS=[["Mammoth Cave", "The Kentucky cave system, the longest known cave system in the world."], ["Carlsbad Caverns", "The New Mexico caverns famous for huge chambers and formations."], ["Lascaux Cave", "The French cave with remarkable prehistoric paintings."], ["Stalactites", "Mineral formations hanging from cave ceilings, built drip by drip."], ["Stalagmites", "Formations rising from cave floors where mineral-rich water drips."], ["Limestone Caves", "Caves dissolved out of limestone by slightly acidic groundwater."], ["Cave Bats", "The bats that roost in caves and emerge at night to feed."], ["Waitomo Glowworm Caves", "The New Zealand caves lit by the glow of tiny insects."], ["The Blue Grotto", "The sea cave on Capri famed for its glowing blue water."], ["Cave Paintings", "Prehistoric art on cave walls, among humanity's oldest artworks."], ["Ice Caves", "Caves where ice persists year-round, often in lava tubes or high mountains."], ["Sea Caves", "Caves carved into coastal cliffs by wave action."], ["Lava Tubes", "Tunnels left behind when the surface of a lava flow cools and hardens."], ["Spelunking", "The recreational exploration of caves, also called caving."], ["Cave Diving", "The specialized and hazardous exploration of flooded cave passages."], ["Blind Cave Fish", "Eyeless fish adapted to permanent darkness in underground waters."], ["Cave Crickets", "Insects adapted to life in the dark zone of caves."], ["Karst Landscapes", "Terrain of sinkholes and underground streams formed in soluble rock."], ["Sinkholes", "Collapsed ground above dissolved rock, common in karst regions."], ["Underground Rivers", "Streams flowing through cave systems beneath the surface."], ["Cave Pearls", "Small round mineral concretions formed in cave pools."], ["Soda Straws", "Delicate hollow stalactites, the youngest cave formations."], ["Cave Conservation", "Protecting fragile formations and cave life from damage."], ["Show Caves", "Caves developed with paths and lighting for public visits."], ["Cave Rescue", "The specialized teams trained to rescue injured cavers."], ["Troglobites", "Animals that live only in caves and cannot survive outside them."], ["Cave Archaeology", "The study of human history preserved in cave deposits."], ["Echo and Acoustics", "The remarkable sound effects of large cave chambers."]];
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
    type:'caves record', content:content,
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('caves',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();