import { Component, OnInit } from '@angular/core';
import { ProyectoService } from 'src/app/servicios/proyecto/proyecto.service';
import { ActivatedRoute, Router } from '@angular/router';
import {FlashMessagesService} from 'angular2-flash-messages';

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
  constructor(private proyectoService: ProyectoService, private rutaActiva: ActivatedRoute, private router: Router,
    private flashMessagesService: FlashMessagesService) { }

  editarProyecto(){
    this.proyectoService.editarProyecto(this.proyecto, this.rutaActiva.snapshot.params.idProyecto).subscribe(
      res =>{
        this.flashMessagesService.show('proyecto editado exitosamente', { cssClass: 'alert-success', timeout: 6000 });
        this.router.navigate(["empresa/"+ localStorage.getItem("url") +"/proyectos/"])
      }, err => console.log(err)
    );
  }
  ngOnInit() {
    this.proyectoService.getProyecto(this.rutaActiva.snapshot.params.idProyecto).subscribe(
      res=>{
      
       this.proyecto.nombre= res['nombre'];
       this.proyecto.descripcion= res['descripcion'];
       this.proyecto.pago= res['pago'];
      
      }, err => console.log(err)
    )
  }

}
