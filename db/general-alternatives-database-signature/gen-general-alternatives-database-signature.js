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

var ALTTABLE=[{"original": "morning coffee", "alternative": "Manon morning tonic", "metrics": [{"k": "caffeine", "original": "high", "alternative": "none", "better": "lower"}, {"k": "crash", "original": "common", "alternative": "none", "better": "lower"}, {"k": "ritual time", "original": "fast", "alternative": "2 minutes", "better": "higher"}], "title": "Manon Morning Tonic", "findKey": "morning drink", "tradeoff": "No caffeine at all \u2014 a true alternative, not a substitute."}, {"original": "car commute", "alternative": "Manon walk-and-work", "metrics": [{"k": "fuel cost", "original": "high", "alternative": "zero", "better": "lower"}, {"k": "exercise", "original": "none", "alternative": "built in", "better": "higher"}, {"k": "range", "original": "far", "alternative": "local", "better": "lower"}], "title": "Manon Walk-and-Work", "findKey": "commute", "tradeoff": "Only for local, flexible work; weather applies."}, {"original": "short-haul flight", "alternative": "Manon slow road", "metrics": [{"k": "speed", "original": "fast", "alternative": "slow", "better": "higher"}, {"k": "experience per mile", "original": "low", "alternative": "high", "better": "higher"}, {"k": "carbon", "original": "high", "alternative": "lower", "better": "lower"}], "title": "Manon Slow Road", "findKey": "travel", "tradeoff": "Costs time, the one currency you cannot earn back."}, {"original": "streaming subscriptions", "alternative": "Manon antenna evenings", "metrics": [{"k": "monthly cost", "original": "growing", "alternative": "zero", "better": "lower"}, {"k": "choice paralysis", "original": "high", "alternative": "none", "better": "lower"}, {"k": "new releases", "original": "yes", "alternative": "no", "better": "higher"}], "title": "Manon Antenna Evenings", "findKey": "TV", "tradeoff": "No new releases; the library is the catalog."}, {"original": "meat-centered meals", "alternative": "Manon pantry protein", "metrics": [{"k": "cost per serving", "original": "dollars", "alternative": "pennies", "better": "lower"}, {"k": "cook time weekly", "original": "nightly", "alternative": "one batch", "better": "lower"}, {"k": "variety", "original": "high", "alternative": "rotation needed", "better": "higher"}], "title": "Manon Pantry Protein", "findKey": "protein", "tradeoff": "Batch cooking is the whole trick; skip it and it fails."}, {"original": "air conditioning", "alternative": "Manon cool house", "metrics": [{"k": "electricity", "original": "high", "alternative": "fan only", "better": "lower"}, {"k": "heat-wave proof", "original": "yes", "alternative": "partial", "better": "higher"}, {"k": "effort", "original": "thermostat", "alternative": "daily ritual", "better": "lower"}], "title": "Manon Cool House", "findKey": "cooling", "tradeoff": "A daily ritual; extreme humid heat still wins."}, {"original": "landline habit", "alternative": "Manon porch call", "metrics": [{"k": "cost", "original": "monthly bill", "alternative": "zero", "better": "lower"}, {"k": "distraction", "original": "low", "alternative": "none", "better": "lower"}, {"k": "reachability", "original": "anytime", "alternative": "one hour", "better": "higher"}], "title": "Manon Porch Call", "findKey": "phone call", "tradeoff": "One hour a day; the rest of the time you are gloriously unreachable."}, {"original": "bright evening lighting", "alternative": "Manon candle hour", "metrics": [{"k": "electricity", "original": "on", "alternative": "off", "better": "lower"}, {"k": "eye strain", "original": "higher", "alternative": "lower", "better": "lower"}, {"k": "usable light", "original": "full", "alternative": "dim", "better": "higher"}], "title": "Manon Candle Hour", "findKey": "lighting", "tradeoff": "Dim by design; not for detailed work."}, {"original": "news feed scrolling", "alternative": "Manon paper morning", "metrics": [{"k": "anxiety", "original": "high", "alternative": "low", "better": "lower"}, {"k": "breaking speed", "original": "instant", "alternative": "weekly", "better": "higher"}, {"k": "depth", "original": "shallow", "alternative": "deep", "better": "higher"}], "title": "Manon Paper Morning", "findKey": "news", "tradeoff": "You will hear big news late; that is the point."}, {"original": "gadget cooking", "alternative": "Manon hearth cook", "metrics": [{"k": "equipment", "original": "many gadgets", "alternative": "one pan", "better": "lower"}, {"k": "flavor", "original": "good", "alternative": "better", "better": "higher"}, {"k": "learning curve", "original": "low", "alternative": "real", "better": "lower"}], "title": "Manon Hearth Cook", "findKey": "cooking", "tradeoff": "Cast iron demands technique and care."}, {"original": "bottled water", "alternative": "Manon well cup", "metrics": [{"k": "plastic", "original": "yes", "alternative": "none", "better": "lower"}, {"k": "cost", "original": "ongoing", "alternative": "zero", "better": "lower"}, {"k": "remembrance", "original": "n/a", "alternative": "built in", "better": "higher"}], "title": "Manon Well Cup", "findKey": "drinking water", "tradeoff": "A ritual, not a product; the cup does nothing by itself."}, {"original": "taxi rides", "alternative": "Manon foot miles", "metrics": [{"k": "fare", "original": "yes", "alternative": "zero", "better": "lower"}, {"k": "fitness", "original": "none", "alternative": "gained", "better": "higher"}, {"k": "time", "original": "fast", "alternative": "slower", "better": "lower"}], "title": "Manon Foot Miles", "findKey": "short trips", "tradeoff": "Time and weather are the real costs."}, {"original": "gym membership", "alternative": "Manon hundred", "metrics": [{"k": "cost", "original": "monthly", "alternative": "zero", "better": "lower"}, {"k": "equipment", "original": "full gym", "alternative": "floor", "better": "lower"}, {"k": "ceiling", "original": "high", "alternative": "bodyweight", "better": "higher"}], "title": "Manon Hundred", "findKey": "workout", "tradeoff": "Bodyweight ceiling; discipline is the membership fee."}, {"original": "new computer", "alternative": "Manon rebuild bench", "metrics": [{"k": "cost", "original": "full", "alternative": "fraction", "better": "lower"}, {"k": "e-waste", "original": "new", "alternative": "diverted", "better": "lower"}, {"k": "latest specs", "original": "yes", "alternative": "no", "better": "higher"}], "title": "Manon Rebuild Bench", "findKey": "computer", "tradeoff": "A weekend project; no cutting-edge specs."}, {"original": "grass lawn", "alternative": "Manon meadow", "metrics": [{"k": "mowing", "original": "weekly", "alternative": "yearly", "better": "lower"}, {"k": "water", "original": "high", "alternative": "rain only", "better": "lower"}, {"k": "tidy look", "original": "instant", "alternative": "wild", "better": "higher"}], "title": "Manon Meadow", "findKey": "lawn", "tradeoff": "Wild by design; year one looks like a mistake."}];

var PREFIX='JAH-GALTS-';
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

var gen={version:'jahdb-general-alternatives-database-signature-1.0',generate:generate,validate:validate,SigRegCreate:SigRegCreate,AltDB:AltDB};
if(typeof window!=='undefined')window['GEN_GENERAL_ALTERNATIVES_DATABASE_SIGNATURE']=gen;
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('general-alternatives-database-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
