//RECORDATORIO: al crear la clase hay que marcar la opcion: main(String[] args)

package fp.universidad.tipos.test;

import fp.universidad.tipos.Asignatura;
import fp.universidad.tipos.TipoAsignatura;

public class TestAsignatura {

	
	
	public static void main(String[] args) {
		try {
			Asignatura fp1 = new Asignatura("Fundamentos de Programación","0000230",12.,TipoAsignatura.ANUAL,1);
		
			System.out.println(fp1);
			System.out.println(fp1.codigo());
			System.out.println(fp1.creditos());
		}
		
		catch(Exception e){
			System.out.println(e);
		}
		
		Asignatura fp1 = new Asignatura("Fundamentos de Programación","0000230",12.,TipoAsignatura.ANUAL,1);
		Asignatura fp2 = new Asignatura("Fundamentos de Programación","0000230",12.,TipoAsignatura.ANUAL,1);
		
		System.out.println(fp1.equals(fp2));
	}
}