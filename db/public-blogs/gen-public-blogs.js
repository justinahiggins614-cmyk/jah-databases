(function(){'use strict';
/* Public Blogs Database generator — jahdb-public-blogs-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   Each record is a complete sample blog profile with FULL sample posts —
   a full file, never a stub — plus a blog-reader demo program.
   src:"signature-generated-sample" = Signature-authored original, clearly labeled. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
var PREFIX='JAH-BLG-';
var GENRES=['technology','science','culture','personal','business','design','travel','food'];
var BLOGS=[
 {blog:'The Quiet Circuit',by:'R. Okafor',g:'technology',about:'a hardware engineer\'s notebook on building small, repairable electronics',post_t:'Fixing a 1987 Radio, One Capacitor at a Time',post:'There is a particular smell to old electronics — warm dust and phenolic resin — and the 1987 portable radio on my bench had it in abundance.\n\nIt was dead on arrival: no sound, no light, not even the optimistic click of the power switch. The owner, a woman named Del, said it had been her father\'s. "He listened to ball games on it," she said. "I\'d like to hear one more."\n\nDiagnosis started with the power supply. The transformer hummed (good), the rectifier diodes tested fine (good), and then I found it: three electrolytic capacitors, bulged like tiny overfilled water balloons. Forty years of service, and they\'d finally given up.\n\nRecapping is unglamorous work — heat, wick, solder, repeat — but there\'s a moment, after the last joint cools, when you hold your breath and flip the switch. Static. Then, faint and warbling, the ball game.\n\nDel cried. I pretended the solder fumes got to me too.\n\nTotal cost: $4.20 in parts. Total value: one more ball game with Dad.\n\nThat\'s why I fix things.'},
 {blog:'Field Notes from the Tide Line',by:'Dr. Lena Marsh',g:'science',about:'a marine biologist\'s dispatches from the intertidal zone',post_t:'What the Tide Pools Remember',post:'The tide was out by 6 a.m., and the pools were holding their breath.\n\nI\'ve been surveying this stretch of coast for nine years, and the pools keep a better diary than I do. The ochre stars are back — five years after the wasting disease, their arms are thick again, purple and defiant. The mussels have reclaimed the lower rocks in a blue-black army.\n\nBut the diary has new entries too. The water is warmer by nearly a degree. Species I used to find only in the southern coves are showing up here, early, like guests arriving before the party.\n\nA student asked me today if it made me sad, watching it change. I told her the truth: the tide pool doesn\'t do nostalgia. It does adaptation. My job isn\'t to freeze it in 2017 — it\'s to witness honestly, record carefully, and tell the story straight.\n\nThe tide came back in at noon, as it always does. The pools exhaled. I wrote it all down.'},
 {blog:'Marginalia',by:'Theo Bennett',g:'culture',about:'essays on books, films and the ideas hiding inside them',post_t:'In Praise of the Second Reading',post:'The first reading is for plot. The second reading is for everything else.\n\nI just finished my third pass through a novel I first read at nineteen, and I\'m annoyed at nineteen-year-old me for missing so much. The jokes! The structural rhymes! The minor character who is clearly the author working through something!\n\nWe treat re-reading as indulgence, but it\'s actually the most efficient form of reading. The first time, your brain is busy with "what happens next." The second time, freed from suspense, it can notice how it happens — the sentences, the architecture, the choices.\n\nSome books are built for this. They plant details that only bloom on return visits. The authors are playing a long game, trusting you\'ll come back.\n\nSo here\'s my proposal: for every three new books, re-read one old favorite. You\'ll be amazed at how much the book has grown.\n\n(Spoiler: it\'s you. You\'ve grown. The book was waiting.)'},
 {blog:'The Long Way Home',by:'Priya Raman',g:'personal',about:'notes on slowing down, paying attention, and ordinary days',post_t:'The 7:12 Bus',post:'I take the 7:12 bus because the 7:40 is crowded and the 7:12 has the window seat.\n\nThis morning the driver, Mr. Abernathy, waited an extra ten seconds for a running teenager. Nobody sighed. A woman shared her umbrella at the stop even though it wasn\'t raining yet — "just in case," she said, like a weather forecast of kindness.\n\nI used to treat the commute as lost time, dead minutes between life\'s real events. Lately I\'ve been trying the opposite: the commute IS the event. The window seat is a front-row ticket to the city waking up.\n\nThe teenager made the bus. The umbrella wasn\'t needed. Mr. Abernathy nodded at each of us as we got off, like a host ending a small, daily party.\n\nOrdinary days, it turns out, are only ordinary if you don\'t look.'},
 {blog:'Bootstrapped',by:'Marcus Webb',g:'business',about:'a founder\'s honest log of building a small profitable company',post_t:'We Turned Down the Money',post:'Last month we turned down a term sheet. I should say: I turned it down, after three sleepless nights, while my co-founder pretended not to watch me agonize.\n\nThe money was real. The valuation was flattering. The deck practically glowed. But the terms wanted us to 10x in 18 months, and our little company — profitable, calm, 14 people who like each other — would not have survived the transformation.\n\nThere\'s a version of ambition that means getting bigger. There\'s another version that means getting better and staying free. We chose the second.\n\nThis isn\'t advice. For some companies, the rocket ship is right. But I want it on record that we were offered the rocket ship and chose the sailboat — because the sailboat was already taking us where we wanted to go.\n\nRevenue is up 8% this quarter. Everyone\'s still here. I sleep fine.'},
 {blog:'Grid & Grace',by:'Sofia Lindqvist',g:'design',about:'a designer on typography, layout and the details nobody notices',post_t:'The Invisible Work of Good Spacing',post:'Nobody has ever complimented my line-height. That\'s how I know it\'s working.\n\nGood spacing is the bass player of design: unnoticed when present, catastrophic when absent. Crowd the lines and the text shouts; spread them too far and it falls apart like a bad alibi.\n\nHere\'s my rule: set the type, then squint. If the page looks like a comfortable grey texture — even, calm, breathable — the spacing is right. If you see dark clumps and pale gaps, keep adjusting.\n\nThe details nobody notices are the details that make everything else noticeable. A well-set paragraph doesn\'t call attention to itself; it calls attention to the words.\n\nDesign is 90% invisible. The trick is making the invisible feel effortless — which, as any bass player will tell you, takes the most practice of all.'},
 {blog:'One Backpack',by:'Diego Fuentes',g:'travel',about:'slow travel notes from someone who packs light and stays long',post_t:'Lisbon on Foot',post:'Day 9 in Lisbon, and I\'ve stopped taking the tram. Not as a rule — the trams are wonderful — but because the hills have started to feel like old friends, and old friends deserve visits.\n\nSlow travel has a math to it: one neighborhood per day, one long lunch, one wrong turn (mandatory). The wrong turns are the point. Yesterday\'s led to a tiny tasca where the owner insisted I try the ginjinha "the proper way" — which involved a lecture, a toast, and a second glass.\n\nI\'m carrying one backpack, 7 kilos. Everything I own right now fits in it, and I\'ve stopped missing the rest. It turns out "enough" is a much smaller number than the shops suggest.\n\nTomorrow: the ferry across the Tagus, no plan. The best plan I\'ve made all trip.'},
 {blog:'The Patient Kitchen',by:'Amara Diallo',g:'food',about:'recipes and stories from a cook who believes in low heat and long time',post_t:'The Stew That Teaches Patience',post:'This stew takes four hours. I tell you this upfront because the stew will test you at hour two, when it looks like nothing is happening and smells like only slightly more than nothing.\n\nHour two is a liar. Under the lid, collagen is surrendering into gelatin, onions are dissolving into sweetness, and the whole pot is quietly becoming greater than its parts. Your only job: low heat, occasional stir, faith.\n\nThe ingredients are humble — chuck, onions, carrots, a parmesan rind if you have one, time if you don\'t think you do. Brown the meat properly (this is non-negotiable), then walk away. Read a book. Call your mother.\n\nAt hour four, taste. Adjust salt. Notice how the broth coats the spoon now — that\'s the gelatin, that\'s patience made visible.\n\nSome recipes feed you. This one reforms you.'}
];
function generate(seed,opts){
 opts=opts||{}; var s=prng(seed);
 var genre=opts.genre&&GENRES.indexOf(opts.genre)>=0?opts.genre:null;
 var pool=genre?BLOGS.filter(function(x){return x.g===genre;}):BLOGS;
 var b=pick(pool.length?pool:BLOGS,s);
 var words=b.post.split(/\s+/).length;
 var program='<!-- Blog reader for "'+b.blog.replace(/-->/g,'')+'" -->\n<article id="blg-post">\n <h2>'+b.post_t.replace(/</g,'&lt;')+'</h2>\n <p class="byline">By '+b.by.replace(/</g,'&lt;')+' · '+b.blog.replace(/</g,'&lt;')+'</p>\n <div id="blg-body"><!-- full post text renders here, paragraph by paragraph --></div>\n</article>\n<script>\n// Reader mode: clean typography, estimated '+Math.max(1,Math.round(words/200))+'-minute read.\nvar body=document.getElementById("blg-body");\nvar paras=POST_TEXT.split("\\n\\n");\nbody.innerHTML=paras.map(function(p){return "<p>"+p.replace(/</g,"&lt;")+"</p>";}).join("");\n<\/script>\n<!-- Set POST_TEXT to the full post text above to render the complete article. -->';
 return {
  id:PREFIX+pad(seed),
  title:b.blog+' — "'+b.post_t+'" (#'+seed+')',
  blog_name:b.blog, author:b.by,
  description:'A complete sample blog profile: "'+b.blog+'" by '+b.by+' — '+b.about+'. Includes the FULL sample post "'+b.post_t+'" (about '+words+' words) plus a reader-mode demo program. A Signature-authored sample, clearly labeled, never presented as a harvested real blog.',
  genre:b.g, type:'blog',
  about_blog:b.about,
  sample_post:{title:b.post_t, full_text:b.post, word_count:words},
  license:'Signature sample — original work, property of Justin Addam Higgins',
  demo:{kind:'blog-reader',program:program,note:'Reader-mode blog program: renders the full post with clean typography. Set POST_TEXT to the post text to render.'},
  src:'signature-generated-sample', _seed:seed
 };
}
function validate(r){
 var e=[];
 if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
 if(!/^JAH-BLG-\d{6}$/.test(r.id||''))e.push('id');
 if(typeof r.title!=='string'||r.title.length<8)e.push('title');
 if(typeof r.description!=='string'||r.description.length<60)e.push('description');
 if(GENRES.indexOf(r.genre)<0)e.push('genre');
 if(!r.sample_post||typeof r.sample_post.full_text!=='string'||r.sample_post.full_text.length<300)e.push('sample_post');
 if(!r.demo||typeof r.demo.program!=='string')e.push('demo');
 if(r.src!=='signature-generated-sample')e.push('src');
 return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
 var dups=(sample||[]).filter(function(r){return r&&(r.t===record.title||r.title===record.title);});
 return dups.length?{ok:false,errors:['duplicate title in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-public-blogs-1.0',generate:generate,validate:validate,driftCheck:driftCheck,genres:GENRES};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-blogs',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
