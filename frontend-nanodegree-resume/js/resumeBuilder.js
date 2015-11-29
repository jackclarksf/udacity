/*
This is empty on purpose! Your code to build the resume will go here.
speed of light = 299792458 meters/second
1 meter = 100 centimeters
1 nanosecond = 1.0/1000000000 seconds
 */


//TEST JS
//


//console.log(jack_clark.job);

//for(var i = 0; i<9; i++) {
//	console.log(i);
//}

//***************
//DATA STRUCTURES
//***************
var education = {
	"schools": [
	  {
	  	"name": "UEA",
	  	"city": "Norwich, Norfolk, UK",
	  	"degree": "BA",
	  	"major": ["Creative writing", "Literature"]
	  },
	  {
	  	"name": "NYU",
	  	"city": "New York, USA",
	  	"degree": "SPACE",
	  	"major": ["orbital mechanics", "cheese architecture", "lemonade creation"]

	  }
	],
  "online courses": [
    {
    	"title": "Javascript Syntax",
    	"School": "Udacity",
    	"Year": 2015,
    }
  ]
};
console.log(education);

var work = {
	"jobs": [
	  {
	  	"employer": "The Register",
	  	"title": "Reporter",
	  	"location": "San Juan",
	  	"dates_worked": "February 2013 to August 2014",
	  	"description": "World's only distributed systems reporter"
	  },
	  {
	  	"employer": "Bloomberg",
	  	"title": "Reporter",
	  	"location": "San Francisco",
	  	"dates_worked": "August 2014 to Present",
	  	"description": "Artificial intelligence and so much more",
	  }
	],
};
console.log(work);

var projects = {
	"projects": [
	  {
	  	"title": "Cheese preparation",
	  	"dates": "March 2013",
	  	"description": "The ultimate dairy curation",
	  	"images": "images/197x148.jpg"
	  },
	  {
	  	"title": "AI research",
	  	"dates": "March 2013",
	  	"description": "The ultimate dairy curation",
	  	"images": "images/197x148.jpg"
	  }
	]

}

projects.display = function() {
 for (project in projects.projects) {
 	$("#projects").append(HTMLprojectStart);

 	var formattedProjectTitle = HTMLprojectTitle.replace("%data%", projects.projects[project].title);
 	var formattedProjectDates = HTMLprojectDates.replace("%data%", projects.projects[project].dates);
 	var formattedProjectDescription = HTMLprojectDescription.replace("%data%", projects.projects[project].description);
 	var formattedProjectImage = HTMLprojectImage.replace("%data%", projects.projects[project].images);
 	$(".project-entry:last").append(formattedProjectTitle);
 	$(".project-entry:last").append(formattedProjectDates);
 	$(".project-entry:last").append(formattedProjectDescription);
 	$(".project-entry:last").append(formattedProjectImage);
 }
}

projects.display();




function udacity_function() {
	for (job in work.jobs) {
		$("#workExperience").append(HTMLworkStart);

		var formattedEmployer = HTMLworkEmployer.replace("%data%", work.jobs[job].employer);
		var formattedTitle = HTMLworkTitle.replace("%data%", work.jobs[job].title);
		var formattedEmployerTitle = formattedEmployer + formattedTitle;

		$(".work-entry:last").append(formattedEmployerTitle);
		var formattedDescription = HTMLworkDescription.replace("%data%", work.jobs[job].description);
		var formattedDates = HTMLworkDates.replace("%data%", work.jobs[job].dates_worked);
		var formattedLocation = HTMLworkLocation.replace("%data%", work.jobs[job].location);

		$(".work-entry:last").append(formattedDates);
		$(".work-entry:last").append(formattedDescription);
		$(".work-entry:last").append(formattedLocation);
	}
}


console.log(projects);

var bio = {
	"name" : "James ",
	"role" :  "Journalist ",
	"contacts" : {
		"mobile" : "666-666-6666",
		"email" : "john@example.com",
		"github" : "mappingbabel",
		"twitter" : "@johndoe",
		"location" : "San Francisco",
	},
	"welcomeMessage" : "Greetings, earthlings ",
	"skills": [" lemon-threading ", "coffin carrying ", "a hundred stars ", "the house of grief ", "my mother's bones stretched out against her body "],
    "bioPic" : "images/fry.jpg",
    //display: function
}

console.log(bio);
//QUIZ - WRITE IF TO CHECK IF STUFF IN BIO

//***************
//DISPLAY SECTION
//***************

var formattedName = HTMLheaderName.replace("%data%", "Jack Lemonade");
var formattedRole = HTMLheaderRole.replace("%data%", bio.role);
var formattedPic = HTMLbioPic.replace("%data%", bio["bioPic"]);
$("#header").prepend([formattedPic]);
$("#header").prepend([formattedRole]);
$("#header").prepend([formattedName]);

var HTMLskillsStart = '<h3 id="skills-h3">Skills at a Glance:</h3><ul id="skills" class="flex-box"></ul>';
//var HTMLskills = '<li class="flex-item"><span class="white-text">%data%</span></li>';
var formattedSkills = HTMLskills.replace("%data%", bio["skills"]);

function Printer_Funk(val, ind, arr) {
	//console.log("The element name is " + val + " and the element index is " + ind);
	var formattedSkills = HTMLskills.replace("%data%", bio.skills[ind]);
    $("#skills").append([formattedSkills]);
}
function category_check_loop(cat_check) {
	$("#header").append([HTMLskillsStart]);
	cat_check.forEach (Printer_Funk);
}

test_speech = "LEMON NIGHTMARE"
category_check_loop(bio.skills);

//jobs_category_check_loop(work.jobs);


function check_object_contents(inp_obj) {
	for (i in inp_obj) {
		var working_object = inp_obj[i];
		$("#workExperience").append([HTMLworkStart]);
			for (var key in working_object) {
				if (working_object.hasOwnProperty(key)) {
					if (key === "employer") {
							var DOG_GONE = HTMLworkEmployer.replace("%data%", working_object[key]);
						}
					if (key === "title") {
							var DOG_LEMON = HTMLworkTitle.replace("%data%", working_object[key]);
					}
				}
			}
		var TWO_HEADED_DOG = DOG_GONE + DOG_LEMON;
		$(".work-entry:last").append([TWO_HEADED_DOG]);
	}
}

// NEED DATES WORKED AND DESCRIPTION EG
//	  	"dates worked": "August 2014 to Present",
//	  	"description": "Artificial intelligence and so much more",
//
//

//SO THIS FUNCTION SORT OF WORKS BUT WE'RE DOING SOME BLOODY WEIRD LOOP STUFF
//SOLUTION - BREAK DOWN INTO SUB FUNCTIONS AND RETURN ENTITIES
//IT IS ALSO, APPARENTLY, TOTALLY WRONG
//ACTUALLY, THIS FUNCTION WAS CORRECT, WE JUST HANDED PUNCTUATED IT CORRECTLY. LOL
//OUR FUNCTION SEEMS TO HANDLE ERRORS BETTER

//console.log("LAUNCHING ANOTHER TEST");
//check_object_contents(work.jobs);
//console.log("END");

function myFunction() {
    return "lemon face";
}

var lemon = myFunction();
console.log(lemon);

function udacity_function() {
	for (job in work.jobs) {
		$("#workExperience").append(HTMLworkStart);

		var formattedEmployer = HTMLworkEmployer.replace("%data%", work.jobs[job].employer);
		var formattedTitle = HTMLworkTitle.replace("%data%", work.jobs[job].title);
		var formattedEmployerTitle = formattedEmployer + formattedTitle;

		$(".work-entry:last").append(formattedEmployerTitle);
		var formattedDescription = HTMLworkDescription.replace("%data%", work.jobs[job].description);
		var formattedDates = HTMLworkDates.replace("%data%", work.jobs[job].dates_worked);
		var formattedLocation = HTMLworkLocation.replace("%data%", work.jobs[job].location);

		$(".work-entry:last").append(formattedDates);
		$(".work-entry:last").append(formattedDescription);
		$(".work-entry:last").append(formattedLocation);
	}
}

udacity_function();

//THIS IS A BIT HACKY, BUT IT WORKS AT DISPLAYING. SEEMS TO ACCESS SUBCLASSES. NEED TO FIDDLE AROUND
function contact_udacity_function() {
	contact_terms = [];
	contact_list = [];
	for (contact in bio.contacts) {
		console.log(contact_list);
		console.log(contact_terms);
		console.log(contact);
		contact_list.push(bio.contacts[contact]);
		contact_terms.push(contact);
		formatted_contacts = HTMLcontactGeneric.replace("%contact%", contact);
		formatted_contacts2 = formatted_contacts.replace("%data%", bio.contacts[contact]);
		$("#topContacts").append(formatted_contacts2);
	}
}

contact_udacity_function();

function locationizer(work_obj) {
	work_locations = [];
	for (work in work_obj) {
		work_locations.push(work_obj[work].location);
	}
	return work_locations;
}

loc_array = locationizer(work.jobs);
console.log(loc_array);

function inName(name_string) {
	console.log("Testing: " + name_string);
	name_string = name_string.trim().split(" ");
	name_string[1] = name_string[1].toUpperCase();
	name_string[0] = name_string[0].slice(0, 1).toUpperCase() + name_string[0].slice(1).toLowerCase();
	return name_string[0] +" "+name_string[1];

}

//inName("Jack CLArk");
$("#main").append(internationalizeButton);

//below here is not USED. AT ALL!
//below here is not USED. AT ALL!
//below here is not USED. AT ALL!
//below here is not USED. AT ALL!
//below here is not USED. AT ALL!
function proper_category_check(entity) {
	for (key in entity) {
		if (entity.hasOwnProperty(key)) {
			if (key === "skills") {
				console.log(entity[key]);
				for (i in key) {
					console.log(i);
					console.log(entity[key]);
				}
			}
		}
	}
}

function jobs_proper_category_check(entity) {
	for (key in entity) {
		if (entity.hasOwnProperty(key)) {
			console.log("Checking" + entity + " against key of: " + key);
			console.log(entity[key]);
		}
	}
}

//proper_category_check(bio);

function PrintThis(val, ind, arr) {
	console.log("The element name is " + val + " and the element index is " + ind);
}

//bio.skills.forEach (PrintThis);


//for (i in work.jobs) {
//	console.log("BEGIN");
//	console.log(i);
//	console.log(work.jobs[i]);
//	for (j in work.jobs[i]) {
//		console.log("test " + j);
//		console.log("other test " + work.jobs[i][j]);
//	}
//}


function category_check(cat_check) {
	if ("skills" in cat_check) {
	  console.log("There are skills in bio");
      $("#header").append([HTMLskillsStart]);
      var formattedSkills = HTMLskills.replace("%data%", bio.skills[0]);
      $("#skills").append([formattedSkills]);
      var formattedSkills = HTMLskills.replace("%data%", bio.skills[1]);
      $("#skills").append([formattedSkills]);
      var formattedSkills = HTMLskills.replace("%data%", bio.skills[2]);
      $("#skills").append([formattedSkills]);
      var formattedSkills = HTMLskills.replace("%data%", bio.skills[3]);
      $("#skills").append([formattedSkills]);
	    }
    else {
    	console.log("Not sure what is going on here!");
    }
}

//category_check(bio);
//^WRITE A FUNCTION TO SIMPLIFY THIS ONE 11/22/2015
//ACHIEVED! 11/24/2015