(function(){'use strict';
/* Signature Paranormal Database generator — jahdb-paranormal-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled) */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-PARA-';
var TOPICS=[["Investigating Haunted Locations", "Paranormal teams use EMF meters, thermal cameras, and audio recorders; critics note the tools detect natural phenomena more reliably than ghosts."], ["Electronic Voice Phenomena (EVP)", "Investigators claim voices appear on recordings inaudible in person; audio experts attribute most EVPs to pareidolia and radio interference."], ["The Amityville Case", "The Lutz family fled their Long Island home in 1975 citing horrors; later legal testimony suggested the story was embellished for profit."], ["The Enfield Poltergeist", "A 1977 London case featured moving furniture and alleged voices; investigators were divided, and some evidence suggested trickery by the children."], ["The Bell Witch Haunting", "Tennessee folklore tells of a spirit that tormented the Bell family in 1817\u20131821; historians trace the tale through 19th-century embellishments."], ["Borley Rectory: The Most Haunted House", "A British rectory's reported phenomena drew Harry Price's investigations; later researchers found natural explanations and possible fraud."], ["The Winchester Mystery House Legends", "Guides tell of s\u00e9ances directing endless construction; historians find the ghost story was largely invented by later promoters."], ["Gettysburg's Battlefield Apparitions", "Visitors report soldiers and phantom gunfire on the battlefield; psychologists link the reports to suggestion in a place of known tragedy."], ["The Tower of London's Ghosts", "Guards and visitors claim sightings of Anne Boleyn and others; the stories form part of the Tower's centuries-old tour tradition."], ["Eastern State Penitentiary", "The abandoned Philadelphia prison markets its hauntings; paranormal tourism now funds much of its preservation."], ["Ouija Boards: Ideomotor Effect", "Planchettes move by tiny unconscious muscle movements, psychologists explain; the effect works even when users are blindfolded."], ["S\u00e9ance History", "Victorian s\u00e9ances combined grief, showmanship, and early photography tricks; magicians like Houdini exposed the era's famous mediums."], ["Physical Mediumship Exposed", "Ectoplasm was revealed as cheesecloth and gauze in controlled tests; the exposures ended the golden age of materialization s\u00e9ances."], ["Near-Death Experiences", "Patients report tunnels and light during resuscitation; neuroscientists link the features to oxygen loss and REM intrusion."], ["Past-Life Regression Claims", "Hypnotized subjects 'recall' former lives; researchers find the memories track the subject's own knowledge and the hypnotist's cues."], ["Psychic Detectives: The Record", "Police departments have tested self-described psychics; controlled reviews find their hit rates match chance."], ["Remote Viewing Programs", "The CIA's Stargate program tested psychic spying for decades; declassified reviews concluded it produced no actionable intelligence."], ["The Ganzfeld Experiments", "Parapsychologists report small above-chance effects in telepathy tests; critics cite methodological flaws and failed replications."], ["Poltergeist Case Patterns", "Cases cluster around adolescents under stress; psychologists propose the phenomena reflect family tension, with some cases exposed as pranks."], ["Crisis Apparitions", "People report seeing loved ones at the moment of their death; researchers collect these as the most common and emotionally compelling ghost reports."], ["Phantom Armies and Sky Battles", "Crowds have reported spectral battles from Edgehill to Gettysburg; atmospheric optics and mass suggestion are proposed explanations."], ["Haunted Objects and Attachments", "Dolls like Robert and Annabelle draw believers; curators note the stories grow with each retelling."], ["The Philip Experiment", "1970s researchers 'created' a ghost through collective imagination; the table movements demonstrated ideomotor action, not spirits."], ["Skeptical Investigation Methods", "Groups like the James Randi Educational Foundation offered prizes for proof; no claimant ever passed controlled testing."], ["Dowsing and Divining Rods", "Rods cross over hidden water, users insist; double-blind tests show results at chance, explained by ideomotor movement."], ["Astrology's Barnum Effect", "Vague horoscopes feel personally accurate; psychologists named the effect after P.T. Barnum's 'something for everyone' patter."], ["Palmistry and Cold Reading", "Readers deliver accurate-sounding readings from visual cues; the techniques are teachable and require no psychic ability."], ["Why Belief Persists", "Cognitive scientists point to agency detection, pattern-seeking, and comfort; belief in the paranormal correlates with creativity and openness."]];
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
    type:'paranormal exploration', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('paranormal',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();