Crafty.scene('Game', function(){
    var pointCounter = 0;
    for(var y=0; y < Game.gameGrid.height; y++){
        Crafty.e('LeftWall').at(0, y);
        Crafty.e('RightWall').at(Game.gameGrid.width - 1, y);
    }
    for(var x=0; x < Game.gameGrid.width - 1; x++){
        Crafty.e('Destroyer').at(x, Game.gameGrid.height)
    }
    Crafty.e('BuildNewFlagReceiver').at(0, 1);
    Crafty.e('AddPointCell').at(
        Game.gameGrid.width - 1,
        Game.gameGrid.height
    );

    Crafty.e('Hero').at(Math.floor(Game.gameGrid.width/2), Game.gameGrid.height - 2);

    var generateBlockRow = function(){
        console.log('Generate Block');
        for(var i=1; i<Game.gameGrid.width-1; i++){
            if(Math.random() > 0.85){
                Crafty.e('Block').at(i, -1);
            }
        }
        Crafty.e('BuildNewFlag').at(0, -1);
        Crafty.e('PointGrid').at(Game.gameGrid.width - 1, -1);
    };
    generateBlockRow();

    /*start movement of blocks*/
    var speed = 2;
    Crafty.trigger('SetSpeed', speed);

    this.canBuildNewHandler = this.bind('CanBuildNew', function(){
        generateBlockRow();
        Crafty.trigger('SetSpeed', speed);
    });
    this.addOnePointHandler = this.bind('AddOnePoint', function(){
        pointCounter++;
        if(pointCounter % 20 == 0){
            speed++;
        }
    });
    this.heroDeadHandler = this.bind('HeroDead', function(){
        Game.pointCounter = pointCounter
        Crafty.scene('Defeat');
        Crafty('Grid').each(function(item){
            item.destroy();
        });
        this.unbind('CanBuildNew', this.canBuildNewHandler);
        this.unbind('AddOnePoint',this.addOnePointHandler);
        this.unbind('HeroDead', this.heroDeadHandler);
    });
}, function(){
});


Crafty.scene('InitGame', function(){
   Crafty.e('2D, DOM, Text')
       .text("Connect your phone and press start button")
       .attr({x:10, y:10})
       .css($textCss);

        this.startGame = this.bind('StartButtonPressed', function(){
            console.log('Start Game');
            Crafty.scene('Game');
        });
}, function(){
    this.unbind('StartButtonPressed', this.startGame);
});


Crafty.scene('Defeat', function(){
    Crafty.e('2D, DOM, Text')
        .text("Score: " + Game.pointCounter)
        .attr({x:10, y:10})
        .css($textCss);

    this.startGame = this.bind('StartButtonPressed', function(){
        console.log('Start Game');
        Crafty.scene('Game');
    });
}, function(){
    this.unbind('StartButtonPressed', this.startGame);
});


Crafty.scene('Loading', function(){
    Crafty.e('2D, DOM, Text')
        .text('Loading. please wait...')
        .attr({x:10, height: Game.getHeight()/2 - 24})
        .css($textCss);

    Crafty.load([
        'static/img/tile1.png'
    ], function(){
        Crafty.sprite(32, 'static/img/tile1.png', {
            spriteBox: [0, 0],
            spriteRightWall: [1, 0],
            spriteLeftWall: [2, 0]
        });
        Crafty.sprite(32, 'static/img/tile1.png', {
            spriteHero: [0, 1]
        });
    });

    Crafty.scene('InitGame');
});

