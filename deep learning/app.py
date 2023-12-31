
import numpy as np
import pickle
import pandas as pd
import streamlit as st
import keras


model = keras.models.load_model('model\model.h5')


def reserve(feature1,feature2,feature3,feature4,feature5,feature6,feature7,feature8,feature9,feature10,feature11,feature12,feature13,feature14,feature15,feature16,feature17):
  prediction=model.predict([[feature1,feature2,feature3,feature4,feature5,feature6,feature7,feature8,feature9,feature10,feature11,feature12,feature13,feature14,feature15,feature16,feature17]])
  print(prediction)
  return prediction

def main():
   st.title("REservation Cancellation")

   feature1 = st.number_input("Feature 1", value=0.0)
   feature2 = st.number_input("Feature 2", value=0.0)
   feature3 = st.number_input("Feature 3", value=0.0)
   feature4 = st.number_input("Feature 3", value=0.0)
   feature5 = st.number_input("Feature 3", value=0.0)
   feature6 = st.number_input("Feature 3", value=0.0)
   feature7 = st.number_input("Feature 3", value=0.0)
   feature8 = st.number_input("Feature 3", value=0.0)
   feature9 = st.number_input("Feature 3", value=0.0)
   feature10 = st.number_input("Feature 3", value=0.0)
   feature11= st.number_input("Feature 3", value=0.0)
   feature12= st.number_input("Feature 3", value=0.0)
   feature13= st.number_input("Feature 3", value=0.0)
   feature14= st.number_input("Feature 3", value=0.0)
   feature15= st.number_input("Feature 3", value=0.0)
   feature16= st.number_input("Feature 3", value=0.0)
   feature17= st.number_input("Feature 3", value=0.0)
   result=''
   if st.button("Predict"):
    result=reserve(feature1,feature2,feature3,feature4,feature5,feature6,feature7,feature8,feature9,feature10,feature11,feature12,feature13,feature14,feature15,feature16,feature17)
   st.success('The output is {}'.format(result))
if __name__=='__main__':
  main()
