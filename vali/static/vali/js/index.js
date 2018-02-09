(function () {
	"use strict";

	var treeviewMenu = $('.app-menu');

	// Toggle Sidebar
	$('[data-toggle="sidebar"]').click(function(event) {
		event.preventDefault();
		$('.app').toggleClass('sidenav-toggled');
	});

	// Activate sidebar treeview toggle
	$("[data-toggle='treeview']").click(function(event) {
		event.preventDefault();
		if(!$(this).parent().hasClass('is-expanded')) {
			treeviewMenu.find("[data-toggle='treeview']").parent().removeClass('is-expanded');
		}
		$(this).parent().toggleClass('is-expanded');
	});

	// Set initial active toggle
	$("[data-toggle='treeview.'].is-expanded").parent().toggleClass('is-expanded');

	//Activate bootstrip tooltips
	$("[data-toggle='tooltip']").tooltip();
    $('.nav-tabs').width($('#pages').width()-17);
})();
function setCookie(c_name,value,expiredays)
{
    var exdate=new Date();
    exdate.setDate(exdate.getDate()+expiredays);
    document.cookie=c_name+ "=" +escape(value)+((expiredays==null) ? "" : ";expires="+exdate.toGMTString());
};
function getCookie(c_name)
{
    if (document.cookie.length>0)
    {
        c_start=document.cookie.indexOf(c_name + "=");
        if (c_start!=-1)
        {
            c_start=c_start + c_name.length+1;
            c_end=document.cookie.indexOf(";",c_start);
            if (c_end==-1) c_end=document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
};
function bodyscroll(){
    var activeframes = $(".tab-pane.active iframe");
    var tp = document.body.scrollTop;
    if (activeframes.length == 1) {
        //var tab =  document.getElementsByClassName('nav-tabs');
        var tabHeightFix = 0;
        //if (tab.length > 0 ){ tabHeightFix = tab[0].clientHeight - 38; }
        var content = activeframes[0].contentDocument;
        var apptitle = content.getElementsByClassName("app-title");
        var wintool = content.getElementsByClassName("formtoolbox");
        $(apptitle).css("top", (tp+tabHeightFix)+"px");
        $(wintool).css("top", tp+tabHeightFix+"px");
    }
};