function checkValid(){
var input = document.getElementById("id_title").value;

        if (input.trim() == '') {
            document.getElementById('title').style.transform= 'translateY(0)';
        } else {
            document.getElementById('title').style.transform = 'translateY(-40px)';
        }
}