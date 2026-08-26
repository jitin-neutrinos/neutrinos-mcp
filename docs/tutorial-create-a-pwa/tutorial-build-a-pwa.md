# Tutorial: Build a PWA on Neutrinos Studio 8.0

<https://documentation.neutrinos.com/articles/#!tutorial-create-a-pwa/tutorial-build-a-pwa>

Build a Progressive Web App on Neutrinos Studio 8.0





 In this tutorial, you will be learning how to:



 Convert the Weather app to a Progressive Web App (PWA)


 Update the application manifest of the PWA


 Cache URLs to work offline


 Subscribe and unsubscribe from Web Push Notifications



 At the end of this tutorial, the end-user should be able to install the app as a PWA from the browser's address bar, subscribe to weather updates of a city by entering the city name of their choice, get weather notification of that city every 10 minutes, unsubscribe to the weather updates by clicking the Unsubscribe button, and access a few URLs even when the app is offline.

 ![Subscribe to weather updates of a city](/resources/Storage/tutorial-create-a-pwa/wea_subscribe.png)

 ![weather notification](/resources/Storage/tutorial-create-a-pwa/weather_notification.png)

 ![unsubscribe from weather updates](/resources/Storage/tutorial-create-a-pwa/wea_unsubscribe.png)






 Step 1: Prerequisites
 Before you convert the weather app to PWA, perform the following steps:

 Learn about Progressive Web App and its advantages. See [Progressive Web Apps](/smart/project-concepts/progressive-web-app).
 Build the Weather app using Neutrinos Studio 8. See [Build a Simple Web App](http://docs1.neutrinos.co/articles/psd-tutorial-publication).
 Download and install the MongoDB Community Server on your local machine from [here](https://www.mongodb.com/try/download/community). We will be using this server to store the subscription details of the weather service. After installing the server, enter the **Connection String** as **mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false**.





 Step 2: Convert the Weather App to PWA - 5 mins


 Use the PWA editor on Studio to convert the Weather app to a PWA and update the [application manifest](/smart/project-concepts/application-manifest).


 [Convert the App to a PWA](/articles/tutorial-create-a-pwa/step1-convert-the-app-into-pwa)








 Step 3: Configure Cache Settings - 10 mins


 Use the Cache Config editor to cache URLs in the Service worker so that after the first access they can be viewed even when the device is offline.


 [Configure Cache Settings](/articles/tutorial-create-a-pwa/step2-configure-cache-settings)








 Step 4: Configure Web Push Notifications - 20 mins


 Create reusable service flows on Client and Server Services Designer to subscribe and unsubscribe from Web Push Notifications.


 [Configure Push Notifications](/articles/tutorial-create-a-pwa/step3-work-with-web-push-notifications)








 Step 5: Build and Test the PWA - 10 mins


 Take a build of the app, run an HTTP Server locally, and test the working of the PWA.


 [Test the PWA](/articles/tutorial-create-a-pwa/step4-test-pwa)
