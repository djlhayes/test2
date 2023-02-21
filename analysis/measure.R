library('tidyverse')
library("ggplot2")
library('dplyr')
library('lubridate')

df <- read_csv(
  here::here("output", "measures", "measure_admissions_by_age_cat.csv"),
  col_types = cols_only(
    
   
    age_cat = col_number(),
    
    admitted  = col_number(),
    population  = col_number(),
    value = col_number(),
    
    date = col_date(format="%Y-%m-%d")
    
  ),
  na = character()
  )

  plot_age_cat <- ggplot(admitted, aes(x=date))

  ggsave(
    plot=plot_age_cat,
    filename="plot_age_cat.jpeg", path=here::("output")
  )