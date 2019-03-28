$(document).ready(function(){

    function check(Form_Name, password,confirm_password)
    {
        var pass1 = document.getElementById(password).value;
        var pass2 = document.getElementById(confirm_password).value;
        if(pass2 != pass1){

            M.toast({html: 'Password Doesnt Match.'})
            return false;
        }

    }

    $('.tabs').tabs({swipeable: false});
    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    $(".dropdown-trigger").dropdown({hover:true});
});