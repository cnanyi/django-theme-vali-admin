/**
https://github.com/zyqwst/bootstrap-closable-tab
*/
var closableTab = {
    frameHeight: 400,
	//frame加载完成后设置父容器的高度，使iframe页面与父页面无缝对接
	frameLoad:function (frame){
       // $(frame).parent().height($("#content").height() -40);
	},
    //添加tab
	addTab:function(tabItem, change_callback){ //tabItem = {id,name,url,closable}  change_callback在标签更改时执行
		var id = "tab_seed_" + tabItem.id;
		var container ="tab_container_" + tabItem.id;
		$("li[id^=tab_seed_]").removeClass("active");
		$("div[id^=tab_container_]").removeClass("active");
		var needloadtab = false;
		if(!$('#'+id)[0]){
			var li_tab = '<li class="nav-item" id="'+id+'"><a href="#'+container+'" class="nav-link" data-toggle="tab" style="position: relative">'+tabItem.name;
			if(tabItem.closable){
				li_tab = li_tab + '<i class="glyphicon glyphicon-remove small" tabclose="'+id+'" style="left: 5px"  onclick="closableTab.closeTab(this)"></i></a></li> ';
			}else{
				li_tab = li_tab + '</a></li>';
			}
			$('.nav-tabs').append(li_tab);
			needloadtab = true;
		}
		if (tabItem.reload){
		    $("#"+container).remove();
		    needloadtab = true;
		}
		if (needloadtab){
            var tabpanel = '<div role="tabpanel" class="tab-pane" id="'+container+'" style="width: 100%;">'+
                                  '<iframe src="'+tabItem.url+'" id="tab_frame_'+tabItem.id+'" frameborder="0" style="overflow-x: hidden; overflow-y: hidden;width:100%;height: 100%"  onload="closableTab.frameLoad(this)"></iframe>'+
                               '</div>';
            $('.tab-content').append(tabpanel);
		}

		$("#"+id).addClass("active");
		$("#"+container).addClass("active");
		if (change_callback){
		    change_callback($("#"+id));
		}
		$("#"+id).click(function(){
            if (change_callback){
                change_callback($("#"+id));
            }
		});
	},
	//关闭tab
	closeTab:function(item){
		var val = $(item).attr('tabclose');
		var containerId = "tab_container_"+val.substring(9);
   	    if($('#'+containerId).hasClass('active')){
   	    	$('#'+val).prev().addClass('active');
   	    	$('#'+containerId).prev().addClass('active');
   	    }
		$("#"+val).remove();
		$("#"+containerId).remove();
	}
}