// Debouncing
// let counter = 0;
// const getData = () => {
//   console.log("Fetching data...", counter++);
// };

// const higherFunc = (getData, delay) => {
//   let timer;
//   return function () {
//     let context = this;

//     clearTimeout(timer);
//     timer = setTimeout(() => {
//       getData.apply(context);
//     }, delay);
//   };
// };

// const betterFunction = higherFunc(getData, 300);

//throtling

// let counter = 0;
// const getData = () => {
//   console.log("Fetching data...", counter++);
// };

// const higherFunc = (getData, delay) => {
//   let flag = true;
//   return function () {
//     if (flag) {
//       getData();
//       flag = false;
//       setTimeout(() => {
//         flag = true;
//       }, delay);
//     }
//   };
// };

// const betterFunction = higherFunc(getData, 3000);

//Promises

// const cart = ["shoes", "pants", "kurtas"];
// const orderId = 0;
// const createOrder = (cart) => {
//   console.log(cart, "cart is here");
// };

// const promise = createOrder(cart);
// promise.then(
//   (res) =>
//     function (orderId) {
//       console.log(res, "orderID");
//     }
// );

// const images = fetch("https://api.thecatapi.com/v1/images/search?limit=10");
// images.then(function (data) {
//   console.log(data.json());
// });

// const cart = ["shoes", "pants", "kurtas"];

// const promise = createOrder(cart);
// promise
//   .then(function (orderId) {
//     console.log(orderId);
//     // proceedToPayment(orderId);
//     return orderId;
//   })

//   .then(function (orderId) {
//     return proceedToPayment(orderId);
//   })
//   .then(function (info) {
//     console.log(info);
//   })
//   .catch(function (error) {
//     console.log(error.message);
//   });

// function createOrder(cart) {
//   const pr = new Promise(function (resolve, reject) {
//     if (!validateCart(cart)) {
//       reject(new Error("cart is not valid"));
//     }

//     const orderId = "12314";
//     if (orderId) {
//       setTimeout(function () {
//         resolve(orderId);
//       }, 5000);
//     }
//   });
//   return pr;
// }
// function validateCart() {
//   return false;
// }
// function proceedToPayment(orderId) {
//   return new Promise(function (resolve, reject) {
//     resolve("payment successful");
//   });
// }

//    promise apis

const p1 = new Promise((resolve, reject) => {
  setTimeout(() => {
    reject("p1 fail");
  }, 3000);
});

const p2 = new Promise((resolve, reject) => {
  // setTimeout(() => {
  //   resolve("p2 success");
  // }, 1000);
  setTimeout(() => {
    reject("p2 fail");
  }, 5000);
});

const p3 = new Promise((resolve, reject) => {
  setTimeout(() => {
    reject("p3 fail");
  }, 2000);
});

//promise.all()

// Promise.all([p1, p2, p3])
//   .then((res) => {
//     console.log(res, "result");
//   })
//   .catch((err) => console.error(err));

//promise.allsettled()

// Promise.allSettled([p1, p2, p3])
//   .then((res) => {
//     console.log(res, "result");
//   })
//   .catch((err) => console.error(err));

//Promise.race()

// Promise.race([p1, p2, p3])
//   .then((res) => {
//     console.log(res, "result");
//   })
//   .catch((err) => console.error(err));

//Promise.any()

Promise.any([p1, p2, p3])
  .then((res) => {
    console.log(res, "result");
  })
  .catch((err) => {
    console.error(err);
    console.log(err.errors);
  });
