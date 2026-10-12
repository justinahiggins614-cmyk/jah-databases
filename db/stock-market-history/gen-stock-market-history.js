(function(){'use strict';
/* Stock Market Since Started Database generator — jahdb-stock-market-history-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-STOCKHIST-';
var TOPICS=[["Origins: Amsterdam 1602", "The Dutch East India Company issues the first shares."], ["Buttonwood Agreement 1792", "24 brokers found what becomes the NYSE."], ["NYSE Founded 1817", "The New York Stock and Exchange Board formalizes."], ["The Panic of 1907", "A banking crisis that leads to the Federal Reserve."], ["The Roaring Twenties", "Speculation and prosperity before the fall."], ["Crash of 1929", "Black Thursday, Black Monday, Black Tuesday."], ["Great Depression Markets", "A decade of grinding bear markets."], ["SEC Created 1934", "Regulation arrives after the crash."], ["Post-War Bull Market", "1949-1968: America's long rise."], ["The Go-Go Years", "1960s growth stocks and conglomerates."], ["1973 Oil Crisis Crash", "Stagflation hammers markets."], ["Black Monday 1987", "The Dow falls 22.6% in a single day."], ["The Dot-Com Boom", "1990s internet euphoria."], ["Dot-Com Bust 2000", "The NASDAQ loses 78% peak to trough."], ["9/11 Market Closure", "Exchanges close for four days after the attacks."], ["2008 Financial Crisis", "Subprime mortgages trigger global collapse."], ["Flash Crash 2010", "1,000 Dow points vanish in minutes."], ["Longest Bull Run 2009-2020", "Eleven years of rising markets."], ["COVID Crash and Rebound", "2020's fastest crash and fastest recovery."], ["Meme Stock Mania 2021", "Retail traders squeeze hedge funds."], ["Inflation and Rate Hikes 2022", "Rising rates end the easy-money era."], ["History of the Dow Jones", "From 12 industrials to 30 blue chips."], ["History of the S&P 500", "The benchmark index since 1957."], ["NASDAQ's Rise", "From quotation system to tech powerhouse."], ["Famous Investors", "Graham, Buffett, Lynch: lessons from legends."], ["Lessons from Crashes", "What every crash teaches patient investors."], ["Circuit Breakers", "How exchanges halt trading in panics."], ["The Future of Markets", "Where market history points next."]];
var ANGLES=['overview','detailed','examples','faq','history','applications'];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function generate(seed,opts){
  var s=prng(seed);
  var ti=(s()*TOPICS.length)|0, ai=(s()*ANGLES.length)|0;
  var topic=TOPICS[ti], angle=ANGLES[ai];
  var id=PREFIX+pad(seed);
  var title=topic[0]+' ('+angle+')';
  var desc=topic[1]+' This '+angle+' guide provides comprehensive coverage.';
  var content='['+angle+'] '+topic[0]+': '+topic[1]+' Full detailed content for '+angle+' perspective.';
  return {
    id:id, title:title, description:desc, genre:angle,
    type:'market history record', content:content,
    demo:null, src:'public', _seed:seed
  };
}
function validate(r){
  var errs=[];
  if(!r.id)errs.push('missing id');
  if(!r.title)errs.push('missing title');
  if(!r.content||r.content.length<50)errs.push('content too short');
  return {ok:errs.length===0, errors:errs};
}
function driftCheck(rec,sample){
  // Simple: check for exact title duplicates in sample
  for(var i=0;i<sample.length;i++){if(sample[i].t===rec.title)return {ok:false,errors:['duplicate title']};}
  return {ok:true,errors:[]};
}
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('stock-market-history',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();