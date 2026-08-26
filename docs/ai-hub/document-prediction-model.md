# Advanced Configuration

<https://documentation.neutrinos.com/articles/#!ai-hub/document-prediction-model>

Document-based prediction in Neutrinos AI Hub involves extracting and analyzing data from semi-structured or unstructured documents—such as PDFs, scanned images, or digital forms—to generate predictive insights.

The prediction workflow typically begins with uploading a document, which is then processed by the platform to predict the type of document. This functionality enables developers and business users to automate manual work, accelerate document review processes, and make data-driven decisions from documents in various formats.

To create a document-based prediction model, follow the steps below:

1. Navigate to Prediction using the left navigation bar. On the Prediction landing page, go to the Document tab, then click the Add button located at the top-right corner of the page. On the following screen, click Get Started to begin. For the initial steps refer [Prediction](/articles/ai-hub/prediction) topic.
2. Click on Document to specify that your prediction model will process document-based inputs—such as PDFs, or scanned images—to detect or classify patterns within the content. This option allows the system to process documents with the objective of content classification or information extraction.
    ![ai-hub-prediction-document](/resources/Storage/ai-hub/images/ai-hub-prediction-document.png)
3. During the setup process, you’ll be prompted to confirm whether the documents being uploaded are organized in a proper folder structure. Select Yes or No based on your setup. A well-organized folder structure is crucial, as it can significantly enhance training speed and model accuracy. After making your selection, click Next at the bottom of the page to proceed.
    ![ai-hub-prediction-document-orgaized-structure](/resources/Storage/ai-hub/images/ai-hub-prediction-document-organized-structure.png)
4. Next, enter the document categories in the ‘Add Category here’ text field and press Enter to register each category for training the prediction model. For example, in this case, we have used 'aadhaar_back', 'aadhaar_front', 'eid_back', and 'eid_front' to represent the back and front sides of the Aadhaar and EID document, respectively. These categories help the model identify and distinguish the corresponding document types during training.
    ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
    Note: Each category you add must have corresponding documents uploaded for training. You can add any number of categories; however, in the following steps, you must upload at least two documents per category. Ensure that you have the necessary documents prepared for each specified category.
    After entering the categories, click the Next button at the bottom of the page to proceed.
    ![ai-hub-prediction-document-categories-add](/resources/Storage/ai-hub/images/ai-hub-prediction-document-categories-add1.png)
5. The next step is to upload documents for training the model. For each category defined in the previous step, a minimum of two documents is required. Additionally, a minimum of 25 documents in total is needed to initiate the training process.
    To upload, select a category from the ‘Category’ dropdown on the page. Then, right-click on the canvas area to browse and upload the corresponding document for the selected category.
    ![ai-hub-prediction-document-upload](/resources/Storage/ai-hub/images/ai-hub-prediction-document-upload1.gif)
    If an incorrect document is uploaded by mistake, you can remove it by clicking the Delete (trash bin) icon on the thumbnail of the uploaded document. After deletion, you can upload the correct document.
    Click the ‘Continue’ button at the bottom of the page after ensuring that the correct documents have been uploaded for training the prediction model.
6. Choose whether the documents need to be split. If splitting is required, select Yes; otherwise, select No. Splitting is useful when a single file contains multiple documents, but only one of them is relevant to the model.
    Note:
    Then, click the ‘Continue’ button at the bottom of the page to proceed.
    ![ai-hub-prediction-document-split-doc](/resources/Storage/ai-hub/images/ai-hub-prediction-document-split-doc.png)
  - If split is enabled (true), the model will undergo training on a page-by-page basis. Each page is treated distinctly, irrespective of the document.
  - If split is disabled (false), the model's training will be document-centric. The entire document is considered as one unit, without splitting it into separate pages.
7. Enter a name and description for the prediction model, then click the ‘Next’ button at the bottom of the page to proceed.
    ![ai-hub-prediction-document-name](/resources/Storage/ai-hub/images/ai-hub-prediction-document-name.png)
8. Define the rules for the prediction model. This step includes two key configurations:
    After configuring the settings as required in the previous step, click Start Training to continue.
    ![ai-hub-prediction-document-start-training](/resources/Storage/ai-hub/images/ai-hub-prediction-document-start-training.png)
  - **Feedback Loop Configuration**: Specify how newly added data should be classified or predicted. You can choose from the following options based on your requirement:
      ![ai-hub-prediction-document-feedback](/resources/Storage/ai-hub/images/ai-hub-prediction-document-feedback1.png)
    - **Always**: When the Feedback Loop Configuration is set to "Always", every generated prediction is routed for human validation. This validation is handled through the Review Hub, a built-in feature that provides an additional layer of oversight and ensures quality assurance.
    - **Never**: When the feedback loop configuration is set to "Never", the generated predictions bypass the Human-in-the-Loop process. As a result, no Review Hub activity is triggered, and all predictions are accepted without human validation.
    - **Confident**: When the feedback loop configuration is set to "Confident", a confidence threshold is defined for model predictions. If a prediction's confidence score falls below this threshold, the classified data is routed to the Review Hub for human validation. If the score meets or exceeds the threshold, the prediction is accepted without further review.
  - **Retention and Others**: In this section, you can configure the model to classify data into a default category when no specific category is available that match the new data.
      **Retention**: You can configure the data retention period to specify how long data is stored on the servers. Choose from predefined options—1 day, 5 days, 15 days, 25 days, or 30 days—or use the available slider to set a custom retention period between 1 and 30 days, based on your requirements. For more information, refer [Data Privacy and Retention](/articles/ai-hub/data-privacy-and-retention) topic.
      ![ai-hub-prediction-doc-retention](/resources/Storage/ai-hub/images/ai-hub-prediction-doc-retention-new.png)
  - **Merging the Document**: If multiple documents need to be merged for the model to make an accurate prediction, you can do so in this section. This is particularly useful when the required information is spread across different documents. Merging them here ensures the model has all the necessary context for prediction.
    - Click the ‘Add Group’ button to add a new group in the List of Groups section.
    - Select a group from the List of Groups panel, then check the box next to the desired document category in the Document Category panel to add it to the selected group.
        ![ai-hub-prediction-document-merge-doc](/resources/Storage/ai-hub/images/ai-hub-prediction-document-merge-doc.gif)
    - You can add multiple groups and repeat the above steps to merge documents as needed. To add different categories to another group, select the desired group from the List of Groups panel, then select the required document categories from the Document Category panel on the right.

Upon completion, the newly created model will be listed on the Prediction page with the other available models, as illustrated in the image below:




 ![ai-hub-prediction-document-final](/resources/Storage/ai-hub/images/ai-hub-prediction-document-final.png)

## Advanced Configuration

The platform allows you to configure advanced options while setting up target categories for the prediction model. To configure these advanced options, follow the steps below:

1. In the Categories section, while creating the prediction model (as shown in the image below), click the Gear icon located at the top-right corner of the page.
    ![ai-hub-prediction-document-advanced](/resources/Storage/ai-hub/images/ai-hub-prediction-document-advanced.png)
2. Clicking the Gear icon opens the Advanced Configuration page, where you can set up various advanced options such as Enhancing Image Contrast, Mirroring and Flipping, Rotate, Resize the Image, Remove Watermark, Gray Scale, and Hyper Parameter Configuration through which you can customize the hyperparameter values in the JSON template to optimize the model performance:
    ![ai-hub-prediction-document-advanced-config](/resources/Storage/ai-hub/images/ai-hub-prediction-document-advanced-config1.png)
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
    Document Quality Check
    This feature when enabled is used to enhance data reliability and model performance by filtering out low-quality scans from the input. Initially, the input is evaluated against a predefined confidence threshold for classification. These checks are performed if the input confidence score falls below the specified threshold value.
    The default threshold is set to 0.3. If the input score is below this value, a transformation metric is triggered to improve input quality. This transformation can either be the default configuration or customized based on specific requirements.
    The default values for the value metrics are listed below:
    The transformation metric can be selected from a dropdown menu. By default, it is set to Default Transform, but it can be changed to Custom Transform if needed. In Custom Transform, the following options are available:
    Hyper Parameter Configuration
    In AI Hub, you can configure hyperparameters based on your specific requirements. Hyperparameter configuration refers to the process of setting external parameters that control the learning behavior of a model before training begins.
    ![ai-hub-prediction-document-adv-congif-hyper-parameters](/resources/Storage/ai-hub/images/ai-hub-prediction-document-adv-congif-hyper-parameters.png)
    These parameters influence the model’s performance, including its learning speed and complexity. Some of the important parameters are discussed below:
    **Option**
    **Description**
    validation_split
    Specifies the portion of the training data to be used for validating the model. The value ranges from 0 to 1.
    For example, if set to 0.2, 20% of the training data will be used for validation to assess the model’s performance.
    preset
    Specifies the quality level for training the model. AI Hub offers three training options: "best_quality", "medium", and "highest". This setting determines the depth and precision of the training process. By default, it is set to "best_quality".
    training_time_limit
    Specifies the time limit for training the model, defined in seconds. By default, the value is set to 25000 seconds for the text prediction model. This value can be adjusted based on your requirements.
    env.per_gpu_batch_size
    The batch size for each GPU.
    env.batch_size
    The batch size used in each training step. If env.batch_size is larger than env.per_gpu_batch_size * env.num_gpus, gradient accumulation is performed to reach the effective env.batch_size before executing a single optimization step.
    env.eval_batch_size_ratio
    Prediction or evaluation uses a larger per gpu batch size env.per_gpu_batch_size * env.eval_batch_size_ratio.
    env.num_workers_evaluation
    The number of worker processes used by the Pytorch dataloader in prediction or evaluation.
    optimization.max_epochs
    Specifies the maximum number of training epochs. Training will stop once this number is reached. By default, the value is set to 10.
    For example, if set to 20, the model will train for 20 epochs.
    optimization.top_k_average_method
    Specifies the strategy used to average the top k model checkpoints. By default, it is set to greedy_soup.
    model.timm_image.checkpoint_name
    Select an image backbone architecture from the TIMM (PyTorch Image Models) library. The chosen backbone will be used as the feature extractor for the image model during training.
3. After setting the configurations, click the Save button at the bottom of the page to apply the changes:
    ![ai-hub-prediction-document-advanced-config-save](/resources/Storage/ai-hub/images/ai-hub-prediction-document-advanced-config-save.png)
