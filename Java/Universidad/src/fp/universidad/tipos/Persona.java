package fp.universidad.tipos;
import java.time.LocalDate;
import java.time.Period;
import java.time.format.DateTimeFormatter;

public class Persona {
	//Atributos -> Siempre privados
	private String dni;
	private String nombre;
	private String apellidos;
	private LocalDate fechaNacimiento;
	private String email;
	
	//Metodos
		//Constructor -> Siempre público llamado igual que la clase
	//Constructor canónico
	public Persona(String dni, String nombre, String apellidos, LocalDate fechaNacimiento, String email) {
		//Asignaciones
		this.dni = dni;
		this.nombre = nombre;
		this.apellidos = apellidos;
		this.fechaNacimiento = fechaNacimiento;
		this.email = email;
		
		//TODO: Restricciones
		
	}
	//Constructor 2
	public Persona(String dni, String nombre, String apellidos, LocalDate fechaNacimiento) {
		//Asignaciones
		this(dni, nombre, apellidos, fechaNacimiento, ""); //Llamando al constructor canónico y ahorro código
		
		//TODO: Restricciones
	}
	
		//Getters & Setters
	public String getDni() {
		return dni;
	}
	public void setDni(String dni) {
		this.dni = dni;
	}
	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	public String getApellidos() {
		return apellidos;
	}
	public void setApellidos(String apellidos) {
		this.apellidos = apellidos;
	}
	public LocalDate getFechaNacimiento() {
		return fechaNacimiento;
	}
	public void setFechaNacimiento(LocalDate fechaNacimiento) {
		this.fechaNacimiento = fechaNacimiento;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	
		//propiedad derivada: edad
	public Integer getEdad() {
		return Period.between(fechaNacimiento, LocalDate.now()).getYears();
	}
	
		//toString, equals, hashcode
		//"28864657W – García Vaquero, Pascual – 15/09/1998"
	public String toString() {
		return dni + " - " + apellidos + ", " + nombre + " - " + fechaNacimiento.format(DateTimeFormatter.ofPattern("dd/MM/yyyy"));
	}
	
		//compareTo
}
