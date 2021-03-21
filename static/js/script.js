$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('.chips').chips();
        $('.chips-placeholder').chips({
                placeholder: 'Enter recipe tags',
                secondaryPlaceholder: '+Tag',
        });
     
});