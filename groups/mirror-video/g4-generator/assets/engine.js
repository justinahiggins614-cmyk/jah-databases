/* Video generator engine: search scorer (the mirror rule) + seeded
   lineup generator from the mirror's own 12 entries. Browser + Node. */
(function(g){
'use strict';
var ENTRIES = [{"title": "How stars shine", "channel": "Sky Watch", "subject": "science", "seconds": 320}, {"title": "How rivers flow", "channel": "Map Walk", "subject": "science", "seconds": 275}, {"title": "How bread is baked", "channel": "Kitchen Table", "subject": "food", "seconds": 410}, {"title": "How a song is built", "channel": "Song Room", "subject": "music", "seconds": 360}, {"title": "How bridges stand", "channel": "Science Bench", "subject": "science", "seconds": 300}, {"title": "How clocks keep time", "channel": "Science Bench", "subject": "science", "seconds": 245}, {"title": "How birds fly", "channel": "Sky Watch", "subject": "science", "seconds": 290}, {"title": "How ships sail", "channel": "Map Walk", "subject": "sea", "seconds": 330}, {"title": "How mountains form", "channel": "Science Bench", "subject": "science", "seconds": 380}, {"title": "How rain falls", "channel": "Sky Watch", "subject": "science", "seconds": 210}, {"title": "How maps are drawn", "channel": "Map Walk", "subject": "maps", "seconds": 265}, {"title": "How books are bound", "channel": "Book Shelf", "subject": "books", "seconds": 355}];
function hashStr(s){var h=2166136261;for(var i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619);}return h>>>0;}
function rng(seed){var a=hashStr(String(seed));return function(){a|=0;a=a+0x6D2B79F5|0;var t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function formatTime(sec){sec=Math.max(0,Math.round(sec));return Math.floor(sec/60)+':'+('0'+(sec%60)).slice(-2);}
function scoreVideos(q){
  q=String(q==null?'':q).toLowerCase().trim();
  if(!q) return [];
  var qw=q.split(/\s+/);
  var scored=ENTRIES.map(function(v){
    var score=0;
    qw.forEach(function(w){
      if(v.title.toLowerCase().indexOf(w)!==-1) score+=3;
      else if((v.channel+' '+v.subject).toLowerCase().indexOf(w)!==-1) score+=1;
    });
    var hay=(v.title+' '+v.channel+' '+v.subject).toLowerCase();
    var all=qw.every(function(w){return hay.indexOf(w)!==-1;});
    return {video:v,score:score,ok:all};
  }).filter(function(x){return x.ok&&x.score>0;});
  scored.sort(function(a,b){return b.score-a.score||(a.video.title<b.video.title?-1:1);});
  return scored;
}
function makeLineup(seed,count){
  count=Math.max(1,Math.min(12,Math.floor(count)||3));
  var r=rng(seed);var pool=ENTRIES.slice();var out=[];
  while(out.length<count&&pool.length){out.push(pool.splice(Math.floor(r()*pool.length),1)[0]);}
  var total=out.reduce(function(a,v){return a+v.seconds;},0);
  return {seed:String(seed),generated:true,entries:out,totalSeconds:total,totalLabel:formatTime(total)};
}
var API={ENTRIES:ENTRIES,scoreVideos:scoreVideos,makeLineup:makeLineup,formatTime:formatTime,hashStr:hashStr};
if(typeof module!=='undefined'){module.exports=API;}
if(typeof window!=='undefined'){window.SigEngine=API;}
if(typeof globalThis!=='undefined'){globalThis.SigEngine=API;}
})(typeof globalThis!=='undefined'?globalThis:this);
