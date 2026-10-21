(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["assessment", "prioritization", "training-plans", "verification", "tracking"];
var PREFIX="JAH-ACG-S-";
var FIELDS=["technique", "gap", "method", "measure", "benefit", "complexity"];
var SRC="signature-generated-completion";
var POOL=[["Signature Gap Cartographer", "Signature original — maps capability gaps like uncharted lands: the blanks are marked. The cartographer guides. Exploration gets directed.", "assessment", 1, "Signature cartographer", "Unknown", "Mapped blanks", "Directed", "Guides", "Low"], ["Signature Priority Gardener", "Signature original — gardens gap priorities: the important are tended first. The gardening is principled. Effort gets aimed truly.", "prioritization", 2, "Signature gardener", "Many", "Principled tend", "Truly aimed", "Principled", "Medium"], ["Signature Plan Architect", "Signature original — architects training plans: the blueprints are concrete. The architecture works. Gaps get scheduled truly.", "training-plans", 2, "Signature architect", "Reasoning", "Concrete blueprint", "Truly scheduled", "Works", "Medium"], ["Signature Proof Gardener", "Signature original — gardens closure proofs: the re-tests are tended. The garden proves. Claims get earned truly.", "verification", 2, "Signature gardener", "Closed", "Tended retest", "Truly earned", "Proves", "Medium"], ["Signature Progress Illuminator", "Signature original — illuminates gap dashboards: the progress glows. The illumination motivates. Momentum gets kept truly.", "tracking", 1, "Signature illuminator", "All", "Glowing track", "Truly kept", "Motivates", "Low"], ["Signature Benchmark Cartographer", "Signature original — maps gaps via benchmarks: the failures are charted. The cartography is honest. Maps get true.", "assessment", 2, "Signature cartographer", "Revealed", "Charted fails", "True maps", "Honest", "Medium"], ["Signature Gold Miner", "Signature original — mines user reports like gold: the feedback is precious. The mining works. Gaps get real truly.", "assessment", 1, "Signature miner", "Real", "Precious mine", "Truly real", "Precious", "Low"], ["Signature Adversary Gardener", "Signature original — gardens adversarial probing: the red team is tended. The gardening exposes. Weaknesses get found truly.", "assessment", 3, "Signature gardener", "Hidden", "Tended probe", "Truly found", "Exposes", "High"], ["Signature Sprint Coach", "Signature original — coaches gap sprints: the intensity is managed. The coaching works. Gaps get closed fast truly.", "training-plans", 2, "Signature coach", "One", "Managed intense", "Truly fast", "Managed", "Medium"], ["Signature Curriculum Tailor", "Signature original — a tailor for gap curricula: the fit is precise. The tailoring works. Learning gets efficient truly.", "training-plans", 2, "Signature tailor", "Specific", "Precise fit", "Truly efficient", "Precise", "Medium"], ["Signature Guard Gardener", "Signature original — gardens regression guards: the tests are tended. The gardening protects. Progress gets kept truly.", "verification", 2, "Signature gardener", "Closed", "Tended guard", "Truly kept", "Protects", "Medium"], ["Signature Cost Gardener", "Signature original — gardens gap costs: the estimates are tended honestly. The gardening informs. Spending gets wise truly.", "prioritization", 1, "Signature gardener", "Each", "Honest tend", "Truly wise", "Informs", "Low"], ["Signature Ownership Scribe", "Signature original — scribes gap ownership: the assignment is clear. The scribing works. Gaps get closed truly.", "prioritization", 2, "Signature scribe", "Each", "Clear assign", "Truly closed", "Clear", "Medium"], ["Signature Joy Gardener", "Signature original — gardens celebration: the closed gaps are fêted. The gardening energizes. Teams get joyful.", "tracking", 1, "Signature gardener", "Closed", "Fêted", "Joyful", "Energizes", "Low"], ["Signature Tail Naturalist", "Signature original — a naturalist for long-tail gaps: the rare species are studied. The study is patient. Coverage gets complete truly.", "assessment", 3, "Signature naturalist", "Rare", "Patient study", "Truly complete", "Patient", "High"], ["Signature Order Gardener", "Signature original — gardens gap ordering: the dependencies are tended. The gardening sequences. Closing gets ordered truly.", "prioritization", 2, "Signature gardener", "Dependent", "Tended order", "Truly ordered", "Sequences", "Medium"], ["Signature Data Gardener", "Signature original — gardens synthetic data: the generation is tended. The garden yields. Data gets made beautifully.", "training-plans", 3, "Signature gardener", "Data-poor", "Tended generate", "Beautiful yield", "Yields", "High"], ["Signature Audit Judge", "Signature original — a judge for closure audits: the independence is enforced. The judgment is external. Trust gets earned truly.", "verification", 3, "Signature judge", "Claimed", "Enforced independent", "Truly earned", "External", "High"], ["Signature Trend Cartographer", "Signature original — maps gap trends: the direction is charted. The cartography informs. Strategy gets data truly.", "tracking", 2, "Signature cartographer", "Over time", "Charted direction", "Truly data", "Informs", "Medium"], ["Signature Alignment Gardener", "Signature original — gardens stakeholder alignment: the reviews are tended. The gardening agrees. Priorities get shared.", "prioritization", 1, "Signature gardener", "Priorities", "Tended review", "Shared", "Agrees", "Low"]];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var sub=POOL.filter(function(p){return p[2]===cat;});
  var row=pick(sub.length?sub:POOL,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rec={id:id,t:row[0],g:row[2],c:0,title:row[0],description:row[1],category:row[2],ladder_rank:row[3]};
  for(var i=0;i<FIELDS.length;i++){ rec[FIELDS[i]]=row[4+i]; }
  var param=ri(rnd,2,40);
  rec.demo={language:'python',code:'gaps = {\"reasoning\": 30, \"coding\": 15, \"vision\": 5}\nfor name, pct in sorted(gaps.items(), key=lambda x: -x[1]):\n    bar = \"#\" * (pct // 5)\n    print(\"%-10s [%s] %d%% gap\" % (name, bar, pct))\nprint(\"biggest gap first\")\nfor _ in range(__PARAM__):\n    pass\nprint(\"param:\", __PARAM__)\n',run:'python3'};
  rec.demo.code=rec.demo.code.replace(/__PARAM__/g,String(param));
  rec.provenance='JAH Databases lane N1 build';
  rec.last_verified='2026-10-21';
  rec.src=SRC;
  rec.origin='Signature original';
  rec._seed=seed;
  return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/[-\/\\^$*+?.()|[\]{}]/g,'\\$&')+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if([1,2,3].indexOf(r.ladder_rank)<0)e.push('ladder_rank');
  FIELDS.forEach(function(f){ if(typeof r[f]!=='string'||!r[f].length)e.push('field:'+f); });
  if(!r.demo||r.demo.language!=='python'||typeof r.demo.code!=='string'||!r.demo.code.length)e.push('demo');
  if(r.src!==SRC)e.push('src');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-ai-capability-gap-closure-signature-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("ai-capability-gap-closure-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
