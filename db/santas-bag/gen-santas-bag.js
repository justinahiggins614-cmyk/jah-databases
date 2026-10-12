(function(){'use strict';
/* JAH Santa's Bag Database generator — jahdb-santas-bag-1.0.
   "Santa's Workshop" — this database only.
   Property of Justin Addam Higgins (JAH).
   Every record is a PRESENT: a full creation wrapped like a Christmas gift.
   Auto-creation rules: software → full app, hardware → 3D printer plans,
   patents → full patent file, both → both. Deterministic: same seed = same present.
   src:"signature" = Signature-authored original (clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a>>>0)+0x6D2B79F5|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function prng2(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function shuffle(s,arr){var a=arr.slice(),i,j,t;for(i=a.length-1;i>0;i--){j=(s()*(i+1))|0;t=a[i];a[i]=a[j];a[j]=t;}return a;}
var PREFIX='JAH-SB-';
/* ---------------- present pools ---------------- */
var WRAPS=['Candy-Cane Stripes','Golden Bell Foil','North-Star Silver','Holly-Berry Red','Frosted Pine Green','Reindeer Brown Kraft','Snowflake White','Midnight Workshop Blue'];
var RIBBONS=['Crimson','Gold','Silver','Emerald','Icy Blue','Candy Pink'];
var FOLDERS=['SantaBag/Items','SantaBag/Packages','SantaBag/Patents','SantaBag/3DPrinter','SantaBag/Software','SantaBag/Descriptions','SantaBag/Sidebar','SantaBag/WorkshopTheme'];
var APPS=[
 ['Starlight Task Manager','A full to-do app: add tasks, mark done, filter by priority, local save.',['Add a task with one tap','Check off done items','Filter: all / active / done','Priority stars','Auto-saves between sessions']],
 ['Workshop Inventory Tracker','A full inventory app: catalog toy parts, counts, low-stock alerts.',['Add parts with counts','Search the shelf','Low-stock warnings','Export the list','Auto-saves between sessions']],
 ['Reindeer Route Planner','A full route app: stops, order, distance estimate, check-off.',['Add delivery stops','Drag to reorder','Distance estimate per leg','Check off as delivered','Auto-saves between sessions']],
 ['Elf Shift Scheduler','A full scheduling app: elves, shifts, swap requests.',['Add elves and roles','Assign shifts by day','Swap request inbox','Weekly view','Auto-saves between sessions']],
 ['Gift Budget Keeper','A full budget app: gift list, costs, running total, per-person caps.',['Add gifts with prices','Per-person spending caps','Running total bar','Over-budget alerts','Auto-saves between sessions']],
 ['Snowfall Habit Tracker','A full habit app: daily check-ins, streaks, calendar heat map.',['Define habits','Daily check-in','Streak counter','Heat-map calendar','Auto-saves between sessions']]
];
var PLANS3D=[
 ['Toy Train Engine','A printable toy train engine: body, chimney, 4 wheels, coupler.',['Engine body (120×60×50 mm)','Chimney stack','4 flanged wheels','Front coupler','Assembly: press-fit, no glue']],
 ['Wooden-Style Toy Blocks','A printable alphabet block set: 6 cubes with raised letters.',['6 cubes, 40 mm each','Raised A–F letters','Rounded edges','Assembly: print, sand lightly']],
 ['Mini Sleigh','A printable miniature sleigh: runners, seat, gift bed.',['2 curved runners','Seat bench','Gift bed platform','Reinforcement ribs','Assembly: slot-fit runners to bed']],
 ['Spinning Top','A printable spinning top: stem, disc, tip.',['Twist stem','Weighted disc','Steel-tip socket','Assembly: press stem into disc']],
 ['Toy Castle Tower','A printable castle tower: cylinder, battlements, door, flag pole.',['Main cylinder','Battlement ring','Arched door','Flag pole','Assembly: stack and twist-lock']],
 ['Puzzle Cube Pieces','Printable interlocking puzzle pieces: 6 unique shapes.',['6 interlocking shapes','Alignment notches','Assembly: slide together in order']]
];
var PATENTS=[
 ['Self-Wrapping Gift Box','A box that folds itself shut when the lid is pressed.',['Rigid base with scored fold lines','Spring-loaded side panels','Lid with locking tabs','Release: press lid, panels snap shut']],
 ['Chimney-Fit Delivery Drone','A small drone sized to descend standard chimneys.',['Foldable rotor arms','Heat-shielded body','Gift gripper claw','Navigation: downward lidar']],
 ['Sleigh-Bell Proximity Alert','Bells that chime when a present is within arm\'s reach.',['Tuned bell set (C major)','Motion sensor','Chime hammer array','Power: single coin cell']],
 ['Snow-Melt Path Heater','A walkway mat that melts snow on contact.',['Heating grid layer','Insulated base','Pressure activation switch','Power: low-voltage DC']],
 ['Toy Assembly Jig','A jig that holds toy parts aligned during assembly.',['Adjustable clamps','Angle guides','Part trays','Assembly: bolt to bench']],
 ['Gift-Weight Balancer','A scale that balances gift weight across a sleigh.',['Load cells (4)','Balance display','Overload alarm','Calibration: one-button tare']]
];
var PACKAGES=[
 ['Workshop Starter Kit','A ready-to-run package: inventory app + 3D block plans + setup guide.',['inventory-app/ (full source)','3d-plans/blocks/ (print files)','setup-guide.txt','Run: open index.html']],
 ['Present Factory Demo','A ready-to-run package: present generator demo + catalog page.',['generator-demo/ (full source)','catalog-page/ (browse UI)','sample-presents.json','Run: open index.html']],
 ['Sleigh Systems Pack','A ready-to-run package: route planner app + bell alert plans.',['route-app/ (full source)','3d-plans/bell-alert/','wiring-notes.txt','Run: open index.html']],
 ['Elf Tools Bundle','A ready-to-run package: shift scheduler + task manager + habit tracker.',['scheduler-app/','tasks-app/','habits-app/','Run: open any index.html']]
];
var STORIES=[
 ['The Clockwork Caroler','A wind-up caroler that sings when the star is placed on the tree.'],
 ['Bramble the Brave Reindeer','A young reindeer who learns the northern lights are a map.'],
 ['The Last Snowflake','A snowflake that refuses to melt until every wish is delivered.'],
 ['Peppermint Express','A candy train that runs on kindness and arrives exactly on time.']
];
/* ---------------- builders ---------------- */
function buildApp(s,topic){
 var d=pick(APPS,s);
 var title=topic?('Present: '+topic+' (app, in the spirit of "'+d[0]+'")'):'Present: '+d[0]+' — Full App';
 return {title:title,
  description:'A complete, working app: "'+d[0]+'". '+d[1]+' Features: '+d[2].join('; ')+'. Wrapped and ready — open the file and it runs.',
  present_type:'software-app',
  creation:{app:d[0],overview:d[1],features:d[2],files:['index.html','app.js','style.css'],run:'Open index.html in any browser — no build step.'},
  demo:{kind:'runnable-app',program:'// '+d[0]+'\n// Files: index.html, app.js, style.css\n// Open index.html — the app runs as-is.',note:'Full app source ships with the record.'}};
}
function buildPlan(s,topic){
 var d=pick(PLANS3D,s);
 var title=topic?('Present: '+topic+' (3D plans, in the spirit of "'+d[0]+'")'):'Present: '+d[0]+' — Full 3D Plans';
 return {title:title,
  description:'Complete 3D printer plans: "'+d[0]+'". '+d[1]+' Parts: '+d[2].join('; ')+'. '+d[3],
  present_type:'hardware-3d-plans',
  creation:{model:d[0],overview:d[1],parts:d[2],assembly:d[3],files:['model.stl.notes.txt','parts-list.txt','assembly-guide.txt'],run:'Slice the STL notes per your printer; follow the assembly guide.'},
  demo:{kind:'assembly-guide',program:d[2].join('\n'),note:'Parts list — print each, then assemble.'}};
}
function buildPatent(s,topic){
 var d=pick(PATENTS,s);
 var title=topic?('Present: '+topic+' (patent, in the spirit of "'+d[0]+'")'):'Present: '+d[0]+' — Full Patent File';
 return {title:title,
  description:'A full patent-style file: "'+d[0]+'". '+d[1]+' Claims: '+d[2].join('; ')+'. '+d[3],
  present_type:'patent-file',
  creation:{invention:d[0],field:'Workshop devices',background:d[1],claims:d[2],embodiment:d[3],files:['patent.txt','claims.txt','figures.txt']},
  demo:null};
}
function buildPackage(s,topic){
 var d=pick(PACKAGES,s);
 var title=topic?('Present: '+topic+' (package, in the spirit of "'+d[0]+'")'):'Present: '+d[0]+' — Ready-to-Run Package';
 return {title:title,
  description:'A ready-to-run package: "'+d[0]+'". '+d[1]+' Contents: '+d[2].join('; ')+'. '+d[3],
  present_type:'ready-package',
  creation:{pack:d[0],overview:d[1],contents:d[2],run:d[3],files:d[2]},
  demo:{kind:'run-instructions',program:d[3],note:'Follow the run line — it just works.'}};
}
function buildStory(s,topic){
 var d=pick(STORIES,s);
 var title=topic?('Present: '+topic+' (storybook)'):'Present: '+d[0]+' — Storybook';
 return {title:title,
  description:'A Christmas storybook present: "'+d[0]+'". '+d[1]+' A full tale to read aloud, wrapped like a gift.',
  present_type:'storybook',
  creation:{story:d[0],premise:d[1],chapters:['The Workshop Wakes','A Small Problem','The Clever Fix','Home by Starlight'],files:['story.txt']},
  demo:null};
}
function buildMixed(s,topic){
 var a=pick(APPS,s), p=pick(PLANS3D,s);
 var title='Present: '+(topic||a[0]+' + '+p[0])+' — App + 3D Plans';
 return {title:title,
  description:'A double present: the full "'+a[0]+'" app AND complete 3D printer plans for "'+p[0]+'". Software and hardware together, one ribbon.',
  present_type:'app-and-hardware',
  creation:{app:{name:a[0],features:a[2]},hardware:{model:p[0],parts:p[2]},files:['app/index.html','3d-plans/notes.txt']},
  demo:{kind:'runnable-app',program:'// '+a[0]+' — open app/index.html',note:'App runs as-is; print the hardware plans.'}};
}
var BUILDERS={'software-app':buildApp,'hardware-3d-plans':buildPlan,'patent-file':buildPatent,'ready-package':buildPackage,'storybook':buildStory,'app-and-hardware':buildMixed};
var TYPES=Object.keys(BUILDERS);
var FAMS=TYPES.map(function(t){return {g:t,t:t.replace(/-/g,' '),type:'christmas present'};});
/* ---------------- main ---------------- */
function normType(g){
 if(!g) return null;
 var t=String(g).toLowerCase().trim().replace(/[^a-z0-9]+/g,'-').replace(/^-+|-+$/g,'');
 if(BUILDERS[t]) return t;
 for(var i=0;i<TYPES.length;i++){ if(TYPES[i].indexOf(t)>=0||t.indexOf(TYPES[i])>=0) return TYPES[i]; }
 return null;
}
function generate(seed,opts,rnd){
 opts=opts||{}; rnd=rnd||prng2(seed);
 var topic=(opts.topic||'').toString().trim().slice(0,120);
 var t=normType(opts.genre)||pick(TYPES,rnd);
 var b=BUILDERS[t](rnd,topic||null);
 var id=PREFIX+String(seed).padStart(6,'0');
 var wrap=pick(WRAPS,rnd), ribbon=pick(RIBBONS,rnd), folder=pick(FOLDERS,rnd);
 return {id:id,title:b.title,description:b.description,genre:t,type:'christmas present',
  present_type:b.present_type,wrap:wrap,ribbon:ribbon,folder:folder,
  catalog:'The Boundless Christmas Catalog',
  content:b.creation,demo:b.demo,src:'signature',
  workshop:'Santa\'s Workshop',_seed:seed,topic:topic||undefined};
}
function validate(r){
 var e=[];
 if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
 if(!/^JAH-SB-\d{6}$/.test(r.id||''))e.push('id');
 if(typeof r.title!=='string'||r.title.length<8)e.push('title');
 if(typeof r.description!=='string'||r.description.length<60)e.push('description');
 if(TYPES.indexOf(r.genre)<0)e.push('genre');
 if(!r.content||typeof r.content!=='object')e.push('content');
 if(typeof r.wrap!=='string'||!r.wrap)e.push('wrap');
 if(typeof r.folder!=='string'||!r.folder)e.push('folder');
 return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
 var dups=(sample||[]).filter(function(r){return r&&r.title===record.title;});
 return dups.length?{ok:false,errors:['duplicate title in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-santas-bag-1.0',generate:generate,validate:validate,driftCheck:driftCheck,genres:TYPES};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('santas-bag',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
