package fp.aeropuerto;
import fp.utiles.*; import java.time.*; import java.util.List;

public class Vuelo {
	private Trayecto trayecto; private Double precio; private Integer num_pasajeros; private Integer num_plazas; private String codigo;
	private LocalDate fecha; private Duration duracion; private List<String> tripulacion;
	private Integer duracion_minutos; private Boolean completo; private Double porcentaje;
	
	//Constructor
	public Vuelo(Trayecto trayecto,  Double precio,  Integer num_pasajeros,  Integer num_plazas,  String codigo,
			 LocalDate fecha,  Duration duracion,  List<String> tripulacion,  String origen,
			 String destino,  Integer duracion_minutos,  Boolean completo,  Double porcentaje) {
		CheckNumPlazas(num_plazas);
		CheckNumPasajeros(num_pasajeros);
		CheckPrecio(precio);
		CheckNumPasajerosVSPlazas(num_pasajeros, num_plazas);
		CheckTripulacion(tripulacion.size());
		CheckCodigo(codigo);
		this.trayecto = trayecto; this.precio = precio; this.num_pasajeros = num_pasajeros; this.num_plazas = num_plazas; this.codigo = codigo;
		this.fecha = fecha; this.duracion = duracion; this.tripulacion = tripulacion;
		this.duracion_minutos = duracion_minutos; this.completo = completo; this.porcentaje = porcentaje;
	}
	
	//Restricciones
	private void CheckNumPlazas(Integer num_plazas) {
		if (num_plazas<0) {
			throw new IllegalArgumentException(
					"El numero de plazas no puede ser negativo");
		}
	}
	private void CheckNumPasajeros(Integer num_pasajeros) {
		if (num_pasajeros<=0) {
			throw new IllegalArgumentException(
					"El numero de pasajeros no puede ser negativo o cero");
		}
	}
	private void CheckPrecio(Double precio) {
		if (precio<0) {
			throw new IllegalArgumentException(
					"El precio no puede ser negativo");
		}
	}
	private void CheckNumPasajerosVSPlazas(Integer num_pasajeros, Integer num_plazas) {
		if (num_pasajeros>num_plazas) {
			throw new IllegalArgumentException(
					"El numero de pasajeros no puede ser mayor al numero de plazas");
		}
	}
	private void CheckTripulacion(Integer tripulacion) {
		if (tripulacion<3) {
			throw new IllegalArgumentException(
					"El numero de tripulantes al menos deben ser 3 (un piloto, un copiloto y al menos un asistente)");
		}
	}
	private void CheckCodigo(String codigo) {
		if (codigo.length() != 6) {
			throw new IllegalArgumentException(
					"El código tiene que tener 6 caracteres");
		}
		if (!codigo.matches("[A-Z]{2}\\d{4}")) {
			throw new IllegalArgumentException("El código debe tener 2 mayusculas y seguido de 4 dígitos");
		}
	}
	//Falta la restriccion 7

	//Getters and Setters
	public Trayecto getTrayecto() {
		return trayecto;
	}

	public void setTrayecto(Trayecto trayecto) {
		this.trayecto = trayecto;
	}

	public Double getPrecio() {
		return precio;
	}

	public void setPrecio(Double precio) {
		CheckPrecio(precio);
		this.precio = precio;
	}

	public Integer getNum_pasajeros() {
		return num_pasajeros;
	}

	public void setNum_pasajeros(Integer num_pasajeros) {
		CheckNumPasajeros(num_pasajeros);
		this.num_pasajeros = num_pasajeros;
	}

	public Integer getNum_plazas() {
		return num_plazas;
	}

	public void setNum_plazas(Integer num_plazas) {
		CheckNumPlazas(num_plazas);
		this.num_plazas = num_plazas;
	}

	public String getCodigo() {
		return codigo;
	}

	public void setCodigo(String codigo) {
		CheckCodigo(codigo);
		this.codigo = codigo;
	}

	public LocalDate getFecha() {
		return fecha;
	}

	public void setFecha(LocalDate fecha) {
		this.fecha = fecha;
	}

	public Duration getDuracion() {
		return duracion;
	}

	public void setDuracion(Duration duracion) {
		this.duracion = duracion;
	}

	public List<String> getTripulacion() {
		return tripulacion;
	}

	public void setTripulacion(List<String> tripulacion) {
		CheckTripulacion(tripulacion.size());
		this.tripulacion = tripulacion;
	}

	public Integer getDuracion_minutos() {
		return duracion_minutos;
	}

	public void setDuracion_minutos(Integer duracion_minutos) {
		this.duracion_minutos = duracion_minutos;
	}

	public Boolean getCompleto() {
		return completo;
	}

	public void setCompleto(Boolean completo) {
		this.completo = completo;
	}

	public Double getPorcentaje() {
		return porcentaje;
	}

	public void setPorcentaje(Double porcentaje) {
		this.porcentaje = porcentaje;
	}
	
	
}
