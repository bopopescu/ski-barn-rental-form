function selectRenter(fullName){
    document.getElementById('id_renter').value = fullName;
    document.getElementById('renterSelect').style.display = 'none';
    document.getElementById('renterDesc').style.display = 'grid';
}

function Next(){
    if(document.getElementById('weight').value !== ''){
    document.getElementById('id_height_inches').value = document.getElementById('height').value;
    document.getElementById('id_weight').value = document.getElementById('weight').value;
    document.getElementById('renterDesc').style.display = 'none';
    document.getElementById('using').style.display = 'grid';
    }
}

function use(using){
    if(using == 1){
        document.getElementById('id_using').value = 'True';
        document.getElementById('id_stance').value = -1;
        document.getElementById('skiStance').style.display = 'grid';
    }
    else{
        document.getElementById('id_using').value = 'False';
        document.getElementById('id_ski_type').value = 0;
        document.getElementById('boardStance').style.display = 'grid';
    }
    document.getElementById('using').style.display = 'none';
}

function type(s){
        document.getElementById('id_ski_type').value = s;
        document.getElementById('form').submit();
}

function stance(s){
    if(s == 'g'){
        document.getElementById('id_stance').value = '0';
    }
    else{
        document.getElementById('id_stance').value = '1';
    }
    document.getElementById('form').submit();
}