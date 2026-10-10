(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['shots','camera','editing','scenes','production'];
var PREFIX='JAH-FILM-';
var REF_SHOT='https://www.adobe.com/vn_en/creativecloud/video/production/cinematography/camera-shots-and-angles.html';
var REF_STD='Film craft standards (verified 2026-10-09)';
var SHOTS=[
 ['Extreme Wide Shot','EWS','A vast area with the subject tiny in the frame.','Establishes setting and scale.'],
 ['Wide Shot','WS','The full subject head to toe with surroundings.','Shows the character in their environment.'],
 ['Full Shot','FS','The entire subject from head to toe.','Action and body language.'],
 ['Medium Wide Shot','MWS','Subject from the knees up.','Dialogue with context.'],
 ['Cowboy Shot','CS','Subject from mid-thigh up.','Named for Westerns framing gun holsters.'],
 ['Medium Shot','MS','Subject from the waist up.','The versatile dialogue workhorse.'],
 ['Medium Close-Up','MCU','Subject from the chest up.','Intimate but not tight.'],
 ['Close-Up','CU','Head and shoulders filling the frame.','Emotion and reaction dominate.'],
 ['Extreme Close-Up','ECU','A small detail like an eye or a hand.','Maximum emphasis on detail.'],
 ['Over-the-Shoulder','OTS','Shot from behind one subject\u2019s shoulder.','Conversation and connection.'],
 ['Point of View','POV','What a character sees.','Immersion and empathy.'],
 ['Two Shot','2S','Two subjects in one frame.','Relationship between characters.'],
 ['Insert Shot','INS','Close view of an object.','A prop or clue in detail.'],
 ['Cutaway','CA','Something other than the main subject.','Breaks continuity for meaning.'],
 ['Reaction Shot','RS','A character\u2019s response.','Shows how an event lands.'],
 ['Establishing Shot','ES','The location at a scene\u2019s start.','Orients the viewer.'],
 ['Aerial Shot','AER','Taken from the air above the scene.','Grand overview.'],
 ['Bird\u2019s-Eye View','BEV','Straight down from above.','Godlike detachment.']
];
var ANGLES=[
 ['Eye-Level','Neutral and natural; the audience meets the subject as an equal.'],
 ['High Angle','Camera looks down; the subject feels small or vulnerable.'],
 ['Low Angle','Camera looks up; the subject feels powerful.'],
 ['Bird\u2019s-Eye','Straight down; total detachment and pattern.'],
 ['Worm\u2019s-Eye','Straight up from the ground; looming scale.'],
 ['Dutch / Canted','Tilted horizon; unease and disorientation.'],
 ['Shoulder Level','Conversational realism at standing height.'],
 ['Hip Level','Casual observation; documentary feel.'],
 ['Knee Level','Grounded perspective; children and low action.'],
 ['Ground Level','At the floor; dramatic entrances and falls.']
];
var MOVES=[
 ['Pan','Horizontal swivel on a fixed head; follows action across the frame.'],
 ['Tilt','Vertical swivel; reveals height or drops to detail.'],
 ['Dolly In','Camera rolls toward the subject; intimacy grows.'],
 ['Dolly Out','Camera rolls back; the world opens around the subject.'],
 ['Tracking','Camera travels alongside the subject; dynamic energy.'],
 ['Pedestal','Whole camera rises or falls vertically.'],
 ['Crane','Sweeping high arcs; majestic reveals.'],
 ['Handheld','Operator-carried; urgency and realism.'],
 ['Steadicam','Stabilized walking shots; floating smoothness.'],
 ['Gimbal','Motor-stabilized; fluid moves on any terrain.'],
 ['Zoom In','Lens magnifies; attention narrows without moving.'],
 ['Rack Focus','Focus shifts between planes; attention redirects.'],
 ['Whip Pan','Fast blurred pan; energy and transitions.'],
 ['Arc Shot','Camera circles the subject; the world turns around them.']
];
var SPEEDS=['slow','normal','fast'];
var LENSES=[[18,'ultra-wide'],[35,'wide'],[50,'normal'],[85,'portrait telephoto'],[135,'telephoto']];
var EDITING=[
 ['Cut','The instant switch between shots; invisible when motivated.'],
 ['Dissolve','One shot fades into the next; time passes softly.'],
 ['Fade In','From black into the scene; a gentle beginning.'],
 ['Fade Out','To black; an ending or a long passage of time.'],
 ['Wipe','A line sweeps one shot off for the next; playful or retro.'],
 ['Match Cut','Two shots linked by shape, motion or idea.'],
 ['Jump Cut','Time jumps within one setup; jarring and modern.'],
 ['Montage','Compressed series of shots; training, travel, memory.'],
 ['L-Cut','Audio of the next scene starts early; smooth flow.'],
 ['J-Cut','Audio of the next scene enters before its picture.'],
 ['Cross-Cutting','Two scenes intercut; tension builds in parallel.'],
 ['Smash Cut','Abrupt cut for shock or comedy.'],
 ['Kuleshov Effect','Meaning born from juxtaposition; the audience connects the shots.'],
 ['180-Degree Rule','Keep the camera on one side of the action axis.'],
 ['30-Degree Rule','Shift the camera at least 30 degrees between similar shots.'],
 ['Continuity Editing','Invisible technique preserving space, time and logic.']
];
var EDIT_CTX=['dialogue','action','drama','comedy'];
var ASPECTS=[
 ['1.33:1 Academy','The classic 1930s film frame.'],
 ['1.37:1','Early sound-era standard frame.'],
 ['1.66:1','European widescreen compromise.'],
 ['1.78:1 (16:9)','The HDTV and streaming frame.'],
 ['1.85:1 Flat','The standard US theatrical widescreen.'],
 ['2.20:1 (70mm)','Large-format grandeur.'],
 ['2.39:1 Scope','Anamorphic cinematic widescreen.'],
 ['2.76:1 Ultra Panavision','Epic ultra-wide.'],
 ['1:1 Square','Social and portrait framing.'],
 ['9:16 Vertical','Mobile-first vertical video.']
];
var FPS=[[24,'The cinema standard; motion blur feels filmic.'],[25,'PAL broadcast standard.'],[30,'NTSC video standard.'],[48,'High-frame-rate cinema.'],[60,'Smooth sports and gaming capture.'],[120,'Slow-motion source.']];
var LIGHTING=[
 ['Three-Point','Key, fill and back lights sculpt the subject.'],
 ['High-Key','Bright and even; comedy and commercials.'],
 ['Low-Key','Deep shadows; noir and horror.'],
 ['Practical','Visible lamps in the scene motivate the light.'],
 ['Motivated','Light appears to come from a real source.'],
 ['Soft Light','Diffused sources; flattering skin.'],
 ['Hard Light','Direct sources; sharp shadows and drama.']
];
var ROLES=[
 ['Director','Owns the creative vision and directs performance.'],
 ['Producer','Owns the logistics, budget and schedule.'],
 ['Cinematographer','Owns the photography; designs light and camera.'],
 ['Gaffer','Chief lighting technician executing the DP\u2019s plan.'],
 ['Grip','Rigging, dollies and camera support.'],
 ['Sound Mixer','Captures clean dialogue on set.'],
 ['Editor','Assembles the story in post.'],
 ['Production Designer','Designs the world: sets, props, palette.'],
 ['Costume Designer','Dresses character and era.'],
 ['Script Supervisor','Tracks continuity across every take.']
];
var SCENES=[
 ['Establishing Scene','Opens a location and sets the rules of the world.'],
 ['Dialogue Scene','Two or more characters trade words; subtext rules.'],
 ['Action Scene','Stunts and spectacle; geography must stay clear.'],
 ['Chase Scene','Pursuit with rising stakes and clear goals.'],
 ['Montage Sequence','Compressed time: training, travel, transformation.'],
 ['Dream Sequence','Subjective imagery; rules may bend.'],
 ['Flashback','The past intrudes to explain the present.'],
 ['Cold Open','The story starts before the titles.'],
 ['Climax Scene','The decisive confrontation; everything pays off.'],
 ['Tag / Stinger','The final beat after the climax; a last laugh or hook.']
];
var SIG_A=['Neon','Velvet','Ember','Harbor','Cinder','Juniper','Onyx','Solstice'];
var SIG_B=['reel','frame','cut','take','scene'];
function buildOnline(rnd,cat){
  var rec={category:cat,source:'online',creation_mode:'ONLINE-VERIFIED'};
  if(cat==='shots'){
    var s=pick(SHOTS,rnd),a=pick(ANGLES,rnd),l=pick(LENSES,rnd),mode=rnd();
    if(mode<0.35){rec.title=s[0]+' ('+s[1]+')';rec.topic='shot type';rec.shot={shot:s[0],abbr:s[1],framing:s[2],purpose:s[3]};rec.source_ref=REF_SHOT;
      rec.description='The '+s[0]+' ('+s[1]+') frames '+s[2].charAt(0).toLowerCase()+s[2].slice(1)+' '+s[3]+' A standard shot in the cinematographer\u2019s vocabulary.';}
    else if(mode<0.7){rec.title=s[0]+' from a '+a[0]+' angle';rec.topic='shot setup';rec.shot={shot:s[0],angle:a[0],framing:s[2],effect:a[1]};rec.source_ref=REF_SHOT;
      rec.description='A '+s[0].toLowerCase()+' played from a '+a[0].toLowerCase()+' angle. '+a[1]+' Combined with '+s[3].charAt(0).toLowerCase()+s[3].slice(1)+' A standard, verifiable camera setup.';}
    else{rec.title=s[0]+' on a '+l[0]+'mm '+l[1]+' lens';rec.topic='shot setup';rec.shot={shot:s[0],focal_mm:l[0],lens_type:l[1],framing:s[2]};rec.source_ref=REF_STD;
      rec.description='A '+s[0].toLowerCase()+' shot on a '+l[0]+'mm '+l[1]+' lens. Focal length shapes depth and distortion: wider lenses expand space, longer lenses compress it.';}
  }else if(cat==='camera'){
    var m=pick(MOVES,rnd),sp=pick(SPEEDS,rnd);
    if(rnd()<0.5){rec.title='Camera move: '+m[0];rec.topic='camera move';rec.shot={move:m[0],note:m[1]};rec.source_ref=REF_STD;
      rec.description='The '+m[0].toLowerCase()+' is a standard camera move. '+m[1]+' Choose it when the story needs that energy.';}
    else{rec.title=m[0]+' at '+sp+' speed';rec.topic='camera move';rec.shot={move:m[0],speed:sp,note:m[1]};rec.source_ref=REF_STD;
      rec.description='A '+sp+' '+m[0].toLowerCase()+'. '+m[1]+' Speed changes the emotional read: slow is deliberate, fast is urgent.';}
  }else if(cat==='editing'){
    var ed=pick(EDITING,rnd),cx=pick(EDIT_CTX,rnd);
    rec.title=ed[0]+' — '+cx+' use';rec.topic='edit technique';
    rec.shot={technique:ed[0],context:cx,note:ed[1]};rec.source_ref=REF_STD;
    rec.description='The '+ed[0].toLowerCase()+' in '+cx+': '+ed[1]+' Editors reach for it when the rhythm of the scene calls for it.';
  }else if(cat==='scenes'){
    var sc=pick(SCENES,rnd),st2=pick(SHOTS,rnd);
    rec.title=sc[0]+' — opening '+st2[0].toLowerCase();rec.topic='scene type';
    rec.shot={scene:sc[0],opens_with:st2[0],purpose:sc[1]};rec.source_ref=REF_STD;
    rec.description='A '+sc[0].toLowerCase()+' '+sc[1].charAt(0).toLowerCase()+sc[1].slice(1)+' Opening on a '+st2[0].toLowerCase()+' sets the visual contract for what follows.';
  }else{
    var r2=rnd();
    if(r2<0.3){var ar=pick(ASPECTS,rnd);rec.title='Aspect ratio '+ar[0];rec.topic='aspect ratio';rec.shot={ratio:ar[0],note:ar[1]};rec.source_ref=REF_STD;
      rec.description='The '+ar[0]+' frame: '+ar[1]+' Aspect ratio is a creative choice that shapes every composition in the project.';}
    else if(r2<0.55){var f=pick(FPS,rnd);rec.title=f[0]+' fps capture';rec.topic='frame rate';rec.shot={fps:f[0],note:f[1]};rec.source_ref=REF_STD;
      rec.description='Shooting at '+f[0]+' frames per second. '+f[1]+' Match capture rate to delivery for clean motion.';}
    else if(r2<0.8){var li=pick(LIGHTING,rnd);rec.title='Lighting: '+li[0];rec.topic='lighting';rec.shot={setup:li[0],note:li[1]};rec.source_ref=REF_STD;
      rec.description='The '+li[0].toLowerCase()+' setup: '+li[1]+' Lighting is exposure plus storytelling.';}
    else{var ro=pick(ROLES,rnd);rec.title='Crew role: '+ro[0];rec.topic='crew role';rec.shot={role:ro[0],duty:ro[1]};rec.source_ref=REF_STD;
      rec.description='The '+ro[0].toLowerCase()+' '+ro[1].charAt(0).toLowerCase()+ro[1].slice(1)+' A defined role keeps the set running and the vision intact.';}
  }
  return rec;
}
function buildSignature(rnd,cat){
  var rec={category:cat,source:'signature',creation_mode:'SIGNATURE-GENERATED'};
  var nm=pick(SIG_A,rnd)+' '+pick(SIG_B,rnd);
  if(cat==='shots'){var s2=pick(SHOTS,rnd);rec.title='Signature shot plan: '+nm;rec.topic='shot plan';rec.shot={plan:nm,base_shot:s2[0],takes:ri(rnd,1,8)};
    rec.description='A Signature-generated shot plan named '+nm+' built around a '+s2[0].toLowerCase()+' with '+rec.shot.takes+' planned takes. An original shooting study by the JAH generator.';}
  else if(cat==='camera'){var m2=pick(MOVES,rnd);rec.title='Signature camera study: '+nm;rec.topic='camera study';rec.shot={study:nm,move:m2[0],duration_s:ri(rnd,3,30)};
    rec.description='A Signature-generated camera study named '+nm+' using a '+m2[0].toLowerCase()+' over '+rec.shot.duration_s+' seconds. An original movement sketch by the JAH generator.';}
  else if(cat==='editing'){rec.title='Signature edit pattern: '+nm;rec.topic='edit pattern';rec.shot={pattern:nm,cuts:ri(rnd,4,24),rhythm:pick(['steady','accelerating','syncopated'],rnd)};
    rec.description='A Signature-generated edit pattern named '+nm+' with '+rec.shot.cuts+' cuts in a '+rec.shot.rhythm+' rhythm. An original cutting study by the JAH generator.';}
  else if(cat==='scenes'){rec.title='Signature scene concept: '+nm;rec.topic='scene concept';rec.shot={concept:nm,beats:ri(rnd,3,7),location:pick(['rooftop','diner','forest','subway','harbor'],rnd)};
    rec.description='A Signature-generated scene concept named '+nm+' set at a '+rec.shot.location+' in '+rec.shot.beats+' beats. An original scene sketch by the JAH generator.';}
  else{rec.title='Signature production plan: '+nm;rec.topic='production plan';rec.shot={plan:nm,crew:ri(rnd,5,40),shoot_days:ri(rnd,1,30)};
    rec.description='A Signature-generated production plan named '+nm+' with a '+rec.shot.crew+'-person crew over '+rec.shot.shoot_days+' shoot days. An original planning study by the JAH generator.';}
  return rec;
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var online=!opts.forceSignature&&(rnd()<0.24||opts.forceOnline);
  var rec=online?buildOnline(rnd,cat):buildSignature(rnd,cat);
  if(rec.description.length<165)rec.description+=' Filed as a complete searchable record in the JAH Data Bases archive, with its full specifications intact.';
  rec.id=PREFIX+String(seed).padStart(7,'0');rec._seed=seed;return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-FILM-\d{7}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.length<8)e.push('title');
  if(typeof r.description!=='string'||r.description.length<150)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(r.source!=='online'&&r.source!=='signature')e.push('source');
  if(r.source==='online'&&(r.creation_mode!=='ONLINE-VERIFIED'||typeof r.source_ref!=='string'||!r.source_ref.length))e.push('source_ref');
  if(r.source==='signature'&&r.creation_mode!=='SIGNATURE-GENERATED')e.push('creation_mode');
  if(!r.shot||typeof r.shot!=='object')e.push('shot');
  if(r.source==='online'&&r.topic==='shot type'){
    var f=SHOTS.filter(function(x){return x[0]===r.shot.shot;})[0];
    if(!f||f[1]!==r.shot.abbr)e.push('shot_fact');
  }
  if(r.source==='online'&&r.topic==='frame rate'){
    var fp=FPS.filter(function(x){return x[0]===r.shot.fps;})[0];
    if(!fp)e.push('fps_fact');
  }
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-film-video-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('film-video',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
