package ceu.dam.ad.libros.model;

import java.util.List;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.OneToMany;
import jakarta.persistence.OneToOne;
import jakarta.persistence.Table;
import lombok.Data;

@Data
@Entity
@Table(name = "autores")
public class Autor {

	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	@Column(name = "idAutor")
	private Long id;
	private String nombre;
	private Integer añoNacimiento;
	
	@OneToMany
	@JoinColumn(name = "id_autor")
	private List<Libro> obra;
	
	
	@OneToOne
	@JoinColumn(name = "codigo_pais")
	private Pais origen;
	
	
	
	
	
	
	
	@Override
	public String toString() {
		return "Autor [id=" + id + ", nombre=" + nombre + ", añoNacimiento=" + añoNacimiento + ", obra=" + obra
				+ ", origen=" + origen + "]";
	}

	
	
	
	
	
	
	
}
