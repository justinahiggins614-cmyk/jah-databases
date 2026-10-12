(function(){'use strict';
/* JAH Global Yellow Pages Database generator — jahdb-global-yellow-pages-1.0.
   Property of Justin Addam Higgins (JAH).
   Business phone directory. Seeded records are REAL publicly-advertised
   business numbers (Type 1 public info). Generated records are CLEARLY
   labeled samples (src:"signature-generated-sample") — never presented
   as real businesses. Deterministic: same seed always makes the same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var PREFIX='JAH-YP-';
var CATEGORIES=['airlines','hotels','car-rental','shipping','cruise-lines','retail','restaurants','banks','insurance','pharmacies','tech-support','telecom','automotive','healthcare','home-services','travel-agencies','real-estate','legal-services','education','entertainment'];
var COUNTRIES=[
 ['United States','+1'],['United Kingdom','+44'],['Canada','+1'],['Australia','+61'],
 ['Germany','+49'],['France','+33'],['Japan','+81'],['India','+91'],
 ['Brazil','+55'],['Mexico','+52'],['Spain','+34'],['Italy','+39'],
 ['Netherlands','+31'],['Ireland','+353'],['New Zealand','+64'],['South Africa','+27'],
 ['United Arab Emirates','+971'],['Singapore','+65'],['Hong Kong','+852'],['South Korea','+82'],
 ['China','+86'],['Argentina','+54'],['Chile','+56'],['Colombia','+57'],
 ['Egypt','+20'],['Nigeria','+234'],['Kenya','+254'],['Sweden','+46'],
 ['Norway','+47'],['Switzerland','+41'],['Austria','+43'],['Belgium','+32'],
 ['Poland','+48'],['Portugal','+351'],['Greece','+30'],['Turkey','+90'],
 ['Thailand','+66'],['Malaysia','+60'],['Philippines','+63'],['Indonesia','+62']
];
var NAME_A=['Apex','Beacon','Crest','Harbor','Summit','Meridian','Cornerstone','Bluebird','Northstar','Ember','Willow','Cobalt','Juniper','Falcon','Meadow','Onyx','Pioneer','Quarry','Ridgeline','Saffron'];
var NAME_B={airlines:'Airways',hotels:'Grand Hotel','car-rental':'Rent-A-Car',shipping:'Express Freight','cruise-lines':'Cruise Line',retail:'Mart',restaurants:'Kitchen',banks:'Trust Bank',insurance:'Mutual Insurance',pharmacies:'Pharmacy','tech-support':'Tech Support',telecom:'Telecom',automotive:'Auto Care',healthcare:'Medical Center','home-services':'Home Services','travel-agencies':'Travel','real-estate':'Realty','legal-services':'Law Offices',education:'Learning Academy',entertainment:'Entertainment Co.'};
var ADDR=['Main Street','High Street','Market Road','Station Avenue','Park Lane','Broadway','Victoria Road','Church Street'];
function samplePhone(s,cc){
  var n=ri(s,1000,1999);
  return cc+'-555-0'+n;
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var cat=opts.category&&CATEGORIES.indexOf(opts.category)>=0?opts.category:pick(CATEGORIES,rnd);
  var ctry=opts.country||pick(COUNTRIES,rnd);
  var country=Array.isArray(ctry)?ctry[0]:ctry;
  var cc=Array.isArray(ctry)?ctry[1]:(function(){for(var i=0;i<COUNTRIES.length;i++){if(COUNTRIES[i][0]===country)return COUNTRIES[i][1];}return '+1';})();
  var name=pick(NAME_A,rnd)+' '+NAME_B[cat];
  var phone=samplePhone(rnd,cc);
  var addr=ri(rnd,1,999)+' '+pick(ADDR,rnd);
  var year=2026;
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:name,
    title:name+' — '+cat,
    description:'SAMPLE LISTING (generated — not a real business). A '+cat.replace(/-/g,' ')+' directory entry for '+country+', in the format of the Global Yellow Pages. Phone numbers in generated samples use the fictional 555 range and must never be dialed expecting a real business.',
    phone:phone,
    address:addr,
    country:country,
    category:cat,
    year:year,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample listing — not a real business. Seeded archive records are real publicly-advertised numbers; this generated record is structural only.',
    demo:{kind:'phone-format-check',program:"function fmt(p){return /^\\+\\d{1,4}-\\d{3}-\\d{4}$/.test(p)?'valid format':'check digits';}",note:'Paste into any JS console to validate directory phone formats.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-YP-\d{6}$/.test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||r.name.length<3)e.push('name');
  if(typeof r.phone!=='string'||r.phone.length<7)e.push('phone');
  if(typeof r.country!=='string'||!r.country)e.push('country');
  if(CATEGORIES.indexOf(r.category)<0)e.push('category');
  if(typeof r.year!=='number')e.push('year');
  if(!r.src)e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.name===record.name&&r.country===record.country;});
  return dups.length?{ok:false,errors:['duplicate name+country in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-global-yellow-pages-1.0',generate:generate,validate:validate,driftCheck:driftCheck,categories:CATEGORIES,countries:COUNTRIES.map(function(c){return c[0];})};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('global-yellow-pages',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
