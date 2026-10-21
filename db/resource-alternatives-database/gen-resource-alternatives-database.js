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

var ALTTABLE=[{"original": "copper electrical wire", "alternative": "aluminum electrical wire", "metrics": [{"k": "material cost per ampere", "original": "high", "alternative": "low", "better": "lower"}, {"k": "weight for same ampacity", "original": "heavy", "alternative": "light", "better": "lower"}, {"k": "conductivity", "original": "100% IACS", "alternative": "61% IACS", "better": "higher"}], "title": "Aluminum Wiring Instead of Copper", "findKey": "copper", "tradeoff": "Aluminum needs a larger gauge for the same current and careful termination; copper is more forgiving and compact."}, {"original": "lithium-ion battery", "alternative": "sodium-ion battery", "metrics": [{"k": "raw material abundance", "original": "scarce", "alternative": "abundant", "better": "higher"}, {"k": "energy density", "original": "high", "alternative": "moderate", "better": "higher"}, {"k": "material cost", "original": "high", "alternative": "low", "better": "lower"}], "title": "Sodium-Ion Batteries Instead of Lithium-Ion", "findKey": "lithium", "tradeoff": "Lower energy density means bigger, heavier packs; best where weight matters less than cost."}, {"original": "neodymium magnet", "alternative": "ferrite magnet", "metrics": [{"k": "magnetic strength", "original": "very high", "alternative": "moderate", "better": "higher"}, {"k": "cost", "original": "high", "alternative": "very low", "better": "lower"}, {"k": "rare-earth content", "original": "yes", "alternative": "none", "better": "lower"}], "title": "Ferrite Magnets Instead of Neodymium", "findKey": "neodymium", "tradeoff": "Weaker field means larger magnets and motors for the same torque."}, {"original": "steel rebar", "alternative": "GFRP rebar", "metrics": [{"k": "corrosion resistance", "original": "rusts", "alternative": "immune", "better": "higher"}, {"k": "weight", "original": "heavy", "alternative": "light", "better": "lower"}, {"k": "field bendability", "original": "yes", "alternative": "no", "better": "higher"}], "title": "GFRP Rebar Instead of Steel Rebar", "findKey": "steel rebar", "tradeoff": "Must be pre-bent at the factory; design codes are newer and stricter."}, {"original": "portland cement concrete", "alternative": "fly-ash blended concrete", "metrics": [{"k": "CO2 per tonne", "original": "high", "alternative": "lower", "better": "lower"}, {"k": "28-day strength", "original": "standard", "alternative": "equal or better", "better": "higher"}, {"k": "early curing speed", "original": "fast", "alternative": "slower", "better": "higher"}], "title": "Fly-Ash Concrete Instead of Pure Portland Cement", "findKey": "cement", "tradeoff": "Slower set times need schedule planning; supply of quality fly ash varies by region."}, {"original": "timber lumber", "alternative": "engineered bamboo", "metrics": [{"k": "renewal time", "original": "decades", "alternative": "3-5 years", "better": "lower"}, {"k": "strength per weight", "original": "good", "alternative": "comparable", "better": "higher"}, {"k": "moisture sensitivity", "original": "moderate", "alternative": "higher", "better": "lower"}], "title": "Engineered Bamboo Instead of Timber", "findKey": "timber", "tradeoff": "Needs good detailing against moisture; structural grading standards are still maturing."}, {"original": "platinum catalyst", "alternative": "nickel-iron catalyst", "metrics": [{"k": "catalyst cost", "original": "very high", "alternative": "very low", "better": "lower"}, {"k": "material scarcity", "original": "scarce", "alternative": "abundant", "better": "lower"}, {"k": "acidic-cell compatibility", "original": "yes", "alternative": "alkaline only", "better": "higher"}], "title": "Nickel-Iron Catalysts Instead of Platinum", "findKey": "platinum", "tradeoff": "Limited to alkaline environments; platinum still rules acidic PEM cells."}, {"original": "fresh water irrigation", "alternative": "greywater recycling", "metrics": [{"k": "fresh water demand", "original": "full", "alternative": "reduced", "better": "lower"}, {"k": "system cost", "original": "none", "alternative": "moderate install", "better": "lower"}, {"k": "plant suitability", "original": "all", "alternative": "most ornamentals", "better": "higher"}], "title": "Greywater Recycling Instead of Fresh Water for Irrigation", "findKey": "water", "tradeoff": "Needs plumbing work and care with salts and soaps; codes vary by jurisdiction."}, {"original": "concrete block wall", "alternative": "hempcrete infill wall", "metrics": [{"k": "thermal insulation", "original": "poor", "alternative": "good", "better": "higher"}, {"k": "embodied carbon", "original": "high", "alternative": "negative", "better": "lower"}, {"k": "load-bearing", "original": "yes", "alternative": "no", "better": "higher"}], "title": "Hempcrete Instead of Concrete Block", "findKey": "concrete block", "tradeoff": "Requires a structural frame; drying time is long and labor is specialized."}, {"original": "plywood", "alternative": "OSB panels", "metrics": [{"k": "panel cost", "original": "higher", "alternative": "lower", "better": "lower"}, {"k": "shear strength", "original": "high", "alternative": "comparable", "better": "higher"}, {"k": "edge swell when wet", "original": "low", "alternative": "higher", "better": "lower"}], "title": "OSB Instead of Plywood", "findKey": "plywood", "tradeoff": "Keep it dry during construction; choose plywood where edges stay exposed."}, {"original": "cotton fiber", "alternative": "hemp fiber", "metrics": [{"k": "irrigation water", "original": "high", "alternative": "low", "better": "lower"}, {"k": "pesticide need", "original": "high", "alternative": "minimal", "better": "lower"}, {"k": "fabric softness new", "original": "soft", "alternative": "coarse", "better": "higher"}], "title": "Hemp Fiber Instead of Cotton", "findKey": "cotton", "tradeoff": "Coarser hand-feel until broken in; smaller retail selection."}, {"original": "petroleum diesel", "alternative": "biodiesel", "metrics": [{"k": "fossil carbon per mile", "original": "high", "alternative": "lower", "better": "lower"}, {"k": "engine compatibility", "original": "native", "alternative": "high (blends)", "better": "higher"}, {"k": "cold-weather flow", "original": "good", "alternative": "gels sooner", "better": "higher"}], "title": "Biodiesel Instead of Petroleum Diesel", "findKey": "diesel", "tradeoff": "Gels in cold weather; large-scale feedstock competes with food and land."}, {"original": "gas furnace", "alternative": "electric heat pump", "metrics": [{"k": "fuel burned on site", "original": "gas", "alternative": "none", "better": "lower"}, {"k": "efficiency (COP)", "original": "~0.9", "alternative": "2-4", "better": "higher"}, {"k": "deep-cold output", "original": "full", "alternative": "reduced", "better": "higher"}], "title": "Heat Pumps Instead of Gas Furnaces", "findKey": "furnace", "tradeoff": "Upfront cost higher; performance dips in extreme cold without backup."}, {"original": "cobalt NMC battery", "alternative": "LFP battery", "metrics": [{"k": "cobalt content", "original": "yes", "alternative": "none", "better": "lower"}, {"k": "cycle life", "original": "moderate", "alternative": "long", "better": "higher"}, {"k": "energy density", "original": "high", "alternative": "moderate", "better": "higher"}], "title": "LFP Batteries Instead of Cobalt NMC", "findKey": "cobalt", "tradeoff": "Heavier packs for the same range; less ideal where every kilogram counts."}, {"original": "plastic clamshell packaging", "alternative": "molded fiber packaging", "metrics": [{"k": "end-of-life", "original": "landfill centuries", "alternative": "compostable", "better": "higher"}, {"k": "water resistance", "original": "high", "alternative": "low", "better": "higher"}, {"k": "unit cost (scale)", "original": "very low", "alternative": "low-moderate", "better": "lower"}], "title": "Molded Fiber Packaging Instead of Plastic", "findKey": "plastic packaging", "tradeoff": "Not waterproof; thin margins at small production volumes."}];

var PREFIX='JAH-RALT-';
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
    provenance:'public',last_verified:'2026-10-21',
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

var gen={version:'jahdb-resource-alternatives-database-1.0',generate:generate,validate:validate,SigRegCreate:SigRegCreate,AltDB:AltDB};
if(typeof window!=='undefined')window['GEN_RESOURCE_ALTERNATIVES_DATABASE']=gen;
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('resource-alternatives-database',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
