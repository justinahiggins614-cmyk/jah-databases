(function(){'use strict';
/* Middle Ages Database generator — jahdb-middle-ages-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-MEDIEVAL-';
var TOPICS=[["Knights", "The armored mounted warriors of medieval Europe."], ["Castles", "The fortified homes of lords, built for defense."], ["Feudalism", "The system of land and loyalty binding lords and vassals."], ["Manors", "The estates where peasants worked the lord's land."], ["The Crusades", "The religious wars fought over the Holy Land."], ["The Black Death", "The fourteenth-century plague that devastated Europe."], ["The Vikings", "The Norse seafarers who raided and settled across Europe."], ["Charlemagne", "The Frankish king crowned emperor, uniting much of Western Europe."], ["Monasteries", "The religious houses preserving learning through the centuries."], ["Gothic Cathedrals", "The soaring churches with pointed arches and stained glass."], ["Guilds", "The associations of craftsmen regulating trades."], ["Jousting", "The mounted tournaments of knights."], ["Heraldry", "The coats of arms identifying knights and families."], ["Troubadours", "The poet-musicians singing of love and chivalry."], ["The Magna Carta", "The 1215 English charter limiting the king's power."], ["The Hundred Years' War", "The long conflict between England and France."], ["Joan of Arc", "The young French heroine of the Hundred Years' War."], ["Marco Polo", "The traveler whose tales of Asia reached medieval Europe."], ["The Hanseatic League", "The trading alliance of northern European cities."], ["Medieval Medicine", "The blend of ancient texts, herbs, and superstition."], ["Illuminated Manuscripts", "The hand-decorated books of the Middle Ages."], ["The University", "The first universities founded in medieval Europe."], ["Pilgrimages", "The religious journeys to holy sites."], ["The Blacksmith", "The essential village craftsman of iron."], ["Medieval Food", "Bread, pottage, and ale on the medieval table."], ["The Plague Doctors", "The masked physicians of plague times."], ["The Late Middle Ages", "The crises and changes ending the medieval era."], ["Medieval Legacy", "What the Middle Ages left to the modern world."]];
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
    type:'middle ages record', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('middle-ages',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();