function solution(priorities, location) {
  let rank = 0;
  while (1) {
    if (priorities[0] === Math.max.apply(null, priorities)) {
      rank += 1;
      if (location === 0) {
        return rank;
      } else {
        location -= 1;
      }
    } else {
      priorities.push(priorities[0]);
      location = location === 0 ? priorities.length - 2 : location - 1;
    }
    priorities.shift(0);
  }
}
