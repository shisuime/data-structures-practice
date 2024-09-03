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
