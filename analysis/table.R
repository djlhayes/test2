library('tidyverse')

df_input <- read_csv(
  here::here("output", "input.csv"),
  col_types = cols(patient_id = col_integer(),age = col_double())
)
#defining all variable types will make code run faster when there are lots of variables 

dftab <- as.data.frame(table(df_input$sex, df_input$ethnicity))
write_csv(dftab, path=here::here("output","table.csv"))

#write_csv(df_ethSex, path=here::here("output","tab_ethSex.csv"))

