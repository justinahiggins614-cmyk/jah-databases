(function(){'use strict';
/* JAH Famous Chess Games Database generator — jahdb-famous-chess-games-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CHESSFAM-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["The Immortal Game: Anderssen vs Kieseritzky, London 1851", "The Evergreen Game: Anderssen vs Dufresne, Berlin 1852", "The Opera Game: Morphy vs Duke Karl and Count Isouard, Paris 1858", "Zukertort vs Blackburne, London 1883", "Rubinstein's Immortal: Rotlevi vs Rubinstein, Lodz 1907", "Marshall's Gold Coins Game: Marshall vs Levitsky, Breslau 1912", "The Game of the Century: Byrne vs Fischer, New York 1956", "Fischer vs Spassky, Game 6, Reykjavik 1972", "Kasparov's Immortal: Kasparov vs Topalov, Wijk aan Zee 1999", "The Deep Blue Decider: Kasparov vs Deep Blue, Game 6, 1997", "Carlsen vs Anand, Game 5, Chennai 2013"], "Compounded": ["Steinitz vs von Bardeleben, Hastings 1895", "Capablanca vs Marshall, New York 1918", "The Polish Immortal: Glucksberg vs Najdorf, Warsaw 1930", "Botvinnik vs Capablanca, AVRO 1938", "Torre's Windmill: Torre vs Adams, New Orleans 1920", "Lasker's King Hunt: Lasker vs Thomas, London 1912", "The Immortal Zugzwang Game: Nimzowitsch vs Saemisch, Copenhagen 1923", "Karpov vs Unzicker, Nice Olympiad 1974", "Karpov vs Kasparov, Game 16, Moscow 1985", "Short vs Timman, Tilburg 1991", "Shirov vs Topalov, Linares 1998", "Carlsen vs Ernst, Wijk aan Zee 2004"], "Advanced": ["AlphaZero vs Stockfish, Game 9, London 2017", "Ding vs Nepomniachtchi, Game 6, Astana 2023", "Gukesh vs Ding, Game 11, Singapore 2024", "Kasparov vs Anand, Game 10, New York 1995", "Anand vs Aronian, Wijk aan Zee 2013", "Carlsen vs Karjakin, Game 10, New York 2016", "The Immortal Draw: Hamppe vs Meitner, Vienna 1872", "La Bourdonnais vs McDonnell, Game 16, London 1834", "Pillsbury vs Lasker, Hastings 1895", "Rubinstein vs Schlechter, San Sebastian 1912", "How to study famous games"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# famous-game-analyzer-demo \u2014 "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record \u2014 structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' \u2014 famous chess game record',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A famous chess game record of \"'+topic+'\" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"famous-game-analyzer-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-famous-chess-games-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('famous-chess-games',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
