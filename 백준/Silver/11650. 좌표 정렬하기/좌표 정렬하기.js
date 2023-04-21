// fs 모듈을 이용해 파일 전체를 읽어와 문자열로 저장하기
let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(input[0]);
let data = [];
for (let i = 1; i <= n; i++) {
  let [x, y] = input[i].split(" ").map(Number);
  data.push([x, y]);
}

function compare(a, b) {
  if (a[0] != b[0]) return a[0] - b[0]; // x 좌표 기준 오름차순
  else return a[1] - b[1]; // x가 같으면 y 좌표 기준 오름차순
}
data.sort(compare);

let answer = "";
for (let point of data) {
  answer += point[0] + " " + point[1] + "\n";
}
console.log(answer);
