
library("ggplot2", lib.loc="~/R/win-library/3.5")
library("readr", lib.loc="~/R/win-library/3.5")
data <- read_csv("/Users/hand/Desktop/education_data-master/bin/Student_Teacher_Ratio_with_AVG_Teacher_Rate.csv")
ggplot(data, aes(x=student_teacher_ratio, y=avg_teacher_rate)) + geom_point(alpha=0.5)
