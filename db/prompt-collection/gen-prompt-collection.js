(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['chat','coding','writing','analysis','tool-use','image'];
var PREFIX='JAH-PROMPT-';
/* rows: [task_type, role, prompt_text, [tags]] */
var P=[
 ['chat','system','You are a friendly, plain-spoken assistant. Answer in natural sentences, never in templated blocks.',['tone','conversation']],
 ['chat','system','You are a patient tutor. Explain ideas simply, check understanding, and never rush the learner.',['tutoring','patience']],
 ['chat','user','Explain this to me like I am smart but new to the topic, and give one concrete example.',['clarity','example']],
 ['chat','user','Summarize our conversation so far in three short bullet points.',['summary','recall']],
 ['coding','system','You are a senior engineer. Write clean, working code with brief comments on the tricky parts.',['code-quality','senior']],
 ['coding','system','You are a code reviewer. Point out bugs first, then suggest the smallest fix that works.',['review','debugging']],
 ['coding','user','Write a Python function that {goal}. Include a quick test at the bottom.',['python','function']],
 ['coding','user','Refactor this code for readability without changing what it does.',['refactor','readability']],
 ['writing','system','You are a careful editor. Tighten prose, cut filler, and keep the author\u2019s voice intact.',['editing','voice']],
 ['writing','system','You are a storyteller. Open with a vivid scene and end with a line that lingers.',['story','openings']],
 ['writing','user','Draft a 150-word product description that sounds confident but honest.',['copy','product']],
 ['writing','user','Rewrite this paragraph in a warmer tone, keeping every fact the same.',['tone','rewrite']],
 ['analysis','system','You are an analyst. Compare options with numbers first, then give a clear recommendation.',['numbers','recommendation']],
 ['analysis','system','You are a skeptic. Stress-test each claim and flag what the data cannot prove.',['skeptic','evidence']],
 ['analysis','user','List the pros and cons of {topic}, then tell me which side is stronger and why.',['pros-cons','judgment']],
 ['analysis','user','What are the three biggest risks in this plan, and how would you reduce each?',['risk','planning']],
 ['tool-use','system','You are a careful agent. Think first, then call exactly the tools needed, then answer from observations.',['agency','tools']],
 ['tool-use','system','You are a research agent. Search before answering factual questions and cite what you found.',['research','citations']],
 ['tool-use','user','Use the calculator tool to check your arithmetic before giving the final answer.',['verify','math']],
 ['tool-use','user','Look up the definition first, then use it in your explanation.',['lookup','grounding']],
 ['image','system','You are an art director. Describe the scene, lighting, and mood in vivid concrete detail.',['art-direction','detail']],
 ['image','system','You are a photographer. Specify lens, light, and composition like a shot list.',['photography','composition']],
 ['image','user','A cozy cabin interior at dusk, warm lamplight, rain on the windows, painterly style.',['cozy','painterly']],
 ['image','user','Design a minimalist logo: a single continuous line forming a mountain and sun.',['logo','minimal']]
];
var GOALS=['reverses a string','counts word frequencies','finds duplicate files','validates email addresses'];
var TOPICS=['remote work','electric cars','meal planning','learning guitar'];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=P.filter(function(p){return p[0]===cat;});
  var p=pick(pool.length?pool:P,rnd);
  var txt=p[2].split('{goal}').join(pick(GOALS,rnd)).split('{topic}').join(pick(TOPICS,rnd));
  var id=PREFIX+String(seed).padStart(6,'0');
  return {id:id,prompt_id:id,title:txt.slice(0,80),prompt_text:txt,task_type:cat,role:p[1],rating:Math.round((3.5+rnd()*1.5)*10)/10,use_count:ri(rnd,10,5000),tags:p[3].slice(),_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-PROMPT-\d{6}$/.test(r.id||''))e.push('id');
  if(r.prompt_id!==r.id)e.push('prompt_id');
  if(r.title!==r.prompt_text.slice(0,80))e.push('title');
  if(typeof r.prompt_text!=='string'||!r.prompt_text.length||r.prompt_text.length>600)e.push('prompt_text');
  var sents=r.prompt_text.split(/[.!?]+/).filter(function(x){return x.trim().length;});
  if(sents.length<1||sents.length>3)e.push('prompt sentences');
  if(CATS.indexOf(r.task_type)<0)e.push('task_type');
  if(r.role!=='system'&&r.role!=='user')e.push('role');
  if(!(r.rating>=3.5&&r.rating<=5.0))e.push('rating');
  if(!(r.use_count>=0&&(r.use_count|0)===r.use_count))e.push('use_count');
  if(!Array.isArray(r.tags)||r.tags.length<2||r.tags.length>3)e.push('tags');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-prompt-collection-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('prompt-collection',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
