package main;

public record Trayecto(String origen, String destino) {
	//Restricciones
	public Trayecto{
		CheckOrigenDestino(origen, destino); //No se pasan argumentos porque son todos los parametros del record, solo se especifica si necesita algunos en concreto
	}
	
	private void CheckOrigenDestino(String origen, String destino) {
		if(origen.equals(destino)) {
			throw new IllegalArgumentException("El origen tiene que ser distinto al destino");
		}
	}
}
