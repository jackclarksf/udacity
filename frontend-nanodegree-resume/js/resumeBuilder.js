/*
This is empty on purpose! Your code to build the resume will go here.
speed of light = 299792458 meters/second
1 meter = 100 centimeters
1 nanosecond = 1.0/1000000000 seconds
 */

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
console.log(json_education);

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
console.log(json_work);

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
	"skills": [" lemon-threading ", "coffin carrying ", "a hundred stars ", "the house of grief ", "my mother's bones stretched out against her body "];
    "bioPic" : "images/fry.jpg",
    //display: function
}
console.log(json_bio);

//***************
//DISPLAY SECTION
//***************