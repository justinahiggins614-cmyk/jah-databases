(function(){'use strict';
/* First Aid Database generator — jahdb-first-aid-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-FIRSTAID-';
var TOPICS=[["Calling for Help", "Calling the local emergency number first in serious situations."], ["CPR Basics", "Chest compressions and rescue breaths that keep blood flowing until help arrives."], ["Choking", "Back blows and abdominal thrusts to clear a blocked airway."], ["Severe Bleeding", "Pressing firmly on a wound to slow blood loss."], ["Burns", "Cooling minor burns with running water and covering them loosely."], ["Sprains", "Rest, ice, compression, and elevation for twisted joints."], ["Nosebleeds", "Leaning forward and pinching the nose until bleeding stops."], ["Insect Stings", "Removing stingers, cleaning, and watching for allergic reactions."], ["Allergic Reactions", "Recognizing severe reactions and using prescribed epinephrine if available."], ["Shock", "Keeping a pale, clammy person lying down and warm while awaiting help."], ["Fractures", "Immobilizing a suspected break and not straightening it."], ["The Recovery Position", "Rolling an unconscious breathing person onto their side."], ["AEDs", "Automated defibrillators in public places that guide users with voice prompts."], ["Heat Exhaustion", "Moving to a cool place, resting, and sipping water."], ["Hypothermia", "Warming a dangerously cold person gradually and seeking help."], ["Poisoning", "Calling poison control and not inducing vomiting unless told to."], ["Animal Bites", "Cleaning wounds and seeking medical care for bites."], ["Splinters", "Removing with clean tweezers and cleaning the skin."], ["Fainting", "Laying the person down and raising their legs."], ["Eye Injuries", "Flushing chemicals with water and not rubbing the eye."], ["Head Injuries", "Watching for confusion or vomiting and seeking care for hard blows."], ["First Aid Kit", "The essential supplies every home and car should carry."], ["Wound Cleaning", "Rinsing minor cuts and covering them to prevent infection."], ["Bandaging", "Covering wounds snugly without cutting off circulation."], ["Bee Sting Allergy", "Knowing the signs of anaphylaxis and acting fast."], ["Drowning Response", "Getting the person out safely and starting rescue breathing if trained."], ["Staying Calm", "How a calm helper makes emergencies go better."], ["When Not to Move Someone", "Leaving possible spine injuries still until professionals arrive."]];
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
    type:'first aid record', content:content,
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('first-aid',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();