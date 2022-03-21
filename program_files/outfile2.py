def out_intensity(file_material, anglex, t_real, refy, tray, absy, EFI_main):
    with open(file_material+"_Ref_Tra_Abs_EF_Al_"+str(t_real[0])+"_Al2O3_"+str(t_real[1])+".csv", 'a') as out_data:
        for i in range(len(anglex)):
            out_data.write(str(anglex[i]) + "," + str(refy[i]) + "," + str(tray[i]) + "," + str(absy[i]) + "," + str(EFI_main[i]) + "\n")
    return 0

def out_EFdir(file_material, anglex, t_real,z0dir,EFI0,z1dir,EFI1,z2dir,EFI2,z3dir,EFI3,z4dir,EFI4,z5dir,EFI5):
    with open(file_material+"_EF_Zdirection_Al_"+str(t_real[0])+"_Al2O3_"+str(t_real[1])+".csv", 'a') as out_data:
        for i in range(len(anglex)):
            out_data.write(str(z0dir[i]) + "," + str(EFI0[i]) + "," + str(z1dir[i]) + "," + str(EFI1[i]) + "," + str(z2dir[i]) + "," + str(EFI2[i]) + "," + str(z3dir[i]) + "," + str(EFI3[i]) + "," + str(z4dir[i]) + "," + str(EFI4[i]) + "," + str(z5dir[i]) + "," + str(EFI5[i]) + "\n")
    return 0

def out_intensity_ri(file_material, anglex, t_real, refy, tray, absy, EFI_main, n1):
    with open(file_material+"_Ref_Tra_Abs_EF_Al_"+str(t_real[0])+"_Al2O3_"+str(t_real[1])+"_ri_"+str(n1)+".csv", 'a') as out_data:
        for i in range(len(anglex)):
            out_data.write(str(anglex[i]) + "," + str(refy[i]) + "," + str(tray[i]) + "," + str(absy[i]) + "," + str(EFI_main[i]) + "\n")
    return 0