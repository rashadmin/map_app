# map_app

> An interactive web dashboard for visualizing Nigeria's power infrastructure on a map.

## 🧠 Overview

This project provides an interactive web application built with Streamlit and Folium for exploring geographical data related to Nigeria's power sector. It allows users to visualize the distribution of substations, power plants, and mini-grids across Nigerian states and local government areas (LGAs), helping to understand the existing infrastructure.

## 🔨 What I Built

I built a dynamic and interactive mapping application that serves as a visual exploration tool for Nigeria's power infrastructure. Its core features include:

-   **Interactive Map Visualization:** Displays geographical data using Folium, allowing users to pan, zoom, and interact with map features.
-   **State-level Filtering:** Users can select a specific Nigerian state from a dropdown menu to focus the map on that region.
-   **Power Infrastructure Overlay:** Overlays critical power assets such as substations, power plants, and mini-grids on the map.
-   **Geospatial Data Utilities:** Includes backend utilities for handling and transforming geospatial data, converting between different Coordinate Reference Systems (CRS), and identifying administrative boundaries.

## 💭 Thought Process

My approach to building this application involved leveraging specialized libraries for web development, mapping, and geospatial data processing. I chose Streamlit for the user interface due to its rapid development capabilities and ease of creating interactive dashboards. For the mapping component, Folium was the clear choice, offering powerful interactive map rendering capabilities that integrate well with Python.

A key architectural decision was to separate the geospatial utility functions into `codes.py`. This modular design allows for clean, reusable code for tasks like converting Well-Known Text (WKT) geometries and reprojecting data, which are crucial for accurately displaying diverse geographic datasets. GeoPandas was instrumental in handling the vector data for states, LGAs, and power assets, making spatial operations straightforward.

One of the challenges involved ensuring accurate CRS transformations and efficient spatial joins to correctly locate power infrastructure within administrative boundaries. The application's design prioritizes user interaction by allowing state-level filtering, which significantly enhances the exploration of detailed infrastructure data without overwhelming the user with too much information at once.

## 🛠️ Tools & Tech Stack

| Layer             | Technology                 |
|-------------------|----------------------------|
| Language          | Python 3.x                 |
| Web Framework     | Streamlit                  |
| Mapping           | Folium, streamlit-folium   |
| Geospatial Data   | GeoPandas, Pyproj, Shapely |
| Data Manipulation | Pandas, NumPy              |

## 🚀 Getting Started

### Prerequisites
- Python 3.8+

### Installation

```bash
git clone https://github.com/rashadmin/map_app.git
cd map_app
pip install -r requirements.txt
```

### Run

```bash
streamlit run map.py
```

## 📖 Usage

Once the application is running, open your web browser to the provided local URL (usually `http://localhost:8501`).

1.  **Select a State:** Use the dropdown menu in the sidebar to choose a Nigerian state.
2.  **Explore the Map:** The map will automatically update to display the selected state's boundaries along with the locations of substations, power plants, and mini-grids within that state.
3.  **Interact:** Zoom in, zoom out, and pan across the map to explore the infrastructure in detail.

## 📚 Resources

- [Streamlit Documentation](https://docs.streamlit.io/) — Web application framework
- [Folium Documentation](https://python-visualization.github.io/folium/) — Interactive mapping library
- [GeoPandas Documentation](https://geopandas.org/en/stable/) — Geospatial data handling
- [Pyproj Documentation](https://pyproj4.github.io/pyproj/stable/) — CRS transformations
- [Shapely Documentation](https://shapely.readthedocs.io/en/stable/manual.html) — Geometric objects

## 📄 License

MIT © [rashadmin](https://github.com/rashadmin)
