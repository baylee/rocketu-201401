/**
 * Created by baylee on 2/28/14.
 */
$(function() {
   $('#hello').on('click', function(){
       $.ajax({
           url: "/ajaxiness",
           success: function(result){
               $('#hello').append(result);
           }
       });
   });

    $('#give_me_more_information').on('click', function(){
       $.ajax({
           url: "/more_information",
           success: function(result){
               $('body').append(result);
           }
       });
    });
});