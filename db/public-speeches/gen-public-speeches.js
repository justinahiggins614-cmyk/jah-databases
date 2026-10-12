(function(){'use strict';
/* Public Speeches Database generator — jahdb-public-speeches-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   Each record carries the COMPLETE original speech text — a full file, never
   a stub — plus a read-aloud demo program.
   src:"signature-generated-sample" = Signature-authored original, clearly labeled. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
var PREFIX='JAH-SPH-';
var GENRES=['civic','commencement','memorial','inaugural','advocacy','scientific','cultural','farewell'];
var SPEECHES=[
 {t:'The Long Work',g:'civic',venue:'Town Hall Centennial',text:'Friends and neighbors —\n\nA hundred years ago, the people of this town raised this hall with their own hands. Farmers took a week off harvest. The blacksmith forged the hinges. The schoolteacher organized the fund drive, nickel by nickel.\n\nThey did not do it for themselves. Most of them knew they would never see the hundredth anniversary. They built for people they would never meet — for us.\n\nThat is the long work. It is planting trees whose shade you will never enjoy. It is writing the first page of a book someone else will finish. It is voting, volunteering, showing up — the unglamorous verbs of a functioning community.\n\nWe live in an age of the instant: instant messages, instant results, instant outrage. The long work asks something harder of us: patience. Faith that small, repeated acts of care compound into something enormous.\n\nSo here is my charge to us on this hundredth birthday: pick one piece of the long work and carry it. Tend the library. Coach the kids. Check on the elder down the street. Plant the tree.\n\nA hundred years from now, someone will stand in this hall and thank people they never met. Let us give them reason to.\n\nThank you.'},
 {t:'Go Build Something That Matters',g:'commencement',venue:'Graduation Address',text:'Graduates —\n\nYou are about to be told, many times, to "follow your passion." I want to offer a friendly amendment: follow your passion to the intersection where it meets someone else\'s need. That intersection is where the good careers — and the good lives — are built.\n\nPassion alone is a hobby. Need alone is a grind. Together, they are a calling.\n\nYou will also be told to move fast. Sometimes you should. But the things that matter most — trust, mastery, character — are slow. They are built in the unphotographed hours: the extra draft, the kept promise, the apology offered first.\n\nExpect to be bad at things. You were bad at walking once. Incompetence is not a verdict; it is a phase, and the only way out is through.\n\nAnd when you succeed — and many of you will — remember that success is a loan, not a possession. Pay it forward with interest: mentor someone, fund something, open a door and hold it.\n\nCongratulations. Now go build something that matters — and bring someone with you.'},
 {t:'We Remember Them Whole',g:'memorial',venue:'Memorial Dedication',text:'We gather to remember — and to remember wholly.\n\nIt is tempting, in grief, to polish the memory until it shines too bright to recognize. To speak only of virtues and skip the rest. But the people we honor today deserve better than statues. They deserve the truth of who they were.\n\nThey were brave — and they were afraid, and they went anyway. They were generous — and they were stubborn, and funny, and occasionally impossible. They burned the toast. They told the same story twice. They loved fiercely and imperfectly, the way real people do.\n\nWe remember them whole because wholeness is the point. A perfect memory is a small one. A whole memory is large enough to live in — large enough to teach us.\n\nSo let us carry them forward not as legends but as examples: proof that ordinary people, with ordinary flaws, can do extraordinary things for each other.\n\nWe remember them. All of them. Always.'},
 {t:'The Work Begins Today',g:'inaugural',venue:'Inaugural Address (Sample)',text:'My fellow citizens —\n\nToday is not an ending. It is a beginning — and beginnings belong to all of us, not to any one person standing at any one podium.\n\nThe challenges before us are real, and I will not insult you by pretending they are simple. They will require more than slogans. They will require the oldest technologies we have: listening, compromising, and keeping our word.\n\nI make you three promises. First: I will tell you the truth, even when it is uncomfortable — especially then. Second: I will measure every decision by one question — does it help the people who sent us here? Third: I will never confuse the office with the person. The office is yours. I am only its temporary keeper.\n\nBut I ask something of you in return. Democracy is not a spectator sport. It needs your attention, your voice, and occasionally your patience.\n\nThe work begins today. Let us do it together — and let us do it worthy of the people who did it before us.\n\nThank you, and may we all prove equal to this moment.'},
 {t:'The River Is Everyone\'s',g:'advocacy',venue:'Clean Water Rally',text:'Look at this river.\n\nIt does not check your party registration before it flows past your town. It does not ask your income before your children swim in it. The river is everyone\'s — which means its protection is everyone\'s job.\n\nFor too long we have treated our common waters as an afterthought and our common air as an ashtray. We have acted as if "the environment" were somewhere else — a postcard, a documentary, somebody else\'s problem.\n\nIt is here. It is the water in your glass. It is the air in your child\'s lungs.\n\nThe good news: rivers recover. Given half a chance — given clean enforcement, honest science, and citizens who refuse to look away — a river can come back in a single generation. We have seen it happen. We can make it happen again.\n\nSo I am asking you to do three things: learn your watershed, hold your officials accountable, and bring one neighbor with you next time.\n\nThe river is everyone\'s. Let\'s keep it that way.'},
 {t:'What We Owe the Future',g:'scientific',venue:'Science Symposium Keynote',text:'Every generation inherits a set of unanswered questions and a set of tools. Our tools have never been sharper. Our questions have never been bigger.\n\nWe can now read the code of life, image the edge of the observable universe, and model the climate decades out. With that power comes a debt — not to our funders, not to our institutions, but to the future.\n\nScience owes the future three things. First: honesty. Publish the negative result. Admit the uncertainty. The public\'s trust is our most precious instrument, and it breaks easily.\n\nSecond: openness. Knowledge locked behind paywalls and patents helps shareholders; knowledge shared helps humanity. Default to open.\n\nThird: humility. Every confident generation has been humbled by the next discovery. Hold your theories lightly and your evidence tightly.\n\nThe universe is under no obligation to make sense to us — and yet, astonishingly, it often does. That is the miracle we serve.\n\nLet us be worthy of it.'},
 {t:'The Stories We Carry',g:'cultural',venue:'Arts Festival Opening',text:'Every culture is a story we tell ourselves about who we are — and every story needs tellers.\n\nThe painter mixing color at midnight. The grandmother teaching the old songs. The teenager filming their neighborhood like it matters — because it does. These are not decorations on a society. They are the society.\n\nWe sometimes treat art as a luxury, the first thing cut and the last thing funded. That is backwards. In hard times, people do not stop singing; they sing louder. Art is not what we do after the important work. It is how we remember why the work matters.\n\nSo support your local tellers. Buy the painting. Attend the play. Fund the library. And tell your own story — badly, at first, then better.\n\nA community that tells its stories will never be truly lost. The stories are the map home.\n\nEnjoy the festival.'},
 {t:'Thank You, and Keep Going',g:'farewell',venue:'Farewell Address (Sample)',text:'When I started, I thought leadership was about having the answers. I leave knowing it is about asking better questions — and about the people who answer them alongside you.\n\nI want to thank the people who did the unglamorous work: the ones who arrived early, stayed late, fixed what broke, and never asked for credit. You know who you are. I know who you are. That will have to be enough — though it was always more than enough.\n\nWe did not finish everything. No one ever does. The unfinished work is not a failure; it is an invitation, extended to whoever comes next.\n\nTo my successor: the desk is yours, the problems are real, and the people are wonderful. Trust them.\n\nTo everyone else: keep going. The arc of our work bends toward better, but only if we keep bending it.\n\nThank you — for the privilege, for the patience, and for the proof, daily given, that people working together can do hard things.\n\nKeep going.'}
];
function generate(seed,opts){
 opts=opts||{}; var s=prng(seed);
 var genre=opts.genre&&GENRES.indexOf(opts.genre)>=0?opts.genre:null;
 var pool=genre?SPEECHES.filter(function(x){return x.g===genre;}):SPEECHES;
 var sp=pick(pool.length?pool:SPEECHES,s);
 var words=sp.text.split(/\s+/).length;
 var mins=Math.max(2,Math.round(words/130));
 var program='(function(){\n var text=document.getElementById("sph-text").innerText;\n var u=new SpeechSynthesisUtterance(text);\n u.rate=0.95;\n speechSynthesis.cancel(); speechSynthesis.speak(u);\n})();\n// Orator\'s read-aloud: paste into a page holding the speech in #sph-text.\n// About '+mins+' minutes at speaking pace.';
 return {
  id:PREFIX+pad(seed),
  title:sp.t+' — '+sp.venue+' (No. '+seed+')',
  speaker:'Signature Oratory Workshop (sample)',
  description:'A complete original '+sp.g+' speech, "'+sp.t+'", delivered as a Signature sample ('+sp.venue+'). The FULL TEXT is included — about '+words+' words, roughly '+mins+' minutes spoken. A Signature-authored sample, clearly labeled, never presented as a harvested historic address.',
  genre:sp.g, type:'speech',
  venue:sp.venue,
  transcript:sp.text, transcript_status:'full — original Signature work',
  word_count:words, estimated_minutes:mins,
  license:'Signature sample — original work, property of Justin Addam Higgins',
  demo:{kind:'orator-read-aloud',program:program,note:'Orator read-aloud program via the Web Speech API. Runs as-is in any PC browser.'},
  src:'signature-generated-sample', _seed:seed
 };
}
function validate(r){
 var e=[];
 if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
 if(!/^JAH-SPH-\d{6}$/.test(r.id||''))e.push('id');
 if(typeof r.title!=='string'||r.title.length<8)e.push('title');
 if(typeof r.description!=='string'||r.description.length<60)e.push('description');
 if(GENRES.indexOf(r.genre)<0)e.push('genre');
 if(typeof r.transcript!=='string'||r.transcript.length<400)e.push('transcript');
 if(!r.demo||typeof r.demo.program!=='string')e.push('demo');
 if(r.src!=='signature-generated-sample')e.push('src');
 return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
 var dups=(sample||[]).filter(function(r){return r&&(r.t===record.title||r.title===record.title);});
 return dups.length?{ok:false,errors:['duplicate title in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-public-speeches-1.0',generate:generate,validate:validate,driftCheck:driftCheck,genres:GENRES};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-speeches',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
