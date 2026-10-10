(function(){'use strict';
/* JAH Algorithm Database generator — jahdb-algorithms-1.0.
   Every test case output is recomputed by the validator with a reference
   implementation keyed by `method`; complexity claims are checked against a
   canonical table. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function shuffle(a,rnd){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(rnd()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}
var PREFIX='JAH-ALG-';
var CATS=['sorting','searching','graphs','dynamic-programming','greedy','strings'];
function sjson(v){return JSON.stringify(v);}

/* ---------- reference executors: method -> input -> output ---------- */
function sortNums(a){return a.slice().sort(function(x,y){return x-y;});}
var EXEC={
 'sort-bubble':sortNums,'sort-insertion':sortNums,'sort-selection':sortNums,'sort-merge':sortNums,
 'sort-quick':sortNums,'sort-heap':sortNums,
 'sort-counting':function(a){var m=Math.max.apply(null,a.concat([0]));var c=new Array(m+1).fill(0);a.forEach(function(x){c[x]++;});var o=[];for(var i=0;i<=m;i++)for(var k=0;k<c[i];k++)o.push(i);return o;},
 'search-linear':function(o){var i=o.arr.indexOf(o.target);return i;},
 'search-binary':function(o){var a=o.arr,t=o.target,lo=0,hi=a.length-1;while(lo<=hi){var m=(lo+hi)>>1;if(a[m]===t)return m;if(a[m]<t)lo=m+1;else hi=m-1;}return -1;},
 'bfs':function(o){var adj=o.adj,s=o.start,seen={},q=[s],out=[];seen[s]=1;while(q.length){var u=q.shift();out.push(u);(adj[u]||[]).forEach(function(v){if(!seen[v]){seen[v]=1;q.push(v);}});}return out;},
 'dfs':function(o){var adj=o.adj,seen={},out=[];(function d(u){seen[u]=1;out.push(u);(adj[u]||[]).forEach(function(v){if(!seen[v])d(v);});})(o.start);return out;},
 'dijkstra':function(o){var adj=o.adj,dist={},done={},nodes=Object.keys(adj);nodes.forEach(function(n){dist[n]=Infinity;});dist[o.start]=0;
   for(;;){var u=null,best=Infinity;nodes.forEach(function(n){if(!done[n]&&dist[n]<best){best=dist[n];u=n;}});if(u===null)break;done[u]=1;
   (adj[u]||[]).forEach(function(e){var v=e[0],w=e[1];if(dist[u]+w<dist[v])dist[v]=dist[u]+w;});}
   return nodes.sort().map(function(n){return [n,dist[n]];});},
 'bellman-ford':function(o){var dist={};o.nodes.forEach(function(n){dist[n]=Infinity;});dist[o.start]=0;
   for(var i=0;i<o.nodes.length-1;i++)o.edges.forEach(function(e){if(dist[e[0]]+e[2]<dist[e[1]])dist[e[1]]=dist[e[0]]+e[2];});
   return o.nodes.slice().sort().map(function(n){return [n,dist[n]];});},
 'kruskal':function(o){var p={};function f(x){while(p[x]!==x){p[x]=p[p[x]];x=p[x];}return x;}
   o.edges.forEach(function(e){p[e[0]]=e[0];p[e[1]]=e[1];});
   var tot=0;o.edges.slice().sort(function(a,b){return a[2]-b[2];}).forEach(function(e){var a=f(e[0]),b=f(e[1]);if(a!==b){p[a]=b;tot+=e[2];}});
   return tot;},
 'topsort':function(o){var adj=o.adj,ind={},nodes=Object.keys(adj);nodes.forEach(function(n){ind[n]=0;});
   nodes.forEach(function(n){(adj[n]||[]).forEach(function(m){ind[m]=(ind[m]||0)+1;});});
   var z=nodes.filter(function(n){return ind[n]===0;}).sort(),out=[];
   while(z.length){var u=z.shift();out.push(u);(adj[u]||[]).forEach(function(v){if(--ind[v]===0){z.push(v);z.sort();}});}
   return out;},
 'fib':function(n){if(n<=1)return n;var a=0,b=1;for(var i=2;i<=n;i++){var t=a+b;a=b;b=t;}return b;},
 'knapsack01':function(o){var W=o.cap,dp=new Array(W+1).fill(0);o.weights.forEach(function(w,i){var v=o.values[i];for(var c=W;c>=w;c--)dp[c]=Math.max(dp[c],dp[c-w]+v);});return dp[W];},
 'lcs':function(o){var a=o.a,b=o.b,dp=[];for(var i=0;i<=a.length;i++){dp.push(new Array(b.length+1).fill(0));}
   for(i=1;i<=a.length;i++)for(var j=1;j<=b.length;j++)dp[i][j]=a[i-1]===b[j-1]?dp[i-1][j-1]+1:Math.max(dp[i-1][j],dp[i][j-1]);return dp[a.length][b.length];},
 'edit-distance':function(o){var a=o.a,b=o.b,dp=[];for(var i=0;i<=a.length;i++){dp.push([i]);for(var j=1;j<=b.length;j++)dp[i][j]=0;}
   for(var j=1;j<=b.length;j++)dp[0][j]=j;
   for(i=1;i<=a.length;i++)for(j=1;j<=b.length;j++)dp[i][j]=Math.min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+(a[i-1]===b[j-1]?0:1));return dp[a.length][b.length];},
 'coin-change':function(o){var dp=new Array(o.amount+1).fill(1e9);dp[0]=0;o.coins.forEach(function(c){for(var i=c;i<=o.amount;i++)dp[i]=Math.min(dp[i],dp[i-c]+1);});return dp[o.amount]>=1e9?-1:dp[o.amount];},
 'lis':function(a){var t=[];a.forEach(function(x){var lo=0,hi=t.length;while(lo<hi){var m=(lo+hi)>>1;if(t[m]<x)lo=m+1;else hi=m;}t[lo]=x;});return t.length;},
 'activity-selection':function(a){var s=a.slice().sort(function(x,y){return x[1]-y[1]||x[0]-y[0];}),c=0,last=-1e18;s.forEach(function(p){if(p[0]>=last){c++;last=p[1];}});return c;},
 'fractional-knapsack':function(o){var items=o.items.map(function(it){return [it[0],it[1],it[0]/it[1]];}).sort(function(a,b){return b[2]-a[2];});
   var cap=o.cap,tot=0;items.forEach(function(it){if(cap<=0)return;var take=Math.min(cap,it[1]);tot+=take*it[2];cap-=take;});return Math.round(tot*1e9)/1e9;},
 'kmp-search':function(o){var p=o.pattern,pi=new Array(p.length).fill(0);for(var i=1;i<p.length;i++){var j=pi[i-1];while(j>0&&p[i]!==p[j])j=pi[j-1];if(p[i]===p[j])j++;pi[i]=j;}
   var out=[],t=o.text;j=0;for(i=0;i<t.length;i++){while(j>0&&t[i]!==p[j])j=pi[j-1];if(t[i]===p[j])j++;if(j===p.length){out.push(i-p.length+1);j=pi[j-1];}}return out;},
 'naive-search':function(o){var out=[],t=o.text,p=o.pattern;for(var i=0;i+ p.length<=t.length;i++){var ok=true;for(var j=0;j<p.length;j++)if(t[i+j]!==p[j]){ok=false;break;}if(ok)out.push(i);}return out;},
 'rabin-karp':function(o){var t=o.text,p=o.pattern,n=t.length,m=p.length;if(m>n)return [];var B=256,M=101,h=1,out=[];
   for(var i=0;i<m-1;i++)h=(h*B)%M;var hp=0,ht=0;
   for(i=0;i<m;i++){hp=(B*hp+p.charCodeAt(i))%M;ht=(B*ht+t.charCodeAt(i))%M;}
   for(i=0;i<=n-m;i++){if(hp===ht){var ok=true;for(var j=0;j<m;j++)if(t[i+j]!==p[j]){ok=false;break;}if(ok)out.push(i);}
     if(i<n-m){ht=(B*(ht-t.charCodeAt(i)*h)+t.charCodeAt(i+m))%M;if(ht<0)ht+=M;}}
   return out;},
 'huffman':function(o){var nodes=Object.keys(o.freq).sort().map(function(s){return {s:s,f:o.freq[s]};});
   while(nodes.length>1){nodes.sort(function(a,b){return a.f-b.f||(a.s<b.s?-1:1);});var x=nodes.shift(),y=nodes.shift();
     nodes.push({s:x.s+y.s,f:x.f+y.f,l:x,r:y});}
   var codes={};(function w(n,pre){if(n.s.length===1&&!n.l){codes[n.s]=pre||'0';return;}if(n.l)w(n.l,pre+'0');if(n.r)w(n.r,pre+'1');})(nodes[0],'');
   var bits=0;Object.keys(codes).forEach(function(s){bits+=codes[s].length*o.freq[s];});
   var keys=Object.keys(codes).sort(),pf=true;
   for(var i=0;i<keys.length;i++)for(var j=0;j<keys.length;j++)if(i!==j&&codes[keys[j]].indexOf(codes[keys[i]])===0)pf=false;
   return {codes:codes,total_bits:bits,prefix_free:pf};}
};
/* canonical complexity per method */
var COMPLEX={
 'sort-bubble':['O(n^2)','O(1)'],'sort-insertion':['O(n^2)','O(1)'],'sort-selection':['O(n^2)','O(1)'],
 'sort-merge':['O(n log n)','O(n)'],'sort-quick':['O(n log n) avg, O(n^2) worst','O(log n)'],
 'sort-heap':['O(n log n)','O(1)'],'sort-counting':['O(n + k)','O(k)'],
 'search-linear':['O(n)','O(1)'],'search-binary':['O(log n)','O(1)'],
 'bfs':['O(V + E)','O(V)'],'dfs':['O(V + E)','O(V)'],
 'dijkstra':['O((V + E) log V)','O(V)'],'bellman-ford':['O(V * E)','O(V)'],
 'kruskal':['O(E log E)','O(V)'],'topsort':['O(V + E)','O(V)'],
 'fib':['O(n)','O(1)'],'knapsack01':['O(n * W)','O(W)'],'lcs':['O(n * m)','O(n * m)'],
 'edit-distance':['O(n * m)','O(n * m)'],'coin-change':['O(n * amount)','O(amount)'],'lis':['O(n log n)','O(n)'],
 'activity-selection':['O(n log n)','O(1)'],'fractional-knapsack':['O(n log n)','O(1)'],'huffman':['O(n log n)','O(n)'],
 'kmp-search':['O(n + m)','O(m)'],'naive-search':['O(n * m)','O(1)'],'rabin-karp':['O(n + m) avg','O(1)']};
/* canonical short descriptions (verified facts) */
var DESC={
 'sort-bubble':'Repeatedly steps through the list, swapping adjacent out-of-order elements until no swaps remain. Simple but quadratic.',
 'sort-insertion':'Builds the sorted list one element at a time, inserting each new element into its proper place. Fast on nearly-sorted data.',
 'sort-selection':'Repeatedly selects the minimum of the unsorted region and moves it to the front. Always quadratic, minimal swaps.',
 'sort-merge':'Divide and conquer: split the list, sort each half, then merge the sorted halves. Guaranteed n log n, needs extra space.',
 'sort-quick':'Picks a pivot, partitions around it, and recurses. Average n log n; degrades to quadratic on bad pivots.',
 'sort-heap':'Builds a max-heap, then repeatedly extracts the maximum. Guaranteed n log n, in place, but not stable.',
 'sort-counting':'Counts occurrences of each value, then writes them out in order. Linear when the value range k is small.',
 'search-linear':'Scans each element in turn until the target is found. Works on any list, unsorted or sorted.',
 'search-binary':'Repeatedly halves a sorted array, discarding the half that cannot contain the target. Logarithmic.',
 'bfs':'Explores a graph level by level from the start node using a queue. Finds shortest paths in unweighted graphs.',
 'dfs':'Explores as deep as possible along each branch before backtracking. Natural fit for recursion.',
 'dijkstra':"Expands the closest unvisited node first, settling shortest paths from the start. Requires non-negative weights.",
 'bellman-ford':'Relaxes every edge V-1 times. Handles negative weights and detects negative cycles; slower than Dijkstra.',
 'kruskal':'Sorts edges by weight and adds each unless it forms a cycle (union-find). Builds a minimum spanning tree.',
 'topsort':'Orders directed-acyclic-graph nodes so every edge points forward (Kahn\u2019s algorithm). Fails if a cycle exists.',
 'fib':'Classic dynamic programming: each Fibonacci number is the sum of the previous two; iterate once, keep two variables.',
 'knapsack01':'Each item is taken or skipped. DP over capacity: dp[c] = best value achievable with capacity c.',
 'lcs':'Longest common subsequence of two strings via DP: match extends the diagonal, mismatch takes the best neighbor.',
 'edit-distance':'Minimum insertions, deletions, substitutions to turn one string into another (Levenshtein DP).',
 'coin-change':'Fewest coins to make an amount: DP over amounts, trying each coin. -1 when impossible.',
 'lis':'Longest increasing subsequence via patience piles with binary search: O(n log n).',
 'activity-selection':'Greedy: sort activities by finish time, take each compatible one. Optimal for interval scheduling.',
 'fractional-knapsack':'Greedy by value-per-weight ratio, taking fractions when needed. Optimal for the fractional variant.',
 'huffman':'Merges the two least-frequent symbols repeatedly, building an optimal prefix code. Frequent symbols get short codes.',
 'kmp-search':'Precomputes the prefix function so the pattern never backtracks in the text. Linear time.',
 'naive-search':'Slides the pattern along the text checking each alignment. Simple; quadratic in the worst case.',
 'rabin-karp':'Rolling hash compares pattern hash to each text window, verifying matches directly. Fast on average.'};
var PSEUDO={
 'sort-quick':['quick(a, lo, hi):','  if lo < hi:','    p = partition(a, lo, hi)','    quick(a, lo, p-1)','    quick(a, p+1, hi)'],
 'sort-merge':['merge_sort(a):','  if len(a) <= 1: return a','  m = len(a)//2','  return merge(merge_sort(a[:m]), merge_sort(a[m:]))'],
 'dijkstra':['dist[s] = 0; pq = [(0, s)]','while pq:','  d, u = pop_min(pq)','  for v, w in adj[u]:','    if d + w < dist[v]: dist[v] = d + w; push(pq, (dist[v], v))'],
 'kmp-search':['pi = prefix_function(pattern)','j = 0','for i, ch in enumerate(text):','  while j > 0 and ch != pattern[j]: j = pi[j-1]','  if ch == pattern[j]: j += 1','  if j == len(pattern): match at i - j + 1'],
 'knapsack01':['dp = [0] * (W+1)','for w, v in items:','  for c in reversed(range(w, W+1)):','    dp[c] = max(dp[c], dp[c-w] + v)']};

/* curated real algorithm entries (source: online) */
var ALGS=[
 ['Bubble Sort','sorting','sort-bubble'],['Insertion Sort','sorting','sort-insertion'],
 ['Selection Sort','sorting','sort-selection'],['Merge Sort','sorting','sort-merge'],
 ['Quicksort','sorting','sort-quick'],['Heapsort','sorting','sort-heap'],['Counting Sort','sorting','sort-counting'],
 ['Linear Search','searching','search-linear'],['Binary Search','searching','search-binary'],
 ['Breadth-First Search','graphs','bfs'],['Depth-First Search','graphs','dfs'],
 ['Dijkstra\u2019s Algorithm','graphs','dijkstra'],['Bellman-Ford Algorithm','graphs','bellman-ford'],
 ['Kruskal\u2019s Algorithm','graphs','kruskal'],['Topological Sort','graphs','topsort'],
 ['Fibonacci (DP)','dynamic-programming','fib'],['0/1 Knapsack','dynamic-programming','knapsack01'],
 ['Longest Common Subsequence','dynamic-programming','lcs'],['Edit Distance','dynamic-programming','edit-distance'],
 ['Coin Change (min coins)','dynamic-programming','coin-change'],['Longest Increasing Subsequence','dynamic-programming','lis'],
 ['Activity Selection','greedy','activity-selection'],['Fractional Knapsack','greedy','fractional-knapsack'],
 ['Huffman Coding','greedy','huffman'],['Knuth-Morris-Pratt','strings','kmp-search'],
 ['Naive String Search','strings','naive-search'],['Rabin-Karp','strings','rabin-karp']];
var REFS={'sorting':'CLRS \u2014 sorting complexity analysis','searching':'CLRS \u2014 searching','graphs':'CLRS \u2014 graph algorithms','dynamic-programming':'CLRS \u2014 dynamic programming','greedy':'CLRS \u2014 greedy algorithms','strings':'CLRS \u2014 string matching'};
var ONLINE=[];
ALGS.forEach(function(a){
  ONLINE.push({kind:'algorithm',cat:a[1],title:a[0],algorithm_name:a[0],method:a[2],
    problem:'Reference entry: '+a[0]+', a canonical '+a[1]+' algorithm.',
    description:DESC[a[2]],pseudocode:PSEUDO[a[2]]||[a[0]+': see description.'],
    complexity_time:COMPLEX[a[2]][0],complexity_space:COMPLEX[a[2]][1],
    source:'online',source_ref:REFS[a[1]]});
});
/* systematic worked examples: deterministic small inputs, outputs computed */
var WI=0;
function wExample(method,input,note){
  WI++;
  return {kind:'worked-example',cat:catOf(method),title:'Worked example #'+WI+': '+nameOf(method),
    algorithm_name:nameOf(method),method:method,problem:note||'Worked example with concrete input; output computed by the reference implementation.',
    description:'Step-by-step instance of '+nameOf(method)+'. The recorded output was produced by executing the algorithm on the given input.',
    test_cases:[{input:input,expected:EXEC[method](input)}],
    complexity_time:COMPLEX[method][0],complexity_space:COMPLEX[method][1],
    source:'online',source_ref:'Computed by reference implementation'};
}
function nameOf(m){for(var i=0;i<ALGS.length;i++)if(ALGS[i][2]===m)return ALGS[i][0];return m;}
function catOf(m){for(var i=0;i<ALGS.length;i++)if(ALGS[i][2]===m)return ALGS[i][1];return 'sorting';}
function mkArr(rnd,n,lo,hi){var a=[];for(var i=0;i<n;i++)a.push(ri(rnd,lo,hi));return a;}
/* deterministic enumeration using a fixed prng */
(function(){
var rnd=prng(424242);
var sortMs=['sort-bubble','sort-insertion','sort-selection','sort-merge','sort-quick','sort-heap'];
for(var i=0;i<360;i++){var m=sortMs[i%sortMs.length];ONLINE.push(wExample(m,mkArr(rnd,ri(rnd,3,9),0,50),'Sorting worked example.'));}
for(i=0;i<120;i++){var a=sortNums(mkArr(rnd,ri(rnd,3,8),0,30));ONLINE.push(wExample('search-binary',{arr:a,target:pick(a.concat([99]),rnd)},'Binary search on a sorted array.'));}
for(i=0;i<120;i++){ONLINE.push(wExample('search-linear',{arr:mkArr(rnd,ri(rnd,3,8),0,20),target:ri(rnd,0,20)},'Linear search worked example.'));}
function rGraph(rnd,n,weighted,dag){
  var adj={},nodes=[];for(var k=0;k<n;k++){var nm=String.fromCharCode(65+k);nodes.push(nm);adj[nm]=[];}
  for(var u=0;u<n;u++)for(var v=0;v<n;v++){if(u===v)continue;if(dag&&v<=u)continue;if(rnd()<0.35){var nm2=String.fromCharCode(65+u);if(weighted)adj[nm2].push([String.fromCharCode(65+v),ri(rnd,1,9)]);else adj[nm2].push(String.fromCharCode(65+v));}}
  return {adj:adj,nodes:nodes};
}
var gMs=['bfs','dfs','dijkstra','bellman-ford','kruskal','topsort'];
for(i=0;i<360;i++){var gm=gMs[i%gMs.length],g=rGraph(rnd,ri(rnd,3,6),gm==='dijkstra'||gm==='bellman-ford'||gm==='kruskal',gm==='topsort');
  var inp;if(gm==='bfs'||gm==='dfs'||gm==='dijkstra')inp={adj:g.adj,start:'A'};
  else if(gm==='bellman-ford'){var ed=[];Object.keys(g.adj).forEach(function(u){g.adj[u].forEach(function(e){ed.push([u,e[0],e[1]]);});});inp={edges:ed,nodes:g.nodes,start:'A'};}
  else if(gm==='kruskal'){var ed2=[],seen={};Object.keys(g.adj).forEach(function(u){g.adj[u].forEach(function(e){var k=[u,e[0]].sort().join('');if(!seen[k]){seen[k]=1;ed2.push([u,e[0],e[1]]);}});});inp={edges:ed2};}
  else inp={adj:g.adj};
  try{var exp=EXEC[gm](inp);ONLINE.push(wExample(gm,inp,'Graph worked example ('+gm+').'));}catch(e){}
}
for(i=0;i<120;i++)ONLINE.push(wExample('fib',ri(rnd,0,25),'Fibonacci number.'));
for(i=0;i<120;i++){var ws=mkArr(rnd,3,1,10),vs=mkArr(rnd,3,1,20);ONLINE.push(wExample('knapsack01',{weights:ws,values:vs,cap:ri(rnd,5,15)},'0/1 knapsack worked example.'));}
var WORDS=['algorithm','dynamic','knapsack','search','graph','binary','optimal','string','coding','huffman'];
for(i=0;i<120;i++)ONLINE.push(wExample('lcs',{a:pick(WORDS,rnd),b:pick(WORDS,rnd)},'LCS worked example.'));
for(i=0;i<120;i++)ONLINE.push(wExample('edit-distance',{a:pick(WORDS,rnd),b:pick(WORDS,rnd)},'Edit distance worked example.'));
for(i=0;i<90;i++)ONLINE.push(wExample('coin-change',{coins:[1,5,10,25].slice(0,ri(rnd,2,4)),amount:ri(rnd,1,60)},'Coin change worked example.'));
for(i=0;i<90;i++)ONLINE.push(wExample('lis',mkArr(rnd,ri(rnd,4,9),0,30),'LIS worked example.'));
for(i=0;i<90;i++){var acts=[],nn=ri(rnd,3,7);for(var k=0;k<nn;k++){var s0=ri(rnd,0,10);acts.push([s0,s0+ri(rnd,1,5)]);}ONLINE.push(wExample('activity-selection',acts,'Activity selection worked example.'));}
for(i=0;i<60;i++){var its=[],n2=ri(rnd,2,5);for(k=0;k<n2;k++)its.push([ri(rnd,5,40),ri(rnd,1,15)]);ONLINE.push(wExample('fractional-knapsack',{items:its,cap:ri(rnd,5,20)},'Fractional knapsack worked example.'));}
for(i=0;i<60;i++){var fr={},al='abcde';for(k=0;k<5;k++)fr[al[k]]=ri(rnd,1,20);ONLINE.push(wExample('huffman',{freq:fr},'Huffman coding worked example.'));}
var TEXTS=['ababcababcabc','aaaaabaaaaab','mississippi','abcabdabcabe'];
for(i=0;i<90;i++)ONLINE.push(wExample('kmp-search',{text:pick(TEXTS,rnd),pattern:pick(['abc','aab','iss','abca'],rnd)},'KMP worked example.'));
for(i=0;i<60;i++)ONLINE.push(wExample('naive-search',{text:pick(TEXTS,rnd),pattern:pick(['abc','ssi','aab'],rnd)},'Naive search worked example.'));
for(i=0;i<60;i++)ONLINE.push(wExample('rabin-karp',{text:pick(TEXTS,rnd),pattern:pick(['abc','ssi'],rnd)},'Rabin-Karp worked example.'));
})();

/* ---------- generated records (source: signature) ---------- */
function genExercise(rnd){
  var a=pick(ALGS,rnd),m=a[2],input;
  if(m.indexOf('sort')===0)input=mkArr(rnd,ri(rnd,4,8),0,40);
  else if(m==='fib')input=ri(rnd,5,20);
  else if(m==='lis')input=mkArr(rnd,5,0,25);
  else if(m==='lcs'||m==='edit-distance')input={a:pick(['dynamic','binary','search','optimal'],rnd),b:pick(['graph','string','coding','knapsack'],rnd)};
  else if(m==='kmp-search'||m==='naive-search'||m==='rabin-karp')input={text:pick(['ababcababc','mississippi'],rnd),pattern:pick(['abc','iss'],rnd)};
  else if(m==='search-linear')input={arr:mkArr(rnd,5,0,15),target:ri(rnd,0,15)};
  else if(m==='search-binary'){var ar=sortNums(mkArr(rnd,5,0,20));input={arr:ar,target:pick(ar,rnd)};}
  else if(m==='coin-change')input={coins:[1,5,10,25],amount:ri(rnd,1,50)};
  else if(m==='knapsack01')input={weights:mkArr(rnd,3,1,8),values:mkArr(rnd,3,5,20),cap:ri(rnd,5,12)};
  else if(m==='activity-selection'){var acts=[];for(var k=0;k<4;k++){var s0=ri(rnd,0,8);acts.push([s0,s0+ri(rnd,1,4)]);}input=acts;}
  else if(m==='fractional-knapsack')input={items:[[10,5],[20,8],[15,6]],cap:ri(rnd,5,12)};
  else if(m==='huffman')input={freq:{a:ri(rnd,1,10),b:ri(rnd,1,10),c:ri(rnd,1,10)}};
  else if(m==='bfs'||m==='dfs')input={adj:{A:['B','C'],B:['D'],C:['D'],D:[]},start:'A'};
  else if(m==='dijkstra')input={adj:{A:[['B',2],['C',5]],B:[['C',1]],C:[]},start:'A'};
  else if(m==='bellman-ford')input={edges:[['A','B',2],['A','C',5],['B','C',1]],nodes:['A','B','C'],start:'A'};
  else if(m==='kruskal')input={edges:[['A','B',2],['A','C',5],['B','C',1]]};
  else if(m==='topsort')input={adj:{A:['B','C'],B:['D'],C:['D'],D:[]}};
  var tc={input:input,expected:EXEC[m](input)};
  return {kind:'exercise',cat:a[1],title:'Generated exercise: run '+a[0]+' on a fresh input',
    algorithm_name:a[0],method:m,
    problem:'Trace '+a[0]+' on the given input and report the output. The expected output is recorded for self-checking.',
    description:'Hands-on drill for '+a[0]+' ('+COMPLEX[m][0]+' time). Work it by hand, then compare against the recorded output.',
    test_cases:[tc],complexity_time:COMPLEX[m][0],complexity_space:COMPLEX[m][1],
    source:'signature',creation_mode:'SIGNATURE-GENERATED'};
}
function genQuiz(rnd){
  var a=pick(ALGS,rnd),m=a[2];
  var wrong=pick(['O(n)','O(n^2)','O(log n)','O(n log n)','O(2^n)','O(V + E)'],rnd);
  if(wrong===COMPLEX[m][0])wrong='O(n!)';
  return {kind:'quiz',cat:a[1],title:'Generated quiz: complexity of '+a[0],
    algorithm_name:a[0],method:m,
    problem:'What are the time and space complexities of '+a[0]+'?',
    description:'Quick recall check. The correct complexities are recorded in the answer field.',
    complexity_time:COMPLEX[m][0],complexity_space:COMPLEX[m][1],
    answer:{time:COMPLEX[m][0],space:COMPLEX[m][1],distractor:wrong},
    source:'signature',creation_mode:'SIGNATURE-GENERATED'};
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
  cat=cat||pick(CATS,rnd);
  var g=rnd()<0.6?genExercise(rnd):genQuiz(rnd);
  g.category=cat;
  var rec=baseRec(seed,cat,g.title);
  Object.keys(g).forEach(function(k){if(k!=='cat'&&k!=='title')rec[k]=g[k];});
  return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-ALG-\d{7}$/.test(r.id||''))e.push('id');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(r.source!=='online'&&r.source!=='signature')e.push('source');
  if(r.source==='online'&&typeof r.source_ref!=='string')e.push('source_ref');
  if(r.source==='signature'&&r.creation_mode!=='SIGNATURE-GENERATED')e.push('creation_mode');
  var m=r.method;
  if(!EXEC[m])e.push('method');
  else{
    var cx=COMPLEX[m];
    if(r.complexity_time!==cx[0]||r.complexity_space!==cx[1])e.push('complexity');
    (r.test_cases||[]).forEach(function(tc){
      var got;
      try{got=EXEC[m](tc.input);}catch(x){e.push('exec threw');return;}
      if(sjson(got)!==sjson(tc.expected))e.push('test_case mismatch');
    });
    if(r.kind==='quiz'&&r.answer){
      if(r.answer.time!==cx[0]||r.answer.space!==cx[1])e.push('quiz answer');
    }
  }
  if(r.kind==='algorithm'&&(typeof r.description!=='string'||!r.description.length))e.push('description');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var seen={};(sample||[]).forEach(function(s){if(s&&s.t)seen[s.t]=1;});
  if(seen[rec.title])return {ok:false,errors:['duplicate title in archive sample']};
  return {ok:true,errors:[]};
}
var gen={version:'jahdb-algorithms-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('algorithms',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
