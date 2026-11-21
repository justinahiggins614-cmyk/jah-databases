/* Seeded deterministic generator for Signature Mail — same seed, same output. Outputs are generated, never archive records. */

function hashSeed(s){
  var h=2166136261>>>0; s=String(s==null?'':s);
  for(var i=0;i<s.length;i++){ h^=s.charCodeAt(i); h=Math.imul(h,16777619); }
  return h>>>0;
}
function rngFrom(seed){ var a=hashSeed(seed); return function(){ a|=0; a=(a+0x6D2B79F5)|0; var t=Math.imul(a^(a>>>15),1|a); t=(t+Math.imul(t^(t>>>7),61|t))^t; return ((t^(t>>>14))>>>0)/4294967296; }; }
function pickN(rng, arr, n){
  var copy=arr.slice(), out=[];
  while(out.length<n && copy.length){ out.push(copy.splice(Math.floor(rng()*copy.length),1)[0]); }
  return out;
}
var NAMES=[{"name": "Rin", "role": "baker"}, {"name": "Mara", "role": "gardener"}, {"name": "Theo", "role": "teacher"}, {"name": "June", "role": "sailor"}, {"name": "Ansel", "role": "carpenter"}, {"name": "Wren", "role": "painter"}, {"name": "Kofi", "role": "drummer"}, {"name": "Lena", "role": "librarian"}];
var SUBJECTS=['Harvest fair','A note','Thank you','A visit','The new season'];
var BODIES=['I hope this letter finds you well. The season is turning, and I thought of you.','Thank you for your help last week. It made a real difference, and I wanted to say so properly.','I am writing to ask after you and to share a little news from the harbor.'];

function writeLetter(seed){
  seed=String(seed==null||String(seed).trim()===''?'morning-cup':seed);
  var rng=rngFrom(seed);
  var to=pickN(rng,NAMES,1)[0];
  var subject=SUBJECTS[Math.floor(rng()*SUBJECTS.length)];
  var body=BODIES[Math.floor(rng()*BODIES.length)];
  return {seed:seed,to:to.name,role:to.role,subject:subject,
    greeting:'Dear '+to.name+',',body:body,closing:'With best wishes,',generated:true};
}
if(typeof module!=='undefined'){module.exports={writeLetter:writeLetter,hashSeed:hashSeed,rngFrom:rngFrom,pickN:pickN,NAMES:NAMES};}
