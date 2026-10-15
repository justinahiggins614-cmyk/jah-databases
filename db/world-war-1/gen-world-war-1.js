(function(){'use strict';
/* World War 1 Database generator — jahdb-world-war-1-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-WW1-';
var TOPICS=[["The First World War", "The 1914-1918 global conflict, the Great War."], ["The Assassination", "The 1914 killing of Archduke Franz Ferdinand that sparked the war."], ["The Allies", "Britain, France, Russia, and later the United States."], ["The Central Powers", "Germany, Austria-Hungary, and the Ottoman Empire."], ["Trench Warfare", "The muddy stalemate of the Western Front."], ["The Western Front", "The long line of trenches across France and Belgium."], ["The Schlieffen Plan", "Germany's strategy of a quick strike through Belgium."], ["The United States Enters", "America's 1917 entry tipping the balance."], ["The Treaty of Versailles", "The 1919 peace settlement ending the war."], ["The League of Nations", "The postwar organization for keeping peace."], ["Tanks", "The new armored vehicles debuting in the war."], ["War Planes", "Aircraft first used widely for combat."], ["Poison Gas", "The chemical weapons of the trenches."], ["The Christmas Truce", "The informal 1914 ceasefire along the front."], ["Gallipoli", "The failed Allied campaign in Turkey."], ["The Somme", "The bloody 1916 battle of the Western Front."], ["Verdun", "The long grinding French battle."], ["The Russian Revolution", "The upheaval that took Russia out of the war."], ["Armistice Day", "November eleventh, when the guns fell silent."], ["Woodrow Wilson", "The American president of Fourteen Points fame."], ["Kaiser Wilhelm II", "The German emperor of the war years."], ["Collapse of Empires", "The fall of the Russian, Austro-Hungarian, and Ottoman empires."], ["War at Sea", "Battleships, blockades, and submarines."], ["The Home Front", "How civilians supported and suffered in the war."], ["War Poetry", "The verses of soldiers like Wilfred Owen."], ["New Nations", "The states born from the peace settlement."], ["The War's Cost", "The millions lost and the world transformed."], ["Lessons of the War", "What the Great War taught the world."]];
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
    type:'world war 1 record', content:content, content_completeness:'stub',
    stub_note:'Topic stub: the topic title and its one-line brief are real; the full guide article is not yet written. This record does not present shell text as a complete guide.',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('world-war-1',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();