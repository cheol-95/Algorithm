// Run by Node.js

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
rl.on('line', function (line) {
  tmp = line.split(' ').map(item => Number(item));
  console.log(tmp[0] >> tmp[1]);
  console.log(tmp[0] << tmp[1]);
  rl.close();
}).on('close', function () {
  process.exit();
});
