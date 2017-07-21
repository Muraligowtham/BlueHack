$(document).ready(function () {
    
     $.ajax({
     url: "http://127.0.0.1:8000/getYelpdetails/getdetails/",
       type: "GET",
        crossDomain: false,
     success: function( response ) {
         
         
    var res = response.split(";");
       console.info(res);
         var innerHtml="";
         for (i = 0; i < res.length; i++) { 
             
             if(res[i]!=""){
   innerHtml=innerHtml+"<img src="+res[i]+" width='300' height='300'></img>"
                 innerHtml=innerHtml+"<button  id="+res[i]+" value='Search'   onclick='myFunction(id)' >search</button><br/>"
             
             
             }
             
         }
         innerHtml.replace("undefined", "");
         $("#Photogrid").html(innerHtml); 
         
        }
  });
        
        
        
       



    
    
$('input').click(function () {
   alert('hjk');
        
 
    });


    
/*unction Search(input){
    
    alert('Hi');
     var xhttp = new XMLHttpRequest();
       
        console.log(input);
        url = "https://watson-api-explorer.mybluemix.net/visual-recognition/api/v3/classify?api_key=15f234085c0aff3a97d4a7906aebaa44535653a4&url=$$url&classifier_ids=food&version=2016-05-20";
        url = url.replace("$$url",input);
        console.log(url);
        xhttp.open("GET", url);
        xhttp.send();

        xhttp.onreadystatechange = function () {
            if (xhttp.readyState == 4) {
                eData = xhttp.responseText;
                if (xhttp.status == 200 && eData.length > 0) {
                    eventConsumerActionRuleData = JSON.parse(eData);
                }

                classes = eventConsumerActionRuleData.images[0].classifiers[0].classes;
                console.log(classes);
                maxScore = classes[0].score;
                item = classes[0].class;
               for(i = 0;i<classes.length;i++){
                   if(classes[i].score > maxScore){
                       item = classes[i].class;
                   }
               }
                console.log(item);
            }
        };
    
    
    
    
}; */


  

        
        
       
});