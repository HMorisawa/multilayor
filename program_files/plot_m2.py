from matplotlib.pyplot import plot,show,xlabel,ylabel,title,legend,grid, axis
import matplotlib.pyplot as plt

def plot_intensity(anglex, refy, tray, absy):
    plot(anglex,refy, label="Reflectance")
    plot(anglex,tray, label="Transmittance")
    plot(anglex,absy, label="Absorptance")
    xlabel(r"Angle (deg.)",fontsize=15)   # x 軸のラベル
    ylabel(r"Intensity (a.u.)",fontsize=15)              # y 軸のラベル
    #title("Reflectance",fontsize=20)          # グラフタイトル
    grid(True)    # グリッドを表示
    plt.xlim(30, 90)
    plt.ylim(0, 1)    
    legend(fontsize=10,loc='center left')            # 凡例の表示とフォントサイズ
    plt.tick_params(labelsize=15)  # 軸の目盛表示とフォントサイズの指定
    plt.savefig('Intensity.png')
    show()                                    # グラフを表示 
    return 0

def plot_EFangle(anglex, EFI_main):
    plot(anglex,EFI_main, label="EFI")
    xlabel(r"Angle (deg.)",fontsize=15)   # x 軸のラベル
    ylabel(r"Intensity (a.u.)",fontsize=15)              # y 軸のラベル
    title("Electric field intensity",fontsize=15)          # グラフタイトル
    grid(True)    # グリッドを表示
    plt.xlim(30, 90)
    #plt.ylim(0, 1)    
    #legend(fontsize=10,loc='upper left')            # 凡例の表示とフォントサイズ
    plt.tick_params(labelsize=15)  # 軸の目盛表示とフォントサイズの指定
    plt.savefig('EF_intensity.png')
    show()                                    # グラフを表示
    return 0

def plot_EFdir(material,inangle, z0dir,EFI0,z1dir,EFI1,z2dir,EFI2,z3dir,EFI3,z4dir,EFI4,z5dir,EFI5):
    if material==1:
        label0="In SiO2"
    else:
        label0="In Sapphire"
    plot(z0dir,EFI0, label=label0)
    plot(z1dir,EFI1, label="In Al")
    plot(z2dir,EFI2, label="In Al2O3")
    plot(z3dir,EFI3, label="In Water")
    plot(z4dir,EFI4, label="In x")
    plot(z5dir,EFI5, label="In x")
    xlabel(r"z-direction (nm)",fontsize=15)   # x 軸のラベル
    ylabel(r"Intensity (a.u.)",fontsize=15)              # y 軸のラベル
    title("Electric field intensity"+", φ="+str(inangle)+"deg.",fontsize=15)          # グラフタイトル
    grid(True)    # グリッドを表示
    plt.xlim(-100, 200)
    #plt.ylim(0, 20)    
    legend(fontsize=10,loc='upper right')            # 凡例の表示とフォントサイズ
    plt.tick_params(labelsize=15)  # 軸の目盛表示とフォントサイズの指定
    #plt.savefig(str(inangle)+'.png')
    show()                                    # グラフを表示
    #plt.clf()
    return 0

def plot_EFdir_w(material,inangle, z0dir,EFI0,z1dir,EFI1,z2dir,EFI2,z3dir,EFI3,z4dir,EFI4,z5dir,EFI5):
    if material==1:
        label0="In SiO2"
    else:
        label0="In Sapphire"
    plot(z0dir,EFI0, label=label0)
    plot(z1dir,EFI1, label="In Al")
    plot(z2dir,EFI2, label="In Al2O3")
    plot(z3dir,EFI3, label="In Water")
    plot(z4dir,EFI4, label="In x")
    plot(z5dir,EFI5, label="In x")
    xlabel(r"z-direction (nm)",fontsize=15)   # x 軸のラベル
    ylabel(r"Intensity (a.u.)",fontsize=15)              # y 軸のラベル
    title("Electric field intensity"+", φ="+str(inangle)+"deg.",fontsize=15)          # グラフタイトル
    grid(True)    # グリッドを表示
    plt.xlim(-100, 200)
    #plt.ylim(0, 20)    
    legend(fontsize=10,loc='upper right')            # 凡例の表示とフォントサイズ
    plt.tick_params(labelsize=15)  # 軸の目盛表示とフォントサイズの指定
    plt.savefig(str(inangle)+'.png')
    #show()                                    # グラフを表示
    plt.clf()
    return 0
