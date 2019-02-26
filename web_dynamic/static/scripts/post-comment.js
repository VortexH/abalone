$(document).ready(function(){
    let feed = $('#message-feed');
    $('#submit-comment').click(function(){
        let newComment = $('textarea.new-comment');
        let textVal = newComment.val();
        feed.stop().animate({ scrollTop: feed[0].scrollHeight}, 1000);
        newComment.val("");
        $('#message-feed ul').append(`<li class="loaded-comment"><span class="username">Username: </span><span class="time">3:25:21</span><br><span class="message">${textVal}</span></li>`);

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
