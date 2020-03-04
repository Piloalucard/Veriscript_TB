#Veriscript_TB 1.0 04/03/2020
#Gustavo Padilla Valdez INCO

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
    texto="module "+nombre+"();\n"
    archivo.write(texto);
    archivo.close();

escribir();