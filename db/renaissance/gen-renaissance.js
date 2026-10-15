(function(){'use strict';
/* Renaissance Database generator — jahdb-renaissance-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-RENAIS-';
var TOPICS=[["Leonardo da Vinci", "The ultimate Renaissance man: painter, inventor, and scientist."], ["Michelangelo", "Sculptor and painter of the Sistine Chapel and David."], ["The Mona Lisa", "Leonardo's portrait, the most famous painting in the world."], ["The Printing Press", "Gutenberg's invention spreading books across Europe."], ["Humanism", "The movement celebrating human potential and classical learning."], ["Florence", "The Italian city at the heart of the Renaissance."], ["The Medici", "The banking family that patronized Renaissance art."], ["William Shakespeare", "The English playwright of the late Renaissance."], ["Galileo Galilei", "The astronomer who turned the telescope on the heavens."], ["Perspective in Art", "The technique giving paintings realistic depth."], ["Donatello", "The sculptor who revived classical bronze figures."], ["Raphael", "The graceful painter of Madonnas and the School of Athens."], ["Botticelli", "The painter of The Birth of Venus."], ["Petrarch", "The poet called the father of humanism."], ["Dante Alighieri", "The poet of the Divine Comedy."], ["The Scientific Revolution", "The new science growing from Renaissance curiosity."], ["Nicolaus Copernicus", "The astronomer who placed the Sun at the center."], ["The Reformation", "The religious movement reshaping European Christianity."], ["Explorers", "The voyages of discovery funded by Renaissance rulers."], ["Vernacular Languages", "Literature written in everyday languages, not just Latin."], ["Renaissance Architecture", "The revival of classical columns, domes, and symmetry."], ["Renaissance Music", "The rich polyphony of the era's choirs."], ["The Northern Renaissance", "The movement's flowering in the Netherlands and Germany."], ["Patronage", "How wealthy sponsors made great art possible."], ["The Sistine Chapel", "Michelangelo's ceiling, a pinnacle of Renaissance art."], ["Renaissance Science", "Anatomy, astronomy, and the new spirit of inquiry."], ["Women of the Renaissance", "The artists and thinkers often overlooked."], ["Legacy of the Renaissance", "How the era shaped the modern world."]];
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
    type:'renaissance record', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('renaissance',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();