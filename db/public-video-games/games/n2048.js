/* 2048 — sliding tile puzzle. Openly licensed original implementation (MIT) for the Public Video Games Database. */
PVG.register('2048', {
  title:'2048', W:400, H:560,
  controls:{ swipe:true, dpad:true, buttons:[] },
  help:'Slide tiles with arrows, numpad 2468, swipe, or the pad. Matching tiles merge. Reach 2048!',
  init:function(P){ this.reset(P); },
  reset:function(P){
    this.n=4; this.cs=84; this.gap=8;
    this.ox=(P.W-(this.n*this.cs+(this.n-1)*this.gap))/2; this.oy=110;
    this.g=[]; for(var r=0;r<this.n;r++){this.g.push([0,0,0,0]);}
    this.score=0; this.best=this.best||0; this.over=false; this.won=false;
    this.spawn(); this.spawn();
  },
  empty:function(){
    var e=[];
    for(var r=0;r<this.n;r++) for(var c=0;c<this.n;c++) if(!this.g[r][c]) e.push([r,c]);
    return e;
  },
  spawn:function(){
    var e=this.empty(); if(!e.length) return;
    var p=e[(Math.random()*e.length)|0];
    this.g[p[0]][p[1]]=Math.random()<0.9?2:4;
  },
  slide:function(row){
    var t=row.filter(function(v){return v;});
    for(var i=0;i<t.length-1;i++){
      if(t[i]===t[i+1]){ t[i]*=2; this.score+=t[i]; t.splice(i+1,1); }
    }
    while(t.length<4) t.push(0);
    return t;
  },
  move:function(P,dir){
    if(this.over) return;
    var before=JSON.stringify(this.g), after=[];
    for(var r=0;r<4;r++){
      var row;
      if(dir==='left') row=this.slide(this.g[r].slice());
      else if(dir==='right') row=this.slide(this.g[r].slice().reverse()).reverse();
      else{
        var col=[]; for(var r2=0;r2<4;r2++) col.push(this.g[r2][r]);
        if(dir==='up') col=this.slide(col); else col=this.slide(col.reverse()).reverse();
        row=col;
      }
      after.push(row);
    }
    if(dir==='up'||dir==='down'){
      var t=[];
      for(var c=0;c<4;c++){ t.push([]); for(var r3=0;r3<4;r3++) t[c].push(after[r3][c]); }
      after=t;
    }
    if(JSON.stringify(after)!==before){
      this.g=after; this.spawn(); P.beep(440,.05);
      this.best=Math.max(this.best,this.score);
      for(var r4=0;r4<4;r4++) for(var c4=0;c4<4;c4++) if(this.g[r4][c4]===2048) this.won=true;
      if(!this.empty().length&&!this.canMove()){ this.over=true; P.beep(150,.4,'sawtooth'); }
    }
  },
  canMove:function(){
    for(var r=0;r<4;r++) for(var c=0;c<4;c++){
      if(!this.g[r][c]) return true;
      if(c<3&&this.g[r][c]===this.g[r][c+1]) return true;
      if(r<3&&this.g[r][c]===this.g[r+1][c]) return true;
    }
    return false;
  },
  update:function(P,dt){
    if(P.pressed.start||P.pressed.a){ if(this.over){ this.reset(P); return; } }
    var d=null;
    if(P.pressed.left)d='left'; else if(P.pressed.right)d='right';
    else if(P.pressed.up)d='up'; else if(P.pressed.down)d='down';
    if(!d&&P.swipeQ.length) d=P.swipeQ.shift();
    P.clearTaps();
    if(d) this.move(P,d);
  },
  draw:function(P,ctx){
    ctx.fillStyle='#0d1526'; ctx.fillRect(0,0,P.W,P.H);
    var cols={2:'#3a4a6b',4:'#4a5a7d',8:'#ff8b3e',16:'#ff7a2e',32:'#e5484d',64:'#d63a3f',128:'#ffd43b',256:'#f0c020',512:'#e8b010',1024:'#00e5a0',2048:'#00c98a'};
    for(var r=0;r<4;r++) for(var c=0;c<4;c++){
      var v=this.g[r][c];
      var x=this.ox+c*(this.cs+this.gap), y=this.oy+r*(this.cs+this.gap);
      ctx.fillStyle=cols[v]||(v?'#9b5de5':'#132a55');
      ctx.fillRect(x,y,this.cs,this.cs);
      if(v){
        var s=v<100?30:(v<1000?26:21);
        P.text(v,x+this.cs/2,y+this.cs/2+1,s,'#fff');
      }
    }
    P.text('SCORE '+this.score+'   BEST '+this.best, P.W/2, 30, 16, '#9fb3d8');
    P.text('Arrows / numpad / swipe to slide', P.W/2, 66, 13, '#9fb3d8');
    if(this.won&&!this.over) P.text('2048! Keep going…', P.W/2, 90, 14, '#00e5a0');
    if(this.over) P.text('NO MOVES — START to retry', P.W/2, P.H-24, 15, '#ff6b6b');
  }
});
