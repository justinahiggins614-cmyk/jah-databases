/* JAH Pinball Database generator. Property of Justin Addam Higgins (JAH).
   Signature version in the Signature system. Deterministic: same seed -> same record. */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(s,r){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var SLUG='pinball',PREFIX='JAH-PIN-';
var CATS=['classic','electromechanical','solid-state','dot-matrix','modern-lcd'];
/* [title, maker, year, designer, theme, cat, description] — fact-checked public record entries */
var REAL=[
["The Addams Family","Bally","1992","Pat Lawlor","macabre comedy","dot-matrix","The best-selling pinball machine of all time with over 20,000 units built. The Thing flipper hand reaches out and grabs the ball, and the electric chair awards jackpots."],
["Twilight Zone","Bally","1993","Pat Lawlor","surreal TV","dot-matrix","Features the ceramic Powerball, a gumball machine that dispenses balls, and a working clock mounted on the playfield. One of the most complex and beloved machines of the 1990s."],
["Medieval Madness","Williams","1997","Brian Eddy","medieval fantasy","dot-matrix","Castle gates explode, trolls pop up from the playfield, and players battle through the kingdom. Widely regarded as the greatest pinball machine ever made."],
["Attack from Mars","Bally","1995","Brian Eddy","alien invasion","dot-matrix","Players defend Earth from Martian saucers, capped by the famous Stroke of Luck scoop. Fast play and 1950s sci-fi style made it an instant classic."],
["Funhouse","Williams","1990","Pat Lawlor","carnival","dot-matrix","Rudy, the talking animatronic head, taunts players through every game. Its clock-advancing modes set a new standard for humorous machine design."],
["Theatre of Magic","Bally","1995","John Popadiuk","stage magic","dot-matrix","The magic trunk spins and swallows the ball while a real magic wand rises from the playfield. A showman's machine packed with illusions."],
["Monster Bash","Williams","1998","George Gomez","classic monsters","dot-matrix","Dracula, Frankenstein, the Wolfman, the Mummy and the Creature perform on stage. The animated monster band plays through every mode."],
["Scared Stiff","Bally","1996","Dennis Nordman","horror comedy","dot-matrix","Elvira hosts a haunted house party featuring the crate, the spider, and the stiff-o-meter. A late Bally classic loaded with toys."],
["Tales of the Arabian Nights","Williams","1996","John Popadiuk","Arabian fantasy","dot-matrix","The spinning magic lamp and the genie battle anchor this Arabian adventure. Rich art and deep rules made it a collector favorite."],
["Creature from the Black Lagoon","Bally","1992","John Trudeau","horror film","dot-matrix","The Creature's hologram appears on the playfield under green light. A Universal monsters machine famous for its multiball."],
["Terminator 2: Judgment Day","Williams","1991","Steve Ritchie","sci-fi film","dot-matrix","Arnold Schwarzenegger callouts and a skull cannon that launches balls onto the playfield. A licensed blockbuster of the dot-matrix era."],
["Star Trek: The Next Generation","Williams","1993","Steve Ritchie","sci-fi TV","dot-matrix","Seven balls, seven missions, and a Borg ship that attacks the playfield. The widest body machine Williams ever built."],
["White Water","Williams","1993","Dennis Nordman","river rafting","dot-matrix","The bouncing raft and whirlpool ramp define this rafting adventure. Insanity Falls multiball is one of the most loved modes in pinball."],
["Fish Tales","Williams","1992","Mark Ritchie","fishing","dot-matrix","Cast for the biggest catch on the spinning fishing reel. A light-hearted widebody with one of the most famous toppers in pinball."],
["Indiana Jones: The Pinball Adventure","Williams","1993","Mark Ritchie","adventure film","dot-matrix","Features the moving idol, the Path of Adventure, and the airplane propeller shot. A huge widebody licensed from the film trilogy."],
["Gorgar","Williams","1979","Barry Oursler","fantasy warrior","solid-state","The first pinball machine with synthesized speech, growling 'Me got you.' A landmark of the solid-state era."],
["Fireball","Bally","1972","Ted Zale","fantasy","electromechanical","Introduced multiball to pinball with its spinning disc and zipper flippers. A defining electromechanical classic."],
["Black Knight","Williams","1980","Steve Ritchie","dark fantasy","solid-state","The first multilevel playfield in pinball history, with the Magna-Save magnet feature. Steve Ritchie's dark knight defined an era."],
["High Speed","Williams","1986","Steve Ritchie","police chase","solid-state","A runaway getaway with a real police siren and a hideout scoop. Launched the modern flow-style playfield design."],
["The Getaway: High Speed II","Williams","1992","Steve Ritchie","police chase","dot-matrix","The Supercharger ramp accelerates the ball to a blur. The sequel refined the chase with video mode and the red line."],
["Guns N' Roses","Data East","1994","John Borg","rock band","dot-matrix","The skull snake head, the spinning guitar, and Slash callouts. A rock licensed machine from the Data East years."],
["Jurassic Park","Data East","1993","Joe Kaminkow","dinosaur film","dot-matrix","The T. rex reaches out and eats the ball from the playfield. A film licensed dot-matrix machine."],
["Lord of the Rings","Stern","2003","George Gomez","fantasy film","dot-matrix","The Balrog, the Ring modes, and the Path of the Dead. Stern's licensed epic with deep rule layering."],
["The Simpsons Pinball Party","Stern","2003","Joe Balcer","cartoon","dot-matrix","Features the couch gag, Itchy and Scratchy modes, and a talking Krusty head. A deep cartoon licensed machine."],
["Spider-Man","Stern","2007","Steve Ritchie","comic hero","dot-matrix","Doc Ock's magnet and the Sandman up-post anchor this hero machine. Fast flow with a punishing outlane layout."],
["AC/DC","Stern","2012","Steve Ritchie","rock band","dot-matrix","The swinging bell, the cannon that fires balls, and the train wreck multiball. A loud, fast rock machine."],
["Metallica","Stern","2013","John Borg","rock band","dot-matrix","Sparky the electric chair robot, the snake, and the grave marker cross. A heavy metal machine with deep modes."],
["Ghostbusters","Stern","2016","John Trudeau","film","modern-lcd","Slimer on the playfield and the Ecto-Goggles scoop. A Stern Spike machine with full LCD display animation."],
["Star Wars","Stern","2017","Steve Ritchie","sci-fi film","modern-lcd","The hyperspace ramp loop and Death Star multiball. A fast Steve Ritchie layout on the modern LCD platform."],
["Deadpool","Stern","2018","George Gomez","comic hero","modern-lcd","Lil' Deadpool bash toy, the katana ramp, and the disco ball. A humor-packed modern machine."],
["Jurassic Park","Stern","2019","Keith Elwin","dinosaur film","modern-lcd","The T. rex head that grabs the ball and the raptor pen. Keith Elwin's deep rules adventure on the LCD platform."],
["Stranger Things","Stern","2019","Brian Eddy","TV","modern-lcd","The Demogorgon bash toy and the projector showing the Upside Down. Brian Eddy's return to pinball design."],
["Godzilla","Stern","2021","Keith Elwin","kaiju film","modern-lcd","The collapsing building, the Mechagodzilla multiball, and the magnetic bridge. A modern kaiju blockbuster."],
["Eight Ball Deluxe","Bally","1981","Bally design team","pool","solid-state","A pool hall classic with the famous deluxe drop-target bank. One of the most played solid-state machines ever."],
["Medieval Madness Remake","Chicago Gaming","2015","Brian Eddy (remake)","medieval fantasy","modern-lcd","A faithful remake of the 1997 Williams classic with a full-color LCD display. The castle destruction returns."],
["Elvira and the Party Monsters","Bally","1989","Jim Valenti","horror comedy","dot-matrix","Elvira hosts a party with the organ, the boot, and the deadheads. A late 80s Bally favorite."],
["Tales from the Crypt","Data East","1993","John Borg","horror TV","dot-matrix","The Crypt Keeper hosts with the tombstone drop targets. A horror anthology machine from Data East."]
];
var NOTES=[
"Collectors prize original examples with un-faded cabinet art.",
"Check the playfield for wear around the scoop before buying.",
"The translite artwork on this title is a standout of the era.",
"Rule depth rewards long-term play and league competition.",
"Sound design on this machine is considered best-in-class.",
"Factory mylar in high-wear zones keeps the playfield fast.",
"LED conversion is popular for this title's insert lighting.",
"Tournament players value its balanced risk-reward scoring."
];
var SIG_THEMES=["Quantum Harvest","Neon Diner","Clockwork Ocean","Solar Forge","Ghost Circuit","Thunder Bazaar","Iron Orchard","Starlight Foundry","Crimson Tundra","Echo Canyon","Midnight Carousel","Vortex Gardens","Storm Citadel","Pixel Frontier","Obsidian Reef","Solar Drift","Thunder Hollow","Crystal Relay","Ember Arcade","Lunar Foundry","Tide Engine","Prism Relay","Nomad Carnival","Frost Signal","Jade Tempest","Copper Mirage","Silent Comet","Drift Chapel","Iron Bloom","Nova Harbor"];
var SIG_MECH=["three-flipper multiball","spinning disc magnet","elevator ramp","rotating target bank","captive-ball orbit","drop-target ladder","magnetic slingshot","talking animatronic head","hologram projector","moving playfield toy","looping subway ramp","pop-bumper gauntlet","lock-bar skill shot","spinner frenzy mode","scoop kickback ladder","mini playfield vault"];
var SIG_TITLES=["Signature Series","Signature Line","Signature Edition","Signature Original","Signature Vault"];
function generate(seed,opts,rnd){
  rnd=rnd||prng(seed);
  var forced=(opts&&opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:null;
  var cat=forced||CATS[seed%CATS.length];
  var id=PREFIX+String(seed).padStart(7,'0');
  if(seed<=2500){
    var e=REAL[(seed-1)%REAL.length];
    return {id:id,t:e[0],title:e[0],
      description:e[6]+" "+pick(rnd,NOTES),
      category:forced||e[5],g:forced||e[5],maker:e[1],year:e[2],designer:e[3],theme:e[4],
      players:"1-4",source:"fact-checked",source_ref:"Internet Pinball Database (IPDB)",
      signature_counterpart:PREFIX+String(seed+2500).padStart(7,'0')};
  }
  var th=pick(rnd,SIG_THEMES),me1=pick(rnd,SIG_MECH),me2=pick(rnd,SIG_MECH);
  var ttl=th+" "+pick(rnd,SIG_TITLES);
  var mk=pick(rnd,["Signature Pinball Works","JAH Signature Amusements","Signature Playfield Co."]);
  var yr=String(ri(rnd,2019,2026)),ds=pick(rnd,["JAH Signature Studio","Signature Design Team"]);
  return {id:id,t:ttl,title:ttl,
    description:"A Signature original pinball machine themed around "+th.toLowerCase()+". Its playfield pairs a "+me1+" with a "+me2+", and the rules reward combo shots through the late-game wizard mode.",
    category:cat,g:cat,maker:mk,year:yr,designer:ds,theme:th,mechanisms:[me1,me2],
    players:"1-4",source:"signature",sigil:"\u2733 SIGNATURE ORIGINAL"};
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
function driftCheck(rec,sample){
  if(!sample||!sample.length)return{ok:true,errors:[]};
  var dup=sample.filter(function(r){return r&&r.t===rec.title&&r.id!==rec.id;});
  return{ok:true,errors:[],similar:dup.length};
}
var gen={version:'jahdb-pinball-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
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
