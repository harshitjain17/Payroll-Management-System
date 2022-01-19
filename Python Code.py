from sqlalchemy import create_engine
import pandas as pd
import datetime
import subprocess

cnx = create_engine(&#39;mysql+pymysql://root:123@localhost:3306/payroll&#39;).connect()
def emp_entry():
  ec = eval(input(&quot;Enter employee code : &quot;))
  fn = input(&quot;Enter First Name of Employee: &quot;)
  ln = input(&quot;Enter Last Name of Employee: &quot;)
  dg = input(&quot;Enter Designation : &quot;)
  ge=input(&quot;Enter Gender : &quot;)
  db = input(&quot;Enter Date of Birth : &quot;)
  dj = input(&quot;Enter Date of Joining : &quot;)
  mb =input(&quot;Enter Mobile Number : &quot;)
  pn =input(&quot;Enter PAN Number : &quot;)
  ac= input(&quot;Enter Bank Account Number: &quot;)
  fc = input(&quot;Enter IFSC code of Bank Account : &quot;)
  sl = eval(input(&quot;Enter Pay Level : &quot;))
  bs=eval(input(&quot;Enter Basic Salary: &quot;))
  ta=eval(input(&quot;Enter Transport Allowance : &quot;))
  hr=input(&quot;Enter employee is Eligible for HRA Y/N : &quot;)
  np=input(&quot;Enter employee is Eligible for NPS Y/N : &quot;)
  data = [[ec, fn, ln, dg, sl, ge, db, dj, mb, pn, ac, fc,bs,ta,hr,np]]
  df = pd.DataFrame(data,columns=[&#39;ecode&#39;,&#39;fname&#39;, &#39;lname&#39;, &#39;desig&#39;, &#39;level&#39;, &#39;gender&#39;,&#39;dob&#39;,&#39;doj&#39;,&#39;mob&#39;,&#39;pan&#39;,&#39;acno&#39;,&#39;ifsc&#39;,&#39;basic&#39;,&#39;ta&#39;,&#39;hrayn&#39;,&#39;npsyn&#39;])
  df.to_sql(name = &#39;emp&#39;, con = cnx, if_exists = &#39;append&#39;, index = False)

def per_setter() :
  dap=eval(input(&quot;Enter DA Percentage : &quot;))
  hrp=eval(input(&quot;Enter HRA Percentage: &quot;))
  data = [[dap,hrp]]
  df = pd.DataFrame(data,columns=[&#39;dap&#39;,&#39;hrap&#39;])
  df.to_sql(name = &#39;setter&#39;, con = cnx, if_exists = &#39;replace&#39;, index = False)

def salary_entry():
  while True:
  try:
    y = eval(input("Enter the salary year (press enter for current year otherwise input new year:" + str(datetime.datetime.today().strftime(&#39;%Y&#39;))))
  except:
    y = str(datetime.datetime.today().strftime(&#39;%Y&#39;))
    break

  while True:
  try:
    m = eval(input("Enter the salary month (press enter for current month otherwise input new month:" + str(datetime.datetime.today().strftime(&#39;%m&#39;))))
  except:
    m = str(datetime.datetime.today().strftime(&#39;%m&#39;))
    break

sql="select * from emp &quot;
df=pd.read_sql(sql,cnx)
print(&quot;enter salary details for the &quot; + str(m) + &quot;/&quot; + str(y))

lec=[]
llevel=[]
lec = df[&quot;ECODE&quot;]
l1=[]
ly = []
lm = []
allw = []
deduc = []
lfee = []
it = []
for x in df[&quot;ECODE&quot;]:
print(&quot;Employee Code : &quot; + str(x) + &quot;\n&quot;)
l1.append(eval(input(&quot;Enter No of days worked : &quot;)))
allw.append(eval(input(&quot;Enter other allowance (or 0): &quot;)))
deduc.append(eval(input(&quot;Enter other deductions (or 0): &quot;)))
it.append(eval(input(&quot;Enter income tax to be deducted (or 0): &quot;)))
lfee.append(eval(input(&quot;Enter other License fee (or 0): &quot;)))
ly.append(y)

lm.append(m)
sql=&quot;select * from pay&quot;
df1=pd.read_sql(sql,cnx)
df1[&quot;YEAR&quot;] = ly
df1[&quot;MONTH&quot;] = lm
df1[&quot;ECODE&quot;] = lec
df1[&quot;NODAYS&quot;] = l1
df1 = pd.merge(df,df1,on=&#39;ECODE&#39;)
df1[&quot;BASIC&quot;] = df1[&quot;BASIC&quot;]/30 * df1[&quot;NODAYS&quot;]
df1[&quot;DA&quot;] = df1[&quot;BASIC&quot;] * DP/100
df1[&quot;DATA&quot;] = df1[&quot;TA&quot;] * DP /100
df1[&quot;HRA&quot;] = df1[&quot;TA&quot;] * HP /100
df1[&quot;NPS_M&quot;] = (df1[&quot;BASIC&quot;] + df1[&quot;DA&quot;] ) * 10 /100
df1[&quot;OTHER_ALLW&quot;] = allw
df1[&quot;GROSS&quot;] = df1[&quot;BASIC&quot;] + df1[&quot;DA&quot;] + df1[&quot;DATA&quot;] + df1[&quot;HRA&quot;] + df1[&quot;NPS_M&quot;] + df1[&quot;OTHER_ALLW&quot;]
df1[&quot;NPS_O&quot;] = df1[&quot;NPS_M&quot;]
df1[&quot;GPF&quot;] = df1[&quot;BASIC&quot;] * 6/100
df1[&quot;LCFEE&quot;] = lfee

df1[&quot;ITAX&quot;] = it
df1[&quot;ODEDUCT&quot;] = deduc
df1[&quot;TOTAL_DEDUC&quot;] = df1[&quot;ITAX&quot;] + df1[&quot;NPS_M&quot;] + df1[&quot;NPS_O&quot;] + df1[&quot;GPF&quot;] + df1[&quot;ODEDUCT&quot;] +
df1[&quot;LCFEE&quot;]
df1[&quot;NETSAL&quot;] = df1[&quot;GROSS&quot;] - df1[&quot;TOTAL_DEDUC&quot;]
df1.to_csv(&#39;C:\Payroll\SALARY.csv&#39;, mode = &#39;w&#39;)

def Date_operations():
x = datetime.datetime.today().strftime(&#39;%Y-%m-
%d&#39;) print(x)
def Sdf_show():
df = pd.read_csv(&#39;c:\payroll\salary.csv&#39;)
print(df)

def Show_Rates():
sql = &quot;select * from setter&quot;
df = pd.read_sql(sql, cnx)
print(df)

def Show_EMP():

sql = &quot;select * from EMP&quot;
df = pd.read_sql(sql, cnx)

print(df)

def Salary_show():
subprocess.call(&#39;C:\Program Files\Microsoft Office\Office15\excel c:\payroll\salary.csv&#39;)

DP=0
HP=0
sql=&quot;select * from setter&quot;
df=pd.read_sql(sql,cnx)
DP = df[&quot;dap&quot;][0]
HP = df[&quot;hrap&quot;][0]
while (True):
print(&quot;1 : Add EMPOYEE DETAILS&quot;)
print(&quot;2 : SHOW EMPOYEE DETAILS&quot;)
print(&quot;3 : FIX DA AND HRA RATES&quot;)

print(&quot;4 : SHOW CURRENT DA AND HRA RATES&quot;)
print(&quot;5 : PAYBILL ENTRY &quot;)
print(&quot;6 : SHOW PAYBILL&quot;)
print(&quot;7 : SHOW PAYBILL (CSV FILE IN EXCEL)&quot;)
print(&quot;8 : Exit&quot;)
choice = int(input(&quot;Please Select An Above Option: &quot;))
if(choice == 1):
emp_entry()
elif (choice==2):
Show_EMP()
elif (choice==3):
per_setter()
elif (choice==4):
Show_Rates()
elif (choice==5):
salary_entry()
elif (choice == 6):
Sdf_show()

elif (choice == 7):
Salary_show()
elif (choice == 8):
break
else:
print(&quot; Wrong choice..........&quot;)
