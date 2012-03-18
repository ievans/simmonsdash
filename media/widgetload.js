function loadEvents() {
    $.ajax({
	url: "/events",
	success: function(events_json){
	    $("#timestamp").html('');
	    $("#eventtitle").html('');
	    for (var key in events_json) {
		$("#timestamp").append("<li>" + events_json[key].timestamp + "</li>");
		$("#eventtitle").append("<li>" + events_json[key].title + "</li>");
	    }
	}
    });
}

function loadEvents2() {
    $.ajax({
	url: "/events",
	success: function(events_json){
	    $("#eventlist").html('');
	    for (var key in events_json) {
		$("#eventlist").append("<tr><td><time>" + events_json[key].timestamp + "</time></td><td>" + events_json[key].title + "</td></tr>");
	    }
	}
    });
}

function loadWeather() {
    $.ajax({
	url: "/weather",
	success: function(weather_json) {
	    for (var key in weather_json) {
		$("#" + key).html(weather_json[key]);
	    }
	    $("#nowicon").attr("src", weather_json["nowicon"]);
	    $("#todayicon").attr("src", weather_json["todayicon"]);
	    $("#tomorrowicon").attr("src", weather_json["tomorrowicon"]);
	    $("#dayaftericon").attr("src", weather_json["dayaftericon"]);
	},
	async: true
    });    
}

function loadClock(){
    var time = new Date ();
    var mins = time.getMinutes();
    if(mins < 10){
	mins = '0' + mins;
    }

    var hours = time.getHours();
    
    var days = new Array('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday');
    var day = days[time.getDay()];
    var date = time.getDate();
    
    var months=new Array("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December");
    var month = months[time.getMonth()];
    
    var year = time.getFullYear();
    
    var M= ( hours < 12 ) ? "AM" : "PM";
    M=String(M);
    if(M.length==0){
        M="00";
    }
    else if(M.length==1){
        M="0"+M;
    }
    if(hours>12){
        hours-=12;
    }
    
    $('#date').html(day + ' ' + month + ' ' + date + ', ' + year);
    $('#time').html(hours + ':' + mins + ' ' + M);
    $('#todayDay').html(day);
    $('#tomorrowDay').html(days[(time.getDay() + 1) % 7]);
    $('#dayAfterDay').html(days[(time.getDay() + 2) % 7]);

}

function loadNews() {
    $.ajax({
	url: "/news",
	success: function(news_json) {
	    $("#newsticker").html('');
	    for (var key in news_json) {
		$("#newsticker").append("<li><p>" + ' ' + news_json[key].title + '&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp'  +"</p></li>");
	    }
	},
	async: false
    });
}

function loadCalendar() {
    $.ajax({
	url: "/calendar",
	success: function(calendar_json){
	    for (var key in calendar_json) {
		$("#" + key).html(calendar_json[key]);
	    }
	}
    });
}

function loadNextbus() {
    $.ajax({
	url: "/nextbus",
	success: function(nextbus_json){
	    $("#nextbus").html('');
	    for (var key in nextbus_json){
		$("#nextTime" + key).html('<p>' + nextbus_json[key] + '</p>');
	    }
	}
    });
}

$(document).ready(function() {
    loadCalendar();
    loadEvents();
    loadEvents2();
    loadNextbus();
    loadClock();
    loadWeather();
    setInterval(loadCalendar, 60000 );
    setInterval(loadEvents, 10000 );
    setInterval(loadEvents2, 10000 );
    setInterval(loadNextbus, 10000);
    setInterval(loadClock, 1000);

    $(function(){
	loadNews();
	$("ul#newsticker").liScroll({travelocity: 0.03});
    });

});

 /*  
   $.ajax({
   url: "/weather",
   success: function(weather_json){
   $("#leftBottom").html(html);
   }
   });
*/
