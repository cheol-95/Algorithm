const getCombinations = (arr, selectNumber) => {
  const results = [];
  if (selectNumber === 1) {
    return arr.map((v) => [v]);
  }

  arr.forEach((fixed, index, origin) => {
    const rest = origin.slice(index + 1);
    const combinations = getCombinations(rest, selectNumber - 1);
    combinations.forEach((combination) => {
      results.push([fixed, ...combination]);
    });
  });

  return results;
};

function solution(orders, course) {
  var answer = [];
  const count = {};

  course.forEach((v) => {
    count[v] = [];
  });

  orders.forEach((order) => {
    course.forEach((cnt) => {
      const tmp = getCombinations(order.split('').sort(), cnt);
      count[cnt].push(...tmp);
    });
  });
  for (let value in count) {
    const res = count[value].reduce((accu, curr) => {
      accu[curr] = (accu[curr] || 0) + 1;
      return accu;
    }, {});

    let max = 0;
    for (let value in res) {
      max = max > res[value] ? max : res[value];
    }

    if (max > 1) {
      for (let value in res) {
        if (max === res[value]) {
          value = value.split(',').join('');
          answer.push(value);
        }
      }
    }
  }

  answer.sort();
  return answer;
}

const [orders, course] = [
  ['XYZ', 'XWY', 'WXA'],
  [2, 3, 4],
];

console.log(solution(orders, course));
