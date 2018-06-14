(function () {
    $('[data-toggle="sidebar"]').click(function(event) {
        if ($('.object-tools').hasClass('object-tools-mr')){
            $('.object-tools').animate({'margin-right': '3%'});
        }else{
            $('.object-tools').animate({'margin-right': '16%'});
        }
        $('.object-tools').toggleClass('object-tools-mr');
    });

})();