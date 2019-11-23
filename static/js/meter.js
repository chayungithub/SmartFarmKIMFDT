// Node A

var unit = [
        "องศาเซลเซียส",
        "เปอร์เซ็นต์",
        "ลักซ์",
        "ไมโครกรัมต่อลูกบาศก์เมตร"
    ]


var colors = {
    red: "#f50057",
    teal: "#1de9b6",
    blue: "#00b0ff",
    green: "#00e676",
    brown: "#795548",
    yellow: "#ffea00"
}

var a_air_temperature = new JustGage({
  id: "a_air_temperature",
  value : a_air_temperature,
  min: 0,
  max: 100,
  label: unit[0],
  gaugeWidthScale: 0.6,
  customSectors: {
    percents: true,
    ranges: [{
      color : colors.blue,
      lo : 0,
      hi : 30
    },{
      color : colors.red,
      lo : 31,
      hi : 100
    }]
  },
  counter: true
});

var a_air_humidity = new JustGage({
  id: "a_air_humidity",
  value : a_air_humidity,
  min: 0,
  max: 100,
  label: unit[1],
  gaugeWidthScale: 0.6,
  customSectors: {
    percents: true,
    ranges: [{
      color : colors.teal,
      lo : 0,
      hi : 50
    },{
      color : colors.blue,
      lo : 51,
      hi : 100
    }]
  },
  counter: true
});


var a_light_intensity= new JustGage({
  id: "a_soil_temperature",
  value : a_soil_temperature,
  min: 0,
  max: 1000,
  label: unit[2],
  gaugeWidthScale: 0.6,
  customSectors: {
    percents: true,
    ranges: [{
      color : colors.blue,
      lo : 0,
      hi : 50
    },{
      color : colors.yellow,
      lo : 51,
      hi : 100
    }]
  },
  counter: true
});

var a_pm25 = new JustGage({
  id: "a_soil_moisure",
  value : a_soil_moisure,
  min: 0,
  max: 250,
  label: unit[3],
  gaugeWidthScale: 0.6,
  customSectors: {
    percents: true,
    ranges: [{
      color : colors.teal,
      lo : 0,
      hi : 50
    },{
      color : colors.brown,
      lo : 51,
      hi : 250
    }]
  },
  counter: true
});

var refA = database.ref("A");
refA.orderByChild("time").limitToLast(1).on("child_added", function(snapshot) {
	var changedData = snapshot.val();
	var air_temperature = changedData.data.air_temperature;
	var air_humidity = changedData.data.air_humidity;
	var light_intensity = changedData.data.light_intensity;
	var pm25 = changedData.data.pm25;
    a_air_temperature.refresh(air_temperature);
    a_air_humidity.refresh(air_humidity);
    a_light_intensity.refresh(light_intensity);
    a_pm25.refresh(pm25);

    // update stat
    var sample = 1500

    database.ref("A").orderByChild("time").limitToLast(sample).on("child_added", function(snapshot){
        var air_temperature_arr = []
        var air_humidity_arr = []
        var light_intensity_arr = []
        var pm25_arr = []
        snapshot.forEach(function(data){
            var data_val = data.val()
            air_temperature_arr.push(data_val.data.air_temperature)
            air_humidity_arr.push(data_val.data.air_humidity)
            light_intensity_arr.push(data_val.data.light_intensity)
            pm25_arr.push(data_val.data.pm25)
        });

        air_temperature_arr = air_temperature_arr.sort(function(a, b){return a - b})
        air_humidity_arr = air_humidity_arr.sort(function(a, b){return a - b})
        light_intensity_arr = light_intensity_arr.sort(function(a, b){return a - b})
        pm25_arr = pm25_arr.sort(function(a, b){return a - b})
            $("#air_temperature_avg").text((air_temperature_arr.reduce((previous, current) => current += previous)/air_temperature_arr.length).toFixed(1));
            $("#air_temperature_max").text(air_temperature_arr[air_temperature_arr.length - 1].toFixed(1));
            $("#air_temperature_min").text(air_temperature_arr[0].toFixed(1));
            $("#air_humidity_avg").text((air_humidity_arr.reduce((previous, current) => current += previous)/air_humidity_arr.length).toFixed(1));
            $("#air_humidity_max").text(air_humidity_arr[air_humidity_arr.length - 1].toFixed(1));
            $("#air_humidity_min").text(air_humidity_arr[0].toFixed(1));
            $("#light_intensity_avg").text((light_intensity_arr.reduce((previous, current) => current += previous)/light_intensity_arr.length).toFixed(1));
            $("#light_intensity_max").text(light_intensity_arr[light_intensity_arr.length - 1].toFixed(1));
            $("#light_intensity_min").text(light_intensity_arr[0].toFixed(1));
            $("#pm25_avg").text((pm25_arr.reduce((previous, current) => current += previous)/pm25_arr.length).toFixed(1));
            $("#pm25_max").text(pm25_arr[pm25_arr.length - 1].toFixed(1));
            $("#pm25_min").text(pm25_arr[0].toFixed(1));
    });

});