import streamlit as st
import gspread as gsp
import pandas as pd
from df2gspread import df2gspread as d2g
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


# Authorising the code with the client key
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json')
gc = gsp.authorize(credentials)

st.title("Preliminary List Automation")
st.write("Refer to the side bar on the left")
st.sidebar.title("Points to remember")
st.sidebar.write("1. Don't forget to change the edit access before pasting the link")
st.sidebar.write("2. Giving the same name to a sheet will modify an existing sheet for a given workbook")
# Give the user options to choose from the list of courses
final_select = st.selectbox("All Courses",["CS","MIS","BA","DS","MEM"]) 

# Give the user input fields for
    # GPA
    # GRE
    # WORK-EX

gpa = st.number_input("Enter student GPA")
gre = st.number_input("Entet student GRE score")
work = st.number_input("Enter the work experience in years")

link_to_user_sheet = st.text_input("Please paste the URL of the students Google Sheet only")
name_of_sheet = st.text_input("Enter the name you wish to give this sheet")
# Code to strip the sheet_ID

sheet_Id = link_to_user_sheet.split('/')[5] if link_to_user_sheet != '' else link_to_user_sheet
submit = st.button("Submit")

# Computer Science
if submit:
    if final_select == "CS":
        st.text("You choose Computer Science")
        gpa_weight = 0.75
        gre_weight = 0.15
        work_weight = 0.1

        score = (gpa_weight * gpa) + (gre_weight * gre) + (work_weight * work)
        if score >= 55:
            st.text("The student is excellent!")
            df = pd.read_csv('./computer_science/Computer_Science_Masters_List - EXCELLENT_PROFILE.csv', index_col=False)
            d2g.upload(df, gfile=sheet_Id, col_names=True, credentials=credentials, wks_name=name_of_sheet)
        elif (score >= 53) and (score < 55):
            st.text("The student is good!")
            df = pd.read_csv('./computer_science/Computer_Science_Masters_List - GOOD_PROFILE.csv', index_col=False)
            d2g.upload(df, gfile=sheet_Id, col_names=True, credentials=credentials, wks_name=name_of_sheet)
        elif (score >= 50) and (score < 53):
            st.text("The student is average")
            df = pd.read_csv('./computer_science/Computer_Science_Masters_List - AVERAGE_PROFILE.csv', index_col=False)
            d2g.upload(df, gfile=sheet_Id, col_names=True, credentials=credentials, wks_name=name_of_sheet)
        else:
            st.text("You know what to do!")
            df = pd.read_csv('./computer_science/Computer_Science_Masters_List - POOR_PROFILE.csv', index_col=False)
            d2g.upload(df, gfile=sheet_Id, col_names=True, credentials=credentials, wks_name=name_of_sheet)
# Mangagement Information Systems and Software Engineering

    if final_select == "MIS":
        st.text("You choose Management Information Systems and Software Engineering")
        gpa_weight = 0.6
        gre_weight = 0.15
        work_weight = 0.25

        score = (gpa_weight * gpa) + (gre_weight * gre) + (work_weight * work)
        if score >= 55:
            st.text("The student is excellent!")
            df = pd.read_csv('./information_systems/MIS - MIS-Excellent.csv',index_col=False)
            d2g.upload(df, gfile=sheet_Id, col_names=True, credentials=credentials, wks_name=name_of_sheet)
        elif (score >= 52) and (score < 55):
            st.text("The student is good!")
            df = pd.read_csv('./information_systems/MIS - MIS-Good.csv',index_col=False)
            d2g.upload(df, gfile=sheet_Id, col_names=True, credentials=credentials, wks_name=name_of_sheet)
        elif (score >= 49) and (score < 51):
            st.text("The student is average")
            df = pd.read_csv('./information_systems/MIS - MIS-Average.csv',index_col=False)
            d2g.upload(df, gfile=sheet_Id, col_names=True, credentials=credentials, wks_name=name_of_sheet)
        else:
            st.text("You know what to do!")
            df = pd.read_csv('./information_systems/MIS - MIS-Poor.csv',index_col=False)
            d2g.upload(df, gfile=sheet_Id, col_names=True, credentials=credentials, wks_name=name_of_sheet)
        
# Business Analytics

    if final_select == "BA":
        st.text("You choose Business Analytics")
        gpa_weight = 0.6
        gre_weight = 0.15
        work_weight = 0.25

        score = (gpa_weight * gpa) + (gre_weight * gre) + (work_weight * work)
        if score >= 55:
            st.text("The student is excellent!")
            df = pd.read_csv('./business_analytics/Business Analytics - BA-Excellent.csv',index_col=False)
            d2g.upload(df, gfile=sheet_Id, col_names=True, credentials=credentials, wks_name=name_of_sheet)
        elif (score >= 52) and (score < 55):
            st.text("The student is good!")
            df = pd.read_csv('./business_analytics/Business Analytics - BA-Good.csv',index_col=False)
            d2g.upload(df, gfile=sheet_Id, col_names=True, credentials=credentials, wks_name=name_of_sheet)
        elif (score >= 49) and (score < 51):
            st.text("The student is average")
            df = pd.read_csv('./business_analytics/Business Analytics - BA-Average.csv',index_col=False)
            d2g.upload(df, gfile=sheet_Id, col_names=True, credentials=credentials, wks_name=name_of_sheet)
        else:
            st.text("You know what to do!")
            df = pd.read_csv('./business_analytics/Business Analytics - BA-Poor.csv',index_col=False)
            d2g.upload(df, gfile=sheet_Id, col_names=True, credentials=credentials, wks_name=name_of_sheet)

# Data Science

    if final_select == "DS":
        st.text("You choose Data Science")
        gpa_weight = 0.6
        gre_weight = 0.25
        work_weight = 0.15

        score = (gpa_weight * gpa) + (gre_weight * gre) + (work_weight * work)
        if score >= 86:
            st.text("The student is excellent!")
            df = pd.read_csv('./data_science/Data_Science - DS-Excellent.csv',index_col=False)
            d2g.upload(df, gfile=sheet_Id, col_names=True, credentials=credentials, wks_name=name_of_sheet)
        elif (score >= 84) and (score < 86):
            st.text("The student is good!")
            df = pd.read_csv('./data_science/Data_Science - DS-Good.csv',index_col=False)
            d2g.upload(df, gfile=sheet_Id, col_names=True, credentials=credentials, wks_name=name_of_sheet)
        elif (score >= 79) and (score < 84):
            st.text("The student is average")
            df = pd.read_csv('./data_science/Data_Science - DS-Average.csv',index_col=False)
            d2g.upload(df, gfile=sheet_Id, col_names=True, credentials=credentials, wks_name=name_of_sheet)
        else:
            st.text("You know what to do!")
            df = pd.read_csv('./data_science/Data_Science - DS-Poor.csv',index_col=False)
            d2g.upload(df, gfile=sheet_Id, col_names=True, credentials=credentials, wks_name=name_of_sheet)

# Engineering Management

    if final_select == "MEM":
        st.text("You choose Engineerig Management")
        gpa_weight = 0.75
        gre_weight = 0.10
        work_weight = 0.15

        score = (gpa_weight * gpa) + (gre_weight * gre) + (work_weight * work)
        if score >= 39:
            st.text("The student is excellent!")
            df = pd.read_csv('./engineering_management/Engineering Management - MEM-Excellent.csv',index_col=False)
            d2g.upload(df, gfile=sheet_Id, col_names=True, credentials=credentials, wks_name=name_of_sheet)
        elif (score >= 38) and (score < 39):
            st.text("The student is good!")
            df = pd.read_csv('./engineering_management/Engineering Management - MEM-Good.csv',index_col=False)
            d2g.upload(df, gfile=sheet_Id, col_names=True, credentials=credentials, wks_name=name_of_sheet)
        elif (score >= 35) and (score < 38):
            st.text("The student is average")
            df = pd.read_csv('./engineering_management/Engineering Management - MEM-Average.csv',index_col=False)
            d2g.upload(df, gfile=sheet_Id, col_names=True, credentials=credentials, wks_name=name_of_sheet)
        else:
            st.text("You know what to do!")
            df = pd.read_csv('./engineering_management/Engineering Management - MEM-Poor.csv',index_col=False)
            d2g.upload(df, gfile=sheet_Id, col_names=True, credentials=credentials, wks_name=name_of_sheet)

# Industrial Engineering

    # if final_select == "IE":
    #     st.text("You choose Industrial Engineering")
    #     gpa_weight = 0.75
    #     gre_weight = 0.10
    #     work_weight = 0.15

    #     score = (gpa_weight * gpa) + (gre_weight * gre) + (work_weight * work)
    #     if score >= 39:
    #         st.text("The student is excellent!")
    #         df = pd.read_csv('./industrial_engineering/')
    #         d2g.upload(df, gfile=sheet_Id, col_names=True, credentials=credentials, wks_name=name_of_sheet)
    #     elif (score >= 38) and (score < 39):
    #         st.text("The student is good!")
    #         df = pd.read_csv('./industrial_engineering/')
    #         d2g.upload(df, gfile=sheet_Id, col_names=True, credentials=credentials, wks_name=name_of_sheet)
    #     elif (score >= 35) and (score < 38):
    #         st.text("The student is average")
    #         df = pd.read_csv('./industrial_engineering/')
    #         d2g.upload(df, gfile=sheet_Id, col_names=True, credentials=credentials, wks_name=name_of_sheet)
    #     else:
    #         st.text("You know what to do!")
    #         df = pd.read_csv('./industrial_engineering/')
    #         d2g.upload(df, gfile=sheet_Id, col_names=True, credentials=credentials, wks_name=name_of_sheet)

