/*
This is empty on purpose! Your code to build the resume will go here.
speed of light = 299792458 meters/second
1 meter = 100 centimeters
1 nanosecond = 1.0/1000000000 seconds
 */


//TEST JS
//

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

console.log(jack_clark.job);

for(var i = 0; i<9; i++) {
	console.log(i);
}

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

var cheeses = ["emental", "cheddar", "nougat"];

for (cheese in cheeses) {
	console.log("Check");
	console.log(cheeses[cheese]);
}

var work = {
	"jobs": [
	  {
	  	"employer": "The Register",
	  	"title": "Reporter",
	  	"location": "San Francisco",
	  	"dates worked": "February 2013 to August 2014",
	  	"description": "World's only distributed systems reporter"
	  },
	  {
	  	"employer": "Bloomberg",
	  	"title": "Reporter",
	  	"location": "San Francisco",
	  	"dates worked": "August 2014 to Present",
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
console.log("COWABUNGER");
console.log(bio);
console.log(bio.skills);
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
var HTMLskills = '<li class="flex-item"><span class="white-text">%data%</span></li>';
var formattedSkills = HTMLskills.replace("%data%", bio["skills"]);

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


function Printer_Funk(val, ind, arr) {
	console.log("The element name is " + val + " and the element index is " + ind);
	var formattedSkills = HTMLskills.replace("%data%", bio.skills[ind]);
    $("#skills").append([formattedSkills]);
}
function category_check_loop(cat_check) {
	$("#header").append([HTMLskillsStart]);
	cat_check.forEach (Printer_Funk);
}

function jobs_Printer_Funk(val, ind, arr) {
	console.log("The element name is " + val + " and the element index is " + ind);
	var HTMLworkStart = '<div class="work-entry"></div>';
    $("#skills").append([HTMLworkStart]);
}
function jobs_category_check_loop(jobs_cat_check) {
	console.log(jobs_cat_check);
	jobs_cat_check.forEach (jobs_Printer_Funk);
}

console.log("Cheese train!!!");

category_check_loop(bio.skills);

//jobs_category_check_loop(work.jobs);

function check_object_contents(inp_obj) {
	for (i in inp_obj) {
		console.log("BEGIN");
		console.log(i);
		console.log(inp_obj[i]);
			for (j in inp_obj[i]) {
				console.log("test " + j);
				console.log("other test " + inp_obj[i][j]);
		}
	}
}

console.log("LAUNCHING ANOTHER TEST");
check_object_contents(work.jobs);
console.log("END");

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