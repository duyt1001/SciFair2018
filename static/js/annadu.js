// Top navbar links switch active
$(".topnavbar .nav-link").on("click", function(){
    $(".nav").find(".active").removeClass("active");
    $(this).addClass("active");
 });
$(function() {
    // color mapping code here is NOT used!
    $('.ircolormapping').click(function(){
        data = {
            ircolormapping: "True",
            select850: $('#850nm option:selected').val(),
            select950: $('#950nm option:selected').val()
        };
        $.get('/runbackend', data, function(result) {
            var seconds = Math.round(new Date() / 1000); // force reloading by random string
            $('#ir-image').attr('src', 'static/img/compare-850-950.png?' + seconds);
            location.href = '#IRBased';
        });
    });
    // Each label next to select box will load the picture
    $('.ir-label').click(function(){
        labelfor = $(this).attr('for');
        imgfile = $('#'+labelfor+' option:selected').text()
        //url="/load?reqtype="+labelfor+"&imgfile="+imgfile
        //window.location.href = url;
        imgsrc = "static/img/"+labelfor+'/'+imgfile;
        $('#ir-image').attr('src', imgsrc);
        location.href = '#IRBased';
    });
    // color based buttons will run backend program with color param
    $('.color-based').click(function(){
        $.get('/runbackend', {color: $(this).text().toLowerCase()}, function(result) {
            location.href = '/#ColorBased';
        });
    });
    // morphology buttons will run backend program with shape and choosen image
    $('.morphology-btn').click(function(){
        data = {
            shape: $(this).text().toLowerCase(),
            imgfile: $('#selectshape option:selected').text()
        };
        $.get('/runbackend', data, function(result) {
            location.href = '/#MorphologyBased';
        });
    });
    // fluorescent button loads the only image file
    $('.fluorescent-btn').click(function(){
        $('#others-image').attr('src', 'static/img/IMG_1768.jpg');
    });
    // uv button loads the only image file
    $('.uv-btn').click(function(){
        $('#others-image').attr('src', 'static/img/UV20181006.png');
    });
  });
