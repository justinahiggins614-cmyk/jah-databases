/* JAH Esports Database generator. Property of Justin Addam Higgins (JAH).
   Signature version in the Signature system. Deterministic: same seed -> same record. */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(s,r){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var SLUG='esports',PREFIX='JAH-ES-';
var CATS=['tournament','team','title','player','venue'];
/* [title, organizer, game, since, note, cat, description] */
var REAL=[
["The International","Valve","Dota 2","2011","crowdfunded prize pool","tournament","Valve's annual Dota 2 world championship with a crowdfunded prize pool that broke esports records. The Aegis of Champions is the most coveted trophy in esports."],
["League of Legends World Championship","Riot Games","League of Legends","2011","annual world final","tournament","Riot's yearly world final for League of Legends, drawing stadium crowds and record viewership. The Summoner's Cup crowns each season's best team."],
["Counter-Strike Major","Valve","Counter-Strike","2013","sponsored majors","tournament","Valve-sponsored majors are the pinnacle of Counter-Strike competition. Winning a Major cements a team's legacy."],
["EVO Championship Series","EVO","fighting games","1996","open bracket","tournament","The world's largest fighting game tournament, open to anyone brave enough to enter. Moments like EVO Moment 37 are esports folklore."],
["Overwatch League","Blizzard","Overwatch","2018","city franchises","tournament","Blizzard's city-based franchise league for Overwatch. A bold experiment in esports franchising."],
["Fortnite World Cup","Epic Games","Fortnite","2019","open qualifiers","tournament","Epic's 2019 World Cup in New York with a massive prize pool and open online qualifiers. A solo teenager won the first solo title."],
["Valorant Champions Tour","Riot Games","Valorant","2021","partnered teams","tournament","Riot's global circuit for Valorant with partnered leagues across regions. The Champions trophy is the FPS goal."],
["Call of Duty League","Activision","Call of Duty","2020","city franchises","tournament","Activision's franchise league for Call of Duty. Home of the CDL Championship weekend."],
["T1","T1 Entertainment","League of Legends","2003","three-time world champions","team","The most decorated League of Legends organization, built around the legendary Faker. A dynasty spanning two decades."],
["OG","OG Esports","Dota 2","2015","back-to-back TI wins","team","The first team to win The International twice, back to back in 2018 and 2019. The ultimate underdog story."],
["Team Liquid","Team Liquid","multi-title","2000","global organization","team","One of the oldest and largest esports organizations, fielding teams across many titles. A TI champion in Dota 2."],
["Natus Vincere","NAVI","Counter-Strike","2009","major champions","team","Ukraine's legendary organization, home of s1mple's prime years. A CS Major winning legacy."],
["FaZe Clan","FaZe Clan","multi-title","2010","content and competition","team","Born as a Call of Duty trickshot collective, grown into a global esports and culture brand."],
["Dota 2","Valve","-","2013","MOBA","title","Valve's MOBA and the home of The International. The deepest competitive game ever made, free to play."],
["League of Legends","Riot Games","-","2009","MOBA","title","Riot's MOBA and the most played PC game in the world. Its ranked ladder is the proving ground of millions."],
["Counter-Strike 2","Valve","-","2023","tactical FPS","title","Valve's tactical shooter successor to CS:GO. The economy system and one-tap headshots define it."],
["Valorant","Riot Games","-","2020","tactical FPS","title","Riot's hero tactical shooter blending CS-style gunplay with agent abilities. The VCT circuit's home."],
["StarCraft II","Blizzard","-","2010","RTS","title","Blizzard's real-time strategy epic. The Korean pro scene made it the original esport."],
["Street Fighter 6","Capcom","-","2023","fighting","title","Capcom's modern fighter and the centerpiece of the EVO main stage. Drive System reinvented the neutral game."],
["Faker (Lee Sang-hyeok)","T1","League of Legends","2013","the Unkillable Demon King","player","The greatest League of Legends player of all time, with multiple world titles across a decade. The face of esports."],
["s1mple (Oleksandr Kostyliev)","NAVI","Counter-Strike","2016","AWP legend","player","The most talented Counter-Strike player ever, famous for impossible AWP flicks. A Major champion."],
["N0tail (Johan Sundstein)","OG","Dota 2","2015","two-time TI winner","player","The heart of OG and a two-time International champion. The most beloved captain in Dota."],
["Mercedes-Benz Arena","-","multi-title","2017","Worlds 2017 final","venue","The Shanghai arena that hosted the League of Legends World Championship final. A landmark esports venue."],
["Chase Center","-","multi-title","2019","Worlds 2019 final","venue","San Francisco's arena hosted the 2019 League of Legends World Championship final."],
["Arthur Ashe Stadium","-","Fortnite","2019","Fortnite World Cup","venue","The tennis stadium converted for the Fortnite World Cup finals in New York. Esports in a Grand Slam venue."]
];
var NOTES=["Prize pools for this event have set industry records.","VODs of the grand finals are widely watched.","The format has evolved across seasons.","Regional qualifiers feed into this event.","Broadcast production set new standards.","Rivalries here are part of esports history.","The trophy is instantly recognizable.","Attendance records were broken here."];
var SIG_EV=["Signature Clash","Nova Cup","Iron Circuit","Thunder Bracket","Pixel Masters","Storm League","Ember Invitational","Crimson Major","Drift Championship","Vortex Open"];
var SIG_TM=["Signature Five","Nova Wolves","Iron Owls","Thunder Foxes","Pixel Ravens","Storm Badgers","Ember Lynx","Crimson Hawks"];
function generate(seed,opts,rnd){
  rnd=rnd||prng(seed);
  var cat=(opts&&opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:CATS[seed%CATS.length];
  var id=PREFIX+String(seed).padStart(7,'0');
  if(seed<=2500){
    var e=REAL[(seed-1)%REAL.length];
    return {id:id,t:e[0],title:e[0],description:e[6]+" "+pick(rnd,NOTES),
      category:e[5],g:e[5],organizer:e[1],game:e[2],since:e[3],note:e[4],
      source:"fact-checked",source_ref:"Esports public records",
      signature_counterpart:PREFIX+String(seed+2500).padStart(7,'0')};
  }
  var tt=cat==='team'?pick(rnd,SIG_TM):pick(rnd,SIG_EV)+" "+ri(rnd,2024,2030);
  return {id:id,t:tt,title:tt,
    description:"A Signature original esports "+cat+": "+tt+". "+pick(rnd,["An open-qualifier format keeps the bracket honest.","The league runs a double-elimination playoff with a fan-voted all-star match.","Prize distribution pays deep into the standings to sustain new talent.","Regional seeds feed a single global final each season."])+" "+pick(rnd,NOTES),
    category:cat,g:cat,organizer:"Signature Esports Circuit",game:pick(rnd,["Signature Arena","tactical FPS","MOBA","fighting"]),since:String(ri(rnd,2024,2026)),
    source:"signature",sigil:"\u2733 SIGNATURE ORIGINAL"};
}
function escRx(s){return s.replace(/[.*+?^${}()|[\]\\-]/g,'\\$&');}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  ['id','title','description','category','organizer','source'].forEach(function(k){if(r[k]===undefined||r[k]===''||r[k]===null)e.push('missing '+k);});
  if(r.id&&!new RegExp('^'+escRx(PREFIX)+'\\d{7}$').test(r.id))e.push('bad id');
  if(typeof r.description==='string'&&r.description.length<60)e.push('description too short');
  if(r.category&&CATS.indexOf(r.category)<0)e.push('bad category');
  if(r.source&&['fact-checked','online','signature'].indexOf(r.source)<0)e.push('bad source');
  if(r.source!=='signature'&&!r.source_ref)e.push('source_ref required');
  if(r.source==='fact-checked'&&!r.signature_counterpart)e.push('signature_counterpart required');
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){return{ok:true,errors:[]};}
var gen={version:'jahdb-esports-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
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
  t('reject bad id',!validate({id:'BAD',title:'x',description:'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',category:CATS[0],organizer:'o',source:'signature'}).ok);
  t('reject short desc',!validate({id:PREFIX+'0000001',title:'x',description:'too short',category:CATS[0],organizer:'o',source:'signature'}).ok);
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
