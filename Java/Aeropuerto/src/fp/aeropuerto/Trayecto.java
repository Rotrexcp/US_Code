package fp.aeropuerto;

public record Trayecto(
		String origen,
		String destino) {
	//Restricciones
	public Trayecto{
		checkOrigenDestino(origen, destino);
	}
	private void checkOrigenDestino(String origen, String destino) {
		if(origen==destino) {
			throw new IllegalArgumentException("el origen no puede ser igual que el destino");
		}
	}
}
