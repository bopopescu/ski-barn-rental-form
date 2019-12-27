let address = document.getElementById('address');
let city = document.getElementById('city');
let state = document.getElementById('state');
let zipCode = document.getElementById('zipCode');
let phone = document.getElementById('phone');
 
function next(){
    document.getElementById('id_address').value = address.value;
    document.getElementById('id_city').value = city.value;
    document.getElementById('id_state').value = state.value;
    document.getElementById('id_zipCode').value = zipCode.value;
    document.getElementById('id_phone').value = phone.value;
    document.getElementById('secondaryInfo').style.display = 'none';
    document.getElementById('locations').style.display = 'grid';
}

function enter(){
    document.getElementById('form').submit();
}

function submit(location){
    document.getElementById('id_location').value = location;
    enter()
}
