ymaps.ready(init);

function init() {
    var myMap = new ymaps.Map("map", {
            center: [55, 37],
            zoom: 5
        }, 
        {
            searchControlProvider: 'yandex#search'
        });
     
        var myClusterer = new ymaps.Clusterer();

        $(document).ready(function() {
            $.getJSON("http://127.0.0.1:8000/propertieslist/?format=json", function(json1) {
              
              
              $.each(json1, function(key, data) {
                point = new ymaps.GeoObject({
                // The geometry description.
                geometry: {
                    type: "Point",
                    coordinates: [data.lon, data.lat]
                },
                // Properties.
                properties: {
                    // The placemark content.
                    iconContent: data.title,
                    clusterCaption: data.id,
                    balloonContentHeader: ['<img width="100px" height="100px" src="http://127.0.0.1:8000/',data.image ,"\">"].join(""),
                    balloonContentBody: ['<p>',"<font size=3><b><a target='_blank' href='", 'http://127.0.0.1:8000/properties/details/', data.id ,"'>", data.title,"</a></b></font>", '</p>',
                                         '<p>','Address: ', data.address, '</p>',
                                        
                                        data.description].join(""),
                }
                }, 
                {
                /**
                 * Options.
                 * The placemark's icon will stretch to fit its contents.
                 */
                preset: 'islands#blackStretchyIcon',
                // The placemark can be dragged.
                draggable: false
                }),
                myMap.geoObjects.add(point);
                myClusterer.add(point);
              });
            });
        });
        myMap.geoObjects.add(myClusterer);
}
