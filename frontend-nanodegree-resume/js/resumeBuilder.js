/*
This is empty on purpose! Your code to build the resume will go here.
speed of light = 299792458 meters/second
1 meter = 100 centimeters
1 nanosecond = 1.0/1000000000 seconds
 */

var firstName = "HEINRICH";
var awesomeThoughts = "I am Jack and I am AWESOME!";
var email = "iamjackc@gmail.com";

var newEmail = email.replace("gmail", "udacity")
console.log(firstName, awesomeThoughts, email, newEmail);

var funThoughts = awesomeThoughts.replace("AWESOME", "fun");
console.log(funThoughts);

var formattedName = HTMLheaderName.replace("%data%", "Jack Lemonade");
var formattedRole = HTMLheaderRole.replace("%data%", "Journalist Trying to Code");
$("#header").append([formattedName, formattedRole]);