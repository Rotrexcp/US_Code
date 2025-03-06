package fp.universidad.tipos;

import java.util.*;

public class Despacho extends Espacio{
	private Set<Profesor> profesores;
	
	public Despacho(String nombre, Integer capacidad) {
		super(TipoEspacio.OTHER, nombre, capacidad);
		this.profesores = new HashSet<String>();
	}
	
	public Despacho(String nombre, Integer capacidad, Profesor p) {
		super(TipoEspacio.OTHER, nombre, capacidad);
		this.profesores = p; //size = 1 (Hacer Checker)
	}
	
	public Despacho(TipoEspacio tipo, String nombre, Integer capacidad) {
		super(TipoEspacio.OTHER, nombre, capacidad);
	}
}
