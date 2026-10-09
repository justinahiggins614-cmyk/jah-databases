/* ✳ JAH Funding Deal Database generator. Property of Justin Addam Higgins (JAH).
   Deterministic (seeded) startup funding record generator: jahdb-startup-funding-1.0.
   All companies and figures are synthetically generated. */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(s,r){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function pad(n){return String(n).padStart(6,'0');}

var CATS=['fintech','healthtech','ai','ecommerce','cleantech','edtech'];
var ROUNDS=['pre-seed','seed','series-a','series-b','series-c'];
var STATUS=['active','acquired','ipo','closed'];
var CITIES=['Austin','San Francisco','New York','Boston','Seattle','Denver','Chicago','Atlanta','Miami','Toronto','London','Berlin','Tel Aviv','Singapore','Bangalore','Toronto','Los Angeles','Portland','Minneapolis','Philadelphia','Amsterdam','Stockholm','Sydney','Nairobi','Lagos','Mexico City','Sao Paulo','Dublin','Warsaw','Seoul'];

var P1=['Quan','Nex','Vel','Zyn','Bright','Core','Hyper','Lum','Opti','Syn','Terra','Volt','Cloud','Data','Fin','Medi','Edu','Green','Smart','Rapid','True','Nova','Pixel','Orbit','Pulse'];
var P2=['ti','blo','ra','va','fi','mo','xa','do','na','lo','ra','mi','co','gi','te'];
var SFX=['va','fy','ly','io','labs','works','hub','wise','point','stack','flow','mind','base','grid','loop'];

var ROUND_RANGE={'pre-seed':[100000,2000000],'seed':[500000,10000000],'series-a':[5000000,40000000],'series-b':[20000000,120000000],'series-c':[60000000,400000000]};

function cap(s){return s.charAt(0).toUpperCase()+s.slice(1);}
function generate(seed,opts,rnd){
  rnd=rnd||prng(seed);
  var cat=(opts&&opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:pick(rnd,CATS);
  var name=cap(pick(rnd,P1)+pick(rnd,P2)+pick(rnd,SFX));
  var round=pick(rnd,ROUNDS);
  var rr=ROUND_RANGE[round];
  var lastAmt=ri(rnd,rr[0],rr[1]);
  var total=lastAmt+ri(rnd,0,Math.max(1,Math.floor(lastAmt*1.5)));
  var founded=ri(rnd,2010,2026);
  var status=pick(rnd,STATUS);
  return {
    id:'JAH-FUND-'+pad(seed),
    startup_id:'JAH-FUND-'+pad(seed),
    name:name,
    sector:cat,
    founded_year:founded,
    hq_city:pick(rnd,CITIES),
    total_raised:total,
    last_round:round,
    last_amount:lastAmt,
    status:status
  };
}
function validate(r){
  var e=[];
  if(typeof r.id!=='string'||!/^JAH-FUND-\d{6}$/.test(r.id))e.push('id');
  if(typeof r.startup_id!=='string'||r.startup_id!==r.id)e.push('startup_id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(CATS.indexOf(r.sector)<0)e.push('sector');
  if(typeof r.founded_year!=='number'||r.founded_year<2010||r.founded_year>2026)e.push('founded_year');
  if(typeof r.hq_city!=='string'||!r.hq_city.length)e.push('hq_city');
  if(typeof r.total_raised!=='number'||r.total_raised<=0)e.push('total_raised');
  if(ROUNDS.indexOf(r.last_round)<0)e.push('last_round');
  if(typeof r.last_amount!=='number'||r.last_amount<=0)e.push('last_amount');
  if(r.last_amount>=r.total_raised)e.push('last_amount<total_raised');
  if(STATUS.indexOf(r.status)<0)e.push('status');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-startup-funding-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('startup-funding',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
