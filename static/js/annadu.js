$(".topnavbar .nav-link").on("click", function(){
    $(".nav").find(".active").removeClass("active");
    $(this).addClass("active");
 });
$(function() {
    $('.ir-colormapping').click(function(){
        $.ajax({
          url: '/runbackend',
          data:{
            colormapping: "True",
            image850: $('#850nm option:selected').val(),
            image950: $('#950nm option:selected').val()
          },
          dataType: 'JSON',
          type: 'GET',
          success: function(data){
            $("#result").html(data.result);
          }
          });
    });
    $('.ir-label').click(function(){
        labelfor = $(this).attr('for');
        imgfile = $('#'+labelfor+' option:selected').text()
        //url="/load?reqtype="+labelfor+"&imgfile="+imgfile
        //window.location.href = url;
        imgsrc = "static/img/"+labelfor+'/'+imgfile;
        $('#ir-image').attr('src', imgsrc);
        location.href = '#IRBased';
    });
    $('.color-based').click(function(){
        $.get('/runbackend', {color: $(this).text().toLowerCase()}, function(result) {
            location.href = '/#ColorBased';
        });
    });
    $('.morphology-btn').click(function(){
        data = {
            shape: $(this).text().toLowerCase(),
            imgfile: $('#selectshape option:selected').text()
        };
        $.get('/runbackend', data, function(result) {
            location.href = '/#MorphologyBased';
        });
    });
    $('.fluorescent-btn').click(function(){
        $('#others-image').attr('src', 'static/img/IMG_1768.jpg');
    });
    $('.uv-btn').click(function(){
        $('#others-image').attr('src', 'static/img/UV20181006.png');
    });
  });
