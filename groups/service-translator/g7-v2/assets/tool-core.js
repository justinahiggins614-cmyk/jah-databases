var LANGS={es:'Spanish',fr:'French',de:'German',it:'Italian'};
var PHRASES={
 'hello':{es:'hola',fr:'bonjour',de:'Hallo',it:'ciao'},
 'good morning':{es:'buenos dias',fr:'bonjour',de:'Guten Morgen',it:'buongiorno'},
 'good afternoon':{es:'buenas tardes',fr:'bon apres-midi',de:'Guten Tag',it:'buon pomeriggio'},
 'good evening':{es:'buenas noches',fr:'bonsoir',de:'Guten Abend',it:'buonasera'},
 'goodbye':{es:'adios',fr:'au revoir',de:'auf Wiedersehen',it:'arrivederci'},
 'good night':{es:'buenas noches',fr:'bonne nuit',de:'Gute Nacht',it:'buonanotte'},
 'welcome':{es:'bienvenido',fr:'bienvenue',de:'willkommen',it:'benvenuto'},
 'how are you':{es:'como estas',fr:'comment allez-vous',de:'wie geht es dir',it:'come stai'},
 'i am well':{es:'estoy bien',fr:'je vais bien',de:'mir geht es gut',it:'sto bene'},
 'nice to meet you':{es:'mucho gusto',fr:'enchante',de:'freut mich',it:'piacere'},
 'please':{es:'por favor',fr:"s'il vous plait",de:'bitte',it:'per favore'},
 'thank you':{es:'gracias',fr:'merci',de:'danke',it:'grazie'},
 'thank you very much':{es:'muchas gracias',fr:'merci beaucoup',de:'vielen Dank',it:'grazie mille'},
 'sorry':{es:'lo siento',fr:'desole',de:'es tut mir leid',it:'mi dispiace'},
 'excuse me':{es:'perdon',fr:'excusez-moi',de:'entschuldigen Sie',it:'mi scusi'},
 'yes':{es:'si',fr:'oui',de:'ja',it:'si'},
 'no':{es:'no',fr:'non',de:'nein',it:'no'},
 'maybe':{es:'quiza',fr:'peut-etre',de:'vielleicht',it:'forse'},
 'i do not understand':{es:'no entiendo',fr:'je ne comprends pas',de:'ich verstehe nicht',it:'non capisco'},
 'do you speak english':{es:'hablas ingles',fr:'parlez-vous anglais',de:'sprechen Sie Englisch',it:'parla inglese'},
 'help':{es:'ayuda',fr:'au secours',de:'Hilfe',it:'aiuto'},
 'one':{es:'uno',fr:'un',de:'eins',it:'uno'},
 'two':{es:'dos',fr:'deux',de:'zwei',it:'due'},
 'three':{es:'tres',fr:'trois',de:'drei',it:'tre'},
 'four':{es:'cuatro',fr:'quatre',de:'vier',it:'quattro'},
 'five':{es:'cinco',fr:'cinq',de:'funf',it:'cinque'},
 'six':{es:'seis',fr:'six',de:'sechs',it:'sei'},
 'seven':{es:'siete',fr:'sept',de:'sieben',it:'sette'},
 'eight':{es:'ocho',fr:'huit',de:'acht',it:'otto'},
 'nine':{es:'nueve',fr:'neuf',de:'neun',it:'nove'},
 'ten':{es:'diez',fr:'dix',de:'zehn',it:'dieci'},
 'monday':{es:'lunes',fr:'lundi',de:'Montag',it:'lunedi'},
 'tuesday':{es:'martes',fr:'mardi',de:'Dienstag',it:'martedi'},
 'wednesday':{es:'miercoles',fr:'mercredi',de:'Mittwoch',it:'mercoledi'},
 'thursday':{es:'jueves',fr:'jeudi',de:'Donnerstag',it:'giovedi'},
 'friday':{es:'viernes',fr:'vendredi',de:'Freitag',it:'venerdi'},
 'saturday':{es:'sabado',fr:'samedi',de:'Samstag',it:'sabato'},
 'sunday':{es:'domingo',fr:'dimanche',de:'Sonntag',it:'domenica'},
 'water':{es:'agua',fr:'eau',de:'Wasser',it:'acqua'},
 'bread':{es:'pan',fr:'pain',de:'Brot',it:'pane'},
 'cheese':{es:'queso',fr:'fromage',de:'Kase',it:'formaggio'},
 'coffee':{es:'cafe',fr:'cafe',de:'Kaffee',it:'caffe'},
 'wine':{es:'vino',fr:'vin',de:'Wein',it:'vino'},
 'the bill please':{es:'la cuenta por favor',fr:"l'addition s'il vous plait",de:'die Rechnung bitte',it:'il conto per favore'},
 'where is the station':{es:'donde esta la estacion',fr:'ou est la gare',de:'wo ist der Bahnhof',it:"dov'e la stazione"},
 'left':{es:'izquierda',fr:'gauche',de:'links',it:'sinistra'},
 'right':{es:'derecha',fr:'droite',de:'rechts',it:'destra'},
 'straight ahead':{es:'todo recto',fr:'tout droit',de:'geradeaus',it:'dritto'},
 'how much':{es:'cuanto cuesta',fr:'combien ca coute',de:'wie viel kostet das',it:'quanto costa'},
 'how much does it cost':{es:'cuanto cuesta',fr:'combien ca coute',de:'wie viel kostet das',it:'quanto costa'},
 'too expensive':{es:'demasiado caro',fr:'trop cher',de:'zu teuer',it:'troppo caro'},
 'the change':{es:'el cambio',fr:'la monnaie',de:'das Wechselgeld',it:'il resto'},
 'mother':{es:'madre',fr:'mere',de:'Mutter',it:'madre'},
 'father':{es:'padre',fr:'pere',de:'Vater',it:'padre'},
 'friend':{es:'amigo',fr:'ami',de:'Freund',it:'amico'},
 'child':{es:'nino',fr:'enfant',de:'Kind',it:'bambino'},
 'red':{es:'rojo',fr:'rouge',de:'rot',it:'rosso'},
 'blue':{es:'azul',fr:'bleu',de:'blau',it:'blu'},
 'green':{es:'verde',fr:'vert',de:'grun',it:'verde'},
 'yellow':{es:'amarillo',fr:'jaune',de:'gelb',it:'giallo'},
 'black':{es:'negro',fr:'noir',de:'schwarz',it:'nero'},
 'white':{es:'blanco',fr:'blanc',de:'weiss',it:'bianco'},
 'it is sunny':{es:'hace sol',fr:'il fait beau',de:'es ist sonnig',it:"c'e il sole"},
 'it is raining':{es:'esta lloviendo',fr:'il pleut',de:'es regnet',it:'piove'},
 'it is cold':{es:'hace frio',fr:'il fait froid',de:'es ist kalt',it:'fa freddo'},
 'it is hot':{es:'hace calor',fr:'il fait chaud',de:'es ist heiss',it:'fa caldo'},
 'what time is it':{es:'que hora es',fr:'quelle heure est-il',de:'wie spat ist es',it:'che ore sono'},
 'today':{es:'hoy',fr:"aujourd'hui",de:'heute',it:'oggi'},
 'tomorrow':{es:'manana',fr:'demain',de:'morgen',it:'domani'},
 'yesterday':{es:'ayer',fr:'hier',de:'gestern',it:'ieri'},
 'big':{es:'grande',fr:'grand',de:'gross',it:'grande'},
 'small':{es:'pequeno',fr:'petit',de:'klein',it:'piccolo'},
 'good':{es:'bueno',fr:'bon',de:'gut',it:'buono'},
 'bad':{es:'malo',fr:'mauvais',de:'schlecht',it:'cattivo'},
 'call a doctor':{es:'llame a un medico',fr:'appelez un medecin',de:'rufen Sie einen Arzt',it:'chiamate un medico'},
 'i need help':{es:'necesito ayuda',fr:"j'ai besoin d'aide",de:'ich brauche Hilfe',it:'ho bisogno di aiuto'},
 'i need a doctor':{es:'necesito un medico',fr:"j'ai besoin d'un medecin",de:'ich brauche einen Arzt',it:'ho bisogno di un medico'},
 'it hurts here':{es:'me duele aqui',fr:'ca me fait mal ici',de:'es tut hier weh',it:'mi fa male qui'},
 'see you tomorrow':{es:'hasta manana',fr:'a demain',de:'bis morgen',it:'a domani'},
 'thank you for your help':{es:'gracias por su ayuda',fr:'merci de votre aide',de:'danke fur Ihre Hilfe',it:'grazie per il suo aiuto'}
};
var PHRASE_LIST=Object.keys(PHRASES).sort(function(a,b){
  var da=a.split(' ').length, db=b.split(' ').length;
  return db-da || b.length-a.length;
});
function translate(text, lang){
  var words=String(text||'').toLowerCase().replace(/[.!?,:;]+/g,' ').split(/\s+/).filter(function(w){return w;});
  var out=[], uncovered=[], covered=0, i=0;
  while(i<words.length){
    var matched=null, mlen=0;
    for(var k=0;k<PHRASE_LIST.length;k++){
      var ph=PHRASE_LIST[k], pw=ph.split(' ');
      if(pw.length<=mlen) continue;
      if(words.slice(i,i+pw.length).join(' ')===ph){ matched=ph; mlen=pw.length; break; }
    }
    if(matched){ out.push(PHRASES[matched][lang]); covered+=mlen; i+=mlen; }
    else if(PHRASES[words[i]]){ out.push(PHRASES[words[i]][lang]); covered++; i++; }
    else { out.push('['+words[i]+']'); uncovered.push(words[i]); i++; }
  }
  return {text:out.join(' '), covered:covered, uncovered:uncovered, total:words.length};
}
if(typeof module!=='undefined'){module.exports={translate: translate, PHRASES: PHRASES, LANGS: LANGS, PHRASE_LIST: PHRASE_LIST};}
