(function(){'use strict';
/* JAH The Ultimate Showdown Generator generator - jahdb-gen-ultimate-showdown-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same output. Real generation, not a sample. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,s){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(s()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}
var PREFIX="JAH-USG-";
var FIELDS=["Sample Brackets", "How It Judges"];
var CONTENDERS=['Cheetah','Peregrine Falcon','Mantis Shrimp','Tardigrade','Blue Whale','Honey Badger',
 'Bullet Train','F1 Car','Saturn V','Quantum Computer','Human Brain','Ant Colony','Volcano','Tsunami',
 'Diamond','Graphene Sheet','Lightning Bolt','Hurricane','Glacier','Black Hole (stellar)','Sun','Neutron Star',
 'Great Pyramid','Burj Khalifa','Hoover Dam','Internet Backbone','GPS Constellation','International Space Station',
 'Printing Press','Steam Engine','Transistor','Laser'];
function powerOf(name,rnd){var h=0;for(var i=0;i<name.length;i++){h=(h*31+name.charCodeAt(i))|0;}
 return 40+(((h^(h>>>13))*2654435761>>>0)%61)+rnd()*4;}
function runBracket(names,rnd){
 var round=names.slice(),rounds=[],rnum=1;
 while(round.length>1){var next=[],matches=[];
  for(var i=0;i<round.length;i+=2){var a=round[i],b=round[i+1];
   var pa=powerOf(a,rnd),pb=powerOf(b,rnd);
   var w=pa>=pb?a:b;
   matches.push({a:a,b:b,pa:+pa.toFixed(1),pb:+pb.toFixed(1),winner:w});next.push(w);}
  rounds.push({round:rnum,matches:matches});round=next;rnum++;}
 return {rounds:rounds,champion:round[0]};
}
function demoProgram(topic,field,bracket){
  var L=['# '+topic,'# Field: '+field,'# bracket simulation - deterministic from the seed','',
   'def power(name):','    h=0','    for ch in name: h=(h*31+ord(ch))&0xFFFFFFFF',
   '    return 40+(h%61)',''];
  bracket.rounds.forEach(function(r,ri){L.push('print("round '+(ri+1)+'")');
   r.matches.forEach(function(m){L.push('print("  '+m.a+' ('+m.pa+') vs '+m.b+' ('+m.pb+') -> '+m.winner+'")');});});
  L.push('print("CHAMPION: '+bracket.champion+'")');L.push('print("OK: bracket simulated")');
  return L.join('\n')+'\n';
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var eight=shuffle(CONTENDERS,rnd).slice(0,8);
  var bracket=runBracket(eight,rnd);
  var topic='Ultimate Showdown: '+eight.join(' vs ');
  var id=PREFIX+String(seed).padStart(6,'0');
  return {id:id,name:'Showdown bracket - '+bracket.champion+' crowned',title:topic,
   description:'GENERATED TOURNAMENT. Eight contenders enter, one champion leaves: '
    +eight.join(', ')+'. Simulated across '+bracket.rounds.length+' rounds on transparent '
    +'power ratings. Champion: '+bracket.champion+'.',
   field:field,contenders:eight,rounds:bracket.rounds,champion:bracket.champion,
   src:'signature-generated',sample:true,
   disclaimer:'Generated bracket - not an archive record.',
   demo:{kind:'showdown-bracket-demo',language:'python',
    program:demoProgram('Showdown bracket',field,bracket),note:'Runnable replay of this exact bracket.'},
   _seed:seed};
}
function validate(r){var e=[];
 if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
 if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
 if(FIELDS.indexOf(r.field)<0)e.push('field');
 if(!r.champion)e.push('champion');
 if(!r.demo||!r.demo.program)e.push('demo');
 return{ok:!e.length,errors:e};}
function driftCheck(record,sample){var dups=(sample||[]).filter(function(r){return r&&r.champion===record.champion&&String(r.contenders)===String(record.contenders);});
 return dups.length?{ok:false,errors:['identical bracket in archive sample']}:{ok:true,errors:[]};}
var gen={version:"jahdb-gen-ultimate-showdown-generator-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:["Sample Brackets", "How It Judges"]};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("gen-ultimate-showdown-generator",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
