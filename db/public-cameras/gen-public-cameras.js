(function(){'use strict';
/* JAH Public Cameras Database generator — jahdb-public-cameras-1.0.
   Property of Justin Addam Higgins (JAH).
   A MAP/DIRECTORY of where public recording happens worldwide.
   Location is the primary organizing principle: every record carries
   precise coordinates, address, and what's visible from the camera.
   Seeded records are REAL publicly-accessible cameras (Type 1 public info).
   Generated records are CLEARLY labeled samples (src:"signature-generated-sample")
   — never presented as real cameras. Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function rf(s,a,b){return a+s()*(b-a);}
var PREFIX='JAH-PCAM-';
var CATEGORIES=['city-landmark','nature-wildlife','traffic','weather','beach-surf','mountain-ski','airport','religious-site','space','harbor-port'];
var CAT_LABEL={'city-landmark':'City & Landmark','nature-wildlife':'Nature & Wildlife','traffic':'Traffic','weather':'Weather','beach-surf':'Beach & Surf','mountain-ski':'Mountain & Ski','airport':'Airport','religious-site':'Religious Site','space':'Space','harbor-port':'Harbor & Port'};
var COUNTRIES=[
 ['United States','US'],['United Kingdom','UK'],['Canada','CA'],['Australia','AU'],
 ['Germany','DE'],['France','FR'],['Japan','JP'],['Italy','IT'],
 ['Spain','ES'],['Brazil','BR'],['Netherlands','NL'],['Norway','NO'],
 ['Ireland','IE'],['Czech Republic','CZ'],['United Arab Emirates','AE'],['Jordan','JO'],
 ['Israel','IL'],['Iceland','IS'],['Mexico','MX'],['New Zealand','NZ']
];
/* Plausible coordinate bounds per country for generated samples */
var BOUNDS={
 'United States':[24.5,49.5,-125.0,-66.9],'United Kingdom':[49.8,58.8,-5.8,1.9],
 'Canada':[41.6,83.6,-141.0,-52.6],'Australia':[-39.0,-10.0,113.0,154.0],
 'Germany':[47.2,55.1,5.8,15.1],'France':[41.3,51.1,-5.2,9.6],
 'Japan':[30.9,45.6,128.9,146.0],'Italy':[35.4,47.1,6.6,18.6],
 'Spain':[35.9,43.9,-9.4,4.4],'Brazil':[-33.8,5.3,-73.9,-34.7],
 'Netherlands':[50.7,53.7,3.3,7.3],'Norway':[57.9,81.0,4.5,31.2],
 'Ireland':[51.4,55.4,-10.7,-5.9],'Czech Republic':[48.5,51.1,12.0,18.9],
 'United Arab Emirates':[22.6,26.1,51.5,56.4],'Jordan':[29.1,33.4,34.9,39.4],
 'Israel':[29.5,33.3,34.2,35.9],'Iceland':[63.3,66.6,-24.6,-13.4],
 'Mexico':[14.5,32.7,-117.2,-86.7],'New Zealand':[-46.7,-34.3,166.3,178.6]
};
var CITY_NAMES=['Harbor View','Summit Point','Old Town','Riverside','Northgate','Lakeside',' clifftop','Bayfront','Highland','Market Square','Cedar Park','Stonebridge','Elm District','Portside','Meadowbrook'];
var VISIBLE={
 'city-landmark':['city square and pedestrian traffic','historic buildings and street life','downtown skyline and public plaza','famous intersection from above'],
 'nature-wildlife':['forest clearing and visiting wildlife','river valley and surrounding hills','meadow with grazing animals','cliff face and nesting birds'],
 'traffic':['highway interchange and traffic flow','major intersection from overhead gantry','bridge deck and vehicle lanes','roundabout and approach roads'],
 'weather':['open sky and horizon for cloud tracking','valley panorama for storm watching','coastline for weather fronts','mountain ridge for snow monitoring'],
 'beach-surf':['sandy beach and surf break','boardwalk and shoreline','pier extending over waves','cove with swimmers and boats'],
 'mountain-ski':['ski slopes and lift lines','alpine peak and glacier','mountain pass and road conditions','resort base area and crowds'],
 'airport':['runway and taxiing aircraft','terminal apron and gates','approach path over city','cargo area and hangars'],
 'religious-site':['shrine courtyard and pilgrims','temple steps and worshippers','historic church square','sacred wall and prayer area'],
 'space':['launch pad and surrounding range','observatory dome and night sky','tracking station dishes','rocket assembly building'],
 'harbor-port':['container terminal and cranes','marina with moored yachts','ferry dock and boarding area','harbor entrance and lighthouse']
};
function sampleCoords(s,country){
  var b=BOUNDS[country]||[20,50,-120,40];
  return [rf(s,b[0],b[1]).toFixed(4)*1, rf(s,b[2],b[3]).toFixed(4)*1];
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var cat=opts.category&&CATEGORIES.indexOf(opts.category)>=0?opts.category:pick(CATEGORIES,rnd);
  var ctry=opts.country||pick(COUNTRIES,rnd);
  var country=Array.isArray(ctry)?ctry[0]:ctry;
  var code=Array.isArray(ctry)?ctry[1]:'XX';
  var coords=sampleCoords(rnd,country);
  var city=pick(CITY_NAMES,rnd).trim();
  var name=city+' '+CAT_LABEL[cat]+' Cam';
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:name,
    title:name+' — '+country,
    description:'SAMPLE CAMERA LISTING (generated — not a real camera). A '+CAT_LABEL[cat].toLowerCase()+' public camera directory entry for '+country+'. Generated samples carry illustrative coordinates and must never be treated as real camera locations.',
    camera_name:name,
    location:{city:city,country:country,country_code:code,lat:coords[0],lon:coords[1],address:ri(rnd,1,999)+' Sample Road, '+city},
    coordinates:[coords[0],coords[1]],
    category:cat,
    category_label:CAT_LABEL[cat],
    visible:pick(VISIBLE[cat],rnd),
    stream_url:'',
    stream_note:'No live stream — generated sample entry.',
    year:2026,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample listing — not a real camera. Seeded archive records are real publicly-accessible cameras; this generated record is structural only.',
    demo:{kind:'map-embed',program:"function mapLink(lat,lon){return 'https://www.openstreetmap.org/?mlat='+lat+'&mlon='+lon+'#map=14/'+lat+'/'+lon;}",note:'Paste into any JS console with coordinates to open the camera location on a map.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-PCAM-\d{6}$/.test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||r.name.length<3)e.push('name');
  if(!r.location||typeof r.location.lat!=='number'||typeof r.location.lon!=='number')e.push('location');
  if(r.location&&(r.location.lat<-90||r.location.lat>90))e.push('lat-range');
  if(r.location&&(r.location.lon<-180||r.location.lon>180))e.push('lon-range');
  if(CATEGORIES.indexOf(r.category)<0)e.push('category');
  if(typeof r.visible!=='string'||!r.visible)e.push('visible');
  if(!r.src)e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.name===record.name&&r.location&&record.location&&r.location.country===record.location.country;});
  return dups.length?{ok:false,errors:['duplicate name+country in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-public-cameras-1.0',generate:generate,validate:validate,driftCheck:driftCheck,categories:CATEGORIES,countryList:COUNTRIES.map(function(c){return c[0];})};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-cameras',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
