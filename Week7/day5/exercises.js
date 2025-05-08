// 🌟 Exercise 1 : Find the numbers divisible by 23
function displayNumbersDivisible(divisor = 23) {
  let sum = 0;
  let numbers = [];
  for (let i = 0; i <= 500; i++) {
    if (i % divisor === 0) {
      numbers.push(i);
      sum += i;
    }
  }
  console.log(numbers.join(' '));
  console.log('Sum :', sum);
}
displayNumbersDivisible(); // default 23
// Bonus examples:
displayNumbersDivisible(3);
displayNumbersDivisible(45);

// 🌟 Exercise 2 : Shopping List
const stock = { 
  "banana": 6, 
  "apple": 0,
  "pear": 12,
  "orange": 32,
  "blueberry":1
};  
const prices = {    
  "banana": 4, 
  "apple": 2, 
  "pear": 1,
  "orange": 1.5,
  "blueberry":10
}; 
const shoppingList = ["banana", "orange", "apple"];
function myBill() {
  let total = 0;
  for (let item of shoppingList) {
    if (item in stock && stock[item] > 0) {
      total += prices[item];
      stock[item] -= 1; // Bonus: decrease stock
    }
  }
  return total;
}
console.log('Total bill:', myBill());

// Exercise 3 : What's in my wallet ?
function changeEnough(itemPrice, amountOfChange) {
  const values = [0.25, 0.10, 0.05, 0.01];
  let total = 0;
  for (let i = 0; i < amountOfChange.length; i++) {
    total += amountOfChange[i] * values[i];
  }
  return total >= itemPrice;
}
console.log(changeEnough(4.25, [25, 20, 5, 0])); // true
console.log(changeEnough(14.11, [2,100,0,0])); // false
console.log(changeEnough(0.75, [0,0,20,5])); // true

// 🌟 Exercise 4 : Vacations Costs
function hotelCost(nights) {
  if (typeof nights !== 'number' || isNaN(nights) || nights <= 0) return 0;
  return nights * 140;
}
function planeRideCost(destination) {
  if (typeof destination !== 'string') return 300;
  destination = destination.toLowerCase();
  if (destination === 'london') return 183;
  if (destination === 'paris') return 220;
  return 300;
}
function rentalCarCost(days) {
  if (typeof days !== 'number' || isNaN(days) || days <= 0) return 0;
  let cost = days * 40;
  if (days > 10) cost *= 0.95;
  return cost;
}
function totalVacationCost() {
  // For mobile: use prompt only here
  let nights, days, destination;
  do {
    nights = Number(prompt('How many nights in the hotel?'));
  } while (!nights || isNaN(nights) || nights <= 0);
  do {
    days = Number(prompt('How many days for car rental?'));
  } while (!days || isNaN(days) || days <= 0);
  do {
    destination = prompt('What is your destination?');
  } while (!destination || typeof destination !== 'string');
  const hotel = hotelCost(nights);
  const car = rentalCarCost(days);
  const plane = planeRideCost(destination);
  console.log(`The car cost: $${car}, the hotel cost: $${hotel}, the plane tickets cost: $${plane}.`);
  return car + hotel + plane;
}
// Uncomment to run:
// totalVacationCost(); 

