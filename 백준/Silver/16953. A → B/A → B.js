// fs 모듈을 이용해 파일 전체를 읽어와 문자열로 저장하기
let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let [a, b] = input[0].split(" ").map(Number);
let flag = false;
let result = 1;

while (a <= b) {
  if (a == b) {
    flag = true;
    break;
  }
  if (b % 2 == 0) {
    //b가 2로 나누어 떨어진다면
    b = parseInt(b / 2);
  } else if (b % 10 == 1) {
    //b가 10으로 안나누어 떨어진다면 즉, b의 1의자리수가 1이라면
    b = parseInt(b / 10);
  } else {
    break;
  }
  result++;
}

if (flag) {
  console.log(result);
} else {
  console.log(-1);
}
