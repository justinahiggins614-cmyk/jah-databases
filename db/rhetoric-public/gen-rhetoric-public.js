(function(){'use strict';
/* Public Rhetoric Database generator — jahdb-rhetoric-public-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-RHET-PUB-';
var TOPICS=[["The Rhetorical Triangle", "Ethos, pathos, logos: Aristotle's appeals."], ["Persuasion", "How attitudes change: central and peripheral routes."], ["Public Speaking", "Delivery, structure, and managing nerves."], ["Argumentation", "Building and defending claims."], ["Debate", "Formats, rebuttal, and competitive debate."], ["Classical Rhetoric", "The five canons: invention to delivery."], ["Figures of Speech", "Metaphor, irony, hyperbole, and their effects."], ["Storytelling", "Narrative as persuasion."], ["Visual Rhetoric", "How images persuade."], ["Digital Rhetoric", "Persuasion online: memes, threads, video."], ["Political Rhetoric", "Campaigns, speeches, and spin."], ["Advertising", "The rhetoric of selling."], ["Negotiation", "Persuasive bargaining."], ["Rhetorical Analysis", "Dissecting how a text persuades."], ["The Speech", "Writing speeches that move audiences."], ["Introductions and Conclusions", "Opening and closing with power."], ["Audience Analysis", "Knowing whom you persuade."], ["Credibility", "Building and keeping ethos."], ["Emotional Appeals", "Pathos used honestly."], ["Evidence and Reasoning", "Logos: data, examples, and logic."], ["Style", "Diction, rhythm, and voice."], ["Impromptu Speaking", "Thinking on your feet."], ["Listening", "The persuader's neglected skill."], ["Propaganda", "Manipulation versus persuasion."], ["Civic Discourse", "Arguing well in public life."]];
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
    type:'rhetoric knowledge record', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('rhetoric-public',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();