$(document).ready(function(){
    $('#submit-video').click(function(){
        let searchText = $('#search-input');
        let videoId = searchText.val();
        localStorage.clear();
        localStorage.setItem("video_id", videoId);
        searchText.val("");
        console.log(videoId);
        $.getJSON('https://www.googleapis.com/youtube/v3/videos?id=' + videoId + '&key=AIzaSyArpdRTVCbPHEpMBZdW2sl9btD5igbul0E&part=status,statistics,snippet', function (video) {
        	try {
        		if (video.items[0].status.embeddable) { $('.video-container').append(`<iframe
width="640" height="360"src="https://www.youtube.com/embed/${videoId}">
</iframe> `);
                    let likeCount = video.items[0].statistics.likeCount;
                    let viewCount = video.items[0].statistics.viewCount;
                    let title = video.items[0].snippet.title;
                    let description = video.items[0].snippet.description;
                    $('.stats_body').html(`<br />Title: ${title}<br /><br />`);
                    $('.stats_body').append(`<strong>Description:</strong> ${description}<br /><br />`);
                    $('.stats_body').append(`<b>Views:</b> ${viewCount}<br /><br />`);
                    $('.stats_body').append(`<b>Likes:</b> ${likeCount}<br /><br />`);
              $.get('https://abalone.holberton.us/api/get_comments/' + String(videoId), function(status) {
              });
        		} else {
        			throw "bad";
        		}
        	}
        	catch {
        		alert("Invalid link");
        	}
        });
    });
    // Enable enter key to submit comment.
    $('#search-bar').keypress(function (e) {
        if(e.which == 13 && !e.shiftKey) {
            $('#submit-video').click();
            e.preventDefault();
            return false;
        }
    });
});
