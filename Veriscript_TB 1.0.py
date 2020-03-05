#Veriscript_TB 1.0 04/03/2020
#Gustavo Padilla Valdez INCO
import msvcrt;

def crear():
    band=0;
    while band==0:
        nombre=str(input("Dame el nombre de tu modulo: "));
        nombre=nombre+"_TB.v";
        try:
            archivo=open(nombre,mode="r",encoding="utf-8");
            print("Ese archivo ya existe, elegir otro");
            input();
            archivo.close();
        except:
            archivo=open(nombre,mode="w",encoding="utf-8");
            print("Archivo creado");
            archivo.close();
            input();
            band=1;
    return nombre;



def escribir():
    nombre=crear();
    archivo=open(nombre,mode="w",encoding="utf-8");
    texto="//Archivo de TestBench para verilog basico generado por Veriscript_TB 1.0\n";
    archivo.write(texto);
    texto="`timescale 1ns/1ns\n\n";
    archivo.write(texto);
    textoaux=nombre.replace(".v","");
    texto="module "+textoaux+"();\n"
    archivo.write(texto);
    instancia="    "+textoaux+" DUV(";
    entradas=[];
    salidas=[];
    agregar=0;
    intaux=0;
    op=0;
    textoaux="";
    while agregar==0:
        band=0;
        caracter=0;
        err=0;
        print("\nPresione 1 para agregar un input, 2 para continuar: ");
        while caracter==0: #Leera todas las teclas que se presionen hasta que presione una valida
            aux=str(msvcrt.getch());
            if "b'1'" == aux: 
                caracter+=1;
                salir=0;
                while salir == 0:
                    texto=str(input("Dame el nombre de la entrada: "));
                    
                    while err==0:
                        intaux=int(input("Dame el tamaño de la entrada en bits: "));
                        try:
                            intaux=intaux-1;
                            if intaux < 0:
                                 print("Ingresa un numero valido de bits");
                            else:
                                err=1;
                        except:
                            print("Ingresa un numero valido de bits");
                    if intaux==0:
                        textoaux="    reg "+texto+";";
                    else:
                        textoaux="    reg ["+str(intaux)+":0]"+texto+";";
                    print(textoaux);
                    print("Presione 1 para agregar ese input, 2 para reingresar datos: ");
                    caracter2=0;
                    while caracter2==0: #Leera todas las teclas que se presionen hasta que presione una valida
                        aux2=str(msvcrt.getch());
                        if "b'1'" == aux: 
                            caracter2+=1;
                            salir=1;

                        elif "b'2'" == aux:
                            salir=0;
                            caracter2+=1;
                        else:
                            pass;  
                for i in entradas:
                    if i == texto:
                        band=1;
                if band == 1:
                    print("Esa entrada ya existe, intente volverla a ingresar");
                else:
                    instancia=instancia+",."+str(input("Dame a que va conectado en el modulo(.a,.b,etc): "))+"("+texto+")";
                    entradas.append(texto);  
                    texto=textoaux+"\n";
                    archivo.write(texto);
                
            elif "b'2'" == aux:
                agregar=1;
                caracter+=1;
            else:
                pass;
    agregar=0;
    intaux=0;
    op=0;
    textoaux="";
    while agregar==0:
        band=0;
        caracter=0;
        err=0;
        print("\nPresione 1 para agregar un output, 2 para continuar: ");
        while caracter==0: #Leera todas las teclas que se presionen hasta que presione una valida
            aux=str(msvcrt.getch());
            if "b'1'" == aux: 
                caracter+=1;
                salir=0;
                while salir == 0:
                    texto=str(input("Dame el nombre de la salida: "));
                    
                    while err==0:
                        intaux=int(input("Dame el tamaño de la salida en bits: "));
                        try:
                            intaux=intaux-1;
                            if intaux < 0:
                                 print("Ingresa un numero valido de bits");
                            else:
                                err=1;
                        except:
                            print("Ingresa un numero valido de bits");
                    if intaux==0:
                        textoaux="    wire "+texto+";";
                    else:
                        textoaux="    wire ["+str(intaux)+":0]"+texto+";";
                    print(textoaux);
                    print("Presione 1 para agregar ese output, 2 para reingresar datos: ");
                    caracter2=0;
                    while caracter2==0: #Leera todas las teclas que se presionen hasta que presione una valida
                        aux2=str(msvcrt.getch());
                        if "b'1'" == aux: 
                            caracter2+=1;
                            salir=1;

                        elif "b'2'" == aux:
                            salir=0;
                            caracter2+=1;
                        else:
                            pass;  
                for i in salidas:
                    if i == texto:
                        band=1;
                if band == 1:
                    print("Esa entrada ya existe, intente volverla a ingresar");
                else:
                    instancia=instancia+",."+str(input("Dame a que va conectado en el modulo(.a,.b,etc): "))+"("+texto+")";
                    salidas.append(texto);  
                    texto=textoaux+"\n";
                    archivo.write(texto);
                
            elif "b'2'" == aux:
                agregar=1;
                caracter+=1;
            else:
                pass;
    instancia=instancia+");\n";
    instancia=instancia.replace(",", "",1);
    archivo.write(instancia);
    archivo.write("endmodule");
    archivo.close();

escribir();