# Extract From Table

<https://documentation.neutrinos.com/articles/#!ai-hub/document-extraction-model>

Document-based Extraction on Neutrinos AI Hub enables intelligent retrieval of structured information from unstructured or semi-structured documents such as PDFs and scanned images. Leveraging pre-trained AI models this feature allows users to automate the extraction of key data points—such as names, dates, invoice numbers, and other contextual information—without the need for extensive manual intervention.

Designed to integrate seamlessly with business processes, the extraction engine supports multiple document formats and uses advanced techniques like Optical Character Recognition (OCR), Named Entity Recognition (NER), and pattern-based matching to ensure accuracy and relevance.

1. Navigate to Extraction from the left navigation bar. On the Extraction landing page, go to the Document tab, then click the Add button located at the top-right corner of the page. On the following screen, click Get Started to begin. For the initial steps refer Extraction topic.
2. On the Create page, click Document to specify a document-based extraction model, then click Next. Use this option when working with unstructured or semi-structured files (e.g., PDFs, scanned forms, or images) to visually tag and extract data.
    ![ai-hub-extraction-text-select](/resources/Storage/ai-hub/images/ai-hub-extraction-document.png)
3. In the next step, select files from your local system to upload to the platform for training the extraction model. A minimum of 25 files is required to effectively train the model.
    ![ai-hub-extraction-document-upload](/resources/Storage/ai-hub/images/ai-hub-extraction-document-upload.png)
    Once the documents are uploaded to the platform, the system displays statistics indicating how many were successfully uploaded and how many failed, if any. Review the upload summary, re-upload any failed documents, and then click Next at the bottom of the page.
    ![ai-hub-extraction-document-upload-complete](/resources/Storage/ai-hub/images/ai-hub-extraction-document-upload-complete.png)
4. Enter a name and description for the extraction model.
    ![ai-hub-extraction-document-name-description](/resources/Storage/ai-hub/images/ai-hub-extraction-document-name-description.png)
5. Add the fields to be extracted from the documents uploaded in the previous step. Follow the steps below to add fields:
  1. Click **Add Field** under Section One, a predefined and available section located in the right panel of the page. The left panel displays the uploaded document. You can either add fields manually or use the platform’s Auto-Fetch feature to automatically extract available fields from the document. The GIF below demonstrates how to manually add fields for extraction.
      ![ai-hub-extraction-document-add-field](/resources/Storage/ai-hub/images/ai-hub-extraction-document-add-fields.gif)
      The GIF below demonstrates how to fetch all available fields from the document using the Auto-Fetch feature:
      ![ai-hub-extraction-document-fields-auto-fetch](/resources/Storage/ai-hub/images/ai-hub-extraction-document-fields-auto-fetch.gif)
      Verify that all the required fields have been added to the section for extraction from the document, and then click the Next button at the bottom of the screen.
      ![ai-hub-extraction-document-fields-add](/resources/Storage/ai-hub/images/ai-hub-extraction-document-fields-add.png)
      ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
      Note: You can change a field’s data type by double-clicking the data type displayed next to the field name.
6. Define the rules for the extraction model. This step includes two key configurations:
    After configuring the settings as required in the previous step, click Next to continue.
    ![ai-hub-extraction-document-rules-next](/resources/Storage/ai-hub/images/ai-hub-extraction-document-rules-next-new.png)
  - **Feedback Loop Configuration**: Specify the extent to which Human-in-the-Loop intervention is required during the document extraction process. This configuration must be done individually for each entity (category) added in the previous step. Based on your requirements, you can choose from the following options:
      ![ai-hub-extraction-document-feedback-loop](/resources/Storage/ai-hub/images/ai-hub-extraction-document-feedback-loop.png)
    1. **Always**: When the Feedback Loop Configuration is set to "Always", every generated prediction is routed for human validation. This validation is handled through the Review Hub, a built-in feature that provides an additional layer of oversight and ensures quality assurance.
    2. **Never**: When the feedback loop configuration is set to "Never", the generated predictions bypass the Human-in-the-Loop process. As a result, no Review Hub activity is triggered, and all predictions are accepted without human validation.
    3. **Confident**: When the feedback loop configuration is set to "Confident", a confidence threshold is defined for model predictions. If a prediction's confidence score falls below this threshold, the classified data is routed to the Review Hub for human validation. If the score meets or exceeds the threshold, the prediction is accepted without further review.
  - **Retention and Others**: You can configure the data retention period to specify how long data is stored on the servers. Choose from predefined options—1 day, 5 days, 15 days, 25 days, or 30 days—or use the available slider to set a custom retention period between 1 and 30 days, based on your requirements. For more information, refer [Data Privacy and Retention](/articles/ai-hub/data-privacy-and-retention) topic.
      ![ai-hub-extraction-document-retention](/resources/Storage/ai-hub/images/ai-hub-extraction-document-retention-new.png)
7. The next step is to train the model. Based on the fields added in the previous step, review the extracted entries in the left panel and confirm their corresponding target categories in the right panel. Click each field in the right panel and validate the corresponding entries extracted from the document in the left panel. It is recommended to confirm at least 25 entries to help ensure accurate model training.
    ![ai-hub-extraction-document-confirm-fields](/resources/Storage/ai-hub/images/ai-hub-extraction-document-confirm-fields.gif)
    Once at least 25 entries have been confirmed for the extracted fields, the Start Training button will appear at the bottom of the page. Click Start Training to begin the training process.
    Note: If a data type is changed, you must manually draw a rectangular box around the field you want to extract from the uploaded document, then click Accept in the pop-up window. The GIF below demonstrates how to draw a rectangular border around a field intended for extraction:
    ![ai-hub-extraction-document-draw-rectangle-extract](/resources/Storage/ai-hub/images/ai-hub-extraction-document-draw-rectangle-extract.gif)
8. After completing the minimum requirement of 25 confirmations for training the model, the Learning Progress indicator at the top of the left panel will show 100%. Once this happens, the Start Training button will appear at the bottom of the page. Click Start Training to initiate the training process. After training is complete, the model will appear in the list of available extraction models on the platform.
    ![ai-hub-extraction-document-min-criteria-next](/resources/Storage/ai-hub/images/ai-hub-extraction-document-min-criteria-next.png)
9. If more than 25 files are uploaded for training, but only 25 are confirmed, a pop-up message will appear, informing you that the remaining unlabelled files will be deleted. Click Yes to confirm deletion of the unused files. To retain all uploaded files on the platform, click No and continue confirming the remaining files.
    ![ai-hub-extraction-document-delete-files-unlabelled](/resources/Storage/ai-hub/images/ai-hub-extraction-document-delete-files-unlabelled.png)
    ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
    Note: The more documents you label, the higher the model’s accuracy. However, a minimum of 25 labeled files is required to proceed with training.

After training is complete, the model will appear in the list of available extraction models under the Documents tab on the platform.




 ![ai-hub-extraction-document-complete](/resources/Storage/ai-hub/images/ai-hub-extraction-document-complete.png)

### Extract From Table

You can extract data from a document table and present it in a structured tabular format. Follow the steps below to perform this extraction:

1. Create a new field and set its data type to Table. For example, consider a table named Item created from the document. This table includes the following columns: No, Description, Net Price, VAT, and Gross Worth. These columns are derived from the document format, as illustrated in the image below:
    ![ai-hub-extraction-document-table](/resources/Storage/ai-hub/images/ai-hub-extraction-document-table.png)
2. In the next step, define the rule configuration. This includes setting up the feedback loop configuration for the fields you’ve added and specifying the data retention rules. After completing these configurations, click the Next button at the bottom of the page to proceed.
3. Information from straightforward fields in the document is fetched automatically. To extract data from a table within the document, follow the steps below:
  1. Click the field that represents the table in the document.
  2. Select the entire table area by clicking and dragging a rectangular box over the table in the document shown in the left panel.
  3. Position the mouse cursor over each column in the table within the document. Annotate the columns according to the table structure defined in the previous steps. This ensures the accurate extraction of the relevant fields from the document into the defined table.
  4. Click the Apply button at the bottom of the left panel to apply the annotations. Then, click the Confirm button at the bottom of the page to finalize the selection of fields for that specific document sample. The GIF below illustrates the process of selecting fields from the table according to the specified requirements:
  5. Repeat the above process for a minimum of 25 documents to train the model effectively. Note: The greater the number of confirmed documents, the higher the resulting model accuracy.

## Advanced Configuration

The platform allows you to configure advanced options while setting up target categories for the extraction model. To configure these advanced options, follow the steps below:

1. In the Upload section, while creating the extraction model (as shown in the image below), click the Gear icon located at the top-right corner of the page.
    ![ai-hub-extraction-document-gear-icon](/resources/Storage/ai-hub/images/ai-hub-extraction-document-gear-icon.png)
2. Clicking the Gear icon opens the Advanced Configuration page, where you can configure advanced image settings such as enhancing contrast, mirroring or flipping the image, rotating, resizing, removing existing watermarks, converting to grayscale, and more. To apply a specific configuration, select the checkbox corresponding to the desired option.
    ![ai-hub-extraction-document-adv-config](/resources/Storage/ai-hub/images/ai-hub-extraction-document-adv-config.png)
    **Option**
    **Description**
    Enhance Image Contrast
    Enhancing image contrast improves the visual distinction between the light and dark areas of an image.
    Use case:
    Mirroring and Flipping
    Mirroring and flipping are basic image transformation techniques often used in image extraction, preprocessing, or augmentation.
    Use Case
    Data Augmentation
    Create variations of training images to improve model generalization.
    Alignment/Normalization
    Adjust images to a consistent orientation
    Feature Detection
    Compare mirrored versions for symmetrical features
    Image Correction
    Fix images that are scanned or captured in reverse
    Rotate
    Rotate Image refers to the process of rotating a scanned or uploaded document image by a specific angle—typically 90°, 180°, or 270°—to ensure proper alignment for accurate processing and prediction. Rotation is necessary because uploaded images may be tilted, upside-down, or sideways due to mobile capture, scanning errors, or incorrect orientation during the upload process.
    Proper rotation ensures consistent image orientation, which is critical for accurate Optical Character Recognition (OCR) and model prediction. This functionality is beneficial during the preprocessing stage of document classification, data extraction, and prediction workflows.
    Resize Image
    Resize image adjusts the size of an image to match what the model expects. For example, a model might only accept images of size 224×224 pixels, so all input images must be resized accordingly.
    Remove Watermark
    It removes or reduces the visibility of watermarks, which are often: Semi-transparent logos, Repeating text ("Confidential", "Draft", etc.) which are diagonal overlays across the image. This cleaning step enhances the clarity and usability of the image for downstream tasks like:
    Task
    Why remove watermarks
    OCR (Optical Character Recognition)
    Watermarks can distort or obscure readable text.
    Text or Field Extraction
    Watermark overlaps may mislead the model (e.g., extract wrong invoice number).
    Document Classification
    Visual noise can mislead CNNs or attention-based models.
    Gray Scale
    Grayscale conversion is a preprocessing step where a color image is transformed into a black-and-white (shades of gray) image. It reduces the image to a single intensity channel, where:
    Document Sensitivity Scoring
    Levenshtein Distance-Based Scoring: The Levenshtein distance is computed between the extracted value and the corrected value (if any) provided in the Review Hub for a given field. If the calculated distance falls below a predefined threshold (e.g., 0.7), the model is given a negative score, indicating an incorrect extraction. Otherwise, a positive score is assigned, and the extracted value is retained.
    For example: If the model extracts "Hose" instead of the correct value "Horse", the Levenshtein distance between the two is calculated. Since the distance is more than 0.7, a positive score is assigned to the model.
    Hyper Parameter Configuration
    In AI Hub, you can configure hyperparameters based on your specific requirements. Hyperparameter configuration refers to the process of setting external parameters that control the learning behavior of a model prior to training.
   ![ai-hub-extraction-document-hyperparameters](/resources/Storage/ai-hub/images/ai-hub-extraction-document-hyperparameters.png)
   These parameters influence the model’s performance, including its learning speed and complexity. Some of the important parameters are discussed below:
    **Option**
   **Description**
   validation_split
   Specifies the portion of the training data to be used for validating the model. The value ranges from 0 to 1.For example, if set to 0.2, 20% of the training data will be used for validation to assess the model’s performance.preset
   Specifies the quality level for training the model. AI Hub offers three training options: "best_quality", "medium", and "highest". This setting determines the depth and precision of the training process. By default, it is set to "best_quality".training_time_limit
   Specifies the time limit for training the model, defined in seconds. By default, the value is set to 25000 seconds for the text prediction model. This value can be adjusted based on your requirements.
   env.per_gpu_batch_size
   The batch size for each GPU.
   env.batch_size
   Specifies the batch size used in each training step. If env.batch_size exceeds the product of env.per_gpu_batch_size and env.num_gpus, gradient accumulation is used. In this case, gradients are accumulated over multiple forward passes until the effective env.batch_size is reached, after which a single optimization step is performed.
   optimization.max_epochs
   Specifies the maximum number of training epochs. Training will stop once this number is reached. By default, the value is set to 10.For example, if set to 20, the model will train for 20 epochs.model.mmdet_image.checkpoint_name
   Specifies the foundational model on which training is performed. Users can choose a valid model name from Hugging Face to serve as the starting point for training or fine-tuning. The selected model name must be compatible with the task and follow the naming conventions used in the Hugging Face model hub(e.g., “yolox_nano”, “yolox_tiny”, “yolox_s”, “yolox_m”, “yolox_l”, or “yolox_x”).
3. After setting the configurations, click the Save button at the bottom of the page to apply the changes.
    ![ai-hub-extraction-document-adv-config-save-button](/resources/Storage/ai-hub/images/ai-hub-extraction-document-adv-config-save-button.png)
