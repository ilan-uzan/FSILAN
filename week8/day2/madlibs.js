const form = document.getElementById('libform');
const storySpan = document.getElementById('story');
const shuffleBtn = document.getElementById('shuffle-button');

let lastInputs = {};
let lastStoryIndex = -1;

const storyTemplates = [
  (noun, adj, person, verb, place) => `Once upon a time, ${person} found a ${adj} ${noun} and decided to ${verb} it in ${place}.`,
  (noun, adj, person, verb, place) => `In ${place}, ${person} was known for their ${adj} ${noun} that could ${verb} like no other.`,
  (noun, adj, person, verb, place) => `Why did ${person} bring a ${adj} ${noun} to ${place}? To ${verb}, of course!`,
  (noun, adj, person, verb, place) => `Legend says that a ${adj} ${noun} can only ${verb} if ${person} is in ${place}.`,
  (noun, adj, person, verb, place) => `${person} couldn't believe their eyes when a ${adj} ${noun} started to ${verb} in ${place}.`
];

function getInputs() {
  return {
    noun: document.getElementById('noun').value.trim(),
    adjective: document.getElementById('adjective').value.trim(),
    person: document.getElementById('person').value.trim(),
    verb: document.getElementById('verb').value.trim(),
    place: document.getElementById('place').value.trim()
  };
}

function validateInputs(inputs) {
  return Object.values(inputs).every(val => val.length > 0);
}

function getRandomStoryIndex(excludeIndex = -1) {
  let idx;
  do {
    idx = Math.floor(Math.random() * storyTemplates.length);
  } while (idx === excludeIndex && storyTemplates.length > 1);
  return idx;
}

function generateStory(inputs, index = null) {
  const { noun, adjective, person, verb, place } = inputs;
  const storyIndex = index !== null ? index : getRandomStoryIndex(lastStoryIndex);
  lastStoryIndex = storyIndex;
  return storyTemplates[storyIndex](noun, adjective, person, verb, place);
}

form.addEventListener('submit', function(event) {
  event.preventDefault();
  const inputs = getInputs();
  if (!validateInputs(inputs)) {
    storySpan.textContent = 'Please fill in all fields!';
    return;
  }
  lastInputs = inputs;
  const story = generateStory(inputs);
  storySpan.textContent = story;
});

shuffleBtn.addEventListener('click', function() {
  if (!validateInputs(lastInputs)) {
    storySpan.textContent = 'Please fill in all fields and generate a story first!';
    return;
  }
  const story = generateStory(lastInputs);
  storySpan.textContent = story;
}); 