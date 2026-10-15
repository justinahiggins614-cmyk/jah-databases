(function(){'use strict';
/* Scientists Database generator — jahdb-scientists-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-SCIENT-';
var TOPICS=[["Marie Curie", "The pioneering physicist and chemist of radioactivity."], ["Albert Einstein", "The physicist who reshaped ideas of space, time, and energy."], ["Isaac Newton", "The founder of classical mechanics and universal gravitation."], ["Charles Darwin", "The naturalist of evolution by natural selection."], ["Galileo Galilei", "The astronomer who observed the heavens through the telescope."], ["Louis Pasteur", "The founder of germ theory and pasteurization."], ["Alexander Fleming", "The discoverer of penicillin."], ["Nikola Tesla", "The electrical inventor of alternating current systems."], ["Ada Lovelace", "The writer of the first computer algorithm."], ["Grace Hopper", "The computer pioneer of programming languages."], ["Jane Goodall", "The primatologist who transformed understanding of chimpanzees."], ["Stephen Hawking", "The cosmologist of black holes and the universe's origins."], ["Rosalind Franklin", "Whose X-ray images revealed DNA's structure."], ["Gregor Mendel", "The monk who founded genetics with pea plants."], ["Dmitri Mendeleev", "The creator of the periodic table."], ["Alan Turing", "The father of computer science and codebreaking."], ["Katherine Johnson", "The NASA mathematician of orbital calculations."], ["George Washington Carver", "The agricultural scientist of crop innovation."], ["Rachel Carson", "The marine biologist who launched environmental awareness."], ["Carl Sagan", "The astronomer who brought the cosmos to the public."], ["Neil deGrasse Tyson", "The astrophysicist and science communicator."], ["Hypatia", "The Alexandrian mathematician and philosopher."], ["Ibn al-Haytham", "The pioneer of optics and the scientific method."], ["Barbara McClintock", "The geneticist of jumping genes."], ["Tu Youyou", "The discoverer of the antimalarial artemisinin."], ["The Scientific Method", "Observation, hypothesis, experiment, and conclusion."], ["Peer Review", "How scientists check each other's work."], ["Women in Science", "The overlooked contributors now being recognized."]];
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
    type:'scientists record', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('scientists',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();