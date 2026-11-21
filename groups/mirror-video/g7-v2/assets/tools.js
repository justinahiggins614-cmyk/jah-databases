/* Group 7 tools for Signature Video. Browser + Node. */
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
var ENTRIES=[{"title": "How stars shine", "channel": "Sky Watch", "subject": "science", "seconds": 320}, {"title": "How rivers flow", "channel": "Map Walk", "subject": "science", "seconds": 275}, {"title": "How bread is baked", "channel": "Kitchen Table", "subject": "food", "seconds": 410}, {"title": "How a song is built", "channel": "Song Room", "subject": "music", "seconds": 360}, {"title": "How bridges stand", "channel": "Science Bench", "subject": "science", "seconds": 300}, {"title": "How clocks keep time", "channel": "Science Bench", "subject": "science", "seconds": 245}, {"title": "How birds fly", "channel": "Sky Watch", "subject": "science", "seconds": 290}, {"title": "How ships sail", "channel": "Map Walk", "subject": "sea", "seconds": 330}, {"title": "How mountains form", "channel": "Science Bench", "subject": "science", "seconds": 380}, {"title": "How rain falls", "channel": "Sky Watch", "subject": "science", "seconds": 210}, {"title": "How maps are drawn", "channel": "Map Walk", "subject": "maps", "seconds": 265}, {"title": "How books are bound", "channel": "Book Shelf", "subject": "books", "seconds": 355}];
function makeQuiz(seed){
  var r=rng(seed);var v=ENTRIES[Math.floor(r()*ENTRIES.length)];
  var chans=['Sky Watch','Map Walk','Kitchen Table','Song Room','Science Bench','Book Shelf'];
  var options=[v.channel];
  while(options.length<4){var c=chans[Math.floor(r()*chans.length)];if(options.indexOf(c)===-1)options.push(c);}
  for(var i=options.length-1;i>0;i--){var j=Math.floor(r()*(i+1));var tmp=options[i];options[i]=options[j];options[j]=tmp;}
  return {kind:'fun',entry:v.title,question:'Which channel made the video "'+v.title+'"?',options:options,answer:v.channel};
}

var API={sumSeconds:sumSeconds,makeQuiz:makeQuiz};
if(typeof module!=='undefined'){module.exports=API;}
if(typeof window!=='undefined'){window.SigTools=API;}
if(typeof globalThis!=='undefined'){globalThis.SigTools=API;}
})(typeof globalThis!=='undefined'?globalThis:this);
