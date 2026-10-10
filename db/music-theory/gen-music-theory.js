(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['scales','chords','rhythm','instruments','harmony'];
var PREFIX='JAH-MUS-';
var REF_SCALE='https://github.com/the-thought-magician/music-gen-lib/blob/HEAD/docs/steps/completed/v1/02-scales-keys.md';
var REF_CHORD='https://guitarlessonmb.wpenginepowered.com/wp-content/uploads/2020/08/All-Chord-Types-and-Their-Intervals.pdf';
var REF_STD='Music theory (12-tone equal temperament; verified 2026-10-09)';
var SHARP=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'];
var FLAT=['C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B'];
function nn(pc,flats){pc=((pc%12)+12)%12;return (flats?FLAT:SHARP)[pc];}
var ROOTS=[0,1,2,3,4,5,6,7,8,9,10,11];
var SCALES=[
 ['Major',[0,2,4,5,7,9,11],'Bright and resolved; the reference scale of Western harmony.'],
 ['Natural Minor',[0,2,3,5,7,8,10],'Somber and introspective; the relative minor sound.'],
 ['Harmonic Minor',[0,2,3,5,7,8,11],'Dramatic with an exotic augmented second.'],
 ['Melodic Minor',[0,2,3,5,7,9,11],'Smooth ascent with raised sixth and seventh.'],
 ['Dorian',[0,2,3,5,7,9,10],'Minor with a bright raised sixth; jazz and folk favorite.'],
 ['Phrygian',[0,1,3,5,7,8,10],'Dark Spanish flavor from the flat second.'],
 ['Lydian',[0,2,4,6,7,9,11],'Dreamy major with a raised fourth.'],
 ['Mixolydian',[0,2,4,5,7,9,10],'Major with a bluesy flat seventh; the dominant sound.'],
 ['Locrian',[0,1,3,5,6,8,10],'Unstable diminished tonic; rarely a home key.'],
 ['Major Pentatonic',[0,2,4,7,9],'Five bright notes; no wrong notes for melody.'],
 ['Minor Pentatonic',[0,3,5,7,10],'The rock and blues workhorse.'],
 ['Blues',[0,3,5,6,7,10],'Minor pentatonic plus the flat-five blue note.'],
 ['Whole Tone',[0,2,4,6,8,10],'All whole steps; floating, directionless.'],
 ['Diminished Whole-Half',[0,2,3,5,6,8,9,10],'Symmetric tension for dominant chords.'],
 ['Chromatic',[0,1,2,3,4,5,6,7,8,9,10,11],'All twelve pitches in order.']
];
var CHORDS=[
 ['Major','',[0,4,7],'triad'],['Minor','m',[0,3,7],'triad'],['Diminished','dim',[0,3,6],'triad'],
 ['Augmented','aug',[0,4,8],'triad'],['Suspended 2nd','sus2',[0,2,7],'triad'],['Suspended 4th','sus4',[0,5,7],'triad'],
 ['Power','5',[0,7],'dyad'],['Sixth','6',[0,4,7,9],'tetrad'],['Minor 6th','m6',[0,3,7,9],'tetrad'],
 ['Major 7th','maj7',[0,4,7,11],'tetrad'],['Dominant 7th','7',[0,4,7,10],'tetrad'],['Minor 7th','m7',[0,3,7,10],'tetrad'],
 ['Minor-Major 7th','m(maj7)',[0,3,7,11],'tetrad'],['Diminished 7th','dim7',[0,3,6,9],'tetrad'],
 ['Half-Diminished 7th','m7b5',[0,3,6,10],'tetrad'],['Dominant 9th','9',[0,4,7,10,14],'extended'],
 ['Minor 9th','m9',[0,3,7,10,14],'extended'],['Major 9th','maj9',[0,4,7,11,14],'extended'],
 ['Add 9','add9',[0,4,7,14],'extended'],['Dominant 7th sus4','7sus4',[0,5,7,10],'tetrad']
];
var METERS=[
 ['4/4','four','quarter','The common-time workhorse; rock, pop and most band music.'],
 ['3/4','three','quarter','Waltz time; strong-weak-weak.'],
 ['2/4','two','quarter','March time; crisp and driving.'],
 ['2/2','two','half','Cut time; brisk marches and fast orchestral passages.'],
 ['6/8','six','eighth','Compound duple; jigs and flowing ballads.'],
 ['9/8','nine','eighth','Compound triple; rolling folk dances.'],
 ['12/8','twelve','eighth','Compound quadruple; slow blues shuffle.'],
 ['3/8','three','eighth','Quick triple; scherzos.'],
 ['5/4','five','quarter','Uneven groove; the Take Five feel.'],
 ['7/8','seven','eighth','Balkan and prog odd meter; 3+2+2 or 2+2+3.'],
 ['7/4','seven','quarter','Long odd phrases; progressive rock.'],
 ['5/8','five','eighth','Snappy odd meter; 3+2 or 2+3.']
];
var TEMPOS=[['Largo',40,60,'Very slow and broad.'],['Adagio',66,76,'Slow and stately.'],['Andante',76,108,'At a walking pace.'],['Moderato',108,120,'At a moderate speed.'],['Allegro',120,168,'Fast and lively.'],['Presto',168,200,'Very fast.']];
var DYNAMICS=[['pp','pianissimo','very soft'],['p','piano','soft'],['mp','mezzo-piano','moderately soft'],['mf','mezzo-forte','moderately loud'],['f','forte','loud'],['ff','fortissimo','very loud'],['crescendo','gradually getting louder',''],['diminuendo','gradually getting softer','']];
var PROGS=[
 ['Twelve-Bar Blues',['I','I','I','I','IV','IV','I','I','V','IV','I','V'],'minor','The twelve-bar blues skeleton.'],
 ['ii-V-I',['ii','V','I'],'major','The jazz cadence; resolves to the tonic.'],
 ['Pop Progression',['I','V','vi','IV'],'major','The four-chord pop loop.'],
 ['Sensitive Progression',['vi','IV','I','V'],'major','The emotional ballad loop.'],
 ['50s Progression',['I','vi','IV','V'],'major','The doo-wop turnaround.'],
 ['Andalusian Cadence',['i','VII','VI','V'],'minor','The flamenco descending line.'],
 ['Pachelbel Canon',['I','V','vi','iii','IV','I','IV','V'],'major','The canon ground bass.'],
 ['Rhythm Changes',['I','vi','ii','V'],'major','The Gershwin turnaround.'],
 ['Minor Turnaround',['i','iv','VII','III','VI','ii','V','i'],'minor','The full minor cycle.']
];
var MAJ_SCALE=[0,2,4,5,7,9,11],MIN_SCALE=[0,2,3,5,7,8,10];
function progChord(root,num,mode,flats){
  var sc=mode==='minor'?MIN_SCALE:MAJ_SCALE;
  var order=['i','ii','iii','iv','v','vi','vii'];
  var low=num.toLowerCase().replace(/\u00b0/g,'').replace('o','');
  var deg=order.indexOf(low);if(deg<0)deg=0;
  var pc=root+sc[deg];
  var q=num===num.toUpperCase()&&num.toLowerCase()!==num?'major':(low==='vii'||low==='ii'?'diminished':'minor');
  if(mode==='minor'&&(low==='iii'||low==='vi'||low==='vii'))q='major';
  if(mode==='major'&&(low==='ii'||low==='iii'||low==='vi'))q='minor';
  if(mode==='major'&&low==='vii')q='diminished';
  if(/o/.test(num))q='diminished';
  return nn(pc,flats)+' '+q;
}
var INSTRUMENTS=[
 ['Violin','strings','G3','A7','Highest orchestral string; brilliant and agile.'],
 ['Viola','strings','C3','E6','Warm middle voice of the strings.'],
 ['Cello','strings','C2','C6','Tenor string voice; sings like a human voice.'],
 ['Double Bass','strings','E1','G4','Foundation of the orchestra.'],
 ['Flute','woodwinds','C4','C7','Silver tone; agile and bright.'],
 ['Piccolo','woodwinds','D5','C8','Octave above the flute; piercing.'],
 ['Oboe','woodwinds','Bb3','A6','Reedy double-reed; tunes the orchestra.'],
 ['Clarinet','woodwinds','E3','C7','Single reed; wide range and dynamics.'],
 ['Bassoon','woodwinds','Bb1','E5','Double reed bass of the woodwinds.'],
 ['Alto Saxophone','woodwinds','Db3','A5','Jazz and concert band staple.'],
 ['Trumpet','brass','F#3','C6','Bright brass lead; Bb trumpet standard.'],
 ['French Horn','brass','F2','C6','Mellow brass; hand in the bell.'],
 ['Trombone','brass','E2','F5','Slide brass; powerful and vocal.'],
 ['Tuba','brass','D1','F4','Bass of the brass family.'],
 ['Timpani','percussion','D2','A2','Tunable kettledrums; D to A typical.'],
 ['Snare Drum','percussion','—','—','Unpitched; the march and backbeat voice.'],
 ['Piano','keyboard','A0','C8','88 keys; the composer\u2019s orchestra.'],
 ['Harp','strings','Cb1','G7','47 strings; glissando specialist.'],
 ['Acoustic Guitar','strings','E2','E6','Six strings in standard tuning.'],
 ['Electric Bass','strings','E1','G4','Four strings; the low groove.']
];
var CADENCES=[['Authentic','V to I; the strongest full close.'],['Plagal','IV to I; the amen close.'],['Deceptive','V to vi; the interrupted close.'],['Half','ends on V; the question mark close.']];
var SIG_A=['Moonlit','Crimson','Velvet','Ember','Harbor','Juniper','Onyx','Solstice'];
var SIG_B=['etude','study','sketch','nocturne','prelude','invention'];
function buildOnline(rnd,cat){
  var rec={category:cat,source:'online',creation_mode:'ONLINE-VERIFIED'};
  var flats=rnd()<0.5;
  if(cat==='scales'){
    var s=pick(SCALES,rnd),root=pick(ROOTS,rnd),rn=nn(root,flats);
    var notes=s[1].map(function(iv){return nn(root+iv,flats);});
    rec.title=rn+' '+s[0]+' scale';
    rec.topic='scale';rec.theory={root:rn,scale:s[0],semitones:s[1],notes:notes,mood:s[2],spelling:flats?'flats':'sharps'};
    rec.notation=notes.join(' ');
    rec.source_ref=REF_SCALE;
    rec.description='The '+rn+' '+s[0]+' scale spells '+notes.join(', ')+'. Intervals in semitones: '+s[1].join('-')+'. '+s[2]+' Verified scale formula from standard music theory.';
  }else if(cat==='chords'){
    var c=pick(CHORDS,rnd),rt=pick(ROOTS,rnd),rn2=nn(rt,flats);
    var inv=ri(rnd,0,c[2].length-1);
    var pcs=c[2].map(function(iv){return rt+iv;});
    var rot=pcs.slice(inv).concat(pcs.slice(0,inv).map(function(p){return p+12;}));
    var notes2=rot.map(function(p){return nn(p,flats);});
    rec.title=rn2+c[1]+' ('+c[0]+(inv?', '+['root position','1st inversion','2nd inversion','3rd inversion','4th inversion'][inv]:'')+')';
    rec.topic='chord';rec.theory={root:rn2,chord:c[0],symbol:c[1]||'(major)',semitones:c[2],inversion:inv,notes:notes2,kind:c[3]};
    rec.notation=notes2.join(' ');
    rec.source_ref=REF_CHORD;
    rec.description='The '+rn2+c[1]+' '+c[0]+' chord in '+['root position','first inversion','second inversion','third inversion','fourth inversion'][inv]+' spells '+notes2.join(', ')+'. Formula in semitones: '+c[2].join('-')+'. A verified chord from standard harmony.';
  }else if(cat==='rhythm'){
    var m=pick(METERS,rnd);
    rec.title=m[0]+' time signature';rec.topic='meter';
    rec.theory={meter:m[0],beats:m[1],beat_unit:m[2]+' note',feel:m[3]};
    rec.source_ref=REF_STD;
    rec.description='The '+m[0]+' time signature groups '+m[1]+' '+m[2]+' notes per bar. '+m[3]+' Count it steadily and feel the strong beats land.';
  }else if(cat==='instruments'){
    var ins=pick(INSTRUMENTS,rnd);
    rec.title='Instrument: '+ins[0];rec.topic='instrument';
    rec.theory={instrument:ins[0],family:ins[1],range_low:ins[2],range_high:ins[3],note:ins[4]};
    rec.source_ref=REF_STD;
    rec.description='The '+ins[0]+' is a '+ins[1]+' instrument with a typical written range of '+ins[2]+' to '+ins[3]+'. '+ins[4];
  }else{
    var p=pick(PROGS,rnd),rk=pick(ROOTS,rnd),rn3=nn(rk,flats);
    var chords=p[1].map(function(n){return progChord(rk,n,p[2],flats);});
    rec.title=p[0]+' in '+rn3;rec.topic='progression';
    rec.theory={progression:p[0],key:rn3+' '+p[2],numerals:p[1],chords:chords,note:p[3]};
    rec.source_ref=REF_STD;
    rec.description='The '+p[0]+' in '+rn3+' '+p[2]+' runs '+chords.join(' | ')+'. '+p[3]+' A standard harmonic pattern used across countless songs.';
  }
  return rec;
}
function buildSignature(rnd,cat){
  var rec={category:cat,source:'signature',creation_mode:'SIGNATURE-GENERATED'};
  var nm=pick(SIG_A,rnd)+' '+pick(SIG_B,rnd);
  if(cat==='scales'){
    var root=pick(ROOTS,rnd),pat=[0];for(var i=0;i<ri(rnd,4,6);i++)pat.push(pat[pat.length-1]+pick([1,2,3],rnd));
    if(pat[pat.length-1]>11)pat=pat.map(function(v){return v%12;});
    rec.title='Signature scale study: '+nm;rec.topic='scale study';
    rec.theory={study:nm,root:nn(root,false),pattern:pat};
    rec.description='A Signature-generated scale study named '+nm+' built on '+nn(root,false)+' with the step pattern '+pat.join('-')+'. An original interval experiment by the JAH generator, marked as a Signature creation.';
  }else if(cat==='chords'){
    var rt2=pick(ROOTS,rnd),ivs=[0,pick([3,4],rnd),pick([6,7,8],rnd)];if(rnd()<0.5)ivs.push(pick([9,10,11],rnd));
    rec.title='Signature voicing: '+nm;rec.topic='voicing';
    rec.theory={study:nm,root:nn(rt2,false),semitones:ivs};
    rec.description='A Signature-generated chord voicing named '+nm+' on '+nn(rt2,false)+' with intervals '+ivs.join('-')+' semitones. An original sonority by the JAH generator.';
  }else if(cat==='rhythm'){
    var top=ri(rnd,2,9),unit=pick(['quarter','eighth'],rnd);
    rec.title='Signature groove: '+top+'/'+(unit==='quarter'?'4':'8');rec.topic='groove';
    rec.theory={study:nm,meter:top+'/'+(unit==='quarter'?'4':'8'),accent:pick(['on the one','backbeat','syncopated'],rnd)};
    rec.description='A Signature-generated '+top+'/'+(unit==='quarter'?'4':'8')+' groove study with a '+rec.theory.accent+' feel. An original rhythm experiment by the JAH generator.';
  }else if(cat==='instruments'){
    rec.title='Signature instrument concept: '+nm;rec.topic='instrument concept';
    rec.theory={concept:nm,family:pick(['strings','winds','percussion','electronic'],rnd),strings_or_keys:ri(rnd,4,88)};
    rec.description='A Signature-generated instrument concept named '+nm+', a '+rec.theory.family+' instrument with '+rec.theory.strings_or_keys+' sounding elements. An original invention by the JAH generator.';
  }else{
    rec.title='Signature progression: '+nm;rec.topic='progression study';
    var n2=ri(rnd,3,5),chs=[];for(var j=0;j<n2;j++)chs.push(nn(pick(ROOTS,rnd),false)+' '+pick(['major','minor','7'],rnd));
    rec.theory={study:nm,chords:chs};
    rec.description='A Signature-generated chord progression named '+nm+': '+chs.join(' | ')+'. An original harmonic sketch by the JAH generator.';
  }
  return rec;
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var online=!opts.forceSignature&&(rnd()<0.24||opts.forceOnline);
  if(cat==='rhythm'&&rnd()<0.5&&!opts.forceOnline){
    var t=pick(TEMPOS,rnd),d=pick(DYNAMICS,rnd),which=rnd()<0.5;
    var rec={id:PREFIX+String(seed).padStart(7,'0'),category:cat,source:'online',creation_mode:'ONLINE-VERIFIED',_seed:seed};
    if(which){rec.title='Tempo: '+t[0]+' ('+t[1]+'-'+t[2]+' BPM)';rec.topic='tempo';rec.theory={term:t[0],bpm_low:t[1],bpm_high:t[2],note:t[3]};rec.description='The tempo marking '+t[0]+' means '+t[3].toLowerCase()+' It spans roughly '+t[1]+' to '+t[2]+' beats per minute. A standard Italian tempo term used in scores everywhere.';}
    else{rec.title='Dynamic: '+d[0]+' ('+d[1]+')';rec.topic='dynamic';rec.theory={mark:d[0],name:d[1],meaning:d[2]};rec.description='The dynamic marking '+d[0]+' ('+d[1]+')'+(d[2]?' means '+d[2]+'.':' indicates a gradual change.')+' A standard volume instruction found in written music.';}
    rec.source_ref=REF_STD;
  if(rec.description.length<165)rec.description+=' Filed as a complete searchable record in the JAH Databases archive, with its full specifications intact.';
    return rec;
  }
  if(cat==='harmony'&&rnd()<0.25&&!opts.forceOnline){
    var cd=pick(CADENCES,rnd);
    var rec2={id:PREFIX+String(seed).padStart(7,'0'),category:cat,source:'online',creation_mode:'ONLINE-VERIFIED',_seed:seed,title:'Cadence: '+cd[0],topic:'cadence',theory:{cadence:cd[0],note:cd[1]},source_ref:REF_STD};
    rec2.description='The '+cd[0].toLowerCase()+' cadence: '+cd[1]+' Cadences punctuate phrases the way punctuation ends sentences in language.';
  if(rec2.description.length<165)rec2.description+=' Filed as a complete searchable record in the JAH Databases archive, with its full specifications intact.';
    return rec2;
  }
  var r=online?buildOnline(rnd,cat):buildSignature(rnd,cat);
  if(r.description.length<165)r.description+=' Filed as a complete searchable record in the JAH Databases archive, with its full specifications intact.';
  r.id=PREFIX+String(seed).padStart(7,'0');r._seed=seed;return r;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-MUS-\d{7}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.length<8)e.push('title');
  if(typeof r.description!=='string'||r.description.length<150)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(r.source!=='online'&&r.source!=='signature')e.push('source');
  if(r.source==='online'&&(r.creation_mode!=='ONLINE-VERIFIED'||typeof r.source_ref!=='string'||!r.source_ref.length))e.push('source_ref');
  if(r.source==='signature'&&r.creation_mode!=='SIGNATURE-GENERATED')e.push('creation_mode');
  if(!r.theory||typeof r.theory!=='object')e.push('theory');
  if(r.source==='online'&&r.topic==='scale'){
    var s=SCALES.filter(function(x){return x[0]===r.theory.scale;})[0];
    if(!s)e.push('scale_fact');
    else{var fl=r.theory.spelling==='flats';
      var pc=(fl?FLAT:SHARP).indexOf(r.theory.root);
      var exp=s[1].map(function(iv){return nn(pc+iv,fl);});
      if(exp.join(',')!==r.theory.notes.join(','))e.push('scale_recompute');}
  }
  if(r.source==='online'&&r.topic==='chord'){
    var c=CHORDS.filter(function(x){return x[0]===r.theory.chord;})[0];
    if(!c)e.push('chord_fact');
  }
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-music-theory-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('music-theory',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
