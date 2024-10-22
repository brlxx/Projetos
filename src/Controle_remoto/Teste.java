package Controle_remoto;

public class Teste {
    public static void main(String[] args){
        ControleRemoto c = new ControleRemoto();
        c.ligar();
        c.abrirMenu();
        c.maisVolume(5);
        c.abrirMenu();
        c.menosVolume(5);
        c.abrirMenu();
        c.menosVolume(10);
        c.abrirMenu();
        c.maisVolume(10);
        c.abrirMenu();


    }

}
