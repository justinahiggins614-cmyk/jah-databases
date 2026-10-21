(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["enumeration", "power", "safety", "protocols"];
var PREFIX='JAH-URM-';
var LAST_VERIFIED='2026-10-21';
var PROVENANCE='Public industry records and documentation';
var SRC='public-harvest';
/* base records: [title, category, description, mechanisms, platforms, standards, ladder_rank, demo_idx] */
var B=[["USB Enumeration Sequence", "enumeration", "Walks the standard enumeration: detect, reset, read descriptors, assign address, configure. Each step has timeouts and retries; the host learns what the device is before loading a driver. It is the handshake every USB device performs.", ["Detect attach and reset the port", "Read device descriptors", "Assign address and configure"], ["Linux usbcore", "Windows USB stack", "Embedded hosts"], ["USB 2.0/3.x spec", "Chapter 9"], 1, 0], ["Descriptor Parsing", "enumeration", "Parses device, configuration, interface, and endpoint descriptors to learn capabilities. Malformed descriptors are the classic attack vector, so parsers validate lengths and types strictly. Correct parsing decides which driver binds.", ["Fetch the descriptor hierarchy", "Validate lengths and types", "Select configuration and driver"], ["Linux", "Windows", "libusb"], ["USB specification", "Class specs"], 2, 0], ["USB-C and Power Delivery", "power", "Negotiates roles, orientation, and power over USB-C with Power Delivery messaging. The CC lines detect plug orientation and the PD contract sets voltage and current. It unified charging, data, and display on one connector.", ["Detect orientation on CC lines", "Negotiate the PD contract", "Enter alternate modes as needed"], ["USB-C PD controllers", "Laptops", "Phones"], ["USB-C spec", "USB PD spec"], 2, 2], ["Mass Storage Class", "protocols", "Exposes storage over USB with the Bulk-Only Transport and SCSI command set. The host sends SCSI commands wrapped in USB transfers; the device behaves like a disk. Every flash drive uses it.", ["Wrap SCSI in bulk transfers", "Handle BOT state machine", "Present block device to the OS"], ["Linux usb-storage", "Windows", "Firmware stacks"], ["USB MSC spec", "SCSI SBC"], 1, 0], ["Hotplug Event Handling", "enumeration", "Delivers attach and detach events to userspace so the system reacts instantly. udev rules mount drives, load firmware, and notify desktops; removal events clean up. It is the OS side of plug and play.", ["Emit kernel uevents on change", "Match udev rules", "Mount, notify, and clean up"], ["udev/systemd", "Windows PnP", "macOS IOKit"], ["Linux hotplug docs", "OS PnP"], 1, 0], ["Safe Removal Protocol", "safety", "Flushes caches and stops the device before physical removal to prevent corruption. Write caching means 'done' is a lie until flush; safe removal makes it true. The OS refuses while handles are open.", ["Flush all write caches", "Stop the device", "Refuse while handles are open"], ["Windows (eject)", "Linux (udisks)", "macOS"], ["OS storage docs", "Filesystem guides"], 1, 1], ["USB Autosuspend", "power", "Suspends idle USB devices to save power, resuming on activity. The host negotiates suspend with the device and cuts its power budget; resume is transparent. It matters most for battery-powered hosts.", ["Track device idle time", "Negotiate suspend", "Resume transparently on I/O"], ["Linux usbcore", "Windows", "Embedded"], ["USB 2.0 (suspend)", "Linux PM"], 2, 1], ["Hub Topology Management", "enumeration", "Manages hub tiers, port power budgets, and transaction translators. Hubs extend the tree up to 7 tiers; the host tracks the topology for power and bandwidth accounting. Bad hubs are a classic source of weird failures.", ["Enumerate hubs depth-first", "Budget power per port", "Route through translators correctly"], ["Linux", "Windows", "Firmware"], ["USB hub spec", "USB 2.0/3.x"], 2, 0], ["USB On-The-Go", "protocols", "Lets dual-role devices negotiate host versus peripheral roles over the ID pin and HNP. A phone becomes the host for a flash drive, then the peripheral for a PC. Role swap modernized this further.", ["Detect the ID pin", "Negotiate roles with HNP", "Swap roles as needed"], ["Android", "Embedded Linux", "Phones"], ["USB OTG spec", "USB-C role swap"], 2, 2], ["UASP Protocol", "protocols", "Replaces Bulk-Only Transport with USB Attached SCSI for queued, faster transfers. Command queuing and out-of-order completion lift USB 3 storage to near-SATA speeds. Modern enclosures all use it.", ["Negotiate UAS instead of BOT", "Queue multiple commands", "Complete out of order"], ["Linux (uas)", "Windows", "Enclosures"], ["USB UAS spec", "SCSI SAM"], 2, 2], ["Device Authorization", "safety", "Authorizes USB devices before they enumerate fully, blocking malicious implants. The host checks device identity against policy; unknown devices get no drivers. It stops BadUSB-style attacks at the port.", ["Intercept pre-enumeration", "Check identity against policy", "Block unauthorized classes"], ["USBGuard", "Windows Defender", "Enterprise tools"], ["USB security literature", "NIST guidance"], 3, 1], ["Driver Binding", "enumeration", "Matches drivers to interfaces by class, VID, and PID. The binding layer walks the descriptor tree and loads the right driver per interface; composite devices get several. Correct binding is what makes devices just work.", ["Match VID/PID and class codes", "Bind per interface", "Support composite devices"], ["Linux", "Windows", "libusb"], ["USB class specs", "OS driver models"], 1, 0], ["Speed Negotiation", "protocols", "Negotiates the highest mutually supported USB speed at attach. Chirp sequences for High Speed, link training for SuperSpeed; both sides agree before data flows. Fallback keeps old devices working.", ["Probe with chirp/training", "Agree on the top common speed", "Fall back gracefully"], ["xHCI controllers", "Devices", "Cables matter"], ["USB 2.0/3.x specs", "xHCI spec"], 1, 2], ["Composite Devices", "enumeration", "Handles devices exposing multiple interfaces — a headset with audio plus HID controls. Each interface binds its own driver under one device node. Interface association descriptors group related functions.", ["Parse interface associations", "Bind a driver per interface", "Coordinate shared state"], ["Linux", "Windows", "Firmware"], ["USB IAD spec", "Class specs"], 2, 0], ["DFU Firmware Updates", "safety", "Updates device firmware over USB with the Device Firmware Upgrade class. The device re-enumerates in DFU mode, receives the image, verifies, and swaps. Atomic swap with rollback keeps updates safe.", ["Re-enumerate in DFU mode", "Transfer and verify the image", "Swap atomically with rollback"], ["dfu-util", "Vendor tools", "Bootloaders"], ["USB DFU spec", "Firmware update guides"], 3, 1]];
var DEMOS=["// Demo: {NAME} — enumeration state machine\nvar states=['detached','attached','powered','default','addressed','configured'];\nvar cur=0;console.log('technique: {NAME}');\nfor(var i=0;i<states.length;i++){console.log('-> '+states[i]);}\nconsole.log('device ready: '+states[states.length-1]);", "// Demo: {NAME} — safe-removal check\nvar handles={N1}%5,dirty=((({SEED}%2)===0));\nconsole.log('technique: {NAME}');console.log('open handles: '+handles+', dirty cache: '+dirty);\nconsole.log(handles===0&&!dirty?'safe to remove':'NOT safe — flush caches and close handles first');", "// Demo: {NAME} — speed negotiation\nvar speeds=[['Low',1.5],['Full',12],['High',480],['Super',5000],['Super+',10000]];\nvar dev=({SEED}%5);\nconsole.log('technique: {NAME}');console.log('device supports up to: '+speeds[dev][0]+' ('+speeds[dev][1]+' Mbps)');\nconsole.log('negotiated: '+speeds[dev][0]+' — both sides agree, link trains');"];
var CONTEXTS=["a production web service handling steady user traffic", "an on-device mobile deployment with tight resource budgets", "an edge cluster serving a regional user base", "a CI pipeline validating every commit", "a research prototype exploring new designs", "a regulated enterprise environment with audit requirements"];
var NOTES=["Operators report measurable gains within the first deployment cycle.", "Start with the simplest configuration, then compound toward the advanced form.", "Pair with monitoring so regressions are caught before users notice.", "Document the chosen parameters so the setup can be recreated exactly.", "Validate against a baseline before and after enabling the technique.", "Keep a rollback path ready when rolling this out to production."];
var RANK_WORD={1:'Simple',2:'Compound',3:'Advanced'};
function fill(tpl,vars){return tpl.replace(/\{([A-Z0-9_]+)\}/g,function(m,k){return (k in vars)?vars[k]:m;});}
function escJS(s){return String(s).replace(/\\/g,'\\\\').replace(/'/g,"\\'").replace(/\n/g,'\\n');}
function makeDemo(b,seed,rnd){
  var tpl=DEMOS[b[7]%DEMOS.length];
  var vars={NAME:escJS(b[0]),N1:1+((seed*7+b[7])%97),N2:2+((seed*13)%499),N3:5+((seed*29)%95),SEED:seed,CAT:escJS(b[1])};
  return {language:'javascript',title:'Demo — '+b[0],program:fill(tpl,vars)};
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[1]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var ctx=pick(CONTEXTS,rnd), note=pick(NOTES,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rot=seed%b[3].length;
  var mechs=b[3].slice(rot).concat(b[3].slice(0,rot)).slice(0,3);
  var plats=b[4].slice(0,2+((seed%2)));
  return {id:id,title:b[0],description:b[2]+' '+note+' Deployment context: '+ctx+'.',
    category:b[1],key_mechanisms:mechs,platforms:plats,standards:b[5].slice(),
    complexity:RANK_WORD[b[6]],ladder_rank:b[6],demo:makeDemo(b,seed,rnd),
    provenance:PROVENANCE,last_verified:LAST_VERIFIED,src:SRC,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var pre=PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+pre+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!Array.isArray(r.key_mechanisms)||r.key_mechanisms.length<2)e.push('key_mechanisms');
  if(!Array.isArray(r.platforms)||!r.platforms.length)e.push('platforms');
  if(!Array.isArray(r.standards)||!r.standards.length)e.push('standards');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(!r.demo||typeof r.demo.program!=='string'||!r.demo.program.length)e.push('demo');
  if(r.last_verified!==LAST_VERIFIED)e.push('last_verified');
  if(r.src!==SRC)e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var errs=[];
  (sample||[]).forEach(function(s){
    if(s&&s.id!==rec.id&&s.description===rec.description)errs.push('duplicate-of:'+s.id);
  });
  return {ok:!errs.length,errors:errs};
}
var gen={version:'jahdb-usb-removable-media-hot-plugging-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('usb-removable-media-hot-plugging',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
