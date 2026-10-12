/* Invaders — space-invaders-style arcade shooter. Openly licensed original (MIT) for the Public Video Games Database. */
PVG.register('invaders', {
  title:'Invaders', W:480, H:560,
  controls:{ dpad:false, buttons:[{k:'left',label:'◀'},{k:'right',label:'▶'},{k:'a',label:'FIRE'}] },
  help:'Stop the invasion. ←/→ or A/D (numpad 4/6) to move, SPACE to fire. Shields block shots — yours and theirs.',
  init:function(P){ this.reset(P); },
  reset:function(P){
    this.px=P.W/2; this.score=0; this.wave=1; this.over=false; this.win=false;
    this.bullets=[]; this.ebullets=[];
    this.spawnWave(P);
    this.shields=[];
    for(var s=0;s<3;s++){
      var sx=70+s*160;
      for(var r=0;r<3;r++) for(var c=0;c<6;c++)
        this.shields.push({x:sx+c*10,y:P.H-140+r*10,w:9,h:9});
    }
    this.edx=30; this.edt=0;
  },
  spawnWave:function(P){
    this.foes=[];
    for(var r=0;r<4;r++) for(var c=0;c<8;c++)
      this.foes.push({x:60+c*44,y:70+r*36,alive:true,pts:(4-r)*10});
    this.edir=1;
  },
  update:function(P,dt){
    if(this.over||this.win){ if(P.pressed.start||P.pressed.a) this.reset(P); return; }
    var k=P.keys, sp=300;
    if(k.left) this.px-=sp*dt;
    if(k.right) this.px+=sp*dt;
    this.px=Math.max(24,Math.min(P.W-24,this.px));
    if((P.pressed.a||P.pressed.start)&&this.bullets.length<3){
      this.bullets.push({x:this.px,y:P.H-170}); P.beep(900,.05);
    }
    // foe march
    this.edt+=dt;
    var alive=this.foes.filter(function(f){return f.alive;});
    if(!alive.length){ this.wave++; this.score+=250; this.spawnWave(P); P.beep(700,.2); }
    var step=Math.max(0.12, 0.5-alive.length*0.012);
    if(this.edt>step){
      this.edt=0;
      var minx=1e9,maxx=-1e9;
      alive.forEach(function(f){minx=Math.min(minx,f.x);maxx=Math.max(maxx,f.x);});
      if((this.edir>0&&maxx>P.W-40)||(this.edir<0&&minx<40)){
        this.edir*=-1;
        alive.forEach(function(f){f.y+=18;});
      } else alive.forEach(function(f){f.x+=this.edx*this.edir;},this);
      // enemy fire
      if(alive.length&&Math.random()<0.5){
        var f=alive[(Math.random()*alive.length)|0];
        this.ebullets.push({x:f.x,y:f.y+14});
      }
      alive.forEach(function(f){ if(f.y>P.H-180){ this.over=true; P.beep(150,.4,'sawtooth'); } },this);
    }
    // bullets
    for(var i=this.bullets.length-1;i>=0;i--){
      var bl=this.bullets[i]; bl.y-=460*dt;
      if(bl.y<0){ this.bullets.splice(i,1); continue; }
      var hit=false;
      for(var j=0;j<this.foes.length;j++){
        var f=this.foes[j];
        if(f.alive&&Math.abs(bl.x-f.x)<16&&Math.abs(bl.y-f.y)<13){
          f.alive=false; this.score+=f.pts; P.beep(660,.06); hit=true; break;
        }
      }
      if(!hit) for(var s=this.shields.length-1;s>=0;s--){
        var sh=this.shields[s];
        if(bl.x>sh.x&&bl.x<sh.x+sh.w&&bl.y>sh.y&&bl.y<sh.y+sh.h){ this.shields.splice(s,1); hit=true; break; }
      }
      if(hit) this.bullets.splice(i,1);
    }
    for(var e=this.ebullets.length-1;e>=0;e--){
      var eb=this.ebullets[e]; eb.y+=300*dt;
      if(eb.y>P.H){ this.ebullets.splice(e,1); continue; }
      if(Math.abs(eb.x-this.px)<16&&eb.y>P.H-190&&eb.y<P.H-140){
        this.over=true; P.beep(150,.4,'sawtooth'); break;
      }
      for(var s2=this.shields.length-1;s2>=0;s2--){
        var sh2=this.shields[s2];
        if(eb.x>sh2.x&&eb.x<sh2.x+sh2.w&&eb.y>sh2.y&&eb.y<sh2.y+sh2.h){ this.shields.splice(s2,1); this.ebullets.splice(e,1); break; }
      }
    }
  },
  draw:function(P,ctx){
    ctx.fillStyle='#0d1526'; ctx.fillRect(0,0,P.W,P.H);
    ctx.fillStyle='#1d2c4d';
    this.shields.forEach(function(s){ ctx.fillRect(s.x,s.y,s.w,s.h); });
    this.foes.forEach(function(f){
      if(!f.alive) return;
      ctx.fillStyle='#e5484d';
      ctx.fillRect(f.x-12,f.y-9,24,16);
      ctx.fillRect(f.x-6,f.y-14,12,5);
    });
    ctx.fillStyle='#ffd43b';
    this.bullets.forEach(function(b){ ctx.fillRect(b.x-2,b.y-8,4,10); });
    ctx.fillStyle='#ff8b3e';
    this.ebullets.forEach(function(b){ ctx.fillRect(b.x-2,b.y-6,4,9); });
    // ship
    ctx.fillStyle='#00e5a0';
    ctx.beginPath();
    ctx.moveTo(this.px,P.H-190); ctx.lineTo(this.px-16,P.H-158); ctx.lineTo(this.px+16,P.H-158);
    ctx.closePath(); ctx.fill();
    ctx.fillRect(this.px-4,P.H-160,8,10);
    P.text('SCORE '+this.score+'   WAVE '+this.wave, P.W/2, 20, 15, '#9fb3d8');
    if(this.over) P.text('INVASION WON — press START to retry', P.W/2, P.H/2, 16, '#ff6b6b');
  }
});
