$(function () {
  $(".tab").click(function () {
    var tab = $(this).data("tab");
    $(".tab").removeClass("active");
    $(this).addClass("active");

    $(".tab-content").hide();
    $("#" + tab + "-tab").show();
  });

  var algoritmo_post = "{{ request.form.get('algoritmo') }}";
  if (algoritmo_post) {
    $(".tab").removeClass("active");
    $('.tab[data-tab="' + algoritmo_post + '"]').addClass("active");
    $(".tab-content").hide();
    $("#" + algoritmo_post + "-tab").show();
  }
});
