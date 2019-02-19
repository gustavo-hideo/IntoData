* # **Working with datasets in `data.world` - R**

`data.world` is a platform where you can find interesting data, store and showcase your own data and data projects, and find and collaborate with other members. In addition to exploring, querying and charting data on the data.world site, you can access data via 'API' endpoints and integrations. Use this package to access, query and explore data sets, and to publish your insights.


## **Library**
```r
#devtools::install_github("datadotworld/data.world-r", build_vignettes = TRUE)
library(tidyverse)
library(data.world)
```

## **Loading data.world configuration (API token)**
To manage your datasets using R (or any other language/tool) you need to get a token, that will be available in the **integrations** page at [data.world.com](https://data.world/integrations). <br><br>
The chunk bellow will save your configuration in the environment.
```r
#save_cfg <- data::world::save_config("YOUR_TOKEN")
data.world::set_config(saved_cfg)
```

## **Creating datasets into data.world**
```r
create_mtcars_dataset <- dwapi::dataset_create_request(
    title = "Mtcars dataset from R",
    visibility = "PRIVATE",
    license_string = "Other",
    description = "This dataset is used only as a demonstration",
    summary = "# Mtcars 
    This section supports markdown."
)

dwapi::create_dataset("owner_id", create_mtcars_dataset)
```

## **Creating files requests**
Uploading datasets using URL <br>
Files requests will be uploaded inside a project<br>
**If a file name already exist in the project, the file will be <span style="color:red">updated/overwritten</span>**
```r
create_mtcars_file <- dwapi::file_create_request(
    file_name = "cars.csv",
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data",
    description = "Mtcars from R",
    labels = list("raw data")
)
```

## **Creating a project**
```r
create_cars_project <- dwapi::project_create_request(
    title = "Cars project",
    visibility = "PRIVATE",
    license = "Other",
    objective = "Files with car's data",
    files = list(create_mtcars_file)
)

dwapi::create_project("owner_id", create_cars_project)
```


## **Loading datasets from data.world**
```r
project <- "project.URL"

data <- data.world::query(data.world::qry_sql("select * from file_name"),
    dataset = project)

glimpse(data)    
```
