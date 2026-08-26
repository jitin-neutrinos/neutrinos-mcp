# ocr

<https://documentation.neutrinos.com/articles/#!create-a-simple-mobile-app/ocr>

The OCR service is used to scan the pan card and capture data.

Open the ocr service and perform the following steps:

**Flow 1**

1. Drag and drop a **Start**** node** to create a flow. Double click the node and enter the following:
    **Property**
    **Value**
    **Action**
    Name
    scanPanCard
    InputVariables -> Key
    info
    Toggle **Output** to true. Click **+** to add the property to the list.
    ![ocr properties](/resources/Storage/create-a-simple-mobile-app/ocr1.png)
2. Drag and drop a** Script node**. In the **Script properties **window, add the following details:
    **Property**
    **Value**
    Name
    Open Camera and Scan Doc
    code editor
    const scan = window['scan'];
   const onScanSuccessBind = this.onScanSuccess.bind(this);
   const onScanFailBind = this.onScanFail.bind(this);
   scan.scanDoc(onScanSuccessBind, onScanFailBind, {
   quality: 5.0
   });
    ![ocr properties](/resources/Storage/create-a-simple-mobile-app/ocr2.png)

---

**Flow 2**

1. Open the service. Drag and drop a **Start**** node** to create a flow. Double click the node and enter the following:
    **Property**
    **Value**
    Name
    onScanSuccess
    Accept flow object
    Toggle to true
    ![ocr properties](/resources/Storage/create-a-simple-mobile-app/ocr3.png)
2. Drag and drop a** Script node**. In the **Script properties **window, add the following details:
    **Property**
    **Value**
    Name
    Run OCR
    code editor
    const textocr = window['textocr'];const imageURI = bh;const serviceInstance = this;const onTextRecognitionSuccessBind = this.onTextRecognitionSuccess.bind(this);const onTextRecognitionFailBind = this.onTextRecognitionFail.bind(this);
   window['resolveLocalFileSystemURI'](imageURI, function (fileEntry) { fileEntry.file(function (fileObject) { var reader = new FileReader() reader.onloadend = function (evt) { var image = new Image() image.onload = function (evt) { serviceInstance['imageHeight'] = this['height']; serviceInstance['imageWidth'] = this['width']; textocr.recText(0, imageURI, onTextRecognitionSuccessBind, onTextRecognitionFailBind); image = null } image.src = evt.target['result'] as string; } reader.readAsDataURL(fileObject) , function () {})})
    ![ocr properties](/resources/Storage/create-a-simple-mobile-app/ocr4.png)

**Flow 3**



 Open the service. Drag and drop a **Start**** node** to create a flow. Double click the node and enter the following:




 **Property**


 **Value**




 Name


 onScanFail




 Accept flow object


 Toggle to true





 ![ocr properties](/resources/Storage/create-a-simple-mobile-app/ocr5.png)



 Drag and drop a** Script node**. In the **Script properties **window, add the following details:





 **Property**


 **Value**




 Name


 Sanning Document Failed




 code editor




 console.log('scanning failed', bh);
this['info'] = null;






 ![ocr properties](/resources/Storage/create-a-simple-mobile-app/ocr6.png)

---

**Flow 4**

1. Open the service. Drag and drop a **Start**** node** to create a flow. Double click the node and enter the following:
    **Property**
    **Value**
    Name
    onTextRecognitionSuccess
    Accept flow object
    Toggle to true
    ![ocr properties 7](/resources/Storage/create-a-simple-mobile-app/ocr7.png)
2. Drag and drop a** Script node**. In the **Script properties **window, add the following details:
    **Property**
    **Value**
    Name
    Break Recognition
    code editor
    const linesFrames = bh['lines']['lineframe'];const linetext = bh['lines']['linetext'];const height = this['imageHeight'];const width = this['imageWidth'];console.log('observered dimensions', height, width);const newObj = {};const keyDeltas = [ { key: "firstName", x: { min: 94, max: 99 }, y: { min: 62, max: 72 } }, { key: "lastName", x: { min: 94, max: 98 }, y: { min: 53, max: 60 } }, { key: "dob", x: { min: 94, max: 97 }, y: { min: 39, max: 45 } }, { key: "pan", x: { min: 94, max: 97 }, y: { min: 26, max: 34 } }]
   for (let i = 0; i < keyDeltas.length; i++) { for (let j = 0; j < linesFrames.length; j++) { const xPercentage = ((width - linesFrames[j].x) / width) * 100; const yPercentage = ((height - linesFrames[j].y) / height) * 100; console.log(linetext[j], xPercentage, yPercentage) if ((keyDeltas[i].x.min <= xPercentage) && (xPercentage <= keyDeltas[i].x.max) && (keyDeltas[i].y.min <= yPercentage) && (keyDeltas[i].y.max >= yPercentage)) { newObj[keyDeltas[i].key] = linetext[j]; } }}
   let pan = '';let date = '';for (let i = 0; i < linetext.length; i++) { const panRegex = new RegExp('^([a-zA-Z]){5}([0-9]){4}([a-zA-Z]){1}?$'); const dateRegex = /\d{1,2}\/\d\d?\/\d{4}/; if (linetext[i].match(panRegex)) { pan = linetext[i]; }
    if (linetext[i].match(dateRegex)) { date = linetext[i]; }}
   newObj['pan'] = pan;newObj['dob'] = date;console.log('newObj', newObj);bh = newObj;
    ![ocr properties](/resources/Storage/create-a-simple-mobile-app/ocr8.png)
3. Drag and drop a **Service variables** node. Double click the node and enter the following properties:
    **Property**
    **Value**
    **Action**
    Name
    get weather
    Operation type
    Set Service variables
    InputVariables -> Key
    info
    select as is property and enter bh. Click + to add the variable
    ![ocr properties](/resources/Storage/create-a-simple-mobile-app/ocr9.png)
4. Drag and drop a **Script node**. This is used to log variables that the user has given in the browser console. Double click the node and enter the following properties:
    **Property**
    **Value**
    Name
    Code editor
    let bh = this.sdService.__constructDefault({});
   bh.system.pubsubService.$pub('scan-complete');
    ![ocr properties](/resources/Storage/create-a-simple-mobile-app/ocr10.png)

**Flow 5**

Open the service. Drag and drop a **Start**** node** to create a flow. Double click the node and enter the following:




 **Property**


 **Value**




 Name


 onTextRecognitionFail




 Accept flow object


 Toggle to true





 ![ocr properties](/resources/Storage/create-a-simple-mobile-app/ocr11.png)



 Drag and drop a** Script node**. In the **Script properties **window, add the following details:





 **Property**


 **Value**




 Name


 Text Recognition Failed




 code editor




 console.log('text recognition failed', bh);
this['info'] = null;






 ![ocr properties](/resources/Storage/create-a-simple-mobile-app/ocr12.png)

Connect the nodes to create the following server flow.
