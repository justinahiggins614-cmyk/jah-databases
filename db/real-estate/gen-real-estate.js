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
/* Real-estate expansion: leases, zoning, mortgages, valuation, ownership, facilities, maintenance.
   Records stay compatible with the listing schema (validate extended only to accept new ptypes). */
var NEW_CATS=['lease','zoning','mortgage','valuation','ownership','facility','maintenance'];
var EXPAND_AFTER=10001;
var LEASE_TERMS=['12-month fixed','24-month fixed','month-to-month','6-month short term'];
var ZONE_CLASSES=[['R-1 Single-family','detached homes only, 6000 sqft min lot'],['R-2 Multi-family','duplexes and small apartments permitted'],['C-1 Neighborhood commercial','retail and office with residential above'],['M-1 Light industrial','warehousing and light manufacturing'],['PUD Planned unit','mixed-use under master plan approval']];
var LOAN_TYPES=['30-year fixed','15-year fixed','5/1 ARM','FHA loan'];
function genExpansion(seed,opts){
  var rnd=prng(seed^0x3e7a);
  var fam=(opts&&opts.category&&NEW_CATS.indexOf(opts.category)>=0)?opts.category:NEW_CATS[(seed-EXPAND_AFTER-1)%NEW_CATS.length];
  var address=ri(rnd,1,9999)+' '+pick(STREETS,rnd)+' '+pick(ENDS,rnd);
  var city=pick(CITY,rnd);
  var id='JAH-PROP-'+String(seed).padStart(6,'0');
  var beds=ri(rnd,1,5), baths=ri(rnd,1,beds), sqft=ri(rnd,600,4000);
  var price, desc, date=p2(ri(rnd,1,12));
  var ymd=ri(rnd,2021,2026)+'-'+p2(ri(rnd,1,12))+'-'+p2(ri(rnd,1,28));
  if(fam==='lease'){
    price=ri(rnd,900,4500);
    desc='Lease listing: '+beds+'bd/'+baths+'ba property at '+address+', '+city+'. '+pick(LEASE_TERMS,rnd)+' at $'+price.toLocaleString('en-US')+'/mo. '+sqft.toLocaleString('en-US')+' sqft. Security deposit one month. Application and screening required.';
  }else if(fam==='zoning'){
    var z=pick(ZONE_CLASSES,rnd); price=ri(rnd,50000,900000); sqft=ri(rnd,4000,60000); beds=0; baths=0;
    desc='Zoning record: parcel at '+address+', '+city+' classified '+z[0]+' ('+z[1]+'). Lot '+sqft.toLocaleString('en-US')+' sqft, assessed $'+price.toLocaleString('en-US')+'. Verify setbacks and permitted uses with the planning office before purchase.';
  }else if(fam==='mortgage'){
    price=ri(rnd,120000,850000);
    var lt=pick(LOAN_TYPES,rnd);
    desc='Mortgage profile: '+lt+' on property at '+address+', '+city+'. Loan amount $'+price.toLocaleString('en-US')+' for a '+beds+'bd/'+baths+'ba, '+sqft.toLocaleString('en-US')+' sqft home. Illustrative terms; consult a licensed lender for actual rates and qualification.';
  }else if(fam==='valuation'){
    price=ri(rnd,150000,1200000);
    desc='Valuation: '+address+', '+city+' appraised at $'+price.toLocaleString('en-US')+' ('+beds+'bd/'+baths+'ba, '+sqft.toLocaleString('en-US')+' sqft). Based on comparable recent sales in the area. Appraisals are opinions of value, not guarantees.';
  }else if(fam==='ownership'){
    price=ri(rnd,150000,1200000);
    var own=pick(['fee simple','condominium','cooperative','leasehold'],rnd);
    desc='Ownership record: '+address+', '+city+' held as '+own+'. '+beds+'bd/'+baths+'ba, '+sqft.toLocaleString('en-US')+' sqft, last recorded value $'+price.toLocaleString('en-US')+'. Title and encumbrance details require a professional title search.';
  }else if(fam==='facility'){
    price=ri(rnd,200000,3000000); sqft=ri(rnd,5000,80000); beds=0; baths=ri(rnd,1,6);
    var ft=pick(['office building','retail center','warehouse','medical plaza'],rnd);
    desc='Facility record: '+ft+' at '+address+', '+city+'. '+sqft.toLocaleString('en-US')+' sqft, listed at $'+price.toLocaleString('en-US')+'. Includes parking, HVAC and common-area specs. Inspect building systems before offer.';
  }else{
    price=ri(rnd,200,8000);
    var mt=pick(['roof replacement','HVAC service','plumbing repair','electrical upgrade','landscaping contract','pest control plan'],rnd);
    desc='Maintenance record: '+mt+' for property at '+address+', '+city+' ('+beds+'bd/'+baths+'ba). Estimated cost $'+price.toLocaleString('en-US')+'. Get licensed quotes; costs vary by scope and region.';
  }
  var title=address+' ['+fam+']';
  return {id:id,property_id:id,address:address,title:title,description:desc.slice(0,600),
    city:city,ptype:fam,beds:beds,baths:baths,sqft:sqft,list_price:price,last_sold_date:ymd};
}

function generate(seed,opts,rnd){
  rnd=rnd||prng(seed);
  if(seed>EXPAND_AFTER)return genExpansion(seed,opts);
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
  if(NEW_CATS.indexOf(r.ptype)<0&&r.title!==r.address)e.push('title');
  if(typeof r.description!=='string'||!r.description||r.description.length>600)e.push('description');
  if(typeof r.city!=='string'||!r.city)e.push('city');
  if((CATS.concat(NEW_CATS)).indexOf(r.ptype)<0)e.push('ptype');
  if(typeof r.beds!=='number'||r.beds<0||typeof r.baths!=='number'||r.baths<0)e.push('bedsbaths');
  if(typeof r.sqft!=='number'||r.sqft<=0)e.push('sqft');
  if(typeof r.list_price!=='number'||r.list_price<=0)e.push('list_price');
  if(typeof r.last_sold_date!=='string'||!/^\d{4}-\d{2}-\d{2}$/.test(r.last_sold_date))e.push('last_sold_date');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-real-estate-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('real-estate',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;})();
