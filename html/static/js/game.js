Game = {
    gameGrid: {
        width: 9,
        height: 13,
        tile: {
            width: 32,
            height:32
        }
    },
    pointCounter: 0,
    getWidth: function(){
        return this.gameGrid.width * this.gameGrid.tile.width;
    },
    getHeight: function(){
        return this.gameGrid.height * this.gameGrid.tile.height
    },
    /**
     * Initialize running game
     */
    init: function(){
        Crafty.init(this.getWidth(), this.getHeight());
        Crafty.background('#FFCA80');
        Crafty.scene('Loading');
    }
}

$textCss = {
    'font-size': '24px',
    'font-family': 'Arial',
    'color': 'grey',
    'text-align': 'center',
    'width': '268px'
}