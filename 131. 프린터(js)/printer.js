function solution(priorities, location) {
  let rank = 0;
  while (1) {
    if (priorities[0] === Math.max.apply(null, priorities)) {
      priorities.splice(0, 1);
      rank += 1;
      if (location === 0) {
        return rank;
      } else {
        location -= 1;
      }
    } else {
      priorities = [...priorities.slice(1), priorities[0]];
      location = location === 0 ? priorities.length - 1 : location - 1;
    }
  }
}
