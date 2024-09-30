//object literals

// const circle = {
//   radius: 2,
//   location: {
//     x: 1,
//     y: 3,
//   },
//   draw: function () {
//     console.log("draw");
//   },
// };

// circle.draw();

//factory function
// function createCircle(radius) {
//   return {
//     radius: radius,

//     draw: function () {
//       console.log("draw");
//     },
//   };
// }

// const circleObj1 = createCircle(1);
// circleObj.draw();

//constructor
// function CircleClass(radius) {
//   this.radius = radius;
//   this.draw = function () {
//     console.log("draw");
//   };
// }

// const circleObj2 = new CircleClass(4);
// circleObj2.draw();

//functions are objects

// function CircleClass(radius) {
//   this.radius = radius;
//   this.draw = function () {
//     console.log("draw");
//   };
// }

// const circleObj2 = new CircleClass(4);
// circleObj2.draw();

//stopwatch
function Stopwatch() {
  let startTime,
    endTime,
    running,
    duration = 0;

  this.start = function () {
    if (running) {
      throw new Error("already started");
    }
    running = true;
    startTime = new Date();
  };
  this.stop = function () {
    if (!running) {
      throw new Error("already stopped");
    }
    running = false;
    endTime = new Date();

    const seconds = (endTime.getTime() - startTime.getTime()) / 1000;
    duration += seconds;
  };

  this.reset = function () {
    startTime = null;
    endTime = null;
    duration = 0;
    running = false;
  };

  Object.defineProperty(this, "duration", {
    get: function () {
      console.log(duration);
    },
  });
}
const s = new Stopwatch();
s.start();
