# Create New Extraction Model

<https://documentation.neutrinos.com/articles/#!ai-hub/extraction>

Extraction is used to configure and deploy AI models that identify and extract specific data points from documents such as PDFs, scanned forms, or image-based records. These models are designed to recognize and retrieve key information such as names, dates, reference numbers, and more. This process transforms unstructured or semi-structured text into structured, actionable data.

In AI Hub, Extraction supports the full lifecycle of an entity extractor—from uploading training data to training, evaluation, and continuous improvement. It enables teams to automate high-volume data extraction processes with accuracy and efficiency. Whether it's for form processing, invoice reading, or claims automation, Extraction models help reduce manual effort and ensure consistent, reliable results.

Click Extraction in the left navigation bar to open the Extraction landing page.




 ![ai-hub-extraction-landing-page](/resources/Storage/ai-hub/images/ai-hub-extraction-landing-page1.png)


 The information related to the available models are presented in a tabular format. The details are organized under the following columns:

1. **Extraction Name**: Displays the name of the extraction model as defined during its creation.
2. **Description**: Displays the description of the model as provided during its creation.
3. **Update Date and Time**: Displays the date and time when the extraction model was last updated.
4. **Actions**: This column contains a kebab menu icon. Clicking it reveals an option to delete the corresponding extraction model.
5. The caret icon at the end of each row allows users to expand the corresponding extraction model entry. When expanded, it reveals additional details such as the available versions of the model, its current status, the author who created it, the last updated date and time, and a kebab menu icon that includes a delete option.

The page is organized into two primary tabs:

- **Text**: Displays models configured for text-based extractions such as classification or intent detection.
- **Document**: Displays models configured for document-based extractions such as information extraction or form understanding.

Use the search bar to locate specific models by name, or use the status filter to narrow down the list based on the workflow stage.

## Create New Extraction Model

To create a new extraction model, follow the steps below:

1. Click Extraction in the left navigation bar to open the Extraction page.
2. On the Extraction page, click the Add button in the top-right corner to begin setting up a new Extraction.
    ![ai-hub-extraction-add-button](/resources/Storage/ai-hub/images/ai-hub-extraction-add-button1.png)
3. A configuration page opens, displaying a detailed step-by-step outline of the process. Click the Get Started button at the bottom of the page to proceed.
    ![ai-hub-extraction-get-started](/resources/Storage/ai-hub/images/ai-hub-extraction-get-started.png)
4. Select the type of data on the create page that the extraction model will be based on. It can be either text (Excel file or CSV) or a document (PDF, image, or other formats).
    ![ai-hub-extraction-model-types](/resources/Storage/ai-hub/images/ai-hub-extraction-model-types.png)
5. To create a Text based extraction model, see the [Text Extraction Model](/articles/ai-hub/text-extraction-model) topic.
6. To create a Document based extraction model, see the [Document Extraction Model](/articles/ai-hub/document-extraction-model) topic.
