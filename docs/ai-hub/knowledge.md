# Knowledge

<https://documentation.neutrinos.com/articles/#!ai-hub/knowledge>

A knowledge source provides information that the assistant uses to respond to user queries. It serves as the foundation for delivering accurate and relevant answers. While it is not mandatory to add a knowledge source, doing so significantly improves the precision and context-awareness of the assistant's responses.


 The landing page displays information about the available knowledge sources that have already been added to the platform, presented in a tabular format as illustrated in the image below:




 ![knowledge-source-landing-page-table](/resources/Storage/ai-hub/images/knowledge-source-landing-page-table.png)

1. **File Name**: Displays the name of the knowledge source that has been added or is currently available in the platform.
2. **Type**: Displays the source type used to create the knowledge source—either an Excel file, another document format (e.g., PDF, Word), or a webpage.
3. **Status**: Displays the outcome of the knowledge source creation process. Shows Imported if the creation was successful or Failed if the operation was unsuccessful.
4. **Created Data**: Displays the creation date and timestamp for a specific knowledge source available on the platform.
5. **Action**: This column contains a kebab menu icon (three vertical dots) that allows you to delete a specific knowledge source, provided it is not currently being used by the assistant.

To add a knowledge source in the platform , follow the steps below:

1. Click Knowledge on the left-hand side navigation bar to open the **Knowledge Source** panel.
    ![knowledge-landing-page](/resources/Storage/ai-hub/images/knowledge-landing-page.png)
2. Click the **Add Source** button in the top-right corner of the page to open a pop-up window. This window allows you to choose from multiple upload options for adding a knowledge source to the platform.
    ![knowledge-add-source](/resources/Storage/ai-hub/images/knowledge-add-source.png)
    You can upload content from an Excel file, a document (e.g., Word or PDF), or a webpage URL.
    ![knowledge-choose-source-type](/resources/Storage/ai-hub/images/knowledge-choose-source-type.png)
3. If you choose Excel or a document file in the previous step, you will be prompted to browse and upload a file from your local computer.
    ![knowledge-excel-file-options](/resources/Storage/ai-hub/images/knowledge-excel-file-options.png)
    If you selected Webpage, you will be asked to enter the name and URL of the webpage. Additionally, you can specify whether the assistant should also scroll through subpages to extract knowledge from linked content.
    ![knowledge-web-page-source](/resources/Storage/ai-hub/images/knowledge-web-page-source.png)
4. After uploading an Excel file or any other document, you will be prompted to provide a name for the knowledge source. This name helps identify and manage the source within the platform.
    ![knowledge-excel-file-name](/resources/Storage/ai-hub/images/knowledge-excel-file-name.png)
5. Click the Add Source button to confirm and add the selected knowledge source to the platform.
    ![knowledge-excel-file-add-source](/resources/Storage/ai-hub/images/knowledge-excel-file-add-source.png)

After completing all the above steps, the knowledge source with the provided name will appear on the landing page.

After you create a Knowledge Source, refer the [Set Knowledge Source](/articles/ai-hub/toolsets/a/h2_1158915101) section under Toolsets to link it to the Assistant.
