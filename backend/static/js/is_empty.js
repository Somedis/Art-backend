function checkValid(){
    var input = document.getElementById("id_email").value;
    var emailText = document.getElementById('emailText');

        if (input.trim() == '') {
            emailText.style.transform= '';
        } else {
            emailText.style.transform = 'translate3d(0, -175%, 0)';
        }
}