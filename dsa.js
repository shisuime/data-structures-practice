// console.log(typeof typeof 1);
// console.log(Math.max(1, 7, 3));
// console.log(1 - 2);
// console.log(4 + "2" + "2");
// let arr = [1, 2, 3];
// let brr = [...arr];
// console.log(arr !== brr);

//Switch case

// const day = "monday";
// switch (day) {
//   case "monday": //day === "monday"
//     console.log("plan course structure");
//     break;

//   case "tuesday":
//     console.log("prepare theory");
//     break;
//   default:
//     console.log("not a valid day");
// }

// closest number to 0 in array

// function findClosest(arr) {
//   let closest = arr[0];
//   for (let x of arr) {
//     if (Math.abs(x) < Math.abs(closest)) {
//       closest = x;
//     }
//   }
//   if (closest < 0 && arr.includes(Math.abs(closest))) {
//     return Math.abs(closest);
//   } else {
//     return closest;
//   }
// }

// console.log(findClosest([1325, -2, 2, 3, 54, 5]));

// 2 words joined in alternative order
// function roman(str) {
//   const obj = { I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000 };
//   let sum = 0;
//   let len = str.length;
//   let i = 0;
//   while (i < n) {
//     if (i < n - 1 && obj[str[i]] < obj[str[i + 1]]) {
//       sum += obj[str[i + 1]] - obj[str[i]];
//       i += 2;
//     } else {
//       sum += obj[str[i]];
//       i += 1;
//     }
//   }
//   return sum;
// }
// const str = ["hi", "hellow", "hey"];
// console.log(str.slice(0, 2));
// const str2 = "dwadawd";
// console.log(str2.indexOf("w"));
