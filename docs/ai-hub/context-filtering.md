# Add Context Filter

<https://documentation.neutrinos.com/articles/#!ai-hub/context-filtering>

Context Filtering is the process of providing an **Assistant** with only the information that is relevant to its role and scope during invocation. Rather than supplying the entire available context, the system evaluates the request and filters the available information to include only the context required for the assistant to perform its assigned task effectively. This approach minimizes unnecessary context, improves response relevance, and optimizes overall efficiency.

| ![Note](/resources/Storage/ai-hub/project-trailproject/note.png) | **Note**: This feature is available only for linked Assistants. It is not supported for the primary Assistant, which orchestrates and coordinates the linked Assistants. |
| --- | --- |

## Add Context Filter

For linked assistants, this feature filters the user query before it is forwarded to the processing pipeline. It ensures that only the information relevant to the assistant's role and scope is passed for processing, while unnecessary or unrelated context is excluded. To add a context filter follow the below steps:

1. Navigate to Assistant from the left navigation pane. The Assistant page displays a list of all the assistants available on the platform.
2. From the list, search for and select the assistant that is linked to the primary assistant. The assistant opens. From the available assistant versions, select the required version. In the left navigation pane, click Context Filter.
    ![ai-hub-context-filtering-context-filter](/resources/Storage/ai-hub/images/ai-hub-context-filtering-context-filter.png)
3. Define the scope within which the assistant operates and specify the context from the user's prompt that the assistant is allowed to consider when processing requests and generating responses.
4. After defining the assistant's scope and allowed context, click Save at the bottom of the page. Then, publish the assistant.
5. Navigate to the main assistant listing page and select the primary assistant that invokes the linked assistants. Open the required version of the assistant and test it by entering a user prompt. If the prompt falls within the scope and allowed context of a linked assistant, the linked assistant processes the request and returns an appropriate response. Any portions of the prompt that fall outside the linked assistant's defined scope or allowed context are ignored and are not considered when generating the response.
6. You can verify the applied context filter in the Review Hub. Only the queries that fall within the linked assistant's defined scope and allowed context are listed in the Review Hub. Queries that fall outside the defined scope are not listed, indicating that they were excluded from processing. This confirms that the context filter has been applied successfully and that the assistant processes only the requests that are within its configured scope.
7. The following illustration demonstrates how context filtering works. In this example, a linked assistant is capable of computing the Fibonacci series and performing unit conversions. However, a context filter is configured to allow the assistant to process only Fibonacci-related requests.
    As a result, when the orchestrator forwards the user's prompt to the linked assistant, only the portions of the prompt that fall within the configured scope are included in the request. Any content outside the defined scope is filtered out and is not forwarded to the linked assistant. Therefore, the first part of the user's request, which asks for a unit conversion from minutes to hours, is not processed because it falls outside the configured scope. The second part of the request, which asks for the computation of the Fibonacci series, falls within the configured scope and is processed successfully. The corresponding response is then returned to the user.
    ![ai-hub-context-filtering-context-filter-applied-review-hub](/resources/Storage/ai-hub/images/ai-hub-context-filtering-context-filter-applied-review-hub.png)
