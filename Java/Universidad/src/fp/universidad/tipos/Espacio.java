package fp.universidad.tipos;

public class Espacio {
	//Atributos
	private TipoEspacio tipo;
	private String nombre;
	private Integer capacidad;
	
	//Métodos
		//Constructor
	//Canónico
	public Espacio(TipoEspacio tipo, String nombre, Integer capacidad) {
		this.tipo = tipo;
		this.nombre = nombre;
		this.capacidad = capacidad;
		
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
	
		
	
		
	
	
}
