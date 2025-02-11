package fp.test;

import fp.animales.*;

public class test_animales {

	public static void main(String[] args) {
		
		System.out.println("Hola");
		
		Perro p1 = new Perro
				("Husky", Color.BLANCO, 1);
		
		System.out.println(p1);
		
		p1.setRaza("Labrador");
		System.out.println(p1);
		System.out.print(p1.getEdad());
		

	}

}
