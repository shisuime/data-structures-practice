class Node {
  constructor(data = null, next = null) {
    this.data = data;
    this.next = next;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
  }

  insert_at_begining(data) {
    let node = new Node(data, this.head);
    this.head = node;
  }

  insert_at_end(data) {
    if (!this.head) {
      this.head = new Node(data, null);
      return;
    }

    let itr = this.head;
    while (itr.next) {
      itr = itr.next;
    }
    itr.next = new Node(data, null);
  }

  insert_by_list(list) {
    this.head = null;
    list.forEach((data) => this.insert_at_end(data));
  }
  getLength() {
    let itr = this.head;
    let count = 0;
    while (itr) {
      count += 1;
      itr = itr.next;
    }
    return count;
  }

  remove_at(index) {
    if (index < 0 || index >= this.getLength()) {
      throw new Error("index out of bounds here");
    } else if (index === 0) {
      this.head = this.head.next;
      return;
    }
    let itr = this.head;
    let count = 0;

    while (itr) {
      if (count == index - 1) {
        itr.next = itr.next.next;
      }
      itr = itr.next;
      count += 1;
    }
  }

  insert_at(index, data) {
    if (index < 0 || index >= this.getLength()) {
      throw new Error("index out of bounds here");
    } else if (index === 0) {
      this.insert_at_begining(data);

      return;
    } else {
      let itr = this.head;
      let count = 0;
      while (itr) {
        if (count === index - 1) {
          let node = new Node(data, itr.next);
          itr.next = node;
          break;
        }
        itr = itr.next;
        count += 1;
      }
    }
  }

  insert_after(data_after, data_to_insert) {
    if (!this.head) {
      return;
    } else if (this.head.data == data_after) {
      this.head.next = new Node(data_to_insert, this.head.next);
    } else {
      let itr = this.head;
      while (itr) {
        if (itr.data == data_after) {
          itr.next = new Node(data_to_insert, itr.next);
          break;
        }

        itr = itr.next;
      }
    }
  }
  remove_by_value(data) {
    if (!this.head) {
      return;
    } else if (this.head.data == data) {
      this.head = this.head.next;
    } else {
      let itr = this.head;
      while (itr.next) {
        if (itr.next.data == data) {
          itr.next = itr.next.next;
          return;
        }

        itr = itr.next;
      }
    }
  }

  printList() {
    if (!this.head) {
      console.log("null list");
      return;
    }
    let itr = this.head;
    let strlist = "";
    while (itr) {
      strlist += itr.data.toString() + "--->";

      itr = itr.next;
    }

    console.log(strlist);
  }
}

obj = new LinkedList();
// obj.insert_at_begining(1);
// obj.insert_at_begining(2);
// obj.insert_at_begining(3);
// obj.insert_at_begining(5);
// obj.insert_at_end(3245);
// obj.insert_at_begining(5);
// obj.insert_at_begining(5);

// obj.insert_at_begining(5);
// obj.insert_at_end(3245);

obj.insert_by_list([1, 2, 3, 4, 5, 6, 7]);
// obj.remove_at(3);
obj.insert_at(3, "nigga");
obj.insert_after(2, "wassupnigga");
obj.remove_by_value(3);
obj.printList();
console.log(obj.getLength());
