(function(){'use strict';
/* Signature Board Games Database generator — jahdb-board-games-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled) */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-BOARD-';
var TOPICS=[["The Board Game Renaissance", "The 2010s boom; the caf\u00e9s."], ["Catan", "The gateway; the trades."], ["Ticket to Ride", "The family; the routes."], ["Pandemic", "The co-op; the legacy."], ["Gloomhaven", "The epic; the weight."], ["Wingspan", "The engine; the beauty."], ["Azul", "The abstract; the tiles."], ["The Eurogame Style", "The efficiency; the lack of luck."], ["The Ameritrash Style", "The theme; the dice."], ["Deck-Builders", "Dominion; the mechanic."], ["Worker Placement", "Agricola; the tension."], ["Legacy Games", "The permanence; the Risk."], ["Cooperative Games", "The teamwork; the quarterbacking."], ["Party Games", "The laughter; the categories."], ["Two-Player Games", "The duels; the best."], ["Solo Gaming", "The alone; the designs."], ["The Design Process", "The prototypes; the playtests."], ["Kickstarter's Role", "The funding; the bloat."], ["The FLGS", "The stores; the community."], ["Board Game Caf\u00e9s", "The venues; the model."], ["The Digital Adaptation", "The apps; the Tabletop Simulator."], ["Tournaments", "The competitive; the scene."], ["The Collector Market", "The OOP; the prices."], ["Teaching Games", "The explain; the art."], ["The 2025 Hits", "The new; the buzz."], ["Designing Your Own", "The print-and-play; the advice."], ["The Future", "The hybrid; the prediction."], ["The Classics", "Chess to Monopoly; the canon."], ["Tidebreakers: A Game of Harbor Rivalry", "Tidebreakers is a Signature-original board game for 2 to 4 players about rival harbor masters competing to dock the most valuable ships before the tide turns."], ["The Cartographer's Dilemma", "The Cartographer's Dilemma is a Signature-original cooperative game where players are mapmakers charting an island that rearranges itself each night."], ["Gears of the Guild", "Gears of the Guild is a Signature-original worker-placement game set in a clockwork city, where players are guild masters building ever more elaborate machines."], ["Night Market Barter", "Night Market Barter is a Signature-original trading game with no money: players swap goods in a bustling night market using only barter and bluff."], ["The Lighthouse Keepers", "The Lighthouse Keepers is a Signature-original cooperative game about maintaining a lighthouse through a century of storms, from 1850 to 1950."], ["Seedvault", "Seedvault is a Signature-original game about preserving crop diversity: players are seed guardians racing to bank the most varieties before blight and war destroy them."], ["The Diplomat's Ball", "The Diplomat's Ball is a Signature-original social deduction game set at a peace conference, where players are diplomats with secret agendas."], ["Ironwood Expedition", "Ironwood Expedition is a Signature-original exploration game where players lead expeditions into a forest of iron-hard trees seeking the legendary heartwood grove."], ["The Recipe Heist", "The Recipe Heist is a Signature-original heist game where rival chefs infiltrate each other's kitchens to steal signature recipes."], ["Constellation Draft", "Constellation Draft is a Signature-original abstract game where players draft stars and connect them into constellations for points."], ["The Last Library", "The Last Library is a Signature-original cooperative game about saving books from a slow apocalypse: players are librarians deciding what to preserve as the world winds down."], ["Monsoon Merchants", "Monsoon Merchants is a Signature-original pick-up-and-deliver game set on the Indian Ocean monsoon trade routes, where the winds dictate everything."], ["The Inventor's Workshop", "The Inventor's Workshop is a Signature-original engine-building game where players are Victorian inventors racing to patent the most world-changing devices."], ["Quarry Kings", "Quarry Kings is a Signature-original tile-laying game about rival stonecutters dividing a mountainside quarry."], ["The Starlight Census", "The Starlight Census is a Signature-original set-collection game where players are astronomers cataloging the night sky before light pollution arrives."]];
var ANGLES=['overview','detailed','examples','faq','history','applications'];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function generate(seed,opts){
  var s=prng(seed);
  var ti=(s()*TOPICS.length)|0, ai=(s()*ANGLES.length)|0;
  var topic=TOPICS[ti], angle=ANGLES[ai];
  var id=PREFIX+pad(seed);
  var title=topic[0]+' ('+angle+')';
  var desc=topic[1];
  var content=topic[0]+' \u2014 '+topic[1];
  return {
    id:id, title:title, description:desc, genre:angle,
    type:'board games exploration', content:content, content_completeness:'stub',
    stub_note:'Topic stub: the topic title and its one-line brief are real; the full guide article is not yet written. This record does not present shell text as a complete guide.',
    demo:null, src:'signature', _seed:seed
  };
}
function validate(r){
  var errs=[];
  if(!r.id)errs.push('missing id');
  if(!r.title)errs.push('missing title');
  if(!r.content||r.content.length<50)errs.push('content too short');
  return {ok:errs.length===0, errors:errs};
}
function driftCheck(rec,sample){
  // Simple: check for exact title duplicates in sample
  for(var i=0;i<sample.length;i++){if(sample[i].t===rec.title)return {ok:false,errors:['duplicate title']};}
  return {ok:true,errors:[]};
}
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('board-games',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();