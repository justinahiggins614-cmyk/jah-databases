(function(){'use strict';
/* Public 3D Models Database generator — jahdb-public-3d-models-1.0.
   Property of Justin Addam Higgins (JAH).
   Type 1 PUBLIC database: every catalog record references a real, verified
   public-domain or openly-licensed asset. The generator never invents assets:
   catalog picks come only from the verified catalog below (src:"public-harvest");
   curated kits are Signature-made guides built only from that catalog
   (src:"signature-generated-sample"). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function shuffle(s,arr){var a=arr.slice(),i,j,t;for(i=a.length-1;i>0;i--){j=(s()*(i+1))|0;t=a[i];a[i]=a[j];a[j]=t;}return a;}
var PREFIX='JAH-P3D-';
/* Verified catalog: full record objects minus id/src (added at build time). */
var CATALOG=[{"title": "Apollo 11 — View of the Moon", "description": "NASA's featured 3D asset: a detailed view of the Moon commemorating the Apollo 11 landing, built from real mission data. Free to download and use, mirrored on NASA's official GitHub. Source: NASA 3D Resources (United States). License: Public Domain (NASA).", "category": "space", "source": "NASA 3D Resources", "source_url": "https://nasa3d.arc.nasa.gov/models", "license": "Public Domain", "tags": ["moon", "apollo", "nasa"], "download_url": "https://github.com/nasa/NASA-3D-Resources/archive/refs/heads/master.zip", "license_url": "https://www.nasa.gov/nasa-brand-center/images-and-media/", "country": "United States", "region": "North America", "year": 2019, "formats": ["STL", "OBJ", "blend"], "preview_url": "https://assets.science.nasa.gov/dynamicimage/assets/science/cds/3d/resources/image/apollo-11---view-of-the-moon/preview.webp?w=640", "printable": true, "demo": {"kind": "model-preview", "program": "Download (STL/OBJ/blend): https://github.com/nasa/NASA-3D-Resources\nPreview: open the file in Blender, Windows 3D Viewer, or any online glTF/STL viewer.", "note": "Free 3D model download — no key needed."}}, {"title": "Pillars of Creation Nebula", "description": "NASA's latest 3D asset: the iconic Pillars of Creation rendered as a 3D-printable nebula sculpture from Hubble and Webb telescope data. Free to download and use. Source: NASA 3D Resources (United States). License: Public Domain (NASA).", "category": "space", "source": "NASA 3D Resources", "source_url": "https://nasa3d.arc.nasa.gov/models", "license": "Public Domain", "tags": ["nebula", "hubble", "printable"], "download_url": "https://github.com/nasa/NASA-3D-Resources/archive/refs/heads/master.zip", "license_url": "https://www.nasa.gov/nasa-brand-center/images-and-media/", "country": "United States", "region": "North America", "year": 2024, "formats": ["STL", "OBJ"], "preview_url": "https://assets.science.nasa.gov/dynamicimage/assets/science/cds/3d/resources/printable/pillars-of-creation/Pillars%20of%20Creation.png?w=640", "printable": true, "demo": {"kind": "model-preview", "program": "Download (STL/OBJ): https://github.com/nasa/NASA-3D-Resources\nPreview: open the file in Blender, Windows 3D Viewer, or any online glTF/STL viewer.", "note": "Free 3D model download — no key needed."}}, {"title": "NASA 3D Resources Hub", "description": "NASA's official repository of 3D models, 3D-printable models and textures from across its missions — spacecraft, planets, rovers and more, all free and without copyright, mirrored on GitHub. Source: NASA (United States). License: Public Domain (NASA).", "category": "space", "source": "NASA 3D Resources", "source_url": "https://nasa3d.arc.nasa.gov/models", "license": "Public Domain", "tags": ["nasa", "hub", "spacecraft"], "download_url": "https://github.com/nasa/NASA-3D-Resources/archive/refs/heads/master.zip", "license_url": "https://www.nasa.gov/nasa-brand-center/images-and-media/", "country": "United States", "region": "North America", "formats": ["STL", "OBJ", "blend", "FBX"], "printable": true, "demo": {"kind": "download", "program": "Download: https://github.com/nasa/NASA-3D-Resources\nWhole-repo ZIP of NASA 3D assets", "note": "Direct download link — free, no key needed."}}, {"title": "Smithsonian 3D Collection", "description": "The Smithsonian's open 3D collection: artifacts, fossils, sculptures and historic objects digitized in 3D and released CC0 — download, print and remix. Source: Smithsonian Institution (United States). License: CC0.", "category": "historical", "source": "Smithsonian Institution", "source_url": "https://3d.si.edu/", "license": "CC0", "tags": ["museum", "artifacts", "cc0"], "download_url": "https://3d.si.edu/", "license_url": "https://creativecommons.org/publicdomain/zero/1.0/", "country": "United States", "region": "North America", "formats": ["OBJ", "STL", "glTF"], "printable": true, "demo": {"kind": "download", "program": "Download: https://3d.si.edu/\nBrowse the collection and download any object free", "note": "Direct download link — free, no key needed."}}, {"title": "Poly Pizza", "description": "Thousands of free low-poly 3D models released CC0 by their creators: game-ready characters, props and environments with instant download. Source: Poly Pizza community (global). License: CC0.", "category": "objects", "source": "Poly Pizza", "source_url": "https://poly.pizza/", "license": "CC0", "tags": ["lowpoly", "game-assets", "cc0"], "download_url": "https://poly.pizza/", "license_url": "https://creativecommons.org/publicdomain/zero/1.0/", "region": "Global", "formats": ["GLB", "OBJ", "FBX"], "printable": false, "demo": {"kind": "download", "program": "Download: https://poly.pizza/\nSearch and download any model free", "note": "Direct download link — free, no key needed."}}, {"title": "Printables Model Library", "description": "Prusa's community 3D-printing library: hundreds of thousands of free printable models — tools, toys, household fixes and art — with verified print profiles. Source: Prusa Research (Czechia). License: varies (many CC).", "category": "printable", "source": "Prusa Research", "source_url": "https://www.printables.com/", "license": "Various (many CC-BY)", "tags": ["3d-printing", "prusa"], "download_url": "https://www.printables.com/", "country": "Czechia", "region": "Europe", "formats": ["STL", "3MF", "STEP"], "printable": true, "demo": {"kind": "download", "program": "Download: https://www.printables.com/\nSearch printable models, download free", "note": "Direct download link — free, no key needed."}}, {"title": "Thingiverse", "description": "The world's largest 3D-printing design community: millions of free user-uploaded models under Creative Commons licenses, from gadgets to art. Source: MakerBot (United States). License: varies (CC).", "category": "printable", "source": "MakerBot", "source_url": "https://www.thingiverse.com/", "license": "Various (CC)", "tags": ["3d-printing", "community"], "download_url": "https://www.thingiverse.com/", "license_url": "https://creativecommons.org/", "country": "United States", "region": "North America", "formats": ["STL", "OBJ"], "printable": true, "demo": {"kind": "download", "program": "Download: https://www.thingiverse.com/\nSearch millions of free printable designs", "note": "Direct download link — free, no key needed."}}, {"title": "MyMiniFactory", "description": "Curated 3D-printable designs with guaranteed printability: every model test-printed by the community before it goes live. Source: MyMiniFactory (United Kingdom). License: varies (CC).", "category": "printable", "source": "MyMiniFactory", "source_url": "https://www.myminifactory.com/", "license": "Various (CC)", "tags": ["3d-printing", "curated"], "download_url": "https://www.myminifactory.com/", "license_url": "https://creativecommons.org/", "country": "United Kingdom", "region": "Europe", "formats": ["STL", "OBJ"], "printable": true, "demo": {"kind": "download", "program": "Download: https://www.myminifactory.com/\nBrowse curated printable models", "note": "Direct download link — free, no key needed."}}, {"title": "NIH 3D Print Exchange", "description": "The National Institutes of Health's collection of scientifically accurate 3D-printable models: anatomy, molecules, lab tools and more, free for education and research. Source: NIH (United States). License: Public Domain / CC.", "category": "anatomy", "source": "National Institutes of Health", "source_url": "https://3d.nih.gov/", "license": "Public Domain / CC", "tags": ["science", "anatomy", "education"], "download_url": "https://3d.nih.gov/", "country": "United States", "region": "North America", "formats": ["STL", "WRL"], "printable": true, "demo": {"kind": "download", "program": "Download: https://3d.nih.gov/\nDownload scientific models free", "note": "Direct download link — free, no key needed."}}, {"title": "Quaternius", "description": "A beloved CC0 game-asset pack: hundreds of charming low-poly characters, creatures, tiles and items, free for any use including commercial. Source: Quaternius (global). License: CC0.", "category": "characters", "source": "Quaternius", "source_url": "https://quaternius.com/", "license": "CC0", "tags": ["game-assets", "cc0", "lowpoly"], "download_url": "https://quaternius.com/", "license_url": "https://creativecommons.org/publicdomain/zero/1.0/", "region": "Global", "formats": ["GLB", "FBX", "OBJ", "blend"], "printable": false, "demo": {"kind": "download", "program": "Download: https://quaternius.com/\nDownload the complete CC0 packs free", "note": "Direct download link — free, no key needed."}}, {"title": "Sketchfab", "description": "The largest platform for 3D content on the web: millions of models, with a large free downloadable section under Creative Commons licenses. Source: Sketchfab (France/United States). License: varies (CC).", "category": "objects", "source": "Sketchfab", "source_url": "https://sketchfab.com/", "license": "Various (CC)", "tags": ["viewer", "marketplace"], "download_url": "https://sketchfab.com/", "license_url": "https://creativecommons.org/", "country": "France", "region": "Europe", "formats": ["GLB", "OBJ", "FBX", "USDZ"], "printable": false, "demo": {"kind": "download", "program": "Download: https://sketchfab.com/\nFilter by Downloadable + Creative Commons", "note": "Direct download link — free, no key needed."}}, {"title": "Blend Swap", "description": "The community library for Blender files: thousands of free .blend scenes, models and materials shared by Blender artists. Source: Blend Swap community (global). License: varies (CC).", "category": "objects", "source": "Blend Swap", "source_url": "https://www.blendswap.com/", "license": "Various (CC)", "tags": ["blender", "community"], "download_url": "https://www.blendswap.com/", "license_url": "https://creativecommons.org/", "region": "Global", "formats": ["blend"], "printable": false, "demo": {"kind": "download", "program": "Download: https://www.blendswap.com/\nDownload free Blender scenes", "note": "Direct download link — free, no key needed."}}, {"title": "OpenGameArt 3D", "description": "Free game art for open projects: 3D models, textures and sprites under GPL/CC0/CC-BY, made for and by indie developers. Source: OpenGameArt community (global). License: varies (GPL/CC0/CC-BY).", "category": "objects", "source": "OpenGameArt", "source_url": "https://opengameart.org/", "license": "Various (GPL/CC0/CC-BY)", "tags": ["game-assets", "indie"], "download_url": "https://opengameart.org/", "region": "Global", "formats": ["blend", "OBJ", "MD2"], "printable": false, "demo": {"kind": "download", "program": "Download: https://opengameart.org/\nBrowse free game-ready 3D art", "note": "Direct download link — free, no key needed."}}, {"title": "Free3D Model Archive", "description": "A large free 3D model archive: thousands of downloadable models in common formats for personal projects and learning. Source: Free3D (global). License: varies (free personal).", "category": "objects", "source": "Free3D", "source_url": "https://free3d.com/", "license": "Free for personal use", "tags": ["archive"], "download_url": "https://free3d.com/", "region": "Global", "formats": ["OBJ", "FBX", "3DS", "MAX"], "printable": false, "demo": {"kind": "download", "program": "Download: https://free3d.com/\nBrowse the free model archive", "note": "Direct download link — free, no key needed."}}, {"title": "CGTrader Free 3D Models", "description": "CGTrader's free section: a large selection of downloadable 3D models for personal and commercial use, royalty-free. Source: CGTrader (Lithuania). License: royalty-free.", "category": "objects", "source": "CGTrader", "source_url": "https://www.cgtrader.com/free-3d-models", "license": "Royalty-free", "tags": ["marketplace"], "download_url": "https://www.cgtrader.com/free-3d-models", "country": "Lithuania", "region": "Europe", "formats": ["OBJ", "FBX", "MAX", "C4D"], "printable": false, "demo": {"kind": "download", "program": "Download: https://www.cgtrader.com/free-3d-models\nBrowse free royalty-free models", "note": "Direct download link — free, no key needed."}}, {"title": "TurboSquid Free 3D Models", "description": "TurboSquid's free collection: professional-grade stock 3D models free for commercial use. Source: TurboSquid (United States). License: royalty-free.", "category": "objects", "source": "TurboSquid", "source_url": "https://www.turbosquid.com/Search/3D-Models/free", "license": "Royalty-free", "tags": ["marketplace", "stock"], "download_url": "https://www.turbosquid.com/Search/3D-Models/free", "country": "United States", "region": "North America", "formats": ["MAX", "OBJ", "FBX", "C4D"], "printable": false, "demo": {"kind": "download", "program": "Download: https://www.turbosquid.com/Search/3D-Models/free\nSearch free stock models", "note": "Direct download link — free, no key needed."}}, {"title": "Archive3D", "description": "A long-running free 3D model archive: thousands of models organized by category, free to download. Source: Archive3D (global). License: free for use.", "category": "objects", "source": "Archive3D", "source_url": "https://archive3d.net/", "license": "Free for use", "tags": ["archive"], "download_url": "https://archive3d.net/", "region": "Global", "formats": ["3DS", "MAX", "OBJ"], "printable": false, "demo": {"kind": "download", "program": "Download: https://archive3d.net/\nBrowse the free archive", "note": "Direct download link — free, no key needed."}}, {"title": "3D Warehouse", "description": "SketchUp's model library: millions of user-shared models of buildings, products and places — many free to download. Source: Trimble (United States). License: varies.", "category": "architecture", "source": "Trimble", "source_url": "https://3dwarehouse.sketchup.com/", "license": "Various", "tags": ["sketchup", "buildings"], "download_url": "https://3dwarehouse.sketchup.com/", "country": "United States", "region": "North America", "formats": ["SKP", "DAE"], "printable": false, "demo": {"kind": "download", "program": "Download: https://3dwarehouse.sketchup.com/\nSearch millions of shared models", "note": "Direct download link — free, no key needed."}}, {"title": "Yeggi 3D Model Search Engine", "description": "The 3D model search engine: searches across printable-model sites so one query finds free models everywhere. Source: Yeggi (Germany). License: varies.", "category": "printable", "source": "Yeggi", "source_url": "https://www.yeggi.com/", "license": "Various", "tags": ["search-engine"], "download_url": "https://www.yeggi.com/", "country": "Germany", "region": "Europe", "formats": ["STL"], "printable": true, "demo": {"kind": "download", "program": "Download: https://www.yeggi.com/\nOne search across all printable sites", "note": "Direct download link — free, no key needed."}}, {"title": "Stanford 3D Scanning Repository", "description": "The legendary computer-graphics test set: the Stanford Bunny, Happy Buddha, Dragon and Armadillo scans that benchmarked a generation of 3D research — free for research. Source: Stanford University (United States). License: free for research/education.", "category": "science", "source": "Stanford University", "source_url": "http://graphics.stanford.edu/data/3Dscanrep/", "license": "Free for research", "tags": ["stanford-bunny", "research"], "download_url": "http://graphics.stanford.edu/data/3Dscanrep/", "country": "United States", "region": "North America", "year": 1994, "formats": ["PLY"], "printable": true, "demo": {"kind": "download", "program": "Download: http://graphics.stanford.edu/data/3Dscanrep/\nDownload the famous scan models", "note": "Direct download link — free, no key needed."}}];
var THEMES=[["space-mission-kit", "The Space Mission Kit", "space", "Spacecraft, planets and rovers for your own mission control."], ["printable-workshop", "The Printable Workshop", "printable", "Tools, gadgets and fixes you can print tonight."], ["character-pack", "The Character Pack", "characters", "Game-ready characters and creatures, free to use."], ["architecture-set", "The Architecture Set", "architecture", "Buildings and places to drop into any scene."], ["nature-pack", "The Nature Pack", "nature", "Plants, rocks and creatures for living worlds."], ["vehicle-fleet", "The Vehicle Fleet", "vehicles", "Cars, planes and ships ready to roll."], ["anatomy-lab", "The Anatomy Lab", "anatomy", "Scientific models for learning and teaching."], ["historical-collection", "The Historical Collection", "historical", "Museum artifacts digitized for everyone."], ["scale-models", "The Scale Models Kit", "scale", "Precision scale models \u2014 architecture, vehicles, and landmarks at exact ratios."]];
var CATEGORIES=["space", "vehicles", "characters", "architecture", "nature", "objects", "anatomy", "science", "historical", "printable", "collection"];
/* ---- Expansion 2026-10-17: point clouds, spatial scenes with object metadata,
   CAD geometry libraries. Signature-authored dataset records (src:
   'signature-generated-sample'), clearly labeled; they extend the catalog, not
   the verified public-asset picks. ---- */
var GEOCATS=["point-cloud","spatial-scene","cad-geometry"];
GEOCATS.forEach(function(c){if(CATEGORIES.indexOf(c)<0)CATEGORIES.push(c);});
var PC_SOURCES=['terrestrial laser scan','photogrammetry reconstruction','aerial LiDAR survey','structured-light scan','depth-camera capture'];
var PC_SUBJECTS=['historic building facade','archaeological trench','bridge pier','factory floor','forest plot','museum gallery','rock outcrop','urban street canyon'];
var SCENE_SUBJECTS=['workshop interior','museum hall','construction site','laboratory bench','warehouse aisle','archaeological dig','observatory dome','classroom'];
var CAD_PARTS=['bearing housing','gear blank','bracket plate','pipe flange','enclosure box','shaft collar','motor mount','hinge leaf'];
var CAD_OPS=['extrude','revolve','loft','sweep','fillet','chamfer','boolean union','boolean difference','shell','pattern array'];
function buildGeo(seed,rnd,cat){
  var id=PREFIX+String(seed).padStart(6,'0');
  var rec={id:id,source:'JAH Signature generator',source_url:'',country:'',region:'Global',
    license:'CC0 (Signature-authored)',license_url:'https://creativecommons.org/publicdomain/zero/1.0/',
    src:'signature-generated-sample',_seed:seed};
  var i,items;
  if(cat==='point-cloud'){
    var subj=pick(PC_SUBJECTS,rnd),srcm=pick(PC_SOURCES,rnd);
    var pts=pick([250000,1200000,4800000,12500000,52000000],rnd);
    rec.title='Point cloud — '+subj+' ('+srcm+', #'+seed+')';
    rec.description='A Signature-authored point-cloud dataset record: '+pts.toLocaleString('en-US')+' points capturing a '+subj+' via '+srcm+'. Registered, cleaned, and classified; delivered as LAS/LAZ plus PLY. Labeled sample record — a real capture would replace these parameters.';
    rec.category=cat;
    rec.point_cloud={subject:subj,capture_method:srcm,point_count:pts,units:'meters',coordinate_reference:'local grid',classification:['ground','structure','vegetation','noise'],formats:['LAS','LAZ','PLY'],density_pts_per_m2:+(pts/pick([400,2500,9000],rnd)).toFixed(1)};
    rec.tags=['point-cloud','lidar','scan',subj.split(' ')[0]];
    rec.demo={kind:'point-cloud-inspector',program:'var p=record.point_cloud;console.log(p.subject+" — "+p.point_count+" points via "+p.capture_method);\nconsole.log("classes: "+p.classification.join(", "));',note:'Summarizes the point-cloud parameters.'};
  }else if(cat==='spatial-scene'){
    var ssub=pick(SCENE_SUBJECTS,rnd),n=ri(rnd,4,7);items=[];
    var objs=['workbench','cabinet','instrument','crate','lamp','shelf','door','window','pillar','machine','table','sensor rig'];
    for(i=0;i<n;i++){items.push({n:i+1,object:pick(objs,rnd)+' '+(i+1),position:[+((rnd()*8-4).toFixed(2)),+((rnd()*3).toFixed(2)),+((rnd()*8-4).toFixed(2))],rotation_deg:ri(rnd,0,359),scale:+((0.5+rnd()*1.5).toFixed(2)),material:pick(['steel','wood','glass','plastic','concrete'],rnd),label:pick(['furniture','equipment','structure','prop'],rnd)});}
    rec.title='Spatial scene — '+ssub+', '+n+' objects (#'+seed+')';
    rec.description='A Signature-authored spatial scene: a '+ssub+' with '+n+' placed objects, each carrying position, rotation, scale, material, and a semantic label. Scene graph is right-handed, Y-up, meters. Labeled sample record.';
    rec.category=cat;
    rec.scene={subject:ssub,object_count:n,up_axis:'Y',units:'meters',objects:items};
    rec.tags=['spatial-scene','scene-graph','3d'];
    rec.demo={kind:'scene-inspector',program:'record.scene.objects.forEach(function(o){console.log(o.n+". "+o.object+" @ ["+o.position.join(", ")+"] "+o.label);});',note:'Lists every object with its placement.'};
  }else{
    var part=pick(CAD_PARTS,rnd),n2=ri(rnd,4,6);items=[];
    for(i=0;i<n2;i++){items.push({n:i+1,operation:pick(CAD_OPS,rnd),parameters:'seeded parameters set #'+(i+1),result:'solid body '+(i+1)});}
    var dims=[ri(rnd,20,400),ri(rnd,20,400),ri(rnd,10,200)];
    rec.title='CAD geometry library — '+part+', '+n2+' features (#'+seed+')';
    rec.description='A Signature-authored CAD geometry record: a fully parametric '+part+' built from '+n2+' ordered modeling features ('+items.map(function(x){return x.operation;}).join(', ')+'). Envelope '+dims.join(' x ')+' mm. Delivered as STEP plus a feature tree. Labeled sample record — dimensions are illustrative.';
    rec.category=cat;
    rec.cad={part:part,feature_count:n2,envelope_mm:dims,features:items,formats:['STEP','IGES'],parametric:true,tolerance_mm:0.05};
    rec.tags=['cad','parametric','geometry',part.split(' ')[0]];
    rec.demo={kind:'cad-inspector',program:'var c=record.cad;console.log(c.part+" — "+c.feature_count+" features, envelope "+c.envelope_mm.join(" x ")+" mm");\nc.features.forEach(function(f){console.log(f.n+". "+f.operation);});',note:'Walks the feature tree in order.'};
  }
  return rec;
}
function catRecord(e,seed){
  var id=PREFIX+String(seed).padStart(6,'0');
  var r={id:id};
  Object.keys(e).forEach(function(k){ r[k]=e[k]; });
  r.src='public-harvest';
  r._seed=seed;
  return r;
}
function buildCollection(s,theme,topic){
  var pool=CATALOG.filter(function(e){return e.category===theme[2];});
  if(pool.length<3) pool=CATALOG.slice();
  var items=shuffle(s,pool).slice(0,ri(s,4,6));
  var title=(topic?('Kit: '+topic+' — '):'')+theme[1];
  var desc='A Signature-curated kit: '+theme[3]+' '+items.length+' hand-picked verified public assets, each free to use.'+(topic?' Themed around \u201c'+topic+'\u201d.':'');
  var list=items.map(function(e,i){return {n:i+1,title:e.title,download_url:e.download_url||e.read_url||e.source_url||'',license:e.license};});
  return {title:title,description:desc,category:'collection',theme:theme[0],
    items:list,
    demo:{kind:'kit-guide',program:list.map(function(x){return x.n+'. '+x.title+' — '+(x.download_url||'(see archive record)');}).join('\n'),note:'Open each download URL to get the asset, free.'},
    src:'signature-generated-sample',topic:topic||undefined};
}
function normTheme(t){
  if(!t) return null;
  var x=String(t).toLowerCase().trim().replace(/[^a-z0-9]+/g,'-');
  for(var i=0;i<THEMES.length;i++){ if(THEMES[i][0]===x||THEMES[i][0].indexOf(x)>=0||x.indexOf(THEMES[i][0])>=0) return THEMES[i]; }
  return null;
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var gf=opts.family&&GEOCATS.indexOf(opts.family)>=0?opts.family:null;
  if(gf)return buildGeo(seed,rnd,gf);
  var topic=(opts.topic||'').toString().trim().slice(0,120);
  var g=opts.genre?String(opts.genre).toLowerCase().trim():null;
  if(g&&GEOCATS.indexOf(g)>=0)return buildGeo(seed,rnd,g);
  var id=PREFIX+String(seed).padStart(6,'0');
  var b;
  if(g==='collection'||topic){
    var th=normTheme(g)||pick(THEMES,rnd);
    b=buildCollection(rnd,th,topic||null);
  }else{
    var e=CATALOG[(seed-1)%CATALOG.length];
    b=catRecord(e,seed); b._via='catalog-pick';
    return b;
  }
  b.id=id; b._seed=seed;
  return b;
}
function validUrl(u){ return typeof u==='string' && /^https?:\/\//.test(u); }
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.length<8)e.push('title');
  if(typeof r.description!=='string'||r.description.length<60)e.push('description');
  if(CATEGORIES.indexOf(r.category)<0)e.push('category');
  if(r.src!=='public-harvest'&&r.src!=='signature-generated-sample')e.push('src');
  if(r.category==='collection'){
    if(!Array.isArray(r.items)||!r.items.length)e.push('items');
    if(r.src!=='signature-generated-sample')e.push('src');
  }
  if(r.src==='public-harvest'&&!validUrl(r.source_url)&&!validUrl(r.download_url)&&!validUrl(r.read_url))e.push('url');
  if(!r.demo||typeof r.demo!=='object'||typeof r.demo.program!=='string'||!r.demo.program.length)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.t===record.title;});
  return dups.length?{ok:false,errors:['duplicate title in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-public-3d-models-1.0',generate:generate,validate:validate,driftCheck:driftCheck,genres:CATEGORIES,catalogSize:CATALOG.length};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-3d-models',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
