$(document).ready(function() {
  $(".table-row").click(function() {
    window.document.location = $(this).data("href");

  });
});
//class="table-row" data-href="/loadapi/matches/{{match.match_id}}