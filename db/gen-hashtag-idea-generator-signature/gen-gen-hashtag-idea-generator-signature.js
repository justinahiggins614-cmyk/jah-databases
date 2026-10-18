(function(){'use strict';
/* JAH Hashtag Idea Generator - jahdb-gen-hashtag-idea-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL client-side generator: style transforms + validation + scoring. Same seed, same hashtag.
   signature edition. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX="JAH-HHIGS-";
var FIELDS=["Food & Drink", "Days", "Animals", "Lifestyle"];
var TOPICS={"Food & Drink": ["coffee", "pizza"], "Days": ["monday", "friday", "weekend"], "Animals": ["cat", "dog"], "Lifestyle": ["gym", "book", "nap", "wifi", "plant"]};
var ADJECTIVES={"c": ["Cozy", "Chaotic", "Caffeinated"], "p": ["Peaceful", "Playful", "Powerful"], "m": ["Moody", "Motivated", "Messy"], "f": ["Fresh", "Fearless", "Funny"], "w": ["Wild", "Warm", "Wacky"], "g": ["Glorious", "Goofy", "Gritty"], "b": ["Bold", "Breezy", "Bright"], "d": ["Daring", "Dreamy", "Delightful"], "n": ["Nifty", "Noble", "Neat"]};
var PUNS={"coffee": ["BrewHaha", "EspressoYourself"], "pizza": ["SliceToMeetYou", "SliceSliceBaby"], "monday": ["Mondaze", "MonYay"], "friday": ["FriYay", "FridayFeeling"], "weekend": ["WeekendWarrior", "SleepEnd"], "cat": ["Purrfection", "MeowMania"], "dog": ["PawSome", "PupCulture"], "gym": ["FlexFest", "SwolePatrol"], "book": ["ShelfAware", "NovelIdea"], "nap": ["NapQueen", "SleepOnIt"], "wifi": ["StreamDream", "ConnectedChaos"], "plant": ["SproutAbout", "LeafItToMe"]};
var RHYMES={"coffee": ["CoffeeToffee", "LattePatter"], "pizza": ["CheesyBreezy", "PizzaFesta"], "monday": ["MondayFunday", "MondayRunDay"], "friday": ["FridayMyDay", "FridaySkyHigh"], "weekend": ["WeekendBlend", "WeekendUnwind"], "cat": ["CatChat", "CatHat"], "dog": ["DogBlog", "DogJog"], "gym": ["TrainGain", "PumpJump"], "book": ["BookNook", "ReadFeed"], "nap": ["NapTrap", "NapClap"], "wifi": ["WifiHiFi", "WifiSciFi"], "plant": ["PlantChant", "LeafRelief"]};
var TAILS=["aholic", "ista", "ology", "verse"];
var TWISTS=["", "Life", "Club", "Era", "Mode", "Daily", "Chronicles"];
var STYLES=["alliteration", "pun", "portmanteau", "rhyme", "contrast", "exaggeration", "relatable", "aspirational"];
var SOURCE='signature';
function pick(r,arr){return arr[(r()*arr.length)|0];}
function cap(s){return s.charAt(0).toUpperCase()+s.slice(1);}
function buildTag(topic,style,r,twist){
  var c=cap(topic), core, label;
  if(style==='alliteration'){var adj=pick(r,ADJECTIVES[topic.charAt(0)]);core=adj+c;label='alliteration: '+adj+' + '+c;}
  else if(style==='pun'){core=pick(r,PUNS[topic]);label="pun on '"+topic+"'";}
  else if(style==='portmanteau'){var tail=pick(r,TAILS);core=c+tail;label='portmanteau: '+c+' + '+tail;}
  else if(style==='rhyme'){core=pick(r,RHYMES[topic]);label="rhyme on '"+topic+"'";}
  else if(style==='contrast'){core=c+'VsReality';label='contrast: '+c+' vs reality';}
  else if(style==='exaggeration'){var pre=pick(r,['Ultra','Extreme','Mega']);core=pre+c;label='exaggeration: '+pre+' '+c;}
  else if(style==='relatable'){core='Relatable'+c;label='relatable: shared '+topic+' experience';}
  else {core=c+'Goals';label='aspirational: '+c+' goals';}
  return {tag:'#'+core+twist,label:label};
}
function scoreTag(tag,style){
  var s=100-2*Math.max(0,tag.length-16);
  if(style==='alliteration')s+=10;
  if(tag.length<=14)s+=5;
  return Math.max(0,Math.min(100,s));
}
function assemble(seed,field){
  var r=prng(seed>>>0||1);
  var f=(field&&TOPICS[field])?field:pick(r,FIELDS);
  var topic=pick(r,TOPICS[f]), style=pick(r,STYLES);
  var tag='',label='',twist='',tries=0;
  while(tries<4){
    twist=tries<2?pick(r,TWISTS):'';
    var b=buildTag(topic,style,r,twist);tag=b.tag;label=b.label;
    if(tag.length<=24)break;
    tries++;
  }
  return {field:f,topic:topic,style:style,twist:twist||'(none)',hashtag:tag,
          technique:label,score:scoreTag(tag,style),length:tag.length};
}
function demoProgram(a){
  function q(s){return String(s).replace(/"/g,"'");}
  return '# Hashtag Idea Generator - live hashtag\nprint("FIELD:    '+q(a.field)+'")\nprint("TOPIC:    '+q(a.topic)+'")\nprint("STYLE:    '+q(a.style)+'")\nprint("TWIST:    '+q(a.twist)+'")\nprint("TECHNIQUE:'+q(a.technique)+'")\nprint()\nprint("HASHTAG: '+q(a.hashtag)+'")\nprint("SCORE: %d/100, LENGTH: %d chars" % ('+a.score+', '+a.length+'))\nprint("OK: hashtag built, validated, and scored")\n';
}
function generate(seed,opts,rnd){
  opts=opts||{};
  var a=assemble(seed>>>0||1,opts.field||null);
  var id=PREFIX+String(seed>>>0||1).padStart(6,'0');
  var title='Fresh Hashtag: '+a.hashtag+(SOURCE==='signature'?' (Signature Edition)':'');
  return {
    id:id,
    name:title+' — '+a.field,
    title:title,
    description:'GENERATED HASHTAG (live generator output - clearly labeled). '+a.hashtag+' — '+a.technique+', shareability '+a.score+'/100.',
    field:a.field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Live generator output - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:demoProgram(a),note:'Live hashtag demo program.'},
    _seed:seed>>>0||1, parts:a
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  if(!r.parts||!r.parts.hashtag)e.push('parts');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-gen-hashtag-idea-generator-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,assemble:assemble,buildTag:buildTag,scoreTag:scoreTag};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gen-hashtag-idea-generator',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
