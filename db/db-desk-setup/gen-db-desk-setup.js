(function(){'use strict';
/* The The Desk Setup Database generator — jahdb-db-desk-setup-pub-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-DESK-SETUP-PUB-";
var GENVER="jahdb-db-desk-setup-pub-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The Student Starter Desk",
  "Laptop-Only Minimal Setup",
  "The Budget Builder Desk",
  "Dorm Room Desk Rescue",
  "The Kitchen-Table Workstation",
  "Lighting First: The $30 Glow-Up",
  "Cable Management Crash Course",
  "Ergonomics in Ten Minutes",
  "The Analog Corner",
  "Small-Space Wall Desk",
  "The Reading Nook Desk",
  "Shared Desk, Two People"
 ],
 "Compounded": [
  "The Dual-Monitor Productivity Rig",
  "Gaming Battlestation Basics",
  "The Art Corner Studio",
  "Standing Desk Conversion",
  "The Streaming-Ready Desk",
  "Music Production Nook",
  "The Craft and Maker Bench",
  "Ultrawide Immersion Setup",
  "The Couple\u2019s Command Center",
  "Portable Pro Kit",
  "The Monitor Arm Upgrade",
  "The Focus Lighting Rig"
 ],
 "Advanced": [
  "The Dream Battlestation",
  "Home Office, Executive Grade",
  "The Triple-Threat Creator Desk",
  "Acoustic-Treated Focus Room",
  "The Sit-Stand-Walk Station",
  "Multi-User Family Hub",
  "The Workshop Command Desk",
  "Smart Desk Automation",
  "The Legacy Studio Build",
  "Setup Photography Masterclass"
 ]
};
var BLURBS={
 "The Student Starter Desk": "A compact, affordable study station: good light, clear surface, and everything for homework within reach. Focus is the feature.",
 "Laptop-Only Minimal Setup": "One laptop, one stand, one keyboard. A full workstation that fits in a backpack and sets up anywhere.",
 "The Budget Builder Desk": "A complete desk setup under a tight budget: thrifted desk, solid chair, smart lighting. Proof that money is not the bottleneck.",
 "Dorm Room Desk Rescue": "Tiny room, shared space, big workload. Vertical storage and quiet gear make a dorm desk actually work.",
 "The Kitchen-Table Workstation": "No dedicated room? A portable kit turns any table into a proper workstation and packs away in five minutes.",
 "Lighting First: The $30 Glow-Up": "Before buying anything else, fix the light. A warm desk lamp and bias lighting transform any setup instantly.",
 "Cable Management Crash Course": "One hour, velcro ties, and a cable tray. Turn spaghetti into invisible and never think about it again.",
 "Ergonomics in Ten Minutes": "Raise the screen, support the feet, un-hunch the shoulders. The fastest comfort upgrade in desk history.",
 "The Analog Corner": "Paper planner, notebook, pen cup. Sometimes the best setup upgrade is less screen, not more.",
 "Small-Space Wall Desk": "A fold-down wall desk for rooms with no floor to spare. Work happens, then the room is yours again.",
 "The Reading Nook Desk": "A desk built for books and notes rather than screens: warm light, deep surface, zero glare.",
 "Shared Desk, Two People": "One desk, two users, zero fights: split zones, labeled storage, and a reset ritual between shifts.",
 "The Dual-Monitor Productivity Rig": "Two screens, one workflow: reference on the left, work on the right. Multitasking without the chaos.",
 "Gaming Battlestation Basics": "High-refresh screen, responsive input, and lighting that sets the mood. Competitive comfort for long sessions.",
 "The Art Corner Studio": "A desk that welcomes mess: big surface, daylight lamp, and supply storage that invites creating.",
 "Standing Desk Conversion": "A riser or adjustable frame for sit-stand days. Movement built into the workday.",
 "The Streaming-Ready Desk": "Camera angle, mic arm, and key light positions planned from day one. Look pro before you go live.",
 "Music Production Nook": "Monitors at ear height, interface within reach, and a surface that respects the gear. Small room, big sound.",
 "The Craft and Maker Bench": "Sturdy top, task lighting, and tool storage for hands-on projects. Built to take a beating beautifully.",
 "Ultrawide Immersion Setup": "One sweeping screen replaces two. Fewer bezels, deeper focus, cleaner cables.",
 "The Couple\u2019s Command Center": "Bills, calendars, and family admin in one organized station. Adulting, centralized.",
 "Portable Pro Kit": "A go-bag that recreates your desk anywhere: stand, keyboard, mouse, hub, light. Work from anywhere, ergonomically.",
 "The Monitor Arm Upgrade": "Free the desk surface: floating screens, perfect angles.",
 "The Focus Lighting Rig": "Bias light plus task lamp: eye comfort for long sessions.",
 "The Dream Battlestation": "No-compromise gaming and creating station: top-tier display, acoustics, and lighting scenes. The endgame setup.",
 "Home Office, Executive Grade": "A professional video-call-ready office: background, lighting, and audio that say you mean business.",
 "The Triple-Threat Creator Desk": "Edit video, stream, and design from one command center with scene-switching at your fingertips.",
 "Acoustic-Treated Focus Room": "Panels, placement, and quiet gear turn a noisy home into a concentration chamber.",
 "The Sit-Stand-Walk Station": "Desk, treadmill, and balance board: the workstation that keeps you moving all day.",
 "Multi-User Family Hub": "One station serving homework, work-from-home, and bills with personal profiles and quick resets.",
 "The Workshop Command Desk": "Half desk, half workbench: design on screen, build on the bench, with dust management that actually works.",
 "Smart Desk Automation": "Lights, monitors, and focus timers triggered by one button or schedule. The desk that sets itself up.",
 "The Legacy Studio Build": "A permanent, beautiful, built-in workspace designed to last a decade. Measure twice, build once, enjoy for years.",
 "Setup Photography Masterclass": "Document your desk like a pro: angles, lighting, and staging that show off the build honestly."
};

function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  var h=0;for(var i=0;i<safe.length;i++){h=(h*31+safe.charCodeAt(i))>>>0;}
  var steps=['Prepare the space','Gather the essentials','Do the core work','Review the result','Lock in the win'];
  var out='# '+safe+' — working demo\n# Field: '+field+'\n';
  out+='steps = '+JSON.stringify(steps)+'\n';
  out+='for i, s in enumerate(steps, 1):\n    print(f"{i}. {s}")\n';
  out+='print("Seed '+h+': repeat the steps in order and the result compounds.")\n';
  return out;
}

function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||['General Study'];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — desk setup record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). '+ (BLURBS[topic]||('A '+field+' study of "'+topic+'".')) +' Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'sample-demo',language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:GENVER,generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-desk-setup',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();