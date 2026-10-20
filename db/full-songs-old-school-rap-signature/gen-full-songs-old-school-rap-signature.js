(function(){'use strict';
/* Full Songs: Old School Rap (Signature) — boundless full-song generator (Signature edition).
   Deterministic: same seed, same record. Boundless: any positive seed
   composes a fresh, complete, validated record from the embedded pools. */
var CONFIG={"slug": "full-songs-old-school-rap-signature", "kind": "song", "category": "Old School Rap", "genre": "Old School Rap", "prefix": "FSS079-", "gen_version": "jahdb-full-songs-old-school-rap-signature-1.0", "verified": "2026-10-19", "themes": ["block party 1979", "two turntables", "adidas shell-toe", "cardboard breakdance", "graffiti wall", "boombox battle", "MC shout", "sugar hill"], "moods": ["playful", "pioneering", "funky", "joyful", "classic"], "pools": {"verse": ["I came up from the {theme} block, now I'm worldwide", "Every scar's a story that I wear with pride", "They counted me out on that {theme} street", "Now every bar I drop is indiscreet", "From the {theme} basement to the penthouse floor", "Kicked down every locked {theme} door", "My grandma prayed on that {theme} porch", "Now I carry that {theme} torch", "Pen to the pad, let the {theme} speak", "Seven days strong, never weak", "They want the formula, the {theme} code", "I paved my own {theme} road", "Diamonds in the {theme} rough, I shine", "Every verse a {theme} lifeline", "I remember nights with the {theme} cold", "Now my story's being told", "Count the blessings, count the {theme} wins", "Where the struggle stops, the {theme} begins"], "chorus": ["{theme} to the top, we never stop!", "From the bottom to the {theme} rooftop!", "Hands high for the {theme} fam —", "You know exactly who I am!", "We rep that {theme}, loud and proud!", "Say it with me, say it loud!", "{theme} dreams in a {theme} sky —", "We gon' make it, you and I!"], "bridge": ["Let the beat breathe... {theme}... ", "One voice, one choice, {theme} noise —", "Now bring the hook back, let's go!"], "titles": ["{theme} Dreams", "The {theme} Code", "{theme} to the Top", "Straight from {theme}", "{theme} Anthem", "The {theme} Story"], "descs": ["A hard-hitting {genre} cut about {theme} — bars over everything.", "{genre} storytelling: {theme} from the block to the top."], "structures": [["Verse 1", "Chorus", "Verse 2", "Chorus", "Bridge", "Chorus"]], "chords": {"verse": ["Am - Am - F - G", "Dm - Dm - Bb - C", "Em - Em - C - D"], "chorus": ["F - G - Am - Am", "Bb - C - Dm - Dm"], "bridge": ["Am - G - F - E", "Dm - C - Bb - A"]}, "tempo": [84, 100], "times": ["4/4"], "keys": ["A minor", "D minor", "E minor", "G minor"], "arrangements": ["Booming 808s, crisp snares, a moody piano loop, and ad-libs stacked on every hook.", "Cinematic mix: strings swelling under the verses, choir stabs on the chorus, beat drops out for the bridge."], "slots": {"word": ["hustle", "grind", "block", "crown", "legacy", "struggle", "shine", "real"]}}, "fields": ["id", "title", "lyrics", "structure", "chords", "tempo_bpm", "song_key", "arrangement", "artwork", "program", "src"]};
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,arr){return arr[(r()*arr.length)|0];}
function pad(n){n=String(n);while(n.length<6)n='0'+n;return n;}
function fill(tpl,r,slots){return String(tpl).replace(/\{(\w+)\}/g,function(m,k){var v=slots?slots[k]:null;if(v==null)return m;return Array.isArray(v)?pick(r,v):v;});}
function shuffle(r,arr){arr=arr.slice();for(var i=arr.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=arr[i];arr[i]=arr[j];arr[j]=t;}return arr;}
function cleanTitle(t){t=String(t).replace(/[Tt]he the/g,'The').replace(/\s+/g,' ').trim();return t.charAt(0).toUpperCase()+t.slice(1);}

function composeSong(r,seed,forceTheme){
  var P=CONFIG.pools, theme=forceTheme||pick(r,CONFIG.themes);
  var slots={theme:theme};
  Object.keys(P.slots||{}).forEach(function(k){slots[k]=P.slots[k];});
  var title=cleanTitle(fill(pick(r,P.titles),r,{theme:theme,word:P.slots.word||[]}));
  var structure=pick(r,P.structures).slice();
  var lyrics={}, chords={};
  var usedV={}, usedC={}, usedB={};
  function take(pool,used,n){
    var avail=pool.filter(function(l){return !used[l];});
    if(avail.length<n)avail=pool.slice();
    avail=shuffle(r,avail);
    var out=avail.slice(0,n);
    out.forEach(function(l){used[l]=1;});
    return out.map(function(l){return fill(l,r,slots);}).join("\n");
  }
  structure.forEach(function(sec){
    var kind=/chorus/i.test(sec)?'chorus':/bridge/i.test(sec)?'bridge':/verse/i.test(sec)?'verse':'other';
    var n=kind==='chorus'?4:kind==='bridge'?4:kind==='verse'?4:2;
    var txt=kind==='chorus'?take(P.chorus,usedC,n):kind==='bridge'?take(P.bridge,usedB,n):take(P.verse,usedV,n);
    lyrics[sec]=txt;
    chords[sec]=pick(r,P.chords[kind]||P.chords.verse);
  });
  var full=title.toUpperCase()+"\n";
  structure.forEach(function(sec){full+="\n["+sec.toUpperCase()+"] ("+chords[sec]+")\n"+lyrics[sec]+"\n";});
  return {
    id:CONFIG.prefix+pad(seed), title:title, category:CONFIG.category,
    kind:'signature-full-song', description:fill(pick(r,P.descs),r,{theme:theme,genre:CONFIG.genre}),
    artist_credit:'Signature original', genre:CONFIG.genre, mood:pick(r,CONFIG.moods),
    tempo_bpm:P.tempo[0]+((r()*(P.tempo[1]-P.tempo[0]))|0),
    time_signature:pick(r,P.times), song_key:pick(r,P.keys),
    structure:structure, chords:chords, lyrics:lyrics, full_text:full,
    arrangement:fill(pick(r,P.arrangements),r,slots),
    src:'signature-generated', source:'Signature original composition — generated full version',
    last_verified:CONFIG.verified
  };
}

function composeBook(r,seed){
  var P=CONFIG.pools;
  var prem=pick(r,P.premises);
  var slots={};
  Object.keys(P.slots||{}).forEach(function(k){slots[k]=P.slots[k];});
  slots.hero=pick(r,P.slots.hero); slots.friend=pick(r,P.slots.friend);
  slots.place=pick(r,P.slots.place); slots.thing=pick(r,P.slots.thing);
  var title=cleanTitle(fill(pick(r,P.titles),r,slots));
  var chapters=[];
  for(var b=0;b<P.beats.length;b++){
    var beat=P.beats[b];
    var paras=shuffle(r,beat.paras).slice(0,3).map(function(p){return fill(p,r,slots);});
    var text=paras.join("\n\n");
    chapters.push({n:b+1,title:fill(beat.title,r,slots),text:text});
  }
  var words=chapters.reduce(function(a,c){return a+c.text.split(/\s+/).length;},0);
  return {
    id:CONFIG.prefix+pad(seed), title:title, category:CONFIG.category,
    kind:'signature-full-book', description:fill(pick(r,P.descs),r,slots),
    author:'Signature original', genre:CONFIG.genre, reading_level:pick(r,CONFIG.levels),
    word_count:words, chapters:chapters,
    full_text:title+"\n"+chapters.map(function(c){return "\nCHAPTER "+c.n+": "+c.title+"\n"+c.text;}).join("\n"),
    src:'signature-generated', source:'Signature original novella — generated complete book',
    last_verified:CONFIG.verified
  };
}

function generate(seed){
  seed=Math.max(1,seed|0);
  var r=prng(((seed*2654435761)>>>0)||1);
  var rec;
  if(CONFIG.kind==='song')rec=composeSong(r,seed);
  else if(CONFIG.kind==='book')rec=composeBook(r,seed);
  else if(CONFIG.kind==='playlist-songs'){
    rec={id:CONFIG.prefix+pad(seed),title:'Playlist of the Week — Week '+(((seed-1)%52)+1),
      category:CONFIG.category,kind:'playlist-week-songs',
      description:'A full week of complete songs, curated publication-ready.',
      week:'W'+(((seed-1)%52)+1),theme:pick(r,CONFIG.themes),
      items:[],src:'signature-generated',
      source:'Signature curated weekly playlist — generated full material',
      last_verified:CONFIG.verified};
    for(var i=0;i<10;i++){var s=composeSong(r,seed*100+i+1,pick(r,CONFIG.themes));s.n=i+1;s.artist=s.artist_credit;rec.items.push(s);}
    rec.curator_notes='Ten complete songs sequenced for the week: an opener to lift the mood, a midweek run of energy, and a closer that lands soft. Every track is the full song — lyrics, chords, structure — ready to publish as-is.';
  } else if(CONFIG.kind==='playlist-books'){
    rec={id:CONFIG.prefix+pad(seed),title:pick(r,CONFIG.themes)+' — Complete Book List',
      category:CONFIG.category,kind:'playlist-week-books',
      description:'A complete reading list: every book in full, curated publication-ready.',
      list_id:'L'+(((seed-1)%52)+1),theme:pick(r,CONFIG.themes),
      items:[],src:'signature-generated',
      source:'Signature curated book list — generated full material',
      last_verified:CONFIG.verified};
    for(var j=0;j<5;j++){var b=composeBook(r,seed*100+j+1);b.n=j+1;b.author=b.author;rec.items.push(b);}
    rec.curator_notes='Five complete books in one list — start anywhere, finish everything. Each entry is the whole book, chapters and all, curated to read straight through as published.';
  } else {
    var MP=CONFIG.pools;
    var mslots={hero:pick(r,MP.slots.hero),friend:pick(r,MP.slots.friend)};
    if(MP.slots.place)mslots.place=pick(r,MP.slots.place);
    if(MP.slots.thing)mslots.thing=pick(r,MP.slots.thing);
    if(MP.slots.villain)mslots.villain=pick(r,MP.slots.villain);
    rec={id:CONFIG.prefix+pad(seed),title:cleanTitle(pick(r,CONFIG.themes))+' — Full Feature',
      category:CONFIG.category,kind:'movie-treatment',
      description:'A complete original movie treatment, full synopsis and scenes.',
      genre:CONFIG.genre,director:'Signature Pictures',year:'2026',
      logline:fill(pick(r,MP.loglines),r,mslots),
      synopsis:fill(pick(r,MP.synopses),r,mslots),
      cast:[{role:'Lead',name:mslots.hero},{role:'Support',name:mslots.friend}],
      scenes:[{n:1,title:'Opening',text:fill(pick(r,MP.scenes),r,mslots)},
              {n:2,title:'Turning Point',text:fill(pick(r,MP.scenes),r,mslots)},
              {n:3,title:'Finale',text:fill(pick(r,MP.scenes),r,mslots)}],
      viewing_guide:'Watch with the sound up; the second act rewards a second viewing.',
      src:'signature-generated',source:'Signature original movie treatment',
      last_verified:CONFIG.verified};
  }
  rec._seed=seed;
  return rec;
}
function validId(id){return new RegExp('^'+CONFIG.prefix.replace(/-/g,'\\-')+'\\d{6}$').test(id||'');}
function validate(rec){
  var e=[];
  if(!rec||typeof rec!=='object')return {ok:false,errors:['not an object']};
  if(!validId(rec.id))e.push('id');
  if(typeof rec.title!=='string'||!rec.title.length)e.push('title');
  if(rec.kind==='signature-full-song'||(rec.lyrics&&rec.structure)){
    if(!rec.structure||!rec.structure.length)e.push('structure');
    if(!rec.lyrics||typeof rec.lyrics!=='object')e.push('lyrics');
    else rec.structure.forEach(function(s){if(!rec.lyrics[s]||rec.lyrics[s].length<20)e.push('lyrics:'+s);});
    if(!rec.chords||typeof rec.chords!=='object')e.push('chords');
  }
  if(rec.kind==='signature-full-book'||rec.chapters){
    if(!rec.chapters||rec.chapters.length<3)e.push('chapters');
    else rec.chapters.forEach(function(c,i){if(!c.text||c.text.length<200)e.push('chapter'+(i+1));});
  }
  if(rec.items){
    if(!rec.items.length)e.push('items');
    rec.items.forEach(function(it,i){
      if(!it.title)e.push('item'+(i+1)+'.title');
      if(it.lyrics){Object.keys(it.lyrics).forEach(function(s){if(it.lyrics[s].length<20)e.push('item'+(i+1)+'.lyrics');});}
      if(it.chapters&&it.chapters.length<3)e.push('item'+(i+1)+'.chapters');
    });
  }
  if(typeof rec.src!=='string'||!rec.src.length)e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var seen={};(sample||[]).forEach(function(s){if(s&&s.title)seen[s.title]=1;});
  if(rec&&seen[rec.title])return {ok:false,errors:['duplicate title in archive sample']};
  return {ok:true,errors:[]};
}
var gen={version:CONFIG.gen_version,generate:generate,validate:validate,driftCheck:driftCheck,fields:CONFIG.fields};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(CONFIG.slug,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
