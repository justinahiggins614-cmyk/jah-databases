(function(){'use strict';
/* Public Facial Expression Database generator — jahdb-facial-expression-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same records.
   src:"signature" = Signature-authored original (clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,fn){return r[(fn()*r.length)|0];}
var PREFIX='JAH-FACE-';
var LAST='2026-10-19';
var TITLES=["AU2 Outer Brow Raiser", "AU4 Brow Lowerer", "AU5 Upper Lid Raiser", "AU6 Cheek Raiser", "AU7 Lid Tightener", "AU9 Nose Wrinkler", "AU10 Upper Lip Raiser", "AU12 Lip Corner Puller", "AU15 Lip Corner Depressor", "AU17 Chin Raiser", "AU20 Lip Stretcher", "AU23 Lip Tightener", "AU24 Lip Pressor", "AU25 Lips Part", "AU26 Jaw Drop", "AU27 Mouth Stretch", "AU43 Eyes Closed", "Fear Face", "Anger Face", "Joy Face", "Sadness Face", "Disgust Face", "Surprise Face", "Contempt", "Microexpression Timing", "Expression Transitions", "Asymmetry of Deceit", "Eye Behavior Grammar", "FACS Intensity Scale", "AU1 Inner Brow Raiser"];
var DEFS=["Frontalis pars lateralis: outer brows lift.", "Corrugator: brows draw down and together.", "Levator palpebrae: upper lids raise, more sclera.", "Orbicularis oculi: the Duchenne marker of true smiles.", "Lids tighten without raising cheeks.", "Levator labii: disgust signal.", "Upper lip lifts, teeth show.", "Zygomaticus major: the smile muscle.", "Depressor anguli oris: sadness.", "Mentalis: chin boss pushes up.", "Risorius: lips stretch horizontally.", "Lips press and narrow.", "Lips pressed together firmly.", "Lips parted, teeth may show.", "Masseter relaxes: jaw drops.", "Jaw stretched open wide.", "Lids close; blink vs held differs.", "AU1+2+4+5+20+26: the full fear configuration.", "AU4+5+7+23: lowered brow, tight lids, pressed lips.", "AU6+12: Duchenne smile.", "AU1+4+15: inner brow up, corners down.", "AU9+15+16: nose wrinkle, lowered lip.", "AU1+2+5+26: raised brow, wide eyes, dropped jaw.", "Unilateral AU12 or AU14: the dimpler.", "Genuine microexpressions last 1/25 to 1/5 second.", "Emotions blend through neutral, rarely snap.", "Posed expressions are more asymmetric than felt ones.", "Gaze, blink rate and pupil tell the inner state.", "A-E intensity coding for every action unit.", "Frontalis pars medialis: inner brows lift."];
var GROUPS=["Action unit", "Coding", "Compound", "Performance", "Timing"];
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
window['JAHDB_GEN_facial_expression']={generate:generate};
})();
