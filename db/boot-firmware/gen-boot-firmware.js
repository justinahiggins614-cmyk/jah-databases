(function(){'use strict';
/* JAH The Boot and Firmware Database generator — jahdb-boot-firmware-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FW-";
var FIELDS=["firmware"];
var TOPICS={
 "firmware": [
  "UEFI Firmware \u2014 firmware",
  "BIOS Firmware \u2014 firmware",
  "Bootloaders \u2014 firmware",
  "Stage-1 Bootloaders \u2014 firmware",
  "Stage-2 Bootloaders \u2014 firmware",
  "EFI Executables \u2014 firmware",
  "Kernel Images \u2014 firmware",
  "Flat Kernels \u2014 firmware",
  "Higher-Half Kernels \u2014 firmware",
  "Monolithic Kernel Images \u2014 firmware",
  "Microkernel Servers \u2014 firmware",
  "Multiboot Kernels \u2014 firmware",
  "Initramfs Images \u2014 firmware",
  "Initial RAM Disks \u2014 firmware",
  "crt0 Startup \u2014 firmware",
  "Linker Scripts \u2014 firmware",
  "Interrupt Vector Tables \u2014 firmware",
  "Global Descriptor Tables \u2014 firmware",
  "Page Table Builders \u2014 firmware",
  "Framebuffer Drivers \u2014 firmware",
  "ACPI Tables \u2014 firmware",
  "Device Trees \u2014 firmware",
  "SMBIOS Tables \u2014 firmware",
  "Coreboot \u2014 firmware",
  "U-Boot \u2014 firmware",
  "Barebox \u2014 firmware",
  "SeaBIOS \u2014 firmware",
  "EDK II \u2014 firmware",
  "OpenSBI \u2014 firmware",
  "ARM Trusted Firmware \u2014 firmware",
  "Power-On Self-Test \u2014 firmware",
  "Memory Training \u2014 firmware",
  "PCI Enumeration \u2014 firmware",
  "USB Initialization \u2014 firmware",
  "SATA Initialization \u2014 firmware",
  "NVMe Boot \u2014 firmware",
  "Network Boot ROMs \u2014 firmware",
  "iPXE \u2014 firmware",
  "Boot Menus \u2014 firmware",
  "Boot Splashes \u2014 firmware",
  "Handoff Protocols \u2014 firmware",
  "ExitBootServices \u2014 firmware",
  "Runtime Services \u2014 firmware",
  "Variable Stores \u2014 firmware",
  "Capsule Updates \u2014 firmware",
  "Secure Boot Chains \u2014 firmware",
  "Measured Boot \u2014 firmware",
  "Verified Boot \u2014 firmware",
  "Boot Guard \u2014 firmware",
  "Firmware Volumes \u2014 firmware",
  "Flash Descriptors \u2014 firmware",
  "ME Firmware \u2014 firmware",
  "BMC Firmware \u2014 firmware",
  "EC Firmware \u2014 firmware",
  "Touch Firmware \u2014 firmware",
  "SSD Firmware \u2014 firmware",
  "HDD Firmware \u2014 firmware",
  "NIC Firmware \u2014 firmware",
  "GPU VBIOS \u2014 firmware"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Boot Firmware — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — firmware record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A firmware record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-boot-firmware-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('boot-firmware',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
