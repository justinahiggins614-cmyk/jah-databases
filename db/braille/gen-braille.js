(function(){'use strict';
/* Braille Database generator — jahdb-braille-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-BRAILLE-';
var TOPICS=[["Braille Alphabet", "The 26 letters of the alphabet represented in raised-dot Braille cells."], ["Braille Numbers", "How digits are written using the number sign followed by letters a-j."], ["Braille Punctuation", "Common punctuation marks and their dot patterns."], ["Grade 1 vs Grade 2 Braille", "Uncontracted Grade 1 versus contracted Grade 2 Braille systems."], ["Common Braille Contractions", "Frequently used contractions that speed up Braille reading."], ["Reading Braille by Touch", "Techniques for tactile reading with the fingertips."], ["Writing with Slate and Stylus", "The traditional manual tools for writing Braille."], ["Refreshable Braille Displays", "Electronic devices that render digital text as Braille."], ["Louis Braille", "The inventor of the Braille system, 1809-1852."], ["History of Tactile Writing", "From raised print to the six-dot cell: the evolution of touch reading."], ["Braille Music Notation", "How music is represented in Braille for blind musicians."], ["Nemeth Code for Math", "The Braille system for mathematics and science notation."], ["Braille in Education", "How Braille literacy is taught in schools."], ["Braille Signage and Accessibility", "Tactile signs in public buildings and where they are required."], ["Unified English Braille", "UEB: the standard Braille code for English adopted internationally."], ["Learning Braille as an Adult", "Approaches for adults newly learning Braille."], ["Braille Embossers", "Printers that produce Braille on paper."], ["Braille Literacy and Opportunity", "The connection between Braille literacy and employment outcomes."], ["Computer Braille Code", "Braille representations used in computing contexts."], ["Braille for Children", "Introducing Braille to young learners through play and stories."], ["Proofreading Braille", "Methods for checking Braille documents for errors."], ["Braille Cell Anatomy", "The six-dot cell: dot numbering and layout."], ["Dot Patterns a through j", "The first ten letters and the patterns that build the rest."], ["Capitalization in Braille", "How capital letters are indicated with the capital sign."], ["Foreign Language Braille", "Braille codes for languages beyond English."], ["Braille and Screen Readers", "How Braille displays pair with screen reader software."], ["Public Braille Resources", "Libraries and services providing Braille materials."], ["Italics and Emphasis", "How emphasis is marked in Braille text."]];
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
    type:'braille record', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('braille',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();