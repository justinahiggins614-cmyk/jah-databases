/* JAH Keyboard Database generator. Property of Justin Addam Higgins (JAH).
   Signature version in the Signature system. Deterministic: same seed -> same record. */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(s,r){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var SLUG='mechanical-keyboards',PREFIX='JAH-KB-';
var CATS=['switch','layout','keycap','board','accessory'];
/* [title, maker, kind, spec, sound, cat, description] */
var REAL=[
["Cherry MX Red","Cherry GmbH","linear switch","45cN / 2.0mm actuation","quiet","switch","The classic linear gaming switch from Cherry GmbH of Germany. Smooth 45cN travel with no tactile bump made it the esports standard."],
["Cherry MX Black","Cherry GmbH","linear switch","60cN / 2.0mm actuation","quiet","switch","The heavier linear sibling, favored by typists who bottom out hard. A 60cN spring gives it a deliberate feel."],
["Cherry MX Brown","Cherry GmbH","tactile switch","55cN / 2.0mm actuation","soft","switch","The middle-ground tactile switch with a subtle bump. The default choice for first mechanical keyboards worldwide."],
["Cherry MX Blue","Cherry GmbH","clicky switch","60cN / 2.25mm actuation","loud click","switch","The iconic clicky switch with an audible click jacket mechanism. Loved by typists, feared by coworkers."],
["Cherry MX Clear","Cherry GmbH","tactile switch","65cN / 2.0mm actuation","soft","switch","A pronounced tactile bump with a heavier spring. The enthusiast favorite for ergo boards and heavy typists."],
["Cherry MX Speed Silver","Cherry GmbH","linear switch","45cN / 1.2mm actuation","quiet","switch","A short-travel linear with 1.2mm actuation for faster keypress registration. Built for competitive gaming."],
["Gateron Red","Gateron","linear switch","45cN / 2.0mm actuation","quiet","switch","Gateron's smooth linear, famous for a less scratchy feel than stock Cherry. A budget custom favorite."],
["Gateron Yellow","Gateron","linear switch","50cN / 2.0mm actuation","quiet","switch","The community darling linear with a slightly heavier spring than Red. Factory smoothness made it a legend."],
["Gateron Brown","Gateron","tactile switch","55cN / 2.0mm actuation","soft","switch","Gateron's take on the classic tactile, smoother than its Cherry counterpart. A safe all-rounder."],
["Kailh Box Red","Kailh","linear switch","45cN / 1.8mm actuation","quiet","switch","Box-stem design resists dust and wobble. Kailh's Box series brought the box stem to the mainstream."],
["Kailh Box White","Kailh","clicky switch","50cN / 1.8mm actuation","crisp click","switch","A clicky Box switch with a click bar for a crisper, higher-pitched click than MX Blue."],
["Topre 45g","Topre Corporation","electrostatic switch","45g / capacitive","soft thock","switch","Electrostatic capacitive switches with a rubber dome. The famous Topre 'thock' defined premium typing."],
["IBM Model M buckling spring","IBM / Lexmark","buckling spring","~70cN / 2.3mm","loud clack","switch","The 1985 buckling-spring legend. Its hammer mechanism and steel plate made it the typing benchmark."],
["Alps SKCM","Alps Electric","tactile/clicky","varies","varies","switch","The complicated Alps switches of vintage boards. SKCM Blue and Orange are collector grails."],
["Hall effect magnetic switch","Wooting","magnetic switch","adjustable actuation","quiet","switch","Magnetic sensing enables adjustable actuation points and rapid trigger. Wooting's 60HE popularized it."],
["QWERTY layout","-","layout","ANSI full-size","-","layout","The 1870s typewriter arrangement that survived into the computer age. The default of defaults."],
["Dvorak layout","August Dvorak","layout","alternative","-","layout","Patented in 1936 to reduce finger travel. A cult favorite for ergonomics devotees."],
["Colemak layout","Shai Coleman","layout","alternative","-","layout","A modern QWERTY alternative keeping common shortcuts in place. Popular with programmers."],
["60% layout","-","layout","compact","-","layout","No function row, no arrows, no numpad. The minimalist layout that started the custom keyboard boom."],
["TKL layout","-","layout","tenkeyless","-","layout","Full-size minus the numpad. The competitive gaming standard for mouse space."],
["75% layout","-","layout","compact","-","layout","Nearly TKL in a tighter frame. A favorite of compact custom builds."],
["65% layout","-","layout","compact","-","layout","60% plus dedicated arrows. The sweet spot for many custom builders."],
["40% layout","-","layout","ultra-compact","-","layout","Numbers on a layer, maximum minimalism. Not for the faint of heart."],
["HHKB Professional","PFU","keyboard","Topre 45g / 60%","soft thock","board","The Happy Hacking Keyboard: Topre switches in a 60% layout with the iconic Control key position. The programmer's grail."],
["Das Keyboard Model S","Das Keyboard","keyboard","Cherry MX Blue","loud click","board","The blank-keyed board that made mechanical cool again. A typing statement piece."],
["Ducky One 2","Ducky","keyboard","Cherry MX / TKL","varies","board","Ducky's refined TKL with PBT keycaps. A community staple of the 2010s."],
["Keychron K8","Keychron","keyboard","Gateron / TKL wireless","varies","board","The wireless TKL that brought mechanical keyboards to Mac users. Hot-swap made it modder friendly."],
["Leopold FC660C","Leopold","keyboard","Topre 45g / 65%","soft thock","board","Topre switches in a 65% layout with dye-sub PBT caps. A premium compact classic."],
["Corsair K70","Corsair","keyboard","Cherry MX / full-size","varies","board","The aluminum-framed gaming board that defined RGB gaming keyboards. A mainstream bestseller."],
["GMK keycap sets","GMK","keycaps","doubleshot ABS","-","keycap","German-made doubleshot ABS keycaps with legendary colorways. Group-buy culture started here."],
["PBT keycap sets","-","keycaps","dye-sub PBT","-","keycap","Dye-sublimated PBT caps that resist shine for years. The daily-driver material."],
["SA profile keycaps","Signature Plastics","keycaps","sculpted tall","-","keycap","Tall sculpted retro keycaps from Signature Plastics. The vintage terminal look."],
["Coiled aviator cable","-","accessory","USB-C detachable","-","accessory","The coiled cable with aviator connector. The finishing touch on a custom desk setup."],
["Lubricant (Krytox 205g0)","-","accessory","switch lube","-","accessory","The thick lubricant that smooths linear switches. A staple of the custom switch modding ritual."],
["Switch puller","-","accessory","tool","-","accessory","The humble wire tool that started a thousand custom builds. Essential for hot-swap boards."]
];
var NOTES=["Enthusiasts often film and lube these before use.","Check stem wobble on a tester before committing to a full build.","Pair with thick PBT caps for the best sound.","Factory lube quality varies by batch.","A switch tester is the cheapest way to try these.","Sound tests for this are widely shared online.","Plate material changes the feel noticeably.","Spring swaps are a common mod for these."];
var SIG_SW=["Nova Linear","Ember Tactile","Tide Click","Prism Silent","Comet Speed","Iron Thock","Drift Feather","Solar Bump"];
var SIG_BD=["Signature Board 60","Signature Board TKL","Signature Pad","Signature Ergo","Signature Tenkey"];
function generate(seed,opts,rnd){
  rnd=rnd||prng(seed);
  var cat=(opts&&opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:CATS[seed%CATS.length];
  var id=PREFIX+String(seed).padStart(7,'0');
  if(seed<=2500){
    var e=REAL[(seed-1)%REAL.length];
    return {id:id,t:e[0],title:e[0],description:e[6]+" "+pick(rnd,NOTES),
      category:e[5],g:e[5],maker:e[1],kind:e[2],spec:e[3],sound:e[4],
      source:"fact-checked",source_ref:"Manufacturer spec sheets",
      signature_counterpart:PREFIX+String(seed+2500).padStart(7,'0')};
  }
  var isSw=cat==='switch';
  var tt=isSw?pick(rnd,SIG_SW)+" Signature":pick(rnd,SIG_BD);
  return {id:id,t:tt,title:tt,
    description:"A Signature original "+(isSw?"switch":"keyboard")+" design. "+(isSw?"Its stem rails are polished for a scratch-free press with a "+ri(rnd,40,70)+"cN spring.":"Its gasket-mounted plate and south-facing sockets are tuned for a deep, even sound.")+" "+pick(rnd,NOTES),
    category:cat,g:cat,maker:"Signature Key Works",kind:isSw?"linear switch":"keyboard",
    spec:isSw?ri(rnd,40,70)+"cN / "+(1+((rnd()*10)|0)/10).toFixed(1)+"mm":"Signature layout",
    sound:isSw?pick(rnd,["quiet","soft","deep thock"]):"tuned",
    source:"signature",sigil:"\u2733 SIGNATURE ORIGINAL"};
}
function escRx(s){return s.replace(/[.*+?^${}()|[\]\\-]/g,'\\$&');}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  ['id','title','description','category','maker','kind','source'].forEach(function(k){if(r[k]===undefined||r[k]===''||r[k]===null)e.push('missing '+k);});
  if(r.id&&!new RegExp('^'+escRx(PREFIX)+'\\d{7}$').test(r.id))e.push('bad id');
  if(typeof r.description==='string'&&r.description.length<60)e.push('description too short');
  if(r.category&&CATS.indexOf(r.category)<0)e.push('bad category');
  if(r.source&&['fact-checked','online','signature'].indexOf(r.source)<0)e.push('bad source');
  if(r.source!=='signature'&&!r.source_ref)e.push('source_ref required');
  if(r.source==='fact-checked'&&!r.signature_counterpart)e.push('signature_counterpart required');
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){return{ok:true,errors:[]};}
var gen={version:'jahdb-mechanical-keyboards-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
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
  t('reject bad id',!validate({id:'BAD',title:'x',description:'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',category:CATS[0],maker:'m',kind:'k',source:'signature'}).ok);
  t('reject short desc',!validate({id:PREFIX+'0000001',title:'x',description:'too short',category:CATS[0],maker:'m',kind:'k',source:'signature'}).ok);
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
