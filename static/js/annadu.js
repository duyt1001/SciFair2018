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
        url="/load?reqtype="+labelfor+"&imgfile="+imgfile
        window.location.href = url;
    });
    $('.fluorescent-btn').click(function(){
        url="/load?reqtype="+"&imgfile="
        window.location.href = url;
    });
    $('.uv-btn').click(function(){
        url="/load?reqtype="+"&imgfile="
        window.location.href = url;
    });
  });
