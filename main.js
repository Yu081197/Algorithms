// fs 모듈을 이용해 파일 전체를 읽어와 문자열로 저장하기
let fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().split("\n");

let groups = input[0].split("-");
console.log(groups);
let answer = 0;
for (i = 0; i < groups.length; i++) {
  let cur = groups[i]
    .split("+")
    .map(Number)
    .reduce((a, b) => a + b);
  console.log(cur);
  if (i == 0) answer += cur;
  else answer -= cur;
}
console.log(answer);
