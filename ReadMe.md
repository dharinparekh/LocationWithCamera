This is an attempt to reduce the dependency of any device on GPS for location.
Inside an organization or an institution the GPS will never work for navigation.

Training Data
Trained on 17 classes of VJTI.(Educational Institution)
Classes Examples:
  Quadrangle
  Ground
  Canteen
  Lab 3
  Computer Department corridor

Interface:
  Android application made to capture an image from the camera send the image to the flask server where the model predicts the classs
  based on the earlier training and return the results on the screen itself. (Even speech synthesis was used)

Use cases:
  Any organization requiring an internal mapping system, without using triangulation of WiFi signals. 
  This can also help drones in navigation.
    Along with the GPS this camera based location will not fail in places GPS is lost or ambiguous.
    
Models Used and Trained:
  Inception V2 model was used in which the last layer (fully connected) was trained by us.
  
