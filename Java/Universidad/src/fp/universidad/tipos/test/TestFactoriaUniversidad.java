package fp.universidad.tipos.test;

import java.util.List;

import fp.universidad.tipos.Espacio;
import fp.universidad.tipos.FactoriaUniversidad;

public class TestFactoriaUniversidad {

	public static void main(String[] args) {
		List<Espacio> e1 = FactoriaUniversidad.leeEspacios("src/data/espacios.csv");
		
		System.out.println(e1);

	}

}
