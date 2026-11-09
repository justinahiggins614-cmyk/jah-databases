const J=o=>console.log(JSON.stringify(o));const assert=(c,m)=>{if(!c)throw new Error('assert failed: '+m);};
const IN={"editions": [{"slug": "19th-century", "rc": 34, "sig": 0}, {"slug": "19th-century-signature", "rc": 34, "sig": 1}]};
function FN_A(IN){const eds=IN.editions.slice().sort((a,b)=>b.rc-a.rc||(b.sig-a.sig)||(a.slug<b.slug?-1:1));return {winner:eds[0].slug,winner_rc:eds[0].rc,losers:eds.slice(1).map(e=>e.slug)};}
const OUT=FN_A(IN);
J(OUT);
assert(OUT.winner==="19th-century-signature",'winner');