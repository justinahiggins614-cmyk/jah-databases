(function(){'use strict';
/* Signature Spontaneous Human Combustion Database generator — jahdb-spontaneous-human-combustion-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled) */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-SHC-';
var TOPICS=[["The Case of Mary Reeser", "A 1951 Florida woman was found almost entirely cremated in her chair; the FBI investigated and found no accelerant."], ["The Wick Effect Explanation", "Experiments show clothed bodies can burn slowly like candles; the wick effect explains the localized destruction."], ["Dr. John Irving Bentley", "A 1966 Pennsylvania doctor was found burned with only a leg intact; a pipe ember was the suspected ignition."], ["The Ewen Family Tragedies", "Multiple 19th-century cases were collected by early writers; most involved elderly smokers near open flames."], ["Charles Dickens and Krook", "Bleak House featured a spontaneous combustion death; Dickens defended it against scientific critics."], ["The 1744 Case of Countess Bandi", "An Italian noblewoman was found reduced to ash; early accounts blamed 'inflammable vapors' in her body."], ["Alcohol and the Flammability Myth", "Victorian temperance writers claimed drunkards could ignite; chemistry shows the body can't reach that state."], ["The Ball Lightning Theory", "Some propose ball lightning as an ignition source; the theory lacks any supporting case evidence."], ["Static Electricity Hypotheses", "Researchers have tested whether body static could ignite clothing; the energy falls far short."], ["Methane Buildup Claims", "Intestinal gas theories fail basic physics; the quantities and ignition conditions don't work."], ["The 2010 Michael Faherty Case", "An Irish coroner recorded spontaneous combustion as cause of death; the finding was controversial among fire scientists."], ["Smoking Materials: The Common Thread", "Nearly all cases involve cigarettes, pipes, or fireplaces; dropped embers explain the ignition."], ["Why Bodies Burn Oddly", "Human fat renders and burns at relatively low temperatures; forensic tests reproduce the patterns."], ["The Unburned Room Mystery", "Victims' surroundings often survive; the wick effect's low, slow burn explains the limited spread."], ["Photographic Evidence Reviews", "Case photos show consistent patterns; fire investigators recognize ordinary, if rare, fire behavior."], ["The Role of Obesity in Cases", "Higher body fat correlates with more complete burning; the fuel-load physics is straightforward."], ["Coroners and Unusual Verdicts", "A few inquests returned spontaneous combustion verdicts; most were later reconsidered."], ["The 1980s Media Wave", "Tabloids and TV specials popularized SHC; the coverage outpaced the case count."], ["Larry Arnold's 'Ablaze!'", "A 1995 book cataloged cases as paranormal; fire scientists rebutted it case by case."], ["Forensic Fire Science Advances", "Modern fire modeling reproduces SHC scenes; the mystery dissolves under simulation."], ["Spontaneous Combustion in Materials", "Oily rags and hay genuinely self-ignite; the real phenomenon is chemical, not biological."], ["The Human Torch Stunt History", "Performers fake fiery deaths with gels and suits; the tricks inform how witnesses misread real fires."], ["Cultural Fears of Inner Fire", "Religious visions of hellfire shaped early SHC beliefs; the metaphor became literal in popular telling."], ["Insurance Investigations", "Arson investigators treat SHC claims as ordinary fires; fraud occasionally hides behind the legend."], ["The Psychology of Mysterious Death", "Families prefer mystery to mundane accident; grief shapes how cases are remembered."], ["Documented Ignition Sources", "Case reviews find fireplaces, cigarettes, and candles in nearly every instance; 'spontaneous' was the absence of a witness."], ["What Science Concludes", "No case has withstood forensic review as truly spontaneous; the wick effect plus ignition source covers the evidence."], ["Teaching Fire Safety From SHC", "The cases warn about smoking near upholstery; the real lesson is mundane and lifesaving."]];
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
    type:'spontaneous human combustion exploration', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('spontaneous-human-combustion',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();