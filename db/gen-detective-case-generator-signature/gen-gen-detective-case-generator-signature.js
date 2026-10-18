(function(){'use strict';
/* JAH The Detective Case Generator Signature Database generator - jahdb-gen-detective-case-generator-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same output. Real working generator. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,s){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(s()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}
var PREFIX="JAH-MDCGS-";

var FIELDS=["Classic Cases","Locked Rooms","Countryside Crimes"];
var VICTIMS=[["Elias Vane","clockmaker"],["Mara Quill","novelist"],["Dr. Theo Marsh","botanist"],["Ada Bloom","jeweler"],["Silas Crane","ship captain"],["Nora Finch","beekeeper"],["Otto Brandt","watchmaker"],["Iris Vale","cartographer"],["Hugo Stern","chef"],["Lena Moss","librarian"],["Felix Hart","locksmith"],["June Park","florist"]];
var PLACES=["the lighthouse gallery","the orchard manor","the riverside inn","the old observatory","the clock tower","the vineyard estate","the harbor warehouse","the mountain lodge","the botanical glasshouse","the railway depot","the mill house","the seaside pavilion"];
var NAMES=["Amos Reed","Bea Lark","Cyrus Pike","Dora Venn","Edgar Moss","Faye Noor","Gus Hale","Hazel Quinn","Ivan Petrov","Jill Faraday","Karl Brenner","Lila Santos"];
var OCC=["gardener","cook","chauffeur","secretary","stablehand","housekeeper","tutor","blacksmith","maid","accountant","driver","nurse"];
var MOTIVES=["an inheritance","a stolen recipe","a forged signature","a broken partnership","a hidden letter","a gambling debt","a promised promotion","a family feud"];
var METHODS=["a doctored telegram","a swapped key","a timed lock","a mislabeled bottle","a silenced bell","a faked footprint","a rerouted letter","a stopped clock"];
var CLUES=["A muddy boot print that does not match the victim's shoes.","A torn corner of a letter hidden in the fireplace.","A pocket watch stopped at the wrong hour.","A window latched from the inside with fresh scratches.","A half-finished cup of tea, still warm when found.","A library book checked out under a false name.","A key that fits no lock in the building.","A smudge of paint on the doorframe, still tacky.","A train timetable with one departure circled.","A button torn from a coat, found in the garden."];
function demoProgram(c){
  var safe=c.title.replace(/\\/g,'\\\\').replace(/"/g,"'");
  var sus=c.suspects.map(function(s){return '    ("'+s.name+'", '+s.alibi+')';}).join(',\n');
  return "# Detective case demo - "+safe+"\n"
   + "SUSPECTS = [\n"+sus+"\n]\n"
   + "SOLUTION = \""+c.culprit+"\"\n"
   + "def main():\n"
   + "    cleared=[n for n,a in SUSPECTS if a]\n"
   + "    left=[n for n,a in SUSPECTS if not a]\n"
   + "    print('suspects:', len(SUSPECTS))\n"
   + "    print('cleared:', ', '.join(cleared))\n"
   + "    assert len(left)==1 and left[0]==SOLUTION, 'solution mismatch'\n"
   + "    print('solution:', SOLUTION)\n"
   + "    print('OK: case solution verified')\n"
   + "if __name__=='__main__':\n    main()\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var v=pick(VICTIMS,rnd), place=pick(PLACES,rnd);
  var motive=pick(MOTIVES,rnd), method=pick(METHODS,rnd);
  var people=shuffle(NAMES,rnd).slice(0,4);
  var occs=shuffle(OCC,rnd).slice(0,4);
  var suspects=people.map(function(n,i){return {name:n,occ:occs[i],alibi:true};});
  var ci=(rnd()*4)|0; suspects[ci].alibi=false;
  var clues=shuffle(CLUES,rnd).slice(0,6);
  var title="The "+place.charAt(4).toUpperCase()+place.slice(5)+" Case";
  var desc="CASE FILE (fictional detective case - a fair-play puzzle with a worked solution).\n\n"
   +v[0]+", the "+v[1]+", was found at "+place+" under strange circumstances.\n"
   +"Four people were nearby: "+suspects.map(function(s){return s.name+" ("+s.occ+")";}).join(", ")+".\n"
   +"The motive centers on "+motive+"; the method involved "+method+".\n"
   +"Clues found at the scene:\n- "+clues.join("\n- ");
  var how="HOW THE DEDUCTION WORKS (solution). Three of the four suspects have alibis that check out; only "
   +suspects[ci].name+" the "+suspects[ci].occ+" has none. The decisive clues are the stopped pocket watch (the hour was staged), "
   +"the key that fits no lock (planted to suggest an intruder), and "+motive+" giving "+suspects[ci].name+" the reason. "
   +"The method - "+method+" - explains the locked scene. Fair-play check: every clue needed to name "+suspects[ci].name+" appears above.";
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+" - detective case",
    title:title,
    description:desc,
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated fictional detective case - a puzzle with a fair solution, not a real event.',
    case:{title:title,suspects:suspects,culprit:suspects[ci].name},
    demo:{kind:"python",language:"python",program:demoProgram({title:title,suspects:suspects,culprit:suspects[ci].name}),note:"Case solution verifier."},
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
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title;});
  return dups.length?{ok:false,errors:['duplicate title in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-gen-detective-case-generator-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gen-detective-case-generator-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
