from tkinter import E
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from numpy import arcsin,arccos,exp,linspace,arange,sqrt,zeros,array,matrix,asmatrix,sin,cos,tan,pi,real
#from matplotlib.pyplot import plot,show,xlabel,ylabel,title,legend,grid, axis
from numpy.linalg import inv
import plot_m2
import outfile2

z = 120*pi #真空中の特性インピーダンス

sintheta=zeros(6,dtype=complex)
costheta=zeros(6,dtype=complex)
g=zeros(6,dtype=complex)
h=zeros(6,dtype=complex)
delta=zeros(6,dtype=complex)
Ref0=0
Tra0=0
Tra_co=0
Mv0=zeros((2,2),dtype=complex)
M1=zeros((2,2),dtype=complex)
M2=zeros((2,2),dtype=complex)
M3=zeros((2,2),dtype=complex)
M4=zeros((2,2),dtype=complex)

A=zeros(6,dtype=complex)
B=zeros(6,dtype=complex)
e=zeros((6,2),dtype=complex)
EFI=zeros(6,dtype=complex)
A[0]=1.0    


def GoCal(material,WL,inangle,t_real,Pol):
    if material==1:
        file_material='SiO2 w/ air'
        n = [1.523, 0.21+3.14j, 1.833, 1., 1., 1.]
    elif material==2:
        file_material='SiO2 w/ water'
        n = [1.523, 0.21+3.14j, 1.833, 1.33, 1.33, 1.33]
    elif material==3:
        file_material='Sapphire w/ air'
        n = [1.833, 0.21+3.14j, 1.833, 1., 1., 1.] 
    elif material==4:
        file_material='Sapphire w/ water'
        n = [1.833, 0.21+3.14j, 1.833, 1.33, 1.33, 1.33] 
    elif material==5:
        file_material='Sapphire w/ arb.(gap)'
        n = [1.833, 1.8, 1.833, 0.21+3.14j, 1.833, 1.33] 
    elif material==6:
        file_material='Sapphire w/ Water-gap'
        n = [1.833, 1.33, 1.833, 0.21+3.14j, 1.833, 1.33] 
    elif material==7:
        file_material='Sapphire w/ air w/ gold'
        n = [1.833, 0.21+3.14j, 1.36+1.7815j, 1., 1., 1.]
    elif material==8:
        file_material='Sapphire w/ air w/ Pt'
        n = [1.833, 0.21+3.14j, 1.1704+2.4384j, 1., 1., 1.]
    elif material==9:
        file_material='Sapphire w/ air w/ Pt'
        n = [1.523, 0.21+3.14j, 1.523, 1., 1., 1.]
    elif material==10:
        file_material='Sapphire w/ air w/ Pt'
        n = [1.523, 0.21+3.14j, 1., 1, 1., 1.]
    elif material==11:
        file_material='Sapphire w/ water'
        n = [1.833, 0.21+3.14j, 1.833, 1.5, 1.5, 1.5] 

    k=zeros(6,dtype=complex)
    kvac=2*pi/WL        # 真空中の波数
    for i in range(6):
        k[i]=n[i]*kvac #媒質中の波数
    
    t = [0, t_real[0], t_real[0]+t_real[1],t_real[0]+t_real[1]+t_real[2],t_real[0]+t_real[1]+t_real[2]+t_real[3]]


    anglex=np.array([])
    refy=np.array([])
    tray=np.array([])
    EFI_main=np.array([])
    EFI0=np.array([])
    EFI1=np.array([])
    EFI2=np.array([])
    EFI3=np.array([])
    EFI4=np.array([])
    EFI5=np.array([])
    
    t1start=0         # 始めの角度
    t1end=89           # 終わりの角度
    t1points=500       # プロット数
    t1Deg = linspace(t1start,t1end,t1points) # 入射角 t1 の配列の生成
    for i in range(t1points):
        getPol=pol(n,k,t,Pol,t1Deg[i],t_real[0]+t_real[1]) #電場はアルミナ面を見ている（real[0]+t_real[1]）
        anglex=np.append(anglex,t1Deg[i])
        refy=np.append(refy,getPol[0]) 
        tray=np.append(tray,getPol[1])
        absy=1-refy-tray
        EFI_main=np.append(EFI_main,getPol[2][2]) #getPol[2][i], i=0:in prism, i=1:in Aluminum, i=2:in Alumina
    
    plot_m2.plot_intensity(anglex, refy, tray, absy) #ref, tra, abの描画

    plot_m2.plot_EFangle(anglex, EFI_main)
    
    #outfile2.out_intensity(file_material, anglex, t_real, refy, tray, absy, EFI_main)　#ref, tra, ab, EFのファイル出力
    #outfile2.out_intensity_ri(file_material, anglex, t_real, refy, tray, absy, EFI_main, n[1])

    zpoints=500
    z0dir = linspace(-100,1,zpoints)
    z1dir = linspace(-1,t_real[0],zpoints)
    z2dir = linspace(t_real[0],t_real[0]+t_real[1],zpoints)
    z3dir = linspace(t_real[0]+t_real[1],t_real[0]+t_real[1]+t_real[2],zpoints)
    z4dir = linspace(t_real[0]+t_real[1]+t_real[2],t_real[0]+t_real[1]+t_real[2]+t_real[3],zpoints)
    z5dir = linspace(t_real[0]+t_real[1]+t_real[2]+t_real[3],500,zpoints)

    for i in range(zpoints):
        getPol=pol(n,k,t,Pol,inangle,z0dir[i])
        EFI0=np.append(EFI0,getPol[2][0])
    
    for i in range(zpoints):
        getPol=pol(n,k,t,Pol,inangle,z1dir[i])
        EFI1=np.append(EFI1,getPol[2][1])
        
    for i in range(zpoints):
        getPol=pol(n,k,t,Pol,inangle,z2dir[i])
        EFI2=np.append(EFI2,getPol[2][2])
        
    for i in range(zpoints):
        getPol=pol(n,k,t,Pol,inangle,z3dir[i])
        EFI3=np.append(EFI3,getPol[2][3])

    for i in range(zpoints):
        getPol=pol(n,k,t,Pol,inangle,z4dir[i])
        EFI4=np.append(EFI4,getPol[2][4])

    for i in range(zpoints):
        getPol=pol(n,k,t,Pol,inangle,z5dir[i])
        EFI5=np.append(EFI5,getPol[2][5])
  
    plot_m2.plot_EFdir(material, inangle, z0dir,EFI0,z1dir,EFI1,z2dir,EFI2,z3dir,EFI3,z4dir,EFI4,z5dir,EFI5)   #グラフ描画
    plot_m2.plot_EFdir_w(material, inangle, z0dir,EFI0,z1dir,EFI1,z2dir,EFI2,z3dir,EFI3,z4dir,EFI4,z5dir,EFI5) #グラフ描画+グラフ保存

    #outfile2.out_EFdir(file_material, anglex, t_real, z0dir, EFI0, z1dir, EFI1, z2dir, EFI2, z3dir, EFI3, z4dir, EFI4, z5dir, EFI5)


def mMATp(delta,g,h):
    return matrix([[cos(delta),-1j*g/h*sin(delta)],
                   [-1j*h/g*sin(delta),cos(delta)]]) # p-偏光 Mij 行列の定義

def Ref(Mv,g,h):
    return (((Mv[0, 0]*g[5] + Mv[0, 1]*h[5])*\
    h[0] - (Mv[1, 0]*g[5] + Mv[1, 1]*h[5])*\
    g[0])/((Mv[0, 0]*g[5] + Mv[0, 1]*h[5])*\
    h[0] + (Mv[1, 0]*g[5] + Mv[1, 1]*h[5])*g[0]))    

def Tra(Mv,g,h,costheta,t,k):
    return ((2*g[0]*h[0]*exp(-1j*t[4]*k[5]*\
      costheta[5]))/((Mv[0, 0]*g[5] + Mv[0, 1]*h[5])*\
     h[0] + (Mv[1, 0]*g[5] + Mv[1, 1]*h[5])*g[0]))
          
def pol(n,k,t,PorS,angDeg,refz):
    
    angRad = angDeg/180*pi #ラジアンへの変換
    sintheta[0]=sin(angRad)
    costheta[0]=sqrt(1-sintheta[0]**2)
    
    for i in range(1,6):
        sintheta[i]=n[0]/n[i]*sintheta[0]
        costheta[i]=sqrt(1-sintheta[i]**2)
        Tra_co=real(n[5]*costheta[5])/real(n[0]*costheta[0])
            
    if PorS=='P':
        for i in range(6):
            g[i]=costheta[i]
            h[i]=n[i]/z
    elif PorS=='S':
        for i in range(6):
            g[i]=1
            h[i]=n[i]*costheta[i]/z
    else:
        pass
            
    for i in range(1,5):
        delta[i]=k[i]*costheta[i]*(t[i]-t[i-1])
        
    M1=mMATp(delta[1],g[1],h[1])
    M2=mMATp(delta[2],g[2],h[2]) 
    M3=mMATp(delta[3],g[3],h[3])
    M4=mMATp(delta[4],g[4],h[4])    
    Mv0=M1@M2@M3@M4
    Ref0=Ref(Mv0,g,h)
    Tra0=Tra(Mv0,g,h,costheta,t,k)
    RefE=abs(Ref0)**2
    TraE=Tra_co*(abs(Tra0)**2)
    
    B[0]=A[0]*Ref0
    B[5]=0
    A[5]=A[0]*Tra0
    e[0]=[g[0]*(A[0]+B[0]),h[0]*(A[0]-B[0])]
    e[1]=inv(M1)@e[0]
    e[2]=inv(M2)@e[1]
    e[3]=inv(M3)@e[2]
    e[4]=inv(M4)@e[3]
    e[5]=inv(Mv0)@e[0]
        
    for i in range(1,5):
        A[i]=(exp(-1j*k[i]*costheta[i]*t[i])/2)*(e[i][[0]]/g[i] + e[i][[1]]/h[i])
        B[i]=(exp(1j*k[i]*costheta[i]*t[i])/2)*(e[i][[0]]/g[i] - e[i][[1]]/h[i])

    for i in range(6): 
        EFI[i]=abs(A[i]*exp(1j*k[i]*costheta[i]*refz) + B[i]*exp(-1j*k[i]*costheta[i]*refz))**2
    
    return RefE, TraE, EFI.real

def Calc_EFI_dir_w(material, WL, inangle, t_real):
    for i in range(90):
        inangle=i
        GoCal(material, WL, inangle, t_real)   
    return 0

def main():
    material=4         #(1=SiO w/ air, 2=SiO w/ water, 3=Sapphire w/ air, 4=Sapphire w/ water, 5=Sapphire w/ arb.(gap), 6=Sapphire w/ Water-gap)
    WL=266            # 真空中の波長 WL〔nm〕
    inangle=58        #距離依存を出すときの入射角度の指定
    t_real = [21, 6, 1, 100] #膜厚[Al,Al3O3,誘電体,誘電体（任意＊誘電体に関して初期は水にしています）]
    Pol='P' #polarization of light
    
    GoCal(material,WL,inangle,t_real,Pol)

    #Calc_EFI_dir_w(material, WL, inangle, t_real)

    return 0

main()
