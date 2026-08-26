# Optical Character Recognition (OCR)

<https://documentation.neutrinos.com/articles/#!components-guide-7/optical-character-recognition>

## Optical Character Recognition (OCR)

### Overview

A custom directive based on Cordova to take pictures using the camera and convert the text in the picture to string. It can be used only on mobiles. If you want to use this directive, add an** n-ocr** custom directive to any component.

| ![Information](/resources/Storage/components-guide-7/info.png) | Make sure version 1.0.0 of the [cordova-plugin-mobile-ocr](https://www.npmjs.com/package/cordova-plugin-mobile-ocr) plugin is installed. |
| --- | --- |

| ![Warning](/resources/Storage/components-guide-7/warning.png) | This directive has reference to UIWebView which may cause rejection of your app on the Apple store. If you are creating an iOS app, we suggest using **ML Text**. See [ML Text documentation](https://github.com/NeutrinosPlatform/cordova-plugin-ml-text) to learn how to use this plugin on Studio. |
| --- | --- |

### Usage

This directive can be added to any component. Once this directive is added to any component, the click event is triggered with the following functions:

- The camera on the mobile device will open.
- The user is provided the option to take a picture.
- Once a picture is taken, all the text is converted into a string and returned.

### How to use

1. Drag and drop any component and then add the following key-value pairs using the **New property: **Attribute section of the HTML page. Note:- If the value field is missing then leave it empty. If an input needs to be added to the value field, click the **Key&Value** tab and then edit the value.
  1. Add the directive as an attribute.
    - **key**: (n-ocr)
    - Leave the value field empty.
    - Click the **ADD** button.
  2. Provide the options that the directive will use.
    - **key** : (ocrOptions)
    - value : {quality:100, correctOrientation: true, uriOrBase:0, returnType:1}
    - Click the **ADD** button.
  3. Input the action that occurs if the directive successfully completed its functionality.
    - **key** : (onsuccess)
    - **value** : success($event)
    - Click the **ADD** button.
    - Then in TS editor add the following function success($event){console.log($event)}
  4. Input the action that occurs if the directive failed to complete its functionality.
    - **key** : (onerror)
    - **value** : error($event)
    - Click the **ADD** button.
    - Then in TS editor add the following function error($event){console.log($event)}
2. The console.log($event) line inside the values of the (onsuccess) and (onerror) keys can be changed as per the developer's requirement.

| ![Information](/resources/Storage/components-guide-7/info.png) | console.log($event) displays the output (which is $event) of the directive for both success and error on a console which can be accessed by google chrome or safari. |
| --- | --- |
