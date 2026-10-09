(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return s[(r()*s.length)|0];}
function ri(r,a,b){return a+((r()*(b-a+1))|0);}
function pad6(n){return String(n).padStart(6,'0');}

var CATS=['math','logic','science','planning','general'];

var FACTS=[
 {q:'What is the chemical symbol for gold?',
  steps:['Gold is a transition metal listed in the periodic table.','Its Latin name is aurum, and symbols often come from Latin names.','The table entry for gold reads Au.','Therefore, the answer is Au.'],
  a:'Au'},
 {q:'At what temperature does pure water boil at sea level?',
  steps:['Boiling happens when vapor pressure equals atmospheric pressure.','At sea level the standard pressure is one atmosphere.','Under one atmosphere, pure water boils at 100 degrees Celsius.','Therefore, the answer is 100°C.'],
  a:'100°C'},
 {q:'How many planets orbit the Sun?',
  steps:['Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune are planets.','Pluto was reclassified as a dwarf planet in 2006.','Counting the eight confirmed planets gives 8.','Therefore, the answer is 8.'],
  a:'8'},
 {q:'What is the speed of light in a vacuum, in km/s?',
  steps:['Light travels at a constant speed in a vacuum, denoted c.','It is defined as exactly 299,792,458 meters per second.','Converting meters to kilometers gives 299,792 km/s.','Therefore, the answer is 299,792 km/s.'],
  a:'299,792 km/s'},
 {q:'Which gas do plants absorb from the air for photosynthesis?',
  steps:['Photosynthesis converts light energy into chemical energy.','Its inputs are water from roots and a gas from the air.','That gas is carbon dioxide, released back as oxygen.','Therefore, the answer is carbon dioxide.'],
  a:'carbon dioxide'},
 {q:'How many sides does a hexagon have?',
  steps:['Polygon names use Greek number prefixes.','The prefix hex- means six.','So a hexagon has 6 sides.','Therefore, the answer is 6.'],
  a:'6'}
];

var RIDDLES=[
 {q:'I have keys but no locks, space but no room. You can enter but never go inside. What am I?',
  steps:['Keys without locks suggests keyboard keys.','Space without room suggests the space bar.','Enter that you press but never go inside matches the Enter key.','Therefore, the answer is a keyboard.'],
  a:'a keyboard'},
 {q:'The more of me you take, the more you leave behind. What am I?',
  steps:['Taking more of something that grows as you take it is unusual.','Walking takes steps and leaves footprints behind.','More steps means more footprints left behind.','Therefore, the answer is footsteps.'],
  a:'footsteps'},
 {q:'I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?',
  steps:['Speaking without a mouth suggests sound without a speaker.','Hearing without ears suggests the sound bounces back.','Wind carries sound across distances.','Therefore, the answer is an echo.'],
  a:'an echo'}
];

var XS=['cats','dogs','birds','fish'],YS=['mammals','animals','pets','vertebrates'],ZS=['Whiskers','Rex','Tweety','Bubbles'];
var DAYS=['3','5','7'],GEAR=['a rain jacket','hiking boots','a power adapter','sunscreen','a first-aid kit'];
var TRIPS=['hiking','beach','city','camping'];

function mathTrace(rnd){
  var kind=ri(rnd,0,2),q,steps,a;
  if(kind===0){
    var b=ri(rnd,20,80),x=ri(rnd,5,30),d=ri(rnd,3,20),s1=b+x,ans=s1-d;
    q='A library has '+b+' books. It buys '+x+' more, then donates '+d+'. How many books does it have now?';
    steps=['Start with '+b+' books.','Add the '+x+' purchased books: '+b+' + '+x+' = '+s1+'.','Subtract the '+d+' donated books: '+s1+' - '+d+' = '+ans+'.','Therefore, the answer is '+ans+'.'];
    a=String(ans);
  }else if(kind===1){
    var m1=ri(rnd,3,12),m2=ri(rnd,3,12),c=ri(rnd,1,20),p=m1*m2,ans2=p+c;
    q='What is '+m1+' × '+m2+' + '+c+'?';
    steps=['Follow the order of operations: multiplication before addition.','First multiply '+m1+' × '+m2+' = '+p+'.','Then add '+c+': '+p+' + '+c+' = '+ans2+'.','Therefore, the answer is '+ans2+'.'];
    a=String(ans2);
  }else{
    var v=ri(rnd,40,110),h=ri(rnd,2,6),ans3=v*h;
    q='A train travels at '+v+' km/h for '+h+' hours. How far does it go?';
    steps=['Speed is '+v+' km/h and time is '+h+' hours.','Distance = speed × time = '+v+' × '+h+' = '+ans3+' km.','Therefore, the answer is '+ans3+' km.'];
    a=ans3+' km';
  }
  return {question:q,steps:steps,answer:a};
}

function logicTrace(rnd){
  var kind=ri(rnd,0,1),q,steps,a;
  if(kind===0){
    var X=pick(rnd,XS),Y=pick(rnd,YS),Z=pick(rnd,ZS);
    q='Premises: All '+X+' are '+Y+'. '+Z+' is a '+X+'. Is '+Z+' a '+Y+'?';
    steps=['All '+X+' are '+Y+' is the universal premise.',''+Z+' is a '+X+' is the particular premise.','By deduction, '+Z+' inherits the property of '+X+'.','Therefore, the answer is Yes.'];
    a='Yes';
  }else{
    q='If it rains, the ground gets wet. It is not raining. Is the ground necessarily dry?';
    steps=['The rule is: rain implies wet ground.','"It is not raining" denies the antecedent.','Denying the antecedent does not deny the consequent; other causes exist.','Therefore, the answer is No.'];
    a='No';
  }
  return {question:q,steps:steps,answer:a};
}

function planningTrace(rnd){
  var d=pick(rnd,DAYS),trip=pick(rnd,TRIPS),gear=pick(rnd,GEAR);
  var q='Plan a packing list for a '+d+'-day '+trip+' trip.';
  var ans='Pack: clothes for '+d+' days, toiletries, travel documents, and '+gear+'.';
  var steps=['List daily needs: clothes for '+d+' days, toiletries, travel documents.','Add trip-specific gear: '+gear+' for the '+trip+' trip.','Check the weather forecast for the '+d+' days and adjust layers.','Therefore, the answer is: '+ans];
  return {question:q,steps:steps,answer:ans};
}

function generate(seed,opts,rnd){
  rnd=rnd||prng(seed);
  var domain=(opts&&opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:pick(rnd,CATS);
  var t;
  if(domain==='math')t=mathTrace(rnd);
  else if(domain==='logic')t=logicTrace(rnd);
  else if(domain==='science'){var f=pick(rnd,FACTS);t={question:f.q,steps:f.steps.slice(),answer:f.a};}
  else if(domain==='planning')t=planningTrace(rnd);
  else{var g=pick(rnd,RIDDLES);t={question:g.q,steps:g.steps.slice(),answer:g.a};}
  var id='JAH-TRACE-'+pad6(seed);
  return {id:id,trace_id:id,question:t.question,reasoning_steps:t.steps,
    final_answer:t.answer,domain:domain,verified:true,title:t.question.slice(0,80)};
}

function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-TRACE-\d{6}$/.test(r.id))e.push('id');
  if(r.trace_id!==r.id)e.push('trace_id');
  if(typeof r.question!=='string'||!r.question.length||r.question.length>600)e.push('question');
  if(!Array.isArray(r.reasoning_steps)||r.reasoning_steps.length<3||r.reasoning_steps.length>5)e.push('reasoning_steps');
  else r.reasoning_steps.forEach(function(s,i){if(typeof s!=='string'||!s.length||s.length>600)e.push('reasoning_steps['+i+']');});
  if(typeof r.final_answer!=='string'||!r.final_answer.length)e.push('final_answer');
  if(CATS.indexOf(r.domain)<0)e.push('domain');
  if(r.verified!==true)e.push('verified');
  if(r.title!==String(r.question).slice(0,80))e.push('title');
  if(!e.length){
    var last=r.reasoning_steps[r.reasoning_steps.length-1];
    if(last.indexOf(r.final_answer)<0)e.push('final_answer not consistent with reasoning steps');
  }
  return {ok:!e.length,errors:e};
}

var gen={version:'jahdb-reasoning-traces-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('reasoning-traces',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
