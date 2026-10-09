(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['math','dictionary','web-search','site-routing','code','general'];
var PREFIX='JAH-TRAJ-';
var TOOLS={
 'math':[{name:'calculate',description:'Evaluate a numeric expression.',args:['expression']},{name:'define_word',description:'Look up a word definition.',args:['word']}],
 'dictionary':[{name:'define_word',description:'Look up a word definition.',args:['word']},{name:'word_history',description:'Show etymology notes for a word.',args:['word']}],
 'web-search':[{name:'web_search',description:'Search the web for a query.',args:['query']},{name:'fetch_page',description:'Fetch a page as plain text.',args:['url']}],
 'site-routing':[{name:'route_site',description:'Route a topic to the best matching site.',args:['topic']},{name:'site_info',description:'Describe a site by name.',args:['site']}],
 'code':[{name:'run_code',description:'Run code and return stdout.',args:['language','code']},{name:'lint_code',description:'Check code for style issues.',args:['code']}],
 'general':[{name:'web_search',description:'Search the web for a query.',args:['query']},{name:'calculate',description:'Evaluate a numeric expression.',args:['expression']}]
};
var WORDS=[['serendipity','the occurrence of happy discoveries by chance','Latin serendip, old name for Sri Lanka'],['ephemeral','lasting a very short time','Greek ephemeros, lasting a day'],['ubiquitous','present everywhere at once','Latin ubique, everywhere'],['pragmatic','dealing with problems practically','Greek pragmatikos, businesslike'],['resilient','able to recover quickly','Latin resilire, to leap back'],['melancholy','a deep, thoughtful sadness','Greek melankholia, black bile'],['synthesize','combine parts into a whole','Greek synthetikos, putting together'],['quintessential','the perfect example of a type','Latin quinta essentia, fifth essence']];
var TOPICS=['renewable energy trends','Mars rover missions','electric vehicle range','open-source AI models','quantum computing breakthroughs','urban farming methods'];
var SITES=[['BakeWell Hub','A community site for baking recipes and tips.'],['FitTrack Daily','Workout plans and fitness tracking guides.'],['CodeStart Academy','Beginner programming lessons and exercises.'],['GardenPatch','Urban gardening advice for small spaces.'],['ChessLab','Chess openings, puzzles, and strategy.'],['TrailMap Pro','Hiking routes and trail conditions.']];
var GOALS=[['Python','reverse a string','s[::-1]','olleh'],['Python','sum a list of numbers','sum(nums)','42'],['JavaScript','filter even numbers from an array','arr.filter(x=>x%2===0)','[2,4,6]'],['JavaScript','sort an array of numbers','arr.sort((a,b)=>a-b)','[1,2,3]'],['SQL','list the top 5 customers by spend','SELECT ... LIMIT 5','5 rows']];
var ITEMS=[['noise-cancelling headphones',249,199],['a standing desk',399,329],['an e-reader',139,99],['a portable SSD 1TB',129,89],['a mechanical keyboard',159,119]];

function asst(thought,tool,args){return {role:'assistant',thought:thought,tool_name:tool,arguments:args};}
function toolObs(obs){return {role:'tool',observation:obs};}

function build(rnd,cat){
  var steps=[],task,final;
  if(cat==='math'){
    var a=ri(rnd,2,99),b=ri(rnd,2,99),c=ri(rnd,2,50),kind=ri(rnd,0,2),ans;
    if(kind===0){task='Compute '+a+' x '+b+' + '+c+'.';ans=a*b+c;
      steps.push(asst('Multiply first, then add.','calculate',{expression:a+'*'+b+'+'+c}));steps.push(toolObs(String(ans)));
      final='The result is '+ans+'.';
    }else if(kind===0||kind===1){var p=pick([10,20,25,40,50],rnd),n=ri(rnd,5,50)*4;ans=p*n/100;
      task='What is '+p+'% of '+n+'?';
      steps.push(asst('Compute the percentage directly.','calculate',{expression:p+'*'+n+'/100'}));steps.push(toolObs(String(ans)));
      final=p+'% of '+n+' is '+ans+'.';
    }else{ans=a*b-c;task='A shelf holds '+a+' books per row with '+b+' rows; '+c+' are removed. How many remain?';
      steps.push(asst('First the total, then subtract.','calculate',{expression:a+'*'+b}));steps.push(toolObs(String(a*b)));
      steps.push(asst('Now subtract the removed books.','calculate',{expression:(a*b)+'-'+c}));steps.push(toolObs(String(ans)));
      final=ans+' books remain.';
    }
  }else if(cat==='dictionary'){
    var w=pick(WORDS,rnd);task='Define "'+w[0]+'" and note its origin.';
    steps.push(asst('Look up the definition.','define_word',{word:w[0]}));steps.push(toolObs(w[1]));
    steps.push(asst('Check its origin notes.','word_history',{word:w[0]}));steps.push(toolObs(w[2]));
    final='"'+w[0]+'" means '+w[1]+'.';
  }else if(cat==='web-search'){
    var t=pick(TOPICS,rnd);task='Summarize the latest news on '+t+'.';
    steps.push(asst('Search for recent coverage.','web_search',{query:t+' latest news'}));steps.push(toolObs('6 recent articles found.'));
    steps.push(asst('Read the top article.','fetch_page',{url:'https://example.news/'+t.replace(/ /g,'-')}));steps.push(toolObs('Top article: steady progress reported across the field.'));
    final='Recent coverage of '+t+' shows steady progress across the field.';
  }else if(cat==='site-routing'){
    var s=pick(SITES,rnd);task='Which site is best for learning about "'+s[1].split(' ')[0].toLowerCase()+' topics" and what does it offer?';
    steps.push(asst('Route the topic to a site.','route_site',{topic:task}));steps.push(toolObs(s[0]));
    steps.push(asst('Get details on that site.','site_info',{site:s[0]}));steps.push(toolObs(s[1]));
    final=s[0]+' is the best match: '+s[1];
  }else if(cat==='code'){
    var g=pick(GOALS,rnd);task='In '+g[0]+', '+g[1]+'.';
    steps.push(asst('Run a candidate snippet.','run_code',{language:g[0],code:g[2]}));steps.push(toolObs(g[3]));
    steps.push(asst('Lint it for style issues.','lint_code',{code:g[2]}));steps.push(toolObs('No issues found.'));
    final='Working '+g[0]+' snippet verified; output: '+g[3]+'.';
  }else{
    var it=pick(ITEMS,rnd);task='Should I buy '+it[0]+' at $'+it[2]+' (was $'+it[1]+')? Research and decide.';
    steps.push(asst('Research the product first.','web_search',{query:it[0]+' review'}));steps.push(toolObs('Reviews are positive; 4.5 stars average.'));
    steps.push(asst('Compute the discount.','calculate',{expression:it[1]+'-'+it[2]}));steps.push(toolObs('Save $'+(it[1]-it[2])+ '.'));
    final='Yes - reviews are strong and you save $'+(it[1]-it[2])+' off the list price.';
  }
  return {task:task,steps:steps,final:final};
}

function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var b=build(rnd,cat);
  var success=rnd()<0.92;
  if(!success){
    b.steps[b.steps.length-1]=toolObs('Error: tool timed out.');
    b.final='The task could not be completed because a tool call failed.';
  }
  var id=PREFIX+String(seed).padStart(6,'0');
  return {id:id,trajectory_id:id,title:b.task,task_text:b.task,domain:cat,tool_schema:{tools:TOOLS[cat]},steps:b.steps,success:success,final_answer:b.final,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-TRAJ-\d{6}$/.test(r.id||''))e.push('id');
  if(r.trajectory_id!==r.id)e.push('trajectory_id');
  if(typeof r.task_text!=='string'||!r.task_text.length)e.push('task_text');
  if(r.title!==r.task_text)e.push('title');
  if(CATS.indexOf(r.domain)<0)e.push('domain');
  var ts=r.tool_schema;
  if(!ts||!Array.isArray(ts.tools)||ts.tools.length<2||ts.tools.length>4)e.push('tool_schema');
  else ts.tools.forEach(function(t){if(!t.name||!t.description||!Array.isArray(t.args))e.push('tool');});
  if(!Array.isArray(r.steps)||r.steps.length<2||r.steps.length>5)e.push('steps');
  else r.steps.forEach(function(s){
    if(s.role==='assistant'){if(!s.thought||!s.tool_name||typeof s.arguments!=='object')e.push('step');}
    else if(s.role==='tool'){if(typeof s.observation!=='string')e.push('step');}
    else e.push('step');
  });
  if(typeof r.success!=='boolean')e.push('success');
  if(typeof r.final_answer!=='string'||!r.final_answer.length)e.push('final_answer');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-tool-trajectories-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tool-trajectories',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
