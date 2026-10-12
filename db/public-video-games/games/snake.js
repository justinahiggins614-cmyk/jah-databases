/* Snake — classic arcade snake. Openly licensed original (MIT) for the Public Video Games Database. */
PVG.register('snake', {
  title:'Snake', W:400, H:560,
  controls:{ dpad:true, buttons:[] },
  help:'Eat the red apples to grow. Arrows / WASD / numpad 2468, or the on-screen pad. Do not hit the walls or yourself.',
  init:function(P){ this.reset(P); },
  reset:function(P){
    this.cell=20; this.cols=P.W/this.cell; this.rows=P.H/this.cell;
    var cy=(this.rows/2)|0;
    this.snake=[{x:8,y:cy},{x:7,y:cy},{x:6,y:cy}];
    this.dir={x:1,y:0}; this.ndir={x:1,y:0};
    this.score=0; this.best=this.best||0; this.alive=true; this.acc=0;
    this.place(P);
  },
  place:function(P){
    while(true){
      var f={x:(Math.random()*this.cols)|0, y:(Math.random()*this.rows)|0};
      var ok=true;
      for(var i=0;i<this.snake.length;i++) if(this.snake[i].x===f.x&&this.snake[i].y===f.y){ok=false;break;}
      if(ok){ this.food=f; return; }
    }
  },
  update:function(P,dt){
    if(!this.alive){ if(P.pressed.start||P.pressed.a){ this.reset(P); P.beep(440,.08);} return; }
    var k=P.keys;
    if(k.left&&this.dir.x!==1) this.ndir={x:-1,y:0};
    if(k.right&&this.dir.x!==-1) this.ndir={x:1,y:0};
    if(k.up&&this.dir.y!==1) this.ndir={x:0,y:-1};
    if(k.down&&this.dir.y!==-1) this.ndir={x:0,y:1};
    this.acc+=dt;
    var step=Math.max(0.06, 0.14-this.score*0.0015);
    if(this.acc>=step){
      this.acc=0; this.dir=this.ndir;
      var h={x:this.snake[0].x+this.dir.x, y:this.snake[0].y+this.dir.y};
      if(h.x<0||h.y<0||h.x>=this.cols||h.y>=this.rows){ this.die(P); return; }
      for(var i=0;i<this.snake.length;i++) if(this.snake[i].x===h.x&&this.snake[i].y===h.y){ this.die(P); return; }
      this.snake.unshift(h);
      if(h.x===this.food.x&&h.y===this.food.y){ this.score+=10; P.beep(880,.06); this.place(P); }
      else this.snake.pop();
    }
  },
  die:function(P){ this.alive=false; this.best=Math.max(this.best,this.score); P.beep(160,.25,'sawtooth'); },
  draw:function(P,ctx){
    var c=this.cell;
    ctx.fillStyle='#0d1526'; ctx.fillRect(0,0,P.W,P.H);
    ctx.fillStyle='#e5484d';
    ctx.fillRect(this.food.x*c+3,this.food.y*c+3,c-6,c-6);
    for(var i=0;i<this.snake.length;i++){
      ctx.fillStyle=i===0?'#00e5a0':'#0fbf7f';
      ctx.fillRect(this.snake[i].x*c+1,this.snake[i].y*c+1,c-2,c-2);
    }
    P.text('SCORE '+this.score+'   BEST '+this.best, P.W/2, 14, 14, '#9fb3d8');
    if(!this.alive) P.text('GAME OVER — press ENTER / START to retry', P.W/2, P.H/2, 15, '#ffb020');
  }
});
