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
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['record']};
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
