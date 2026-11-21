/* Group 7 tools for Signature Tunes. Browser + Node. */
(function(g){
'use strict';
function hashStr(s){var h=2166136261;for(var i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619);}return h>>>0;}
function rng(seed){var a=hashStr(String(seed));return function(){a|=0;a=a+0x6D2B79F5|0;var t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function sumSeconds(text){
  var parts=String(text==null?'':text).split(/[ ,;]+/).filter(function(x){return x!=='';});
  if(!parts.length) return {error:'Enter some seconds, separated by commas.'};
  var total=0;
  for(var i=0;i<parts.length;i++){var n=Number(parts[i]);if(!isFinite(n)||n<0) return {error:'Seconds must be 0 or more, numbers only.'};total+=n;}
  return {value:total,label:Math.floor(total/60)+':'+('0'+(total%60)).slice(-2)};
}
var TRACKS=[{"title": "Morning Light Waltz", "tags": ["calm", "gentle"], "seconds": 184}, {"title": "Quiet River Song", "tags": ["calm", "gentle"], "seconds": 201}, {"title": "Still Meadow Hymn", "tags": ["calm", "quiet"], "seconds": 176}, {"title": "Bright Parade March", "tags": ["bright", "lively"], "seconds": 150}, {"title": "Sunny Day Chorus", "tags": ["bright", "lively"], "seconds": 168}, {"title": "Festival Drum Dance", "tags": ["bright", "lively"], "seconds": 192}, {"title": "Evening Lantern Ballad", "tags": ["evening", "soft"], "seconds": 214}, {"title": "Night Window Lullaby", "tags": ["evening", "soft"], "seconds": 189}, {"title": "Star Path Serenade", "tags": ["evening", "soft"], "seconds": 207}, {"title": "Swift Runner Tune", "tags": ["lively", "fast"], "seconds": 142}, {"title": "Harbor Bell Chime", "tags": ["gentle", "quiet"], "seconds": 158}, {"title": "Green Valley Reel", "tags": ["lively", "bright"], "seconds": 175}];
function makeQuiz(seed){
  var r=rng(seed);var t=TRACKS[Math.floor(r()*TRACKS.length)];
  var moods=['calm','bright','evening','lively','gentle','quiet','soft','fast'];
  var options=[];var correct=t.tags[0];
  options.push(correct);
  while(options.length<4){var m=moods[Math.floor(r()*moods.length)];if(options.indexOf(m)===-1)options.push(m);}
  for(var i=options.length-1;i>0;i--){var j=Math.floor(r()*(i+1));var tmp=options[i];options[i]=options[j];options[j]=tmp;}
  return {kind:'fun',track:t.title,question:'Which mood word fits the track "'+t.title+'"?',options:options,answer:correct};
}

var API={sumSeconds:sumSeconds,makeQuiz:makeQuiz};
if(typeof module!=='undefined'){module.exports=API;}
if(typeof window!=='undefined'){window.SigTools=API;}
if(typeof globalThis!=='undefined'){globalThis.SigTools=API;}
})(typeof globalThis!=='undefined'?globalThis:this);
