// fs 모듈을 이용해 파일 전체를 읽어와 문자열로 저장하기
let fs = require("fs");
let input = fs.readFileSync("./dev/stdin").toString().split("\n");

let n = Number(input[0]);
let arr = input[1].split(" ").map(Number);

newArr = [...new Set(arr)];
newArr.sort((a, b) => a - b);

let myMap = new Map();
for (let i = 0; i < newArr.length; i++) {
  myMap.set(newArr[i], i);
}

answer = "";
for (x of arr) answer += myMap.get(x) + " ";
console.log(answer);
