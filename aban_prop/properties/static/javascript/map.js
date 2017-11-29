<div id="map"></div>
    <script>
      var map;
      function initMap() {
        map = new google.maps.Map(document.getElementById('map'), {
          zoom: 5,
          center: new google.maps.LatLng(0,0),
          mapTypeId: 'terrain'
        });
        
      }
     </script>

     <script type="text/javascript" src="http://code.jquery.com/jquery-latest.min.js"></script>  
    <script type="text/javascript">
      $(document).ready(function() {
        $.getJSON("http://127.0.0.1:8000/propertieslist/?format=json", function(json1) {
          
          
          $.each(json1, function(key, data) {
            var latLng = new google.maps.LatLng(data.lat, data.lon); 
            // Creating a marker and putting it on the map
            
            var marker = new google.maps.Marker({
                position: latLng,
                title: data.title
            });    

            var contentString = data.title;

          var infowindow = new google.maps.InfoWindow({
            content: contentString
          });

          marker.addListener('click', function() {
            infowindow.open(map, marker);
          });


            marker.setMap(map);
          });
        });
      });
    </script>

    <script src="https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/markerclusterer.js">
    </script>
    <script async defer
    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBiB5iKNfCbMFqX70ULP039rt1QZV1zs0s&callback=initMap">
    </script>
