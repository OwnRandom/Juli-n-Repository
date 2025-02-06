import { scoreboard } from "../componentes/Scoreboard.js";

export class Game extends Phaser.Scene {
    constructor() {
        super({ key: 'game' });
    }
 
    init() {
        this.scoreboard = new scoreboard(this);
    }
 
    preload() {
        this.load.image('background', 'images/background.png');
        this.load.image('ball', 'images/ball.png');
        this.load.image('peg', 'images/peg.png');
        this.load.image('bucket', 'images/bucket.png');
    }
 
    create() {
        this.add.image(400, 300, 'background');
        this.physics.world.setBoundsCollision(true, true, true, false);

        this.scoreboard.create();

        this.pegs = this.physics.add.staticGroup();
        this.createPegs();

        this.buckets = this.physics.add.staticGroup();
        this.createBuckets();

        this.ball = this.physics.add.image(400, 50, 'ball');
        this.ball.setCollideWorldBounds(true);
        this.ball.setBounce(0.75);

        this.physics.add.collider(this.ball, this.pegs);
        this.physics.add.collider(this.ball, this.buckets, this.ballLands, null, this);
    }

    createPegs() {
        let rows = 6;
        let spacingX = 70;
        let spacingY = 80;
        for (let y = 0; y < rows; y++) {
            for (let x = 0; x <= y; x++) {
                let posX = 400 + (x - y / 2) * spacingX;
                let posY = 100 + y * spacingY;
                this.pegs.create(posX, posY, 'peg');
            }
        }
    }

    createBuckets() {
        let numBuckets = 7;
        let bucketWidth = 100;
        for (let i = 0; i < numBuckets; i++) {
            let x = 100 + i * bucketWidth;
            let bucket = this.buckets.create(x, 500, 'bucket');
            bucket.setData('points', (i + 1) * 10);
        }
    }

    ballLands(ball, bucket) {
        this.scoreboard.incrementPoints(bucket.getData('points'));
        ball.destroy();
        this.time.delayedCall(1000, () => this.createNewBall(), [], this);
    }

    createNewBall() {
        this.ball = this.physics.add.image(400, 50, 'ball');
        this.ball.setCollideWorldBounds(true);
        this.ball.setBounce(0.75);
        this.physics.add.collider(this.ball, this.pegs);
        this.physics.add.collider(this.ball, this.buckets, this.ballLands, null, this);
    }
}
