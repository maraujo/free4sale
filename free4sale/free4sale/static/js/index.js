$(document).ready(function(ev){
    $('#wanted_carousel').on('slide.bs.carousel', function (evt) {
      $('#wanted_carousel .controls li.active').removeClass('active');
      $('#wanted_carousel .controls li:eq('+$(evt.relatedTarget).index()+')').addClass('active');
    })
    $('#sale_carousel').on('slide.bs.carousel', function (evt) {
      $('#sale_carousel .controls li.active').removeClass('active');
      $('#sale_carousel .controls li:eq('+$(evt.relatedTarget).index()+')').addClass('active');
    })
});