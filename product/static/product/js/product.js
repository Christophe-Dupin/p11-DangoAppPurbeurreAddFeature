$(function () {
    $(".search_id").autocomplete({
        source: "product/autocomplete",
        minLength: 2

    });
});