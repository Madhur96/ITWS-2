var addLost = function(name,email,lquery)
{
	quer= 'lquery=' + lquery + '\&email=' + email;
	$.ajax({
		url: "http:127.0.0.1:5000/addLost",
		method: "POST",
		data: quer,
		success:function(response)
		{
			console.log(response)
		}
		error:function(xhr,response,err)
		{
			alert(response)
			console.log(response)
		}


	});	
}
var get_alllost=function()
{
    $.ajax({
    
    url: 'http://127.0.0.1:5000/get_all_lost',
    
    method: 'GET',
    
    dataType: "JSON",
    
    success:function(response)
    {
        
        var lo=response.SOMETHING;	
        
        var tble="";
         
         for (var i=0;i<lo.length;i++)
        {
                tble += "<tr>" + "<td>" + lo[i].SOMETHING + "</td>" + "<td>" + lo[i].SOMETHING + "</td>" + "<td>" + lo[i].SOMETHING + "</td>" + "</tr>";
        };
        
        $("#getalllost").html(tble);
        
        

        error:function(xhr,response,err)
        {
            alert(response);
            console.log(response);

        
        }
    });

};
var addLostbutton= function()
{
        var email = $('#email').val();

        var lquery = $("#lquery").val();

        var name = $("#name").val();
               
        addLost(name,email,lquery);
};


IN THE SAME WAY FOUND......