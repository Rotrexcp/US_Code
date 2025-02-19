package main;
import java.time.*; import java.util.List;
import java.util.Objects;

public class Vuelo {
   private Trayecto trayecto; private Double precio; private Integer num_pasajeros; private Integer num_plazas;
   private String codigo; private LocalDate fecha; private Duration duracion; private List<String> tripulacion; private Boolean completo; private Double porcentaje;

   public Vuelo(Trayecto trayecto, Double precio, Integer num_pasajeros, Integer num_plazas, String codigo, 
		   LocalDate fecha, Duration duracion, List<String> tripulacion, Boolean completo, Double porcentaje) {
      CheckNumPlazas(num_plazas);
      CheckNumPasajeros(num_pasajeros);
      CheckPrecio(precio);
      CheckNumPasajerosVSPlazas(num_pasajeros, num_plazas);
      CheckCodigo(codigo);
      CheckTripulacion(tripulacion);
      this.trayecto = trayecto;
      this.precio = precio;
      this.num_pasajeros = num_pasajeros;
      this.num_plazas = num_plazas;
      this.codigo = codigo;
      this.fecha = fecha;
      this.duracion = duracion;
      this.tripulacion = tripulacion;
      this.completo = completo;
      this.porcentaje = porcentaje;
   }

   private void CheckNumPlazas(Integer num_plazas) {
      if (num_plazas < 0) {
         throw new IllegalArgumentException("El numero de plazas no puede ser negativo");
      }
   }

   private void CheckNumPasajeros(Integer num_pasajeros) {
      if (num_pasajeros <= 0) {
         throw new IllegalArgumentException("El numero de pasajeros no puede ser negativo o cero");
      }
   }

   private void CheckPrecio(Double precio) {
      if (precio < 0.0) {
         throw new IllegalArgumentException("El precio no puede ser negativo");
      }
   }

   private void CheckNumPasajerosVSPlazas(Integer num_pasajeros, Integer num_plazas) {
      if (num_pasajeros > num_plazas) {
         throw new IllegalArgumentException("El numero de pasajeros no puede ser mayor al numero de plazas");
      }
   }

   private void CheckCodigo(String codigo) {
      if (codigo.length() != 6) {
         throw new IllegalArgumentException("El codigo tiene que tener 6 caracteres");
      } else if (!codigo.matches("[A-Z]{2}\\d{4}")) {
         throw new IllegalArgumentException("El codigo de cada tripulante debe tener 2 mayusculas significativas seguido de 4 digitos");
      }
   }

   private void CheckTripulacion(List<String> tripulacion) {
      if (tripulacion.size() < 3) {
         throw new IllegalArgumentException("El numero de tripulantes al menos deben ser 3 (un piloto, un copiloto y al menos un asistente)");
      }
      long pilotos = tripulacion.stream().filter(t -> t.startsWith("PP")).count();
      long copilotos = tripulacion.stream().filter(t -> t.startsWith("CP")).count();
      long asistentes = tripulacion.stream().filter(t -> t.startsWith("AV")).count();

      if (pilotos != 1) {
          throw new IllegalArgumentException("Debe haber exactamente un piloto.");
      }
      if (copilotos != 1) {
          throw new IllegalArgumentException("Debe haber exactamente un copiloto.");
      }
      if (asistentes < 1) {
          throw new IllegalArgumentException("Debe haber al menos un asistente.");
      }
   }

   public Trayecto getTrayecto() {
      return this.trayecto;
   }

   public void setTrayecto(Trayecto trayecto) {
      this.trayecto = trayecto;
   }

   public Double getPrecio() {
      return this.precio;
   }

   public void setPrecio(Double precio) {
      this.CheckPrecio(precio);
      this.precio = precio;
   }

   public Integer getNum_pasajeros() {
      return this.num_pasajeros;
   }

   public void setNum_pasajeros(Integer num_pasajeros) {
      this.CheckNumPasajeros(num_pasajeros);
      this.num_pasajeros = num_pasajeros;
   }

   public Integer getNum_plazas() {
      return this.num_plazas;
   }

   public void setNum_plazas(Integer num_plazas) {
      this.CheckNumPlazas(num_plazas);
      this.num_plazas = num_plazas;
   }

   public String getCodigo() {
      return this.codigo;
   }

   public void setCodigo(String codigo) {
      this.CheckCodigo(codigo);
      this.codigo = codigo;
   }

   public LocalDate getFecha() {
      return this.fecha;
   }

   public void setFecha(LocalDate fecha) {
      this.fecha = fecha;
   }

   public Duration getDuracion() {
      return this.duracion;
   }

   public void setDuracion(Duration duracion) {
      this.duracion = duracion;
   }

   public List<String> getTripulacion() {
      return this.tripulacion;
   }

   public void setTripulacion(List<String> tripulacion) {
      this.CheckTripulacion(tripulacion);
      this.tripulacion = tripulacion;
   }

   public Boolean getCompleto() {
      return this.completo;
   }

   public void setCompleto(Boolean completo) {
      this.completo = completo;
   }
   
   public Double getPorcentaje() {
	      return this.porcentaje;
	   }

	   public void setPorcentaje(Double porcentaje) {
	      this.porcentaje = porcentaje;
	   }
   
		@Override
	public int hashCode() {
		return Objects.hash(codigo, fecha);
	}
	
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Vuelo other = (Vuelo) obj;
		return Objects.equals(codigo, other.codigo) && Objects.equals(fecha, other.fecha);
	}
	
	public int compareTo(Vuelo o) {
		int r = this.fecha.compareTo(o.fecha);
		if(r==0) {
			r = this.codigo.compareTo(o.codigo);
		}
		return r;
	}
	
	private void incrementaPrecioPorcentaje(Double porcentaje) {
		Double p = getPrecio();
		setPrecio(p*porcentaje + p);
	}
	
	@Override
	public String toString() {
		return "Vuelo [trayecto=" + trayecto + ", codigo=" + codigo + ", fecha=" + fecha + "]";
	}
}
