import pandas
data=pandas.read_csv("squl.csv")
squ=data.Age
value=squ.to_list()
adult_count=len(data[data.Age=="Adult"])
juven_count=len(data[data.Age=="Juvenile"])
data_dict={
"gender":["adult","juven"],
"count": [adult_count,juven_count]
}
print(data_dict)
data1=pandas.DataFrame(data_dict)
data1.to_csv("adult.csv")

