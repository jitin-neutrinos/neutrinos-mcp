# Import Client Services to the Page UI

<https://documentation.neutrinos.com/articles/#!studio-guide-7/import-client-services-to-the-page-ui>

After creating a client service, you should **import** the service and **inject** the service into the constructor of an application page.

To use the input and local properties in an application page, you have to **import** the relevant service (the service in which you have declared these properties) to that page. For example, in this screenshot, a service named **c****alculator** is created:![](/resources/Storage/studio-guide-7/project-server-side-service-designer/calculator.png)To access the input and local properties of the **c****alculator **service in the **i****ndex** page of the app, perform the following steps:**Import** the service to the page:![](/resources/Storage/studio-guide-7/project-server-side-service-designer/import_service.png)

- **Inject** the **calculator** service in the constructor of the page:

Copy CodeJavaScriptconstructor(private bdms: NDataModelService, private calc: calculator)
 {
 // your code here
 }

Now, you can call any flow that you have created in client services by using the calc property of the page. For example, to access the **s****ubtraction** flow, use calc.subtraction(). Every flow when called will return the bh. object on success.You can then use the bh object to access the client services properties. For example:Copy CodeJavaScriptthis.result = this.calc.calculator(Number(this.first), Number(this.second), $event).then(bh => {
 console.log(bh);
 this.result = bh.local.result;
 });
