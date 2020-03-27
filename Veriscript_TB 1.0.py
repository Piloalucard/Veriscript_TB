#Veriscript_TB BETA 1.0 24/03/2020
#Gustavo Padilla Valdez
from random import randrange
import easygui
import time

def leer():
    band=0;
    err=0;
    print("Elige tu archivo .v");
    while band==0:
        nombre="";
        try:
            nombre=str(easygui.fileopenbox());
            if nombre == "None":
                print("ERROR, No abriste un archivo\nSaliendo...");
                time.sleep(1.5);
                band=1;
                err=1;
            else:
                print("Buena eleccion de archivo");
                band=1;
        except:
            print("ERROR");
            input();
            band=0;
    if err==1:
        exit();
    else:
        return nombre;



def extraer():
    nombre=leer();
    archivo=open(nombre,mode="r",encoding="utf-8");
    nam_module="";
    stauxlist=[];
    stauxlist2=[];
    lineas=[];
    entradas=[];
    salidas=[];
    while(True):
        linea=archivo.readline();#Lee por linea los caracteres
        if not linea: #Si ya no hay lineas
            break;
        lineas.append(linea);
    
    archivo.close();
    for i in lineas:
        if "input" in i:
            staux="";
            staux2="";
            ultimo="";
            if "input[" in i:
                i=i.replace("input[","input [");
            if "] " in i:
                pass;
            else:
                i=i.replace("]","] ");
            stauxlist=i;   
            stauxlist=stauxlist.split(" ");
            for j in stauxlist:
                if "[" in j:
                    staux=j;
                if "," in j:
                    staux2=j;
            stauxlist=staux2.split(",");
            if len(stauxlist)==1:
                entradas.append(staux+ultimo); 
            else:
                for j in stauxlist:
                    if j != "," and j!="\n" and j!=" ":
                        entradas.append(staux+j);
        if "output" in i:
            staux="";
            staux2="";
            ultimo="";
            if "output[" in i:
                i=i.replace("output[","output [");
            if "reg[" in i:
                i=i.replace("reg[","reg [");
            if "] " in i:
                pass;
            else:
                i=i.replace("]","] ");
            stauxlist=i;
            stauxlist=stauxlist.split(" ");
            for j in stauxlist:
                if "[" in j:
                    staux=j;
                if "," in j:
                    staux2=j;
                ultimo=j;
            stauxlist=staux2.split(",");
            if len(stauxlist)==1:
                salidas.append(staux+ultimo); 
            else:
                for j in stauxlist:
                    if j != "," and j!="\n" and j!=" ":
                        salidas.append(staux+j);    

        if "module" in i:
            if "endmodule" in i:
                pass;
            else:
                nam_module=i;
    stauxlist=nam_module.split(" ");
    for i in stauxlist:
        if i != "module" and i !=" " and i != "\n" and i !="(":
            nam_module=i;
    stauxlist=nam_module.split("(");
    for i in stauxlist:
        if i !=" " and i != "\n" and i !="(":
            nam_module=i;
    entradas_f=[];
    for i in entradas:
        i=i.replace("[","");
        i=i.replace("\n","");
        entradas_f.append(i);
    salidas_f=[];
    for i in salidas:
        i=i.replace("[","");
        i=i.replace("\n","");
        salidas_f.append(i);
    escribir(nam_module,entradas_f,salidas_f);
    
def escribir(nam_module,entradas,salidas):
    texto="";
    clock="";
    listaux=[];
    entradas_bit=[];
    salidas_bit=[];
    entradas_f=[];
    salidas_f=[];
    aux=0;
    nombre=nam_module+"_TB_SCRPT.v";
    archivo=open(nombre,mode="w",encoding="utf-8");
    archivo.write("//Archivo de TestBench para verilog basico generado por Veriscript_TB BETA 1.0\n");
    archivo.write("`timescale 1ns/1ns\n\n");
    archivo.write("module "+nam_module+"_TB();\n")
    for i in salidas:
        
        if "0" in i:
            archivo.write("    wire ["+str(i)+";\n");
            cont=0;
            a=int(i[0]);
            listaux=i.split("]");
            for j in listaux:   
                if cont == 1:
                    salidas_f.append(j);
                cont=1;
            salidas_bit.append(a);
        else:
            archivo.write("    wire "+str(i)+";\n");
            a=1;
            salidas_f.append(i);
            salidas_bit.append(a);
    band=0;
    for i in entradas:
        
        if "0" in i:
            archivo.write("    reg ["+str(i)+";\n");
            cont=0;
            a=int(i[0]);
            listaux=i.split("]");
            for j in listaux:   
                if cont == 1:
                    entradas_f.append(j);
                cont=1;
            entradas_bit.append(a);
        else:
            texto=i;
            texto=texto.lower();
            if band==0:
                if texto == "clk" or texto == "clock":
                    clock=i;
                    band=1;
                    archivo.write("    reg "+str(i)+"=0;\n");
                else:
                    archivo.write("    reg "+str(i)+";\n");
            else:
                archivo.write("    reg "+str(i)+";\n");
            a=1;
            entradas_f.append(i);
            entradas_bit.append(a);

    texto="    "+nam_module+" DUV(";
    for i in entradas_f:
        texto=texto+",."+str(i)+"("+str(i)+")";
    for i in salidas_f:
        texto=texto+",."+str(i)+"("+str(i)+")";
    texto=texto+");\n\n"
    texto=texto.replace(",","",1);
    archivo.write(texto);
  
    err=1;
    if band == 1:      
        while err==1: 
            try:
                aux=int(input("Hemos encontrado un input tipo CLOCK\n Porfavor, digite en enteros cada cuanto tiempo lo iteraremos (ns): "));
                if aux < 1:
                    print("Elija un numero mayor a 0");
                else:
                    err=0;
            except:
                print("Digite numero enteros positivos");
        archivo.write("    always #"+str(aux)+" "+clock+"=!"+clock+";\n\n");
    opc=0;
    while opc < 1 or opc > 3:
        try:
            print("\nDigita la opcion de como deseas rellenar los input: ");
            opc=int(input("1.Sin rellenar\n2.Relleno iterado\n3.Relleno Automatico: "));
            if opc==1:
                archivo.write("    initial begin\n\n");
        
            elif opc==2:
                iterar=[];
                archivo.write("    initial begin\n\n");
                err2=1;    
                while err2==1: 
                    try:
                        aux=int(input("Las entradas seran iteradas, indique hasta que numero: "));
                        if aux < 1:
                            print("Elija un numero mayor a 0");
                        else:
                            err2=0;
                    except:
                        print("Digite numero enteros positivos");
                err2=1;    
                while err2==1: 
                    try:
                        nano=int(input("Cuantos nanosegundos durara cada conjunto de valores: "));
                        if nano < 1:
                            print("Elija un numero mayor a 0");
                        else:
                            err2=0;
                    except:
                        print("Digite numero enteros positivos");

                conttotal=0;
                for i in entradas_f:
                    err2=1;  
                    si=2;  
                    while err2==1: 
                        try:
                            texto=i.lower();
                            if texto != "clk" and texto != "clock":
                                print(i,end=": ");
                                si=int(input("¿Esta entrada debe ser iterada? 1=SI  2=NO: "));
                            
                            if si < 1 or si > 2:
                                print("Elija 1 o 2");
                            else:
                                err2=0;
                        except:
                            print("Digite numeros, porfavor");
                    iterar.append(str(si));
                while conttotal <= aux:
                    cont=0;
                    for i in entradas_f:
                        texto=i.lower();
                        if texto != "clk" and texto != "clock":
                            cont2=0;
                            for j in entradas_bit:
                                cont3=0;
                                if j > 1:
                                    j+=1;
                                if cont == cont2:
                                    for h in iterar:
                                        if cont2==cont3:
                                            if h == "1":
                                                archivo.write("        "+i+"="+str(j)+"'d"+str(conttotal)+";\n");
                                        cont3+=1;
                              
                                cont2+=1;
                        cont+=1;
                    archivo.write("        #"+str(nano)+";\n\n");
                    conttotal+=1;
               
            elif opc==3:
                archivo.write("    initial begin\n\n");
                err2=1;    
                while err2==1: 
                    try:
                        aux=int(input("Cuantos datos aleatorios desea generar en cada variable: "));
                        if aux < 1:
                            print("Elija un numero mayor a 0");
                        else:
                            err2=0;
                    except:
                        print("Digite numero enteros positivos");
                err2=1;    
                while err2==1: 
                    try:
                        nano=int(input("Cuantos nanosegundos durara cada conjunto de valores: "));
                        if nano < 1:
                            print("Elija un numero mayor a 0");
                        else:
                            err2=0;
                    except:
                        print("Digite numero enteros positivos");

                conttotal=0;
                while conttotal < aux:
                    cont=0;
                    for i in entradas_f:
                        texto=i.lower();
                        if texto != "clk" and texto != "clock":
                            cont2=0;
                            for j in entradas_bit:
                                if j > 1:
                                    j+=1;
                                if cont == cont2:
                                    bitaux=2**int(j);
                                    bitaux=int(randrange(0,bitaux));
                                    archivo.write("        "+i+"="+str(j)+"'d"+str(bitaux)+";\n");
                              
                                cont2+=1;
                        cont+=1;
                    archivo.write("        #"+str(nano)+";\n\n");
                    conttotal+=1;
            else:
                print("ERROR, Debe ingresar una de las 3 opciones");
        except:
            opc=0;
            print("ERROR,Debe ingresar un numero entero");
    archivo.write("        $stop\n\n");
    archivo.write("        end\n\n");
    archivo.write("endmodule");
    archivo.close();

def tobinary(n):
    return bin(n).replace("0b", ""); 

def main():
    print("Bienvenido VeriScript!\n");
    extraer();
    print("\nARCHIVO CREADO CON EXITO! \nPUEDE VISUALIZAR SU ARCHIVO CON EL MISMO NOMBRE DEL MODULO + _TB_SCRPT");
    input();
main();