// fs 모듈을 이용해 파일 전체를 읽어와 문자열로 저장하기
let fs = require("fs");
let input = fs.readFileSync("./dev/stdin").toString().split("\n");

let s = Number(input[0]);
let sum = 0;
let current = 0;

while (sum <= s) {
  current += 1;
  sum += current;
}

console.log(current - 1);