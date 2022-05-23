import java.util.Scanner;

class IntegralFracaoParcial {
    private String integral;
    private String denominador;
    private String numerador;
    private int limiteSuperior;
    private int limiteInferior;

    /**
     * Construtor para a integral caso não tenha um limite superior e inferior
     */
    public IntegralFracaoParcial(String integral) {
        this.integral = integral;
        removeDenominadorAndNumerador(integral);    // Declarar os numeradores e denimadores da Integral
    }

    /**
     *  Construtor para a integral caso tenha um limite superior e inferior
     */
    public IntegralFracaoParcial(String integral, int limiteInferior, int limiteSuperior) {
        this.integral = integral;
        this.limiteInferior = limiteInferior;
        this.limiteSuperior = limiteSuperior;
        removeDenominadorAndNumerador(integral);
    }

    public void setIntegral(String integral) {
        this.integral = integral;
    }

    public void setDenominador(String denominador) {
        this.denominador = denominador;
    }

    public void setNumerador(String numerador) {
        this.numerador = numerador;
    }

    public void setLimiteInferior(int limiteInferior) {
        this.limiteInferior = limiteInferior;
    }

    public void setLimiteSuperior(int limiteSuperior) {
        this.limiteSuperior = limiteSuperior;
    }

    public String getIntegral() {
        return this.integral;
    }

    public String getDenominador() {
        return this.denominador;
    }

    public String getNumerador() {
        return this.numerador;
    }

    public int getLimiteInferior() {
        return this.limiteInferior;
    }

    public int getLimiteSuperior() {
        return this.limiteSuperior;
    }

    /**
     * Função utilizada para setar o denominador e o numerador da Integral
     * @param integral -> Integral a ser descoberta o denominador e numerador
     */
    public void removeDenominadorAndNumerador(String integral) {
        String[] arrayFracao = new String[2];
        arrayFracao = integral.split("/");
        setNumerador(arrayFracao[0]);
        setDenominador(arrayFracao[1]);
    }

    /**
     * Se caso a fração a ser integrada precisar a funcao faz a fatoração do denominador
     * @param denominador -> Denominador da integral
     * @return -> String com a fatoração feita
     */
    public String fatorarDenominador(String denominador) {
        String denominadorFatorado = "";
        // https://www.infoescola.com/matematica/equacao-e-fatoracao/#:~:text=Para%20fatorar%20uma%20equa%C3%A7%C3%A3o%20ser%C3%A1,fator%20comum%20%C3%A9%20x2.
        return denominadorFatorado;
    }
}

public class Main {
    // Global
    static Scanner input = new Scanner(System.in);

    public static void main(String[] args) {
        // Declaração das variaveis
        IntegralFracaoParcial calculator;
        String integral;

        // Pegar a integral do usuário e criar o Objeto
        System.out.println("Digite alguma integral: ");
        integral = input.nextLine();
        calculator = new IntegralFracaoParcial(integral);
    }
}