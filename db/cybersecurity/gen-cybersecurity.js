(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}
var CATS=['threats','vulnerabilities','controls','remediation','test-cases'];
var SEVS=['critical','high','medium','low','informational'];
var PREFIX='JAH-SEC-';

/* Synthetic defensive scenarios. Generated records NEVER carry real CVE IDs;
   every test case is labeled synthetic:true and the synthetic_id carries a
   check digit the validator recomputes. */
var SCEN=[
{cat:'threats',cls:'phishing',t:'Phishing lure triage drill',
 d:'A simulated phishing wave targets staff with credential-harvest lures. The drill measures report rate, click rate, and time-to-report, then feeds misses into coaching. Purely defensive: it trains recognition, never deception tradecraft.',
 ind:['lure email reported via the phish button','user clicked but entered no credentials','credentials entered on the lookalike domain','report arrived within 10 minutes of delivery'],
 ctl:[['Report pipeline','A one-click report button routes lures to the SOC queue within seconds.'],['Lookalike-domain watch','Newly registered similar domains trigger review before they can be weaponized.'],['Coaching loop','Clickers get a 3-minute interactive refresher, not punishment.']],
 rem:'Run the drill quarterly, publish only aggregate report rates, and retire lures that everyone catches. Trend the click rate down; investigate any team that trends up.',
 tc:['Wave of 500 lures, 40 clicks, 320 reports','Lure mimicking the helpdesk portal','Repeat drill after coaching']},
{cat:'threats',cls:'ransomware',t:'Ransomware tabletop exercise',
 d:'A tabletop walks leadership through a simulated encryption event: detection, containment, comms, and restore. No malware is involved — the value is in decisions, roles, and timing under pressure.',
 ind:['simulated EDR alert for mass file renames','backup integrity check requested','comms draft prepared within one hour','restore priority list confirmed by owners'],
 ctl:[['Offline backups','Immutable, offline copies tested by restore every quarter.'],['Network segmentation','Lateral movement paths are mapped and pruned yearly.'],['EDR coverage','Behavioral detection on every endpoint, alerts tuned to a 15-minute SLA.']],
 rem:'Document every decision and gap found; convert gaps into funded projects with owners and dates. Re-run yearly or after major infrastructure change.',
 tc:['Simulated encryption on a file share','Executive decision drill: pay vs restore','Backup restore timed run']},
{cat:'vulnerabilities',cls:'patch-management',t:'Patch cadence audit',
 d:'A recurring audit that measures mean time to patch by severity tier and finds the stragglers: systems missing critical patches past SLA. It treats patching as a measurable pipeline, not a hope.',
 ind:['critical patch older than 14 days on an internet-facing host','scanner and agent disagree on patch state','reboot-pending fleet growing week over week'],
 ctl:[['Tiered SLAs','Critical: 14 days; high: 30; medium: 90 — tracked on one dashboard.'],['Maintenance windows','Pre-approved windows remove the scheduling excuse.'],['Exception ledger','Every deferral has an owner, a compensating control, and an expiry.']],
 rem:'Shrink the critical backlog to zero, then hold it there for two quarters before tightening SLAs. Report the trend, not just the snapshot.',
 tc:['Audit of 200 hosts finds 12 past SLA','Scanner-vs-agent disagreement drill','Exception ledger review']},
{cat:'vulnerabilities',cls:'misconfiguration',t:'Cloud storage exposure review',
 d:'A review that hunts publicly readable storage buckets and open snapshots. Misconfiguration, not malware, causes most cloud breaches — this check is cheap and high-value.',
 ind:['bucket policy allows public read','snapshot shared with "all users"','access logging disabled on the bucket'],
 ctl:[['Default-deny baseline','New buckets inherit private-only policy by default.'],['Config scanner','Continuous check flags public exposure within minutes.'],['Access logging','Every bucket logs access; logs are reviewed weekly.']],
 rem:'Remediate exposures same-day, then find how the misconfiguration happened and fix the template or runbook that allowed it.',
 tc:['Scan of 80 buckets finds 3 public','Template fix verification rescan','Quarterly access-log review']},
{cat:'controls',cls:'authentication',t:'MFA rollout control',
 d:'Phishing-resistant multi-factor authentication on every privileged and remote-access path. The single highest-leverage control against credential theft.',
 ind:['privileged account without MFA enrolled','MFA fatigue prompts observed in logs','legacy protocol bypassing MFA still enabled'],
 ctl:[['Phishing-resistant MFA','Hardware keys or platform authenticators for admins.'],['Legacy protocol block','IMAP/POP/SMTP-auth cannot bypass MFA.'],['Enrollment campaign','Weekly nudges plus a hard deadline with executive backing.']],
 rem:'Reach 100% on privileged accounts first, then all remote access, then everyone. Measure weekly and publish the curve.',
 tc:['Enrollment audit across 300 accounts','Legacy protocol block verification','Simulated MFA-fatigue prompt test']},
{cat:'controls',cls:'access-control',t:'Least-privilege access review',
 d:'Quarterly review that trims standing privileges: dormant accounts, over-broad roles, and privilege creep. Access should expire by default and be re-justified.',
 ind:['dormant privileged account older than 90 days','role grants beyond the job description','service account with interactive logon rights'],
 ctl:[['Just-in-time elevation','Privileges are granted for hours, not forever.'],['Quarterly recertification','Managers re-approve their team\'s access or it laps like milk.'],['Service-account inventory','Every non-human account has an owner and a purpose.']],
 rem:'Revoke first, ask later for the obvious cases; schedule the rest with owners. Automate deprovisioning on HR exit events.',
 tc:['Review of 150 privileged accounts','Dormant account cleanup sprint','Service-account ownership drive']},
{cat:'controls',cls:'network',t:'Network segmentation design check',
 d:'Verifies that flat-network lateral paths are actually blocked: can a compromised workstation reach the backup server, the domain controller, the OT zone? Test, don\'t assume.',
 ind:['workstation subnet reaches backup VLAN directly','unrestricted east-west traffic between user zones','OT network bridged to IT without a DMZ'],
 ctl:[['Zone firewalling','Inter-zone traffic denied by default, allowed by explicit rule.'],['Jump hosts','Admin access flows through hardened, monitored bastions.'],['Micro-segmentation','Critical assets get host-level policy as well as network policy.']],
 rem:'Draw the real traffic map from flow logs, then write policy to match the intended design. Re-test after every firewall change.',
 tc:['Lateral-path probe from user VLAN','Bastion-only admin access test','Firewall rule cleanup review']},
{cat:'controls',cls:'detection',t:'Log review and alert tuning drill',
 d:'A weekly drill where analysts review a sample of alerts and tune the noisy ones. Detection engineering is a loop: detect, measure, tune, repeat.',
 ind:['alert fired 200 times with zero true positives','critical log source stopped shipping for 6 hours','analyst bypassed the queue for a known-good pattern'],
 ctl:[['Detection-as-code','Rules live in version control with tests and owners.'],['Log-source health','A dead log source pages like an outage.'],['Tuning backlog','Noisy rules get fixed or disabled — alert fatigue is a vulnerability.']],
 rem:'Track precision per rule monthly; retire or fix anything under 5% precision. Celebrate the rules that catch real activity.',
 tc:['Weekly sample review of 50 alerts','Dead log-source fire drill','Precision report for top-10 noisy rules']},
{cat:'remediation',cls:'incident-response',t:'Incident response runbook rehearsal',
 d:'Rehearses the first 60 minutes of an incident: who declares, who contains, who talks to legal and customers. Rehearsal turns a plan into muscle memory.',
 ind:['runbook step references a decommissioned tool','on-call rotation has a single point of failure','comms template missing for the scenario'],
 ctl:[['Defined severity levels','SEV-1 through SEV-4 with clear entry criteria.'],['Pre-authorized containment','Analysts may isolate hosts without waiting for approval.'],['Comms templates','Legal-approved drafts for customers, staff, and regulators.']],
 rem:'Fix every gap the rehearsal finds within 30 days. Rotate scenarios so no two rehearsals test the same path.',
 tc:['60-minute simulated intrusion','Comms drill with legal observer','After-action review and gap tickets']},
{cat:'remediation',cls:'backup',t:'Backup restore verification test',
 d:'Restores a random backup set to an isolated environment and boots it. Untested backups are Schrödinger\'s backups — this test opens the box.',
 ind:['last successful restore test older than 90 days','backup job succeeding but restore failing','recovery time exceeds the documented RTO'],
 ctl:[['Quarterly restore tests','Random set, isolated network, timed end to end.'],['Immutable copies','Backups cannot be altered or deleted within retention.'],['Documented RTO/RPO','Recovery targets written, agreed, and actually met.']],
 rem:'Publish restore times against RTO; fund the gap if restores are too slow. Test the thing you will need at 3am.',
 tc:['Random quarterly restore to isolated VLAN','RTO timing measurement','Backup integrity hash verification']},
{cat:'test-cases',cls:'validation',t:'Firewall rule audit lab',
 d:'A synthetic lab exercise: given a firewall ruleset, find the overly broad rules and shadowed entries. Trains careful rule reading without touching production.',
 ind:['lab ruleset contains an allow-any-any rule','shadowed rule never matches traffic','rule without ticket reference or expiry'],
 ctl:[['Default deny','Implicit deny at the end of every ruleset.'],['Rule documentation','Every allow cites a ticket and an owner.'],['Periodic recertification','Rules expire unless re-justified yearly.']],
 rem:'In the lab, rewrite the ruleset minimal and correct; in production, schedule the same review with change control.',
 tc:['Find the 3 bad rules in a 40-rule lab set','Rewrite exercise: minimal correct ruleset','Shadowed-rule hunt']},
{cat:'test-cases',cls:'validation',t:'Password policy strength lab',
 d:'A synthetic exercise testing password policy logic against common weak choices. Teaches why length beats complexity rules.',
 ind:['lab policy accepts an 8-character dictionary word','no breach-corpus check in the lab validator','complexity rules without length minimum'],
 ctl:[['Length minimum of 12+','Long passphrases resist cracking far better than short complex ones.'],['Breach-corpus screening','Reject passwords seen in known breaches.'],['No periodic rotation','Rotation only on suspected compromise (per current guidance).']],
 rem:'Update the lab validator, then mirror the policy change in the real directory with user comms.',
 tc:['Weak-password acceptance test','Breach-corpus rejection test','Passphrase usability trial']},
{cat:'controls',cls:'data-protection',t:'Encryption at rest verification',
 d:'Verifies that sensitive data stores actually encrypt at rest with managed keys — not just "the disk is encrypted" folklore, but checked per datastore.',
 ind:['database without storage encryption enabled','keys stored alongside the data they protect','rotation never performed on data keys'],
 ctl:[['Managed key service','Keys live in a KMS/HSM, never in app config.'],['Per-datastore check','Each store\'s encryption status is inventoried.'],['Key rotation','Annual rotation with a tested, reversible procedure.']],
 rem:'Enable encryption store by store, verify with the vendor\'s own status API, and document key custody.',
 tc:['Encryption status inventory of 25 datastores','Key rotation dry run','KMS access-policy review']},
{cat:'controls',cls:'email-security',t:'Email authentication hardening',
 d:'Deploys SPF, DKIM and DMARC with a reject policy so attackers cannot spoof the organization\'s domains. The core anti-impersonation control for email.',
 ind:['domain without any DMARC record','DMARC policy stuck at none for over a year','SPF record with too many lookups'],
 ctl:[['DMARC reject','Policy progresses none -> quarantine -> reject on a schedule.'],['Aggregate reports','RUA reports feed a dashboard of spoofing attempts.'],['Subdomain coverage','Policy covers every subdomain, not just the apex.']],
 rem:'Move one policy step per quarter until reject; monitor reports for legitimate senders before each step.',
 tc:['DMARC record audit across 12 domains','Spoofing simulation against the lab domain','RUA report review drill']},
{cat:'remediation',cls:'vulnerability',t:'Vulnerability disclosure intake drill',
 d:'Practices receiving an external vulnerability report: acknowledge fast, triage honestly, fix, and credit the reporter. Good intake turns strangers into allies.',
 ind:['report sat unacknowledged for 5 days','no published security contact','triage stalled waiting for ownership'],
 ctl:[['Published contact','security.txt and a monitored inbox.'],['SLA clock','Acknowledge in 2 business days, triage in 5.'],['Safe harbor','Policy protects good-faith researchers.']],
 rem:'Run the drill with a synthetic report, time every handoff, and fix the slowest one.',
 tc:['Synthetic report intake timing','security.txt presence check','Researcher comms dry run']},
{cat:'threats',cls:'insider',t:'Insider-risk awareness exercise',
 d:'A discussion exercise on insider-risk indicators and proportionate responses — focused on support and least-intrusive controls, never surveillance overreach.',
 ind:['mass download before a resignation date in the scenario','privilege escalation requests outside role in the scenario','policy exception shopping in the scenario'],
 ctl:[['Least privilege','Limits what any one person can take.'],['Clear offboarding','Access revoked same-day, accounts audited.'],['Support channels','People with grievances get help before they become risks.']],
 rem:'Debrief with HR and legal; keep the exercise focused on process, not on any individual.',
 tc:['Scenario walkthrough with managers','Offboarding checklist audit','Privilege review for sensitive roles']},
{cat:'vulnerabilities',cls:'supply-chain',t:'Dependency freshness audit',
 d:'Audits third-party dependencies for known-vulnerable versions and unmaintained packages. Supply-chain risk hides in the transitive tree.',
 ind:['direct dependency two majors behind','transitive dependency with a known CVE past SLA','abandoned package with no maintainer activity'],
 ctl:[['Software bill of materials','Every build emits an SBOM; diffs are reviewed.'],['Automated update PRs','Dependabot-style PRs keep the tree fresh.'],['Allow-list for critical paths','High-risk components need explicit approval.']],
 rem:'Patch the known-vulnerable items immediately; schedule upgrades or replacements for the abandoned ones.',
 tc:['SBOM diff review for the last release','Transitive-tree vulnerability scan','Abandoned-package replacement plan']},
{cat:'controls',cls:'endpoint',t:'Endpoint baseline hardening check',
 d:'Checks endpoints against a hardened baseline: disk encryption, firewall on, auto-update on, no local admin for daily use. Drift gets remediated, not just reported.',
 ind:['endpoint without disk encryption','local admin on a daily-use account','auto-update disabled'],
 ctl:[['Configuration baseline','One gold image standard, enforced by policy.'],['Drift remediation','Non-compliant endpoints auto-remediate or quarantine.'],['No daily-driver admin','Elevation is just-in-time, never standing.']],
 rem:'Remediate the drift list weekly; investigate repeat offenders for broken policy delivery.',
 tc:['Baseline compliance scan of 120 endpoints','Drift remediation timing test','Gold-image rebuild verification']},
{cat:'test-cases',cls:'validation',t:'Incident severity triage quiz',
 d:'A synthetic quiz: given 10 scenario blurbs, assign SEV-1 through SEV-4 and the first three actions. Trains fast, consistent triage calls.',
 ind:['trainee declares SEV-1 for a single-user issue','containment step skipped in the answer','comms owner unassigned in the answer'],
 ctl:[['Severity rubric','One page: criteria plus three examples per level.'],['First-30-minutes checklist','Declare, contain, communicate — in that order.'],['Triage buddy','New analysts pair with a senior for their first quarter.']],
 rem:'Review answers as a team; update the rubric wherever reasonable people disagreed.',
 tc:['10-scenario triage quiz','First-30-minutes drill','Rubric update workshop']},
{cat:'remediation',cls:'access',t:'Stale access cleanup sprint',
 d:'A time-boxed sprint revoking stale access: ex-employees, completed contractors, finished projects. The fastest risk reduction per hour in identity security.',
 ind:['active account for someone who left 6 months ago','contractor access past contract end','project share still open a year after close'],
 ctl:[['HR-driven deprovisioning','Exit events revoke access automatically.'],['Contract end dates','Contractor accounts expire on the contract date.'],['Project share lifecycle','Shares close when the project closes.']],
 rem:'Sprint quarterly; automate whatever the sprint keeps finding by hand.',
 tc:['Stale-account hunt across the directory','Contractor expiry audit','Project-share closure sweep']}
];

function synthId(seed){
  var d=String(seed%10000).padStart(4,'0');
  var sum=0;for(var i=0;i<4;i++)sum+=+d[i];
  return 'SYN-'+d+'-'+(sum%10);
}
function checkSynth(id){
  var m=/^SYN-(\d{4})-(\d)$/.exec(id||'');
  if(!m)return false;
  var sum=0;for(var i=0;i<4;i++)sum+=+m[1][i];
  return String(sum%10)===m[2];
}

function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var pool=opts.category?SCEN.filter(function(s){return s.cat===opts.category;}):SCEN;
  if(!pool.length)pool=SCEN;
  var s=pick(pool,rnd);
  var sev=pick(SEVS,rnd);
  if(s.cls==='ransomware'||s.cls==='phishing')sev=pick(['critical','high'],rnd);
  var inds=shuffle(s.ind,rnd).slice(0,3);
  var ctls=shuffle(s.ctl,rnd).slice(0,3).map(function(c){return {control:c[0],detail:c[1]};});
  var tcs=shuffle(s.tc,rnd).slice(0,2).map(function(t){
    return {scenario:'Synthetic training scenario: '+t+'.',expected:'Team completes the exercise and files findings; no production systems are touched.',
      note:'Clearly labeled synthetic — for training and validation only.',synthetic:true};
  });
  tcs.push({scenario:'Synthetic training scenario: red-team-free walkthrough of the full control set.',
    expected:'All controls demonstrated working; gaps ticketed with owners.',
    note:'Clearly labeled synthetic — for training and validation only.',synthetic:true});
  var id=PREFIX+String(seed).padStart(7,'0');
  var rem=s.rem;
  if(rem.length<80)rem+=' Re-run the sprint on a fixed cadence; automate whatever the team keeps finding by hand.';
  return {id:id,title:s.t+' — defensive drill '+synthId(seed),category:s.cat,
    threat_class:s.cls,severity:sev,synthetic_id:synthId(seed),
    description:s.d+' This is a defensive record: it describes how to detect, prevent, and recover — never how to attack. Severity for this instance is rated '+sev+'.',
    indicators:inds,controls:ctls,remediation:rem,
    test_cases:tcs,references:['Defensive control catalog — internal training reference','NIST Cybersecurity Framework 2.0 (functions: Govern, Identify, Protect, Detect, Respond, Recover)'],
    source:'signature',creation_mode:'SIGNATURE-GENERATED',_seed:seed};
}

function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-SEC-\d{7}$/.test(r.id||''))e.push('id');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(SEVS.indexOf(r.severity)<0)e.push('severity');
  if(typeof r.threat_class!=='string'||!r.threat_class.length)e.push('threat_class');
  if(typeof r.title!=='string'||r.title.length<8)e.push('title');
  if(typeof r.description!=='string'||r.description.length<120)e.push('description');
  if(!Array.isArray(r.indicators)||r.indicators.length<2||r.indicators.length>6)e.push('indicators');
  else r.indicators.forEach(function(x){if(typeof x!=='string'||!x.length)e.push('indicator');});
  if(!Array.isArray(r.controls)||r.controls.length<2||r.controls.length>5)e.push('controls');
  else r.controls.forEach(function(c){if(!c||typeof c.control!=='string'||typeof c.detail!=='string')e.push('control');});
  if(typeof r.remediation!=='string'||r.remediation.length<80)e.push('remediation');
  if(!Array.isArray(r.test_cases)||r.test_cases.length<2||r.test_cases.length>4)e.push('test_cases');
  else r.test_cases.forEach(function(t){
    if(!t||typeof t.scenario!=='string'||typeof t.expected!=='string'||typeof t.note!=='string')e.push('test_case');
    if(r.source==='signature'&&t.synthetic!==true)e.push('synthetic');
  });
  if(!Array.isArray(r.references)||!r.references.length)e.push('references');
  if(r.source!=='signature'&&r.source!=='online')e.push('source');
  if(r.source==='signature'&&r.creation_mode!=='SIGNATURE-GENERATED')e.push('creation_mode');
  if(r.source==='online'&&!(typeof r.source_ref==='string'&&r.source_ref.length))e.push('source_ref');
  /* REAL invariants: no real CVE IDs in generated records; check-digit on synthetic_id. */
  if(r.source==='signature'){
    if(/CVE-\d{4}-\d{4,}/.test(r.title+' '+r.description))e.push('cve-leak');
    if(!checkSynth(r.synthetic_id))e.push('synthetic_id');
  }
  if(r.cve_id){
    if(!/^CVE-\d{4}-\d{4,}$/.test(r.cve_id))e.push('cve_id');
    if(r.source!=='online')e.push('cve-source');
    var hit=(r.references||[]).some(function(x){return String(x).indexOf(r.cve_id)>=0;});
    if(!hit)e.push('cve-ref');
  }
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-cybersecurity-1.0',generate:generate,validate:validate,PREFIX:PREFIX};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('cybersecurity',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
