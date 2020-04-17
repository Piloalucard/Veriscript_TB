
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
    print("-PRESIONE 2 PARA SALIR-");
    while True: #Leera todas las teclas que se presionen hasta que presione una valida
            
            if(car==1):
                print("-PRESIONE 1 PARA AGREGAR UNA INSTRUCCION-");
                print("-PRESIONE 2 PARA SALIR-\n");
            aux=str(msvcrt.getch());  
            if(aux=="b'1'"):
                print("\n¿De que tipo sera la instruccion?");
                print("PRESIONE 1 PARA TIPO (I)");
                print("PRESIONE 2 PARA TIPO (R)");
                print("PRESIONE 3 PARA TIPO (J)");

                while True:
                    aux2=str(msvcrt.getch());  
                    if(aux2=="b'1'"):
                        linea=tipoi();
                        archivo.write(linea+"\n");
                        break;
                    elif(aux2=="b'2'"):
                        linea=tipor();
                        archivo.write(linea+"\n");
                        break;
                    elif(aux2=="b'3'"):
                        linea=tipoj();
                        archivo.write(linea+"\n");
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
    pass;

def tipor():
    pass;

def tipoi():
    pass;

def main():
    print("\t\t/INSTRUCCIONES MIPS DE 32 BITS/");
    crear();
    

main();