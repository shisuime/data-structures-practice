// // const array = [2020, 2320, 2520, 2130, 2190];
// // array[3] += 300;
// // console.log(array);

// //arrays
// // var heros = ["spider man", "thor", "hulk", "iron man", "captain america"];
// // heros.push("panther");
// // heros.pop();
// // heros.splice(2, 0, "panther");
// // heros.splice(3, 1, "strange");
// // heros.sort();
// // console.log(heros);

// //stack
// class Stack {
//   constructor() {
//     this.item = [];
//   }
//   push(element) {
//     this.item.push(element);
//   }
//   pop() {
//     return this.item.pop();
//   }
//   size() {
//     return this.item.length;
//   }
// }

// function reverse(str) {
//   const obj = new Stack();
//   for (const char of str) {
//     obj.push(char);
//   }

//   let rev = "";

//   while (obj.size() != 0) {
//     rev += obj.pop();
//   }
//   return rev;
// }

// console.log(reverse("We will conquere COVID-19"));

// function isMatch(ch1, ch2) {
//   const matchObj = {
//     ")": "(",
//     "]": "[",
//     "}": "{",
//   };
//   return matchObj[ch1] === ch2;
// }

// function isBalanced(str) {
//   const stack = new Stack();
//   for (const char of str) {
//     if (char == "(" || char == "{" || char == "[") {
//       stack.push(char);
//     }
//     if (char == ")" || char == "}" || char == "]") {
//       if (stack.size() === 0) {
//         return false;
//       }
//       if (!isMatch(char, stack.pop())) {
//         return false;
//       }
//     }
//   }
//   return stack.size() === 0;
// }
// console.log(isBalanced("))((a+b}{"));

//queue

// class Queue {
//   constructor() {
//     this.buffer = [];
//   }
//   enqueue(n) {
//     this.buffer.unshift(n);
//   }
//   dequeue() {
//     if (this.buffer.length === 0) {
//       console.log("queue is empty");
//       return;
//     }
//     return this.buffer.pop();
//   }
//   front() {
//     return this.buffer[this.buffer.length - 1];
//   }
// }

// function produceBinary(n) {
//   const queue = new Queue();
//   queue.enqueue("1");

//   for (let i = 0; i <= n; i++) {
//     front = queue.front();
//     console.log(" ", front);

//     queue.enqueue(front + "0");
//     queue.enqueue(front + "1");

//     queue.dequeue();
//   }
// }
// produceBinary(10);

//flattening an array
function flattenArray(arr) {
  let result = [];
  for (let i = 0; i < arr.length; i++) {
    if (Array.isArray(arr[i])) {
      result = result.concat(flattenArray(arr[i]));
    } else {
      result.push(arr[i]);
    }
  }
  return result;
}

// Example usage
let nestedArray = [1, [2, [3, 4], 5], [6, 7]];
console.log(flattenArray(nestedArray));
