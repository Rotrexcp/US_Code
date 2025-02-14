package fp.universidad.tipos.test;

import java.time.LocalDate; import fp.universidad.tipos.Persona;

public class TestPersona {

	public static void main(String[] args) {
		Persona p1 = new Persona("12345678A", "Nombre1", "Apellidos1", LocalDate.of(2000, 1, 1), "email1@us.es"); 
		
		Persona p2 = new Persona("87654321A", "Nombre2", "Apellidos2", LocalDate.of(2001, 2, 2)); 
		
		
		System.out.println(p1);
		System.out.println(p2);
		System.out.println(p1.getEmail());
		System.out.println(p2.getEmail());
		p2.setEmail("email2@us.es");
		System.out.println(p2.getEmail());
	}

}
