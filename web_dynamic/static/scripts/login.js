(document).ready(function(){
    let feed = $('#login-form');
    $('#submit-login').click(function(){
        let username = $('form');
        let textVal = newComment.val();
        let time = new Date();
        let time_db = String(time.toLocaleString());
        let time_chat = time.toLocaleTimeString();
        feed.stop().animate({ scrollTop: feed[0].scrollHeight}, 1000);
        newComment.val("");
        $('#message-feed ul').append(`<li class="loaded-comment"><span class="username"><strong>Username:</strong> </span><span class="time">${time_chat}</span><br><span class="message">${textVal}</span></li>`);
        videoId = localStorage.getItem('video_id');
        dict = {videoId: ['user_name', textVal, time_db]}
       $.ajax({
             url: 'https://abalone.holberton.us/api/submit_comment',
             dataType: 'json',
             type: 'post',
             contentType: 'application/json',
             data: JSON.stringify(dict),
         success: function(data) {}
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
