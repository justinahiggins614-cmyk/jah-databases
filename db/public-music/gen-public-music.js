(function(){'use strict';
/* JAH Public Music Database generator — jahdb-public-music-1.0.
   Property of Justin Addam Higgins (JAH).
   Type 1 (public): this generator NEVER invents songs, composers, or recordings.
   It creates LISTENING GUIDES (curatorial notes about real public-domain works)
   and THEMED PLAYLISTS (groupings of real works). Deterministic: same seed,
   same record. src:"signature" for the curatorial guide text itself (clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(s,arr){var a=arr.slice(),i,j,t;for(i=a.length-1;i>0;i--){j=(s()*(i+1))|0;t=a[i];a[i]=a[j];a[j]=t;}return a;}
var PREFIX='JAH-PMUS-';
var POOL={
 'classical-baroque':[
  ['Brandenburg Concerto No. 3','J.S. Bach','1721'],['Goldberg Variations','J.S. Bach','1741'],
  ['Toccata and Fugue in D minor','J.S. Bach','c.1704'],['The Four Seasons','Antonio Vivaldi','1725'],
  ['Messiah','G.F. Handel','1741'],['Water Music','G.F. Handel','1717'],
  ['Canon in D','Johann Pachelbel','c.1694'],['Air on the G String','J.S. Bach','1731'],
  ['St Matthew Passion','J.S. Bach','1727'],['Zadok the Priest','G.F. Handel','1727'],
  ['Gloria in D major','Antonio Vivaldi','c.1715'],['Dido\'s Lament','Henry Purcell','1689']],
 'classical-viennese':[
  ['Symphony No. 40 in G minor','W.A. Mozart','1788'],['Symphony No. 41 "Jupiter"','W.A. Mozart','1788'],
  ['Eine kleine Nachtmusik','W.A. Mozart','1787'],['Requiem in D minor','W.A. Mozart','1791'],
  ['Symphony No. 5 in C minor','Ludwig van Beethoven','1808'],['Symphony No. 9 "Choral"','Ludwig van Beethoven','1824'],
  ['Moonlight Sonata','Ludwig van Beethoven','1801'],['Für Elise','Ludwig van Beethoven','c.1810'],
  ['Symphony No. 94 "Surprise"','Joseph Haydn','1791'],['The Creation','Joseph Haydn','1798'],
  ['Clarinet Concerto','W.A. Mozart','1791'],['Pathétique Sonata','Ludwig van Beethoven','1799']],
 'classical-romantic':[
  ['Nocturne in E-flat, Op. 9 No. 2','Frédéric Chopin','1832'],['1812 Overture','P. Tchaikovsky','1880'],
  ['Swan Lake','P. Tchaikovsky','1876'],['The Nutcracker','P. Tchaikovsky','1892'],
  ['Hungarian Dance No. 5','Johannes Brahms','1869'],['Symphony No. 9 "From the New World"','A. Dvořák','1893'],
  ['In the Hall of the Mountain King','Edvard Grieg','1876'],['Pictures at an Exhibition','M. Mussorgsky','1874'],
  ['Scheherazade','N. Rimsky-Korsakov','1888'],['Danse macabre','C. Saint-Saëns','1874'],
  ['Clair de lune','Claude Debussy','1890'],['Boléro','Maurice Ravel','1928']],
 'opera-vocal':[
  ['Nessun dorma (Turandot)','Giacomo Puccini','1926'],['Habanera (Carmen)','Georges Bizet','1875'],
  ['William Tell Overture','Gioachino Rossini','1829'],['Ride of the Valkyries','Richard Wagner','1870'],
  ['The Blue Danube','Johann Strauss II','1866'],['Va, pensiero (Nabucco)','Giuseppe Verdi','1842'],
  ['La donna è mobile (Rigoletto)','Giuseppe Verdi','1851'],['Flower Duet (Lakmé)','Léo Delibes','1883'],
  ['Barcarolle (Tales of Hoffmann)','Jacques Offenbach','1881'],['Ave Maria','Charles Gounod','1853']],
 'classical-impressionist':[
  ['Finlandia','Jean Sibelius','1899'],['The Lark Ascending','R. Vaughan Williams','1914'],
  ['Pomp and Circumstance March No. 1','Edward Elgar','1901'],['Mars, the Bringer of War','Gustav Holst','1916'],
  ['Rhapsody in Blue','George Gershwin','1924'],['The Entertainer','Scott Joplin','1902'],
  ['The Stars and Stripes Forever','J.P. Sousa','1896'],['Vocalise','Sergei Rachmaninoff','1915'],
  ['Piano Concerto No. 2','Sergei Rachmaninoff','1901'],['Zigeunerweisen','Pablo de Sarasate','1878']],
 'folk-american':[
  ['Oh! Susanna','Stephen Foster','1848'],['Camptown Races','Stephen Foster','1850'],
  ['House of the Rising Sun','Traditional','traditional'],['Shenandoah','Traditional','traditional'],
  ['John Henry','Traditional','traditional'],['Midnight Special','Traditional','traditional'],
  ['Wayfaring Stranger','Traditional','traditional'],['Man of Constant Sorrow','Dick Burnett','1913'],
  ['I\'ll Fly Away','A.E. Brumley','1929'],['Home on the Range','Traditional','1873']],
 'folk-british-irish':[
  ['Scarborough Fair','Traditional','traditional'],['Greensleeves','Traditional','16th c.'],
  ['Auld Lang Syne','Robert Burns','1788'],['Danny Boy','Traditional','traditional'],
  ['Molly Malone','Traditional','1883'],['Whiskey in the Jar','Traditional','traditional'],
  ['The Wild Rover','Traditional','traditional'],['Loch Lomond','Traditional','traditional'],
  ['Waltzing Matilda','Traditional','1895'],['The Parting Glass','Traditional','traditional']],
 'folk-world':[
  ['La Cucaracha','Traditional','traditional'],['Cielito Lindo','Q. Mendoza','1882'],
  ['Guantanamera','Traditional','traditional'],['Hava Nagila','Traditional','traditional'],
  ['Sakura Sakura','Traditional','traditional'],['Arirang','Traditional','traditional'],
  ['Kalinka','Ivan Larionov','1860'],['Funiculì, Funiculà','Luigi Denza','1880']],
 'spirituals-hymns':[
  ['Amazing Grace','John Newton','1779'],['Swing Low, Sweet Chariot','Traditional','c.1865'],
  ['Go Down, Moses','Traditional','spiritual'],['Wade in the Water','Traditional','spiritual'],
  ['Simple Gifts','Joseph Brackett','1848'],['It Is Well with My Soul','H. Spafford','1873'],
  ['Abide with Me','Henry Lyte','1847'],['Come, Thou Fount','Robert Robinson','1757'],
  ['When the Saints Go Marching In','Traditional','traditional'],['This Little Light of Mine','Traditional','traditional']],
 'blues-early-jazz':[
  ['St. Louis Blues','W.C. Handy','1914'],['Memphis Blues','W.C. Handy','1912'],
  ['Downhearted Blues','Hunter/Austin','1923'],['Nobody Knows You When You\'re Down and Out','Ida Cox','1923'],
  ['Alexander\'s Ragtime Band','Irving Berlin','1911'],['Blue Skies','Irving Berlin','1926'],
  ['Over There','G.M. Cohan','1917'],['Take Me Out to the Ball Game','Norworth/Von Tilzer','1908'],
  ['Shine On, Harvest Moon','Norworth/Bayes','1908'],['I\'m Forever Blowing Bubbles','John Kellette','1919']],
 'seasonal-christmas':[
  ['Silent Night','Gruber/Mohr','1818'],['Jingle Bells','J.L. Pierpont','1857'],
  ['Deck the Halls','Traditional','traditional'],['O Holy Night','Adolphe Adam','1847'],
  ['Joy to the World','Watts/Mason','1836'],['Hark! The Herald Angels Sing','Wesley/Mendelssohn','1840'],
  ['O Come, All Ye Faithful','Traditional','18th c.'],['The First Noel','Traditional','traditional'],
  ['Away in a Manger','Traditional','1885'],['God Rest Ye Merry, Gentlemen','Traditional','traditional']],
 'anthems':[
  ['The Star-Spangled Banner','F.S. Key','1814'],['God Save the King','Traditional','traditional'],
  ['La Marseillaise','Rouget de Lisle','1792'],['O Canada','C. Lavallée','1880'],
  ['Advance Australia Fair','P.D. McCormick','1878'],['Deutschlandlied','Haydn/von Fallersleben','1841']]
};
var GENRES=Object.keys(POOL);
var GUIDE_ANGLES=[
 ['First listen','What to notice the first time you hear it — the opening gesture, the main theme, and the moment everything changes.'],
 ['Deep background','The story behind the music: who wrote it, when, and what was happening in the world at the time.'],
 ['Structure tour','How the piece is built — movements, sections, and the architecture holding it together.'],
 ['Performance notes','What performers wrestle with: tempo choices, famous interpretations, and the hard passages.'],
 ['Why it endures','Why this music survived centuries — the emotional core that keeps listeners returning.'],
 ['For newcomers','A friendly on-ramp: no jargon, just what to feel for and when to lean in.']];
var PLAYLIST_THEMES=[
 ['Rainy afternoon','Music for grey skies and a warm room.'],
 ['Morning energy','Bright openings to start the day.'],
 ['Deep focus','Steady, spacious music for concentration.'],
 ['Celebration','Joyful music for good news.'],
 ['Quiet night','Gentle music for the end of the day.'],
 ['Road trip','Singable, rolling music for the long road.'],
 ['Study hall','Calm, even-tempered companions for work.'],
 ['Grand occasions','Ceremonial music for big moments.']];
function normGenre(g){
 if(!g) return null;
 var t=String(g).toLowerCase().trim().replace(/[^a-z0-9]+/g,'-').replace(/^-+|-+$/g,'');
 if(POOL[t]) return t;
 for(var i=0;i<GENRES.length;i++){ if(GENRES[i].indexOf(t)>=0||t.indexOf(GENRES[i])>=0) return GENRES[i]; }
 return null;
}
function buildGuideIdx(w,ang,genre,topic,rnd,ed){
 var title='Listening Guide: '+w[0]+' — '+ang[0]+((ed&&ed>1)?' (Vol. '+ed+')':'');
 var desc='A '+ang[0].toLowerCase()+' guide to "'+w[0]+'" by '+w[1]+' ('+w[2]+'). '+ang[1]+(topic?' Requested theme: '+topic+'.':'');
 return {title:title,description:desc,kind:'listening-guide',
  content:{work:w[0],composer:w[1],year:w[2],genre:genre,angle:ang[0],guide_text:ang[1],
   listen_for:['The opening gesture — how the piece announces itself','The main theme and where it returns','The emotional peak — usually two-thirds through','The ending — how the composer lets go'],
   tip:'Listen once all the way through without reading, then read the guide and listen again.'},
  demo:{kind:'guide-checklist',program:'["opening","theme return","peak","ending"].forEach(function(x,i){console.log((i+1)+". "+x);});',note:'Paste into any JS console as a listening checklist.'}};
}
function buildPlaylistIdx(th,vol,genre,topic,rnd){
 var gs=shuffle(rnd,GENRES).slice(0,4);
 var tracks=[];
 gs.forEach(function(g2){ var w=pick(POOL[g2],rnd); tracks.push({work:w[0],composer:w[1],year:w[2],genre:g2}); });
 var title='Playlist: '+th[0]+' — Vol. '+vol+(topic?' — '+topic:'');
 var desc='A themed playlist for "'+th[0].toLowerCase()+'": '+th[1]+' '+tracks.length+' public-domain works from the archive, sequenced for flow.'+(topic?' Theme request: '+topic+'.':'');
 return {title:title,description:desc,kind:'themed-playlist',
  content:{theme:th[0],volume:vol,mood:th[1],tracks:tracks,how_to:'Play in order. Each track is a real public-domain work from the archive — search its title on the Archive tab.'},
  demo:{kind:'playlist-order',program:JSON.stringify(tracks.map(function(t,i){return (i+1)+'. '+t.work+' — '+t.composer;}),null,1),note:'The play order.'}};
}
function generate(seed,opts,rnd){
 opts=opts||{}; rnd=rnd||prng(seed);
 var topic=(opts.topic||'').toString().trim().slice(0,120);
 var idx=Math.max(0,(seed|0)-1);
 var g=normGenre(opts.genre)||GENRES[idx%GENRES.length];
 var isGuide=(idx%2===0);
 var b;
 if(isGuide){
  var n=Math.floor(idx/2);
  var gg=normGenre(opts.genre);
  var guse=gg||GENRES[n%GENRES.length];
  var pool=POOL[guse];
  var wi=Math.floor(n/GENRES.length)%pool.length;
  var ai=Math.floor(n/(GENRES.length*pool.length))%GUIDE_ANGLES.length;
  var cyc=GENRES.length*pool.length*GUIDE_ANGLES.length;
  var ed=Math.floor(n/cyc)+1;
  b=buildGuideIdx(pool[wi],GUIDE_ANGLES[ai],guse,topic||null,rnd,ed);
  g=guse;
 }else{
  var ti=Math.floor(idx/2)%PLAYLIST_THEMES.length;
  var vol=Math.floor(idx/(2*PLAYLIST_THEMES.length))+1;
  b=buildPlaylistIdx(PLAYLIST_THEMES[ti],vol,g,topic||null,rnd);
 }
 var id=PREFIX+String(seed).padStart(6,'0');
 return {id:id,title:b.title,description:b.description,genre:g,type:b.kind,
  content:b.content,demo:b.demo,src:'signature',_seed:seed,topic:topic||undefined,
  note:'Curatorial guide — the musical works referenced are real public-domain works; this guide text is Signature-authored.'};
}
function validate(r){
 var e=[];
 if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
 if(!/^JAH-PMUS-\d{6}$/.test(r.id||''))e.push('id');
 if(typeof r.title!=='string'||r.title.length<8)e.push('title');
 if(typeof r.description!=='string'||r.description.length<60)e.push('description');
 if(GENRES.indexOf(r.genre)<0)e.push('genre');
 if(r.type!=='listening-guide'&&r.type!=='themed-playlist')e.push('type');
 if(!r.content||typeof r.content!=='object')e.push('content');
 return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
 var dups=(sample||[]).filter(function(r){return r&&r.title===record.title;});
 return dups.length?{ok:false,errors:['duplicate title in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-public-music-1.0',generate:generate,validate:validate,driftCheck:driftCheck,genres:GENRES};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-music',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
