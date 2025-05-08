const navBar = document.getElementById('navBar');
navBar.setAttribute('id', 'socialNetworkNavigation');
const ul = document.querySelector('#socialNetworkNavigation ul');
const newLi = document.createElement('li');
const logoutText = document.createTextNode('Logout');
newLi.appendChild(logoutText);
ul.appendChild(newLi);
console.log('First link:', ul.firstElementChild.textContent);
console.log('Last link:', ul.lastElementChild.textContent);