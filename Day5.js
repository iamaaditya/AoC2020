// AoC 2020 Day 5
// 12/5/2020 10:47:38 AM
// Updated 12/5/2020 8:34:13 PM

const fs = require('fs');
const X = require('./Utilities');

function sum_n(e){
	return e*(e+1)/2;
}

fs.readFile('data', 'utf8' , (err, data) => {
	if (err) {
	console.error(err)
	return
	}
  	seats = data.split('\r\n')
  	let highest_seat = 0;
  	let smallest_seat = Number.MAX_SAFE_INTEGER;
  	let sum_of_seats = 0;
	for(seat of seats){
		current_seat = parseInt(seat.replace(/B/g, 1).replace(/F/g, 0));
		highest_seat = Math.max(highest_seat, current_seat);
		smallest_seat = Math.min(smallest_seat, current_seat);
		sum_of_seats += current_seat;
	}

	X.p(highest_seat);
	missing_seat = sum_n(highest_seat) - sum_of_seats - sum_n(smallest_seat-1);
	X.p(missing_seat);

})




