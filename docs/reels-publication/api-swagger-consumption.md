# API/Swagger Consumption

<https://documentation.neutrinos.com/articles/#!reels-publication/api-swagger-consumption>

**API documentation for product rules execution**

1. After creating a product, navigate to product info.
2. Deploy the product.
   A product token is generated as shown below.
   ![](/resources/Storage/reels-publication/api-swagger-consumption/prodtoken.png)
3. Download swagger.
4. Import the downloaded file using Swagger Editor.
5. Verify the following:
   - Verify the Server URL. The server URL is provided below
    ![](/resources/Storage/reels-publication/api-swagger-consumption/serverurl.png)
   - Check the request body to confirm if the Product ID, Product Version and Input objects are being displayed.
6. Execute the API and verify the result.
   After the API is executed, a run id is generated.
7. Paste the run id within the exec response.
8. Verify the response and confirm if all the outputs are displayed correctly.
