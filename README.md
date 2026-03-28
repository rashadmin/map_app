# map_app

> An interactive dashboard visualizing Nigeria's power infrastructure, allowing users to explore substations, power plants, and mini-grids by state.

## 🧠 Overview

This project provides a web-based interactive map application built with Streamlit and Folium. Its primary purpose is to offer a clear visualization of Nigeria's power infrastructure, including the locations of substations, power plants, and mini-grids. Users can select specific states to filter and view relevant geographical data, aiding in the understanding of power distribution across the country.

## 🔨 What I Built

The application delivers a dynamic and filterable map experience. Key features include:

-   **Interactive Map Display:** Powered by Folium, presenting geospatial data on an zoomable and pannable map.
-   **State-Level Filtering:** Users can select a Nigerian state from a dropdown to focus the map on specific regions.
-   **Power Infrastructure Overlay:** Visualizes the locations of substations, power plants, and mini-grids within the selected state.
-   **Geospatial Data Processing:** Backend utilities handle the conversion of Well-Known Text (WKT) geometries, reprojecting Coordinate Reference Systems (CRS) (e.g., UTM to WGS84), and identifying administrative regions (LGAs and states) for given points.

## 💭 Thought Process

I decided to leverage Streamlit for the frontend due to its rapid development capabilities for data applications, allowing for quick creation of an interactive user interface with minimal code. For the mapping component, Folium was chosen for its ability to render interactive Leaflet maps directly within Python, providing a rich user experience for exploring geospatial data. GeoPandas was a natural fit for handling the underlying geospatial vector data, ensuring robust processing and manipulation of shapefiles and other geographical formats.

A key design choice was to structure the application with a dedicated utility file (`codes.py`) for core geospatial operations. This separation of concerns ensures that the mapping logic in `map.py` remains focused on presentation, while `codes.py` handles the complexities of CRS transformations, WKT parsing, and spatial joins against administrative boundaries. This modular approach enhances maintainability and readability. I specifically focused on Nigerian administrative boundaries, assuming the availability of specific local datasets, to provide a tailored solution for the project's scope.

## 🛠️ Tools & Tech Stack

| Layer      | Technology           |
|------------|----------------------|
| Language   | Python               |
| Web App    | Streamlit            |
| Mapping    | Folium, streamlit-folium |
| Geospatial | GeoPandas, Pyproj, Shapely |
| Data       | Pandas, NumPy        |

## 🚀 Getting Started

### Prerequisites
- Python 3.x

### Installation

```bash
git clone https://github.com/rashadmin/map_app.git
cd map_app
pip install -r requirements.txt
```
*(Note: A `requirements.txt` file is assumed to be present with all necessary dependencies listed.)*

### Run

```bash
streamlit run map.py
```

## 📖 Usage

After running the application, a web browser window will open displaying the interactive map.

### Interactive Map Dashboard

1.  **Select a State:** Use the dropdown menu on the sidebar to choose a Nigerian state.
2.  **View Infrastructure:** The map will automatically update to display substations, power plants, and mini-grids within the selected state.
3.  **Explore:** Zoom in, zoom out, and pan across the map to explore the geographical distribution of power infrastructure.

## 📚 Resources

-   [Streamlit Documentation](https://docs.streamlit.io/) — Building web applications with Python
-   [Folium Documentation](https://python-visualization.github.io/folium/) — Python wrapper for Leaflet.js
-   [GeoPandas Documentation](https://geopandas.org/en/stable/) — Geospatial data in Python
-   [Pyproj Documentation](https://pyproj4.github.io/pyproj/stable/) — CRS transformations
-   [Shapely Documentation](https://shapely.readthedocs.io/en/stable/manual.html) — Manipulation and analysis of geometric objects

## 📄 License

MIT © [rashadmin](https://github.com/rashadmin)
