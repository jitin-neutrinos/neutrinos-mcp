# Advanced Configuration

<https://documentation.neutrinos.com/articles/#!ai-hub/text-extraction-model>

Text-Based Extraction on Neutrinos AI Hub enables intelligent retrieval of structured information from text files. Leveraging AI models and customizable pipelines, this feature allows users to automate the extraction of key data points—such as names, dates, invoice numbers, and other contextual information—without the need for extensive manual intervention. With Neutrinos AI Hub, users can configure, train, and deploy extraction models making it accessible for both developers and business users.

To create a text-based extraction model, follow the steps below:

1. Navigate to Extraction from the left navigation bar. On the Extraction landing page, go to the Text tab, then click the Add button located at the top-right corner of the page. On the following screen, click Get Started to begin. For the initial steps refer [Extraction](/articles/ai-hub/extraction) topic.
2. On the Create page, click Text to specify a text-based extraction model, then click Next. Use this option when your source data is structured text (e.g., CSV or Excel), and you want to extract fields from rows and columns.
    ![ai-hub-extraction-text-select](/resources/Storage/ai-hub/images/ai-hub-extraction-text-select1.png)
3. You will be prompted to upload a text file in either Excel or CSV format, which is required to train the model. Choose the appropriate file type based on your requirements, then click Next at the bottom of the page. For example, here, we have used Excel for illustration purposes.
    ![ai-hub-extraction-text-excel-select](/resources/Storage/ai-hub/images/ai-hub-extraction-text-excel-select.png)
4. Select a file from your local system to upload it to the platform for training the extraction model.
    ![ai-hub-extraction-text-browse-upload-file](/resources/Storage/ai-hub/images/ai-hub-extraction-text-browse-upload-file.png)
5. Once a file is selected from your local computer, click Continue at the bottom of the page.
    ![ai-hub-extraction-text-upload-success](/resources/Storage/ai-hub/images/ai-hub-extraction-text-upload-success.png)
    If an incorrect file is uploaded, you can remove it by clicking the delete (trash bin) icon next to the uploaded file. You can then upload a new file as needed.
6. In the next step, the information from the uploaded file is organized into columns, reflecting the structure of the original file. Review the data to ensure it is accurate. If the Excel sheet includes a header row with labels used for model training, you can choose to exclude it by selecting the Discard the First Row checkbox to remove the default column names provided by the platform such as column_1, column_2, and so on. By default, this checkbox is unchecked. Then, click the Next button at the bottom of the page to proceed.
    ![ai-hub-extraction-text-uploaded-information](/resources/Storage/ai-hub/images/ai-hub-extraction-text-uploaded-information1.png)
7. In the next step, add the categories that need to be extracted from the uploaded text document based on your requirements. Once the categories are added, click the Continue button at the bottom of the page. For example, as shown below, we have added categories to extract information such as State, Capital, Population, Literacy Rate, Area, Major Language Spoken, and Major Industry in a particular state in India.
    ![ai-hub-extraction-add-category.png](/resources/Storage/ai-hub/images/ai-hub-extraction-add-category.png)
8. In the next step, provide a name for the extraction model along with a brief description that outlines the purpose of the model. After entering the name and description, click Next to proceed.
    ![ai-hub-extraction-text-give-name-model](/resources/Storage/ai-hub/images/ai-hub-extraction-text-give-name-model.png)
9. Define the rules for the extraction model. This step includes two key configurations:
    After configuring the settings as required in the previous step, click Next to continue.
    ![ai-hub-extraction-text-configuration-next](/resources/Storage/ai-hub/images/ai-hub-extraction-text-configuration-next-new.png)
  - **Feedback Loop Configuration**: Specify the extent to which Human-in-the-Loop intervention is required during the data extraction process. This configuration must be done individually for each entity (category) added in the previous step. Based on your requirements, you can choose from the following options:
      ![ai-hub-extraction-text-feedback-config](/resources/Storage/ai-hub/images/ai-hub-extraction-text-feedback-config.png)
    - **Always**: When the Feedback Loop Configuration is set to "Always", every extraction is routed for human validation. This validation is handled through the Review Hub, a built-in feature that provides an additional layer of oversight and ensures quality assurance.
    - **Never**: When the feedback loop configuration is set to "Never", the extraction bypasses the Human-in-the-Loop process. As a result, no Review Hub activity is triggered, and all extractions are accepted without human validation.
    - **Confident**: When the feedback loop configuration is set to "Confident", a confidence threshold is defined for model extractions. If the model's confidence score falls below this threshold, the classified data is routed to the Review Hub for human validation. If the score meets or exceeds the threshold, the extraction is accepted without further review.
  - **Retention and Other**: You can configure the data retention period to specify how long data is stored on the servers. Choose from predefined options—1 day, 5 days, 15 days, 25 days, or 30 days—or use the available slider to set a custom retention period between 1 and 30 days, based on your requirements. For more information, refer [Data Privacy and Retention](/articles/ai-hub/data-privacy-and-retention) topic.
      ![ai-hub-extraction-text-retention](/resources/Storage/ai-hub/images/ai-hub-extraction-text-retention-new.png)
10. Tag the identifier in the right panel with the corresponding text data in the left panel, extracted from the uploaded text document. To tag the identifier, follow the steps below:
    ![ai-hub-tag-indentifiers-text-data](/resources/Storage/ai-hub/images/ai-hub-tag-indentifiers-text-data.gif)
  1. Click the identifier on the right panel.
  2. Click the text data on the left panel that corresponds to the selected identifier on the right. This action will tag the selected text with the chosen identifier.
  3. Repeat the above two steps to perform a minimum of 25 extractions required to train the model. Once 25 entries are completed, the Start Training button will appear at the bottom of the page. Click the Start Training button to begin training the model.

Upon completion, the newly created model will be listed on the Extraction page with the other available models, as illustrated in the image below:




 ![ai-hub-extraction-text-final](/resources/Storage/ai-hub/images/ai-hub-extraction-text-final.png)

## Advanced Configuration

The platform allows you to configure advanced options while setting up target categories for the extraction model. To configure these advanced options, follow the steps below:

1. In the Upload section, while creating the extraction model (as shown in the image below), click the Gear icon located at the top-right corner of the page.
    ![ai-hub-extraction-text-adv-config-gear](/resources/Storage/ai-hub/images/ai-hub-extraction-text-adv-config-gear.png)
2. Clicking the Gear icon opens the Advanced Configuration page, where you can set up various advanced options such as removing URLs, special characters from text, digits, stop words, and more from the text. To configure each option, enable the check box in the appropriate configuration you wish to set up.
    ![ai-hub-extraction-text-adv-config-page](/resources/Storage/ai-hub/images/ai-hub-extraction-text-adv-config-page.png)
    **Option
    **
    **
    Description**
    Remove URL
    When enabled, this option removes URLs from the data fields This feature is useful for filtering out spam links or non-essential data, helping to reduce the overall dataset size.
    For example, consider the following data row:
    "Assam, Dispur, Assamese, Tea, www.google.com".
    This row includes a URL.
    With the URL removal option enabled, the cleaned version of the data would be:
    "Assam, Dispur, Assamese, Tea"
    The URL (www.google.com) is excluded from the dataset, ensuring only relevant and structured information is retained.
    Remove special characters from text
    When enabled, this option removes special characters from the data fields.
    For example, consider the following data row:
    "Assam, Dispur, Assamese, Tea!".
    In this example, the field "Tea!" contains a special character (!).
    With the special character removal option enabled, the cleaned version of the data becomes:
    "Assam, Dispur, Assamese, Tea"
    The exclamation mark is removed, ensuring that only clean and relevant data is retained.
    Remove digits from text
    When enabled, this option removes digits from the data fields. This feature helps standardize and clean textual data by eliminating embedded numeric characters, which may be unnecessary or introduce noise into the dataset.
    For example, consider the following data row:
    "Assam, Dispur, Assamese, Tea4"
    In this example, the field "Tea4" contains a digit (4).
    With the remove digits from text option enabled, the cleaned version of the data becomes:
    "Assam, Dispur, Assamese, Tea"
    The digit is removed from the field, ensuring that only clean and relevant text is retained in the dataset.
    Remove stop words
    When enabled, this option removes stop words—such as articles, prepositions, and conjunctions—from the data fields.
    Removing these stop words can make text processing more efficient, as NLP algorithms don’t need to analyze commonly used words that add little to no value.
    For example, consider the following data row:
    "Assam, Dispur, Assamese, about Tea"
    In this example, the field "about Tea" contains the stop word "about".
    With the Remove Stop Words option enabled, the cleaned version of the data becomes:
    "Assam, Dispur, Assamese, Tea"
    The stop word is removed, ensuring that only meaningful and relevant text is retained in the dataset.
    Note: The stop words can be picked either from the default dictionary provided by NLP, or you can choose to add custom words.
    Perform Stemming
    When enabled, this option removes affixes from words in the data fields. This process, known as stemming, is a text preprocessing technique that normalizes words by converting them to their root form.
    For example, consider the following data row:
    "Assam, Dispur, Assamese, Tea, Thinking better"
    In this example, the phrase "Thinking better" contains the word "Thinking", which can be stemmed.
    With the Perform Stemming option enabled, the cleaned version of the data becomes:
    "Assam, Dispur, Assamese, Tea, Think better"
    The word "Thinking" is stemmed to "Think", ensuring that only base forms of relevant words are retained in the dataset.
    Perform Lemmatization
    When enabled, this option returns the words to their base or dictionary form in the data fields. This process, known as Lemmatization, is a text normalization technique that returns the words to the base or dictionary form. Lemmatization often relies on identifying the part of speech (noun, verb, etc.) of a word to determine its lemma.
    For example, consider the following data row:
    "Assam, Dispur, Assamese, Tea, Thinking running".
    In this example, the phrase "Thinking running" contains two words—"Thinking" and "Running"—that can be lemmatized.
    With the Perform Lemmatization option enabled, the cleaned version of the data becomes:
    "Assam, Dispur, Assamese, Tea, Think run".
    The words "Thinking" and "Running" are lemmatized to "Think" and "run" respectively, ensuring that only the dictionary forms of meaningful and relevant words are retained in the dataset.
    Regular expression pattern for text removal
    Regular expression patterns are a powerful tool in Natural Language Processing (NLP). When enabled, this option uses regular expressions to remove specific text from the data fields. This technique is widely used for filtering, normalizing, validating, and cleaning unnecessary text from the data.
    For example, consider the following data row:
    "Assam, Dispur, Assamese, Tea, https://help.example.com".
    In this example, the text includes a URL (https://help.example.com), which can be removed using a regular expression pattern.
    With the regular expression patter for text removal enabled, the cleaned version of the data becomes:
    "Assam, Dispur, Assamese, Tea".
    The link is removed, ensuring that only relevant and structured information remains in the dataset.
    Replacement string replacement
    When enabled, this option allows you to replace an old string with a new string in the data fields.
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
    ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
    Note: Although the options appear similar to those in the Text Prediction model, the operations in the Extraction model function at the row level, whereas in the Prediction model, the same operations apply at the column level.
    Hyper Parameter Configuration
    In AI Hub, you can configure hyperparameters based on your specific requirements. Hyperparameter configuration refers to the process of setting external parameters that control the learning behavior of a model before training begins.
    ![ai-hub-extraction-text-hyperparameter](/resources/Storage/ai-hub/images/ai-hub-extraction-text-hyperparameter.png)
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
    env.per_gpu_batch_size
    Specifies the batch size for each GPU.
    env.batch_size
    The batch size to use in each step of training. If env.batch_size is larger than env.per_gpu_batch_size * env.num_gpus, we accumulate gradients to reach the effective env.batch_size before performing one optimization step.
    optimization.max_epochs
    Specifies the maximum number of training epochs. Training will stop once this number is reached. By default, the value is set to 10.
    For example, if set to 20, the model will train for 20 epochs.
    optimization.top_k_average_method
    Specifies the strategy used to average the top k model checkpoints. By default, it is set to greedy_soup.
    model.hf_text.max_text_len
    Set the maximum text length: Different models support different maximum input lengths. If model.hf_text.max_text_len is set to a value greater than 0, the effective maximum length is determined by the lesser of model.hf_text.max_text_len and the model’s inherent maximum limit. If model.hf_text.max_text_len is set to 0 or a negative value, the model’s default maximum length will be used.
    model.hf_text.text_trivial_aug_maxscale
    Set the maximum percentage of text tokens for data augmentation: For each text token sequence, a random percentage is sampled from the range [0, model.hf_text.text_trivial_aug_maxscale]. One of four trivial augmentation operations is then randomly selected—synonym replacement, random word swap, random word deletion, or random punctuation insertion—and applied to the sampled proportion of tokens.
    model.ner_text.checkpoint_name
    Specifies the foundational model on which training is performed. Users can choose a valid model name from Hugging Face to serve as the starting point for training or fine-tuning. The selected model name must be compatible with the task and follow the naming conventions used in the Hugging Face model hub (e.g., bert-base-uncased, roberta-large, distilbert-base-cased, etc.).
3. After setting the configurations, click the Save button at the bottom of the page to apply the changes.
    ![ai-hub-extraction-text-adv-config-page-save-btn](/resources/Storage/ai-hub/images/ai-hub-extraction-text-adv-config-page-save-btn.png)
