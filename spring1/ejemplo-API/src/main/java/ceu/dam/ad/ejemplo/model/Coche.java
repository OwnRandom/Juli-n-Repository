package ceu.dam.ad.ejemplo.model;

import java.util.List;

import io.swagger.v3.oas.annotations.media.Schema;
import jakarta.persistence.CascadeType;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.OneToMany;
import jakarta.validation.Valid;
import jakarta.validation.constraints.NotBlank;
import lombok.Data;

@Entity
@Data
public class Coche {

	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	@Schema(description = "Id autogenerado del coche. No se debe introducir en post")
	private Long id;
	@NotBlank(message = ("La marca es obligatoria"))
	private String marca;
	@NotBlank(message = ("El modelo es obligatorio"))
	private String modelo;
	
	@OneToMany(cascade = CascadeType.ALL)
	@JoinColumn(name = "id_coche", nullable = false)
	@Valid
	private List<Conductor> conductores;
	
}
