/* JAH Public Books Database generator — jahdb-public-books-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   Generates COMPLETE original short works (short story / poem / fable), clearly
   labeled src:"signature-generated-sample" — never presented as public-domain harvest. */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(s,r){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function shuffle(s,arr){var a=arr.slice(),i,j,t;for(i=a.length-1;i>0;i--){j=(s()*(i+1))|0;t=a[i];a[i]=a[j];a[j]=t;}return a;}
var PREFIX='JAH-PBK-';
var GENRES=['Short Story','Poetry','Fable'];

var NAMES=[['Mara Ellison','she'],['Jonas Pike','he'],['Adaeze Okafor','she'],['Tomas Reyes','he'],['Wren Halloway','she'],['Silas Brandt','he'],['Imogen Vale','she'],['Casper Lind','he'],['Noor Haddad','she'],['Edwin Marsh','he'],['Lucia Ferreira','she'],['Amos Quill','he']];
var PLACES=['a lighthouse on a cliff that the maps forgot','a night market that appears only when it rains','a railway station at the end of a discontinued line','a small town where every clock stopped in 1962','a lighthouse library built inside a decommissioned ship','a valley town famous for a bell no one is allowed to ring','a coastal inn kept by three sisters','a mountain observatory above the cloud line','a bookshop that sells only books its owner has read twice','a ferry crossing that runs one boat, once a day'];
var OBJECTS=[['a brass key with no known lock','the brass key'],['a letter posted forty years late','the letter'],['a pocket watch that runs backward','the pocket watch'],['a photograph of a street that never existed','the photograph'],['a music box that plays an unknown tune','the music box'],['a ledger written in two different hands','the ledger'],['a telescope aimed at an empty patch of sky','the telescope'],['a recipe card in a stranger\'s handwriting','the recipe card'],['a ticket stub for a voyage never taken','the ticket stub'],['a compass whose needle points at people, not north','the compass']];
var TRAITS=['a cartographer','a retired sea captain','a clockmaker','a beekeeper','a night-shift baker','a lighthouse keeper','a map restorer','a former telegram operator','a gardener of rare roses','a collector of broken instruments'];

function storyTitle(s,name,place){
  var t=[['The '+pick(s,['Brass','Glass','Paper','Copper','Iron','Silver'])+' '+pick(s,['Key','Letter','Watch','Compass','Ledger','Ticket'])],
   ['What the '+pick(s,['Rain','Night','Sea','Wind','Clocks'])+' Brought'],
   ['The Last '+pick(s,['Lighthouse','Market','Ferry','Bookshop','Bell'])],
   ['A '+pick(s,['Cartographer','Captain','Baker','Keeper'])+'\'s Promise'],
   [name.split(' ')[0]+' and the '+pick(s,['Unknown Tune','Empty Sky','Forty-Year Letter','Backward Watch'])]];
  return pick(s,t)[0];
}
function buildStory(s,topic){
  var nm=pick(s,NAMES), place=pick(s,PLACES), ob=pick(s,OBJECTS), obj=ob[0], objShort=ob[1], trait=pick(s,TRAITS);
  var pro=nm[1], PRO=pro==='she'?'She':'He';
  var objp=pro==='she'?'her':'him', refl=pro==='she'?'herself':'himself';
  var title=topic?('Story: '+topic):storyTitle(s,nm[0],place);
  var beats=shuffle(s,[
   'The trouble began on an ordinary Tuesday, when '+nm[0]+' found '+obj+' where no such thing should have been.',
   'Everyone in town knew '+nm[0].split(' ')[0]+' as '+addIndef(trait)+', steady and unremarkable \u2014 until that Tuesday.',
   'Nobody believed the story at first, least of all '+nm[0].split(' ')[0]+' '+refl+'.',
   'The discovery changed the shape of ordinary days: '+pro+' began to notice small wrongnesses everywhere.'
  ]);
  var mids=shuffle(s,[
   'Following the only clue '+pro+' had, '+nm[0].split(' ')[0]+' went to '+place+', where the air itself seemed to be waiting.',
   'At '+place+', an old keeper of the place listened to the whole tale and said only: "You had better be certain."',
   'The second clue was worse than the first, and '+pro+' nearly turned back \u2014 but '+objShort+' would not let '+objp+' rest.',
   'Three nights of watching taught '+objp+' what the days had hidden: the pattern was deliberate, and it was patient.'
  ]);
  var ends=shuffle(s,[
   'In the end the truth was smaller and kinder than the fear: what was lost had only been waiting to be found.',
   'The town never learned the whole of it, and '+nm[0].split(' ')[0]+' never told \u2014 some stories are kept, not spent.',
   'When it was over, '+pro+' put '+objShort+' back where it belonged, and slept the deep sleep of the honest.',
   'And from that season on, '+place+' was different \u2014 though no visitor could ever quite say how.'
  ]);
  var paras=[beats[0]+' '+beats[1], mids[0]+' '+mids[1], mids[2], ends[0]+' '+ends[1]];
  var text=title.toUpperCase()+'\nAn original story in the Public Books collection\n\n'+paras.join('\n\n');
  return {title:title, genre:'Short Story', text:text};
}
function addIndef(w){return (/^[aeiou]/i.test(w)?'an ':'a ')+w;}
var POEM_L1=['I walked the shoreline at first light,','The winter stars were sharp and near,','A letter came without a name,','The old clock counted out the rain,','I found a garden in the stone,','The river kept its silver vow,'];
var POEM_L2=['and thought of all the roads behind,','and every wish I held was clear,','and left its questions at my door,','and every drop recalled a name,','where quiet flowers made their own,','and carried moonlight on its brow,'];
var POEM_L3=['The world was wider than my fear,','The night was honest, cold, and true,','I answered nothing, only smiled,','Time writes its ledger line by line,','No wall could keep the wild away,','The current sang, I let it go,'];
var POEM_L4=['and morning made the pathway kind.','and morning made the whole world new.','and kept the mystery a while.','and every debt is paid in time.','and I was glad to let it stay.','and learned what rivers always know.'];
function buildPoem(s,topic){
  var title=topic?('Poem: '+topic):pick(s,['First Light','The Ledger of Rain','What Rivers Know','Winter Stars','The Unnamed Letter','Garden in the Stone']);
  var stanzas=[],used={};
  for(var q=0;q<4;q++){
    var a=pick(s,POEM_L1),b=pick(s,POEM_L2),c=pick(s,POEM_L3),d=pick(s,POEM_L4);
    stanzas.push([a,b,c,d].join('\n'));
  }
  var text=title+'\n\n'+stanzas.join('\n\n');
  return {title:title, genre:'Poetry', text:text};
}
var FABLE_BEASTS=[['Hare','Tortoise'],['Fox','Stork'],['Ant','Grasshopper'],['Oak','Reed'],['Crow','Fox'],['Lion','Mouse']];
var FABLE_MORALS=['Slow and steady wins the race.','Prepare today for the needs of tomorrow.','Pride goes before a fall.','The flexible survive where the rigid break.','Do not trust flatterers.','Even the small can help the great.'];
var FABLE_PLOTS=[
 'boasted loudly of speed, and challenged the other to a race. The race began, and the boaster sprinted ahead, then lay down to nap, certain of victory. The other kept steadily on, passed the sleeper, and won.',
 'invited the other to dinner, but served the meal in a vessel the guest could not use. The guest returned the invitation in kind, serving dinner in a vessel the host could not reach. Both learned the same lesson.',
 'worked through the summer storing grain while the other sang and played. When winter came, the singer went hungry, and the worker shared \u2014 but not before the lesson was learned.'
];
function buildFable(s,topic){
  var pair=pick(s,FABLE_BEASTS), plot=pick(s,FABLE_PLOTS), moral=pick(s,FABLE_MORALS);
  var title=topic?('Fable: '+topic):('The '+pair[0]+' and the '+pair[1]);
  var text=title.toUpperCase()+'\n\nThe '+pair[0].toLowerCase()+' '+plot+'\n\nMoral: '+moral;
  return {title:title, genre:'Fable', text:text};
}
function demoProgram(rid,title,snippet){
  var j=function(x){return JSON.stringify(x);};
  return '/* JAH interactive demo program \u2014 jahdb-demo-1.0\n'+
   ' * Database: public-books \u00b7 Record: '+rid+' \u00b7 '+title+'\n'+
   ' * Guided reading + text analysis of this generated work.\n'+
   ' * RUN ON PC: save as demo.js, then run:  node demo.js\n'+
   ' * RUN IN BROWSER: press F12, paste into the console, press Enter. */\n'+
   '(function(){var TITLE='+j(title)+';var TEXT='+j(snippet)+';\n'+
   'var w=TEXT.split(/\\s+/).filter(Boolean).length;\n'+
   'console.log("=== "+TITLE+" ===");\n'+
   'console.log(w+" words in excerpt \u00b7 ~"+Math.max(1,Math.round(w/200))+" min reading time");\n'+
   'console.log(TEXT.slice(0,500));\n'+
   'console.log("Demo complete \u2014 open the full record to read the complete work.");})();';
}
function normGenre(g){
  if(g==='Short Story')return 0; if(g==='Poetry')return 1; if(g==='Fable')return 2;
  return -1;
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var topic=(opts.topic||'').toString().trim().slice(0,120)||null;
  var fam=normGenre(opts.genre); if(fam<0) fam=ri(rnd,0,2);
  var s=rnd, b;
  if(fam===0)b=buildStory(s,topic);else if(fam===1)b=buildPoem(s,topic);else b=buildFable(s,topic);
  var id=PREFIX+String(seed).padStart(7,'0');
  var words=b.text.split(/\s+/).filter(Boolean).length;
  return {
   id:id, title:b.title, author:'JAH Boundless Generator (original work)', year:2026,
   genre:b.genre, gkey:b.genre==='Short Story'?'story':(b.genre==='Poetry'?'poetry':'fable'),
   desc:'A complete original '+(b.genre==='Fable'?'fable':b.genre.toLowerCase())+' generated for the Public Books Database ('+words+' words, full text). Clearly labeled as a Signature-generated sample, never as public-domain harvest.',
   words:words, chapters:[{t:'Complete Text',b:b.text}],
   image:'', image_full:'',
   demo:{engine:'jahdb-demo-1.0',kind:'read',title:'Guided reading demo \u2014 '+b.title,language:'javascript',
     program:demoProgram(id,b.title,b.text.slice(0,2000))},
   src:'signature-generated-sample', origin:'signature',
   note:'Original generated work. Labeled sample; not a public-domain harvest.',
   sources:[{kind:'signature-generated',detail:'Original work created by the JAH boundless generator.'}],
   _seed:seed, topic:topic||undefined
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-PBK-\d{7}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.length<8)e.push('title');
  if(!Array.isArray(r.chapters)||!r.chapters.length||typeof r.chapters[0].b!=='string'||r.chapters[0].b.length<200)e.push('chapters');
  if(!r.demo||typeof r.demo.program!=='string'||r.demo.program.indexOf('jahdb-demo-1.0')<0)e.push('demo');
  if(r.src!=='signature-generated-sample')e.push('src');
  if(GENRES.indexOf(r.genre)<0)e.push('genre');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title;});
  return dups.length?{ok:false,errors:['duplicate title in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-public-books-1.0',generate:generate,validate:validate,driftCheck:driftCheck,genres:GENRES};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-books',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
