package fp.universidad.tipos.test;

import fp.universidad.tipos.Espacio;
import fp.universidad.tipos.TipoEspacio;
public class TestEspacio {

	public static void main(String[] args) {
		Espacio e1 = new Espacio(TipoEspacio.AULA_EXAMEN, "A3.10", 156);
		
		System.out.println(e1);
		System.out.println(e1.getPlanta());

	}

}
