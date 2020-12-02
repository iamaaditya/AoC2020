// AoC 2020 Day 1
// 12/2/2020 11:04:33 AM   
// The first part can be done in O(N) by using hashmap
// but since this is my first day with JS
// using O(N^2) as a practice to using for-loops

const URL = 'https://adventofcode.com/2020/day/1/input';

var data;

// get the data
fetch(URL)
.then(res => res.text())
.then(text => {
    data=text;
})
.catch(err => console.log(err));

var arr = data.split('\n').filter(Number);

var numbers = arr.map(function (x) {
	return parseInt(x, 10)
});

var sumMap = new Map();

for(let i=0; i < numbers.length - 1; i++){
	for (let j=i+1; j < numbers.length; j++){
		a = numbers[i];
		b = numbers[j];
		sumMap.set(a+b, [a,b]);
		if (a + b == 2020){
			console.log(`a=${a}, b=${b}, a+b=${a+b}, a*b=${a*b}`);
			break;
		}
	}
};

// second part - 3SUM
// this one uses hashmap
for (const e of numbers){
    var remaining = 2020 - e;
    if(sumMap.has(remaining)){
        var [c, d] = sumMap.get(remaining);
		console.log(c,d,e, c+d+e, c*d*e);
		break;
    }
}