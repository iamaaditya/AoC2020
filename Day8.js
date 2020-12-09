// AoC 2020 Day 8
// 12/8/2020 1:00:06 AM

const fs = require('fs');

p = console.log

var path = 'input.txt'

var text = fs.readFileSync(path,'utf8').split(/\r?\n/)
const data = text.map(x => x.split(' '));

const ends = (data, part1= false) => {
    let visited = Array(data.length).fill(false);
    let total = 0;
    let index = 0;
    while(true){
        if(index >= data.length) break;
        if(visited[index]) 
            return part1 ? total : false
        else
            visited[index] = true
        if(data[index][0] === 'acc')
            total += parseInt(data[index][1])
        if(data[index][0] === 'jmp'){
            index += parseInt(data[index][1])
            continue
        }
        index++;
    }
    return total;
}

p('Part1: ' + ends(data, true))

for(const [i, d] of data.entries()){
    if(d[0] === 'acc') continue;
    data[i] = (d[0] === 'nop') ? ['jmp', d[1]] : ['nop', d[1]]
    var total = ends(data)
    if(total) break;
    data[i] = d
}
p('Part2: ' + total)