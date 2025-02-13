package fp.universidad.tipos;

public record Asignatura (String nombre, String codigo, Double creditos, TipoAsignatura tipo, Integer curso) {
	//HECHO:
		//Constructor canónico
		//Getters
		//toString, equals, hashcode -> el toString hay que sobrescribirlo para dar nuestras condiciones
	
	//NO HECHO:
		//Propiedades derivadas
		//Restricciones
		//compareTo
	
	//TODO: Propiedad derivada: acronimo (significa TO DO [por hacer, no "todo"])
	public String acronimo() {
		return null;
	}
	
	//toString, sobre escribirlo
	@Override
	public String toString() {
		return "(" + codigo + ") " + nombre;
	}
	
	//Restricciones
	public Asignatura{
		CheckDigitos(codigo);
	}

	private void CheckDigitos(String codigo) {
		if(codigo.length()!=7) {
			throw new IllegalArgumentException("No se puede más de 7 dígitos");
		}
	}
}
