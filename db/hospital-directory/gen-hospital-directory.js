/* ✳ JAH Hospital Directory Database generator. Property of Justin Addam Higgins (JAH).
   Deterministic (seeded) facility record generator: jahdb-hospital-directory-1.0.
   All facilities are synthetically generated directory entries. */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(s,r){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function pad(n){return String(n).padStart(6,'0');}

var CATS=['hospital','clinic','urgent-care','specialty','rehab'];
var PRE=['Riverside','Lakeside','Summit','Cedar','Willow','Granite','Harbor','Meadow','Brook','Stone','Pine','Elm','Maple','Birch','Aspen','Redwood','Blue','Golden','Silver','Copper','Prairie','Desert','Ocean','Mountain'];
var KIND={hospital:['General Hospital','Medical Center','Community Hospital','Regional Hospital'],clinic:['Family Clinic','Health Clinic','Community Clinic','Care Clinic'], 'urgent-care':['Urgent Care Center','Express Care Clinic','After-Hours Care'],specialty:['Heart Center','Orthopedic Institute','Cancer Center','Neurology Institute','Pediatric Center'],rehab:['Rehabilitation Center','Recovery Hospital','Physical Therapy Center']};
var CITIES=['Springfield','Riverdale','Lakeside','Cedar Falls','Brookfield','Fairview','Maple Grove','Hillcrest','Oakdale','Pinehurst','Westfield','Northgate','Elmwood','Clearwater','Stonebridge','Meadowbrook','Sunnyvale','Ridgemont','Ashford','Granite City','Willow Creek','Bayport','Summit','Harborview','Kingsport','Milltown','Eastvale','Portside','Fairhaven','Crestview'];
var SPECS=['cardiology','oncology','orthopedics','pediatrics','neurology','emergency medicine','radiology','surgery','primary care','dermatology','psychiatry','obstetrics','geriatrics','physical therapy','ophthalmology','urology','endocrinology','pulmonology'];
var BED_RANGE={hospital:[100,900],clinic:[0,30],'urgent-care':[0,20],specialty:[50,300],rehab:[40,200]};

function uniqPick(rnd,arr,n){
  var out=[],used={},tries=0;
  while(out.length<n&&tries<60){tries++;var v=pick(rnd,arr);if(!used[v]){used[v]=1;out.push(v);}}
  return out;
}
function generate(seed,opts,rnd){
  rnd=rnd||prng(seed);
  var cat=(opts&&opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:pick(rnd,CATS);
  var name=pick(rnd,PRE)+' '+pick(rnd,KIND[cat]);
  var br=BED_RANGE[cat];
  var rating=Math.round((1.0+rnd()*4.0)*10)/10;
  return {
    id:'JAH-HOSP-'+pad(seed),
    facility_id:'JAH-HOSP-'+pad(seed),
    name:name,
    type:cat,
    city:pick(rnd,CITIES),
    specialties:uniqPick(rnd,SPECS,ri(rnd,2,5)),
    beds:ri(rnd,br[0],br[1]),
    rating:rating,
    accepting_patients:rnd()<0.8,
    phone:'+1-555-01'+String(ri(rnd,0,99)).padStart(2,'0')+String(ri(rnd,0,99)).padStart(2,'0')
  };
}
function validate(r){
  var e=[];
  if(typeof r.id!=='string'||!/^JAH-HOSP-\d{6}$/.test(r.id))e.push('id');
  if(typeof r.facility_id!=='string'||r.facility_id!==r.id)e.push('facility_id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(CATS.indexOf(r.type)<0)e.push('type');
  if(typeof r.city!=='string'||!r.city.length)e.push('city');
  if(!Array.isArray(r.specialties)||r.specialties.length<2||r.specialties.length>5||r.specialties.some(function(s){return typeof s!=='string'||!s.length;}))e.push('specialties');
  if(typeof r.beds!=='number'||r.beds<0||r.beds!==Math.floor(r.beds))e.push('beds');
  if(typeof r.rating!=='number'||r.rating<1.0||r.rating>5.0)e.push('rating');
  if(typeof r.accepting_patients!=='boolean')e.push('accepting_patients');
  if(typeof r.phone!=='string'||!/^\+1-555-01\d{4}$/.test(r.phone))e.push('phone');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-hospital-directory-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('hospital-directory',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
