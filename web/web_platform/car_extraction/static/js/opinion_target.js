$(function(){
			$('.left > textarea').focus(); // 页面加载完毕后将焦点交给左侧框

			$('#analysis').click(function() { // 处理分词请求

				if( $(".left > textarea").val() == "" ) {
				    //alert("")
					//$('#notice').text("待分语句不能为空!").show(100);
					//setTimeout(hideNotice, 3000);
					return; // 如果左侧框为空就不处理并弹提示
				} // end if

                /*
				if( isNaN( $('#p1').val() ) || parseFloat($('#p1').val()) < 0 || parseFloat( $('#p1').val() ) > 1 ) {
					$('#notice').text("出词概率必填且必须是0-1之间!").show(100);
					setTimeout(hideNotice, 3000);
					return; // 如果不是数字就不处理并弹提示
				} // end if
                */

				$.ajax({ // 向服务器发出 POST 分词请求
					type : "post",
					url : "/analysis/segmentation/",  // 这里是处理 POST 分词请求的目的地址，请务必按需要来改!!!
					data : {content:$(".left > textarea").val()},
					// 序列化结果是：source=待分句子&param1=第一个数&param2=第二个，$_POST['source']、$_POST['param1']这样接收皆可
					async : false, 
					success : function(data){ // 这里直接返回分完的结果纯文本data，如果是json的话请先解析再赋给右侧框
						if(data.status==0){
							result = parse_to_html(data.data);
						    //$('.right > textarea').html(result);
						    $('.show_').html(result);
						    
						}else{
						    alert(data.info);
						}
					},
					error : function(XMLHttpRequest, textStatus, errorThrown) {
					    alert("服务器资源错误，请稍后再试。");
						//$('#notice').text("处理请求失败!").show(100);
						//setTimeout(hideNotice, 3000);
					}
				});
			});

			//解析返回数组，并标红
			function parse_to_html(arr2v){
				var content = ""
				for(var i in arr2v){
					
					if(arr2v[i][1]=='B'){
						content += "<font color='red'>";
						content += arr2v[i][0];
						content += '</font> '

					}else{
						content += arr2v[i][0]+' ';
					}

					//console.log(content[i]);
				}
				console.log(content);
				return content;
				//console.log(content)
			}


		});
