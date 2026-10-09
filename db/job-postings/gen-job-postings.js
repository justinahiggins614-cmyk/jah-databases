(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function p2(n){return String(n).padStart(2,'0');}
var CATS=['technology','healthcare','finance','education','retail','manufacturing'];
var SAL={technology:[70000,220000],healthcare:[60000,200000],finance:[80000,250000],education:[40000,120000],retail:[35000,110000],manufacturing:[45000,130000]};
var TITLES=['Software Engineer','Registered Nurse','Financial Analyst','High School Teacher','Store Manager','Mechanical Engineer','Data Scientist','Pharmacist','Accountant','Elementary Teacher','Cashier','Electrician','Product Manager','Physical Therapist','Loan Officer','Professor','Sales Associate','Welder','UX Designer','Dental Hygienist','Auditor','Librarian','Customer Service Rep','Machinist','DevOps Engineer','Surgeon','Investment Banker','Principal'];
var COS=['BluePeak Technologies','Cedar Health Partners','IronGate Financial','Maplewood Schools','BrightMart Retail','ForgeLine Manufacturing','NovaSoft Labs','HarborCare Clinics','Summit Trust Bank','Elm Street Academy','QuickStop Stores','PrecisionWorks Co','DataHarbor Inc','WellSpring Medical','CapitalCrest Group','NorthStar Learning','ValuePlus Market','SteelCore Industries','CloudNine Systems','FamilyFirst Hospitals','MetroBank Alliance','Greenfield College','ShopSmart Outlets','TitanFabricators LLC'];
var CITY=['Austin','Denver','Portland','Chicago','Boston','Seattle','Miami','Phoenix','Nashville','Atlanta','Dallas','Minneapolis','Raleigh','Charlotte','Columbus','Indianapolis','Kansas City','Cleveland','Pittsburgh','Boise'];
var SKILLS=['Python','SQL','project management','communication','data analysis','JavaScript','nursing','patient care','financial modeling','Excel','teaching','curriculum design','sales','inventory management','welding','CAD','machine learning','statistics','pharmacy','bookkeeping','auditing','lesson planning','customer service','CNC machining','cloud computing','cybersecurity'];
function generate(seed,opts,rnd){
  rnd=rnd||prng(seed);
  var sector=(opts&&opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:pick(CATS,rnd);
  var title=pick(TITLES,rnd), company=pick(COS,rnd), location=pick(CITY,rnd);
  var band=SAL[sector];
  var smin=ri(rnd,band[0],band[1]-20000);
  var smax=smin+ri(rnd,5000,60000);
  var n=ri(rnd,3,6), skills=[], pool=SKILLS.slice();
  for(var i=0;i<n&&pool.length;i++){skills.push(pool.splice((rnd()*pool.length)|0,1)[0]);}
  var date='2026-'+p2(ri(rnd,1,10))+'-'+p2(ri(rnd,1,28));
  var id='JAH-JOB-'+String(seed).padStart(6,'0');
  var desc=title+' at '+company+', '+location+'. '+sector+' sector. Salary $'+smin+'-$'+smax+'. Skills: '+skills.join(', ')+'. Posted '+date+'.';
  return {id:id,job_id:id,title:title+' @ '+company,description:desc.slice(0,600),
    company:company,location:location,sector:sector,
    salary_min:smin,salary_max:smax,skills:skills,posted_date:date};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['record']};
  if(typeof r.id!=='string'||!/^JAH-JOB-\d{6}$/.test(r.id))e.push('id');
  if(r.job_id!==r.id)e.push('job_id');
  if(typeof r.title!=='string'||r.title.indexOf(' @ ') < 0)e.push('title_fmt');
  if(typeof r.description!=='string'||!r.description||r.description.length>600)e.push('description');
  if(typeof r.company!=='string'||!r.company)e.push('company');
  if(typeof r.location!=='string'||!r.location)e.push('location');
  if(CATS.indexOf(r.sector)<0)e.push('sector');
  if(typeof r.salary_min!=='number'||typeof r.salary_max!=='number'||r.salary_max<=r.salary_min||r.salary_min<20000||r.salary_max>400000)e.push('salary');
  if(!Array.isArray(r.skills)||r.skills.length<3||r.skills.length>6||r.skills.some(function(s){return typeof s!=='string';}))e.push('skills');
  if(typeof r.posted_date!=='string'||!/^2026-\d{2}-\d{2}$/.test(r.posted_date))e.push('posted_date');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-job-postings-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('job-postings',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;})();
