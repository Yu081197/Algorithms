// fs 모듈을 이용해 파일 전체를 읽어와 문자열로 저장하기
let fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().split("\n");

let t = Number(input[0]);
let line = 1;

for (let tc = 1; tc <= t; t++) {
  n = Number(input[line]);
  let arr = [];
  for (let i = line + 1; i <= line + n; i++) {
    let data = input[i].split(" ").map(Number);
    arr.push(data);
  }
}
