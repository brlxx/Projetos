package Controle_remoto;

public class ControleRemoto implements Controlador {
    private int volume;
    private boolean ligado;
    private boolean tocando;

    public ControleRemoto(){
        this.setLigado(true);
        this.setVolume(50);
        this.setTocando(true);
    }

    private int getVolume() {
        return this.volume;
    }
    private boolean getTocando(){
        return this.tocando;
    }
    private boolean getLigado(){
        return this.ligado;
    }

    private void setVolume(int v){

        if (this.getLigado()){
            this.volume = v;
        }
    }

    private void setLigado(boolean x){
        this.ligado = x;
    }

    private void setTocando(boolean y){
        if (this.getLigado()) {
            this.tocando = y;
        }else{
            this.tocando = false;
        }
    }


    @Override
    public void ligar() {
        this.setLigado(true);
    }

    @Override
    public void desligar() {
        this.setLigado(false);
    }

    @Override
    public void abrirMenu() {
        System.out.println("-------Menu-------");
        System.out.println("Ligado: "+ this.getLigado());
        System.out.println("Volume: "+ this.getVolume());
        System.out.println("Tocando: "+ this.getTocando());
        for (int i = 0;i<=this.getVolume();i+= 10){
            System.out.print("|");
        }
        System.out.println("");
        System.out.println("-------Fim-------");
    }

    @Override
    public void fecharMenu() {

    }

    @Override
    public void maisVolume(int y) {
        if (this.getLigado()){
            for (int i = 1;i <= y;i+=1){
                if (this.getVolume() >= 0 && this.getVolume() <= 100){
                    this.setVolume(this.getVolume() + 5);
                }
            }

        }
    }

    @Override
    public void menosVolume(int y) {
        if (this.getLigado()){
            if (this.getVolume() > 0){
                for(int i = 1;i<=y;i+= 1){
                    if (this.getVolume() >= 5 && this.getVolume() <= 100 ) {
                        this.setVolume(this.getVolume() - 5);
                    }
                }

            }
        }
    }

    @Override
    public void ligarMudo() {
        if (this.getLigado() || this.getVolume() > 0){
            this.setVolume(0);
        }
    }

    @Override
    public void desligarMudo() {
        if (this.getLigado() && this.getVolume() == 0){
            this.setVolume(50);
        }
    }

    @Override
    public void play() {
        if (this.getLigado() && !(this.getTocando())) {
            this.setTocando(true);
        }
    }

    @Override
    public void pause() {
        if (this.getLigado() && this.getTocando()){
            this.setTocando(false);
        }
    }
}
