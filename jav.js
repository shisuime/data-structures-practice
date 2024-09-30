//hoisting

// func();
// console.log(x);
// console.log(func);

// let x = 7;

// function func() {
//   console.log("n");
// }

//scope chain

// function func() {
//   function c() {
//     console.log(b);
//   }
//   c();
// }
// const b = 7;
// func();

//temporal dead zone
// const a;
// a = 6;

// console.log(a);

//  block scope and shadowing
// var c = 121;
// {
//   var a = 10;
//   let b = 34;
//   const c = 12;
//   console.log(a);
//     console.log(b);
//   console.log(c);
// }
// console.log(a);
// console.log(b);
// console.log(c);

//closures

// function func() {
//   function y() {
//     function z() {
//       console.log(a);
//     }
//     return z;
//   }
//   let a = 7;
//   return y;
// }
// let a = 700;
// const res = func();
// const res1 = res();
// res1();

//settiemout

// function x() {
//   for (var i = 1; i < 10; i++) {
//     setTimeout(() => {
//       console.log(i);
//     }, 1 * 1000);
//   }
// }
// x();

// function Func() {
//   var count = 0;
//   this.incerement = function () {
//     count++;
//   };
// }

// var obj = new Func();
// obj.incerement();

// var b = () => {
//   console.log("hi");
// };

// callback function
// function func() {
//   setTimeout(() => {
//     console.log("timout ran");
//   }, 3000);
// }
// function x() {
//   console.log("2nd func");
// }

// func();
// x();

//;blocking the meain thread
// function block(miliseconds) {
//   const start = Date.now();
//   while (Date.now() - start < miliseconds) {}
//   console.log("blocked");
// }
// block(5000);
// function block(miliseconds) {
//   const start = new Date().getTime();
//   while (new Date().getTime() - start < miliseconds) {}
//   console.log(start);
// }
// block(5000);

//reduce()
// const arr = [1, 7, 3, 4, 5, 6];
// console.log(
//   arr.reduce((acc, current) => {
//     acc = acc + current;
//     return acc;
//   })
// );

// function findmax(arr) {
//   let max = 0;
//   for (let i = 0; i < arr.length; i++) {
//     if (arr[i] > max) {
//       max = arr[i];
//     }
//   }
//   return max;
// }

// console.log(
//   arr.reduce((acc, current) => {
//     if (current > acc) {
//       acc = current;
//     }
//     return acc;
//   })
// );

// const users = [
//   {
//     firstname: "a",
//     age: 26,
//   },
//   {
//     firstname: "b",
//     age: 261,
//   },
//   {
//     firstname: "c",
//     age: 26,
//   },
//   {
//     firstname: "agf",
//     age: 263,
//   },
// ];

// function cal(users) {
//   return users.reduce((acc, current) => {
//     if (current.age < 30) {
//       acc.push(current.firstname);
//     }
//     return acc;
//   }, []);
// }

// console.log(cal(users));

//promises
// const api = "https://jsonplaceholder.typicode.com/posts";
// const user = fetch(api);
// console.log(user.json());

// async function getData() {
//   try {
//     const response = await fetch(api);
//     const data = await response.json();
//     console.log(typeof data);
//   } catch (error) {
//     console.log(error);
//   }
// }

// getData();

// async
// async function nawme() {
//   return "somethign";
// }

// const data = nawme();
// data.then((res) => console.log(res));

// const p = new Promise((res, rej) => {
//   res("done");
// });

// async function nameis() {
//   const data = await p;
//   return data;
// }

// const data = nameis();
// data.then((data) => console.log(data));

//array functions
// const arr = [1, 2, [2, 3], 4];
// console.log(arr.flat());

// string functions
// const str = "hello word";
// console.log(typeof str);
// console.log(str[2]);

//object functions
// const obj = { name: "alice", age: 25 };
// console.log(Object.entries(obj));

// rest and spread
// const arr = [1, 2, 3, 4, 5];
// function func(first, second, ...arr) {
//   console.log(arr);
//   console.log(first);
//   console.log(second);
// }
// func(...arr);
// console.log(...arr);
// const b = { ...arr };
// console.log(b);

// alternate string
// const str1 = "hello";
// const str2 = "world12345";

// let result = "";
// const min = Math.min(str1.length, str2.length);

// for (let i = 0; i < min; i++) {
//   result += str1[i] + str2[i];
// }

// result += str1.slice(min) + str2.slice(min);

// console.log(result);

//shallow
// const _ = require("lodash");
// const original = [1, 2, { a: 3 }];
// const shallow = [...original];

// shallow[2].a = 4;

// console.log(original, shallow);

// const deep = _.cloneDeep(original);
// console.log(deep);
// function pyramid(height) {
//   for (let i = 1; i <= height; i++) {
//     let spaces = " ".repeat(height - i);
//     let start = "*".repeat(i * 2 - 1);
//     console.log(spaces + start);
//   }
// }

// pyramid(5);

// function blockMainThread() {
//   const start = Date.now();
//   let end = start;
//   while (end < start + 5000) {
//     end = Date.now();
//   }
//   console.log("done");
// }
// console.log("start");
// blockMainThread();
// console.log("end");

// reverse an array

//
