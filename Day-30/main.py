##################### Hard Starting Project ######################
import smtplib
import datetime as dt
import pandas
import random

my_email = "siv23shiva@gmail.com"
password = "qihu kjjx mbwk vfua"
recivor_mail = "shivashiva100000@gmail.com"

now = dt.datetime.now()
today = (now.month,now.day)


data = pandas.read_csv("E:/Python Udemy/Day-32/birthday wishes mail/letter_templates/birthdays.csv")
birthday_dict = {(data_row["month"],data_row["day"]):data_row for (index , data_row) in data.iterrows()}
if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"E:/Python Udemy/Day-32/birthday wishes mail/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        contents = content.replace("[NAME]",birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday\n\n{content}")




