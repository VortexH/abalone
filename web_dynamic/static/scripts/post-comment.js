$(document).ready(function(){
    let feed = $('#message-feed');
    $('#submit-comment').click(function(){
        let newComment = $('textarea.new-comment');
        let textVal = newComment.val();
        let time = new Date();
        let time_db = time.toLocaleString();
        let time_chat = time.toLocaleTimeString();
        feed.stop().animate({ scrollTop: feed[0].scrollHeight}, 1000);
        newComment.val("");
        $('#message-feed ul').append(`<li class="loaded-comment"><span class="username"><strong>Username:</strong> </span><span class="time">${time_chat}</span><br><span class="message">${textVal}</span></li>`);
        videoId = localStorage.getItem("video_id");
        dict = {[videoId]: ['user_name', textVal, time]}
        // alert(dict.videoId)
        $.ajax({
          url: 'https://abalone.holberton.us/api/submit_comment',
          dataType: 'json',
          crossDomain: true,
          type: 'post',
          contentType: 'application/json',
          data: JSON.stringify(dict),
          success: function(data, status) {}
        });
    });
    // Enable enter key to submit comment.
    $("textarea").keypress(function (e) {
        if(e.which == 13 && !e.shiftKey) {
            $('#submit-comment').click();
            e.preventDefault();
            return false;
        }
    });
});
