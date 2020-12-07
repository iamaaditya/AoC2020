// AoC 2020 Day 7
// 12/7/2020 10:16:31 AM

const fs = require('fs');

p = console.log

var path = 'input.txt'

var text = fs.readFileSync(path,'utf8').split(/\r?\n/)

const regexp = /(\d+) (\w+ \w+)/g;
var adj = new Map()
for(const d of text){
    if(!d) continue
    var source, dest;
    [source, dest] = d.split(' bags contain')
    adj.set(source, [...dest.matchAll(regexp)])
}

function path_exists(source, target){
	if(source === target) return true;
	var exist = false
	for(const child of adj.get(source)){
		if(child[2] === target) return true;
		else{
			exist = exist || path_exists(child[2], target)
		}
	}
	return exist
}

function part1(target){
	var count = 0
	for(const n of adj.keys()){
		p(n)
		if(path_exists(n, target)) count++;
	}
	return count;
}

function part2(target){
	var total = 1;
	for(const child of adj.get(target)){
		if(child){
			total += parseInt(child[1]) * part2(child[2]);
		}
	}
	return total;
}

var target = 'shiny gold'
p(part1(target)-1)
p(part2(target)-1)
