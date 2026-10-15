(function(){'use strict';
/* Dictionaries Database generator — jahdb-dictionaries-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-DICT-REF-';
var TOPICS=[["Alphabetical Order", "The A-to-Z arrangement that makes words easy to find."], ["Headword", "The main word entry at the start of a dictionary definition."], ["Pronunciation", "The guide showing how a word is spoken, often in phonetic symbols."], ["Part of Speech", "Labels like noun, verb, and adjective showing how a word is used."], ["Definitions", "The explanations of what a word means, listed by sense."], ["Etymology", "The history of a word's origin and development."], ["Usage Examples", "Sample sentences showing a word in context."], ["Synonyms", "Words with similar meanings, often listed in a thesaurus."], ["Antonyms", "Words with opposite meanings."], ["Thesaurus", "The reference book of synonyms and related words."], ["Bilingual Dictionaries", "Dictionaries translating between two languages."], ["Unabridged Dictionaries", "The largest, most complete dictionary editions."], ["Abridged Dictionaries", "Shorter editions with the most common words."], ["Samuel Johnson", "The eighteenth-century author of the landmark Dictionary of the English Language."], ["Oxford English Dictionary", "The great historical dictionary tracing English words through the centuries."], ["Merriam-Webster", "The long-running American dictionary publisher."], ["Phonetic Transcription", "Writing pronunciation with the International Phonetic Alphabet."], ["Slang Dictionaries", "References collecting informal and street language."], ["Specialized Dictionaries", "Dictionaries for fields like medicine, law, or music."], ["Spelling", "How dictionaries record the accepted spellings of words."], ["Word Frequency", "How often words are used, guiding which words dictionaries include."], ["New Words", "How dictionaries decide when a new word has earned an entry."], ["Usage Notes", "Guidance on tricky or disputed points of word use."], ["Idioms in Dictionaries", "How fixed phrases get their own entries."], ["Rhyming Dictionaries", "References organized by sound for poets and lyricists."], ["Children's Dictionaries", "Simplified dictionaries written for young readers."], ["Electronic Dictionaries", "Dictionary apps and websites with search and audio."], ["Dictionary Abbreviations", "The short labels like n., v., and adj. used in entries."]];
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
    type:'dictionaries record', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('dictionaries',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();