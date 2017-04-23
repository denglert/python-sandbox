///////////////////////////////////
// --- First-class functions --- //
///////////////////////////////////

// First-class functions:
// "A programming language is said to have first-class function if it treats
// functions as first-class citizens."

// First class citizens:
// "A first-class citizen (sometimes called first-class objects) in a programming
// language is an entity which supports all the operations generally available to
// other entities. These operations typically inclued being passed as an
// argument, returned from a function, and assigned to a variable."


function square(x)
{
    return x*x ;
}

function cube(x)
{
    return x*x*x ;
}

var f = square(5)

console.log('square: ', square)
console.log('f: ', f)
console.log('End of first segment.\n')

///////////////////////////////////////////////////////

var f = square

console.log('square: ', square)
console.log('f: ', f)
console.log('f(5): ', f(5))
console.log('End of second segment.\n')


///////////////////////////////////////////////////////
// -  So far we assigned a function to a variable, but we can also pass
// functions as arguments and return functions as the result of other functions.
// Let's take a look at both of these examples.

// Higher-order function: a function which accepts other functions as arguments,
// or returns functions as their result

// - Example 1: map(function, array) function
// Passing a function as an argument to another function

function my_map ( func, arg_list)
{
	 result = [];
	 for(var i = 0; i < arg_list.length; i++ )
	 {

		  result.push( func( arg_list[i] ) )
	 }

	 return result;
}

var squares = my_map( square, [1,2,3,4,5] )
var cubes   = my_map( cube,  [1,2,3,4,5] )

console.log('squares: ', squares )
console.log('cubes: ', cubes )
console.log('End of third segment.\n')

///////////////////////////////////////////////////////
// - Example 2: logger function
// Return a function from another function

function logger(msg)
{
	 function log_message()
	 {
		  console.log('Log: ' + msg)
	 }

	 return log_message
}

log_hi = logger('Hi!')
log_hi()
log_hi()

console.log('End of fourth segment.\n')

///////////////////////////////////////////////////////
// - Example 3: html tag
// Return a function from another function

function html_tag(tag)
{
	 function wrap_text( msg )
	 {
		  console.log( '<' + tag + '>' + msg + '</' + tag + '>' ) 
	 }

	 return wrap_text
}

print_h1 = html_tag('h1')

print_h1('Test headline!')
print_h1('Another Headline!')

print_p = html_tag('p')
print_p('Test paragraph!')
