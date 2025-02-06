import { RestartButton } from "../componentes/RestartButton"


export class Gameover extends Phaser.Scene {
    
constructor(){
    super({ key: 'gameover'});
    this.restartButton = new this.restartButton(this);
}

preload() {
    this.load.image('gameover','images/gameover.png');
    this.restartButton.preload();
}

create() {
    this.add.image(410,250, 'background');
    this.restartButton.create();
    this.gameoverImage = this.add.image(400, 90, 'gameover');
}

}