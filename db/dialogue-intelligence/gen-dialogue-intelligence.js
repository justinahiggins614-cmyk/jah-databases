(function(){'use strict';
/* Signature Dialogue Intelligence Database generator — jahdb-dialogue-intelligence-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same records.
   src:"signature" = Signature-authored original (clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,fn){return r[(fn()*r.length)|0];}
var PREFIX='JAH-DIALG-';
var LAST='2026-10-19';
var TITLES=["The Evasion", "Status Transaction", "The Confession", "Comic Rhythm", "Threat Without Threats", "The Apology", "Flirtation Duel", "Interrogation", "The Goodbye", "Workplace Banter", "Family Dinner", "Negotiation", "The Pitch", "Breaking News", "The Lecture", "Lovers Quarrel", "The Pep Talk", "Villain Monologue", "The Toast", "Phone Call Tension", "Whispered Plot", "The Interview", "Eulogy", "The Warning", "Reunion", "The Bargain", "Seduction of Ideas", "The Debrief", "Last Words", "Subtext Exchange"];
var DEFS=["A character dodges a direct question three ways.", "High-status and low-status trade places mid-scene.", "Truth told sideways, in pieces.", "Setup, heighten, button.", "Menace delivered as courtesy.", "A bad apology vs a real one.", "Wit as courtship.", "Questions as weapons.", "Everything unsaid, said.", "Jargon as affection.", "Old roles, new wounds.", "Numbers with feelings.", "Selling the impossible.", "Information under pressure.", "Teaching as drama.", "The real fight under the dishes.", "Belief transferred.", "The philosophy of the antagonist.", "Praise with an edge.", "Half a conversation, full tension.", "Conspiracy in plain sight.", "Performance of the self.", "Grief with structure.", "Danger delivered gently.", "Time collapsed into minutes.", "Souls on the table.", "Recruiting a believer.", "Aftermath accounting.", "Final lines that reframe everything.", "Two characters negotiate power while discussing something trivial."];
var GROUPS=["Dialogue"];
function demoFor(title,defn){return '/* '+title+' \u2014 runnable demo. Save as demo.js and run: node demo.js */\n\'use strict\';\nconsole.log('+JSON.stringify(title)+');\nconsole.log('+JSON.stringify(defn)+');';}
function generate(seed,count){
  var rnd=prng(seed*7919+13),rows=[],n=Math.max(1,Math.min(50,count||5));
  for(var i=0;i<n;i++){
    var ti=(rnd()*TITLES.length)|0, gi=(rnd()*GROUPS.length)|0;
    var title=TITLES[ti], defn=DEFS[ti%DEFS.length], grp=GROUPS[gi];
    var desc=defn.length>170?defn.slice(0,170)+'...':defn;
    var id=PREFIX+String(seed*1000+i+1).padStart(6,'0');
    var demo=demoFor(title,defn);
    rows.push({id:id,t:title,title:title,g:grp,genre:grp,description:desc,definition:defn,
      content:{generated:true,seed:seed,variant:i+1,topic:title,key_points:['Define the standard','Apply per production','Verify at the gate']},
      program_demo:demo,demo:{kind:'program',title:title+' \u2014 demo',program:demo,language:'javascript'},
      source:'signature-original',last_verified:LAST,src:'signature'});
  }
  return rows;
}
window['JAHDB_GEN_dialogue_intelligence']={generate:generate};
})();
