// Demo for the The Signature Rocket Propulsion Database database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. NASA-level means engineering
// targets modeled on public NASA standards, never NASA certification,
// approval, affiliation, funding, or endorsement. No design here is
// presented as flight-ready. JAH live retrieval was NOT verified.
const RECORDS = [{"id": "JAH-RPROS-000001", "title": "Signature Methalox Expander-Cycle Engine Concept", "subject": "the Signature methalox expander-cycle engine concept"}, {"id": "JAH-RPROS-000002", "title": "Signature Dual-Mode Chemical-Electric Stage Concept", "subject": "the Signature dual-mode chemical-electric stage concept"}, {"id": "JAH-RPROS-000003", "title": "Signature Aerospike Nozzle Concept", "subject": "the Signature aerospike nozzle concept"}, {"id": "JAH-RPROS-000004", "title": "Signature Green Propellant Thruster Concept", "subject": "the Signature green propellant thruster concept"}, {"id": "JAH-RPROS-000005", "title": "Signature Rotating Detonation Engine Study", "subject": "the Signature rotating detonation engine study"}, {"id": "JAH-RPROS-000006", "title": "Signature Solar-Electric Tug Concept", "subject": "the Signature solar-electric tug concept"}, {"id": "JAH-RPROS-000007", "title": "Signature Nuclear-Thermal Mars Transfer Stage Study", "subject": "the Signature nuclear-thermal Mars transfer stage study"}, {"id": "JAH-RPROS-000008", "title": "Signature Water-Electrolysis Propulsion Concept", "subject": "the Signature water-electrolysis propulsion concept"}, {"id": "JAH-RPROS-000009", "title": "Signature Magnetic Nozzle Plasma Concept", "subject": "the Signature magnetic nozzle plasma concept"}, {"id": "JAH-RPROS-000010", "title": "Signature Variable-Specific-Impulse Magnetoplasma Concept", "subject": "the Signature variable-specific-impulse magnetoplasma concept"}, {"id": "JAH-RPROS-000011", "title": "Signature In-Situ Propellant Production Concept", "subject": "the Signature in-situ propellant production concept"}, {"id": "JAH-RPROS-000012", "title": "Signature Reusable Booster Recovery Concept", "subject": "the Signature reusable booster recovery concept"}, {"id": "JAH-RPROS-000013", "title": "Signature Throttleable Lunar Lander Engine Concept", "subject": "the Signature throttleable lunar lander engine concept"}, {"id": "JAH-RPROS-000014", "title": "Signature CubeSat Micro-Propulsion Concept", "subject": "the Signature CubeSat micro-propulsion concept"}, {"id": "JAH-RPROS-000015", "title": "Signature Deep-Space Ion Array Concept", "subject": "the Signature deep-space ion array concept"}, {"id": "JAH-RPROS-000016", "title": "Signature Propellant Depot Concept", "subject": "the Signature propellant depot concept"}, {"id": "JAH-RPROS-000017", "title": "Signature Lightweight Composite Tank Concept", "subject": "the Signature lightweight composite tank concept"}, {"id": "JAH-RPROS-000018", "title": "Signature Autonomous Engine Health Monitor Concept", "subject": "the Signature autonomous engine health monitor concept"}, {"id": "JAH-RPROS-000019", "title": "Signature Multi-Mode Propulsion Bus Concept", "subject": "the Signature multi-mode propulsion bus concept"}, {"id": "JAH-RPROS-000020", "title": "Signature Solar Sail Cargo Concept", "subject": "the Signature solar sail cargo concept"}, {"id": "JAH-RPROS-000021", "title": "Signature Beamed-Energy Propulsion Study", "subject": "the Signature beamed-energy propulsion study"}, {"id": "JAH-RPROS-000022", "title": "Signature Cryogenic Boil-Off Management Concept", "subject": "the Signature cryogenic boil-off management concept"}, {"id": "JAH-RPROS-000023", "title": "Signature Propulsion Test Cell Concept", "subject": "the Signature propulsion test cell concept"}, {"id": "JAH-RPROS-000024", "title": "Signature Propulsion Risk Register Concept", "subject": "the Signature propulsion risk register concept"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: rocket-propulsion-signature');
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
