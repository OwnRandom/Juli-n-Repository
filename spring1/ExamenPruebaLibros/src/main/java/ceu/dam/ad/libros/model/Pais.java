package ceu.dam.ad.libros.model;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Data;

@Data
@Entity
@Table(name = "paises")
public class Pais {
	
	@Id
	private String codigo;
	
	@Column(name = "descripcion")
	private String nombre;
	
	
	@Override
	public String toString() {
		return "Pais [codigo=" + codigo + ", nombre=" + nombre + "]";
	}
	
	
	
}
