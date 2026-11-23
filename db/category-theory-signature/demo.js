// Demo for the The Signature Category Theory Database database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Evidence status is stated
// exactly as the sources support it; an open problem is reported
// open. Signature framing is a SIGNATURE DESIGN CLAIM only.
const RECORDS = [{"id": "JAH-CATS-000001", "title": "Signature Arrow Atlas: A Design Study", "subject": "Signature arrow atlas design study"}, {"id": "JAH-CATS-000002", "title": "Signature Morphism Workbench: A Design Study", "subject": "Signature morphism workbench design study"}, {"id": "JAH-CATS-000003", "title": "Signature Functor Bridge: A Design Study", "subject": "Signature functor bridge design study"}, {"id": "JAH-CATS-000004", "title": "Signature Naturality Checker: A Design Study", "subject": "Signature naturality checker design study"}, {"id": "JAH-CATS-000005", "title": "Signature Yoneda Explorer: A Design Study", "subject": "Signature Yoneda explorer design study"}, {"id": "JAH-CATS-000006", "title": "Signature Adjunction Pairing Bench: A Design Study", "subject": "Signature adjunction pairing bench design study"}, {"id": "JAH-CATS-000007", "title": "Signature Limit Builder: A Design Study", "subject": "Signature limit builder design study"}, {"id": "JAH-CATS-000008", "title": "Signature Colimit Gluer: A Design Study", "subject": "Signature colimit gluer design study"}, {"id": "JAH-CATS-000009", "title": "Signature Monad Workshop: A Design Study", "subject": "Signature monad workshop design study"}, {"id": "JAH-CATS-000010", "title": "Signature Universal Property Studio: A Design Study", "subject": "Signature universal property studio design study"}, {"id": "JAH-CATS-000011", "title": "Signature Cartesian Closed Lab: A Design Study", "subject": "Signature cartesian closed lab design study"}, {"id": "JAH-CATS-000012", "title": "Signature Topos Universe Simulator: A Design Study", "subject": "Signature topos universe simulator design study"}, {"id": "JAH-CATS-000013", "title": "Signature Abelian Ledger: A Design Study", "subject": "Signature abelian ledger design study"}, {"id": "JAH-CATS-000014", "title": "Signature Tensor Loom: A Design Study", "subject": "Signature tensor loom design study"}, {"id": "JAH-CATS-000015", "title": "Signature Enrichment Studio: A Design Study", "subject": "Signature enrichment studio design study"}, {"id": "JAH-CATS-000016", "title": "Signature Kan Extension Engine: A Design Study", "subject": "Signature Kan extension engine design study"}, {"id": "JAH-CATS-000017", "title": "Signature Sheaf Garden: A Design Study", "subject": "Signature sheaf garden design study"}, {"id": "JAH-CATS-000018", "title": "Signature Site Builder: A Design Study", "subject": "Signature site builder design study"}, {"id": "JAH-CATS-000019", "title": "Signature Derived Workshop: A Design Study", "subject": "Signature derived workshop design study"}, {"id": "JAH-CATS-000020", "title": "Signature Higher Category Climber: A Design Study", "subject": "Signature higher category climber design study"}, {"id": "JAH-CATS-000021", "title": "Signature Equivalence Tester: A Design Study", "subject": "Signature equivalence tester design study"}, {"id": "JAH-CATS-000022", "title": "Signature Free Category Generator: A Design Study", "subject": "Signature free category generator design study"}, {"id": "JAH-CATS-000023", "title": "Signature Exponential Studio: A Design Study", "subject": "Signature exponential studio design study"}, {"id": "JAH-CATS-000024", "title": "Signature Forgetful Lens: A Design Study", "subject": "Signature forgetful lens design study"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: category-theory-signature');
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
