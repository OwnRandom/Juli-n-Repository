package ceu.dam.ad.libros.model;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Data;

@Data
@Entity
@Table(name = "libros")
public class Libro {

	@Id
	private String isbn;
	
	
	private String titulo;
	
	@Column(name = "edicion")
	private Integer añoEdicion;
	
	
	@Override
	public String toString() {
		return "Libro [isbn=" + isbn + ", titulo=" + titulo + ", añoEdicion=" + añoEdicion + "]";
	}
	
	
	
	
}
