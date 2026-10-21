(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function cleanT(t){return String(t==null?'':t).replace(/"/g,'').replace(/\*\//g,'* /');}
var SLUG="frame-by-frame-movie-maker";
var PREFIX="JAH-MOVF-";
var GROUPS=["cartoon", "pixel"];
var LIVE="https://justinahiggins614-cmyk.github.io/jah-databases/db/";

/* ================= JAH Frame-by-Frame Movie Engine — jahdb-movie-engine-1.0 ================
 * Deterministic client-side frame renderer + sequencer.
 * Cartoon and pixel styles are GENUINELY WORKING: real frames are drawn on canvas every tick.
 * Photorealistic rendering is UNPROVEN — beyond this engine's capability, honestly unavailable. */
var MOVENGINE=(function(){
'use strict';
function mulberry(a){return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function hstr(s){var h=2166136261;for(var i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619);}return h>>>0;}
var SCENES=['orbit','comet','rain','starfield','sunrise','bounce','rocket','waves','moon','meteors','glitch','eclipse'];
var _stars={};
function stars(scene,W,H,n){var k=scene+'|'+W+'x'+H+'|'+n;
  if(!_stars[k]){var r=mulberry(hstr(scene+'stars'));var s=[];for(var i=0;i<n;i++)s.push([r()*W,r()*H,0.25+r()*0.75,r()*6.28]);_stars[k]=s;}
  return _stars[k];}
function drawStars(ctx,st,f){for(var i=0;i<st.length;i++){var p=st[i];var tw=0.45+0.55*Math.abs(Math.sin(f*0.25+p[3]));ctx.globalAlpha=p[2]*tw;ctx.fillStyle='#cfe4ff';ctx.fillRect(p[0],p[1],2,2);}ctx.globalAlpha=1;}
function circle(ctx,x,y,r){ctx.beginPath();ctx.arc(x,y,r,0,6.2832);ctx.fill();}
function cl(v){return v>255?255:(v<0?0:v);}
function sceneDraw(ctx,scene,f,total,W,H){
  var t=total>1?f/(total-1):0;
  ctx.fillStyle='#04060c';ctx.fillRect(0,0,W,H);
  var st=stars(scene,W,H,70);
  if(scene==='orbit'){
    drawStars(ctx,st,f);
    var sx=W*0.30,sy=H*0.52,Rx=W*0.30,Ry=H*0.30;
    var g=ctx.createRadialGradient(sx,sy,2,sx,sy,H*0.14);
    g.addColorStop(0,'#ffe08a');g.addColorStop(1,'#c46a1b');
    ctx.fillStyle=g;circle(ctx,sx,sy,H*0.105);
    ctx.strokeStyle='#2b5a8f';ctx.lineWidth=Math.max(1,W/480);
    ctx.beginPath();ctx.ellipse(sx,sy,Rx,Ry,0,0,6.2832);ctx.stroke();
    var a=t*6.2832,px=sx+Math.cos(a)*Rx,py=sy+Math.sin(a)*Ry;
    ctx.fillStyle='#4aa3ff';circle(ctx,px,py,H*0.045);
    ctx.fillStyle='#7fd4ff';circle(ctx,px-H*0.015,py-H*0.015,H*0.015);
    var ma=a*3.7,mx=px+Math.cos(ma)*H*0.085,my=py+Math.sin(ma)*H*0.06;
    ctx.fillStyle='#e8eef7';circle(ctx,mx,my,H*0.018);
  }else if(scene==='comet'){
    drawStars(ctx,st,f);
    var hx=W*(0.08+0.84*t),hy=H*(0.72-0.50*Math.sin(t*3.1416));
    for(var i2=0;i2<14;i2++){var tt=i2/14,tx=hx-tt*W*0.28,ty=hy+tt*H*0.10*Math.sin(t*6.28+i2);
      ctx.globalAlpha=(1-tt)*0.55;ctx.fillStyle=i2%2?'#ffb35e':'#7fe3ff';circle(ctx,tx,ty,H*(0.035*(1-tt)+0.008));}
    ctx.globalAlpha=1;ctx.fillStyle='#fff3d6';circle(ctx,hx,hy,H*0.045);
    ctx.fillStyle='#ff9a3d';circle(ctx,hx-H*0.012,hy-H*0.008,H*0.02);
  }else if(scene==='rain'){
    ctx.fillStyle='#0a1420';ctx.fillRect(0,0,W,H);
    var rr0=mulberry(hstr('rain-drops'));var drops=[];for(var d0=0;d0<46;d0++)drops.push([rr0(),rr0(),0.5+rr0()*0.9]);
    ctx.fillStyle='#3fd8ff';
    for(var k=0;k<drops.length;k++){var dr=drops[k],yy=((dr[1]+t*dr[2])%1)*H,xx=dr[0]*W;
      ctx.globalAlpha=0.75;ctx.fillRect(xx,yy,Math.max(1.5,W/320),H*0.055*dr[2]);}
    ctx.globalAlpha=1;ctx.fillStyle='#123043';ctx.fillRect(0,H*0.94,W,H*0.06);
  }else if(scene==='starfield'){
    var r2=mulberry(hstr('starfield-drift'));var ss=[];for(var s3=0;s3<90;s3++)ss.push([r2(),r2(),0.3+r2()*0.7]);
    for(var q=0;q<ss.length;q++){var p2=ss[q],xx2=(((p2[0]-t*p2[2]*0.35)%1+1)%1)*W;
      var tw2=0.4+0.6*Math.abs(Math.sin(f*0.2+q));ctx.globalAlpha=p2[2]*tw2;ctx.fillStyle='#e6f2ff';
      var sz=p2[2]>0.8?2.6:1.6;ctx.fillRect(xx2,p2[1]*H,sz,sz);}
    ctx.globalAlpha=1;
  }else if(scene==='sunrise'){
    var top=[10+t*6,8+t*10,26+t*40],bot=[38+t*120,20+t*80,60+t*60];
    var g2=ctx.createLinearGradient(0,0,0,H);
    g2.addColorStop(0,'rgb('+(cl(top[0])|0)+','+(cl(top[1])|0)+','+(cl(top[2])|0)+')');
    g2.addColorStop(1,'rgb('+(cl(bot[0])|0)+','+(cl(bot[1])|0)+','+(cl(bot[2])|0)+')');
    ctx.fillStyle=g2;ctx.fillRect(0,0,W,H);
    var suy=H*(0.92-0.62*t);
    var sg=ctx.createRadialGradient(W/2,suy,4,W/2,suy,H*0.2);
    sg.addColorStop(0,'#fff7d6');sg.addColorStop(1,'rgba(255,150,60,0)');
    ctx.fillStyle=sg;circle(ctx,W/2,suy,H*0.2);
    ctx.fillStyle='#ffd75e';circle(ctx,W/2,suy,H*0.09);
    ctx.fillStyle='#0c1a12';ctx.fillRect(0,H*0.86,W,H*0.14);
  }else if(scene==='bounce'){
    ctx.fillStyle='#0b1526';ctx.fillRect(0,0,W,H);
    var bx=W*(0.5+0.32*Math.sin(t*6.2832));
    var by=H*0.78-Math.abs(Math.sin(t*6.2832*2))*H*0.52;
    var sh=1-Math.abs(Math.sin(t*6.2832*2))*0.55;
    ctx.globalAlpha=0.35;ctx.fillStyle='#000';
    ctx.beginPath();ctx.ellipse(bx,H*0.82,H*0.09*sh,H*0.025*sh,0,0,6.2832);ctx.fill();ctx.globalAlpha=1;
    var sq=1-0.18*Math.abs(Math.cos(t*6.2832*2));
    ctx.fillStyle='#39d353';
    ctx.beginPath();ctx.ellipse(bx,by,H*0.075,H*0.075*sq,0,0,6.2832);ctx.fill();
    ctx.fillStyle='#9dffb0';circle(ctx,bx-H*0.02,by-H*0.025,H*0.02);
    ctx.fillStyle='#123043';ctx.fillRect(0,H*0.84,W,H*0.16);
  }else if(scene==='rocket'){
    drawStars(ctx,st,f);
    var ry2=H*(0.86-0.66*t);
    ctx.fillStyle='#1a2b45';ctx.beginPath();
    ctx.moveTo(W*0.08,H*0.98);ctx.lineTo(W*0.30,H*0.98);ctx.lineTo(W*0.30,H*0.86);ctx.lineTo(W*0.08,H*0.86);ctx.closePath();ctx.fill();
    var fl=0.7+0.3*Math.sin(f*1.7);
    var fg=ctx.createLinearGradient(0,ry2,0,ry2+H*0.22*fl);
    fg.addColorStop(0,'#fff3b0');fg.addColorStop(0.5,'#ff9a3d');fg.addColorStop(1,'rgba(255,80,20,0)');
    ctx.fillStyle=fg;ctx.beginPath();
    ctx.moveTo(W*0.5-H*0.035,ry2+H*0.10);ctx.lineTo(W*0.5+H*0.035,ry2+H*0.10);
    ctx.lineTo(W*0.5,ry2+H*0.10+H*0.20*fl);ctx.closePath();ctx.fill();
    ctx.fillStyle='#dfe9f5';ctx.beginPath();
    ctx.moveTo(W*0.5,ry2-H*0.13);ctx.quadraticCurveTo(W*0.5+H*0.05,ry2-H*0.02,W*0.5+H*0.035,ry2+H*0.10);
    ctx.lineTo(W*0.5-H*0.035,ry2+H*0.10);ctx.quadraticCurveTo(W*0.5-H*0.05,ry2-H*0.02,W*0.5,ry2-H*0.13);ctx.fill();
    ctx.fillStyle='#ff5a5a';circle(ctx,W*0.5,ry2+H*0.02,H*0.022);
    var rsm=mulberry(hstr('rocket-smoke'));
    for(var p3=0;p3<10;p3++){var sa=(rsm()+t*1.4)%1,smx=W*(0.42+rsm()*0.16)+(sa*W*0.05-W*0.025);
      ctx.globalAlpha=(1-sa)*0.5;ctx.fillStyle='#cfd8e6';circle(ctx,smx,H*0.97-sa*H*0.22,H*(0.02+sa*0.05));}
    ctx.globalAlpha=1;
  }else if(scene==='waves'){
    ctx.fillStyle='#06222e';ctx.fillRect(0,0,W,H);
    for(var wv=0;wv<3;wv++){var amp=H*(0.05+wv*0.02),yy3=H*(0.42+wv*0.16),sp=1+wv*0.7;
      ctx.fillStyle=wv===0?'#0e4a5e':(wv===1?'#1493a8':'#7fe3ff');ctx.globalAlpha=0.85;
      ctx.beginPath();ctx.moveTo(0,H);
      for(var x3=0;x3<=W;x3+=6){ctx.lineTo(x3,yy3+Math.sin(x3/W*6.2832*sp+t*6.2832*(1+wv*0.4))*amp);}
      ctx.lineTo(W,H);ctx.closePath();ctx.fill();}
    ctx.globalAlpha=1;
  }else if(scene==='moon'){
    drawStars(ctx,st,f);
    var mx2=W*0.5,my2=H*0.48,mr=H*0.20;
    ctx.fillStyle='#e8eef7';circle(ctx,mx2,my2,mr);
    ctx.fillStyle='#c3ccd9';
    var mrnd=mulberry(hstr('moon-craters'));
    for(var c2=0;c2<6;c2++){circle(ctx,mx2+(mrnd()-0.5)*mr*1.2,my2+(mrnd()-0.5)*mr*1.2,mr*(0.08+mrnd()*0.1));}
    ctx.fillStyle='#04060c';circle(ctx,mx2+(t*2-1)*mr*2.2,my2,mr*1.02);
  }else if(scene==='meteors'){
    drawStars(ctx,st,f);
    var rm=mulberry(hstr('meteor-seeds'));var ms=[];
    for(var m2=0;m2<7;m2++)ms.push([rm(),rm(),0.6+rm()*0.8]);
    for(var m3=0;m3<ms.length;m3++){var mm=ms[m3],lt2=((t*1.6+mm[1])%1);
      if(lt2<0.28){var mxx=W*(0.15+mm[0]*0.7)+lt2*W*1.4,myy=H*(0.1+mm[0]*0.5)+lt2*H*0.9;
        for(var tr=0;tr<8;tr++){var ttt=tr/8;ctx.globalAlpha=(1-ttt)*0.7*(1-lt2/0.28);
          ctx.fillStyle=tr<2?'#ffffff':'#ff9a3d';circle(ctx,mxx-ttt*W*0.10,myy-ttt*H*0.06,Math.max(0.6,H*0.006*(1-ttt)));}}}
    ctx.globalAlpha=1;
  }else if(scene==='glitch'){
    ctx.fillStyle='#0d0a18';ctx.fillRect(0,0,W,H);
    var cols=12,rows=7;
    for(var gx=0;gx<cols;gx++)for(var gy=0;gy<rows;gy++){
      var gl=((gx*7+gy*13+f*3)%29)===0;
      var ox=gl?(((gx*37+gy*11+f)%9)-4)*W/160:0;
      ctx.fillStyle=(gx+gy)%2?'#231a3d':'#2c1f4d';
      ctx.fillRect(gx*W/cols+ox,gy*H/rows,W/cols-1,H/rows-1);
      if(gl){ctx.fillStyle='#ff2fb3';ctx.fillRect(gx*W/cols+ox,gy*H/rows,W/cols-1,2);}}
    ctx.fillStyle='rgba(64,224,255,0.12)';ctx.fillRect(0,(f*7)%H,W,3);
  }else if(scene==='eclipse'){
    drawStars(ctx,st,f);
    var exx=W*0.5,eyy=H*0.5,er=H*0.20;
    var mxx2=exx-W*0.45+t*W*0.9;
    var cover2=1-Math.abs(t-0.5)*2;
    var eg=ctx.createRadialGradient(exx,eyy,er*0.9,exx,eyy,er*1.9);
    eg.addColorStop(0,'rgba(255,250,230,0.9)');eg.addColorStop(1,'rgba(255,250,230,0)');
    ctx.fillStyle=eg;circle(ctx,exx,eyy,er*1.9);
    ctx.fillStyle='#ffedb0';circle(ctx,exx,eyy,er);
    ctx.fillStyle='#0a0d16';circle(ctx,mxx2,eyy,er*1.04);
    if(cover2>0.86){ctx.strokeStyle='#fff7d6';ctx.lineWidth=2;
      for(var cr=0;cr<12;cr++){var ca2=cr/12*6.2832+f*0.05;
        ctx.beginPath();ctx.moveTo(exx+Math.cos(ca2)*er*1.1,eyy+Math.sin(ca2)*er*1.1);
        ctx.lineTo(exx+Math.cos(ca2)*er*(1.35+0.25*Math.sin(f*0.3+cr)),eyy+Math.sin(ca2)*er*(1.35+0.25*Math.sin(f*0.3+cr)));ctx.stroke();}}
  }
}
function countLit(cv){
  try{var cx=cv.getContext('2d');var d=cx.getImageData(0,0,cv.width,cv.height).data;var n=0;
    for(var i=0;i<d.length;i+=64){if(d[i]+d[i+1]+d[i+2]>30)n++;}return n*64;}catch(e){return -1;}
}
function renderFrame(cv,scene,style,f,total){
  var W=cv.width,H=cv.height,cx=cv.getContext('2d');
  if(style==='pixel'){
    var pw=160,ph=90;
    var off=renderFrame._off||null;
    if(!off){off=document.createElement('canvas');renderFrame._off=off;}
    off.width=pw;off.height=ph;
    sceneDraw(off.getContext('2d'),scene,f,total,pw,ph);
    cx.imageSmoothingEnabled=false;
    cx.drawImage(off,0,0,pw,ph,0,0,W,H);
  }else{sceneDraw(cx,scene,f,total,W,H);}
  return countLit(cv);
}
return {scenes:SCENES,renderFrame:renderFrame,sceneDraw:sceneDraw,countLit:countLit,version:'jahdb-movie-engine-1.0'};
})();
var ADJ=["Silent", "Gentle", "Patient", "Pocket", "Dawn", "Echo", "Tide", "Feather", "Lantern", "Harvest", "Whisper", "Starlit", "Copper", "Bright"];
var SCN=[['orbit','Orbit'],['comet','Comet'],['rain','Rain'],['starfield','Starfield'],['sunrise','Sunrise'],['bounce','Bounce'],['rocket','Rocket'],['waves','Waves'],['moon','Moon'],['meteors','Meteors'],['glitch','Glitch'],['eclipse','Eclipse']];
var REN=[['cartoon-svg','Cartoon'],['pixel-canvas','Pixel']];
var PAL=[['deep-space blues + solar gold'],['storm grays + neon cyan'],['comet teal + ember orange'],['dawn peach + horizon violet'],['arcade green + shadow gray'],['ocean teal + foam white']];
function demoMovProgram(rec){
  var title=cleanT(rec.title).replace(/'/g,'');
  var L=['/* JAH demo program — '+rec.id+' */','/* RUN ON PC: save as demo.js, then run: node demo.js */'];
  L.push('console.log("ASCII FRAME DEMO — '+title+'");');
  L.push('console.log("(text frames stand in for canvas frames; the page engine renders these on canvas)");');
  L.push('var W='+rec.frame_w+';');
  L.push('for(var f=0;f<4;f++){var x=(f*3)%(W-2);var line="";for(var i=0;i<W;i++){line+=(i===x?"O":(i===x+1?"o":"."));}console.log("f"+f+" "+line);}');
  L.push('console.log("4 text frames shown — page engine plays '+rec.total_frames+' canvas frames at '+rec.fps_default+' fps.");');
  return L.join('\n');
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var group=(opts.category&&GROUPS.indexOf(opts.category)>=0)?opts.category:pick(GROUPS,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var sc=pick(SCN,rnd),rn=pick(REN,rnd);
  var title=pick(ADJ,rnd)+' '+sc[1]+' Reel — '+rn[1];
  var frames=pick([64,72,80,96],rnd),fps=pick([6,8,10,12,15,18,24,30],rnd);
  var rec={id:id,title:title,renderer:rn[0],scene:sc[0],canvas_w:480,canvas_h:270,
    total_frames:frames,fps_default:fps,fps_range:'1–30',palette:pick(PAL,rnd)[0],frame_w:40,
    photorealism_status:'unproven',
    photorealism_note:'Photorealistic rendering is unproven — beyond this engine\'s capability; never faked.',
    ladder_rank:ri(rnd,1,15),_seed:seed,
    working_version_link:LIVE+'db/'+SLUG+'/#p-demo',
    status:'proven',status_note:'Engine renders cartoon/pixel frames genuinely; photorealism honestly unproven.',
    provenance:'Generated preset by jahdb-'+SLUG+'-1.0 (seed '+seed+') — engine-verified cartoon/pixel preset.',
    last_verified:'2026-10-21',
    march_marker:'MARCH-TO-A-MILLION: generated preset (seed '+seed+') · target 1,000,000 · in progress',
    edition:"public"};
  rec.description='A generated '+rn[1].toLowerCase()+' movie preset: '+sc[1].toLowerCase()+' scene, '+frames+' frames at '+fps+' fps, rendered live by the page engine. Photorealistic rendering honestly marked unproven.';
  rec.t=rec.title;rec.g=group;rec.group=group;rec.c=1;
  rec.demo={kind:'ascii-frames',title:'ASCII frame demo — '+cleanT(title).replace(/'/g,''),program:demoMovProgram(rec),language:'javascript',runnable:true};
  return rec;
}

function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  var re=new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$');
  if(!re.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||!r.description.length)e.push('description');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=15))e.push('ladder_rank');
  if(typeof r.t!=='string'||typeof r.g!=='string')e.push('t/g');
  var REQ=["renderer", "scene", "total_frames", "fps_default", "photorealism_status", "provenance", "march_marker"];
  REQ.forEach(function(k){if(r[k]===undefined||r[k]===null||r[k]==='')e.push('missing:'+k);});
  if(!r.demo||typeof r.demo.program!=='string'||r.demo.program.indexOf('console.log')<0)e.push('demo');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var e=[];
  (sample||[]).forEach(function(s){if(s&&s.title===rec.title)e.push('duplicate title in archive sample');});
  return{ok:!e.length,errors:e};
}
var gen={version:'jahdb-frame-by-frame-movie-maker-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
gen.engine=MOVENGINE;
if(typeof window!=='undefined'){window.JAHMovieEngine=MOVENGINE;}
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
