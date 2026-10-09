(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return s[(r()*s.length)|0];}
function ri(r,a,b){return a+((r()*(b-a+1))|0);}
function pad6(n){return String(n).padStart(6,'0');}
function fill(s,m){return s.replace(/\{(\w+)\}/g,function(_,k){return m[k]!=null?m[k]:'';});}

var CATS=['spanish','french','german','portuguese','italian','dutch'];
var DOMAINS=['general','tech','health'];

var V=['save','open','close','send','read','write','download','upload','delete','share'];
var N=['file','document','photo','message','account','password','screen','report','folder','link'];
var A=['now','quickly','today','here'];

var SRC=[
 'Please {v} the {n} {adv}.',
 'Do not {v} the {n}.',
 '{v} the {n}, then {v2} the {n2}.',
 'Can you {v} the {n} {adv}?'
];

var LANGS={
spanish:{v:{save:'guardar',open:'abrir',close:'cerrar',send:'enviar',read:'leer',write:'escribir',download:'descargar',upload:'subir',delete:'eliminar',share:'compartir'},
 n:{file:'el archivo',document:'el documento',photo:'la foto',message:'el mensaje',account:'la cuenta',password:'la contraseña',screen:'la pantalla',report:'el informe',folder:'la carpeta',link:'el enlace'},
 a:{now:'ahora',quickly:'rápidamente',today:'hoy',here:'aquí'},
 t:['Por favor {v} {n} {adv}.','No {v} {n}.','{v} {n}, luego {v2} {n2}.','¿Puedes {v} {n} {adv}?']},
french:{v:{save:'enregistrer',open:'ouvrir',close:'fermer',send:'envoyer',read:'lire',write:'écrire',download:'télécharger',upload:'téléverser',delete:'supprimer',share:'partager'},
 n:{file:'le fichier',document:'le document',photo:'la photo',message:'le message',account:'le compte',password:'le mot de passe',screen:"l'écran",report:'le rapport',folder:'le dossier',link:'le lien'},
 a:{now:'maintenant',quickly:'rapidement',today:"aujourd'hui",here:'ici'},
 t:['Veuillez {v} {n} {adv}.','Ne {v} pas {n}.','{v} {n}, puis {v2} {n2}.','Peux-tu {v} {n} {adv} ?']},
german:{v:{save:'speichern',open:'öffnen',close:'schließen',send:'senden',read:'lesen',write:'schreiben',download:'herunterladen',upload:'hochladen',delete:'löschen',share:'teilen'},
 n:{file:'die Datei',document:'das Dokument',photo:'das Foto',message:'die Nachricht',account:'das Konto',password:'das Passwort',screen:'der Bildschirm',report:'der Bericht',folder:'der Ordner',link:'der Link'},
 a:{now:'jetzt',quickly:'schnell',today:'heute',here:'hier'},
 t:['Bitte {n} {adv} {v}.','{n} nicht {v}.','{n} {v}, dann {n2} {v2}.','Kannst du {n} {adv} {v}?']},
portuguese:{v:{save:'salvar',open:'abrir',close:'fechar',send:'enviar',read:'ler',write:'escrever',download:'baixar',upload:'enviar',delete:'excluir',share:'compartilhar'},
 n:{file:'o arquivo',document:'o documento',photo:'a foto',message:'a mensagem',account:'a conta',password:'a senha',screen:'a tela',report:'o relatório',folder:'a pasta',link:'o link'},
 a:{now:'agora',quickly:'rapidamente',today:'hoje',here:'aqui'},
 t:['Por favor {v} {n} {adv}.','Não {v} {n}.','{v} {n}, depois {v2} {n2}.','Você pode {v} {n} {adv}?']},
italian:{v:{save:'salvare',open:'aprire',close:'chiudere',send:'inviare',read:'leggere',write:'scrivere',download:'scaricare',upload:'caricare',delete:'eliminare',share:'condividere'},
 n:{file:'il file',document:'il documento',photo:'la foto',message:'il messaggio',account:"l'account",password:'la password',screen:'lo schermo',report:'il rapporto',folder:'la cartella',link:'il link'},
 a:{now:'ora',quickly:'velocemente',today:'oggi',here:'qui'},
 t:['Per favore {v} {n} {adv}.','Non {v} {n}.','{v} {n}, poi {v2} {n2}.','Puoi {v} {n} {adv}?']},
dutch:{v:{save:'opslaan',open:'openen',close:'sluiten',send:'verzenden',read:'lezen',write:'schrijven',download:'downloaden',upload:'uploaden',delete:'verwijderen',share:'delen'},
 n:{file:'het bestand',document:'het document',photo:'de foto',message:'het bericht',account:'het account',password:'het wachtwoord',screen:'het scherm',report:'het rapport',folder:'de map',link:'de link'},
 a:{now:'nu',quickly:'snel',today:'vandaag',here:'hier'},
 t:['{v} {n} {adv}, alstublieft.','{v} {n} niet.','{v} {n}, dan {v2} {n2}.','Kun je {n} {adv} {v}?']}
};

function translate(lang,tIdx,lex){
  var L=LANGS[lang];
  var m={v:L.v[V[lex[1]]],n:L.n[N[lex[2]]],adv:L.a[A[lex[3]]],v2:L.v[V[lex[4]]],n2:L.n[N[lex[5]]]};
  return fill(L.t[tIdx],m);
}
function sourceText(tIdx,lex){
  var m={v:V[lex[1]],n:'the '+N[lex[2]],adv:A[lex[3]],v2:V[lex[4]],n2:'the '+N[lex[5]]};
  return fill(SRC[tIdx],m);
}

function generate(seed,opts,rnd){
  rnd=rnd||prng(seed);
  var cat=(opts&&opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:pick(rnd,CATS);
  var tIdx=ri(rnd,0,3);
  var lex=[tIdx,ri(rnd,0,V.length-1),ri(rnd,0,N.length-1),ri(rnd,0,A.length-1),ri(rnd,0,V.length-1),ri(rnd,0,N.length-1)];
  var src=sourceText(tIdx,lex), tgt=translate(cat,tIdx,lex);
  var domain=pick(rnd,DOMAINS);
  var quality=Number((0.7+rnd()*0.3).toFixed(2));
  var id='JAH-ML-'+pad6(seed);
  return {id:id,pair_id:id,source_lang:'en',target_lang:cat,source_text:src,target_text:tgt,
    domain:domain,quality:quality,title:src.slice(0,80),lex:lex};
}

function validate(r){
  var e=[];
  if(!r||typeof r!=='object'){return {ok:false,errors:['not an object']};}
  if(!/^JAH-ML-\d{6}$/.test(r.id))e.push('id');
  if(r.pair_id!==r.id)e.push('pair_id');
  if(r.source_lang!=='en')e.push('source_lang');
  if(CATS.indexOf(r.target_lang)<0)e.push('target_lang');
  if(typeof r.source_text!=='string'||!r.source_text.length||r.source_text.length>600)e.push('source_text');
  if(typeof r.target_text!=='string'||!r.target_text.length||r.target_text.length>600)e.push('target_text');
  if(DOMAINS.indexOf(r.domain)<0)e.push('domain');
  if(typeof r.quality!=='number'||r.quality<0.7||r.quality>1.0)e.push('quality');
  if(r.title!==String(r.source_text).slice(0,80))e.push('title');
  if(!Array.isArray(r.lex)||r.lex.length!==6||r.lex.some(function(x){return typeof x!=='number';}))e.push('lex');
  else{
    if(sourceText(r.lex[0],r.lex)!==r.source_text)e.push('source_text mismatch');
    if(translate(r.target_lang,r.lex[0],r.lex)!==r.target_text)e.push('target_text mismatch');
  }
  return {ok:!e.length,errors:e};
}

var gen={version:'jahdb-multilingual-pairs-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('multilingual-pairs',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
