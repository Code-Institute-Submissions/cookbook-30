$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('.chips').chips();
    $('.chips-placeholder').chips({
            placeholder: 'Enter recipe tags',
            secondaryPlaceholder: '+ Tag'
        });
    $('.slider').slider();
    $(window).scroll(function () {
        $(".fadeIn").each(function (i) {
        $(this)
            .delay(i * 1000)
            .fadeIn(1000);
        });
    });
   
});
