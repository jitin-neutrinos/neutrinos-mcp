# CheatSheet

<https://documentation.neutrinos.com/articles/#!studio-guide-9/cheatsheet>

Here are a few hacks/cheatsheet items to use on Studio:

Call any node's functionality in the **Script** node using this.<functionName>() where the functionName of the node can be accessed from its attribute window.

 **Example 1: **This is how you call the function name of the node called closeDialogWindow in a **Script** node. The node you are calling should always be part of a flow that starts with any start node.


 ![function name of the node](/resources/Storage/studio-guide-9/close_dialog_funcname.png)


 ![Calling node function name in the script node](/resources/Storage/studio-guide-9/script_page.png)


 **Example 2:** This is how you use [Angular NgZone](https://angular.io/guide/zone) to call another flow:


 You import the NgZone module using the [Use Dependency](/smart/project-page-services-designer-guide/use-dependency-node) node:


 ![Importing the NgZone module](/resources/Storage/studio-guide-9/import%20ngzone.png)


 Call another flow using the imported module:


 ![Calling another flow](/resources/Storage/studio-guide-9/ngzone%20script.png)





 Access the page variables in the User Interface of the page and in the** Script** node using page.<pageVariable>.

 For example, this is how you assign value to the page variable called data in the **Script **node:


 ![Calling page variable in the Script node](/resources/Storage/studio-guide-9/page_data.png)


 This is how you access a page variable in the HTML editor of the HTML5 component:


 ![Accessing the page variable from the component attribute](/resources/Storage/studio-guide-9/page_h3.png)



 Call a client service flow anywhere in a page using __serviceInvoker__.invoke('<service_id>', '<functionName>', <arg1>, <arg2>). Where,


 The service_id can be accessed from the application folder's /designs/services/<service_name>.json file.

 ![Service ID](/resources/Storage/studio-guide-9/service_id.png)




 The functionName can be accessed from the attributes window of the Start node of the client service flow.


 arg1, arg2, etc. are the arguments passed to the **Start** node of the client service flow. These are the input variables that were defined in the **Start** node of that client service flow.



 For example, this is how you call the client service flow from a **Script** node:

 ![Calling a client low from the script node](/resources/Storage/studio-guide-9/script_client.png)





 Add Angular pipes to any component attribute to which you can bind a property or a flow. To learn about the types of Angular pipes supported on Studio and see a few examples, navigate to the [Angular documentation](https://angular.io/guide/pipes).

 For example, this is how you add title casing to the content of a Toolbar:



 ![Title casing the content of Toolbar](/resources/Storage/studio-guide-9/toolbar_titlecase.png)
