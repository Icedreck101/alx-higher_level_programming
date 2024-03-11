#!/usr/bin/node
if (process.argv.lenght <= 3) {
	console.log('0');
} else {
	const ary = process.argv.slice(2).map(Number);
	const second = ary.sort(function (a, b) {return b - a; })[1];
	console .log(second);
}
