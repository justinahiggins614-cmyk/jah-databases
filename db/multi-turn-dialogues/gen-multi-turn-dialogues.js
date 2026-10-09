(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['tech-support','tutoring','planning','troubleshooting','chit-chat','research'];
var PREFIX='JAH-DLG-';
var EXCH={
 'tech-support':[
  ['My {dev} will not turn on. What should I check first?','Check the power cable and outlet first, then look for any indicator lights.'],
  ['The cable looks fine but there are no lights at all.','Try a different outlet and hold the power button for 10 seconds.'],
  ['Still nothing. Could the {part} be dead?','It is possible - the {part} is a common failure point on this model.'],
  ['How do I test the {part} myself?','Unplug it, reseat the connectors, and listen for any beep codes on boot.'],
  ['I hear two short beeps now. What does that mean?','Two beeps means the {part} is detected - try booting with one stick of memory.']
 ],
 'tutoring':[
  ['I do not understand {topic}. Can you explain it simply?','Sure. Think of {topic} as a way to {analogy}.'],
  ['So it is like {analogy2}?','Exactly - and the key rule is {rule}.'],
  ['Can you give me a practice example?','Try this: {example}. Work it out and tell me your answer.'],
  ['I got {ans}. Is that right?','{fb} Walk me through your steps so we can check.'],
  ['I think I see my mistake now.','That is the exact insight that makes {topic} click. Nice work.']
 ],
 'planning':[
  ['I want to plan a {trip} for next month. Where do I start?','Start with your dates and budget - those two shape every other choice.'],
  ['I have {n} days and about ${b}. What is realistic?','That covers {dest} comfortably if you book lodging early.'],
  ['What should I book first?','Transport and lodging - they fill up fastest and set your schedule.'],
  ['Any tips to save money?','Travel midweek, eat where locals eat, and book refundable rates.'],
  ['Can you sketch a rough itinerary?','Day 1: arrive and explore; day 2: the main sights; day 3: a slow morning, then depart.']
 ],
 'troubleshooting':[
  ['My {app} keeps crashing on startup. Help?','Let us start simple: restart the device and try again.'],
  ['It still crashes right away.','Clear the app cache and check for an update in the store.'],
  ['Updated and cleared, but no change.','Reinstall the app - your account data syncs back on sign-in.'],
  ['Reinstall worked. Why did that happen?','Usually a corrupted cache file from an interrupted update.'],
  ['How do I prevent it next time?','Keep auto-updates on and avoid force-closing during an update.']
 ],
 'chit-chat':[
  ['How has your day been?','Busy but good - lots of interesting questions like yours. How about you?'],
  ['Pretty quiet. Got any {hobby} tips?','For {hobby}, start small: 20 minutes a day beats one long weekend session.'],
  ['What got you into {hobby}?','I just like how it rewards patience - progress sneaks up on you.'],
  ['Fair enough. Any book recommendations?','Try one classic and one new release in the same month - great contrast.'],
  ['Thanks, I will check those out.','Enjoy - and tell me what you thought of them later.']
 ],
 'research':[
  ['I need quick facts on {subject} for a school project.','{subject} in brief: {fact1} And it matters because {fact2}.'],
  ['Do you have a source I can cite?','Look for encyclopedia entries and museum pages - both are citable.'],
  ['What is the most debated point about {subject}?','Whether {debate} - scholars split roughly down the middle.'],
  ['Can you summarize it in two sentences?','{sum1} {sum2}'],
  ['Perfect, that is all I needed.','Good luck with the project - cite your sources and you will do great.']
 ]
};
var SLOT={
 'tech-support':{dev:['laptop','desktop','tablet'],part:['battery','power adapter','RAM']},
 'tutoring':{topic:['fractions','long division','photosynthesis'],analogy:['cutting a pizza into equal slices','sharing cookies fairly'],analogy2:['splitting a bill at dinner'],rule:['keep denominators equal before adding'],example:['1/2 + 1/4 = ?'],ans:['3/4'],fb:['Close - recheck the second step.']},
 'planning':{trip:['weekend getaway','road trip','city break'],n:['3','4','5'],b:['800','1200','600'],dest:['the coast','the mountains','a nearby city']},
 'troubleshooting':{app:['email app','photo editor','music player']},
 'chit-chat':{hobby:['guitar','gardening','running']},
 'research':{subject:['the Roman aqueducts','honeybee colonies','the printing press'],fact1:['they moved water for miles using gravity alone.'],fact2:['they shaped how cities grew.'],debate:['the system was overbuilt or perfectly sized'],sum1:['Gravity-fed channels carried water across vast distances.'],sum2:['That engineering still inspires water projects today.']}
};
function fill(s,slots,rnd){
  return s.replace(/\{(\w+)\}/g,function(m,k){
    var bank=slots[k];if(!bank)return m;
    return Array.isArray(bank)?pick(bank,rnd):bank;
  });
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var ex=EXCH[cat],slots=SLOT[cat];
  var n=ri(rnd,2,Math.min(4,ex.length));
  var start=ri(rnd,0,ex.length-n);
  var turns=[];
  for(var i=0;i<n;i++){
    turns.push({speaker:'user',text:fill(ex[start+i][0],slots,rnd)});
    turns.push({speaker:'assistant',text:fill(ex[start+i][1],slots,rnd)});
  }
  var id=PREFIX+String(seed).padStart(6,'0');
  var rt=pick(['resolved','resolved','resolved','clarified','escalated'],rnd);
  return {id:id,dialogue_id:id,title:cat+' — '+turns.length+' turns',topic:cat,turns:turns,turn_count:turns.length,resolution_type:rt,satisfaction:Math.round((0.6+rnd()*0.4)*100)/100,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-DLG-\d{6}$/.test(r.id||''))e.push('id');
  if(r.dialogue_id!==r.id)e.push('dialogue_id');
  if(r.title!==r.topic+' — '+r.turn_count+' turns')e.push('title');
  if(CATS.indexOf(r.topic)<0)e.push('topic');
  if(!Array.isArray(r.turns)||r.turns.length<4||r.turns.length>8)e.push('turns');
  else r.turns.forEach(function(t,i){
    var want=i%2===0?'user':'assistant';
    if(!t||t.speaker!==want||typeof t.text!=='string'||!t.text.length)e.push('turn');
  });
  if(r.turn_count!==r.turns.length)e.push('turn_count');
  if(['resolved','clarified','escalated'].indexOf(r.resolution_type)<0)e.push('resolution_type');
  if(!(r.satisfaction>=0.6&&r.satisfaction<=1.0))e.push('satisfaction');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-multi-turn-dialogues-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('multi-turn-dialogues',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
