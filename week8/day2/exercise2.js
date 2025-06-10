// 1. Retrieve the form and console.log it.
const form = document.querySelector('form');
console.log(form);

// 2. Retrieve inputs by id and console.log them.
const fnameInput = document.getElementById('fname');
const lnameInput = document.getElementById('lname');
console.log(fnameInput, lnameInput);

// 3. Retrieve inputs by name and console.log them.
const inputsByName = document.querySelectorAll('input[name]');
inputsByName.forEach(input => console.log(input));

// 4. Submit event
form.addEventListener('submit', function(event) {
  event.preventDefault(); // Prevents page reload
  const fname = fnameInput.value.trim();
  const lname = lnameInput.value.trim();
  if (!fname || !lname) return; // Don't add empty

  const ul = document.querySelector('.usersAnswer');
  ul.innerHTML = ''; // Clear previous
  [fname, lname].forEach(val => {
    const li = document.createElement('li');
    li.textContent = val;
    ul.appendChild(li);
  });
}); 