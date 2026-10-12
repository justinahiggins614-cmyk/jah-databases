(function(){'use strict';
/* Public Podcasts Database generator — jahdb-public-podcasts-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature-generated-sample" = Signature-authored sample episode,
   clearly labeled — never presented as a harvested public record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
var PREFIX='JAH-POD-';
var GENRES=['technology','science','history','storytelling','education','arts','news','comedy'];
var SHOWS=[
 {show:'The Open Airwaves Hour',host:'Mara Ellison',genre:'technology',premise:'long-form conversations with builders about how technology actually gets made'},
 {show:'Field Notes',host:'Dr. Theo Okafor',genre:'science',premise:'a working scientist explains one discovery at a time, with all the wrong turns included'},
 {show:'The Long Nineteenth Century',host:'Prof. Ada Whitfield',genre:'history',premise:'history told through the letters, ledgers and lost objects of ordinary people'},
 {show:'Static & Signal',host:'The Night Desk',genre:'storytelling',premise:'original audio fiction — one complete story per episode, no cliffhangers'},
 {show:'How It Works, Really',host:'Sam Reyes',genre:'education',premise:'patient explainers that start from zero and end with genuine understanding'},
 {show:'The Gallery Ear',host:'June Park',genre:'arts',premise:'artists describe the work they make and the life that makes it possible'},
 {show:'The Week, Carefully',host:'R. Calloway',genre:'news',premise:'one week of world events, slowed down and put back in context'},
 {show:'The Laugh Track Test',host:'Duo Beaumont',genre:'comedy',premise:'two comedians stress-test jokes the way engineers stress-test bridges'}
];
var TOPICS={
 technology:['the quiet return of the personal website','why small software teams beat big ones','the undersea cables carrying this episode','repair culture and the right to fix','what "open" really means in open source'],
 science:['how migratory birds read the night sky','the microbes that clean our water','why sleep scientists changed their minds','volcanoes as climate time machines','the mathematics of murmuration'],
 history:['the telegraph operators who saved a town','when libraries lent more than books','the canal diggers of the industrial age','a lighthouse keeper\'s logbook, 1891','the women who mapped the ocean floor'],
 storytelling:['The Lighthouse at Greyrock','The Last Projectionist','A Field of Static','The Cartographer\'s Daughter','Night Train to Meridian'],
 education:['how to read a scientific paper','the one idea behind compound interest','what maps get wrong on purpose','a beginner\'s guide to logical fallacies','how elections are actually counted'],
 arts:['the color that changed painting','street photography ethics','why we hum in minor keys','the architecture of small libraries','pottery and patience'],
 news:['a slow look at the week in technology','a slow look at the week in science','a slow look at the week in culture','a slow look at the week in cities','a slow look at the week in exploration'],
 comedy:['the science of the punchline','hecklers: a field guide','when jokes stop being funny','the rule of three, explained badly','audience participation disasters']
};
var SEG={
 technology:['We start with the artifact itself — what it is, who made it, and the problem it was trying to solve.','Then we zoom out: the supply chains, standards and quiet agreements that make it possible.','We close with what it means for the next ten years, and one prediction we will happily be wrong about.'],
 science:['First, the observation that started it all — often an accident, always a curiosity.','Then the experiment: what was tested, what failed, and what finally held up.','We end with the open questions, because every answered question in science is a doorway.'],
 history:['We open on the primary source — a letter, a logbook, a ledger entry — read aloud in full.','Then the context: the world that made this document necessary, and the people it names.','We close by tracing one thread from that world into ours.'],
 storytelling:['Our story begins, as all good ones do, with someone who wants something they cannot have.','The middle turns on a choice — the kind with no clean answer.','It ends the way the best stories end: resolved, but still echoing.'],
 education:['We define our terms carefully, because most confusion starts with fuzzy words.','Then we build the idea up in layers, checking each step as we go.','Finally, three worked examples — and one common mistake to watch for.'],
 arts:['We begin with the work itself: what you see, hear or feel when you meet it.','Then the maker\'s story — the constraints, accidents and obsessions behind it.','We close with how to look at it yourself, next time you get the chance.'],
 news:['First, what actually happened this week — the verified facts, in order.','Then the context the headlines skipped: the history and incentives underneath.','We finish with what to watch next, and the questions nobody is asking yet.'],
 comedy:['We open with the bit itself, performed live and unedited.','Then the autopsy: why it works, when it fails, and the mechanics underneath.','We close with an audience dare — try the technique yourself this week.']
};
function fmtDate(s){
 var y=2019+ri(s,0,6), m=ri(s,1,12), d=ri(s,1,28);
 return y+'-'+String(m).padStart(2,'0')+'-'+String(d).padStart(2,'0');
}
function generate(seed,opts){
 opts=opts||{}; var s=prng(seed);
 var genre=opts.genre&&GENRES.indexOf(opts.genre)>=0?opts.genre:pick(GENRES,s);
 var candidates=SHOWS.filter(function(x){return x.genre===genre;});
 var sh=candidates.length?pick(candidates,s):pick(SHOWS,s);
 var topic=pick(TOPICS[sh.genre],s);
 var epNo=seed;
 var segs=SEG[sh.genre];
 var title=sh.show+' #'+epNo+': '+topic.charAt(0).toUpperCase()+topic.slice(1);
 var transcript='['+sh.show+' — Episode '+epNo+' — "'+topic+'"]\n\n'+sh.host.toUpperCase()+': Welcome back to '+sh.show+'. I\'m '+sh.host+', and this week we\'re taking on '+topic+'.\n\n'+segs.map(function(g,i){return 'SEGMENT '+(i+1)+': '+g;}).join('\n\n')+'\n\n'+sh.host.toUpperCase()+': That\'s our show. '+sh.show+' is a Signature sample production — every episode is an original work. If '+topic+' caught your interest, start with the sources in our notes and keep asking questions. I\'m '+sh.host+'. See you next week.';
 var mins=ri(s,18,75);
 return {
  id:PREFIX+pad(seed),
  title:title,
  show:sh.show, host:sh.host,
  description:'Sample episode of "'+sh.show+'", hosted by '+sh.host+' ('+sh.premise+'). This installment tackles '+topic+' in three segments over about '+mins+' minutes. A Signature-authored sample episode — full transcript included, clearly labeled as a sample, never presented as a harvested public record.',
  genre:sh.genre, type:'podcast episode',
  duration_minutes:mins, release_date:fmtDate(s),
  audio_note:'Sample episode — no harvested audio file; the full transcript below is the complete episode content, plus a player-template demo program.',
  transcript:transcript,
  license:'Signature sample — original work, property of Justin Addam Higgins',
  demo:{kind:'podcast-player',program:'<audio controls preload="none" src="EPISODE_AUDIO_URL_HERE">\n  <p>'+title.replace(/</g,'&lt;')+'</p>\n</audio>\n<!-- Replace EPISODE_AUDIO_URL_HERE with the episode MP3 to make this player live. -->',note:'Drop-in HTML5 audio player template for this episode. Replace the placeholder URL with a real MP3.'},
  src:'signature-generated-sample', _seed:seed
 };
}
function validate(r){
 var e=[];
 if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
 if(!/^JAH-POD-\d{6}$/.test(r.id||''))e.push('id');
 if(typeof r.title!=='string'||r.title.length<8)e.push('title');
 if(typeof r.description!=='string'||r.description.length<60)e.push('description');
 if(GENRES.indexOf(r.genre)<0)e.push('genre');
 if(typeof r.transcript!=='string'||r.transcript.length<200)e.push('transcript');
 if(!r.demo||typeof r.demo.program!=='string')e.push('demo');
 if(r.src!=='signature-generated-sample')e.push('src');
 return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
 var dups=(sample||[]).filter(function(r){return r&&(r.t===record.title||r.title===record.title);});
 return dups.length?{ok:false,errors:['duplicate title in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-public-podcasts-1.0',generate:generate,validate:validate,driftCheck:driftCheck,genres:GENRES};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-podcasts',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
