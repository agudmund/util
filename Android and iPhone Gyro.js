function load_model(urlid){
    var iframe = document.getElementById( 'api-frame' );
    var version = '1.0.0';
    var client = new Sketchfab( version, iframe );

    client.init( urlid, {
        success: function onSuccess( api ){ console.log( 'Model loaded successfully' );
        error: function onError(callback){ console.log(this.error ) };
        api.load();
        api.start();

        api.addEventListener('viewerready', function() 
                {
                    let $apiFrame = document.getElementById("api-frame");
                    $apiFrame.classList.remove("hidden");
                    console.log( 'Viewer is ready');
                });
        
        window.ondevicemotion = function(event) {
            var accelerationX = Math.round(event.accelerationIncludingGravity.x * 1)/1
            var accelerationY = Math.round(event.accelerationIncludingGravity.y * 1)/1
            var accelerationZ = Math.round(event.accelerationIncludingGravity.z * 1)/1

            var zoom = 11.6
            var Xcoord = (1.1 - accelerationX).toFixed(0)
            var Ycoord = (5.6 + accelerationY).toFixed(0)

            if (Xcoord>5){
                Xcoord = (10 - Xcoord) ;
            }

            if (Xcoord<-5){
                Xcoord = (10 + Xcoord) ;
            }

            if (Xcoord==0){
                Xcoord = 0.1;
            }

            rot = event.rotationRate;
            if (rot != null) {
              rotAlpha = Math.round(rot.alpha);
              rotBeta = Math.round(rot.beta);
              rotGamma = Math.round(rot.gamma);
                         }

            api.lookat(
                [zoom - Math.abs(accelerationX*3), Xcoord*2, Ycoord],
                [0, 0, 7],
                0
                );

            api.getCameraLookAt(function( err, camera ){


            btn_information.addEventListener('click', function(){
                document.getElementById('info').innerHTML = 
                     "<b>Accelerometer</b>" +
                     "<br>X:  " + accelerationX +
                     "<br>Y:  " + accelerationY +
                     "<br>Z:  " + accelerationZ +
                     "<br>" +
                     "<br><b>Gyroscope</b>" +
                     "<br>Alpha: " + rotAlpha +
                     "<br>Beta: " + rotBeta +
                     "<br>Gamma: " + rotGamma +
                     "<br>" +
                     "<br><b>Camera</b>" +
                     "<br>CamXpos: " + camera.position[0] +
                     "<br>CamYpos: " + camera.position[1] +
                     "<br>CamZpos: " + camera.position[2] +
                     "<br>CamTarget: " + camera.target


            })});
        }

}})

}
