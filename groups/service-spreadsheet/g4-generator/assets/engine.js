/* Pure engine extracted verbatim from the spreadsheet service site (no document access). */

/* Pure formula engine: no document access, testable in Node. */
var COLS=['A','B','C','D','E'], ROWS=6;
function colToNum(c){ return c.charCodeAt(0)-64; }
function numToCol(n){ return String.fromCharCode(64+n); }
function refParts(ref){ var m=/^([A-E])([1-9])$/.exec(ref); return m?{col:colToNum(m[1]),row:+m[2]}:null; }
function expandRange(a,b){
  var pa=refParts(a), pb=refParts(b); if(!pa||!pb) throw new Error('bad range '+a+':'+b);
  var out=[];
  for(var r=Math.min(pa.row,pb.row); r<=Math.max(pa.row,pb.row); r++)
    for(var c=Math.min(pa.col,pb.col); c<=Math.max(pa.col,pb.col); c++) out.push(numToCol(c)+r);
  return out;
}
function tokenize(expr){
  var toks=[], i=0;
  while(i<expr.length){
    var ch=expr[i];
    if(/\s/.test(ch)){ i++; continue; }
    if(/[0-9.]/.test(ch)){ var m=/^[0-9]*\.?[0-9]+/.exec(expr.slice(i)); toks.push({t:'num',v:parseFloat(m[0])}); i+=m[0].length; continue; }
    if(/[A-Za-z]/.test(ch)){ var w=/^[A-Za-z]+/.exec(expr.slice(i))[0]; i+=w.length;
      if(/^[0-9]/.test(expr.slice(i))){ var d=/^[0-9]+/.exec(expr.slice(i))[0]; i+=d.length; toks.push({t:'ref',v:(w+d).toUpperCase()}); }
      else toks.push({t:'name',v:w.toUpperCase()});
      continue; }
    if('+-*/(),:'.indexOf(ch)>=0){ toks.push({t:ch,v:ch}); i++; continue; }
    throw new Error('unexpected character '+ch);
  }
  return toks;
}
function evalFormulaText(formula, values){
  /* values: {A1: raw string}. Returns {value} or {error}. */
  var memo={}, visiting={};
  function resolveRef(ref){
    if(memo.hasOwnProperty(ref)) return memo[ref];
    if(visiting[ref]) throw new Error('circular reference at '+ref);
    var raw=(values[ref]===undefined)?'':String(values[ref]).trim();
    if(raw==='') return {num:false,value:''};
    if(raw.charAt(0)==='='){ visiting[ref]=1; var r=evalExpr(raw.slice(1)); delete visiting[ref]; memo[ref]=r; return r; }
    var n=Number(raw);
    if(raw!=='' && !isNaN(n)) return {num:true,value:n};
    return {num:false,value:raw};
  }
  function evalExpr(expr){
    var toks=tokenize(expr), pos=0;
    function peek(){ return toks[pos]; }
    function next(){ return toks[pos++]; }
    function parseExpr(){ var v=parseTerm(); while(peek()&&(peek().t==='+'||peek().t==='-')){ var op=next().t; var r=parseTerm(); v=op==='+'?v+r:v-r; } return v; }
    function parseTerm(){ var v=parseFactor(); while(peek()&&(peek().t==='*'||peek().t==='/')){ var op=next().t; var r=parseFactor(); v=op==='*'?v*r:v/r; } return v; }
    function numOf(x){ if(typeof x==='object'){ if(!x.num) throw new Error('not a number'); return x.value; } return x; }
    function parseFactor(){
      var tk=peek(); if(!tk) throw new Error('empty formula');
      if(tk.t==='-'){ next(); return -parseFactor(); }
      if(tk.t==='('){ next(); var v=parseExpr(); if(!peek()||peek().t!==')') throw new Error('missing )'); next(); return v; }
      if(tk.t==='num'){ next(); return tk.v; }
      if(tk.t==='ref'){ next(); var cell=resolveRef(tk.v); if(!cell.num) throw new Error(tk.v+' is not a number'); return cell.value; }
      if(tk.t==='name'){
        var fn=next().v;
        if(!peek()||peek().t!=='(') throw new Error(fn+' needs ( )');
        next();
        var args=[];
        if(peek()&&peek().t!==')'){
          while(true){
            if(peek()&&peek().t==='ref'){
              var a=next().v;
              if(peek()&&peek().t===':'){ next(); var b=next(); if(!b||b.t!=='ref') throw new Error('bad range end'); expandRange(a,b.v).forEach(function(r){args.push(r);}); }
              else args.push(a);
            } else args.push(parseExpr());
            if(peek()&&peek().t===','){ next(); continue; }
            break;
          }
        }
        if(!peek()||peek().t!==')') throw new Error('missing ) after '+fn);
        next();
        var nums=args.map(function(a){ if(typeof a==='string'){ var c=resolveRef(a); return c.num?c.value:null; } return (typeof a==='number')?a:null; }).filter(function(x){return x!==null;});
        if(fn==='SUM') return nums.reduce(function(s,x){return s+x;},0);
        if(fn==='AVERAGE') return nums.length?nums.reduce(function(s,x){return s+x;},0)/nums.length:0;
        if(fn==='MAX') return nums.length?Math.max.apply(null,nums):0;
        if(fn==='MIN') return nums.length?Math.min.apply(null,nums):0;
        if(fn==='COUNT') return nums.length;
        throw new Error('unknown function '+fn);
      }
      throw new Error('unexpected token');
    }
    var v=parseExpr();
    if(pos<toks.length) throw new Error('extra text after formula');
    return {num:true,value:v};
  }
  try{
    var f=String(formula||'').trim();
    if(f.charAt(0)==='=') f=f.slice(1);
    return evalExpr(f);
  }catch(e){ return {error:e.message}; }
}
function cellValue(raw, values){
  var s=String(raw===undefined?'':raw).trim();
  if(s==='') return {value:''};
  if(s.charAt(0)==='=') return evalFormulaText(s, values);
  var n=Number(s);
  if(!isNaN(n)) return {num:true,value:n};
  return {num:false,value:s};
}
function computeGrid(values){
  var out={};
  COLS.forEach(function(c){ for(var r=1;r<=ROWS;r++){ var ref=c+r; out[ref]=cellValue(values[ref], values); } });
  return out;
}
function gridToCsv(values){
  var lines=[];
  COLS.forEach(function(c){});
  lines.push(','+COLS.join(','));
  for(var r=1;r<=ROWS;r++){
    var row=[r];
    COLS.forEach(function(c){ var v=String(values[c+r]===undefined?'':values[c+r]); row.push(v.indexOf(',')>=0?'"'+v.replace(/"/g,'""')+'"':v); });
    lines.push(row.join(','));
  }
  return lines.join('\n')+'\n';
}
if(typeof window!=='undefined'){ window.SheetTool={evalFormulaText:evalFormulaText,cellValue:cellValue,computeGrid:computeGrid,expandRange:expandRange,gridToCsv:gridToCsv,COLS:COLS,ROWS:ROWS}; }

if(typeof module!=='undefined'){module.exports={evalFormulaText:evalFormulaText,cellValue:cellValue,computeGrid:computeGrid,gridToCsv:gridToCsv,expandRange:expandRange};}
