(function(){'use strict';
/* JAH The Strange Diary Generator Database generator - jahdb-gen-strange-diary-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same output. Real working generator. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,s){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(s()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}
var PREFIX="JAH-MSDG-";

var FIELDS=["Vanishings","Discoveries","Midnight Mysteries"];
var NARR=[["Elena Marsh","lighthouse keeper's daughter"],["Tom Beck","night watchman"],["Ada Lovelock","botanist"],["Silas Wren","retired sailor"],["Mira Chen","mapmaker"],["Jonah Pike","innkeeper"],["Rosa Delgado","beekeeper"],["Felix Grant","clock repairer"]];
var ARCS=[
 {m:"the brass key that opens no known door",clues:["a brass key found in a coat pocket","a door in the cellar that was not on any plan","scratches on the inside of the cellar door","a name etched under the key's bow"],truth:"the key opened a smuggler's cache walled up a century ago"},
 {m:"the lighthouse lamp that lit itself",clues:["the lamp found burning at dawn","oil missing though no one climbed the tower","a gull feather on the lamp room floor","footprints in dust that stopped mid-room"],truth:"a nesting gull had knocked the lens cover, focusing sunrise onto the wick"},
 {m:"the violin heard from the empty attic",clues:["music on windless nights","a broken string on the old violin","dust undisturbed on the attic floor","the tune matched a songbook from 1911"],truth:"the new radio in the room below carried a late broadcast through the heating vent"},
 {m:"the garden that bloomed in winter",clues:["roses open in January","warmth rising from one flowerbed","a cracked hot-water pipe below","the gardener's quiet smile"],truth:"a leaking hot-water pipe had warmed the soil for weeks"},
 {m:"the letters that arrived with no sender",clues:["envelopes with no stamp","handwriting that changed mid-letter","paper from the old mill","ink still wet on the last page"],truth:"the writer was practicing forgery and testing the household's attention"},
 {m:"the clock that chimed thirteen",clues:["thirteen chimes at midnight","the count always started early","a loose hammer in the mechanism","the clockmaker's apprentice grinning"],truth:"a loose striking hammer bounced and struck twice on the twelfth chime"}];
function demoProgram(d){
  var safe=d.title.replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Strange diary demo - "+safe+"\n"
   + "ENTRIES = "+d.n+"\n"
   + "def main():\n"
   + "    print('diary entries:', ENTRIES)\n"
   + "    assert ENTRIES >= 5, 'a diary arc needs at least 5 entries'\n"
   + "    print('OK: diary arc verified ('+ENTRIES+' entries)')\n"
   + "if __name__=='__main__':\n    main()\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var n=pick(NARR,rnd), arc=pick(ARCS,rnd);
  var dates=["Mar 3","Mar 5","Mar 8","Mar 12","Mar 16","Mar 21"];
  var entries=arc.clues.map(function(c,i){
    return dates[i]+": "+["Found "+c+". I cannot explain it.",
      "Still thinking about "+c+". Asked around; no one admits anything.",
      c.charAt(0).toUpperCase()+c.slice(1)+". There must be a reason.",
      "Dreamed about "+c+". Woke up certain I am close."][i%4];
  });
  entries.push(dates[5]+": It is solved. "+arc.truth.charAt(0).toUpperCase()+arc.truth.slice(1)+".");
  var title="The Diary of "+n[0]+" - "+arc.m.charAt(0).toUpperCase()+arc.m.slice(1);
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+" - strange diary",
    title:title,
    description:"DIARY (fictional diary entries that gradually reveal a mystery).\nKept by "+n[0]+", "+n[1]+".\n\n"+entries.join("\n\n"),
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated fictional diary - the mystery and its solution are invented.',
    demo:{kind:"python",language:"python",program:demoProgram({title:title,n:entries.length}),note:"Diary arc verifier."},
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
var gen={version:'jahdb-gen-strange-diary-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gen-strange-diary',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
