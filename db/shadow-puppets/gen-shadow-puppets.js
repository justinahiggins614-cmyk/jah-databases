(function(){'use strict';
/* Signature Shadow Puppets Database generator — jahdb-shadow-puppets-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled) */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-SHADOW-P-';
var TOPICS=[["Hand Shadows", "Classic bunny and bird."], ["Dog Shadow", "Barking hand art."], ["Bird Shadows", "Flying figures."], ["Shadow Stories", "Narrative shadow play."], ["Cutout Puppets", "Cardboard characters."], ["Screen Setup", "Sheet-and-lamp theaters."], ["Light Sources", "Best lamps for shadows."], ["Jointed Puppets", "Moving-part figures."], ["Colored Shadows", "Gel-filter effects."], ["Shadow Animals", "Zoo of hand shapes."], ["Shadow Monsters", "Spooky figures."], ["Shadow Scenery", "Background cutouts."], ["Wayang Kulit", "Indonesian shadow art."], ["Chinese Shadow Play", "Ancient traditions."], ["Shadow Dance", "Body-shadow performance."], ["Kids Shadow Play", "Easy starters."], ["Shadow Games", "Guess-the-shadow."], ["Multiplayer Shadows", "Team figures."], ["Shadow Photography", "Capturing silhouettes."], ["Story Scripts", "Shadow tale scripts."], ["Music Shadows", "Rhythmic play."], ["Shadow Festivals", "Cultural celebrations."], ["DIY Shadow Kits", "Homemade sets."], ["Shadow History", "Ancient storytelling."], ["Practice Drills", "Hand dexterity."]];
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
    type:'shadow puppets creation', content:content, content_completeness:'stub',
    stub_note:'Topic stub: the topic title and its one-line brief are real; the full guide article is not yet written. This record does not present shell text as a complete guide.',
    demo:null, src:'signature', _seed:seed
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('shadow-puppets',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}

/* Group-0 expansion: 10 new topics. */
TOPICS.push(
["Wayang Kulit: Java’s Shadow Theater","A thousand years of leather puppets, gamelan music, and all-night epics: the world’s greatest shadow tradition."],
["Chinese Pi Ying Xi","Two thousand years of donkey-hide shadows: China’s pi ying xi, born for emperors and still performed today."],
["Karagöz and Hacivat","The Ottoman Empire’s beloved shadow clowns: Karagöz the trickster and Hacivat the scholar, bickering for five centuries."],
["Thai Nang Yai","Shadows the size of doors: Thailand’s nang yai uses meter-tall cowhide panels to tell the Ramakien epic."],
["Indian Tholu Bommalata","Andhra Pradesh’s colored shadows: translucent puppets big as children, glowing like stained glass."],
["Cambodian Sbek Thom","The Khmer Empire’s sacred shadows: two-meter panels of the Reamker, danced before gods and kings."],
["Hand Shadowgraphy: The Art of Trewey","No puppets, just hands: Félicien Trewey’s 19th-century shadowgraphy turned fingers into elephants, clowns, and whole plays."],
["Modern Shadow Dance","Bodies as puppets: contemporary troupes like Pilobolus turn human silhouettes into living shadow theater."],
["Shadow Puppetry in Film","From Lotte Reiniger’s silhouettes to modern cinema: how shadow puppetry became film’s most poetic technique."],
["Building a Home Shadow Theater","A bedsheet, a lamp, and cardboard: everything needed to stage shadow plays at home tonight."]
);
})();