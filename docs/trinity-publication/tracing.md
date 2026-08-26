# Tracing

<https://documentation.neutrinos.com/articles/#!trinity-publication/tracing>

The tracing feature in Trinity empowers you to actively monitor API behavior. It encompasses details pertaining to the calls initiated by your APIs. For instance, if your application is not performing as expected, you can capture all the API calls sent and received by the application.

![](/resources/Storage/trinity-publication/tracing/Readtraces.png)

The description and usage of each available component are provided below:

**Traces**

Traces represent the whole journey of a request as it moves through all the nodes of a distributed system. Traces help developers alike in understanding the end-to-end journey of a request, from its initial entry point to all the different services it touches, and finally to its completion.

**Spans**

Spans actively capture work as it happens on a service. For example they record events like a web server's response to an HTTP request or the execution of a single function, marking both their start and end times. These timed intervals, known as spans, join together to form a single trace within distributed tracing.

Spans branch out in a tree-like structure, each tethered to a parent. The trace acts as the tree, while spans form its branches. A parent span, also called a root span, takes charge of measuring the end-to-end latency of an entire request. Child spans, triggered by their parent spans, represent actions like function calls, database interactions, or calls to other services. By assembling all the spans within a trace, you gain a detailed, step-by-step account of a request's performance throughout its entire lifecycle.

To View Tracing details related to an application:

1. Navigate to Applications link within Trinity and click on the required app.
   ![](/resources/Storage/trinity-publication/tracing/navigate2.png)
   Note: Tracing data is available only for deployed applications.
   The navigation link to tracing is displayed.
   ![](/resources/Storage/trinity-publication/tracing/Data.png)
2. Click on the Tracing link.
   The tracing page is displayed.
   ![](/resources/Storage/trinity-publication/tracing/Readtraces.png)
3. To view the desired tracing data:
   - Select an environment from the drop-down list.
   - The version is default.
   - Select the type of operation.
   - Set the limit from the drop-down list.
   - Select the required time range.
    - To customize the time range enter the custom range - Enter the values in dd-mm-yy format - To set an end time enable the toggle button.
   ![](/resources/Storage/trinity-publication/tracing/Tracing-1.png)
4. Click on the Apply button to view the tracing data.

####
