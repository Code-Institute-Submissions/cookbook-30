$(document).ready(function(){
    /* Side navigation opens to the right */
    $('.sidenav').sidenav({edge: "right"});
    /* Materialize's Tag jQuery to create custom and placeholder */
    $('.chips').chips();
    $('.chips-placeholder').chips({
            placeholder: 'Enter recipe tags',
            secondaryPlaceholder: '+ Tag'
        });
    /* Scroll effect on items with class 'fadeIn' */
    $(window).scroll(function () {
        $(".fadeIn").each(function (i) {
        $(this)
            .delay(i * 1000)
            .fadeIn(1000);
        });
    });
   
});
