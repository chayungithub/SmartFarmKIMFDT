var config_firebase = {
    apiKey: "AIzaSyAjaGj1__Xg7XY1H32izkClXw1Y4fmySHQ",
    authDomain: "smartfarming-4581d.firebaseapp.com",
    databaseURL: "https://smartfarming-4581d.firebaseio.com",
    projectId: "smartfarming-4581d",
    storageBucket: "smartfarming-4581d.appspot.com",
    messagingSenderId: "63050324538"
  };

firebase.initializeApp(config_firebase);
var status = 0;
var database = firebase.database();
var chartColors = {
	red: 'rgb(255, 99, 132)',
	orange: 'rgb(255, 159, 64)',
	yellow: 'rgb(255, 205, 86)',
	green: 'rgb(75, 192, 192)',
	blue: 'rgb(54, 162, 235)',
	purple: 'rgb(153, 102, 255)',
	grey: 'rgb(201, 203, 207)',
	brown: '#BCAAA4',
};


var station_name = ["สถานีตรวจวัด 1"]
var measure_type = [
        "อุณหภูมิ",
        "ความชื้นสัมพัทธ์",
        "ความสว่าง",
        "ดัชนีคุณภาพอากาศ"
    ]

var unit = [
        "องศาเซลเซียส",
        "เปอร์เซ็นต์",
        "ลักซ์",
        "ไมโครกรัมต่อลูกบาศก์เมตร"
    ]


// แสดงชื่อสถานี
var legend_display = false;
var graph_duration = 24*60*60000;
var graph_ttl = 24*60*60000;

var color1 = Chart.helpers.color;
var config1 = {
	type: 'line',
	data: {
		datasets: [{
			label: station_name[0],
			backgroundColor: color1(chartColors.red).alpha(0.5).rgbString(),
			borderColor: chartColors.red,
			fill: true,
			cubicInterpolationMode: 'monotone',
			data: []
        }
    ]
	},
	options: {
		elements: {
      point:{
      	radius: 0
      }
    },
		responsive: true,
		maintainAspectRatio: true,
		title: {
			display: true,
			text: measure_type[0]
		},
		scales: {
			xAxes: [{
				type: 'realtime',
				realtime: {
					duration: graph_duration,
					ttl: graph_ttl,
					refresh: 1500,
					delay: 0,
					pause: false,
				}
			}],
			yAxes: [{
				type: 'linear',
				display: true,
				scaleLabel: {
					display: true,
					labelString: unit[0]
				},
				ticks: {
                	beginAtZero:true,
                }
			}]
		},
		 legend: {
            display: legend_display,
            labels: {
                boxWidth:30
            }

        },
		tooltips: {
			mode: 'nearest',
			intersect: false
		},
		hover: {
			mode: 'nearest',
			intersect: true
		},
		plugins: {
			streaming: {
				frameRate: 60
			},
		},
	}
};

var color2 = Chart.helpers.color;
var config2 = {
	type: 'line',
	data: {
		datasets: [{
			label: station_name[0],
			backgroundColor: color2(chartColors.blue).alpha(0.5).rgbString(),
			borderColor: chartColors.blue,
			fill: true,
			cubicInterpolationMode: 'monotone',
			data: []
        }
    ]
	},
	options: {
		elements: {
      point:{
      	radius: 0
      }
    },
		responsive: true,
		maintainAspectRatio: true,
		title: {
			display: true,
			text: measure_type[1]
		},
		scales: {
			xAxes: [{
				type: 'realtime',
				realtime: {
					duration: graph_duration,
					ttl: graph_ttl,
					refresh: 1500,
					delay: 0,
					pause: false,
				}
			}],
			yAxes: [{
				type: 'linear',
				display: true,
				scaleLabel: {
					display: true,
					labelString: unit[1]
				},
				ticks: {
                	beginAtZero:true,
                }
			}]
		},
		 legend: {
            display: legend_display,
            labels: {
                boxWidth:30,
            }

        },
		tooltips: {
			mode: 'nearest',
			intersect: false
		},
		hover: {
			mode: 'nearest',
			intersect: true
		},
		plugins: {
			streaming: {
				frameRate: 60
			},
		},
	}
};

var color3 = Chart.helpers.color;
var config3 = {
	type: 'line',
	data: {
		datasets: [{
			label: station_name[0],
			backgroundColor: color3(chartColors.yellow).alpha(0.5).rgbString(),
			borderColor: chartColors.yellow,
			fill: true,
			cubicInterpolationMode: 'monotone',
			data: []
        }
    ]
	},
	options: {
		elements: {
      point:{
      	radius: 0
      }
    },
		responsive: true,
		maintainAspectRatio: true,
		title: {
			display: true,
			text: measure_type[2]
		},
		scales: {
			xAxes: [{
				type: 'realtime',
				realtime: {
					duration: graph_duration,
					ttl: graph_ttl,
					refresh: 1500,
					delay: 0,
					pause: false,
				}
			}],
			yAxes: [{
				type: 'linear',
				display: true,
				scaleLabel: {
					display: true,
					labelString: unit[2]
				},
				ticks: {
                	beginAtZero:true,
                }
			}]
		},
		 legend: {
            display: legend_display,
            labels: {
                boxWidth:30,
            }

        },
		tooltips: {
			mode: 'nearest',
			intersect: false
		},
		hover: {
			mode: 'nearest',
			intersect: true
		},
		plugins: {
			streaming: {
				frameRate: 60
			},
		},
	}
};

var color4 = Chart.helpers.color;
var config4 = {
	type: 'line',
	data: {
		datasets: [{
			label: station_name[0],
			backgroundColor: color4(chartColors.brown).alpha(0.5).rgbString(),
			borderColor: chartColors.brown,
			fill: true,
			cubicInterpolationMode: 'monotone',
			data: []
        }
    ]
	},
	options: {
		elements: {
      point:{
      	radius: 0
      }
    },
		responsive: true,
		maintainAspectRatio: true,
		title: {
			display: true,
			text: measure_type[3]
		},
		scales: {
			xAxes: [{
				type: 'realtime',
				realtime: {
					duration: graph_duration,
					ttl: graph_ttl,
					refresh: 1500,
					delay: 0,
					pause: false,
				}
			}],
			yAxes: [{
				type: 'linear',
				display: true,
				scaleLabel: {
					display: true,
					labelString: unit[3]
				},
				ticks: {
                	beginAtZero:true,
				    max: 200
                }
			}]
		},
		 legend: {
            display: legend_display,
            labels: {
                boxWidth:30,
            }

        },
		tooltips: {
			mode: 'nearest',
			intersect: false
		},
		hover: {
			mode: 'nearest',
			intersect: true
		},
		plugins: {
			streaming: {
				frameRate: 60
			},
		},
	}
};

var x = window.matchMedia("(max-width: 767px)");
var ctx = document.getElementById('airtempChart').getContext('2d');
var ctx2 = document.getElementById('airhumidChart').getContext('2d');
var ctx3 = document.getElementById('soiltempChart').getContext('2d');
var ctx4 = document.getElementById('soilhumidChart').getContext('2d');
if (!x.matches) {
    // ความสูงกราฟ มุมมองคอมพิวเตอร์
  ctx.canvas.height = 130;
  ctx2.canvas.height = 130;
  ctx3.canvas.height = 130;
  ctx4.canvas.height = 130;
}else{
  ctx.canvas.height = 400;
  ctx2.canvas.height = 400;
  ctx3.canvas.height = 400;
  ctx4.canvas.height = 400;
}
window.myChart1 = new Chart(ctx, config1);
window.myChart2 = new Chart(ctx2, config2);
window.myChart3 = new Chart(ctx3, config3);
window.myChart4 = new Chart(ctx4, config4);

function create_graph(state,node,air_temperature, air_humidity, pm25, light_intensity){
		if(state == "py"){
    		myChart1.data.datasets[node].data = air_temperature;
    		myChart2.data.datasets[node].data = air_humidity;
    		myChart3.data.datasets[node].data = light_intensity;
    		myChart4.data.datasets[node].data = pm25;
		}else{
			myChart1.data.datasets[node].data.push(air_temperature);
			myChart2.data.datasets[node].data.push(air_humidity);
			myChart3.data.datasets[node].data.push(light_intensity);
			myChart4.data.datasets[node].data.push(pm25);
		}

  	myChart1.update({
	  preservation: true
  	});
    myChart2.update({
      preservation: true
    });
    myChart3.update({
      preservation: true
    });
    myChart4.update({
      preservation: true
    });
}

var ref2 = database.ref("A");
ref2.orderByChild("time").limitToLast(1).on("child_added", function(snapshot) {
  	var changedData = snapshot.val();
  	var js_air_temperature = {
  		'x': changedData.time*1000,
  		'y': changedData.data.air_temperature
  	}
  	var js_air_humidity = {
  		'x': changedData.time*1000,
  		'y': changedData.data.air_humidity
  	}
  	var js_pm25 = {
  		'x': changedData.time*1000,
  		'y': changedData.data.pm25
  	}
  	var js_light_intensity = {
  		'x': changedData.time*1000,
  		'y': changedData.data.light_intensity
  	}
  	create_graph("js", 0, js_air_temperature, js_air_humidity, js_pm25, js_light_intensity)
})

window.onload = function() {
    // from python view
    create_graph("py", 0, a_air_temperature, a_air_humidity, a_soil_moisure, a_soil_temperature)
}


