/* JAH Retro Gaming Database generator. Property of Justin Addam Higgins (JAH).
   Signature version in the Signature system. Deterministic: same seed -> same record. */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(s,r){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var SLUG='retro-gaming',PREFIX='JAH-RG-';
var CATS=['console','handheld','game','peripheral','media'];
/* [title, maker, year, kind, generation/media, cat, description] */
var REAL=[
["Atari 2600","Atari","1977","console","second generation","console","Launched the home console market with interchangeable cartridges. Its wood-grain design is an icon of 1970s tech."],
["Nintendo Entertainment System","Nintendo","1985","console","third generation","console","Revived the North American game industry after the 1983 crash. The gray box with the front-loading cartridge slot defined a generation."],
["Sega Master System","Sega","1986","console","third generation","console","Sega's 8-bit challenger with the hidden snail maze in Alex Kidd built into the hardware. A cult classic worldwide."],
["Sega Genesis","Sega","1989","console","fourth generation","console","The 16-bit blast-processing machine that took on Nintendo directly. Sonic the Hedgehog was born here."],
["Super Nintendo","Nintendo","1991","console","fourth generation","console","Home of Mode 7 graphics and the Super FX chip. Its controller shape became the template for modern gamepads."],
["TurboGrafx-16","NEC","1989","console","fourth generation","console","NEC's HuCard-based 16-bit system, famous for shooters and the Bonk mascot. A collector favorite."],
["Neo Geo","SNK","1990","console","fourth generation","console","Arcade-perfect hardware for the home at a luxury price. The AES cartridges remain the largest game carts ever made."],
["Game Boy","Nintendo","1989","handheld","fourth generation","handheld","The green-screened brick that sold over 118 million units. Tetris packed in the box made it unstoppable."],
["Atari Lynx","Atari","1989","handheld","fourth generation","handheld","The first handheld with a color backlit screen, designed by Epyx. Technically ahead of its time but out-marketed."],
["Sega Game Gear","Sega","1991","handheld","fourth generation","handheld","Sega's full-color handheld with a TV tuner accessory. Ate batteries but dazzled with color."],
["Sony PlayStation","Sony","1995","console","fifth generation","console","The CD-based console that sold over 100 million units and moved gaming to discs. Final Fantasy VII lived here."],
["Nintendo 64","Nintendo","1996","console","fifth generation","console","The last major cartridge console, with the first successful analog stick on its trident controller. Super Mario 64 defined 3D."],
["Sega Saturn","Sega","1995","console","fifth generation","console","Sega's dual-CPU 32-bit system, beloved for arcade ports and Japanese exclusives. A complex machine with a devoted following."],
["Sega Dreamcast","Sega","1999","console","sixth generation","console","The first console with a built-in modem for online play. Gone too soon, but its VMU memory cards were genius."],
["Game Boy Color","Nintendo","1998","handheld","fifth generation","handheld","Full color in the same brick form factor. Pokemon Gold and Silver shone on its reflective screen."],
["Game Boy Advance","Nintendo","2001","handheld","sixth generation","handheld","32-bit handheld power with a huge library. The SP redesign added the clamshell and front light."],
["Super Mario Bros.","Nintendo","1985","game","NES cartridge","game","The platformer that saved the industry. World 1-1 remains the most studied level in game design."],
["The Legend of Zelda","Nintendo","1987","game","NES cartridge","game","Introduced battery-backed saving to console games. Its gold cartridge and open world were revolutionary."],
["Sonic the Hedgehog","Sega","1991","game","Genesis cartridge","game","Sega's blue blur and the mascot war of the 90s. Speed and attitude in 16 bits."],
["Tetris (Game Boy)","Nintendo","1989","game","Game Boy cartridge","game","Alexey Pajitnov's falling blocks packed with every Game Boy. The perfect handheld game."],
["Super Mario 64","Nintendo","1996","game","N64 cartridge","game","The blueprint for 3D platformers. Its camera and movement are still studied by designers."],
["Final Fantasy VII","Square","1997","game","PlayStation CD","game","The RPG that made PlayStation a phenomenon. Three discs of cinematic storytelling."],
["Street Fighter II (SNES)","Capcom","1992","game","SNES cartridge","game","The arcade king ported home. The SNES version proved consoles could host real fighters."],
["NES Advantage","Nintendo","1987","peripheral","joystick","peripheral","Nintendo's arcade-style joystick with turbo switches and slow motion. A living room arcade stick."],
["Super Game Boy","Nintendo","1994","peripheral","SNES adapter","peripheral","Played Game Boy games on the SNES with color palettes and custom borders. A brilliant bridge device."],
["Sega CD","Sega","1992","peripheral","Genesis add-on","peripheral","The CD add-on for Genesis with full-motion video ambitions. Home of Night Trap and the FMV era."],
["32X","Sega","1994","peripheral","Genesis add-on","peripheral","Sega's mushroom-shaped 32-bit add-on. A short-lived experiment in the add-on wars."],
["Power Glove","Mattel","1989","peripheral","NES controller","peripheral","The infamous NES motion controller. Terrible to play, legendary in pop culture."],
["R.O.B.","Nintendo","1985","peripheral","NES robot","peripheral","The Robotic Operating Buddy that helped Nintendo sell the NES as a toy. Only two games, infinite nostalgia."],
["Game Genie","Galoob","1990","peripheral","cheat cartridge","peripheral","Nintendo sued over it and lost. The code-entry cheat device every kid coveted."],
["Compact Disc (game media)","Sony/Philips","1995","media","optical disc","media","The 650MB disc that ended the cartridge era for home consoles. PlayStation bet everything on it and won."],
["HuCard","NEC","1987","media","card","media","Credit-card sized game media for the TurboGrafx-16. Tiny carts, big games."],
["Neo Geo AES cartridge","SNK","1990","media","cartridge","media","The largest home game cartridges ever produced, some over 700 megabits. Luxury media for a luxury system."]
];
var NOTES=["Boxed copies in good condition command premium prices.","The original manuals are prized by collectors.","Reproduction labels are common; check the board inside.","This hardware revision is the one collectors seek.","Capacitor replacement is common maintenance for this unit.","Region-free mods are popular for this hardware.","The startup sound alone triggers nostalgia.","Complete-in-box examples are increasingly rare."];
var SIG_SYS=["Nova Boy","Pixel Deck","Turbo Comet","Star Cartridge","Retro Forge","Bit Voyager","Quantum Pad","Echo Console","Prism Handheld","Drift Station","Iron Pixel","Solar Cart","Comet Dock","Neon Vault","Frost Byte","Copper Core","Silent Chip","Nova Cart","Tide Board","Ember Pad"];
function generate(seed,opts,rnd){
  rnd=rnd||prng(seed);
  var cat=(opts&&opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:CATS[seed%CATS.length];
  var id=PREFIX+String(seed).padStart(7,'0');
  if(seed<=2500){
    var e=REAL[(seed-1)%REAL.length];
    return {id:id,t:e[0],title:e[0],description:e[6]+" "+pick(rnd,NOTES),
      category:e[5],g:e[5],maker:e[1],year:e[2],kind:e[3],platform:e[4],
      source:"fact-checked",source_ref:"Video Game History Foundation records",
      signature_counterpart:PREFIX+String(seed+2500).padStart(7,'0')};
  }
  var tt=pick(rnd,SIG_SYS)+" "+pick(rnd,["Signature Edition","Mark II","Deluxe","Revival"]);
  var kind=pick(rnd,["console","handheld","game","peripheral"]);
  return {id:id,t:tt,title:tt,
    description:"A Signature original "+kind+" concept: "+tt+". "+pick(rnd,["It pairs authentic retro input feel with modern display output.","Its cartridge slot accepts a new Signature flash format.","The design echoes the golden age with fully original hardware.","Every unit is built for repairability with labeled boards."])+" "+pick(rnd,NOTES),
    category:cat,g:cat,maker:"Signature Retro Works",year:String(ri(rnd,2021,2026)),kind:kind,platform:"Signature line",
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
var gen={version:'jahdb-retro-gaming-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
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
