(function(){'use strict';
/* JAH The Compliments Database generator — jahdb-compliments-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CMPL-";
var FIELDS=["Foundations","Compounded","Advanced", "Compliment Challenge", "Compliment Battle", "Compliment Finder", "Kindness Quest"];
var TOPICS={
 "Foundations": [
  "Thank You, and I Mean It - Foundations",
  "Noticing Small Efforts - Foundations",
  "You Are a Kind Person - Foundations",
  "Greeting People by Name - Foundations",
  "Praising Punctuality - Foundations",
  "Praising a Good Question - Foundations",
  "Acknowledging Hard Work in Progress - Foundations",
  "Complimenting Calm Under Pressure - Foundations",
  "Thanking Someone Publicly - Foundations",
  "Noticing Consistency - Foundations",
  "Praising Good Listening - Foundations",
  "Thanking Someone for Their Time - Foundations"
 ],
 "Compounded": [
  "Praising Craftsmanship - Compounded",
  "Complimenting a Well-Run Meeting - Compounded",
  "Acknowledging Everyday Courage - Compounded",
  "Praising Clear Writing - Compounded",
  "Complimenting Patience - Compounded",
  "Tasteful Appearance Compliments - Compounded",
  "Praising a Good Mentor - Compounded",
  "Complimenting Integrity - Compounded",
  "Recognizing Behind-the-Scenes Work - Compounded",
  "Praising Problem Solving - Compounded",
  "Complimenting Humor That Lifts a Room - Compounded",
  "Praising a Comeback From a Mistake - Compounded"
 ],
 "Advanced": [
  "Complimenting a Person's Whole Character - Advanced",
  "The Lifetime Achievement Tribute - Advanced",
  "Praising Moral Courage - Advanced",
  "Honoring a Life's Work - Advanced",
  "The Living Tribute: Say It While They Can Hear It - Advanced",
  "Recognizing a Mentor's Legacy - Advanced",
  "Complimenting Grace in Hard Times - Advanced",
  "Recognizing the Unsung Hero - Advanced",
  "Praising Forgiveness - Advanced",
  "The Compliment That Changes a Life - Advanced"
 ]
,
 "Compliment Challenge": [
  "The 7-Day Compliment Challenge",
  "The Stranger Compliment Dare",
  "The Colleague Challenge",
  "The Family Challenge",
  "The Written Challenge",
  "The Behind-Your-Back Challenge",
  "The Self-Compliment Challenge",
  "The Service Worker Challenge",
  "The Mentor Challenge",
  "The Difficult Person Challenge",
  "The Public Challenge",
  "The Quiet Challenge",
  "The Specificity Challenge",
  "The Morning Challenge",
  "The Legacy Challenge"
 ],
 "Compliment Battle": [
  "Battle Format: The Kindness Duel",
  "Battle Format: The Roast-to-Toast",
  "Battle Format: The Tag Team",
  "Battle Format: The Speed Round",
  "Battle Format: The Blind Battle",
  "Battle Judging: The Sincerity Meter",
  "Battle: The Championship",
  "Battle: The Audience Round",
  "Battle: The Themed Battle",
  "Battle: The Comeback",
  "Battle: The Written Round",
  "Battle: The Impromptu",
  "Battle: The Team Battle",
  "Battle: The Finals",
  "Battle: The Hall of Fame"
 ],
 "Compliment Finder": [
  "Finding the Unnoticed Effort",
  "Finding the Growth",
  "Finding the Character",
  "Finding the Craft",
  "Finding the Courage",
  "Finding the Consistency",
  "Finding the Kindness",
  "Finding the Humor",
  "Finding the Resilience",
  "Finding the Wisdom",
  "Finding the Generosity",
  "Finding the Precision",
  "Finding the Warmth",
  "Finding the Originality",
  "Finding the Everyday"
 ],
 "Kindness Quest": [
  "Quest: The Kindness Map",
  "Quest: The Thank-You Tour",
  "Quest: The Encouragement Drop",
  "Quest: The Listening Post",
  "Quest: The Skill Share",
  "Quest: The Welcome Wagon",
  "Quest: The Forgiveness Mission",
  "Quest: The Gratitude Wall",
  "Quest: The Compliment Flash Mob",
  "Quest: The Kindness Audit",
  "Quest: The Mentor Match",
  "Quest: The Celebration Squad",
  "Quest: The Repair Cafe",
  "Quest: The Story Collection",
  "Quest: The Kindness Legacy"
 ]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Compliment Study — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — compliment record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A compliment record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"compliment-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-compliments-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('compliments',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
