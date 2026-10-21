(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["os", "hardware", "network", "runtime", "behavioral"];
var PREFIX='JAH-PEEF-';
var USE="Used by licensing, anti-fraud, forensics, and debugging to identify where code ran.";
var FLD=[["signal", "Signal"], ["source", "Source"], ["stability", "Stability"]];
var DEMO="# {title} - fingerprint stability (python3)\nsignals={d1}\nstable={d2}\nmin_pct={d3}\npct=100.0*stable/signals\nprint(\"stable signals: %d/%d (%.1f%%)\" % (stable, signals, pct))\nprint(\"RELIABLE FINGERPRINT\" if pct >= min_pct else \"TOO VOLATILE\")\n";
var SIG=false;
var SRC="public-harvest";
var B=[["os", "OS Version String", "The kernel and distribution version, the coarsest but most available signal.", "OS Version String", "uname", "high", "24", "22", "85.0"], ["hardware", "CPU Feature Flags", "Instruction-set extensions (AVX, NEON) that distinguish CPU generations.", "CPU Feature Flags", "cpuid", "very high", "18", "17", "90.0"], ["network", "Kernel Build", "Exact kernel build string including distro patches.", "Kernel Build", "/proc/version", "high", "12", "11", "85.0"], ["runtime", "Environment Variables", "PATH, LANG, and app-specific variables that vary by deployment.", "Environment Variables", "environ", "medium", "30", "20", "60.0"], ["behavioral", "Hostname Hash", "Hashed hostname identifying the machine without exposing the name.", "Hostname Hash", "gethostname", "high", "8", "8", "95.0"], ["os", "MAC Address", "Network interface hardware address, stable per NIC.", "MAC Address", "interfaces", "very high", "6", "6", "95.0"], ["hardware", "Filesystem UUIDs", "Volume identifiers that survive reboots but change on reformat.", "Filesystem UUIDs", "blkid", "high", "10", "9", "90.0"], ["network", "Timezone Offset", "UTC offset revealing coarse geographic region.", "Timezone Offset", "tzdata", "medium", "4", "3", "70.0"], ["runtime", "Locale Settings", "Language and formatting locale of the runtime environment.", "Locale Settings", "locale", "medium", "6", "4", "60.0"], ["behavioral", "Installed Library Versions", "Versions of shared libraries that shift with patch cycles.", "Installed Library Versions", "package db", "medium", "40", "28", "65.0"], ["os", "GPU Driver Version", "Graphics driver version tied to hardware and update policy.", "GPU Driver Version", "driver API", "medium", "5", "4", "70.0"], ["hardware", "Timing Jitter Profile", "Microarchitectural timing signature from calibrated loops.", "Timing Jitter Profile", "rdtsc loops", "low", "16", "8", "40.0"], ["network", "Network Interface List", "Names and types of interfaces (eth, wlan, vpn) describing connectivity.", "Network Interface List", "netlink", "medium", "7", "5", "65.0"], ["runtime", "Process Tree Shape", "Parent process chain revealing launchers (systemd, docker, IDE).", "Process Tree Shape", "procfs", "medium", "9", "6", "60.0"], ["behavioral", "Container Cgroup Path", "Cgroup hierarchy exposing container runtimes and orchestration.", "Container Cgroup Path", "/proc/self/cgroup", "high", "5", "5", "90.0"], ["os", "Cloud Metadata Endpoint", "Instance type, region, and ID from the cloud metadata service.", "Cloud Metadata Endpoint", "169.254.169.254", "very high", "12", "12", "95.0"], ["hardware", "CPUID Serial", "Processor serial where exposed, the strongest hardware signal.", "CPUID Serial", "cpuid", "very high", "3", "3", "98.0"], ["network", "Boot ID", "Random per-boot identifier from the kernel.", "Boot ID", "/proc/sys/kernel/random/boot_id", "per-boot", "2", "0", "10.0"], ["runtime", "Font Inventory", "Installed font list that varies strongly across desktops.", "Font Inventory", "fontconfig", "medium", "120", "85", "70.0"], ["behavioral", "Screen Resolution", "Display geometry, weak alone but useful in combination.", "Screen Resolution", "display server", "low", "4", "2", "40.0"]];
function buildTitle(b){ return SIG?('Signature '+b[1]):b[1]; }
function buildDesc(b){
  var d=b[2]+' Recorded facts \u2014 '+FLD[0][1]+': '+b[3]+'; '+FLD[1][1]+': '+b[4]+'; '+FLD[2][1]+': '+b[5]+'. '+USE;
  if(SIG) d='Signature-original: '+d+' Built as a Signature-authored original for the JAH network; clearly labeled Signature and never presented as a public record.';
  return d;
}
function buildDemo(b){
  return DEMO.split('{title}').join(b[1]).split('{d1}').join(b[6]).split('{d2}').join(b[7]).split('{d3}').join(b[8]);
}
function generate(seed,opts){
  opts=opts||{}; var rnd=prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title=buildTitle(b);
  var fields={}; fields[FLD[0][0]]=b[3]; fields[FLD[1][0]]=b[4]; fields[FLD[2][0]]=b[5];
  if(SIG) fields['signature_label']='Signature-authored original';
  return {id:id,title:title,description:buildDesc(b),category:cat,fields:fields,
    ladder_rank:1+(seed%3),
    demo:'# '+title+' \u2014 runnable demo (python3)\n'+buildDemo(b),
    provenance:'JAH Databases \u00b7 lane N3 build',last_verified:'2026-10-21',src:SRC,_seed:seed};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){
    if(sample[i]&&sample[i].title===rec.title&&sample[i].category===rec.category)
      return {ok:false,errors:['duplicate of archive record '+sample[i].id]};
  }
  return {ok:true,errors:[]};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var idre=new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$');
  if(!idre.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('print(')<0)e.push('demo');
  if(['public-harvest','signature-generated-completion'].indexOf(r.src)<0)e.push('src');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-program-execution-environment-fingerprint-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('program-execution-environment-fingerprint',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
