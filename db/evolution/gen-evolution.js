(function(){'use strict';
/* Evolution Database generator — jahdb-evolution-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-EVOL-';
var TOPICS=[["Charles Darwin", "The naturalist whose theory of natural selection explained evolution."], ["Natural Selection", "How organisms best adapted to their environment tend to survive and reproduce."], ["On the Origin of Species", "Darwin's book presenting the case for evolution by natural selection."], ["Adaptation", "Traits that help organisms survive in their environment."], ["Fossils", "The preserved remains that document life's history."], ["Common Descent", "The idea that all living things share common ancestors."], ["Mutation", "Random changes in DNA that create new variation."], ["Speciation", "How new species arise from existing ones."], ["Homologous Structures", "Similar body structures revealing shared ancestry."], ["Vestigial Structures", "Leftover features, like the human tailbone, from earlier forms."], ["DNA Evidence", "How genetics confirms the relationships evolution predicts."], ["Darwin's Finches", "The Galapagos birds whose beaks illustrated adaptation."], ["Antibiotic Resistance", "Bacteria evolving to survive medicines, evolution in action."], ["Artificial Selection", "How humans breed plants and animals for desired traits."], ["Survival of the Fittest", "The phrase for nature favoring the best-adapted."], ["The Tree of Life", "The branching diagram of how species are related."], ["Extinction", "When the last members of a species die out."], ["Human Evolution", "The fossil story of how humans arose in Africa."], ["Gregor Mendel", "The monk whose pea experiments founded genetics."], ["The Modern Synthesis", "The merging of Darwin's ideas with genetics."], ["Transitional Fossils", "Fossils showing intermediate forms between groups."], ["Convergent Evolution", "Unrelated species evolving similar solutions independently."], ["Coevolution", "How species shape each other's evolution, like flowers and pollinators."], ["Mass Extinctions", "The great dyings that reshaped life, including the dinosaurs' end."], ["The Cambrian Explosion", "The burst of new animal forms in ancient seas."], ["Sexual Selection", "Evolution driven by competition for mates."], ["Genetic Drift", "Random changes in small populations over generations."], ["Evolutionary Timescales", "The millions of years over which evolution works."], ["From Fins to Limbs: The Tiktaalik Transition", "Tiktaalik, a 375-million-year-old fossil fish, shows the transition from fins to limbs: its fins contain wrist-like bones and a flexible neck."], ["The Eye's Many Inventions", "Eyes evolved independently at least 40 times, from simple light-sensitive patches to camera eyes, proving that complex organs can arise repeatedly."], ["Whales: The Return to the Sea", "Whales evolved from land mammals: fossils like Pakicetus, Ambulocetus, and Basilosaurus document the return to the water over 10 million years."], ["Feathers Before Flight", "Feathers evolved before flight, first as insulation and display in dinosaurs like Sinosauropteryx, only later co-opted for flying."], ["The Mammalian Ear: Jawbones to Hearing", "Mammalian middle-ear bones, the malleus, incus, and stapes, evolved from reptilian jaw joints, a transformation documented in fossils and embryos."], ["Antibiotic Resistance: Evolution in Real Time", "Antibiotic resistance is evolution observable in years: bacteria evolve defenses against our drugs faster than we invent new ones."], ["The Peppered Moth: Industrial Melanism", "The peppered moth famously evolved dark coloration during industrial soot pollution, then reverted as air cleaned up, evolution tracked in real time."], ["Cichlid Radiations: Speciation at Speed", "African cichlid fish radiated into hundreds of species in a few thousand years, the fastest vertebrate speciation known."], ["The Human Brain's Expansion", "The human brain tripled in size over 2 million years, driven by a feedback loop of diet, tool use, and social complexity."], ["Venom's Convergent Evolution", "Venom evolved independently in snakes, spiders, scorpions, jellyfish, and even mammals like the platypus, converging on similar molecular weapons."], ["Flight's Four Inventions", "Powered flight evolved four times: insects, pterosaurs, birds, and bats, each with a radically different wing."], ["The Placenta's Viral Origin", "The mammalian placenta evolved with help from retroviruses: syncytin, essential for placental cell fusion, is a captured viral gene."], ["Cavefish: Evolution in Reverse", "Cavefish lost their eyes in darkness, but the loss is active evolution, not decay: eye development is suppressed to save energy."], ["The Immune System's Arms Race", "The vertebrate immune system evolved through an arms race with pathogens, producing the most diverse genes in the genome."], ["Eusociality: The Superorganism Leap", "Eusociality, with reproductive division of labor, evolved in ants, bees, wasps, termites, and even naked mole rats, creating superorganisms."]];
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
    type:'evolution record', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('evolution',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();