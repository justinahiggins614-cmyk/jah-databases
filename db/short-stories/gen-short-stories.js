(function(){'use strict';
/* Signature Short Stories Database generator — jahdb-short-stories-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled) */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-STORY-';
var TOPICS=[["Adventure Shorts", "Punchy quests in few pages."], ["Mystery Minis", "Whodunits with quick twists."], ["Sci-Fi Shorts", "Future flashes of fiction."], ["Fantasy Flashes", "Magic in miniature."], ["Comedy Shorts", "Laugh-out-loud little tales."], ["Spooky Shorts", "Chills in short form."], ["Animal Tales", "Creature-centered short stories."], ["Robot Tales", "Mechanical-heart stories."], ["Space Tales", "Cosmic short adventures."], ["Ocean Tales", "Seaside short stories."], ["Forest Tales", "Woodland wanderings."], ["Desert Tales", "Dry-land dramas."], ["Mountain Tales", "High-altitude heroics."], ["City Tales", "Street-level short fiction."], ["Village Tales", "Small-town storytelling."], ["Time-Travel Tales", "Short hops through time."], ["Pirate Tales", "Swashbuckling shorts."], ["Knight Tales", "Chivalry in brief."], ["Wizard Tales", "Spell-sized stories."], ["Dragon Tales", "Fire-breathing fiction."], ["Fairy Tales Retold", "Classic tales with new twists."], ["Bedtime Shorts", "Gentle stories for lights-out."], ["Friendship Tales", "Heartwarming buddy stories."], ["Courage Tales", "Brave-heart short fiction."], ["Discovery Tales", "Stories of finding the unknown."],
 ["The Laundromat at 2 A.M.", "The laundromat at 2 a.m. hums like a choir of tired machines, and Mara folds someone else's abandoned shirt because the alternative is thinking."],
 ["Instructions for Watering My Plants", "Water the fern on Tuesdays, the succulent when you remember, and the thing in the blue pot never — it is plastic and I like the mystery."],
 ["The Last Video Store", "The last video store on the street keeps 4,000 tapes nobody rents, and Ellis keeps it open because closing it would be admitting something."],
 ["Eleven Percent", "The weather app says eleven percent chance of rain, and June packs an umbrella anyway, because eleven percent is how her mother died — a small chance, taken ..."],
 ["The Substitute Bus Driver", "The substitute bus driver does not know the route, so the 7:10 becomes an expedition, and the regulars, who have ridden together for 6 years, become tour gui..."],
 ["What the Dog Buried", "The dog buried something in March, and by June Elena's curiosity outweighed her dignity, so she dug: a tennis ball, 3 bottle caps, and a wedding ring that wa..."],
 ["The Museum of Lost Gloves", "The museum of lost gloves has 2,300 single gloves, each tagged with where it was found, and the curator, a former detective, has reunited 41 pairs."],
 ["Static", "The old radio picks up a station that does not exist, playing news from 1974, and Ruth, who is 81, listens every night at 9 because the broadcaster sounds li..."],
 ["The Cartographer's Apology", "The cartographer spent 40 years mapping coastlines and retired having never visited the sea, a fact his daughter finds unforgivable and then, slowly, underst..."],
 ["Second Breakfast", "The inn serves second breakfast at 10, a tradition started when a hiker in 1962 ate two breakfasts and the cook, delighted, made it policy."]];
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
    type:'short stories creation', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('short-stories',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();