(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["linear", "nonlinear", "normalization", "attention", "loss"];
var PREFIX='JAH-NNO-S-';
var USE="Used by ML engineers, compiler writers, and students to understand exactly what each layer computes.";
var FLD=[["operator", "Operator"], ["math", "Math"], ["shapes", "Shapes"]];
var DEMO="# {title} - softmax with temperature (python3)\nimport math\nx={d1}\nT={d2}\nnd={d3}\nm=max(x)\ne=[math.exp((v-m)/T) for v in x]\ns=sum(e)\nout=[round(v/s, nd) for v in e]\nprint(\"softmax:\", out, \"sum=%.3f\" % sum(out))\n";
var SIG=true;
var SRC="signature-generated-completion";
var B=[["linear", "MatMul", "Computes C = A @ B, the workhorse of linear layers and attention projections.", "MatMul", "C[i,j] = sum_k A[i,k]*B[k,j]", "[M,K]x[K,N] -> [M,N]", "[2.0, 1.0, 0.5]", "1.0", "4"], ["nonlinear", "Convolution2D", "Slides a learned kernel over the input, computing cross-correlation at each position.", "Convolution2D", "(I*K)[i,j] = sum_mn I[i+m,j+n]K[m,n]", "[B,C,H,W] -> [B,C',H',W']", "[1.0, 2.0, 3.0]", "1.0", "4"], ["normalization", "Softmax", "Turns logits into a probability distribution with the normalized exponential.", "p_i = exp(x_i/T)/sum_j exp(x_j/T)", "[B,S] -> [B,S]", "1.0", "[0.5, 1.5, 2.5]", "0.5", "4"], ["attention", "LayerNorm", "Normalizes each sample to zero mean and unit variance, then applies learned scale and shift.", "LayerNorm", "y = (x-mean)/sqrt(var+eps)*g + b", "[B,S,H] -> same", "[3.0, 1.0, 4.0]", "1.0", "4"], ["loss", "ReLU", "Rectified linear unit: passes positive values, zeroes negatives; cheap and effective.", "ReLU", "y = max(0, x)", "any -> same", "[-1.0, 0.0, 2.0]", "1.0", "4"], ["linear", "GELU", "Gaussian error linear unit: smooth ReLU approximation used in transformers.", "GELU", "y = x*Phi(x)", "any -> same", "[0.5, -0.5, 1.5]", "1.0", "4"], ["nonlinear", "Multi-Head Attention", "Computes softmax(QK^T/sqrt(d))V in parallel heads, letting positions attend to each other.", "Multi-Head Attention", "head_i = Attn(QW_q, KW_k, VW_v)", "[B,S,D] -> [B,S,D]", "[1.0, 2.0, 0.0]", "1.0", "4"], ["normalization", "Embedding Lookup", "Maps integer token IDs to learned dense vectors from an embedding table.", "Embedding Lookup", "y = E[id]", "ids [B,S] -> [B,S,D]", "[0.2, 0.8, 0.1]", "1.0", "4"], ["attention", "BatchNorm", "Normalizes across the batch during training, using running stats at inference.", "BatchNorm", "y = (x-mu_b)/sqrt(s_b^2+eps)*g + b", "[B,C,H,W] -> same", "[2.0, 2.0, 2.0]", "1.0", "4"], ["loss", "MaxPool", "Downsamples by taking the maximum in each window, keeping translation invariance.", "MaxPool", "y[i,j] = max window", "[B,C,H,W] -> [B,C,H/2,W/2]", "[1.0, 3.0, 2.0]", "1.0", "4"], ["linear", "Dropout", "Randomly zeroes activations with probability p during training as regularization.", "Dropout", "y = mask*x/(1-p)", "any -> same", "[1.0, 1.0, 1.0]", "1.0", "4"], ["nonlinear", "Linear Projection", "Applies y = Wx + b, the basic learned affine transform in every dense layer.", "Linear Projection", "y = Wx + b", "[B,in] -> [B,out]", "[0.5, 1.5, 2.5]", "2.0", "4"], ["normalization", "Sigmoid", "Squashes values to (0,1); used for gates and binary probabilities.", "Sigmoid", "y = 1/(1+exp(-x))", "any -> same", "[-2.0, 0.0, 2.0]", "1.0", "4"], ["attention", "Tanh", "Squashes values to (-1,1); zero-centered alternative to sigmoid.", "Tanh", "y = (e^x - e^-x)/(e^x + e^-x)", "any -> same", "[-1.0, 0.0, 1.0]", "1.0", "4"], ["loss", "Cross-Entropy Loss", "Measures the negative log-likelihood of the true class under predicted probabilities.", "Cross-Entropy Loss", "L = -sum y_i log p_i", "logits [B,C] -> scalar", "[2.0, 1.0, 0.1]", "1.0", "4"], ["linear", "RMSNorm", "Normalizes by root-mean-square without mean centering; cheaper than LayerNorm.", "RMSNorm", "y = x/sqrt(mean(x^2)+eps)*g", "any -> same", "[1.0, 2.0, 3.0]", "1.0", "4"], ["nonlinear", "Grouped-Query Attention", "Shares key/value heads across query groups, cutting KV-cache memory with little quality loss.", "Grouped-Query Attention", "GQA(Q, K_g, V_g)", "[B,S,D] -> [B,S,D]", "[1.5, 0.5, 2.5]", "1.0", "4"], ["normalization", "Depthwise Convolution", "Applies one kernel per channel instead of mixing channels, slashing parameters.", "Depthwise Convolution", "per-channel conv", "[B,C,H,W] -> same", "[0.5, 2.5, 1.0]", "1.0", "4"], ["attention", "Upsampling", "Increases spatial resolution by nearest, bilinear, or learned transposed convolution.", "Upsampling", "y = interp(x, scale)", "low-res -> high-res", "[1.0, 2.0]", "1.0", "4"], ["loss", "Residual Add", "Adds a layer's input to its output so networks learn residual functions, enabling very deep models.", "Residual Add", "y = x + F(x)", "same -> same", "[1.0, 0.5, 1.5]", "1.0", "4"]];
function buildTitle(b){ return SIG?('Signature '+b[1]):b[1]; }
function buildDesc(b){
  var d=b[2]+' Recorded facts \u2014 '+FLD[0][1]+': '+b[3]+'; '+FLD[1][1]+': '+b[4]+'; '+FLD[2][1]+': '+b[5]+'. '+USE;
  if(SIG) d='Signature-original: '+d+' Built as a Signature-authored original for the JAH network; clearly labeled Signature and never presented as a public record.';
  return d;
}
function buildDemo(b){
  return DEMO.split('{title}').join(b[1]).split('{d1}').join(b[6]).split('{d2}').join(b[7]).split('{d3}').join(b[8]);
}
function generate(seed,opts){
  opts=opts||{}; var rnd=prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title=buildTitle(b);
  var fields={}; fields[FLD[0][0]]=b[3]; fields[FLD[1][0]]=b[4]; fields[FLD[2][0]]=b[5];
  if(SIG) fields['signature_label']='Signature-authored original';
  return {id:id,title:title,description:buildDesc(b),category:cat,fields:fields,
    ladder_rank:1+(seed%3),
    demo:'# '+title+' \u2014 runnable demo (python3)\n'+buildDemo(b),
    provenance:'JAH Databases \u00b7 lane N3 build',last_verified:'2026-10-21',src:SRC,_seed:seed};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){
    if(sample[i]&&sample[i].title===rec.title&&sample[i].category===rec.category)
      return {ok:false,errors:['duplicate of archive record '+sample[i].id]};
  }
  return {ok:true,errors:[]};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var idre=new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$');
  if(!idre.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('print(')<0)e.push('demo');
  if(['public-harvest','signature-generated-completion'].indexOf(r.src)<0)e.push('src');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-neural-network-operator-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('neural-network-operator-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
