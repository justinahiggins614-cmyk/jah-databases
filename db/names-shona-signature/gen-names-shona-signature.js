(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=['given-name','surname','place-name','naming-convention'];
var PREFIX="JAH-NMSS8-";
var LABEL="Shona";
var SIG=true;
var SRC="signature-generated-completion";
var GIVEN=[["Tendaimoyo", "unisex", "from tendai (thanks) + moyo (heart): 'thankful heart'"], ["Rudofarai", "unisex", "from rudo (love) + farai (rejoice): 'joyful love'"], ["Tatendanyasha", "unisex", "from tatenda + nyasha (grace)"], ["Chiporudo", "unisex", "from chipo (gift) + rudo (love): 'gift of love'"], ["Faraitenda", "unisex", "from farai + tendai"], ["Nyasharudo", "unisex", "from nyasha + rudo: 'graceful love'"]];
var SURN=[["Moyorudo", "Signature surname: 'heart of love'"], ["Tendaimoyoza", "Signature surname"], ["Farainyasha", "Signature surname"], ["Rudomoyo", "Signature surname: 'love heart'"]];
var PLACES=["Rudopolis", "Tendaiguta", "Faraiharare"];
var CONV=[["Signature Shona-style naming", "Signature originals compound real Shona roots such as rudo, tendai and moyo in the circumstance-name tradition."], ["Labeled creations", "Each is a new Signature creation with its gloss; none is presented as a traditional Shona name."]];
function cap(s){s=String(s||'');return s.charAt(0).toUpperCase()+s.slice(1);}
function descGiven(e){
  if(SIG)return e[0]+' is a Signature original '+LABEL+'-style given name. '+cap(e[2]);
  return e[0]+' is a '+e[1]+' given name in '+LABEL+(e[2]?'. It means "'+e[2]+'".':'.');
}
function descSurn(s){
  if(SIG)return s[0]+' is a Signature original '+LABEL+'-style family name. '+cap(s[1]);
  return s[0]+' is a '+LABEL+' family name'+(s[1]?'. It means "'+s[1]+'".':'.');
}
function descPlace(p){
  if(SIG)return p+' is a Signature original '+LABEL+'-style place name.';
  return p+' is a notable '+LABEL+' place.';
}
function demoFor(r){
  var t={};
  GIVEN.forEach(function(e){t[e[0]]=e[2]||'';});
  SURN.forEach(function(s){t[s[0]]=s[1]||'';});
  var prog='/* '+LABEL+' names — name-meaning lookup demo (jahdb-demo-1.0)\n'+
   ' * RUN ON PC: save as demo.js, then run:  node demo.js [name] */\n'+
   'var TABLE='+JSON.stringify(t)+';\n'+
   'function lookup(q){q=String(q||"").toLowerCase().trim();var ks=Object.keys(TABLE);'+
   'for(var i=0;i<ks.length;i++){if(ks[i].toLowerCase()===q)return ks[i]+" — "+TABLE[ks[i]];}'+
   'var h=ks.filter(function(k){return k.toLowerCase().indexOf(q)>=0;});'+
   'return h.length?h.map(function(k){return k+" — "+TABLE[k];}).join("\\n"):"No match for \\""+q+"\\".";}\n'+
   'var q=(typeof process!=="undefined"&&process.argv[2])||'+JSON.stringify(r.name||"")+';\n'+
   'console.log(lookup(q));\n';
  return {kind:'lookup',title:'Name-meaning lookup demo',program:prog,language:'javascript',run_hint:'node demo.js [name]'};
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var r={id:id,g:cat,c:0,_seed:seed,last_verified:'2026-10-21',src:SRC};
  if(cat==='given-name'){
    var e=pick(GIVEN,rnd);
    r.title=e[0]+(SIG?' — Signature '+LABEL+'-style given name':' — '+LABEL+' given name');
    r.t=r.title;r.description=descGiven(e);r.ladder_rank=1;
    r.name=e[0];r.gender=e[1];r.meaning=e[2];
    r.provenance=SIG?'Signature original: new name created from genuine '+LABEL+' word-roots; labeled a Signature creation.':'Public record: name documented from public linguistic and onomastic sources.';
  }else if(cat==='surname'){
    var s2=pick(SURN,rnd);
    r.title=s2[0]+(SIG?' — Signature '+LABEL+'-style surname':' — '+LABEL+' surname');
    r.t=r.title;r.description=descSurn(s2);r.ladder_rank=2;
    r.name=s2[0];r.meaning=s2[1];
    r.provenance=SIG?'Signature original: new family name created from genuine '+LABEL+' word-roots; labeled a Signature creation.':'Public record: family name documented from public linguistic and onomastic sources.';
  }else if(cat==='place-name'){
    var p=pick(PLACES,rnd);
    r.title=p+(SIG?' — Signature '+LABEL+'-style place name':' — '+LABEL+' place name');
    r.t=r.title;r.description=descPlace(p);r.ladder_rank=2;r.name=p;
    r.provenance=SIG?'Signature original: new place name created from genuine '+LABEL+' word-roots; labeled a Signature creation.':'Public record: place name documented from public geographic sources.';
  }else{
    var cv=pick(CONV,rnd);
    r.title=SIG?('Signature '+LABEL+' naming: '+cv[0]):(cv[0]+' — '+LABEL+' naming convention');
    r.t=r.title;r.description=cv[1];r.ladder_rank=3;r.topic=cv[0];
    r.provenance=SIG?'Signature original: naming practice described for this Signature database.':'Public record: naming custom documented from public cultural sources.';
  }
  r.demo=demoFor(r);
  return r;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  var rx=new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$');
  if(!rx.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||!r.description.length)e.push('description');
  if(CATS.indexOf(r.g)<0)e.push('g');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(!r.demo||typeof r.demo.program!=='string'||!r.demo.program.length)e.push('demo');
  if(!r.src)e.push('src');
  return{ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-shona-signature-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('names-shona-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
