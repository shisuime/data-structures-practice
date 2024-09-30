let name = {
  firstname: "akshay",
  lastname: "saini",
  printFullname: function () {
    console.log(this.firstname + this.lastname);
  },
};

const printFullname = function (hometown, state) {
  console.log(this.firstname + this.lastname + " " + hometown + state);
};

let name2 = {
  firstname: "me",
  lastname: "you",
};

//function borrowing

// const bindVar = name.printFullname.bind(name2);
// bindVar();

// printFullname.call(name, "nigga", "gustav");

// call and apply difference is that it takes args in a different way

// printFullname.apply(name, ["nigga", "gustav"]);

//polyfills with bind()

let name1 = {
  firstname: "akshay",
  lastname: "saini",
};

let printName = function (hometown, state, country) {
  console.log(
    this.firstname + this.lastname + " " + hometown + state + country
  );
};

Function.prototype.myBind = function (...args) {
  let obj = this;
  params = args.slice(1);
  return function (...arg2) {
    obj.apply(args[0], [...params, ...arg2]);
  };
};
let PrintMyName = printName.bind(name1, "da", "pa", "la");
PrintMyName();
