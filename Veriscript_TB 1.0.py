#Veriscript_TB ALPHA 0.1 06/03/2020
#Gustavo Padilla Valdez INCO

def leer():
    band=0;
    while band==0:
        nombre=str(input("Dame el nombre de tu modulo(Con extension .v): "));
        try:
            archivo=open(nombre,mode="r",encoding="utf-8");
            print("Buena eleccion de archivo");
            input();
            archivo.close();
            band=1;
        except:
            print("Archivo no existente, verifique el nombre");
            input();
            band=0;
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
    input();
    
def escribir(nam_module,entradas,salidas):
    texto="";
    listaux=[];
    entradas_bit=[];
    salidas_bit=[];
    entradas_f=[];
    salidas_f=[];
    aux=0;
    nombre=nam_module+"_TB_SCRPT.v";
    archivo=open(nombre,mode="w",encoding="utf-8");
    archivo.write("//Archivo de TestBench para verilog basico generado por Veriscript_TB ALPHA 0.1\n");
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
extraer();