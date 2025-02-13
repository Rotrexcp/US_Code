//RECORDATORIO: al crear la clase hay que marcar la opcion: main(String[] args)

package fp.universidad.tipos.test;

import fp.universidad.tipos.Asignatura;
import fp.universidad.tipos.TipoAsignatura;

public class TestAsignatura {

	public static void main(String[] args) {
		Asignatura fp = new Asignatura("Fundamentos de Programación","0000230",12.,TipoAsignatura.ANUAL,1);
		
		System.out.println(fp);
		System.out.println(fp.codigo());
		System.out.println(fp.creditos());
	}

}
