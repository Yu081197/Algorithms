let fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().split("\n");

let n = Number(input[0]);
let dist = input[1].split(" ").map(Number);
let cost = input[2].split(" ").map(Number);
// console.log(dist, cost);

//주유비용(cost) 배열의 값을 비오름차순이 되도록 변환
// [5, 2, 4, 1] => [5, 2, 2, 1]

let minCost = cost[0];

for (let i = 0; i < n; i++) {
  minCost = Math.min(minCost, cost[i]);
  cost[i] = minCost;
}

let answer = BigInt(0); //큰 정수를 처리할 때 사용
for (let i = 0; i < n - 1; i++) {
  answer += BigInt(dist[i]) * BigInt(cost[i]);
}

console.log(String(answer));
