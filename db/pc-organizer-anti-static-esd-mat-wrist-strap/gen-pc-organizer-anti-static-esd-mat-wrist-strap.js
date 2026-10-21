/* jahdb-pc-organizer-anti-static-esd-mat-wrist-strap-1.0 — deterministic boundless generator for Anti-Static ESD Mat &amp; Wrist Strap Database.
   Self-regulation (Signature standard): hard stop at 1,000,000,000,000 records;
   throttled output (<=50 records per call); every generated record labeled
   "simulated"; correctness verified by validate(); completion detected when the
   template pool is exhausted for the requested seed space. */
(function(){'use strict';
var HARD_STOP=1000000000000;
var MAX_PER_CALL=50;
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["ESD Basics", "Mat Specs", "Wrist Strap Specs", "Workstation Setup", "Testing", "Comparisons"];
var PREFIX='JAH-PCO2-';
/* Deterministic template pool: [category, title_pattern, detail_pattern] */
var B=[["ESD Basics", "What ESD Is and Why It Kills PC Components", "Electrostatic discharge is the spark you feel touching a doorknob in winter — thousands of volts from a charge your body picked up walking across carpet. Modern"], ["ESD Basics", "How an ESD Mat Drains Charge: Dissipative Surfaces", "An ESD mat is made from a dissipative material — not a conductor, not an insulator, but in between, with surface resistivity typically between 10^6 and 10^9 ohm"], ["Mat Specs", "Mat Sizes, Layers, and What to Buy", "Common bench mats run 24 by 36 inches — enough for a motherboard, tools, and parts — with smaller 18 by 24 inch mats for tight desks. Two-layer mats (dissipativ"], ["Wrist Strap Specs", "Wrist Strap Anatomy: Band, Cord, and the 1-Megohm Resistor", "A wrist strap has three parts: an adjustable band (fabric with conductive fibers or a metal plate) that must touch bare skin, a coiled cord with a 10 mm snap, a"], ["Workstation Setup", "The Common Ground Point: Tying Mat, Strap, and Bench Together", "Mat and strap must share one ground — the common point ground, usually a small bar or block with multiple 10 mm snaps. The ground cord then runs to a verified e"], ["Workstation Setup", "Setting Up a Complete ESD-Safe Build Bench", "Lay the mat flat on the bench with the snap at the back edge, plug the mat's ground cord into the common point, and snap the wrist strap cord to the same point."], ["ESD Basics", "ANSI/ESD S20.20: The Standard Behind the Gear", "ANSI/ESD S20.20 is the industry standard for ESD control programs, used by electronics manufacturers worldwide. It requires wrist straps to test under 35 megohm"], ["Testing", "Testing Your Strap and Mat: What Passes and What Fails", "A wrist-strap tester checks the whole skin-to-ground path in one second: green means under the limit, red means the band, cord, or resistor has failed. Test by "], ["Workstation Setup", "Use Case: Handling a CPU and RAM Safely", "CPUs and RAM are the most ESD-sensitive parts in a build. The safe sequence: strap on and tested, open the motherboard box on the mat, ground yourself by touchi"], ["Workstation Setup", "Use Case: GPU Installs and Long Build Sessions", "GPUs are big, expensive, and handled for minutes at a time — prime ESD victims. Keep the strap on for the whole session, rest the GPU on the mat (not the desk) "], ["Maintenance", "Maintenance: Cleaning Mats Without Killing the Dissipative Layer", "Clean mats with a damp cloth and a cleaner rated for ESD surfaces — harsh solvents and silicone sprays coat the dissipative layer and raise its resistance into "], ["ESD Basics", "Common ESD Mistakes That Void All Your Protection", "The classic mistakes: strap over a shirt sleeve, parts sitting on the bare bench instead of the mat, the mat's ground cord unplugged, standing on carpet while h"], ["Comparisons", "ESD Mat vs Anti-Static Bag vs ESD Flooring", "The mat protects the bench surface where parts rest; anti-static bags protect parts in storage and transit (insides only); ESD flooring and heel straps protect "], ["Comparisons", "Wrist Strap Alternatives: Heel Straps, Smocks, and Continuous Monitors", "Heel grounders strap to the shoe and drain through ESD flooring — the choice when you must stand and move. ESD smocks with conductive threads keep clothing from"], ["Workstation Setup", "The Complete ESD-Safe Build Station Blueprint", "The master setup: a two-layer 24x36 dissipative mat with its snap at the back, a common point ground bar bonded to verified earth, a coiled wrist strap with 1-m"]];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  if(seed>=HARD_STOP)return {error:'HARD_STOP: 1,000,000,000,000 record limit reached',complete:true};
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title=b[1].replace('{n}',String(ri(rnd,2,48)));
  return {id:id,title:title,t:title.slice(0,70),g:cat,category:cat,
    description:b[2].replace('{n}',String(ri(rnd,2,48)))+' This is a simulated record generated by jahdb-pc-organizer-anti-static-esd-mat-wrist-strap-1.0.',
    ladder_rank:ri(rnd,1,15),
    demo:{language:'python',program:'print("simulated demo for '+id+'")'},
    provenance:'Simulated record generated by jahdb-pc-organizer-anti-static-esd-mat-wrist-strap-1.0 (seed '+seed+'). Labeled simulated per the Signature self-regulation standard.',
    last_verified:'2026-10-21',
    march_marker:'March to a million in progress — simulated generation record '+seed+'.',
    edition:'simulated',simulated:true,_seed:seed,_version:'jahdb-pc-organizer-anti-static-esd-mat-wrist-strap-1.0'};
}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var re=/^JAH\-PCO2\-\d{6}$/;
  if(!re.test(r.id||''))e.push('id');
  if(r.title!==undefined&&(typeof r.title!=='string'||!r.title.length))e.push('title');
  if(typeof r.description!=='string'||r.description.length<20)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=15))e.push('ladder_rank');
  if(r.simulated!==true)e.push('simulated-must-be-true');
  if(r._seed===undefined||r._seed>=HARD_STOP)e.push('seed');
  return {ok:!e.length,errors:e,complete:r._seed>=B.length*1000};
}
function driftCheck(rec,sample){
  var e=[];
  (sample||[]).forEach(function(s){ if(s&&s.id===rec.id)e.push('duplicate of archive record '+s.id); });
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-pc-organizer-anti-static-esd-mat-wrist-strap-1.0',HARD_STOP:HARD_STOP,MAX_PER_CALL:MAX_PER_CALL,generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-anti-static-esd-mat-wrist-strap',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
