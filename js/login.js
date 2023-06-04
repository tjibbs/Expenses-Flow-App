  window.console = window.console || function(t) {};

  if (document.location.search.match(/type=embed/gi)) {
    window.parent.postMessage("resize", "*");
  }

$(function () {
  $("#loaded").html("Login");
  var images = ['img/bg2.jpg', 'img/landingbg.jpg'];

  $('#container').append('<style>#container, .acceptContainer:before, #logoContainer:before {background: url(' + images[Math.floor(Math.random() * images.length)] + ') center fixed }');




  setTimeout(function () {
    $('.logoContainer').transition({ scale: 1 }, 700, 'ease');
    setTimeout(function () {
      $('.logoContainer .logo').addClass('loadIn');
      setTimeout(function () {
        $('.logoContainer .text').addClass('loadIn');
        setTimeout(function () {
          $('.acceptContainer').transition({ height: '431.5px' });
          setTimeout(function () {
            $('.acceptContainer').addClass('loadIn');
            setTimeout(function () {
              $('.formDiv, form h1').addClass('loadIn');
            }, 500);
          }, 500);
        }, 500);
      }, 500);
    }, 1000);
  }, 10);
});

$("#submit").click(function(){
    $("#loaded").html("<i class='fa fa-spinner  fa-spin' style='font-size:48px;color:white'>");
    var uname=$("#uid").val();
    var pwd=$("#pwd").val();
    $.post("adconnect.php",
    {
      submit:1,
      uid:uname,
      pwd:pwd
    },function(data,status){
          if(data=="Successful"){
            window.location.assign("home.py");
          }else{
            $('#msg').html(data);
            $("#loaded").html("Login");
          }
    })
  });
