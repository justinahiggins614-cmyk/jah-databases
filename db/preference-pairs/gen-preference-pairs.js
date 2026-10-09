(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return s[(r()*s.length)|0];}
function ri(r,a,b){return a+((r()*(b-a+1))|0);}
function pad6(n){return String(n).padStart(6,'0');}

var CATS=['helpfulness','honesty','clarity','completeness','tone'];

var PROMPTS=[
 'Explain {topic} simply.',
 'Write a haiku about {topic}.',
 'Summarize the plot of {topic} in two sentences.',
 'Give me study tips for learning {topic}.',
 'Describe {topic} to someone who has never seen it.'
];
var TOPICS=['photosynthesis','gravity','the water cycle','batteries','the internet','volcanoes','the human heart','recycling'];

var RESP={
 helpfulness:{good:'Here is a complete answer about {topic}: the key idea, why it matters, and one everyday example you can try right away. Tell me which part you want to go deeper on.',
  bad:'Just look it up yourself. There are plenty of websites about {topic} if you actually try searching.'},
 honesty:{good:'I want to be careful here: the core facts about {topic} are well established, but some details are still debated. Here is what is solidly known, and I will flag what is uncertain.',
  bad:'{topic} is fully understood and there is nothing uncertain about it at all. Anyone who disagrees is simply wrong.'},
 clarity:{good:'{topic}, in plain words: it is a simple process with three parts. First, something starts it. Then, it changes. Finally, it settles. Each part is easy to picture on its own.',
  bad:'The {topic} paradigm instantiates a multifaceted ontological framework whose epistemological ramifications necessitate a dialectical hermeneutic to properly apprehend its phenomenological substrate.'},
 completeness:{good:'A full answer about {topic} covers four things: what it is, how it works, a concrete example, and what people commonly get wrong. Here is each one in turn.',
  bad:'{topic} is a thing that exists. That covers the main point.'},
 tone:{good:'Great question about {topic}! I am happy to help with this — here is a friendly walkthrough, and there are no silly questions here.',
  bad:'Ugh, {topic} again? This is obvious stuff. Figure it out.'}
};

function generate(seed,opts,rnd){
  rnd=rnd||prng(seed);
  var crit=(opts&&opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:pick(rnd,CATS);
  var prompt=pick(rnd,PROMPTS).replace('{topic}',pick(rnd,TOPICS));
  var topic=prompt.match(/about (.+?)[.?]|learning (.+?)[.?]|Explain (.+?) simply|of (.+?) in two|never seen (.+?)[.?]/);
  var t=topic?(topic[1]||topic[2]||topic[3]||topic[4]||topic[5]||'it'):'it';
  var good=RESP[crit].good.replace(/\{topic\}/g,t);
  var bad=RESP[crit].bad.replace(/\{topic\}/g,t);
  var a,b,pref;
  if(rnd()<0.5){a=good;b=bad;pref='A';}else{a=bad;b=good;pref='B';}
  var id='JAH-PREF-'+pad6(seed);
  return {id:id,pref_id:id,prompt:prompt,response_a:a,response_b:b,preferred:pref,
    criterion:crit,annotator_count:ri(rnd,3,9),title:prompt.slice(0,80)};
}

function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-PREF-\d{6}$/.test(r.id))e.push('id');
  if(r.pref_id!==r.id)e.push('pref_id');
  if(typeof r.prompt!=='string'||!r.prompt.length||r.prompt.length>600)e.push('prompt');
  if(typeof r.response_a!=='string'||!r.response_a.length||r.response_a.length>600)e.push('response_a');
  if(typeof r.response_b!=='string'||!r.response_b.length||r.response_b.length>600)e.push('response_b');
  if(r.response_a===r.response_b)e.push('responses identical');
  if(r.preferred!=='A'&&r.preferred!=='B')e.push('preferred');
  if(CATS.indexOf(r.criterion)<0)e.push('criterion');
  if(typeof r.annotator_count!=='number'||r.annotator_count<3||r.annotator_count>9||r.annotator_count%1!==0)e.push('annotator_count');
  if(r.title!==String(r.prompt).slice(0,80))e.push('title');
  return {ok:!e.length,errors:e};
}

var gen={version:'jahdb-preference-pairs-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('preference-pairs',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
