# Barcode Scanner

<https://documentation.neutrinos.com/articles/#!components-guide/barcode-scanner5>

## Barcode Scanner

OverviewCustom directive based on Cordova to scan barcodes or Qr codes using the camera and retrieve the barcode as a string. It can be used only on mobiles. If you want to use this add **n-barcode** custom directive to any component.UsageThis directive is intended to be added to any component. Once added any click event on the component will trigger the following function:The camera on the mobile device will open.The user is provided the option to scan a barcode.Once a barcode has scanned an object with the barcode and the format of the barcode is returned.How to useDrag and drop any component and then add the following key-value pairs using the **New property: Attribute** section of the HTML page. **Note**: If the value field is missing then leave it empty. If an input needs to be added to the value field, click the slide-toggle button; this makes the value field editable.Add the directive as an attribute.key: (n-barcode)No value fieldClick the **ADD** buttonProvide the options that the directive will use.key : (barcodeOptions) value :Copy CodeJavaScript{
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
Click the **ADD** buttonInput the action that occurs if the directive successfully completed its functionality.key : (onsuccess) value : `success($event)`Click the **ADD** buttonThen is TS file add the following function `success($event){console.log($event)}`The object returned on success contains the following values:-**result.text** that contains the text obtained from the barcode.**result.format** which is the format of the code returned.**result.cancelled** is a boolean value which is true if the user canceled the operation and false if the user didn't cancel. This value is always false in the success callback function.Input the action that occurs if the directive failed to complete its functionality.key : (onerror) value : `error($event)`Click the** ADD** buttonThen is TS file add the following function `error($event){console.log($event)}`The `console.log($event)` line inside the values of the (onsuccess) and (onerror) keys can be changed as per the developers requirement. **Note**:- `console.log($event)` displays the output (which is $event) of the directive for both success and error on a console which can be accessed by google chrome or safari.**Support****Devices:** Android, iOS**Browsers:** Latest version of all modern browsers**Dependencies version:**Angular CLI version: 6.0.0 +Cordova version: 7.1.0 +
