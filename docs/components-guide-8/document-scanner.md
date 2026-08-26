# Document Scanner

<https://documentation.neutrinos.com/articles/#!components-guide-8/document-scanner>

## Document Scanner

### Overview

Custom directive based on Cordova to scan documents using the camera and upload the file. It can be used only on mobiles. If you want to use this directive, add **n-scan** custom directive to any component.

| ![Information](/resources/Storage/components-guide-8/info.png) | Make sure the version 2.0.1 of the [cordova-plugin-document-scanner](https://www.npmjs.com/package/cordova-plugin-document-scanner) plugin is installed. |
| --- | --- |

### Usage

This directive can be added to any component. Once the directive is added, the **click** event is triggered in the following functions:

- The camera on the mobile device will open.
- The user is provided the option to take a picture.
- The edges of the document in the picture are detected and cropped.
- Once a document is scanned it is saved to the local device and uploaded.

### How to use

1. Drag and drop any component and then add the following key-value pairs using the **New property: **Attribute section of the HTML page. If the value field is missing then leave it empty. If an input needs to be added to the value field, click the **Key&Value **tab and edit the value of the attribute.
  1. Add the directive as an attribute.
    - **key**: (n-scan)
    - Leave the value field empty.
    - Click the **ADD **button.
  2. Provide the options that the directive will use.
    - **key** : (scanOptions)
    - **value **: {entityName: 'profile', metadata: {key:example@neutrinos.co'}, sourceType: 1, doUpload : true}
    - Click the** ADD** button.
  3. Input the action that occurs if the directive successfully completed its functionality.
    - **key **: (onsuccess)
    - **value** : success($event)
    - Click the **ADD** button.
    - Then in the TS editor add the following function success($event){console.log($event)}
  4. Input the action that occurs if the directive failed to complete its functionality.
    - **key** : (onerror)
    - **value** : error($event)
    - Click the **ADD** button.
    - Then in the TS editor add the following function error($event){console.log($event)}
2. The console.log($event) line inside the values of the (onsuccess) and (onerror) keys can be changed as per the developer's requirement.

| ![Information](/resources/Storage/components-guide-8/info.png) | console.log($event) displays the output (which is $event) of the directive for both success and error on a console which can be accessed by google chrome or safari. |
| --- | --- |
