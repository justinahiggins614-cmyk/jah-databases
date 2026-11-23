// Demo for the The Signature Theoretical Computer Science Database database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Evidence status is stated
// exactly as the sources support it; an open problem is reported
// open. Signature framing is a SIGNATURE DESIGN CLAIM only.
const RECORDS = [{"id": "JAH-THCSS-000001", "title": "Signature Turing Bench: A Design Study", "subject": "Signature Turing bench design study"}, {"id": "JAH-THCSS-000002", "title": "Signature Tableau Builder: A Design Study", "subject": "Signature tableau builder design study"}, {"id": "JAH-THCSS-000003", "title": "Signature Open Problem Observatory: A Design Study", "subject": "Signature open problem observatory design study"}, {"id": "JAH-THCSS-000004", "title": "Signature Reduction Web: A Design Study", "subject": "Signature reduction web design study"}, {"id": "JAH-THCSS-000005", "title": "Signature Verifier Studio: A Design Study", "subject": "Signature verifier studio design study"}, {"id": "JAH-THCSS-000006", "title": "Signature Hierarchy Climber: A Design Study", "subject": "Signature hierarchy climber design study"}, {"id": "JAH-THCSS-000007", "title": "Signature Reachability Lab: A Design Study", "subject": "Signature reachability lab design study"}, {"id": "JAH-THCSS-000008", "title": "Signature Spot-Check Studio: A Design Study", "subject": "Signature spot-check studio design study"}, {"id": "JAH-THCSS-000009", "title": "Signature Middle-Ground Explorer: A Design Study", "subject": "Signature middle-ground explorer design study"}, {"id": "JAH-THCSS-000010", "title": "Signature Program Property Lab: A Design Study", "subject": "Signature program property lab design study"}, {"id": "JAH-THCSS-000011", "title": "Signature Circuit Bench: A Design Study", "subject": "Signature circuit bench design study"}, {"id": "JAH-THCSS-000012", "title": "Signature Coin-Flip Lab: A Design Study", "subject": "Signature coin-flip lab design study"}, {"id": "JAH-THCSS-000013", "title": "Signature Conversation Verifier: A Design Study", "subject": "Signature conversation verifier design study"}, {"id": "JAH-THCSS-000014", "title": "Signature Secret-Keeper: A Design Study", "subject": "Signature secret-keeper design study"}, {"id": "JAH-THCSS-000015", "title": "Signature Period Finder: A Design Study", "subject": "Signature period finder design study"}, {"id": "JAH-THCSS-000016", "title": "Signature Qubit Garden: A Design Study", "subject": "Signature qubit garden design study"}, {"id": "JAH-THCSS-000017", "title": "Signature Quantum Toybox: A Design Study", "subject": "Signature quantum toybox design study"}, {"id": "JAH-THCSS-000018", "title": "Signature Message Cost Meter: A Design Study", "subject": "Signature message cost meter design study"}, {"id": "JAH-THCSS-000019", "title": "Signature Parameter Lens: A Design Study", "subject": "Signature parameter lens design study"}, {"id": "JAH-THCSS-000020", "title": "Signature Near-Optimum Studio: A Design Study", "subject": "Signature near-optimum studio design study"}, {"id": "JAH-THCSS-000021", "title": "Signature Agreement Impossibility Demo: A Design Study", "subject": "Signature agreement impossibility demo design study"}, {"id": "JAH-THCSS-000022", "title": "Signature One-Way Workbench: A Design Study", "subject": "Signature one-way workbench design study"}, {"id": "JAH-THCSS-000023", "title": "Signature Randomness Remover: A Design Study", "subject": "Signature randomness remover design study"}, {"id": "JAH-THCSS-000024", "title": "Signature Complexity Atlas: A Design Study", "subject": "Signature complexity atlas design study"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: theoretical-computer-science-signature');
  console.log('EDITION: signature');
  console.log('RECORDS: '+RECORDS.length);
  const words0=RECORDS[0].title.split(/\s+/).filter(w=>w.length>3);
  const q1=(words0[0]||RECORDS[0].title.split(/\s+/)[0]).toLowerCase();
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
