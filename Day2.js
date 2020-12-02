// AoC 2020 Day 2
// 12/2/2020 11:45:03 AM


const URL = 'https://adventofcode.com/2020/day/2/input';

var data;

// get the data
fetch(URL)
.then(res => res.text())
.then(text => {
    data=text;
})
.catch(err => console.log(err));

var reg = /(\d*)-(\d*) (.): (.*)/

// Part 1
var valid = 0
for (const current of data.split('\n')){
	//console.log(current)
	var captured_groups = current.match(reg);

	if(! captured_groups) {
		continue;
	}

	var len_min = parseInt(captured_groups[1]);
	var len_max = parseInt(captured_groups[2]);
	var char    = captured_groups[3];
	var password= captured_groups[4];

	var number_of_occurence = password.split(char).length - 1;

	if (number_of_occurence >= len_min && number_of_occurence <= len_max){
		//console.log(len_min, len_max, char, password);
		valid++;
	}
};
console.log('Answer for number of valid passwords: ' + valid);


// Part 2
var valid2 = 0
for (const current of data.split('\n')){
	//console.log(current)
	var captured_groups = current.match(reg);

	if(! captured_groups) {
		continue;
	}

	var start = parseInt(captured_groups[1]) -1;
	var end = parseInt(captured_groups[2]) - 1;
	var char    = captured_groups[3];
	var password= captured_groups[4];

	if (start + 2 > password.length || end + 1 > password.length){
		// check if start or end are off the string
		console.log(password, password.length, start, end);
	}

	var number_of_occurence = password.split(char).length - 1;

	if (password[start] == char ^ password[end] == char){
		//console.log(len_min, len_max, char, password);
		valid2++;
	}
};

console.log('Answer for number of valid passwords: ' + valid2);
