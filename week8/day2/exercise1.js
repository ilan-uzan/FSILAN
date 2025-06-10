// 1. Retrieve the h1 and console.log it.
const h1 = document.querySelector('h1');
console.log(h1);

// 2. Remove the last paragraph in the <article>
const article = document.querySelector('article');
article.removeChild(article.lastElementChild);

// 3. h2 background red on click
const h2 = document.querySelector('h2');
h2.addEventListener('click', function() {
  h2.style.backgroundColor = 'red';
});

// 4. Hide h3 on click
const h3 = document.querySelector('h3');
h3.addEventListener('click', function() {
  h3.style.display = 'none';
});

// 5. Button to make all paragraphs bold
document.getElementById('bold-btn').addEventListener('click', function() {
  document.querySelectorAll('article p').forEach(p => {
    p.style.fontWeight = 'bold';
  });
});

// BONUS: h1 random font size on hover
h1.addEventListener('mouseenter', function() {
  const randomSize = Math.floor(Math.random() * 101); // 0-100px
  h1.style.fontSize = randomSize + 'px';
});
h1.addEventListener('mouseleave', function() {
  h1.style.fontSize = ''; // reset
});

// BONUS: 2nd paragraph fades out on hover
const secondP = document.getElementById('second-p');
secondP.addEventListener('mouseenter', function() {
  secondP.classList.add('fade-out');
});
secondP.addEventListener('animationend', function() {
  secondP.style.display = 'none';
}); 