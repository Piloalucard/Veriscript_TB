
#Gustavo Padilla Valdez
import msvcrt; 
import time;
def leer():
    band=0;
    while band==0:
        nombre=str(input("Dame el nombre del archivo(sin extension): "));
        try:
            archivo=open(nombre,mode="r",encoding="utf-8");
            print("NOMBRE EXISTENTE EN ESTA CARPETA,USE OTRO");
            input();
            archivo.close();
            band=0;
        except:
            print("Buen nombre!");
            band=1;
    return nombre;

def crear():
    nombre=leer();
    nombre=nombre+".txt";
    car=0;
    archivo=open(nombre,mode="w",encoding="utf-8");
    print("-PRESIONE 1 PARA AGREGAR UNA INSTRUCCION-");
    print("-PRESIONE 2 PARA GUARDAR Y SALIR-");
    while True: #Leera todas las teclas que se presionen hasta que presione una valida
            
            if(car==1):
                print("\n-PRESIONE 1 PARA AGREGAR UNA INSTRUCCION-");
                print("-PRESIONE 2 PARA GUARDAR Y SALIR-\n");
            aux=str(msvcrt.getch());  
            if(aux=="b'1'"):
                print("\n¿De que tipo sera la instruccion?");
                print("PRESIONE 1 PARA TIPO (I)");
                print("PRESIONE 2 PARA TIPO (R)");
                print("PRESIONE 3 PARA TIPO (J)");
                print("PRESIONE 4 PARA REGRESAR");
                while True:
                    aux2=str(msvcrt.getch());  
                    if(aux2=="b'1'"):
                        linea=tipoi();
                        archivo.write(str(linea)+"\n");
                        break;
                    elif(aux2=="b'2'"):
                        linea=tipor();
                        archivo.write(str(linea)+"\n");
                        break;
                    elif(aux2=="b'3'"):
                        linea=tipoj();
                        archivo.write(str(linea)+"\n");
                        break;
                    elif(aux2=="b'4'"):
                        break;
                car=1;
            elif(aux=="b'2'"):
                sal=0;
                car=1;
                print("\n¿SEGURO QUE QUIERES SALIR?");
                print("Y/N");
                while True:
                    aux2=str(msvcrt.getch());  
                    if(aux2=="b'y'" or aux2=="b'Y'"):
                        sal=1;
                        break;
                    elif(aux2=="b'n'" or aux2=="b'N'"):
                        break;
                if(sal==1):
                    break;
    print("Terminando...");
    archivo.close();
    time.sleep(2.5);                

def tipoj():
    acep=0;
    special="";
    while acep==0:
        special=str(input("Dame el codigo SPECIAL (6 DIGITOS): "));
        special=special[:6];
        special=special.zfill(6);
        print("¿Este codigo es correcto?: "+special);
        print("Y/N");
        while True:
            aux2=str(msvcrt.getch());  
            if(aux2=="b'y'" or aux2=="b'Y'"):
                acep=1;
                break;
            elif(aux2=="b'n'" or aux2=="b'N'"):
                break;
    acep=0;
    jump="";
    while acep==0:
        jump=str(input("Dame la DIRECCION (26 DIGITOS): "));
        jump=jump[:26];
        jump=jump.zfill(26);
        print("¿Este codigo es correcto?: "+jump);
        print("Y/N");
        while True:
            aux2=str(msvcrt.getch());  
            if(aux2=="b'y'" or aux2=="b'Y'"):
                acep=1;
                break;
            elif(aux2=="b'n'" or aux2=="b'N'"):
                break;
    regresar=str(special+jump+" ");
    print("AGREGADO CON EXITO!\n");
    return regresar;
    

def tipor():
    acep=0;
    special="";
    while acep==0:
        special=str(input("Dame el codigo SPECIAL (6 DIGITOS): "));
        special=special[:6];
        special=special.zfill(6);
        print("¿Este codigo es correcto?: "+special);
        print("Y/N");
        while True:
            aux2=str(msvcrt.getch());  
            if(aux2=="b'y'" or aux2=="b'Y'"):
                acep=1;
                break;
            elif(aux2=="b'n'" or aux2=="b'N'"):
                break;

    acep=0;
    rs="";
    while acep==0:
        aux=-1;
        while aux==-1:
            aux=int(input("Dame el Primer SOURCE REGISTER RS (DECIMAL MAXIMO 31): "));
            if(aux>31 or aux<0):
                aux=-1;
                print("INGRESA DIRECCION MAYOR O IGUAL A O, O MENOR A 32");
        rs=str(tobinary(aux));
        rs=rs.zfill(5);
        print("¿Este codigo es correcto?: "+rs);
        print("Y/N");
        while True:
            aux2=str(msvcrt.getch());  
            if(aux2=="b'y'" or aux2=="b'Y'"):
                acep=1;
                break;
            elif(aux2=="b'n'" or aux2=="b'N'"):
                break;
    acep=0;
    rt="";
    while acep==0:
        aux=-1;
        while aux==-1:
            aux=int(input("Dame el Segundo SOURCE REGISTER RT (DECIMAL MAXIMO 31): "));
            if(aux>31 or aux<0):
                aux=-1;
                print("INGRESA DIRECCION MAYOR O IGUAL A O, O MENOR A 32");
        rt=str(tobinary(aux));
        rt=rt.zfill(5);
        print("¿Este codigo es correcto?: "+rt);
        print("Y/N");
        while True:
            aux2=str(msvcrt.getch());  
            if(aux2=="b'y'" or aux2=="b'Y'"):
                acep=1;
                break;
            elif(aux2=="b'n'" or aux2=="b'N'"):
                break;
    acep=0;
    rd="";
    while acep==0:
        aux=-1;
        while aux==-1:
            aux=int(input("Dame el DESTINY REGISTER RD (DECIMAL MAXIMO 31): "));
            if(aux>31 or aux<0):
                aux=-1;
                print("INGRESA DIRECCION MAYOR O IGUAL A O, O MENOR A 32");
        rd=str(tobinary(aux));
        rd=rd.zfill(5);
        print("¿Este codigo es correcto?: "+rd);
        print("Y/N");
        while True:
            aux2=str(msvcrt.getch());  
            if(aux2=="b'y'" or aux2=="b'Y'"):
                acep=1;
                break;
            elif(aux2=="b'n'" or aux2=="b'N'"):
                break;
    acep=0;
    sham="";
    while acep==0:
        sham=str(input("Dame el codigo SHAMT (5 DIGITOS): "));
        sham=sham[:5];
        sham=sham.zfill(5);
        print("¿Este codigo es correcto?: "+sham);
        print("Y/N");
        while True:
            aux2=str(msvcrt.getch());  
            if(aux2=="b'y'" or aux2=="b'Y'"):
                acep=1;
                break;
            elif(aux2=="b'n'" or aux2=="b'N'"):
                break;
    acep=0;
    fun="";
    while acep==0:
        fun=str(input("Dame el codigo FUNCTION (6 DIGITOS): "));
        fun=fun[:6];
        fun=fun.zfill(6);
        print("¿Este codigo es correcto?: "+fun);
        print("Y/N");
        while True:
            aux2=str(msvcrt.getch());  
            if(aux2=="b'y'" or aux2=="b'Y'"):
                acep=1;
                break;
            elif(aux2=="b'n'" or aux2=="b'N'"):
                break;
    regresar=str(special+rs+rt+rd+sham+fun+" ");
    print("AGREGADO CON EXITO!\n");
    return regresar;
    
  

def tipoi():
    acep=0;
    special="";
    while acep==0:
        special=str(input("Dame el codigo SPECIAL (6 DIGITOS): "));
        special=special[:6];
        special=special.zfill(6);
        print("¿Este codigo es correcto?: "+special);
        print("Y/N");
        while True:
            aux2=str(msvcrt.getch());  
            if(aux2=="b'y'" or aux2=="b'Y'"):
                acep=1;
                break;
            elif(aux2=="b'n'" or aux2=="b'N'"):
                break;

    acep=0;
    rs="";
    while acep==0:
        aux=-1;
        while aux==-1:
            aux=int(input("Dame el Primer SOURCE REGISTER RS (DECIMAL MAXIMO 31): "));
            if(aux>31 or aux<0):
                aux=-1;
                print("INGRESA DIRECCION MAYOR O IGUAL A O, O MENOR A 32");
        rs=str(tobinary(aux));
        rs=rs.zfill(5);
        print("¿Este codigo es correcto?: "+rs);
        print("Y/N");
        while True:
            aux2=str(msvcrt.getch());  
            if(aux2=="b'y'" or aux2=="b'Y'"):
                acep=1;
                break;
            elif(aux2=="b'n'" or aux2=="b'N'"):
                break;
    acep=0;
    rt="";
    while acep==0:
        aux=-1;
        while aux==-1:
            aux=int(input("Dame el Segundo SOURCE REGISTER RT (DECIMAL MAXIMO 31): "));
            if(aux>31 or aux<0):
                aux=-1;
                print("INGRESA DIRECCION MAYOR O IGUAL A O, O MENOR A 32");
        rt=str(tobinary(aux));
        rt=rt.zfill(5);
        print("¿Este codigo es correcto?: "+rt);
        print("Y/N");
        while True:
            aux2=str(msvcrt.getch());  
            if(aux2=="b'y'" or aux2=="b'Y'"):
                acep=1;
                break;
            elif(aux2=="b'n'" or aux2=="b'N'"):
                break;
    acep=0;
    inme="";
    while acep==0:
        inme=str(input("Dame el codigo INMEDIATO/DESPLAZAMIENTO (16 DIGITOS): "));
        inme=inme[:16];
        inme=inme.zfill(16);
        print("¿Este codigo es correcto?: "+inme);
        print("Y/N");
        while True:
            aux2=str(msvcrt.getch());  
            if(aux2=="b'y'" or aux2=="b'Y'"):
                acep=1;
                break;
            elif(aux2=="b'n'" or aux2=="b'N'"):
                break;
    regresar=str(special+rs+rt+inme+" ");
    print("AGREGADO CON EXITO!\n");
    return regresar;

def tobinary(n):
    return bin(n).replace("0b", "");  

def main():
    print("\t\t/INSTRUCCIONES MIPS DE 32 BITS/");
    crear();
    

main();