$(document).ready(function(){
    $('#submit-video').click(function(){
        let searchText = $('#search-input');
        let videoId = searchText.val();
        localStorage.clear();
        localStorage.setItem("video_id", videoId);
        searchText.val("");
        console.log(videoId);
        $.getJSON('https://www.googleapis.com/youtube/v3/videos?id=' + videoId + '&key=AIzaSyArpdRTVCbPHEpMBZdW2sl9btD5igbul0E&part=status,statistics', function (video) {
        	try {
        		if (video.items[0].status.embeddable) { $('.video-container').append(`<iframe width="640" height="360"src="https://www.youtube.com/embed/${videoId}"></iframe> `);
                let like_count = video.items[0].statistics
                $.get('https://abalone.holberton.us/api/get_comments/' + String(videoId), function(status) {});
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
