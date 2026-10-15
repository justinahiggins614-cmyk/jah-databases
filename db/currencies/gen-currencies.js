(function(){'use strict';
/* Currencies Database generator — jahdb-currencies-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-CURRENCY-';
var TOPICS=[["US Dollar", "The currency of the United States, code USD, the world's main reserve currency."], ["Euro", "The shared currency of many European Union countries, code EUR."], ["British Pound", "The currency of the United Kingdom, code GBP, one of the oldest still in use."], ["Japanese Yen", "The currency of Japan, code JPY."], ["Swiss Franc", "The currency of Switzerland, code CHF, known for stability."], ["Canadian Dollar", "The currency of Canada, code CAD."], ["Australian Dollar", "The currency of Australia, code AUD."], ["Chinese Yuan", "The currency of China, code CNY, also called the renminbi."], ["Indian Rupee", "The currency of India, code INR."], ["Mexican Peso", "The currency of Mexico, code MXN."], ["Brazilian Real", "The currency of Brazil, code BRL."], ["Russian Ruble", "The currency of Russia, code RUB."], ["South African Rand", "The currency of South Africa, code ZAR."], ["Swedish Krona", "The currency of Sweden, code SEK."], ["Norwegian Krone", "The currency of Norway, code NOK."], ["South Korean Won", "The currency of South Korea, code KRW."], ["Thai Baht", "The currency of Thailand, code THB."], ["Turkish Lira", "The currency of Turkey, code TRY."], ["Egyptian Pound", "The currency of Egypt, code EGP."], ["Nigerian Naira", "The currency of Nigeria, code NGN."], ["Exchange Rates", "The price of one currency in terms of another, changing with markets."], ["Inflation", "The general rise of prices that reduces what money can buy."], ["Central Banks", "The institutions that issue currency and guide monetary policy."], ["Coins and Banknotes", "The physical forms of money used in everyday transactions."], ["Cryptocurrency", "Digital currencies, such as Bitcoin, secured by cryptography."], ["The Gold Standard", "The historical system tying currency value to gold."], ["Foreign Exchange Market", "The global market where currencies are traded."], ["Currency Symbols", "The signs like $, euro, pound, and yen that stand for currencies."], ["Digital Payments", "Electronic ways of paying, from cards to mobile wallets."], ["Devaluation", "When a currency officially loses value against others."]];
var ANGLES=['overview','detailed','examples','faq','history','applications'];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function generate(seed,opts){
  var s=prng(seed);
  var ti=(s()*TOPICS.length)|0, ai=(s()*ANGLES.length)|0;
  var topic=TOPICS[ti], angle=ANGLES[ai];
  var id=PREFIX+pad(seed);
  var title=topic[0]+' ('+angle+')';
  var desc=topic[1];
  var content=topic[0]+' \u2014 '+topic[1];
  return {
    id:id, title:title, description:desc, genre:angle,
    type:'currencies record', content:content, content_completeness:'stub',
    stub_note:'Topic stub: the topic title and its one-line brief are real; the full guide article is not yet written. This record does not present shell text as a complete guide.',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('currencies',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();