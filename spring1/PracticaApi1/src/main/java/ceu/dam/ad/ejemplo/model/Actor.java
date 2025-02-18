package ceu.dam.ad.ejemplo.model;

import java.time.LocalDate;

import io.swagger.v3.oas.annotations.media.Schema;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.validation.constraints.NotBlank;
import lombok.Data;

@Entity
@Data
public class Actor {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	@Schema(description = "Id long autogenerada, no introducir al crear en post")
	private Long actorId;
	
	@NotBlank(message = ("El nombre es obligatorio"))
	private String firstName;
	
	@NotBlank(message = ("El apellido es obligatorio"))
	private String lastName;
	
	private LocalDate lastUpdate;
	

}
