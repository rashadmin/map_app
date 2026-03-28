# Nigeria Power Infrastructure Map

> Interactive visualization and exploration of Nigeria's power sector assets.

## 🧠 Overview

This project provides an interactive web application built with Streamlit and Folium for visualizing critical power infrastructure across Nigeria. It allows users to explore the distribution of substations, power plants, and mini-grids, offering a geographical understanding of the country's power sector challenges and opportunities.

## 🔨 What I Built

The application delivers a dynamic, map-centric view of Nigeria's power landscape. Key features include:

-   An interactive map displaying the geographical locations of power substations, plants, and mini-grids.
-   The ability to filter and zoom into specific Nigerian states, providing a detailed view of infrastructure within selected administrative boundaries.
-   Integration of administrative boundary data for states and Local Government Areas (LGAs) to provide context for the infrastructure.
-   Utility functions for robust geospatial data handling, including conversion of Well-Known Text (WKT) geometries, Coordinate Reference System (CRS) transformations (e.g., UTM to WGS84), and spatial queries to identify points within specific LGAs or states.

## 💭 Thought Process

My approach focused on creating an accessible and informative tool for spatial data analysis of Nigeria's power infrastructure. I chose **Streamlit** for its rapid development capabilities, enabling the swift creation of an interactive web dashboard without extensive front-end development.

For the mapping component, **Folium** was the natural choice due to its strong integration with Python and its ability to render highly interactive Leaflet maps. This allowed for seamless display of geospatial data layers and user interaction.

**GeoPandas** was fundamental for all geospatial data manipulation and processing. It provided the necessary tools to handle shapefiles, perform spatial joins, and manage different geometric types. To ensure data accuracy and compatibility, a dedicated utility file (`codes.py`) was created to abstract complex geospatial operations, such as WKT string parsing and critical CRS transformations using `pyproj`. This separation of concerns made `map.py` cleaner and more focused on the Streamlit application logic. Challenges included ensuring accurate geographical alignment across diverse datasets and optimizing spatial queries for performance, especially when dealing with Nigeria's numerous administrative boundaries.

## 🛠️ Tools & Tech Stack

| Layer          | Technology            |
|----------------|-----------------------|
| Language       | Python 3.x            |
| Web Framework  | Streamlit             |
| Mapping        | Folium, streamlit-folium |
| Geospatial     | GeoPandas, Pyproj, Shapely |
| Data           | Pandas, NumPy         |

## 🚀 Getting Started

### Prerequisites
-   Python 3.8+ (or a compatible version for the libraries)

### Installation

```bash
git clone https://github.com/rashadmin/map_app.git
cd map_app
pip install -r requirements.txt
```

*Note: A `requirements.txt` file needs to be created based on the `Tools & Tech Stack` above for these commands to work directly. If not, install each library individually.*

Example `requirements.txt` content:
```
streamlit
streamlit-folium
folium
geopandas
pyproj
shapely
pandas
numpy
```

### Run

To launch the interactive map application:

```bash
streamlit run map.py
```

## 📖 Usage

Once the application is running, your web browser will automatically open to the Streamlit interface.

### Interacting with the Map

-   **State Selection:** Use the dropdown menu on the sidebar to select a specific Nigerian state. The map will automatically filter and zoom to display the power infrastructure within that state.
-   **Map Navigation:** Pan and zoom around the map using standard controls to explore different regions.
-   **Data Layers:** Observe the overlaid markers representing substations, power plants, and mini-grids.

## 📚 Resources

-   [Streamlit Documentation](https://docs.streamlit.io/) — Build interactive web apps
-   [Folium Documentation](https://python-visualization.github.io/folium/) — Python interactive mapping
-   [GeoPandas Documentation](https://geopandas.org/en/stable/) — Geospatial data in Python
-   [Pyproj Documentation](https://pyproj4.github.io/pyproj/stable/) — CRS transformations
-   [Shapely Documentation](https://shapely.readthedocs.io/en/stable/manual.html) — Manipulation and analysis of geometric objects

## 📄 License

MIT © [rashadmin](https://github.com/rashadmin)
