// Source code is decompiled from a .class file using FernFlower decompiler.
package main;

import java.time.Duration;
import java.time.LocalDate;
import java.util.List;

public class Vuelo {
   private Trayecto trayecto;
   private Double precio;
   private Integer num_pasajeros;
   private Integer num_plazas;
   private String codigo;
   private LocalDate fecha;
   private Duration duracion;
   private List<String> tripulacion;
   private Integer duracion_minutos;
   private Boolean completo;
   private Double porcentaje;

   public Vuelo(Trayecto trayecto, Double precio, Integer num_pasajeros, Integer num_plazas, String codigo, LocalDate fecha, Duration duracion, List<String> tripulacion, String origen, String destino, Integer duracion_minutos, Boolean completo, Double porcentaje) {
      this.CheckNumPlazas(num_plazas);
      this.CheckNumPasajeros(num_pasajeros);
      this.CheckPrecio(precio);
      this.CheckNumPasajerosVSPlazas(num_pasajeros, num_plazas);
      this.CheckTripulacion(tripulacion.size());
      this.CheckCodigo(codigo);
      this.trayecto = trayecto;
      this.precio = precio;
      this.num_pasajeros = num_pasajeros;
      this.num_plazas = num_plazas;
      this.codigo = codigo;
      this.fecha = fecha;
      this.duracion = duracion;
      this.tripulacion = tripulacion;
      this.duracion_minutos = duracion_minutos;
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

   private void CheckTripulacion(Integer tripulacion) {
      if (tripulacion < 3) {
         throw new IllegalArgumentException("El numero de tripulantes al menos deben ser 3 (un piloto, un copiloto y al menos un asistente)");
      }
   }

   private void CheckCodigo(String codigo) {
      if (codigo.length() != 6) {
         throw new IllegalArgumentException("El c\u00f3digo tiene que tener 6 caracteres");
      } else if (!codigo.matches("[A-Z]{2}\\d{4}")) {
         throw new IllegalArgumentException("El c\u00f3digo debe tener 2 mayusculas y seguido de 4 d\u00edgitos");
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
      this.CheckTripulacion(tripulacion.size());
      this.tripulacion = tripulacion;
   }

   public Integer getDuracion_minutos() {
      return this.duracion_minutos;
   }

   public void setDuracion_minutos(Integer duracion_minutos) {
      this.duracion_minutos = duracion_minutos;
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
}
