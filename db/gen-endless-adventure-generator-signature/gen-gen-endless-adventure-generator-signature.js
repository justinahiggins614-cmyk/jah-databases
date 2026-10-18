(function(){'use strict';
/* JAH The Endless Adventure Generator Signature Database generator - jahdb-gen-endless-adventure-generator-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same output. Real working generator. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,s){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(s()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}
var PREFIX="JAH-MEAGS-";

var FIELDS=["Quests","Expeditions","Mysteries"];
var THEMES=["the sunken library","the clockwork city","the whispering forest","the floating market","the crystal caverns","the paper kingdom","the tide-locked isle","the observatory of echoes"];
var HOOKS=["A stranger leaves a map on your doorstep.","A bell rings where no bell should be.","A letter arrives dated fifty years from now.","The river runs backwards for one hour.","A door appears in a wall you know well.","Your shadow points the wrong way at noon."];
var LOCS=["the rusted gatehouse","the flooded archive","the lantern market","the hollow hill","the glass bridge","the quiet station","the thorn maze","the salt flats","the ivory tower stair","the ember fields"];
var CHARS=[["Captain Ilsa Venn","retired sky-pilot"],["Bram Okafor","map forger"],["Sister Lumen","keeper of echoes"],["Pip Alder","messenger, age eleven"],["Dr. Cornelius Fry","disgraced scholar"],["Nadia Reyes","tide-reader"],["Old Tam","ferryman who remembers everything"],["Wren Solace","lockpick and poet"]];
var TWISTS=["the guide was the treasure all along","the map was drawn by your future self","the monster was guarding the exit, not the treasure","the quest-giver caused the problem","the treasure is a library, not gold","waking up was part of the quest"];
function demoProgram(a){
  var safe=a.title.replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Endless adventure demo - "+safe+"\n"
   + "LOCS = "+a.nloc+"\nHOOKS = "+a.nhook+"\n"
   + "def main():\n"
   + "    print('locations:', LOCS, '| onward hooks:', HOOKS)\n"
   + "    assert LOCS >= 3 and HOOKS >= 2, 'quest chain too short'\n"
   + "    print('OK: adventure quest chain verified')\n"
   + "if __name__=='__main__':\n    main()\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var theme=pick(THEMES,rnd), hook=pick(HOOKS,rnd);
  var locs=shuffle(LOCS,rnd).slice(0,3), chars=shuffle(CHARS,rnd).slice(0,4);
  var twist=pick(TWISTS,rnd);
  var hooks=[pick(HOOKS,rnd),pick(HOOKS,rnd)];
  var title="Quest: "+theme.charAt(0).toUpperCase()+theme.slice(1);
  var desc="ADVENTURE SEED (fictional connected quest - expandable forever).\n\nHook: "+hook+"\n"
   +"The trail leads through "+locs.join(", ")+".\n"
   +"Travelers you meet: "+chars.map(function(c){return c[0]+" ("+c[1]+")";}).join("; ")+".\n"
   +"The twist: "+twist+".\n"
   +"Onward hooks (the adventure never has to end):\n- "+hooks.join("\n- ");
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+" - endless adventure",
    title:title,
    description:desc,
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated fictional adventure seed - expand it however you like.',
    demo:{kind:"python",language:"python",program:demoProgram({title:title,nloc:locs.length,nhook:hooks.length}),note:"Quest chain verifier."},
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
var gen={version:'jahdb-gen-endless-adventure-generator-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gen-endless-adventure-generator-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
