(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function p2(n){return String(n).padStart(2,'0');}
function r2(x){return Math.round(x*100)/100;}
var CATS=['technology','finance','healthcare','energy','consumer','industrial'];
var LET='ABCDEFGHIJKLMNOPQRSTUVWXYZ';
/* Zeller's congruence: 0=Sat,1=Sun — shift weekend dates back to Friday. Deterministic. */
function zeller(y,m,d){if(m<3){m+=12;y-=1;}var K=y%100,J=(y/100)|0;return (d+((13*(m+1)/5)|0)+K+((K/4)|0)+((J/4)|0)+5*J)%7;}
function generate(seed,opts,rnd){
  opts=opts||{};
  if(opts.asset_class&&ASSET_CLASSES.indexOf(opts.asset_class)>=0)return generateAsset(seed,opts,rnd);
  rnd=rnd||prng(seed);
  var sector=(opts&&opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:pick(CATS,rnd);
  var len=ri(rnd,1,5), ticker='';
  for(var i=0;i<len;i++)ticker+=LET[(rnd()*26)|0];
  var exchange=pick(['NYSE','NASDAQ'],rnd);
  var y=ri(rnd,2024,2026), m=ri(rnd,1,12), d=ri(rnd,3,28);
  var h=zeller(y,m,d);
  if(h===0)d-=1; else if(h===1)d-=2;
  var date=y+'-'+p2(m)+'-'+p2(d);
  var base=ri(rnd,500,80000)/100;
  var open=r2(base*(0.97+rnd()*0.06));
  var close=r2(base*(0.97+rnd()*0.06));
  var high=r2(Math.max(open,close)*(1+rnd()*0.04));
  var low=r2(Math.min(open,close)*(1-rnd()*0.04));
  var volume=ri(rnd,50000,80000000);
  var id='JAH-STK-'+String(seed).padStart(6,'0');
  var desc=ticker+' ('+exchange+') '+date+': open $'+open+', high $'+high+', low $'+low+', close $'+close+', volume '+volume.toLocaleString('en-US')+'.';
  return {id:id,ticker:ticker,title:ticker+' '+date,description:desc.slice(0,600),
    exchange:exchange,date:date,open:open,high:high,low:low,close:close,
    volume:volume,sector:sector};
}
/* ============ EXPANSION 2026-10-17 (audit item 56) ============
   Commodity, FX, and futures price records plus pricing-methodology records.
   Opt-in via opts.asset_class='commodity'|'fx'|'futures'|'methodology';
   the equity OHLCV path is untouched. */
var ASSET_CLASSES=['commodity','fx','futures','methodology'];
var COMMODITIES=[['XAU','Gold','COMEX'],['XAG','Silver','COMEX'],['WTI','WTI Crude Oil','NYMEX'],['BRENT','Brent Crude Oil','ICE'],['NATGAS','Natural Gas','NYMEX'],['CORN','Corn','CBOT'],['WHEAT','Wheat','CBOT'],['COPPER','Copper','COMEX']];
var FX_PAIRS=[['EURUSD','Euro / US Dollar'],['GBPUSD','British Pound / US Dollar'],['USDJPY','US Dollar / Japanese Yen'],['USDCHF','US Dollar / Swiss Franc'],['AUDUSD','Australian Dollar / US Dollar'],['USDCAD','US Dollar / Canadian Dollar'],['NZDUSD','New Zealand Dollar / US Dollar'],['EURGBP','Euro / British Pound']];
var FUTURES=[['ES','E-mini S&P 500','CME'],['NQ','E-mini Nasdaq-100','CME'],['CL','WTI Crude Oil Future','NYMEX'],['GC','Gold Future','COMEX'],['ZC','Corn Future','CBOT'],['6E','Euro FX Future','CME'],['ZN','10-Year T-Note Future','CBOT'],['SI','Silver Future','COMEX']];
var METHOD_TOPICS=[
 ['Cost of carry','The cost-of-carry model prices futures from the spot price plus carrying costs minus convenience yield: F = S * e^((r + u - y) * T). For a non-dividend asset the forward price is the spot grown at the risk-free rate; storage costs (u) raise it and convenience yield (y) lowers it. The model explains contango (futures above spot) and backwardation (futures below spot) as the balance of carry versus convenience.'],
 ['Black-76 for options on futures','The Black-76 model values options on futures and forwards by treating the futures price as lognormally distributed with the option expiry as horizon. A call is worth e^(-rT) * (F * N(d1) - K * N(d2)), where F is the futures price and K the strike. It is the market-standard quoting model for commodity and rates options.'],
 ['Covered interest parity (FX forwards)','Covered interest rate parity pins the FX forward rate to the spot rate and the two risk-free rates: F = S * (1 + r_d)^T / (1 + r_f)^T. If parity breaks, arbitrageurs borrow in the cheap currency, convert, invest, and lock the forward — pushing the forward back in line. Persistent deviations signal funding stress or balance-sheet costs.'],
 ['Futures margin and leverage','Futures trade on margin: a fraction of notional (initial margin) plus daily mark-to-market variation margin. Leverage magnifies both gains and losses; a 5% adverse move on 20x leverage wipes the margin. Clearinghouses set margins from volatility (SPAN) and can raise them in stress, forcing deleveraging.'],
 ['Commodity curve structure','Commodity futures trade as a curve across expiries. Contango (upward-sloping) reflects storage costs and typically penalizes long roll positions; backwardation (downward-sloping) reflects scarcity and rewards them. Curve shape drives the economics of ETFs, hedgers, and storage operators.'],
 ['FX spot conventions','Spot FX quotes as base/quote: EURUSD 1.0850 means one euro buys 1.0850 dollars. Majors trade with tight spreads around the clock; value dates are T+2 (T+1 for some pairs). Pips, lots, and leverage conventions are standardized so a price means the same thing on every venue.']];
function assetDate(rnd){
  var y=ri(rnd,2024,2026),m=ri(rnd,1,12),d=ri(rnd,3,28);
  var h=zeller(y,m,d); if(h===0)d-=1; else if(h===1)d-=2;
  return y+'-'+p2(m)+'-'+p2(d);
}
function assetOHLC(rnd,base){
  var open=r2(base*(0.97+rnd()*0.06)), close=r2(base*(0.97+rnd()*0.06));
  var high=r2(Math.max(open,close)*(1+rnd()*0.04)), low=r2(Math.min(open,close)*(1-rnd()*0.04));
  return {open:open,high:high,low:low,close:close};
}
function generateAsset(seed,opts,rnd){
  rnd=rnd||prng(seed^0x77aa1);
  var ac=opts.asset_class, id='JAH-STK-'+String(seed).padStart(6,'0');
  if(ac==='methodology'){
    var mt=METHOD_TOPICS[(seed-10025)%METHOD_TOPICS.length];
    var mdesc='Pricing methodology record: '+mt[0]+'. '+mt[1]+' Methodology records document how the prices in this database are formed, quoted, and arbitraged — the theory behind the tape.';
    return {id:id,asset_class:'methodology',ticker:'METHOD',title:mt[0]+' — pricing methodology',
      description:mdesc.slice(0,900),topic:mt[0],methodology:mt[1],
      source:'synthetic',creation_mode:'SIGNATURE-GENERATED'};
  }
  var sym,name,exch,base;
  if(ac==='commodity'){var c=COMMODITIES[(seed-10001)%COMMODITIES.length];sym=c[0];name=c[1];exch=c[2];base=ri(rnd,20,9000)/10;}
  else if(ac==='fx'){var f=FX_PAIRS[(seed-10009)%FX_PAIRS.length];sym=f[0];name=f[1];exch='OTC-SPOT';base=ri(rnd,50,20000)/10000;}
  else{var u=FUTURES[(seed-10017)%FUTURES.length];sym=u[0];name=u[1];exch=u[2];base=ri(rnd,100,60000)/10;}
  var date=assetDate(rnd), o=assetOHLC(rnd,base);
  var volume=ac==='fx'?ri(rnd,1000000,50000000):ri(rnd,50000,80000000);
  var desc=sym+' ('+name+', '+exch+') '+date+': open '+o.open+', high '+o.high+', low '+o.low+', close '+o.close+', volume '+volume.toLocaleString('en-US')+'. '+ac.charAt(0).toUpperCase()+ac.slice(1)+' price record.';
  return {id:id,asset_class:ac,ticker:sym,symbol_name:name,title:sym+' '+date,
    description:desc.slice(0,600),exchange:exch,date:date,
    open:o.open,high:o.high,low:o.low,close:o.close,volume:volume,
    source:'synthetic',creation_mode:'SIGNATURE-GENERATED'};
}
function validateAsset(r,e){
  if(ASSET_CLASSES.indexOf(r.asset_class)<0)e.push('asset_class');
  if(typeof r.id!=='string'||!/^JAH-STK-\d{6}$/.test(r.id))e.push('id');
  if(r.asset_class==='methodology'){
    if(typeof r.topic!=='string'||!r.topic.length)e.push('topic');
    if(typeof r.methodology!=='string'||r.methodology.length<120)e.push('methodology');
    if(typeof r.title!=='string'||!r.title.length)e.push('title');
    if(typeof r.description!=='string'||!r.description.length||r.description.length>900)e.push('description');
    return {ok:!e.length,errors:e};
  }
  if(typeof r.ticker!=='string'||!r.ticker.length||r.ticker.length>6)e.push('ticker');
  if(r.title!==r.ticker+' '+r.date)e.push('title');
  if(typeof r.description!=='string'||!r.description||r.description.length>600)e.push('description');
  if(typeof r.exchange!=='string'||!r.exchange.length)e.push('exchange');
  if(typeof r.date!=='string'||!/^202[4-6]-\d{2}-\d{2}$/.test(r.date))e.push('date');
  var f=['open','high','low','close'];
  for(var i=0;i<f.length;i++){if(typeof r[f[i]]!=='number'||r[f[i]]<=0)e.push(f[i]);}
  if(r.low>Math.min(r.open,r.close))e.push('low_invariant');
  if(Math.max(r.open,r.close)>r.high)e.push('high_invariant');
  if(typeof r.volume!=='number'||r.volume<0||r.volume%1!==0)e.push('volume');
  return {ok:!e.length,errors:e};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['record']};
  if(r.asset_class&&ASSET_CLASSES.indexOf(r.asset_class)>=0)return validateAsset(r,e);
  if(typeof r.id!=='string'||!/^JAH-STK-\d{6}$/.test(r.id))e.push('id');
  if(typeof r.ticker!=='string'||!/^[A-Z]{1,5}$/.test(r.ticker))e.push('ticker');
  if(r.title!==r.ticker+' '+r.date)e.push('title');
  if(typeof r.description!=='string'||!r.description||r.description.length>600)e.push('description');
  if(r.exchange!=='NYSE'&&r.exchange!=='NASDAQ')e.push('exchange');
  if(typeof r.date!=='string'||!/^202[4-6]-\d{2}-\d{2}$/.test(r.date))e.push('date');
  var f=['open','high','low','close'];
  for(var i=0;i<f.length;i++){if(typeof r[f[i]]!=='number'||r[f[i]]<=0)e.push(f[i]);}
  if(r.low>Math.min(r.open,r.close))e.push('low_invariant');
  if(Math.max(r.open,r.close)>r.high)e.push('high_invariant');
  if(typeof r.volume!=='number'||r.volume<0||r.volume%1!==0)e.push('volume');
  if(CATS.indexOf(r.sector)<0)e.push('sector');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-stock-timeseries-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('stock-timeseries',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;})();
