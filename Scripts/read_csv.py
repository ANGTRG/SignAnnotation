import csv
import os
import glob

#POI = Point of Intrest
#ROC = Rate of Change
def read_cord_csv(csv_file):
    frame_idxs = []
    l_x = []
    l_y = []
    r_x = []
    r_y = []
    
    with open(csv_file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            frame_idxs.append(float(row["frame_idx"]))
            l_x.append(float(row["l_x"]))
            l_y.append(float(row["l_y"]))
            r_x.append(float(row["r_x"]))
            r_y.append(float(row["r_y"]))
            
    return frame_idxs, l_x, l_y, r_x, r_y


def read_features_csv(csv_file):
    frame_idxs = []
    
    l_roc_x_sec = []
    l_roc_y_sec = []
    r_roc_x_sec = []
    r_roc_y_sec = []
    
    l_move_mag_sec = []
    r_move_mag_sec = []  
    
    poi = [] #will sometimes straight up be null but still want this colom for constancy
    
    with open(csv_file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            frame_idxs.append(float(row["frame_idx"]))
            
            l_roc_x_sec.append(float(row["l_roc_x_sec"]))
            l_roc_y_sec.append(float(row["l_roc_y_sec"]))
            r_roc_x_sec.append(float(row["r_roc_x_sec"]))
            r_roc_y_sec.append(float(row["r_roc_y_sec"]))
            
            l_move_mag_sec.append(float(row["l_move_mag_sec"]))
            r_move_mag_sec.append(float(row["r_move_mag_sec"]))
            
    return frame_idxs, l_roc_x_sec, l_roc_y_sec, r_roc_x_sec, r_roc_y_sec, l_roc_x_sec, l_move_mag_sec, r_move_mag_sec, poi

def read_prediction_csv(csv_file):
    frame_idx =[]
    
    poi =[]

    #thinkin about making it so it uses the highest probability of 1 in the first 30 frames as 1? avoids the issue of when no 1 cases are predicted
    poi_prob_0 = []
    poi_prob_1 = []
    
    with open(csv_file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            frame_idx.append(float(row["frame_idx"]))
            
            poi.append(float(row["poi"]))
            
            poi_prob_0.append(float(row["poi_prob_0"]))
            poi_prob_1.append(float(row["poi_prob_1"]))

    return  frame_idx, poi, poi_prob_0, poi_prob_1
   
