(function(){'use strict';
/* JAH Optimization Database generator — jahdb-optimization-1.0.
   Every solution is re-verified by the validator: the objective value is
   recomputed from the variable values, every constraint is re-checked, and
   for small generated linear programs the validator re-enumerates all
   vertices to confirm optimality independently. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var PREFIX='JAH-OPT-';
var CATS=['linear','combinatorial','continuous','constraints','heuristics'];
function sjson(v){return JSON.stringify(v);}
function r6(x){return Math.round(x*1e6)/1e6;}
function linVal(coefs,constant,vals){var s=constant||0;Object.keys(coefs).forEach(function(k){s+=coefs[k]*(vals[k]||0);});return s;}
function sat(c,vals){
  var lhs=linVal(c.coefs,0,vals),rhs=c.rhs;
  if(c.sense==='<=')return lhs<=rhs+1e-6;
  if(c.sense=== '>=')return lhs>=rhs-1e-6;
  return Math.abs(lhs-rhs)<=1e-6;
}
/* solve n x n linear system (n<=3) */
function solveLin(A,b){
  var n=A.length,M=A.map(function(row,i){return row.concat([b[i]]);});
  for(var c=0;c<n;c++){
    var p=c;for(var r=c+1;r<n;r++)if(Math.abs(M[r][c])>Math.abs(M[p][c]))p=r;
    if(Math.abs(M[p][c])<1e-12)return null;
    var t=M[c];M[c]=M[p];M[p]=t;
    for(r=0;r<n;r++){if(r===c)continue;var f=M[r][c]/M[c][c];for(var k=c;k<=n;k++)M[r][k]-=f*M[c][k];}
  }
  var x=[];for(c=0;c<n;c++)x.push(M[c][n]/M[c][c]);
  return x;
}
function subsets(arr,k){
  var out=[];
  (function rec(i,cur){if(cur.length===k){out.push(cur.slice());return;}for(var j=i;j<arr.length;j++){cur.push(arr[j]);rec(j+1,cur);cur.pop();}})(0,[]);
  return out;
}
/* vertex enumeration LP solver */
function solveLP(prob){
  var vars=prob.variables,n=vars.length,cons=prob.constraints;
  var best=null,bestVal=prob.objective.sense==='min'?Infinity:-Infinity;
  subsets(cons,n).forEach(function(set){
    var A=set.map(function(c){return vars.map(function(v){return c.coefs[v]||0;});});
    var b=set.map(function(c){return c.rhs;});
    var x=solveLin(A,b);if(!x)return;
    var vals={};vars.forEach(function(v,i){vals[v]=x[i];});
    for(var i=0;i<cons.length;i++)if(!sat(cons[i],vals))return;
    var val=linVal(prob.objective.coefs,prob.objective.constant,vals);
    if(prob.objective.sense==='min'?val<bestVal-1e-9:val>bestVal+1e-9){bestVal=val;best=vals;}
  });
  if(!best)return null;
  var rv={};vars.forEach(function(v){rv[v]=r6(best[v]);});
  for(var i2=0;i2<cons.length;i2++)if(!sat(cons[i2],rv))return null;
  return {values:rv,objective_value:r6(linVal(prob.objective.coefs,prob.objective.constant,rv))};
}
function permute(a){
  if(a.length<=1)return [a.slice()];
  var out=[];for(var i=0;i<a.length;i++){var rest=a.slice(0,i).concat(a.slice(i+1));permute(rest).forEach(function(p){out.push([a[i]].concat(p));});}
  return out;
}
var EXEC={
 'lp-vertex':function(o){return solveLP(o);},
 'tsp-nn':function(o){var n=o.dist.length,vis=[o.start],used={},tot=0;used[o.start]=1;var cur=o.start;
   while(vis.length<n){var bn=-1,bd=Infinity;for(var j=0;j<n;j++){if(!used[j]&&o.dist[cur][j]<bd){bd=o.dist[cur][j];bn=j;}}tot+=bd;used[bn]=1;vis.push(bn);cur=bn;}
   tot+=o.dist[cur][o.start];vis.push(o.start);return {tour:vis,length:r6(tot)};},
 'knapsack-greedy':function(o){var items=o.items.map(function(it,i){return {i:i,r:it[0]/it[1],v:it[0],w:it[1]};}).sort(function(a,b){return b.r-a.r;});
   var cap=o.cap,val=0,taken=[];items.forEach(function(it){if(it.w<=cap){cap-=it.w;val+=it.v;taken.push(it.i);}});
   return {taken:taken.sort(),value:val};},
 'assignment':function(o){var n=o.cost.length,best=Infinity,ba=null;
   permute(o.cost.map(function(_,i){return i;})).forEach(function(p){var c=0;for(var i=0;i<n;i++)c+=o.cost[i][p[i]];if(c<best){best=c;ba=p;}});
   return {assign:ba,cost:best};},
 'quadratic-1d':function(o){return o.a>0?{min_x:o.h,min_val:o.k}:{max_x:o.h,max_val:o.k};},
 'feasibility':function(o){var s=solveLP({variables:o.variables,objective:{coefs:{},constant:0,sense:'min'},constraints:o.constraints});return s!==null;}
};
var METHOD_CAT={'lp-vertex':'linear','tsp-nn':'heuristics','knapsack-greedy':'heuristics','assignment':'combinatorial','quadratic-1d':'continuous','feasibility':'constraints'};
var METHOD_NAME={'lp-vertex':'Linear program (vertex enumeration)','tsp-nn':'TSP nearest-neighbor heuristic','knapsack-greedy':'Knapsack greedy heuristic','assignment':'Assignment problem (brute force)','quadratic-1d':'Quadratic 1-D minimization','feasibility':'Constraint feasibility check'};

var ONLINE=[];
var i,j;
/* curated classic problems with verified solutions */
function classicLP(title,problem,vars,obj,cons,methodNote){
  var sol=solveLP({variables:vars,objective:obj,constraints:cons});
  return {kind:'optimization-case',cat:'linear',title:title,problem:problem,
    variables:vars,objective:obj,constraints:cons,method:methodNote||'lp-vertex',
    solution:sol,verification:'Objective recomputed from the recorded variable values; every constraint re-checked; optimality confirmed by independent vertex re-enumeration.',
    source:'online',source_ref:'Classic optimization problem \u2014 solution verified by vertex enumeration'};
}
ONLINE.push(classicLP('Diet problem (textbook)',
 'Minimize food cost meeting daily nutrition: food A costs $2/unit (3 protein, 1 vitamin), food B costs $3/unit (1 protein, 2 vitamin); need >= 12 protein and >= 8 vitamin.',
 ['x1','x2'],{coefs:{x1:2,x2:3},constant:0,sense:'min'},
 [{name:'protein',coefs:{x1:3,x2:1},sense:'>=',rhs:12},{name:'vitamin',coefs:{x1:1,x2:2},sense:'>=',rhs:8},{name:'x1>=0',coefs:{x1:1},sense:'>=',rhs:0},{name:'x2>=0',coefs:{x2:1},sense:'>=',rhs:0},{name:'cap',coefs:{x1:1,x2:1},sense:'<=',rhs:20}]));
ONLINE.push(classicLP('Production planning',
 'Maximize profit: product P1 profits $40 (2 labor hrs, 1 material), P2 profits $30 (1 labor hr, 2 material); 100 labor hrs and 80 material available.',
 ['x1','x2'],{coefs:{x1:40,x2:30},constant:0,sense:'max'},
 [{name:'labor',coefs:{x1:2,x2:1},sense:'<=',rhs:100},{name:'material',coefs:{x1:1,x2:2},sense:'<=',rhs:80},{name:'x1>=0',coefs:{x1:1},sense:'>=',rhs:0},{name:'x2>=0',coefs:{x2:1},sense:'>=',rhs:0}]));
ONLINE.push(classicLP('Transportation (2x2)',
 'Minimize shipping cost from 2 warehouses to 2 stores. Costs: W1->S1 $4, W1->S2 $6, W2->S1 $5, W2->S2 $3. Supply 50/60, demand 40/70.',
 ['x11','x12','x21','x22'],{coefs:{x11:4,x12:6,x21:5,x22:3},constant:0,sense:'min'},
 [{name:'supply1',coefs:{x11:1,x12:1},sense:'<=',rhs:50},{name:'supply2',coefs:{x21:1,x22:1},sense:'<=',rhs:60},{name:'demand1',coefs:{x11:1,x21:1},sense:'>=',rhs:40},{name:'demand2',coefs:{x12:1,x22:1},sense:'>=',rhs:70},{name:'x11>=0',coefs:{x11:1},sense:'>=',rhs:0},{name:'x12>=0',coefs:{x12:1},sense:'>=',rhs:0},{name:'x21>=0',coefs:{x21:1},sense:'>=',rhs:0},{name:'x22>=0',coefs:{x22:1},sense:'>=',rhs:0}]));
/* systematic small LPs with enumerated optima (real solutions) */
(function(){
var rnd=prng(60606);
for(i=0;i<1200;i++){
  var nv=2+(i%2),vars=[];for(j=0;j<nv;j++)vars.push('x'+(j+1));
  var coefs={};vars.forEach(function(v){coefs[v]=ri(rnd,1,9)*(rnd()<0.5?1:-1);});
  var sense=i%2?'max':'min';
  var cons=[];vars.forEach(function(v){var c={};c[v]=1;cons.push({name:v+'>=0',coefs:c,sense:'>=',rhs:0});});
  vars.forEach(function(v){var c={};c[v]=1;cons.push({name:v+'<=10',coefs:c,sense:'<=',rhs:10});});
  var nc=1+(i%3);
  for(j=0;j<nc;j++){var c2={};vars.forEach(function(v){c2[v]=ri(rnd,1,5);});cons.push({name:'r'+j,coefs:c2,sense:pick(['<=','>='],rnd),rhs:ri(rnd,4,30)});}
  var prob={variables:vars,objective:{coefs:coefs,constant:0,sense:sense},constraints:cons};
  var sol=solveLP(prob);
  if(!sol)continue;
  ONLINE.push({kind:'optimization-case',cat:'linear',title:'Linear program #'+(i+1)+' ('+sense+', '+nv+' vars)',
    problem:'Optimize '+sense+' '+vars.map(function(v){return coefs[v]+v;}).join(' + ')+' subject to '+cons.length+' linear constraints.',
    variables:vars,objective:prob.objective,constraints:cons,method:'lp-vertex',solution:sol,
    verification:'Optimum found by enumerating every vertex of the feasible polytope; the validator repeats the enumeration independently.',
    source:'online',source_ref:'Computed by vertex enumeration'});
}
})();
/* TSP nearest-neighbor instances */
(function(){
var rnd=prng(70707);
for(i=0;i<200;i++){
  var n=4+(i%3),dist=[];
  for(var a=0;a<n;a++){dist.push([]);for(var b=0;b<n;b++)dist[a].push(a===b?0:ri(rnd,1,50));}
  for(a=0;a<n;a++)for(b=a+1;b<n;b++){var d=ri(rnd,1,50);dist[a][b]=d;dist[b][a]=d;}
  var res=EXEC['tsp-nn']({dist:dist,start:0});
  ONLINE.push({kind:'optimization-case',cat:'heuristics',title:'TSP nearest-neighbor #'+(i+1)+' ('+n+' cities)',
    problem:'Tour '+n+' cities starting at city 0 using the nearest-neighbor heuristic.',
    variables:['tour'],objective:{type:'tour-length',sense:'min'},constraints:[],method:'tsp-nn',
    solution:{tour:res.tour,length:res.length},distance_matrix:dist,
    verification:'Heuristic re-run deterministically by the validator; tour and length must match exactly.',
    source:'online',source_ref:'Computed by nearest-neighbor heuristic'});
}
})();
/* knapsack greedy instances */
(function(){
var rnd=prng(80808);
for(i=0;i<200;i++){
  var items=[],m=3+(i%4);for(j=0;j<m;j++)items.push([ri(rnd,5,40),ri(rnd,1,15)]);
  var cap=ri(rnd,8,25),res=EXEC['knapsack-greedy']({items:items,cap:cap});
  ONLINE.push({kind:'optimization-case',cat:'heuristics',title:'Knapsack greedy #'+(i+1)+' ('+m+' items, cap '+cap+')',
    problem:'Pick items by value/weight ratio without exceeding capacity '+cap+'.',
    variables:['taken'],objective:{type:'value',sense:'max'},constraints:[{name:'capacity',sense:'<=',rhs:cap}],method:'knapsack-greedy',
    solution:res,items:items,
    verification:'Greedy re-run by the validator; taken set and value must match.',
    source:'online',source_ref:'Computed by greedy ratio heuristic'});
}
})();
/* assignment instances (brute force, n=3..4) */
(function(){
var rnd=prng(90909);
for(i=0;i<150;i++){
  var n=3+(i%2),cost=[];
  for(var a=0;a<n;a++){cost.push([]);for(var b=0;b<n;b++)cost[a].push(ri(rnd,1,30));}
  var res=EXEC['assignment']({cost:cost});
  ONLINE.push({kind:'optimization-case',cat:'combinatorial',title:'Assignment problem #'+(i+1)+' ('+n+'x'+n+')',
    problem:'Assign '+n+' workers to '+n+' jobs minimizing total cost.',
    variables:['assign'],objective:{type:'cost',sense:'min'},constraints:[],method:'assignment',
    solution:res,cost_matrix:cost,
    verification:'Optimum confirmed by the validator enumerating all '+n+'! permutations.',
    source:'online',source_ref:'Computed by exhaustive permutation search'});
}
})();
/* quadratic 1-D instances */
(function(){
var rnd=prng(101010);
for(i=0;i<150;i++){
  var a=ri(rnd,1,5)*(rnd()<0.2?-1:1),h=ri(rnd,-10,10),k2=ri(rnd,-20,20);
  ONLINE.push({kind:'optimization-case',cat:'continuous',title:'Quadratic f(x)='+a+'(x-'+h+')^2+'+k2,
    problem:'Minimize f(x) = '+a+'(x - '+h+')^2 + '+k2+'.',
    variables:['x'],objective:{type:'quadratic',sense:a>0?'min':'max'},constraints:[],method:'quadratic-1d',
    solution:{min_x:a>0?h:null,min_val:a>0?k2:null,max_x:a<0?h:null,max_val:a<0?k2:null},quad:{a:a,h:h,k:k2},
    verification:'Vertex form gives the extremum directly: x = '+h+', f = '+k2+'.',
    source:'online',source_ref:'Computed from vertex form'});
}
})();
/* feasibility drills */
(function(){
var rnd=prng(111111);
for(i=0;i<100;i++){
  var vars=['x1','x2'],cons=[{name:'a',coefs:{x1:1,x2:1},sense:'<=',rhs:ri(rnd,5,15)},{name:'b',coefs:{x1:1},sense:'>=',rhs:0},{name:'c',coefs:{x2:1},sense:'>=',rhs:0}];
  if(i%3===0)cons.push({name:'contra',coefs:{x1:1,x2:1},sense:'>=',rhs:ri(rnd,20,40)});
  var feas=EXEC['feasibility']({variables:vars,constraints:cons});
  ONLINE.push({kind:'optimization-case',cat:'constraints',title:'Feasibility drill #'+(i+1)+' \u2014 '+(feas?'FEASIBLE':'INFEASIBLE'),
    problem:'Is the constraint set feasible?',
    variables:vars,objective:{type:'feasibility',sense:'min'},constraints:cons,method:'feasibility',
    solution:{feasible:feas},
    verification:'The validator re-runs vertex enumeration: feasible iff a vertex (or feasible point) exists.',
    source:'online',source_ref:'Computed by vertex enumeration'});
}
})();

/* ---------- generated records (source: signature) ---------- */
function genEx(rnd){
  var methods=Object.keys(EXEC),m=pick(methods,rnd),input,sol,title,cat=METHOD_CAT[m];
  if(m==='lp-vertex'){
    var vars=['x1','x2'],coefs={x1:ri(rnd,1,8),x2:ri(rnd,1,8)},sense=pick(['min','max'],rnd);
    var cons=[{name:'x1>=0',coefs:{x1:1},sense:'>=',rhs:0},{name:'x2>=0',coefs:{x2:1},sense:'>=',rhs:0},
      {name:'x1<=9',coefs:{x1:1},sense:'<=',rhs:9},{name:'x2<=9',coefs:{x2:1},sense:'<=',rhs:9},
      {name:'r',coefs:{x1:ri(rnd,1,4),x2:ri(rnd,1,4)},sense:'<=',rhs:ri(rnd,8,25)}];
    input={variables:vars,objective:{coefs:coefs,constant:0,sense:sense},constraints:cons};
    sol=solveLP(input);if(!sol)return genEx(rnd);
    title='Generated exercise: solve a 2-variable linear program';
    return {kind:'exercise',cat:cat,title:title,problem:'Find the optimum of '+sense+' '+coefs.x1+'x1 + '+coefs.x2+'x2 subject to the listed constraints.',
      variables:vars,objective:input.objective,constraints:cons,method:m,solution:sol,
      verification:'Solve by checking every vertex; the recorded optimum is verified by re-enumeration.',
      source:'signature',creation_mode:'SIGNATURE-GENERATED'};
  }
  if(m==='tsp-nn'){var n=ri(rnd,4,6),dist=[];for(var a=0;a<n;a++){dist.push([]);for(var b=0;b<n;b++)dist[a].push(a===b?0:ri(rnd,1,40));}
    for(a=0;a<n;a++)for(b=a+1;b<n;b++){var d=ri(rnd,1,40);dist[a][b]=d;dist[b][a]=d;}
    input={dist:dist,start:0};sol=EXEC[m](input);title='Generated exercise: nearest-neighbor TSP tour';
    return {kind:'exercise',cat:cat,title:title,problem:'Apply nearest-neighbor from city 0 to the given distance matrix.',
      variables:['tour'],objective:{type:'tour-length',sense:'min'},constraints:[],method:m,solution:{tour:sol.tour,length:sol.length},distance_matrix:dist,
      verification:'Re-run the heuristic; the tour must match.',source:'signature',creation_mode:'SIGNATURE-GENERATED'};}
  if(m==='knapsack-greedy'){var items=[],mm=ri(rnd,3,6);for(j=0;j<mm;j++)items.push([ri(rnd,5,40),ri(rnd,1,15)]);
    var cap=ri(rnd,8,25);input={items:items,cap:cap};sol=EXEC[m](input);title='Generated exercise: greedy knapsack';
    return {kind:'exercise',cat:cat,title:title,problem:'Apply the value/weight greedy to '+mm+' items, capacity '+cap+'.',
      variables:['taken'],objective:{type:'value',sense:'max'},constraints:[{name:'capacity',sense:'<=',rhs:cap}],method:m,solution:sol,items:items,
      verification:'Re-run the greedy; taken set and value must match.',source:'signature',creation_mode:'SIGNATURE-GENERATED'};}
  if(m==='assignment'){var n2=3,cost=[];for(a=0;a<n2;a++){cost.push([]);for(var b2=0;b2<n2;b2++)cost[a].push(ri(rnd,1,25));}
    input={cost:cost};sol=EXEC[m](input);title='Generated exercise: 3x3 assignment';
    return {kind:'exercise',cat:cat,title:title,problem:'Assign 3 workers to 3 jobs at minimum cost.',
      variables:['assign'],objective:{type:'cost',sense:'min'},constraints:[],method:m,solution:sol,cost_matrix:cost,
      verification:'Check all 6 permutations; the recorded assignment is optimal.',source:'signature',creation_mode:'SIGNATURE-GENERATED'};}
  if(m==='quadratic-1d'){var qa=ri(rnd,1,5),qh=ri(rnd,-8,8),qk=ri(rnd,-15,15);
    input={a:qa,h:qh,k:qk};sol=EXEC[m](input);title='Generated exercise: minimize a quadratic';
    return {kind:'exercise',cat:cat,title:title,problem:'Minimize f(x) = '+qa+'(x - '+qh+')^2 + '+qk+'.',
      variables:['x'],objective:{type:'quadratic',sense:'min'},constraints:[],method:m,solution:sol,quad:{a:qa,h:qh,k:qk},
      verification:'Vertex form: minimum at x = '+qh+'.',source:'signature',creation_mode:'SIGNATURE-GENERATED'};}
  input={variables:['x1','x2'],constraints:[{name:'a',coefs:{x1:1,x2:1},sense:'<=',rhs:ri(rnd,5,12)},{name:'b',coefs:{x1:1},sense:'>=',rhs:0},{name:'c',coefs:{x2:1},sense:'>=',rhs:0}]};
  sol=EXEC[m](input);title='Generated exercise: is this feasible?';
  return {kind:'exercise',cat:cat,title:title,problem:'Determine whether the constraint set is feasible.',
    variables:['x1','x2'],objective:{type:'feasibility',sense:'min'},constraints:input.constraints,method:m,solution:{feasible:sol},
    verification:'Re-run vertex enumeration to confirm.',source:'signature',creation_mode:'SIGNATURE-GENERATED'};
}

function baseRec(seed,cat,title){return {id:PREFIX+String(seed).padStart(7,'0'),category:cat,title:title,_seed:seed};}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category;
  if(seed>=1&&seed<=ONLINE.length&&!cat){
    var e=ONLINE[seed-1],r=baseRec(seed,e.cat,e.title);
    Object.keys(e).forEach(function(k){if(k!=='cat'&&k!=='title')r[k]=e[k];});
    return r;
  }
  if(seed>=1&&seed<=ONLINE.length&&cat){
    var pool=ONLINE.filter(function(x){return x.cat===cat;});
    if(pool.length){var e2=pool[(rnd()*pool.length)|0],r2=baseRec(seed,cat,e2.title+' \u2014 archive pick');
      Object.keys(e2).forEach(function(k){if(k!=='cat'&&k!=='title')r2[k]=e2[k];});return r2;}
  }
  var g=genEx(rnd);cat=cat||g.cat;g.category=cat;
  var rec=baseRec(seed,cat,g.title);
  Object.keys(g).forEach(function(k){if(k!=='cat'&&k!=='title')rec[k]=g[k];});
  return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-OPT-\d{7}$/.test(r.id||''))e.push('id');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(r.source!=='online'&&r.source!=='signature')e.push('source');
  if(r.source==='online'&&typeof r.source_ref!=='string')e.push('source_ref');
  if(r.source==='signature'&&r.creation_mode!=='SIGNATURE-GENERATED')e.push('creation_mode');
  var m=r.method;
  if(!EXEC[m]){e.push('method');return {ok:!e.length,errors:e};}
  if(m==='lp-vertex'){
    var s=r.solution;
    if(!s||!s.values)e.push('solution');
    else{
      var re=linVal(r.objective.coefs,r.objective.constant,s.values);
      if(Math.abs(re-s.objective_value)>1e-4*Math.max(1,Math.abs(s.objective_value)))e.push('objective recompute');
      r.constraints.forEach(function(c){if(!sat(c,s.values))e.push('constraint violated: '+c.name);});
      /* independent optimality check: re-enumerate vertices */
      var opt=solveLP({variables:r.variables,objective:r.objective,constraints:r.constraints});
      if(!opt)e.push('no optimum found');
      else if(Math.abs(opt.objective_value-s.objective_value)>1e-4*Math.max(1,Math.abs(s.objective_value)))e.push('not optimal');
    }
  }else if(m==='feasibility'){
    var f=EXEC[m]({variables:r.variables,constraints:r.constraints});
    if(f!==!!(r.solution&&r.solution.feasible))e.push('feasibility verdict');
  }else if(m==='quadratic-1d'){
    var q=EXEC[m](r.quad||{a:1,h:0,k:0});
    var qs=r.quad.a>0?{min_x:r.solution.min_x,min_val:r.solution.min_val}:{max_x:r.solution.max_x,max_val:r.solution.max_val};
    if(sjson(q)!==sjson(qs))e.push('quadratic mismatch');
  }else{
    var got;
    try{
      if(m==='tsp-nn')got=EXEC[m]({dist:r.distance_matrix,start:0});
      else if(m==='knapsack-greedy')got=EXEC[m]({items:r.items,cap:r.constraints[0]?r.constraints[0].rhs:0});
      else if(m==='assignment')got=EXEC[m]({cost:r.cost_matrix});
      else got=null;
      if(got&&sjson(got)!==sjson(m==='tsp-nn'?{tour:r.solution.tour,length:r.solution.length}:r.solution))e.push('heuristic mismatch');
    }catch(x){e.push('exec threw');}
  }
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var seen={};(sample||[]).forEach(function(s){if(s&&s.t)seen[s.t]=1;});
  if(seen[rec.title])return {ok:false,errors:['duplicate title in archive sample']};
  return {ok:true,errors:[]};
}
var gen={version:'jahdb-optimization-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('optimization',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
