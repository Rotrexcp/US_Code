package fp.universidad.tipos.test;

import fp.universidad.tipos.Espacio;
import fp.universidad.tipos.TipoEspacio;
public class TestEspacio {

	public static void main(String[] args) {
		try {
			Espacio e1 = new Espacio(TipoEspacio.AULA_EXAMEN, "A3.10", 156);
			Espacio e2 = new Espacio(TipoEspacio.AULA_EXAMEN, "A4.10", 156);
		
			//System.out.println(e2.getPlanta());
			//e1.setCapacidad(-1);
			//System.out.println(e2.hashCode());
			//System.out.println(e1.equals(e2));
			System.out.println(e1.compareTo(e2));
		}
		catch(Exception e) {
			System.out.println(e);
		}
	}

}
