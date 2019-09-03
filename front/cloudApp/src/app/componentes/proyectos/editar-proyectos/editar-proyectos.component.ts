import { Component, OnInit } from '@angular/core';
import { ProyectoService } from 'src/app/servicios/proyecto/proyecto.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-editar-proyectos',
  templateUrl: './editar-proyectos.component.html',
  styleUrls: ['./editar-proyectos.component.css']
})
export class EditarProyectosComponent implements OnInit {

  proyecto = {
    nombre: '',
    descripcion: '',
    pago: '',
    empresa: localStorage.getItem("id")
  }
  constructor(private proyectoService: ProyectoService, private rutaActiva: ActivatedRoute, private router: Router) { }

  editarProyecto(){
    this.proyectoService.editarProyecto(this.proyecto, this.rutaActiva.snapshot.params.idProyecto).subscribe(
      res =>{
        this.router.navigate(["empresa/"+ localStorage.getItem("url") +"/proyectos/"])
      }, err => console.log(err)
    );
  }
  ngOnInit() {
  }

}
