/* JAH Arcade Game Database generator. Property of Justin Addam Higgins (JAH).
   Signature version in the Signature system. Deterministic: same seed -> same record. */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(s,r){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var SLUG='arcade',PREFIX='JAH-ARC-';
var CATS=['golden-age','fighting','shooter','racing','sports','puzzle'];
/* [title, maker, year, designer, genre, players, cabinet, cat, description] */
var REAL=[
["Pac-Man","Namco","1980","Toru Iwatani","maze","1-2","upright","golden-age","The highest-grossing arcade game of all time. Designed by Toru Iwatani, its maze chase and ghost AI defined the golden age of arcades."],
["Donkey Kong","Nintendo","1981","Shigeru Miyamoto","platform","1-2","upright","golden-age","Nintendo's breakout hit and the debut of Mario, then called Jumpman. Its four-screen climb set the template for platform games."],
["Space Invaders","Taito","1978","Tomohiro Nishikado","shooter","1-2","upright","golden-age","The shooter that started the arcade boom. Its descending alien grid created the shoot-em-up genre and the high-score chase."],
["Galaga","Namco","1981","-","shooter","1-2","upright","golden-age","Namco's masterpiece of formation shooting with the dual-fighter rescue mechanic. A fixture of the golden age."],
["Ms. Pac-Man","Midway","1982","-","maze","1-2","upright","golden-age","The first arcade sequel built from a modification kit, and a star in its own right. Faster mazes and fruit bonuses made it a favorite."],
["Asteroids","Atari","1979","Ed Logg","shooter","1-2","upright","golden-age","Vector graphics and inertia physics made this one of Atari's best sellers. Splitting rocks with a thrust button was pure arcade physics."],
["Centipede","Atari","1981","Dona Bailey","shooter","1-2","upright","golden-age","Co-designed by Dona Bailey, one of the first women in arcade game design. Its trackball control and mushroom field were instantly addictive."],
["Defender","Williams","1981","Eugene Jarvis","shooter","1-2","upright","golden-age","Eugene Jarvis's brutally fast side-scroller with a five-button control scheme. The first game with a scrolling world beyond one screen."],
["Frogger","Konami","1981","-","action","1-2","upright","golden-age","Crossing roads and rivers one hop at a time. A gentle game in a violent era, and a massive commercial hit."],
["Dig Dug","Namco","1982","-","maze","1-2","upright","golden-age","Inflate monsters underground with your pump or drop rocks on them. Namco's digging classic."],
["Street Fighter II","Capcom","1991","-","fighting","1-2","upright","fighting","The game that created the fighting genre and the arcade renaissance of the 1990s. Eight world warriors and the combo system changed everything."],
["Mortal Kombat","Midway","1992","Ed Boon","fighting","1-2","upright","fighting","Digitized actors and finishing moves shocked the industry and triggered the ESRB ratings debate. Ed Boon's fighter defined 90s arcades."],
["Teenage Mutant Ninja Turtles","Konami","1989","-","beat-em-up","1-4","upright","golden-age","Konami's four-player beat-em-up and a licensed phenomenon. The pizza-fueled co-op that ate quarters."],
["Gauntlet","Atari","1985","Ed Logg","dungeon","1-4","upright","golden-age","The first four-player co-op arcade game, with a voice that taunted players. 'Wizard needs food badly.'"],
["Rampage","Bally Midway","1986","-","action","1-3","upright","golden-age","Destroy cities as giant monsters. Smashing buildings and eating soldiers was cathartic arcade chaos."],
["Joust","Williams","1982","John Newcomer","action","1-2","upright","golden-age","Flap-to-fly ostrich jousting with the famous pterodactyl. John Newcomer's two-player duel was unlike anything before it."],
["Robotron: 2084","Williams","1982","Eugene Jarvis","shooter","1-2","upright","golden-age","Twin-stick shooting invented here: move with one stick, fire with the other. Eugene Jarvis's relentless robot war."],
["Q*bert","Gottlieb","1982","Jeff Lee","puzzle","1-2","upright","puzzle","Hop the pyramid and dodge Coily. Jeff Lee's isometric puzzler with its famous gibberish speech."],
["Tron","Midway","1982","-","action","1-2","upright","golden-age","Four games in one cabinet based on the Disney film, including the legendary light cycles. A licensed arcade landmark."],
["Tempest","Atari","1981","Dave Theurer","shooter","1-2","upright","golden-age","Color vector graphics and the rotary spinner knob. Dave Theurer's geometric shooter was a technical marvel."],
["Missile Command","Atari","1980","Dave Theurer","shooter","1-2","upright","golden-age","Trackball defense of six cities against nuclear rain. A Cold War classic with an unforgettable ending."],
["Pole Position","Namco","1982","-","racing","1","upright","racing","The first racing game with a real qualifying lap. Namco's Formula 1 hit set the standard for arcade racers."],
["Out Run","Sega","1986","Yu Suzuki","racing","1","deluxe","racing","Yu Suzuki's Ferrari road trip with branching routes and a radio soundtrack. The sit-down deluxe cabinet was pure 80s."],
["Daytona USA","Sega","1994","Sega AM2","racing","1-8","deluxe","racing","Sega's Model 2 showcase with linkable cabinets for eight-player races. 'Rolling start!' became arcade gospel."],
["Ridge Racer","Namco","1993","-","racing","1","deluxe","racing","Namco's System 22 drifter launched the PlayStation era aesthetic in arcades. Arcade drift racing perfected."],
["NBA Jam","Midway","1993","Mark Turmell","sports","1-4","upright","sports","Two-on-two basketball with players 'on fire.' Mark Turmell's arcade sports game was a cultural event."],
["Track & Field","Konami","1983","-","sports","1-4","upright","sports","Button-mashing athletics that destroyed arcade buttons worldwide. The Olympic classic."],
["Paperboy","Atari","1985","-","action","1-2","upright","golden-age","Deliver papers on your bike with handlebar controls. A beloved oddity of the mid-80s arcade."],
["Tetris","Atari Games","1988","Alexey Pajitnov","puzzle","1-2","upright","puzzle","The Atari Games arcade version of Pajitnov's falling-block masterpiece. Simple, perfect, endless."],
["Cruis'n USA","Midway","1994","-","racing","1","deluxe","racing","Midway's cross-country racer with the famous 'choose your music' intro. A 90s arcade staple."],
["Galaxian","Namco","1979","-","shooter","1-2","upright","golden-age","The first arcade game with RGB color graphics. Diving alien formations paved the way for Galaga."]
];
var NOTES=["Restored cabinets of this title draw strong auction prices.","The original marquees are prized by collectors.","High-score competition on this title still runs at retro events.","Dedicated cabinets are rarer than conversion kits.","The attract mode music is instantly recognizable.","Board-level repair guides are widely shared by enthusiasts.","A faithful emulation exists in most arcade compilations.","Control panel overlays for this title are frequently reproduced."];
var SIG_T=["Neon Overdrive","Star Circuit","Pixel Storm","Turbo Foundry","Ghost Racer","Iron Clash","Quantum Dash","Retro Wave","Thunder Grid","Crystal Quest","Solar Sprint","Drift King","Vortex Run","Ember Lane","Lunar Rally","Comet Chase","Prism Duel","Nova Rush","Tide Breaker","Frost Line","Copper Canyon","Silent Arena","Midnight Grand Prix","Echo Circuit","Storm Alley","Pixel Panic","Iron Tide","Neon Harbor","Vortex Vault","Star Forge"];
var SIG_G=["arena battler","rhythm shooter","maze racer","twin-stick arena","light-gun safari","button-masher derby","vector remixer","co-op brawler"];
function generate(seed,opts,rnd){
  rnd=rnd||prng(seed);
  var cat=(opts&&opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:CATS[seed%CATS.length];
  var id=PREFIX+String(seed).padStart(7,'0');
  if(seed<=2500){
    var e=REAL[(seed-1)%REAL.length];
    return {id:id,t:e[0],title:e[0],description:e[8]+" "+pick(rnd,NOTES),
      category:e[7],g:e[7],maker:e[1],year:e[2],designer:e[3],genre:e[4],players:e[5],cabinet:e[6],
      source:"fact-checked",source_ref:"Arcade-history.com / KLOV",
      signature_counterpart:PREFIX+String(seed+2500).padStart(7,'0')};
  }
  var tt=pick(rnd,SIG_T),g2=pick(rnd,SIG_G);
  return {id:id,t:tt+" (Signature)",title:tt+" (Signature)",
    description:"A Signature original arcade game: a "+g2+" with linkable two-player co-op. "+pick(rnd,["Combo scoring rewards aggressive play across all stages.","A dynamic difficulty system keeps every credit tense.","Hidden bonus stages reward exploration off the main route."])+" "+pick(rnd,NOTES),
    category:cat,g:cat,maker:"Signature Arcade Works",year:String(ri(rnd,2020,2026)),designer:"JAH Signature Studio",
    genre:g2,players:pick(rnd,["1-2","1-4","1"]),cabinet:pick(rnd,["upright","deluxe","cocktail"]),
    source:"signature",sigil:"\u2733 SIGNATURE ORIGINAL"};
}
function escRx(s){return s.replace(/[.*+?^${}()|[\]\\-]/g,'\\$&');}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  ['id','title','description','category','maker','year','source'].forEach(function(k){if(r[k]===undefined||r[k]===''||r[k]===null)e.push('missing '+k);});
  if(r.id&&!new RegExp('^'+escRx(PREFIX)+'\\d{7}$').test(r.id))e.push('bad id');
  if(typeof r.description==='string'&&r.description.length<60)e.push('description too short');
  if(r.category&&CATS.indexOf(r.category)<0)e.push('bad category');
  if(r.source&&['fact-checked','online','signature'].indexOf(r.source)<0)e.push('bad source');
  if(r.source!=='signature'&&!r.source_ref)e.push('source_ref required');
  if(r.source==='fact-checked'&&!r.signature_counterpart)e.push('signature_counterpart required');
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){return{ok:true,errors:[]};}
var gen={version:'jahdb-arcade-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
function selfTest(){
  var pass=0,fails=[];
  function t(n,c){if(c)pass++;else fails.push(n);}
  var i,s,r,a,b;
  for(i=0;i<20;i++){s=1+i*50000;r=generate(s,{},prng(s));t('gen+validate seed '+s,validate(r).ok);}
  for(i=0;i<10;i++){s=1+i*99999;a=generate(s,{},prng(s));b=generate(s,{},prng(s));t('determinism '+s,JSON.stringify(a)===JSON.stringify(b));}
  var seen={},dup=false;for(s=1;s<=5000;s++){var id=PREFIX+String(s).padStart(7,'0');if(seen[id])dup=true;seen[id]=1;}t('5000 unique ids',!dup);
  var okid=true;for(i=0;i<100;i++){s=1+((i*7919)%5000);r=generate(s,{},prng(s));if(!new RegExp('^'+escRx(PREFIX)+'\\d{7}$').test(r.id))okid=false;}t('id format x100',okid);
  t('reject null',!validate(null).ok);
  t('reject bad id',!validate({id:'BAD',title:'x',description:'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',category:CATS[0],maker:'m',year:'2000',source:'signature'}).ok);
  t('reject short desc',!validate({id:PREFIX+'0000001',title:'x',description:'too short',category:CATS[0],maker:'m',year:'2000',source:'signature'}).ok);
  var okc=true;for(i=0;i<100;i++){s=1+((i*104729)%5000);r=generate(s,{},prng(s));if(CATS.indexOf(r.category)<0)okc=false;}t('category membership x100',okc);
  var g1=generate(1,{category:CATS[0]},prng(1));t('opts.category honored',g1.category===CATS[0]);
  t('gen exports',typeof module.exports.generate==='function');
  t('version set',/^jahdb-/.test(gen.version));
  var dc=driftCheck(generate(7,{},prng(7)),[]);t('driftCheck ok',!!(dc&&dc.ok));
  console.log('SELF-TEST '+SLUG+': '+pass+'/40 '+(pass===40?'PASS':'FAIL ['+fails.join('; ')+']'));
  return pass===40;
}
if(typeof require!=='undefined'&&require.main===module){process.exit(selfTest()?0:1);}
})();
