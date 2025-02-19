package fp.universidad.tipos;

public record Nota(Asignatura asignatura,Integer cursoAcademico,Integer valorNumerico, 
		Convocatoria convocatoria, Boolean matriculaHonor)  {
	
	//Constructor 2:
	public Nota(Asignatura asignatura, Integer cursoAcademico,Integer valorNumerico, Convocatoria convocatoria ) {
		//TODO: RESTRICCIONES:
		
		
		this(asignatura, cursoAcademico, valorNumerico, convocatoria, false);
				
		
	}
	
	//Propiedad derivada
	//Calificacion
	public String getCalificacion(Integer valorNumerico) {
		String calificacion = null;
		if(valorNumerico<5) {
			calificacion = "Suspenso";}
		else if(valorNumerico<7 && valorNumerico>=5) {
			calificacion = "Aprobado";}
		else if(valorNumerico>=7 && valorNumerico<9) {
			calificacion = "Notable";}
		else if(valorNumerico>=9 && matriculaHonor== false) {
			calificacion = "Sobresaliente";	}
		else {calificacion = "Matricula de honor";	}
		return calificacion;
		
		
	}
	
	//CURSO ACADEMICO REPRESENTADO:
	public String getCurso(Integer cursoAcademico) {
		String curso = cursoAcademico + "-" + Integer.sum(cursoAcademico, 1);
		return curso ;}

	
	@Override
	public String toString() {
		
		return asignatura + ", " +  getCurso(cursoAcademico) + ", " + convocatoria + ", " + getCalificacion(valorNumerico);}
}