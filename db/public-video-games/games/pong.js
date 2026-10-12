/* Pong — classic table-tennis arcade. Openly licensed original (MIT) for the Public Video Games Database. */
PVG.register('pong', {
  title:'Pong', W:480, H:360,
  controls:{ dpad:false, buttons:[{k:'up',label:'▲'},{k:'down',label:'▼'}], dragx:false },
  help:'First to 7 wins. Move with W/S or ↑/↓ (numpad 8/2), drag on the court, or use the ▲▼ buttons.',
  init:function(P){ this.reset(P); },
  reset:function(P){
    this.pw=10; this.ph=70;
    this.pl={y:P.H/2-this.ph/2, s:0}; this.ai={y:P.H/2-this.ph/2, s:0};
    this.ball={x:P.W/2,y:P.H/2,vx:0,vy:0,r:7};
    this.serve(P, Math.random()<0.5?1:-1); this.over=false;
  },
  serve:function(P,dir){
    this.ball.x=P.W/2; this.ball.y=P.H/2;
    var sp=260, a=(Math.random()*0.6-0.3);
    this.ball.vx=Math.cos(a)*sp*dir; this.ball.vy=Math.sin(a)*sp;
  },
  update:function(P,dt){
    if(this.over){ if(P.pressed.start||P.pressed.a) this.reset(P); return; }
    var k=P.keys, sp=340;
    if(k.up||k.w) this.pl.y-=sp*dt;
    if(k.down||k.s) this.pl.y+=sp*dt;
    if(P.dragX!==null){ /* drag anywhere moves paddle by y */ }
    var taps=P.tapQ;
    for(var i=0;i<taps.length;i++){
      var ty=taps[i].y, mid=this.pl.y+this.ph/2;
      if(ty<mid-14) this.pl.y-=130;
      else if(ty>mid+14) this.pl.y+=130;
    }
    P.clearTaps();
    this.pl.y=Math.max(0,Math.min(P.H-this.ph,this.pl.y));
    // AI
    var cy=this.ai.y+this.ph/2, aspd=240+this.pl.s*12+this.ai.s*12;
    if(cy<this.ball.y-8) this.ai.y+=aspd*dt;
    else if(cy>this.ball.y+8) this.ai.y-=aspd*dt;
    this.ai.y=Math.max(0,Math.min(P.H-this.ph,this.ai.y));
    // ball
    var b=this.ball;
    b.x+=b.vx*dt; b.y+=b.vy*dt;
    if(b.y-b.r<0){b.y=b.r;b.vy=Math.abs(b.vy);P.beep(300,.04);}
    if(b.y+b.r>P.H){b.y=P.H-b.r;b.vy=-Math.abs(b.vy);P.beep(300,.04);}
    // paddles
    if(b.vx<0 && b.x-b.r<this.pw && b.y>this.pl.y && b.y<this.pl.y+this.ph){
      var rel=(b.y-(this.pl.y+this.ph/2))/(this.ph/2);
      var spd=Math.min(520,Math.hypot(b.vx,b.vy)*1.06);
      b.vx=Math.abs(Math.cos(rel*0.9))*spd; b.vy=Math.sin(rel*0.9)*spd;
      b.x=this.pw+b.r; P.beep(520,.05);
    }
    if(b.vx>0 && b.x+b.r>P.W-this.pw && b.y>this.ai.y && b.y<this.ai.y+this.ph){
      var rel2=(b.y-(this.ai.y+this.ph/2))/(this.ph/2);
      var spd2=Math.min(520,Math.hypot(b.vx,b.vy)*1.06);
      b.vx=-Math.abs(Math.cos(rel2*0.9))*spd2; b.vy=Math.sin(rel2*0.9)*spd2;
      b.x=P.W-this.pw-b.r; P.beep(420,.05);
    }
    if(b.x<-20){ this.ai.s++; P.beep(140,.2,'sawtooth'); this.checkOver(P); this.serve(P,1); }
    if(b.x>P.W+20){ this.pl.s++; P.beep(660,.12); this.checkOver(P); this.serve(P,-1); }
  },
  checkOver:function(P){
    if(this.pl.s>=7||this.ai.s>=7){ this.over=true; P.beep(880,.3); }
  },
  draw:function(P,ctx){
    ctx.fillStyle='#0d1526'; ctx.fillRect(0,0,P.W,P.H);
    ctx.strokeStyle='#1d2c4d'; ctx.setLineDash([8,8]);
    ctx.beginPath(); ctx.moveTo(P.W/2,0); ctx.lineTo(P.W/2,P.H); ctx.stroke(); ctx.setLineDash([]);
    ctx.fillStyle='#00e5a0'; ctx.fillRect(0,this.pl.y,this.pw,this.ph);
    ctx.fillStyle='#2f7bff'; ctx.fillRect(P.W-this.pw,this.ai.y,this.pw,this.ph);
    ctx.fillStyle='#fff'; ctx.beginPath(); ctx.arc(this.ball.x,this.ball.y,this.ball.r,0,7); ctx.fill();
    P.text(this.pl.s+' : '+this.ai.s, P.W/2, 24, 26, '#e8f1ff');
    if(this.over) P.text((this.pl.s>=7?'YOU WIN!':'CPU WINS — press START to retry'), P.W/2, P.H/2, 18, '#ffb020');
  }
});
