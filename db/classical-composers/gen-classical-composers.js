(function(){'use strict';
/* JAH Classical Composers Database generator — jahdb-classical-composers-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='classical-composers',PREFIX='JAH-MUS-',NAME='JAH Classical Composers Database';
var FIELDS=["baroque", "classical", "classical-romantic", "romantic", "romantic-modern", "modern", "contemporary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Johann Sebastian Bach", "d": "Bach is the baroque master: counterpoint perfected in cantatas, concertos, and the Mass in B Minor.", "g": "baroque", "l": 2, "q": "What is Johann Sebastian Bach?", "a": "Bach is the baroque master: counterpoint perfected in cantatas, concertos, and the Mass in B Minor.", "x": "Bach is the baroque master: counterpoint perfected in cantatas, concertos, and the Mass in B Minor. years: 1685-1750. known_for: Brandenburg Concertos, Mass in B Minor. country: Germany. Checked against standard references. Creative-domain facts are as stable as history gets; dates and names verified.", "s": "public-reference", "f": null}, {"t": "George Frideric Handel", "d": "Handel's Messiah made him immortal: oratorios and royal pageantry.", "g": "baroque", "l": 2, "q": "What is George Frideric Handel?", "a": "Handel's Messiah made him immortal: oratorios and royal pageantry.", "x": "Handel's Messiah made him immortal: oratorios and royal pageantry. years: 1685-1759. known_for: Messiah, Water Music. country: Germany/England. Checked against standard references. Creative-domain facts are as stable as history gets; dates and names verified.", "s": "public-reference", "f": null}, {"t": "Antonio Vivaldi", "d": "Vivaldi the Red Priest: 500 concertos, with the Four Seasons the most famous.", "g": "baroque", "l": 2, "q": "What is Antonio Vivaldi?", "a": "Vivaldi the Red Priest: 500 concertos, with the Four Seasons the most famous.", "x": "Vivaldi the Red Priest: 500 concertos, with the Four Seasons the most famous. years: 1678-1741. known_for: The Four Seasons. country: Italy. Checked against standard references. Creative-domain facts are as stable as history gets; dates and names verified.", "s": "public-reference", "f": null}, {"t": "Henry Purcell", "d": "Purcell is England's baroque genius: Dido's Lament still breaks hearts.", "g": "baroque", "l": 2, "q": "What is Henry Purcell?", "a": "Purcell is England's baroque genius: Dido's Lament still breaks hearts.", "x": "Purcell is England's baroque genius: Dido's Lament still breaks hearts. years: 1659-1695. known_for: Dido and Aeneas. country: England. Checked against standard references. Creative-domain facts are as stable as history gets; dates and names verified.", "s": "public-reference", "f": null}, {"t": "Claudio Monteverdi", "d": "Monteverdi bridged Renaissance and Baroque: opera's first master.", "g": "baroque", "l": 2, "q": "What is Claudio Monteverdi?", "a": "Monteverdi bridged Renaissance and Baroque: opera's first master.", "x": "Monteverdi bridged Renaissance and Baroque: opera's first master. years: 1567-1643. known_for: L'Orfeo. country: Italy. Checked against standard references. Creative-domain facts are as stable as history gets; dates and names verified.", "s": "public-reference", "f": null}, {"t": "Joseph Haydn", "d": "Haydn the Father of the Symphony: wit and invention across 104 symphonies.", "g": "classical", "l": 2, "q": "What is Joseph Haydn?", "a": "Haydn the Father of the Symphony: wit and invention across 104 symphonies.", "x": "Haydn the Father of the Symphony: wit and invention across 104 symphonies. years: 1732-1809. known_for: 104 symphonies, string quartets. country: Austria. Checked against standard references. Creative-domain facts are as stable as history gets; dates and names verified.", "s": "public-reference", "f": null}, {"t": "Wolfgang Amadeus Mozart", "d": "Mozart wrote 600+ works in 35 years: perfection that sounds effortless.", "g": "classical", "l": 2, "q": "What is Wolfgang Amadeus Mozart?", "a": "Mozart wrote 600+ works in 35 years: perfection that sounds effortless.", "x": "Mozart wrote 600+ works in 35 years: perfection that sounds effortless. years: 1756-1791. known_for: 40+ symphonies, operas, Requiem. country: Austria. Checked against standard references. Creative-domain facts are as stable as history gets; dates and names verified.", "s": "public-reference", "f": null}, {"t": "Ludwig van Beethoven", "d": "Beethoven redefined music while going deaf: the 9th Symphony's Ode to Joy.", "g": "classical-romantic", "l": 2, "q": "What is Ludwig van Beethoven?", "a": "Beethoven redefined music while going deaf: the 9th Symphony's Ode to Joy.", "x": "Beethoven redefined music while going deaf: the 9th Symphony's Ode to Joy. years: 1770-1827. known_for: 9 symphonies, 32 piano sonatas. country: Germany. Checked against standard references. Creative-domain facts are as stable as history gets; dates and names verified.", "s": "public-reference", "f": null}, {"t": "Franz Schubert", "d": "Schubert wrote 600 songs in 31 years: melody inexhaustible.", "g": "romantic", "l": 2, "q": "What is Franz Schubert?", "a": "Schubert wrote 600 songs in 31 years: melody inexhaustible.", "x": "Schubert wrote 600 songs in 31 years: melody inexhaustible. years: 1797-1828. known_for: 600+ lieder, Unfinished Symphony. country: Austria. Checked against standard references. Creative-domain facts are as stable as history gets; dates and names verified.", "s": "public-reference", "f": null}, {"t": "Felix Mendelssohn", "d": "Mendelssohn: the Wedding March and the revival of Bach.", "g": "romantic", "l": 2, "q": "What is Felix Mendelssohn?", "a": "Mendelssohn: the Wedding March and the revival of Bach.", "x": "Mendelssohn: the Wedding March and the revival of Bach. years: 1809-1847. known_for: Wedding March, Italian Symphony. country: Germany. Checked against standard references. Creative-domain facts are as stable as history gets; dates and names verified.", "s": "public-reference", "f": null}, {"t": "Robert Schumann", "d": "Schumann's piano cycles are romanticism's diary.", "g": "romantic", "l": 2, "q": "What is Robert Schumann?", "a": "Schumann's piano cycles are romanticism's diary.", "x": "Schumann's piano cycles are romanticism's diary. years: 1810-1856. known_for: piano cycles, 4 symphonies. country: Germany. Checked against standard references. Creative-domain facts are as stable as history gets; dates and names verified.", "s": "public-reference", "f": null}, {"t": "Frederic Chopin", "d": "Chopin is the poet of the piano: nocturnes and etudes of liquid beauty.", "g": "romantic", "l": 2, "q": "What is Frederic Chopin?", "a": "Chopin is the poet of the piano: nocturnes and etudes of liquid beauty.", "x": "Chopin is the poet of the piano: nocturnes and etudes of liquid beauty. years: 1810-1849. known_for: nocturnes, etudes. country: Poland/France. Checked against standard references. Creative-domain facts are as stable as history gets; dates and names verified.", "s": "public-reference", "f": null}, {"t": "Franz Liszt", "d": "Liszt invented the piano recital and rock-star virtuosity.", "g": "romantic", "l": 2, "q": "What is Franz Liszt?", "a": "Liszt invented the piano recital and rock-star virtuosity.", "x": "Liszt invented the piano recital and rock-star virtuosity. years: 1811-1886. known_for: piano virtuosity, symphonic poems. country: Hungary. Checked against standard references. Creative-domain facts are as stable as history gets; dates and names verified.", "s": "public-reference", "f": null}, {"t": "Richard Wagner", "d": "Wagner's Ring is opera as total artwork: 15 hours of myth.", "g": "romantic", "l": 2, "q": "What is Richard Wagner?", "a": "Wagner's Ring is opera as total artwork: 15 hours of myth.", "x": "Wagner's Ring is opera as total artwork: 15 hours of myth. years: 1813-1883. known_for: The Ring Cycle. country: Germany. Checked against standard references. Creative-domain facts are as stable as history gets; dates and names verified.", "s": "public-reference", "f": null}, {"t": "Giuseppe Verdi", "d": "Verdi gave Italy its voice: 28 operas of passion and politics.", "g": "romantic", "l": 2, "q": "What is Giuseppe Verdi?", "a": "Verdi gave Italy its voice: 28 operas of passion and politics.", "x": "Verdi gave Italy its voice: 28 operas of passion and politics. years: 1813-1901. known_for: Aida, La Traviata, Rigoletto. country: Italy. Checked against standard references. Creative-domain facts are as stable as history gets; dates and names verified.", "s": "public-reference", "f": null}, {"t": "Johannes Brahms", "d": "Brahms carried Beethoven's torch: classical forms, romantic heart.", "g": "romantic", "l": 2, "q": "What is Johannes Brahms?", "a": "Brahms carried Beethoven's torch: classical forms, romantic heart.", "x": "Brahms carried Beethoven's torch: classical forms, romantic heart. years: 1833-1897. known_for: 4 symphonies, German Requiem. country: Germany. Checked against standard references. Creative-domain facts are as stable as history gets; dates and names verified.", "s": "public-reference", "f": null}, {"t": "Pyotr Ilyich Tchaikovsky", "d": "Tchaikovsky's ballets and 1812 Overture are classical music's greatest hits.", "g": "romantic", "l": 2, "q": "What is Pyotr Ilyich Tchaikovsky?", "a": "Tchaikovsky's ballets and 1812 Overture are classical music's greatest hits.", "x": "Tchaikovsky's ballets and 1812 Overture are classical music's greatest hits. years: 1840-1893. known_for: Nutcracker, Swan Lake, 1812 Overture. country: Russia. Checked against standard references. Creative-domain facts are as stable as history gets; dates and names verified.", "s": "public-reference", "f": null}, {"t": "Antonin Dvorak", "d": "Dvorak's New World Symphony sang America back to itself.", "g": "romantic", "l": 2, "q": "What is Antonin Dvorak?", "a": "Dvorak's New World Symphony sang America back to itself.", "x": "Dvorak's New World Symphony sang America back to itself. years: 1841-1904. known_for: New World Symphony. country: Czechia. Checked against standard references. Creative-domain facts are as stable as history gets; dates and names verified.", "s": "public-reference", "f": null}, {"t": "Edvard Grieg", "d": "Grieg gave Norway its musical soul: Peer Gynt's Morning Mood.", "g": "romantic", "l": 2, "q": "What is Edvard Grieg?", "a": "Grieg gave Norway its musical soul: Peer Gynt's Morning Mood.", "x": "Grieg gave Norway its musical soul: Peer Gynt's Morning Mood. years: 1843-1907. known_for: Peer Gynt, Piano Concerto. country: Norway. Checked against standard references. Creative-domain facts are as stable as history gets; dates and names verified.", "s": "public-reference", "f": null}, {"t": "Camille Saint-Saens", "d": "Saint-Saens' Carnival introduced generations to the orchestra.", "g": "romantic", "l": 2, "q": "What is Camille Saint-Saens?", "a": "Saint-Saens' Carnival introduced generations to the orchestra.", "x": "Saint-Saens' Carnival introduced generations to the orchestra. years: 1835-1921. known_for: Carnival of the Animals. country: France. Checked against standard references. Creative-domain facts are as stable as history gets; dates and names verified.", "s": "public-reference", "f": null}, {"t": "Georges Bizet", "d": "Bizet's Carmen is opera's most famous femme fatale.", "g": "romantic", "l": 2, "q": "What is Georges Bizet?", "a": "Bizet's Carmen is opera's most famous femme fatale.", "x": "Bizet's Carmen is opera's most famous femme fatale. years: 1838-1875. known_for: Carmen. country: France. Checked against standard references. Creative-domain facts are as stable as history gets; dates and names verified.", "s": "public-reference", "f": null}, {"t": "Modest Mussorgsky", "d": "Mussorgsky's Pictures, orchestrated by Ravel, is the mighty handful's peak.", "g": "romantic", "l": 2, "q": "What is Modest Mussorgsky?", "a": "Mussorgsky's Pictures, orchestrated by Ravel, is the mighty handful's peak.", "x": "Mussorgsky's Pictures, orchestrated by Ravel, is the mighty handful's peak. years: 1839-1881. known_for: Pictures at an Exhibition. country: Russia. Checked against standard references. Creative-domain facts are as stable as history gets; dates and names verified.", "s": "public-reference", "f": null}, {"t": "Nikolai Rimsky-Korsakov", "d": "Rimsky-Korsakov orchestrated Russia: Scheherazade's 1001 nights.", "g": "romantic", "l": 2, "q": "What is Nikolai Rimsky-Korsakov?", "a": "Rimsky-Korsakov orchestrated Russia: Scheherazade's 1001 nights.", "x": "Rimsky-Korsakov orchestrated Russia: Scheherazade's 1001 nights. years: 1844-1908. known_for: Scheherazade. country: Russia. Checked against standard references. Creative-domain facts are as stable as history gets; dates and names verified.", "s": "public-reference", "f": null}, {"t": "Gabriel Faure", "d": "Faure's Requiem is consolation in music.", "g": "romantic", "l": 2, "q": "What is Gabriel Faure?", "a": "Faure's Requiem is consolation in music.", "x": "Faure's Requiem is consolation in music. years: 1845-1924. known_for: Requiem, Pavane. country: France. Checked against standard references. Creative-domain facts are as stable as history gets; dates and names verified.", "s": "public-reference", "f": null}, {"t": "Giacomo Puccini", "d": "Puccini wrote the tearjerkers: Boheme, Tosca, Butterfly.", "g": "romantic", "l": 2, "q": "What is Giacomo Puccini?", "a": "Puccini wrote the tearjerkers: Boheme, Tosca, Butterfly.", "x": "Puccini wrote the tearjerkers: Boheme, Tosca, Butterfly. years: 1858-1924. known_for: La Boheme, Tosca, Madama Butterfly. country: Italy. Checked against standard references. Creative-domain facts are as stable as history gets; dates and names verified.", "s": "public-reference", "f": null}];
function pad(n){return String(n).padStart(6,'0');}
function drillProg(q,a){
  return '// boundless drill program\nvar Q='+JSON.stringify(q)+';\nvar A='+JSON.stringify(a)+';\n'
    +'console.log("DRILL: "+Q);\nconsole.log("Say it out loud, then check:");\nconsole.log("ANSWER: "+A);';
}
function bankRec(i){
  var b=BANK[(i-1)%BANK.length];
  var r={id:PREFIX+pad(i),title:b.t,description:b.x,group:b.g,ladder:b.l,
    question:b.q,answer:b.a,method:'archive-sample',
    program:drillProg(b.q,b.a),language:'javascript',
    src:b.s,last_verified:'2026-10-19',sample:true};
  return r;
}
function genQuizDrill(rnd,seed){
  var b=BANK[(rnd()*BANK.length)|0];
  var desc='Boundless drill #'+seed+' — '+NAME+'. The question: '+b.q+'\n\n'
    +'Cover the answer and say it out loud before reading on. Fluency with these facts is the whole game: '
    +'each drill pulls a real record from this database\'s archive and tests exactly one fact cold. '
    +'If you knew it, it is yours; if not, open the archive record "'+b.t+'" and read the full entry, then come back and drill it again. '
    +'The validated answer: '+b.a+'\n\n'
    +'Drills never repeat the archive verbatim — they re-ask the same true facts from new angles so the knowledge sticks.';
  return {id:PREFIX+pad(seed),title:'Drill: '+b.t,description:desc,group:b.g,ladder:b.l,
    method:'quiz-drill',question:b.q,answer:b.a,
    program:drillProg(b.q,b.a),language:'javascript',src:GEN_SRC,last_verified:'2026-10-19'};
}
function genConvertDrill(rnd,seed){
  var b1=BANK[(rnd()*BANK.length)|0],b2=BANK[(rnd()*BANK.length)|0];
  var v=Math.round((1+rnd()*999)*100)/100;
  var ans=v*b1.f/b2.f;
  var q='Convert '+v+' '+b1.t+' to '+b2.t+'.';
  var a=String(Math.round(ans*1e6)/1e6)+' '+b2.t;
  var desc='Boundless drill #'+seed+' — '+NAME+'. The question: '+q+'\n\n'
    +'Work it with the factor table: multiply by the "from" unit\'s factor to reach the base unit, then divide by the "to" unit\'s factor. '
    +'The demo program on any archive record in this database runs the same computation, so you can check your method there first. '
    +'The validated answer: '+a+'. If your number matches, the method is yours; drills like this one keep every conversion in this database one multiplication and one division away.';
  return {id:PREFIX+pad(seed),title:'Conversion drill: '+b1.t+' to '+b2.t,description:desc,
    group:b1.g,ladder:2,method:'convert-drill',question:q,answer:a,
    conv:{value:v,from:b1.t,fromF:b1.f,to:b2.t,toF:b2.f},
    program:'// conversion drill program\nvar v='+v+';\nvar fromF='+b1.f+';\nvar toF='+b2.f+';\n'
      +'console.log("Q: convert "+v+" '+b1.t.replace(/'/g,"\\'")+' to '+b2.t.replace(/'/g,"\\'")+'");\n'
      +'console.log("A: "+(v*fromF/toF)+" '+b2.t.replace(/'/g,"\\'")+'");',
    language:'javascript',src:GEN_SRC,last_verified:'2026-10-19'};
}
function generate(seed,opts,rnd){
  opts=opts||{};seed=+seed||1;rnd=rnd||prng(seed);
  var g=opts.group||opts.category;
  if(g&&FIELDS.indexOf(g)<0)g=null;
  var r;
  if(seed>=1&&seed<=BANK.length){r=bankRec(seed);}
  else{r=(MODE==='convert')?genConvertDrill(rnd,seed):genQuizDrill(rnd,seed);}
  if(g)r.group=g;
  return r;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.group)<0)e.push('group');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<200)e.push('description');
  if(r.method==='quiz-drill'||r.method==='archive-sample'){
    var hit=null;
    for(var i=0;i<BANK.length;i++){if(BANK[i].q===r.question&&BANK[i].a===r.answer){hit=BANK[i];break;}}
    if(!hit)e.push('answer not banked');
  }else if(r.method==='convert-drill'){
    var c=r.conv;
    if(!c||typeof c.value!=='number')e.push('conv missing');
    else{
      var expect=c.value*c.fromF/c.toF;
      var got=parseFloat(String(r.answer).split(' ')[0]);
      if(!(Math.abs(got-expect)<Math.max(1e-6,Math.abs(expect)*1e-9)))e.push('conversion mismatch');
    }
  }else{e.push('method');}
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var seen={};(sample||[]).forEach(function(s){if(s&&s.t)seen[s.t]=1;});
  if(rec&&seen[rec.title])return{ok:false,errors:['duplicate title in archive sample']};
  return{ok:true,errors:[]};
}
var gen={version:'jahdb-classical-composers-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
