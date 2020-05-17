    var form = document.getElementById('com-for');
    form.addEventListener(
        'submit', sendComment, false
    );


    function updateComment(json_text){
        try{
            var comments = JSON.parse(json_text);
        }
        catch{}
        var without_parent = comments.filter(item=>item.fields.parent==null);
        var children = {};
        for(var i=0; i<without_parent.length; i++){
            var key = without_parent[i].pk;
            var comment = `<div  style="display: flex; margin-left: 20px; margin-top: 20px;">
            <div style="width: 25%">
                <img src="http://localhost:8000/static/movie/images/account_comment.png" alt="account">
                <p style="margin 10px">${without_parent[i].fields.author}</p>
            </div>
            <div style="width: 75%">
              <p class="m-4">${without_parent[i].fields.body}</p>
            </div>
        </div>`;
            var childrenObjects = comments.filter(i=>i.fields.parent==key);
            children[comment] = [];
            for(var j=0;j<childrenObjects.length;j++){
                children[comment].push(`<div  style="display: flex; margin-left: 70px;">
                <div style="width: 26%">
                <img src="http://localhost:8000/static/movie/images/account_comment.png" alt="account">
                <p style="margin 10px">${childrenObjects[j].fields.author}</p>
                </div>
                <div style="width: 75%">
                <p class="m-4">${childrenObjects[j].fields.body}</p>
                </div>
                </div>`);
            }
        }

        var panel = document.getElementById('panel');
        var commentsHtml = '';
        for(var key in children){
            var commentHtml = '<div class="comment">' + key + children[key] + '</div>';
            commentsHtml += commentHtml;
        }
        panel.innerHTML = commentsHtml;
    }

    function sendComment(ev){
        ev.preventDefault();
        var text = document.getElementById('text');
        var url = document.getElementsByName('url')[0].value;
        var request = new XMLHttpRequest();
        var body = 'body=' + text.value;
        var csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value;
        request.open('POST',  url);
        request.setRequestHeader("X-CSRFToken", csrf);
        request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
        request.send(body);
        request.addEventListener('readystatechange', ()=>{
            if(request.readyState == 4){
                updateComment(request.responseText);
            }

        });
    }
