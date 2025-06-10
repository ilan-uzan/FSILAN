// Part I: setTimeout alert after 2 seconds
setTimeout(function() {
  alert('Hello World');
}, 2000);

// Part II: setTimeout to add a paragraph after 2 seconds
setTimeout(function() {
  const container = document.getElementById('container');
  const p = document.createElement('p');
  p.textContent = 'Hello World';
  container.appendChild(p);
}, 2000);

// Part III: setInterval to add a paragraph every 2 seconds
let intervalId;
let paraCount = 0;
function addParagraph() {
  const container = document.getElementById('container');
  const p = document.createElement('p');
  p.textContent = 'Hello World';
  container.appendChild(p);
  paraCount++;
  if (paraCount >= 5) {
    clearInterval(intervalId);
  }
}
intervalId = setInterval(addParagraph, 2000);

document.getElementById('clear').addEventListener('click', function() {
  clearInterval(intervalId);
}); 