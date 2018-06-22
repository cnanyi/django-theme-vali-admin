(function () {
    $('[data-toggle="sidebar"]').click(function(event) {
        if ($('.object-tools').hasClass('object-tools-mr')){
            $('.object-tools').animate({'margin-right': '3%'});
        }else{
            $('.object-tools').animate({'margin-right': '16%'});
        }
        $('.object-tools').toggleClass('object-tools-mr');
    });
    if ($('.vali-multicheckbox').length > 0){
        $('.vali-multicheckbox li').addClass('list-group-item');
        // ul
        $('.vali-multicheckbox').each(function(){
            // li
            var inputs = {};
            $(this).children().each(function(){
                var lbl = $(this).find('label');
                if (lbl.length > 0){
                    var txts = lbl.text().trim().split('|');
                    // app | model | permissions
                    if (txts.length  == 3){
                        var appname = txts[0].trim();
                        var modelname = txts[1].trim();
                        var permission = txts[2].trim();
                        //lbl.text(permission);
                        if (appname in inputs){
                            if (modelname in inputs[appname]){
                                inputs[appname][modelname].push(lbl);
                            }else{
                                //
                            }
                        }else{
                            inputs[appname] = {};
                            inputs[appname][modelname] = [lbl];
                        }
                    }
                }
            });

            var html = "";
            for (var key in inputs) {
                html += '<li class="list-group-item"><div class="row"><span class="col-3">'+key+'</span>';
                for (var mkey in inputs[key]){
                    html += '<div class="col-9 row"><span class="col">'+mkey+'</span>';
                    inputs[key][mkey].sort();
                    for (var inputkey in inputs[key][mkey]){
                        html += '<div class="col">'+ inputs[key][mkey][inputkey].prop('outerHTML')+'</div>';
                    }
                    html += '</div>';
                }
                html += '</div></li>';
            }
            $(this).children().remove();
            $(this).html(html);
        });
    }
})();