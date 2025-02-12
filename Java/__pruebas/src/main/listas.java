package main;

import java.util.*;

public class listas {
    public static void main(String[] args) {
        List<String> nombres = new LinkedList<>();
        Scanner scanner = new Scanner(System.in);

        System.out.println("Introduce varios nombres para incluir en la lista (escribe 'salir' para terminar):");

        while (true) {
            System.out.print("Nombre: ");
            String input = scanner.nextLine();

            if (input.equalsIgnoreCase("salir")) { // Condición de salida
                break;
            }

            // Validación: Solo se permiten letras y espacios
            if (input.matches("^[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\\s]+$")) {
                nombres.add(input);
                System.out.println("✅ Nombre agregado con éxito.");
            } else {
                throw new IllegalArgumentException("❌ Error: Solo se permiten nombres con letras y espacios.");
            }
        }

        System.out.println("\n📋 Lista final de nombres:");
        System.out.println(nombres);

        scanner.close();
    }
}
