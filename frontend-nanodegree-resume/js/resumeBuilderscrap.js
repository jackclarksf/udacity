/*
This is empty on purpose! Your code to build the resume will go here.
speed of light = 299792458 meters/second
1 meter = 100 centimeters
1 nanosecond = 1.0/1000000000 seconds
/*
this works as well and is more efficiednt
var s = "audacity";

var udacityizer = function(s) {
    s = s.slice(1);
    s = s.charAt(0).toUpperCase() + s.slice(1);

    return s;
};

// Did your code work? The line below will tell you!
console.log(udacityizer(s));
/*
 */

var light_speed = 299792458
var light_speed_centimeter = light_speed * 100
var light_speed_c_nanoseconds = light_speed_centimeter / 1000000000

var firstName = "HEINRICH";
$("#main").append(["Jack Clark"]);
$("#main").append([" The speed of light is: " + light_speed + "meters per second and: " + light_speed_centimeter + " centimeters per second and: " + light_speed_c_nanoseconds + " centimeters per nanosecond" ]);

var skills = [" jelly ", "programming", "tennis", "cheese"];
console.log(skills.length);
//$("#main").append(skills);

$("#main").append(skills[0]);

console.log(firstName);

var string_to_change = "Audacity";
console.log(string_to_change);
changed_string = string_to_change.slice(1);
console.log(changed_string);

function capitalize(string_chg) {
	return string_chg.charAt(0).toUpperCase() + string_chg.slice(1);
}

new_string = capitalize(changed_string);
console.log(new_string);

var numbered_array = [4, 5, 7, 3, 7];
console.log(numbered_array);
var manipulate_number = numbered_array[4];
var changed_number = manipulate_number + 1
numbered_array.pop();
numbered_array.push(changed_number);
console.log(numbered_array);

// now let's do a function for this

function array_manipulate(array_fiddle) {
	get_length = array_fiddle.length;
	pop_n = get_length - 1;
	man_number = array_fiddle[pop_n];
	man_number_chg = man_number + 1;
	array_fiddle.pop();
	array_fiddle.push(man_number_chg);
	return array_fiddle;
}

function_array = array_manipulate(numbered_array);
console.log(function_array);

///If given a string of a two word name formatted with any mix of capitalization, can you manipulate the string to ensure the first name has a capital first letter and the last name is totally capitalized? Assume there's a space between the names. For instance, turning a string like "cAmEROn PittMAN" into "Cameron PITTMAN". Your answer should be a single string saved to the variable called finalName.

var name_fiddle = prompt("Please type a name with a space in the middle");
console.log("Let's try and change the string: " + name_fiddle);

function name_cleaner(input_name) {
  cap_up = capitalize(input_name);
  console.log(cap_up);
  var space_pos = cap_up.indexOf(" ");
  console.log(space_pos);
  var upper_case = cap_up.slice(space_pos).toUpperCase();
  var first_name = cap_up.slice(0, space_pos);
  console.log(first_name, upper_case);
  final_name = first_name + upper_case;
  console.log(final_name);
  return final_name;
}

cute_dog = name_cleaner(name_fiddle);
console.log(cute_dog);
console.log("NOW, THE OTHER METHOD!")

function generic_clean(input_s) {
  var low_case = input_s.toLowerCase();
  var up_first = low_case.charAt(0).toUpperCase() + low_case.slice(1);
  var space_pos = up_first.indexOf(" ");
  var final_name = up_first.slice(0, space_pos) + up_first.slice(space_pos).toUpperCase();
  return final_name;
}

new_name_fiddle = generic_clean(name_fiddle);
console.log(new_name_fiddle);

// SOMEWHAT MORE EFFICIENT METHOD function nameChanger(oldName) {
//    var finalName = oldName;
//    var names = oldName.split(" ");
//    names[1] = names[1].toUpperCase();
//    names[0] = names[0].slice(0,1).toUpperCase() + names[0].slice(1).toLowerCase();
//    finalName = names.join(" ");
//    return finalName;
//}


var jack_clark = {};
jack_clark.job = "course dev";

var makeCourse = function() {
  console.log("Made a course");
}

var courses = 0;
while(jack_clark.job === "course dev") {
  makeCourse();
  courses = courses + 1;
  if(courses === 10) {
    jack_clark.job = "learning specialist";
  }
}
