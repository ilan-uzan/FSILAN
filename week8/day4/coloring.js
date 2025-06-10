const grid = document.getElementById('grid');
const colorPicker = document.getElementById('colorPicker');
const clearBtn = document.getElementById('clearBtn');
const eraserBtn = document.getElementById('eraserBtn');
const rainbowBtn = document.getElementById('rainbowBtn');
const gridBtn = document.getElementById('gridBtn');
const penSizeSelect = document.getElementById('penSize');

let mouseDown = false;
let currentColor = colorPicker.value;
let eraserMode = false;
let rainbowMode = false;
let showGridLines = true;
let penSize = 1;

// Responsive grid size
const isMobile = window.innerWidth <= 600;
const gridSize = isMobile ? 12 : 16;

// Create grid
function createGrid(size) {
  grid.innerHTML = '';
  grid.style.gridTemplateColumns = `repeat(${size}, 1fr)`;
  grid.style.gridTemplateRows = `repeat(${size}, 1fr)`;
  for (let i = 0; i < size * size; i++) {
    const square = document.createElement('div');
    square.className = 'square';
    square.dataset.index = i;
    square.addEventListener('pointerdown', colorSquare);
    square.addEventListener('pointerover', colorSquareOnDrag);
    grid.appendChild(square);
  }
}

function getColor() {
  if (eraserMode) return '#fff';
  if (rainbowMode) return `hsl(${Math.floor(Math.random()*360)}, 90%, 60%)`;
  return currentColor;
}

function colorSquare(e) {
  e.preventDefault();
  paintSquares(this);
  mouseDown = true;
}
function colorSquareOnDrag(e) {
  if (mouseDown) {
    paintSquares(this);
  }
}
function paintSquares(square) {
  const idx = parseInt(square.dataset.index);
  const row = Math.floor(idx / gridSize);
  const col = idx % gridSize;
  for (let dr = 0; dr < penSize; dr++) {
    for (let dc = 0; dc < penSize; dc++) {
      const r = row + dr;
      const c = col + dc;
      if (r < gridSize && c < gridSize) {
        const sq = grid.children[r * gridSize + c];
        if (sq) sq.style.background = getColor();
      }
    }
  }
}

document.body.addEventListener('pointerdown', () => mouseDown = true);
document.body.addEventListener('pointerup', () => mouseDown = false);

colorPicker.addEventListener('input', e => {
  currentColor = e.target.value;
  eraserMode = false;
  eraserBtn.classList.remove('active');
});

clearBtn.addEventListener('click', () => {
  document.querySelectorAll('.square').forEach(sq => sq.style.background = '#fff');
});

eraserBtn.addEventListener('click', () => {
  eraserMode = !eraserMode;
  eraserBtn.classList.toggle('active', eraserMode);
  if (eraserMode) {
    rainbowMode = false;
    rainbowBtn.classList.remove('active');
  }
});

rainbowBtn.addEventListener('click', () => {
  rainbowMode = !rainbowMode;
  rainbowBtn.classList.toggle('active', rainbowMode);
  if (rainbowMode) {
    eraserMode = false;
    eraserBtn.classList.remove('active');
  }
});

gridBtn.addEventListener('click', () => {
  showGridLines = !showGridLines;
  grid.classList.toggle('no-lines', !showGridLines);
  gridBtn.classList.toggle('active', !showGridLines);
});

penSizeSelect.addEventListener('change', e => {
  penSize = parseInt(e.target.value);
});

createGrid(gridSize); 