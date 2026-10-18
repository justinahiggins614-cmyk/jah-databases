(function(){'use strict';
/* The The Creator Brand Studio Signature generator — jahdb-gen-creator-brand-studio-signature-sig-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-CREATOR-BRAND-STUDIO-SIG-";
var GENVER="jahdb-gen-creator-brand-studio-signature-sig-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The Name Game",
  "The One-Word Tone",
  "The Color Three",
  "The Tagline Draft",
  "The Avatar Concept",
  "The Bio Rewrite",
  "The Niche Sentence",
  "The Voice Note",
  "The First Impression Audit",
  "The Consistency Check",
  "The Enemy List",
  "The Promise"
 ],
 "Compounded": [
  "The Visual System",
  "The Content Pillars",
  "The Voice Guide",
  "The Intro/Outro Identity",
  "The Community Name",
  "The Merch Seed",
  "The Collab Brand",
  "The Platform Adaptation",
  "The Story Arc",
  "The Values Statement",
  "The Rebrand Decision",
  "The Press Kit"
 ],
 "Advanced": [
  "The Brand Bible",
  "The Multi-Channel Empire",
  "The Licensing Play",
  "The Legacy Brand",
  "The Acquisition-Ready Brand",
  "The Global Brand",
  "The Movement Brand",
  "The Succession Plan",
  "Teaching Brand Building",
  "Masterclass: Brand Psychology"
 ]
};
var BLURBS={
 "The Name Game": "Brainstorm channel names that are searchable, sayable, and yours.",
 "The One-Word Tone": "Define your brand in one word: the decision filter.",
 "The Color Three": "Pick three brand colors: the visual signature.",
 "The Tagline Draft": "Ten taglines, one keeper: the promise in a sentence.",
 "The Avatar Concept": "A profile image idea that reads at any size.",
 "The Bio Rewrite": "A bio that says who, what, and why-follow in two lines.",
 "The Niche Sentence": "I make X for Y: the clarity statement.",
 "The Voice Note": "Record how you sound: the audio brand.",
 "The First Impression Audit": "What newcomers see in ten seconds: the fix list.",
 "The Consistency Check": "Does everything match? The brand audit.",
 "The Enemy List": "What your brand is NOT: the boundaries.",
 "The Promise": "What viewers can always expect: the brand contract.",
 "The Visual System": "Logo, palette, fonts, motifs: the complete look.",
 "The Content Pillars": "Three repeating formats: the brand\u2019s backbone.",
 "The Voice Guide": "How you write, speak, and joke: the documented voice.",
 "The Intro/Outro Identity": "Signature open and close: the bookends.",
 "The Community Name": "What fans call themselves: the tribe\u2019s title.",
 "The Merch Seed": "One product your brand could sell: the tangible brand.",
 "The Collab Brand": "How you show up with others: the guest protocol.",
 "The Platform Adaptation": "One brand, many platforms: the translation guide.",
 "The Story Arc": "Your creator journey as narrative: the brand\u2019s myth.",
 "The Values Statement": "What you stand for: the brand\u2019s spine.",
 "The Rebrand Decision": "When and how to evolve: the careful pivot.",
 "The Press Kit": "One page that explains you: the professional proof.",
 "The Brand Bible": "The complete documented identity: the definitive guide.",
 "The Multi-Channel Empire": "Sub-brands and spin-offs: the brand architecture.",
 "The Licensing Play": "Your brand on products: the business of identity.",
 "The Legacy Brand": "Built to outlast trends: the timeless identity.",
 "The Acquisition-Ready Brand": "A brand with real equity: the valuable asset.",
 "The Global Brand": "Crossing cultures: the universal identity.",
 "The Movement Brand": "Beyond content: the cause with a creator.",
 "The Succession Plan": "The brand beyond you: the enduring entity.",
 "Teaching Brand Building": "Show others the craft: the generous expert.",
 "Masterclass: Brand Psychology": "Why identities work: the science of recognition."
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
    name:topic+' — creator brand record',
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

var BUILD_BRAND_STUDIO=(function(){
var TONES={playful:['Witty sidekick','Chaos gremlin (lovable)','Hype friend'],calm:['Gentle guide','Thoughtful curator','Cozy narrator'],bold:['Hot-take machine','Myth-buster','High-energy coach'],nerdy:['Deep-dive analyst','Lore keeper','Experiment lab']};
var PALETTES=[['#0f172a midnight','#38bdf8 signal blue','#f8fafc paper white'],['#1a1a2e dusk purple','#e94560 punch pink','#f5f5f5 bone'],['#10231a forest','#a3e635 lime pop','#fefce8 cream'],['#2b2118 espresso','#d97706 amber','#fff7ed milk']];
var PILLARS=['Teach: one clear lesson per week','Entertain: one pure-fun piece per week','Connect: one community-driven piece per week'];
return function(inp){
  var r=prng(inp.seed||21);
  var niche=inp.niche||'gaming', tone=inp.tone||'playful';
  var names=[niche+' & chill', 'the '+niche+' lab', niche.charAt(0).toUpperCase()+niche.slice(1)+' FM', 'Ctrl+'+niche];
  var pal=pick(PALETTES,r), persona=pick(TONES[tone]||TONES.playful,r);
  return {title:'Creator brand: '+pick(names,r),intro:'A cohesive identity for a '+(tone)+' '+(niche)+' creator — name, look, voice, and content pillars in one kit.',
    sections:[{h:'Name shortlist',items:shuffle(names,r).slice(0,3)},{h:'Visual identity',items:pal},{h:'Voice — you are the '+persona,text:'Write every caption like the '+persona+' would say it out loud.'},{h:'Content pillars',items:PILLARS},{h:'Tagline starters',items:['"'+niche+', but funnier."','"New here? Start with the chaos."','"'+niche+' for people with 5 minutes."']}]};
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
gen.builderId="brand-studio";
gen.builderFields=[["niche", "Niche", "text", "gaming"], ["tone", "Tone", "select", ["playful", "calm", "bold", "nerdy"]], ["seed", "Seed (optional)", "number", "21"]];
gen.build=BUILD_BRAND_STUDIO;

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gen-creator-brand-studio-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();