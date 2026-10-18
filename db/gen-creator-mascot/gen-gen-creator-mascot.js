(function(){'use strict';
/* The The Creator Mascot Database generator — jahdb-gen-creator-mascot-pub-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-CREATOR-MASCOT-PUB-";
var GENVER="jahdb-gen-creator-mascot-pub-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The First Sketch",
  "The Name Vote",
  "The Three Traits",
  "The Color Pick",
  "The Standout Feature",
  "The Happy Pose",
  "The Catchphrase",
  "The Debut",
  "The Emote Version",
  "The Fan Art Seed",
  "The Plush Dream",
  "The Lore Seed"
 ],
 "Compounded": [
  "The Expression Sheet",
  "The Outfit Variants",
  "The Animated Idle",
  "The Sidekick",
  "The Villain",
  "The Lore Episodes",
  "The Mascot Cam",
  "The Community Variants",
  "The Crossover",
  "The Holiday Mascot",
  "The Origin Comic",
  "The Voice"
 ],
 "Advanced": [
  "The Mascot Universe",
  "The Animated Series",
  "The Game Cameo",
  "The Merch Empire",
  "The Live Suit",
  "The Legacy Mascot",
  "The Handoff",
  "The Museum",
  "Teaching Mascot Design",
  "Masterclass: Character Appeal"
 ]
};
var BLURBS={
 "The First Sketch": "Rough concept: the mascot\u2019s birth.",
 "The Name Vote": "Community names the mascot: the christening.",
 "The Three Traits": "Personality in three words: the character core.",
 "The Color Pick": "Signature colors: the visual identity.",
 "The Standout Feature": "The one memorable thing: the hook.",
 "The Happy Pose": "The default expression: the welcome.",
 "The Catchphrase": "Three words or less: the verbal mascot.",
 "The Debut": "Introducing the mascot: the unveiling.",
 "The Emote Version": "Mascot as emote: the tiny ambassador.",
 "The Fan Art Seed": "Inspiring community art: the creative spark.",
 "The Plush Dream": "The merch goal: the huggable future.",
 "The Lore Seed": "Where did it come from? The mystery.",
 "The Expression Sheet": "Hype, lurk, GG, RIP, sus: the full emotional range.",
 "The Outfit Variants": "Seasonal and event looks: the wardrobe.",
 "The Animated Idle": "A living mascot: the breathing character.",
 "The Sidekick": "A companion character: the duo.",
 "The Villain": "A playful antagonist: the drama.",
 "The Lore Episodes": "Backstory installments: the unfolding tale.",
 "The Mascot Cam": "Picture-in-picture mascot: the co-host.",
 "The Community Variants": "Fan-made versions: the shared creation.",
 "The Crossover": "Mascot meets mascot: the universe expands.",
 "The Holiday Mascot": "Seasonal forms: the festive shapeshifter.",
 "The Origin Comic": "The backstory, illustrated: the canon.",
 "The Voice": "How the mascot sounds: the audio identity.",
 "The Mascot Universe": "Full cast and world: the franchise.",
 "The Animated Series": "The mascot\u2019s own show: the spinoff.",
 "The Game Cameo": "Playable mascot: the interactive star.",
 "The Merch Empire": "Plushies, figures, apparel: the tangible mascot.",
 "The Live Suit": "The mascot, in person: the meet-and-greet.",
 "The Legacy Mascot": "A decade of love: the icon.",
 "The Handoff": "The mascot outlives the channel: the enduring character.",
 "The Museum": "The mascot\u2019s history, archived: the hall of fame.",
 "Teaching Mascot Design": "Show others: the character mentor.",
 "Masterclass: Character Appeal": "Why mascots work: the psychology of cute."
};

function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  var h=0;for(var i=0;i<safe.length;i++){h=(h*31+safe.charCodeAt(i))>>>0;}
  var steps=['Prepare the space','Gather the essentials','Do the core work','Review the result','Lock in the win'];
  var out='# '+safe+' — working demo\n# Field: '+field+'\n';
  out+='steps = '+JSON.stringify(steps)+'\n';
  out+='for i, s in enumerate(steps, 1):\n    print(f"{i}. {s}")\n';
  out+='print("Seed '+h+': repeat the steps in order and the result compounds.")\n';
  return out;
}

function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||['General Study'];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — mascot design record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). '+ (BLURBS[topic]||('A '+field+' study of "'+topic+'".')) +' Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'sample-demo',language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}

var BUILD_MASCOT=(function(){
var SPECIES=['a sleepy axolotl','a hyperactive raccoon','a chill capybara','a dramatic raven','a tiny dragon','a robot cat','a frog in a hoodie','a loaf-shaped blob'];
var TRAITS=['collects shiny things','naps through important moments','hypes up chat unprompted','judges silently, loves loudly','speaks only in emotes'];
return function(inp){
  var r=prng(inp.seed||29);
  var species=inp.species||pick(SPECIES,r);
  var trait=pick(TRAITS,r);
  return {title:'Channel mascot: '+species,intro:'A recognizable mascot for a '+(inp.theme||'variety')+' channel — design, personality, and expressions in one sheet.',
    sections:[{h:'Design',items:['Base: '+species+', 2-3 signature colors','One standout feature (oversized eyes, tiny hat, glowing accessory)','Chibi proportions: big head, small body — reads at any size']},{h:'Personality',text:'The mascot '+trait+'. It is the channel\u2019s emotional support creature.'},{h:'Expression sheet',items:['Hype (sparkles, open mouth)','Lurk (half-lidded, blanket)','GG (salute or bow)','RIP (X eyes, tiny ghost)','Sus (side-eye, magnifier)']},{h:'Backstory seed',text:'It showed up in chat one day during a raid and never left. The community named it; the lore writes itself from there.'}]};
};})();

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
var gen={version:GENVER,generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
gen.builderId="mascot";
gen.builderFields=[["theme", "Channel theme", "text", "variety"], ["species", "Base creature (blank = surprise me)", "text", ""], ["seed", "Seed (optional)", "number", "29"]];
gen.build=BUILD_MASCOT;

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gen-creator-mascot',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();