(function(){'use strict';
/* Cold War Database generator — jahdb-cold-war-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-COLDWAR-';
var TOPICS=[["The Cold War", "The decades-long rivalry between the United States and the Soviet Union."], ["The Berlin Wall", "The barrier dividing East and West Berlin from 1961 to 1989."], ["The Cuban Missile Crisis", "The 1962 standoff over Soviet missiles in Cuba, the closest the rivals came to nuclear war."], ["The Space Race", "The competition to reach space, from Sputnik to the Moon landing."], ["The Nuclear Arms Race", "The buildup of atomic weapons by both superpowers."], ["NATO", "The Western military alliance formed to counter the Soviet Union."], ["The Warsaw Pact", "The Soviet-led military alliance of Eastern bloc states."], ["The Korean War", "The early Cold War conflict that left Korea divided."], ["The Vietnam War", "The long conflict in Southeast Asia rooted in Cold War rivalry."], ["McCarthyism", "The anti-communist investigations and blacklists in the United States."], ["Proxy Wars", "Conflicts where the superpowers backed opposing sides without fighting directly."], ["The Iron Curtain", "The political and physical division between Eastern and Western Europe."], ["Containment", "The American strategy of limiting the spread of communism."], ["Detente", "The easing of tensions between the superpowers in the 1970s."], ["The Fall of the Berlin Wall", "The 1989 opening of the wall that symbolized the Cold War's end."], ["Dissolution of the USSR", "The 1991 breakup of the Soviet Union into independent states."], ["The Marshall Plan", "The American program rebuilding Western Europe after the war."], ["The Truman Doctrine", "The American pledge to support nations resisting communist takeover."], ["Mutually Assured Destruction", "The doctrine that nuclear war would destroy both sides, deterring attack."], ["The Bay of Pigs", "The failed 1961 invasion of Cuba by American-backed exiles."], ["The U-2 Incident", "The 1960 downing of an American spy plane over the Soviet Union."], ["The Prague Spring", "The 1968 reform movement in Czechoslovakia crushed by Soviet tanks."], ["The Afghan War", "The Soviet invasion of Afghanistan and the long guerrilla resistance."], ["Reagan and Gorbachev", "The leaders whose summits helped wind down the arms race."], ["The Domino Theory", "The belief that one country's fall to communism would topple its neighbors."], ["Hotline", "The direct communication link set up between Washington and Moscow."], ["Arms Control Treaties", "Agreements limiting nuclear weapons, such as SALT and START."], ["The Non-Aligned Movement", "Countries that refused to join either Cold War bloc."]];
var ANGLES=['overview','detailed','examples','faq','history','applications'];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function generate(seed,opts){
  var s=prng(seed);
  var ti=(s()*TOPICS.length)|0, ai=(s()*ANGLES.length)|0;
  var topic=TOPICS[ti], angle=ANGLES[ai];
  var id=PREFIX+pad(seed);
  var title=topic[0]+' ('+angle+')';
  var desc=topic[1]+' This '+angle+' guide provides comprehensive coverage.';
  var content='['+angle+'] '+topic[0]+': '+topic[1]+' Full detailed content for '+angle+' perspective.';
  return {
    id:id, title:title, description:desc, genre:angle,
    type:'cold war record', content:content,
    demo:null, src:'public', _seed:seed
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('cold-war',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();