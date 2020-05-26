function clearForm(form_){
    var children = form_.children;
    for(var i=0;i<children.length;i++){
        if(children[i].hasAttribute('data-default-value')){
            children[i].value = children[i].dataset.defaultValue;
        }
    }
}