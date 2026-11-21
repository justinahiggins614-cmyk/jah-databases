/* Tunes generator engine: playlist builder (the mirror rule) + seeded
   playlist generator from the mirror's own 12 tracks. Browser + Node. */
(function(g){
'use strict';
var TRACKS = [{"title": "Morning Light Waltz", "tags": ["calm", "gentle"], "seconds": 184}, {"title": "Quiet River Song", "tags": ["calm", "gentle"], "seconds": 201}, {"title": "Still Meadow Hymn", "tags": ["calm", "quiet"], "seconds": 176}, {"title": "Bright Parade March", "tags": ["bright", "lively"], "seconds": 150}, {"title": "Sunny Day Chorus", "tags": ["bright", "lively"], "seconds": 168}, {"title": "Festival Drum Dance", "tags": ["bright", "lively"], "seconds": 192}, {"title": "Evening Lantern Ballad", "tags": ["evening", "soft"], "seconds": 214}, {"title": "Night Window Lullaby", "tags": ["evening", "soft"], "seconds": 189}, {"title": "Star Path Serenade", "tags": ["evening", "soft"], "seconds": 207}, {"title": "Swift Runner Tune", "tags": ["lively", "fast"], "seconds": 142}, {"title": "Harbor Bell Chime", "tags": ["gentle", "quiet"], "seconds": 158}, {"title": "Green Valley Reel", "tags": ["lively", "bright"], "seconds": 175}];
function hashStr(s){var h=2166136261;for(var i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619);}return h>>>0;}
function rng(seed){var a=hashStr(String(seed));return function(){a|=0;a=a+0x6D2B79F5|0;var t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function formatTime(sec){sec=Math.max(0,Math.round(sec));return Math.floor(sec/60)+':'+('0'+(sec%60)).slice(-2);}
function totalSeconds(list){return list.reduce(function(a,t){return a+t.seconds;},0);}
function buildPlaylist(q){
  q=String(q==null?'':q).toLowerCase().trim();
  if(!q) return {query:q,tracks:[],totalSeconds:0,totalLabel:'0:00'};
  var qw=q.split(/\s+/);
  var picked=TRACKS.filter(function(t){
    var hay=(t.title+' '+t.tags.join(' ')).toLowerCase();
    return qw.some(function(w){return hay.indexOf(w)!==-1;});
  });
  var total=totalSeconds(picked);
  return {query:q,tracks:picked,totalSeconds:total,totalLabel:formatTime(total)};
}
function makePlaylist(seed,count){
  count=Math.max(1,Math.min(12,Math.floor(count)||3));
  var r=rng(seed);var pool=TRACKS.slice();var out=[];
  while(out.length<count&&pool.length){out.push(pool.splice(Math.floor(r()*pool.length),1)[0]);}
  var total=totalSeconds(out);
  return {seed:String(seed),generated:true,tracks:out,totalSeconds:total,totalLabel:formatTime(total)};
}
var API={TRACKS:TRACKS,buildPlaylist:buildPlaylist,makePlaylist:makePlaylist,formatTime:formatTime,totalSeconds:totalSeconds,hashStr:hashStr};
if(typeof module!=='undefined'){module.exports=API;}
if(typeof window!=='undefined'){window.SigEngine=API;}
if(typeof globalThis!=='undefined'){globalThis.SigEngine=API;}
})(typeof globalThis!=='undefined'?globalThis:this);
