
function hashSeed(s){ var h=2166136261; s=String(s); for(var i=0;i<s.length;i++){ h^=s.charCodeAt(i); h=Math.imul(h,16777619); } return h>>>0; }
function rng(seed){ var a=hashSeed(seed); return function(){ a|=0; a=(a+0x6D2B79F5)|0; var t=Math.imul(a^(a>>>15),1|a); t=(t+Math.imul(t^(t>>>7),61|t))^t; return ((t^(t>>>14))>>>0)/4294967296; }; }
function pick(r, arr){ return arr[Math.floor(r()*arr.length)]; }
function num6(r){ return String(100000 + Math.floor(r()*900000)); }

function makeOutputs(seed, n, data){
  if(!(n>=1)) n=1; if(n>5) n=5;
  var out=[];
  for(var k=0;k<n;k++){
    var r=rng(seed+':'+k);
    var depts=Object.keys(data.byDept);
    var dept=pick(r, depts);
    var items=[], pool=data.byDept[dept].slice();
    while(items.length<3 && pool.length){
      var x=pool.splice(Math.floor(r()*pool.length),1)[0];
      items.push(x);
    }
    var id='JAH-STOREGEN-'+num6(r);
    out.push({id:id, dept:dept, items:items,
      text:'Generated storefront '+id+' (simulated): Department '+dept+' — '+items.join('; ')+'. A storefront plan only, made from real product names in the archive.'});
  }
  return out;
}
if (typeof module !== 'undefined' && module.exports) module.exports = { makeOutputs: makeOutputs, hashSeed: hashSeed };
