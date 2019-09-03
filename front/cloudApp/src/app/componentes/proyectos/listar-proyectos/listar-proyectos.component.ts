import { Component, OnInit } from '@angular/core';
import { ProyectoService } from 'src/app/servicios/proyecto/proyecto.service';
import { PageEvent } from '@angular/material/paginator';
import { UsuarioService } from 'src/app/servicios/usuario/usuario.service';

@Component({
  selector: 'app-listar-proyectos',
  templateUrl: './listar-proyectos.component.html',
  styleUrls: ['./listar-proyectos.component.css']
})
export class ListarProyectosComponent implements OnInit {

  public isLogged= false;
  proyectos: any = [];
  constructor(private proyectosService: ProyectoService, private usuarioService: UsuarioService) { }

  page_size: number = 1;
  page_number: number =1 ;

  chequearLogin(){
    if(this.usuarioService.getToken()){
      this.isLogged=true;
    }else{
      this.isLogged=false;
    }
  }
  ngOnInit() {
    this.chequearLogin();
    this.proyectosService.getProyectos(localStorage.getItem("usuario")).subscribe(
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
