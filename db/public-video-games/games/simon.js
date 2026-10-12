/* Simon — memory sequence game. Openly licensed original (MIT) for the Public Video Games Database. */
PVG.register('simon', {
  title:'Simon', W:400, H:560,
  controls:{ tap:true, buttons:[] },
  help:'Watch the sequence, then repeat it. Tap the pads, click them, or press numpad 1-4 (7-4 also works).',
  init:function(P){ this.reset(P); },
  reset:function(P){
    this.seq=[]; this.pos=0; this.round=0; this.best=this.best||0;
    this.phase='idle'; this.pt=0; this.showI=0; this.lit=-1; this.lt=0;
    this.pads=[
      {x:P.W/2-105,y:180,c:'#00e5a0',f:392,k:'1'},
      {x:P.W/2+105,y:180,c:'#e5484d',f:330,k:'2'},
      {x:P.W/2-105,y:340,c:'#ffd43b',f:262,k:'3'},
      {x:P.W/2+105,y:340,c:'#2f7bff',f:196,k:'4'}
    ];
  },
  nextRound:function(P){
    this.seq.push((Math.random()*4)|0);
    this.round=this.seq.length; this.pos=0;
    this.phase='show'; this.showI=0; this.pt=0;
    this.best=Math.max(this.best,this.round-1);
  },
  press:function(P,i){
    if(this.phase!=='input') return;
    this.lit=i; this.lt=0.25; P.beep(this.pads[i].f,.18);
    if(this.seq[this.pos]===i){
      this.pos++;
      if(this.pos>=this.seq.length){ this.phase='pause'; this.pt=0; P.beep(880,.2); }
    } else {
      this.phase='dead'; P.beep(120,.5,'sawtooth');
      this.best=Math.max(this.best,this.round-1);
    }
  },
  update:function(P,dt){
    if(P.pressed.start||P.pressed.a){
      if(this.phase==='idle'||this.phase==='dead'){ this.reset(P); this.nextRound(P); return; }
    }
    var taps=P.tapQ;
    for(var i=0;i<taps.length;i++){
      for(var j=0;j<4;j++){
        var pd=this.pads[j];
        if(Math.hypot(taps[i].x-pd.x,taps[i].y-pd.y)<58){ this.press(P,j); break; }
      }
    }
    for(var k=0;k<4;k++) if(P.pressed[this.pads[k].k]) this.press(P,k);
    P.clearTaps();
    if(this.lt>0){ this.lt-=dt; if(this.lt<=0) this.lit=-1; }
    if(this.phase==='show'){
      this.pt+=dt;
      if(this.pt>0.55){
        this.pt=0;
        if(this.showI<this.seq.length){
          this.lit=this.seq[this.showI]; this.lt=0.4;
          P.beep(this.pads[this.lit].f,.3);
          this.showI++;
        } else { this.phase='input'; }
      }
    }
    if(this.phase==='pause'){
      this.pt+=dt;
      if(this.pt>0.9) this.nextRound(P);
    }
  },
  draw:function(P,ctx){
    ctx.fillStyle='#0d1526'; ctx.fillRect(0,0,P.W,P.H);
    for(var i=0;i<4;i++){
      var pd=this.pads[i];
      ctx.fillStyle=this.lit===i?'#ffffff':pd.c;
      ctx.globalAlpha=this.lit===i?1:0.55;
      ctx.beginPath(); ctx.arc(pd.x,pd.y,52,0,7); ctx.fill();
      ctx.globalAlpha=1;
      P.text(i+1, pd.x, pd.y, 26, '#070b16');
    }
    P.text('ROUND '+this.round+'   BEST '+(this.best), P.W/2, 60, 17, '#9fb3d8');
    var msg={idle:'Press START / tap to begin',show:'Watch…',input:'Your turn — repeat it',pause:'Nice!',dead:'Wrong! START to retry'}[this.phase];
    P.text(msg, P.W/2, 470, 16, '#ffb020');
  }
});
