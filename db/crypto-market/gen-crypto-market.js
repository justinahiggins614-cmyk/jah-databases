(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function p2(n){return String(n).padStart(2,'0');}
var CATS=['large','mid','small'];
var PRE=['Nova','Quantum','Orbit','Stellar','Hyper','Neo','Aero','Lumen','Zenith','Pulse','Vortex','Atlas','Echo','Flux','Ion','Onyx','Prism','Sol','Kryo','Tidal'];
var SUF=['coin','chain','token','cash','pay','net','link','swap','mint','vault'];
var LET='ABCDEFGHIJKLMNOPQRSTUVWXYZ';
var MCAP_MIN={large:1000000001,mid:10000000,small:1};
var MCAP_MID={large:2000000000,mid:200000000,small:2000000};
function cap(s){return s.charAt(0).toUpperCase()+s.slice(1);}
function tierOf(m){return m>1e9?'large':m>=1e7?'mid':'small';}
function mkP(rnd){
  var price=Number(Math.pow(10,-4+rnd()*9).toPrecision(8));
  var supply=Math.max(1,Math.round(Math.pow(10,2+rnd()*8)));
  var mcap=Math.round(price*supply);
  return {price:price,supply:supply,mcap:mcap};
}
function generate(seed,opts,rnd){
  rnd=rnd||prng(seed);
  var wantTier=(opts&&opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:(function(){var x=rnd();return x<0.15?'large':x<0.45?'mid':'small';})();
  var p=mkP(rnd), tries=0;
  while((tierOf(p.mcap)!==wantTier||p.mcap<1000)&&tries<120){p=mkP(rnd);tries++;}
  if(tierOf(p.mcap)!==wantTier||p.mcap<1000){
    var target=MCAP_MID[wantTier];
    p.supply=Math.max(1,Math.round(target/p.price));
    p.mcap=Math.round(p.price*p.supply);
  }
  var tier=tierOf(p.mcap), price=p.price, supply=p.supply, mcap=p.mcap;
  var name=cap(pick(PRE,rnd))+pick(SUF,rnd);
  var slen=ri(rnd,2,5), symbol='';
  for(var i=0;i<slen;i++)symbol+=LET[(rnd()*26)|0];
  var exchanges=ri(rnd,1,40);
  var launch=ri(rnd,2015,2026)+'-'+p2(ri(rnd,1,12))+'-'+p2(ri(rnd,1,28));
  var id='JAH-CRYPTO-'+String(seed).padStart(6,'0');
  var desc=name+' ('+symbol+') trades at $'+price+' with a market cap of $'+mcap.toLocaleString('en-US')+' ('+tier+' cap), '+supply.toLocaleString('en-US')+' in circulation across '+exchanges+' exchanges. Launched '+launch+'.';
  return {id:id,token_id:id,title:name+' ('+symbol+')',description:desc.slice(0,600),
    symbol:symbol,name:name,price_usd:price,market_cap:mcap,
    circulating_supply:supply,exchange_count:exchanges,launch_date:launch,tier:tier};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['record']};
  if(typeof r.id!=='string'||!/^JAH-CRYPTO-\d{6}$/.test(r.id))e.push('id');
  if(r.token_id!==r.id)e.push('token_id');
  if(r.title!==r.name+' ('+r.symbol+')')e.push('title');
  if(typeof r.description!=='string'||!r.description||r.description.length>600)e.push('description');
  if(typeof r.symbol!=='string'||!/^[A-Z]{2,5}$/.test(r.symbol))e.push('symbol');
  if(typeof r.name!=='string'||!r.name)e.push('name');
  if(typeof r.price_usd!=='number'||r.price_usd<=0)e.push('price_usd');
  if(typeof r.market_cap!=='number'||r.market_cap<=0)e.push('market_cap');
  if(typeof r.circulating_supply!=='number'||r.circulating_supply<1)e.push('circulating_supply');
  if(Math.abs(r.price_usd*r.circulating_supply-r.market_cap)/r.market_cap>0.02)e.push('mcap_consistency');
  if(typeof r.exchange_count!=='number'||r.exchange_count<1||r.exchange_count%1!==0)e.push('exchange_count');
  if(typeof r.launch_date!=='string'||!/^\d{4}-\d{2}-\d{2}$/.test(r.launch_date))e.push('launch_date');
  if(CATS.indexOf(r.tier)<0)e.push('tier');
  else{
    if(r.tier==='large'&&!(r.market_cap>1e9))e.push('tier_large');
    if(r.tier==='mid'&&!(r.market_cap>=1e7&&r.market_cap<=1e9))e.push('tier_mid');
    if(r.tier==='small'&&!(r.market_cap<1e7))e.push('tier_small');
  }
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-crypto-market-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('crypto-market',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;})();
