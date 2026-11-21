/* Calculator generator engine: safe expression sums + linear solver +
   seeded equation generator in the archive's own format. Browser + Node. */
(function(g){
'use strict';
function hashStr(s){var h=2166136261;for(var i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619);}return h>>>0;}
function rng(seed){var a=hashStr(String(seed));return function(){a|=0;a=a+0x6D2B79F5|0;var t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function evalExpr(src){
  src=String(src==null?'':src).trim();
  if(!src) return {error:'Enter a sum.'};
  if(!/^[0-9+\-*/().\s]+$/.test(src)) return {error:'Only digits and + - * / ( ) . are allowed.'};
  var i=0;
  function peek(){return src[i];}
  function num(){var s='';while(i<src.length&&/[0-9.]/.test(src[i])){s+=src[i++];}if(s===''||s.split('.').length>2) throw new Error('bad number');return parseFloat(s);}
  function factor(){while(src[i]===' ')i++;if(src[i]==='('){i++;var v=expr();while(src[i]===' ')i++;if(src[i]!==')')throw new Error('missing )');i++;return v;}if(src[i]==='-'){i++;return -factor();}return num();}
  function term(){var v=factor();for(;;){while(src[i]===' ')i++;if(src[i]==='*'){i++;v*=factor();}else if(src[i]==='/'){i++;var d=factor();if(d===0)throw new Error('divide by zero');v/=d;}else return v;}}
  function expr(){var v=term();for(;;){while(src[i]===' ')i++;if(src[i]==='+'){i++;v+=term();}else if(src[i]==='-'){i++;v-=term();}else return v;}}
  try{var v=expr();while(src[i]===' ')i++;if(i<src.length) return {error:'Could not read the whole sum.'};if(!isFinite(v)) return {error:'The answer is not a finite number.'};return {value:v};}
  catch(e){return {error:e.message==='divide by zero'?'Cannot divide by zero.':'Could not read that sum.'};}
}
function solveLinear(a,b){
  if(typeof a!=='number'||typeof b!=='number'||!isFinite(a)||!isFinite(b)) return {error:'Enter numbers.'};
  if(a===0) return {error:'The x term must not be 0.'};
  var x=-b/a;
  return {value:x,steps:[''+a+'x + '+b+' = 0',''+a+'x = '+(-b),'x = '+(-b)+' / '+a+' = '+x],check:'Put x = '+x+' back in: '+(a*x+b)+' = 0'};
}
function makeEquation(seed){
  var r=rng(seed);
  var a=2+Math.floor(r()*8);var x=-(5+Math.floor(r()*10))+Math.floor(r()*11);
  if(x===0)x=3;
  var b=-(a*x);
  var eq=a+'x + '+b+' = 0';
  return {seed:String(seed),generated:true,type:'linear',title:'Solve '+a+'x + '+b+' = 0',
    equation:eq,steps:[eq,''+a+'x = '+(-b),'x = '+(-b)+' / '+a+' = '+x],
    solution:'x = '+x,check:'Put x = '+x+' back in: '+(a*x+b)+' = 0'};
}
var API={evalExpr:evalExpr,solveLinear:solveLinear,makeEquation:makeEquation,hashStr:hashStr};
if(typeof module!=='undefined'){module.exports=API;}
if(typeof window!=='undefined'){window.SigEngine=API;}
if(typeof globalThis!=='undefined'){globalThis.SigEngine=API;}
})(typeof globalThis!=='undefined'?globalThis:this);
