/* SIGNATURE — JAH Databases generator. Property of Justin Addam Higgins (JAH).
   Generator for the JAH Sony Signature Archive Database.
   Deterministic: same seed + version always makes the same record.
   Address space: seeds 1..1000000. Slots 1..600000 -> Class 1 (Signature versions of
   actual Sony products; alludes_to carries the nominative reference only).
   Slots 600001..1000000 -> Class 2 (original forward concepts; title is 'Class 2 ' + name).
   signature_name is always fully original and never contains the company trademark. */
(function(){'use strict';
var CFG={"slug":"sony","name":"JAH Sony Signature Archive Database","id_prefix":"JAH-SONY-","company":"Sony","forbidden":["\\bsony\\b","playstation","dualsense","bravia","walkman","\\balpha\\b","exmor","xperia","aibo"],"categories":[{"id":"gaming","label":"Gaming","fam":"console","kind2":"Game Console"},{"id":"cameras","label":"Cameras","fam":"camera","kind2":"Mirrorless Camera"},{"id":"audio","label":"Audio","fam":"audio","kind2":"Quiet Headphones"},{"id":"televisions","label":"Televisions","fam":"display","kind2":"OLED Television"},{"id":"sensors","label":"Imaging Sensors","fam":"sensor","kind2":"Image Sensor"},{"id":"mobile","label":"Mobile","fam":"phone","kind2":"Slate Phone"}],"products":[{"cat":"gaming","ref":"Sony PlayStation 5 — home game console","year":2020,"kind":"Game Console","audience":"gamers","facts":"ultra-fast SSD with ray-tracing graphics and 4K output","specs":{"storage":"825 GB SSD","output":"4K/120","ray_tracing":true,"audio":"Tempest 3D"}},{"cat":"gaming","ref":"Sony PlayStation 5 Pro — enhanced game console","year":2024,"kind":"Game Console","audience":"enthusiast gamers","facts":"a mid-generation refresh with faster GPU and AI upscaling","specs":{"gpu":"+67% compute units","upscaling":"PSSR AI","storage":"2 TB"}},{"cat":"gaming","ref":"Sony DualSense — wireless game controller","year":2020,"kind":"Haptic Controller","audience":"console gamers","facts":"haptic feedback with adaptive triggers","specs":{"haptics":true,"triggers":"adaptive","charging":"USB-C"}},{"cat":"gaming","ref":"Sony PlayStation VR2 — VR headset","year":2023,"kind":"Immersive Visor","audience":"console VR gamers","facts":"4K HDR VR with eye tracking for the home console","specs":{"display":"OLED 4K HDR","tracking":"inside-out + eye","haptics":"headset and controllers","resolution":"2000x2040 per eye"}},{"cat":"cameras","ref":"Sony Alpha 7 IV — full-frame mirrorless camera","year":2021,"kind":"Mirrorless Camera","audience":"hybrid photo-video shooters","facts":"33 MP full-frame sensor with 4K 60p video","specs":{"mp":33,"sensor":"full-frame","video":"4K60p","ibis":true}},{"cat":"cameras","ref":"Sony Alpha 7R V — high-resolution mirrorless camera","year":2022,"kind":"Mirrorless Camera","audience":"landscape and studio photographers","facts":"61 MP sensor with AI-based subject recognition","specs":{"mp":61,"af":"AI subject recognition","video":"8K24p","ibis":true}},{"cat":"cameras","ref":"Sony Alpha 6700 — APS-C mirrorless camera","year":2023,"kind":"Mirrorless Camera","audience":"creators","facts":"26 MP APS-C with 4K 120p for creators","specs":{"mp":26,"sensor":"APS-C","video":"4K120p"}},{"cat":"cameras","ref":"Sony ZV-1 — vlogging compact camera","year":2020,"kind":"Vlog Camera","audience":"vloggers","facts":"1-inch sensor with a flip screen and directional mic","specs":{"sensor":"1-inch","screen":"flip","mic":"directional 3-capsule"}},{"cat":"audio","ref":"Sony WH-1000XM5 — noise-canceling headphones","year":2022,"kind":"Quiet Headphones","audience":"travelers and office workers","facts":"leading noise canceling with 30-hour battery","specs":{"anc":true,"battery_hr":30,"codecs":"LDAC","weight_g":250}},{"cat":"audio","ref":"Sony WH-1000XM6 — noise-canceling headphones","year":2025,"kind":"Quiet Headphones","audience":"travelers","facts":"newest processor with a fold-flat design","specs":{"anc":true,"battery_hr":30,"foldable":true}},{"cat":"audio","ref":"Sony WF-1000XM5 — noise-canceling earbuds","year":2023,"kind":"True Wireless Buds","audience":"commuters","facts":"compact buds with strong ANC and 24-hour total battery","specs":{"anc":true,"battery_hr":24,"water":"IPX4"}},{"cat":"televisions","ref":"Sony BRAVIA 8 II — QD-OLED television","year":2025,"kind":"OLED Television","audience":"home cinema fans","facts":"QD-OLED panel in 55 and 65-inch sizes","specs":{"panel":"QD-OLED","sizes_in":"55, 65","hdr":"Dolby Vision"}},{"cat":"televisions","ref":"Sony BRAVIA 9 II — RGB mini-LED television","year":2026,"kind":"Mini-LED Television","audience":"home cinema fans","facts":"true RGB mini-LED backlight in sizes up to 115 inches","specs":{"backlight":"RGB mini-LED","sizes_in":"65-115","hdr":"Dolby Vision","sound":"acoustic multi-audio"}},{"cat":"sensors","ref":"Sony IMX989 — 1-inch smartphone image sensor","year":2022,"kind":"Image Sensor","audience":"phone makers","facts":"a 1-inch stacked sensor for flagship phone cameras","specs":{"size":"1-inch","mp":50,"type":"stacked CMOS"}},{"cat":"mobile","ref":"Sony Xperia 1 VI — flagship smartphone","year":2024,"kind":"Slate Phone","audience":"camera-focused phone buyers","facts":"4K OLED display with camera tech derived from the mirrorless line","specs":{"display":"4K OLED 120Hz","camera":"triple 48 MP","battery_mah":5000}}]};
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function r1(s,a,b){return Math.round((a+s()*(b-a))*10)/10;}
var ADJ=['Apex','Nova','Vertex','Pulse','Zenith','Forge','Lumen','Vector','Halo','Strata','Flux','Ember','Onyx','Cirrus','Dynamo','Keystone','Beacon','Quantum','Nebula','Solstice','Meridian','Axiom','Cobalt','Drift','Echo','Flint','Grove','Harbor','Ion','Jade','Kite','Lark','Mist','North','Opal','Prism','Quill','Ridge','Sable','Talon','Umber','Vale','Wren','Zephyr','Alto','Brio','Cinder','Dune','Elm','Fern','Glade','Heath','Iris','Lotus','Mesa'];
var TIER=['Prime','Max','Elite','Plus','Pro','X','S','GT','LX','One'];
function catById(id){for(var i=0;i<CFG.categories.length;i++)if(CFG.categories[i].id===id)return CFG.categories[i];return null;}
function sigName(rnd,kind,isC2){var n=pick(ADJ,rnd)+' '+kind+' '+pick(TIER,rnd);if(rnd()<0.45)n+=' '+ri(rnd,2,9);if(isC2)n+=' Concept';return n;}
function c2Specs(rnd,fam){
var sp={};
if(fam==='compute'){var c=ri(rnd,16,512);sp.cores=c;sp.threads=c*2;sp.boost_ghz=r1(rnd,5.5,8.5);sp.process_nm=pick(['2','1.6','1'],rnd);sp.tdp_w=ri(rnd,15,1000);sp.memory=pick(['DDR6-8800','DDR6-9600','HBM4'],rnd);}
else if(fam==='gpu'){sp.vram_gb=pick([24,32,48,64,96,128],rnd);sp.compute_units=ri(rnd,64,256);sp.ray_tracing='generation '+ri(rnd,4,7);sp.tdp_w=ri(rnd,200,900);sp.memory_type='GDDR8';}
else if(fam==='vehicle'){sp.range_mi=ri(rnd,400,900);sp.zero_sixty_s=r1(rnd,1.2,3.5);sp.battery_kwh=ri(rnd,90,220);sp.charge_kw=ri(rnd,350,1000);sp.drive=pick(['AWD','tri-motor','quad-motor'],rnd);}
else if(fam==='energy'){sp.capacity_kwh=r1(rnd,20,200);sp.power_kw=ri(rnd,15,120);sp.cycles=ri(rnd,6000,15000);sp.chemistry=pick(['LFP','sodium-ion','solid-state'],rnd);}
else if(fam==='robot'){sp.degrees_of_freedom=ri(rnd,28,60);sp.payload_kg=r1(rnd,10,80);sp.runtime_hr=r1(rnd,8,48);sp.sensors=pick(['full vision plus tactile','vision plus lidar plus tactile'],rnd);}
else if(fam==='autonomy'){sp.compute_tops=ri(rnd,2000,20000);sp.sensors=pick(['vision plus radar plus lidar','full vision array'],rnd);sp.redundancy=pick(['dual','triple'],rnd);sp.updates='continuous over-the-air';}
else if(fam==='switch'||fam==='network'){sp.ports=ri(rnd,24,96);sp.speed_gbps=pick([100,400,800],rnd);sp.switching_tbps=r1(rnd,12.8,204.8);sp.poe_w=ri(rnd,90,240);}
else if(fam==='router'){sp.throughput_tbps=r1(rnd,10,200);sp.ports_400g=ri(rnd,8,64);sp.power_efficiency='next-generation';}
else if(fam==='sec'){sp.throughput_gbps=ri(rnd,100,2000);sp.tls_inspection='line-rate';sp.ai_triage=true;sp.zero_trust='built-in';}
else if(fam==='wifi'){sp.standard=pick(['Wi-Fi 8','Wi-Fi 9'],rnd);sp.streams=ri(rnd,8,32);sp.peak_gbps=r1(rnd,20,100);sp.iot_radios=true;}
else if(fam==='collab'){sp.display_in=ri(rnd,27,86);sp.camera=pick(['8K','12K'],rnd);sp.ai_features='real-time translation plus framing';sp.audio='spatial array';}
else if(fam==='display'){sp.size_in=ri(rnd,43,115);sp.resolution=pick(['8K','16K'],rnd);sp.refresh_hz=ri(rnd,144,480);sp.brightness_nits=ri(rnd,2000,10000);}
else if(fam==='camera'){sp.mp=ri(rnd,50,200);sp.video=pick(['8K120p','12K60p'],rnd);sp.ibis=true;sp.af='AI subject tracking';}
else if(fam==='audio'){sp.anc_db=ri(rnd,35,60);sp.battery_hr=ri(rnd,40,120);sp.codecs='next-generation lossless';sp.spatial_audio=true;}
else if(fam==='console'){sp.compute_tflops=ri(rnd,40,200);sp.storage_tb=ri(rnd,2,16);sp.output=pick(['8K/120','16K/60'],rnd);sp.ai_upscaling=true;}
else if(fam==='chip'){sp.node_nm=pick(['1.6','1','0.7'],rnd);sp.transistor='CFET';sp.density_gain='+40 percent';sp.status='research';}
else if(fam==='pack'){sp.interposer=pick(['glass','silicon-photonic'],rnd);sp.reticle_x=r1(rnd,4,12);sp.bandwidth_tbps=r1(rnd,20,200);sp.bonding='hybrid';}
else if(fam==='rocket'){sp.height_m=ri(rnd,100,200);sp.leo_t=ri(rnd,150,500);sp.reusable='fully';sp.turnaround_hr=ri(rnd,1,24);sp.propellant='methalox';}
else if(fam==='craft'){sp.crew=ri(rnd,4,20);sp.duration_days=ri(rnd,30,1000);sp.docking='autonomous';sp.reusable=true;}
else if(fam==='engine'){sp.thrust_tf=ri(rnd,300,900);sp.isp_s=ri(rnd,360,420);sp.reuse_flights=ri(rnd,50,500);sp.propellant='CH4/LOX';}
else if(fam==='satnet'){sp.satellites=ri(rnd,10000,100000);sp.downlink_gbps=r1(rnd,1,20);sp.latency_ms=ri(rnd,5,30);sp.interlink='laser mesh';}
else if(fam==='vr'){sp.resolution=pick(['8K per eye','16K per eye'],rnd);sp.refresh_hz=ri(rnd,144,240);sp.fov_deg=ri(rnd,140,220);sp.weight_g=ri(rnd,80,200);sp.tracking='full body plus eye';}
else if(fam==='glasses'){sp.display=pick(['holographic','retinal projection'],rnd);sp.battery_hr=ri(rnd,12,48);sp.camera_mp=ri(rnd,24,100);sp.weight_g=ri(rnd,25,45);}
else if(fam==='ai'){sp.params_b=ri(rnd,500,5000);sp.context_k=ri(rnd,256,4096);sp.multimodal=true;sp.agentic=true;}
else if(fam==='platform'){sp.users_m=ri(rnd,500,5000);sp.worlds=ri(rnd,100000,10000000);sp.creator_revenue_share=r1(rnd,50,95);sp.xr_native=true;}
else if(fam==='laptop'){sp.display=pick(['tandem OLED','microLED'],rnd);sp.battery_hr=ri(rnd,24,72);sp.weight_kg=r1(rnd,0.5,1.2);sp.ai_tops=ri(rnd,100,1000);}
else if(fam==='server'){sp.sockets=ri(rnd,2,16);sp.cores_total=ri(rnd,256,4096);sp.memory_tb=r1(rnd,4,64);sp.cooling='liquid';}
else if(fam==='sensor'){sp.mp=ri(rnd,100,400);sp.size=pick(['1-inch','medium format'],rnd);sp.readout='global shutter';sp.dynamic_range_db=ri(rnd,90,130);}
else if(fam==='phone'){sp.display=pick(['rollable OLED','foldable microLED'],rnd);sp.battery_mah=ri(rnd,6000,12000);sp.camera_mp=ri(rnd,100,300);sp.satellite_link=true;}
else{sp.capability='next-generation';sp.horizon='forward concept';}
return sp;}
function c2Facts(sp){var ks=Object.keys(sp).slice(0,3);return ks.map(function(k){return k.replace(/_/g,' ')+' of '+sp[k];}).join(', ');}
var D1=[
'The {N} is a Signature-original {K} in the {C} family. It tracks the working profile of {R}: {F}. Introduced in {Y}, it serves {A}.',
'Built as the Signature version of {R}, the {N} reproduces its operational facts in original expression \u2014 {F}. Its {Y} release positioned it for {A}.',
'{R} is the nominative anchor for this record. The {N} carries the same working details \u2014 {F} \u2014 rendered as a fully original Signature work. It reached the market in {Y}, aimed at {A}.'
];
var D2=[
'The {N} is a Class 2 Signature concept in the {C} family. It sketches a {K} with {F}, aimed at a {Y} horizon. No existing product is referenced; this record is an original forward-looking work.',
'A Class 2 forward concept, the {N} explores what a {K} could become: {F}. Target horizon {Y}. It stands alone as a Signature-original work with no real-world counterpart.'
];
function fill(t,m){return t.replace(/\{(\w)\}/g,function(x,k){return m[k];});}
function buildClass1(seed,rnd,prod,cat){
var name=sigName(rnd,prod.kind,false);
var desc=fill(pick(D1,rnd),{N:name,K:prod.kind.toLowerCase(),C:cat.label.toLowerCase(),R:prod.ref,F:prod.facts,Y:prod.year,A:prod.audience});
var id=CFG.id_prefix+String(seed).padStart(7,'0');
return {id:id,title:name,signature_name:name,alludes_to:prod.ref,class:1,category:prod.cat,specs:prod.specs,description:desc,year:prod.year};}
function buildClass2(seed,rnd,cat){
var name=sigName(rnd,cat.kind2,true);
var sp=c2Specs(rnd,cat.fam);
var year=ri(rnd,2027,2035);
var desc=fill(pick(D2,rnd),{N:name,K:cat.kind2.toLowerCase(),C:cat.label.toLowerCase(),F:c2Facts(sp),Y:year});
var id=CFG.id_prefix+String(seed).padStart(7,'0');
return {id:id,title:'Class 2 '+name,signature_name:name,alludes_to:'No nominative reference \u2014 Class 2 original Signature concept in the '+cat.label.toLowerCase()+' lineage.',class:2,category:cat.id,specs:sp,description:desc,year:year};}
function generate(seed,opts,rnd){
opts=opts||{};rnd=rnd||prng(seed);
seed=Math.max(1,Math.floor(seed)||1);
var slot=(seed-1)%1000000;
var cls=slot<600000?1:2;
var cat=opts.category?catById(opts.category):null;
if(cls===1){
var pool=cat?CFG.products.filter(function(p){return p.cat===cat.id;}):CFG.products;
if(!pool.length)pool=CFG.products;
var prod=cat?pick(pool,rnd):pool[slot%pool.length];
return buildClass1(seed,rnd,prod,catById(prod.cat));}
if(!cat)cat=pick(CFG.categories,rnd);
return buildClass2(seed,rnd,cat);}
function validate(r){
var e=[];
if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
var idre=new RegExp('^'+CFG.id_prefix.replace(/[-]/g,'\\-')+'\\d{7}$');
if(!idre.test(r.id||''))e.push('id');
if(typeof r.signature_name!=='string'||!r.signature_name.length)e.push('signature_name');
else{var low=r.signature_name.toLowerCase();
for(var i=0;i<CFG.forbidden.length;i++){var fr=new RegExp(CFG.forbidden[i],'i');if(fr.test(r.signature_name)){e.push('trademark in signature_name: '+CFG.forbidden[i]);break;}}
if(/projected/i.test(r.signature_name))e.push('projected in signature_name');}
if(typeof r.alludes_to!=='string'||!r.alludes_to.length)e.push('alludes_to');
if(r.class!==1&&r.class!==2)e.push('class');
if(!catById(r.category))e.push('category');
if(!r.specs||typeof r.specs!=='object'||Array.isArray(r.specs)||Object.keys(r.specs).length<3)e.push('specs');
if(typeof r.description!=='string'||r.description.length<60)e.push('description');
else{var sents=r.description.split(/[.!?]+(?=\s|$)/).filter(function(s){return s.trim().length;});
if(sents.length<2||sents.length>4)e.push('description sentences');
if(/projected/i.test(r.description))e.push('projected in description');}
if(!Number.isInteger(r.year)||r.year<2000||r.year>2036)e.push('year');
if(r.class===1&&r.title!==r.signature_name)e.push('title');
if(r.class===2&&r.title!=='Class 2 '+r.signature_name)e.push('title');
if(/projected/i.test(r.title||''))e.push('projected in title');
return {ok:!e.length,errors:e};}
function driftCheck(rec,sample){
var e=[];(sample||[]).forEach(function(s){if(s&&s.id!==rec.id&&s.signature_name===rec.signature_name&&JSON.stringify(s.specs)===JSON.stringify(rec.specs))e.push('duplicate of '+s.id);});
return {ok:!e.length,errors:e};}
var gen={version:'jahdb-sony-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('sony',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
