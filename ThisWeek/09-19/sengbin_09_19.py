
Real_Mardrid_data = [(1,'Navas','GK','Yes'),
                     (2,'Carvajal','DF','Yes'),
                     (3,'Vallejo','DF'),
                     (4,'Ramos','DF','Yes'),
                     (5,'Varane','DF','Yes'),
                     (6,'Nacho','DF','Yes'),
                     (7,'Mariano','FW')]

Keys = {'Back_Number','Name','Position','Regular'}
Dic_Real = [{}]*8
for i in range(Real_Mardrid_data.__len__()):
    if Real_Mardrid_data[i].__len__() > 3:
        Dic_Real[Real_Mardrid_data[i][0]] = {'Back_Number': Real_Mardrid_data[i][0], 'Name': Real_Mardrid_data[i][1],
                                         'Position': Real_Mardrid_data[i][2],'Regular':Real_Mardrid_data[i][3]}
    else:
        Dic_Real[Real_Mardrid_data[i][0]] = {'Back_Number': Real_Mardrid_data[i][0], 'Name': Real_Mardrid_data[i][1],
                                             'Position': Real_Mardrid_data[i][2]}

for i in range(Dic_Real.__len__()):
    Dic_Real[i].setdefault('Regular','No')

for i in range(Dic_Real.__len__()):
    print(Dic_Real[i])