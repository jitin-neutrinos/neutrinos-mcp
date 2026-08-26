# bh.system.pubSubService Resolver

<https://documentation.neutrinos.com/articles/#!service-designer-user-s-guide/system-pubsubservice>

The bh.system.pubSubService Service provides methods to publish and subscribe to events with various types of callbacks.

**Methods:**





 [$pub(event: string, eventObject?: any);](/articles/service-designer-user-s-guide/system-pubsubservice/a/pub)
 [$sub(event: string, callback?: (value: any) => void, error?: (error: any) => void, complete?: () => void): Subscription;](/articles/service-designer-user-s-guide/system-pubsubservice/a/sub)
 $pub(event: string, eventObject?: any);



 This method is used to publish an event with the data passed as eventObject.









 **Parameter**

 **Description**






 event

 The name of the event that is published.



 eventObject?

 Optional. The data to be sent to the subscriber of the event.









 **Return type: **void

 **Syntax:**


 Copy CodeJavaScript$pub(event: string, eventObject?: any); -> {}







 $sub(event: string, callback?: (value: any) => void, error?: (error: any) => void, complete?: () => void): Subscription;

 This method is used to subscribe to an event. It accepts callback, error, and complete as optional parameters.








 variable
 Description




 event
 The name of the subscribed event.

 callback
 Is called with the data that the event was published with. It is called once the subscribed event fires.


 errorUsed to handle the error (if any) that could have occurred while publishing the event.
completeChecks for completeness







 **Return type: **Subscription

 **Syntax:**


 Copy CodeJavaScript$sub(event: string, callback?: (value: any) => void, error?: (error: any) => void, complete?: () => Subscription); -> {}




 **Returns:**
 The subscription of the event.
