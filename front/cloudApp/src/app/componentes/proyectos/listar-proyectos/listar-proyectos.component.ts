import { Component, OnInit } from '@angular/core';
import { ProyectoService } from 'src/app/servicios/proyecto/proyecto.service';
import { PageEvent } from '@angular/material/paginator';
import { UsuarioService } from 'src/app/servicios/usuario/usuario.service';
import { ActivatedRoute, Params, Router } from '@angular/router';


@Component({
  selector: 'app-listar-proyectos',
  templateUrl: './listar-proyectos.component.html',
  styleUrls: ['./listar-proyectos.component.css']
})
export class ListarProyectosComponent implements OnInit {

  public isLogged = false;
  proyectos: any = [];
  constructor(private proyectosService: ProyectoService, private usuarioService: UsuarioService, private rutaActiva: ActivatedRoute
    , private router : Router) { }

  page_size: number = 10;
  page_number: number = 1;

  chequearLogin() {
    if (this.usuarioService.getToken()) {
      this.isLogged = true;
    } else {
      this.isLogged = false;
    }
  }
  ngOnInit() {
    this.chequearLogin();
    if (localStorage.getItem("url") != null) {
      this.proyectosService.getProyectos(localStorage.getItem("url")).subscribe(
        res => {
          this.proyectos = res
        }, err => console.log(err)
      )
    }else{
      this.proyectosService.getProyectos(this.rutaActiva.snapshot.params.url).subscribe(
        res => {
          this.proyectos = res
        }, err => console.log(err)
      )
      
    }
  }
  handlePage(e: PageEvent) {
    this.page_size = e.pageSize
    this.page_number = e.pageIndex + 1
  }
  formularioAgregar(){
    this.router.navigate(["empresa/"+ localStorage.getItem("url") +"/proyectos/agregar"]);
  }
  eliminarProyecto(id){
    this.proyectosService.eliminarProyecto(id).subscribe(
      res=>{
        this.router.navigate(["empresa/"+ localStorage.getItem("url") +"/proyectos/"])
        location.reload()
      },
      err=> console.log(err)
    )
  }
  formularioEditar(id){
    this.router.navigate(["empresa/proyectos/"+ id+ "/editar"])
  }
  mostrarDisenos(id){
    this.router.navigate(["empresa/proyectos/"+ id + "/disenos"])
  }

}
