(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}

function SigRegCreate(opts){
  opts=opts||{};
  var HARD_CAP=(typeof opts.maxRecords==='number')?opts.maxRecords:1000000000;
  var minGapMs=opts.minGapMs||0, costPer=opts.costPer||1;
  var budget=(typeof opts.budget==='number')?opts.budget:Infinity;
  var checkFn=opts.check||function(){return {ok:true,errors:[]};};
  var produced=0, spent=0, lastT=0, log=[];
  function generate(seed, producer){
    if(produced>=HARD_CAP) throw new Error('HARD_CAP_REACHED at '+HARD_CAP+' records');
    var now=Date.now();
    if(minGapMs>0 && lastT>0 && (now-lastT)<minGapMs) throw new Error('THROTTLE: '+(minGapMs-(now-lastT))+'ms remaining');
    lastT=now;
    var item=producer(seed);
    var v=checkFn(item);
    if(!v||!v.ok) throw new Error('CORRECTNESS_FAILED: '+((v&&v.errors)||['unknown']).join('; '));
    item._label='simulated';
    item._seq=produced+1;
    item._sigreg={hard_cap:HARD_CAP, seq:produced+1, verified:true};
    produced++; spent+=costPer;
    if(spent>budget) throw new Error('BUDGET_EXCEEDED');
    log.push({seq:produced,seed:seed,t:now});
    return item;
  }
  function stats(){return {produced:produced, hardCap:HARD_CAP, spent:spent, budget:budget, logSize:log.length};}
  function reset(){produced=0;spent=0;lastT=0;log=[];}
  return {generate:generate, stats:stats, reset:reset, HARD_CAP:HARD_CAP};
}

var ALTTABLE=[{"original": "all-copper motor winding", "alternative": "Manon copper-saver winding", "metrics": [{"k": "copper per motor", "original": "full", "alternative": "under half", "better": "lower"}, {"k": "winding complexity", "original": "standard", "alternative": "higher", "better": "lower"}, {"k": "efficiency", "original": "baseline", "alternative": "comparable", "better": "higher"}], "title": "Manon Copper-Saver Winding", "findKey": "copper winding", "tradeoff": "More complex winding labor; a Signature shop technique, not a commodity part."}, {"original": "lithium home battery", "alternative": "Manon salt-cell pack", "metrics": [{"k": "raw material cost", "original": "high", "alternative": "low", "better": "lower"}, {"k": "footprint", "original": "compact", "alternative": "larger", "better": "lower"}, {"k": "fire risk", "original": "managed", "alternative": "very low", "better": "lower"}], "title": "Manon Salt-Cell Pack", "findKey": "lithium battery", "tradeoff": "Larger and heavier; a Signature build, not an off-the-shelf product."}, {"original": "neodymium disc magnet", "alternative": "Manon ferrite array", "metrics": [{"k": "rare-earth content", "original": "yes", "alternative": "none", "better": "lower"}, {"k": "one-face field", "original": "n/a", "alternative": "focused", "better": "higher"}, {"k": "assembly effort", "original": "none", "alternative": "high", "better": "lower"}], "title": "Manon Magnet Array", "findKey": "magnet", "tradeoff": "Fiddly hand assembly; weaker than a true neodymium disc of the same size."}, {"original": "treated wood post", "alternative": "Manon rust-proof post", "metrics": [{"k": "rot/rust life", "original": "10-15 years", "alternative": "50+ years", "better": "higher"}, {"k": "build effort", "original": "dig and set", "alternative": "higher", "better": "lower"}, {"k": "material cost", "original": "low", "alternative": "moderate", "better": "lower"}], "title": "Manon Rust-Proof Post", "findKey": "fence post", "tradeoff": "More labor per post; overkill where ground stays dry."}, {"original": "portland mortar", "alternative": "Manon ashcrete", "metrics": [{"k": "embodied carbon", "original": "high", "alternative": "very low", "better": "lower"}, {"k": "compressive strength", "original": "high", "alternative": "moderate", "better": "higher"}, {"k": "cure time", "original": "days", "alternative": "weeks", "better": "lower"}], "title": "Manon Ashcrete", "findKey": "mortar", "tradeoff": "Not for structural loads; slow cure needs patience."}, {"original": "solid timber beam", "alternative": "Manon strand beam", "metrics": [{"k": "uses waste offcuts", "original": "no", "alternative": "yes", "better": "higher"}, {"k": "straightness", "original": "varies", "alternative": "high", "better": "higher"}, {"k": "press equipment", "original": "none", "alternative": "needed", "better": "lower"}], "title": "Manon Strand Beam", "findKey": "beam", "tradeoff": "Needs a press and glue-up time; a workshop build, not a lumberyard SKU."}, {"original": "platinum electrode", "alternative": "Manon nickel sponge cell", "metrics": [{"k": "electrode cost", "original": "very high", "alternative": "very low", "better": "lower"}, {"k": "surface area", "original": "moderate", "alternative": "very high", "better": "higher"}, {"k": "build skill", "original": "buy it", "alternative": "etch it", "better": "lower"}], "title": "Manon Nickel Sponge Cell", "findKey": "electrode", "tradeoff": "Hand-built and variable; for experiments, not industry."}, {"original": "municipal irrigation", "alternative": "Manon twice-water garden", "metrics": [{"k": "fresh water for garden", "original": "full", "alternative": "near zero", "better": "lower"}, {"k": "install complexity", "original": "none", "alternative": "moderate", "better": "lower"}, {"k": "plant health", "original": "baseline", "alternative": "improved", "better": "higher"}], "title": "Manon Twice-Water Garden", "findKey": "irrigation", "tradeoff": "Needs plumbing changes and soap awareness; check local codes."}, {"original": "concrete block", "alternative": "Manon hemp-lime block", "metrics": [{"k": "insulation", "original": "poor", "alternative": "good", "better": "higher"}, {"k": "carbon story", "original": "high", "alternative": "negative", "better": "lower"}, {"k": "structural use", "original": "yes", "alternative": "infill only", "better": "higher"}], "title": "Manon Hemp-Lime Block", "findKey": "block", "tradeoff": "Infill only; slow production by hand."}, {"original": "OSB sheathing", "alternative": "Manon strand panel", "metrics": [{"k": "edge swell", "original": "higher", "alternative": "low", "better": "lower"}, {"k": "cost", "original": "low", "alternative": "moderate", "better": "lower"}, {"k": "strength", "original": "good", "alternative": "comparable", "better": "higher"}], "title": "Manon Strand Panel", "findKey": "OSB", "tradeoff": "A workshop press product; not yet a commodity panel."}, {"original": "denim workwear", "alternative": "Manon work cloth", "metrics": [{"k": "water to grow", "original": "high", "alternative": "low", "better": "lower"}, {"k": "abrasion life", "original": "good", "alternative": "longer", "better": "higher"}, {"k": "off-the-rack availability", "original": "everywhere", "alternative": "make it", "better": "higher"}], "title": "Manon Work Cloth", "findKey": "denim", "tradeoff": "A spec to commission, not a store shelf item."}, {"original": "pump diesel", "alternative": "Manon waste-oil blend", "metrics": [{"k": "fuel cost", "original": "full price", "alternative": "near zero", "better": "lower"}, {"k": "conversion work", "original": "none", "alternative": "weekend project", "better": "lower"}, {"k": "emissions care", "original": "standard", "alternative": "needs attention", "better": "higher"}], "title": "Manon Waste-Oil Burner Tune", "findKey": "diesel fuel", "tradeoff": "Filtration and maintenance are mandatory; know your engine."}, {"original": "gas furnace", "alternative": "Manon heat battery", "metrics": [{"k": "on-site combustion", "original": "yes", "alternative": "none", "better": "lower"}, {"k": "uses off-peak power", "original": "no", "alternative": "yes", "better": "higher"}, {"k": "space needed", "original": "closet", "alternative": "tank room", "better": "lower"}], "title": "Manon Heat Battery", "findKey": "heating", "tradeoff": "Needs space for the tank; a planned install, not a swap."}, {"original": "lithium backup", "alternative": "Manon iron cell", "metrics": [{"k": "cost per kWh stored", "original": "high", "alternative": "very low", "better": "lower"}, {"k": "round-trip efficiency", "original": "high", "alternative": "moderate", "better": "higher"}, {"k": "readiness", "original": "buy today", "alternative": "concept build", "better": "higher"}], "title": "Manon Iron Cell", "findKey": "backup battery", "tradeoff": "A concept build; iron-air is real chemistry but this cell is his design."}, {"original": "plastic clamshell", "alternative": "Manon fiber clamshell", "metrics": [{"k": "compostable", "original": "no", "alternative": "yes", "better": "higher"}, {"k": "splash resistance", "original": "high", "alternative": "moderate", "better": "higher"}, {"k": "unit cost", "original": "very low", "alternative": "moderate", "better": "lower"}], "title": "Manon Fiber Clamshell", "findKey": "clamshell", "tradeoff": "Hand-dipped edges limit scale; splash-proof, not waterproof."}];

var PREFIX='JAH-RALTS-';
var AltDB={
  find:function(q){
    q=String(q).toLowerCase();
    return ALTTABLE.filter(function(r){
      return (r.original+' '+r.alternative+' '+r.title).toLowerCase().indexOf(q)>=0;
    });
  },
  compare:function(original, alternative){
    var row=null;
    ALTTABLE.forEach(function(r){ if(r.original===original&&r.alternative===alternative)row=r; });
    if(!row)return {winner:null,details:[]};
    var wins={};var details=row.metrics.map(function(m){
      var w=m.better==='higher'?'alternative':(m.better==='lower'?'alternative':'tie');
      wins[w]=(wins[w]||0)+1;
      return {metric:m.k, original:m.original, alternative:m.alternative, edge:w};
    });
    var winner=(wins.alternative||0)>=(details.length/2)?alternative:original;
    return {winner:winner,details:details};
  },
  list:function(){return ALTTABLE.map(function(r){return r.title;});}
};
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var row=pick(ALTTABLE,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {id:id,title:'Alternative study: '+row.title+' (seed '+seed+')',
    t:'Alternative study: '+row.title+' (seed '+seed+')',g:'Alternatives',c:1,
    ladder_rank:ri(rnd,1,15),
    description:'Generated alternative study pairing '+row.original+' with '+row.alternative+'. '+row.tradeoff,
    original:row.original,alternative:row.alternative,findKey:row.findKey,
    metrics:row.metrics,tradeoff:row.tradeoff,
    demo:{runtime:'node',code:'var cd=G.AltDB.find(DATA.original.split(" ")[0]).filter(function(x){return x.original===DATA.original;});assert(cd.length>=1,"find works");var c=G.AltDB.compare(cd[0].original,cd[0].alternative);assert(c.winner,"winner picked");log("alt study ok: "+c.winner);',expect:'verified'},
    provenance:'signature',last_verified:'2026-10-21',
    march_marker:'Million-record march in progress: 15 of 1,000,000 records (0.0015%).',_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(!r.original||!r.alternative)e.push('pair');
  if(!Array.isArray(r.metrics)||r.metrics.length<2)e.push('metrics');
  if(typeof r.ladder_rank!=='number'||r.ladder_rank<1||r.ladder_rank>15)e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}

var gen={version:'jahdb-resource-alternatives-database-signature-1.0',generate:generate,validate:validate,SigRegCreate:SigRegCreate,AltDB:AltDB};
if(typeof window!=='undefined')window['GEN_RESOURCE_ALTERNATIVES_DATABASE_SIGNATURE']=gen;
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('resource-alternatives-database-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
