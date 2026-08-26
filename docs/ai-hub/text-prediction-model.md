# Advanced Configuration

<https://documentation.neutrinos.com/articles/#!ai-hub/text-prediction-model>

Text-based prediction is a feature in Neutrinos AI Hub that leverages machine learning and natural language processing (NLP) models to analyze, interpret, and predict outcomes from text data. This functionality enables developers and business users to extract meaningful insights, classify content, and automate decision-making processes using textual input.

To create a text-based prediction model, follow the steps below:

1. Navigate to Prediction using the left navigation bar. On the Prediction landing page, go to the Text tab, then click the Add button located at the top-right corner of the page. On the following screen, click Get Started to begin. For the initial steps refer [Prediction](/articles/ai-hub/prediction) topic.
2. Click Text on the create page to specify a text-based prediction model, then click Next. This option is suitable for analyzing data from structured text sources, such as Excel or CSV files.
    ![ai-hub-prediction-text](/resources/Storage/ai-hub/images/ai-hub-prediction-text1.png)
3. You will be prompted to upload a text file in either Excel or CSV format, which is required to train the model. Choose the appropriate file type based on your requirements, then click Next at the bottom of the page. For example, here, we have used Excel for illustration purposes.
    ![ai-hub-prediction-text-excel](/resources/Storage/ai-hub/images/ai-hub-prediction-text-excel.png)
4. Select a file from your local system to upload it to the platform for training the prediction model.
    ![ai-hub-prediction-text-browse-upload](/resources/Storage/ai-hub/images/ai-hub-prediction-text-browse-upload.png)
5. Once a file is selected from your local computer, click Continue at the bottom of the page.
    ![ai-hub-prediction-texxt-upload](/resources/Storage/ai-hub/images/ai-hub-prediction-texxt-upload.png)
    If an incorrect file is uploaded, you can remove it by clicking the delete (trash bin) icon next to the uploaded file. You can then upload a new file as needed.
6. The data from the uploaded file is displayed in a columnar format, preserving the structure of the original file. Review the data to ensure it has been imported correctly. If the Excel sheet includes a header row with labels used for model training, you can choose to exclude it by selecting the Discard the First Row checkbox. This option is unchecked by default. Once you have verified the data, click Next at the bottom of the page to proceed.
    ![ai-hub-prediction-text-uploaded-information](/resources/Storage/ai-hub/images/ai-hub-prediction-text-uploaded-information.png)
7. In the next step, select Yes if the dataset is categorized and the corresponding target categories are already included. Otherwise, click No. Then, click Continue to proceed. If the target categories are not provided in the uploaded file, you will be required to manually enter them in the following step.
    ![ai-hub-prediction-text-category](/resources/Storage/ai-hub/images/ai-hub-prediction-text-category.png)
    If you selected No in the previous step, you will be prompted to manually enter the target categories that the model will use to classify and predict the data. Add the required categories in the input field, as demonstrated in the GIF below. Once done, click Continue at the bottom of the page to proceed to Step 9.
    ![ai-hub-prediction-text-add-categories](/resources/Storage/ai-hub/images/ai-hub-prediction-text-add-categories.gif)
8. If you selected Yes in Step 6 (i.e., the data is already categorized), choose the column from the dropdown that contains the target categories. This step is crucial, as the prediction model will use this column to classify the data. Click Continue to proceed to the next step.
    ![ai-hub-prediction-text-column-select-target](/resources/Storage/ai-hub/images/ai-hub-prediction-text-column-select-target.png)
9. A list of distinct categories from the selected column is displayed, based on the data uploaded to the platform. Verify that all expected categories are listed before proceeding.
    ![ai-hub-prediction-text-target-category](/resources/Storage/ai-hub/images/ai-hub-prediction-text-target-category.png)
    If additional categories are needed for prediction, you can add them by typing the category name in the Add Category here.. text field and pressing Enter.
    ![ai-hub-prediction-text-add-category](/resources/Storage/ai-hub/images/ai-hub-prediction-text-add-category.png)
    After confirming that all required categories are available for model prediction, click Continue at the bottom of the page.
    ![ai-hub-prediction-text-continue](/resources/Storage/ai-hub/images/ai-hub-prediction-text-continue.png)
10. Enter a name and description for the prediction model.
    ![ai-hub-prediction-text-final-step](/resources/Storage/ai-hub/images/ai-hub-prediction-text-final-step.png)
11. Define the rules for the prediction model. This step includes two key configurations:
    After configuring the settings as required in the previous step, click Next to continue.
    ![ai-hub-prediction-text-final](/resources/Storage/ai-hub/images/ai-hub-prediction-text-final-new.png)
  - **Feedback Loop Configuration**: Specify the extent to which Human-in-the-Loop intervention is required during the data classification process. Based on your requirements, you can choose from the following options:
      ![ai-hub-prediction-document-rules-feedback](/resources/Storage/ai-hub/images/ai-hub-prediction-text-feedback.png)
      ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
      To learn more about Review Hub, refer [Review Hub](/articles/ai-hub/review-hub-text-model) topic.
    - **Always**: When the Feedback Loop Configuration is set to "Always", every generated prediction is routed for human validation. This validation is handled through the Review Hub, a built-in feature that provides an additional layer of oversight and ensures quality assurance.
    - **Never**: When the feedback loop configuration is set to "Never", the generated predictions bypass the Human-in-the-Loop process. As a result, no Review Hub activity is triggered, and all predictions are accepted without human validation.
    - **Confident**: When the feedback loop configuration is set to "Confident", a confidence threshold is defined for model predictions. If a prediction's confidence score falls below this threshold, the classified data is routed to the Review Hub for human validation. If the score meets or exceeds the threshold, the prediction is accepted without further review.
  - **Retention and Others**: In this section, you can configure the model to classify data into a default category when no specific category matches the new data.
      **Retention**: You can configure the data retention period to specify how long data is stored on the servers. Choose from predefined options—1 day, 5 days, 15 days, 25 days, or 30 days—or use the available slider to set a custom retention period between 1 and 30 days, based on your requirements. For more information, refer [Data Privacy and Retention](/articles/ai-hub/data-privacy-and-retention) topic.
      ![ai-hub-prediction-text-retention](/resources/Storage/ai-hub/images/ai-hub-prediction-text-retention-new.png)
12. The next step is training the model. Based on the uploaded data, review the text entries in the left panel and confirm their corresponding target categories in the right panel. Click Confirm for each entry. It's recommended to confirm at least 25 entries to help ensure accurate model training.
    This step is optional only if the categories are detected from the uploaded training data. In such cases, you may choose to skip category confirmation.
    However, if the categories were added manually, you are required to confirm which category each text entry belongs to by selecting from the list available on the right. This step is mandatory when categories are manually defined.
    ![ai-hub-prediction-text-start-training](/resources/Storage/ai-hub/images/ai-hub-prediction-text-start-training.png)

Upon completion, the newly created model will be listed on the Prediction page with the other available models, as illustrated in the image below:




 ![ai-hub-prediction-text-final-add](/resources/Storage/ai-hub/images/ai-hub-prediction-text-final-add.png)

## Advanced Configuration

The platform provides advanced configuration options to give you greater control when setting up target categories for a prediction model. These settings allow you to fine-tune various aspects of data preprocessing, model training, and performance evaluation. Use this section to tailor the prediction model to your specific requirements.

To configure these advanced options, follow the steps below:

1. In the Categories section, while creating the prediction model (as shown in the image below), click the Gear icon located at the top-right corner of the page.
    ![ai-hub-prediction-text-advanced-config](/resources/Storage/ai-hub/images/ai-hub-prediction-text-advanced-config.png)
2. Clicking the Gear icon opens the Advanced Configuration page, where you can set up various advanced options such as removing URLs, special characters, digits, stop words, and more from the text. To configure each option, select the appropriate column from the dropdown in the corresponding row of the configuration you wish to set up. Note: Multiple columns can be selected from the dropdown.
    ![ai-hub-prediction-text-advanced-config-setup](/resources/Storage/ai-hub/images/ai-hub-prediction-text-advanced-config-setup.png)
    **Option**
    **Description**
    Remove URL
    When enabled, this option removes URLs from the data fields selected in the column list in the drop-down. This feature is useful for filtering out spam links or non-essential data, helping to reduce the overall dataset size.
    For example, consider the following data row:
    "Assam, Dispur, Assamese, Tea, www.google.com".
    This row includes a URL.
    With the URL removal option enabled, the cleaned version of the data would be:
    "Assam, Dispur, Assamese, Tea"
    The URL (www.google.com) is excluded from the dataset, ensuring only relevant and structured information is retained.
    Remove special characters from text
    When enabled, this option removes special characters from the data fields selected in the column list in the drop-down.
    For example, consider the following data row:
    "Assam, Dispur, Assamese, Tea!".
    In this example, the field "Tea!" contains a special character (!).
    With the special character removal option enabled, the cleaned version of the data becomes:
    "Assam, Dispur, Assamese, Tea"
    The exclamation mark is removed, ensuring that only clean and relevant data is retained.
    Remove digits from text
    When enabled, this option removes digits from the data fields selected in the column list in the drop-down. This feature helps standardize and clean textual data by eliminating embedded numeric characters, which may be unnecessary or introduce noise into the dataset.
    For example, consider the following data row:
    "Assam, Dispur, Assamese, Tea4"
    In this example, the field "Tea4" contains a digit (4).
    With the remove digits from text option enabled, the cleaned version of the data becomes:
    "Assam, Dispur, Assamese, Tea"
    The digit is removed from the field, ensuring that only clean and relevant text is retained in the dataset.
    Remove stop words
    When enabled, this option removes stop words—such as articles, prepositions, and conjunctions—from the data fields selected in the column list in the drop-down.
    Removing these stop words can make text processing more efficient, as NLP algorithms don’t need to analyze commonly used words that add little to no value.
    For example, consider the following data row:
    "Assam, Dispur, Assamese, about Tea"
    In this example, the field "about Tea" contains the stop word "about".
    With the Remove Stop Words option enabled, the cleaned version of the data becomes:
    "Assam, Dispur, Assamese, Tea"
    The stop word is removed, ensuring that only meaningful and relevant text is retained in the dataset.
    Note: The stop words can be picked either from the default dictionary provided by NLP, or you can choose to add custom words.
    Perform Stemming
    When enabled, this option removes affixes from words in the data fields selected in the column list in the drop-down. This process, known as stemming, is a text preprocessing technique that normalizes words by converting them to their root form.
    For example, consider the following data row:
    "Assam, Dispur, Assamese, Tea, Thinking better"
    In this example, the phrase "Thinking better" contains the word "Thinking", which can be stemmed.
    With the Perform Stemming option enabled, the cleaned version of the data becomes:
    "Assam, Dispur, Assamese, Tea, Think better"
    The word "Thinking" is stemmed to "Think", ensuring that only base forms of relevant words are retained in the dataset.
    Perform Lemmatization
    When enabled, this option returns the words to their base or dictionary form in the data fields selected in the column list in the drop-down. This process, known as Lemmatization, is a text normalization technique that returns the words to the base or dictionary form. Lemmatization often relies on identifying the part of speech (noun, verb, etc.) of a word to determine its lemma.
    For example, consider the following data row:
    "Assam, Dispur, Assamese, Tea, Thinking running".
    In this example, the phrase "Thinking running" contains two words—"Thinking" and "Running"—that can be lemmatized.
    With the Perform Lemmatization option enabled, the cleaned version of the data becomes:
    "Assam, Dispur, Assamese, Tea, Think run".
    The words "Thinking" and "Running" are lemmatized to "Think" and "run" respectively, ensuring that only the dictionary forms of meaningful and relevant words are retained in the dataset.
    Regular expression pattern for text removal
    Regular expression patterns are a powerful tool in Natural Language Processing (NLP). When enabled, this option uses regular expressions to remove specific text from the data fields selected in the column list in the drop-down. This technique is widely used for filtering, normalizing, validating, and cleaning unnecessary text from the data.
    For example, consider the following data row:
    "Assam, Dispur, Assamese, Tea, https://help.example.com".
    In this example, the text includes a URL (https://help.example.com), which can be removed using a regular expression pattern.
    With the regular expression patter for text removal enabled, the cleaned version of the data becomes:
    "Assam, Dispur, Assamese, Tea".
    The link is removed, ensuring that only relevant and structured information remains in the dataset.
    Replacement string replacement
    When enabled, this option allows you to replace an old string with a new string in the data fields selected from the column list in the drop-down.
    You can specify the replacement in the format {"old" : "new"}, where the occurrences of the string defined as old will be replaced with the string defined as new.
    For example, consider the following data row:
    "Assam, Dispur, Assamese, Tea".
    In this example, the field "Tea" can be replaced with "Tourism" using the string replacement option. The updated data becomes:
    "Assam, Dispur, Assamese, Tourism"
    The string "Tea" is successfully replaced with "Tourism", and the dataset is updated accordingly.
    Remove extra white space
    When enabled, this option removes unnecessary whitespace from the data fields, helping to clean and standardize the text for further processing.
    For example, consider the following data row:
    "Assam, Dispur, Assamese, Tea, Think run ".
    In this example, the field "Think run " contains extra whitespace between and after the words.
    With the Remove Extra Whitespace option enabled, the updated data becomes:
    "Assam, Dispur, Assamese, Tea, Think run".
    The unnecessary spaces are removed, ensuring the dataset is clean and consistent.
    Maximum length of cleaned text
    This option allows you to specify the number of characters to retain in a data row when it is used for training the model. If the content exceeds the specified limit, the additional characters will be truncated.
    For example, consider the following data row:
    "Assam, Dispur, Assamese, Tea".
    If the maximum character limit is set to 50, and the data row exceeds this threshold, all characters beyond the 50th character will be truncated during preprocessing.
    Hyper Parameter Configuration
    In AI Hub, you can configure hyperparameters based on your specific requirements. Hyperparameter configuration refers to the process of setting external parameters that control the learning behavior of a model before training begins.
    ![ai-hub-prediction-text-adv-config-hyper-parameter](/resources/Storage/ai-hub/images/ai-hub-prediction-text-adv-config-hyper-parameter.png)
    These parameters influence the model’s performance, including its learning speed, and complexity. Some of the important parameters are discussed below:
    **Option**
    **Description**
    validation_split
    Specifies the portion of the training data to be used for validating the model. The value ranges from 0 to 1.
    For example, if set to 0.2, 20% of the training data will be used for validation to assess the model’s performance.
    preset
    Specifies the quality level for training the model. AI Hub offers three training options: "best_quality", "medium", and "highest". This setting determines the depth and precision of the training process. By default, it is set to "best_quality".
    training_time_limit
    Specifies the time limit for training the model, defined in seconds. By default, the value is set to 25000 seconds for the text prediction model. This value can be adjusted based on your requirements.
    optimization.patience
    Specifies the number of checks to be performed before stopping the training when no improvement is detected. The value is an integer, and by default, it is set to 25. This means that if there is no improvement after 25 consecutive checks, the training process will be stopped.
    optimization.val_check_interval
    Specifies how frequently the validation set is checked during a single training epoch. This can be defined using either a float or an integer value:
    optimization.top_k
    Based on the validation score, this setting determines how many of the top model checkpoints to use for model averaging. By default, it is set to 3. For example, if the value is set to 5, the top 5 checkpoints with the highest validation scores will be selected for model averaging.
    optimization.top_k_average_method
    Specifies the strategy used to average the top k model checkpoints. By default, it is set to greedy_soup.
    optimization.max_epochs
    Specifies the maximum number of training epochs. Training will stop once this number is reached. By default, the value is set to 10.
    For example, if set to 20, the model will train for 20 epochs.
    model.timm_image.checkpoint_name
    Select an image backbone architecture from the TIMM (PyTorch Image Models) library. The chosen backbone will be used as the feature extractor for the image model during training.
3. After setting the configurations, click the Save button at the bottom of the page to apply the changes.
