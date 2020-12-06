// AoC 2020 Day 6
// Sun, Dec  6, 2020 12:45:53 AM

const fs = require('fs');
const p = console.log;
var _ = require('lodash');

fs.readFile('input.txt', 'utf8' , (err, data) => {
	if (err) {
	console.error(err)
	return
	}
  	seats = data.split('\n\n')
  	var total = 0
  	var total2 = 0
  	for(seat of seats){
  	    if(!seat){
  	        continue
        }
        var d = seat.replace(/\n/g, '').split('')
        var t = _.countBy(d)
        group_count = seat.split('\n').length
        for(v of Object.values(t)){
            if(parseInt(v)==group_count) total2 += 1
        }
        var s = new Set(d)
        total += s.size
    }
    p(total)
    p(total2)
})


