import { scoreboard } from "../componentes/Scoreboard.js";


export class Game extends Phaser.Scene {
    constructor() {
        super({ key: 'game' });
    }
 
    init(){
        this.scoreboard = new scoreboard(this);
    }
 
 
    preload() {
        this.load.image('background','images/background.png');
        this.load.image('platform','images/platform.png');
        this.load.image('ball','images/ball.png');
    }
 
    create() {
        this.physics.world.setBoundsCollision(true, true, true, false);



        //plataforma
        this.platform = this.physics.add.image(400,460,'platform').setImmovable();
        this.platform.body.allowGravity = false;

        //llamada al metodo scoreboard
        this.scoreboard.create();

        //bola
        //colision con mundo
        this.ball = this.physics.add.image(385, 430, 'ball');
        this.ball.setData('glue', true);
        this.ball.setCollideWorldBounds(true);
        //collider
        this.physics.add.collider(this.ball, this.platform, this.platformImpact, null, this);

        //rebote bola con plataforma
        //rebote
        this.ball.setBounce(1);

        this.cursors = this.input.keyboard.createCursorKeys();
       
    }

    update(){
        if (this.cursors.left.isDown){
            this.platform.setVelocityX(-500);
            if(this.ball.getData('glue')){
                this.ball.setVelocityX(-500);
            }
            
        }
        else if(this.cursors.right.isDown){
            this.platform.setVelocityX(500);
            if(this.ball.getData('glue')){
                this.ball.setVelocityX(500);
            }
            
        }
        else{
            this.platform.setVelocity(0);
            if(this.ball.getData('glue')){
                this.ball.setVelocity(0);
            }
            
        }

        if(this.cursors.up.isDown){
            this.ball.setVelocity(-75, -300);
            this.ball.setData('glue', false);
        }

        if(this.ball.y > 500){
            console.log("fin de la partida");
            this.gameoverImage.visible = true;
            this.scene.pause();
        }
    }

    platformImpact(ball, platform){
        this.scoreboard.incrementPoints(1);
        let relativeImpact = ball.x - platform.x;
        if(relativeImpact <0.1 && relativeImpact >-0.1){
            ball.setVelocityX(Phaser.Math.Between(-10,10))
        }else{
            ball.setVelocityX(10 * relativeImpact);
        }
    }

    
}