//OBJECTS AND SUCH


var firstName = "HEINRICH";
var awesomeThoughts = "I am Jack and I am AWESOME!";
var email = "iamjackc@gmail.com";

var newEmail = email.replace("gmail", "udacity")
console.log(firstName, awesomeThoughts, email, newEmail);

var funThoughts = awesomeThoughts.replace("AWESOME", "fun");
console.log(funThoughts);

var role = "Journalist trying to code"
var formattedName = HTMLheaderName.replace("%data%", "Jack Lemonade");
var formattedRole = HTMLheaderRole.replace("%data%", role);
var formattedWelcome = HTMLwelcomeMsg.replace("%data%", "") = '<span class="welcome-message">%data%</span>';
$("#header").prepend([formattedRole]);
$("#header").prepend([formattedName]);


var skills = [" lemon-threading ", "coffin carrying ", "a hundred stars ", "the house of grief ", "my mother's bones stretched out against her body "];

var bio = {
	"name" : "James ",
	"role" :  "Journalist ",
	"contact info" : "Cheese mail",
	"welcome_message" : "Greetings, earthlings ",
	"picture" : "images/fry.jpg",
	"skills": skills
};

bio["lemons"] = "Juicy";
bio.oranges = "Bells of st clemens";

console.log(bio["skills"]);

var altBio = {
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
	"skills": skills,
    "bioPic" : "images/fry.jpg",
}

var work = { };
work.position = "Reporter";
work.employer = "Bloomberg";
work.years = 2;
work.city = "San Francisco";

console.log(work);

var education = { };
education["name"] = " University of East Anglia";
education["years attended"] = 3;
education["location"] = "Norwich, East Anglia, UK"

console.log(education);

var json_education = {
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
console.log(json_education);

var json_work = {
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

console.log(json_work);

var json_projects = {
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

var json_bio = {
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
	"skills": skills,
    "bioPic" : "images/fry.jpg",
}

//DISPLAY GOES HERE

var formattedName = HTMLheaderName.replace("%data%", bio["name"]);
var formattedRole = HTMLheaderRole.replace("%data%", bio["role"]);
var formattedWelcome = HTMLwelcomeMsg.replace("%data%", bio["welcome_message"]);
var formattedPic = HTMLbioPic.replace("%data%", bio["picture"]);
var formattedContact = HTMLcontactGeneric.replace("%data%", bio["contact info"]);
var formattedSkills = HTMLskills.replace("%data%", bio["skills"]);

$("#header").prepend([formattedName]);
$("#header").prepend([formattedRole]);
$("#header").prepend([formattedWelcome]);
$("#header").prepend([formattedPic]);
$("#header").prepend([formattedContact]);
$("#header").prepend([formattedSkills]);

$("#main").append(work["position"]);
$("#main").append(education.name);