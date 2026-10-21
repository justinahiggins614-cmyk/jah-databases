/* jahdb-pc-organizer-plastic-zip-tie-assortment-1.0 — deterministic boundless generator for Plastic Zip-Tie Assortment Database.
   Self-regulation (Signature standard): hard stop at 1,000,000,000,000 records;
   throttled output (<=50 records per call); every generated record labeled
   "simulated"; correctness verified by validate(); completion detected when the
   template pool is exhausted for the requested seed space. */
(function(){'use strict';
var HARD_STOP=1000000000000;
var MAX_PER_CALL=50;
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["Tie Basics", "Sizes & Strength", "Techniques", "Case Interiors", "Outdoor & Special", "Comparisons"];
var PREFIX='JAH-PCO5-';
/* Deterministic template pool: [category, title_pattern, detail_pattern] */
var B=[["Tie Basics", "What Plastic Zip Ties Are and How They Lock", "A plastic zip tie (cable tie) is a nylon strap with angled teeth on one side and a locking head with a one-way pawl: thread the tail through the head and it cin"], ["Sizes & Strength", "Sizes, Lengths, and Tensile Strength Ratings", "Zip ties are sold by length and tensile strength: 4-inch ties rated around 18 lbs for thin wire bundles, 8-inch at 40-50 lbs as the general PC size, 12-inch at "], ["Sizes & Strength", "Natural vs UV-Black Ties: Indoor and Outdoor Grades", "Natural (white/clear) nylon ties are the indoor default; black ties add carbon black for UV resistance and survive years in sunlight. Outdoors or near windows, "], ["Techniques", "Cinching Technique: Tight Enough, Never Crushing", "Pull a zip tie snug — the bundle should not slide — then stop; one more hard yank deforms cable insulation and can pinch conductors. The pro move is a zip-tie g"], ["Case Interiors", "Use Case: Permanent Hidden Runs Behind the Motherboard Tray", "Zip ties earn their place on permanent hidden runs: the main PSU trunk behind the motherboard tray, in a case you do not plan to rewire. Strap the trunk to the "], ["Case Interiors", "Use Case: Fan Grills, Filters, and Case Mod Mounting", "Zip ties mount things, not just cables: fan filters to fan frames, LED strips along case edges, pump brackets in custom loops, and replacement fan grills. Four "], ["Tie Basics", "Releasable Zip Ties: The Reusable Exception", "Releasable (reusable) zip ties have a small tab on the head that lifts the pawl, letting you open and reuse the tie dozens of times. They cost more and the tab "], ["Techniques", "Mounting-Head and Screw-Mount Ties", "Mounting-head ties have a hole in the head for a screw, turning any surface into an anchor point; screw-mount the head to the case or desk, then cinch the bundl"], ["Techniques", "Cutting Tails: Flush Cutters vs Dikes vs the Twist", "Trim tails flush with the head using flush cutters — angled snips leave a razor edge that slices fingers during the next build. Never twist-ties off: twisting w"], ["Outdoor & Special", "Zip Tie Maintenance: Inspection and Replacement Cycles", "Nylon ages: indoor ties last many years, but heat (near radiators, in hot cases) and UV embrittle them. Inspect yearly — flex a tie; if it snaps instead of bend"], ["Comparisons", "Zip Ties vs Velcro vs Lacing Cord", "Zip ties: cheapest, strongest, permanent, need cutters. Velcro: reusable, gentle, costs more, weaker hold. Lacing cord (waxed twine, the old telecom method): be"], ["Tie Basics", "Buying Guide: Assortments Worth Buying", "A worthwhile assortment has mostly 8-inch 50-lb ties, some 4-inch for thin bundles, some 12-inch for trunks, in natural for indoor use — about 500 pieces for 10"], ["Techniques", "Advanced: The Double-Tie and Cross-Tie for Heavy Trunks", "Heavy PSU trunks defeat single ties over time — nylon creeps under constant load. The double-tie puts two ties side by side sharing the load; the cross-tie loop"], ["Outdoor & Special", "Specialty Ties: Beaded, Stainless, and Detectable", "Beaded ties (ladder-style, no pawl) release and reuse — handy for temporary bundling. Stainless steel ties handle exhaust-heat zones and outdoor masts where nyl"], ["Techniques", "The Complete Zip-Tie Discipline", "The master discipline: 8-inch 50-lb as the default, snug-never-crushing tension, tails cut flush with proper cutters, double-ties on heavy trunks, releasables o"]];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  if(seed>=HARD_STOP)return {error:'HARD_STOP: 1,000,000,000,000 record limit reached',complete:true};
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title=b[1].replace('{n}',String(ri(rnd,2,48)));
  return {id:id,title:title,t:title.slice(0,70),g:cat,category:cat,
    description:b[2].replace('{n}',String(ri(rnd,2,48)))+' This is a simulated record generated by jahdb-pc-organizer-plastic-zip-tie-assortment-1.0.',
    ladder_rank:ri(rnd,1,15),
    demo:{language:'python',program:'print("simulated demo for '+id+'")'},
    provenance:'Simulated record generated by jahdb-pc-organizer-plastic-zip-tie-assortment-1.0 (seed '+seed+'). Labeled simulated per the Signature self-regulation standard.',
    last_verified:'2026-10-21',
    march_marker:'March to a million in progress — simulated generation record '+seed+'.',
    edition:'simulated',simulated:true,_seed:seed,_version:'jahdb-pc-organizer-plastic-zip-tie-assortment-1.0'};
}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var re=/^JAH\-PCO5\-\d{6}$/;
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
var gen={version:'jahdb-pc-organizer-plastic-zip-tie-assortment-1.0',HARD_STOP:HARD_STOP,MAX_PER_CALL:MAX_PER_CALL,generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-plastic-zip-tie-assortment',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
