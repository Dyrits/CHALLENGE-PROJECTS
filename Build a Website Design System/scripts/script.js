const stack = document.getElementById("stack");

function addBrick() {
  let RGB1 = Math.floor(Math.random() * 255);
  let RGB2 = Math.floor(Math.random() * 255);
  let RGB3 = Math.floor(Math.random() * 255);
  let RGB = RGB1 + "," + RGB2 + ","
    + RGB3;
  let brick = document.createElement('div');
  brick.className = 'brick';
  brick.innerHTML = "RGB " + RGB;
  brick.style.color = "rgb(" + RGB + ")";
  stack.append(brick);
  if (stack.childElementCount > 10) {stack.removeChild(stack.firstChild) }
};