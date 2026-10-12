(function(){'use strict';
/* JAH Public Magazines Database generator — jahdb-public-magazines-1.0.
   Property of Justin Addam Higgins (JAH).
   Archive of ALL public magazines — current and historical, worldwide.
   Seeded records are REAL magazines (Type 1 public info — name, founding
   year, publisher are public facts). Generated records are CLEARLY labeled
   samples (src:"signature-generated-sample") — never presented as real
   magazines. Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var PREFIX='JAH-MAG-';
var CATEGORIES=['news','science','fashion','sports','entertainment','technology','business','culture','history','nature','health','food','travel','art','music','literature','children','home','automotive','general'];
var CAT_LABEL={'news':'News & Current Affairs','science':'Science','fashion':'Fashion & Style','sports':'Sports','entertainment':'Entertainment','technology':'Technology','business':'Business & Finance','culture':'Culture','history':'History','nature':'Nature & Environment','health':'Health & Wellness','food':'Food & Cooking','travel':'Travel','art':'Art & Design','music':'Music','literature':'Literature','children':"Children's",'home':'Home & Garden','automotive':'Automotive','general':'General Interest'};
var COUNTRIES=[
 ['United States','US'],['United Kingdom','UK'],['Canada','CA'],['Australia','AU'],
 ['Germany','DE'],['France','FR'],['Japan','JP'],['Italy','IT'],
 ['Spain','ES'],['Brazil','BR'],['Netherlands','NL'],['India','IN'],
 ['Mexico','MX'],['South Africa','ZA'],['Sweden','SE'],['China','CN']
];
var NAME_A=['Global','Modern','Classic','Prime','Ever','True','Grand','Bright','Clear','Bold','Fresh','Prime','Vivid','Noble','Prime'];
var NAME_B=['Review','Journal','Digest','Chronicle','Herald','Companion','Observer','Pioneer','Beacon','Atlas','Compass','Ledger','Forum','Scope','Vision'];
var PUBLISHERS=['Meridian Press','Halcyon Media','Northgate Publishing','Bluebird House','Crestline Media','Foxglove Press','Ironwood Publishing','Larkspur Media'];
var FREQ=['Weekly','Monthly','Biweekly','Quarterly','Bimonthly'];
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var cat=opts.category&&CATEGORIES.indexOf(opts.category)>=0?opts.category:pick(CATEGORIES,rnd);
  var ctry=opts.country||pick(COUNTRIES,rnd);
  var country=Array.isArray(ctry)?ctry[0]:ctry;
  var code=Array.isArray(ctry)?ctry[1]:'XX';
  var name=pick(NAME_A,rnd)+' '+CAT_LABEL[cat].split(' ')[0]+' '+pick(NAME_B,rnd);
  var founded=ri(rnd,1890,2020);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:name,
    title:name+' — '+country,
    description:'SAMPLE MAGAZINE LISTING (generated — not a real magazine). A '+CAT_LABEL[cat].toLowerCase()+' magazine directory entry for '+country+'. Generated samples must never be treated as real publications.',
    magazine_name:name,
    publisher:pick(PUBLISHERS,rnd),
    founded:founded,
    frequency:pick(FREQ,rnd),
    country:country,
    country_code:code,
    category:cat,
    category_label:CAT_LABEL[cat],
    language:pick(['English','English','English','Spanish','French','German','Portuguese'],rnd),
    issn:'ISSN '+ri(rnd,1000,9999)+'-'+ri(rnd,1000,9999)+' (sample)',
    year:2026,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample listing — not a real magazine. Seeded archive records are real magazines; this generated record is structural only.',
    demo:{kind:'catalog-card',program:"function magCard(m){return m.magazine_name+' ('+m.founded+') — '+m.publisher+'; '+m.frequency+', '+m.country;}",note:'Paste into any JS console with a magazine record to render a one-line catalog card.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-MAG-\d{6}$/.test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||r.name.length<3)e.push('name');
  if(typeof r.founded!=='number'||r.founded<1800||r.founded>2026)e.push('founded');
  if(typeof r.publisher!=='string'||!r.publisher)e.push('publisher');
  if(CATEGORIES.indexOf(r.category)<0)e.push('category');
  if(typeof r.country!=='string'||!r.country)e.push('country');
  if(!r.src)e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.magazine_name===record.magazine_name&&r.country===record.country;});
  return dups.length?{ok:false,errors:['duplicate name+country in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-public-magazines-1.0',generate:generate,validate:validate,driftCheck:driftCheck,categories:CATEGORIES,countryList:COUNTRIES.map(function(c){return c[0];})};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-magazines',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
