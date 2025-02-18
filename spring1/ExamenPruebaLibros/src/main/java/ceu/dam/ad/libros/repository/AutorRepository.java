package ceu.dam.ad.libros.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import ceu.dam.ad.libros.model.Autor;

@Repository
public interface AutorRepository extends JpaRepository<Autor, Long>{

}
