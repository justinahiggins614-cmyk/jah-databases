(function(){'use strict';
/* Writers Database generator — jahdb-writers-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-WRITER-';
var TOPICS=[["William Shakespeare", "The English playwright of Hamlet, Macbeth, and the sonnets."], ["Jane Austen", "The novelist of Pride and Prejudice and sharp social wit."], ["Charles Dickens", "The Victorian novelist of A Christmas Carol and Oliver Twist."], ["Mark Twain", "The American humorist of Tom Sawyer and Huckleberry Finn."], ["Ernest Hemingway", "The spare-styled novelist of The Old Man and the Sea."], ["F. Scott Fitzgerald", "The Jazz Age novelist of The Great Gatsby."], ["Leo Tolstoy", "The Russian master of War and Peace."], ["Fyodor Dostoevsky", "The Russian novelist of Crime and Punishment."], ["Virginia Woolf", "The modernist of Mrs. Dalloway and To the Lighthouse."], ["James Joyce", "The Irish modernist of Ulysses."], ["Gabriel Garcia Marquez", "The Colombian Nobel laureate of magical realism."], ["Toni Morrison", "The American Nobel laureate of Beloved."], ["Maya Angelou", "The poet and memoirist of I Know Why the Caged Bird Sings."], ["Agatha Christie", "The queen of detective fiction."], ["J.R.R. Tolkien", "The creator of The Hobbit and The Lord of the Rings."], ["C.S. Lewis", "The author of The Chronicles of Narnia."], ["George Orwell", "The writer of 1984 and Animal Farm."], ["Harper Lee", "The author of To Kill a Mockingbird."], ["J.K. Rowling", "The creator of the Harry Potter books."], ["Stephen King", "The prolific master of horror and suspense."], ["Edgar Allan Poe", "The American master of the macabre and the detective story."], ["Walt Whitman", "The American poet of Leaves of Grass."], ["Emily Dickinson", "The reclusive poet of hundreds of brilliant short poems."], ["Langston Hughes", "The leading poet of the Harlem Renaissance."], ["Homer", "The ancient Greek poet of the Iliad and Odyssey."], ["Dante Alighieri", "The Italian poet of the Divine Comedy."], ["Miguel de Cervantes", "The Spanish author of Don Quixote."], ["Mary Shelley", "The author of Frankenstein."]];
var ANGLES=['overview','detailed','examples','faq','history','applications'];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function generate(seed,opts){
  var s=prng(seed);
  var ti=(s()*TOPICS.length)|0, ai=(s()*ANGLES.length)|0;
  var topic=TOPICS[ti], angle=ANGLES[ai];
  var id=PREFIX+pad(seed);
  var title=topic[0]+' ('+angle+')';
  var desc=topic[1];
  var content=topic[0]+' \u2014 '+topic[1];
  return {
    id:id, title:title, description:desc, genre:angle,
    type:'writers record', content:content, content_completeness:'stub',
    stub_note:'Topic stub: the topic title and its one-line brief are real; the full guide article is not yet written. This record does not present shell text as a complete guide.',
    demo:null, src:'public', _seed:seed
  };
}
function validate(r){
  var errs=[];
  if(!r.id)errs.push('missing id');
  if(!r.title)errs.push('missing title');
  if(!r.content||r.content.length<50)errs.push('content too short');
  return {ok:errs.length===0, errors:errs};
}
function driftCheck(rec,sample){
  // Simple: check for exact title duplicates in sample
  for(var i=0;i<sample.length;i++){if(sample[i].t===rec.title)return {ok:false,errors:['duplicate title']};}
  return {ok:true,errors:[]};
}
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('writers',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();