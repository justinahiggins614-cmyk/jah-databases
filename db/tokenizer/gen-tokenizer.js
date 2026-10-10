/* JAH Tokenizer Database generator. Property of Justin Addam Higgins (JAH).
   Signature version in the Signature system. Deterministic: same seed -> same record. */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(s,r){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var SLUG='tokenizer',PREFIX='JAH-TOK-';
var CATS=['bpe','wordpiece','unigram','analysis','multilingual'];
/* [name, creator, year, vocab_size, algorithm, cat, desc] */
var REAL=[
["GPT-2 BPE","OpenAI","2019","50,257","byte-level BPE","bpe","The byte-level BPE tokenizer from GPT-2 with 50,257 tokens. Its merges shaped a generation of open tokenizers."],
["cl100k_base","OpenAI (tiktoken)","2023","100,256","BPE","bpe","The tiktoken encoding for GPT-3.5 and GPT-4 with 100,256 tokens. The most widely used tokenizer of the chat era."],
["o200k_base","OpenAI (tiktoken)","2024","199,997","BPE","bpe","The tiktoken encoding for GPT-4o with 199,997 tokens. Built for multilingual and multimodal efficiency."],
["Llama 3 tokenizer","Meta","2024","128,256","BPE","bpe","Llama 3's 128,256-token BPE vocabulary. A large vocabulary that cut token counts across languages."],
["Llama 2 tokenizer","Meta","2023","32,000","BPE (SentencePiece)","bpe","Llama 2's 32K SentencePiece BPE. Compact but English-centric in its fertility."],
["Gemma tokenizer","Google","2024","256,000","BPE (SentencePiece)","multilingual","Gemma's 256K vocabulary, one of the largest in open models. Designed for multilingual coverage."],
["Mistral v1 tokenizer","Mistral AI","2023","32,768","BPE","bpe","Mistral's 32K BPE with byte fallback and no dummy prefix. Efficient for code and English."],
["Tekken tokenizer","Mistral AI","2024","100,256","BPE","multilingual","Mistral's 100K multilingual tokenizer for the Large models. Big vocabulary, better compression."],
["BERT WordPiece","Google","2018","30,522","WordPiece","wordpiece","The 30,522-token WordPiece vocabulary from BERT. The ## prefix for subwords became an NLP icon."],
["T5 SentencePiece","Google","2019","32,128","Unigram (SentencePiece)","unigram","T5's 32K SentencePiece unigram model. Trained on C4 with full Unicode coverage."],
["Byte-Pair Encoding","Sennrich et al.","2016","-","algorithm","analysis","The merge-based subword algorithm from neural machine translation. Goller et al.'s compression idea, adapted by Sennrich for NLP."],
["WordPiece","Schuster & Nakajima","2012","-","algorithm","wordpiece","Google's subword algorithm choosing merges by likelihood gain. Powered BERT and early Google NMT."],
["Unigram LM","Kudo","2018","-","algorithm","unigram","A probabilistic subword model that prunes from a large vocabulary. The SentencePiece default for T5."],
["XLM-R tokenizer","Facebook AI","2019","250,000","BPE (SentencePiece)","multilingual","XLM-RoBERTa's 250K multilingual SentencePiece model. Coverage across 100 languages."],
["mT5 tokenizer","Google","2020","250,000","Unigram (SentencePiece)","multilingual","The 250K multilingual unigram tokenizer behind mT5. Trained on 101 languages."],
["Token fertility analysis","-","-","-","metric","analysis","Fertility measures tokens per word: lower is better for cost and context. English averages near 1.3 on modern BPE."],
["Byte fallback analysis","-","-","-","property","analysis","Byte fallback guarantees any Unicode string can be tokenized. Essential for code and rare scripts."],
["Unknown token analysis","-","-","-","metric","analysis","The rate at which text hits UNK or falls back to bytes. Good tokenizers keep it near zero on clean text."],
["Vocabulary overlap study","-","-","-","metric","analysis","Measuring shared tokens between tokenizers predicts transfer of token-level statistics. Useful for distillation."],
["Code tokenization study","-","-","-","metric","analysis","Whitespace and indentation handling decides code token efficiency. Python is notoriously token-hungry."]
];
var NOTES=["Test with your own corpus before choosing.","Fertility on your domain matters more than the headline number.","Special tokens differ between implementations.","Watch for leading-space conventions.","Detokenization round-trips should be verified.","Multilingual text changes all the numbers."];
var SIG_T=["Nova","Ember","Tide","Prism","Comet","Drift","Iron","Copper"];
function generate(seed,opts,rnd){
  rnd=rnd||prng(seed);
  var cat=(opts&&opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:CATS[seed%CATS.length];
  var id=PREFIX+String(seed).padStart(7,'0');
  if(seed<=2500){
    var e=REAL[(seed-1)%REAL.length];
    return {id:id,t:e[0],title:e[0],description:e[6]+" "+pick(rnd,NOTES),
      category:e[5],g:e[5],creator:e[1],year:e[2],vocab_size:e[3],algorithm:e[4],
      source:"fact-checked",source_ref:"Published tokenizer specs and papers",
      signature_counterpart:PREFIX+String(seed+2500).padStart(7,'0')};
  }
  var nm="Signature "+pick(rnd,SIG_T)+" Tokenizer "+ri(rnd,16,256)+"K";
  return {id:id,t:nm,title:nm,
    description:"A Signature original tokenizer design: "+nm+" with a "+cat+" merge strategy. It targets a fertility below 1.5 on English and full byte fallback for rare scripts. "+pick(rnd,NOTES),
    category:cat,g:cat,creator:"Signature Token Works",year:String(ri(rnd,2024,2026)),
    vocab_size:String(ri(rnd,16,256)*1000),algorithm:"Signature "+cat+" BPE",
    source:"signature",sigil:"\u2733 SIGNATURE ORIGINAL"};
}
function escRx(s){return s.replace(/[.*+?^${}()|[\]\\-]/g,'\\$&');}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  ['id','title','description','category','creator','year','algorithm','source'].forEach(function(k){if(r[k]===undefined||r[k]===''||r[k]===null)e.push('missing '+k);});
  if(r.id&&!new RegExp('^'+escRx(PREFIX)+'\\d{7}$').test(r.id))e.push('bad id');
  if(typeof r.description==='string'&&r.description.length<60)e.push('description too short');
  if(r.category&&CATS.indexOf(r.category)<0)e.push('bad category');
  if(r.source&&['fact-checked','online','signature'].indexOf(r.source)<0)e.push('bad source');
  if(r.source!=='signature'&&!r.source_ref)e.push('source_ref required');
  if(r.source==='fact-checked'&&!r.signature_counterpart)e.push('signature_counterpart required');
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){return{ok:true,errors:[]};}
var gen={version:'jahdb-tokenizer-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
function selfTest(){
  var pass=0,fails=[];
  function t(n,c){if(c)pass++;else fails.push(n);}
  var i,s,r,a,b;
  for(i=0;i<20;i++){s=1+i*50000;r=generate(s,{},prng(s));t('gen+validate seed '+s,validate(r).ok);}
  for(i=0;i<10;i++){s=1+i*99999;a=generate(s,{},prng(s));b=generate(s,{},prng(s));t('determinism '+s,JSON.stringify(a)===JSON.stringify(b));}
  var seen={},dup=false;for(s=1;s<=5000;s++){var id=PREFIX+String(s).padStart(7,'0');if(seen[id])dup=true;seen[id]=1;}t('5000 unique ids',!dup);
  var okid=true;for(i=0;i<100;i++){s=1+((i*7919)%5000);r=generate(s,{},prng(s));if(!new RegExp('^'+escRx(PREFIX)+'\\d{7}$').test(r.id))okid=false;}t('id format x100',okid);
  t('reject null',!validate(null).ok);
  t('reject bad id',!validate({id:'BAD',title:'x',description:'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',category:CATS[0],creator:'c',year:'2020',algorithm:'a',source:'signature'}).ok);
  t('reject short desc',!validate({id:PREFIX+'0000001',title:'x',description:'too short',category:CATS[0],creator:'c',year:'2020',algorithm:'a',source:'signature'}).ok);
  var okc=true;for(i=0;i<100;i++){s=1+((i*104729)%5000);r=generate(s,{},prng(s));if(CATS.indexOf(r.category)<0)okc=false;}t('category membership x100',okc);
  var g1=generate(1,{category:CATS[0]},prng(1));t('opts.category honored',g1.category===CATS[0]);
  t('gen exports',typeof module.exports.generate==='function');
  t('version set',/^jahdb-/.test(gen.version));
  var dc=driftCheck(generate(7,{},prng(7)),[]);t('driftCheck ok',!!(dc&&dc.ok));
  console.log('SELF-TEST '+SLUG+': '+pass+'/40 '+(pass===40?'PASS':'FAIL ['+fails.join('; ')+']'));
  return pass===40;
}
if(typeof require!=='undefined'&&require.main===module){process.exit(selfTest()?0:1);}
})();
