/* SIGNATURE — JAH Databases generator. Property of Justin Addam Higgins (JAH).
   Generator for the JAH Intel Signature Archive Database.
   Deterministic: same seed + version always makes the same record.
   Address space: seeds 1..1000000. Slots 1..600000 -> Class 1 (Signature versions of
   actual Intel products; alludes_to carries the nominative reference only).
   Slots 600001..1000000 -> Class 2 (original forward concepts; title is 'Class 2 ' + name).
   signature_name is always fully original and never contains the company trademark. */
(function(){'use strict';
var CFG={"slug":"intel","name":"JAH Intel Signature Archive Database","id_prefix":"JAH-INTC-","company":"Intel","forbidden":["intel","xeon","pentium","celeron","optane","vpro","thunderbolt","nuc","\\bcore\\b","\\barc\\b"],"categories":[{"id":"processors","label":"Processors","fam":"compute","kind2":"Compute Engine"},{"id":"mobile","label":"Mobile Processors","fam":"compute","kind2":"Mobile Compute Unit"},{"id":"server","label":"Server Processors","fam":"compute","kind2":"Rack Compute Node"},{"id":"graphics","label":"Graphics","fam":"gpu","kind2":"Visual Compute Card"},{"id":"networking","label":"Networking","fam":"network","kind2":"Fabric Adapter"},{"id":"chipsets","label":"Chipsets","fam":"chip","kind2":"Platform Logic Set"}],"products":[{"cat":"processors","ref":"Intel Core Ultra 9 285K — 24-core (8P+16E) desktop processor","year":2024,"kind":"Compute Engine","audience":"desktop builders and gamers","facts":"24 cores with a 5.7 GHz boost and 125 W base power on the LGA 1851 platform","specs":{"cores":24,"threads":24,"p_cores":8,"e_cores":16,"boost_ghz":5.7,"base_power_w":125,"max_turbo_power_w":250,"socket":"LGA 1851","memory":"DDR5-6400"}},{"cat":"processors","ref":"Intel Core Ultra 7 265K — 20-core desktop processor","year":2024,"kind":"Compute Engine","audience":"enthusiasts and creators","facts":"20 cores with a 5.5 GHz boost and 125 W base power on LGA 1851","specs":{"cores":20,"threads":20,"p_cores":8,"e_cores":12,"boost_ghz":5.5,"base_power_w":125,"max_turbo_power_w":250,"socket":"LGA 1851","memory":"DDR5-6400"}},{"cat":"processors","ref":"Intel Core Ultra 5 245K — 14-core desktop processor","year":2024,"kind":"Compute Engine","audience":"mainstream builders","facts":"14 cores with a 5.2 GHz boost and 159 W maximum turbo power","specs":{"cores":14,"threads":14,"p_cores":6,"e_cores":8,"boost_ghz":5.2,"base_power_w":125,"max_turbo_power_w":159,"socket":"LGA 1851","memory":"DDR5-6400"}},{"cat":"processors","ref":"Intel Core i9-14900K — 24-core desktop processor","year":2023,"kind":"Compute Engine","audience":"gamers and overclockers","facts":"24 cores and 32 threads with a 6.0 GHz boost on LGA 1700","specs":{"cores":24,"threads":32,"p_cores":8,"e_cores":16,"boost_ghz":6,"base_power_w":125,"max_turbo_power_w":253,"socket":"LGA 1700","memory":"DDR5-5600"}},{"cat":"processors","ref":"Intel Core i7-14700K — 20-core desktop processor","year":2023,"kind":"Compute Engine","audience":"gamers and streamers","facts":"20 cores and 28 threads with a 5.6 GHz boost","specs":{"cores":20,"threads":28,"boost_ghz":5.6,"base_power_w":125,"socket":"LGA 1700"}},{"cat":"processors","ref":"Intel Core i5-14600K — 14-core desktop processor","year":2023,"kind":"Compute Engine","audience":"value-focused builders","facts":"14 cores and 20 threads with a 5.3 GHz boost","specs":{"cores":14,"threads":20,"boost_ghz":5.3,"base_power_w":125,"socket":"LGA 1700"}},{"cat":"mobile","ref":"Intel Core Ultra 9 288V (Lunar Lake) — 8-core mobile processor","year":2024,"kind":"Mobile Compute Unit","audience":"ultraportable laptop makers","facts":"8 cores with an NPU delivering 48 TOPS for on-device AI","specs":{"cores":8,"threads":8,"npu_tops":48,"graphics":"Arc 140V","memory":"LPDDR5X-8533","base_power_w":30}},{"cat":"mobile","ref":"Intel Core Ultra 7 155H (Meteor Lake) — 16-core mobile processor","year":2023,"kind":"Mobile Compute Unit","audience":"thin-and-light laptop makers","facts":"16 cores and 22 threads with integrated Arc graphics","specs":{"cores":16,"threads":22,"npu_tops":11,"base_power_w":28}},{"cat":"server","ref":"Intel Xeon 6 6980P (Granite Rapids) — 128-core server processor","year":2024,"kind":"Rack Compute Node","audience":"data-center operators","facts":"128 cores and 256 threads inside a 500 W thermal envelope","specs":{"cores":128,"threads":256,"tdp_w":500,"socket":"LGA 7529","memory":"DDR5-6400 12-channel"}},{"cat":"server","ref":"Intel Xeon Platinum 8480+ — 56-core server processor","year":2023,"kind":"Rack Compute Node","audience":"enterprise data centers","facts":"56 cores and 112 threads at up to 3.8 GHz with 350 W TDP","specs":{"cores":56,"threads":112,"boost_ghz":3.8,"tdp_w":350,"socket":"LGA 4677"}},{"cat":"graphics","ref":"Intel Arc A770 — 16 GB desktop graphics card","year":2022,"kind":"Visual Compute Card","audience":"mainstream gamers","facts":"32 Xe cores paired with 16 GB of GDDR6 memory","specs":{"xe_cores":32,"vram_gb":16,"vram_type":"GDDR6","tdp_w":225,"outputs":"3x DisplayPort 2.0, 1x HDMI 2.1"}},{"cat":"graphics","ref":"Intel Arc B580 (Battlemage) — 12 GB desktop graphics card","year":2024,"kind":"Visual Compute Card","audience":"1080p and 1440p gamers","facts":"20 Xe2 cores with 12 GB of GDDR6 memory","specs":{"xe_cores":20,"vram_gb":12,"vram_type":"GDDR6","tdp_w":190}},{"cat":"networking","ref":"Intel Ethernet Network Adapter E810 — 100 GbE dual-port adapter","year":2019,"kind":"Fabric Adapter","audience":"data-center network teams","facts":"dual 100-gigabit ports with application device queues","specs":{"ports":2,"speed_gbps":100,"interface":"PCIe 4.0 x16","features":"ADQ, DDP"}},{"cat":"chipsets","ref":"Intel Z890 chipset — LGA 1851 platform controller","year":2024,"kind":"Platform Logic Set","audience":"motherboard designers","facts":"20 PCIe 5.0 lanes with Thunderbolt 4 and DDR5-6400 support","specs":{"pcie5_lanes":20,"usb":"10x USB 3.2","memory":"DDR5-6400","socket":"LGA 1851"}},{"cat":"networking","ref":"Intel Thunderbolt 5 controller (Barlow Ridge) — 120 Gbps connectivity","year":2024,"kind":"Fabric Adapter","audience":"dock and display makers","facts":"80 Gbps bidirectional with a 120 Gbps boost mode for displays","specs":{"bandwidth_gbps":80,"boost_gbps":120,"display":"3x 4K144 or 2x 8K","power_delivery_w":240}}]};
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
var gen={version:'jahdb-intel-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('intel',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
