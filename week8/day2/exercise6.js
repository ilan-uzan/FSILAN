function myMove() {
  const elem = document.getElementById('animate');
  const container = document.getElementById('container');
  let pos = 0;
  const maxPos = container.offsetWidth - elem.offsetWidth;
  clearInterval(elem._intervalId); // Prevent multiple intervals
  elem.style.left = '0px';
  elem._intervalId = setInterval(frame, 1);
  function frame() {
    if (pos >= maxPos) {
      clearInterval(elem._intervalId);
    } else {
      pos++;
      elem.style.left = pos + 'px';
    }
  }
} 