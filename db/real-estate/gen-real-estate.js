(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function p2(n){return String(n).padStart(2,'0');}
var CATS=['house','condo','apartment','land','townhouse'];
var STREETS=['Oakwood','Maple','Cedar','Pine','Elm','Birch','Willow','Aspen','Hickory','Laurel','Magnolia','Sycamore','Juniper','Redwood'];
var ENDS=['Street','Drive','Avenue','Lane','Court','Boulevard','Way','Terrace'];
var CITY=['Austin','Denver','Portland','Chicago','Boston','Seattle','Miami','Phoenix','Nashville','Atlanta','Dallas','Minneapolis','Raleigh','Charlotte','Columbus','Indianapolis','Kansas City','Cleveland','Pittsburgh','Boise'];
var PPSF={house:[140,420],townhouse:[150,380],condo:[180,520],apartment:[150,450],land:[8,60]};
var SQFT={house:[900,4500],townhouse:[900,2800],condo:[500,1800],apartment:[400,1400],land:[2000,40000]};
function generate(seed,opts,rnd){
  rnd=rnd||prng(seed);
  var ptype=(opts&&opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:pick(CATS,rnd);
  var address=ri(rnd,1,9999)+' '+pick(STREETS,rnd)+' '+pick(ENDS,rnd);
  var city=pick(CITY,rnd);
  var beds,baths;
  if(ptype==='land'){beds=0;baths=0;}
  else if(ptype==='house'){beds=ri(rnd,2,6);baths=ri(rnd,1,beds);}
  else if(ptype==='townhouse'){beds=ri(rnd,2,5);baths=ri(rnd,1,beds);}
  else if(ptype==='condo'){beds=ri(rnd,1,4);baths=ri(rnd,1,beds);}
  else {beds=ri(rnd,1,3);baths=ri(rnd,1,beds+1);}
  var sr=SQFT[ptype], sqft=ri(rnd,sr[0],sr[1]);
  var pr=PPSF[ptype], ppsf=pr[0]+rnd()*(pr[1]-pr[0]);
  var price=Math.round(sqft*ppsf/1000)*1000;
  var sold=ri(rnd,2021,2026)+'-'+p2(ri(rnd,1,12))+'-'+p2(ri(rnd,1,28));
  var id='JAH-PROP-'+String(seed).padStart(6,'0');
  var desc=(beds?beds+'bd/'+baths+'ba ':'')+ptype+' at '+address+', '+city+'. '+sqft.toLocaleString('en-US')+' sqft listed at $'+price.toLocaleString('en-US')+'.';
  return {id:id,property_id:id,address:address,title:address,description:desc.slice(0,600),
    city:city,ptype:ptype,beds:beds,baths:baths,sqft:sqft,list_price:price,last_sold_date:sold};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['record']};
  if(typeof r.id!=='string'||!/^JAH-PROP-\d{6}$/.test(r.id))e.push('id');
  if(r.property_id!==r.id)e.push('property_id');
  if(typeof r.address!=='string'||!r.address)e.push('address');
  if(r.title!==r.address)e.push('title');
  if(typeof r.description!=='string'||!r.description||r.description.length>600)e.push('description');
  if(typeof r.city!=='string'||!r.city)e.push('city');
  if(CATS.indexOf(r.ptype)<0)e.push('ptype');
  if(typeof r.beds!=='number'||r.beds<0||typeof r.baths!=='number'||r.baths<0)e.push('bedsbaths');
  if(typeof r.sqft!=='number'||r.sqft<=0)e.push('sqft');
  if(typeof r.list_price!=='number'||r.list_price<=0)e.push('list_price');
  if(typeof r.last_sold_date!=='string'||!/^\d{4}-\d{2}-\d{2}$/.test(r.last_sold_date))e.push('last_sold_date');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-real-estate-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('real-estate',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;})();
