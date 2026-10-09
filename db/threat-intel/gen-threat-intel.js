(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function p2(n){return String(n).padStart(2,'0');}
var CATS=['critical','high','medium','low'];
var FLAW=['Buffer overflow','SQL injection','Cross-site scripting','Privilege escalation','Path traversal','Deserialization flaw','Authentication bypass','Command injection','Use-after-free','Integer overflow'];
var SOFT=['NexusGate VPN','PixelForge CMS','DataHarbor Server','CloudNine Mail','IronOak Firewall','BluePeak Portal','SummitWorks CRM','HarborDrive NAS','ForgeLine SCADA','LumenChat App','QuantumSync Backup','OrbitDesk Agent'];
var IMPACT=['remote code execution','data exfiltration','privilege escalation to root','denial of service','session hijacking','arbitrary file read'];
function generate(seed,opts,rnd){
  rnd=rnd||prng(seed);
  var sev=(opts&&opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:(function(){var x=rnd();return x<0.1?'critical':x<0.35?'high':x<0.7?'medium':'low';})();
  var cvss=sev==='critical'?Math.round((9+rnd()*1)*10)/10
    :sev==='high'?Math.round((7+rnd()*1.9)*10)/10
    :sev==='medium'?Math.round((4+rnd()*2.9)*10)/10
    :Math.round((0.1+rnd()*3.8)*10)/10;
  var cve='CVE-2024-'+String(seed).padStart(6,'0');
  var flaw=pick(FLAW,rnd), soft=pick(SOFT,rnd);
  var ver=ri(rnd,1,9)+'.'+ri(rnd,0,9);
  var title=flaw+' in '+soft+' '+ver+' allows '+pick(IMPACT,rnd);
  var n=ri(rnd,2,4), prods=[], pool=SOFT.slice();
  for(var i=0;i<n&&pool.length;i++){prods.push(pool.splice((rnd()*pool.length)|0,1)[0]);}
  var pub=ri(rnd,2024,2026)+'-'+p2(ri(rnd,1,12))+'-'+p2(ri(rnd,1,28));
  var exploit=rnd()<0.3;
  var rem='Upgrade '+soft+' to a fixed release and apply the vendor patch; restrict network exposure until the patch is verified.';
  var id='JAH-CVE-'+String(seed).padStart(6,'0');
  var desc=cve+' ('+sev+', CVSS '+cvss+'): '+title+'. Affects '+prods.length+' products. Published '+pub+'.'+(exploit?' Exploit available.':'');
  return {id:id,cve_id:cve,title:cve+' '+title,description:desc.slice(0,600),
    severity:sev,cvss_score:cvss,affected_products:prods,published_date:pub,
    exploit_available:exploit,remediation:rem};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['record']};
  if(typeof r.id!=='string'||!/^JAH-CVE-\d{6}$/.test(r.id))e.push('id');
  if(typeof r.cve_id!=='string'||!/^CVE-2024-\d{6}$/.test(r.cve_id))e.push('cve_id');
  if(typeof r.title!=='string'||r.title.indexOf(r.cve_id)!==0)e.push('title');
  if(typeof r.description!=='string'||!r.description||r.description.length>600)e.push('description');
  if(CATS.indexOf(r.severity)<0)e.push('severity');
  if(typeof r.cvss_score!=='number'||r.cvss_score<0||r.cvss_score>10)e.push('cvss_score');
  else{
    if(r.severity==='critical'&&!(r.cvss_score>=9))e.push('sev_critical');
    if(r.severity==='high'&&!(r.cvss_score>=7&&r.cvss_score<9))e.push('sev_high');
    if(r.severity==='medium'&&!(r.cvss_score>=4&&r.cvss_score<7))e.push('sev_medium');
    if(r.severity==='low'&&!(r.cvss_score<4))e.push('sev_low');
  }
  if(!Array.isArray(r.affected_products)||r.affected_products.length<2||r.affected_products.length>4)e.push('affected_products');
  if(typeof r.published_date!=='string'||!/^202[4-6]-\d{2}-\d{2}$/.test(r.published_date))e.push('published_date');
  if(typeof r.exploit_available!=='boolean')e.push('exploit_available');
  if(typeof r.remediation!=='string'||!r.remediation||r.remediation.length>600)e.push('remediation');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-threat-intel-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('threat-intel',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;})();
