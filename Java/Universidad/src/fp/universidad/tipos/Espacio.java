package fp.universidad.tipos;

import fp.utiles.Checkers;

public class Espacio {
	//Atributos
	private TipoEspacio tipo;
	private String nombre;
	private Integer capacidad;
	
	//Métodos
		//Constructor
	//Canónico
	public Espacio(TipoEspacio tipo, String nombre, Integer capacidad) {
		setTipo(tipo);
		setNombre(nombre);
		setCapacidad(capacidad);
		
		//TODO: Restricciones
		
	}

		//Getters & Setters
	public TipoEspacio getTipo() {
		return tipo;
	}
	public void setTipo(TipoEspacio tipo) {
		this.tipo = tipo;
	}
	

	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	

	public Integer getCapacidad() {
		return capacidad;
	}
	public void setCapacidad(Integer capacidad) {
		Checkers.check("Capacidad debe ser mayor que 0", capacidad>0);
		this.capacidad = capacidad;
	}
	
	
		//propiedad derivada: planta
	public Integer getPlanta() {
		char character = nombre.charAt(1);
		String p = String.valueOf(character);
		Integer planta = Integer.valueOf(p);
		return planta;
	}

	
		//toString
		//"A3.10 (planta 3)"
	@Override
	public String toString() {
		return nombre + " (planta " + getPlanta() + ") ";
	}
	
	
	public int hashCode() {
		return getNombre().hashCode() + 31*getPlanta().hashCode();
	}
	
	
	public boolean equals(Object o) {
		if(this == o) return true;
		if(o instanceof Espacio) {
			Espacio espacio = (Espacio) o;
			return getNombre().equals(espacio.getNombre()) && getPlanta().equals(espacio.getPlanta());
		}
		return false;
	}
	
	
	public int compareTo(Espacio o) {
		int res = getPlanta().compareTo(o.getPlanta());
		if(res == 0) {
			res = getNombre().compareTo(o.getNombre());
		}
		return res;
	}
}