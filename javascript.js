// class Person {
//   constructor(age, name) {
//     this.name = name;
//     this.age = age;
//   }

//   greet() {
//     console.log(this.age, this.name, this.jobtitle, "parent");
//   }
// }

// class Child extends Person {
//   constructor(age, name, jobtitle) {
//     super();
//     this.age = age;
//     this.name = name;
//     this.jobtitle = jobtitle;
//   }

//   greet() {
//     console.log(this.age, this.name, this.jobtitle, "child");
//   }
// }

// const obj = new Child(4, "shisui", "frontend developer");

// obj.greet();

// map
// const num = [1, 2, 3, 4, 5];

// const items = num.map((e) => {
//   return { value: e };
// });

// console.log(items);

//filter
// const num = [1, 2, 3, 4, 5];

// const newArray = num.filter((e) => e <= 0);

// console.log(newArray);

// Reduce
// const num = [1, 2, 3, 4, 5];

// let sum = num.reduce((acc, idx) => {
//   return acc + idx;
// });

// console.log(sum);

//forEach
// const num = [1, 2, 3, 4, 5];

// const test = num.forEach((e) => {
//   return [{ value: e }];
// });

// console.log(test);
// const a = { num: 7 };

// let c = 7;
// if (a.num == c) {
//   console.log(true);
// } else {
//   console.log(false);
// }
// function x() {
//   function y() {
//     const a = 7;
//   }
//   console.log(a);
//   y();
// }
// x();

// const func = (str1, str2) => {
//   let res = "";
//   let m;
//   for (let i = 0; i < str1.length && i < str2.length; i++) {
//     res = res + str1[i] + str2[i];
//     m = i;
//   }

//   while (m < str1.length || m < str2.length) {
//     if (m < str1.length && m !== str1.length) {
//       res = res + str1[m];
//       m++;
//     } else {
//       res = res + str2[m];
//       m++;
//     }
//   }
//   console.log(res);
// };

// func("hello 123", "world");

// const sum = (a) => (b) => console.log(a + b);

// sum(2)(4);

// const arr = [
//   [1, 2],
//   [3, 4],
//   [5, 6],
// ];
// const res = [];
// const flatIt = (array, res) => {
//   for (let i = 0; i < array.length; i++) {
//     if (Array.isArray(array[i])) {
//       flatIt(array[i], res);
//     } else {
//       res.push(array[i]);
//     }
//   }
//   return res;
// };
// console.log(flatIt(arr, res));

// const arr = [
//   [1, 2],
//   [1, 3],
//   [1, 4],
// ];

// result = [];
// function flatiIt(arr, result) {
//   for (let i = 0; i < arr.length; i++) {
//     if (Array.isArray(arr[i])) {
//       flatiIt(arr[i], result);
//     } else {
//       result.push(arr[i]);
//     }
//   }
//   return result;
// }

// console.log(flatiIt(arr, result));

// closure

// function outer() {
//   let count = 0;
//   function innerfucntion() {
//     count++;
//     console.log(count);
//   }
//   return innerfucntion;
// }

// const counter = outer();
// counter();
// counter();
// counter();

// this keyword

// const obj = {
//   name: "hi",
//   showName: function () {
//     console.log(this);
//   },
// };
// obj.showName();

// function Person(name) {
//   this.name = name;
// }

// const obj = new Person("john");
// console.log(obj.name);

// blocking main thread

// console.log("start");
// function busyWait(duration) {
//   const now = Date.now();
//   while (Date.now() - now < duration) {}
// }
// busyWait(2000);
// console.log("end");

// const arr = [1, 2, 3];

// arr[0] = 8;
// console.log(arr);
// console.log(arr.length);

// const [, , , , ,a] = [1, 2, 3, 4, 5];
// const { 4: a } = [1, 2, 3, 4, 5];

// console.log(a);

// function abc() {
//   console.log("hi");
// }

// const obj = new abc();
// console.log(obj);

// const arr = [1, 2, 3];

// function f(i) {
//   i = 5;
// }
// f(arr[2]);
// console.log(arr);

// function pyramid(n) {
//   for (let i = 1; i <= n; i++) {
//     let spaces = "";
//     let stars = "";

//     // Add spaces to center the stars
//     for (let j = 1; j <= n - i; j++) {
//       spaces += " "; // Add actual spaces here to center the stars
//     }

//     // Add stars
//     for (let k = 1; k <= 2 * i - 1; k++) {
//       stars += "*"; // Add stars to form the pyramid
//     }

//     // Combine spaces and stars, then print the line
//     console.log(spaces + stars);
//   }
// }

// pyramid(5);

// function find(arr) {
//   const seen = new Set();
//   for (let i = 0; i <= arr.length; i++) {
//     if (seen.has(arr[i])) {
//       return i;
//     }
//     seen.add(arr[i]);
//   }
//   return -1;
// }
// console.log(find([2, 5, 1, 2, 3, 5, 1, 2, 4]));

// function findNoRepeat(string) {
//   const arr = string.split();
//   const seen = new Set();
//   for (let i = 0; i <= arr.length; i++) {
//     if (!seen.has(arr[i])) {
//       return i;
//     }
//     seen.add(arr[i]);
//   }
//   return -1;
// }
// console.log(findNoRepeat("leetcode"));

// function isPallindrome(nums,target) {

// }

// console.log(isPallindrome("-121-"));

// var removeDuplicates = function (nums) {
//   if (nums.length === 0) return 0;
//   let j = 0;

//   for (let i = 0; i < nums.length; i++) {
//     if (nums[i] !== nums[j]) {
//       j++;
//       nums[j] = nums[i];
//     }
//   }
//   return nums.slice(0, j + 1);
// };

// console.log(removeDuplicates([1, 1, 2]));

// var removeElement = function (nums, val) {
//   if (nums.length < 0 || !nums.includes(val)) {
//     return [];
//   }
//   if (nums.length === 1) {
//     if (nums[0] === val) return [];
//     else {
//       return [nums[0]];
//     }
//   }

//   let slowpointer = 0;
//   for (let fastpointer = 0; fastpointer < nums.length; fastpointer++) {
//     if (nums[fastpointer] !== val) {
//       nums[slowpointer] = nums[fastpointer];
//       slowpointer++;
//     }
//   }
//   return slowpointer;
// };

// console.log(removeElement([2], 3));
