String.prototype.replaceAt = function(index, replacement) {
	// from https://stackoverflow.com/a/1431113
    return this.substr(0, index) + replacement + this.substr(index + replacement.length);
}
