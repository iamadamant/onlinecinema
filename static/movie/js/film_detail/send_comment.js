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
            var comment = `<div  style="display: flex; margin-left: 20px; margin-top: 20px" class="comment">
            <div style="width: 25%">
                <img src="http://localhost:8000/static/movie/images/account_comment.png" alt="account">
                <a style="margin: 10px" class="author" onclick="responseHandler(${key}, this.innerText)">${without_parent[i].fields.author[1]}</a>
            </div>
            <div style="width: 75%">
              <p class="m-4">${without_parent[i].fields.body}</p>
            </div>
        </div>`;
            var childrenObjects = comments.filter(i=>i.fields.parent==key);
            children[comment] = [];
            for(var j=0;j<childrenObjects.length;j++){
                children[comment].push(`<div  style="display: flex; margin-left: 70px;" class="comment">
                <div style="width: 26%">
                <img src="http://localhost:8000/static/movie/images/account_comment.png" alt="account">
                <a style="margin: 10px">${childrenObjects[j].fields.author[1]}</a>
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
            var commentHtml = '<div>' + key + children[key] + '</div>';
            commentsHtml += commentHtml;
        }
        panel.innerHTML = commentsHtml;
    }

    function getParent(){
        var parent = document.getElementsByName('parent_id')[0];
        if(parent != undefined){
            return parent.value;
        }
        else{
            return null;
        }
    }

    function sendComment(ev){
        ev.preventDefault();
        var text = document.getElementById('text');
        var hasError = checkError(text.value);
        if (hasError){
            alert('Text can not contains html tags!');
            return;
        }
        var url = document.getElementsByName('url')[0].value;
        var request = new XMLHttpRequest();
        var body = 'body=' + text.value;
        var parent = getParent();
        if(parent != null){
            body+='&parent='+parent;
        }
        var csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value;
        request.open('PUT',  url);
        request.setRequestHeader("X-CSRFToken", csrf);
        request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
        request.send(body);
        request.addEventListener('readystatechange', ()=>{
            if(request.readyState == 4){
                updateComment(request.responseText);
            }
        });
    }

    function checkError(text){
        var pattern = new RegExp("^[0-9a-zA-Zа-яА-ЯёЁ \-:;.,()]+$");
        if (pattern.test(text)){
            return false;
        }
        return true;
    }
