# Shake Detector

<https://documentation.neutrinos.com/articles/#!components-guide-8/shake-detector>

## Shake Detector

### Overview

A custom directive based on Cordova to detect shakes. It can be used only on mobiles. If you want to use this directive, add the **n-shake** custom directive to any component.

| ![Information](/resources/Storage/components-guide-8/info.png) | Make sure the version 1.0.0 of the **[cordova-plugin-neushake](https://www.npmjs.com/package/cordova-plugin-neushake) **plugin is installed. |
| --- | --- |

### Usage

This directive can be added to any component. Once the directive is added the click event is triggered the following functions:

- The shake detector will start listening for shakes once the input option start is set to** true** and the component is clicked.
- Once a shake is detected successfully the (onsuccess) runs.
- The shake detector will stop listening for shakes only once the input option start is set to **false** and the component is clicked.
- There can be separate components for starting and stopping shake.

### How to use

1. Drag and drop any component and then add the following **key&value** pairs using the **New property:** Attribute section of the HTML page. If the value field is missing then leave it empty. If an input needs to be added to the value field, click the **Key&Value** tab and then edit the value.
  1. Add the directive as an attribute.
    - **key**: (n-shake)
    - Leave the value field empty.
    - Click the **ADD** button.
  2. Provide the options that the directive will use.
    - **key** : (shakeOptions)
    - **value **: {sensitivity:30, start:true}
    - Click the** ADD** button.
  3. Input the action that occurs if the directive successfully completed its functionality.
    - **key** : (onsuccess)
    - **value** : success($event)
    - Click the **ADD **button.
    - Then in TS editor add the following function success($event){console.log($event)}
  4. Input the action that occurs if the directive failed to complete its functionality.
    - **key** : (onerror)
    - **value** : error($event)
    - Click the **ADD **button.
    - Then in TS editor add the following function error($event){console.log($event)}
2. The console.log($event) line inside the values of the (onsuccess) and (onerror) keys can be changed as per the developer's requirement.

| ![Information](/resources/Storage/components-guide-8/info.png) | console.log($event) displays the output (which is $event) of the directive for both success and error on a console which can be accessed by google chrome or safari. |
| --- | --- |
