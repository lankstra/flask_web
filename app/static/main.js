$(function() {
    $(".navbar-collapse").find("li").each(function () {
        var a = $(this).find("a:first")[0];
        if ($(a).attr("href") === location.pathname) {
            $(this).addClass("active");
        } else {
            $(this).removeClass("active");
        }
    });

    // if (!navigator.userAgent.toLowerCase().match('mobile')) {
        $(window).scroll(function() {
            if ($(window).scrollTop() > 300)
                $('div.go-top').show();
            else
                $('div.go-top').hide();
        });
        $('div.go-top').click(function() {
            $('html, body').animate({scrollTop: 0}, 500);
        });
    // }
});
