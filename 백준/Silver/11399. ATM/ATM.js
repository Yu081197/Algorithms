// fs 모듈을 이용해 파일 전체를 읽어와 문자열로 저장하기
let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(input[0]);
let arr = input[1].split(" ").map(Number);

arr.sort((a, b) => a - b);

let answer = 0;
let summary = 0;
for (let i = 0; i < n; i++) {
  summary += arr[i]; //i번째 사람이 기다린 총 시간
  answer += summary; //지금까지 소요된 총 시간
}

console.log(answer);
