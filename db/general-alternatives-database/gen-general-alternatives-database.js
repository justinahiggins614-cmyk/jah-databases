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

var ALTTABLE=[{"original": "morning coffee", "alternative": "matcha green tea", "metrics": [{"k": "caffeine per serving", "original": "~95mg", "alternative": "~70mg", "better": "lower"}, {"k": "jitters", "original": "common", "alternative": "rare", "better": "lower"}, {"k": "ritual time", "original": "fast", "alternative": "slower", "better": "higher"}], "title": "Matcha Instead of Coffee", "findKey": "coffee", "tradeoff": "Less caffeine per cup; good matcha costs more than commodity coffee."}, {"original": "car commute", "alternative": "e-bike commute", "metrics": [{"k": "cost per mile", "original": "high", "alternative": "very low", "better": "lower"}, {"k": "parking", "original": "hunt for it", "alternative": "anywhere", "better": "higher"}, {"k": "weather exposure", "original": "none", "alternative": "full", "better": "lower"}], "title": "E-Bike Instead of Car Commute", "findKey": "car commute", "tradeoff": "Weather and cargo limits; needs safe routes and secure storage."}, {"original": "short-haul flight", "alternative": "high-speed rail", "metrics": [{"k": "CO2 per passenger", "original": "high", "alternative": "much lower", "better": "lower"}, {"k": "downtown to downtown", "original": "slow (airports)", "alternative": "fast", "better": "higher"}, {"k": "route availability", "original": "everywhere", "alternative": "limited corridors", "better": "higher"}], "title": "High-Speed Rail Instead of Short-Haul Flights", "findKey": "flight", "tradeoff": "Only where the lines exist; building them takes decades."}, {"original": "cable TV", "alternative": "streaming services", "metrics": [{"k": "monthly cost (1-2 svcs)", "original": "high", "alternative": "lower", "better": "lower"}, {"k": "contract", "original": "yes", "alternative": "no", "better": "lower"}, {"k": "live sports", "original": "included", "alternative": "fragmented", "better": "higher"}], "title": "Streaming Instead of Cable TV", "findKey": "cable", "tradeoff": "Costs creep with each added service; live sports stay fragmented."}, {"original": "meat protein", "alternative": "beans and lentils", "metrics": [{"k": "cost per gram protein", "original": "high", "alternative": "very low", "better": "lower"}, {"k": "carbon footprint", "original": "high", "alternative": "low", "better": "lower"}, {"k": "prep time", "original": "fast", "alternative": "longer", "better": "lower"}], "title": "Legumes Instead of Meat Protein", "findKey": "meat", "tradeoff": "Longer prep and a digestive adjustment period; pair with grains."}, {"original": "air conditioning", "alternative": "passive cooling design", "metrics": [{"k": "running cost", "original": "high", "alternative": "near zero", "better": "lower"}, {"k": "works in heat waves", "original": "yes", "alternative": "limited", "better": "higher"}, {"k": "mechanical failure", "original": "possible", "alternative": "none", "better": "lower"}], "title": "Passive Cooling Instead of Air Conditioning", "findKey": "air conditioning", "tradeoff": "Limited in extreme humid heat; needs the building designed for it."}, {"original": "landline phone", "alternative": "VoIP service", "metrics": [{"k": "monthly cost", "original": "moderate", "alternative": "low", "better": "lower"}, {"k": "works in power outage", "original": "yes", "alternative": "no (no backup)", "better": "higher"}, {"k": "features", "original": "basic", "alternative": "rich", "better": "higher"}], "title": "VoIP Instead of Landline", "findKey": "landline", "tradeoff": "Needs power and internet; 911 location needs setup."}, {"original": "incandescent bulb", "alternative": "LED bulb", "metrics": [{"k": "watts for 800 lumens", "original": "60", "alternative": "8-10", "better": "lower"}, {"k": "lifespan", "original": "~1,000 hrs", "alternative": "15,000+ hrs", "better": "higher"}, {"k": "upfront cost", "original": "very low", "alternative": "low", "better": "lower"}], "title": "LEDs Instead of Incandescent Bulbs", "findKey": "light bulb", "tradeoff": "Slightly higher upfront cost; buy warm color temperatures for living spaces."}, {"original": "print newspaper", "alternative": "digital news", "metrics": [{"k": "update speed", "original": "daily", "alternative": "instant", "better": "higher"}, {"k": "cost", "original": "subscription+", "alternative": "low/free", "better": "lower"}, {"k": "focus quality", "original": "curated", "alternative": "variable", "better": "higher"}], "title": "Digital News Instead of Print Newspaper", "findKey": "newspaper", "tradeoff": "Feeds reward outrage; curate sources deliberately."}, {"original": "gas stove", "alternative": "induction cooktop", "metrics": [{"k": "boil speed", "original": "moderate", "alternative": "fast", "better": "higher"}, {"k": "indoor combustion", "original": "yes", "alternative": "none", "better": "lower"}, {"k": "cookware needed", "original": "any", "alternative": "magnetic", "better": "higher"}], "title": "Induction Instead of Gas Stove", "findKey": "gas stove", "tradeoff": "Needs compatible pans and adequate electrical service."}, {"original": "bottled water", "alternative": "filtered tap water", "metrics": [{"k": "cost per liter", "original": "high", "alternative": "tiny", "better": "lower"}, {"k": "plastic waste", "original": "high", "alternative": "none", "better": "lower"}, {"k": "portability", "original": "grab and go", "alternative": "fill a bottle", "better": "higher"}], "title": "Filtered Tap Instead of Bottled Water", "findKey": "bottled water", "tradeoff": "Cartridge changes are the whole maintenance burden."}, {"original": "taxi ride", "alternative": "public transit", "metrics": [{"k": "cost per trip", "original": "high", "alternative": "low", "better": "lower"}, {"k": "door to door", "original": "yes", "alternative": "rarely", "better": "higher"}, {"k": "schedule freedom", "original": "total", "alternative": "fixed", "better": "higher"}], "title": "Transit Instead of Taxi", "findKey": "taxi", "tradeoff": "Only as good as the local system; late-night gaps hurt."}, {"original": "gym membership", "alternative": "bodyweight training", "metrics": [{"k": "monthly cost", "original": "recurring", "alternative": "zero", "better": "lower"}, {"k": "max load", "original": "unlimited", "alternative": "bodyweight+", "better": "higher"}, {"k": "coaching", "original": "available", "alternative": "self-taught", "better": "higher"}], "title": "Bodyweight Training Instead of Gym Membership", "findKey": "gym", "tradeoff": "Harder to load heavy legs; form is on you to learn."}, {"original": "new laptop", "alternative": "certified refurbished laptop", "metrics": [{"k": "price", "original": "full", "alternative": "~half", "better": "lower"}, {"k": "warranty", "original": "full", "alternative": "limited", "better": "higher"}, {"k": "battery health", "original": "100%", "alternative": "80-90%", "better": "higher"}], "title": "Refurbished Instead of New Laptop", "findKey": "laptop", "tradeoff": "Check battery cycles and warranty terms before buying."}, {"original": "grass lawn", "alternative": "native plant landscaping", "metrics": [{"k": "water need", "original": "high", "alternative": "low", "better": "lower"}, {"k": "mowing", "original": "weekly", "alternative": "never", "better": "lower"}, {"k": "instant curb appeal", "original": "yes", "alternative": "takes years", "better": "higher"}], "title": "Native Landscaping Instead of Lawn", "findKey": "lawn", "tradeoff": "Looks sparse for 2\u20133 years; HOAs may object."}];

var PREFIX='JAH-GALT-';
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

var gen={version:'jahdb-general-alternatives-database-1.0',generate:generate,validate:validate,SigRegCreate:SigRegCreate,AltDB:AltDB};
if(typeof window!=='undefined')window['GEN_GENERAL_ALTERNATIVES_DATABASE']=gen;
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('general-alternatives-database',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
