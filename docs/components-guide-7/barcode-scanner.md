# Barcode Scanner

<https://documentation.neutrinos.com/articles/#!components-guide-7/barcode-scanner>

## Barcode Scanner

### Overview

Barcode Scanner is a custom directive based on Cordova. It is used to scan barcodes or QR codes using the camera and retrieve the barcode as a string. It can be used only on mobiles. If you want to use this directive, add an** n-barcode** custom directive to any component.

| ![Information](/resources/Storage/components-guide-7/info.png) | Make sure the version 8.0.1 of the **[phonegap-plugin-barcodescanner](https://www.npmjs.com/package/phonegap-plugin-barcodescanner) **plugin is installed. |
| --- | --- |

### Usage

This directive can be added to any component. Once this directive is added click event will be triggered with the following functions:

- The camera on the mobile device will open.
- The user is provided the option to scan a barcode.
- Once a barcode has scanned an object with the barcode and the format of the barcode is returned.

### How to use

1. Drag and drop any component and then add the following key-value pairs using the New property: Attribute section of the HTML page. If the value field is missing, then leave it empty. If an input needs to be added to the value field, click the** Key&Value **tab of the custom properties and edit the value field.
  1. Add the directive as an attribute.
    - **key**: (n-barcode)
    - No value field
    - Click the **ADD** button
  2. Provide the options that the directive will use.
    - **key** : (barcodeOptions)
    - **value** : Copy CodeJavaScript{
        preferFrontCamera: boolean, // boolean fields take true or false as value
        showFlipCameraButton: boolean,
        showTorchButton: boolean,
        torchOn: boolean,
        saveHistory: boolean,
        prompt: 'Place a barcode inside the scan area',
        resultDisplayDuration: 1500,
        formats: 'QR_CODE,DATA_MATRIX,UPC_A,UPC_E,EAN_8,EAN_13,CODE_39,CODE_93,CODE_128,CODABAR,ITF,RSS14,MSI',
        orientation: string, //'portrait' or 'landscape'
        disableAnimations: boolean,
        disableSuccessBeep: boolean
        }

- Click the** ADD** button.

Input the action that occurs if the directive successfully completed its functionality.

- **key** : (onsuccess)
- **value** : success($event)
- Click the **ADD** button
- Then in the TS editor add the following function success($event){console.log($event)}
- The object returned on success contains the following values:-
  - result.text that contains the text obtained from the barcode.
  - result.format which is the format of the code returned.
  - result.cancelled is a boolean value which is true if the user canceled the operation and false if the user didn't cancel. This value is always false in the success callback function.

Input the action that occurs if the directive failed to complete its functionality.

- **key** : (onerror)
- **value** : error($event)
- Click the **ADD** button
- Then in the TS editor add the following function error($event){console.log($event)}

The console.log($event) line inside the values of the (onsuccess) and (onerror) keys that can be changed as per the developer's requirement.

| ![Information](/resources/Storage/components-guide-7/info.png) | console.log($event) displays the output (which is $event) of the directive for both success and error on a console which can be accessed by google chrome or safari. |
| --- | --- |
