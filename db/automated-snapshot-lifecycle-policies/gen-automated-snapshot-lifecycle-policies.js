(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["cloud", "filesystem", "database", "vm", "backup"];
var PREFIX='JAH-ASL-';
var GENVER='jahdb-automated-snapshot-lifecycle-policies-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["system", "policy", "retention", "trigger"];
var DEMO_TPL="// $TITLE - retention pruning demo\nvar snaps = [];\nfor (var i = 0; i < 30; i++) snaps.push({ day: i, size: 100 });\nfunction prune(list, keepDaily, keepWeekly) {\n  return list.filter(function(s, i) { return i >= list.length - keepDaily || (s.day % 7 === 0 && i >= list.length - keepWeekly * 7); });\n}\nvar kept = prune(snaps, 7, 4);\nconsole.log(\"System: $SYSTEM | Policy: $POLICY\");\nconsole.log(\"Before: \" + snaps.length + \" snapshots, after prune: \" + kept.length);\nconsole.log(\"Retention: $RETENTION -> ENFORCED\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["cloud", "AWS DLM", "Data Lifecycle Manager automates EBS snapshot creation and deletion by tags and age. Policy: tag-based schedules. Retention: count or age based. Trigger: cron schedule.", {"system": "AWS DLM", "policy": "tag-based schedules", "retention": "count or age based", "trigger": "cron schedule"}], ["filesystem", "ZFS + sanoid", "sanoid takes and prunes ZFS snapshots with grandfather-father-son style policies. Policy: hourly/daily/monthly tiers. Retention: configurable per tier. Trigger: cron.", {"system": "sanoid", "policy": "hourly/daily/monthly tiers", "retention": "configurable per tier", "trigger": "cron"}], ["filesystem", "Btrfs + snapper", "snapper manages Btrfs subvolume snapshots with timeline and number cleanup. Policy: timeline + number limits. Retention: keep N hourly/daily. Trigger: cron / apt hooks.", {"system": "snapper", "policy": "timeline + number limits", "retention": "keep N hourly/daily", "trigger": "cron / apt hooks"}], ["filesystem", "LVM thin snapshots", "Thin provisioning makes LVM snapshots cheap; scripts prune by age. Policy: scripted pruning. Retention: age-based. Trigger: cron.", {"system": "LVM", "policy": "scripted pruning", "retention": "age-based", "trigger": "cron"}], ["cloud", "GCP scheduled snapshots", "Compute Engine snapshot schedules with retention and guest-flush options. Policy: schedule + retention. Retention: max retention days. Trigger: schedule.", {"system": "GCP snapshots", "policy": "schedule + retention", "retention": "max retention days", "trigger": "schedule"}], ["cloud", "Azure Backup", "Recovery Services vaults apply retention ranges from days to years per policy. Policy: vault policies. Retention: daily/weekly/yearly. Trigger: schedule.", {"system": "Azure Backup", "policy": "vault policies", "retention": "daily/weekly/yearly", "trigger": "schedule"}], ["vm", "Proxmox vzdump", "vzdump backs up VMs/containers on schedules with configurable keep counts. Policy: keep-last N. Retention: N backups. Trigger: datacenter schedule.", {"system": "vzdump", "policy": "keep-last N", "retention": "N backups", "trigger": "datacenter schedule"}], ["backup", "restic forget", "forget applies --keep-daily/weekly/monthly rules and prunes unreferenced data. Policy: keep-* tiers. Retention: tiered counts. Trigger: post-backup hook.", {"system": "restic forget", "policy": "keep-* tiers", "retention": "tiered counts", "trigger": "post-backup hook"}], ["backup", "borg prune", "prune enforces --keep-daily etc. inside repositories with compact afterwards. Policy: keep-* tiers. Retention: tiered counts. Trigger: post-backup.", {"system": "borg prune", "policy": "keep-* tiers", "retention": "tiered counts", "trigger": "post-backup"}], ["backup", "Veeam retention", "Veeam jobs chain incrementals with GFS (grandfather-father-son) long-term retention. Policy: GFS retention. Retention: daily/weekly/monthly/yearly. Trigger: job schedule.", {"system": "Veeam", "policy": "GFS retention", "retention": "daily/weekly/monthly/yearly", "trigger": "job schedule"}], ["backup", "Time Machine", "macOS keeps hourly backups for a day, daily for a month, weekly until the disk fills. Policy: automatic thinning. Retention: space-driven. Trigger: hourly.", {"system": "Time Machine", "policy": "automatic thinning", "retention": "space-driven", "trigger": "hourly"}], ["filesystem", "Windows VSS", "Volume Shadow Copy keeps file versions with storage-area size caps. Policy: storage-area cap. Retention: space-driven. Trigger: scheduled.", {"system": "VSS", "policy": "storage-area cap", "retention": "space-driven", "trigger": "scheduled"}], ["filesystem", "Ceph RBD snapshots", "RBD snapshots with trash purging and mirroring schedules for clusters. Policy: mirror + purge schedules. Retention: configurable. Trigger: cron.", {"system": "Ceph RBD", "policy": "mirror + purge schedules", "retention": "configurable", "trigger": "cron"}], ["backup", "Kopia policies", "Kopia applies per-path policies for retention, compression, and scheduling. Policy: per-path policies. Retention: keep-* tiers. Trigger: schedule.", {"system": "Kopia", "policy": "per-path policies", "retention": "keep-* tiers", "trigger": "schedule"}], ["backup", "rsnapshot", "rsnapshot rotates rsync-based snapshots through alpha/beta/gamma intervals. Policy: interval rotation. Retention: retain N per interval. Trigger: cron.", {"system": "rsnapshot", "policy": "interval rotation", "retention": "retain N per interval", "trigger": "cron"}]];
function demoFor(title,id,f){
  var vars={TITLE:title,ID:id};
  for(var k in f){ if(Object.prototype.hasOwnProperty.call(f,k)) vars[k.toUpperCase()]=f[k]; }
  return fillTpl(DEMO_TPL,vars);
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var fields={}; for(var k in b[3]){fields[k]=b[3][k];}
  return {id:id,t:b[1],title:b[1],g:cat,c:1,category:cat,description:b[2],fields:fields,ladder_rank:1+(seed%3),demo:demoFor(b[1],id,fields),provenance:PROV,src:SRC,last_verified:'2026-10-21',edition:EDITION,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+'JAH\\-ASL\\-'+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(r.t!==r.title)e.push('t');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(r.g!==r.category)e.push('g');
  if(!r.fields||typeof r.fields!=='object')e.push('fields');
  else{FIELDS.forEach(function(k){if(typeof r.fields[k]!=='string'||!r.fields[k].length)e.push('fields.'+k);});}
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('console.log')<0)e.push('demo');
  if(r.src!==SRC)e.push('src');
  if(r.edition!==EDITION)e.push('edition');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  if(typeof r.provenance!=='string'||!r.provenance.length)e.push('provenance');
  return {ok:!e.length,errors:e};
}
var gen={version:GENVER,generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('automated-snapshot-lifecycle-policies',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
