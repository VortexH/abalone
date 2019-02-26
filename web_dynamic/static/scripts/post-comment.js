$(document).ready(function(){
    $('#submit-comment').click(function(){
        let newComment = $('textarea.new-comment');
        let textVal = newComment.val();
        newComment.val("");
        $('#message-feed ul').append(`<li class="loaded-comment"><span class="username">Username: </span><span class="time">3:25:21</span><br><span class="message">${textVal}</span></li>`);
        console.log(textVal);
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
