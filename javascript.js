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

const arr = [
  [1, 2],
  [3, 4],
  [5, 6],
];
const res = [];
const flatIt = (array, res) => {
  for (let i = 0; i < array.length; i++) {
    if (Array.isArray(array[i])) {
      flatIt(array[i], res);
    } else {
      res.push(array[i]);
    }
  }
  return res;
};
console.log(flatIt(arr, res));
