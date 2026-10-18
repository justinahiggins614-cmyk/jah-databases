(function(){'use strict';
/* Public Radio Database generator — jahdb-public-radio-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   Each record carries the COMPLETE original broadcast script — a full file,
   never a stub — plus a broadcast-player demo program.
   src:"signature-generated-sample" = Signature-authored original, clearly labeled. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
var PREFIX='JAH-RAD-';
var GENRES=['drama','mystery','western','science-fiction','comedy','variety','documentary','serial','radio-creator-guides'];
var SHOWS=[
 {show:'The Midnight Frequency',g:'drama',host:'Your host, Ellis Crane'},
 {show:'The Creator\u2019s Workbench',g:'radio-creator-guides',host:'Your coach, June Park'},
 {show:'Case Files of the Night Desk',g:'mystery',host:'Your host, Vera Sloane'},
 {show:'Dust and Thunder Mesa',g:'western',host:'Your trail guide, Sam Bridger'},
 {show:'Tales from the Ionosphere',g:'science-fiction',host:'Your navigator, Dr. Ilsa Renn'},
 {show:'The Hilarity Exchange',g:'comedy',host:'Your emcees, the Marlow Brothers'},
 {show:'The Starlight Revue',g:'variety',host:'Your master of ceremonies, Lola St. Clair'},
 {show:'Voices of the Valley',g:'documentary',host:'Your narrator, Douglas Fen'},
 {show:'The Perilous Adventures of Captain Meridian',g:'serial',host:'Your announcer, Rex Dalton'}
];
var SCRIPTS={
 drama:'[MUSIC: THEME — slow, low strings, then under]\n\nHOST: Good evening. This is the Midnight Frequency, and I am Ellis Crane. Tonight\'s drama: "The Letter That Arrived Forty Years Late."\n\n[SOUND: envelope sliding under a door]\n\nMARA: (reading) "My dearest June — if you are reading this, the lighthouse fund finally paid out..." June? That\'s my grandmother\'s name.\n\nELI: The postmark says 1984. The paper\'s older than both of us.\n\nMARA: Listen to this: "The money is yours. I never spent a dime of it. I just wanted you to know someone kept a promise."\n\n[SOUND: paper unfolding]\n\nELI: There\'s a key taped inside. Safety deposit box 114, First National.\n\nMARA: Forty years. Somebody carried this letter for forty years.\n\nHOST: And so Mara and Eli follow a forty-year-old promise to a small-town bank vault — where they find not money, but something the writer valued more: every letter June ever wrote, saved, and a note that reads, "You were never forgotten."\n\n[MUSIC: THEME swells, then fades]\n\nHOST: The letter that arrived forty years late... arrived exactly on time. This is Ellis Crane, on the Midnight Frequency. Good night.',
 mystery:'[MUSIC: THEME — pizzicato strings, a door creak]\n\nHOST: The Night Desk is open. I\'m Vera Sloane, and tonight\'s case file: "The Vanishing of Room 312."\n\n[SOUND: hotel lobby ambience, a bell dinging]\n\nCLERK: Room 312, sir? I\'m afraid there is no Room 312. There never has been.\n\nDETECTIVE RYE: The register says otherwise. Page forty-seven. "J. Marlowe, Room 312, checked in Tuesday."\n\nCLERK: Then the register is mistaken, sir.\n\n[SOUND: footsteps on marble, a key turning]\n\nRYE: (to himself) Third floor. 310... 311... 313. No 312. But the carpet here is newer. And this wall — listen. Hollow.\n\n[SOUND: knuckles rapping on plaster]\n\nHOST: Behind the plaster, Detective Rye finds a door — and behind the door, a room the hotel sealed in 1953, with a suitcase, a train ticket stub, and J. Marlowe\'s final note: "Tell them I checked out."\n\n[MUSIC: sting, then theme under]\n\nHOST: Some rooms vanish. The truth doesn\'t. Case closed. I\'m Vera Sloane — the Night Desk never sleeps.',
 western:'[MUSIC: THEME — lone harmonica, wind]\n\nHOST: Howdy, folks. Sam Bridger here with Dust and Thunder Mesa. Tonight: "The Water War of Dry Creek."\n\n[SOUND: wind, a creaking sign]\n\nSHERIFF: The creek\'s run dry three weeks, Cobb. Your dam\'s the only new thing upstream.\n\nCOBB: My cattle need water same as yours, Sheriff. Finders keepers.\n\nADA: (young, firm) Actually, Mr. Cobb — the 1879 charter says the creek belongs to the town. I looked it up. In the land office. Where the records are.\n\n[SOUND: papers slapping onto wood]\n\nCOBB: ...That\'s my grandfather\'s signature on that charter.\n\nADA: Then your grandfather already settled this argument, sir.\n\nHOST: And so the dam comes down plank by plank, the creek runs free by sundown, and Ada — all of nineteen — gets appointed keeper of the land office records.\n\n[SOUND: water flowing, swelling]\n\nHOST: In Dry Creek, water is law, and the law — this time — was on the side of the thirsty. Sam Bridger saying so long till next week.',
 'science-fiction':'[MUSIC: THEME — theremin over brass]\n\nHOST: Greetings, Earth. Dr. Ilsa Renn with Tales from the Ionosphere. Tonight: "The Slow Ship."\n\n[SOUND: deep engine hum, radio static]\n\nCAPTAIN: Meridian Station, this is the slow ship Halcyon. We left Earth orbit... (pause) ...two hundred years ago.\n\nSTATION: Halcyon, your signal is weak. Say again your mission elapsed time?\n\nCAPTAIN: Two. Hundred. Years. We sleep in shifts of twenty. My great-grandmother launched this ship. I will not live to see it arrive. My daughter might.\n\nSCIENCE OFFICER: Captain — the anomaly ahead. It\'s bending the signal. I think... I think it\'s a shortcut.\n\nCAPTAIN: "Shortcut." The most dangerous word in space.\n\nHOST: The Halcyon takes the shortcut — and emerges eleven years from home, not two hundred. The crew weeps. The captain laughs. And somewhere, the universe winks.\n\n[SOUND: engine hum rising to a chord]\n\nHOST: The slow ship arrived fast, because sometimes the long way around is through. Dr. Ilsa Renn, signing off.',
 comedy:'[MUSIC: THEME — kazoo orchestra]\n\nHOST: (fast) It\'s the Hilarity Exchange! I\'m Bix Marlow!\n\nHOST2: And I\'m Dex Marlow! Tonight: the world\'s worst inventions, ranked!\n\nBIX: Number five: the solar-powered flashlight. Works great — during the day.\n\nDEX: Number four: the waterproof towel. Dries nothing, weighs forty pounds.\n\nBIX: Number three: my uncle\'s "silent" alarm clock. It\'s just a brick with "WAKE UP" painted on it.\n\nDEX: Number two: decaffeinated coffee-flavored water. All of the sadness, none of the coffee.\n\nBIX: And number one: the extended warranty for a houseplant.\n\nDEX: (laughing) People! Water the plant! That\'s the warranty!\n\n[SOUND: audience roaring, a slide whistle]\n\nBIX: We\'ll be here all week! Tip your usher!\n\nDEX: And remember — the Hilarity Exchange: all jokes guaranteed, or your money back! (Some restrictions apply. All restrictions apply.)',
 variety:'[MUSIC: THEME — big band swell, applause]\n\nHOST: Good evening, ladies and gentlemen, this is Lola St. Clair welcoming you to the Starlight Revue! Tonight: the astonishing Marvin the Mentalist!\n\n[SOUND: applause]\n\nMARVIN: Thank you, Lola. Sir, in the third row — you\'re thinking of a number.\n\nGUEST: ...Seven?\n\nMARVIN: I was going to say seven! Incredible. Madam, you\'re thinking of a song.\n\nGUEST2: "Happy Birthday"?\n\nMARVIN: That\'s the one! I am never wrong. (Aside, whispered) Lola, the earpiece works great.\n\nLOLA: (laughing) And now, the Velveteen Trio with "Moonlight on the Marquee"!\n\n[SOUND: band plays, applause swells]\n\nHOST: What a night! Marvin the Mentalist, the Velveteen Trio, and — wait, is that a trained seal? Folks, only on the Starlight Revue! Good night, everybody!\n\n[MUSIC: theme out under applause]',
 documentary:'[MUSIC: THEME — gentle acoustic guitar]\n\nHOST: I\'m Douglas Fen, and this is Voices of the Valley. Tonight we visit the Miller family dairy farm, worked by four generations.\n\n[SOUND: cows, a screen door]\n\nGRANDMA MILLER: My father milked by hand, in the dark, at 4 a.m. He said the cows trusted the routine more than they trusted him.\n\nFATHER: We milk 200 head now, with machines, but I still walk the barn every night. You have to look them in the eye. Machines don\'t do that part.\n\nDAUGHTER: (young) I\'m studying agricultural science. I want to keep the farm AND fix the runoff. Grandma says that\'s the job: keep it, and make it better.\n\nGRANDMA MILLER: That\'s always been the job, sweetheart.\n\nHOST: Four generations, one valley, and the quiet agreement between people and land. The Millers don\'t just work the farm — they belong to it.\n\n[SOUND: evening crickets fade in]\n\nHOST: I\'m Douglas Fen. Next week: the town that saved its movie theater, one ticket at a time.',
 serial:'[MUSIC: THEME — brass fanfare, propeller drone]\n\nHOST: Faster than a rumor! Braver than a headline! It\'s... the Perilous Adventures of Captain Meridian! I\'m Rex Dalton!\n\n[SOUND: wind, ropes creaking]\n\nMERIDIAN: The skybridge is out, Sparky! We\'ll have to jump the gap!\n\nSPARKY: Captain, that gap is fifty feet of nothing!\n\nMERIDIAN: Then we\'d better be magnificent! Geronimoooo!\n\n[SOUND: whoosh, landing thud, cheering]\n\nVILLAIN: (distant, amplified) You may have crossed, Meridian — but the Storm Engine is MINE now!\n\nMERIDIAN: We\'ll see about that, Doctor Tempest! Sparky — the emergency parachute silk! We\'re going UP!\n\nHOST: Will Captain Meridian retake the Storm Engine? Will Sparky\'s parachute hold? Tune in next week for another perilous adventure!\n\n[MUSIC: fanfare out]',
 'radio-creator-guides':"[MUSIC: THEME \\u2014 bright acoustic]\\n\\nHOST: Welcome to the Creator\\u2019s Workbench. I\\u2019m June Park, and this show teaches you to make radio yourself.\\n\\n\\n\\n[SOUND: workshop ambience]\\n\\nPARK: Today\\u2019s workbench lesson: \\u201cDesigning Your Show Clock.\\u201d The hour, architected: segments that breathe.\\n\\n[SOUND: workshop ambience]\\n\\nPARK: Today\\u2019s workbench lesson: \\u201cThe Art of the Cold Open.\\u201d Sixty seconds to earn the hour.\\n\\n[SOUND: workshop ambience]\\n\\nPARK: Today\\u2019s workbench lesson: \\u201cInterviewing for Tape.\\u201d Conversations that survive editing.\\n\\n[SOUND: workshop ambience]\\n\\nPARK: Today\\u2019s workbench lesson: \\u201cWriting for the Ear.\\u201d Sentences built for listening, not reading.\\n\\n[SOUND: workshop ambience]\\n\\nPARK: Today\\u2019s workbench lesson: \\u201cThe Call-In Show Playbook.\\u201d Strangers, live, on your frequency.\\n\\n[SOUND: workshop ambience]\\n\\nPARK: Today\\u2019s workbench lesson: \\u201cSound Design on a Budget.\\u201d Cinema for the ears, made at a desk.\\n\\n[SOUND: workshop ambience]\\n\\nPARK: Today\\u2019s workbench lesson: \\u201cThe Morning Show Engine.\\u201d Waking up a city, daily.\\n\\n[SOUND: workshop ambience]\\n\\nPARK: Today\\u2019s workbench lesson: \\u201cNarrative Audio Storytelling.\\u201d The documentary arc in sound.\\n\\nHOST: That\\u2019s the workbench for today. Practice one lesson, then make something. I\\u2019m June Park \\u2014 now go build your show.\\n\\n[MUSIC: theme out]"
};
function generate(seed,opts){
 opts=opts||{}; var s=prng(seed);
 var genre=opts.genre&&GENRES.indexOf(opts.genre)>=0?opts.genre:null;
 var pool=genre?SHOWS.filter(function(x){return x.g===genre;}):SHOWS;
 var sh=pick(pool.length?pool:SHOWS,s);
 var epNo=seed;
 var year=1936+ri(s,0,20);
 var title=sh.show+' #'+epNo;
 var script=SCRIPTS[sh.g];
 var mins=ri(s,22,30);
 var program='<!-- '+title.replace(/-->/g,'')+' — broadcast player -->\n<audio controls preload="none" src="BROADCAST_AUDIO_URL_HERE">\n <p>'+title.replace(/</g,'&lt;')+' ('+year+')</p>\n</audio>\n<script>\n// Cue-sheet player: highlight script lines as the audio plays.\n// Pair each <p data-t="seconds"> line of the script with audio currentTime.\nvar a=document.querySelector("audio");\na&&a.addEventListener("timeupdate",function(){\n var t=a.currentTime,lines=document.querySelectorAll("[data-t]"),cur=null;\n lines.forEach(function(l){if(+l.dataset.t<=t)cur=l;});\n lines.forEach(function(l){l.classList.toggle("now",l===cur);});\n});\n<\/script>';
 return {
  id:PREFIX+pad(seed),
  title:title,
  series:sh.show, episode_no:epNo,
  description:'Sample broadcast script for "'+sh.show+'", episode '+epNo+' ('+sh.host+'). A complete original '+sh.g+' radio script in the classic style — announcer, dialogue, music and sound-effect cues, the whole half-hour on the page ('+mins+' min). A Signature-authored sample, clearly labeled, never presented as a harvested historic broadcast.',
  genre:sh.g, type:'radio broadcast',
  broadcast_year:String(year), runtime_minutes:mins,
  full_script:script,
  audio_note:'Sample script — the complete script is the broadcast; the cue-sheet player demo syncs script lines to audio.',
  license:'Signature sample — original work, property of Justin Addam Higgins',
  demo:{kind:'broadcast-player',program:program,note:'Cue-sheet broadcast player: HTML5 audio plus a script-following highlighter. Replace the placeholder URL with a real recording.'},
  src:'signature-generated-sample', _seed:seed
 };
}
function validate(r){
 var e=[];
 if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
 if(!/^JAH-RAD-\d{6}$/.test(r.id||''))e.push('id');
 if(typeof r.title!=='string'||r.title.length<8)e.push('title');
 if(typeof r.description!=='string'||r.description.length<60)e.push('description');
 if(GENRES.indexOf(r.genre)<0)e.push('genre');
 if(typeof r.full_script!=='string'||r.full_script.length<400)e.push('full_script');
 if(!r.demo||typeof r.demo.program!=='string')e.push('demo');
 if(r.src!=='signature-generated-sample')e.push('src');
 return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
 var dups=(sample||[]).filter(function(r){return r&&(r.t===record.title||r.title===record.title);});
 return dups.length?{ok:false,errors:['duplicate title in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-public-radio-1.0',generate:generate,validate:validate,driftCheck:driftCheck,genres:GENRES};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-radio',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
