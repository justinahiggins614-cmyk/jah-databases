(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['explanation','how-to','creative','analysis','coding','math'];
var PREFIX='JAH-INST-';
var CONCEPTS=[
 ['photosynthesis','plants turn sunlight, water and carbon dioxide into food','a leaf in bright sunlight'],
 ['gravity','a force that pulls objects with mass toward each other','an apple falling from a tree'],
 ['supply and demand','prices rise when demand outruns supply','concert tickets selling out'],
 ['evaporation','liquid molecules escaping into the air as gas','a puddle shrinking on a hot day'],
 ['inflation','a general rise in prices over time','a grocery bill growing each year'],
 ['the water cycle','water moving between ocean, air and land in a loop','rain filling a mountain stream'],
 ['compound interest','interest earning interest on itself over time','a savings account doubling across decades'],
 ['photosynthesis in algae','single-celled organisms making food from light','a pond turning green in spring']
];
var HOWTOS=[
 ['tie a shoelace so it stays tied','Make two loops ("bunny ears"), cross them, pull tight, then double-knot the loops.','Test it with a firm tug.'],
 ['boil an egg with a firm yolk','Lower eggs into boiling water, cook 9 minutes, then move to ice water.','Peel under running water.'],
 ['back up files to an external drive','Plug in the drive, copy your folders, then verify a few files open.','Keep the drive somewhere safe.'],
 ['change a flat tire','Loosen the lug nuts, jack up the car, swap the wheel, tighten in a star pattern.','Lower the car and re-check the nuts.'],
 ['write a clear to-do list','List tasks, mark the top three, estimate each time, then start with the hardest.','Cross items off as you go.'],
 ['plant a tomato seedling','Dig a hole twice the root ball, bury the stem deep, water well, add a stake.','Mulch around the base.']
];
var CREATIVE=[
 ['a lighthouse keeper on a foggy night','The lamp room smelled of oil and salt as the fog pressed against the glass.','Somewhere below, a ship answered with one long, grateful horn.'],
 ['a robot learning to paint','Its first strokes were straight lines; by dusk it was mixing sunset colors it had no word for.','The gallery called it "promisingly strange."'],
 ['the last train out of a sleepy town','The platform lights buzzed as the 11:40 pulled in, half empty and warm.','Mara boarded with a suitcase full of unsent letters.'],
 ['a garden that grows backwards in time','Each morning the roses were buds again, and the gardener younger by a day.','She decided some mysteries are better tended than solved.'],
 ['a detective who only solves breakfast crimes','The Case of the Missing Muffin cracked wide open at 7:15 a.m.','The culprit: a very guilty-looking raccoon.']
];
var ANALYZE=[
 ['the pros and cons of remote work','Remote work saves commute time and widens the talent pool, but it can blur work-life boundaries and weaken team bonds.','The best setups pair clear async habits with regular in-person weeks.'],
 ['why small habits beat big resolutions','A tiny daily habit compounds; a grand resolution collapses under its own weight by February.','Pick the smallest version of the goal you can repeat daily.'],
 ['the trade-offs of electric cars','EVs cut tailpipe emissions and fuel costs, while batteries raise upfront price and mining concerns.','For most drivers the math favors electric over a 5-year window.'],
 ['whether social media helps or harms teens','It connects isolated teens to community, yet rewards comparison and outrage.','Outcomes hinge on how the feed is curated, not the app itself.']
];
var CODING=[
 ['a function that checks if a string is a palindrome','Clean the string to lowercase letters, compare it with its reverse, return the result.','Test with "racecar" (true) and "hello" (false).'],
 ['code that finds the largest number in a list','Walk the list once, keep the biggest value seen so far, return it at the end.','Test with negatives to be safe.'],
 ['a loop that prints the first 10 Fibonacci numbers','Start with 0 and 1, print each, then shift the pair forward ten times.','Check the sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.'],
 ['a function that counts vowels in a sentence','Lowercase the text, count characters in "aeiou", return the count.','Test "hello world" - expect 3.']
];
var MATHQ=[
 ['If a train travels 60 mph for 2.5 hours, how far does it go?','Distance equals speed times time: 60 x 2.5 = 150 miles.','Always check that the units multiply correctly.'],
 ['What is 15% of 200?','Convert 15% to 0.15, then multiply: 0.15 x 200 = 30.','A quick check: 10% is 20, so 15% being 30 makes sense.'],
 ['Solve 3x + 7 = 22.','Subtract 7 from both sides to get 3x = 15, then divide by 3: x = 5.','Plug back in: 3(5) + 7 = 22. Correct.'],
 ['A rectangle is 8 by 5. What is its area?','Area equals length times width: 8 x 5 = 40 square units.','Perimeter would be 2(8+5) = 26, a different question.']
];
var ANGLES=['It matters because it shapes everyday decisions.','Beginners often trip on this, so take it slow.','Once this clicks, harder topics get easier.','This is one of those ideas worth revisiting yearly.'];

function build(rnd,cat){
  var ins,resp;
  if(cat==='explanation'){
    var c=pick(CONCEPTS,rnd);
    ins='Explain '+c[0]+' in simple terms.';
    resp='At its core, '+c[1]+'. A good example is '+c[2]+', which shows the idea in action. '+pick(ANGLES,rnd);
  }else if(cat==='how-to'){
    var h=pick(HOWTOS,rnd);
    ins='How do I '+h[0]+'?';
    resp=h[1]+' '+h[2]+' '+pick(ANGLES,rnd);
  }else if(cat==='creative'){
    var cr=pick(CREATIVE,rnd);
    ins='Write a short story opening about '+cr[0]+'.';
    resp=cr[1]+' '+cr[2];
  }else if(cat==='analysis'){
    var an=pick(ANALYZE,rnd);
    ins='Analyze '+an[0]+'.';
    resp=an[1]+' '+an[2];
  }else if(cat==='coding'){
    var cd=pick(CODING,rnd);
    ins='Describe how to write '+cd[0]+'.';
    resp=cd[1]+' '+cd[2];
  }else{
    var m=pick(MATHQ,rnd);
    ins=m[0];
    resp=m[1]+' '+m[2];
  }
  return {ins:ins,resp:resp};
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var b=build(rnd,cat);
  var id=PREFIX+String(seed).padStart(6,'0');
  var qs=Math.round((0.7+rnd()*0.3)*100)/100;
  return {id:id,pair_id:id,title:b.ins,instruction:b.ins,response:b.resp,category:cat,difficulty:ri(rnd,1,5),language:rnd()<0.92?'en':'es',quality_score:qs,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-INST-\d{6}$/.test(r.id||''))e.push('id');
  if(r.pair_id!==r.id)e.push('pair_id');
  if(typeof r.instruction!=='string'||!r.instruction.length)e.push('instruction');
  if(r.title!==r.instruction)e.push('title');
  if(typeof r.response!=='string'||!r.response.length)e.push('response');
  var sents=r.response.split(/[.!?]+/).filter(function(x){return x.trim().length;});
  if(sents.length<2||sents.length>4)e.push('response sentences');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.difficulty>=1&&r.difficulty<=5&&r.difficulty===(r.difficulty|0)))e.push('difficulty');
  if(r.language!=='en'&&r.language!=='es')e.push('language');
  if(!(r.quality_score>=0.7&&r.quality_score<=1.0))e.push('quality_score');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-instruction-pairs-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('instruction-pairs',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
