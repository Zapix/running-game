Crafty.c('Grid', {
    init: function(){
        this.attr({
            w: Game.gameGrid.tile.width,
            h: Game.gameGrid.tile.height
        });
    },

    at: function(x, y){
        if(x === undefined && y === undefined){
            return {x: this.x / Game.gameGrid.tile.width,
                    y: this.y / Game.gameGrid.tile.height}
        }
        this.attr({x: x * Game.gameGrid.tile.width,
                   y: y * Game.gameGrid.tile.height});
        return this;
    }
});

Crafty.c('Actor', {
    init: function(){
        this.requires('2D, Canvas, Grid');
    }
})


Crafty.c('LeftWall', {
   init: function(){
       this.requires('Actor, spriteLeftWall');
   }
});


Crafty.c('RightWall', {
    init: function(){
        this.requires('Actor, spriteRightWall');
    }
});


Crafty.c('MoveGrid', {
    init: function(){
        this.requires('Actor, Collision');
        this.bind('SetSpeed', this.setSpeed);
        this.bind('StopMove', this.stopMove);
        this.onHit('Destroyer', this.destroyerMet)
        this.startMove(0);
    },

    destroyerMet: function(data){
        this.destroy();
    },

    startMove: function(speed){
        this.speed = speed;
        this.bind('EnterFrame', this.moveCell)
    },

    moveCell: function(speed){
        this.y += this.speed;
        return this;
    },

    setSpeed: function(speed){
        this.speed = speed;
    },

    stopMove: function(){
        this.speed = 0;
    }
});


Crafty.c('Block', {
    init: function(){
        this.requires('MoveGrid, spriteBox');
    }
});


Crafty.c('BuildNewFlagReceiver',{
    init: function(){
        this.requires('2D, Canvas, Grid');
    }
});


Crafty.c('BuildNewFlag', {
    init: function(){
        this.requires('MoveGrid');
        this.onHit('BuildNewFlagReceiver', this.newFlagReceived);
    },

    newFlagReceived: function(data){
        Crafty.trigger('CanBuildNew', null);
        this.destroy();
    }
});

Crafty.c('AddPointCell', {
    init: function(){
        this.requires('Actor');
    }
});


Crafty.c('PointGrid', {
    init: function(){
        this.requires('MoveGrid');
        this.onHit('AddPointCell', this.addPoint);
    },

   addPoint: function(){
       Crafty.trigger('AddOnePoint', null)
       this.destroy();
   }
});

Crafty.c('Destroyer', {
    init: function(){
        this.requires('2D, Canvas, Grid');
    }
});


Crafty.c('Hero', {
    init: function(){
        this.requires('Actor, Collision, spriteHero, SpriteAnimation');
        this.bind('LeftButtonPressed', this.stepLeft);
        this.bind('RightButtonPressed', this.stepRight);
        this.onHit('Block', this.dieHero);
        this.animate('MoveUp', 0, 1, 2);
        this.animate('MoveUp', 4, -1);
    },

    /*
      stepPointer < 0 move left
      stepPointer > 0 move right
     */
    step: function(stepPointer){
        coord = this.at();
        if(stepPointer > 0 && coord.x < Game.gameGrid.width - 2){
            coord.x++;
        }else if(stepPointer < 0 && coord.x > 1){
            coord.x--;
        }
        this.at(coord.x, coord.y);
        return this;
    },

    stepLeft: function(){
        return this.step(-1);
    },

    stepRight: function(){
        return this.step(1);
    },

    dieHero: function(){
        Crafty.trigger('HeroDead', null);
        this.destroy();
    }
});
