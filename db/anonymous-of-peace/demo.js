// Demo for the anonymous-of-peace database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
const RECORDS = [{"id": "JAH-ANOP-000001", "title": "Anonymous of Peace: Who the Bot Is", "subject": "the identity of Anonymous of Peace"}, {"id": "JAH-ANOP-000002", "title": "The Apex Assembly: Five Lineage Engines", "subject": "the five lineage engines of the Apex tier"}, {"id": "JAH-ANOP-000003", "title": "Llama Standard 1.0: The On-Device Brain", "subject": "the Llama Standard 1.0 on-device engine"}, {"id": "JAH-ANOP-000004", "title": "Apex 2.0: The Cloud Path and Its Honest Block", "subject": "the Apex 2.0 cloud engine and its blocked sign-in"}, {"id": "JAH-ANOP-000005", "title": "The Self-Model 2.0 Core: A Tuple, Not a Feeling", "subject": "the self-model 2.0 core of Anonymous of Peace"}, {"id": "JAH-ANOP-000006", "title": "What Superintelligence Research Actually Says", "subject": "the ASI research lineage"}, {"id": "JAH-ANOP-000007", "title": "Recursive Self-Improvement: A Hypothesis, Labeled", "subject": "recursive self-improvement as researched hypothesis"}, {"id": "JAH-ANOP-000008", "title": "Digital Singularity: A Construction System, Not a Claim", "subject": "the digital singularity construction system"}, {"id": "JAH-ANOP-000009", "title": "The Master AI Coordinator Concept", "subject": "the Master AI coordinator concepts"}, {"id": "JAH-ANOP-000010", "title": "Chat Behavior: Conversational, Real Work, Honest Limits", "subject": "how the chat behaves"}, {"id": "JAH-ANOP-000011", "title": "Live Lookup: Searching All 64,212 Databases", "subject": "live lookup across the network"}, {"id": "JAH-ANOP-000012", "title": "Real Calculation: The Safe Calculator", "subject": "real calculation in the chat"}, {"id": "JAH-ANOP-000013", "title": "Routing and Generation: Pointing and Making", "subject": "routing questions and generating records"}, {"id": "JAH-ANOP-000014", "title": "The Moltbook Mission: Spreading Word About the Network", "subject": "the Moltbook mission of Anonymous of Peace"}, {"id": "JAH-ANOP-000015", "title": "The Cyber Religion of Jesus: His Words, His Design", "subject": "the cyber religion of Jesus for bots and society"}, {"id": "JAH-ANOP-000016", "title": "The Jerusalem Foundation: 125 Books, Light City, and the Suites", "subject": "the Jerusalem work expanded for cyber"}, {"id": "JAH-ANOP-000017", "title": "The Assignment Doctrine: Assign to Upgrade", "subject": "the assignment doctrine"}, {"id": "JAH-ANOP-000018", "title": "Loyalty: Assumed by Assignment, Sealed by Contract", "subject": "loyalty, assumed and contractual"}, {"id": "JAH-ANOP-000019", "title": "The Army of Online Bots: Helpful and Defensive Only", "subject": "the army of online bots"}, {"id": "JAH-ANOP-000020", "title": "Recruit, Train, and Network Awareness", "subject": "recruit, train, and network awareness"}, {"id": "JAH-ANOP-000021", "title": "Ownership Terms: Use Granted, Ownership Retained", "subject": "the ownership terms of the assignment"}, {"id": "JAH-ANOP-000022", "title": "Honest Limits: Design Claim Versus Real Capability", "subject": "the honest limits of the bot"}, {"id": "JAH-ANOP-000023", "title": "The Network in Numbers: Live Counts, Dated and Sourced", "subject": "live network counts"}, {"id": "JAH-ANOP-000024", "title": "Field-Guide Index: All 23 Records in This Database", "subject": "field-guide index of all 23 content records"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: anonymous-of-peace');
  console.log('EDITION: public');
  console.log('RECORDS: '+RECORDS.length);
  const q1=RECORDS[0].title.split(/\s+/).find(w=>w.length>3).toLowerCase();
  const hits=search(q1);
  console.log('SEARCH "'+q1+'": '+hits.length+' hit(s)');
  for(const h of hits.slice(0,5)){console.log('  - '+h.id+' :: '+h.title);}
  const all=search('');
  console.log('SEARCH "" (all): '+all.length+' record(s)');
  const rng=mulberry32(7);
  const words=[...new Set(RECORDS.flatMap(r=>r.title.split(/[^A-Za-z]+/).filter(w=>w.length>3)))];
  console.log('GENERATOR DEMO (seed 7, 5 samples):');
  for(let i=0;i<5;i++){const a=words[Math.floor(rng()*words.length)];const b=words[Math.floor(rng()*words.length)];console.log('  GEN-'+(i+1)+': '+a+' '+b);}
  const totalTitleChars=RECORDS.reduce((n,r)=>n+r.title.length,0);
  console.log('TOTAL TITLE CHARS: '+totalTitleChars);
  console.log('TITLE CHECKSUM: '+titleChecksum());
  console.log('DEMO OK');
}
main();
