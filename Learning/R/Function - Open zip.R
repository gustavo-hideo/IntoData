# Function - Open ZIP



read_zip <- function(path){

    require(fs)
    require(downloader)
    require(sf)
    df <- fs::file_temp()
    uf <- fs::path_temp("zip")
    downloader::download(wells_path, df, mode = "wb") 
    unzip(df, exdir = uf)
    dat <- sf::read_sf(uf)
    fs::file_delete(df)
    fs::dir_delete(uf)
    dat
}

data <- read_zip(url_path)


