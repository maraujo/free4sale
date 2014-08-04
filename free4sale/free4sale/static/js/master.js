
function closeMessages(){
    $.each($(".alert"), function(index, val) {
         $(val).hide();
    });
}

function getUrlParameters(parameter){
   /*
    Function: getUrlParameters
    Description: Get the value of URL parameters either from 
                 current URL or static URL
    Author: Tirumal
    URL: www.code-tricks.com
   */
   staticURL = document.URL
   decode = true;
   var currLocation = (staticURL.length)? staticURL : window.location.search,
       parArr = currLocation.split("?")[1].split("&"),
       returnBool = true;
   
   for(var i = 0; i < parArr.length; i++){
        parr = parArr[i].split("=");
        if(parr[0] == parameter){
            parr[1] = parr[1].split("+").join(" ")
            return (decode) ? decodeURIComponent(parr[1]) : parr[1];
            returnBool = true;
        }else{
            returnBool = false;            
        }
   }
   
   if(!returnBool) return false;  
}

$(document).ready(function(){

    //Check logged.
    $.get('/islogged', function(data) {
        if(data.logged){
            $("#logged").addClass('show');
            $("#user_name").html(data.logged);
            $("#signin_link").addClass('hidden');
            $("#signup_link").addClass('hidden');
            $("#logout").addClass('show');
            $("#profile_link").addClass('show');   
        }
        else{
            $("#logout_link").addClass('hidden');   
            $("#profile_link").addClass('hidden');   
            $("#logged").addClass('hidden');   
        }
    });

    //Chack Message
    if(getUrlParameters("msg_show")){
        type = getUrlParameters("msg_type");
        switch(type){
            case "success":
                $("#alert_success").fadeIn();
                break;
            case "warning":
                $("#alert_warning").fadeIn();
                break;
            case "danger":
                $("#alert_danger").fadeIn();
                break
        }
        $(".alert_text").html(getUrlParameters("msg_text"));
    }


    //MENU

    $('[data-toggle=offcanvas]').click(function() {
    $('.row-offcanvas').toggleClass('active');
  });
      $('#radioBtn a').on('click', function(){
        var sel = $(this).data('title');
        var tog = $(this).data('toggle');
        $('#'+tog).prop('value', sel);
        
        $('a[data-toggle="'+tog+'"]').not('[data-title="'+sel+'"]').removeClass('active').addClass('notActive');
        $('a[data-toggle="'+tog+'"][data-title="'+sel+'"]').removeClass('notActive').addClass('active');
    })   
    $("#menu-toggle").click(function(e) {
        e.preventDefault();
        $("#wrapper").toggleClass("toggled");
    }); 




});
