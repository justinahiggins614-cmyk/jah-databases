(function(){'use strict';
/* Public Human Anatomy Database generator — jahdb-human-anatomy-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same records.
   src:"signature" = Signature-authored original (clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,fn){return r[(fn()*r.length)|0];}
var PREFIX='JAH-ANAT-';
var LAST='2026-10-19';
var TITLES=["Heroic Eight-Head Canon", "Child Proportions", "Shoulder Width Rule", "Arm Span Equals Height", "Hand Proportion", "Foot Proportion", "Contrapposto Stance", "Spine Curves", "Pelvis as Bowl", "Ribcage Ovoid", "Skull Landmarks", "Eye Placement", "Nose Thirds", "Mouth Placement", "Neck Cylinder", "Shoulder Girdle", "Arm Segments", "Leg Segments", "Torso Twist Range", "Weight Distribution Sitting", "Hand Articulation", "Facial Planes", "Age Markers", "Muscle Groups Major", "Fat Distribution", "Contrapposto Seated", "Forced Perspective Limbs", "Silhouette Read", "Anatomy for Animation", "Head-Unit Canon"];
var DEFS=["Idealized figures use 8 heads for heroic elongation.", "Children are 5-6 heads tall with large heads.", "Male shoulders span about 2 head-widths; female about 1.8.", "Fingertip to fingertip approximates total height.", "The hand is about 0.85 head-heights; the face from chin to hairline equals hand length.", "The foot is about 1 head long.", "Weight on one leg: the classic S-curve of relaxed standing.", "Cervical lordosis, thoracic kyphosis, lumbar lordosis.", "The pelvis tilts; it is the root of posture.", "The ribcage is an egg tilted forward, narrower at top.", "Brow ridge, cheekbones, jaw angle define the head.", "Eyes sit on the midline of the head, one eye-width apart.", "The face divides into three equal thirds.", "The mouth sits one-third down from nose base to chin.", "The neck is a tapered cylinder, thicker at the base.", "Clavicles and scapulae float over the ribcage.", "Upper arm, forearm, hand: the forearm is slightly shorter.", "Thigh and shin with the knee as hinge.", "The torso rotates about 45 degrees each way.", "Seated weight rests on the sit bones.", "27 bones: the hand is the most expressive tool.", "The face is built from interlocking planes.", "Age reads in skin, posture, and proportion shifts.", "Deltoids, pectorals, abdominals, quadriceps, calves define the surface.", "Fat softens landmarks differently by sex and age.", "Seated figures still show weight shifts.", "Foreshortened limbs compress toward the viewer.", "A readable silhouette identifies the character instantly.", "Rigging follows the same landmarks.", "The adult figure measures 7.5 heads tall; the head is the master unit."];
var GROUPS=["Anatomy", "Animation", "Design", "Drawing", "Motion", "Posture", "Proportions"];
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
window['JAHDB_GEN_human_anatomy']={generate:generate};
})();
