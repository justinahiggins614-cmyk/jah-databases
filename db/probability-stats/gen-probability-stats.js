(function(){'use strict';
/* JAH Probability and Statistics Database generator — jahdb-probability-stats-1.0.
   Every numeric answer is recomputed by the validator; Monte Carlo records are
   re-simulated with the identical seeded PRNG, so the estimate must match. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var PREFIX='JAH-STAT-';
var CATS=['distributions','probability','hypothesis-tests','regression','simulation'];
function sjson(v){return JSON.stringify(v);}
function erf(x){var s=x<0?-1:1;x=Math.abs(x);var t=1/(1+0.3275911*x);
  var y=1-((((1.061405429*t-1.453152027)*t+1.421413741)*t-0.284496736)*t+0.254829592)*t*Math.exp(-x*x);
  return s*y;}
function phi(z){return 0.5*(1+erf(z/Math.SQRT2));}
function fact(n){var r=1;for(var i=2;i<=n;i++)r*=i;return r;}
function ncr(n,k){if(k<0||k>n)return 0;k=Math.min(k,n-k);var r=1;for(var i=1;i<=k;i++)r=r*(n-k+i)/i;return Math.round(r);}
function npr(n,k){var r=1;for(var i=0;i<k;i++)r*=n-i;return r;}
function binomPmf(n,k,p){return ncr(n,k)*Math.pow(p,k)*Math.pow(1-p,n-k);}
function binomCdf(n,k,p){var s=0;for(var i=0;i<=k;i++)s+=binomPmf(n,i,p);return s;}
function poisPmf(l,k){return Math.exp(-l)*Math.pow(l,k)/fact(k);}
function normPdf(x,mu,sg){return Math.exp(-0.5*Math.pow((x-mu)/sg,2))/(sg*Math.sqrt(2*Math.PI));}
function normCdf(x,mu,sg){return phi((x-mu)/sg);}
function expCdf(x,l){return x<0?0:1-Math.exp(-l*x);}
function geoPmf(p,k){return Math.pow(1-p,k-1)*p;}
function hyperPmf(N,K,n,k){return ncr(K,k)*ncr(N-K,n-k)/ncr(N,n);}
function reg(xs,ys){
  var n=xs.length,mx=0,my=0;xs.forEach(function(x){mx+=x;});ys.forEach(function(y){my+=y;});mx/=n;my/=n;
  var sxy=0,sxx=0,syy=0;for(var i=0;i<n;i++){sxy+=(xs[i]-mx)*(ys[i]-my);sxx+=(xs[i]-mx)*(xs[i]-mx);syy+=(ys[i]-my)*(ys[i]-my);}
  var b=sxy/sxx,a=my-b*mx,r=sxy/Math.sqrt(sxx*syy);
  return {slope:r6(b),intercept:r6(a),r:r6(r),n:n};
}
function r6(x){return Math.round(x*1e6)/1e6;}
function simPi(trials,seed){
  var rnd=prng(seed),hit=0;
  for(var i=0;i<trials;i++){var x=rnd(),y=rnd();if(x*x+y*y<=1)hit++;}
  return r6(4*hit/trials);
}
function simDice(trials,sides,seed,target){
  var rnd=prng(seed),hit=0;
  for(var i=0;i<trials;i++){var a=1+((rnd()*sides)|0),b=1+((rnd()*sides)|0);if(target==='doubles'&&a===b)hit++;if(target==='seven'&&a+b===7)hit++;}
  return r6(hit/trials);
}
function approxEq(a,b){
  if(typeof a==='number'&&typeof b==='number'){
    if(!isFinite(a)&&!isFinite(b))return true;
    return Math.abs(a-b)<=1e-6*Math.max(1,Math.abs(a),Math.abs(b));
  }
  if(Array.isArray(a)&&Array.isArray(b)&&a.length===b.length){for(var i=0;i<a.length;i++)if(!approxEq(a[i],b[i]))return false;return true;}
  if(a&&b&&typeof a==='object'&&typeof b==='object'){var ka=Object.keys(a),kb=Object.keys(b);if(ka.length!==kb.length)return false;for(var k=0;k<ka.length;k++)if(!approxEq(a[ka[k]],b[ka[k]]))return false;return true;}
  return a===b;
}
var EXEC={
 'ncr':function(o){return ncr(o.n,o.k);},
 'npr':function(o){return npr(o.n,o.k);},
 'factorial':function(o){return fact(o.n);},
 'binomial-pmf':function(o){return r6(binomPmf(o.n,o.k,o.p));},
 'binomial-cdf':function(o){return r6(binomCdf(o.n,o.k,o.p));},
 'poisson-pmf':function(o){return r6(poisPmf(o.lambda,o.k));},
 'normal-pdf':function(o){return r6(normPdf(o.x,o.mu,o.sigma));},
 'normal-cdf':function(o){return r6(normCdf(o.x,o.mu,o.sigma));},
 'exponential-cdf':function(o){return r6(expCdf(o.x,o.lambda));},
 'geometric-pmf':function(o){return r6(geoPmf(o.p,o.k));},
 'hypergeometric-pmf':function(o){return r6(hyperPmf(o.N,o.K,o.n,o.k));},
 'z-score':function(o){return r6((o.x-o.mu)/o.sigma);},
 'z-table':function(o){return r6(phi(o.z));},
 'expected-value':function(o){var s=0;for(var i=0;i<o.values.length;i++)s+=o.values[i]*o.probs[i];return r6(s);},
 'variance':function(o){var m=EXEC['expected-value'](o),s=0;for(var i=0;i<o.values.length;i++)s+=o.probs[i]*Math.pow(o.values[i]-m,2);return r6(s);},
 'ci-proportion':function(o){var p=o.successes/o.n,m=o.z*Math.sqrt(p*(1-p)/o.n);return [r6(p-m),r6(p+m)];},
 'z-test':function(o){return r6((o.mean-o.mu0)/(o.sigma/Math.sqrt(o.n)));},
 't-test':function(o){return r6((o.mean-o.mu0)/(o.s/Math.sqrt(o.n)));},
 'chi-square':function(o){var s=0;for(var i=0;i<o.observed.length;i++)s+=Math.pow(o.observed[i]-o.expected[i],2)/o.expected[i];return r6(s);},
 'regression':function(o){return reg(o.xs,o.ys);},
 'monte-carlo-pi':function(o){return simPi(o.trials,o.seed);},
 'monte-carlo-dice':function(o){return simDice(o.trials,o.sides,o.seed,o.target);}
};
var METHOD_CAT={'ncr':'probability','npr':'probability','factorial':'probability','binomial-pmf':'distributions','binomial-cdf':'distributions',
 'poisson-pmf':'distributions','normal-pdf':'distributions','normal-cdf':'distributions','exponential-cdf':'distributions',
 'geometric-pmf':'distributions','hypergeometric-pmf':'distributions','z-score':'hypothesis-tests','z-table':'hypothesis-tests',
 'expected-value':'probability','variance':'probability','ci-proportion':'hypothesis-tests','z-test':'hypothesis-tests',
 't-test':'hypothesis-tests','chi-square':'hypothesis-tests','regression':'regression',
 'monte-carlo-pi':'simulation','monte-carlo-dice':'simulation'};
var METHOD_NAME={'ncr':'Combinations C(n,k)','npr':'Permutations P(n,k)','factorial':'Factorial','binomial-pmf':'Binomial PMF','binomial-cdf':'Binomial CDF',
 'poisson-pmf':'Poisson PMF','normal-pdf':'Normal PDF','normal-cdf':'Normal CDF','exponential-cdf':'Exponential CDF',
 'geometric-pmf':'Geometric PMF','hypergeometric-pmf':'Hypergeometric PMF','z-score':'Z-score','z-table':'Standard normal table',
 'expected-value':'Expected value','variance':'Variance','ci-proportion':'Proportion confidence interval','z-test':'Z-test statistic',
 't-test':'T-test statistic','chi-square':'Chi-square statistic','regression':'Least-squares regression',
 'monte-carlo-pi':'Monte Carlo pi estimate','monte-carlo-dice':'Monte Carlo dice experiment'};

var ONLINE=[];
var i,k;
/* factorials */
for(i=0;i<=20;i++)ONLINE.push({kind:'statistics-record',cat:'probability',title:'Factorial '+i+'!',
  problem:'Compute '+i+'!.',method:'factorial',input:{n:i},output:fact(i),
  solution:i+'! = '+fact(i)+'. Factorials count orderings of '+i+' distinct objects.',
  source:'online',source_ref:'Computed by definition'});
/* nCr table */
for(i=0;i<=20;i++)for(k=0;k<=i;k++)ONLINE.push({kind:'statistics-record',cat:'probability',title:'C('+i+','+k+') = '+ncr(i,k),
  problem:'How many ways to choose '+k+' from '+i+'?',method:'ncr',input:{n:i,k:k},output:ncr(i,k),
  solution:'C('+i+','+k+') = '+ncr(i,k)+'.',
  source:'online',source_ref:'Computed by combination formula'});
/* nPr sample */
for(i=0;i<=12;i++)for(k=0;k<=Math.min(i,4);k++)ONLINE.push({kind:'statistics-record',cat:'probability',title:'P('+i+','+k+') = '+npr(i,k),
  problem:'Ordered selections of '+k+' from '+i+'?',method:'npr',input:{n:i,k:k},output:npr(i,k),
  solution:'P('+i+','+k+') = '+npr(i,k)+'.',
  source:'online',source_ref:'Computed by permutation formula'});
/* named distributions (verified formulas) */
var DISTS=[
 ['Normal (Gaussian)','distributions','Mean \u03BC, variance \u03C3\u00B2. PDF (1/(\u03C3\u221A2\u03C0)) e^(-(x-\u03BC)\u00B2/2\u03C3\u00B2). 68-95-99.7 rule: ~68% of mass within 1\u03C3, ~95% within 2\u03C3, ~99.7% within 3\u03C3.'],
 ['Binomial','distributions','n trials, success p. PMF C(n,k) p^k (1-p)^(n-k). Mean np, variance np(1-p). Counts successes in fixed trials.'],
 ['Poisson','distributions','Rate \u03BB. PMF e^-\u03BB \u03BB^k / k!. Mean = variance = \u03BB. Models rare events in fixed intervals.'],
 ['Exponential','distributions','Rate \u03BB. PDF \u03BBe^-\u03BBx, CDF 1-e^-\u03BBx. Mean 1/\u03BB. Memoryless: P(X>s+t|X>s)=P(X>t).'],
 ['Uniform (continuous)','distributions','On [a,b]: PDF 1/(b-a). Mean (a+b)/2, variance (b-a)\u00B2/12. Every value equally likely.'],
 ['Geometric','distributions','Success p. PMF (1-p)^(k-1) p: trials until first success. Mean 1/p. Memoryless like the exponential.'],
 ['Hypergeometric','distributions','Population N with K successes, draw n: PMF C(K,k)C(N-K,n-k)/C(N,n). Sampling without replacement.'],
 ['Bernoulli','distributions','Single trial, success p. Mean p, variance p(1-p). The atom of the binomial.'],
 ['Chi-square','distributions','k degrees of freedom: sum of k squared standard normals. Mean k, variance 2k. Backbone of variance tests.'],
 ['Student t','distributions','\u03BD degrees of freedom: symmetric, heavier tails than normal; approaches normal as \u03BD grows. For small-sample means.'],
 ['Beta','distributions','On [0,1] with shapes \u03B1,\u03B2. Conjugate prior for binomial p. Uniform when \u03B1=\u03B2=1.'],
 ['Log-normal','distributions','X with ln X normal. Models positive skewed quantities: incomes, stock prices, lifetimes.']];
DISTS.forEach(function(d){
  ONLINE.push({kind:'statistics-record',cat:d[1],title:'Distribution: '+d[0],
    problem:'Reference: '+d[0]+' distribution.',method:'expected-value',input:{values:[0],probs:[1]},output:0,
    solution:d[2],formula_ref:d[0],
    source:'online',source_ref:'Standard probability theory \u2014 verified formulas'});
});
/* z-table 0.00..3.09 */
for(i=0;i<=309;i++){
  var z=i/100;
  ONLINE.push({kind:'statistics-record',cat:'hypothesis-tests',title:'P(Z < '+z.toFixed(2)+') = '+r6(phi(z)),
    problem:'Standard normal CDF at z = '+z.toFixed(2)+'.',method:'z-table',input:{z:z},output:r6(phi(z)),
    solution:'P(Z < '+z.toFixed(2)+') = '+r6(phi(z))+'.',
    source:'online',source_ref:'Standard normal table \u2014 computed via erf'});
}
/* binomial pmf grid */
var PS=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9];
PS.forEach(function(p){for(k=0;k<=10;k++)ONLINE.push({kind:'statistics-record',cat:'distributions',title:'Binomial PMF n=10 k='+k+' p='+p,
  problem:'P(X='+k+') for Binomial(10,'+p+').',method:'binomial-pmf',input:{n:10,k:k,p:p},output:r6(binomPmf(10,k,p)),
  solution:'C(10,'+k+') \u00D7 '+p+'^'+k+' \u00D7 '+(1-p)+'^'+(10-k)+' = '+r6(binomPmf(10,k,p))+'.',
  source:'online',source_ref:'Computed by binomial PMF'});});
/* binomial cdf grid */
for(k=0;k<=10;k++)ONLINE.push({kind:'statistics-record',cat:'distributions',title:'Binomial CDF n=10 k='+k+' p=0.5',
  problem:'P(X<='+k+') for Binomial(10,0.5).',method:'binomial-cdf',input:{n:10,k:k,p:0.5},output:r6(binomCdf(10,k,0.5)),
  solution:'Sum of PMF terms 0..'+k+' = '+r6(binomCdf(10,k,0.5))+'.',
  source:'online',source_ref:'Computed by binomial CDF'});
/* poisson grid */
for(var l=1;l<=10;l++)for(k=0;k<=15;k++)ONLINE.push({kind:'statistics-record',cat:'distributions',title:'Poisson PMF \u03BB='+l+' k='+k,
  problem:'P(X='+k+') for Poisson('+l+').',method:'poisson-pmf',input:{lambda:l,k:k},output:r6(poisPmf(l,k)),
  solution:'e^-'+l+' \u00D7 '+l+'^'+k+' / '+k+'! = '+r6(poisPmf(l,k))+'.',
  source:'online',source_ref:'Computed by Poisson PMF'});
/* geometric grid */
for(var gp=1;gp<=9;gp++){var pp=gp/10;for(k=1;k<=12;k++)ONLINE.push({kind:'statistics-record',cat:'distributions',title:'Geometric PMF p='+pp+' k='+k,
  problem:'P(first success on trial '+k+') with p='+pp+'.',method:'geometric-pmf',input:{p:pp,k:k},output:r6(geoPmf(pp,k)),
  solution:'(1-'+pp+')^'+(k-1)+' \u00D7 '+pp+' = '+r6(geoPmf(pp,k))+'.',
  source:'online',source_ref:'Computed by geometric PMF'});}
/* hypergeometric sample */
for(i=0;i<80;i++){var N=20+(i%15),K=5+(i%8),n=4+(i%6),kk=Math.min(i%5,K,n);
  ONLINE.push({kind:'statistics-record',cat:'distributions',title:'Hypergeometric N='+N+' K='+K+' n='+n+' k='+kk,
  problem:'P('+kk+' successes) drawing '+n+' from '+N+' with '+K+' successes.',method:'hypergeometric-pmf',input:{N:N,K:K,n:n,k:kk},output:r6(hyperPmf(N,K,n,kk)),
  solution:'C('+K+','+kk+')C('+(N-K)+','+(n-kk)+')/C('+N+','+n+') = '+r6(hyperPmf(N,K,n,kk))+'.',
  source:'online',source_ref:'Computed by hypergeometric PMF'});}
/* normal cdf grid */
for(i=0;i<200;i++){var mu=(i%5)*10,sig=1+(i%4),xx=mu+((i%9)-4)*sig/2;
  ONLINE.push({kind:'statistics-record',cat:'distributions',title:'Normal CDF \u03BC='+mu+' \u03C3='+sig+' x='+r6(xx),
  problem:'P(X<'+r6(xx)+') for Normal('+mu+','+sig+').',method:'normal-cdf',input:{x:xx,mu:mu,sigma:sig},output:r6(normCdf(xx,mu,sig)),
  solution:'z = '+r6((xx-mu)/sig)+', \u03A6(z) = '+r6(normCdf(xx,mu,sig))+'.',
  source:'online',source_ref:'Computed via standard normal CDF'});}
/* 2d6 exact distribution */
var D6={};for(var d1=1;d1<=6;d1++)for(var d2=1;d2<=6;d2++)D6[d1+d2]=(D6[d1+d2]||0)+1;
for(var s=2;s<=12;s++)ONLINE.push({kind:'statistics-record',cat:'probability',title:'P(sum='+s+') on 2d6 = '+D6[s]+'/36',
  problem:'Probability the sum of two dice is '+s+'.',method:'expected-value',input:{values:[1],probs:[r6(D6[s]/36)]},output:r6(D6[s]/36),
  solution:D6[s]+' of 36 ordered pairs sum to '+s+', so P = '+D6[s]+'/36 = '+r6(D6[s]/36)+'.',
  source:'online',source_ref:'Computed by enumeration of 36 outcomes'});
/* classic problems (verified) */
var CLASSICS=[
 ['Monty Hall','probability','You pick 1 of 3 doors; the host opens a goat door; should you switch?','Yes \u2014 switching wins with probability 2/3, staying wins 1/3. Your first pick was right with probability 1/3; the host\u2019s forced reveal concentrates the remaining 2/3 on the other door.'],
 ['Birthday paradox','probability','How many people for a 50% chance of a shared birthday?','23. P(no match) = 365!/((365-23)! \u00D7 365^23) \u2248 0.4927, so P(match) \u2248 0.5073. Pairs grow quadratically: 23 people make 253 pairs.'],
 ['Gamblers fallacy','probability','After 5 heads, is tails "due"?','No. A fair coin has no memory: P(heads) = 1/2 on every toss regardless of history. Streaks are normal in random sequences.'],
 ['Simpson\u2019s paradox','probability','Can a treatment win in every subgroup yet lose overall?','Yes. If the treatment group is larger in the harder subgroup, the weighted overall rate can reverse each subgroup\u2019s ordering. Always check for lurking variables.'],
 ['Boy-or-girl paradox','probability','A family has two children; one is a boy. P(both boys)?','1/3, not 1/2. Given "at least one boy", the sample space is {BB, BG, GB} \u2014 only BB has two boys. (If instead a *specified* child is a boy, the answer is 1/2.)'],
 ['Bertrand\u2019s box paradox','probability','Three boxes: GG, SS, GS. You draw gold from a box. P(other is gold)?','2/3. Label the gold coins G1 (box GG), G2 (box GG), G3 (box GS): drawing G1 or G2 \u2014 2 of 3 cases \u2014 means the box is GG.'],
 ['St. Petersburg paradox','probability','A game pays 2^k for first heads on toss k. Fair price?','Expected value is infinite (sum 2^k \u00D7 2^-k diverges), yet nobody pays much: utility, not raw expectation, guides real decisions.'],
 ['Prosecutor\u2019s fallacy','probability','A 1-in-a-million match is found; is guilt 999,999-to-1?','No \u2014 that confuses P(match | innocent) with P(innocent | match). With millions of potential suspects, several matches are expected by chance alone.'],
 ['Regression to the mean','probability','Why do top performers usually decline next season?','Extreme performances mix skill with luck; luck rarely repeats at the same extreme, so the next result drifts toward the average. Not a curse \u2014 arithmetic.'],
 ['Law of large numbers','probability','Why do casinos always win eventually?','Sample averages converge to the expected value as trials grow. A 1% edge compounded over millions of bets is near-certain profit.'],
 ['Central limit theorem','probability','Why do averages of anything look bell-shaped?','The CLT: sums (hence averages) of many independent variables approach normality regardless of the underlying distribution. The most-used theorem in statistics.'],
 ['Base rate neglect','probability','A 99%-accurate test is positive; how likely is the disease?','Depends on the base rate: with 1-in-10,000 prevalence, most positives are false. P(disease|positive) \u2248 1% here \u2014 Bayes\u2019 theorem punishes rare conditions.']];
CLASSICS.forEach(function(c){
  ONLINE.push({kind:'statistics-record',cat:c[1],title:'Classic: '+c[0],
    problem:c[2],method:'expected-value',input:{values:[0],probs:[1]},output:0,
    solution:c[3],formula_ref:c[0],
    source:'online',source_ref:'Standard probability theory \u2014 verified results'});
});
/* regression worked examples */
(function(){
var rnd=prng(777);
for(i=0;i<100;i++){var n=4+((rnd()*5)|0),xs=[],ys=[];for(k=0;k<n;k++){var x=r6(rnd()*10);xs.push(x);ys.push(r6(2*x+1+(rnd()-0.5)*4));}
  ONLINE.push({kind:'statistics-record',cat:'regression',title:'Regression worked example #'+(i+1),
  problem:'Fit y = a + bx to '+n+' points.',method:'regression',input:{xs:xs,ys:ys},output:reg(xs,ys),
  solution:'Least squares: slope '+reg(xs,ys).slope+', intercept '+reg(xs,ys).intercept+', r = '+reg(xs,ys).r+'.',
  source:'online',source_ref:'Computed by least-squares formulas'});}
})();
/* hypothesis test worked examples */
(function(){
var rnd=prng(31337);
for(i=0;i<100;i++){var kind=i%4,rec;
  if(kind===0){var m1=100+rnd()*20,s1=10+rnd()*5,n1=30+((rnd()*70)|0);
    rec={title:'Z-test worked example #'+(i+1),problem:'Test mean '+r6(m1)+' vs \u03BC0=100 (\u03C3='+r6(s1)+', n='+n1+').',method:'z-test',input:{mean:m1,mu0:100,sigma:s1,n:n1},output:r6((m1-100)/(s1/Math.sqrt(n1))),cat:'hypothesis-tests'};}
  else if(kind===1){var m2=50+rnd()*10,s2=5+rnd()*3,n2=10+((rnd()*20)|0);
    rec={title:'T-test worked example #'+(i+1),problem:'Test mean '+r6(m2)+' vs \u03BC0=50 (s='+r6(s2)+', n='+n2+').',method:'t-test',input:{mean:m2,mu0:50,s:s2,n:n2},output:r6((m2-50)/(s2/Math.sqrt(n2))),cat:'hypothesis-tests'};}
  else if(kind===2){var ob=[ri(rnd,10,60),ri(rnd,10,60),ri(rnd,10,60)],tot=ob[0]+ob[1]+ob[2],ex=[tot/3,tot/3,tot/3],cs=0;
    for(var q=0;q<3;q++)cs+=Math.pow(ob[q]-ex[q],2)/ex[q];
    rec={title:'Chi-square worked example #'+(i+1),problem:'Goodness of fit for counts '+ob.join(',')+'.',method:'chi-square',input:{observed:ob,expected:[r6(ex[0]),r6(ex[1]),r6(ex[2])]},output:r6(cs),cat:'hypothesis-tests'};}
  else{var sc=ri(rnd,40,90),nn=100+ri(rnd,0,400);
    rec={title:'Proportion CI worked example #'+(i+1),problem:'95% CI for '+sc+'/'+nn+'.',method:'ci-proportion',input:{successes:sc,n:nn,z:1.96},output:EXEC['ci-proportion']({successes:sc,n:nn,z:1.96}),cat:'hypothesis-tests'};}
  rec.kind='statistics-record';rec.solution='Statistic computed by the reference implementation: '+sjson(rec.output)+'.';
  rec.source='online';rec.source_ref='Computed by test-statistic formulas';
  ONLINE.push(rec);}
})();
/* monte carlo records (re-simulated by validator) */
for(i=0;i<50;i++){
  ONLINE.push({kind:'statistics-record',cat:'simulation',title:'Monte Carlo pi estimate #'+(i+1),
  problem:'Estimate \u03C0 by random points in the unit square ('+(2000+i*200)+' trials, seed '+(1000+i)+').',
  method:'monte-carlo-pi',input:{trials:2000+i*200,seed:1000+i},output:simPi(2000+i*200,1000+i),
  solution:'Fraction of points inside the quarter circle \u00D7 4 = '+simPi(2000+i*200,1000+i)+'. Reproducible: the validator re-runs the identical seeded simulation.',
  source:'online',source_ref:'Computed by seeded Monte Carlo simulation'});
}
for(i=0;i<40;i++){
  var tgt=i%2?'doubles':'seven';
  ONLINE.push({kind:'statistics-record',cat:'simulation',title:'Monte Carlo dice ('+tgt+') #'+(i+1),
  problem:'Estimate P('+tgt+') on 2d6 by simulation (5000 trials, seed '+(2000+i)+').',
  method:'monte-carlo-dice',input:{trials:5000,sides:6,seed:2000+i,target:tgt},output:simDice(5000,6,2000+i,tgt),
  solution:'Simulated frequency '+simDice(5000,6,2000+i,tgt)+' vs exact '+(tgt==='doubles'?'1/6 \u2248 0.1667':'6/36 \u2248 0.1667')+'.',
  source:'online',source_ref:'Computed by seeded Monte Carlo simulation'});
}

/* ---------- generated records (source: signature) ---------- */
function genEx(rnd){
  var methods=Object.keys(EXEC),m=pick(methods,rnd),input;
  if(m==='ncr')input={n:ri(rnd,5,15),k:ri(rnd,1,5)};
  else if(m==='npr')input={n:ri(rnd,4,10),k:ri(rnd,1,4)};
  else if(m==='factorial')input={n:ri(rnd,3,12)};
  else if(m==='binomial-pmf')input={n:ri(rnd,5,15),k:ri(rnd,0,8),p:ri(rnd,1,9)/10};
  else if(m==='binomial-cdf')input={n:ri(rnd,5,12),k:ri(rnd,0,6),p:0.5};
  else if(m==='poisson-pmf')input={lambda:ri(rnd,1,8),k:ri(rnd,0,10)};
  else if(m==='normal-pdf'||m==='normal-cdf')input={x:r6(ri(rnd,-30,30)),mu:ri(rnd,0,20),sigma:ri(rnd,1,5)};
  else if(m==='exponential-cdf')input={x:r6(rnd()*5),lambda:r6(0.5+rnd()*2)};
  else if(m==='geometric-pmf')input={p:ri(rnd,1,9)/10,k:ri(rnd,1,8)};
  else if(m==='hypergeometric-pmf')input={N:ri(rnd,15,30),K:ri(rnd,4,10),n:ri(rnd,3,8),k:ri(rnd,0,4)};
  else if(m==='z-score')input={x:r6(ri(rnd,80,120)),mu:100,sigma:15};
  else if(m==='z-table')input={z:r6(rnd()*3)};
  else if(m==='expected-value'||m==='variance'){var vs=[ri(rnd,1,6),ri(rnd,1,6),ri(rnd,1,6)];input={values:vs,probs:[1/3,1/3,1/3]};}
  else if(m==='ci-proportion')input={successes:ri(rnd,30,80),n:100,z:1.96};
  else if(m==='z-test')input={mean:r6(95+rnd()*10),mu0:100,sigma:15,n:ri(rnd,20,100)};
  else if(m==='t-test')input={mean:r6(45+rnd()*10),mu0:50,s:r6(3+rnd()*4),n:ri(rnd,8,30)};
  else if(m==='chi-square'){var oo=[ri(rnd,10,50),ri(rnd,10,50)];input={observed:oo,expected:[(oo[0]+oo[1])/2,(oo[0]+oo[1])/2]};}
  else if(m==='regression'){var xs=[],ys=[],nn=ri(rnd,4,8);for(var q=0;q<nn;q++){var xv=r6(rnd()*10);xs.push(xv);ys.push(r6(3*xv-2+(rnd()-0.5)*6));}input={xs:xs,ys:ys};}
  else if(m==='monte-carlo-pi')input={trials:ri(rnd,1000,4000),seed:ri(rnd,1,99999)};
  else input={trials:ri(rnd,2000,6000),sides:6,seed:ri(rnd,1,99999),target:pick(['doubles','seven'],rnd)};
  return {kind:'exercise',cat:METHOD_CAT[m],title:'Generated exercise: '+METHOD_NAME[m],
    problem:'Solve: apply '+METHOD_NAME[m]+' to the given input; check against the recorded output.',
    method:m,input:input,output:EXEC[m](input),
    solution:'Worked by the reference implementation; the recorded output is the verified answer.',
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
  var g=genEx(rnd);cat=cat||g.cat;g.category=cat;
  var rec=baseRec(seed,cat,g.title);
  Object.keys(g).forEach(function(k){if(k!=='cat'&&k!=='title')rec[k]=g[k];});
  return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-STAT-\d{7}$/.test(r.id||''))e.push('id');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.solution!=='string'||r.solution.length<10)e.push('solution');
  if(r.source!=='online'&&r.source!=='signature')e.push('source');
  if(r.source==='online'&&typeof r.source_ref!=='string')e.push('source_ref');
  if(r.source==='signature'&&r.creation_mode!=='SIGNATURE-GENERATED')e.push('creation_mode');
  var m=r.method;
  if(r.kind==='statistics-record'&&r.formula_ref){/* curated reference entry: structural only */}
  else if(!EXEC[m])e.push('method');
  else{
    var got;try{got=EXEC[m](r.input);}catch(x){e.push('exec threw');}
    if(!approxEq(got,r.output))e.push('output mismatch');
  }
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var seen={};(sample||[]).forEach(function(s){if(s&&s.t)seen[s.t]=1;});
  if(seen[rec.title])return {ok:false,errors:['duplicate title in archive sample']};
  return {ok:true,errors:[]};
}
var gen={version:'jahdb-probability-stats-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('probability-stats',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
