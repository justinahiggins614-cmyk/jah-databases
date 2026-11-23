// Demo for the Category Theory Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Evidence status is stated
// exactly as the sources support it; an open problem is reported
// open. Signature framing is a SIGNATURE DESIGN CLAIM only.
const RECORDS = [{"id": "JAH-CAT-000001", "title": "Category Theory: An Overview", "subject": "category theory overview"}, {"id": "JAH-CAT-000002", "title": "Categories and Morphisms", "subject": "categories and morphisms"}, {"id": "JAH-CAT-000003", "title": "Functors: Maps Between Categories", "subject": "functors between categories"}, {"id": "JAH-CAT-000004", "title": "Natural Transformations", "subject": "natural transformations between functors"}, {"id": "JAH-CAT-000005", "title": "The Yoneda Lemma", "subject": "the Yoneda lemma"}, {"id": "JAH-CAT-000006", "title": "Adjoint Functors", "subject": "adjoint functors"}, {"id": "JAH-CAT-000007", "title": "Limits in Category Theory", "subject": "limits in category theory"}, {"id": "JAH-CAT-000008", "title": "Colimits in Category Theory", "subject": "colimits in category theory"}, {"id": "JAH-CAT-000009", "title": "Monads in Category Theory", "subject": "monads in category theory"}, {"id": "JAH-CAT-000010", "title": "Universal Properties", "subject": "universal properties in category theory"}, {"id": "JAH-CAT-000011", "title": "Cartesian Closed Categories", "subject": "cartesian closed categories"}, {"id": "JAH-CAT-000012", "title": "Topos Theory", "subject": "topos theory"}, {"id": "JAH-CAT-000013", "title": "Abelian Categories", "subject": "abelian categories"}, {"id": "JAH-CAT-000014", "title": "Monoidal Categories", "subject": "monoidal categories"}, {"id": "JAH-CAT-000015", "title": "Enriched Categories", "subject": "enriched categories"}, {"id": "JAH-CAT-000016", "title": "Kan Extensions", "subject": "Kan extensions"}, {"id": "JAH-CAT-000017", "title": "Sheaves in Category Theory", "subject": "sheaves in category theory"}, {"id": "JAH-CAT-000018", "title": "Grothendieck Topologies", "subject": "Grothendieck topologies"}, {"id": "JAH-CAT-000019", "title": "Derived Categories", "subject": "derived categories"}, {"id": "JAH-CAT-000020", "title": "Higher Category Theory", "subject": "higher category theory"}, {"id": "JAH-CAT-000021", "title": "Equivalence of Categories", "subject": "equivalence of categories"}, {"id": "JAH-CAT-000022", "title": "Free Categories", "subject": "free categories"}, {"id": "JAH-CAT-000023", "title": "Exponential Objects", "subject": "exponential objects"}, {"id": "JAH-CAT-000024", "title": "Forgetful Functors", "subject": "forgetful functors"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: category-theory');
  console.log('EDITION: public');
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
