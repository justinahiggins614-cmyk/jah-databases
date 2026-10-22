(function(){'use strict';
/* The Performance Enhancers Reference Database generator - jahdb-performance-enhancers-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   HARD STOP: 10^15 records (one quadrillion) or genuine completion, whichever comes first.
   Generator ladder: simple -> competitive -> mix-and-match -> unmade -> top-notch -> future-grade -> god-mode.
   Throttled: minimum 5ms between generations; max 50 per batch.
   Public edition: generates reference-format records from the DOCUMENTED topic pool only -
   never invents new substances, dosages, or effects. */
var HARD_STOP = 1e15;
var THROTTLE_MS = 5;
var MAX_BATCH = 50;
var lastGen = 0;
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-PEF-';
var LADDER=['simple','competitive','mix-and-match','unmade','top-notch','future-grade','god-mode'];
var TOPICS=[["Caffeine", "Documented ergogenic aid: Caffeine. The most studied legal performance enhancer: improves alertness, reaction time, endurance performance, a", "Stimulant / ergogenic aid"], ["Creatine monohydrate", "Documented ergogenic aid: Creatine monohydrate. Raises muscle phosphocreatine stores, improving short-burst power, sprint repeatability, and", "Muscle energy / strength"], ["Beta-alanine", "Documented ergogenic aid: Beta-alanine. Buffers acid in working muscles, delaying fatigue in efforts lasting 1-4 minutes - rowing, swimming ", "Muscular endurance buffer"], ["L-citrulline", "Documented ergogenic aid: L-citrulline. Boosts nitric oxide, widening blood vessels: improves high-intensity endurance, reduces soreness, an", "Nitric oxide / blood flow"], ["Dietary nitrate (beetroot juice)", "Documented ergogenic aid: Dietary nitrate (beetroot juice). Lowers the oxygen cost of exercise, improving time-trial and endurance performan", "Oxygen efficiency"], ["Sodium bicarbonate (baking soda)", "Documented ergogenic aid: Sodium bicarbonate (baking soda). Buffers blood acidity during all-out efforts of 1-7 minutes - track sprints, swi", "Acid buffer"], ["Whey protein", "Documented ergogenic aid: Whey protein. Fast-digesting complete protein supporting muscle repair and growth after resistance training.", "Protein / recovery"], ["Casein protein", "Documented ergogenic aid: Casein protein. Slow-digesting protein that feeds muscles overnight; supports recovery and reduces muscle breakdow", "Protein / recovery"], ["Taurine", "Documented ergogenic aid: Taurine. Supports cellular hydration and calcium handling in muscle; modest endurance and reduced muscle-damage si", "Amino acid / cellular support"], ["L-tyrosine", "Documented ergogenic aid: L-tyrosine. Precursor to dopamine and norepinephrine; helps maintain focus and decision-making under stress, sleep", "Amino acid / focus"], ["Ashwagandha (Withania somnifera)", "Documented ergogenic aid: Ashwagandha (Withania somnifera). May improve strength, muscle size, testosterone levels, stress hormones, and sle", "Adaptogen"], ["Rhodiola rosea", "Documented ergogenic aid: Rhodiola rosea. May reduce perceived exertion and fatigue and support endurance under stress.", "Adaptogen"], ["Beta-hydroxy-beta-methylbutyrate (HMB)", "Documented ergogenic aid: Beta-hydroxy-beta-methylbutyrate (HMB). May reduce muscle breakdown during intense training blocks and support str", "Muscle preservation"], ["Fish oil (omega-3 EPA/DHA)", "Documented ergogenic aid: Fish oil (omega-3 EPA/DHA). May reduce exercise-induced muscle soreness and support joint, heart, and brain health", "Recovery / inflammation"], ["Vitamin D3 (for athletes)", "Documented ergogenic aid: Vitamin D3 (for athletes). Adequate vitamin D supports muscle function, bone health, immunity, and possibly reduce", "Micronutrient / performance support"], ["Iron (for deficient athletes)", "Documented ergogenic aid: Iron (for deficient athletes). Restores oxygen-carrying capacity and endurance in iron-deficient athletes, especia", "Micronutrient"], ["Magnesium", "Documented ergogenic aid: Magnesium. Supports muscle relaxation, sleep quality, and energy metabolism; many athletes fall short of intake.", "Micronutrient / recovery"], ["Carbohydrate gels and drinks", "Documented ergogenic aid: Carbohydrate gels and drinks. The foundational endurance enhancer: maintains blood sugar and spares muscle glycoge", "Fuel / endurance"], ["Electrolyte drinks", "Documented ergogenic aid: Electrolyte drinks. Maintains hydration and blood sodium, preventing cramps and dangerous hyponatremia in enduranc", "Hydration"], ["Tart cherry juice", "Documented ergogenic aid: Tart cherry juice. May reduce muscle soreness and improve sleep quality via natural melatonin and anti-inflammator", "Recovery"], ["Curcumin (turmeric extract)", "Documented ergogenic aid: Curcumin (turmeric extract). May reduce exercise-induced inflammation and soreness; studied in athletes and arthri", "Recovery / inflammation"], ["Coenzyme Q10 (CoQ10)", "Documented ergogenic aid: Coenzyme Q10 (CoQ10). Supports mitochondrial energy production; may reduce statin-related muscle symptoms and supp", "Cellular energy"], ["L-carnitine", "Documented ergogenic aid: L-carnitine. Shuttles fatty acids into mitochondria; may modestly support recovery and fat metabolism with chronic", "Fat metabolism"], ["Alpha-GPC", "Documented ergogenic aid: Alpha-GPC. Choline donor that may support power output and focus; studied in resistance exercise.", "Choline / focus"], ["Betaine (trimethylglycine)", "Documented ergogenic aid: Betaine (trimethylglycine). May support power output and cellular hydration during resistance training.", "Power / hydration"], ["Collagen peptides", "Documented ergogenic aid: Collagen peptides. May support tendon and joint health and reduce joint pain in athletes.", "Joint / connective tissue"], ["Ginseng (Panax)", "Documented ergogenic aid: Ginseng (Panax). Traditionally used for stamina and fatigue resistance; modest modern evidence.", "Adaptogen"], ["Cordyceps (fungal)", "Documented ergogenic aid: Cordyceps (fungal). Traditionally used for stamina; early studies suggest possible oxygen-utilization benefits.", "Endurance (traditional)"], ["WADA Prohibited List: anabolic agents (S1)", "Doping reference entry: WADA Prohibited List: anabolic agents (S1). Doping reference: anabolic androgenic steroids raise muscle mass and str", "anti-doping reference"], ["WADA Prohibited List: peptide hormones and growth factors (S2)", "Doping reference entry: WADA Prohibited List: peptide hormones and growth factors (S2). Doping reference: erythropoietin (EPO), human growth", "anti-doping reference"], ["WADA Prohibited List: beta-2 agonists (S3)", "Doping reference entry: WADA Prohibited List: beta-2 agonists (S3). Doping reference: asthma medicines such as salbutamol are permitted by i", "anti-doping reference"], ["WADA Prohibited List: hormone and metabolic modulators (S4)", "Doping reference entry: WADA Prohibited List: hormone and metabolic modulators (S4). Doping reference: aromatase inhibitors, anti-estrogens,", "anti-doping reference"], ["WADA Prohibited List: diuretics and masking agents (S5)", "Doping reference entry: WADA Prohibited List: diuretics and masking agents (S5). Doping reference: diuretics are prohibited at all times bec", "anti-doping reference"], ["WADA Prohibited List: stimulants (S6)", "Doping reference entry: WADA Prohibited List: stimulants (S6). Doping reference: amphetamines, cocaine, and high-dose ephedrine are prohibit", "anti-doping reference"], ["WADA Prohibited List: narcotics (S7)", "Doping reference entry: WADA Prohibited List: narcotics (S7). Doping reference: heroin, morphine, fentanyl, and similar narcotics are prohib", "anti-doping reference"], ["Therapeutic Use Exemptions (TUEs)", "Doping reference entry: Therapeutic Use Exemptions (TUEs). A TUE lets an athlete use a prohibited medicine for a genuine diagnosed condition", "anti-doping reference"], ["Supplement contamination and strict liability", "Doping reference entry: Supplement contamination and strict liability. Athletes are strictly liable for whatever is in their body: a contami", "anti-doping reference"], ["How to read a performance enhancer entry", "Doping reference entry: How to read a performance enhancer entry. Each entry follows the same layout: substance name, category, the document", "anti-doping reference"]];
var ANGLES=['overview','dosage-focus','effects-focus','warnings-focus','interactions-focus','faq'];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function throttled(){
  var now=Date.now();
  if(now-lastGen<THROTTLE_MS){var wait=THROTTLE_MS-(now-lastGen);var t0=Date.now();while(Date.now()-t0<wait){}}
  lastGen=Date.now();
}
function generate(seed,opts){
  if(seed>HARD_STOP)return null;
  throttled();
  opts=opts||{};
  var s=prng(seed);
  var stage=LADDER[(s()*LADDER.length)|0];
  var topic=opts.topic||null, base=null;
  if(topic){
    for(var i=0;i<TOPICS.length;i++){if(TOPICS[i][0].toLowerCase().indexOf(String(topic).toLowerCase().slice(0,24))>=0){base=TOPICS[i];break;}}
  }
  var id=PREFIX+pad(seed);
  if(!base){
    var bt=String(topic||'reference brief').slice(0,80);
    return {id:id,title:'Reference brief: '+bt+' ('+stage+')',
      description:'A structured brief of what a documented reference entry on this topic would cover. Topics enter the archive only after documentation from public sources.',
      genre:'reference brief',type:'performance enhancer record',stage:stage,ladder:LADDER.indexOf(stage)+1,
      content:'Reference brief ('+stage+' ladder stage) for: '+bt+'. A full entry documents: identity and class, documented typical dosing, documented effects, warnings, interactions, and legal status - each verified against public references before filing.',
      demo:null,src:'assistant-built',_seed:seed};
  }
  var angle=pick(ANGLES,s);
  var title=base[0]+' ('+angle+', '+stage+')';
  return {id:id,title:title,description:base[1],genre:base[2]||'reference',
    type:'performance enhancer record',stage:stage,ladder:LADDER.indexOf(stage)+1,
    content:base[0]+' - '+angle+' view ('+stage+' stage). '+base[1]+' See the archive entry for the fully documented reference.',
    demo:null,src:'assistant-built',_seed:seed};
}
function generateBatch(n,startSeed){
  var out=[],i;
  n=Math.min(n||1,MAX_BATCH);
  for(i=0;i<n;i++){var r=generate((startSeed||1)+i);if(r)out.push(r);else break;}
  return out;
}
function validate(r){
  var errs=[];
  if(!r.id)errs.push('missing id');
  if(!r.title)errs.push('missing title');
  if(!r.content||r.content.length<50)errs.push('content too short');
  if(r._seed>HARD_STOP)errs.push('past hard stop');
  return {ok:errs.length===0,errors:errs};
}
function driftCheck(rec,sample){
  for(var i=0;i<sample.length;i++){if(sample[i].t===rec.title||sample[i].title===rec.title)return {ok:false,errors:['duplicate title']};}
  return {ok:true,errors:[]};
}
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('performance-enhancers',{generate:generate,generateBatch:generateBatch,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,generateBatch:generateBatch,validate:validate,driftCheck:driftCheck,HARD_STOP:HARD_STOP};}
})();
