// Demo for the The Signature Photonic Computing Database database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Horizons are PLANNING WINDOWS,
// never predictions. Public records are documented evidence; Signature
// records are design-study, never authentic public record.
const RECORDS = [{"id": "JAH-PHTCS-000001", "title": "Signature Design: Light Library", "subject": "signature light library"}, {"id": "JAH-PHTCS-000002", "title": "Signature Design: Waveguide Garden", "subject": "signature waveguide garden"}, {"id": "JAH-PHTCS-000003", "title": "Signature Design: Silicon Orchard", "subject": "signature silicon orchard"}, {"id": "JAH-PHTCS-000004", "title": "Signature Design: Integrated Circuit City", "subject": "signature integrated circuit city"}, {"id": "JAH-PHTCS-000005", "title": "Signature Design: Optical Brain Loft", "subject": "signature optical brain loft"}, {"id": "JAH-PHTCS-000006", "title": "Signature Design: Two-Path Mill", "subject": "signature two-path mill"}, {"id": "JAH-PHTCS-000007", "title": "Signature Design: Ring Pond", "subject": "signature ring pond"}, {"id": "JAH-PHTCS-000008", "title": "Signature Design: Rainbow Post Office", "subject": "signature rainbow post office"}, {"id": "JAH-PHTCS-000009", "title": "Signature Design: Memory Attic", "subject": "signature memory attic"}, {"id": "JAH-PHTCS-000010", "title": "Signature Design: Photon Courier Guild", "subject": "signature photon courier guild"}, {"id": "JAH-PHTCS-000011", "title": "Signature Design: Data Center Light Railway", "subject": "signature data center light railway"}, {"id": "JAH-PHTCS-000012", "title": "Signature Design: Nonlinear Prism House", "subject": "signature nonlinear prism house"}, {"id": "JAH-PHTCS-000013", "title": "Signature Design: Tensor Mill", "subject": "signature tensor mill"}, {"id": "JAH-PHTCS-000014", "title": "Signature Design: Coherence Choir", "subject": "signature coherence choir"}, {"id": "JAH-PHTCS-000015", "title": "Signature Design: Sensor Lanterns", "subject": "signature sensor lanterns"}, {"id": "JAH-PHTCS-000016", "title": "Signature Design: Energy Ledger", "subject": "signature energy ledger"}, {"id": "JAH-PHTCS-000017", "title": "Signature Design: Chip Bakery", "subject": "signature chip bakery"}, {"id": "JAH-PHTCS-000018", "title": "Signature Design: Testing Lighthouse", "subject": "signature testing lighthouse"}, {"id": "JAH-PHTCS-000019", "title": "Signature Design: Compiler Loom", "subject": "signature compiler loom"}, {"id": "JAH-PHTCS-000020", "title": "Signature Design: Logic Gate Garden", "subject": "signature logic gate garden"}, {"id": "JAH-PHTCS-000021", "title": "Signature Design: Reservoir Lake", "subject": "signature reservoir lake"}, {"id": "JAH-PHTCS-000022", "title": "Signature Design: Hybrid House", "subject": "signature hybrid house"}, {"id": "JAH-PHTCS-000023", "title": "Signature Design: AI Mill Race", "subject": "signature AI mill race"}, {"id": "JAH-PHTCS-000024", "title": "Signature Design: Photonic City of Light", "subject": "signature photonic city of light"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: photonic-computing-signature');
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
