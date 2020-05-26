function responseHandler(commentId, name){
    var parent = document.getElementsByName('parent_id')[0];
    var body = document.getElementsByName('body')[0];
    parent.value = commentId;
    body.value = name + ', ';
}