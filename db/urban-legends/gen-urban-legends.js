(function(){'use strict';
/* Signature Urban Legends Database generator — jahdb-urban-legends-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled) */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-URBAN-LEG-';
var TOPICS=[["The Vanishing Hitchhiker", "Drivers report picking up a young woman who disappears from the back seat; folklorists have cataloged hundreds of variants across continents since the early 1900s."], ["Bloody Mary and Mirror Rituals", "Children dare each other to chant a name before a mirror; scholars trace the ritual through centuries of mirror-divination folklore."], ["Alligators in the Sewers", "New York legend claims pet alligators flushed down toilets colonized the sewers; sanitation workers and biologists find the claim unsupported, yet it persists in pop culture."], ["The Killer in the Backseat", "A driver is warned at a gas station that someone hides in their back seat; the legend encodes real anxiety about car safety and stranger danger."], ["The Hookman of Lovers' Lane", "A scraping hook on a car door handle terrifies parked teenagers; folklorists read it as a cautionary tale about teenage risk-taking."], ["Poisoned Halloween Candy", "Fears of tampered treats circulate every October; documented cases of stranger-poisoned Halloween candy are vanishingly rare, with most incidents involving family members."], ["The Organ-Theft Business Trip", "Travelers wake in ice-filled bathtubs missing a kidney; law-enforcement agencies report no verified cases of this exact scenario."], ["Rats in the Fried Chicken", "A diner bites into a battered rat; the legend attaches to whichever chain is currently unpopular and has never been substantiated."], ["The Licked Hand", "A girl home alone feels her dog lick her hand, then finds a warning note; the story's structure mirrors classic gothic short fiction."], ["The Kidney Heist Email Forward", "Chain emails warning of organ theft circulated for decades; fact-checkers debunked the specifics while noting real organ-trafficking crime exists in very different forms."], ["Crocodiles and the Choking Doberman", "A dog chokes on human fingers, leading owners to a burglar in the closet; the tale recycles through breeds and cities."], ["The Ghostly Grey Lady of the Dorm", "College campuses each claim a haunted founder's wife; the legends serve as unofficial orientation rituals for freshmen."], ["The Elevator Game Ritual", "Internet folklore describes a ritual for visiting another dimension via elevators; it exemplifies how creepypasta builds participatory legend cycles."], ["Polybius: The Cursed Arcade Cabinet", "Players claim a 1981 arcade game caused nightmares and government agents collected the machines; no cabinet has ever been found, making it gaming's favorite legend."], ["The Momo Challenge Hoax", "Viral warnings claimed a creepy sculpture figure was instructing children to self-harm; investigations found no verified cases, only panic amplification."], ["The Slender Man Stabbing Case", "A fictional horror character created online inspired a real 2014 attack; the case is studied as a warning about blurry lines between fiction and belief."], ["Buried Alive in the Morgue", "Victims wake inside coffins or morgue drawers; historical cases of premature burial were real enough that 19th-century coffins included bells and air tubes."], ["The Babysitter and the Man Upstairs", "Calls from inside the house terrorize a sitter; the legend traces to real 1970s murder cases and became a horror-movie template."], ["The Clown Statue", "A sitter mistakes an intruder for a statue; the tale spikes whenever creepy-clown sightings make the news."], ["Green Ribbon Girl", "A girl wears a ribbon around her neck her whole life; the revelation ending is a staple of children's scary-story collections."], ["The Russian Sleep Experiment", "Creepypasta claims Soviet scientists kept subjects awake until they transformed; no such experiment is documented, and the photos are Halloween props."], ["The Hum and Mystery Noises", "Residents report a persistent low hum; investigators have traced some cases to industrial equipment, leaving others unexplained but mundane-adjacent."], ["Phantom Social Workers", "Parents fear strangers stealing children at malls; criminologists note stranger abductions are rare compared to the legend's scale."], ["The Cursed Videotape Chain", "Watching a tape dooms the viewer unless they copy it; the legend dramatizes pre-internet media anxiety and inspired a film franchise."], ["Airplane Mode Baby Myth", "Travelers claim a crying baby was really a smuggled animal; the legend reflects suspicion of fellow passengers in cramped cabins."], ["Legend Tripping and Local Haunts", "Teenagers visit supposedly haunted bridges and tunnels; folklorists study these pilgrimages as living legend performance."], ["How Legends Mutate Online", "Email forwards became forum threads became TikToks; digital folklore mutates faster, but the core cautionary structures remain centuries old."], ["FOAF: The Friend-of-a-Friend Source", "Legends always happened to a friend of a friend; folklorist Jan Harold Brunvand coined the term to explain unverifiable transmission chains."]];
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
    type:'urban legends exploration', content:content,
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('urban-legends',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();