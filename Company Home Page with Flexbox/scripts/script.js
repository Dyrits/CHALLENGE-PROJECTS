const removeTransition = $event => {
  if ($event.propertyName !== "transform") { return; }
  $event.target.classList.remove("playing")
};

const playSound = $event => {
  $event.preventDefault();
  const audio = document.querySelector(`audio[data-key="${$event.keyCode}"`);
  const key = document.querySelector(`.key[data-key="${$event.keyCode}"`);
  if (!audio) { return; }
  audio.currentTime = 0; // Set the audio to the beginning
  key.classList.add("playing");
  audio.play();
}

const keys = document.querySelectorAll(".key");
window.addEventListener("keydown", playSound);
keys.forEach(key => key.addEventListener("transitionend", removeTransition));