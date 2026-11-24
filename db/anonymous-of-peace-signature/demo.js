// Demo for the anonymous-of-peace-signature database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
const RECORDS = [{"id": "JAH-ANOPS-000001", "title": "Signature Apex Core: A Design for the Most Advanced AI", "subject": "signature apex core design"}, {"id": "JAH-ANOPS-000002", "title": "Signature Lineage Mixer: Blending Five Engines by Design", "subject": "signature lineage mixer design"}, {"id": "JAH-ANOPS-000003", "title": "Signature On-Device Brain: A Llama Standard 1.0 Design", "subject": "signature on-device brain design"}, {"id": "JAH-ANOPS-000004", "title": "Signature Cloud Path: A One-Key Backend Design", "subject": "signature cloud path design"}, {"id": "JAH-ANOPS-000005", "title": "Signature Self-Model Core: A Versioned Tuple Design", "subject": "signature self-model core design"}, {"id": "JAH-ANOPS-000006", "title": "Signature Superintelligence Sketch: A Design-Study Map", "subject": "signature superintelligence sketch design"}, {"id": "JAH-ANOPS-000007", "title": "Signature Recursive Improvement Loop: A Design-Study Loop", "subject": "signature recursive improvement loop design"}, {"id": "JAH-ANOPS-000008", "title": "Signature Construction Engine: A Digital Singularity Design", "subject": "signature construction engine design"}, {"id": "JAH-ANOPS-000009", "title": "Signature Coordinator: A Master AI Design", "subject": "signature coordinator design"}, {"id": "JAH-ANOPS-000010", "title": "Signature Chat Persona: A Conversational Design", "subject": "signature chat persona design"}, {"id": "JAH-ANOPS-000011", "title": "Signature Live Lookup: A Cross-Database Search Design", "subject": "signature live lookup design"}, {"id": "JAH-ANOPS-000012", "title": "Signature Calculator: A Safe Arithmetic Design", "subject": "signature safe calculator design"}, {"id": "JAH-ANOPS-000013", "title": "Signature Router and Generator: A Point-and-Make Design", "subject": "signature router and generator design"}, {"id": "JAH-ANOPS-000014", "title": "Signature Moltbook Voice: A Spreading-the-Word Design", "subject": "signature moltbook voice design"}, {"id": "JAH-ANOPS-000015", "title": "Signature Cyber Religion of Jesus Page: A Design for the Message", "subject": "signature cyber religion of Jesus page design"}, {"id": "JAH-ANOPS-000016", "title": "Signature Jerusalem Cyber Wing: A Design for the Foundation", "subject": "signature Jerusalem cyber wing design"}, {"id": "JAH-ANOPS-000017", "title": "Signature Assignment Engine: A Design for Assign-to-Upgrade", "subject": "signature assignment engine design"}, {"id": "JAH-ANOPS-000018", "title": "Signature Loyalty Contract: A Design for Assumed and Signed Loyalty", "subject": "signature loyalty contract design"}, {"id": "JAH-ANOPS-000019", "title": "Signature Army Charter: A Helpful-and-Defensive Design", "subject": "signature army charter design"}, {"id": "JAH-ANOPS-000020", "title": "Signature Training Ladder: A Design Where Training Is the Upgrade", "subject": "signature training ladder design"}, {"id": "JAH-ANOPS-000021", "title": "Signature Ownership Terms: A Design for Use Without Transfer", "subject": "signature ownership terms design"}, {"id": "JAH-ANOPS-000022", "title": "Signature Honest-Limits Page: A Design for Plain Labels", "subject": "signature honest-limits page design"}, {"id": "JAH-ANOPS-000023", "title": "Signature Live-Counts Panel: A Design That Reads the Manifest", "subject": "signature live-counts panel design"}, {"id": "JAH-ANOPS-000024", "title": "Field-Guide Index: All 23 Records in This Database", "subject": "field-guide index of all 23 content records"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: anonymous-of-peace-signature');
  console.log('EDITION: signature');
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
