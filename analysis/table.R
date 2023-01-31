library('tidyverse')

df_input <- read_csv(
  here::here("output", "input.csv"),
  col_types = cols(patient_id = col_integer(),age = col_double())
)

dftab <- as.data.frame(table(df_input$region))
write_csv(dftab, path=here::here("output","table.csv"))

#write_csv(df_ethSex, path=here::here("output","tab_ethSex.csv"))
