# Download the Base App

<https://documentation.neutrinos.com/articles/#!tutorial-integrate-your-app-with-apis/download-import>

### Download the Base App

The Weather app is used to display the weather data for a city based on user inputs. You will be updating this app to integrate with the external API provider.

- To create the weather app in Neutrinos studio version **6.0.0 to 6.1.0**, download the base app from [here](/resources/Storage/tutorial-integrate-your-app-with-apis/weather.nos).
- To create the weather app in Neutrinos Studio version **6.1.x to 7.0.1**, download the base app from [here](/resources/Storage/tutorial-integrate-your-app-with-apis/weatherdevsoft.nos).
- To create the weather app in Neutrinos Studio version **7****.0.2 or later, ** see our l[atest](/articles/tutorial-create-your-first-app/title) tutorial.

---

### Import the App to Studio

1. Open Neutrinos Studio.
2. Click ![](/resources/Storage/tutorial-integrate-your-app-with-apis/import_app.png)on the Studio home page, and select the downloaded base app from your local machine.
3. The app gets imported to the Studio.

| ![Warning](/resources/Storage/tutorial-integrate-your-app-with-apis/warning.png) | This app is built on Neutrinos Studio version 6.0.3. If you are using a later version of Neutrinos Studio, migrate the app to the latest version by clicking ![](/resources/Storage/tutorial-integrate-your-app-with-apis/ota_icon.png) on the app card. After migrating the app, follow manual migration steps (if any) mentioned in the [Migration guide](http://docs1.neutrinos.co/articles/neutrinos-studio-migration-guide). |
| --- | --- |

---

### Explore the App

Click the app to open its Application page and explore the existing elements.

#### Pages

Click the **Pages** option on the Studio Application page to see the app pages.

![Pages in the weather app](/resources/Storage/tutorial-integrate-your-app-with-apis/weather_pages.png)

The app will display the following pages:

- **weathersearch:** This page provides the UI for the user to input the city name for which the weather details have to be fetched. Also, notice that the **weathercard** and **log **view is added to the **weathersearch** page. See [Reuse Pages using Views](/smart/project-sample-how-to-guide/views) for more details.

![weather search page](/resources/Storage/tutorial-integrate-your-app-with-apis/Tutweathersearch.png)

- **weathercard:** This page is used to create a weather card that shows the weather information returned from the **Openmapweather** API provider.

![Weather card page](/resources/Storage/tutorial-integrate-your-app-with-apis/tutweathercarrd.png)

- **log: **This page is used to log the success and failure of the API call while fetching the weather data.

![Log page](/resources/Storage/tutorial-integrate-your-app-with-apis/tutlog.png)

#### Styles

Click the **Styles** option on the Studio Application page to view the app styling. The following CSS styling is set for the app pages and its components:

Copy CodeCSS/*Importing default angular material css theme. */

@import "~@angular/material/prebuilt-themes/deeppurple-amber.css";
@import "nDefaults.scss";
body {
 padding: 5px;
}
* {
 box-sizing: border-box;
 font-family: Roboto,"Helvetica Neue",sans-serif;
}

mat-grid-tile {
 background: #b9c6d8;
 border-radius: 4px;
}

.weathers {
 padding: 0 5px;
}

.weather-card {
 border: 2px solid rgba(0, 0, 0, 0.12);
 border-radius: 15px;
 width: 500px;
}

mat-card-title {
 font-weight: bold;
}

.get-weather-button {
 color: white !important;
 background: #343438 !important;
}

#### Data Model

Click the **Models **option on the Studio Application page menu bar to view the data models.

The **logobject** data model is created as follows. This data model determines the logical structure of the logged data.

![Data models](/resources/Storage/tutorial-integrate-your-app-with-apis/datamodelWA.png)

#### Routes

Click the **Routes** tab to view the app navigation. On deployment, routes enable navigation from one page to another as a user performs various tasks using the application.

![Routes page](/resources/Storage/tutorial-integrate-your-app-with-apis/routes.png)
