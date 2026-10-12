(function(){'use strict';
/* JAH Global White Pages Database generator — jahdb-global-white-pages-1.0.
   Property of Justin Addam Higgins (JAH).
   Public directory of PUBLIC listings only: public offices, embassies,
   helplines, professional associations, public-figure offices.
   PRIVACY RULE: this generator NEVER invents personal/residential phone
   numbers. Generated records are institutional samples only, clearly
   labeled (src:"signature-generated-sample"). Deterministic. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var PREFIX='JAH-WP-';
var TYPES=['public-office','embassy-consulate','helpline','professional-association','public-figure-office'];
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
var OFFICE_A=['Harborview','Northgate','Lakeside','Brookfield','Stonebridge','Fairview','Elmwood','Clearwater','Maplewood','Ridgemont'];
var OFFICE_B={'public-office':'Community Services Office','embassy-consulate':'Consular Services Desk','helpline':'Public Helpline Center','professional-association':'Professional Association Chapter','public-figure-office':'Public Liaison Office'};
var ADDR=['Civic Plaza','Government Row','Embassy District','Public Square','Liberty Avenue','Constitution Way'];
function samplePhone(s,cc){
  var n=ri(s,1000,1999);
  return cc+'-555-0'+n;
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var lt=opts.listing_type&&TYPES.indexOf(opts.listing_type)>=0?opts.listing_type:pick(TYPES,rnd);
  var ctry=opts.country||pick(COUNTRIES,rnd);
  var country=Array.isArray(ctry)?ctry[0]:ctry;
  var cc=Array.isArray(ctry)?ctry[1]:(function(){for(var i=0;i<COUNTRIES.length;i++){if(COUNTRIES[i][0]===country)return COUNTRIES[i][1];}return '+1';})();
  var name=pick(OFFICE_A,rnd)+' '+OFFICE_B[lt];
  var phone=samplePhone(rnd,cc);
  var addr=ri(rnd,1,200)+' '+pick(ADDR,rnd);
  var year=2026;
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:name,
    title:name+' — '+lt.replace(/-/g,' '),
    description:'SAMPLE LISTING (generated — not a real office). A '+lt.replace(/-/g,' ')+' directory entry for '+country+', in the format of the Global White Pages. This directory lists PUBLIC offices and helplines only — never private residential numbers. Generated sample phones use the fictional 555 range.',
    phone:phone,
    address:addr,
    country:country,
    listing_type:lt,
    year:year,
    src:'signature-generated-sample',
    sample:true,
    privacy:'This database carries PUBLIC listings only. Private personal residential numbers are never collected, never generated, never stored.',
    disclaimer:'Generated sample listing — not a real office. Seeded archive records are real publicly-listed numbers; this generated record is structural only.',
    demo:{kind:'phone-format-check',program:"function fmt(p){return /^\\+\\d{1,4}-\\d{3}-\\d{4}$/.test(p)?'valid format':'check digits';}",note:'Paste into any JS console to validate directory phone formats.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-WP-\d{6}$/.test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||r.name.length<3)e.push('name');
  if(typeof r.phone!=='string'||r.phone.length<7)e.push('phone');
  if(typeof r.country!=='string'||!r.country)e.push('country');
  if(TYPES.indexOf(r.listing_type)<0)e.push('listing_type');
  if(typeof r.year!=='number')e.push('year');
  if(!r.src)e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.name===record.name&&r.country===record.country;});
  return dups.length?{ok:false,errors:['duplicate name+country in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-global-white-pages-1.0',generate:generate,validate:validate,driftCheck:driftCheck,listing_types:TYPES,countries:COUNTRIES.map(function(c){return c[0];})};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('global-white-pages',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
