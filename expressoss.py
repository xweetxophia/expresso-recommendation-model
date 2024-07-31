import pandas as pd
import streamlit as st
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import pypickle

#load the model
loaded_model = pypickle.load('expresso.pkl')


#create a function that called prediction that will take in cfunctions entered by the users

def prediction(data):
    
 #create a dataframe for the data
   df= pd.DataFrame(data)

#convert the categorical columns to numerical
   label = LabelEncoder()
# create a list of the categorical colum
   cat_cols = [0,1,2,14,16]

   for i in cat_cols:
        df.iloc[i] = label.fit_transform(df.iloc[1])

#create a variable that will convert the data to a numpy array
   num_data = df.drop([0, 10, 11, 12, 13]).values.reshape(1,-1)

   scalar= StandardScaler()
   num_data = scalar.fit_transform(num_data)

#predicting the model
   pred = loaded_model.predict(num_data)

   if pred[0] == 0:
        return "The client will not churn"
   else:
        return "The client will churn"

def main():
      st.markdown("""<style>body{background-color: #FFC0CB;}</style>""",unsafe_allow_html=True)
      st.image("pretty.jpg")
      st.title("Expresso Churn Prediction Model")
      user_id = st.number_input("Please enter your ID no: ")
      REGION = st.selectbox("Please enter your region: ",
      ('FATICK', 'DAKAR', 'LOUGA', 'TAMBACOUNDA', 'KAOLACK', 'THIES',
       'SAINT-LOUIS', 'KOLDA', 'KAFFRINE', 'DIOURBEL', 'ZIGUINCHOR',
       'MATAM', 'SEDHIOU', 'KEDOUGOU'))
      TENURE = st.radio("Please select your tenure: ",('9-12 months', '12-15 months', '15-18 months', '18-21 months', '21 -24 months', '> 24 months'))
      MONTANT = st.number_input("Please enter your top-up amount: ")
      FREQUENCE_RECH = st.number_input("Please enter the number of times you refilled: ")
      REVENUE = st.number_input("How much do you earn monthly?: ")
      ARPU_SEGMENT = st.number_input("Please enter your income over 90days/3: ")
      FREQUENCE = st.number_input("Please enter the number of times you made an income: ")
      DATA_VOLUME = st.number_input("Please enter the number of connections: ")
      ON_NET = st.number_input ("How many inter Expresso calls did you make? ")
      ORANGE = st.number_input ("How many calls did you make to Orange: ")
      TIGO = st.number_input ("How many calls did you make to Tigo: ")
      ZONE1 = st.number_input ("How many calls did you make to zone 1: ")
      ZONE2 = st.number_input ("How many calls did you make to zone 2: ")
      MRG = st.radio("Are you going? select yes or no ", ("yes" , "no"))
      REGULARITY = st.number_input("Please enter the numbe of times you have been active in the last 90 days: ")
      TOP_PACK = st.selectbox("Please enter your most active packs", ('On net 200F=Unlimited _call24H', 'All-net 500F=2000F;5d',
       'On-net 1000F=10MilF;10d', 'Data:1000F=5GB,7d',
       'Mixt 250F=Unlimited_call24H',
       'MIXT:500F= 2500F on net _2500F off net;2d', 'On-net 500F_FNF;3d',
       'Data: 100 F=40MB,24H', 'MIXT: 200mnoff net _unl on net _5Go;30d',
       'Jokko_Daily', 'Data: 200 F=100MB,24H', 'Data:490F=1GB,7d',
       'Twter_U2opia_Daily', 'On-net 500=4000,10d', 'Data:1000F=2GB,30d',
       'IVR Echat_Daily_50F', 'Pilot_Youth4_490',
       'All-net 500F =2000F_AllNet_Unlimited', 'Twter_U2opia_Weekly',
       'Data:200F=Unlimited,24H', 'On-net 200F=60mn;1d',
       'All-net 600F= 3000F ;5d', 'Pilot_Youth1_290',
       'All-net 1000F=(3000F On+3000F Off);5d', 'VAS(IVR_Radio_Daily)',
       'Data:3000F=10GB,30d', 'All-net 1000=5000;5d',
       'Twter_U2opia_Monthly', 'MIXT: 390F=04HOn-net_400SMS_400 Mo;4h\t',
       'FNF2 ( JAPPANTE)', 'Yewouleen_PKG', 'Data:150F=SPPackage1,24H',
       'WIFI_Family_2MBPS', 'Data:500F=2GB,24H', 'MROMO_TIMWES_RENEW',
       'New_YAKALMA_4_ALL', 'Data:1500F=3GB,30D',
       'All-net 500F=4000F ; 5d', 'Jokko_promo', 'All-net 300=600;2d',
       'Data:300F=100MB,2d',
       'MIXT: 590F=02H_On-net_200SMS_200 Mo;24h\t\t',
       'All-net 500F=1250F_AllNet_1250_Onnet;48h', 'Facebook_MIX_2D',
       '500=Unlimited3Day', 'On net 200F= 3000F_10Mo ;24H',
       '200=Unlimited1Day', 'YMGX 100=1 hour FNF, 24H/1 month',
       'SUPERMAGIK_5000', 'Data:DailyCycle_Pilot_1.5GB', 'Staff_CPE_Rent',
       'MIXT:1000F=4250 Off net _ 4250F On net _100Mo; 5d',
       'Data:50F=30MB_24H', 'Data:700F=SPPackage1,7d',
       'Data: 490F=Night,00H-08H', 'Data:700F=1.5GB,7d',
       'Data:1500F=SPPackage1,30d', 'Data:30Go_V 30_Days',
       'MROMO_TIMWES_OneDAY', 'On-net 300F=1800F;3d',
       'All-net 5000= 20000off+20000on;30d', 'WIFI_ Family _4MBPS',
       'CVM_on-net bundle 500=5000', 'Internat: 1000F_Zone_3;24h\t\t',
       'DataPack_Incoming', 'Jokko_Monthly', 'EVC_500=2000F',
       'On-net 2000f_One_Month_100H; 30d',
       'MIXT:10000F=10hAllnet_3Go_1h_Zone3;30d\t\t', 'EVC_Jokko_Weekly',
       '200F=10mnOnNetValid1H', 'IVR Echat_Weekly_200F',
       'WIFI_ Family _10MBPS', 'Internat: 1000F_Zone_1;24H\t\t',
       'Jokko_Weekly', 'SUPERMAGIK_1000',
       'MIXT: 500F=75(SMS, ONNET, Mo)_1000FAllNet;24h\t\t',
       'VAS(IVR_Radio_Monthly)',
       'MIXT: 5000F=80Konnet_20Koffnet_250Mo;30d\t\t',
       'Data: 200F=1GB,24H', 'EVC_JOKKO30',
       'NEW_CLIR_TEMPALLOWED_LIBERTE_MOBILE', 'TelmunCRBT_daily',
       'FIFA_TS_weekly', 'VAS(IVR_Radio_Weekly)',
       'Internat: 2000F_Zone_2;24H\t\t', 'APANews_weekly', 'EVC_100Mo',
       'pack_chinguitel_24h', 'Data_EVC_2Go24H',
       'Mixt : 500F=2500Fonnet_2500Foffnet ;5d', 'FIFA_TS_daily',
       'MIXT: 4900F= 10H on net_1,5Go ;30d', 'CVM_200f=400MB',
       'IVR Echat_Monthly_500F', 'All-net 500= 4000off+4000on;24H',
       'FNF_Youth_ESN', 'Data:1000F=700MB,7d', '1000=Unlimited7Day',
       'Incoming_Bonus_woma', 'CVM_100f=200 MB', 'CVM_100F_unlimited',
       'pilot_offer6', '305155009', 'Postpaid FORFAIT 10H Package',
       'EVC_1Go', 'GPRS_3000Equal10GPORTAL',
       'NEW_CLIR_PERMANENT_LIBERTE_MOBILE', 'Data_Mifi_10Go_Monthly',
       '1500=Unlimited7Day', 'EVC_700Mo', 'CVM_100f=500 onNet',
       'CVM_On-net 1300f=12500', 'pilot_offer5', 'EVC_4900=12000F',
       'CVM_On-net 400f=2200F', 'YMGX on-net 100=700F, 24H',
       'CVM_150F_unlimited', 'EVC_MEGA10000F', 'pilot_offer7',
       'CVM_500f=2GB', 'SMS Max', '301765007', '150=unlimited pilot auto',
       'MegaChrono_3000F=12500F TOUS RESEAUX', 'pilot_offer4',
       'Go-NetPro-4 Go', '200=unlimited pilot auto',
       'ESN_POSTPAID_CLASSIC_RENT', 'Data_Mifi_10Go',
       'Data:New-GPRS_PKG_1500F', 'All-ne'))
      FREQ_TOP_PACK =st.number_input("Please enter the number of times you acivated the top-up package: ")

      CHURN = ""

      if st.button("Result"):
         CHURN =prediction([user_id, REGION, TENURE, MONTANT, FREQUENCE_RECH, REVENUE, ARPU_SEGMENT, FREQUENCE, DATA_VOLUME,
         ON_NET, ORANGE, TIGO, ZONE1, ZONE2, MRG, REGULARITY, TOP_PACK, FREQ_TOP_PACK])

         st.success(CHURN)
if  __name__ == "__main__":
         main()