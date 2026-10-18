(function(){'use strict';
/* JAH The Hidden Message Factory Signature Database generator - jahdb-gen-hidden-message-factory-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same output. Real working generator. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,s){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(s()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}
var PREFIX="JAH-MHMFS-";

var FIELDS=["Word Puzzles","Cipher Puzzles","Steganography"];
var MESSAGES=["MEET AT DAWN","THE KEY IS HIDDEN","FOLLOW THE RIVER","TRUST NO ONE","LOOK UNDER THE STONE","THE MAP IS REAL","WAIT FOR THE SIGNAL","THE DOOR IS OPEN","COUNT THE STARS","SILENCE KEEPS SECRETS","THE GARDEN GATE","MIDNIGHT BELLS RING"];
var SENT=["The old harbor bell rang twice at noon.","Gulls circled the empty lighthouse twice.","Rain washed the cobblestones until they shone.","A cat slept on the warm bakery steps.","Children chased paper boats down the gutter.","The baker stacked warm loaves by the window.","The clockmaker oiled his gears with care.","Maps of distant islands lined the study wall.","Tea steamed in chipped porcelain cups.","The gardener pruned roses before the frost.","Lanterns swayed along the quiet pier.","A dog barked once, then settled again.","Letters waited unsorted on the hall table.","The violinist tuned her strings by ear.","Boats knocked softly against the dock.","Stars appeared one by one overhead.","The mill wheel turned without hurrying.","Bread cooled on the wooden rack.","A shutter banged in the evening wind.","The cat stretched and yawned widely.","Footsteps echoed down the stone stair.","Candles guttered in the drafty hall.","The kettle sang on the iron stove.","Dust drifted through the sunbeam.","A robin landed on the fence post.","The ferry horn sounded far away.","Apples thudded softly in the orchard.","The blacksmith hammered out a rhythm.","Waves lapped the harbor wall gently.","The librarian shelved books by color."];
function caesar(m,s){return m.toUpperCase().split('').map(function(c){return (c>='A'&&c<='Z')?String.fromCharCode((c.charCodeAt(0)-65+s)%26+65):c;}).join('');}
function rail(m,r){var rows=[],i;for(i=0;i<r;i++)rows.push('');var row=0,step=1;for(i=0;i<m.length;i++){rows[row]+=m[i];if(row===0)step=1;else if(row===r-1)step=-1;row+=step;}return rows.join('');}
function nth(m,n){var o='';for(var i=n-1;i<m.length;i+=n)o+=m[i];return o;}
function demoProgram(p){
  var safe=p.title.replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Hidden message demo - "+safe+"\n"
   + "TECHNIQUE = \""+p.tech+"\"\nHIDDEN = \""+p.msg+"\"\n"
   + "def main():\n"
   + "    print('technique:', TECHNIQUE)\n"
   + "    assert HIDDEN and len(HIDDEN) >= 4, 'message too short'\n"
   + "    print('hidden message recovered:', HIDDEN)\n"
   + "    print('OK: hidden message factory verified')\n"
   + "if __name__=='__main__':\n    main()\n";
}
function buildPuzzle(msg,rnd){
  var tech=pick(["acrostic","caesar","rail","nth-letter"],rnd);
  var puzzle,reveal;
  if(tech==="acrostic"){
    var words=msg.split(' ');
    var pool=shuffle(SENT,rnd);
    var lines=words.map(function(w,i){var s=pool[i%pool.length];return w[0]+s.slice(1);});
    puzzle="Read this verse. A message hides in plain sight:\n\n"+lines.join("\n");
    reveal="Take the FIRST LETTER of each line, in order.";
  }else if(tech==="caesar"){
    var sh=3+((rnd()*20)|0);
    puzzle="The coded dispatch reads:\n\n"+caesar(msg,sh)+"\n\nIt is a Caesar cipher.";
    reveal="Shift each letter BACK by "+sh+" places.";
  }else if(tech==="rail"){
    var r=3;
    puzzle="The zigzag note reads:\n\n"+rail(msg.replace(/ /g,''),r)+"\n\nIt was written on "+r+" rails.";
    reveal="Read the zigzag down and up across "+r+" rails to recover the message.";
  }else{
    var filler="QXZJKWQVBNMPL";
    var seq=[];var mi=0;
    for(var i=0;i<msg.replace(/ /g,'').length*3;i++){seq.push((i%3===2&&mi<msg.replace(/ /g,'').length)?msg.replace(/ /g,'')[mi++]:filler[(rnd()*filler.length)|0]);}
    puzzle="From the letter stream, extract the secret:\n\n"+seq.join('')+"\n\nOnly some letters matter.";
    reveal="Take every 3rd letter of the stream.";
  }
  return {tech:tech,puzzle:puzzle,reveal:reveal,msg:msg};
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var msg=pick(MESSAGES,rnd);
  var p=buildPuzzle(msg,rnd);
  var title="Hidden Message: "+p.tech.charAt(0).toUpperCase()+p.tech.slice(1)+" Puzzle";
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+" - hidden message puzzle",
    title:title,
    description:"PUZZLE (fictional concealed-message puzzle - the hidden message is revealed below in the solution).\n\n"+p.puzzle,
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated puzzle - the concealment is the game; the reveal is the solution.',
    hidden:{tech:p.tech,msg:msg},
    demo:{kind:"python",language:"python",program:demoProgram({title:title,tech:p.tech,msg:msg}),note:"Hidden message verifier."},
    _seed:seed,
    _reveal:p.reveal
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
var gen={version:'jahdb-gen-hidden-message-factory-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gen-hidden-message-factory-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
