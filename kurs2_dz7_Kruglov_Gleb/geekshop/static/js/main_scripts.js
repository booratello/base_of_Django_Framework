$( document ).on( 'click', '.our_gallery a', function(event) {
   if (event.target.hasAttribute('href')) {
       var link = event.target.href + 'ajax/';
       var link_array = link.split('/');
       if (link_array[4] == 'category') {
           $.ajax({
               url: link,
               success: function (data) {
                   $('.our_gallery').html(data.result);
               },
           });

           event.preventDefault();
       }
   }
});