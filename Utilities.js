String.prototype.replaceAt = function(index, replacement) {
	// from https://stackoverflow.com/a/1431113
    return this.substr(0, index) + replacement + this.substr(index + replacement.length);
}

function p(e){
	console.log(e);
}

function read_data(path, splitter='\n'){
	fs.readFile(path, 'utf8' , (err, data) => {
		if (err) {
			console.error(err)
			return
		}
	  	seats = data.split(splitter)
  	}

module.exports = {p};