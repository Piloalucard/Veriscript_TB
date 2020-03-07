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



def escribir():
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

    for i in entradas:
        print(i);
    for i in salidas:
        print(i);
    input();
    

escribir();