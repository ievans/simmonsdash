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

function loadClock(){
    var time = new Date ();
    var hours=time.getHours();
    var mins=time.getMinutes();
    var months=new Array("january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december");
    var month=months[time.getMonth()];
    var M= ( hours < 12 ) ? "AM" : "PM";
    if(hours>12){
        hours-=12;
    }
    $("#newclock").html('<date>'+month+' '+time.getDay()+', '+(time.getYear()+1900)+'</date><br><time>'+hours+":"+mins+'</time><m> '+M+'</m>');

}

function loadNews() {
    $.ajax({
	url: "/news",
	success: function(news_json) {
	    $("#newsticker").html('');
	    for (var key in news_json) {
		$("#newsticker").append("<li><span>" + news_json[key].timestamp + '</span><a href="#">'
					+ news_json[key].title + "</a></li>");
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
	    $("#nextbus").html("");
	    for (var key in nextbus_json) {
		$("#nextbus").append("<li>" + nextbus_json[key] + "</li>");
	    }
	}
    });
}

$(document).ready(function() {
    setInterval(loadCalendar, 60000 );
    setInterval(loadEvents, 10000 );
    setInterval(loadNextbus, 10000);
    setInterval(loadClock, 1000);

$(function(){
    loadNews();
    $("ul#newsticker").liScroll({travelocity: 0.05});
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
