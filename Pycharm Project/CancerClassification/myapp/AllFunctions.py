
import pickle


#Load the SVM model and use for cancer classificaition

def SVM_CancerClassification(selected_feature_array_data):
    pkl_filename = "C:/Users/Amina/Videos/26-09/CancerClassification/myapp/pickle_model.pkl"
    with open(pkl_filename, 'rb') as file:
        pickle_model = pickle.load(file)

    firstarray=selected_feature_array_data
    x_new = [firstarray]
    y_predict = pickle_model.predict(x_new)
    y_predict
    return y_predict

#get the name of  the class of cancer

def print_class(x):
    cancer_class = "Cancer Not Found"
    if (x==1):
        cancer_class = "ACC"
    if (x==2):
        cancer_class = "BRCA"
    if (x==3):
        cancer_class = "COAD"
    if (x==4):
        cancer_class = "GBM"
    if (x==5):
        cancer_class = "LAML"
    if (x==6):
        cancer_class = "LGG"
    if (x==7):
        cancer_class = "OV"
    if (x==8):
        cancer_class = "READ"
    if (x==9):
        cancer_class = "UCEC"
    return cancer_class


