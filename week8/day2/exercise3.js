// Declare global variable
let allBoldItems;

// Collect all <strong> in the paragraph
function getBoldItems() {
  allBoldItems = document.querySelectorAll('#sentence strong');
}
getBoldItems();

// Highlight all bold text to blue
function highlight() {
  allBoldItems.forEach(item => item.style.color = 'blue');
}

// Return all bold text to black
function returnItemsToDefault() {
  allBoldItems.forEach(item => item.style.color = 'black');
}

// Add event listeners
const para = document.getElementById('sentence');
para.addEventListener('mouseover', highlight);
para.addEventListener('mouseout', returnItemsToDefault); 