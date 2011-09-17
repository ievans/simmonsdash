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

$(document).ready(function() {
    setInterval(loadCalendar, 1000 );
    setInterval(loadEvents, 1000 );
$(function(){
    $("ul#ticker02").liScroll({travelocity: 0.05});
});

});

/* $.ajax({
   url: "/nextbus",
   success: function(nextbus_json){
   $("#leftTop").html(html);
   }
   });
   
   $.ajax({
   url: "/weather",
   success: function(weather_json){
   $("#leftBottom").html(html);
   }
   });
*/