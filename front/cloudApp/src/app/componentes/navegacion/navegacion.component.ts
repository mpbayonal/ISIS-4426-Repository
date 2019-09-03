import { Component, OnInit } from '@angular/core';
import { UsuarioService } from 'src/app/servicios/usuario/usuario.service';
import { Router } from '@angular/router';
import {Location} from '@angular/common';

@Component({
  selector: 'app-navegacion',
  templateUrl: './navegacion.component.html',
  styleUrls: ['./navegacion.component.css']
})
export class NavegacionComponent implements OnInit {
  
  public isLogged= false;
  constructor(private usuarioService: UsuarioService, private router:Router, private location: Location) { }

  logOut(): void{
    this.usuarioService.logoutUser();
    
    location.reload();
  }
  chequearLogin(){
    if(this.usuarioService.getToken()){
      this.isLogged=true;
    }else{
      this.isLogged=false;
    }
  }
  ngOnInit() {
    this.chequearLogin();
  }
  listarProyectos(){
    this.router.navigate(['empresa/'+ localStorage.getItem("url")+ '/proyectos'])
  }

}
