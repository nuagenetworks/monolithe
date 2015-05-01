var FILTERABLE_CACHE = {};

function generate_filterable_cache()
{
    var filterables = $(".filterable");

    for (var i = 0; i < filterables.length; i++)
    {
        var keyword     = $(filterables[i]).attr("data-filter-keyword");
            list_item   = $("<li role='presentation'>"),
            anchor_item = $("<a role='menuitem'>" + keyword + "</a>");

        list_item.append(anchor_item);

        FILTERABLE_CACHE[keyword] = list_item;
    }
}

function initialize_search(id_prefix)
{
    generate_filterable_cache();

    var searchfield = $('#searchfield');

    searchfield.on('keyup', function() {

        var filter       = $(this).val(),
            searchResult = $("#searchresult");

        searchResult.empty();
        searchResult.css("display", "none");

        if (filter.length < 2)
            return;

        $.each(FILTERABLE_CACHE, function(keyword, item){

            if (keyword.match("^" + filter))
            {
                item.click(function() {
                    $("html,body").animate({scrollTop: $("#" + id_prefix + keyword).offset().top - 60}, 300);
                    searchResult.css("display", "none");
                    searchfield.val(keyword);
                })
                searchResult.append(item);
            }
        });

        searchResult.css("display", searchResult.children().length ? "block" : "none");
    });
}

function initialize_scrollspy()
{
    $("body").scrollspy({target:"#navbarmain", offset: 0});

    $("#navbarmain li a[data-id]").click(function(event) {
        $("html,body").animate({scrollTop: $("#" + $(this).attr("data-id")).offset().top}, 300);
        return false;
    });
}
