// Demo for the The Signature Spacecraft Guidance Database database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. NASA-level means engineering
// targets modeled on public NASA standards, never NASA certification,
// approval, affiliation, funding, or endorsement. No design here is
// presented as flight-ready. JAH live retrieval was NOT verified.
const RECORDS = [{"id": "JAH-SGUIS-000001", "title": "Signature Adaptive Ascent Guidance Study", "subject": "signature adaptive ascent guidance"}, {"id": "JAH-SGUIS-000002", "title": "Signature Powered Descent Guidance Study", "subject": "signature powered descent guidance"}, {"id": "JAH-SGUIS-000003", "title": "Signature Rendezvous Guidance Study", "subject": "signature rendezvous guidance"}, {"id": "JAH-SGUIS-000004", "title": "Signature Docking Guidance Study", "subject": "signature docking guidance"}, {"id": "JAH-SGUIS-000005", "title": "Signature Quaternion Attitude Guidance Study", "subject": "signature quaternion attitude guidance"}, {"id": "JAH-SGUIS-000006", "title": "Signature Lambert Targeting Study", "subject": "signature Lambert targeting"}, {"id": "JAH-SGUIS-000007", "title": "Signature Entry Corridor Guidance Study", "subject": "signature entry corridor guidance"}, {"id": "JAH-SGUIS-000008", "title": "Signature Station-Keeping Guidance Study", "subject": "signature station-keeping guidance"}, {"id": "JAH-SGUIS-000009", "title": "Signature Formation Flying Guidance Study", "subject": "signature formation flying guidance"}, {"id": "JAH-SGUIS-000010", "title": "Signature Low-Thrust Guidance Study", "subject": "signature low-thrust guidance"}, {"id": "JAH-SGUIS-000011", "title": "Signature Asteroid Proximity Guidance Study", "subject": "signature asteroid proximity guidance"}, {"id": "JAH-SGUIS-000012", "title": "Signature Safe-Mode Guidance Study", "subject": "signature safe-mode guidance"}, {"id": "JAH-SGUIS-000013", "title": "Signature Terrain-Relative Landing Guidance Study", "subject": "signature terrain-relative landing guidance"}, {"id": "JAH-SGUIS-000014", "title": "Signature Aerocapture Guidance Study", "subject": "signature Mars aerocapture guidance"}, {"id": "JAH-SGUIS-000015", "title": "Signature Solar Sail Steering Study", "subject": "signature solar sail steering"}, {"id": "JAH-SGUIS-000016", "title": "Signature Servicing Approach Guidance Study", "subject": "signature servicing approach guidance"}, {"id": "JAH-SGUIS-000017", "title": "Signature Tether Deployment Guidance Study", "subject": "signature tether deployment guidance"}, {"id": "JAH-SGUIS-000018", "title": "Signature Earth Return Guidance Study", "subject": "signature Earth return guidance"}, {"id": "JAH-SGUIS-000019", "title": "Signature Lunar Insertion Guidance Study", "subject": "signature lunar insertion guidance"}, {"id": "JAH-SGUIS-000020", "title": "Signature Comet Flyby Guidance Study", "subject": "signature comet flyby guidance"}, {"id": "JAH-SGUIS-000021", "title": "Signature Spin Stabilization Guidance Study", "subject": "signature spin stabilization guidance"}, {"id": "JAH-SGUIS-000022", "title": "Signature Multi-Burn Orbit Raising Study", "subject": "signature multi-burn orbit raising"}, {"id": "JAH-SGUIS-000023", "title": "Signature Crossrange Guidance Study", "subject": "signature crossrange guidance"}, {"id": "JAH-SGUIS-000024", "title": "Signature Guidance Health Monitor Study", "subject": "signature guidance health monitor"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: spacecraft-guidance-signature');
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
