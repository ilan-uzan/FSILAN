// 🌟 Exercise 1 : List of people
let people = ["Greg", "Mary", "Devon", "James"];
people.shift();
people[people.indexOf("James")] = "Jason";
people.push("Ilan");
console.log("Mary's index:", people.indexOf("Mary"));
const peopleCopy = people.slice(1, 3); 
console.log("Copy without Mary and Ilan:", peopleCopy);
console.log("Index of Foo:", people.indexOf("Foo")); 
const last = people[people.length - 1];
console.log("Last element:", last);

// Part II - Loops
for (let person of people) {
  console.log(person);
}
for (let person of people) {
  console.log(person);
  if (person === "Devon") break;
}

// 🌟 Exercise 2 : Your favorite colors
const colors = ["blue", "red", "green", "purple", "yellow"];
for (let i = 0; i < colors.length; i++) {
  console.log(`My #${i + 1} choice is ${colors[i]}`);
}
const suffixes = ["st", "nd", "rd", "th", "th"];
for (let i = 0; i < colors.length; i++) {
  let suffix = suffixes[i] || "th";
  console.log(`My ${i + 1}${suffix} choice is ${colors[i]}`);
}

// 🌟 Exercise 3 : Repeat the question
let number;
do {
  number = prompt("Enter a number (10 or greater to stop):");
  number = Number(number);
} while (number < 10);

// 🌟 Exercise 4 : Building Management
const building = {
  numberOfFloors: 4,
  numberOfAptByFloor: {
    firstFloor: 3,
    secondFloor: 4,
    thirdFloor: 9,
    fourthFloor: 2,
  },
  nameOfTenants: ["Sarah", "Dan", "David"],
  numberOfRoomsAndRent:  {
    sarah: [3, 990],
    dan:  [4, 1000],
    david: [1, 500],
  },
};
console.log("Number of floors:", building.numberOfFloors);
console.log("Apartments on 1st and 3rd floors:", building.numberOfAptByFloor.firstFloor, building.numberOfAptByFloor.thirdFloor);
console.log("Second tenant and rooms:", building.nameOfTenants[1], building.numberOfRoomsAndRent.dan[0]);
const sarahRent = building.numberOfRoomsAndRent.sarah[1];
const davidRent = building.numberOfRoomsAndRent.david[1];
const danRent = building.numberOfRoomsAndRent.dan[1];
if (sarahRent + davidRent > danRent) {
  building.numberOfRoomsAndRent.dan[1] = 1200;
  console.log("Dan's rent increased to 1200");
}

// 🌟 Exercise 5 : Family
const family = {
  father: "John",
  mother: "Jane",
  child: "Jimmy"
};
for (let key in family) {
  console.log("Key:", key);
}
for (let key in family) {
  console.log("Value:", family[key]);
}

// Exercise 6 : Rudolf
const details = {
  my: 'name',
  is: 'Rudolf',
  the: 'reindeer'
};
let sentence = '';
for (let key in details) {
  sentence += key + ' ' + details[key] + ' ';
}
console.log(sentence.trim());

// Exercise 7 : Secret Group
const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
const secretName = names.map(name => name[0]).sort().join("");
console.log("Secret society name:", secretName);
