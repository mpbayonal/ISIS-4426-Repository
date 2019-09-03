import { Component, OnInit } from '@angular/core';
import { UsuarioService } from 'src/app/servicios/usuario/usuario.service';
import { Router } from '@angular/router';
import {Location} from '@angular/common'

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {


  constructor(private usuarioService: UsuarioService, private router:Router, private location: Location) { }

  usuario  = {
    username: "",
    email: "",
    password: ""
  }
  

  setUsuario(){
    localStorage.setItem("usuario", this.usuario.username);
  }
  getUsuario(){
    return localStorage.getItem("usuario")
  }
  login(){
    this.usuarioService.loginUsuario(this.usuario).subscribe(
      data=>{
        
        let token = data
        this.usuarioService.setToken(token)
        this.setUsuario();
        this.router.navigate( ['empresa/'+ this.usuario.username +'/proyectos']);
        location.reload();
      }, err => console.log(err)
    )
  }

  
  
  ngOnInit() {

  }

}
