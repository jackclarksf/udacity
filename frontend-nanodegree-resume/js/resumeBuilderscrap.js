/*
This is empty on purpose! Your code to build the resume will go here.
speed of light = 299792458 meters/second
1 meter = 100 centimeters
1 nanosecond = 1.0/1000000000 seconds
 */

var light_speed = 299792458
var light_speed_centimeter = light_speed * 100
var light_speed_c_nanoseconds = light_speed_centimeter / 1000000000

var firstName = "HEINRICH";
$("#main").append(["Jack Clark"]);
$("#main").append([" The speed of light is: " + light_speed + "meters per second and: " + light_speed_centimeter + " centimeters per second and: " + light_speed_c_nanoseconds + " centimeters per nanosecond" ]);

console.log(firstName);