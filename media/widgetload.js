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
        var prev="";
        var dow="";
	    for (var key in events_json) {
        var na=events_json[key].timestamp.split(' ')
        if(na[0]!=prev){
            prev=na[0];
            if(prev=="Sun"){
                dow="sunday";
            }
            if(prev=="Mon"){
                dow="monday";
            }
            if(prev=="Tue"){
                dow="tuesday";
            }
            if(prev=="Wed"){
                dow="wednesday";
            }
            if(prev=="Thu"){
                dow="thursday";
            }
            if(prev=="Fri"){
                dow="friday";
            }
            if(prev=="Sat"){
                dow="saturday";
            }
		    $("#eventlist").append("<p class='dow'>" + dow + " events</p>");
        }
		$("#eventlist").append("<li><time>" +na[1].replace('a', 'am').replace('p', 'pm')+" </time> " +events_json[key].title+ "</li>");
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
	},
	async: true
    });    
}

function loadClock(){
    var time = new Date ();
    var hours=time.getHours();
    var mins=time.getMinutes();
    var months=new Array("january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december");
    var month=months[time.getMonth()];
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
    $("#newclock").html('<p class="date">'+month+' '+time.getDay()+', '+(time.getYear()+1900)+'</p><time>'+hours+":"+mins+'</time><m> '+M+'</m>');

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
    loadCalendar();
    loadEvents();
    loadEvents2();
    loadNextbus();
    loadClock();
    setInterval(loadCalendar, 60000 );
    setInterval(loadEvents, 10000 );
    setInterval(loadEvents2, 10000 );
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
