library('tidyverse')

df_input <- read_csv(
  here::here("output", "input.csv"),
  col_types = cols(patient_id = col_integer(),age = col_double())
)

plot_age <- ggplot(data=df_input, aes(df_input$age,fill=sex)) + 
geom_histogram() +
labs (title = "Age Distribution",
x = "Age (years)")

ggsave(
  plot= plot_age,
  filename="descriptive.png", path=here::here("output"),
)

plot_age_region <- ggplot(data=df_input, aes(df_input$age,fill=region)) + 
geom_histogram() +
labs (title = "Age Distribution",
x = "Age (years)")

ggsave(
  plot= plot_age_region,
  filename="descriptive2.png", path=here::here("output"),
)

plot_age_ethnicity <- ggplot(data=df_input, aes(df_input$age,fill=ethnicity)) +
geom_histogram() +
labs (title = "Age by ethnicity",
x = "Age (years)")

ggsave(
  plot= plot_age_ethnicity,
  filename="descriptive3.png", path=here::here("output"),
)





