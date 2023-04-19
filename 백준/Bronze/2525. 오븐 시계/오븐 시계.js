// fs 모듈을 이용해 파일 전체를 읽어와 문자열로 저장하기
let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
let [a, b] = input[0].split(' ').map(Number);
let c = Number(input[1]);
let totalMinute = a * 60 + b + c; // 분의 형태로 바꾸기
totalMinute %= 1440;
let hour = parseInt(totalMinute / 60);
let minute = totalMinute % 60;
console.log(hour + " " + minute);