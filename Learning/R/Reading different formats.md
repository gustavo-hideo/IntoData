# Reading different formats

## .zip
```r
temp <- tempfile()
downloader::download("file_path_or_web_address.tar.gz.zip", destfile = temp)
sales <- read.csv(unzip(temp, unzip = "internal"))
```

<br>
<br>

## .rar.gz
```r
fn <- "file_path_or_web_address.tar.gz"
download.file(fn,destfile = "tmp.tar.gz")
untar("tmp.tar.gz",list = TRUE)  ## check contents
untar("tmp.tar.gz")
```

<br>
<br>


## .dta
```{r}
haven::read_dta("path")
```
