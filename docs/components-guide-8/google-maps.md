# Google Maps

<https://documentation.neutrinos.com/articles/#!components-guide-8/google-maps>

## Google Maps

### Overview

The Google Map component allows maps to be embedded on third-party websites and offers a locator for businesses and other organizations in numerous countries around the world.

### How to use

1. Navigate to [Neutrinos Store](https://store.neutrinos.co/) and download the **Google Maps** component.
2. Once downloaded, the component gets installed on Neutrinos Studio and shows up in the palette list. Drag and drop a component from the palette list to the page.
3. In the TypeScript editor of the page where you dropped the Google Maps component, add the following code inside the constructor class:
4. Copy CodeMarkdown constructor(httpClient: HttpClient) {
    super();
    this.apiLoaded = httpClient.jsonp('https://maps.googleapis.com/maps/api/js?key=AIzaSyDrg99Fl3VR8x7c-_PjrJ2dLhg7O0rhi7E', 'callback')
    .pipe(
    map(() => true),
    catchError(() => of(false)),
    );
    }
5. To use this component, you should generate an API Key. See [https://developers.google.com/maps/documentation/javascript/get-api-key](https://developers.google.com/maps/documentation/javascript/get-api-key)
6. Save and run the application.

### Associated Attributes

- **Google Map Label**: The display name for the component.
- **Style**:  It accepts a string value and affects different properties (height, width, color, etc.) of the component based on the values provided (example- background: orange; height:200px;).
- **Class**: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The "Class" attribute accepts space-separated class names (example- class1 class2) which are defined in the Style tab as shown below.
    CSS
    .class1 {
   border-radius:10px;
   flex-basis:10%;
   height:100px;
   }
   .class2 {
   border-radius:10px;
   flex-basis:10%;
   height:100px;
   }
- **[height]**: The height along the y-axis, in pixels.
- **[width]: **The width along the x-axis, in pixels.
- **[center]:** The center of the Circle.
- **[zoom]: **The maximum zoom level for the map display.
- **[options]: **Sets a collection of key-value pairs.
- **(boundsChanged): **This event is fired when the viewport bounds have changed.
- **(centerChanged):** This event is fired when the map center property changes.
- **(mapClick): **This event is fired when the user clicks on the map.
- **(mapDblClick): **This event is fired when the user double-clicks on the map. Note that the **click **event will fire, before this event.
- **(mapDrag): **This event is repeatedly fired while the user drags the map.
- **(mapDragend): **This event is fired when the user stops dragging the map.
- **(mapDragstart): **This event is fired when the user starts dragging the map.
- **(mapMousemove): **This event is fired whenever the user's mouse moves over the map container.
- **(mapMouseout): **This event is fired when the user's mouse exits the map container.
- **(mapMouseover): **This event is fired when the user's mouse exits the map container.
- **(mapRightclick): **This event is fired when the user clicks on the map.
- **(zoomChanged): **This event is fired when the map's zoom property changes.

### Other Properties

These properties are unique to each component:

#### Map Bicycling Layer

A layer that displays bike lanes and paths and demotes large roads.

#### Map Circle

Creates a circle using the passed Circle options that specify the center, radius, and style.

- **[center]:** The center of the circle.
- **[radius]: **The radius in meters on the Earth's surface.
- **[options]: **Sets a collection of key-value pairs.
- **(centerChanged): **This event is fired when the circle's center is changed.
- **(circleClick): **This event is fired when the DOM click event is fired on the circle.
- **(circleDblClick): **This event is fired when the DOM dblclick event is fired on the circle.
- **(circleDrag): **This event is repeatedly fired while the user drags the circle.
- **(circleDragend): **This event is fired when the user stops dragging the circle.
- **(circleDragstart): **This event is fired when the user starts dragging the circle.
- **(circleMouseDown):** This event is fired when the DOM mouse down event is fired on the circle.
- **(circleMousemove): **This event is fired when the DOM mouse move event is fired on the circle.
- **(circleMouseout): **This event is fired on circle mouse out.
- **(circleMouseover): **This event is fired on circle mouseover.
- **(circleMouseup):** This event is fired when the DOM mouse up event is fired on the circle.
- **(radiusChanged): **This event is fired when the circle's radius is changed.
- **(circleRightclick):** This event is fired when the circle is right-clicked on.

#### Map Ground Overlay

Creates an OverlayView.

- **[URL]: **Gets the URL of the projected image.
- **[bounds]: **Gets the bounds of this overlay.
- **(mapClick): **This event is fired when the DOM click event is fired on the GroundOverlay.

#### Map KML Layer

Creates a KML (Keyhole Markup Language) Layer which renders the contents of the specified KML/KMZ file.

- **[URL]: **Gets the URL of the KML file being displayed.
- **[options]: **Sets a collection of key-value pairs.
- **[kmlClick): **This event is fired when a feature in the layer is clicked.

#### Map info Window

Creates an info window with the given options.

- **[options]: **Sets a collection of key-value pairs.
- **[position]: **The Latitude and Longitude at which to display this InfoWindow. If the InfoWindow is opened with an anchor, the anchor's position will be used instead.
- **(closeClick): **This event is fired when the close button was clicked.
- **(positionChanged): **This event is fired when the position property changes.

#### Map Marker

Creates a marker with the options specified. If a map is specified, the marker is added to the map upon construction. Note that the position must be set for the marker to display.

- **label: **label of the Marker.
- **[options]:** Sets a collection of key-value pairs.
- **[position]: **Set the position for the Marker.
- **[title]: **Set the title of the Marker tooltip.
- **(mapClick)**: This event is fired when the Marker icon was clicked.
- **(clickableChanged)**: This event is fired when the Marker clickable property changes.
- **(cursorChanged):** This event is fired when the Marker cursor property changes.
- **(mapDblclick): **This event is fired when the Marker icon was double-clicked.
- **(mapDrag):** This event is repeatedly fired while the user drags the Marker.
- (**mapDragend)**: This event is fired when the user stops dragging the Marker.
- **(draggableChanged)**: This event is fired when the Marker draggable property changes.
- **(mapDragstart):** This event is fired when the user starts dragging the Marker.
- **(flatChanged):** This event is fired when the Marker flat property changes.
- **(mapMousedown):** This event is fired for a mouse down on the Marker.
- **(mapMouseout): **This event is fired when the mouse leaves the area of the Marker icon.
- **(mapMouseover): **This event is fired when the mouse enters the area of the Marker icon.
- **(mapMouseup):** This event is fired for a mouseup on the Marker.
- **(positionChanged)**: This event is fired when the Marker position property changes.
- **(mapRightclick):** This event is fired for a click on the Marker.
- **(titleChanged)**: This event is fired when the Marker title property changes.
- **(visibleChanged)**: This event is fired when the Marker visible property changes.

#### Map Polygon

Create a polygon using the passed Polygon Options, which specify the polygon's path, the stroke style for the polygon's edges, and the fill style for the polygon's interior regions.

- **[options]: **Sets a collection of key-value pairs.
- **[paths]: **Retrieves the path.
- **(polygonClick): **This event is fired when the DOM click event is fired on the Polygon.
- **(polygonDblclick): **This event is fired when the DOM dblclick event is fired on the Polygon.
- **(polygonDrag): **This event is repeatedly fired while the user drags the polygon.
- **(polygonDragend): **This event is fired when the user stops dragging the polygon.
- **(polugonDragstart): **This event is fired when the user starts dragging the polygon.
- **(polygonMousedown): **This event is fired when the DOM mouse down event is fired on the Polygon.
- **(polygonMousemove): **This event is fired when the DOM mouse move event is fired on the Polygon.
- **(polygonMouseout): **This event is fired on Polygon mouse out.
- (**polygonMouseover):** This event is fired on Polygon mouseover.
- **(polygonMouseup):** This event is fired when the DOM mouse up event is fired on the Polygon**.**
- **(polygonRightclick): **This event is fired when the Polygon is right-clicked on.

#### Map Polyline

Create a polyline using the passed PolylineOptions, which specify both the path of the polyline and the stroke style to use when drawing the polyline.

- **[options]: **Sets a collection of key-value pairs.
- **[paths]: **Retrieves the path.
- **(polylineClick):** This event is fired when the DOM click event is fired on the Polyline.
- **(polylineDblclick): **This event is fired when the DOM dblclick event is fired on the Polyline.
- **(polylineDrag): **This event is repeatedly fired while the user drags the polyline.
- **(polylineDragend): **This event is fired when the user stops dragging the polyline.
- **(polylineDragstart):** This event is fired when the user starts dragging the polyline.
- **(polylineMousedown): **This event is fired when the DOM mouse down event is fired on the Polyline.
- **(polylineMousemove): **This event is fired when the DOM mouse move event is fired on the Polyline.
- **(polylineMouseout): **This event is fired on Polyline mouse out.
- **(polylineMouseover): **This event is fired on Polyline mouse over.
- **(polylineMouseup)**: This event is fired when the DOM mouse up event is fired on the Polyline.
- **(polylineRightclick): **This event is fired when the Polyline is right-clicked on.

#### Map Rectangle

Create a rectangle using the passed Rectangle Options, which specify the bounds and style.

- **[options]: **Sets a collection of key-value pairs.
- **[bounds]: **Returns the bounds of this rectangle.
- **(boundsChanged):** This event is fired when the rectangle's bounds are changed.
- **(rectangleClick): **This event is fired when the DOM click event is fired on the rectangle.
- **(rectangleDblclick): **This event is fired when the DOM dblclick event is fired on the rectangle.
- **(rectangleDrag): **This event is repeatedly fired while the user drags the rectangle.
- **(rectangleDragend): **This event is fired when the user stops dragging the rectangle.
- **(rectangleDragstart): **This event is fired when the user starts dragging the rectangle.
- **(rectangleMousedown): **This event is fired when the DOM mouse down event is fired on the rectangle.
- **(rectangleMousemove):** This event is fired when the DOM mousemove event is fired on the rectangle.
- **(rectangleMouseout): **This event is fired on the rectangle mouse out.
- **(rectangleMouseover): **This event is fired on the rectangle mouse over.
- **(rectangleMouseup): **This event is fired when the DOM mouse up event is fired on the rectangle.
- **(rectangleRightclick): **This event is fired when the rectangle is right-clicked on.

#### Map Traffic Layer

A layer that displays current road traffic.

- **[autoRefresh]: **Whether the traffic layer refreshes with updated information automatically.

#### Map Transit Layer

A layer that displays transit lines.
