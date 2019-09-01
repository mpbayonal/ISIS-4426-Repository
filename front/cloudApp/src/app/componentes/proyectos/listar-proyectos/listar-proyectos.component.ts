import { Component, OnInit } from '@angular/core';
import { ProyectoService } from 'src/app/servicios/proyecto/proyecto.service';
import { PageEvent } from '@angular/material/paginator';

@Component({
  selector: 'app-listar-proyectos',
  templateUrl: './listar-proyectos.component.html',
  styleUrls: ['./listar-proyectos.component.css']
})
export class ListarProyectosComponent implements OnInit {

  proyectos: any = [];
  constructor(private proyectosService: ProyectoService) { }

  page_size: number = 1;
  page_number: number =1 ;

  ngOnInit() {
    this.proyectosService.getProyectos().subscribe(
      res =>{
        this.proyectos=res
      }, err => console.log(err)
    )
  }
  handlePage(e: PageEvent){
    this.page_size=e.pageSize
    this.page_number= e.pageIndex+1
  }

}
