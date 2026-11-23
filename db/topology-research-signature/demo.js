// Demo for the The Signature Topology Research Database database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Evidence status is stated
// exactly as the sources support it; an open problem is reported
// open. Signature framing is a SIGNATURE DESIGN CLAIM only.
const RECORDS = [{"id": "JAH-TOPRS-000001", "title": "Signature Topology Studio: Open-Set Workbench", "subject": "Signature open-set workbench"}, {"id": "JAH-TOPRS-000002", "title": "Signature Compactness Checker", "subject": "Signature compactness checker"}, {"id": "JAH-TOPRS-000003", "title": "Signature Connectedness Explorer", "subject": "Signature connectedness explorer"}, {"id": "JAH-TOPRS-000004", "title": "Signature Hausdorff Separator", "subject": "Signature Hausdorff separator"}, {"id": "JAH-TOPRS-000005", "title": "Signature Product-Quotient Builder", "subject": "Signature product-quotient builder"}, {"id": "JAH-TOPRS-000006", "title": "Signature Loop Counter: Fundamental Group Lab", "subject": "Signature fundamental group lab"}, {"id": "JAH-TOPRS-000007", "title": "Signature Homotopy Deformer", "subject": "Signature homotopy deformer"}, {"id": "JAH-TOPRS-000008", "title": "Signature Homology Calculator", "subject": "Signature homology calculator"}, {"id": "JAH-TOPRS-000009", "title": "Signature Euler Characteristic Counter", "subject": "Signature Euler counter"}, {"id": "JAH-TOPRS-000010", "title": "Signature Manifold Atlas Viewer", "subject": "Signature manifold atlas viewer"}, {"id": "JAH-TOPRS-000011", "title": "Signature Surface Classifier", "subject": "Signature surface classifier"}, {"id": "JAH-TOPRS-000012", "title": "Signature Knot Untangler", "subject": "Signature knot untangler"}, {"id": "JAH-TOPRS-000013", "title": "Signature Covering Space Unwrapper", "subject": "Signature covering unwrapper"}, {"id": "JAH-TOPRS-000014", "title": "Signature Fixed-Point Finder", "subject": "Signature fixed-point finder"}, {"id": "JAH-TOPRS-000015", "title": "Signature Jordan Curve Tester", "subject": "Signature Jordan curve tester"}, {"id": "JAH-TOPRS-000016", "title": "Signature Urysohn Function Builder", "subject": "Signature Urysohn function builder"}, {"id": "JAH-TOPRS-000017", "title": "Signature Compactification Adder", "subject": "Signature compactification adder"}, {"id": "JAH-TOPRS-000018", "title": "Signature Antipodal Pair Finder", "subject": "Signature antipodal pair finder"}, {"id": "JAH-TOPRS-000019", "title": "Signature Triangulation Builder", "subject": "Signature triangulation builder"}, {"id": "JAH-TOPRS-000020", "title": "Signature Lie Group Explorer", "subject": "Signature Lie group explorer"}, {"id": "JAH-TOPRS-000021", "title": "Signature Van Kampen Gluer", "subject": "Signature van Kampen gluer"}, {"id": "JAH-TOPRS-000022", "title": "Signature Metric Space Completer", "subject": "Signature metric space completer"}, {"id": "JAH-TOPRS-000023", "title": "Signature Open Problem Board: Topology", "subject": "Signature topology problem board"}, {"id": "JAH-TOPRS-000024", "title": "Signature Shape Sorter", "subject": "Signature shape sorter"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: topology-research-signature');
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
