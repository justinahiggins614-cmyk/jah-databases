// Demo for the The Signature Space Mission Database database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. NASA-level means engineering
// targets modeled on public NASA standards, never NASA certification,
// approval, affiliation, funding, or endorsement. No design here is
// presented as flight-ready. JAH live retrieval was NOT verified.
const RECORDS = [{"id": "JAH-SPMIS-000001", "title": "Signature Lunar Shuttle Mission Design", "subject": "Signature lunar shuttle mission design"}, {"id": "JAH-SPMIS-000002", "title": "Signature Mars Transit Habitat Mission", "subject": "Signature Mars transit habitat mission"}, {"id": "JAH-SPMIS-000003", "title": "Signature Asteroid Survey Mission", "subject": "Signature asteroid survey mission"}, {"id": "JAH-SPMIS-000004", "title": "Signature Earth-Moon Cycler Mission", "subject": "Signature Earth-Moon cycler mission"}, {"id": "JAH-SPMIS-000005", "title": "Signature Lunar Polar Base Supply Mission", "subject": "Signature lunar polar base supply mission"}, {"id": "JAH-SPMIS-000006", "title": "Signature Mars Surface Sortie Mission", "subject": "Signature Mars surface sortie mission"}, {"id": "JAH-SPMIS-000007", "title": "Signature Deep Space Observatory Mission", "subject": "Signature deep space observatory mission"}, {"id": "JAH-SPMIS-000008", "title": "Signature Venus Atmospheric Survey Mission", "subject": "Signature Venus atmospheric survey mission"}, {"id": "JAH-SPMIS-000009", "title": "Signature Jupiter Flyby Science Mission", "subject": "Signature Jupiter flyby science mission"}, {"id": "JAH-SPMIS-000010", "title": "Signature Comet Sample Return Mission", "subject": "Signature comet sample return mission"}, {"id": "JAH-SPMIS-000011", "title": "Signature Orbital Debris Survey Mission", "subject": "Signature orbital debris survey mission"}, {"id": "JAH-SPMIS-000012", "title": "Signature Lunar Far Side Radio Mission", "subject": "Signature lunar far side radio mission"}, {"id": "JAH-SPMIS-000013", "title": "Signature Mars Relay Constellation Mission", "subject": "Signature Mars relay constellation mission"}, {"id": "JAH-SPMIS-000014", "title": "Signature Titan Reconnaissance Mission", "subject": "Signature Titan reconnaissance mission"}, {"id": "JAH-SPMIS-000015", "title": "Signature Solar Polar Observation Mission", "subject": "Signature solar polar observation mission"}, {"id": "JAH-SPMIS-000016", "title": "Signature Near-Earth Object Patrol Mission", "subject": "Signature near-Earth object patrol mission"}, {"id": "JAH-SPMIS-000017", "title": "Signature Lunar Lava Tube Survey Mission", "subject": "Signature lunar lava tube survey mission"}, {"id": "JAH-SPMIS-000018", "title": "Signature Mars Polar Cap Mission", "subject": "Signature Mars polar cap mission"}, {"id": "JAH-SPMIS-000019", "title": "Signature Interstellar Precursor Mission", "subject": "Signature interstellar precursor mission"}, {"id": "JAH-SPMIS-000020", "title": "Signature Earth Observation Constellation Mission", "subject": "Signature Earth observation constellation mission"}, {"id": "JAH-SPMIS-000021", "title": "Signature Lunar Construction Support Mission", "subject": "Signature lunar construction support mission"}, {"id": "JAH-SPMIS-000022", "title": "Signature Asteroid Deflection Study Mission", "subject": "Signature asteroid deflection study mission"}, {"id": "JAH-SPMIS-000023", "title": "Signature Cislunar Logistics Mission", "subject": "Signature cislunar logistics mission"}, {"id": "JAH-SPMIS-000024", "title": "Signature Deep Space Crew Transit Mission", "subject": "Signature deep space crew transit mission"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: space-mission-signature');
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
