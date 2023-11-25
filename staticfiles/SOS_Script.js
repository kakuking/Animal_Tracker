SOS_button = document.getElementById("SOSButton");
var beep;

function sendSOS(){
    if(!beep || beep.paused){
        beep = new Audio('{% static "loud_beep.mp3" %}');
        beep.loop = true;
        beep.play();

        SOS_button.classList.add("flashingButton");
    }else{
        beep.pause();
        SOS_button.classList.remove("flashingButton");
    }
}