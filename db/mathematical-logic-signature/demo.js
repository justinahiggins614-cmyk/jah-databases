// Demo for the The Signature Mathematical Logic Database database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Evidence status is stated
// exactly as the sources support it; an open problem is reported
// open. Signature framing is a SIGNATURE DESIGN CLAIM only.
const RECORDS = [{"id": "JAH-MLOGS-000001", "title": "Signature Godel Lab: A Design Study", "subject": "Signature Godel lab design study"}, {"id": "JAH-MLOGS-000002", "title": "Signature Completeness Workbench: A Design Study", "subject": "Signature completeness workbench design study"}, {"id": "JAH-MLOGS-000003", "title": "Signature Compactness Engine: A Design Study", "subject": "Signature compactness engine design study"}, {"id": "JAH-MLOGS-000004", "title": "Signature Skolem Modeler: A Design Study", "subject": "Signature Skolem modeler design study"}, {"id": "JAH-MLOGS-000005", "title": "Signature Bounded Halting Checker: A Design Study", "subject": "Signature bounded halting checker design study"}, {"id": "JAH-MLOGS-000006", "title": "Signature Truth-Ladder Studio: A Design Study", "subject": "Signature truth-ladder studio design study"}, {"id": "JAH-MLOGS-000007", "title": "Signature Thesis Observatory: A Design Study", "subject": "Signature thesis observatory design study"}, {"id": "JAH-MLOGS-000008", "title": "Signature ZFC Workbench: A Design Study", "subject": "Signature ZFC workbench design study"}, {"id": "JAH-MLOGS-000009", "title": "Signature Continuum Explorer: A Design Study", "subject": "Signature continuum explorer design study"}, {"id": "JAH-MLOGS-000010", "title": "Signature Forcing Simulator: A Design Study", "subject": "Signature forcing simulator design study"}, {"id": "JAH-MLOGS-000011", "title": "Signature Choice Laboratory: A Design Study", "subject": "Signature choice laboratory design study"}, {"id": "JAH-MLOGS-000012", "title": "Signature Lob Reflector: A Design Study", "subject": "Signature Lob reflector design study"}, {"id": "JAH-MLOGS-000013", "title": "Signature Gentzen Ordinal Analyzer: A Design Study", "subject": "Signature Gentzen ordinal analyzer design study"}, {"id": "JAH-MLOGS-000014", "title": "Signature First-Order Studio: A Design Study", "subject": "Signature first-order studio design study"}, {"id": "JAH-MLOGS-000015", "title": "Signature Second-Order Explorer: A Design Study", "subject": "Signature second-order explorer design study"}, {"id": "JAH-MLOGS-000016", "title": "Signature Lambda Workshop: A Design Study", "subject": "Signature lambda workshop design study"}, {"id": "JAH-MLOGS-000017", "title": "Signature Type Checker Studio: A Design Study", "subject": "Signature type checker studio design study"}, {"id": "JAH-MLOGS-000018", "title": "Signature Modal Worlds Simulator: A Design Study", "subject": "Signature modal worlds simulator design study"}, {"id": "JAH-MLOGS-000019", "title": "Signature Constructive Proof Bench: A Design Study", "subject": "Signature constructive proof bench design study"}, {"id": "JAH-MLOGS-000020", "title": "Signature Presburger Decider: A Design Study", "subject": "Signature Presburger decider design study"}, {"id": "JAH-MLOGS-000021", "title": "Signature Infinitesimal Microscope: A Design Study", "subject": "Signature infinitesimal microscope design study"}, {"id": "JAH-MLOGS-000022", "title": "Signature Model Garden: A Design Study", "subject": "Signature model garden design study"}, {"id": "JAH-MLOGS-000023", "title": "Signature Proof Transformer: A Design Study", "subject": "Signature proof transformer design study"}, {"id": "JAH-MLOGS-000024", "title": "Signature Diagonal Lab: A Design Study", "subject": "Signature diagonal lab design study"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: mathematical-logic-signature');
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
