function switchActive(navlinkToActive) {
    $(".nav").find(".active").removeClass("active");
    navlinkToActive.addClass("active");
}

// Top navbar links switch active
$(".topnavbar .nav-link").on("click", function(){
//    $(".nav").find(".active").removeClass("active");
//    $(this).addClass("active");
    switchActive($(this));
 });
 // Left navbar links switch top navbar links active
 $(".left-navlink-main").on("click", function() {
    toActive = '#topnavbar' + this.id.substring(11);
    switchActive($(toActive));
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
            switchActive($('#topnavbar-ir'));
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
        switchActive($('#topnavbar-ir'));
        location.href = '#IRBased';
    });
    // color based buttons will run backend program with color param
    $('.color-based').click(function(){
        $.get('/runbackend', {color: $(this).text().toLowerCase()}, function(result) {
            switchActive($('#topnavbar-color'));
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
            switchActive($('#topnavbar-morphology'));
            location.href = '/#MorphologyBased';
        });
    });
    // fluorescent button loads the only image file
    $('.fluorescent-btn').click(function(){
        $('#verification-image').attr('src', 'static/img/IMG_1768.jpg');
        switchActive($('#topnavbar-verification'));
        location.href = '/#VerificationBased';
    });
    // uv button loads the only image file
    $('.uv-btn').click(function(){
        $('#verification-image').attr('src', 'static/img/UV20181006.png');
        switchActive($('#topnavbar-verification'));
        location.href = '/#VerificationBased';
    });
  });
