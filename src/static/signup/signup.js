let email = document.getElementById('email');
let password = document.getElementById('password');
let passwordConf = document.getElementById('passwordConf');

function init(){
    document.getElementById('id_password').type = 'password';
}

function submit(){
    document.getElementById('id_email').value = email.value;
    if (email.value == ''){
        document.getElementById('noEmailErr').style.display = 'block';

    }
    else if(password.value == ''){
        document.getElementById('noPassErr').style.display = 'block';
    }
    else if (password.value == passwordConf.value){
        document.getElementById('id_password').value = password.value;
        document.getElementById('form').submit();
    }
    else{
        document.getElementById('passErr').style.display = 'block';
    }

}