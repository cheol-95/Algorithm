// Run by Node.js

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on('line', function (line) {
  line = parseInt(line, 10);
  arr = [];
  for (var i = 1; i <= parseInt(line / 2); i++) {
    if (line % i === 0 && !arr.includes(i)) {
      arr.push(line / i);
      arr.push(i);
    }
  }
  console.log(arr.sort((a, b) => a - b));
  rl.close();
}).on('close', function () {
  process.exit();
});
