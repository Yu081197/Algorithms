// fs 모듈을 이용해 파일 전체를 읽어와 문자열로 저장하기
let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(input[0]);
let cnt = 0;
let flag = false;

while (n >= 0) {
  if (n == 0 || n % 5 == 0) {
    cnt += parseInt(n / 5);
    console.log(cnt);
    flag = true;
    break;
  }
  n -= 3;
  cnt += 1;
}
if (!flag) {
  console.log(-1);
}