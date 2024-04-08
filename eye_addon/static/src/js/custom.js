function setupCanvas() {
        var canvas1 = document.getElementById("sig-canvas1");
        if (canvas1){
              var ctx1 = canvas1.getContext("2d");
              ctx1.strokeStyle = "#222222";
              ctx1.lineWidth = 2;

             
              var backgroundImage2 = new Image();
              backgroundImage2.src = "eye_addon/static/description/eye_diagram.png";
                // Draw background image onto the canvas

                backgroundImage2.onload = function() {
                  ctx1.drawImage(backgroundImage2, 0, 0, canvas1.width, canvas1.height);
                };
              var drawing = false;
              var mousePos = {
                x: 0,
                y: 0
              };
              var lastPos = mousePos;
              canvas1.addEventListener("mousedown", function(e) {
                drawing = true;
                lastPos = getMousePos(canvas1, e);
              }, false);

              canvas1.addEventListener("mouseup", function(e) {
                drawing = false;
              }, false);

              canvas1.addEventListener("mousemove", function(e) {
                mousePos = getMousePos(canvas1, e);
              }, false);

              // Add touch event support for mobile
              canvas1.addEventListener("touchstart", function(e) {

              }, false);

              canvas1.addEventListener("touchmove", function(e) {
                var touch = e.touches[0];
                var me = new MouseEvent("mousemove", {
                  clientX: touch.clientX,
                  clientY: touch.clientY
                });
                canvas1.dispatchEvent(me);
              }, false);

              canvas1.addEventListener("touchstart", function(e) {
                mousePos = getTouchPos(canvas1, e);
                var touch = e.touches[0];
                var me = new MouseEvent("mousedown", {
                  clientX: touch.clientX,
                  clientY: touch.clientY
                });
                canvas1.dispatchEvent(me);
              }, false);

              canvas1.addEventListener("touchend", function(e) {
                var me = new MouseEvent("mouseup", {});
                canvas1.dispatchEvent(me);
              }, false);

              function getMousePos(canvas1Dom, mouseEvent) {
                var rect = canvas1Dom.getBoundingClientRect();
                return {
                  x: mouseEvent.clientX - rect.left,
                  y: mouseEvent.clientY - rect.top
                }
              }

              function getTouchPos(canvas1Dom, touchEvent) {
                var rect = canvas1Dom.getBoundingClientRect();
                return {
                  x: touchEvent.touches[0].clientX - rect.left,
                  y: touchEvent.touches[0].clientY - rect.top
                }
              }

              function rendercanvas1() {
                if (drawing) {
                  ctx1.moveTo(lastPos.x, lastPos.y);
                  ctx1.lineTo(mousePos.x, mousePos.y);
                  ctx1.stroke();
                  lastPos = mousePos;
                }
              }

              // Prevent scrolling when touching the canvas1
                function sltechHandleTouchEvents(event) {
                    if (event.target == canvas1) {
                        event.preventDefault();
                    }
                }

                // Attach touch event listeners to the canvas element
                canvas1.addEventListener("touchstart", sltechHandleTouchEvents, false);
                canvas1.addEventListener("touchend", sltechHandleTouchEvents, false);
                canvas1.addEventListener("touchmove", sltechHandleTouchEvents, false);

              (function() {
                    window.requestAnimFrame = (function(callback) {
                        return window.requestAnimationFrame ||
                            window.webkitRequestAnimationFrame ||
                            window.mozRequestAnimationFrame ||
                            window.oRequestAnimationFrame ||
                            window.msRequestAnimationFrame ||
                            function(callback) {
                                window.setTimeout(callback, 1000 / 60);
                            };
                    })();

                    function drawLoop() {
                        requestAnimFrame(drawLoop);
                        rendercanvas1(); // Assuming rendercanvas1() is defined elsewhere
                    }

                    drawLoop(); // Start the animation loop
                })();

            function clearcanvas1() {
            canvas1.width = canvas1.width;
            var ctx1 = canvas1.getContext("2d");
              ctx1.strokeStyle = "#222222";
              ctx1.lineWidth = 2;
            

            var backgroundImage2 = new Image();
              backgroundImage2.src = "eye_addon/static/description/eye_diagram.png";

            // Draw background image onto the canvas
            backgroundImage2.onload = function() {
              ctx1.drawImage(backgroundImage2, 0, 0, canvas1.width, canvas1.height);
            };
          }

          // Set up the UI
          var sigText = document.getElementById("sig-dataUrl1");
          var sigImage = document.getElementById("sig-image1");
          var clearBtn = document.getElementById("sig-clearBtn1");
          var submitBtn = document.getElementById("sig-submitBtn1");
          clearBtn.addEventListener("click", function(e) {
            clearcanvas1();
            sigText.innerHTML = "Data URL for your signature will go here!";
            sigImage.setAttribute("src", "");
            document.getElementById("sig-image-div").style.display = 'none';
          }, false);
          submitBtn.addEventListener("click", function(e) {
            var dataUrl = canvas1.toDataURL();
            sigText.innerHTML = dataUrl;
            sigImage.setAttribute("src", dataUrl);
            const urlObject = new URL(window.location.href);
            var activeRecordId = extractIdFromString(urlObject.hash);

            $.ajax({
                url : '/save/edited/image',
                type : 'post',
                data:{
                    'id':activeRecordId,
                    'digital_sign': dataUrl
                },
                success : function (result) {
                var response = JSON.parse(result);
                location.reload();

                },
            });

          }, false);


                    }
    }

function extractIdFromString(urlString) {
    var keyValuePairs = urlString.split('&');
    var idPair = keyValuePairs.find(pair => pair.startsWith('#id='));
    if (idPair) {
        var idValue = idPair.split('=')[1];
        return idValue;
    } else {
        return null;
    }
}
