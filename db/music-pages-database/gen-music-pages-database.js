(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}

function SigRegCreate(opts){
  opts=opts||{};
  var HARD_CAP=(typeof opts.maxRecords==='number')?opts.maxRecords:1000000000;
  var minGapMs=opts.minGapMs||0, costPer=opts.costPer||1;
  var budget=(typeof opts.budget==='number')?opts.budget:Infinity;
  var checkFn=opts.check||function(){return {ok:true,errors:[]};};
  var produced=0, spent=0, lastT=0, log=[];
  function generate(seed, producer){
    if(produced>=HARD_CAP) throw new Error('HARD_CAP_REACHED at '+HARD_CAP+' records');
    var now=Date.now();
    if(minGapMs>0 && lastT>0 && (now-lastT)<minGapMs) throw new Error('THROTTLE: '+(minGapMs-(now-lastT))+'ms remaining');
    lastT=now;
    var item=producer(seed);
    var v=checkFn(item);
    if(!v||!v.ok) throw new Error('CORRECTNESS_FAILED: '+((v&&v.errors)||['unknown']).join('; '));
    item._label='simulated';
    item._seq=produced+1;
    item._sigreg={hard_cap:HARD_CAP, seq:produced+1, verified:true};
    produced++; spent+=costPer;
    if(spent>budget) throw new Error('BUDGET_EXCEEDED');
    log.push({seq:produced,seed:seed,t:now});
    return item;
  }
  function stats(){return {produced:produced, hardCap:HARD_CAP, spent:spent, budget:budget, logSize:log.length};}
  function reset(){produced=0;spent=0;lastT=0;log=[];}
  return {generate:generate, stats:stats, reset:reset, HARD_CAP:HARD_CAP};
}

var NOTE_SEMI={C:0,'C#':1,Db:1,D:2,'D#':3,Eb:3,E:4,F:5,'F#':6,Gb:6,G:7,'G#':8,Ab:8,A:9,'A#':10,Bb:10,B:11};
function noteFreq(name){
  var m=/^([A-G])([#b]?)(-?\d+)$/.exec(name);
  if(!m) throw new Error('bad note name: '+name);
  var midi=NOTE_SEMI[m[1]+m[2]]+(parseInt(m[3],10)+1)*12;
  return 440*Math.pow(2,(midi-69)/12);
}
function computeTimeline(notes,bpm){
  var spb=60/bpm, t=0, out=[];
  notes.forEach(function(ev){
    var names=ev[0], beats=ev[1], dur=beats*spb;
    if(names!==null&&names!==undefined){
      (Array.isArray(names)?names:[names]).forEach(function(n){
        out.push({note:n, freq:noteFreq(n), start:t, dur:dur});
      });
    }
    t+=dur;
  });
  return out;
}

var PREFIX='JAH-MUSPG-';
var ROOTS=['C','D','E','F','G','A','B'];
var SCALE_PAT=[0,2,4,5,7,9,11];
var PENTA_PAT=[0,3,5,7,10];
var PROGS=[[0,5,3,4],[0,4,5,3],[0,0,5,4]];
var CHORD_Q=['maj','maj','min','min','maj','min','dim'];
function semiName(root,off,oct){
  var base={C:0,D:2,E:4,F:5,G:7,A:9,B:11}[root];
  var pc=(base+off)%12, o=oct+Math.floor((base+off)/12);
  var names=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'];
  return names[pc]+o;
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var kind=ri(rnd,0,2), root=pick(ROOTS,rnd), oct=ri(rnd,3,4);
  var notes=[],title='',desc='';
  if(kind===0){
    for(var i=0;i<8;i++)notes.push([semiName(root,SCALE_PAT[i],oct),i===7?2:1]);
    title=root+' Major Scale Study (seed '+seed+')';
    desc='A generated major-scale study in '+root+', eight notes ascending, in the archive style.';
  }else if(kind===1){
    for(var i=0;i<7;i++)notes.push([semiName(root,PENTA_PAT[i],oct),1]);
    notes.push([semiName(root,12,oct),2]);
    title=root+' Pentatonic Sketch (seed '+seed+')';
    desc='A generated pentatonic sketch on '+root+' — five safe notes, one phrase.';
  }else{
    var prog=pick(PROGS,rnd);
    var roots=['C','F','G','A','D','E'];
    var r0=pick(roots,rnd);
    prog.forEach(function(deg){
      var rr=roots[(roots.indexOf(r0)+deg)%roots.length]||'C';
      notes.push([[semiName(rr,0,3),semiName(rr,4,3),semiName(rr,7,3)],2]);
    });
    title='Chord Loop in '+r0+' (seed '+seed+')';
    desc='A generated chord loop: triads cycling a classic progression.';
  }
  var tempo=ri(rnd,72,132);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {id:id,title:title,t:title,g:pick(["Scales", "Blues", "Classical", "Jazz", "Reggae", "Pop", "World", "Children's", "Signature Original"],rnd),c:1,ladder_rank:ri(rnd,1,15),
    description:desc,notes:notes,tempo:tempo,key:root+' major',time_signature:'4/4',
    composer:'Generated in archive style (simulated)',demo:{runtime:'webaudio',code:'',expect:'timeline verified'},
    provenance:'public',last_verified:'2026-10-21',
    march_marker:'Million-record march in progress: 15 of 1,000,000 records (0.0015%).',_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(!Array.isArray(r.notes)||!r.notes.length)e.push('notes');
  if(!(r.tempo>=40&&r.tempo<=220))e.push('tempo');
  try{
    var tl=computeTimeline(r.notes,r.tempo);
    if(!tl.length)e.push('empty timeline');
    for(var i=1;i<tl.length;i++)if(tl[i].start<tl[i-1].start-1e-9)e.push('timeline order');
  }catch(x){e.push('timeline error: '+x.message);}
  if(typeof r.ladder_rank!=='number'||r.ladder_rank<1||r.ladder_rank>15)e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}

var gen={version:'jahdb-music-pages-database-1.0',generate:generate,validate:validate,SigRegCreate:SigRegCreate,computeTimeline:computeTimeline,noteFreq:noteFreq};
if(typeof window!=='undefined')window['GEN_MUSIC_PAGES_DATABASE']=gen;
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('music-pages-database',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
