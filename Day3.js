// AoC 2020 Day 3
//12/3/2020 3:20:57 PM 


data_small = ["..##.......",
"#...#...#..",
".#....#..#.",
"..#.#...#.#",
".#...##..#.",
"..#.##.....",
".#.#.#....#",
".#........#",
"#.##...#...",
"#...##....#",
".#..#...#.#"];

const URL = "https://adventofcode.com/2020/day/3/input";


// get the data
var data;
fetch(URL)
.then(res => res.text())
.then(text => {
    data=text;
})
.catch(err => console.log(err));
var data = data.split('\n').filter(String);


function count_trees(data, incr_down, incr_right) {
	var right,down,tree_count;
	right=down=tree_count=0;
	for(; down < data.length; down += incr_down){
		var max_len = data[down].length;
		if(data[down][right%max_len] == '#') tree_count++;
		right += incr_right;
	};
	return tree_count;
};

// Part 1
var incr_right, incr_down;
incr_down=1;
incr_right=3;
var tree_count = count_trees(data, incr_down, incr_right);
console.log("Tree count:" + String(tree_count));


// Part 2
var ans = 1;
var slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
for(const xy of slopes){
	incr_right = xy[0];
	incr_down = xy[1];
	// console.log(incr_right, incr_down);
	ans *= count_trees(data, incr_down, incr_right);
};
console.log("Answer part 2: " + String(ans));

