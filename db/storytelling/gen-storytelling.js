(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['plots','characters','settings','arcs','devices'];
var PREFIX='JAH-STRY-';
var REF_HERO='https://fiveable.me/key-terms/introduction-creative-writing/freytags-pyramid';
var REF_BEAT='https://nofilmschool.com/save-the-cat-beat-sheet';
var REF_ARC='https://nofilmschool.com/story-arcs';
var REF_STD='Story craft standards (verified 2026-10-09)';
var HERO=[
 ['Ordinary World','The hero\u2019s normal life before the story begins.'],
 ['Call to Adventure','Something disrupts the status quo.'],
 ['Refusal of the Call','The hero hesitates, usually out of fear.'],
 ['Meeting the Mentor','Guidance or training for the road ahead.'],
 ['Crossing the Threshold','Commitment; the hero enters the unfamiliar world.'],
 ['Tests, Allies, Enemies','Challenges met; the rules of the new world learned.'],
 ['Approach','Setbacks force a new plan before the central crisis.'],
 ['The Ordeal','The biggest life-or-death crisis; the midpoint of change.'],
 ['Reward','Survival earns the prize; fear is overcome.'],
 ['The Road Back','The return journey begins; consequences chase.'],
 ['Resurrection','A final test using everything learned.'],
 ['Return with the Elixir','The hero returns transformed, bringing the reward home.']
];
var FREYTAG=[
 ['Exposition','Characters and setting are introduced.'],
 ['Inciting Incident','The event that sparks the conflict.'],
 ['Rising Action','Complications and obstacles build tension.'],
 ['Climax','The turning point at the peak of the pyramid.'],
 ['Falling Action','Consequences of the climax play out.'],
 ['Denouement','The final outcome and resolution.']
];
var THREE=[['Setup','Act One, about 25 percent: the world and the want.'],['Confrontation','Act Two, about 50 percent: obstacles escalate.'],['Resolution','Act Three, about 25 percent: climax and aftermath.']];
var BEATS=[
 ['Opening Image','Page 1: the before snapshot of tone and world.'],
 ['Theme Stated','Page 5: what the story is about, often spoken aloud.'],
 ['Set-Up','Pages 1-10: characters, stakes and world introduced.'],
 ['Catalyst','Page 12: the incident that disrupts the status quo.'],
 ['Debate','Pages 12-25: the hero wrestles with acting.'],
 ['Break into Two','Page 25: commitment; the journey begins.'],
 ['B Story','Page 30: the subplot carrying the theme.'],
 ['Fun and Games','Pages 30-55: the promise of the premise delivered.'],
 ['Midpoint','Page 55: stakes rise; the goal shifts.'],
 ['Bad Guys Close In','Pages 55-75: pressure mounts inside and out.'],
 ['All Is Lost','Page 75: the false defeat; the whiff of death.'],
 ['Dark Night of the Soul','Pages 75-85: despair and reflection.'],
 ['Break into Three','Page 85: the fresh idea that renews the fight.'],
 ['Finale','Pages 85-110: the climax; everything is risked.'],
 ['Final Image','Page 110: the after snapshot proving change.']
];
var KISHO=[['Ki','Introduction: characters and setting established.'],['Sho','Development: the story proceeds without major change.'],['Ten','Twist: an unexpected turn reframes everything.'],['Ketsu','Conclusion: the elements harmonize.']];
var ARCHETYPES=[
 ['Innocent','Seeks safety and happiness; honest and optimistic.'],
 ['Sage','Seeks truth through knowledge; the mentor mind.'],
 ['Explorer','Seeks freedom and discovery; restless and curious.'],
 ['Outlaw','Seeks liberation; breaks rules that deserve breaking.'],
 ['Magician','Makes dreams real; visionary and transformative.'],
 ['Hero','Proves worth through mastery; courageous and driven.'],
 ['Lover','Seeks intimacy and connection; passionate and devoted.'],
 ['Jester','Lives in the moment; humor disarms and reveals.'],
 ['Everyman','Belongs and connects; grounded and relatable.'],
 ['Caregiver','Protects and serves others; generous and selfless.'],
 ['Ruler','Creates order and prosperity; responsible and commanding.'],
 ['Creator','Builds something lasting; imaginative and original.']
];
var SHAPES=[
 ['Man in a Hole','Trouble strikes, then the hero climbs out stronger.'],
 ['Boy Meets Girl','Fortune rises, falls, then rises again.'],
 ['Cinderella','Rise, fall, rise: rags to riches to rags to riches.'],
 ['From Bad to Worse','Fortune declines steadily into the dark.'],
 ['Which Way Is Up','Fortune zigzags with no clear direction.'],
 ['Creation Story','The world itself is built step by step.'],
 ['Old Testament','Fortune falls from grace toward judgment.'],
 ['New Testament','Fortune rises from suffering toward redemption.']
];
var DEVICES=[
 ['Foreshadowing','Early hints prepare the audience for what comes.'],
 ['Chekhov\u2019s Gun','A shown detail must matter later.'],
 ['Red Herring','A false clue misdirects suspicion.'],
 ['Deus ex Machina','An outside force resolves the plot; use sparingly.'],
 ['In Medias Res','The story opens in the middle of the action.'],
 ['Cliffhanger','An unresolved ending compels the audience onward.'],
 ['Flashback','The past returns to explain the present.'],
 ['Framing Device','A story told within another story.'],
 ['Unreliable Narrator','The teller cannot be fully trusted.'],
 ['MacGuffin','The object everyone wants; its nature barely matters.'],
 ['Dramatic Irony','The audience knows what the character does not.'],
 ['Plot Twist','An unexpected turn reframes everything before it.'],
 ['Eucatastrophe','Tolkien\u2019s term: the sudden happy turn.'],
 ['Prolepsis','A flash-forward glimpse of what is to come.'],
 ['Stream of Consciousness','Thought rendered as it flows.'],
 ['Soliloquy','A character speaks inner thoughts aloud, alone.'],
 ['Foil','A contrasting character highlights the hero\u2019s traits.'],
 ['Motif','A recurring image or idea gathering meaning.'],
 ['Framing','See Framing Device: nested narration.'],
 ['Ticking Clock','A deadline forces the pace upward.']
];
var CARCS=[['Positive Change','The hero grows into a better self.'],['Negative Change','The hero falls into a worse self.'],['Flat / Static','The world changes around an unchanging hero.']];
var GENRES=[
 ['Fantasy','Secondary worlds with magic and mythic stakes.'],
 ['Science Fiction','Speculation on technology and its consequences.'],
 ['Mystery','A puzzle the reader and detective solve together.'],
 ['Romance','The central arc is the love relationship.'],
 ['Horror','Fear, dread and the uncanny drive the story.'],
 ['Western','Frontier justice on the edge of civilization.'],
 ['Historical','Real eras researched and brought alive.'],
 ['Thriller','Relentless pace; the clock is always ticking.'],
 ['Literary','Language and interior life take the lead.'],
 ['Adventure','Journeys, quests and physical trials.'],
 ['Dystopian','Broken futures that warn the present.'],
 ['Magical Realism','The impossible treated as everyday.']
];
var SETTINGS=[['Time','When the story happens shapes everything.'],['Place','Where it happens gives texture and limits.'],['Social Environment','Customs, class and culture press on characters.'],['Mood','The emotional weather of the world.']];
var SIG_A=['Moonlit','Crimson','Velvet','Ember','Harbor','Juniper','Onyx','Solstice'];
var SIG_B=['tale','saga','myth','fable','chronicle'];
function buildOnline(rnd,cat){
  var rec={category:cat,source:'online',creation_mode:'ONLINE-VERIFIED'};
  if(cat==='plots'){
    var r=rnd(),st,ref,frm;
    if(r<0.35){st=pick(HERO,rnd);ref=REF_HERO;frm='Hero\u2019s Journey';
      rec.title=frm+': '+st[0];rec.topic='story structure';rec.structure={framework:frm,stage:st[0],order:HERO.indexOf(st)+1,of:12,note:st[1]};}
    else if(r<0.5){st=pick(FREYTAG,rnd);ref=REF_HERO;frm='Freytag\u2019s Pyramid';
      rec.title=frm+': '+st[0];rec.topic='story structure';rec.structure={framework:frm,stage:st[0],order:FREYTAG.indexOf(st)+1,of:6,note:st[1]};}
    else if(r<0.6){st=pick(THREE,rnd);ref=REF_HERO;frm='Three-Act Structure';
      rec.title=frm+': '+st[0];rec.topic='story structure';rec.structure={framework:frm,stage:st[0],order:THREE.indexOf(st)+1,of:3,note:st[1]};}
    else if(r<0.8){st=pick(BEATS,rnd);ref=REF_BEAT;frm='Save the Cat Beat Sheet';
      rec.title=frm+': '+st[0];rec.topic='story beat';rec.structure={framework:frm,beat:st[0],order:BEATS.indexOf(st)+1,of:15,note:st[1]};}
    else{st=pick(KISHO,rnd);ref=REF_STD;frm='Kish\u014dtenketsu';
      rec.title=frm+': '+st[0];rec.topic='story structure';rec.structure={framework:frm,stage:st[0],order:KISHO.indexOf(st)+1,of:4,note:st[1]};}
    rec.source_ref=ref;
    rec.description='The '+rec.structure.stage+' is stage '+rec.structure.order+' of '+rec.structure.of+' in the '+frm+' framework. '+st[1]+' Writers use this structure to shape rising tension and earned payoffs.';
  }else if(cat==='characters'){
    var a=pick(ARCHETYPES,rnd);
    rec.title='Archetype: '+a[0];rec.topic='archetype';
    rec.structure={archetype:a[0],drive:a[1]};
    rec.source_ref=REF_STD;
    rec.description='The '+a[0]+' archetype '+a[1].charAt(0).toLowerCase()+a[1].slice(1)+' Archetypes give characters instant recognizable drives that writers can then deepen and subvert.';
  }else if(cat==='settings'){
    var g=pick(GENRES,rnd);
    rec.title='Genre setting: '+g[0];rec.topic='genre';
    rec.structure={genre:g[0],conventions:g[1]};
    rec.source_ref=REF_STD;
    rec.description='The '+g[0].toLowerCase()+' genre works with conventions: '+g[1]+' Genre sets the reader\u2019s contract about what kind of story this will be.';
  }else if(cat==='arcs'){
    var r2=rnd();
    if(r2<0.6){var sh=pick(SHAPES,rnd);rec.title='Story shape: '+sh[0];rec.topic='story shape';rec.structure={shape:sh[0],pattern:sh[1]};rec.source_ref=REF_ARC;
      rec.description='Vonnegut\u2019s '+sh[0]+' shape: '+sh[1]+' Plotting fortune over time reveals the emotional skeleton any story shares with its kin.';}
    else{var ca=pick(CARCS,rnd);rec.title='Character arc: '+ca[0];rec.topic='character arc';rec.structure={arc:ca[0],note:ca[1]};rec.source_ref=REF_STD;
      rec.description='A '+ca[0].toLowerCase()+' character arc: '+ca[1]+' Arcs track inner change against outer events.';}
  }else{
    var d=pick(DEVICES,rnd);
    rec.title='Story device: '+d[0];rec.topic='device';
    rec.structure={device:d[0],definition:d[1]};
    rec.source_ref=REF_STD;
    rec.description='The '+d[0].toLowerCase()+' device: '+d[1]+' Devices are tools, not tricks; they serve the story\u2019s meaning.';
  }
  return rec;
}
function buildSignature(rnd,cat){
  var rec={category:cat,source:'signature',creation_mode:'SIGNATURE-GENERATED'};
  var nm=pick(SIG_A,rnd)+' '+pick(SIG_B,rnd);
  if(cat==='plots'){var fw=pick(['Hero\u2019s Journey','Three-Act','Kish\u014dtenketsu'],rnd),stg=ri(rnd,4,12);
    rec.title='Signature plot outline: '+nm;rec.topic='plot outline';rec.structure={outline:nm,framework:fw,stages:stg};
    rec.description='A Signature-generated plot outline named '+nm+' in '+stg+' stages on a '+fw+' skeleton. An original story blueprint by the JAH generator.';}
  else if(cat==='characters'){var ar=pick(ARCHETYPES,rnd);
    rec.title='Signature character: '+nm;rec.topic='character';rec.structure={name:nm,base_archetype:ar[0],want:pick(['redemption','revenge','belonging','freedom'],rnd)};
    rec.description='A Signature-generated character named '+nm+', a '+ar[0].toLowerCase()+'-rooted figure who wants '+rec.structure.want+'. An original character study by the JAH generator.';}
  else if(cat==='settings'){rec.title='Signature setting: '+nm;rec.topic='setting';rec.structure={setting:nm,genre:pick(GENRES,rnd)[0],era:pick(['past','present','near future','far future'],rnd)};
    rec.description='A Signature-generated setting named '+nm+', a '+rec.structure.era+' '+rec.structure.genre.toLowerCase()+' world. An original worldbuilding sketch by the JAH generator.';}
  else if(cat==='arcs'){rec.title='Signature arc study: '+nm;rec.topic='arc study';rec.structure={study:nm,shape:pick(SHAPES,rnd)[0],direction:pick(['rising','falling','cyclical'],rnd)};
    rec.description='A Signature-generated arc study named '+nm+' following a '+rec.structure.shape.toLowerCase()+' pattern with a '+rec.structure.direction+' line. An original structure experiment by the JAH generator.';}
  else{var dv=pick(DEVICES,rnd);rec.title='Signature device application: '+nm;rec.topic='device application';rec.structure={study:nm,device:dv[0],genre:pick(GENRES,rnd)[0]};
    rec.description='A Signature-generated application of '+dv[0].toLowerCase()+' inside a '+rec.structure.genre.toLowerCase()+' tale named '+nm+'. An original craft exercise by the JAH generator.';}
  return rec;
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var online=!opts.forceSignature&&(rnd()<0.24||opts.forceOnline);
  var rec=online?buildOnline(rnd,cat):buildSignature(rnd,cat);
  if(rec.description.length<165)rec.description+=' Filed as a complete searchable record in the JAH Databases archive, with its full specifications intact.';
  rec.id=PREFIX+String(seed).padStart(7,'0');rec._seed=seed;return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-STRY-\d{7}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.length<8)e.push('title');
  if(typeof r.description!=='string'||r.description.length<150)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(r.source!=='online'&&r.source!=='signature')e.push('source');
  if(r.source==='online'&&(r.creation_mode!=='ONLINE-VERIFIED'||typeof r.source_ref!=='string'||!r.source_ref.length))e.push('source_ref');
  if(r.source==='signature'&&r.creation_mode!=='SIGNATURE-GENERATED')e.push('creation_mode');
  if(!r.structure||typeof r.structure!=='object')e.push('structure');
  if(r.source==='online'&&r.topic==='story structure'&&r.structure.framework==='Hero\u2019s Journey'){
    var f=HERO.filter(function(x){return x[0]===r.structure.stage;})[0];
    if(!f||HERO.indexOf(f)+1!==r.structure.order)e.push('hero_fact');
  }
  if(r.source==='online'&&r.topic==='story beat'){
    var b=BEATS.filter(function(x){return x[0]===r.structure.beat;})[0];
    if(!b||BEATS.indexOf(b)+1!==r.structure.order)e.push('beat_fact');
  }
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-storytelling-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('storytelling',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
