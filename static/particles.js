let canvas;
let context;
let fpsInterval = 1000/30;
let now;
let then = Date.now();

let x=250;
let y=150;
let size=10;
let xChange=randint(-10,10);
let yChange=randint(-10,10);

document.addEventListener('DOMContentLoaded', init, false);

function init() {
    canvas=document.querySelector('canvas');
    context=canvas.getContext('2d');

    draw();
    console.log("A");
}

function draw() {
    window.requestAnimationFrame(draw);
    console.log("B");
    let now= Date.now();
    let elapsed=now-then;
    if(elapsed<= fpsInterval) {
        return;
    }
    then=now-(elapsed%fpsInterval);

    context.clearRect(0,0, canvas.width, canvas.height);
    context.fillStyle='yellow';
    context.fillRect(x,y,size,size);
    x=x+xChange;
    y=y+yChange;
}

function randint(min,max){
    return Math.round(Math.random() * (max-min))+min;
}