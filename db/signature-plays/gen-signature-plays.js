/* JAH Signature Plays Database generator — jahdb-signature-plays-1.0
   Original Signature-made plays. Type 2 (Signature-developed). Full plays only. */
(function(){
'use strict';
var GEN_NAME='jahdb-signature-plays-1.0';
function prng(seed){var s=seed>>>0;return function(){s=(s*1664525+1013904223)>>>0;return s/4294967296;};}
function pick(r,arr){return arr[Math.floor(r()*arr.length)];}
function pickN(r,arr,n){var c=arr.slice(),o=[];while(o.length<n&&c.length){o.push(c.splice(Math.floor(r()*c.length),1)[0]);}return o;}

var GENRES=['tragedy','comedy','drama','sci-fi','mystery','historical','absurdist','musical'];
var SETTINGS=[
  'a lighthouse on a cliff during a storm','a space station orbiting a dying star',
  'a small town diner at 3 AM','a courtroom in the year 2089',
  'an old library where books write themselves','a submarine at crush depth',
  'a rooftop garden above a flooded city','a train that never stops',
  'a workshop where time is repaired','a village at the edge of the map'
];
var THEMES=[
  'memory and what we choose to forget','the price of knowing the future',
  'a promise made to someone who is gone','the last message ever sent',
  'what machines dream about','the weight of an unspoken apology',
  'a door that should never be opened','the sound of a name being forgotten'
];
var CHAR_NAMES=['MARA','ELIAS','JUNE','THEO','ADA','RUE','CALE','WREN','IDO','SABLE','NOX','LIRA'];
var CHAR_ROLES=['a keeper of lost things','an engineer of impossible machines','a cartographer of forgotten places','a singer who lost her voice','a clockmaker','a translator of dead languages','a pilot','a gardener of glass flowers'];

function makePlay(seed){
  var r=prng(seed);
  var genre=pick(r,GENRES), setting=pick(r,SETTINGS), theme=pick(r,THEMES);
  var chars=pickN(r,CHAR_NAMES,3+Math.floor(r()*3));
  var roles={}; chars.forEach(function(c){roles[c]=pick(r,CHAR_ROLES);});
  var title=pick(r,['The Last Light of','Echoes Beneath','The Glass','A Song for','The Weight of','Where']);
  var title2=pick(r,['Tomorrow','the Drowned Bell','Winter','Static','the Ninth Hour','Ashes']);
  var fullTitle=title+' '+title2;
  var nActs=2+Math.floor(r()*2);
  var acts=[];
  for(var a=1;a<=nActs;a++){
    var scenes=[];
    var nScenes=2+Math.floor(r()*2);
    for(var s=1;s<=nScenes;s++){
      var lines=[];
      lines.push('[Stage lights rise on '+setting+'.]');
      var nLines=8+Math.floor(r()*8);
      for(var l=0;l<nLines;l++){
        var c=pick(r,chars);
        var txt=pick(r,[
          'You heard it too, didn\'t you. The '+pick(r,['silence','hum','crack','whisper'])+' before the '+pick(r,['storm','dawn','change','fall'])+'.',
          'I kept the '+pick(r,['letter','key','photograph','compass'])+' all these years. I never told anyone.',
          'If we '+pick(r,['leave now','wait','go back','speak first'])+', there\'s no undoing it.',
          'That\'s the thing about '+theme.split(' ')[0]+' — it never asks permission.',
          '[A '+pick(r,['bell','horn','voice','light'])+' sounds in the distance.]',
          'Tell me the truth. Not the kind one. The real one.',
          'I\'ve been '+pick(r,['counting','waiting','listening','watching'])+' since '+pick(r,['dawn','the blackout','you left','it started'])+'.',
          'Then we agree. '+pick(r,['No one speaks of this.','We finish what we started.','Dawn, then.','It ends tonight.'])
        ]);
        lines.push(c+': '+txt);
      }
      lines.push('[Lights fade.]');
      scenes.push({scene:s,setting:setting,text:lines.join('\n')});
    }
    acts.push({act:a,scenes:scenes});
  }
  return {
    id:'JAH-SPLAY-'+String(seed).padStart(6,'0'),
    title:fullTitle, playwright:'Signature', genre:genre, setting:setting, theme:theme,
    characters:chars.map(function(c){return {name:c,role:roles[c]};}),
    acts:acts,
    synopsis:'A '+genre+' set in '+setting+', exploring '+theme+'.',
    performance_notes:'Staging emphasizes light and silence. Minimal set; the setting is evoked through sound and light.',
    src:'signature', _seed:seed
  };
}
function validate(rec){
  if(!rec||!rec.id||!rec.title||!rec.acts||!rec.acts.length)return false;
  if(!/^JAH-SPLAY-\d{6}$/.test(rec.id))return false;
  return true;
}
function driftCheck(a,b){return JSON.stringify(a)===JSON.stringify(b);}
var gen={name:GEN_NAME,generate:function(seed){return makePlay(seed);},
  generateIndexed:function(i){return makePlay(i+1);},validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('signature-plays',gen);}
if(typeof module!=='undefined'&&module.exports){module.exports=gen;}
})();
