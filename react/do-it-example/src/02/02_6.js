//  learn before ES6 define class

function Shape(x, y) {
  this.name = 'Shape';
  this.move(x, y);
}

Shape.create = function (x, y) {
  return new Shape(x, y);
};

Shape.prototype.move = function (x, y) {
  this.x = x;
  this.y = y;
};
Shape.prototype.area = function (x, y) {
  return 0;
};

// or

Shape.prototype = {
  move: function (x, y) {
    this.x = x;
    this.y = y;
  },
  area: function (x, y) {
    return 0;
  },
};
let s = new Shape(0, 0);
s.area();

// how to define class in ES6

class Shape {
  static create(x, y) {
    return new Shape(x, y);
  }
  name = 'Shape';
  constructor(x, y) {
    this.move(x, y);
  }
  move(x, y) {
    this.x = x;
    this.y = y;
  }
  area() {
    return 0;
  }
}

var ss = new Shape(0, 0);
ss.area();
