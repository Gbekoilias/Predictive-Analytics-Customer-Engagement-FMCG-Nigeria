# Load necessary libraries
library(ggplot2)
library(lavaan)

# Import survey data
data <- read.csv("../data/survey_data.csv")

# Conduct Regression Analysis
model <- lm(Sales.Growth ~ Customer.Retention.Rate + Predictive.Analytics.Usage, data = data)
summary(model)

# Structural Equation Modeling (SEM)
sem_model <- ' 
  Sales.Growth ~ Customer.Retention.Rate + Predictive.Analytics.Usage
'
fit <- sem(sem_model, data = data)
summary(fit)
