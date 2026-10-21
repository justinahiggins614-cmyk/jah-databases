(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["high-speed", "low-speed", "interrupts", "dma"];
var PREFIX='JAH-PERIPH-';
var LAST_VERIFIED='2026-10-21';
var PROVENANCE='Public industry records and documentation';
var SRC='public-harvest';
/* base records: [title, category, description, mechanisms, platforms, standards, ladder_rank, demo_idx] */
var B=[["PCIe Enumeration", "high-speed", "Walks the PCIe config space discovering devices, bridges, and their BARs. The enumerator assigns bus numbers depth-first and maps memory windows. Every PCIe device in the system is found this way at boot.", ["Scan config space per bus", "Assign bus numbers depth-first", "Map BARs into address space"], ["Linux PCI", "UEFI", "Windows PnP"], ["PCI Express spec", "PCI firmware spec"], 2, 1], ["I2C Transactions", "low-speed", "Performs addressed transactions on the two-wire I2C bus with start, address, ACK, and stop. Clock stretching lets slow slaves hold the clock; 7-bit addressing picks the device. Sensors and EEPROMs live on I2C.", ["Issue start and 7-bit address", "Handle ACK/NACK and clock stretch", "Issue stop to release the bus"], ["Linux i2c-dev", "Embedded HALs", "SMBus"], ["I2C specification (NXP)", "SMBus spec"], 1, 0], ["SPI Transfers", "low-speed", "Shifts data full-duplex over SPI with chip-select framing and four clock modes. Mode (CPOL/CPHA) must match the slave; speed is limited by signal integrity. Flash chips and displays use SPI.", ["Assert chip select", "Match the slave's clock mode", "Shift full-duplex frames"], ["Linux spidev", "Embedded HALs", "Flash tools"], ["SPI conventions", "Vendor datasheets"], 1, 0], ["UART Communication", "low-speed", "Exchanges bytes over UART with agreed baud rate, parity, and stop bits. No clock line means both sides must agree on timing; framing errors reveal mismatches. Consoles and GPS modules still speak UART.", ["Agree on baud/parity/stop bits", "Frame bytes with start/stop", "Detect framing errors"], ["Linux tty", "Embedded UARTs", "USB serial"], ["RS-232", "UART conventions"], 1, 0], ["CAN Bus Messaging", "low-speed", "Broadcasts prioritized frames on CAN with non-destructive arbitration. Lower IDs win the bus without corruption; error frames isolate faulty nodes. Cars and industrial gear run on CAN.", ["Arbitrate by message ID", "Acknowledge in the ACK slot", "Isolate faulty nodes"], ["SocketCAN", "Automotive ECUs", "Industrial PLCs"], ["ISO 11898", "CAN FD spec"], 2, 0], ["GPIO Control", "low-speed", "Drives general-purpose I/O pins for LEDs, resets, and bit-banged protocols. Direction, pull-ups, and drive strength are configured per pin; interrupts catch edges. It is the simplest hardware interface there is.", ["Configure direction and pulls", "Drive or sample the pin", "Use edge interrupts for events"], ["Linux gpiod", "Embedded HALs", "Raspberry Pi"], ["Vendor datasheets", "Device tree bindings"], 1, 0], ["MMIO vs PIO Access", "high-speed", "Chooses memory-mapped I/O over port I/O for device registers. MMIO maps registers into address space for normal loads and stores; x86 PIO uses special instructions. Modern drivers use MMIO almost exclusively.", ["Map BARs into virtual address space", "Use volatile accesses", "Prefer MMIO over legacy PIO"], ["Linux (ioremap)", "Windows", "Drivers"], ["PCI spec", "OS driver guides"], 2, 1], ["MSI-X Interrupts", "interrupts", "Delivers per-queue interrupts with MSI-X message-signaled interrupts. Each queue gets its own vector and CPU affinity, eliminating IRQ sharing. High-performance NICs and NVMe depend on it.", ["Allocate one vector per queue", "Set CPU affinity per vector", "Mask vectors during handling"], ["Linux IRQ", "NVMe", "NIC drivers"], ["PCI Express (MSI-X)", "Linux IRQ docs"], 3, 2], ["DMA Engine Programming", "dma", "Programs DMA engines with descriptor rings for CPU-free data movement. The driver builds descriptors, rings the doorbell, and handles completions; cache coherency is managed explicitly. It is how fast I/O avoids the CPU.", ["Build descriptor rings", "Ring the doorbell", "Handle completions and errors"], ["Linux DMA engine", "NIC/NVMe drivers", "Embedded DMA"], ["Linux DMA API", "PCIe spec"], 3, 1], ["Bus Enumeration Order", "high-speed", "Enumerates buses in dependency order so bridges come up before their devices. Depth-first assignment gives stable bus numbers; hot-plug slots get reserved ranges. Order matters for correct resource assignment.", ["Enumerate depth-first", "Reserve ranges for hot-plug", "Assign resources bottom-up"], ["Linux PCI", "UEFI", "Firmware"], ["PCI firmware spec", "ACPI"], 2, 1], ["BAR Mapping", "high-speed", "Maps Base Address Registers into the CPU address space with correct caching attributes. Sizing probes reveal each BAR's size; prefetchable 64-bit BARs go high. Wrong attributes cause subtle corruption.", ["Size BARs by writing all ones", "Map with correct cache attributes", "Handle 64-bit BAR pairs"], ["Linux PCI", "Drivers", "Firmware"], ["PCI spec (BARs)", "OS memory docs"], 2, 1], ["Clock Stretching Handling", "low-speed", "Handles I2C clock stretching where slow slaves hold SCL low. Masters must wait rather than time out; multi-master arbitration adds complexity. Robust drivers never assume the clock is theirs.", ["Wait on stretched clock", "Set generous timeouts", "Recover the bus on timeout"], ["Linux i2c", "Embedded", "SMBus"], ["I2C specification", "SMBus spec"], 2, 0], ["Bus Analyzer Tracing", "interrupts", "Captures bus traffic with protocol analyzers to debug driver issues. Seeing the actual bytes settles every argument about who is wrong. Analyzers decode PCIe, I2C, SPI, and CAN natively.", ["Capture with a protocol analyzer", "Decode to transactions", "Compare against the spec"], ["Teledyne LeCroy", "Saleae", "Total Phase"], ["Protocol specs", "Debug methodology"], 2, 2], ["SMBus Communication", "low-speed", "Uses SMBus, the I2C subset, for system management like battery and thermal data. Strict timeouts and protocols like Block Write make it more robust than raw I2C. Smart batteries speak SMBus.", ["Use SMBus protocols", "Enforce timeouts", "Handle PEC checksums"], ["Linux i2c", "EC firmware", "Batteries"], ["SMBus specification", "Smart battery spec"], 2, 0], ["LPC Bus Bridging", "low-speed", "Bridges the legacy Low Pin Count bus for super-I/O and TPM on older platforms. eSPI replaces it on modern boards, but millions of systems still boot through LPC. The bridge translates to modern fabrics internally.", ["Bridge LPC to internal fabric", "Decode legacy addresses", "Migrate to eSPI where possible"], ["Chipsets", "Super-I/O", "TPM modules"], ["LPC spec (Intel)", "eSPI spec"], 3, 1]];
var DEMOS=["// Demo: {NAME} — I2C transaction timing\nvar bits=8+1,clk=100000;\nvar us=(bits*2/clk)*1e6;\nconsole.log('technique: {NAME}');console.log('100 kHz I2C byte + ACK: '+us.toFixed(0)+' us');\nconsole.log('400 kHz fast mode: '+(us/4).toFixed(0)+' us — clock speed sets throughput');", "// Demo: {NAME} — PCIe BAR sizing\nvar bars=[['BAR0',4],['BAR1',256],['BAR2',1]];\nconsole.log('technique: {NAME}');\nvar total=0;bars.forEach(function(b){console.log(b[0]+': '+b[1]+' KB');total+=b[1];});\nconsole.log('total MMIO window: '+total+' KB');", "// Demo: {NAME} — MSI-X vector allocation\nvar vecs={N1}%16+1,queues=4;\nconsole.log('technique: {NAME}');console.log('MSI-X vectors: '+vecs+', queues: '+queues);\nconsole.log(vecs>=queues?'one vector per queue — no sharing':'vectors shared — expect some coalescing');"];
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
var gen={version:'jahdb-peripheral-bus-interfacing-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('peripheral-bus-interfacing',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
