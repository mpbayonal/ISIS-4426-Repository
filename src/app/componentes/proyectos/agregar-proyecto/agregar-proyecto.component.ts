import { Component, OnInit } from '@angular/core';
import { ProyectoService } from 'src/app/servicios/proyecto/proyecto.service';
import { Router } from '@angular/router';
import { FlashMessagesService } from 'angular2-flash-messages';


@Component({
  selector: 'app-agregar-proyecto',
  templateUrl: './agregar-proyecto.component.html',
  styleUrls: ['./agregar-proyecto.component.css']
})
export class AgregarProyectoComponent implements OnInit {

  constructor(
    private proyectoService: ProyectoService,
    private router: Router,
    private flashMessagesService: FlashMessagesService
  ) { }

  proyecto = {
    nombre: '',
    descripcion: '',
    pago: '',
    empresa: localStorage.getItem('id')
  };

  agregarProyecto() {
    this.proyectoService.agregarProyecto(this.proyecto, localStorage.getItem('email')).subscribe(
      res => {
        this.flashMessagesService.show('proyecto agregado exitosamente', { cssClass: 'alert-success', timeout: 6000 });
        this.router.navigate(['empresa/' + localStorage.getItem('url') + '/proyectos']);
      },
      err => console.log(err)
    );


  }
  ngOnInit() {

  }

}
