/* Asteroids — vector-style space shooter. Openly licensed original (MIT) for the Public Video Games Database. */
PVG.register('asteroids', {
  title:'Asteroids', W:480, H:560,
  controls:{ dpad:false, buttons:[{k:'left',label:'◀'},{k:'right',label:'▶'},{k:'up',label:'THRUST'},{k:'a',label:'FIRE'}] },
  help:'←/→ rotate, ↑ thrust, SPACE fire. Numpad 4/6/8/5 too. Blast every rock — big ones split.',
  init:function(P){ this.reset(P); },
  reset:function(P){
    this.ship={x:P.W/2,y:P.H/2,a:-Math.PI/2,vx:0,vy:0};
    this.rocks=[]; this.shots=[]; this.score=0; this.lives=3; this.over=false;
    this.inv=2;
    for(var i=0;i<5;i++) this.spawnRock(P,80);
  },
  spawnRock:function(P,r,x,y){
    this.rocks.push({
      x:x===undefined?Math.random()*P.W:x, y:y===undefined?Math.random()*P.H:y,
      vx:(Math.random()-0.5)*90, vy:(Math.random()-0.5)*90, r:r,
      rot:Math.random()*6, vr:(Math.random()-0.5)*2,
      pts:r>60?20:(r>35?50:100)
    });
  },
  wrap:function(P,o){
    if(o.x<-30)o.x=P.W+30; if(o.x>P.W+30)o.x=-30;
    if(o.y<-30)o.y=P.H+30; if(o.y>P.H+30)o.y=-30;
  },
  update:function(P,dt){
    if(this.over){ if(P.pressed.start||P.pressed.a) this.reset(P); return; }
    var k=P.keys, s=this.ship;
    if(k.left) s.a-=4.4*dt;
    if(k.right) s.a+=4.4*dt;
    if(k.up){ s.vx+=Math.cos(s.a)*260*dt; s.vy+=Math.sin(s.a)*260*dt; if(Math.random()<0.4)P.beep(120,.03,'sine'); }
    s.vx*=0.995; s.vy*=0.995;
    s.x+=s.vx*dt; s.y+=s.vy*dt; this.wrap(P,s);
    if(this.inv>0) this.inv-=dt;
    if(P.pressed.a||P.pressed.start){
      if(this.shots.length<6){
        this.shots.push({x:s.x+Math.cos(s.a)*14,y:s.y+Math.sin(s.a)*14,vx:Math.cos(s.a)*420+s.vx,vy:Math.sin(s.a)*420+s.vy,life:1.1});
        P.beep(980,.05);
      }
    }
    for(var i=this.shots.length-1;i>=0;i--){
      var sh=this.shots[i]; sh.x+=sh.vx*dt; sh.y+=sh.vy*dt; sh.life-=dt;
      this.wrap(P,sh);
      if(sh.life<=0){ this.shots.splice(i,1); continue; }
      for(var j=this.rocks.length-1;j>=0;j--){
        var r=this.rocks[j];
        if(Math.hypot(sh.x-r.x,sh.y-r.y)<r.r){
          this.shots.splice(i,1); this.score+=r.pts; P.beep(200,.08,'sawtooth');
          if(r.r>35){ this.spawnRock(P,r.r/2.2,r.x,r.y); this.spawnRock(P,r.r/2.2,r.x,r.y); }
          this.rocks.splice(j,1); break;
        }
      }
    }
    this.rocks.forEach(function(r){ r.x+=r.vx*dt; r.y+=r.vy*dt; r.rot+=r.vr*dt; },this);
    var self=this;
    this.rocks.forEach(function(r){ self.wrap(P,r); });
    if(this.inv<=0){
      for(var k2=0;k2<this.rocks.length;k2++){
        var r2=this.rocks[k2];
        if(Math.hypot(s.x-r2.x,s.y-r2.y)<r2.r+10){
          this.lives--; P.beep(120,.35,'sawtooth');
          if(this.lives<=0){ this.over=true; }
          else { s.x=P.W/2; s.y=P.H/2; s.vx=0; s.vy=0; this.inv=2; }
          break;
        }
      }
    }
    if(!this.rocks.length){
      this.score+=500; P.beep(880,.25);
      for(var n=0;n<6;n++) this.spawnRock(P,80);
    }
  },
  draw:function(P,ctx){
    ctx.fillStyle='#0d1526'; ctx.fillRect(0,0,P.W,P.H);
    ctx.strokeStyle='#9fb3d8'; ctx.lineWidth=2;
    this.rocks.forEach(function(r){
      ctx.beginPath();
      for(var i=0;i<8;i++){
        var a=r.rot+i*Math.PI/4, rr=r.r*(0.8+0.2*Math.sin(i*3+r.rot));
        var x=r.x+Math.cos(a)*rr, y=r.y+Math.sin(a)*rr;
        if(i===0)ctx.moveTo(x,y); else ctx.lineTo(x,y);
      }
      ctx.closePath(); ctx.stroke();
    });
    var s=this.ship;
    ctx.strokeStyle=this.inv>0?'#ffb020':'#00e5a0';
    ctx.beginPath();
    ctx.moveTo(s.x+Math.cos(s.a)*16,s.y+Math.sin(s.a)*16);
    ctx.lineTo(s.x+Math.cos(s.a+2.5)*12,s.y+Math.sin(s.a+2.5)*12);
    ctx.lineTo(s.x+Math.cos(s.a-2.5)*12,s.y+Math.sin(s.a-2.5)*12);
    ctx.closePath(); ctx.stroke();
    ctx.fillStyle='#ffd43b';
    this.shots.forEach(function(sh){ ctx.fillRect(sh.x-1.5,sh.y-1.5,3,3); });
    ctx.lineWidth=1;
    P.text('SCORE '+this.score+'   SHIP '+(this.lives>0?'▲'.repeat(this.lives):'—'), P.W/2, 20, 15, '#9fb3d8');
    if(this.over) P.text('GAME OVER — press START to retry', P.W/2, P.H/2, 16, '#ff6b6b');
  }
});
