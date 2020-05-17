var form = document.getElementById('com-for');
form.addEventListener(
   'submit', sayError, false
);


function sayError(ev){
    ev.preventDefault();
    alert("You must be authenticate!");
}


