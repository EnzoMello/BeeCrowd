 package Surprise_Exercise.entities;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

// ATIVIDADE FEITA POR ENZO MELO ARÁUJO E JOÃO VICTOR DE SOUSA DOS SANTOS
public class SystemCall {
    public static void main(String[] args) throws IOException {
        System.out.println("Coloque o nome do diretório");
        Scanner sc = new Scanner(System.in);

        String directory = sc.nextLine();
        File directoryFile = new File(directory);
        directoryFile.mkdir();

        String pathFile = directory + "\\arquivo.txt";

        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(pathFile));
        bufferedWriter.write("Só alegria hahaha");
        bufferedWriter.close();

        sc.close();
    }
}