#  Indian Census Data Analysis (Python)

This project presents an **exploratory data analysis (EDA)** of Indian Census data, focusing on villages and towns across India.  
The goal is to understand population distribution, area coverage, household counts, density patterns, and gender ratios using Python-based data analysis techniques.



## Dataset Overview

The dataset contains aggregated census-level information, including:
- Number of villages and towns
- Population (male & female)
- Area (in sq. km)
- Households
- Inhabited vs uninhabited villages

The data is sourced from publicly available **Indian Census records** and stored in CSV format.



##  Objectives of the Project

- Clean and preprocess raw census data  
- Derive meaningful metrics for better insights  
- Perform statistical analysis to identify trends and anomalies  
- Visualize patterns using graphs and charts  



##  Tools & Libraries Used

- **Python**
- **Pandas & NumPy** – Data manipulation
- **Matplotlib & Seaborn** – Data visualization
- **SciPy** – Statistical analysis (Z-score, T-test)


##  Key Features & Analysis

###  Data Cleaning
- Handled missing values
- Standardized column names
- Converted data types where required

### Feature Engineering
Derived new columns such as:
- **`real_density`** → Population / Area  
- **`sex_ratio`** → Females per 1000 males  
- **`inhabited_percentage`** → % of inhabited villages  

###  Visualizations
- Correlation heatmap
- Bar charts & pie charts
- Scatter plots
- Histograms & box plots

###  Statistical Analysis
- Outlier detection using **Z-score**
- **T-test** to compare male vs female population distributions



##  Sample Insights

- Population density varies significantly between villages and towns  
- Certain regions show extreme density outliers  
- Gender ratio patterns differ across habitation types  

*(Exact results depend on dataset values and visual interpretation)*



## 🚀 How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/GANDEEDRAMESH/indian-census-data-analysis.git
