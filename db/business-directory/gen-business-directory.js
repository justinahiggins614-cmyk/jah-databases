(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['technology','healthcare','finance','retail','manufacturing','services','food','education'];
var PRE=['Northgate','Bright','Clear','Blue','Iron','Silver','Golden','Copper','Rapid','Prime','Apex','Nova','Summit','Harbor','Cedar','Maple','Stone','River','Beacon','Pioneer','Crest','Falcon','Ember','Lumen','Forge','Onyx','Quartz','Vantage','Zenith','Halcyon'];
var COREW=['Systems','Dynamics','Labs','Works','Industries','Solutions','Ventures','Partners','Collective','Group','Holdings','Makers','Supply','Trading','Craft','Network','Studio','Fields','Harvest','Logistics','Media','Design','Foods','Care','Capital','Energy'];
var SUF=['LLC','Inc.','Ltd.','Co.','Group','Partners','Corp.','Enterprises'];
var CITY=[['Austin','USA'],['Denver','USA'],['Portland','USA'],['Chicago','USA'],['Boston','USA'],['Seattle','USA'],['Toronto','Canada'],['London','UK'],['Berlin','Germany'],['Paris','France'],['Dublin','Ireland'],['Sydney','Australia'],['Singapore','Singapore'],['Tokyo','Japan'],['Amsterdam','Netherlands'],['Madrid','Spain'],['Lisbon','Portugal'],['Oslo','Norway'],['Stockholm','Sweden'],['Zurich','Switzerland']];
var BANDS=['1-10','11-50','51-200','201-1000','1000+'];
function generate(seed,opts,rnd){
  rnd=rnd||prng(seed);
  var cat=(opts&&opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:pick(CATS,rnd);
  var name=pick(PRE,rnd)+' '+pick(COREW,rnd)+' '+pick(SUF,rnd);
  var cc=pick(CITY,rnd);
  var band=pick(BANDS,rnd);
  var year=ri(rnd,1950,2026);
  var id='JAH-BIZ-'+String(seed).padStart(6,'0');
  var desc=name+' is a '+band+'-employee '+cat+' company based in '+cc[0]+', '+cc[1]+', founded in '+year+'.';
  return {id:id,company_id:id,legal_name:name,title:name,description:desc.slice(0,600),
    industry:cat,city:cc[0],country:cc[1],employee_band:band,
    website:'https://example-'+seed+'.com',founded_year:year};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['record']};
  if(typeof r.id!=='string'||!/^JAH-BIZ-\d{6}$/.test(r.id))e.push('id');
  if(r.company_id!==r.id)e.push('company_id');
  if(typeof r.legal_name!=='string'||!r.legal_name)e.push('legal_name');
  if(r.title!==r.legal_name)e.push('title');
  if(typeof r.description!=='string'||!r.description||r.description.length>600)e.push('description');
  if(CATS.indexOf(r.industry)<0)e.push('industry');
  if(typeof r.city!=='string'||!r.city)e.push('city');
  if(typeof r.country!=='string'||!r.country)e.push('country');
  if(BANDS.indexOf(r.employee_band)<0)e.push('employee_band');
  if(typeof r.website!=='string'||!/^https:\/\/example-\d+\.com$/.test(r.website))e.push('website');
  if(typeof r.founded_year!=='number'||r.founded_year<1950||r.founded_year>2026)e.push('founded_year');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-business-directory-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('business-directory',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;})();
