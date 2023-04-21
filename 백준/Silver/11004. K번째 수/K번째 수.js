// fs 모듈을 이용해 파일 전체를 읽어와 문자열로 저장하기
let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let [n, k] = input[0].split(" ").map(Number)
let arr = input[1].split(" ").map(Number);

arr.sort(function (a, b) {
  return a - b;
});

console.log(arr[k - 1]);