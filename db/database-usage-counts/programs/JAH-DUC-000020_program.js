const J=o=>console.log(JSON.stringify(o));const assert=(c,m)=>{if(!c)throw new Error('assert failed: '+m);};
const IN={"record_count": 25, "link_count": 1, "group_size": 2};
function FN_C(IN){const lc=IN.link_count,rc=IN.record_count,gs=IN.group_size;return {usage_score:Math.round(rc*(1+Math.log10(1+lc))+100*gs)};}
const OUT=FN_C(IN);
J(OUT);
assert(OUT.usage_score===233,'score');