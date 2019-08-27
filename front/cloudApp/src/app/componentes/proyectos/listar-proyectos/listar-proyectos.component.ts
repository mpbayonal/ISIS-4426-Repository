import { Component, OnInit } from '@angular/core';
import { ProyectoService } from 'src/app/servicios/proyecto/proyecto.service';

@Component({
  selector: 'app-listar-proyectos',
  templateUrl: './listar-proyectos.component.html',
  styleUrls: ['./listar-proyectos.component.css']
})
export class ListarProyectosComponent implements OnInit {

  proyectos: any = [];
  constructor(private proyectosService: ProyectoService) { }

  ngOnInit() {
    this.proyectosService.getProyectos().subscribe(
      res =>{
        this.proyectos=res
      }, err => console.log(err)
    )
  }

}
