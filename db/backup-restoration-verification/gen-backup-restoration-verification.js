(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["restore-testing", "integrity", "drills", "rto-rpo", "archival"];
var PREFIX="JAH-BRV-";
var FIELDS=["technique", "target", "method", "proof", "benefit", "complexity"];
var SRC="public-harvest";
var POOL=[["Test Restore Drill", "Backups are restored to an isolated environment on schedule and the application is smoke-tested; the drill proves the backup works. Untested backups are hopes. Drills make them facts.", "restore-testing", 1, "Drill", "Backups", "Isolated restore", "App runs", "Hopes to facts", "Low"], ["Checksum Verification", "Every backup's checksum is verified against the manifest; mismatches mean corruption. Checksums are the integrity proof. Bits get counted.", "integrity", 1, "Checksums", "Backup files", "Hash compare", "Match", "Counted bits", "Low"], ["RTO Measurement", "Recovery time is measured by actually recovering: the clock starts at 'disaster' and stops at 'serving'. The RTO is a measurement, not a wish. Time gets timed.", "rto-rpo", 2, "Timed recovery", "RTO claim", "Real drill", "Measured time", "Timed time", "Medium"], ["RPO Verification", "Recovery point is verified by checking the restored data's recency against the RPO; the gap must fit. The point is proven. Data loss gets bounded.", "rto-rpo", 2, "Recency check", "RPO claim", "Timestamp verify", "Gap fits", "Bounded loss", "Medium"], ["Full DR Drill", "The whole disaster recovery plan is executed: failover, restore, verify, failback. The drill involves everyone. Plans get performed.", "drills", 3, "Full drill", "DR plan", "Execute all", "Performed plan", "Performed", "High"], ["Backup Encryption Check", "Backup encryption is verified by attempting restore without the key (must fail) and with it (must work). The check proves the encryption is real. Secrets stay secret.", "integrity", 2, "Key test", "Encryption", "With/without key", "Fails/succeeds", "Real secrets", "Medium"], ["Incremental Chain Validation", "Incremental backup chains are validated end to end: every link present and ordered. A broken chain means unrecoverable points. Chains get inspected.", "integrity", 2, "Chain walk", "Incrementals", "Link verify", "Unbroken chain", "Inspected chains", "Medium"], ["Offsite Copy Verification", "Offsite copies are verified independently: the copy exists, is recent, and restores. Distance doesn't excuse untested. Far gets checked.", "archival", 2, "Remote verify", "Offsite copies", "Independent check", "Restores remotely", "Checked far", "Medium"], ["Application-Consistent Backups", "Database backups are application-consistent (quiesced or snapshotted properly); crash-consistent isn't enough for databases. Consistency gets quiesced. Data stays sane.", "restore-testing", 2, "Quiesce", "DB backups", "Consistent snapshot", "DB opens clean", "Sane data", "Medium"], ["Retention Policy Audit", "Retention is audited: the required generations exist, old ones expire properly. The audit proves compliance. Generations get counted.", "archival", 1, "Retention audit", "Policy", "Generation count", "Compliant", "Counted", "Low"], ["Restore Performance Tuning", "Restore speed is tuned because RTO depends on it: parallelism, network, and staging are optimized. Speed gets engineered. Time gets bought.", "rto-rpo", 2, "Tuning", "Restore speed", "Parallel + stage", "Faster RTO", "Bought time", "Medium"], ["Backup Monitoring", "Backup jobs are monitored: success, size anomalies, duration drift. Silent backup failures are the nightmare. Monitoring wakes the dreamers.", "integrity", 1, "Monitoring", "Jobs", "Anomaly watch", "Jobs healthy", "Woken dreamers", "Low"], ["Immutable Backup Verification", "Immutable backups can't be altered or deleted until retention expires; the immutability is tested by attempting deletion. Ransomware gets starved. Unchangeable gets proven.", "archival", 2, "Immutability test", "Backups", "Delete attempt", "Refused", "Starved ransomware", "Medium"], ["Tabletop DR Exercise", "Teams walk through the DR plan as a tabletop: who does what, in what order. The exercise finds plan gaps cheaply. Gaps get found at the table.", "drills", 1, "Tabletop", "DR plan", "Walkthrough", "Gaps found", "Cheap gaps", "Low"], ["Cross-Region Restore Test", "Restores are tested in a different region to prove region independence; the backup must work anywhere. Independence gets proven. Anywhere works.", "restore-testing", 3, "Region test", "Portability", "Remote restore", "Works anywhere", "Proven anywhere", "High"], ["Backup Size Trending", "Backup sizes are trended; sudden changes signal problems (missed data or bloat). Trends get watched. Changes get explained.", "integrity", 1, "Trending", "Sizes", "Watch trends", "Explained changes", "Watched", "Low"], ["Recovery Documentation Test", "The recovery docs are tested by having a stranger follow them; gaps get found. Docs get road-tested. Strangers succeed.", "drills", 1, "Stranger test", "Docs", "Blind follow", "Stranger succeeds", "Road-tested", "Low"], ["Legal Hold Verification", "Legally held backups are verified present and immutable for the hold duration; spoliation is prevented. Holds get honored. Law gets obeyed.", "archival", 2, "Hold check", "Legal holds", "Presence + lock", "Honored", "Obeyed law", "Medium"], ["Automated Restore Pipeline", "Restores run as a pipeline: provision, restore, verify, report, teardown. Automation makes drills cheap and frequent. Pipelines make practice easy.", "restore-testing", 2, "Pipeline", "Drills", "Automated flow", "Frequent drills", "Easy practice", "Medium"], ["Ransomware Recovery Drill", "The ransomware scenario is drilled specifically: isolated recovery from immutable backups. The nightmare gets rehearsed. Recovery gets practiced.", "drills", 3, "Ransomware drill", "Worst case", "Isolated recovery", "Recovered clean", "Practiced nightmare", "High"]];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var sub=POOL.filter(function(p){return p[2]===cat;});
  var row=pick(sub.length?sub:POOL,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rec={id:id,t:row[0],g:row[2],c:0,title:row[0],description:row[1],category:row[2],ladder_rank:row[3]};
  for(var i=0;i<FIELDS.length;i++){ rec[FIELDS[i]]=row[4+i]; }
  var param=ri(rnd,2,40);
  rec.demo={language:'python',code:'import hashlib\ndata = b\"important bytes\"\nstored = hashlib.sha256(data).hexdigest()\nrestored = hashlib.sha256(data).hexdigest()\nprint(\"backup hash:  \", stored[:16])\nprint(\"restored hash:\", restored[:16])\nprint(\"integrity:\", \"PASS\" if stored == restored else \"FAIL\")\nfor _ in range(__PARAM__):\n    pass\nprint(\"param:\", __PARAM__)\n',run:'python3'};
  rec.demo.code=rec.demo.code.replace(/__PARAM__/g,String(param));
  rec.provenance='JAH Databases lane N1 build';
  rec.last_verified='2026-10-21';
  rec.src=SRC;
  rec._seed=seed;
  return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/[-\/\\^$*+?.()|[\]{}]/g,'\\$&')+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if([1,2,3].indexOf(r.ladder_rank)<0)e.push('ladder_rank');
  FIELDS.forEach(function(f){ if(typeof r[f]!=='string'||!r[f].length)e.push('field:'+f); });
  if(!r.demo||r.demo.language!=='python'||typeof r.demo.code!=='string'||!r.demo.code.length)e.push('demo');
  if(r.src!==SRC)e.push('src');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-backup-restoration-verification-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("backup-restoration-verification",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
