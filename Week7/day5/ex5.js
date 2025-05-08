const containerDiv = document.getElementById('container');
console.log(containerDiv);
document.querySelectorAll('.list')[0].children[1].textContent = 'Richard';
document.querySelectorAll('.list')[1].children[1].remove();
const myName = 'Ilan';
document.querySelectorAll('.list').forEach(ul => {
  ul.children[0].textContent = myName;
});
document.querySelectorAll('.list').forEach(ul => ul.classList.add('student_list'));
document.querySelectorAll('.list')[0].classList.add('university', 'attendance');
containerDiv.style.background = 'lightblue';
containerDiv.style.padding = '10px';
document.querySelectorAll('.list')[1].querySelectorAll('li').forEach(li => {
  if (li.textContent === 'Dan') li.style.display = 'none';
});
document.querySelectorAll('.list')[0].querySelectorAll('li').forEach(li => {
  if (li.textContent === 'Richard') li.style.border = '2px solid black';
});
document.body.style.fontSize = '18px';
if (containerDiv.style.background === 'lightblue') {
  const users = Array.from(document.querySelectorAll('.list li')).map(li => li.textContent);
  alert(`Hello ${users[0]} and ${users[1]}`);
}