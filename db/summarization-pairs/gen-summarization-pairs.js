/* JAH Summarization Database generator. Property of Justin Addam Higgins (JAH). */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(s,r){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['bullets','paragraph','tldr'];
var T=[
['Photosynthesis in green plants',
['Photosynthesis is the process by which green plants convert light energy into chemical energy.','Chlorophyll, the pigment that makes leaves green, captures photons from sunlight.','Water absorbed by the roots travels up the stem to the leaves.','Carbon dioxide enters the leaf through tiny pores called stomata.','Inside chloroplasts, light energy splits water molecules and releases oxygen.','The plant combines carbon dioxide and water to form glucose, a simple sugar.','Glucose serves as food for the plant and as building material for growth.','Oxygen, a byproduct of the reaction, is released into the atmosphere.','Almost all life on Earth depends directly or indirectly on photosynthesis.','Farmers select crop varieties partly for their photosynthetic efficiency.','Scientists study photosynthesis to design better solar panels.','Rising carbon dioxide levels can speed up photosynthesis in some plants.','Deforestation removes photosynthesizing trees and disrupts the carbon cycle.','Understanding the process helps engineers build artificial leaves.'],
[1,4,5,8]],
['The water cycle',
['The water cycle describes how water moves between oceans, air, and land.','Heat from the sun evaporates water from seas, lakes, and rivers.','Plants also release water vapor through a process called transpiration.','Rising vapor cools and condenses into tiny droplets that form clouds.','When droplets grow heavy enough, they fall as rain or snow.','Precipitation feeds rivers, fills lakes, and soaks into groundwater.','Groundwater slowly migrates back toward the oceans.','Some water is locked for centuries in glaciers and ice caps.','Human activity alters the cycle through dams, irrigation, and deforestation.','Climate change intensifies both droughts and floods in many regions.','Cities manage stormwater to reduce flooding and pollution.','Desalination plants convert seawater into drinking water in dry regions.','Watershed protection keeps drinking water clean at the source.','Every drop of water on Earth has cycled through this system for billions of years.'],
[0,3,5,13]],
['How vaccines work',
['Vaccines train the immune system to recognize dangerous pathogens.','Most vaccines contain a weakened or inactivated form of a germ.','Others use only a fragment of the pathogen, such as a protein.','Newer mRNA vaccines instruct cells to build a harmless viral protein.','The immune system responds by producing antibodies against the target.','Memory cells remain long after vaccination, ready to react quickly.','If the real pathogen arrives, the body defeats it before illness takes hold.','Herd immunity protects people who cannot be vaccinated.','Vaccines undergo years of clinical trials before approval.','Regulators monitor safety continuously after vaccines reach the public.','Smallpox was eradicated worldwide through vaccination campaigns.','Polio has been nearly eliminated by sustained immunization.','Side effects are usually mild, such as a sore arm or brief fever.','The benefits of approved vaccines far outweigh their risks for the public.'],
[0,4,5,10]],
['The rise of the internet',
['The internet began as ARPANET, a U.S. research network from the late 1960s.','Packet switching let messages travel in pieces across many routes.','TCP/IP became the standard language of the network in 1983.','The Domain Name System made addresses human-readable.','Tim Berners-Lee invented the World Wide Web in 1989.','The first web browsers made the network accessible to everyone.','Commercial ISPs opened the internet to the public in the 1990s.','Email became the first killer application of the network.','Search engines organized the exploding volume of web pages.','Social networks connected billions of people in the 2000s.','Smartphones put the internet in nearly every pocket.','Cloud computing moved storage and software into data centers.','Today the internet carries commerce, education, and entertainment.','Its design as an open network shaped modern digital life.'],
[0,4,5,13]],
['Black holes',
['A black hole is a region where gravity is so strong that nothing escapes.','They form when massive stars collapse at the end of their lives.','The boundary of no return is called the event horizon.','Inside, all matter is crushed toward a singularity.','Stellar black holes weigh a few to dozens of times the Sun.','Supermassive black holes sit at the centers of galaxies.','Our galaxy\'s central black hole is called Sagittarius A*.','Stephen Hawking showed black holes slowly radiate energy.','In 2019 astronomers imaged a black hole\'s shadow for the first time.','Merging black holes produce gravitational waves.','Detectors like LIGO have recorded dozens of mergers.','Nearby gas spiraling in heats up and glows brightly.','Studying black holes tests the limits of physics.','They remain among the most extreme objects in the universe.'],
[0,1,8,13]],
['The printing press',
['Johannes Gutenberg\'s printing press appeared in Europe around 1440.','Movable metal type let pages be composed and reused quickly.','A single press could produce thousands of pages per day.','Before printing, books were copied by hand at great cost.','Printed Bibles were among the earliest mass-produced books.','Cheaper books spread literacy across Europe.','Pamphlets carried new ideas during the Reformation.','Newspapers emerged as regular printed publications.','Scientific journals let researchers share results widely.','Standardized texts stabilized spelling and languages.','The press is often called the most important invention of the millennium.','It laid the groundwork for mass media and public education.','Later steam and rotary presses industrialized printing further.','Digital publishing is the press\'s modern descendant.'],
[0,1,5,10]],
['Machine learning basics',
['Machine learning lets computers learn patterns from data.','Instead of hand-written rules, models adjust internal parameters.','Training data shows the model many correct examples.','A loss function measures how wrong the model\'s predictions are.','Optimization algorithms reduce the loss step by step.','Supervised learning uses labeled examples for training.','Unsupervised learning finds structure in unlabeled data.','Reinforcement learning rewards agents for good decisions.','Neural networks stack layers of simple computing units.','Deep learning uses many layers to capture complex patterns.','Overfitting happens when a model memorizes training noise.','Validation data checks that the model generalizes.','Machine learning powers translation, vision, and recommendation.','Careful evaluation keeps models honest and useful.'],
[0,1,8,12]],
['Coral reefs',
['Coral reefs are built by tiny animals called coral polyps.','Polyps secrete limestone skeletons that accumulate over centuries.','Reefs thrive in warm, shallow, sunlit tropical waters.','Algae living inside corals provide food through photosynthesis.','Reefs support about a quarter of all marine species.','They protect coastlines by absorbing wave energy.','Millions of people depend on reefs for food and income.','Rising ocean temperatures cause coral bleaching.','Bleached corals expel their algae and may starve.','Ocean acidification weakens coral skeletons.','Pollution and overfishing add further stress.','Marine protected areas give reefs a chance to recover.','Restoration projects grow corals in nurseries for replanting.','Reefs are among the ecosystems most threatened by climate change.'],
[0,4,7,13]],
['Ancient Rome',
['Rome grew from a small settlement into a vast empire.','Roman law shaped legal systems across the world.','Engineers built roads, aqueducts, and concrete structures.','The Colosseum hosted public spectacles for tens of thousands.','Latin evolved into the Romance languages of today.','The republic gave way to emperors after Julius Caesar.','Augustus established two centuries of relative peace.','Roman citizenship spread rights across conquered lands.','Trade networks linked Britain to Egypt and beyond.','The empire split into western and eastern halves.','The western empire fell in 476 CE.','The eastern Byzantine Empire lasted another thousand years.','Roman ruins still dot three continents.','Its institutions echo through modern government and law.'],
[0,1,5,13]],
['Quantum computing',
['Quantum computers use qubits instead of classical bits.','Qubits exploit superposition to hold many states at once.','Entanglement links qubits in powerful correlations.','Quantum gates manipulate these states to run algorithms.','Some problems run exponentially faster on quantum hardware.','Shor\'s algorithm could break today\'s public-key encryption.','Grover\'s algorithm speeds up unstructured search.','Qubits are fragile and lose coherence quickly.','Error correction requires many physical qubits per logical qubit.','Superconducting circuits and trapped ions are leading designs.','Tech companies now offer quantum cloud access.','Hybrid algorithms mix quantum and classical steps.','Useful large-scale machines are still years away.','The field blends physics, math, and computer science.'],
[0,1,7,12]],
['The human brain',
['The human brain contains about 86 billion neurons.','Neurons communicate through electrical and chemical signals.','Synapses, the connections between neurons, number in the trillions.','The cortex handles thought, language, and perception.','The cerebellum coordinates movement and balance.','The hippocampus is key to forming memories.','Sleep consolidates memories and clears waste.','Neuroplasticity lets the brain rewire with experience.','Learning physically strengthens useful connections.','Emotions involve networks including the amygdala.','The brain uses about 20 percent of the body\'s energy.','Injuries can sometimes be routed around through rehab.','Brain imaging reveals activity in living subjects.','Understanding the brain guides treatments for disease.'],
[0,1,6,13]],
['Renewable energy',
['Renewable energy comes from sources that naturally replenish.','Solar panels convert sunlight directly into electricity.','Wind turbines capture the kinetic energy of moving air.','Hydropower uses flowing water to spin generators.','Geothermal plants tap heat from inside the Earth.','Costs of solar and wind have fallen dramatically.','Batteries store renewable power for calm, dark hours.','Grids must balance variable supply with demand.','Renewables cut the emissions driving climate change.','Jobs in clean energy are growing worldwide.','Policies and subsidies accelerated the transition.','Some regions already run mostly on renewables.','Transmission lines carry power from windy and sunny places.','The shift to renewables is reshaping the energy economy.'],
[0,1,8,13]]
];
function shuffle(r,a){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}
function generate(seed,opts,rnd){
  opts=opts||{};
  rnd=rnd||prng(seed);
  var style=opts.category||pick(rnd,CATS);
  var t=pick(rnd,T);
  var title=t[0], sents=t[1], keys=t[2].map(function(i){return sents[i];});
  var order=shuffle(rnd,sents.map(function(_,i){return i;})).sort(function(a,b){return a-b;});
  var src='',k=0;
  while(k<order.length&&(src.length<300||k<4)){src+=(src?' ':'')+sents[order[k]];k++;}
  if(src.length>560)src=src.slice(0,557).trim()+'…';
  var summary;
  if(style==='bullets'){
    summary=keys.slice(0,3).map(function(s){return '• '+s.slice(0,90).trim();}).join('\n');
  }else if(style==='paragraph'){
    summary=keys[0]+' '+keys[1];
    if(summary.length>400)summary=summary.slice(0,397).trim()+'…';
  }else{
    summary='TL;DR: '+keys[0];
    if(summary.length>160)summary=summary.slice(0,157).trim()+'…';
  }
  var ratio=Math.round(summary.length/src.length*1000)/1000;
  var faith=Math.round((0.8+rnd()*0.2)*100)/100;
  return {
    id:'JAH-SUM-'+String(seed).padStart(6,'0'),
    doc_id:'JAH-SUM-'+String(seed).padStart(6,'0'),
    source_text:src,
    summary:summary,
    compression_ratio:ratio,
    style:style,
    faithfulness_score:faith,
    title:src.slice(0,80)
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  ['id','doc_id','source_text','summary','compression_ratio','style','faithfulness_score','title'].forEach(function(k){if(r[k]===undefined||r[k]===''||r[k]===null)e.push('missing '+k);});
  if(r.id&&!/^JAH-SUM-\d{6}$/.test(r.id))e.push('bad id');
  if(r.doc_id&&r.doc_id!==r.id)e.push('doc_id != id');
  if(r.source_text&&(r.source_text.length<300||r.source_text.length>600))e.push('source_text length '+r.source_text.length);
  if(r.summary&&r.summary.length>=r.source_text.length)e.push('summary not shorter');
  if(typeof r.compression_ratio!=='number'||r.compression_ratio<=0||r.compression_ratio>=1)e.push('bad ratio');
  if(r.style&&CATS.indexOf(r.style)<0)e.push('bad style');
  if(typeof r.faithfulness_score!=='number'||r.faithfulness_score<0.8||r.faithfulness_score>1.0)e.push('bad faithfulness');
  return{ok:!e.length,errors:e};
}
var gen={version:'jahdb-summarization-pairs-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('summarization-pairs',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
