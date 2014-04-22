$(document).ready(iniciar)
function iniciar()
{	
	$("table#1 tr:first").css("font-weight","bold");
	$("table#1 tr:first").css("background-color","#003");
	$("table#1 tr:first").css('color','white');
	
	$("table#1 tr").each(function (x) {
	if (x==2|| x==1)
	$(this).css("font-weight","bold");
	});
	
}