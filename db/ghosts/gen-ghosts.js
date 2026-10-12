(function(){'use strict';
/* Signature Ghosts Database generator — jahdb-ghosts-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled) */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-GHOST-';
var TOPICS=[["The Science of Haunted Places", "Infrasound, mold, and suggestion explain many hauntings; investigators find mundane causes more often than not."], ["The Tower of London's Spirits", "Anne Boleyn's reported ghost walks the battlements; the stories are part of the Tower's 900-year narrative."], ["Gettysburg's Phantom Soldiers", "Visitors report apparitions on the battlefield; the emotional weight of the place primes perception."], ["The Brown Lady of Raynham Hall", "A famous 1936 photograph shows a descending figure; analysts debate double exposure versus apparition."], ["The Amityville Horror Case", "The Lutzes' 1975 claims became a franchise; the defense lawyer later said it was a hoax over drinks."], ["The Enfield Poltergeist", "Peggy Hodgson's children reported phenomena in 1977; investigators split between belief and evidence of trickery."], ["Borley Rectory Investigations", "Harry Price's 'most haunted house' burned in 1939; later researchers found fraud and natural causes."], ["The Bell Witch of Tennessee", "An 1817\u20131821 haunting allegedly killed John Bell; the tale grew through 19th-century retellings."], ["The Winchester Mystery House", "Sarah Winchester's maze-like mansion invites ghost stories; historians find the s\u00e9ances were later inventions."], ["Eastern State Penitentiary", "The abandoned prison leans into its hauntings; paranormal tourism funds preservation."], ["The Stanley Hotel", "Stephen King's inspiration markets its ghosts; staff stories sustain the legend."], ["The Queen Mary", "The retired liner's staterooms host ghost tours; maritime history blends with haunting claims."], ["Poveglia Island", "The Venetian quarantine island is called the world's most haunted; its real history of plague and asylums is grim enough."], ["The Catacombs' Whispers", "Paris tunnel explorers report voices; acoustics and darkness do the rest."], ["Aokigahara's Reputation", "The Japanese forest's suicide association spawned ghost lore; locals and officials discourage the sensationalism."], ["Crisis Apparitions", "The dying reportedly appear to loved ones at a distance; these are the most widely reported and least explained cases."], ["After-Death Communication", "Many grieving people sense the deceased; psychologists view it as a normal part of mourning."], ["Electronic Voice Phenomena", "Investigators claim spirit voices on recordings; audio science points to pareidolia and interference."], ["Spirit Photography History", "Victorian double exposures faked ghosts; the fraud techniques are well documented."], ["Ouija Boards and Ideomotor Action", "Planchettes move by unconscious muscle motion; blindfold tests prove users steer them."], ["S\u00e9ance Tricks Exposed", "Houdini and others revealed table-tipping and ectoplasm frauds; the exposures ended an era."], ["Poltergeist Psychology", "Cases center on stressed adolescents; some are pranks, others remain puzzling but natural."], ["The Philip Experiment", "Researchers invented a ghost and 'contacted' it; the result demonstrated expectation's power."], ["Infrasound and Dread", "Low-frequency sound induces unease and visual disturbances; some 'haunted' labs were simply humming."], ["Carbon Monoxide Hauntings", "A famous case traced hauntings to a faulty furnace; the poisoning explained visions and paranoia."], ["Sleep Paralysis Entities", "The 'old hag' visitation matches paralysis hallucinations; neurology explains the intruder."], ["Why Ghost Belief Persists", "Grief, agency detection, and storytelling sustain belief; the experiences feel real because they are experienced."], ["Ghost Hunting Technology", "EMF meters and thermal cameras look scientific; skeptics note they measure everything except ghosts."]];
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
    type:'ghosts exploration', content:content,
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('ghosts',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();