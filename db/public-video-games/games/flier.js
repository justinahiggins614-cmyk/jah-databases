/* Flier — flap-through-the-pipes arcade. Openly licensed original (MIT) for the Public Video Games Database. */
PVG.register('flier', {
  title:'Flier', W:400, H:560,
  controls:{ tap:true, buttons:[{k:'a',label:'FLAP'}] },
  help:'Tap, click, or press SPACE to flap. Thread the pipes — one hit ends the run.',
  init:function(P){ this.reset(P); },
  reset:function(P){
    this.x=110; this.y=P.H/2; this.v=0;
    this.pipes=[]; this.t=0; this.score=0; this.best=this.best||0;
    this.alive=true; this.started=false;
  },
  addPipe:function(P){
    var gap=150, minY=90, maxY=P.H-90-gap;
    var y=minY+Math.random()*(maxY-minY);
    this.pipes.push({x:P.W+20,y:y,gap:gap,passed:false});
  },
  update:function(P,dt){
    if(P.pressed.a||P.pressed.start||P.tapQ.length){
      P.clearTaps();
      if(!this.alive){ this.reset(P); return; }
      this.started=true; this.v=-330; P.beep(600,.05);
    }
    if(!this.started||!this.alive) return;
    this.v+=1050*dt; this.y+=this.v*dt;
    this.t+=dt;
    if(this.t>1.5){ this.t=0; this.addPipe(P); }
    for(var i=this.pipes.length-1;i>=0;i--){
      var p=this.pipes[i]; p.x-=170*dt;
      if(p.x<-60){ this.pipes.splice(i,1); continue; }
      if(!p.passed&&p.x<this.x){ p.passed=true; this.score++; P.beep(880,.06); }
      var hw=26;
      if(this.x+12>p.x-hw&&this.x-12<p.x+hw){
        if(this.y-12<p.y||this.y+12>p.y+p.gap){ this.die(P); return; }
      }
    }
    if(this.y>P.H-10||this.y<0) this.die(P);
  },
  die:function(P){ this.alive=false; this.best=Math.max(this.best,this.score); P.beep(150,.35,'sawtooth'); },
  draw:function(P,ctx){
    ctx.fillStyle='#0d1526'; ctx.fillRect(0,0,P.W,P.H);
    ctx.fillStyle='#1d2c4d';
    this.pipes.forEach(function(p){
      ctx.fillRect(p.x-26,0,52,p.y);
      ctx.fillRect(p.x-26,p.y+p.gap,52,P.H-(p.y+p.gap));
      ctx.fillStyle='#0fbf7f';
      ctx.fillRect(p.x-26,p.y-14,52,14); ctx.fillRect(p.x-26,p.y+p.gap,52,14);
      ctx.fillStyle='#1d2c4d';
    });
    ctx.fillStyle='#ffd43b';
    ctx.beginPath(); ctx.arc(this.x,this.y,13,0,7); ctx.fill();
    ctx.fillStyle='#ff8b3e';
    ctx.beginPath(); ctx.moveTo(this.x+13,this.y); ctx.lineTo(this.x+24,this.y-7); ctx.lineTo(this.x+24,this.y+7); ctx.closePath(); ctx.fill();
    ctx.fillStyle='#070b16'; ctx.beginPath(); ctx.arc(this.x+5,this.y-3,2.6,0,7); ctx.fill();
    P.text(this.score, P.W/2, 60, 40, '#e8f1ff');
    P.text('BEST '+this.best, P.W/2, 96, 14, '#9fb3d8');
    if(!this.started) P.text('Tap / SPACE to start', P.W/2, P.H/2, 16, '#ffb020');
    if(!this.alive) P.text('CRASH — tap / SPACE to retry', P.W/2, P.H/2, 15, '#ff6b6b');
  }
});
