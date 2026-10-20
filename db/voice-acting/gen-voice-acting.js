(function(){'use strict';
/* Public Voice Acting Database generator — jahdb-voice-acting-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same records.
   src:"signature" = Signature-authored original (clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,fn){return r[(fn()*r.length)|0];}
var PREFIX='JAH-VACT-';
var LAST='2026-10-19';
var TITLES=["Cold Read Skill", "Character Voice Build", "Emotional Recall Honest", "Subtext Playing", "Microphone Technique", "Popping Control", "Sibilance Care", "Pacing Variety", "Pause Power", "Whisper Acting", "Shout Safety", "Crying Honest", "Laughing Real", "Aging the Voice", "Child Voice Honest", "Accent Integrity", "Creature Voices", "Narration Warmth", "Commercial Energy", "Villain Delight", "Hero Doubt", "Romance Breath", "Horror Dread Voice", "Comedy Timing", "Doubling Voices", "ADR Matching", "Walla Groups", "Efforts and Grunts", "Master Voice Bible", "Breath Control"];
var DEFS=["Truth on first sight.", "Find the voice in the body.", "Feeling without forcing.", "Say the lines, play the want.", "Distance is dynamics.", "Plosives tamed.", "Esses gentle.", "Speed tells story.", "Silence acts.", "Intimacy without mumbling.", "Loud without damage.", "Tears without pushing.", "Laughter from the body.", "Years in the throat.", "Young without cartoon.", "Accents with respect.", "Non-human truth.", "Storyteller presence.", "Sell with smile.", "Evil enjoys.", "Strength with cracks.", "Intimacy in air.", "Fear in the throat.", "Rhythm is everything.", "Many characters, one actor.", "Match the picture.", "Crowd voices.", "Physical truth.", "One voice per character.", "Diaphragm support for long lines."];
var GROUPS=["Technique"];
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
window['JAHDB_GEN_voice_acting']={generate:generate};
})();
