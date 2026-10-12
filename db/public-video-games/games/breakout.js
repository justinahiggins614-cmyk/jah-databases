/* Breakout — brick-breaker arcade. Openly licensed original (MIT) for the Public Video Games Database. */
PVG.register('breakout', {
  title:'Breakout', W:480, H:560,
  controls:{ dpad:false, buttons:[{k:'left',label:'◀'},{k:'right',label:'▶'}], dragx:true },
  help:'Clear all bricks. Move with ←/→ (A/D, numpad 4/6), drag on the court, or use ◀ ▶. Press SPACE to launch.',
  init:function(P){ this.reset(P); },
  reset:function(P){
    this.pw=80; this.ph=12; this.px=P.W/2-this.pw/2;
    this.ball={x:P.W/2,y:P.H-90,vx:0,vy:0,r:7,stuck:true};
    this.lives=3; this.score=0; this.over=false; this.win=false;
    this.bricks=[]; var cols=8, rows=5;
    var bw=(P.W-40)/cols;
    var colors=['#e5484d','#ff8b3e','#ffd43b','#00e5a0','#2f7bff'];
    for(var r=0;r<rows;r++) for(var c=0;c<cols;c++)
      this.bricks.push({x:20+c*bw,y:60+r*26,w:bw-4,h:22,color:colors[r],hp:1});
  },
  update:function(P,dt){
    if(this.over||this.win){ if(P.pressed.start||P.pressed.a) this.reset(P); return; }
    var k=P.keys, sp=420;
    if(k.left) this.px-=sp*dt;
    if(k.right) this.px+=sp*dt;
    if(P.dragX!==null) this.px=P.dragX-this.pw/2;
    this.px=Math.max(4,Math.min(P.W-this.pw-4,this.px));
    var b=this.ball;
    if(b.stuck){
      b.x=this.px+this.pw/2; b.y=P.H-110;
      if(P.pressed.a||P.pressed.start){ b.stuck=false; b.vx=200*(Math.random()<0.5?-1:1); b.vy=-300; P.beep(500,.06); }
      return;
    }
    b.x+=b.vx*dt; b.y+=b.vy*dt;
    if(b.x-b.r<0){b.x=b.r;b.vx=Math.abs(b.vx);P.beep(280,.04);}
    if(b.x+b.r>P.W){b.x=P.W-b.r;b.vx=-Math.abs(b.vx);P.beep(280,.04);}
    if(b.y-b.r<0){b.y=b.r;b.vy=Math.abs(b.vy);P.beep(280,.04);}
    var py=P.H-96;
    if(b.vy>0 && b.y+b.r>py && b.y+b.r<py+this.ph+14 && b.x>this.px-6 && b.x<this.px+this.pw+6){
      var rel=(b.x-(this.px+this.pw/2))/(this.pw/2);
      var spd=Math.min(560,Math.hypot(b.vx,b.vy)+8);
      b.vx=rel*spd*0.9; b.vy=-Math.sqrt(Math.max(100,spd*spd-b.vx*b.vx));
      P.beep(560,.05);
    }
    for(var i=this.bricks.length-1;i>=0;i--){
      var br=this.bricks[i];
      if(b.x+b.r>br.x&&b.x-b.r<br.x+br.w&&b.y+b.r>br.y&&b.y-b.r<br.y+br.h){
        this.bricks.splice(i,1); this.score+=50; b.vy=-b.vy; P.beep(760,.05);
        break;
      }
    }
    if(b.y-b.r>P.H){
      this.lives--;
      P.beep(150,.25,'sawtooth');
      if(this.lives<=0){ this.over=true; }
      else { b.stuck=true; }
    }
    if(!this.bricks.length){ this.win=true; P.beep(880,.3); }
  },
  draw:function(P,ctx){
    ctx.fillStyle='#0d1526'; ctx.fillRect(0,0,P.W,P.H);
    for(var i=0;i<this.bricks.length;i++){
      var br=this.bricks[i];
      ctx.fillStyle=br.color; ctx.fillRect(br.x,br.y,br.w,br.h);
    }
    var b=this.ball;
    ctx.fillStyle='#fff'; ctx.beginPath(); ctx.arc(b.x,b.y,b.r,0,7); ctx.fill();
    ctx.fillStyle='#00e5a0'; ctx.fillRect(this.px,P.H-96,this.pw,this.ph);
    P.text('SCORE '+this.score+'   LIVES '+this.lives, P.W/2, 22, 15, '#9fb3d8');
    if(b.stuck&&!this.over) P.text('Press SPACE / A to launch', P.W/2, P.H/2, 15, '#ffb020');
    if(this.over) P.text('GAME OVER — press START to retry', P.W/2, P.H/2, 16, '#ff6b6b');
    if(this.win) P.text('YOU WIN! — press START for new game', P.W/2, P.H/2, 16, '#00e5a0');
  }
});
