(function(){'use strict';
/* Inventors Database generator — jahdb-inventors-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-INVENT-';
var TOPICS=[["Thomas Edison", "The prolific American inventor associated with the light bulb and phonograph."], ["Alexander Graham Bell", "The inventor of the telephone."], ["The Wright Brothers", "Orville and Wilbur Wright, pioneers of powered flight."], ["Nikola Tesla", "The electrical genius behind alternating current systems."], ["Marie Curie", "The pioneering researcher of radioactivity."], ["Benjamin Franklin", "The statesman-scientist of electricity experiments and practical inventions."], ["Leonardo da Vinci", "The Renaissance genius whose notebooks sketched flying machines and more."], ["Johannes Gutenberg", "The inventor of movable-type printing in Europe."], ["Eli Whitney", "The inventor of the cotton gin."], ["Samuel Morse", "The developer of the telegraph and Morse code."], ["George Washington Carver", "The agricultural scientist of peanut and crop innovations."], ["Henry Ford", "The automaker who brought the assembly line to car-making."], ["Tim Berners-Lee", "The inventor of the World Wide Web."], ["Grace Hopper", "The computer pioneer of compilers and programming languages."], ["Ada Lovelace", "The nineteenth-century writer of the first computer algorithm."], ["Louis Pasteur", "The scientist of pasteurization and germ theory."], ["Alexander Fleming", "The discoverer of penicillin."], ["James Watt", "The improver of the steam engine."], ["Karl Benz", "The builder of the first practical automobile."], ["The Lumiere Brothers", "The French pioneers of motion pictures."], ["Philo Farnsworth", "The inventor of electronic television."], ["Hedy Lamarr", "The actress and inventor of frequency-hopping technology."], ["Garrett Morgan", "The inventor of the traffic signal and safety hood."], ["Madam C. J. Walker", "The entrepreneur and inventor of hair-care products."], ["Patents", "The legal protection granted to inventors."], ["The Inventive Process", "From idea to prototype to finished product."], ["Women Inventors", "The often-overlooked women behind major inventions."], ["Invention vs. Discovery", "Creating something new versus finding what exists."]];
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
    type:'inventors record', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('inventors',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();